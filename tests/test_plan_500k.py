"""Tests für plan/plan_500k.py - App-Weg zu 500.000 EUR bis 31.08.2027."""

from __future__ import annotations

import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plan"))

import plan_500k as p  # noqa: E402


class TestPlan500k(unittest.TestCase):
    def test_kalender(self):
        """Wochen bis 31.08.2027, Abiturphasen mit wenig Stunden."""
        self.assertEqual(p.WEEKS, 39)
        lv = {k: (k, k, k) for k in ("h_school", "h_holiday", "h_abiprep", "h_abi", "h_oral", "h_gap", "h_full")}
        from datetime import date
        self.assertEqual(p.hours_level(date(2027, 4, 26), lv)[0], "h_abi")       # schriftliches Abitur
        self.assertEqual(p.hours_level(date(2026, 12, 28), lv)[0], "h_holiday")   # Weihnachtsferien
        self.assertEqual(p.hours_level(date(2027, 7, 5), lv)[0], "h_full")        # Sommer

    def test_spitzen_mrr_stufen(self):
        """Die latente Spitzen-MRR trifft die vorgegebenen Stufenwahrscheinlichkeiten."""
        rng = random.Random(1)
        n = 200_000
        werte = [p.draw_peak(rng, 0.25, 0.07, 0.2, 0.12, 1.5) for _ in range(n)]
        self.assertAlmostEqual(sum(x >= 1_000 for x in werte) / n, 0.25, delta=0.005)
        self.assertAlmostEqual(sum(x >= 10_000 for x in werte) / n, 0.07, delta=0.003)
        self.assertAlmostEqual(sum(x >= 100_000 for x in werte) / n, 0.014, delta=0.002)
        self.assertLessEqual(max(werte), 5e6)

    def test_ergebnis_im_rahmen(self):
        r = p.auswerten(p.SZENARIEN[next(k for k in p.SZENARIEN if k.startswith("DER PLAN"))], 3_000)
        for k in ("p_ziel", "p_gewinn", "p_verkauf", "p_papier"):
            self.assertGreaterEqual(r[k], 0.0)
            self.assertLessEqual(r[k], 1.0)
        self.assertLessEqual(r["p_ziel"], r["p_papier"])
        self.assertLess(r["gewinn_median"], 0)          # der Normalfall: kleiner Verlust
        self.assertLessEqual(r["gewinn_p10"], r["gewinn_median"])
        self.assertLessEqual(r["gewinn_median"], r["gewinn_p90"])

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

    def test_meilensteine(self):
        r = p.auswerten(p.SZENARIEN["Strengere Quoten (Gegenprüfung)"], 3_000)
        ms = {(m["bis"], m["mrr_usd"]): m for m in r["meilensteine"]}
        # Derselbe Umsatz ist bis zu einem späteren Datum mindestens so oft erreicht
        self.assertGreaterEqual(ms[("28.02.", 5_000)]["p"], ms[("31.01.", 5_000)]["p"])
        self.assertGreaterEqual(ms[("31.03.", 10_000)]["p"], ms[("28.02.", 10_000)]["p"])
        # Eine höhere Schwelle bis zum selben Datum seltener
        self.assertLessEqual(ms[("31.03.", 30_000)]["p"], ms[("31.03.", 10_000)]["p"])


if __name__ == "__main__":
    unittest.main()
