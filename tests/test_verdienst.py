"""Tests für plan/verdienst_2027.py - maximaler Verdienst bis 31.08.2027."""

from __future__ import annotations

import random
import sys
import unittest
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plan"))

import verdienst_2027 as v  # noqa: E402


class TestVerdienst(unittest.TestCase):
    def test_reihenfolge_der_kennzahlen(self):
        r = v.auswerten(3_000)
        o = v.obergrenze()
        self.assertGreater(r["p10"], 0)
        self.assertLess(r["p10"], r["median"])
        self.assertLess(r["median"], r["p90"])
        self.assertLessEqual(r["p99"], o["netto"])

    def test_regeln_werden_eingehalten(self):
        a = v.Annahmen()
        rng = random.Random(3)
        monate = {2026: sum(p.monate for p in a.phasen if p.jahr == 2026),
                  2027: sum(p.monate for p in a.phasen if p.jahr == 2027)}
        for _ in range(2_000):
            e = v.ein_verlauf(rng, a)
            for jahr in (2026, 2027):
                # Familienversicherung: regelmäßiges Einkommen unter der (Minijob-)Grenze
                self.assertLessEqual(e["regelmaessig"][jahr], a.grenze_minijob[jahr] * monate[jahr] + 1e-6)
                # Kurzfristige Beschäftigung: höchstens 70 Arbeitstage je Kalenderjahr
                self.assertLessEqual(e["tage_kurzfristig"][jahr], a.tage_kurzfristig + 1e-6)

    def test_duales_studium_danach_kostet_abgaben(self):
        fh = v.auswerten(3_000, a=replace(v.Annahmen(), p_dual=0.0))
        dual = v.auswerten(3_000, a=replace(v.Annahmen(), p_dual=1.0))
        self.assertGreater(fh["median"], dual["median"])

    def test_sommerjob_ist_der_groesste_hebel(self):
        ohne = v.auswerten(3_000, a=replace(v.Annahmen(), mit_kurzfristig=False))
        mit = v.auswerten(3_000)
        self.assertGreater(mit["median"], 2 * ohne["median"])

    def test_mehr_wochenstunden_erhoehen_die_obergrenze(self):
        o48 = v.obergrenze()
        o60 = v.obergrenze(replace(v.Annahmen(), max_stunden_woche=60.0))
        self.assertGreater(o60["netto"], o48["netto"])


if __name__ == "__main__":
    unittest.main()
