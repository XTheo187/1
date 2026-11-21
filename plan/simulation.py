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
END_ALTER = 50
JAHRE = END_ALTER - START_ALTER + 1


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


def netto_angestellt(brutto: float, index: float) -> float:
    """Netto aus Bruttogehalt: Sozialabgaben Arbeitnehmeranteil + Steuer.

    KV 7,3 % + halber Zusatzbeitrag 1,45 %, PV 2,4 % (kinderlos), bis zur
    BBG KV 69.750 EUR; RV 9,3 % + AV 1,3 % bis BBG RV 101.400 EUR (Werte 2026).
    """
    bbg_kv = 69_750 * index
    bbg_rv = 101_400 * index
    kvpv = min(brutto, bbg_kv) * (0.073 + 0.0145 + 0.024)
    rvav = min(brutto, bbg_rv) * (0.093 + 0.013)
    sozial = kvpv + rvav
    zve = brutto - 1_230 * index - kvpv * 0.96 - min(rvav, 0.093 * bbg_rv)
    return brutto - sozial - steuer(zve, index)


def netto_selbststaendig(gewinn: float, index: float) -> float:
    """Netto aus Gewinn eines Einzelunternehmens.

    Freiwillige KV/PV rund 19,7 % vom Gewinn, mindestens auf ca. 1.250 EUR
    Monatseinkommen, höchstens bis BBG. Keine Pflicht-RV (Altersvorsorge
    läuft über das ETF-Depot und zählt dort mit). Gewerbesteuer wird bei
    Hebesatz um 400 % weitgehend auf die Einkommensteuer angerechnet und
    deshalb nicht gesondert angesetzt.
    """
    if gewinn <= 0:
        return gewinn - 1_250 * 12 * 0.197 * index
    basis = min(max(gewinn, 1_250 * 12 * index), 69_750 * index)
    kvpv = basis * 0.197
    return gewinn - kvpv - steuer(gewinn - kvpv, index)


# --------------------------------------------------------------------------
# Gemeinsame Bausteine eines Lebens
# --------------------------------------------------------------------------


def dreieck(rng: random.Random, low: float, mid: float, high: float) -> float:
    return rng.triangular(low, high, mid)


@dataclass
class Welt:
    """Was für alle Strategien in einem simulierten Leben gleich ist."""

    rendite: float          # erwartete nominale ETF-Rendite p.a. (arithmetisch)
    vola: float             # Volatilität p.a.
    inflation: float
    renditen: list[float] = field(default_factory=list)  # Jahresrenditen

    @classmethod
    def ziehen(cls, rng: random.Random) -> "Welt":
        # MSCI World in EUR seit 1970: rund 7-8,5 % nominal, Vola um 15 %.
        # Die Spanne reicht bewusst tiefer (5 %), weil niemand weiß, ob die
        # nächsten 30 Jahre so gut werden wie die letzten 50.
        r = dreieck(rng, 0.05, 0.072, 0.085)
        v = dreieck(rng, 0.14, 0.16, 0.19)
        inf = dreieck(rng, 0.015, 0.022, 0.035)
        mu_log = math.log(1 + r) - v * v / 2
        renditen = [math.exp(rng.gauss(mu_log, v)) - 1 for _ in range(JAHRE)]
        return cls(r, v, inf, renditen)

    def index(self, jahr: int) -> float:
        return (1 + self.inflation) ** jahr


@dataclass
class Konsum:
    """Ausgaben: ein Grundbedarf plus ein Anteil jedes Euros darüber.

    Der Grenzkonsum ``lam`` ist der Hebel, den ein Plan tatsächlich steuern
    kann: Bei 0,5 wandert jeder zweite zusätzliche Euro ins Depot.
    """

    grundbedarf: float      # EUR/Jahr in heutigen Euro
    lam: float

    def ausgaben(self, netto: float, index: float) -> float:
        g = self.grundbedarf * index
        if netto <= g:
            return netto     # Lücke tragen Eltern/BAföG/Nebenjob - kein Kredit
        return g + self.lam * (netto - g)


def jahr_abschliessen(depot: float, sparen: float, rendite: float) -> float:
    """Sparbetrag fließt übers Jahr verteilt ein, im Schnitt halbes Jahr investiert."""
    return depot * (1 + rendite) + sparen * (1 + rendite / 2)


# --------------------------------------------------------------------------
# Strategien
# --------------------------------------------------------------------------

Strategie = Callable[[random.Random, Welt], list[float]]


def _gehalt_pfad(rng: random.Random, start: float, wachstum_frueh: float,
                 wachstum_spaet: float, knick: int, streu: float,
                 sprung_p: float = 0.0, sprung_faktor: float = 1.0):
    """Reales Gehaltswachstum: früh steil, später flach, mit Einzelstreuung.

    ``sprung_p``: jährliche Chance auf einen Karrieresprung (Führung,
    Wechsel in die Spitzengruppe), der das Gehalt dauerhaft anhebt.
    """
    talent = math.exp(rng.gauss(0, streu))
    g = start * talent
    jahr = 0
    while True:
        yield g
        w = wachstum_frueh if jahr < knick else wachstum_spaet
        g *= 1 + w + rng.gauss(0, 0.02)
        if sprung_p and rng.random() < sprung_p:
            g *= sprung_faktor
            sprung_p = 0.0   # einmaliger Sprung
        jahr += 1


def angestellt(studienjahre: int, start: float, frueh: float, spaet: float,
               knick: int, streu: float, lam: float, grund: float,
               sprung_p: float = 0.0, sprung_faktor: float = 1.0,
               neben_netto: float = 6_000) -> Strategie:
    """Studium/Ausbildung, danach angestellt, Überschuss ins ETF-Depot."""

    def leben(rng: random.Random, w: Welt) -> list[float]:
        konsum = Konsum(grund, lam)
        studium = Konsum(12_000, 0.6)
        depot = 1_000.0
        pfad = _gehalt_pfad(rng, start, frueh, spaet, knick, streu, sprung_p, sprung_faktor)
        werte = []
        for j in range(JAHRE):
            idx = w.index(j)
            if j < studienjahre:
                netto = neben_netto * idx
                sparen = netto - studium.ausgaben(netto, idx)
            else:
                brutto = next(pfad) * idx
                netto = netto_angestellt(brutto, idx)
                sparen = netto - konsum.ausgaben(netto, idx)
            depot = jahr_abschliessen(depot, sparen, w.renditen[j])
            werte.append(depot)
        return werte

    return leben


@dataclass
class AgenturParameter:
    """Spannweiten (low, mid, high) für das Agenturmodell."""

    umsatz_2027: tuple = (0, 6_000, 20_000)          # Jahr 1 neben dem Abitur
    eur_je_stunde_solo: tuple = (35, 60, 90)          # Umsatz je Arbeitsstunde inkl. Akquise
    auslastung_start: tuple = (0.15, 0.35, 0.6)       # gefüllter Anteil der Kapazität im 1. Vollzeitjahr
    lernrate: tuple = (0.1, 0.25, 0.45)               # wie schnell sich die Lücke zur Vollauslastung schließt
    kosten_anteil: tuple = (0.08, 0.15, 0.22)         # Werkzeuge, Versicherung, Fahrzeug, Buchhaltung
    hazard_solo: tuple = (0.08, 0.15, 0.25)           # jährliche Aufgabewahrscheinlichkeit als Solo
    hazard_team: tuple = (0.03, 0.06, 0.10)           # jährliche Krise, die das Team-Geschäft beendet
    p_skalieren: tuple = (0.10, 0.25, 0.45)           # Chance je Jahr, vom Solo- ins Teammodell zu wechseln
    umsatz_je_fte: tuple = (65_000, 90_000, 120_000)  # Umsatz je Vollzeitkraft in Agenturen
    kosten_je_fte: tuple = (55_000, 63_000, 72_000)   # Gehalt + AG-Anteil + Platz/Software
    neue_fte_je_jahr: tuple = (0.3, 1.0, 2.5)         # Wachstum des Teams pro Jahr
    max_fte: tuple = (2, 8, 30)                       # Obergrenze, die dieser Gründer erreicht
    preistrend: tuple = (-0.05, -0.01, 0.02)          # realer Preistrend durch KI-Baukästen
    multiple: tuple = (2.0, 3.0, 4.5)                 # EBITDA-Multiple beim Verkauf kleiner Agenturen
    ersatz_gehalt_inhaber: float = 60_000             # Marktgehalt für die Rolle des Inhabers


def agentur(studium_parallel: bool, lam: float, grund: float,
            p: AgenturParameter | None = None,
            rueckfall_start: float = 48_000) -> Strategie:
    """Webagentur für lokale Betriebe - der Weg, den standortcheck vorbereitet.

    ``studium_parallel``: Informatikstudium mit 20 h/Woche Agentur, danach
    Wahl zwischen Vollzeit-Agentur und Anstellung (je nachdem, was mehr
    bringt). Ohne Studium: ab Sommer 2027 Vollzeit.

    Scheitert die Agentur, geht es in eine Anstellung als Webentwickler weiter,
    das Depot bleibt. Der Firmenwert zählt nur ab drei Vollzeitkräften (vorher
    hängt alles am Inhaber und ist praktisch unverkäuflich) und nur mit dem
    Gewinn über einem Marktgehalt für den Inhaber.
    """
    p = p or AgenturParameter()

    def leben(rng: random.Random, w: Welt) -> list[float]:
        d = lambda t: dreieck(rng, *t)  # noqa: E731
        eur_h, aus, lern = d(p.eur_je_stunde_solo), d(p.auslastung_start), d(p.lernrate)
        kosten, hz_solo, hz_team = d(p.kosten_anteil), d(p.hazard_solo), d(p.hazard_team)
        p_skal, u_fte, k_fte = d(p.p_skalieren), d(p.umsatz_je_fte), d(p.kosten_je_fte)
        fte_wachstum, fte_max = d(p.neue_fte_je_jahr), d(p.max_fte)
        trend, mult = d(p.preistrend), d(p.multiple)
        konsum = Konsum(grund, lam)
        studium = Konsum(12_000, 0.6)

        depot, fte, aktiv, angestellt_seit = 1_000.0, 0.0, True, None
        gehalt = _gehalt_pfad(rng, rueckfall_start, 0.04, 0.015, 10, 0.2)
        studienjahre = 5 if studium_parallel else 0
        werte = []
        for j in range(JAHRE):
            idx = w.index(j)
            preis = (1 + trend) ** j
            firmenwert = 0.0
            if aktiv:
                if j == 0:
                    umsatz = d(p.umsatz_2027) * idx
                    stunden = 0
                else:
                    stunden = 900 if j < studienjahre else 2_000
                    erfahrung = 1 - (1 - aus) * (1 - lern) ** (j - 1)
                    umsatz = stunden * eur_h * erfahrung * preis * idx
                    umsatz *= math.exp(rng.gauss(0, 0.15))      # gutes/schlechtes Jahr
                gewinn = umsatz * (1 - kosten)
                if fte > 0:
                    team = fte * (u_fte * preis * idx - k_fte * idx)
                    team *= math.exp(rng.gauss(0, 0.2))
                    gewinn += team
                netto = netto_selbststaendig(gewinn, idx)
                studium_jahr = j < studienjahre
                sparen = netto - (studium if studium_jahr else konsum).ausgaben(netto, idx)

                # Wechsel ins Teammodell / Teamwachstum (nur in Vollzeit)
                if not studium_jahr and j >= 1:
                    if fte == 0 and rng.random() < p_skal and gewinn > 50_000 * idx:
                        fte = 1.0
                    elif fte > 0:
                        fte = min(fte_max, fte + max(0.0, rng.gauss(fte_wachstum, 0.7)))
                # Ende der Selbstständigkeit
                hz = hz_team if fte >= 3 else hz_solo
                if rng.random() < hz:
                    aktiv, fte, angestellt_seit = False, 0.0, j
                # Nach dem Studium: Anstellung, wenn sie klar mehr bringt
                if studium_parallel and j == studienjahre and fte == 0 and aktiv:
                    angebot = rueckfall_start * 1.1 * idx
                    if gewinn < angebot:
                        aktiv, angestellt_seit = False, j
                if fte >= 3:
                    uebergewinn = gewinn - p.ersatz_gehalt_inhaber * idx
                    firmenwert = max(0.0, uebergewinn) * mult * 0.7  # 30 % Abschlag: Steuer, Illiquidität
            else:
                brutto = next(gehalt) * idx
                netto = netto_angestellt(brutto, idx)
                sparen = netto - konsum.ausgaben(netto, idx)
            depot = jahr_abschliessen(depot, sparen, w.renditen[j])
            werte.append(depot + firmenwert)
        return werte

    return leben


@dataclass
class NachfolgeParameter:
    """Kauf eines bestehenden, profitablen Kleinbetriebs (Nachfolge).

    Spannweiten (low, mid, high). Finanzierung typisch für Deutschland:
    Eigenkapital + Verkäuferdarlehen + Bank/KfW (ERP-Gründerkredit).
    """

    ab_alter: tuple = (25, 27, 30)
    eigenkapital_quote: tuple = (0.10, 0.15, 0.25)
    min_eigenkapital: float = 40_000
    p_abschluss_je_jahr: tuple = (0.15, 0.30, 0.50)   # passendes Objekt finden UND finanzieren
    ebitda: tuple = (120_000, 200_000, 350_000)        # Gewinn vor Zinsen/Abschreibung beim Kauf
    kaufmultiple: tuple = (2.5, 3.5, 5.0)
    zins: tuple = (0.045, 0.055, 0.07)
    tilgungsjahre: int = 8
    wachstum: tuple = (-0.04, 0.01, 0.05)              # reales EBITDA-Wachstum nach Kauf
    schock_sigma: float = 0.15
    hazard: tuple = (0.02, 0.05, 0.09)                 # jährliche Wahrscheinlichkeit eines Totalausfalls
    buergschaft: tuple = (0.0, 0.15, 0.35)             # Anteil Restschuld, für den man persönlich haftet
    gehalt_inhaber: float = 80_000
    exit_multiple: tuple = (2.5, 3.5, 4.5)


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
        depot = schuld = ebitda = 0.0
        for j in range(JAHRE):
            idx = w.index(j)
            alter = START_ALTER + j
            if zustand == "basis":
                depot = basis_werte[j]
                if alter >= ab and rng.random() < p_deal:
                    e = d(p.ebitda) * idx
                    preis = e * d(p.kaufmultiple)
                    ek = max(preis * ek_quote, p.min_eigenkapital * idx)
                    if depot >= ek:
                        zustand, ebitda, schuld = "inhaber", e, preis - ek
                        depot -= ek
                        werte.append(depot + max(0.0, preis - schuld) * 0.7)
                        continue
                werte.append(depot)
                continue
            if zustand == "ausgefallen":
                netto = netto_angestellt(next(gehalt_nach_ausfall) * idx, idx)
                depot = jahr_abschliessen(depot, netto - konsum.ausgaben(netto, idx), w.renditen[j])
                werte.append(depot)
                continue
            # Inhaber
            ebitda *= (1 + wachstum + w.inflation) * math.exp(rng.gauss(0, p.schock_sigma))
            if rng.random() < hz:
                depot = max(0.0, depot - buerg * schuld)
                zustand, schuld = "ausgefallen", 0.0
                werte.append(depot)
                continue
            gehalt = p.gehalt_inhaber * idx
            zinsen = schuld * zins
            tilgung_soll = schuld / p.tilgungsjahre if schuld > 0 else 0.0
            vor_steuer = ebitda - gehalt - zinsen - 0.03 * ebitda   # Ersatzinvestitionen
            frei = vor_steuer * (1 - 0.30) if vor_steuer > 0 else vor_steuer  # GmbH ~30 %
            if frei < tilgung_soll:
                depot -= tilgung_soll - frei                        # Nachschuss aus dem Depot
                tilgung = tilgung_soll
                ueberschuss = 0.0
            else:
                tilgung = min(schuld, frei)                         # Sondertilgung mit allem Freien
                ueberschuss = frei - tilgung
            schuld = max(0.0, schuld - tilgung)
            netto = netto_angestellt(gehalt, idx)
            sparen = netto - konsum.ausgaben(netto, idx)
            # Überschuss bleibt in der GmbH, beim Ausschütten fiele ~26 % an
            depot = jahr_abschliessen(depot, sparen, w.renditen[j]) + ueberschuss * 0.74
            eigen = max(0.0, ebitda * exit_m - schuld) * 0.7
            werte.append(depot + eigen)
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
    de = angestellt(5, 52_000, 0.045, 0.015, 10, 0.2, lam=lam, grund=16_000)

    def leben(rng: random.Random, w: Welt) -> list[float]:
        if rng.random() >= dreieck(rng, *p_stelle):
            return de(rng, w)
        konsum = Konsum(grund_ch, lam)
        studium = Konsum(12_000, 0.6)
        pfad = _gehalt_pfad(rng, dreieck(rng, *start), 0.035, 0.012, 10, 0.18)
        depot, pk = 1_000.0, 0.0
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
            depot = jahr_abschliessen(depot, sparen, w.renditen[j])
            werte.append(depot + pk)
        return werte

    return leben


@dataclass
class Weichen:
    """Die Entscheidungsregeln des Weichenplans."""

    bachelor_jahre: int = 3
    agentur_schwelle_real: float = 55_000   # Gewinn mit 22, ab dem Vollzeit-Agentur gewinnt
    p_stelle_ch: tuple = (0.25, 0.40, 0.60) # Schweizer Stelle mit Bachelor + Praxis
    start_ch: tuple = (75_000, 88_000, 105_000)
    start_de: tuple = (44_000, 50_000, 58_000)
    nachfolge: bool = True
    freelance: bool = True
    freelance_nach_jahren: int = 3          # Berufserfahrung, die Projektvermittler verlangen
    p_freelance: tuple = (0.4, 0.6, 0.8)    # traut sich und findet Projekte
    satz: tuple = (70, 92, 115)             # EUR/h, Freelancer-Kompass 2025: IT im Schnitt ~105
    auslastung: tuple = (0.55, 0.75, 0.90)  # Anteil von 1.700 möglichen Stunden
    hazard_freelance: tuple = (0.03, 0.07, 0.12)  # zurück in Anstellung (Flaute, Statusrisiko)
    lam: float = 0.5
    grund_de: float = 16_000
    grund_ch: float = 34_000


def weichenplan(wp: Weichen | None = None, ap: AgenturParameter | None = None,
                np_: NachfolgeParameter | None = None) -> Strategie:
    """Agentur neben dem Bachelor, dann die jeweils bessere Weiche.

    Zustände: studium (Bachelor + Agentur 20 h) -> agentur (Vollzeit, ggf.
    Team) | job_ch | job_de -> optional inhaber (Nachfolgekauf) -> ggf.
    ausgefallen (zurück in Anstellung). Jede Weiche wird nur gestellt, wenn
    die harte Zahl dafür spricht - nicht nach Gefühl.
    """
    wp, ap, np_ = wp or Weichen(), ap or AgenturParameter(), np_ or NachfolgeParameter()

    def leben(rng: random.Random, w: Welt) -> list[float]:
        d = lambda t: dreieck(rng, *t)  # noqa: E731
        # Persönliche Ziehungen
        eur_h, aus, lern = d(ap.eur_je_stunde_solo), d(ap.auslastung_start), d(ap.lernrate)
        kosten, hz_solo, hz_team = d(ap.kosten_anteil), d(ap.hazard_solo), d(ap.hazard_team)
        p_skal, u_fte, k_fte = d(ap.p_skalieren), d(ap.umsatz_je_fte), d(ap.kosten_je_fte)
        fte_wachstum, fte_max = d(ap.neue_fte_je_jahr), d(ap.max_fte)
        trend, mult = d(ap.preistrend), d(ap.multiple)
        nf_ab, nf_ek, nf_p = int(round(d(np_.ab_alter))), d(np_.eigenkapital_quote), d(np_.p_abschluss_je_jahr)
        nf_zins, nf_wachs, nf_hz, nf_buerg = d(np_.zins), d(np_.wachstum), d(np_.hazard), d(np_.buergschaft)
        nf_exit = d(np_.exit_multiple)
        ch_ok = rng.random() < d(wp.p_stelle_ch)
        fl_ok = wp.freelance and rng.random() < d(wp.p_freelance)
        fl_satz, fl_aus, fl_hz = d(wp.satz), d(wp.auslastung), d(wp.hazard_freelance)
        berufsjahre = 0
        gehalt_ch = _gehalt_pfad(rng, d(wp.start_ch), 0.035, 0.012, 10, 0.18)
        gehalt_de = _gehalt_pfad(rng, d(wp.start_de), 0.045, 0.015, 10, 0.2)
        konsum_de, konsum_ch = Konsum(wp.grund_de, wp.lam), Konsum(wp.grund_ch, wp.lam)
        studium = Konsum(12_000, 0.6)

        zustand = "studium"
        depot, pk, fte = 1_000.0, 0.0, 0.0
        schuld = ebitda = 0.0
        agentur_jahre = 0
        werte: list[float] = []
        for j in range(JAHRE):
            idx = w.index(j)
            alter = START_ALTER + j
            preis = (1 + trend) ** j
            zusatz = 0.0          # Firmenwert, Pensionskasse
            konsum = konsum_ch if zustand == "job_ch" else konsum_de

            if zustand in ("studium", "agentur"):
                if j == 0:
                    umsatz = d(ap.umsatz_2027) * idx
                else:
                    stunden = 900 if zustand == "studium" else 2_000
                    erfahrung = 1 - (1 - aus) * (1 - lern) ** agentur_jahre
                    umsatz = stunden * eur_h * erfahrung * preis * idx * math.exp(rng.gauss(0, 0.15))
                agentur_jahre += 1 if j > 0 else 0
                gewinn = umsatz * (1 - kosten)
                if fte > 0:
                    gewinn += fte * (u_fte * preis - k_fte) * idx * math.exp(rng.gauss(0, 0.2))
                netto = netto_selbststaendig(gewinn, idx)
                sparen = netto - (studium if zustand == "studium" else konsum_de).ausgaben(netto, idx)
                if zustand == "agentur":
                    if fte == 0 and rng.random() < p_skal and gewinn > 50_000 * idx:
                        fte = 1.0
                    elif fte > 0:
                        fte = min(fte_max, fte + max(0.0, rng.gauss(fte_wachstum, 0.7)))
                    if fte >= 3:
                        zusatz += max(0.0, gewinn - ap.ersatz_gehalt_inhaber * idx) * mult * 0.7
                # Weichen
                if rng.random() < (hz_team if fte >= 3 else hz_solo):
                    zustand, fte = ("job_ch" if ch_ok else "job_de"), 0.0
                elif zustand == "studium" and j == wp.bachelor_jahre:
                    hochgerechnet = gewinn / idx * 2_000 / 900 * 0.8   # Vollzeit, vorsichtig
                    zustand = "agentur" if hochgerechnet >= wp.agentur_schwelle_real else (
                        "job_ch" if ch_ok else "job_de")
            elif zustand == "freelance":
                umsatz = 1_700 * fl_aus * fl_satz * idx * math.exp(rng.gauss(0, 0.12))
                gewinn = umsatz * 0.90                   # Versicherung, Technik, Weiterbildung
                netto = netto_selbststaendig(gewinn, idx)
                sparen = netto - konsum_de.ausgaben(netto, idx)
                if rng.random() < fl_hz:
                    zustand = "job_de"
            elif zustand in ("job_ch", "job_de", "ausgefallen"):
                berufsjahre += 1
                if zustand == "job_ch":
                    brutto = next(gehalt_ch) * idx
                    st = min(0.30, max(0.06, 0.06 + 0.08 * math.log(max(brutto / idx, 60_000) / 60_000)))
                    netto = brutto * (1 - 0.064 - 0.07 - st)
                    pk = pk * 1.02 + brutto * 0.07
                else:
                    brutto = next(gehalt_de) * idx
                    netto = netto_angestellt(brutto, idx)
                sparen = netto - konsum.ausgaben(netto, idx)
            else:  # inhaber
                ebitda *= (1 + nf_wachs + w.inflation) * math.exp(rng.gauss(0, np_.schock_sigma))
                if rng.random() < nf_hz:
                    depot = max(0.0, depot - nf_buerg * schuld)
                    zustand, schuld = "ausgefallen", 0.0
                    werte.append(depot + pk)
                    continue
                gehalt = np_.gehalt_inhaber * idx
                vor = ebitda - gehalt - schuld * nf_zins - 0.03 * ebitda
                frei = vor * 0.70 if vor > 0 else vor
                soll = schuld / np_.tilgungsjahre if schuld > 0 else 0.0
                if frei < soll:
                    depot -= soll - frei
                    tilgung, ueber = soll, 0.0
                else:
                    tilgung, ueber = min(schuld, frei), frei - min(schuld, frei)
                schuld = max(0.0, schuld - tilgung)
                netto = netto_angestellt(gehalt, idx)
                sparen = netto - konsum_de.ausgaben(netto, idx) + ueber * 0.74
                zusatz += max(0.0, ebitda * nf_exit - schuld) * 0.7

            depot = jahr_abschliessen(depot, sparen, w.renditen[j])

            # Freelance-Weiche: aus der deutschen Anstellung nach genug Praxis.
            # (Aus der Schweiz heraus lohnt sie sich meist nicht.)
            if zustand == "job_de" and fl_ok and berufsjahre >= wp.freelance_nach_jahren:
                zustand, fl_ok = "freelance", False

            # Nachfolge-Weiche: nur aus einer Anstellung oder Solo-Agentur heraus
            if (wp.nachfolge and zustand in ("job_ch", "job_de", "agentur", "freelance") and fte < 3
                    and alter >= nf_ab and rng.random() < nf_p):
                e = d(np_.ebitda) * idx
                kaufpreis = e * d(np_.kaufmultiple)
                ek = max(kaufpreis * nf_ek, np_.min_eigenkapital * idx)
                if depot >= ek * 1.3:            # Puffer: nicht das letzte Geld einsetzen
                    depot -= ek
                    zustand, ebitda, schuld, fte = "inhaber", e, kaufpreis - ek, 0.0
                    zusatz = max(0.0, kaufpreis - schuld) * 0.7
            werte.append(depot + pk + zusatz)
        return werte

    return leben


STRATEGIEN: dict[str, tuple[str, Strategie]] = {}


def _registrieren() -> None:
    s = STRATEGIEN
    # Angestellt, Informatik (Master, 5 Jahre), normales Sparverhalten
    s["it_normal"] = ("Informatik-Master, angestellt, spart normal",
                      angestellt(5, 52_000, 0.045, 0.015, 10, 0.2, lam=0.75, grund=18_000))
    s["it_sparsam"] = ("Informatik-Master, angestellt, spart 50 %",
                       angestellt(5, 52_000, 0.045, 0.015, 10, 0.2, lam=0.5, grund=16_000))
    s["agentur_voll"] = ("Webagentur Vollzeit ab Sommer 2027",
                         agentur(False, lam=0.5, grund=16_000))
    s["agentur_hybrid"] = ("Informatikstudium + Agentur 20 h/Woche",
                           agentur(True, lam=0.5, grund=16_000))
    s["agentur_nachfolge"] = ("Agentur, dann Betrieb kaufen (Nachfolge)",
                              nachfolge(agentur(False, lam=0.5, grund=16_000), lam=0.5, grund=16_000))
    s["it_nachfolge"] = ("Informatik angestellt, dann Betrieb kaufen",
                         nachfolge(angestellt(5, 52_000, 0.045, 0.015, 10, 0.2, lam=0.5, grund=16_000),
                                   lam=0.5, grund=16_000))
    s["agentur_wette"] = ("Agentur + Software-Wette nebenher",
                          mit_wette(agentur(False, lam=0.5, grund=16_000)))
    s["dual"] = ("Duales Studium Informatik, spart 50 %",
                 angestellt(3, 48_000, 0.045, 0.015, 10, 0.18, lam=0.5, grund=16_000,
                            neben_netto=13_000))
    s["schweiz"] = ("Informatik-Master, dann Stelle in der Schweiz",
                    schweiz())
    s["weichen"] = ("WEICHENPLAN: Bachelor+Agentur, dann beste Weiche",
                    weichenplan())
    s["weichen_ohne_nf"] = ("Weichenplan ohne Nachfolgekauf",
                            weichenplan(Weichen(nachfolge=False)))
    s["weichen_ohne_fl"] = ("Weichenplan ohne Freelance-Weiche",
                            weichenplan(Weichen(freelance=False)))
    s["weichen_nur_job"] = ("Weichenplan nur Anstellung (ohne FL/NF)",
                            weichenplan(Weichen(freelance=False, nachfolge=False)))


_registrieren()


# --------------------------------------------------------------------------
# Auswertung
# --------------------------------------------------------------------------


def simulieren(strategie: Strategie, n: int, seed: int = 2027) -> list[list[float]]:
    rng = random.Random(seed)
    return [strategie(rng, Welt.ziehen(rng)) for _ in range(n)]


def quote_bis_alter(leben: list[list[float]], alter: int) -> float:
    j = alter - START_ALTER
    return sum(1 for w in leben if w[j] >= ZIEL) / len(leben)


def fruehestes_alter(leben: list[list[float]], schwelle: float = 0.5) -> int | None:
    for alter in range(START_ALTER, END_ALTER + 1):
        if quote_bis_alter(leben, alter) >= schwelle:
            return alter
    return None


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


def sensitivitaet(n: int = 2_000) -> None:
    """Welche Annahme verschiebt das 50-%-Alter des Weichenplans am stärksten?

    Jede Annahme wird einzeln auf ihren pessimistischen bzw. optimistischen
    Rand festgesetzt, alle anderen bleiben unsicher.
    """
    from dataclasses import replace

    basis = fruehestes_alter(simulieren(weichenplan(), n))
    print(f"Sensitivität des Weichenplans (50 %-Alter, Basis {basis}):")
    print("-" * 72)
    faelle: list[tuple[str, Strategie, Strategie]] = []
    ap = AgenturParameter()
    for feld, text in (("eur_je_stunde_solo", "Umsatz je Agenturstunde"),
                       ("p_skalieren", "Chance, ein Team aufzubauen"),
                       ("hazard_solo", "Aufgaberisiko als Solo"),
                       ("preistrend", "Preisdruck durch KI"),
                       ("umsatz_je_fte", "Umsatz je Mitarbeiter")):
        low, _mid, high = getattr(ap, feld)
        schlecht, gut = (high, low) if feld.startswith("hazard") else (low, high)
        faelle.append((text,
                       weichenplan(ap=replace(ap, **{feld: (schlecht, schlecht, schlecht)})),
                       weichenplan(ap=replace(ap, **{feld: (gut, gut, gut)}))))
    wp = Weichen()
    faelle.append(("Schweizer Stelle klappt", weichenplan(replace(wp, p_stelle_ch=(0, 0, 0))),
                   weichenplan(replace(wp, p_stelle_ch=(1, 1, 1)))))
    faelle.append(("Sparverhalten (Grenzkonsum 0,7 / 0,35)",
                   weichenplan(replace(wp, lam=0.7)), weichenplan(replace(wp, lam=0.35))))
    for text, schlecht, gut in faelle:
        a = fruehestes_alter(simulieren(schlecht, n))
        b = fruehestes_alter(simulieren(gut, n))
        print(f"  {text:42s} pessimistisch {a if a else '>50':>4}   optimistisch {b if b else '>50':>4}")
    print()


def sommer_meilensteine(n: int = 20_000, seed: int = 7) -> dict[str, float]:
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
    umsaetze.sort(); kunden.sort(); pakete.sort()

    def q(liste, anteil):
        return liste[int(len(liste) * anteil)]

    ergebnis = {
        "umsatz_median": q(umsaetze, 0.5), "umsatz_p25": q(umsaetze, 0.25),
        "umsatz_p75": q(umsaetze, 0.75), "kunden_median": q(kunden, 0.5),
        "pakete_median": q(pakete, 0.5),
        "p_mind_1_paket": sum(1 for x in pakete if x >= 1) / n,
        "p_mind_5_kunden": sum(1 for x in kunden if x >= 5) / n,
        "p_umsatz_3000": sum(1 for x in umsaetze if x >= 3_000) / n,
        "p_umsatz_5000": sum(1 for x in umsaetze if x >= 5_000) / n,
        "p_umsatz_10000": sum(1 for x in umsaetze if x >= 10_000) / n,
    }
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
    alter_spalten = (25, 30, 35, 40, 45, 50)
    print(f"  {'Strategie':44s}" + "".join(f"{x:>7d}" for x in alter_spalten) + "   50 % ab")
    for name, (titel, strat) in STRATEGIEN.items():
        leben = simulieren(strat, a.n)
        quoten = [quote_bis_alter(leben, x) for x in alter_spalten]
        ab = fruehestes_alter(leben)
        print(f"  {titel[:44]:44s}" + "".join(f"{q:>7.0%}" for q in quoten)
              + f"   {ab if ab else '> 50':>6}")
    print()


if __name__ == "__main__":
    main()
