"""Tests für plan/plan_500k.py - App-Weg zu 500.000 EUR bis 31.08.2027."""

from __future__ import annotations

import random
import sys
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plan"))

import plan_500k as p  # noqa: E402


class TestPlan500k(unittest.TestCase):
    def test_kalender(self):
        """Wochen bis 31.08.2027, Abiturphasen mit wenig Stunden."""
        self.assertEqual(p.WEEKS, 39)
        lv = {k: (k, k, k) for k in ("h_school", "h_holiday", "h_abiprep", "h_abi", "h_oral", "h_gap", "h_full")}
        self.assertEqual(p.hours_level(date(2027, 4, 26), lv)[0], "h_abi")       # schriftliches Abitur
        self.assertEqual(p.hours_level(date(2026, 12, 28), lv)[0], "h_holiday")   # Weihnachtsferien
        self.assertEqual(p.hours_level(date(2027, 7, 5), lv)[0], "h_full")        # Sommer
        # Weihnachtsferien erst ab Do 24.12.: die Woche ab 21.12. ist eine Schulwoche
        self.assertEqual(p.hours_level(date(2026, 12, 21), lv)[0], "h_school")
        self.assertEqual(p.hours_level(date(2027, 1, 4), lv)[0], "h_holiday")
        self.assertEqual(p.hours_level(date(2027, 1, 11), lv)[0], "h_school")
        # Frühjahrsferien 08.-12.02.2027
        self.assertEqual(p.hours_level(date(2027, 2, 8), lv)[0], "h_holiday")
        self.assertEqual(p.hours_level(date(2027, 2, 15), lv)[0], "h_school")
        # Stichtage zählen nur volle Wochen: 31.01. (So) schließt Woche 8 ab, 31.03. (Mi) Woche 16
        self.assertEqual(p.bis_woche(date(2027, 1, 31)), 8)
        self.assertEqual(p.bis_woche(date(2027, 3, 31)), 16)

    def test_nebenaufgaben_kosten_app_stunden(self):
        """Partnersuche, Gründung und Sicherheitsnetz gehen von den App-Stunden ab (Wochenplan)."""
        self.assertEqual(p.nebenstunden(date(2026, 11, 30), False), 7.5)   # Partnersuche + Gründung
        self.assertEqual(p.nebenstunden(date(2026, 12, 28), False), 8.5)   # + Bewerbungen
        self.assertEqual(p.nebenstunden(date(2026, 12, 28), True), 6.0)    # Partner gefunden
        self.assertEqual(p.nebenstunden(date(2027, 1, 25), False), 2.5)
        self.assertEqual(p.nebenstunden(date(2027, 2, 1), False), 0.0)
        gesamt = sum(p.nebenstunden(p.START + p.timedelta(weeks=w), False) for w in range(p.WEEKS))
        self.assertAlmostEqual(gesamt, 9 * 2.5 + 2 * 5 + 12)

    def test_allein_ohne_partnersuche(self):
        """Wer bewusst allein arbeitet, verliert keine Stunden an die Partnersuche."""
        self.assertEqual(p.nebenstunden(date(2026, 11, 30), False, partnersuche=False), 5.0)
        self.assertEqual(p.nebenstunden(date(2027, 1, 25), False, partnersuche=False), 0.0)
        for name in ("Claude-Stufe", "Claude gestaffelt"):
            for k, P in p.SZENARIEN.items():
                if k.startswith(name):
                    self.assertFalse(P["partnersuche"], k)
                    self.assertEqual(P["stopps"], p.TORE, k)            # Tore und Abiturschutz bleiben
                    self.assertLessEqual(P["h_school"][2] * 1.2, 16, k)

    def test_agent_erst_bei_einem_treffer(self):
        """Gestaffelt: Agent und teures Abo kommen nur, wenn eine große App als Treffer erkannt ist."""
        P = p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("Claude gestaffelt:"))]
        rng = random.Random(17)
        for _ in range(300):
            r = p.simulate(rng, P)
            if r["agent_aktiv"]:
                self.assertTrue(any(x * p.FX >= 50000 for x in r["peaks"]))
            if not any(x * p.FX >= 50000 for x in r["peaks"]):
                self.assertFalse(r["agent_aktiv"])
        O = dict(p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("Obergrenze"))],
                 agent_bei_treffer=P["agent_bei_treffer"])
        rng = random.Random(18)
        self.assertGreater(sum(p.simulate(rng, O)["agent_aktiv"] for _ in range(60)), 40)

    def test_einrichtung_wird_nachgeholt(self):
        """Einrichtungsstunden, die in einer Woche keinen Platz finden, werden später nachgeholt."""
        P = p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("Claude-Stufe 3"))]
        rng = random.Random(19)
        offen = [p.simulate(rng, P)["einmal_offen"] for _ in range(300)]
        self.assertGreater(sum(x < 1e-6 for x in offen), 290)

    def test_plan_haelt_die_eigenen_stundenregeln(self):
        """Das Hauptszenario rechnet mit den Stunden des Wochenplans (Abiturschutz)."""
        P = p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("DER PLAN"))]
        self.assertLessEqual(P["h_school"][2] * 1.2, 16)       # Schulwochen höchstens ~15 h
        for k in ("h_abiprep", "h_abi", "h_oral"):             # Abiturzeit höchstens ~5 h
            self.assertLessEqual(P[k][2] * 1.2, 6)
        self.assertEqual(P["stopps"], p.TORE)
        self.assertTrue(P["nebenaufgaben"])
        self.assertEqual(P["credit0"], (0, 0, 0))               # kein Kredit
        self.assertEqual(P["p_fin"], (0.0, 0.0, 0.0))           # keine Finanzierung

    def test_kassenprobe(self):
        """Gewinn = Kasse - Einlagen + offene Forderungen - offene Kosten, in jedem Lauf.

        Fängt nicht bezahlte Kosten (Zahlungsziel 0) und doppelt gekürzte Apple-Zahlungen ab.
        """
        plan = p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("DER PLAN"))]
        faelle = [plan, dict(plan, cost_lag_weeks=(0, 0, 0)),
                  p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("Obergrenze"))],
                  p.SZENARIEN[next(k for k in p.SZENARIEN if "10 % vom Umsatz" in k)]]
        for i, P in enumerate(faelle):
            rng = random.Random(100 + i)
            for _ in range(150):
                r = p.simulate(rng, P)
                probe = r["cash"] - P["start_cash"] - r["nachschuss"] - r["angel_geld"] + r["forderungen"] - r["offene_kosten"]
                self.assertAlmostEqual(r["profit_firma"], probe, delta=1e-6 * max(1.0, abs(probe)))

    def test_verkauf_nur_wenn_er_das_ziel_erreicht(self):
        P = p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("Obergrenze"))]
        rng = random.Random(3)
        verkauft = 0
        for _ in range(300):
            r = p.simulate(rng, P)
            if r["exit"] > 0:
                verkauft += 1
                self.assertGreaterEqual(r["profit"] + r["exit"], P["profit_target"])
        self.assertGreater(verkauft, 0)

    def test_kein_dispo(self):
        """Ohne Kredit: Werbung und Tests drücken die Kasse nie unter null (früher ein versteckter Dispo)."""
        for name in ("DER PLAN", "Obergrenze"):
            P = p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith(name))]
            rng = random.Random(21)
            for _ in range(200 if name == "Obergrenze" else 400):
                r = p.simulate(rng, P)
                self.assertGreaterEqual(r["min_kasse"], 0.0, name)
                self.assertEqual(r["nachschuss"], 0.0, name)

    def test_freiwillige_ausgaben_halten_das_budget(self):
        """Wachstum, Erhalt und gekürzte Werbung bleiben im Budget, auch mit Umsatzbeteiligung."""
        for name in ("Der Plan + Partner (Zusage bis 31.01.), Partner erhält 10", "Obergrenze"):
            P = p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith(name))]
            if name == "Obergrenze":
                P = dict(P, partner_rev_share=0.10, partner=p.PARTNER, partner_week=(0, 1),
                         partner_vertrag=p.VERTRAG_UMSATZ)
            rng = random.Random(31)
            for _ in range(150):
                self.assertLessEqual(p.simulate(rng, P)["max_ueber"], 1e-6, name)

    def test_g5_beendet_neue_versuche(self):
        """Unter 50.000 USD am 30.04. beginnt kein neuer Bau mehr (G5)."""
        P = dict(p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("DER PLAN"))], stopps=())
        g5 = p.bis_woche(date(2027, 4, 30))
        rng = random.Random(13)
        for _ in range(200):
            r = p.simulate(rng, P)
            if p._bis(r["chk"], g5) < 50_000 * p.FX:
                # spätestens ein laufender Bau wird noch fertig: höchstens eine App startet nach G5 + Review
                spaet = [w for w in r["launches"] if w > g5 + 5]
                self.assertLessEqual(len(spaet), 1)

    def test_tore_beenden_die_jagd(self):
        """Nach dem Tor: kein neuer Bau, kein Testbudget; ein abgebrochener Bau zählt nicht als Versuch."""
        for name in ("DER PLAN", "Der Plan + Partner (Zusage bis 31.01.), Partner erhält 25"):
            P = p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith(name))]
            rng = random.Random(11)
            g3 = p.bis_woche(date(2027, 2, 28))
            gestoppt = 0
            for _ in range(400):
                r = p.simulate(rng, P)
                if p._bis(r["chk"], g3) < 5_000 * p.FX:
                    self.assertTrue(r["gestoppt"])
                if r["gestoppt"]:
                    gestoppt += 1
                    self.assertEqual(r["bau_nach_stopp"], 0)
                    for woche, kosten in r["test_log"]:
                        if woche >= r["stopp_woche"]:
                            self.assertEqual(kosten, 0.0)
                self.assertEqual(r["attempts"], r["gestartet"] + r["offene_versuche"])
            self.assertGreater(gestoppt, 300)

    def test_testbudget_bis_g3(self):
        """Creator-Tests bis 28.02. zusammen höchstens 1.500 EUR (auch mit Partner)."""
        for name in ("DER PLAN", "Der Plan + Partner (Zusage bis 31.01.), Partner erhält 10"):
            P = p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith(name))]
            rng = random.Random(12)
            for _ in range(400):
                self.assertLessEqual(p.simulate(rng, P)["testkosten_g3"], P["test_cap"] + 1e-9)

    def test_gruender_traegt_den_verlust(self):
        """Der Partner bringt kein Geld ein: Bei Verlust verliert der Gründer mindestens den Firmenverlust."""
        P = p.SZENARIEN[next(k for k in p.SZENARIEN if "25 % der Anteile" in k)]
        rng = random.Random(4)
        verluste = 0
        for _ in range(300):
            r = p.simulate(rng, P)
            self.assertLessEqual(r["partner_woche"], p.bis_woche(date(2027, 1, 31)) + 1)
            if r["profit_firma"] < 0 and r["exit"] == 0:
                verluste += 1
                self.assertLessEqual(r["ergebnis"], r["profit_firma"] + 1e-9)
        self.assertGreater(verluste, 100)

    def test_spitzen_mrr_stufen(self):
        """Die latente Spitzen-MRR trifft die vorgegebenen Stufenwahrscheinlichkeiten."""
        rng = random.Random(1)
        n = 200_000
        werte = [p.draw_peak(rng, 0.25, 0.07, 0.2, 0.12, 1.5) for _ in range(n)]
        self.assertAlmostEqual(sum(x >= 1_000 for x in werte) / n, 0.25, delta=0.005)
        self.assertAlmostEqual(sum(x >= 10_000 for x in werte) / n, 0.07, delta=0.003)
        self.assertAlmostEqual(sum(x >= 100_000 for x in werte) / n, 0.014, delta=0.002)
        self.assertLessEqual(max(werte), 5e6)
        # Fehlschläge sind rechtsschief: Median ~1.000 x 0,5^4 = 62,5 USD (RevenueCat: Median < 50 USD)
        flops = sorted(p.draw_peak(rng, 0.0, 0.0, 0.2, 0.12, 1.5, 4.0) for _ in range(20_000))
        self.assertAlmostEqual(flops[len(flops) // 2], 62.5, delta=5)

    def test_ergebnis_im_rahmen(self):
        r = p.auswerten(p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("DER PLAN"))], 3_000)
        self.assertLess(r["gewinn_median"], 0)          # der Normalfall: Verlust
        self.assertGreater(r["gewinn_median"], -5_000)  # aber nicht mehr als das Startkapital
        self.assertEqual(r["p_nachschuss"], 0.0)

    def test_cal_ai_treffer_hebt_die_chance(self):
        """Ein Cal-AI-Treffer als erste App ist die Obergrenze: Ziel deutlich wahrscheinlicher."""
        ober = p.auswerten(p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("Obergrenze"))], 400)
        plan = p.auswerten(p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("DER PLAN"))], 400)
        self.assertGreater(ober["p_ziel"], 0.1)
        self.assertGreater(ober["p_ziel"], plan["p_ziel"])

    def test_anteil_abgeben_senkt_die_chance(self):
        P = dict(p.SZENARIEN["Obergrenze: erste App ist ein Cal-AI-Treffer (Start 30k, Spitze 1,5 Mio. USD MRR)"])
        voll = p.auswerten(P, 400, seed=5)["p_ziel"]
        halb = p.auswerten(dict(P, founder_share=0.5), 400, seed=5)["p_ziel"]
        self.assertLess(halb, voll)

    def test_ohne_cash_limit_nicht_schlechter(self):
        P = dict(p.SZENARIEN["Obergrenze: erste App ist ein Cal-AI-Treffer (Start 30k, Spitze 1,5 Mio. USD MRR)"])
        mit = p.auswerten(P, 400, seed=7)["p_ziel"]
        ohne = p.auswerten(dict(P, no_cash_limit=True), 400, seed=7)["p_ziel"]
        self.assertGreaterEqual(ohne, mit)

    def test_meilensteine_fester_lauf(self):
        """Cal-AI-Treffer mit 30k USD Start und Faktor 3 je Monat: 10k USD in der Launch-Woche,
        100k USD frühestens 5 Wochen später (30k x 3^(5/4,33) >= 100k)."""
        # ohne Einbruch (p_kill = 0), sonst kann ein früher Einbruch die 100k verhindern
        P = dict(p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("Obergrenze"))], p_kill=(0, 0, 0))
        for frei in (True, False):
            rng = random.Random(8)
            erreicht = 0
            gestartet = 0
            for _ in range(50):
                r = p.simulate(rng, dict(P, no_cash_limit=frei))
                if r["launch1"] == 99:       # App 1 bis zum Tor G3 nicht fertig: Bau verworfen
                    self.assertTrue(r["gestoppt"])
                    continue
                gestartet += 1
                # Launch-Woche des Treffers (bei gleichzeitigem Bau kann App 2 früher aus dem Review kommen)
                start = r["launches"][r["peaks"].index(max(r["peaks"]))]
                w10 = min(w for w, x in r["chk"].items() if x >= 10_000 * p.FX)
                self.assertEqual(w10, start)
                w100 = [w for w, x in r["chk"].items() if x >= 100_000 * p.FX]
                if w100:
                    erreicht += 1
                    self.assertGreaterEqual(min(w100), start + 5)
            self.assertGreater(gestartet, 40)
            if frei:                     # ohne Kassengrenze wächst jeder dieser Treffer über 100k
                self.assertEqual(erreicht, gestartet)


    # ---- Deine Angaben: Niedersachsen, ohne Programmierkenntnisse, Gesamtverlust <= 5.000 EUR ----
    def _deine(self, teil="DEIN PLAN"):
        return p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("Deine Angaben") and teil in k)]

    def test_kalender_niedersachsen(self):
        """Ferienordnung NI und Abiturtermine 2027: Q4 als eigene Stufe, Abitur geschützt."""
        lv = {"h_school": 10, "h_holiday": 38, "h_abiprep": 2.5, "h_abi": 0.5, "h_oral": 3, "h_gap": 28,
              "h_full": 55, "h_q4": 5}
        h = lambda y, m, d: p.hours_level(date(y, m, d), lv, "NI")  # noqa: E731
        self.assertEqual(h(2026, 12, 14), 10)                     # Schulwoche (Q3)
        self.assertAlmostEqual(h(2026, 12, 21), 2 + 35 / 5)       # Mo/Di je 1 h, Mi 23.12. Ferientag, 24.-27. frei
        self.assertAlmostEqual(h(2026, 12, 28), 3 + 35 * 4 / 5)   # Neujahr frei
        self.assertEqual(h(2027, 1, 4), 38)                       # 06.01. ist in NI kein Feiertag
        self.assertEqual(h(2027, 1, 11), 10)                      # erster Schultag 11.01.
        self.assertAlmostEqual(h(2027, 2, 1), 2 * 35 / 5 + 5)     # Halbjahresferien Mo/Di, ab Mi 03.02. Q4
        for d in (date(2027, 2, 8), date(2027, 3, 8)):            # Q4 bis 18.03.
            self.assertEqual(p.hours_level(d, lv, "NI"), 5)
        self.assertEqual(h(2027, 3, 22), 2.5)                     # Osterferien = Abiturvorbereitung
        self.assertEqual(h(2027, 4, 5), 0.5)                      # schriftlich 06.04.-13.05.
        self.assertEqual(h(2027, 5, 10), 0.5)
        self.assertEqual(h(2027, 5, 17), 3)                       # 5. Fach und Nachschreiben bis 07.06.
        self.assertEqual(h(2027, 6, 7), 28)
        self.assertEqual(h(2027, 7, 5), 55)
        # Bayern bleibt unverändert
        self.assertEqual(p.hours_level(date(2027, 2, 8), lv), 38)

    def test_nebenaufgaben_niedersachsen(self):
        """ETH-Bewerbung in den Weihnachtsferien, Rückfall-Bewerbung, Zeugnis, ab Juli Umzug nach Zürich."""
        P = self._deine()
        self.assertFalse(P["partnersuche"])
        gesamt = sum(p.nebenstunden(p.START + p.timedelta(weeks=w), False, False, P["neben"])
                     for w in range(p.WEEKS))
        self.assertAlmostEqual(gesamt, 6 + 2 + 1 + 8 * 6)
        self.assertEqual(p.nebenstunden(date(2026, 12, 28), False, False, P["neben"]), 6.0)

    def test_erst_bauen_dann_gruenden(self):
        """Gegründet wird erst, wenn App 1 halb steht; vorher nur Werkzeugkosten, kein Start ohne Firma."""
        P = self._deine()
        rng = random.Random(41)
        ohne = 0
        for _ in range(300):
            r = p.simulate(rng, P)
            if r["gegruendet"]:
                self.assertIsNotNone(r["gruendung_woche"])
                for w in r["launches"]:
                    self.assertGreaterEqual(w, r["gruendung_woche"])
            else:
                ohne += 1
                self.assertEqual(r["launches"], [])
                self.assertEqual(r["abwicklung"], 0.0)
                self.assertGreater(r["ergebnis"], -400)       # nur Claude Pro und Ähnliches
        rng = random.Random(42)
        frueh = [p.simulate(rng, self._deine("Tore wie bisher")) for _ in range(300)]
        self.assertGreater(sum(not r["gegruendet"] for r in frueh), 0)   # Bau am 28.02. abgebrochen

    def test_harte_grenze_fuenftausend(self):
        """Mit allen Pflichtkosten und der Auflösung nach dem 31.08. nie mehr als 5.000 EUR Verlust."""
        for k, P in p.SZENARIEN.items():
            if not k.startswith("Deine Angaben"):
                continue
            self.assertTrue(P["harte_grenze"], k)
            rng = random.Random(43)
            for _ in range(150):
                r = p.simulate(rng, P)
                self.assertGreaterEqual(r["ergebnis"], -P["start_cash"] - 1e-6, k)
                self.assertEqual(r["nachschuss"], 0.0, k)
                self.assertGreaterEqual(r["min_kasse"], 0.0, k)

    def test_ug_zu_teuer_heisst_kein_start(self):
        """Passt eine UG mit Pflichtkosten und Auflösung nicht in den Einsatz, wird nicht gegründet."""
        P = self._deine("gemieteter Geschäftsadresse")
        rng = random.Random(44)
        teuer = 0
        for _ in range(300):
            r = p.simulate(rng, P)
            if r["zu_teuer"]:
                teuer += 1
                self.assertFalse(r["gegruendet"])
                self.assertEqual(r["launches"], [])
        self.assertGreater(teuer, 0)

    def test_kein_start_im_abitur(self):
        """Zwischen 15.03. und 06.06. startet keine App; eine freigegebene wartet bis 07.06."""
        P = self._deine()
        von, bis = p.woche_ab(date(2027, 3, 15)), p.woche_ab(date(2027, 6, 7))
        rng = random.Random(45)
        for _ in range(300):
            for w in p.simulate(rng, P)["launches"]:
                self.assertFalse(von <= w < bis, w)

    def test_kassenprobe_deine_angaben(self):
        """Gewinn = Kasse - Einlagen + Forderungen - offene Kosten, auch mit späterer Gründung."""
        for teil in ("DEIN PLAN", "Anschrift der Eltern", "falls du schneller baust"):
            P = self._deine(teil)
            rng = random.Random(46)
            for _ in range(150):
                r = p.simulate(rng, P)
                probe = r["cash"] - P["start_cash"] - r["nachschuss"] - r["angel_geld"] + r["forderungen"] \
                    - r["offene_kosten"]
                self.assertAlmostEqual(r["profit_firma"], probe, delta=1e-6 * max(1.0, abs(probe)))

    def test_creator_geld_nur_nach_signal(self):
        """Signalregel: beim Start kein Testgeld; bezahlt wird nur drei Wochen später für eine App mit Signal."""
        P = self._deine()
        rng = random.Random(47)
        bezahlt = 0
        for _ in range(400):
            r = p.simulate(rng, P)
            ende_pause = p.woche_ab(P["startpause"][1])
            for woche, kosten in r["test_log"]:
                if kosten > 0:
                    bezahlt += 1
                    # drei Wochen nach einem Start, oder zum Ende der Startpause, wenn die Prüfung hineinfiel
                    self.assertTrue(woche - P["signal"]["wochen"] in r["launches"] or woche == ende_pause, woche)
                    self.assertGreaterEqual(kosten, 100.0)
            self.assertLessEqual(r["testkosten_g3"], P["test_cap"] + 1e-9)
        self.assertGreater(bezahlt, 0)

    def _bis_signal(self, P, peak, n=60, seed=50):
        """Läufe mit fester Spitze der ersten App, deren Signalprüfung vor Tor 1 und nach der Startpause liegt."""
        rng = random.Random(seed)
        tor = p.bis_woche(P["stopps"][0][0])
        out = []
        for _ in range(n):
            r = p.simulate(rng, dict(P, force_first_peak=peak))
            if r["launches"] and r["launches"][0] + P["signal"]["wochen"] <= tor \
                    and r["launches"][0] >= p.woche_ab(date(2027, 6, 7)):
                out.append(r)
        return out

    def test_signal_trennt_flop_und_treffer(self):
        """Ein Flop bekommt kein Testgeld; ein großer Treffer mit Signal bekommt es und seine Spitze zurück."""
        P = self._deine()
        flops = self._bis_signal(P, 300.0)
        self.assertGreater(len(flops), 5)
        for r in flops:
            self.assertFalse(any(w == r["launches"][0] + 3 and c > 0 for w, c in r["test_log"]))
        P_sicher = dict(P, m0_ohne_test=(1, 1, 1), signal=dict(P["signal"], abschlag=(1, 1, 1)))
        treffer = self._bis_signal(P_sicher, 20000.0)
        self.assertGreater(len(treffer), 5)
        for r in treffer:
            self.assertTrue(any(w == r["launches"][0] + 3 and c > 0 for w, c in r["test_log"]))
            self.assertEqual(r["peaks"][0], 20000.0)

    def test_signal_ist_unsicher(self):
        """Ohne bezahlten Test startet ein kleiner Treffer oft unter der Schwelle und bekommt kein Geld."""
        P = self._deine()
        laeufe = self._bis_signal(P, 1500.0, n=200, seed=51)
        ohne = sum(not any(w == r["launches"][0] + 3 and c > 0 for w, c in r["test_log"]) for r in laeufe)
        self.assertGreater(ohne, 0)

    def test_kein_testgeld_nach_dem_tor_und_nicht_im_abitur(self):
        """Testgeld nur vor dem Tor und nie in der Startpause (15.03.-06.06.)."""
        P = self._deine()
        von, bis = p.woche_ab(date(2027, 3, 15)), p.woche_ab(date(2027, 6, 7))
        rng = random.Random(52)
        for _ in range(400):
            r = p.simulate(rng, P)
            for w, c in r["test_log"]:
                if c > 0:
                    self.assertFalse(von <= w < bis, w)
                    if r["gestoppt"]:
                        self.assertLess(w, r["stopp_woche"])

    def test_ganz_ohne_testgeld(self):
        P = self._deine("ganz ohne Testgeld")
        rng = random.Random(53)
        for _ in range(200):
            self.assertEqual(sum(c for _, c in p.simulate(rng, P)["test_log"]), 0.0)

    def test_harte_grenze_ug_mit_gruendung(self):
        """Auch eine gegründete UG verliert mit Auflösung nie mehr als 5.000 EUR (günstigere Kosten zum Testen)."""
        P = dict(self._deine("Anschrift der Eltern"), abwicklung=(1500, 1800, 2200),
                 fixed_month=(80, 120, 160), fixed_stop=(60, 90, 120))
        rng = random.Random(54)
        gegruendet = 0
        for _ in range(400):
            r = p.simulate(rng, P)
            gegruendet += r["gegruendet"]
            self.assertGreaterEqual(r["ergebnis"], -P["start_cash"] - 1e-6)
            self.assertEqual(r["nachschuss"], 0.0)
            if r["gegruendet"] and r["launches"]:
                self.assertGreaterEqual(r["launches"][0], r["apple_ab"])      # Apple-Wartezeit
                self.assertGreaterEqual(r["einreichung1"], r["gruendung_woche"])
            self.assertEqual(r["kv_kosten"], 0.0)                            # UG: keine Krankenversicherung
        self.assertGreater(gegruendet, 200)

    def test_gruendung_bei_der_haelfte(self):
        """Wird App 1 am 28.02. abgebrochen, bevor sie halb steht, gibt es keine Gründung und keine Kosten."""
        P = self._deine("Tore wie bisher")
        rng = random.Random(55)
        ohne = 0
        for _ in range(300):
            r = p.simulate(rng, P)
            if not r["gegruendet"]:
                ohne += 1
                self.assertEqual(r["launches"], [])
                self.assertGreater(r["ergebnis"], -400)
            elif r["gestoppt"]:
                self.assertLess(r["gruendung_woche"], r["stopp_woche"])       # nie in der Woche des Tors
        self.assertGreater(ohne, 0)

    def test_krankenversicherung_nur_bei_dauerhaftem_gewinn(self):
        """Eigene Krankenversicherung nur, wenn der Gewinn dauerhaft über der Grenze liegt."""
        P = self._deine()
        rng = random.Random(56)
        for _ in range(300):
            r = p.simulate(rng, P)
            if r["profit_firma"] < 0:
                self.assertEqual(r["kv_kosten"], 0.0)
        gross = dict(P, force_first_peak=60000.0, force_m0=20000.0, force_g=2.0, startpause=None)
        rng = random.Random(57)
        self.assertGreater(sum(p.simulate(rng, gross)["kv_kosten"] > 0 for _ in range(40)), 10)

    def test_deine_angaben_ohne_web_und_angel(self):
        for k, P in p.SZENARIEN.items():
            if k.startswith("Deine Angaben"):
                self.assertEqual(P["web_share"], (0.0, 0.0, 0.0), k)
                self.assertFalse(P["angel"], k)

    def test_alte_szenarien_lauf_fuer_lauf_gleich(self):
        """Die bisherigen Szenarien rechnen mit dem neuen Code Lauf für Lauf wie im Stand 7cb0468."""
        import importlib.util
        import subprocess
        import tempfile
        root = Path(__file__).resolve().parents[1]
        try:
            alt_code = subprocess.run(["git", "-C", str(root), "show", "7cb0468:plan/plan_500k.py"],
                                      capture_output=True, text=True, check=True).stdout
        except (OSError, subprocess.CalledProcessError):
            self.skipTest("git oder Stand 7cb0468 nicht verfügbar")
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(alt_code)
        spec = importlib.util.spec_from_file_location("plan_alt", f.name)
        alt = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(alt)
        for name, P_alt in alt.SZENARIEN.items():
            r1, r2 = random.Random(5), random.Random(5)
            for _ in range(15):
                a, b = alt.simulate(r1, P_alt), p.simulate(r2, p.SZENARIEN[name])
                for k in a:
                    self.assertEqual(a[k], b[k], (name, k))

    def test_frueher_frei_nach_der_letzten_pruefung(self):
        """Liegt die Prüfung im 5. Fach früh, beginnen die freien Wochen früher (Standard: 07.06.)."""
        lv = {"h_school": 10, "h_holiday": 38, "h_abiprep": 2.5, "h_abi": 0.5, "h_oral": 3, "h_gap": 28,
              "h_full": 55, "h_q4": 5}
        self.assertEqual(p.hours_level(date(2027, 5, 31), lv, "NI"), 3)
        self.assertEqual(p.hours_level(date(2027, 5, 31), lv, "NI", date(2027, 5, 31)), 28)
        self.assertEqual(p.hours_level(date(2027, 5, 24), lv, "NI", date(2027, 5, 31)), 3)
        self.assertEqual(p.hours_level(date(2027, 5, 10), lv, "NI", date(2027, 5, 24)), 0.5)   # Abitur bleibt

    def test_restwert_und_ferienjob(self):
        """Restwert nur bei laufendem Gewinn, Ferienjob nur nach dem Ende der Jagd; beides getrennt ausgewiesen."""
        P = dict(self._deine(), restwert=dict(monate=(2, 5, 10), p=(1, 1, 1)),
                 ferienjob=dict(ab=date(2027, 7, 19), netto_woche=(600, 600, 600), max_app_h=5))
        rng = random.Random(58)
        mit_rest = 0
        for _ in range(300):
            r = p.simulate(rng, P)
            self.assertAlmostEqual(r["ergebnis"], r["ergebnis_app"] + r["restwert"] + r["job_netto"])
            self.assertGreaterEqual(r["restwert"], 0.0)
            mit_rest += r["restwert"] > 0
            if r["gestoppt"]:
                # Tor 1 am 18.07.: Job in den 6 Wochen ab 19.07. (bei Tor 2 am 08.08. entsprechend weniger)
                self.assertEqual(r["job_wochen"], p.WEEKS - max(r["stopp_woche"], p.woche_ab(date(2027, 7, 19))))
                self.assertAlmostEqual(r["job_netto"], 600.0 * r["job_wochen"])
            else:
                self.assertEqual(r["job_netto"], 0.0)
        self.assertGreater(mit_rest, 0)
        ohne = self._deine()
        self.assertIsNone(ohne["restwert"])
        self.assertIsNone(ohne["ferienjob"])

    def test_ruhezeit_im_abitur(self):
        """Ruhezeit: ohne App im Store und im Review ruhen die Abos und der Bau; mit wirkungslosen Werten
        (Kosten nicht niedriger, Stunden nicht gedeckelt) ändert sie nichts."""
        von, bis = date(2027, 3, 15), date(2027, 6, 7)
        basis = self._deine()
        neutral = dict(basis, fix_ruhe=dict(von=von, bis=bis, monat=(1e9, 1e9, 1e9), max_h=1e9))
        ruhe = dict(basis, fix_ruhe=dict(von=von, bis=bis, monat=(5, 5, 5), max_h=0.0))
        nur_kosten = dict(basis, fix_ruhe=dict(von=von, bis=bis, monat=(5, 5, 5), max_h=1e9))
        r0 = [p.simulate(random.Random(s), basis) for s in range(120)]
        rn = [p.simulate(random.Random(s), neutral) for s in range(120)]
        rr = [p.simulate(random.Random(s), ruhe) for s in range(120)]
        rk = [p.simulate(random.Random(s), nur_kosten) for s in range(120)]
        spaeter = 0
        for a, n, r in zip(r0, rn, rr):
            self.assertAlmostEqual(a["ergebnis"], n["ergebnis"])
            if a["einreichung1"] is not None and r["einreichung1"] is not None:
                # ohne Baustunden in der Ruhezeit wird App 1 nie früher fertig
                self.assertGreaterEqual(r["einreichung1"], a["einreichung1"])
                spaeter += r["einreichung1"] > a["einreichung1"]
        self.assertGreater(spaeter, 0)
        # nur niedrigere Kosten (Stunden unverändert): im Mittel besser, in vielen Läufen spürbar
        self.assertGreater(sum(x["ergebnis"] for x in rk), sum(x["ergebnis"] for x in r0))
        self.assertGreater(sum(k["ergebnis"] > a["ergebnis"] + 20 for a, k in zip(r0, rk)), 30)
        self.assertIsNone(basis["fix_ruhe"])

    def test_ferienjob_chance_und_vorrang(self):
        """Ferienjob: ohne Zusage kein Lohn; mit Vorrang (immer) läuft er ab dem Datum auch ohne Tor."""
        ab = date(2027, 6, 14)
        kein = dict(self._deine(), ferienjob=dict(ab=date(2027, 7, 19), netto_woche=(600, 600, 600), max_app_h=5,
                                                  p=(0, 0, 0)))
        immer = dict(self._deine(), ferienjob=dict(ab=ab, netto_woche=(600, 600, 600), max_app_h=10, immer=True))
        rng = random.Random(61)
        for _ in range(150):
            r = p.simulate(rng, kein)
            self.assertEqual((r["job_wochen"], r["job_netto"]), (0, 0.0))
            self.assertAlmostEqual(r["ergebnis"], r["ergebnis_app"] + r["restwert"])
        for _ in range(150):
            r = p.simulate(rng, immer)
            self.assertEqual(r["job_wochen"], p.WEEKS - p.woche_ab(ab))
            self.assertAlmostEqual(r["job_netto"], 600.0 * r["job_wochen"])

    def test_restwert_braucht_alter_und_gewinn(self):
        """Restwert nur für Apps, die lange genug im Store sind und genug Monatsgewinn bringen."""
        basis = dict(self._deine(), build_first=(20, 30, 40), einmal_stunden=(0, 0, 0))
        offen = dict(basis, restwert=dict(monate=(4, 4, 4), p=(1, 1, 1)))
        zu_jung = dict(basis, restwert=dict(monate=(4, 4, 4), p=(1, 1, 1), min_alter_w=p.WEEKS + 1))
        zu_klein = dict(basis, restwert=dict(monate=(4, 4, 4), p=(1, 1, 1), min_monat=1e12))
        schwelle = dict(basis, restwert=dict(monate=(4, 4, 4), p=(1, 1, 1), min_alter_w=8, min_monat=100.0))
        mit = 0
        for s in range(400):
            a = p.simulate(random.Random(s), offen)
            mit += a["restwert"] > 0
            self.assertEqual(p.simulate(random.Random(s), zu_jung)["restwert"], 0.0)
            self.assertEqual(p.simulate(random.Random(s), zu_klein)["restwert"], 0.0)
            b = p.simulate(random.Random(s), schwelle)
            self.assertIn(b["restwert"], (0.0, a["restwert"]))
            if b["restwert"] > 0:
                self.assertGreater(b["restwert"], 4 * 100.0)
                self.assertLessEqual(max(l for l in b["launches"]) if len(b["launches"]) == 1 else 0, p.WEEKS - 8)
        self.assertGreater(mit, 0)

    def test_zweite_signalpruefung(self):
        """Eine vor dem Abitur gestartete App bekommt am 28.06. eine zweite Prüfung; Testgeld fließt nie früher
        als ohne die Regel und nie in der Startpause."""
        zweite = date(2027, 6, 28)
        basis = dict(self._deine(), build_first=(20, 30, 40), einmal_stunden=(0, 0, 0))
        mit = dict(basis, signal=dict(p.SIGNAL, zweite=zweite))
        sp0, sp1 = p.woche_ab(p.STARTPAUSE_NI[0]), p.woche_ab(p.STARTPAUSE_NI[1])
        mehr = 0
        for s in range(500):
            a = p.simulate(random.Random(s), basis)
            b = p.simulate(random.Random(s), mit)
            for w, c in b["test_log"]:
                if c > 0:
                    self.assertFalse(sp0 <= w < sp1)
            ta = sum(c for _, c in a["test_log"])
            tb = sum(c for _, c in b["test_log"])
            mehr += tb > ta + 1
        self.assertGreater(mehr, 0)        # die zweite Prüfung löst in manchen Läufen zusätzlich Testgeld aus

    def test_verkaufsstopp_ohne_nachfolger(self):
        """Endet die Jagd ohne Verkauf oder Übergabe, entfallen die Erlöse nach dem Verkaufsstopp; ein später
        Stichtag (31.08.) ändert nichts, ein früher kostet mehr."""
        basis = dict(self._deine(), build_first=(20, 30, 40), einmal_stunden=(0, 0, 0))
        def mit(tag):
            return dict(basis, stilllegung=dict(verkauf_bis=tag))
        abzug = 0
        for s in range(300):
            a = p.simulate(random.Random(s), basis)
            b31 = p.simulate(random.Random(s), mit(date(2027, 8, 31)))
            b15 = p.simulate(random.Random(s), mit(date(2027, 8, 15)))
            b07 = p.simulate(random.Random(s), mit(date(2027, 7, 31)))
            self.assertEqual(a["abschalt_abzug"], 0.0)
            self.assertAlmostEqual(b31["ergebnis"], a["ergebnis"])
            self.assertAlmostEqual(b15["ergebnis"], a["ergebnis"] - b15["abschalt_abzug"])
            self.assertAlmostEqual(b07["ergebnis"], a["ergebnis"] - b07["abschalt_abzug"])
            if not b15["gestoppt"]:
                self.assertEqual(b15["abschalt_abzug"], 0.0)       # Treffer über dem Tor: keine Stilllegung
            abzug += b15["abschalt_abzug"] > 0
        self.assertGreater(abzug, 50)
        # mit Nachfolger (Übergabe sicher, ohne Schwelle) entfällt der Abzug, sobald ein Restwert entsteht
        nachfolger = dict(mit(date(2027, 7, 31)), restwert=dict(monate=(2, 2, 2), p=(1, 1, 1)))
        for s in range(300):
            r = p.simulate(random.Random(s), nachfolger)
            if r["restwert"] > 0:
                self.assertEqual(r["abschalt_abzug"], 0.0)

    def test_kosten_vor_dem_ersten_start(self):
        """Zwischen Gründung und erstem Start laufen nur die kleinen Kosten; mit gleichen Werten ändert sich nichts."""
        basis = self._deine()
        gleich = dict(basis, fix_vor_start=(1e9, 1e9, 1e9))
        billig = dict(basis, fix_vor_start=(0, 0, 0))
        ra = [p.simulate(random.Random(s), basis)["ergebnis"] for s in range(150)]
        rb = [p.simulate(random.Random(s), billig)["ergebnis"] for s in range(150)]
        self.assertGreater(sum(rb), sum(ra) + 150 * 20)       # im Mittel deutlich weniger Kosten
        # ein Wert über fixed_month wirkt nicht (es gilt das Minimum), nur der Zufallsstrom verschiebt sich
        rg = [p.simulate(random.Random(s), gleich) for s in range(150)]
        self.assertTrue(all(r["gegruendet"] or r["zu_teuer"] or r["gruendung_woche"] is None for r in rg))

    def test_frueher_jobstart_ohne_app(self):
        """Ist am Stichtag noch keine App im Store, endet die Jagd und der Job beginnt früher."""
        frueh = date(2027, 7, 5)
        P = dict(self._deine(), ferienjob=dict(ab=date(2027, 7, 19), netto_woche=(600, 600, 600), max_app_h=5,
                                               frueh_ab=frueh))
        wf = p.woche_ab(frueh)
        n_frueh = 0
        for s in range(300):
            r = p.simulate(random.Random(s), P)
            if r["job_frueh"]:
                n_frueh += 1
                self.assertTrue(r["gestoppt"])
                self.assertEqual(r["stopp_woche"], wf)
                self.assertEqual(r["job_wochen"], p.WEEKS - wf)
                self.assertTrue(all(l >= wf for l in r["launches"]))     # vorher war keine App im Store
            elif r["gestoppt"]:
                self.assertEqual(r["job_wochen"], p.WEEKS - max(r["stopp_woche"], p.woche_ab(date(2027, 7, 19))))
                self.assertTrue(any(l < wf for l in r["launches"]))
        self.assertGreater(n_frueh, 10)

    def test_restwert_verkauf_vor_uebergabe(self):
        """Verkauf nur ab Umsatzschwelle und Mindestalter, sonst Übergabe abzüglich der Einmalkosten."""
        basis = dict(self._deine(), build_first=(20, 30, 40), einmal_stunden=(0, 0, 0))
        nur_verkauf = dict(basis, restwert=dict(monate=(2, 2, 2), p=(0, 0, 0), verkauf=dict(
            ab_umsatz_usd=300, min_alter_w=8, p=(1, 1, 1), monate=(4, 4, 4))))
        nur_uebergabe = dict(basis, restwert=dict(monate=(2, 2, 2), p=(1, 1, 1), kosten=(200, 200, 200)))
        ohne_kosten = dict(basis, restwert=dict(monate=(2, 2, 2), p=(1, 1, 1)))
        verkauft = 0
        for s in range(500):
            v = p.simulate(random.Random(s), nur_verkauf)
            if v["restwert"] > 0:
                verkauft += 1
                self.assertGreaterEqual(max(v["max_mrr"], 0), 300 * p.FX * 0.99)
                self.assertTrue(any(l <= p.WEEKS - 8 for l in v["launches"]))
            u = p.simulate(random.Random(s), nur_uebergabe)
            o = p.simulate(random.Random(s), ohne_kosten)
            self.assertAlmostEqual(u["restwert"], max(0.0, o["restwert"] - 200.0))
        self.assertGreater(verkauft, 0)

    def test_plan_mit_hebeln(self):
        """Der Plan mit Hebeln nutzt die geprüften Werte; Restwert und Ferienjob sind getrennte Zusätze."""
        P = p.scen(**p.PLAN_HEBEL)
        self.assertEqual(P["build_first"], (78, 130, 260))
        self.assertEqual(P["p_faktor"], (0.8, 0.95, 1.2))
        self.assertEqual(P["abwicklung"], (20, 80, 500))
        self.assertEqual(P["gruendung"]["setup"], (140, 200, 380))
        self.assertEqual(P["gruendung"]["bei"], 0.5)
        self.assertEqual(P["stilllegung"]["verkauf_bis"], date(2027, 8, 15))
        self.assertEqual(P["start_cash"], 5000.0)
        self.assertTrue(P["harte_grenze"])
        self.assertIsNone(P["restwert"])
        self.assertIsNone(P["ferienjob"])
        namen = [k for k in p.SZENARIEN if k.startswith("Hebel:")]
        self.assertGreaterEqual(len(namen), 12)
        self.assertEqual(sum("PLAN MIT HEBELN" in k for k in namen), 1)
        for s in range(200):
            r = p.simulate(random.Random(s), P)
            self.assertGreaterEqual(r["ergebnis"], -5000.0 - 1e-6)       # nie mehr als der Einsatz verloren
            self.assertAlmostEqual(r["ergebnis"], r["ergebnis_app"])

    def test_bisherige_szenarien_ohne_neue_teile(self):
        """Die früheren Szenarien rechnen mit Bayern, sofortiger Gründung und ohne harte Grenze."""
        for k, P in p.SZENARIEN.items():
            if k.startswith(("Deine Angaben", "Hebel:")):
                continue
            self.assertEqual(P["kalender"], "BY", k)
            self.assertIsNone(P.get("gruendung"), k)
            self.assertFalse(P["harte_grenze"], k)
            self.assertEqual(P["abwicklung"], (0, 0, 0), k)

if __name__ == "__main__":
    unittest.main()
