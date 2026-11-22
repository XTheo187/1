"""Tests für plan/hebel_2027.py - Hebel-Wege gegen den Job-Weg bis 31.08.2027."""

from __future__ import annotations

import random
import sys
import unittest
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plan"))

import hebel_2027 as h  # noqa: E402
import verdienst_2027 as v  # noqa: E402


class Nichts(h.Option):
    name, kurz = "nichts", "nichts"

    def ziehen(self, rng, basis, zustand):
        return h.Ergebnis(v.Zusatz(), 0.0, 0.0)


class NurStunden(h.Option):
    name, kurz = "nur Stunden", "stunden"

    def ziehen(self, rng, basis, zustand):
        return h.Ergebnis(v.Zusatz(stunden=((h.PH_JAN, 40.0), (h.PH_DEZ, 10.0))), 0.0, 50.0)


class TestZusatzImJobModell(unittest.TestCase):
    def test_ohne_zusatz_unveraendert(self):
        """Der Standardaufruf zieht dieselben Zufallszahlen wie vorher (Dokumentzahlen bleiben)."""
        a = v.Annahmen()
        for s in range(200):
            e1 = v.ein_verlauf(random.Random(s), a)
            e2 = v.ein_verlauf(random.Random(s), a, None)
            self.assertEqual(e1["netto"], e2["netto"])

    def test_gleiche_zufallszahlen_mit_und_ohne_zusatz(self):
        """Ein leerer Zusatz und einer mit verdrängten Stunden teilen sich Weg, Satz und Sommer."""
        a = v.Annahmen()
        for s in range(300):
            b = v.ein_verlauf(random.Random(s), a, v.Zusatz())
            m = v.ein_verlauf(random.Random(s), a, v.Zusatz(stunden=((h.PH_JAN, 60.0),)))
            self.assertEqual((b["dual"], b["start"], b["industrie"]), (m["dual"], m["start"], m["industrie"]))
            somm = [k for k in b["je_quelle"] if k.startswith("Sommerjob")]
            for k in somm:
                self.assertAlmostEqual(b["je_quelle"][k], m["je_quelle"][k], places=6)
            self.assertLessEqual(m["stunden"], b["stunden"] + 1e-6)

    def test_verdraengte_stunden_kosten_geld(self):
        r = h.auswerten(NurStunden(), 1_500)
        self.assertLessEqual(r["mehr_p90"], 1e-6)
        self.assertLess(r["mehr_mittel"], 0)
        null = h.auswerten(Nichts(), 500)
        self.assertEqual((null["mehr_p10"], null["mehr_p90"]), (0.0, 0.0))

    def test_ohne_sommerjob(self):
        a = replace(v.Annahmen(), p_dual=0.0)
        for s in range(100):
            m = v.ein_verlauf(random.Random(s), a, v.Zusatz(sommer_anteil=0.0))
            self.assertFalse(any(k.startswith("Sommerjob") for k in m["je_quelle"]))
            self.assertEqual(m["kontostand"], m["kontostand_ohne_augustlohn"])

    def test_spaeter_beginn_zahlt_august(self):
        """Beginnt der Sommerjob nach einem Abbruch später, liegt sein Lohn im August, nicht im Juni."""
        a = replace(v.Annahmen(), p_dual=0.0)
        m = v.ein_verlauf(random.Random(5), a, v.Zusatz(sommer_anteil=0.3, sommer_teilzeit=False))
        self.assertGreater(m["kontostand"] - m["kontostand_ohne_augustlohn"], 0)
        voll = v.ein_verlauf(random.Random(5), a, v.Zusatz())
        k_voll = voll["kalendertage_kurzfristig"][2027]
        self.assertLess(m["kalendertage_kurzfristig"][2027], k_voll)

    def test_samstage_anteilig(self):
        # berufsmäßig (keine Tagesgrenze) und 7,5 h/Tag: 6 x 7,5 h bleibt unter 48 h je Woche
        a = replace(v.Annahmen(), p_dual=1.0, start_dual=(("01.09.", 1.0),), samstage=(1.0, 1.0, 1.0),
                    stunden_tag=(7.5, 7.5, 7.5))
        e = [v.ein_verlauf(random.Random(2), a, v.Zusatz(sommer_samstage=x))["stunden"] for x in (1.0, 0.5, 0.0)]
        self.assertGreater(e[0], e[1])
        self.assertGreater(e[1], e[2])

    def test_gewinn_zaehlt_zur_steuer(self):
        a = replace(v.Annahmen(), p_dual=0.0)
        b = v.ein_verlauf(random.Random(9), a, v.Zusatz())
        m = v.ein_verlauf(random.Random(9), a, v.Zusatz(gewinn=((2027, 8_000.0),)))
        self.assertGreater(m["steuer"][2027], b["steuer"][2027])
        self.assertAlmostEqual(m["pruef"][2027]["selbst"], b["pruef"][2027]["selbst"] + 8_000, places=6)
        self.assertLess(m["netto"] - b["netto"], 8_000)


class TestRegeln(unittest.TestCase):
    def test_familienversicherung(self):
        a = v.Annahmen()
        grenze = 12 * a.grenze_regel[2027]
        self.assertFalse(h.famv_verloren({"selbst": grenze, "mini": 0.0, "mini_monate": 0.0}, a))
        self.assertTrue(h.famv_verloren({"selbst": grenze + 1, "mini": 0.0, "mini_monate": 0.0}, a))
        # mit Minijob: Minijob/Monat + Gewinn/12 <= 633
        self.assertFalse(h.famv_verloren({"selbst": 1_200.0, "mini": 500.0 * 5, "mini_monate": 5.0}, a))
        self.assertTrue(h.famv_verloren({"selbst": 1_800.0, "mini": 500.0 * 5, "mini_monate": 5.0}, a))

    def test_kv_nur_bei_verlust_der_familienversicherung(self):
        rng = random.Random(1)
        self.assertEqual(h.kv_kosten(rng, False, True, h.KV()), (0.0, 0.0))
        bis, danach = h.kv_kosten(rng, True, True, h.KV())
        self.assertGreater(bis, 4 * 250)
        self.assertGreater(danach, 0)

    def test_dreieck_quantil(self):
        self.assertAlmostEqual(h.dreieck_quantil((0, 0.5, 1), 0.5), 0.5)
        self.assertAlmostEqual(h.dreieck_quantil((0, 0.5, 1), 0.0), 0.0)
        self.assertAlmostEqual(h.dreieck_quantil((0, 0.5, 1), 1.0), 1.0)
        rng = random.Random(4)
        xs = sorted(h.dreieck_quantil((9, 26, 40), rng.random()) for _ in range(20_000))
        self.assertAlmostEqual(sum(xs) / len(xs), 25.0, delta=0.3)

    def test_kombination_nur_ein_sommer(self):
        k = h.Kombination("x", "x", (h.WebSommer(None), h.Umzug(stufenplan=False)))
        with self.assertRaises(ValueError):
            h.auswerten(k, 50)


class TestOptionen(unittest.TestCase):
    def test_alle_optionen_laufen(self):
        for o in h.optionen():
            r = h.auswerten(o, 300)
            self.assertLessEqual(r["p10"], r["median"])
            self.assertLessEqual(r["median"], r["p90"])
            self.assertGreaterEqual(r["p_besser"], 0.0)
            self.assertLessEqual(r["p_besser"], 1.0)

    def test_stufenplan_begrenzt_das_risiko(self):
        """Mit Frühindikator fällt der schlechte Rand weniger tief als ohne."""
        ohne = h.auswerten(h.WebSommer(None), 1_500)
        mit = h.auswerten(h.WebSommer(1_500.0), 1_500)
        self.assertGreater(mit["mehr_p10"], ohne["mehr_p10"])
        ohne = h.auswerten(h.Umzug(stufenplan=False), 1_500)
        mit = h.auswerten(h.Umzug(stufenplan=True), 1_500)
        self.assertGreater(mit["mehr_p10"], ohne["mehr_p10"])

    def test_no_go_aendert_nur_die_testkosten(self):
        """Web-Stufenplan ohne Go: genau der Job-Weg (das Webgeschäft im Schuljahr läuft ohnehin)."""
        o = h.WebSommer(10 ** 9)
        for i in range(200):
            r = h.vergleich(o, i)
            self.assertFalse(r["go"])
            self.assertEqual(r["mehr"], 0.0)


if __name__ == "__main__":
    unittest.main()
