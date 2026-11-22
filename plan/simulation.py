"""Monte-Carlo-Simulation: Welcher Weg macht einen Abiturienten mit
mindestens 50 % Wahrscheinlichkeit zum Millionär - und wann?

Nur Standardbibliothek, wie der Rest des Projekts. Aufruf:

    python3 plan/simulation.py            # alle Strategien, 4.000 Leben je Strategie
    python3 plan/simulation.py --n 20000  # genauer, dauert länger
    python3 plan/simulation.py --sommer   # nur die Rechnung für Sommer 2027

Was "Millionär" hier heißt: Nettovermögen zum Marktwert >= 1.000.000 EUR
(nominal), gemessen am jeweiligen Stichtag - nicht "irgendwann einmal kurz
erreicht". Ein Firmenanteil zählt nur mit einem vorsichtigen Verkaufswert.

Jedes simulierte Leben zieht seine eigenen Annahmen (Rendite, Inflation,
Abschlussquoten, Fleiß) aus einer Spannweite. Das Ergebnis ist deshalb nicht
"bei mittleren Annahmen klappt es", sondern "über die ganze Unsicherheit der
Annahmen hinweg klappt es in X % der Fälle".

Die Spannweiten stammen aus der Recherche in docs/MILLIONENPLAN.md und sind
dort mit Quellen belegt. Jede Zahl unten trägt einen Kommentar, woher sie
kommt oder warum sie so gewählt ist.
"""

from __future__ import annotations

import argparse
import math
import random
from dataclasses import dataclass, field
from typing import Callable

ZIEL = 1_000_000.0
START_ALTER = 19          # Sommer 2027, nach dem Abitur
END_ALTER = 60
JAHRE = END_ALTER - START_ALTER   # Jahr j endet mit Alter START_ALTER + j + 1


# --------------------------------------------------------------------------
# Steuern und Abgaben (Tarif 2026, Grenzen mit der Inflation mitgeführt)
# --------------------------------------------------------------------------


def est_2026(zve: float) -> float:
    """Einkommensteuer nach § 32a EStG, Tarif 2026, Einzelveranlagung."""
    x = max(0.0, zve)
    if x <= 12_348:
        return 0.0
    if x <= 17_799:
        y = (x - 12_348) / 10_000
        return (914.51 * y + 1_400) * y
    if x <= 69_878:
        z = (x - 17_799) / 10_000
        return (173.10 * z + 2_397) * z + 1_034.87
    if x <= 277_825:
        return 0.42 * x - 11_135.63
    return 0.45 * x - 19_470.38


def soli(est: float) -> float:
    """Solidaritätszuschlag mit Freigrenze und Milderungszone (2026)."""
    freigrenze = 20_350
    if est <= freigrenze:
        return 0.0
    return min(0.055 * est, 0.119 * (est - freigrenze))


def steuer(zve: float, index: float) -> float:
    """Tarif in heutigen Euro, damit Inflation keine kalte Progression erzeugt."""
    real = zve / index
    e = est_2026(real)
    return (e + soli(e)) * index


def netto_angestellt(brutto: float, index: float, jahr: int = 0) -> float:
    """Netto aus Bruttogehalt: Sozialabgaben Arbeitnehmeranteil + Steuer.

    KV 7,3 % + halber Zusatzbeitrag 1,45 %, PV 2,4 % (kinderlos), bis zur
    BBG KV 69.750 EUR; RV 9,3 % + AV 1,3 % bis BBG RV 101.400 EUR (Werte 2026).
    """
    lohn = 1.01 ** jahr                   # BBG folgt den Löhnen (real ~+1 %/Jahr), nicht nur der Inflation
    # Sozialabgaben steigen (IGES 2026: 42,8 % -> 48,8 % bis 2035): Arbeitnehmeranteil
    # bis Jahr 9 (2036) linear um 3 Prozentpunkte höher.
    aufschlag = 0.03 * min(1.0, jahr / 9)
    bbg_kv = 69_750 * index * lohn
    bbg_rv = 101_400 * index * lohn
    kvpv = min(brutto, bbg_kv) * (0.073 + 0.0145 + 0.024 + aufschlag / 2)
    rvav = min(brutto, bbg_rv) * (0.093 + 0.013 + aufschlag / 2)
    sozial = kvpv + rvav
    # Vorsorgeaufwand: RV voll, KV/PV-Basis 96 %; die AV fällt unter den schon
    # ausgeschöpften Höchstbetrag für sonstige Vorsorge und mindert nichts.
    zve = brutto - 1_230 * index - kvpv * 0.96 - 0.093 * min(brutto, bbg_rv)
    return brutto - sozial - steuer(zve, index)


def netto_selbststaendig(gewinn: float, index: float, jahr: int = 0) -> float:
    """Netto aus Gewinn eines Einzelunternehmens.

    Freiwillige KV/PV rund 19,7 % vom Gewinn, mindestens auf ca. 1.250 EUR
    Monatseinkommen, höchstens bis BBG. Keine Pflicht-RV (Altersvorsorge
    läuft über das ETF-Depot und zählt dort mit). Gewerbesteuer wird bei
    Hebesatz um 400 % weitgehend auf die Einkommensteuer angerechnet und
    deshalb nicht gesondert angesetzt.
    """
    if gewinn <= 0:
        return gewinn - 1_250 * 12 * 0.197 * index
    basis = min(max(gewinn, 1_250 * 12 * index), 69_750 * index * 1.01 ** jahr)
    kvpv = basis * (0.197 + 0.03 * min(1.0, jahr / 9) / 2)
    return gewinn - kvpv - steuer(gewinn - kvpv, index)


# --------------------------------------------------------------------------
# Gemeinsame Bausteine eines Lebens
# --------------------------------------------------------------------------


def dreieck(rng: random.Random, low: float, mid: float, high: float) -> float:
    return rng.triangular(low, high, mid)


def _t5(rng: random.Random) -> float:
    """Student-t mit 5 Freiheitsgraden, auf Varianz 1 skaliert."""
    nu = 5
    z = rng.gauss(0, 1) / math.sqrt(rng.gammavariate(nu / 2, 2) / nu)
    return z * math.sqrt((nu - 2) / nu)


@dataclass
class Welt:
    """Was für alle Strategien in einem simulierten Leben gleich ist."""

    rendite: float          # erwartete nominale ETF-Rendite p.a. (arithmetisch)
    vola: float             # Volatilität p.a.
    inflation: float
    renditen: list[float] = field(default_factory=list)  # Jahresrenditen

    @classmethod
    def ziehen(cls, rng: random.Random, geo: float | None = None) -> "Welt":
        """Ein Kapitalmarkt-Szenario für ein ganzes Leben.

        Welt-Aktien in EUR, geometrisch 3,5-8 % (Mitte 6 %) nominal:
        MSCI World Net seit 2000 6,68 %, seit 1970 ~7,7-8 %; die Mitte liegt
        bewusst darunter, weil das Bewertungsniveau hoch ist (KGV 22) und
        die Zehnjahresprognosen der großen Häuser für Welt-Aktien bei ~5-5,3 %
        liegen (Vanguard, Morningstar-Überblick 2025/26). Volatilität 13-18 %. Jahresrenditen mit dicken Rändern
        (t-Verteilung, 5 Freiheitsgrade), damit Crashs wie 2001-2009 (-54 %)
        nicht unterschätzt werden. Abzüglich 0,2 % Fondskosten.
        """
        g = geo if geo is not None else dreieck(rng, 0.035, 0.06, 0.08)
        v = dreieck(rng, 0.13, 0.15, 0.18)
        inf = dreieck(rng, 0.015, 0.021, 0.03)
        mu_log = math.log(1 + g)
        renditen = [math.exp(mu_log + v * _t5(rng)) - 1 - 0.002 for _ in range(JAHRE)]
        return cls(g + v * v / 2, v, inf, renditen)

    def index(self, jahr: int) -> float:
        """Preisniveau relativ zu Mitte 2026; Jahr 0 läuft Sep 2027 - Aug 2028 (Mitte Feb 2028)."""
        return (1 + self.inflation) ** (jahr + 1.67)


@dataclass
class Konsum:
    """Ausgaben: ein Grundbedarf plus ein Anteil jedes Euros darüber.

    Der Grenzkonsum ``lam`` ist der Hebel, den ein Plan tatsächlich steuern
    kann: Bei 0,5 wandert jeder zweite zusätzliche Euro ins Depot.
    """

    grundbedarf: float      # EUR/Jahr in heutigen Euro
    lam: float
    traegheit: float = 0.0  # realer Konsum sinkt höchstens um (1 - traegheit) je Jahr
    _letzter: float = 0.0   # realer Konsum des Vorjahres

    def ausgaben(self, netto: float, index: float) -> float:
        g = self.grundbedarf * index
        if netto <= g and not self.traegheit:
            return netto     # Lücke tragen Eltern/BAföG/Nebenjob - kein Kredit
        regel = min(netto, g) if netto <= g else g + self.lam * (netto - g)
        if self.traegheit and netto > 0:
            # Sinkt das Einkommen, bleiben Miete und Gewohnheiten zunächst;
            # gekürzt wird zuerst das Sparen (Fehlbetrag kommt aus dem Depot).
            regel = max(regel, self.traegheit * self._letzter * index)
        self._letzter = regel / index
        return regel


class Depot:
    """ETF-Depot mit Einstandswert, damit die Steuer beim Verkauf zählt.

    Aktien-ETF: 26,375 % Abgeltungsteuer + Soli auf 70 % der Gewinne
    (Teilfreistellung) = 18,46 % effektiv. ``netto`` ist der Wert nach
    dieser latenten Steuer - strenger als der übliche Marktwert.
    """

    STEUER = 0.7 * 0.26375

    def __init__(self, wert: float = 0.0):
        self.wert = wert
        self.basis = wert

    def jahr(self, sparen: float, rendite: float) -> None:
        """Sparbetrag fließt übers Jahr verteilt ein, im Schnitt halbes Jahr investiert."""
        if sparen < 0:
            self.entnehmen(-sparen)
            sparen = 0.0
        if self.wert < 0:
            # Schuld (Studienkredit, Eltern): verzinst mit 5 %, Sparen tilgt zuerst
            self.wert *= 1.05
            tilgung = min(sparen, -self.wert)
            self.wert += tilgung
            sparen -= tilgung
            if self.wert < 0 or sparen <= 0:
                return
            self.basis = 0.0
        self.wert = self.wert * (1 + rendite) + sparen * (1 + rendite / 2)
        self.basis += sparen

    def entnehmen(self, betrag: float) -> None:
        """Verkauf für ``betrag`` Euro netto; die Steuer auf den Gewinnanteil kommt dazu."""
        if betrag <= 0:
            return
        if self.wert <= 0:
            self.wert -= betrag
            return
        if betrag >= self.netto:
            # alles verkaufen, der Rest wird Schuld
            rest = betrag - self.netto
            self.wert, self.basis = -rest, 0.0
            return
        gewinnanteil = max(0.0, 1 - self.basis / self.wert)
        brutto = betrag / (1 - self.STEUER * gewinnanteil)
        anteil = min(1.0, brutto / self.wert)
        self.basis *= 1 - anteil
        self.wert -= brutto

    @property
    def netto(self) -> float:
        if self.wert <= 0:
            return self.wert
        return self.wert - self.STEUER * max(0.0, self.wert - self.basis)


# --------------------------------------------------------------------------
# Strategien
# --------------------------------------------------------------------------

Strategie = Callable[[random.Random, Welt], list[float]]


def _w(rng: random.Random, x) -> float:
    """Zahl oder Spannweite (low, mid, high) -> eine Ziehung je Leben."""
    return dreieck(rng, *x) if isinstance(x, tuple) else float(x)


class GehaltPfad:
    """Realer Gehaltspfad (in heutigen Euro), je Leben einmal gezogen.

    - ``start``: Einstiegsgehalt (Median); ``streu``: dauerhafte Einzelstreuung
      (log-SD, Recherche: IT 0,22-0,40).
    - Reales Wachstum früh (bis ``knick``) und spät, inkl. Reallohndrift.
    - ``schock``: vorübergehende Jahresschwankung (Bonus, Provision), log-SD.
    - Karrieresprung (SDR -> Account Executive): Chance ``sprung_p`` je Jahr,
      nur im Fenster ``sprung_ab``..``sprung_bis``; danach nur noch spätes
      Wachstum (kein Stapeln von Sprung und Einstiegswachstum). Mit
      ``p_scheitern`` scheitert die Beförderung im Folgejahr (Bridge Group:
      26 %), dann zurück auf das alte Niveau + 10 %.
    """

    def __init__(self, rng: random.Random, start, wachstum_frueh, wachstum_spaet,
                 knick: int, streu, sprung_p=0.0, sprung_faktor=1.0,
                 schock: float = 0.08, sprung_ab: int = 0, sprung_bis: int = 99,
                 p_scheitern=0.0):
        self.rng = rng
        self.g = _w(rng, start) * math.exp(rng.gauss(0, _w(rng, streu)))
        self.frueh, self.spaet = _w(rng, wachstum_frueh), _w(rng, wachstum_spaet)
        self.p_sprung, self.f_sprung = _w(rng, sprung_p), _w(rng, sprung_faktor)
        self.p_scheitern = _w(rng, p_scheitern)
        self.knick, self.schock = knick, schock
        self.sprung_ab, self.sprung_bis = sprung_ab, sprung_bis
        self.jahr = 0
        self.gesprungen = self.gescheitert = False
        self.seit_sprung = -1
        self.vor_sprung = 0.0

    @property
    def befoerdert(self) -> bool:
        return self.gesprungen and not self.gescheitert

    def __iter__(self):
        return self

    def __next__(self) -> float:
        rng = self.rng
        wert = self.g * math.exp(rng.gauss(0, self.schock) - self.schock * self.schock / 2)
        frueh = self.jahr < self.knick and not self.gesprungen
        self.g *= 1 + (self.frueh if frueh else self.spaet) + rng.gauss(0, 0.015)
        if self.gesprungen:
            self.seit_sprung += 1
            if self.seit_sprung == 1 and rng.random() < self.p_scheitern:
                self.g = self.vor_sprung * 1.1
                self.gescheitert = True
        elif self.p_sprung and self.sprung_ab <= self.jahr <= self.sprung_bis \
                and rng.random() < self.p_sprung:
            self.vor_sprung = self.g
            self.g *= self.f_sprung
            self.gesprungen = True
            self.seit_sprung = 0
        self.jahr += 1
        return wert


def _gehalt_pfad(rng: random.Random, *args, **kwargs) -> GehaltPfad:
    return GehaltPfad(rng, *args, **kwargs)


# Gehaltspfade aus der Recherche (Stepstone 2026, BA-Entgeltstatistik 2025,
# levels.fyi; Details in docs/MILLIONENPLAN.md). Wachstum real, inkl. Drift.
# Abgleich Stack Overflow DE 2024+25 (Rohdaten, n=4.345 Angestellte): Median
# 49 Tsd. (1-3 J.), 66 Tsd. (5-8 J.), 78 Tsd. (10-13 J.), 80 Tsd. (15-18 J.);
# P(>=100 Tsd.) nach 10-13 Jahren 18 %.
IT_UNI = dict(start=(45_000, 55_000, 68_000), wachstum_frueh=(0.025, 0.042, 0.075),
              wachstum_spaet=(0.0, 0.008, 0.02), knick=10, streu=(0.22, 0.30, 0.40))
IT_BACHELOR = dict(IT_UNI, start=(44_000, 50_000, 58_000))
DUAL = dict(IT_UNI, start=(45_000, 52_000, 60_000))
WEBDEV = dict(IT_UNI, start=(42_000, 48_500, 56_000))   # Stepstone: Webentwickler-Einstieg 48.500
# IT-/SaaS-Vertrieb, korrigiert nach der Gegenprüfung (Bridge Group 2025,
# UNIFY ~180.000 SDRs, RepVue DE, JOIN, Skipcall, gehalt.de):
# - Einstieg als SDR mit 19: 34-50 Tsd. tatsächlich gezahlt (fix 35-42 + Provision).
# - Beförderung zum AE nur in den SDR-Jahren 2-5, je Jahr 8-25 %
#   -> jemals AE ~35-55 % (UNIFY: 22-46 %); Gehaltssprung x1,3-1,9
#   (AE-Mitte mit 34-39: ~70 / ~95 / ~125 Tsd. tatsächlich gezahlt).
# - 15-35 % der Beförderungen scheitern im ersten Jahr (Bridge Group: 26 %).
# - Nach dem Sprung nur noch spätes Wachstum (0-2 %).
VERTRIEB = dict(start=(34_000, 42_000, 50_000), wachstum_frueh=(0.01, 0.035, 0.06),
                wachstum_spaet=(0.0, 0.01, 0.02), knick=10, streu=(0.20, 0.30, 0.40),
                sprung_p=(0.08, 0.15, 0.25), sprung_faktor=(1.3, 1.55, 1.9),
                schock=0.18, sprung_ab=2, sprung_bis=4, p_scheitern=(0.15, 0.25, 0.35))


def angestellt(studienjahre: int, pfad_param: dict, lam: float, grund: float,
               neben_netto: float = 6_000, p_einstieg: tuple | float = 1.0,
               ersatz: dict | None = None) -> Strategie:
    """Studium/Ausbildung, danach angestellt, Überschuss ins ETF-Depot.

    ``p_einstieg``: Chance, den Zielberuf überhaupt zu bekommen; sonst gilt
    der Ersatzpfad ``ersatz`` (z. B. normaler IT-Job statt Vertrieb).
    """

    def leben(rng: random.Random, w: Welt) -> list[float]:
        konsum = Konsum(grund, lam)
        studium = Konsum(12_000, 0.6)
        depot = Depot(1_000.0)
        param = pfad_param if (ersatz is None or rng.random() < _w(rng, p_einstieg)) else ersatz
        pfad = _gehalt_pfad(rng, **param)
        werte = []
        for j in range(JAHRE):
            idx = w.index(j)
            if j < studienjahre:
                netto = neben_netto * idx
                sparen = netto - studium.ausgaben(netto, idx)
            else:
                brutto = next(pfad) * idx
                netto = netto_angestellt(brutto, idx, j)
                sparen = netto - konsum.ausgaben(netto, idx)
            depot.jahr(sparen, w.renditen[j])
            werte.append(depot.netto)
        return werte

    return leben


@dataclass
class AgenturParameter:
    """Spannweiten (low, mid, high) für das Agenturmodell.

    Kalibriert gegen die Recherche (siehe ``kalibrierung_agentur``):
    Überleben nach 1/3/5/10 Jahren ~76/53/38/24 % (IfM, Eurostat); von den
    überlebenden Vollzeit-Inhabern in Jahr 3-5 zahlen sich ~20 % mindestens
    50 Tsd. aus, ~4-5 % mindestens 100 Tsd. (Admin Bar 2026, n=622); kaum
    eine Agentur wächst über 10 Köpfe.
    """

    eur_je_stunde_solo: tuple = (18, 24, 30)          # Median-Umsatz je Arbeitsstunde inkl. Akquise und Leerlauf
    streu_eur_h: float = 0.5                          # Unterschiede zwischen Gründern (log-SD): Preis, Talent, Nische
    auslastung_start: tuple = (0.15, 0.35, 0.6)       # gefüllter Anteil der Kapazität im 1. Jahr
    lernrate: tuple = (0.1, 0.25, 0.45)               # wie schnell sich die Lücke zur Vollauslastung schließt
    kosten_anteil: tuple = (0.08, 0.15, 0.22)         # Werkzeuge, Versicherung, Fahrzeug, Buchhaltung
    hazard_frueh: tuple = (0.09, 0.13, 0.19)          # Aufgabe/Scheitern je Jahr in den Jahren 1-5 (vor Auslese)
    hazard_spaet: tuple = (0.05, 0.07, 0.10)          # danach, solange solo
    hazard_team: tuple = (0.03, 0.05, 0.08)           # Krise, die ein Team-Geschäft beendet
    p_skalieren: tuple = (0.03, 0.10, 0.20)           # Chance je Jahr (ab 50 Tsd. Gewinn), erste Vollzeitkraft
    umsatz_je_fte: tuple = (75_000, 105_000, 140_000) # BVDW 2026: ~112-127 Tsd. bei großen Agenturen
    marge_je_fte: tuple = (0.03, 0.15, 0.25)          # Promethean: Nettomarge 5-20 %, kleine Studios ~19 %
    neue_fte_je_jahr: tuple = (0.3, 1.0, 2.0)         # Wachstum des Teams pro Jahr
    max_fte: tuple = (2, 6, 30)                       # Obergrenze, die dieser Gründer erreicht
    preistrend: tuple = (-0.06, -0.02, 0.01)          # real; Freelancer-Kompass 2026: Projektumsatz -17 %
    multiple: tuple = (1.5, 2.5, 4.0)                 # x Übergewinn; FE/Empire Flippers: 1,6-3,5x SDE
    ersatz_gehalt_inhaber: float = 60_000             # Marktgehalt für die Rolle des Inhabers


class AgenturLauf:
    """Ein Agenturleben: zieht seine Parameter einmal und rechnet Jahr für Jahr.

    Von beiden Strategien (``agentur`` und ``weichenplan``) genutzt, damit
    das Agenturmodell nur an einer Stelle steht.
    """

    def __init__(self, rng: random.Random, p: AgenturParameter):
        d = lambda t: dreieck(rng, *t)  # noqa: E731
        self.rng, self.p = rng, p
        self.eur_h = d(p.eur_je_stunde_solo) * math.exp(rng.gauss(0, p.streu_eur_h))
        self.aus, self.lern = d(p.auslastung_start), d(p.lernrate)
        self.kosten, self.hz_frueh, self.hz_spaet = d(p.kosten_anteil), d(p.hazard_frueh), d(p.hazard_spaet)
        self.hz_team, self.p_skal = d(p.hazard_team), d(p.p_skalieren)
        self.u_fte, self.marge = d(p.umsatz_je_fte), d(p.marge_je_fte)
        self.fte_wachstum, self.fte_max = d(p.neue_fte_je_jahr), d(p.max_fte)
        self.trend, self.mult = d(p.preistrend), d(p.multiple)
        self.jahre = 0
        self.fte = 0.0
        self.gewinn = self.gewinn_real = 0.0

    def jahr(self, j: int, idx: float, stunden: float, wachsen: bool) -> float:
        """Gewinn dieses Jahres (nominal); ``wachsen``: Team darf entstehen."""
        rng = self.rng
        preis = (1 + self.trend) ** j
        erfahrung = 1 - (1 - self.aus) * (1 - self.lern) ** self.jahre
        umsatz = stunden * self.eur_h * erfahrung * preis * idx * math.exp(rng.gauss(0, 0.15))
        gewinn = umsatz * (1 - self.kosten)
        if self.fte > 0:
            gewinn += self.fte * self.u_fte * self.marge * preis * idx * math.exp(rng.gauss(0, 0.3))
        if wachsen:
            if self.fte == 0 and gewinn > 50_000 * idx and rng.random() < self.p_skal:
                self.fte = 1.0
            elif self.fte > 0:
                self.fte = min(self.fte_max, self.fte + max(0.0, rng.gauss(self.fte_wachstum, 0.7)))
        self.jahre += 1
        self.gewinn = gewinn
        self.gewinn_real = gewinn / idx
        return gewinn

    def endet(self) -> bool:
        """Scheitern oder Aufgabe in diesem Jahr?"""
        if self.fte >= 3:
            hz = self.hz_team
        else:
            hz = self.hz_frueh if self.jahre <= 5 else self.hz_spaet
            # Auslese: Wer wenig verdient, hört eher auf; wer gut verdient, bleibt.
            if self.gewinn_real < 25_000:
                hz *= 1.5
            elif self.gewinn_real > 60_000:
                hz *= 0.4
        if self.rng.random() < hz:
            self.fte = 0.0
            return True
        return False

    def firmenwert(self, idx: float) -> float:
        """Vorsichtiger Verkaufswert: erst ab 3 Vollzeitkräften, mit 30 % Abschlag
        (nur ein Teil wird bar gezahlt, Earn-outs fließen selten voll, Steuer)."""
        if self.fte < 3:
            return 0.0
        uebergewinn = self.gewinn - self.p.ersatz_gehalt_inhaber * idx
        return max(0.0, uebergewinn) * self.mult * 0.7


def agentur(studium_parallel: bool, lam: float, grund: float,
            p: AgenturParameter | None = None,
            rueckfall_start=(42_000, 48_500, 56_000),
            beobachter: Callable | None = None) -> Strategie:
    """Webagentur für lokale Betriebe - der Weg, den standortcheck vorbereitet.

    ``studium_parallel``: Informatikstudium (5 Jahre) mit 20 h/Woche Agentur,
    danach Vollzeit-Agentur oder Anstellung, je nachdem, was mehr bringt.
    Ohne Studium: ab Sommer 2027 Vollzeit. Scheitert die Agentur, geht es in
    eine Anstellung als Webentwickler weiter; das Depot bleibt.

    ``beobachter(j, aktiv, gewinn, fte)``: für die Kalibrierung.
    """
    p = p or AgenturParameter()

    def leben(rng: random.Random, w: Welt) -> list[float]:
        lauf = AgenturLauf(rng, p)
        konsum = Konsum(grund, lam)
        studium = Konsum(12_000, 0.6)
        gehalt = _gehalt_pfad(rng, **dict(WEBDEV, start=rueckfall_start))
        studienjahre = 5 if studium_parallel else 0
        depot, aktiv = Depot(1_000.0), True
        werte = []
        for j in range(JAHRE):
            idx = w.index(j)
            firmenwert = 0.0
            if aktiv:
                im_studium = j < studienjahre
                gewinn = lauf.jahr(j, idx, 900 if im_studium else 2_000, wachsen=not im_studium)
                netto = netto_selbststaendig(gewinn, idx, j)
                sparen = netto - (studium if im_studium else konsum).ausgaben(netto, idx)
                firmenwert = lauf.firmenwert(idx)
                if beobachter:
                    beobachter(j, True, gewinn, lauf.fte)
                if lauf.endet():
                    aktiv, firmenwert = False, 0.0
                elif studium_parallel and j == studienjahre - 1 and lauf.fte == 0:
                    if gewinn * 2_000 / 900 * 0.8 < 55_000 * idx:   # IT-Einstieg mit Master
                        aktiv = False
            else:
                if beobachter:
                    beobachter(j, False, 0.0, 0.0)
                netto = netto_angestellt(next(gehalt) * idx, idx, j)
                sparen = netto - konsum.ausgaben(netto, idx)
            depot.jahr(sparen, w.renditen[j])
            werte.append(depot.netto + firmenwert)
        return werte

    return leben


def kalibrierung_agentur(n: int = 20_000, p: AgenturParameter | None = None) -> dict[str, float]:
    """Vergleicht das Agenturmodell (Vollzeit, nominal ~heutige Euro) mit der Recherche."""
    daten: list[list[tuple]] = []
    aktuell: list[tuple] = []

    def beob(j, aktiv, gewinn, fte):
        aktuell.append((aktiv, gewinn, fte))

    strat = agentur(False, 0.5, 16_000, p, beobachter=beob)
    rng = random.Random(99)
    for _ in range(n):
        aktuell = []
        strat(rng, Welt(0.07, 0.15, 0.0, [0.0] * JAHRE))
        daten.append(aktuell)

    def aktiv_nach(jahre):   # nach "jahre" Jahren noch aktiv (Eintrag des Folgejahres aktiv)
        return sum(1 for z in daten if z[jahre][0]) / n

    def bedingt(jahre, schwelle):
        lebend = [z for z in daten if any(z[k][0] for k in jahre) and all(z[k][0] for k in jahre)]
        if not lebend:
            return 0.0
        return sum(1 for z in lebend if max(z[k][1] for k in jahre) >= schwelle) / len(lebend)

    erg = {
        "aktiv_nach_1": aktiv_nach(1), "aktiv_nach_3": aktiv_nach(3),
        "aktiv_nach_5": aktiv_nach(5), "aktiv_nach_10": aktiv_nach(10),
        "p50k_j3bis5_lebend": bedingt(range(2, 5), 50_000),
        "p100k_j3bis5_lebend": bedingt(range(2, 5), 100_000),
        "p100k_j6bis10_lebend": bedingt(range(5, 10), 100_000),
        "team3_j10": sum(1 for z in daten if z[9][2] >= 3) / n,
        "team10_j10": sum(1 for z in daten if z[9][2] >= 10) / n,
    }
    return erg


@dataclass
class NachfolgeParameter:
    """Kauf eines bestehenden, profitablen Kleinbetriebs (Nachfolge).

    Spannweiten (low, mid, high) nach der Recherche: KfW-Nachfolgemonitoring
    (Median-Kaufpreiswunsch 375 Tsd. EUR, entspricht ~95 Tsd. EBITDA),
    DUB-Multiples Micro-Cap 3,2-5,7x, Stanford/Yale/IESE Search-Fund-Studien
    (26-31 % Verlust-Deals, außerhalb USA Median-IRR 9 %, ohne MBA 1 %),
    Finanzierung über ERP-Förderkredit, Bürgschaftsbank, Verkäuferdarlehen.
    """

    ab_alter: tuple = (25, 28, 32)                     # bankfähige Erfahrung; Suchende sonst im Median 32-34
    eigenkapital_quote: tuple = (0.10, 0.15, 0.25)     # IHK: 15 % Untergrenze, 20-25 % üblich
    min_eigenkapital: float = 40_000
    p_abschluss_je_jahr: tuple = (0.08, 0.18, 0.30)    # Objekt finden (30-75 % je Suche) UND Finanzierung (30-70 %)
    ebitda: tuple = (80_000, 150_000, 350_000)         # Gewinn vor Zinsen/Abschreibung beim Kauf
    kaufmultiple: tuple = (3.0, 4.3, 5.5)
    zins: tuple = (0.04, 0.055, 0.075)
    tilgungsjahre: int = 8
    wachstum: tuple = (-0.04, 0.01, 0.05)              # reales EBITDA-Wachstum nach Kauf
    schock_sigma: float = 0.15
    hazard: tuple = (0.02, 0.05, 0.09)                 # ~28 % Verlust-Deals über ~6 Jahre
    buergschaft: tuple = (0.0, 0.15, 0.35)             # Anteil Restschuld, für den man persönlich haftet
    gehalt_inhaber: float = 80_000
    exit_multiple: tuple = (3.0, 4.3, 5.5)             # Aufschlag nur bei Wachstum über ~5 Mio. Umsatz


def nachfolge(basis: Strategie, lam: float, grund: float,
              p: NachfolgeParameter | None = None) -> Strategie:
    """Erst einen Basisweg gehen (Depot aufbauen), dann einen Betrieb kaufen.

    Der Basisweg liefert bis zum Kauf das Vermögen; das Eigenkapital kommt
    aus dem Depot. Danach lebt man vom Geschäftsführergehalt, der
    Überschuss tilgt den Kredit. Vermögen = Depot + (Firmenwert - Schulden)
    mit 30 % Abschlag.
    """
    p = p or NachfolgeParameter()

    def leben(rng: random.Random, w: Welt) -> list[float]:
        d = lambda t: dreieck(rng, *t)  # noqa: E731
        basis_werte = basis(rng, w)
        ab = int(round(d(p.ab_alter)))
        ek_quote, p_deal = d(p.eigenkapital_quote), d(p.p_abschluss_je_jahr)
        zins, wachstum, hz, buerg = d(p.zins), d(p.wachstum), d(p.hazard), d(p.buergschaft)
        exit_m = d(p.exit_multiple)
        konsum = Konsum(grund, lam)
        gehalt_nach_ausfall = _gehalt_pfad(rng, 60_000, 0.02, 0.01, 10, 0.15)

        werte: list[float] = []
        zustand = "basis"          # basis -> inhaber -> (ausgefallen)
        depot = Depot(0.0)
        schuld = ebitda = 0.0
        for j in range(JAHRE):
            idx = w.index(j)
            alter = START_ALTER + j
            if zustand == "basis":
                kasse = basis_werte[j]          # Basiswert ist schon nach Steuer
                if alter >= ab and rng.random() < p_deal:
                    e = d(p.ebitda) * idx
                    preis = e * d(p.kaufmultiple)
                    ek = max(preis * ek_quote, p.min_eigenkapital * idx)
                    if kasse >= ek:
                        zustand, ebitda, schuld = "inhaber", e, preis - ek
                        depot = Depot(kasse - ek)
                        werte.append(depot.netto + max(0.0, preis - schuld) * 0.7)
                        continue
                werte.append(kasse)
                continue
            if zustand == "ausgefallen":
                netto = netto_angestellt(next(gehalt_nach_ausfall) * idx, idx, j)
                depot.jahr(netto - konsum.ausgaben(netto, idx), w.renditen[j])
                werte.append(depot.netto)
                continue
            # Inhaber
            ebitda *= (1 + wachstum + w.inflation) * math.exp(rng.gauss(0, p.schock_sigma))
            if rng.random() < hz:
                depot.entnehmen(buerg * schuld)
                if depot.wert < 0:
                    depot = Depot(0.0)            # Privatinsolvenz: mehr als alles ist nicht zu verlieren
                zustand, schuld = "ausgefallen", 0.0
                werte.append(depot.netto)
                continue
            gehalt = p.gehalt_inhaber * idx
            zinsen = schuld * zins
            tilgung_soll = schuld / p.tilgungsjahre if schuld > 0 else 0.0
            vor_steuer = ebitda - gehalt - zinsen - 0.03 * ebitda   # Ersatzinvestitionen
            frei = vor_steuer * (1 - 0.30) if vor_steuer > 0 else vor_steuer  # GmbH ~30 %
            if frei < tilgung_soll:
                depot.entnehmen(tilgung_soll - frei)                 # Nachschuss aus dem Depot
                tilgung = tilgung_soll
                ueberschuss = 0.0
            else:
                tilgung = min(schuld, frei)                         # Sondertilgung mit allem Freien
                ueberschuss = frei - tilgung
            schuld = max(0.0, schuld - tilgung)
            netto = netto_angestellt(gehalt, idx, j)
            sparen = netto - konsum.ausgaben(netto, idx)
            # Überschuss bleibt in der GmbH, beim Ausschütten fiele ~26 % an
            depot.jahr(sparen + ueberschuss * 0.74, w.renditen[j])
            eigen = max(0.0, ebitda * exit_m - schuld) * 0.7
            werte.append(depot.netto + eigen)
        return werte

    return leben


def mit_wette(basis: Strategie, p_gross: float = 0.04, p_klein: float = 0.20,
              kosten_anteil: float = 0.85) -> Strategie:
    """Basisweg plus eine Software-Wette nebenher (z. B. standortcheck als SaaS).

    Die Wette kostet Zeit: Der Basisweg verliert ``1 - kosten_anteil`` seines
    Vermögenszuwachses in den Wettjahren. Ausgänge nach 4 Jahren:
    groß (1-5 Mio. Verkaufswert), klein (50-300 Tsd.) oder nichts.
    """

    def leben(rng: random.Random, w: Welt) -> list[float]:
        werte = basis(rng, w)
        z = rng.random()
        if z < p_gross:
            gewinn = dreieck(rng, 1_000_000, 1_800_000, 5_000_000)
        elif z < p_gross + p_klein:
            gewinn = dreieck(rng, 50_000, 120_000, 300_000)
        else:
            gewinn = 0.0
        ergebnis = []
        for j, v in enumerate(werte):
            if j < 4:
                v *= kosten_anteil
            else:
                v = v * (1 - (1 - kosten_anteil) * 0.5)
                v += gewinn * 0.75 * (1 + w.rendite) ** (j - 4)   # nach Steuer, angelegt
            ergebnis.append(v)
        return ergebnis

    return leben


def schweiz(p_stelle: tuple = (0.3, 0.5, 0.7), start: tuple = (80_000, 95_000, 115_000),
            lam: float = 0.5, grund_ch: float = 34_000) -> Strategie:
    """Informatik-Master in Deutschland, dann Stelle in der Schweiz.

    Bekommt man keine Stelle (Wahrscheinlichkeit 1 - p_stelle), läuft der
    deutsche Angestelltenweg weiter. Schweizer Abzüge: AHV/IV/EO/ALV ~6,4 %,
    Pensionskasse ~7 % (zählt zur Hälfte als Vermögen), Einkommensteuer je
    nach Kanton grob 8-20 %. Lebenshaltung deutlich höher (Miete Zürich).
    """
    de = angestellt(5, IT_UNI, lam=lam, grund=16_000)

    def leben(rng: random.Random, w: Welt) -> list[float]:
        if rng.random() >= dreieck(rng, *p_stelle):
            return de(rng, w)
        konsum = Konsum(grund_ch, lam)
        studium = Konsum(12_000, 0.6)
        pfad = _gehalt_pfad(rng, start, (0.02, 0.035, 0.055), (0.005, 0.012, 0.025), 10, (0.2, 0.25, 0.32))
        depot, pk = Depot(1_000.0), 0.0
        werte = []
        for j in range(JAHRE):
            idx = w.index(j)
            if j < 5:
                netto = 6_000 * idx
                sparen = netto - studium.ausgaben(netto, idx)
            else:
                brutto = next(pfad) * idx
                real = brutto / idx
                st = min(0.30, max(0.06, 0.06 + 0.08 * math.log(max(real, 60_000) / 60_000)))
                netto = brutto * (1 - 0.064 - 0.07 - st)
                pk = pk * 1.02 + brutto * 0.14 * 0.5      # AN+AG-Beitrag, Verzinsung ~2 %
                sparen = netto - konsum.ausgaben(netto, idx)
            depot.jahr(sparen, w.renditen[j])
            werte.append(depot.netto + pk)
        return werte

    return leben


@dataclass
class Weichen:
    """Die Entscheidungsregeln des Weichenplans."""

    erste_phase: str = "studium"            # "studium": Studium + Agentur 20 h; "agentur": Vollzeit;
                                            # "vertrieb": sofort IT-Vertrieb, Agentur nur als Plan B;
                                            # "dual": duales Studium (bezahlt, ohne Agentur)
    studienjahre: int = 3                   # 3 = Bachelor, 5 = Master
    dual_brutto: tuple = (13_000, 15_000, 18_000)    # Vergütung im dualen Studium (BIBB ~1.209 EUR/Monat)
    p_abbruch_dual: tuple = (0.10, 0.18, 0.28)       # DHBW Technik: 18,1 %
    p_dual_platz: tuple = (0.40, 0.60, 0.80)         # Schätzung, nur bei 20-40 Bewerbungen bis Feb. 2027
    p_dual_bindung: float = 0.67                     # Bindungs-/Rückzahlungsklausel nach dem Studium
    p_frueher_abbruch: float = 0.5                   # etwa die Hälfte bricht im ersten Jahr ab (DHBW)
    p_neustart: float = 0.5                          # davon beginnt ein Teil gleich neu (Schätzung)
    # Praxisintegriertes Bachelorstudium (PiBS) in der Schweiz: 4 Jahre, 40 %
    # Arbeit im Partnerbetrieb (ZHAW, FHNW, BFH, HSLU, FFHS). Lohn z. B. Post CH
    # 800/1.350/1.700/1.700 CHF im Monat, Studiengebühr bezahlt die Firma.
    p_pibs_platz: tuple = (0.10, 0.20, 0.35)         # Schätzung: 2022 schweizweit nur 128 PiBS-Eintritte
                                                     # über alle MINT-Fächer; Firmenplätze sind der Engpass
    pibs_brutto: tuple = (15_000, 19_000, 24_000)    # EUR/Jahr im Schnitt der 4 Jahre (Post: ~18 Tsd. CHF)
    grund_ch_studium: float = 25_000                 # Zimmer + Leben + Krankenkasse in der Schweiz
    p_abbruch_pibs: tuple = (0.15, 0.22, 0.30)       # Schätzung (FH-Abbruch, Doppelbelastung)
    p_stelle_ch_nach_pibs: tuple = (0.65, 0.78, 0.90)  # SBFI: 50 % bleiben im Partnerbetrieb
    start_ch_pibs: tuple = (75_000, 85_000, 95_000)    # Junior mit 4 Jahren Praxis
    pruefjahre: int = 3                     # nach so vielen Jahren wird die Weiche gestellt
    agentur_schwelle_real: float = 55_000   # Vollzeit-Gewinn (heutige Euro), ab dem die Agentur gewinnt
    rueckfall: tuple = ("ch", "de")         # Reihenfolge der Alternativen, falls die Agentur nicht trägt
    p_stelle_ch: tuple = (0.18, 0.32, 0.50) # Schweizer Stelle mit deutschem Abschluss (Schätzung;
                                            # Einsteigermarkt enger: FH-IT-Erwerbslose 6,4 %)
    p_ch_mit_partner: float = 0.7           # Faktor, wenn schon eine Partnerschaft besteht
    p_ch_zweiter_anlauf: tuple = (0.20, 0.25, 0.30)  # einmalig nach 4 Berufsjahren in DE (Schätzung)
    rueckkehr_ch: tuple = (0.025, 0.035, 0.05)       # je Jahr zurück nach DE. SECO: 45 % aller EU-
                                                     # Zuwanderer gehen binnen 10 J.; wer mit Abschluss
                                                     # und Plan bleibt, seltener -> ~30-35 % in 10 J.
    rueckkehr_ch_kind: float = 0.015                 # zusätzlich ab dem ersten Kind
    rueckkehr_lohn: tuple = (0.60, 0.68, 0.75)       # DE-Gehalt relativ zum letzten CH-Gehalt
    ch_steuer_zuschlag: float = 0.015                # Zürich-Stadt/Basel/Bern über der Kurve (ESTV/BAK)
    ch_abgaben: float = 0.072                        # AHV/IV/EO/ALV + NBU + Krankentaggeld
    ch_pk_an: float = 0.058                          # Arbeitnehmerbeitrag Pensionskasse (BVG 23-45)
    ch_pk_gutschrift: float = 0.0625                 # zählt: halbe Altersgutschrift (Kapital gebunden)
    ch_pk_zins: float = 0.014                        # BVG-Mindestzins 1,25 %
    ch_kinder_faktor: float = 1.7                    # Kita in der Schweiz fast zum Vollpreis (4 Jahre)
    ch_wachstum_spaet: tuple = (0.0, 0.006, 0.018)   # SwissICT: ICT-Löhne nominal kaum gestiegen
    start_ch: tuple = (75_000, 88_000, 105_000)    # SwissICT 2026: FH-Bachelor 81.850 CHF
    start_de: tuple = (44_000, 50_000, 58_000)
    # Vertrieb (korrigiert nach der Gegenprüfung; Markt 2024-26 geschrumpft:
    # 36 % der B2B-Firmen haben SDR-Teams verkleinert, SDR-Anzeigen -21 %)
    p_vertrieb: tuple = (0.27, 0.40, 0.52)  # SaaS-SDR-Stelle mit 19 ohne Studium (Schätzung)
    vertrieb_bonus_erfolg: float = 1.3      # x, wenn bis 08/2027 >= 1 Paket und >= 5 Kunden verkauft
    p_sommer_erfolg: float = 0.71           # P(>= 1 Paket und >= 5 Kunden), aus sommer_meilensteine
    p_vertrieb_mit_abschluss: tuple = (0.35, 0.50, 0.65)  # zweiter Versuch nach dem Bachelor
    vertrieb_sprung_ab: int = 1             # mit Verkaufserfahrung frühestens nach 2 SDR-Jahren AE
    hazard_sdr: tuple = (0.08, 0.12, 0.18)  # raus aus dem Vertrieb vor der Beförderung (Bridge: 13 % unfreiwillig)
    hazard_ae: tuple = (0.02, 0.04, 0.07)   # raus als Account Executive
    vertrieb_rest: tuple = (0.55, 0.70, 0.85)     # Gehalt danach relativ zum letzten (Account Mgmt., Innendienst)
    vertrieb_boden: tuple = (36_000, 45_000, 55_000)  # Innendienst/Kaufmann mit Erfahrung
    vertrieb_deckel: float = 90_000                   # CSM/Account Management (Jobrise 55-100 Tsd.)
    grund_vertrieb: tuple = (18_000, 19_500, 22_000)  # Großstadt: WG-Zimmer München 850, Berlin 650 EUR
    p_studienabbruch: tuple = (0.35, 0.42, 0.50)      # DZHW: Uni-Bachelor Informatik 42 %, + Agentur
    nachfolge: bool = True
    freelance: bool = True
    # IT-Freelancing (Freelancer-Kompass 2026: Software/Web 91 EUR/h, Median ~145
    # fakturierte Tage, 25 % mit >= 100 Tsd. Gewinn, 80 % mit > 10 J. Praxis)
    freelance_nach_jahren: int = 5          # vorher kaum Projekte (nur 5 % mit < 5 J. Praxis)
    p_freelance: tuple = (0.3, 0.45, 0.6)   # traut sich und findet Projekte
    satz: tuple = (65, 82, 105)             # EUR/h für junge Software-/Web-Freelancer
    auslastung: tuple = (0.40, 0.62, 0.85)  # Anteil von 1.700 möglichen Stunden (~85-180 Tage)
    hazard_freelance: tuple = (0.03, 0.07, 0.12)  # zurück in Anstellung (Flaute, Statusrisiko)
    lam: float = 0.5
    lam_streu: tuple | None = None          # Sparregel je Leben gezogen (Einhaltung ist nicht perfekt)
    grund_de: tuple | float = (15_000, 18_000, 22_000)  # WG Berlin ~15, WG München ~17,5, Wohnung ~19,5 Tsd.
    grund_ch: tuple | float = (34_000, 38_000, 45_000)  # inkl. Krankenkasse (~CHF 4,2-8,3 Tsd./Jahr)
    traegheit: float = 0.95                 # Konsum sinkt real höchstens 5 % je Jahr
    lam_partner: float = 0.05               # gemeinsamer Lebensstandard steigt mit
    p_aufgeben: float = 0.15                # Sparregel wird irgendwann halbherzig (Sparanteil halbiert)
    # Weitere Risiken (Gegenprüfung)
    p_ki: tuple = (0.25, 0.35, 0.50)        # KI-Szenario: Einsteigermarkt dauerhaft enger
    ki_chancen: float = 0.8                 # Plätze/Stellen x0,8
    ki_start: float = 0.92                  # Startgehälter x0,92
    ki_arbeitslos: float = 0.015            # +1,5 Pp. Arbeitslosigkeit in den ersten 5 Berufsjahren
    lohnnarbe: tuple = (0.02, 0.05, 0.08)   # bleibende Lohneinbuße je Arbeitslosigkeit (Schmieder et al.:
                                            # 10-15 % nach Massenentlassung; Wechsellücken kosten weniger)
    p_bu: tuple = (0.001, 0.0015, 0.002)    # Berufsunfähigkeit je Jahr
    bu_rente: tuple = (0.45, 0.55, 0.65)    # Anteil des letzten Nettos (BU-Versicherung im Plan)
    bu_kosten: float = 900                  # BU-Prämie je Jahr (heutige Euro), ab dem ersten Job
    # Erbschaft: standardmäßig AUS - der Plan soll nicht vom Erben abhängen.
    # DIW 5/2021: ~10 % erhalten binnen 15 Jahren eine Erbschaft/Schenkung,
    # Median ~32 Tsd., Mittel ~85 Tsd. EUR; Eltern einer Kohorte 2008 sterben
    # meist, wenn das Kind 50-60 ist.
    erbe: bool = False
    p_erbe: tuple = (0.5, 0.6, 0.7)
    erbe_alter: tuple = (48, 55, 62)
    erbe_betrag: tuple = (30_000, 90_000, 250_000)   # heutige Euro
    betreuung_rest: tuple = (0.10, 0.20, 0.30)  # Anteil des Agenturgewinns, der als Betreuung weiterläuft
    # Krisen: Jahre, in denen Aktien stark fallen, treffen auch Job und Provision.
    krise_schwelle: float = -0.15
    p_arbeitslos: tuple = (0.02, 0.03, 0.05)        # je Jahr, normale Jahre (IAB: Akademiker 2-3,6 %)
    p_arbeitslos_krise: tuple = (0.05, 0.10, 0.18)  # je Jahr, Krisenjahre
    arbeitslos_verlust: tuple = (0.2, 0.35, 0.5)    # Anteil des Jahresnettos, der verloren geht
    krise_provision: tuple = (0.75, 0.85, 0.95)     # Vertriebseinkommen im Krisenjahr relativ
    krise_agentur: tuple = (0.7, 0.8, 0.9)          # Agenturgewinn im Krisenjahr relativ
    # Lebensereignisse (pro Person gerechnet, Kosten in heutigen Euro)
    lebensereignisse: bool = True
    p_partner: tuple = (0.6, 0.75, 0.85)            # feste Partnerschaft mit gemeinsamer Wohnung
    alter_partner: tuple = (24, 28, 33)
    ersparnis_partner: tuple = (0.0, 0.10, 0.20)    # geteilte Wohnung, aber oft größer
    p_kinder: tuple = (0.60, 0.72, 0.80)            # Destatis: ~20 % Kinderlose (Frauen 45-49)
    alter_kind: tuple = (30, 33.3, 37)              # Destatis: Väter beim 1. Kind im Mittel 33,3
    kosten_kinder: tuple = (5_000, 8_000, 12_000)   # eigener Anteil je Jahr, 18 Jahre (EVS 2018, 10. Dezil:
                                                    # 1.212 EUR bei 1 Kind, 2.024 bei 2; VPI x1,27,
                                                    # abzgl. Kindergeld, hälftig geteilt)
    # Immobilienkauf: Der Plan rät bis zum Ziel davon ab, trotzdem kaufen manche.
    p_haus: tuple = (0.2, 0.3, 0.4)
    haus_alter: tuple = (30, 34, 39)
    haus_preis: tuple = (350_000, 480_000, 650_000)
    haus_nk: tuple = (0.05, 0.07, 0.09)             # Grunderwerbsteuer, Notar, Makler: sofort weg
    p_heirat: tuple = (0.45, 0.55, 0.65)
    scheidung: tuple = (0.008, 0.013, 0.016)        # je Ehejahr (Destatis: 28 % der Ehen)
    scheidung_verlust: tuple = (0.10, 0.25, 0.40)   # Anteil des in der Ehe aufgebauten Vermögens (Zugewinn)
    betreuung_abgang: float = 0.20              # jährliche Kündigungen der verbliebenen Verträge


def weichenplan(wp: Weichen | None = None, ap: AgenturParameter | None = None,
                np_: NachfolgeParameter | None = None, protokoll: list | None = None) -> Strategie:
    """Agentur zuerst, dann die jeweils bessere Weiche.

    Zustände: studium | agentur -> (agentur weiter, ggf. Team) oder der erste
    machbare Rückfallweg (ch: Schweizer IT-Stelle, nur mit Abschluss; vertrieb:
    IT-/SaaS-Vertrieb; de: IT-Stelle in Deutschland) -> optional freelance
    (aus de) -> optional inhaber (Nachfolgekauf) -> ggf. ausgefallen.
    Jede Weiche folgt einer harten Zahl, nicht dem Gefühl.
    """
    wp, ap, np_ = wp or Weichen(), ap or AgenturParameter(), np_ or NachfolgeParameter()

    def leben(rng: random.Random, w: Welt) -> list[float]:
        d = lambda t: dreieck(rng, *t)  # noqa: E731
        lauf = AgenturLauf(rng, ap)
        nf_ab, nf_ek, nf_p = int(round(d(np_.ab_alter))), d(np_.eigenkapital_quote), d(np_.p_abschluss_je_jahr)
        nf_zins, nf_wachs, nf_hz, nf_buerg = d(np_.zins), d(np_.wachstum), d(np_.hazard), d(np_.buergschaft)
        nf_exit = d(np_.exit_multiple)
        if wp.lebensereignisse:
            partner_ab = d(wp.alter_partner) if rng.random() < d(wp.p_partner) else 999
            partner_faktor = 1 - d(wp.ersparnis_partner)
            kind_ab = d(wp.alter_kind) if rng.random() < d(wp.p_kinder) else 999
            kind_kosten = d(wp.kosten_kinder)
            heirat_ab = partner_ab + d((1, 3, 6)) if rng.random() < d(wp.p_heirat) else 999
            p_scheidung, scheidung_verlust = d(wp.scheidung), d(wp.scheidung_verlust)
        else:
            partner_ab = kind_ab = heirat_ab = 999
            partner_faktor, kind_kosten = 1.0, 0.0
            p_scheidung = scheidung_verlust = 0.0
        ki = rng.random() < d(wp.p_ki)
        ki_f = wp.ki_chancen if ki else 1.0
        p_vertrieb = d(wp.p_vertrieb)
        if rng.random() < wp.p_sommer_erfolg:
            p_vertrieb = min(0.95, p_vertrieb * wp.vertrieb_bonus_erfolg)
        glueck = {
            "ch": rng.random() < d(wp.p_stelle_ch) * ki_f,   # zählt nur mit Abschluss
            "ch_partner": rng.random() < wp.p_ch_mit_partner,
            "ch_zweiter": rng.random() < d(wp.p_ch_zweiter_anlauf) * ki_f,
            "vertrieb": rng.random() < p_vertrieb,
            "vertrieb_mit_abschluss": rng.random() < d(wp.p_vertrieb_mit_abschluss),
            "vertrieb_nach_abbruch": rng.random() < d(wp.p_vertrieb),
        }
        abschluss = {"wert": False, "abgebrochen": False}
        bricht_ab = rng.random() < d(wp.p_studienabbruch)

        lage = {"alter": START_ALTER, "war_ch": False}

        def moeglich(option: str) -> bool:
            if option == "ch":
                mit_partner = lage["alter"] >= partner_ab
                return abschluss["wert"] and glueck["ch"] and (glueck["ch_partner"] or not mit_partner)
            if option == "vertrieb":
                if abschluss["wert"]:
                    return glueck["vertrieb_mit_abschluss"]
                if abschluss["abgebrochen"]:
                    return glueck["vertrieb_nach_abbruch"]
                return glueck["vertrieb"]
            return option == "de"

        def studium_beenden() -> None:
            if bricht_ab:
                abschluss["abgebrochen"] = True
            else:
                abschluss["wert"] = True

        fl_ok = wp.freelance and rng.random() < d(wp.p_freelance)
        rk_hz, rk_lohn = d(wp.rueckkehr_ch), d(wp.rueckkehr_lohn)
        narbe, p_bu, bu_rente = d(wp.lohnnarbe), d(wp.p_bu), d(wp.bu_rente)
        lohnfaktor = 1.0
        bu_netto_real = None
        nach_ch = 0.0           # reales DE-Gehalt nach der Rückkehr aus der Schweiz
        aufgeben_ab = d((25, 32, 40)) if rng.random() < wp.p_aufgeben else 999
        erbe_ab = round(d(wp.erbe_alter)) if wp.erbe and rng.random() < d(wp.p_erbe) else 999
        erbe_betrag = d(wp.erbe_betrag)
        bindung = d((1, 1.6, 3)) if rng.random() < wp.p_dual_bindung else 0
        fl_satz, fl_aus, fl_hz = d(wp.satz), d(wp.auslastung), d(wp.hazard_freelance)
        hz_sdr, hz_ae, vt_rest = d(wp.hazard_sdr), d(wp.hazard_ae), d(wp.vertrieb_rest)
        vt_boden, grund_vt = d(wp.vertrieb_boden), d(wp.grund_vertrieb)
        p_al, p_al_krise, al_verlust = d(wp.p_arbeitslos), d(wp.p_arbeitslos_krise), d(wp.arbeitslos_verlust)
        kr_prov, kr_ag = d(wp.krise_provision), d(wp.krise_agentur)
        verheiratet, vermoegen_bei_heirat = False, 0.0
        nach_vertrieb = 0.0     # reales Gehalt nach dem Ausstieg aus dem Vertrieb
        letztes_brutto_real = 0.0
        pfade = {
            "ch": None,   # wird nach der Studienwahl angelegt (Start hängt am Weg)
            "vertrieb": _gehalt_pfad(rng, **dict(VERTRIEB, sprung_ab=wp.vertrieb_sprung_ab)),
            "de": _gehalt_pfad(rng, **dict(IT_BACHELOR, start=wp.start_de)),
            "de_bachelor": _gehalt_pfad(rng, **IT_BACHELOR),
            "de_ohne": _gehalt_pfad(rng, **dict(WEBDEV, start=(36_000, 42_000, 50_000))),
        }
        if ki:
            for pf in pfade.values():
                if pf is not None:
                    pf.g *= wp.ki_start
        lam_i = d(wp.lam_streu) if wp.lam_streu else wp.lam
        g_de, g_ch = _w(rng, wp.grund_de), _w(rng, wp.grund_ch)
        konsum_de = Konsum(g_de, lam_i, wp.traegheit)
        konsum_ch = Konsum(g_ch, lam_i, wp.traegheit)
        haus_ab = d(wp.haus_alter) if rng.random() < d(wp.p_haus) else 999
        haus_preis, haus_nk = d(wp.haus_preis), d(wp.haus_nk)
        studium = Konsum(12_000, 0.6)

        def rueckfall() -> str:
            for option in wp.rueckfall + ("de",):
                if moeglich(option):
                    return option
            return "de"

        pibs_platz = wp.erste_phase == "pibs" and rng.random() < d(wp.p_pibs_platz) * ki_f
        p_dual = d(wp.p_dual_platz) * ki_f
        if wp.erste_phase == "pibs":
            p_dual *= 0.85      # gleiches Bewerberprofil, Termine kollidieren
        if pibs_platz:
            zustand = "pibs"
        elif wp.erste_phase in ("dual", "pibs"):
            # Plan B ohne Platz: duales Studium, sonst Bachelor + Agentur
            zustand = "dual" if rng.random() < p_dual else "studium"
        elif wp.erste_phase == "vertrieb":
            # Plan B, falls 2027 keine Vertriebsstelle: Bachelor + Agentur,
            # danach Vertrieb (neuer Versuch mit Abschluss), Schweiz, Deutschland.
            zustand = "vertrieb" if moeglich("vertrieb") else "studium"
        else:
            zustand = wp.erste_phase
        studium_ende = (3 if wp.erste_phase in ("vertrieb", "dual", "pibs") else wp.studienjahre) \
            if zustand == "studium" else None
        programm_ende = {"pibs": 3, "dual": 2}.get(zustand, studium_ende - 1 if studium_ende else None)
        frueher_abbruch = rng.random() < wp.p_frueher_abbruch
        neustart = rng.random() < wp.p_neustart
        dual_brutto, bricht_dual_ab = d(wp.dual_brutto), rng.random() < d(wp.p_abbruch_dual)
        pibs_brutto, bricht_pibs_ab = d(wp.pibs_brutto), rng.random() < d(wp.p_abbruch_pibs)
        if pibs_platz:
            glueck["ch"] = rng.random() < d(wp.p_stelle_ch_nach_pibs) * ki_f
            pfade_ch_start = wp.start_ch_pibs
        else:
            pfade_ch_start = wp.start_ch
        studium_ch = Konsum(wp.grund_ch_studium, 0.6)
        dual_absolviert = False
        erste_stelle_jahr = None
        rueckfall_nach_studium = ("vertrieb", "ch", "de") if wp.erste_phase == "vertrieb" else wp.rueckfall
        rest_anteil = d(wp.betreuung_rest)
        agentur_tot = False
        nebenher = 0.0          # weiterlaufende Betreuungsverträge (real, vor Steuer)
        depot, pk = Depot(1_000.0), 0.0
        schuld = ebitda = 0.0
        berufsjahre = 0
        werte: list[float] = []
        for j in range(JAHRE):
            idx = w.index(j)
            alter = START_ALTER + j
            zusatz = 0.0
            krise = w.renditen[j] < wp.krise_schwelle
            zustand_anfang = zustand
            # Lebensereignisse verschieben den Grundbedarf dieses Jahres
            faktor = partner_faktor if alter >= partner_ab else 1.0
            konsum_de.grundbedarf = (max(grund_vt, g_de) if zustand == "vertrieb" else g_de) * faktor
            konsum_ch.grundbedarf = g_ch * faktor
            lam_jahr = lam_i if alter < aufgeben_ab else (1 + lam_i) / 2
            konsum_de.lam = konsum_ch.lam = min(0.95, lam_jahr + (wp.lam_partner if alter >= partner_ab else 0.0))
            kinder_jahr = kind_kosten * idx if kind_ab <= alter < kind_ab + 18 else 0.0
            if zustand == "ch" and kinder_jahr:
                kinder_jahr *= wp.ch_kinder_faktor if alter < kind_ab + 4 else 1.1

            lage["alter"] = alter
            if pfade["ch"] is None:
                pfade["ch"] = _gehalt_pfad(rng, pfade_ch_start, (0.02, 0.035, 0.055),
                                           wp.ch_wachstum_spaet, 10, (0.2, 0.25, 0.32))
                if ki:
                    pfade["ch"].g *= wp.ki_start
            if zustand == "pibs":
                netto = pibs_brutto * idx * (1 - 0.064 - 0.05)   # AHV/ALV, kaum Steuer
                # Gleiche Familienhilfe wie im deutschen Studium (dort trägt sie die Lücke
                # zwischen 6.000 EUR Nebenjob und 12.000 EUR Bedarf); was darüber hinaus
                # fehlt, wird Schuld (Studienkredit).
                sparen = netto + 6_000 * idx - wp.grund_ch_studium * idx
                if bricht_pibs_ab and frueher_abbruch and j == 0:
                    bricht_pibs_ab = False
                    # PiBS-Vorteile entfallen: normale Chance auf die Schweiz, normaler Start
                    glueck["ch"] = rng.random() < d(wp.p_stelle_ch) * ki_f
                    pfade["ch"] = _gehalt_pfad(rng, wp.start_ch, (0.02, 0.035, 0.055),
                                               wp.ch_wachstum_spaet, 10, (0.2, 0.25, 0.32))
                    if ki:
                        pfade["ch"].g *= wp.ki_start
                    if neustart:    # Neustart in DE: dual, sonst Bachelor (Studium ab Jahr 1)
                        if rng.random() < p_dual / 0.85:
                            zustand, programm_ende = "dual", j + 3
                        else:
                            zustand, studium_ende = "studium", j + 4
                            bricht_ab = rng.random() < d(wp.p_studienabbruch)
                    else:
                        abschluss["abgebrochen"] = True
                        zustand = "de"
                elif j == programm_ende:
                    if bricht_pibs_ab:
                        abschluss["abgebrochen"] = True
                        zustand = "de"
                    else:
                        abschluss["wert"] = True
                        zustand = "ch" if glueck["ch"] else "de"
            elif zustand == "dual":
                netto = netto_angestellt(dual_brutto * idx, idx, j)
                sparen = netto - studium.ausgaben(netto, idx)
                if bricht_dual_ab and frueher_abbruch and j == programm_ende - 2:
                    bricht_dual_ab = False
                    if neustart:    # Neustart: Bachelor + Agentur
                        zustand, studium_ende = "studium", j + 4
                        bricht_ab = rng.random() < d(wp.p_studienabbruch)
                    else:
                        abschluss["abgebrochen"] = True
                        zustand = "de"
                elif j == programm_ende:
                    if bricht_dual_ab:
                        abschluss["abgebrochen"] = True
                        zustand = "de"
                    else:
                        abschluss["wert"] = True
                        dual_absolviert = True
                        # Bindungsklausel: erst einige Jahre im Ausbildungsbetrieb
                        zustand = "de" if bindung else rueckfall()
            elif zustand == "studium" and agentur_tot:
                # Agentur aufgegeben: weiterstudieren mit Nebenjob.
                gewinn = 0.0
                netto = 6_000 * idx
                sparen = netto - studium.ausgaben(netto, idx)
                if j == studium_ende - 1:
                    studium_beenden()
                    zustand = next((o for o in rueckfall_nach_studium + ("de",) if moeglich(o)), "de")
            elif zustand in ("studium", "agentur"):
                im_studium = zustand == "studium"
                if im_studium and bricht_ab and frueher_abbruch and j == studium_ende - 3:
                    # Abbruch im ersten Jahr: ohne Abschluss in den Beruf (Agentur läuft weiter).
                    # bricht_ab bleibt True, damit studium_beenden() keinen Abschluss vergibt.
                    abschluss["abgebrochen"] = True
                    studium_ende = j + 1
                gewinn = lauf.jahr(j, idx, 900 if im_studium else 2_000, wachsen=not im_studium)
                if krise:
                    gewinn *= kr_ag
                netto = netto_selbststaendig(gewinn, idx, j)
                sparen = netto - (studium if im_studium else konsum_de).ausgaben(netto, idx)
                zusatz += lauf.firmenwert(idx)
                if lauf.endet():
                    zusatz = 0.0
                    if im_studium and j < studium_ende - 1:
                        agentur_tot = True
                    else:
                        if im_studium:
                            studium_beenden()
                        zustand = rueckfall() if not im_studium else next(
                            (o for o in rueckfall_nach_studium + ("de",) if moeglich(o)), "de")
                elif zustand == "studium" and j == studium_ende - 1:
                    studium_beenden()
                    vollzeit = gewinn / idx * 2_000 / 900 * 0.8
                    if vollzeit >= wp.agentur_schwelle_real:
                        zustand = "agentur"
                    else:
                        nebenher = max(0.0, gewinn / idx) * rest_anteil
                        zustand = next((o for o in rueckfall_nach_studium + ("de",) if moeglich(o)), "de")
                elif (zustand == "agentur" and wp.erste_phase == "agentur"
                      and j == wp.pruefjahre - 1 and lauf.fte < 1):
                    if gewinn / idx < wp.agentur_schwelle_real:
                        # Bewusster Wechsel: Betreuungsverträge laufen nebenher weiter.
                        nebenher = max(0.0, gewinn / idx) * rest_anteil
                        zustand = rueckfall()
            elif zustand == "freelance":
                next(pfade["de" if dual_absolviert else "de_bachelor"])   # Anstellungspfad altert mit
                fl_satz *= 1.01                   # Erfahrung: real +1 %/Jahr
                umsatz = 1_700 * fl_aus * fl_satz * idx * math.exp(rng.gauss(0, 0.12))
                if krise:
                    umsatz *= kr_ag
                netto = netto_selbststaendig(umsatz * 0.86, idx, j)   # ~780 EUR/Monat Betriebsausgaben
                sparen = netto - konsum_de.ausgaben(netto, idx)
                if rng.random() < fl_hz:
                    zustand = "de"
            elif bu_netto_real is not None:
                netto = bu_netto_real * idx
                sparen = netto - (konsum_ch if zustand == "ch" else konsum_de).ausgaben(netto, idx)
            elif zustand in ("ch", "vertrieb", "de", "ausgefallen", "nach_vertrieb", "nach_ch"):
                berufsjahre += 1
                if erste_stelle_jahr is None:
                    erste_stelle_jahr = j
                # Rückkehr aus der Schweiz
                if zustand == "ch":
                    lage["war_ch"] = True
                    if rng.random() < rk_hz + (wp.rueckkehr_ch_kind if alter >= kind_ab else 0.0):
                        zustand = "nach_ch"
                        basis_lohn = letztes_brutto_real or pfade["ch"].g * lohnfaktor
                        nach_ch = basis_lohn / lohnfaktor * rk_lohn   # Narbe wirkt unten einmal
                # Bindungsklausel abgelaufen / zweiter Anlauf auf die Schweiz
                if zustand == "de" and abschluss["wert"] and not lage["war_ch"] and "ch" in wp.rueckfall:
                    if bindung and berufsjahre == round(bindung) + 1 and moeglich("ch"):
                        zustand = "ch"
                    elif berufsjahre == 5 and glueck["ch_zweiter"] and (glueck["ch_partner"] or alter < partner_ab):
                        zustand = "ch"
                        pfade["ch"].g *= 1.1    # 4 Jahre Berufserfahrung
                hz_vt = hz_ae if pfade["vertrieb"].befoerdert else hz_sdr
                if zustand == "vertrieb" and berufsjahre > 1 and rng.random() < hz_vt:
                    zustand = "nach_vertrieb"
                    nach_vertrieb = min(max(letztes_brutto_real / lohnfaktor * vt_rest, vt_boden),
                                        wp.vertrieb_deckel)
                art = "de" if zustand == "ausgefallen" else zustand
                if art == "de" and not abschluss["wert"]:
                    art = "de_ohne"
                elif art == "de" and not dual_absolviert:
                    art = "de_bachelor"     # Bachelor oder PiBS: Einstieg auf Bachelor-Niveau
                if art == "nach_vertrieb":
                    nach_vertrieb *= 1 + rng.gauss(0.008, 0.015)
                    brutto = nach_vertrieb * idx
                elif art == "nach_ch":
                    nach_ch *= 1 + rng.gauss(0.008, 0.015)
                    brutto = nach_ch * idx
                else:
                    brutto = next(pfade[art]) * idx
                brutto *= lohnfaktor
                letztes_brutto_real = brutto / idx
                if krise and art == "vertrieb":
                    brutto *= kr_prov
                p_al_jahr = p_al_krise if krise else p_al
                if ki and j - erste_stelle_jahr < 5:
                    p_al_jahr += wp.ki_arbeitslos
                arbeitslos = rng.random() < p_al_jahr
                if arbeitslos:
                    lohnfaktor *= 1 - narbe       # Lohnnarbe bleibt
                if art == "ch":
                    real = brutto / idx
                    st = min(0.30, max(0.06, 0.06 + 0.08 * math.log(max(real, 60_000) / 60_000)))
                    st += wp.ch_steuer_zuschlag
                    netto = brutto * (1 - wp.ch_abgaben - (wp.ch_pk_an if alter >= 25 else 0.01) - st)
                    gutschrift = brutto * wp.ch_pk_gutschrift if alter >= 25 else 0.0
                    if arbeitslos:
                        gutschrift *= 1 - al_verlust
                    pk = pk * (1 + wp.ch_pk_zins) + gutschrift
                    if arbeitslos:
                        netto *= 1 - al_verlust
                    sparen = netto - konsum_ch.ausgaben(netto, idx)
                else:
                    netto = netto_angestellt(brutto, idx, j)
                    if arbeitslos:
                        netto *= 1 - al_verlust
                    sparen = netto - konsum_de.ausgaben(netto, idx)
                sparen -= wp.bu_kosten * idx
                if rng.random() < p_bu:
                    bu_netto_real = bu_rente * netto / idx
            else:  # inhaber
                ebitda *= (1 + nf_wachs + w.inflation) * math.exp(rng.gauss(0, np_.schock_sigma))
                if rng.random() < nf_hz:
                    depot.entnehmen(nf_buerg * schuld)
                    if depot.wert < 0:
                        depot = Depot(0.0)
                    zustand, schuld = "ausgefallen", 0.0
                    werte.append(depot.netto + pk)
                    if protokoll is not None:
                        protokoll.append((zustand, depot.netto, pk, dict(abschluss)))
                    continue
                gehalt = np_.gehalt_inhaber * idx
                vor = ebitda - gehalt - schuld * nf_zins - 0.03 * ebitda
                frei = vor * 0.70 if vor > 0 else vor
                soll = schuld / np_.tilgungsjahre if schuld > 0 else 0.0
                if frei < soll:
                    depot.entnehmen(soll - frei)
                    tilgung, ueber = soll, 0.0
                else:
                    tilgung = min(schuld, frei)
                    ueber = frei - tilgung
                schuld = max(0.0, schuld - tilgung)
                netto = netto_angestellt(gehalt, idx, j)
                sparen = netto - konsum_de.ausgaben(netto, idx) + ueber * 0.74
                zusatz += max(0.0, ebitda * nf_exit - schuld) * 0.7

            # Kinderkosten verdrängen auch eigenen Konsum: Wie jeder andere Euro gehen sie
            # nur zum Sparanteil (1 - lam) zulasten des Depots (Studium: voll).
            if zustand_anfang in ("studium", "dual", "pibs"):
                sparen -= kinder_jahr
            else:
                sparen -= kinder_jahr * (1 - konsum_de.lam)
            if nebenher > 0 and zustand_anfang not in ("studium", "agentur"):
                sparen += nebenher * idx * 0.55 * (1 - konsum_de.lam)   # nach Grenzsteuer + KV, Sparregel
                nebenher *= 1 - wp.betreuung_abgang
            if alter == erbe_ab:
                sparen += erbe_betrag * idx
            depot.jahr(sparen, w.renditen[j])
            if alter >= haus_ab and depot.netto > 0.3 * haus_preis * idx:
                depot.entnehmen(haus_nk * haus_preis * idx)
                haus_ab = 999
            if not verheiratet and alter >= heirat_ab:
                verheiratet, vermoegen_bei_heirat = True, depot.netto
            elif verheiratet and rng.random() < p_scheidung:
                depot.entnehmen(scheidung_verlust * max(0.0, depot.netto - vermoegen_bei_heirat))
                verheiratet, heirat_ab = False, 999
                partner_ab = 999                 # Trennung: geteilte Wohnung entfällt

            if zustand == "de" and fl_ok and abschluss["wert"] and berufsjahre >= wp.freelance_nach_jahren:
                fl_ok = False
                if 1_700 * fl_aus * fl_satz * 0.86 > 1.2 * letztes_brutto_real:
                    zustand = "freelance"        # nur, wenn es sich deutlich lohnt

            if (wp.nachfolge and zustand in ("ch", "vertrieb", "de", "agentur", "freelance", "nach_vertrieb", "nach_ch")
                    and lauf.fte < 3 and alter >= nf_ab and rng.random() < nf_p):
                e = d(np_.ebitda) * idx
                kaufpreis = e * d(np_.kaufmultiple)
                ek = max(kaufpreis * nf_ek, np_.min_eigenkapital * idx)
                if depot.netto >= ek * 1.3:      # Puffer: nicht das letzte Geld einsetzen
                    depot.entnehmen(ek)
                    zustand, ebitda, schuld = "inhaber", e, kaufpreis - ek
                    lauf.fte = 0.0
                    zusatz = max(0.0, kaufpreis - schuld) * 0.7
            werte.append(depot.netto + pk + zusatz)
            if protokoll is not None:
                protokoll.append((zustand, depot.netto, pk, dict(abschluss)))
        return werte

    return leben


STRATEGIEN: dict[str, tuple[str, Strategie]] = {}


def _registrieren() -> None:
    """Alle Kandidaten laufen durch dasselbe Modell (weichenplan) mit denselben
    Risiken - Krisen, Arbeitslosigkeit, Studienabbruch, Partnerschaft, Kinder,
    Scheidung - und derselben Sparregel. Nur so ist der Vergleich fair.
    """
    from dataclasses import replace
    s = STRATEGIEN
    basis = Weichen(nachfolge=False, lam=0.4, lam_streu=PLAN.lam_streu)
    s["bachelor_ch"] = ("Bachelor Informatik + Agentur, dann CH/DE",
                        weichenplan(replace(basis, rueckfall=("ch", "de"))))
    s["master_ch"] = ("Master Informatik + Agentur, dann CH/DE",
                      weichenplan(replace(basis, studienjahre=5, rueckfall=("ch", "de"),
                                          start_de=IT_UNI["start"], start_ch=(80_000, 95_000, 115_000),
                                          p_stelle_ch=(0.30, 0.50, 0.70))))
    s["dual"] = ("Duales Studium (sonst Bachelor), dann CH/DE",
                 weichenplan(replace(basis, erste_phase="dual", rueckfall=("ch", "de"),
                                     start_de=DUAL["start"])))
    s["bachelor_de"] = ("Bachelor + Agentur, dann nur DE (keine Schweiz)",
                        weichenplan(replace(basis, rueckfall=("de",))))
    s["bachelor_vertrieb"] = ("Bachelor + Agentur, dann Vertrieb/CH/DE",
                              weichenplan(replace(basis, rueckfall=("vertrieb", "ch", "de"))))
    s["vertrieb_zuerst"] = ("Vertrieb ab 2027 (Plan B: Bachelor)",
                            weichenplan(replace(basis, erste_phase="vertrieb", rueckfall=("de",))))
    s["agentur_zuerst"] = ("2 J. Agentur Vollzeit, dann Vertrieb/DE",
                           weichenplan(replace(basis, erste_phase="agentur", pruefjahre=2,
                                               rueckfall=("vertrieb", "de"))))
    s["bachelor_ch_nf"] = ("Bachelor + Agentur, CH/DE, + Nachfolgekauf",
                           weichenplan(replace(basis, rueckfall=("ch", "de"), nachfolge=True)))
    s["plan_ohne_ch"] = ("Plan, aber ohne Schweiz",
                         weichenplan(replace(PLAN, rueckfall=("de",))))
    s["plan_typisch"] = ("Plan, aber spart wie typische Gutverdiener",
                         weichenplan(replace(PLAN, lam_streu=(0.50, 0.62, 0.75))))
    s["plan_perfekt"] = ("Plan, Sparregel 60 % perfekt eingehalten",
                         weichenplan(replace(PLAN, lam_streu=None, lam=0.4, p_aufgeben=0.0)))
    s["plan_erbe"] = ("Plan mit typischem Elternerbe",
                      weichenplan(replace(PLAN, erbe=True)))
    s["pibs_sicher"] = ("Plan mit sicherem PiBS-Platz",
                        weichenplan(replace(PLAN, p_pibs_platz=(1, 1, 1))))
    s["plan"] = ("EMPFOHLEN: PiBS > dual > Bachelor, dann CH/DE", weichenplan(PLAN))

# --------------------------------------------------------------------------
# Auswertung
# --------------------------------------------------------------------------


def simulieren(strategie: Strategie, n: int, seed: int = 2027) -> list[list[float]]:
    rng = random.Random(seed)
    return [strategie(rng, Welt.ziehen(rng)) for _ in range(n)]


def quote_bis_alter(leben: list[list[float]], alter: int) -> float:
    """Anteil der Leben mit >= 1 Mio. am Ende des Lebensjahres ``alter``.

    Jahr j läuft von Alter START_ALTER + j bis START_ALTER + j + 1 (Sep-Aug);
    werte[j] ist der Stand an dessen Ende.
    """
    j = alter - START_ALTER - 1
    return sum(1 for w in leben if w[j] >= ZIEL) / len(leben)


def fruehestes_alter(leben: list[list[float]], schwelle: float = 0.5) -> int | None:
    for alter in range(START_ALTER + 1, END_ALTER + 1):
        if quote_bis_alter(leben, alter) >= schwelle:
            return alter
    return None


def mehrfach(strategie: Strategie, n: int = 10_000, seeds: tuple = (2027, 1, 2, 3),
             alter: tuple = (35, 40, 45, 50, 55, 60)) -> dict:
    """Quoten über mehrere Seeds gemittelt, mit 95-%-Intervall und 50-%-Alter.

    Zusätzlich: ohne Pensionskasse gerechnet geht nicht ohne neuen Lauf; dafür
    gibt es ``real``: P(1 Mio. in Kaufkraft von 2026), mit der Inflation des
    jeweiligen Lebens zurückgerechnet.
    """
    quoten = {a: [] for a in alter}
    real = {a: [] for a in alter}
    ab = []
    for sd in seeds:
        rng = random.Random(sd)
        leben, welten = [], []
        for _ in range(n):
            w = Welt.ziehen(rng)
            leben.append(strategie(rng, w))
            welten.append(w)
        for a in alter:
            j = a - START_ALTER - 1
            quoten[a].append(sum(1 for x in leben if x[j] >= ZIEL) / n)
            # Stichtag Ende August: Preisniveau ein halbes Jahr nach Jahresmitte
            real[a].append(sum(1 for x, w in zip(leben, welten)
                               if x[j] / (w.index(j) * (1 + w.inflation) ** 0.5) >= ZIEL) / n)
        ab.append(fruehestes_alter(leben))
    erg = {}
    for a in alter:
        p = sum(quoten[a]) / len(seeds)
        erg[a] = (p, konfidenz(p, n * len(seeds)), sum(real[a]) / len(seeds))
    erg["ab"] = ab
    return erg


def konfidenz(p: float, n: int) -> float:
    """Halbe Breite des 95-%-Intervalls (Normalapproximation)."""
    return 1.96 * math.sqrt(max(p * (1 - p), 1e-9) / n)


# --------------------------------------------------------------------------
# Sommer 2027: die Obergrenze
# --------------------------------------------------------------------------


def sommer_2027(start: float = 5_000.0) -> None:
    print("Sommer 2027: Wie wahrscheinlich ist 1 Mio. EUR aus", f"{start:,.0f} EUR?".replace(",", "."))
    print("-" * 64)
    print(f"  Obergrenze für JEDE Strategie bei fairem Spiel (Ville):  {start / ZIEL:.2%}")
    # Roulette, einfache Chance, kühnes Spiel (nach Dubins/Savage optimal bei
    # ungünstigem Spiel): immer alles setzen, was bis zum Ziel fehlt.
    p = 18 / 37
    rng = random.Random(1)
    n, treffer = 200_000, 0
    for _ in range(n):
        k = start
        while 0 < k < ZIEL:
            einsatz = min(k, ZIEL - k)
            k += einsatz if rng.random() < p else -einsatz
        treffer += k >= ZIEL
    print(f"  Roulette, kühnes Spiel (beste Strategie), simuliert:     {treffer / n:.2%}")
    # Aktien-ETF mit Hebel über 8 Monate: selbst mit positivem Drift
    rng = random.Random(2)
    for hebel in (1, 3, 10):
        n, treffer = 100_000, 0
        mu, sig, t = 0.072, 0.16, 8 / 12
        for _ in range(n):
            k = start
            for _m in range(8):
                r = rng.gauss(mu / 12, sig / math.sqrt(12))
                k *= max(0.0, 1 + hebel * r)
            treffer += k >= ZIEL
        print(f"  Welt-ETF mit Hebel {hebel:>2}, 8 Monate:                      {treffer / n:.3%}")
    print()


# Der empfohlene Plan (Ergebnis des fairen Vergleichs und zweier Gegenprüfungen):
# bis Sommer 2027 Webgeschäft neben dem Abitur; dann PiBS in der Schweiz, wenn
# ein Platz kommt, sonst duales Studium Informatik, sonst Bachelor + Agentur;
# danach Stelle in der Schweiz (oder später im zweiten Anlauf), sonst in
# Deutschland. Sparregel: Grundbedarf ~18.000 EUR/Jahr in Deutschland bzw.
# ~38.000 EUR in der Schweiz (heutige Euro), von jedem Euro darüber werden je
# Leben 38-62 % gespart (Regel: 60 %; realistisch im Mittel ~50 %, 15 % geben auf).
PLAN = Weichen(erste_phase="pibs", rueckfall=("ch", "de"), start_de=DUAL["start"],
               nachfolge=False, lam=0.4, lam_streu=(0.38, 0.47, 0.62))


def sensitivitaet(n: int = 3_000, basis: Weichen = PLAN) -> None:
    """Welche Annahme verschiebt den empfohlenen Plan am stärksten?

    Jede Annahme wird einzeln auf ihren pessimistischen bzw. optimistischen
    Rand festgesetzt, alle anderen bleiben unsicher. Gezeigt werden das
    50-%-Alter und die Chance mit 40.
    """
    from dataclasses import replace

    def kennzahl(strat: Strategie) -> str:
        leben = simulieren(strat, n)
        ab = fruehestes_alter(leben)
        return f"{ab if ab else '>60':>4} / {quote_bis_alter(leben, 50):4.0%}"

    print(f"Sensitivität des Plans (50-%-Alter / Chance mit 50), Basis: {kennzahl(weichenplan(basis))}")
    print("-" * 84)
    faelle: list[tuple[str, Strategie, Strategie]] = []
    wp = basis
    faelle.append(("Schweizer Stelle (nie / sicher)",
                   weichenplan(replace(wp, p_stelle_ch=(0, 0, 0))),
                   weichenplan(replace(wp, p_stelle_ch=(1, 1, 1)))))
    faelle.append(("Dualer Studienplatz (nie / sicher)",
                   weichenplan(replace(wp, p_dual_platz=(0, 0, 0))),
                   weichenplan(replace(wp, p_dual_platz=(1, 1, 1)))))
    faelle.append(("Sparen wie typische Gutverdiener / perfekt nach Regel",
                   weichenplan(replace(wp, lam_streu=(0.50, 0.62, 0.75))),
                   weichenplan(replace(wp, lam_streu=None, lam=0.35))))
    faelle.append(("Grundbedarf (22 / 13 Tsd. EUR im Jahr)",
                   weichenplan(replace(wp, grund_de=22_000, grund_ch=40_000)),
                   weichenplan(replace(wp, grund_de=13_000, grund_ch=30_000))))
    faelle.append(("Rückkehr aus der Schweiz (4 %/J. / nie)",
                   weichenplan(replace(wp, rueckkehr_ch=(0.04, 0.04, 0.04))),
                   weichenplan(replace(wp, rueckkehr_ch=(0, 0, 0), rueckkehr_ch_kind=0.0))))
    faelle.append(("KI-Szenario für Einsteiger (sicher / nie)",
                   weichenplan(replace(wp, p_ki=(1, 1, 1))),
                   weichenplan(replace(wp, p_ki=(0, 0, 0)))))
    faelle.append(("Kinder (sicher, teuer / keine)",
                   weichenplan(replace(wp, p_kinder=(1, 1, 1), kosten_kinder=(8_000, 8_000, 8_000))),
                   weichenplan(replace(wp, p_kinder=(0, 0, 0)))))
    welt_alt = Welt.ziehen

    ergebnisse = []
    for text, schlecht, gut in faelle:
        ergebnisse.append((text, kennzahl(schlecht), kennzahl(gut)))
    try:
        Welt.ziehen = classmethod(lambda cls, rng: welt_alt.__func__(cls, rng, geo=0.04))
        a_ = kennzahl(weichenplan(wp))
        Welt.ziehen = classmethod(lambda cls, rng: welt_alt.__func__(cls, rng, geo=0.08))
        b_ = kennzahl(weichenplan(wp))
    finally:
        Welt.ziehen = welt_alt
    ergebnisse.append(("Aktienrendite 4 % / 8 % geometrisch", a_, b_))
    for text, a_, b_ in ergebnisse:
        print(f"  {text:44s} pessimistisch {a_}   optimistisch {b_}")
    print()


def kontrollwerte(strategie: Strategie | None = None, n: int = 6_000,
                  alter: tuple = (25, 30, 35, 40, 45, 50, 55)) -> dict[int, tuple[float, float, float]]:
    """Vermögen (nach Steuer, nominal) je Alter: 25-, 50- und 75-%-Quantil.

    Damit lässt sich der eigene Stand später einordnen: Wer unter dem
    25-%-Wert liegt, ist hinter dem Plan und muss nachsteuern.
    """
    leben = simulieren(strategie or weichenplan(PLAN), n)
    erg = {}
    for a in alter:
        werte = sorted(w[a - START_ALTER - 1] for w in leben)
        erg[a] = (werte[len(werte) // 4], werte[len(werte) // 2], werte[3 * len(werte) // 4])
    return erg


def sommer_meilensteine(n: int = 20_000, seed: int = 7, ausgabe: bool = True) -> dict[str, float]:
    """Was ist bis 31.08.2027 mit >= 50 % erreichbar - neben dem Abitur?

    Zeit: Dez-März ~5 h/Woche (17 Wochen), April bis Mitte Mai Prüfungen
    (0 h), Mitte Mai bis Ende August ~25 h/Woche (15 Wochen). Davon wird nur
    ein Teil wirklich gearbeitet (Disziplin 50-100 %).

    Quoten: die Werte aus ``standortcheck plan`` (Vor-Ort-Einstieg 6,1 % je
    Kontakt), aber halbiert als Mitte angesetzt, weil sie noch nicht gemessen
    sind. Ablauf je Kontakt: Besuch mit ausgedrucktem Bericht, Einstiegsangebot,
    nach gelieferter Maßnahme ein Teil Paketkunden mit Betreuungsvertrag.
    """
    rng = random.Random(seed)
    umsaetze, kunden, pakete, betreuung = [], [], [], []
    for _ in range(n):
        disziplin = dreieck(rng, 0.5, 0.8, 1.0)
        stunden = (17 * dreieck(rng, 3, 5, 8) + 15 * dreieck(rng, 15, 25, 35)) * disziplin
        stunden -= 15                                  # Gewerbe, eigene Seite, Einrichtung
        p_einstieg = dreieck(rng, 0.01, 0.03, 0.07)
        p_upsell = dreieck(rng, 0.10, 0.25, 0.40)
        h_kontakt = dreieck(rng, 0.33, 0.45, 0.7)      # inkl. Fahrt und Nachbereitung
        # Begrenzt durch erreichbare Betriebe: OpenStreetMap lieferte im
        # Feldtest nur 35 Betriebe aus 4 Gewerken in 15 km um Regensburg;
        # mehr Leads kosten Handrecherche (Gelbe Seiten, Kammerverzeichnis).
        kontakte_max = int(dreieck(rng, 80, 180, 400))
        u = 0.0
        k = pk = 0
        # Netzwerk zuerst: Familie, Bekannte, Vereine
        for _ in range(int(dreieck(rng, 5, 15, 30))):
            if stunden <= 0:
                break
            stunden -= 0.5
            if rng.random() < dreieck(rng, 0.04, 0.10, 0.18):
                u += dreieck(rng, 69, 200, 349); k += 1; stunden -= 2.5
        while stunden > 0 and kontakte_max > 0:
            kontakte_max -= 1
            stunden -= h_kontakt
            if rng.random() < p_einstieg:
                u += dreieck(rng, 69, 200, 349); k += 1; stunden -= 2.5
                if rng.random() < p_upsell and stunden > 25:
                    u += dreieck(rng, 1_400, 1_900, 2_600); pk += 1; stunden -= dreieck(rng, 18, 28, 40)
        umsaetze.append(u); kunden.append(k); pakete.append(pk)
        betreuung.append(pk * dreieck(rng, 0.5, 0.7, 0.9))
    kunden_roh, pakete_roh = list(kunden), list(pakete)
    umsaetze.sort(); kunden.sort(); pakete.sort()

    def q(liste, anteil):
        return liste[int(len(liste) * anteil)]

    ergebnis = {
        "umsatz_median": q(umsaetze, 0.5), "umsatz_p25": q(umsaetze, 0.25),
        "umsatz_p75": q(umsaetze, 0.75), "kunden_median": q(kunden, 0.5),
        "pakete_median": q(pakete, 0.5),
        "p_mind_1_paket": sum(1 for x in pakete if x >= 1) / n,
        "p_mind_5_kunden": sum(1 for x in kunden if x >= 5) / n,
        "p_paket_und_5_kunden": sum(1 for k, pk in zip(kunden_roh, pakete_roh) if k >= 5 and pk >= 1) / n,
        "p_umsatz_3000": sum(1 for x in umsaetze if x >= 3_000) / n,
        "p_umsatz_5000": sum(1 for x in umsaetze if x >= 5_000) / n,
        "p_umsatz_10000": sum(1 for x in umsaetze if x >= 10_000) / n,
    }
    if not ausgabe:
        return ergebnis
    print("Bis 31.08.2027 neben dem Abitur (Webagentur, Vor-Ort-Ansprache):")
    print("-" * 64)
    print(f"  Umsatz: Median {ergebnis['umsatz_median']:,.0f} EUR "
          f"(25-75 %: {ergebnis['umsatz_p25']:,.0f} - {ergebnis['umsatz_p75']:,.0f})".replace(",", "."))
    print(f"  Kunden: Median {ergebnis['kunden_median']}, davon Pakete {ergebnis['pakete_median']}")
    for schluessel, text in (("p_mind_5_kunden", "mindestens 5 zahlende Kunden"),
                             ("p_mind_1_paket", "mindestens 1 Website-Paket"),
                             ("p_umsatz_3000", "mindestens 3.000 EUR Umsatz"),
                             ("p_umsatz_5000", "mindestens 5.000 EUR Umsatz"),
                             ("p_umsatz_10000", "mindestens 10.000 EUR Umsatz")):
        print(f"  P({text}):".ljust(48) + f"{ergebnis[schluessel]:.0%}")
    print()
    return ergebnis


_registrieren()


# --------------------------------------------------------------------------


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--n", type=int, default=4_000)
    ap.add_argument("--sommer", action="store_true")
    a = ap.parse_args()
    sommer_2027()
    if a.sommer:
        return
    print(f"Wahrscheinlichkeit, mit Alter X Millionär zu sein (n = {a.n} Leben je Strategie)")
    print("-" * 96)
    alter_spalten = (30, 35, 40, 45, 50, 55, 60)
    print(f"  {'Strategie':44s}" + "".join(f"{x:>7d}" for x in alter_spalten) + "   50 % ab")
    for name, (titel, strat) in STRATEGIEN.items():
        leben = simulieren(strat, a.n)
        quoten = [quote_bis_alter(leben, x) for x in alter_spalten]
        ab = fruehestes_alter(leben)
        print(f"  {titel[:44]:44s}" + "".join(f"{q:>7.0%}" for q in quoten)
              + f"   {ab if ab else '> 60':>6}")
    print()


if __name__ == "__main__":
    main()
