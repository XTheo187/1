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
        for p_dual in (0.0, 1.0):
            a = replace(v.Annahmen(), p_dual=p_dual)
            rng = random.Random(3)
            for _ in range(2_000):
                e = v.ein_verlauf(rng, a)
                for jahr in (2026, 2027):
                    p = e["pruef"][jahr]
                    # Familienversicherung: Gewinn / 12 unter 565/590; mit Minijob Minijob + Gewinn / 12 unter 603/633
                    if p["mini"] > 1e-9:
                        self.assertLessEqual(p["mini"] / p["mini_monate"] + p["selbst"] / 12,
                                             a.grenze_minijob[jahr] + 1e-6)
                    else:
                        self.assertLessEqual(p["selbst"], 12 * a.grenze_regel[jahr] + 1e-6)
                    # Rentenversicherung: Nachhilfe-Gewinn höchstens 603/633 EUR je Monat
                    if p["nachhilfe"] > 0:
                        self.assertLessEqual(p["nachhilfe"], a.grenze_minijob[jahr] * p["nachhilfe_monate"] + 1e-6)
                    # Übungsleiterpauschale
                    self.assertLessEqual(p["frei"], a.uebungsleiter_frei + 1e-6)
                    # Kurzfristige Beschäftigung: 70 Arbeitstage oder 90 Kalendertage je Kalenderjahr
                    self.assertTrue(p["arbeitstage"] <= a.tage_kurzfristig + 1e-6
                                    or p["kalendertage"] <= a.kalendertage_kurzfristig + 1e-6)

    def test_sozialabgaben_nur_nach_dem_zeugnis(self):
        """Schülerjobs bis zum Zeugnis sind SV-frei; vor dualem Studium nur Sommerjob und Vergütung."""
        a = replace(v.Annahmen(), p_dual=1.0)
        rng = random.Random(8)
        for _ in range(500):
            e = v.ein_verlauf(rng, a)
            nach_zeugnis = sum(x for k, x in e["je_quelle"].items()
                               if k.startswith(("Sommerjob", "Ausbildungsvergütung")))
            self.assertAlmostEqual(e["sv"], a.sv_berufsmaessig * nach_zeugnis, places=6)
        fh = v.ein_verlauf(random.Random(8), replace(v.Annahmen(), p_dual=0.0))
        self.assertEqual(fh["sv"], 0.0)

    def test_familienversicherung_rechnet_den_jahresgewinn(self):
        """Gewinn aus dem Webgeschäft darf über die Monate verteilt bis 12 x 590 EUR gehen."""
        o = v.obergrenze()
        self.assertGreater(o["pruef"][2027]["selbst"], 6 * 590)
        self.assertLessEqual(o["pruef"][2027]["selbst"], 12 * 590 + 1e-6)

    def test_einbehaltene_lohnsteuer_fehlt_am_31_august(self):
        r = v.auswerten(3_000, a=replace(v.Annahmen(), p_dual=0.0))
        self.assertGreater(r["einbehalten_median"], 500)
        self.assertLess(r["kontostand_median"], r["median"])
        # kurze Ferienjobs: Tagestabelle behält mehr ein als die Monatstabelle
        self.assertGreater(v.lohnsteuer(740, 5, 2027), 5 / 30 * v.lohnsteuer(740, 30, 2027))
        self.assertEqual(v.lohnsteuer(1_000, 30, 2027), 0.0)

    def test_jobtage_vor_dem_zeugnis_bringen_mehr(self):
        mit = v.auswerten(3_000)
        ohne = v.auswerten(3_000, a=v.ohne_jobtage_mai_juni(v.Annahmen()))
        self.assertGreater(mit["median"], ohne["median"])

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
