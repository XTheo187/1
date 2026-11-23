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

    def test_gruenderin_traegt_den_verlust(self):
        """Der Partner bringt kein Geld ein: Bei Verlust verliert die Gründerin mindestens den Firmenverlust."""
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
        P = p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("Obergrenze"))]
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


if __name__ == "__main__":
    unittest.main()
