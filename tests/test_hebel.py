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


class TestPruefbefunde(unittest.TestCase):
    def test_ueberlauf_wird_berechnet(self):
        a = v.Annahmen()
        e = v.ein_verlauf(random.Random(3), a, v.Zusatz(stunden=((h.PH_JAN, 10_000.0),)))
        self.assertGreater(e["ueberlauf"][h.PH_JAN], 9_000)
        z, rest = h._ueberlauf_verteilen(v.Zusatz(), {h.PH_JAN: 100.0})
        self.assertEqual(z.ferientage, ((h.PH_FRUEH, 5.0),))
        self.assertAlmostEqual(rest, 60.0)

    def test_web_sortierung_beim_erwartungswert(self):
        o = h.WebSommer("abends")
        a = v.Annahmen()
        for i in range(30):
            a_lauf, _ = o.vorbereiten(random.Random(i), a)
            web = next(r for r in a_lauf.regelmaessig if r.name == h.WEB)
            self.assertAlmostEqual(web.sortier_satz, v._mitte(next(r for r in a.regelmaessig if r.name == h.WEB).satz))

    def test_teilzeit_behaelt_samstage(self):
        a = replace(v.Annahmen(), p_dual=1.0, start_dual=(("01.09.", 1.0),), samstage=(1.0, 1.0, 1.0),
                    stunden_tag=(7.5, 7.5, 7.5))
        voll = v.ein_verlauf(random.Random(2), a, v.Zusatz())["sommer_lohn_monate"]
        teil = v.ein_verlauf(random.Random(2), a, v.Zusatz(sommer_anteil=0.6))["sommer_lohn_monate"]
        # 3 Tage + Samstag = 4 von 6 Tagen
        self.assertAlmostEqual(sum(teil) / sum(voll), 4 / 6, places=6)

    def test_sonderausgaben_senken_die_steuer(self):
        a = replace(v.Annahmen(), p_dual=0.0)
        z = v.Zusatz(gewinn=((2027, 9_000.0),))
        ohne = v.ein_verlauf(random.Random(4), a, z)
        mit = v.ein_verlauf(random.Random(4), a, replace(z, sonderausgaben=((2027, 2_000.0),)))
        self.assertLess(mit["steuer"][2027], ohne["steuer"][2027])


class TestRegeln(unittest.TestCase):
    def test_familienversicherung(self):
        a = v.Annahmen()
        grenze = 12 * a.grenze_regel[2027]
        self.assertIsNone(h.famv_verloren({"selbst": grenze, "mini": 0.0, "mini_monate": 0.0}, a))
        self.assertEqual(h.famv_verloren({"selbst": grenze + 1, "mini": 0.0, "mini_monate": 0.0}, a), "grenze")
        # mit Minijob: Minijob/Monat + Gewinn/12 <= 633
        self.assertIsNone(h.famv_verloren({"selbst": 1_200.0, "mini": 500.0 * 5, "mini_monate": 5.0}, a))
        self.assertEqual(h.famv_verloren({"selbst": 1_800.0, "mini": 500.0 * 5, "mini_monate": 5.0}, a), "minijob")

    def test_kv_nur_bei_verlust_der_familienversicherung(self):
        kv = h.KV()
        fh = {"dual": False, "start": "01.10.", "sommer_lohn_monate": [400.0, 3_300.0, 3_300.0]}
        self.assertEqual(h.kv_kosten(random.Random(1), kv, fh, 5_000.0, None, False), (0.0, 0.0))
        # nur über die Minijob-Regel: Minijob endet vor dem Sommer, ehrliche Prognose -> keine Kosten
        self.assertEqual(h.kv_kosten(random.Random(1), kv, fh, 5_000.0, "minijob", False), (0.0, 0.0))
        # geplant: ab April, auch wenn der Gewinn am Ende unter der Grenze bleibt
        self.assertGreater(h.kv_kosten(random.Random(1), kv, fh, 5_000.0, None, True)[0], 0.0)
        bis, danach = h.kv_kosten(random.Random(1), kv, fh, 9_000.0, "grenze", True)
        mindest = 5 * 0.200 * kv.mindestbemessung
        # Studium: April bis August freiwillig, und im Juli/August ist auch der Sommerjob-Lohn beitragspflichtig
        self.assertGreater(bis, mindest + 0.2 * 6_000)
        self.assertGreater(danach, 0)

    def test_kv_dual_endet_mit_dem_berufsmaessigen_job(self):
        kv = h.KV()
        dual = {"dual": True, "start": "01.09.", "sommer_lohn_monate": [400.0, 3_300.0, 3_300.0]}
        bis, danach = h.kv_kosten(random.Random(1), kv, dual, 9_000.0, "grenze", True)
        r_max = 0.140 + 0.036 + 0.036
        # April, Mai voll, Juni zu 27/30, Juli/August pflichtversichert über den Sommerjob
        self.assertLessEqual(bis, (2 + 27 / 30) * r_max * max(kv.mindestbemessung, 9_000 / 8) + 1e-6)
        self.assertEqual(danach, 0.0)
        ohne_job = dict(dual, sommer_lohn_monate=[0.0, 0.0, 0.0])
        self.assertGreater(h.kv_kosten(random.Random(1), kv, ohne_job, 9_000.0, "grenze", True)[0], bis)
        # Beitragsbemessungsgrenze: nie mehr als 5 Monate x Satz x 6.375 EUR
        riesig = h.kv_kosten(random.Random(1), kv, ohne_job, 900_000.0, "grenze", True)[0]
        self.assertLessEqual(riesig, 5 * r_max * kv.bbg + 1e-6)

    def test_hauptberuflich_nur_bei_vollzeit(self):
        kv = h.KV()
        fh = {"dual": False, "start": "01.10.", "sommer_lohn_monate": [0.0, 0.0, 0.0]}
        # 20 h/Woche: erst über 75 % der Bezugsgröße (~3.100 EUR im Monat) hauptberuflich
        teil = [h.kv_kosten(random.Random(s), kv, fh, 4_000.0, None, False, (7, 8), 3_000.0, 20.0, 2.0)[0]
                for s in range(50)]
        self.assertEqual(max(teil), 0.0)
        voll = [h.kv_kosten(random.Random(s), kv, fh, 4_000.0, None, False, (7, 8), 3_000.0, 40.0, 2.0)[0]
                for s in range(200)]
        anteil = sum(1 for x in voll if x > 0) / len(voll)
        self.assertAlmostEqual(anteil, kv.p_hauptberuflich, delta=0.1)

    def test_dreieck_quantil(self):
        self.assertAlmostEqual(h.dreieck_quantil((0, 0.5, 1), 0.5), 0.5)
        self.assertAlmostEqual(h.dreieck_quantil((0, 0.5, 1), 0.0), 0.0)
        self.assertAlmostEqual(h.dreieck_quantil((0, 0.5, 1), 1.0), 1.0)
        rng = random.Random(4)
        xs = sorted(h.dreieck_quantil((9, 26, 40), rng.random()) for _ in range(20_000))
        self.assertAlmostEqual(sum(xs) / len(xs), 25.0, delta=0.3)

    def test_familienversicherung_mit_nachlauf(self):
        a = v.Annahmen()
        p = {"selbst": 6_000.0, "mini": 0.0, "mini_monate": 0.0}
        self.assertIsNone(h.famv_verloren(p, a))
        self.assertEqual(h.famv_verloren(p, a, nachlauf=1_500.0), "grenze")

    def test_kombination_nur_ein_sommer(self):
        k = h.Kombination("x", "x", (h.WebSommer("vollzeit"), h.Umzug(stufenplan=False)))
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
        ohne = h.auswerten(h.WebSommer("vollzeit"), 1_500)
        mit = h.auswerten(h.WebSommer("vollzeit_start"), 1_500)
        self.assertGreater(mit["mehr_p10"], ohne["mehr_p10"])
        ohne = h.auswerten(h.Umzug(stufenplan=False), 1_500)
        mit = h.auswerten(h.Umzug(stufenplan=True), 1_500)
        self.assertGreater(mit["mehr_p10"], ohne["mehr_p10"])

    def test_web_abends_laesst_den_sommerjob(self):
        o = h.WebSommer("abends")
        a = v.Annahmen()
        for i in range(100):
            rng = random.Random(i)
            a_lauf, z = o.vorbereiten(rng, a)
            basis = v.ein_verlauf(random.Random(i), a_lauf, v.Zusatz())
            e = o.ziehen(rng, basis, z)
            mit = v.ein_verlauf(random.Random(i), a_lauf, e.zusatz)
            self.assertEqual(basis["sommer_lohn_monate"], mit["sommer_lohn_monate"])
            self.assertEqual(e.hb_monate, ())

    def test_provision(self):
        a = v.Annahmen()
        f, g = h.Provision("fundraising"), h.Provision("glasfaser")
        for i in range(100):
            basis = v.ein_verlauf(random.Random(i), a, v.Zusatz())
            ef = f.ziehen(random.Random(i), basis, {})
            self.assertIsNotNone(ef.zusatz.sommer_brutto)   # angestellt: Lohn, kein Gewinn
            self.assertEqual(ef.gewinn, 0.0)
            self.assertGreaterEqual(ef.zusatz.sommer_brutto, 0.0)
            eg = g.ziehen(random.Random(i), basis, {})
            # selbstständig: Gewinn; ein später Job nach dem Abbruch nur als Lohn für die Resttage
            if eg.zusatz.sommer_brutto is not None:
                self.assertTrue(eg.abbruch)
                self.assertGreater(eg.zusatz.sommer_anteil, 0.0)
            self.assertLessEqual(eg.zusatz.sommer_anteil, 1.0)
            self.assertGreater(eg.wochenstunden, 30)

    def test_gegenproben_laufen(self):
        for o in h.gegenproben():
            r = h.auswerten(o, 200)
            self.assertLessEqual(r["p10"], r["p90"])


if __name__ == "__main__":
    unittest.main()
