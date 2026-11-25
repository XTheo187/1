"""Tests für plan/plan_500k.py - App-Weg zu 500.000 EUR bis 31.08.2027."""

from __future__ import annotations

import random
import sys
import unittest
from datetime import date, timedelta
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
        """Die bisherigen Szenarien rechnen mit dem neuen Code Lauf für Lauf wie in den Ständen 7cb0468 (alle
        damaligen Szenarien), e2b0430 (die Szenarien „Deine Angaben“, Ausgangslage der Hebel in 07) und bcad479
        (alte Ausgangslage der Hebel mit Verkaufsstopp)."""
        import importlib.util
        import subprocess
        import tempfile
        root = Path(__file__).resolve().parents[1]
        for stand, praefix in (("7cb0468", ""), ("e2b0430", "Deine Angaben"),
                               ("bcad479", "Hebel: Plan vom 23.11. mit Verkaufsstopp am 15.08.")):
            try:
                alt_code = subprocess.run(["git", "-C", str(root), "show", f"{stand}:plan/plan_500k.py"],
                                          capture_output=True, text=True, check=True).stdout
            except (OSError, subprocess.CalledProcessError):
                self.skipTest(f"git oder Stand {stand} nicht verfügbar")
            with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
                f.write(alt_code)
            spec = importlib.util.spec_from_file_location(f"plan_alt_{stand}", f.name)
            alt = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(alt)
            for name, P_alt in alt.SZENARIEN.items():
                if not name.startswith(praefix):
                    continue
                r1, r2 = random.Random(5), random.Random(5)
                for _ in range(15):
                    a, b = alt.simulate(r1, P_alt), p.simulate(r2, p.SZENARIEN[name])
                    for k in a:
                        self.assertEqual(a[k], b[k], (stand, name, k))

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
        # ein Wert über fixed_month wirkt nicht (es gilt das Minimum); gleiche Werte ziehen keine Zufallszahl
        rg = [p.simulate(random.Random(s), gleich)["ergebnis"] for s in range(150)]
        self.assertEqual(rg, ra)

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

    # ---- Prüfung des Modells vom 25.11.2026 ----
    DEIN_PLAN = "Hebel: Plan mit Hebeln + Übergabe oder Verkauf + Ferienjob (DEIN PLAN, Stand 25.11.)"
    MIT_HEBELN = "Hebel: PLAN MIT HEBELN (Kosten, Bau, Markt, Signal; Verkaufsstopp 15.08.)"
    OHNE_STARTPAUSE = ("Hebel: DEIN PLAN ohne Startpause (eine freigegebene App erscheint auch im Abitur, ohne Arbeit "
                       "daran)")

    def test_hebel_szenarien_kasse_und_grenze(self):
        """Alle Hebel-Szenarien: nie mehr als der Einsatz verloren, kein Nachschuss, Kasse nie im Minus,
        Kassenprobe stimmt, und die Ergebnisse setzen sich richtig zusammen."""
        for k, P in p.SZENARIEN.items():
            if not k.startswith("Hebel:"):
                continue
            rng = random.Random(43)
            for _ in range(100):
                r = p.simulate(rng, P)
                self.assertGreaterEqual(r["ergebnis_app"], -P["start_cash"] - 1e-6, k)
                self.assertEqual(r["nachschuss"], 0.0, k)
                self.assertGreaterEqual(r["min_kasse"], 0.0, k)
                probe = (r["cash"] - P["start_cash"] - r["nachschuss"] - r["angel_geld"] + r["forderungen"]
                         - r["offene_kosten"])
                self.assertAlmostEqual(r["profit_firma"], probe, delta=1e-6 * max(1.0, abs(probe)))
                self.assertAlmostEqual(r["ergebnis_dein"], r["ergebnis_app"] + r["verkauf"] + r["job_netto"])
                self.assertAlmostEqual(r["ergebnis"], r["ergebnis_app"] + r["restwert"] + r["job_netto"]
                                       - r["eltern_kosten"])

    def test_neue_nebenaufgaben_nur_in_hebel_szenarien(self):
        """Die Stunden der Detailpläne gelten in allen Hebel-Szenarien außer der alten Ausgangslage."""
        alt = "Hebel: Plan vom 23.11. mit Verkaufsstopp am 15.08. (Pflicht, bisher nicht gerechnet)"
        for k, P in p.SZENARIEN.items():
            if not k.startswith("Hebel:") or k == alt:
                continue
            self.assertIs(P["neben"], p.NEBEN_PLAN, k)
            self.assertEqual(P["gruendung"]["stunden"], 6.0, k)
            self.assertEqual(P["pflege_h_woche"], (0.4, 0.5, 0.6), k)
            if P["signal"]:
                self.assertTrue(P["signal"].get("creator_nach_pause"), k)
            self.assertEqual(P["kasse_ab_gruendung"], 10 / 60, k)
            self.assertEqual(P["konten_je_einreichung"], 1.83, k)
            self.assertEqual(P["gruendung"]["spaet"], (date(2027, 3, 1), date(2027, 6, 7)), k)
            self.assertEqual(P["vorb_nach_einreichung1"], 3.5, k)
            if "Gegenprobe" not in k:
                self.assertEqual(P["vorlage_h"], 3.5, k)
                self.assertEqual(P["post_deckel"], (1.5, 6.5), k)
                self.assertEqual(P["c_organisch"], (0.15, 0.18, 0.20), k)
                self.assertEqual(P["c_organisch_bis_usd"], 100000.0, k)
                self.assertFalse(P["c_organisch_aus"], k)
                self.assertEqual(P["ohne_posts"], dict(pause=1.0, ende=0.5), k)
                self.assertEqual(P["m0"], (300, 1000, 3000), k)
                self.assertTrue(P["kv_bis_dienstende"], k)
                self.assertEqual(P["exit_min_age_weeks"], p.WEEKS + 1, k)
                if "Schnittliste" not in k:
                    self.assertEqual(P["schnitt_mp"], (141, 1e9, 0.938), k)
        mehr = sum(p.NEBEN_PLAN.values()) - sum(p.NEBEN_NI.values())
        self.assertAlmostEqual(mehr, 25.5)
        self.assertAlmostEqual(p.NEBEN_PLAN[date(2027, 6, 21)], 2.0)     # Finanzierungsbrief und Zeitarbeitsanfrage
        # Hannover (2 h) in KW 28 statt KW 24, Zimmersuche 2 h in KW 24
        self.assertAlmostEqual(p.NEBEN_PLAN[date(2027, 7, 12)], p.NEBEN_NI[date(2027, 7, 12)] + 2.0)
        self.assertAlmostEqual(p.NEBEN_PLAN[date(2027, 6, 14)], 2.0)
        self.assertIs(p.SZENARIEN[alt]["neben"], p.NEBEN_NI)

    def test_creator_nie_vor_ende_der_startpause(self):
        """Ein Signal vor dem Abitur zählt, Creator-Geld fließt aber erst nach der letzten Prüfung, auch ohne
        Startpause (dann gilt die Prüfungszeit aus signal_pause)."""
        for name in (self.MIT_HEBELN, self.DEIN_PLAN, self.OHNE_STARTPAUSE):
            P = dict(p.SZENARIEN[name], build_first=(30, 45, 60), einmal_stunden=(0, 0, 0))
            pause = P["startpause"] or P["signal_pause"]
            ende = p.woche_ab(pause[1])
            vor_pause = 0
            for s in range(600):
                r = p.simulate(random.Random(s), P)
                vor_pause += any(l < p.woche_ab(pause[0]) for l in r["launches"])
                for w, c in r["test_log"]:
                    if c > 0:
                        self.assertGreaterEqual(w, ende, (name, s, w))
            self.assertGreater(vor_pause, 100)

    def test_ruhe_wirkt_nicht_mit_app_im_store(self):
        """Ist App 1 vor dem 15.03. im Store, ändert die Ruhezeit (ohne nur_betrieb) nichts."""
        basis = dict(p.SZENARIEN[self.MIT_HEBELN], fix_ruhe=None, build_first=(30, 45, 60))
        mit = dict(basis, fix_ruhe=dict(von=date(2027, 3, 15), bis=date(2027, 6, 7), monat=(5, 5, 5), max_h=0.0))
        von = p.woche_ab(date(2027, 3, 15))
        n = 0
        for s in range(600):
            a = p.simulate(random.Random(s), basis)
            b = p.simulate(random.Random(s), mit)
            if a["launches"] and a["launches"][0] < von:
                n += 1
                self.assertAlmostEqual(a["ergebnis"], b["ergebnis"])
        self.assertGreater(n, 100)

    def test_im_abitur_nur_betrieb(self):
        """Mit App im Store oder im Review gibt es in den Abiturwochen weder Bau noch Tests; ohne die Regel
        flössen die Abiturstunden in die nächste App."""
        P = dict(p.SZENARIEN[self.MIT_HEBELN], build_first=(30, 45, 60))
        ohne = dict(P, fix_ruhe=dict(P["fix_ruhe"], nur_betrieb=False))
        genutzt = 0
        for s in range(400):
            self.assertEqual(p.simulate(random.Random(s), P)["abitur_h"], 0.0)
            genutzt += p.simulate(random.Random(s), ohne)["abitur_h"] > 0
        self.assertGreater(genutzt, 50)

    def test_job_nie_bei_laufender_jagd(self):
        """Der Lohn zählt nur nach dem Ende der Jagd, ab dem 05.07. (Stichtag) oder dem 19.07."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        for s in range(800):
            r = p.simulate(random.Random(s), P)
            if r["job_wochen"] > 0:
                self.assertTrue(r["gestoppt"])
                ab = p.woche_ab(date(2027, 7, 5) if r["job_frueh"] else date(2027, 7, 19))
                self.assertEqual(r["job_wochen"], p.WEEKS - max(r["stopp_woche"], ab))

    def test_stichtag_auch_ohne_job(self):
        """Ist am 04.07. keine App im Store, endet die Jagd auch dann, wenn kein Job zustande kommt."""
        frueh = date(2027, 7, 5)
        P = dict(p.SZENARIEN[self.MIT_HEBELN], ferienjob=dict(ab=date(2027, 7, 19), netto_woche=(600, 600, 600),
                                                              max_app_h=5, p=(0, 0, 0), frueh_ab=frueh))
        wf = p.woche_ab(frueh)
        n = 0
        for s in range(400):
            r = p.simulate(random.Random(s), P)
            self.assertEqual(r["job_wochen"], 0)
            self.assertFalse(r["job_frueh"])
            if r["stichtag_stopp"]:
                n += 1
                self.assertTrue(r["gestoppt"])
                self.assertEqual(r["stopp_woche"], wf)
                self.assertTrue(all(l >= wf for l in r["launches"]))
                self.assertEqual(r["bau_nach_stopp"], 0, s)      # nach dem Stichtag beginnt keine neue App
        self.assertGreater(n, 50)

    def test_zweite_pruefung_nur_in_der_woche_ab_2806(self):
        """Die zweite Signalprüfung ändert vor der Woche ab 28.06. nichts; die erste Abweichung ist eine Zahlung
        genau in dieser Woche."""
        basis = p.SZENARIEN["Hebel: Plan vom 23.11. mit Verkaufsstopp und allen Nebenaufgaben der Detailpläne "
                            "(Ausgangslage)"]
        basis = dict(basis, build_first=(30, 45, 60))
        mit = dict(basis, signal=dict(basis["signal"], zweite=date(2027, 6, 28)))
        w2 = p.woche_ab(date(2027, 6, 28))
        n = 0
        for s in range(1500):
            a = p.simulate(random.Random(s), basis)["test_log"]
            b = p.simulate(random.Random(s), mit)["test_log"]
            for x, y in zip(a + [None], b):
                if x != y:
                    n += 1
                    self.assertEqual(y[0], w2, (s, x, y))
                    break
        self.assertGreater(n, 0)

    def test_erloese_nach_der_uebertragung_gehoeren_dem_nachfolger(self):
        """Ab der Übertragung zählen die Erlöse nicht mehr für dich. Bei einer Übergabe stecken sie schon im Wert
        der zwölf Monate ab der Übertragung (06, 4.7: 0,7/2/5 Monatsgewinne), beim Verkauf gehören sie dem Käufer."""
        rw = dict(p.RESTWERT["restwert"], p=(1, 1, 1), anmeldung=None)
        rw_v = dict(rw, verkauf=dict(rw["verkauf"], p=(1, 1, 1)))
        P = dict(p.SZENARIEN[self.MIT_HEBELN], build_first=(30, 45, 60))
        ohne = dict(P, restwert=dict(rw, uebertragung=None))
        mit = dict(P, restwert=rw)
        ohne_v, mit_v = dict(P, restwert=dict(rw_v, uebertragung=None)), dict(P, restwert=rw_v)
        n_u = n_v = 0
        for s in range(500):
            a, b = p.simulate(random.Random(s), ohne), p.simulate(random.Random(s), mit)
            self.assertEqual(a["art"], b["art"])
            # die Familienversicherung richtet sich nach dem eigenen Jahresgewinn, also ohne die Erlöse ab der Übertragung
            kv = a["kv_kosten"] - b["kv_kosten"]
            if b["art"] == "uebergabe":
                n_u += 1
                self.assertAlmostEqual(b["ergebnis_app"], a["ergebnis_app"] - b["nach_uebertragung"] + kv)
                self.assertAlmostEqual(b["restwert"], a["restwert"])        # nicht doppelt gezählt
                self.assertAlmostEqual(b["ergebnis"], a["ergebnis"] - b["nach_uebertragung"] + kv)
                self.assertEqual(b["abschalt_abzug"], 0.0)                  # die Abos bleiben im Verkauf
            av, bv = p.simulate(random.Random(s), ohne_v), p.simulate(random.Random(s), mit_v)
            if bv["art"] == "verkauf":
                n_v += 1
                kv_v = av["kv_kosten"] - bv["kv_kosten"]
                self.assertAlmostEqual(bv["ergebnis_app"], av["ergebnis_app"] - bv["nach_uebertragung"] + kv_v)
                self.assertAlmostEqual(bv["restwert"], av["restwert"])      # Kaufpreis unverändert
                self.assertAlmostEqual(bv["ergebnis_dein"], bv["ergebnis_app"] + bv["verkauf"] + bv["job_netto"])
        self.assertGreater(n_u, 5)
        self.assertGreater(n_v, 5)

    def test_entscheidung_mit_dem_stand_am_stichtag(self):
        """Übergabe und Verkauf hängen am Stand bis Sa 07.08.: Apps, die danach erscheinen oder bis zum
        Umschalttag So 08.08. keine acht vollen Wochen im Store sind (Start nach So 13.06.), werden nicht
        verkauft."""
        rw = dict(p.RESTWERT["restwert"], p=(1, 1, 1), anmeldung=None, verkauf=dict(
            p.RESTWERT["restwert"]["verkauf"], p=(1, 1, 1)))
        P = dict(p.SZENARIEN[self.MIT_HEBELN], build_first=(30, 45, 60), restwert=rw)
        grenze = p.woche_ab(date(2027, 8, 8)) - 8           # Woche ab Mo 07.06.
        self.assertEqual(p.START + timedelta(weeks=grenze), date(2027, 6, 7))
        n = 0
        for s in range(600):
            r = p.simulate(random.Random(s), P)
            if r["art"] == "verkauf":
                n += 1
                self.assertTrue(any(l <= grenze for l in r["launches"]), s)
            if r["art"] is not None:
                self.assertTrue(any(l <= p.bis_woche(date(2027, 8, 7)) for l in r["launches"]), s)
        self.assertGreater(n, 5)

    def test_anmeldung_des_elternteils(self):
        """Übergabe nur, wenn sich das Elternteil nach dem Messtag (Mo 28.06., ~100 USD MRR) angemeldet hat;
        bleibt die Übergabe aus, sind seine Kosten verloren (Geld der Familie, nicht deines)."""
        rw = dict(p.RESTWERT["restwert"], p=(1, 1, 1))
        P = dict(p.SZENARIEN[self.MIT_HEBELN], build_first=(30, 45, 60), restwert=rw)
        n_k = n_u = 0
        for s in range(600):
            r = p.simulate(random.Random(s), P)
            if r["art"] == "uebergabe":
                n_u += 1
                self.assertTrue(r["eltern_konto"])
                self.assertEqual(r["eltern_kosten"], 0.0)
            if r["eltern_konto"] and r["art"] != "uebergabe":
                n_k += 1
                self.assertGreaterEqual(r["eltern_kosten"], 120.0)
                self.assertLessEqual(r["eltern_kosten"], 165.0)
            if not r["eltern_konto"]:
                self.assertEqual(r["eltern_kosten"], 0.0)
            self.assertAlmostEqual(r["ergebnis_dein"], r["ergebnis_app"] + r["verkauf"] + r["job_netto"])
        self.assertGreater(n_u, 5)
        self.assertGreater(n_k, 5)


    def test_lohn_bis_zum_letzten_arbeitstag(self):
        """Läuft der Job bis zum Ende des Modells, zählen die Werktage bis zum letzten Arbeitstag mit
        (Fr 10.09.: 10 Werktage, Di 31.08.: 2)."""
        basis = dict(p.SZENARIEN[self.MIT_HEBELN], ferienjob=dict(ab=date(2027, 7, 19), netto_woche=(600, 600, 600),
                                                                   max_app_h=5, frueh_ab=date(2027, 7, 5)))
        for bis, extra in ((None, 0.0), (date(2027, 8, 31), 0.4), (date(2027, 9, 10), 2.0)):
            P = dict(basis, ferienjob=dict(basis["ferienjob"], bis=bis)) if bis else basis
            for s in range(150):
                r = p.simulate(random.Random(s), P)
                if r["job_wochen"]:
                    self.assertAlmostEqual(r["job_nach_w"], extra)
                    self.assertAlmostEqual(r["job_netto"], 600.0 * (r["job_wochen"] + extra))
                else:
                    self.assertEqual(r["job_netto"], 0.0)

    def test_stichtag_nur_ohne_eingereichte_app(self):
        """Mit frueh_wenn='eingereicht' endet die Jagd am Stichtag nur, wenn auch keine App im Review ist; das
        sind nie mehr Läufe als mit der Regel „keine App im Store“."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        E = dict(P, ferienjob=dict(P["ferienjob"], frueh_wenn="eingereicht"))
        n_p = n_e = 0
        for s in range(400):
            a, b = p.simulate(random.Random(s), P), p.simulate(random.Random(s), E)
            n_p += a["stichtag_stopp"]
            n_e += b["stichtag_stopp"]
            if b["stichtag_stopp"]:
                self.assertTrue(a["stichtag_stopp"])
                self.assertEqual(b["launches"], [])
        self.assertGreater(n_p, n_e)
        self.assertGreater(n_e, 0)

    # ---- Prüfung des Modells vom 25.11.2026 (abends) ----
    def test_ruhe_spart_erst_ab_kosten_ab_und_live_kostet_mindestens(self):
        """Ruhezeit spart erst ab 29.03.; mit App im Store gilt im Abitur mindestens monat_live (ohne Testgeld,
        damit keine Ausgabe vom Kassenstand abhängt)."""
        P = dict(p.SZENARIEN[self.MIT_HEBELN], build_first=(30, 60, 200), signal=None, test_cap=0.0,
                 kein_testgeld=True)
        FR = P["fix_ruhe"]
        frueh = dict(P, fix_ruhe=dict(FR, kosten_ab=FR["von"]))
        ohne_live = dict(P, fix_ruhe=dict(FR, monat_live=None))
        von = p.woche_ab(FR["von"])
        n_ruhe = n_live = 0
        for s in range(400):
            a = p.simulate(random.Random(s), P)
            b = p.simulate(random.Random(s), frueh)
            c = p.simulate(random.Random(s), ohne_live)
            if a["squeeze"] or b["squeeze"] or c["squeeze"]:
                continue                       # gedrosseltes Wachstum: Ergebnis hängt dann am Kassenstand
            # profit_firma statt ergebnis: die Krankenversicherung springt an einer Gewinngrenze
            if a["launches"] and a["launches"][0] < von:
                self.assertAlmostEqual(b["profit_firma"], a["profit_firma"])          # keine Ruhe: kosten_ab egal
                self.assertGreaterEqual(c["profit_firma"], a["profit_firma"] - 1e-9)  # monat_live kostet
                self.assertLessEqual(c["profit_firma"] - a["profit_firma"], 12 * FR["monat_live"] / p.WPM + 1e-6)
                n_live += c["profit_firma"] > a["profit_firma"] + 1.0
            elif a["einreichung1"] is None or a["einreichung1"] >= von:
                self.assertGreaterEqual(b["profit_firma"], a["profit_firma"] - 1e-9)  # Ruhe ab 15.03. spart mehr
                n_ruhe += b["profit_firma"] > a["profit_firma"] + 1.0
        self.assertGreater(n_ruhe, 50)
        self.assertGreater(n_live, 5)

    def test_bestanden_vor_der_pause_zahlt_nach_der_pause(self):
        """Vor der Startpause bestanden zählt: Wo ohne die Regel vor dem 15.03. gezahlt würde, zahlt das Modell
        oft in der Woche ab 07.06."""
        P = dict(p.SZENARIEN[self.MIT_HEBELN], build_first=(30, 45, 60), einmal_stunden=(0, 0, 0))
        alt = dict(P, signal=dict(P["signal"], creator_nach_pause=False))
        sp0, ende = p.woche_ab(P["startpause"][0]), p.woche_ab(P["startpause"][1])
        n = nach = 0
        for s in range(600):
            a = p.simulate(random.Random(s), alt)
            if any(w < sp0 and c > 0 for w, c in a["test_log"]):
                n += 1
                b = p.simulate(random.Random(s), P)
                nach += any(w == ende and c > 0 for w, c in b["test_log"])
        self.assertGreater(n, 5)
        self.assertGreaterEqual(nach, n // 4)      # ein Teil fällt bis Juni schon ab (Phase decay)

    def test_anmeldung_mit_dem_stand_vom_2706(self):
        """Das Elternteil meldet sich nur an, wenn bis So 27.06. eine App im Store war und eine App die Schwelle
        erreicht hatte."""
        P = dict(p.SZENARIEN[self.MIT_HEBELN], build_first=(30, 45, 60),
                 restwert=dict(p.RESTWERT["restwert"], p=(1, 1, 1)))
        w = p.woche_ab(date(2027, 6, 28)) - 1
        n = 0
        for s in range(600):
            r = p.simulate(random.Random(s), P)
            if r["eltern_konto"]:
                n += 1
                self.assertTrue(any(l <= w for l in r["launches"]), s)
                self.assertGreaterEqual(r["chk"][w], 100 * p.FX - 1e-9, s)
        self.assertGreater(n, 20)

    def test_uebertragung_wie_verkaufsstopp_am_0808(self):
        """Die Erlöse ab der Übertragung (Mo 09.08.) sind genau das, was ein Verkaufsstopp am So 08.08. abziehen
        würde (gleiche Läufe, die Restwert-Züge kommen erst nach der Schleife)."""
        rw = dict(p.RESTWERT["restwert"], p=(1, 1, 1), anmeldung=None)
        P = dict(p.SZENARIEN[self.MIT_HEBELN], build_first=(30, 45, 60), restwert=rw)
        Q = dict(P, restwert=None, stilllegung=dict(verkauf_bis=date(2027, 8, 8)))
        n = 0
        for s in range(600):
            a = p.simulate(random.Random(s), P)
            if a["art"] is not None and a["gestoppt"]:
                n += 1
                b = p.simulate(random.Random(s), Q)
                self.assertAlmostEqual(a["nach_uebertragung"], b["abschalt_abzug"], places=6)
        self.assertGreater(n, 10)

    def test_app2_erst_nach_der_freigabe_von_app1(self):
        """App 2 beginnt frühestens in der Woche, in der App 1 freigegeben ist (aus der Vorlage); ohne die Regel
        beginnt sie oft schon während des Reviews."""
        for name in (self.DEIN_PLAN, self.MIT_HEBELN):
            P = p.SZENARIEN[name]
            n = 0
            for s in range(500):
                r = p.simulate(random.Random(s), P)
                if r["bau2_code_w"] is not None:
                    n += 1
                    self.assertIsNotNone(r["frei1_w"], (name, s))
                    self.assertGreaterEqual(r["bau2_code_w"], r["frei1_w"], (name, s))
            self.assertGreater(n, 100, name)
        ohne = dict(p.SZENARIEN[self.DEIN_PLAN], vorlage_h=None)
        frueher = 0
        for s in range(500):
            r = p.simulate(random.Random(s), ohne)
            if r["bau2_w"] is not None and (r["frei1_w"] is None or r["bau2_w"] < r["frei1_w"]):
                frueher += 1
        self.assertGreater(frueher, 50)

    def test_wochendeckel_fuer_posts(self):
        """Posts und Tests nehmen je Woche höchstens den Deckel; ohne Deckel liegen sie oft darüber."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        eng = dict(P, post_deckel=(1.5, 1.5))
        ohne = dict(P, post_deckel=None)
        ueber = 0
        for s in range(300):
            self.assertLessEqual(p.simulate(random.Random(s), P)["post_max"], P["post_deckel"][1] + 1e-9)
            self.assertLessEqual(p.simulate(random.Random(s), eng)["post_max"], 1.5 + 1e-9)
            ueber += p.simulate(random.Random(s), ohne)["post_max"] > 10.0
        self.assertGreater(ueber, 50)

    def test_vorentscheidung_am_2506(self):
        """War am Fr 25.06. (Stand Ende der Woche) eine App im Store oder im Review und ist am 04.07. keine im
        Store, beginnt der Job nur mit der kurzfristigen Zeitarbeit am 05.07., sonst am 19.07."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        nie = dict(P, ferienjob=dict(P["ferienjob"], zeitarbeit_p=(0, 0, 0), zeitarbeit_vorlauf_p=(1, 1, 1), p=(1, 1, 1)))
        immer = dict(P, ferienjob=dict(P["ferienjob"], zeitarbeit_p=(1, 1, 1), zeitarbeit_vorlauf_p=(1, 1, 1),
                                       p=(1, 1, 1)))
        n_g = n_o = 0
        for s in range(600):
            a, b = p.simulate(random.Random(s), nie), p.simulate(random.Random(s), immer)
            self.assertEqual(a["genannt_19"], b["genannt_19"])
            if a["stichtag_stopp"]:
                if a["genannt_19"]:
                    n_g += 1
                    self.assertFalse(a["job_frueh"], s)
                    self.assertTrue(b["job_frueh"], s)
                    self.assertEqual(a["job_wochen"], p.WEEKS - p.woche_ab(date(2027, 7, 19)), s)
                else:
                    n_o += 1
                    self.assertTrue(a["job_frueh"], s)
        self.assertGreater(n_g, 20)
        self.assertGreater(n_o, 20)

    def test_kleine_nebenstunden_ziehen_stunden_ab(self):
        """Kassenprüfung ab der Gründung und Markenkonten nach einer Einreichung kosten Wochenstunden: mit sehr
        großen Werten bleibt nach der Gründung bzw. nach der ersten Einreichung nichts für den Bau."""
        P = p.SZENARIEN[self.MIT_HEBELN]
        kasse = dict(P, kasse_ab_gruendung=1000.0)
        konten = dict(P, konten_je_einreichung=1000.0)
        for s in range(200):
            r = p.simulate(random.Random(s), kasse)
            if r["gegruendet"] and r["gruendung_woche"] is not None:
                self.assertEqual(r["launches"], [], s)    # gegründet bei der Hälfte, danach keine Baustunde mehr
            self.assertLessEqual(len(p.simulate(random.Random(s), konten)["launches"]), 1, s)

    def test_spaete_gruendung_erst_nach_der_letzten_pruefung(self):
        """Ist M2 bis Mo 01.03. nicht erreicht, wird nicht vor dem Abitur gegründet, sondern in der Woche ab
        07.06."""
        P = p.SZENARIEN[self.MIT_HEBELN]
        a, b = p.woche_ab(date(2027, 3, 1)), p.woche_ab(date(2027, 6, 7))
        spaet = 0
        for s in range(800):
            r = p.simulate(random.Random(s), P)
            if r["gegruendet"] and r["gruendung_woche"] is not None:
                self.assertFalse(a < r["gruendung_woche"] < b, (s, r["gruendung_woche"]))
                spaet += r["gruendung_woche"] == b
        self.assertGreater(spaet, 5)

    # ---- Prüfung des Modells vom 25.11.2026 (spät) ----
    GEGENPROBE_ZEITARBEIT = "Hebel: DEIN PLAN, falls die Zeitarbeit ab 05.07. immer klappt (Gegenprobe)"

    def test_wochendeckel_vor_und_nach_der_pruefungszeit(self):
        """Vor dem 15.03. gilt der erste Wert des Deckels, ab dem 15.03. der zweite, auch ohne Startpause
        (Grenze aus signal_pause). Mit (1,5; 0) gibt es Posts nur in Q4."""
        for name in (self.DEIN_PLAN, self.OHNE_STARTPAUSE):
            P = dict(p.SZENARIEN[name], post_deckel=(1.5, 0.0))
            grenze = p.woche_ab((P["signal_pause"] or P["startpause"])[0])
            n_q4 = 0
            for s in range(400):
                r = p.simulate(random.Random(s), P)
                if any(l < grenze for l in r["launches"]):
                    self.assertLessEqual(r["post_max"], 1.5 + 1e-9, (name, s))
                    n_q4 += r["post_max"] > 0
                else:
                    self.assertEqual(r["post_max"], 0.0, (name, s))
            self.assertGreater(n_q4, 5, name)

    def test_app2_in_der_freigabewoche_und_mit_vorlage(self):
        """App 2 beginnt meist schon in der Woche, in der App 1 freigegeben wird; die Vorlage kostet Stunden
        (mit 5.000 Vorlagenstunden erscheint App 2 nie)."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        gross = dict(P, vorlage_h=5000.0)
        n = gleich = 0
        for s in range(400):
            r = p.simulate(random.Random(s), P)
            if r["bau2_code_w"] is not None:
                n += 1
                gleich += r["bau2_code_w"] == r["frei1_w"]
            self.assertLessEqual(len(p.simulate(random.Random(s), gross)["launches"]), 1, s)
        self.assertGreater(n, 100)
        self.assertGreater(gleich, n // 2)

    def test_vorentscheidung_mit_dem_stand_vom_2706(self):
        """genannt_19 heißt: App 1 war bis So 27.06. (Ende der Woche mit dem Fr 25.06.) eingereicht."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        w = p.woche_ab(date(2027, 6, 25))
        n_w = n_w1 = 0
        for s in range(600):
            r = p.simulate(random.Random(s), P)
            e = r["einreichung1"]
            if e is None:
                self.assertFalse(r["genannt_19"], s)
            elif e == int(e):                      # Apple-Konto schon aktiv: eingereicht in Woche e
                self.assertEqual(r["genannt_19"], e <= w, (s, e))
                n_w += e == w
                n_w1 += e == w + 1
        self.assertGreater(n_w, 5)
        self.assertGreater(n_w1, 5)
        fj = p.FERIENJOB_FRUEH["ferienjob"]
        self.assertEqual(fj["vorentscheid"], date(2027, 6, 25))
        self.assertEqual(fj["zeitarbeit_p"], (0.3, 0.5, 0.7))
        self.assertEqual(fj["zeitarbeit_vorlauf_p"], (0.5, 0.7, 0.85))

    def test_zeitarbeit_mit_vorlauf_ohne_nennung(self):
        """Ohne Nennung des 19.07. gibt es den frühen Beginn nur über Zeitarbeit mit Vorlauf (06, 2.4)."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        nie = dict(P, ferienjob=dict(P["ferienjob"], zeitarbeit_vorlauf_p=(0, 0, 0), zeitarbeit_p=(1, 1, 1), p=(1, 1, 1)))
        n = 0
        for s in range(600):
            r = p.simulate(random.Random(s), nie)
            if r["stichtag_stopp"]:
                if r["genannt_19"]:
                    self.assertTrue(r["job_frueh"], s)
                else:
                    n += 1
                    self.assertFalse(r["job_frueh"], s)
        self.assertGreater(n, 20)

    def test_kasse_erst_ab_der_gruendung_und_nur_bis_zum_start(self):
        """Die Kassenprüfung ändert vor der Gründung nichts (gleiche Gründungswoche); nach dem ersten Start steckt
        sie in pflege_h_woche (mit Gründung erst bei fertiger App 1 erscheint App 2 trotz 1.000 h Kasse)."""
        P = p.SZENARIEN[self.MIT_HEBELN]
        kasse = dict(P, kasse_ab_gruendung=1000.0)
        n_g = 0
        for s in range(300):
            a, b = p.simulate(random.Random(s), P), p.simulate(random.Random(s), kasse)
            self.assertEqual(b["gruendung_woche"], a["gruendung_woche"], s)
            n_g += b["gegruendet"]
        self.assertGreater(n_g, 250)
        fertig = dict(kasse, gruendung=dict(P["gruendung"], bei=1.0, spaet=None))
        n2 = sum(len(p.simulate(random.Random(s), fertig)["launches"]) >= 2 for s in range(300))
        self.assertGreater(n2, 10)

    def test_nebenaufgaben_nur_an_montagen(self):
        """nebenstunden() liest die Liste nur mit dem Montag der Woche: andere Tage fielen still weg."""
        for liste in (p.NEBEN_NI, p.NEBEN_PLAN):
            self.assertEqual([d for d in liste if d.weekday() != 0], [])

    def test_gruendung_in_der_woche_ab_0103_noch_erlaubt(self):
        """M2 bis So 28.02. erreicht: Gründung in der Woche ab Mo 01.03. ist noch erlaubt (03, Zeile Mo 01.03.)."""
        P = p.SZENARIEN[self.MIT_HEBELN]
        w = p.woche_ab(date(2027, 3, 1))
        n = sum(p.simulate(random.Random(s), P)["gruendung_woche"] == w for s in range(800))
        self.assertGreater(n, 3)

    def test_spaete_gruendung_am_tag_nach_der_letzten_pruefung(self):
        """Im späten Fall wird in der Woche ab 07.06. gegründet, auch wenn App 1 noch nicht zur Hälfte steht; später
        wird nie gegründet."""
        P = p.SZENARIEN[self.MIT_HEBELN]
        b = p.woche_ab(date(2027, 6, 7))
        for s in range(800):
            r = p.simulate(random.Random(s), P)
            if r["gegruendet"] and r["gruendung_woche"] is not None:
                self.assertLessEqual(r["gruendung_woche"], b, s)

    def test_verkauf_nur_mit_acht_vollen_wochen(self):
        """Eine einzige App, keine Schwellen, Verkauf sicher: verkauft wird genau dann, wenn sie bis So 13.06. (Woche
        ab 07.06.) startet. Ein Start in der Woche ab 14.06. ist am So 08.08. keine acht vollen Wochen im Store."""
        rw = dict(p.RESTWERT["restwert"], min_monat=-1e12, anmeldung=None,
                  verkauf=dict(p.RESTWERT["restwert"]["verkauf"], ab_umsatz_usd=0, p=(1, 1, 1)))
        P = dict(p.SZENARIEN[self.MIT_HEBELN], n_attempts=(1, 1), restwert=rw)
        grenze = p.woche_ab(date(2027, 6, 7))
        stand = p.bis_woche(date(2027, 8, 7))
        n = {}
        for s in range(600):
            r = p.simulate(random.Random(s), P)
            if r["launches"] and r["launches"][0] <= stand and r["exit"] == 0:
                w = r["launches"][0]
                self.assertEqual(r["art"] == "verkauf", w <= grenze, (s, w, r["art"]))
                n[w] = n.get(w, 0) + 1
        self.assertGreater(n.get(grenze, 0), 5)
        self.assertGreater(n.get(grenze + 1, 0), 5)

    def test_zweite_pruefung_auch_ohne_startpause(self):
        """Ohne Startpause gilt die zweite Signalprüfung (Woche ab 28.06.) weiter für Apps mit Start vor dem 15.03.
        (Prüfungszeit aus signal_pause); die erste Abweichung ist eine Zahlung genau in dieser Woche."""
        mit = dict(p.SZENARIEN[self.OHNE_STARTPAUSE], build_first=(30, 45, 60))
        ohne = dict(mit, signal=dict(mit["signal"], zweite=None))
        w2 = p.woche_ab(date(2027, 6, 28))
        n = 0
        for s in range(1500):
            a = p.simulate(random.Random(s), ohne)["test_log"]
            b = p.simulate(random.Random(s), mit)["test_log"]
            for x, y in zip(a + [None], b):
                if x != y:
                    n += 1
                    self.assertEqual(y[0], w2, (s, x, y))
                    break
        self.assertGreater(n, 0)

    def test_gegenprobe_zeitarbeit_bleibt_gepaart(self):
        """Die Gegenprobe „Zeitarbeit klappt immer“ zieht dieselben Zufallszahlen wie DEIN PLAN: gleiche Starts und
        Spitzen in jedem Lauf, nur der Jobbeginn ändert sich."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        G = p.SZENARIEN[self.GEGENPROBE_ZEITARBEIT]
        n = 0
        for s in range(600):
            a, b = p.simulate(random.Random(s), P), p.simulate(random.Random(s), G)
            self.assertEqual((a["launches"], a["peaks"]), (b["launches"], b["peaks"]), s)
            n += a["job_frueh"] != b["job_frueh"]
        self.assertGreater(n, 20)

    def test_umsatzabhaengige_kosten_nach_dem_plan(self):
        """Bis 100.000 USD MRR kostet jeder Euro Umsatz nur c_organisch: Läufe mit kleinen Apps, ohne Testgeld und ohne
        gedrosseltes Wachstum, haben mit 0 % nie weniger Gewinn als mit 50 %; im Mittel deutlich mehr."""
        basis = dict(p.SZENARIEN[self.MIT_HEBELN], signal=None, test_cap=0.0, kein_testgeld=True)
        null, halb = dict(basis, c_organisch=(0.0, 0.0, 0.0)), dict(basis, c_organisch=(0.5, 0.5, 0.5))
        n = 0
        summe = 0.0
        for s in range(400):
            a, b = p.simulate(random.Random(s), null), p.simulate(random.Random(s), halb)
            summe += a["profit_firma"] - b["profit_firma"]
            if a["launches"] and a["max_mrr"] < 5000 * p.FX and not a["squeeze"] and not b["squeeze"]:
                n += 1
                self.assertGreaterEqual(a["profit_firma"], b["profit_firma"] - 1e-9, s)
        self.assertGreater(n, 100)
        self.assertGreater(summe / 400, 10.0)
        self.assertEqual(p.AUFWAND_PLAN["c_organisch"], (0.15, 0.18, 0.20))

    def test_vorbereitung_der_posts_nach_der_einreichung(self):
        """V1–V4 kosten Stunden erst nach der Einreichung von App 1: mit sehr großem Wert bleibt danach nichts für
        App 2, vorher ändert sich nichts."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        gross = dict(P, vorb_nach_einreichung1=1000.0)
        for s in range(200):
            a, b = p.simulate(random.Random(s), P), p.simulate(random.Random(s), gross)
            self.assertEqual(a["einreichung1"], b["einreichung1"], s)
            self.assertLessEqual(len(b["launches"]), 1, s)

    def test_app2_im_review_vorbereiten(self):
        """Mit vorlage_vorab_h bekommt App 2 vor der Freigabe von App 1 höchstens diese Stunden (ohne Code)."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        self.assertEqual(P["vorlage_vorab_h"], 6.0)
        ohne = dict(P, vorlage_vorab_h=None)
        frueher = 0
        for s in range(400):
            r = p.simulate(random.Random(s), P)
            self.assertLessEqual(r["vorab_h"], 6.0 + 1e-9, s)
            frueher += r["bau2_w"] is not None and r["frei1_w"] is not None and r["bau2_w"] < r["frei1_w"]
            self.assertEqual(p.simulate(random.Random(s), ohne)["vorab_h"], 0.0)
        self.assertGreater(frueher, 20)

    # ---- Prüfung des Modells vom 25.11.2026 (nachts): Altlasten aus dem 500k-Modell ----
    ALTE_KOSTEN = "Hebel: DEIN PLAN mit den alten umsatzabhängigen Kosten (Werbung aus dem Umsatz wie im 500k-Modell, Gegenprobe)"

    def test_gegenprobe_alte_kosten_genau_und_gepaart(self):
        """Die Gegenprobe zieht c_organisch wie DEIN PLAN (gleicher Zufallsstrom), benutzt es aber nicht."""
        G = p.SZENARIEN[self.ALTE_KOSTEN]
        self.assertTrue(G["c_organisch_aus"])
        self.assertEqual(G["c_organisch"], p.AUFWAND_PLAN["c_organisch"])
        for s in range(200):
            a = p.simulate(random.Random(s), dict(G, c_organisch=(0.1, 0.2, 0.3)))
            b = p.simulate(random.Random(s), dict(G, c_organisch=(0.5, 0.6, 0.7)))
            self.assertEqual(a, b, s)

    def test_unter_100000_usd_zaehlt_nur_c_organisch(self):
        """Bis 100.000 USD MRR je App gilt nur c_organisch, in jeder Phase: Andere c_early/c_plateau ändern einen Lauf
        nicht, solange keine App so groß wird; mit der alten Schwelle (5.000 USD) kosten sie darüber wieder."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        teuer = {"c_early": (0.6, 0.7, 0.8), "c_plateau": (0.6, 0.7, 0.8)}
        n = 0
        for s in range(400):
            a, b = p.simulate(random.Random(s), P), p.simulate(random.Random(s), dict(P, **teuer))
            if a["max_mrr"] < 100000 * p.FX:
                n += 1
                self.assertEqual(a["ergebnis_dein"], b["ergebnis_dein"], s)
        self.assertGreater(n, 390)
        gross = dict(P, force_first_peak=20000.0, force_m0=6000.0, c_organisch_bis_usd=5000.0)
        n_ueber = n_anders = 0
        for s in range(150):
            a, b = p.simulate(random.Random(s), gross), p.simulate(random.Random(s), dict(gross, **teuer))
            if 5000 * p.FX <= a["max_mrr"] < 20000 * p.FX:
                n_ueber += 1
                n_anders += a["profit_firma"] > b["profit_firma"]
        self.assertGreater(n_ueber, 20)
        self.assertGreater(n_anders, 0.9 * n_ueber)

    def test_vorbereitung_mit_winziger_kappe_wie_ohne(self):
        """Die Vorbereitung von App 2 zieht keine Zufallszahl: Mit einer Kappe von 1e-9 h rechnet jeder Lauf wie ganz
        ohne Vorbereitung (bis auf die Prüfgrößen der Vorbereitung)."""
        P = dict(p.SZENARIEN[self.DEIN_PLAN], vorlage_vorab_h=None)
        Q = dict(P, vorlage_vorab_h=1e-9)
        for s in range(400):
            a, b = p.simulate(random.Random(s), P), p.simulate(random.Random(s), Q)
            for k in a:
                if k not in ("bau2_w", "vorab_h", "offene_versuche", "attempts"):
                    self.assertEqual(a[k], b[k], (s, k))

    def test_app2_vorbereitung_bis_zur_kappe(self):
        """Die Vorbereitung im Review erreicht oft ihre Kappe und geht nie darüber."""
        for kappe in (6.0, 0.5):
            P = dict(p.SZENARIEN[self.DEIN_PLAN], vorlage_vorab_h=kappe)
            voll = 0
            for s in range(300):
                r = p.simulate(random.Random(s), P)
                self.assertLessEqual(r["vorab_h"], kappe + 1e-9, s)
                voll += abs(r["vorab_h"] - kappe) < 1e-9
            self.assertGreater(voll, 100, kappe)

    def test_v1_v4_nur_bei_app1(self):
        """V1–V4 fallen nur nach der Einreichung von App 1 an, nicht bei jeder Einreichung."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        k, v = P["konten_je_einreichung"], P["vorb_nach_einreichung1"]
        B = dict(P, konten_je_einreichung=k + v, vorb_nach_einreichung1=0.0)
        n_eine = n_anders = 0
        for s in range(400):
            a, b = p.simulate(random.Random(s), P), p.simulate(random.Random(s), B)
            if len(a["launches"]) <= 1 and a["attempts"] <= 1:
                n_eine += 1
                self.assertEqual(a["ergebnis_dein"], b["ergebnis_dein"], s)
            n_anders += a["ergebnis_dein"] != b["ergebnis_dein"]
        self.assertGreater(n_eine, 50)
        self.assertGreater(n_anders, 5)

    def test_vergleich_nur_ferienjob_ohne_gruendung(self):
        """In den Vergleichen ohne App wird nie gegründet, und die App bringt und kostet nichts."""
        for k in [k for k in p.SZENARIEN if k.startswith("Hebel: nur Ferienjob")]:
            for s in range(100):
                r = p.simulate(random.Random(s), p.SZENARIEN[k])
                self.assertFalse(r["gegruendet"], (k, s))
                self.assertEqual(r["ergebnis_app"], 0.0, (k, s))

    def test_ohne_posts_sinkt_der_umsatz_in_der_pruefungszeit(self):
        """In der Prüfungszeit gibt es keine Posts: Der Umsatz der vorher gestarteten Apps sinkt bis zum Ende der Pause;
        ohne die Regel steigt er oft."""
        P = dict(p.SZENARIEN[self.DEIN_PLAN], build_first=(30, 45, 60))
        ohne = dict(P, ohne_posts=None)
        n = steigt = 0
        for s in range(400):
            r = p.simulate(random.Random(s), P)
            if r["umsatz_vor_pause"]:
                n += 1
                self.assertLess(r["umsatz_nach_pause"], r["umsatz_vor_pause"], s)
            q = p.simulate(random.Random(s), ohne)
            steigt += bool(q["umsatz_vor_pause"]) and q["umsatz_nach_pause"] > q["umsatz_vor_pause"]
        self.assertGreater(n, 100)
        self.assertGreater(steigt, 30)

    def test_schnittliste_am_stunden_messpunkt(self):
        """Mit der Schnittliste ist App 1 nie später eingereicht als ohne; sie greift nur bei langsamem Durchstich."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        ohne = dict(P, schnitt_mp=None, v11_h=0.0)
        n = 0
        for s in range(400):
            a, b = p.simulate(random.Random(s), P), p.simulate(random.Random(s), ohne)
            if a["einreichung1"] is not None and b["einreichung1"] is not None:
                self.assertLessEqual(a["einreichung1"], b["einreichung1"], s)
            n += a["schnitt"]
            self.assertFalse(b["schnitt"], s)
        self.assertGreater(n, 150)
        self.assertLess(n, 350)

    def test_familienversicherung_nach_dem_jahresgewinn(self):
        """Beiträge zur Krankenversicherung gibt es nur, wenn der Gewinn des Jahres über 12 x 590 EUR liegt."""
        P = p.SZENARIEN[self.DEIN_PLAN]
        for s in range(400):
            r = p.simulate(random.Random(s), P)
            if r["kv_kosten"] > 0:
                self.assertGreater(r["profit_firma"] - r["abschalt_abzug"] - r["nach_uebertragung"], 12 * 590.0, s)

    def test_tarifbetrieb_fruehe_wochen_ueber_zeitarbeit(self):
        """Im Tarifbetrieb-Szenario zählen die zwei frühen Wochen ab 05.07. als Zeitarbeit."""
        P = p.SZENARIEN["Hebel: DEIN PLAN, falls ein Tarifbetrieb ab 19.07. zusagt (Bewerbung nach 06, 2.3)"]
        n = 0
        for s in range(400):
            r = p.simulate(random.Random(s), P)
            if r["job_wochen"]:
                self.assertEqual(r["job_frueh_w"], 2 if r["job_frueh"] else 0, s)
                n += r["job_frueh_w"] > 0
        self.assertGreater(n, 20)

    def test_exit_in_den_plan_szenarien_abgeschaltet(self):
        """Verkauft wird nur über restwert (06, 5), nie über den alten Verkauf der Firma."""
        for k, P in p.SZENARIEN.items():
            if k.startswith("Hebel:") and P["neben"] is p.NEBEN_PLAN:
                self.assertEqual(P["exit_min_age_weeks"], p.WEEKS + 1, k)

if __name__ == "__main__":
    unittest.main()
