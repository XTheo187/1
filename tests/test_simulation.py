"""Tests für plan/simulation.py - die Rechnung hinter dem Millionenplan."""

from __future__ import annotations

import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plan"))

import simulation as sim  # noqa: E402


class TestSteuer(unittest.TestCase):
    def test_tarif_ist_an_den_grenzen_stetig(self):
        for grenze in (12_348, 17_799, 69_878, 277_825):
            unten, oben = sim.est_2026(grenze), sim.est_2026(grenze + 1)
            self.assertLess(abs(oben - unten), 1.0, grenze)

    def test_grundfreibetrag(self):
        self.assertEqual(sim.est_2026(12_348), 0.0)
        self.assertGreater(sim.est_2026(12_349), 0.0)

    def test_netto_trifft_eckwerte_2026(self):
        # Steuerklasse I, kinderlos, ohne Kirchensteuer (geprüft gegen test.de):
        # 50.000 -> 64,7 %, 80.000 -> 60,0 %, 120.000 -> 57,1 %
        for brutto, quote in ((50_000, 0.647), (80_000, 0.600), (120_000, 0.571)):
            self.assertAlmostEqual(sim.netto_angestellt(brutto, 1.0) / brutto, quote, delta=0.01)

    def test_inflation_erzeugt_keine_kalte_progression(self):
        heute = sim.netto_angestellt(60_000, 1.0) / 60_000
        spaeter = sim.netto_angestellt(60_000 * 1.5, 1.5) / (60_000 * 1.5)
        self.assertAlmostEqual(heute, spaeter, places=6)

    def test_soli_erst_ueber_der_freigrenze(self):
        self.assertEqual(sim.soli(20_350), 0.0)
        self.assertGreater(sim.soli(30_000), 0.0)


class TestAuswertung(unittest.TestCase):
    def test_alter_bezieht_sich_auf_das_ende_des_lebensjahres(self):
        # Ein Leben, das am Ende von Jahr j=0 (Alter 20) Millionär ist.
        leben = [[sim.ZIEL] * sim.JAHRE]
        self.assertEqual(sim.fruehestes_alter(leben), sim.START_ALTER + 1)
        nur_spaet = [[0.0] * (sim.JAHRE - 1) + [sim.ZIEL]]
        self.assertEqual(sim.quote_bis_alter(nur_spaet, sim.END_ALTER), 1.0)
        self.assertEqual(sim.quote_bis_alter(nur_spaet, sim.END_ALTER - 1), 0.0)

    def test_gezaehlt_wird_der_stand_nicht_das_maximum(self):
        leben = [[0.0] * sim.JAHRE]
        leben[0][10] = sim.ZIEL          # kurz Millionär, dann Absturz
        alter = sim.START_ALTER + 11
        self.assertEqual(sim.quote_bis_alter(leben, alter), 1.0)
        self.assertEqual(sim.quote_bis_alter(leben, alter + 1), 0.0)


class TestStrategien(unittest.TestCase):
    N = 600

    def _quote(self, strategie, alter=45):
        return sim.quote_bis_alter(sim.simulieren(strategie, self.N, seed=11), alter)

    def test_alle_strategien_laufen_und_liefern_volle_laenge(self):
        for name, (_titel, strategie) in sim.STRATEGIEN.items():
            leben = sim.simulieren(strategie, 20, seed=3)
            self.assertTrue(all(len(w) == sim.JAHRE for w in leben), name)
            self.assertTrue(all(isinstance(x, float) for w in leben for x in w), name)

    def test_mehr_sparen_hilft_immer(self):
        sparsam = sim.angestellt(5, sim.IT_UNI, lam=0.4, grund=16_000)
        normal = sim.angestellt(5, sim.IT_UNI, lam=0.8, grund=16_000)
        self.assertGreater(self._quote(sparsam), self._quote(normal))

    def test_gleicher_seed_gleiches_ergebnis(self):
        s = sim.STRATEGIEN["plan"][1]
        a = sim.simulieren(s, 50, seed=5)
        b = sim.simulieren(s, 50, seed=5)
        self.assertEqual(a, b)

    def test_niemand_ist_mit_20_millionaer_ohne_firma(self):
        s = sim.angestellt(5, sim.IT_UNI, lam=0.5, grund=16_000)
        self.assertEqual(self._quote(s, alter=sim.START_ALTER + 1), 0.0)


class TestDepot(unittest.TestCase):
    def test_latente_steuer_nur_auf_gewinne(self):
        d = sim.Depot(100_000.0)
        d.jahr(0.0, 0.5)                       # +50 % Kursgewinn
        self.assertAlmostEqual(d.netto, 150_000 - sim.Depot.STEUER * 50_000)

    def test_schuld_wird_verzinst_und_zuerst_getilgt(self):
        d = sim.Depot(-10_000.0)
        d.jahr(0.0, 0.30)                      # Aktienboom ändert die Schuld nicht
        self.assertAlmostEqual(d.wert, -10_500.0)
        d.jahr(12_000.0, 0.0)                  # erst Zins, dann Tilgung, Rest angelegt
        self.assertAlmostEqual(d.wert, 12_000.0 - 11_025.0)
        self.assertAlmostEqual(d.basis, 12_000.0 - 11_025.0)

    def test_entnahme_ueber_vermoegen_wird_schuld(self):
        d = sim.Depot(1_000.0)
        d.entnehmen(1_500.0)
        self.assertAlmostEqual(d.wert, -500.0)


class TestPlanmodell(unittest.TestCase):
    def test_rueckkehr_aus_der_schweiz_kommt_vor(self):
        protokoll = []
        s = sim.weichenplan(sim.PLAN, protokoll=protokoll)
        rng = random.Random(8)
        zustaende = set()
        for _ in range(300):
            protokoll.clear()
            s(rng, sim.Welt.ziehen(rng))
            zustaende.update(z for z, _d, _p, _a in protokoll)
        for z in ("ch", "nach_ch", "de", "pibs", "dual", "studium"):
            self.assertIn(z, zustaende)

    def test_frueher_abbruch_ist_kein_abschluss(self):
        from dataclasses import replace
        wp = replace(sim.PLAN, erste_phase="studium", p_studienabbruch=(1, 1, 1),
                     p_frueher_abbruch=1.0, p_stelle_ch=(1, 1, 1), p_ch_zweiter_anlauf=(1, 1, 1))
        protokoll = []
        s = sim.weichenplan(wp, protokoll=protokoll)
        rng = random.Random(5)
        for _ in range(200):
            protokoll.clear()
            s(rng, sim.Welt.ziehen(rng))
            self.assertFalse(any(a["wert"] for _z, _d, _p, a in protokoll))
            self.assertNotIn("ch", {z for z, _d, _p, _a in protokoll})

    def test_stress_ist_schlechter_als_basis(self):
        basis = sim.quote_bis_alter(sim.simulieren(sim.weichenplan(sim.PLAN), 800, seed=6), sim.ZIEL_ALTER)
        stress = sim.quote_bis_alter(sim.simulieren(sim.weichenplan(sim.PLAN_STRESS), 800, seed=6),
                                     sim.ZIEL_ALTER)
        self.assertLess(stress, basis)

    def test_garantiealter_haelt_auch_ohne_schweiz(self):
        from dataclasses import replace
        wp = replace(sim.PLAN_OHNE_CH, p_ki=(1, 1, 1), p_dual_platz=(0, 0, 0))
        p = sim.quote_bis_alter(sim.simulieren(sim.weichenplan(wp), 3000, seed=9), sim.GARANTIE_ALTER)
        self.assertGreater(p, 0.5)

    def test_ohne_schweiz_ist_schlechter(self):
        from dataclasses import replace
        mit = sim.quote_bis_alter(sim.simulieren(sim.weichenplan(sim.PLAN), 800, seed=4), 55)
        ohne = sim.quote_bis_alter(sim.simulieren(
            sim.weichenplan(replace(sim.PLAN, rueckfall=("de",))), 800, seed=4), 55)
        self.assertGreater(mit, ohne)


class TestSommer(unittest.TestCase):
    def test_obergrenze_kuehnes_spiel(self):
        # Kühnes Spiel bei Roulette bleibt unter der Ville-Schranke S/Z.
        rng = random.Random(4)
        start, n, treffer = 5_000.0, 40_000, 0
        for _ in range(n):
            k = start
            while 0 < k < sim.ZIEL:
                e = min(k, sim.ZIEL - k)
                k += e if rng.random() < 18 / 37 else -e
            treffer += k >= sim.ZIEL
        self.assertLess(treffer / n, start / sim.ZIEL + 0.002)

    def test_meilensteine_sind_plausibel(self):
        e = sim.sommer_meilensteine(n=2_000, seed=1, ausgabe=False)
        self.assertGreater(e["p_mind_5_kunden"], e["p_umsatz_10000"])
        self.assertGreaterEqual(e["umsatz_p75"], e["umsatz_median"])
        self.assertGreaterEqual(e["umsatz_median"], e["umsatz_p25"])


if __name__ == "__main__":
    unittest.main()
