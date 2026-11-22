"""Mehr als arbeiten gehen? Hebel-Wege bis 31.08.2027 gegen den Job-Weg gerechnet.

Jede Option wird Lauf für Lauf gegen denselben Job-Weg (plan/verdienst_2027.py)
gerechnet – mit denselben Zufallszahlen für Schule, Ferienjobs und Sommerjob.
So zeigt sich direkt, was die Option zusätzlich bringt oder kostet:

- Sie braucht Stunden, die im Job-Weg Nachhilfe, Webgeschäft oder Minijob
  bekommen hätten (das Stundenbudget schützt das Abitur und wächst nicht).
- Sie ersetzt ganz oder teilweise den Sommerjob oder belegt dessen Samstage.
- Ihr Gewinn zählt zur Einkommensteuer und – zusammen mit Nachhilfe und
  Webgeschäft – zur Grenze der Familienversicherung (§ 10 SGB V: Summe aller
  Gewinne 2027 höchstens 12 x 590 EUR). Wird sie überschritten, kostet die
  eigene Krankenversicherung Geld (``kv_kosten``).

Stufenpläne mit Frühindikator: Wo eine Option den Sommer braucht, entscheidet
ein Signal bis 31.03.2027, ob der Sommer ins Geschäft geht oder in den
Sommerjob. Bricht das Geschäft im Sommer nach drei Wochen ab, gibt es mit
einer gewissen Wahrscheinlichkeit noch einen späten Sommerjob.

Aufruf:

    python3 plan/hebel_2027.py            # alle Optionen
    python3 plan/hebel_2027.py --n 40000  # genauer

Eingaben mit Quellen: docs/HEBEL_BIS_SOMMER_2027.md.
"""

from __future__ import annotations

import argparse
import math
import random
import statistics
import sys
from dataclasses import dataclass, field, replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verdienst_2027 as v  # noqa: E402

dreieck = v.dreieck
_NORMAL = statistics.NormalDist()

PH_DEZ = "Schulzeit 23.11.–23.12.2026"
PH_JAN = "Schulzeit Januar – März 2027"
PH_PRUEF = "Lern- und Prüfungszeit"
PH_WEIH_26 = "Weihnachtsferien (2026)"
PH_WEIH_27 = "Weihnachtsferien (2027)"
PH_FRUEH = "Frühjahrsferien"
WEB = "Webgeschäft (standortcheck)"


# --------------------------------------------------------------------------
# Hilfsfunktionen
# --------------------------------------------------------------------------

def d(rng: random.Random, t: tuple) -> float:
    return dreieck(rng, *t) if t[0] != t[2] else float(t[0])


def dreieck_quantil(t: tuple, u: float) -> float:
    """Quantil der Dreiecksverteilung (min, Mitte, max) zum Anteil u."""
    a, c, b = t
    if b == a:
        return float(a)
    f = (c - a) / (b - a)
    if u < f:
        return a + math.sqrt(u * (b - a) * (c - a))
    return b - math.sqrt((1 - u) * (b - a) * (b - c))


def korreliert(rng: random.Random, u: float, rho: float) -> float:
    """Zweiter Anteil, mit u über eine Normal-Kopula korreliert (rho)."""
    u = min(max(u, 1e-9), 1 - 1e-9)
    z = rho * _NORMAL.inv_cdf(u) + math.sqrt(1 - rho * rho) * rng.gauss(0, 1)
    return _NORMAL.cdf(z)


def poisson(rng: random.Random, lam: float) -> int:
    if lam <= 0:
        return 0
    if lam > 60:
        return max(0, int(round(rng.gauss(lam, math.sqrt(lam)))))
    grenze, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= grenze:
            return k
        k += 1


def negbin(rng: random.Random, mittel: float, streuung: float, obergrenze: int) -> int:
    """Gamma-Poisson: viele Neulinge mit wenig Buchungen, wenige mit vielen."""
    return min(obergrenze, poisson(rng, rng.gammavariate(streuung, mittel / streuung)))


def sommer_wochen(basis: dict) -> float:
    """Wochen vom 28.06. bis 31.08. (bzw. bis Ausbildungsbeginn 01.08.)."""
    return v.SOMMER_TAGE[basis["start"]] / 5


# --------------------------------------------------------------------------
# Krankenversicherung, wenn die Familienversicherung wegfällt
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class KV:
    # Freiwillige Versicherung, Mindestbeitrag: Mindestbemessung (1/3 der Bezugsgröße, 2026
    # 1.318,33 EUR) x (14,0 % ermäßigt + Ø-Zusatzbeitrag ~2,9 % + Pflege 3,6 %) ~ 270 EUR/Monat
    beitrag_monat: tuple = (255.0, 270.0, 285.0)
    # Gewinn eines geplanten Geschäfts, das man bei der Kasse angeben muss (Prognose): die
    # Familienversicherung endet ab dem Monat nach der Entscheidung (Stufenplan: April)
    geplant_ab_monat: int = 4
    # Ungeplant über der Grenze (Preisgeld, Glückssommer): erst ein Steuerbescheid (2028)
    # oder die Meldung einer geänderten Prognose wirkt – bis 31.08. 0 bis wenige Monate
    ungeplant_monate: tuple = (0.0, 0.0, 2.0)


def famv_verloren(pruef_2027: dict, a: v.Annahmen) -> bool:
    """§ 10 SGB V: Gewinn/12 <= 590 EUR; mit Minijob Minijob/Monat + Gewinn/12 <= 633 EUR."""
    selbst = pruef_2027["selbst"]
    if selbst > 12 * a.grenze_regel[2027] + 1e-6:
        return True
    mini, monate = pruef_2027["mini"], pruef_2027["mini_monate"]
    if mini > 0 and monate > 0:
        return mini / monate + selbst / 12 > a.grenze_minijob[2027] + 1e-6
    return False


def kv_kosten(rng: random.Random, verloren: bool, geplant: bool, kv: KV) -> tuple[float, float]:
    """(Kosten bis 31.08.2027, Kosten danach bis Jahresende) – nur wenn die Grenze reißt."""
    if not verloren:
        return 0.0, 0.0
    beitrag = d(rng, kv.beitrag_monat)
    monate = (8 - kv.geplant_ab_monat + 1) if geplant else d(rng, kv.ungeplant_monate)
    return monate * beitrag, 4 * beitrag


# --------------------------------------------------------------------------
# Ergebnis einer Option in einem Lauf
# --------------------------------------------------------------------------

@dataclass
class Ergebnis:
    zusatz: v.Zusatz
    gewinn: float                 # Geschäftsgewinn bis 31.08.2027 (vor Steuer), auch negativ
    stunden: float                # eigene Stunden im Geschäft
    geplant: bool = False         # Geschäft so geplant, dass der Gewinn über der Grenze liegen soll
    go: bool | None = None        # Entscheidung am Frühindikator (None: kein Stufenplan)
    abbruch: bool = False
    info: dict = field(default_factory=dict)


def _sommer_rueckfall(rng: random.Random, rest_anteil: float, p_finden: tuple) -> float:
    """Anteil des Sommers, den ein später Sommerjob nach einem Abbruch noch abdeckt."""
    return rest_anteil if rng.random() < d(rng, p_finden) else 0.0


class Option:
    name = ""
    kurz = ""

    def vorbereiten(self, rng: random.Random, a: v.Annahmen) -> tuple[v.Annahmen, dict]:
        return a, {}

    def ziehen(self, rng: random.Random, basis: dict, zustand: dict) -> Ergebnis:
        raise NotImplementedError


# --------------------------------------------------------------------------
# Optionen
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class WebParameter:
    """Vertrieb wie in plan/simulation.py (sommer_meilensteine), im Sommer in Vollzeit."""
    stunden_woche: tuple = (30, 38, 45)
    disziplin: tuple = (0.7, 0.85, 1.0)
    h_kontakt: tuple = (0.33, 0.45, 0.7)          # Besuch mit Bericht, Fahrt, Nachbereitung
    kosten_kontakt: tuple = (0.3, 0.8, 2.0)       # Druck, Fahrt
    pool: tuple = (150, 300, 600)                 # erreichbare Betriebe im Raum Regensburg (Handrecherche)
    anteil_akquise_schule: float = 0.5            # Anteil der Web-Stunden im Schuljahr, der Kontakte verbraucht
    p_einstieg: tuple = (0.01, 0.03, 0.07)        # je Kontakt (standortcheck plan 6,1 %, halbiert)
    saison: tuple = (0.6, 0.8, 1.0)               # Juli/August: Handwerk in der Hochsaison und im Urlaub
    rho: float = 0.7                              # Zusammenhang Schuljahr <-> Sommer (gleiche Person, gleiches Angebot)
    einstieg_preis: tuple = (69, 200, 349)
    einstieg_h: float = 2.5
    p_upsell: tuple = (0.10, 0.25, 0.40)
    paket_preis: tuple = (1_400, 1_900, 2_600)
    paket_h: tuple = (18, 28, 40)
    p_betreuung: tuple = (0.5, 0.7, 0.9)
    betreuung_monat: tuple = (49, 69, 89)
    fix: tuple = (200, 450, 900)                  # Werbung, Fahrten, Druck im Sommer
    p_abbruch: float = 0.7                        # nach 3 Wochen ohne bezahlten Auftrag
    p_spaeter_job: tuple = (0.5, 0.7, 0.85)


def web_vertrieb(rng: random.Random, u: float, stunden: float, wochen: float, pool: float,
                 p: WebParameter) -> dict:
    """Vertriebstrichter für ``stunden`` Arbeitsstunden in ``wochen`` Wochen."""
    h_kontakt = d(rng, p.h_kontakt)
    p_ein = dreieck_quantil(p.p_einstieg, korreliert(rng, u, p.rho)) * d(rng, p.saison)
    p_up = d(rng, p.p_upsell)
    h_woche = stunden / max(wochen, 1e-9)
    umsatz = kosten = 0.0
    verbraucht = 0.0
    einstiege = pakete = 0
    abbruch_geprueft = abbruch = False
    kontakte = 0
    while verbraucht + h_kontakt <= stunden and kontakte < pool:
        if not abbruch_geprueft and verbraucht >= 3 * h_woche:
            abbruch_geprueft = True
            if einstiege == 0 and rng.random() < p.p_abbruch:
                abbruch = True
                break
        kontakte += 1
        verbraucht += h_kontakt
        kosten += d(rng, p.kosten_kontakt)
        if rng.random() < p_ein:
            einstiege += 1
            umsatz += d(rng, p.einstieg_preis)
            verbraucht += p.einstieg_h
            if rng.random() < p_up:
                bau = d(rng, p.paket_h)
                preis = d(rng, p.paket_preis)
                pakete += 1
                if verbraucht + bau <= stunden:
                    verbraucht += bau
                    umsatz += preis
                    rest_wochen = max(0.0, wochen - verbraucht / max(h_woche, 1e-9))
                    if rng.random() < d(rng, p.p_betreuung):
                        umsatz += d(rng, p.betreuung_monat) * int(rest_wochen / 4.33)
                else:
                    umsatz += 0.5 * preis       # Anzahlung; Rest erst nach dem 31.08.
                    verbraucht = stunden
    wochen_aktiv = (verbraucht / h_woche) if h_woche > 0 else 0.0
    return {"umsatz": umsatz, "kosten": kosten, "stunden": verbraucht, "einstiege": einstiege,
            "pakete": pakete, "abbruch": abbruch, "wochen_aktiv": min(wochen, wochen_aktiv), "kontakte": kontakte}


class WebSommer(Option):
    """Webgeschäft im Sommer in Vollzeit (oder an 2 Tagen je Woche) statt (neben) Sommerjob."""

    def __init__(self, schwelle: float | None = 1_500.0, tage_woche: float = 5.0,
                 p: WebParameter = WebParameter()):
        self.schwelle, self.tage, self.p = schwelle, tage_woche, p
        teil = "Vollzeit statt Sommerjob" if tage_woche >= 5 else f"{tage_woche:.0f} Tage/Woche neben 3-Tage-Sommerjob"
        gate = f", nur wenn bis 31.03. Web-Gewinn >= {schwelle:,.0f} EUR".replace(",", ".") if schwelle else ", ohne Frühindikator"
        self.name = f"Webgeschäft im Sommer: {teil}{gate}"
        self.kurz = f"web_{int(tage_woche)}t_{int(schwelle or 0)}"

    def vorbereiten(self, rng, a):
        # Gleiche Zugkraft im Schuljahr und im Sommer: der Web-Satz des Job-Wegs wird für diesen
        # Lauf aus demselben Anteil u gezogen (gleiche Verteilung wie im Job-Weg)
        u = rng.random()
        regel = tuple(replace(r, satz=(dreieck_quantil(r.satz, u),) * 3) if r.name == WEB else r
                      for r in a.regelmaessig)
        return replace(a, regelmaessig=regel), {"u": u}

    def ziehen(self, rng, basis, zustand):
        p = self.p
        signal = sum(basis["je_phase"].get(ph, {}).get(WEB, 0.0) for ph in basis["je_phase"]
                     if ph.startswith((PH_DEZ, PH_JAN)))
        go = self.schwelle is None or signal >= self.schwelle
        if not go:
            return Ergebnis(v.Zusatz(), 0.0, 0.0, go=False, info={"signal": signal})
        wochen = sommer_wochen(basis)
        anteil_web = self.tage / 5
        stunden = wochen * d(rng, p.stunden_woche) * anteil_web * d(rng, p.disziplin)
        pool = d(rng, p.pool) - p.anteil_akquise_schule * basis["stunden_je_quelle"].get(WEB, 0.0) / 0.45
        r = web_vertrieb(rng, zustand["u"], stunden, wochen, max(30.0, pool), p)
        gewinn = r["umsatz"] - r["kosten"] - d(rng, p.fix) * anteil_web
        sommer_job = 1 - anteil_web
        teilzeit = True
        # Abgebrochen oder alle erreichbaren Betriebe angesprochen: Rest des Sommers jobben, wenn
        # sich so spät noch ein Job findet (Vollzeit: späterer Beginn; Teilzeit: mehr Tage je Woche)
        rest = max(0.0, 1 - r["wochen_aktiv"] / wochen)
        if r["abbruch"] or rest * wochen >= 2:
            spaet = _sommer_rueckfall(rng, rest, p.p_spaeter_job)
            if self.tage >= 5:
                sommer_job, teilzeit = spaet, False
            else:
                sommer_job = min(1.0, sommer_job + anteil_web * spaet)
        z = v.Zusatz(sommer_anteil=sommer_job, sommer_teilzeit=teilzeit,
                     gewinn=((2027, gewinn),))
        return Ergebnis(z, gewinn, r["stunden"], geplant=True, go=True, abbruch=r["abbruch"],
                        info={"signal": signal, "pakete": r["pakete"], "einstiege": r["einstiege"],
                              "kontakte": r["kontakte"], "rest_sommer": rest})


@dataclass(frozen=True)
class UmzugParameter:
    """Trageteam für Umzüge (ohne Lkw) mit kurzfristig beschäftigten Helfern – Kategorie A der Recherche."""
    zugkraft_sigma: float = 0.75                  # Lognormal-Streuung der Nachfrage (persistent)
    auftraege_woche: float = 2.5                  # Median bei voller Werbung
    max_woche: float = 10.0
    preis_helferstunde: tuple = (32, 35, 38)      # Umzugshelfer 25-40 EUR/h (Portale), Neuling ohne Bewertungen
    anfahrt: tuple = (20, 25, 30)
    helferstunden_auftrag: tuple = (9, 12, 16)    # z. B. 3 x 4 h
    lohn: tuple = (17.0, 18.0, 19.0)              # muss mit Industrie-Ferienjobs (18-20 EUR) konkurrieren
    lohnnebenkosten: tuple = (1.10, 1.12, 1.18)   # Umlagen, BG, Urlaub; teils berufsmäßige Helfer (SV)
    leerlauf: tuple = (0.08, 0.11, 0.15)          # bezahlte, nicht abrechenbare Zeit
    ausfall: tuple = (0.02, 0.035, 0.05)
    lead: tuple = (10, 20, 30)                    # Anzeigen/Portale je Auftrag
    fix: tuple = (1_300, 1_900, 2_400)            # Haftpflicht, Ausrüstung, Lohnabrechnung, Werbung (nach Go)
    test_kosten: tuple = (400, 650, 900)          # Gewerbe, Website, Testanzeigen, Versicherung anteilig
    aufbau_h: tuple = (30, 45, 60)                # vor dem Abitur
    test_auftrag_h: float = 7.0
    test_erloes: tuple = (150, 225, 300)
    pruefzeit_h: tuple = (24, 36, 48)             # Anfragen, Angebote, Crew in der Prüfungszeit (nur bei Go)
    schwelle_anfragen: int = 10                   # Anfragen im Februar/März
    p_abbruch: float = 0.7
    p_spaeter_job: tuple = (0.5, 0.7, 0.85)


class Umzug(Option):
    def __init__(self, stufenplan: bool = True, hybrid: bool = False, p: UmzugParameter = UmzugParameter()):
        self.stufen, self.hybrid, self.p = stufenplan, hybrid, p
        art = ("nur Fr/Sa und Monatsende, dazu 3-Tage-Sommerjob (Mo–Mi)" if hybrid
               else "statt Sommerjob")
        self.name = (f"Umzugs-Trageteam mit Helfern, {art}, "
                     + ("nur bei >= 10 Anfragen im Feb./März" if stufenplan else "ohne Frühindikator"))
        self.kurz = "umzug" + ("_hybrid" if hybrid else "") + ("_stufen" if stufenplan else "_immer")

    def ziehen(self, rng, basis, zustand):
        p = self.p
        zug = rng.lognormvariate(0.0, p.zugkraft_sigma)
        test_auftraege = min(6, poisson(rng, 1.5 * zug))
        aufbau = d(rng, p.aufbau_h) + test_auftraege * p.test_auftrag_h
        vorab = test_auftraege * d(rng, p.test_erloes) - d(rng, p.test_kosten)
        anfragen = poisson(rng, 6 * zug)
        go = (not self.stufen) or anfragen >= p.schwelle_anfragen
        stunden_vorab = ((PH_JAN, aufbau),)
        if not go:
            z = v.Zusatz(stunden=stunden_vorab, gewinn=((2027, vorab),))
            return Ergebnis(z, vorab, aufbau, go=False, info={"anfragen": anfragen})
        wochen = sommer_wochen(basis)
        lam = min(p.auftraege_woche * zug, p.max_woche)
        if self.hybrid:
            lam = min(0.6 * lam, 4.0)                                 # nur Fr/Sa und Monatsende
        auftraege = poisson(rng, lam * max(0.0, wochen - 0.75))      # Anlauf: Woche 1 50 %, Woche 2 75 %
        drei = poisson(rng, lam * 1.75)
        abbruch = (not self.hybrid) and drei < 2 and rng.random() < p.p_abbruch
        if abbruch:
            auftraege = min(auftraege, drei)
        wochen_aktiv = 3.0 if abbruch else wochen
        crew = auftraege * d(rng, p.helferstunden_auftrag)
        eigen = min(crew, min(auftraege, 5 * wochen_aktiv) * 4.5)
        helfer = crew - eigen
        kosten_h = d(rng, p.lohn) * d(rng, p.lohnnebenkosten) * (1 + d(rng, p.leerlauf))
        umsatz = crew * d(rng, p.preis_helferstunde) + auftraege * d(rng, p.anfahrt)
        schaden = (rng.random() < 1 - 0.97 ** auftraege) * dreieck(rng, 250, 500, 1_000)
        gewinn = (vorab + umsatz * (1 - d(rng, p.ausfall)) - auftraege * d(rng, p.lead) - d(rng, p.fix)
                  - schaden - helfer * kosten_h)
        pruefzeit = d(rng, p.pruefzeit_h)
        stunden = aufbau + pruefzeit + eigen + auftraege * 3.0 + wochen_aktiv * 4
        sommer_job, teilzeit = (0.6 if self.hybrid else 0.0), True
        if abbruch:
            sommer_job = _sommer_rueckfall(rng, max(0.0, 1 - 3 / wochen), p.p_spaeter_job)
            teilzeit = False
        z = v.Zusatz(stunden=stunden_vorab + ((PH_PRUEF, pruefzeit),), sommer_anteil=sommer_job,
                     sommer_teilzeit=teilzeit, sommer_samstage=0.0, gewinn=((2027, gewinn),))
        return Ergebnis(z, gewinn, stunden, geplant=True, go=True, abbruch=abbruch,
                        info={"anfragen": anfragen, "auftraege": auftraege, "helferstunden": helfer})


@dataclass(frozen=True)
class FotoboxParameter:
    """Fotobox-Verleih (gebraucht gekauft) mit Lieferung – Kategorie C der Recherche."""
    events_mittel: float = 8.5
    events_streuung: float = 1.6
    events_max: int = 30
    preis: tuple = (190, 260, 360)
    druckanteil: tuple = (0.5, 0.7, 0.9)
    drucke: tuple = (150, 280, 500)
    eur_druck: float = 0.16
    fahrt: tuple = (8, 14, 25)
    fix: tuple = (300, 550, 1_100)
    kauf: tuple = (1_100, 1_350, 1_900)
    restwert: tuple = (0.60, 0.75, 0.88)          # Wiederverkauf am 31.08. (Gebrauchtmarkt)
    p_schaden: float = 0.08
    schaden: tuple = (200, 450, 900)
    aufbau_h: tuple = (40, 60, 90)
    event_h: tuple = (4, 5, 6.5)
    anteil_vor_zeugnis: float = 0.3


class Fotobox(Option):
    name = "Fotobox-Verleih am Wochenende, neben dem Sommerjob"
    kurz = "fotobox"

    def __init__(self, p: FotoboxParameter = FotoboxParameter()):
        self.p = p

    def ziehen(self, rng, basis, zustand):
        p = self.p
        n = negbin(rng, p.events_mittel, p.events_streuung, p.events_max)
        var = d(rng, p.druckanteil) * d(rng, p.drucke) * p.eur_druck + d(rng, p.fahrt) + 5
        schaden = d(rng, p.schaden) if rng.random() < p.p_schaden else 0.0
        gewinn = (n * (d(rng, p.preis) - var) - d(rng, p.fix) - d(rng, p.kauf) * (1 - d(rng, p.restwert))
                  - schaden)
        aufbau = d(rng, p.aufbau_h)
        event_h = n * d(rng, p.event_h)
        vor = event_h * p.anteil_vor_zeugnis
        events_sommer = n * (1 - p.anteil_vor_zeugnis)
        frei = max(0.0, 1 - events_sommer / sommer_wochen(basis))    # ein Event je belegtem Samstag
        z = v.Zusatz(stunden=((PH_DEZ, 0.3 * aufbau), (PH_JAN, 0.7 * aufbau + vor / 2), (PH_PRUEF, vor / 2)),
                     sommer_samstage=frei, gewinn=((2027, gewinn),))
        return Ergebnis(z, gewinn, aufbau + event_h, info={"events": n})


class Flipping(Option):
    """Gebrauchte Smartphones, Konsolen, Laptops aufbereiten und verkaufen – Kategorie D."""
    name = "Technik-Flipping neben Schule und Sommerjob"
    kurz = "flipping"

    def ziehen(self, rng, basis, zustand):
        h_schule = 14 * rng.uniform(3, 7)
        h_ferien = 3 * rng.uniform(5, 20)
        h_pruef = rng.uniform(0, 15)
        h_sommer = 10 * rng.uniform(3, 8)                 # Abende neben dem Vollzeitjob
        if rng.random() < 0.35:                           # früher Abbruch (JPMorgan: 71 % nur 1-3 Monate aktiv)
            f = rng.uniform(0.15, 0.35)
            h_schule, h_ferien, h_pruef, h_sommer = h_schule * f, h_ferien * f, 0.0, 0.0
            abbruch = True
        else:
            abbruch = False
        stunden = h_schule + h_ferien + h_pruef + h_sommer
        h1 = rng.lognormvariate(1.1, 0.3)                 # ~3 h je Flip am Anfang
        h2 = h1 * rng.uniform(0.45, 0.8)
        n1 = min(10.0, stunden / h1)
        flips = int(n1 + max(0.0, stunden - n1 * h1) / h2)
        db = rng.uniform(15, 65)                          # Deckungsbeitrag nach eBay 5 % + 0,45, Versand, Teile
        p_panne, p_gewaehr = rng.uniform(0.04, 0.10), rng.uniform(0.02, 0.05)
        gewinn = 0.0
        for _ in range(flips):
            gewinn += rng.gauss(db, 18)
            if rng.random() < p_panne:
                gewinn -= rng.uniform(60, 200)
            if rng.random() < p_gewaehr:                  # Gewährleistung 1 Jahr (§ 476 BGB)
                gewinn -= rng.uniform(30, 120)
            if rng.random() < 0.005:                      # Hehlerware sichergestellt
                gewinn -= 220
        gewinn -= 45 + 26 + rng.uniform(60, 120) + 30 + rng.uniform(0, 100)
        if abbruch:
            gewinn -= rng.uniform(0, 3) * 220 * 0.12      # Restbestand mit Abschlag
        z = v.Zusatz(stunden=((PH_DEZ, h_schule * 4.5 / 13.5), (PH_JAN, h_schule * 9 / 13.5), (PH_PRUEF, h_pruef)),
                     ferientage=tuple((ph, h_ferien / 3 / 8) for ph in (PH_WEIH_26, PH_WEIH_27, PH_FRUEH)),
                     gewinn=((2027, gewinn),))
        return Ergebnis(z, gewinn, stunden, abbruch=abbruch, info={"flips": flips})


class StartupTeens(Option):
    """Businessplan-Wettbewerb mit dem vorhandenen Plan und Werkzeug (Startup Teens Bayern + national)."""
    name = "Startup-Teens-Wettbewerb mit standortcheck, nur mit Beleg bis 31.01."
    kurz = "startup_teens"

    def __init__(self, qualitaet_median: float = 4.0):
        self.m_median = qualitaet_median

    def ziehen(self, rng, basis, zustand):
        m = min(15.0, max(1.0, rng.lognormvariate(math.log(self.m_median), 0.6)))
        beleg = rng.random() < min(0.9, 0.25 + 0.05 * m)  # zahlender Kunde/Prototyp-Beleg bis 31.01.
        if not beleg:
            return Ergebnis(v.Zusatz(stunden=((PH_JAN, 2.0),)), 0.0, 2.0, go=False)
        stunden = dreieck(rng, 15, 25, 40)
        n_bayern = dreieck(rng, 150, 250, 400)
        p_bayern = min(0.30, 3 / n_bayern * m)
        p_bund = min(0.15, 7 / 1_482 * m)
        preis = 0.0
        if rng.random() < p_bayern:
            preis += rng.choice((5_000, 3_000, 2_000))
        bund = rng.random() < p_bund
        if bund:
            preis += 10_000
        finale = bund or rng.random() < min(0.4, 3 * p_bund)
        reise = dreieck(rng, 50, 150, 300) if finale else 0.0
        gewinn = preis - reise
        z = v.Zusatz(stunden=((PH_JAN, stunden),), gewinn=((2027, gewinn),))
        return Ergebnis(z, gewinn, stunden, go=True, info={"preis": preis})


class Kombination(Option):
    """Mehrere Optionen zugleich: Stunden und Gewinne addieren sich, den Sommer ändert nur eine."""

    def __init__(self, name: str, kurz: str, teile: tuple):
        self.name, self.kurz, self.teile = name, kurz, teile

    def vorbereiten(self, rng, a):
        zustaende = []
        for t in self.teile:
            a, z = t.vorbereiten(rng, a)
            zustaende.append(z)
        return a, {"teile": zustaende}

    def ziehen(self, rng, basis, zustand):
        ergs = [t.ziehen(rng, basis, z) for t, z in zip(self.teile, zustand["teile"])]
        sommer = [e.zusatz for e in ergs if e.zusatz.sommer_anteil < 1 or e.zusatz.sommer_samstage < 1]
        if len(sommer) > 1:
            raise ValueError("Nur eine Option darf den Sommer ändern")
        s = sommer[0] if sommer else v.Zusatz()
        gewinn = sum(e.gewinn for e in ergs)
        z = v.Zusatz(stunden=tuple(x for e in ergs for x in e.zusatz.stunden),
                     ferientage=tuple(x for e in ergs for x in e.zusatz.ferientage),
                     sommer_anteil=s.sommer_anteil, sommer_teilzeit=s.sommer_teilzeit,
                     sommer_samstage=s.sommer_samstage, gewinn=((2027, gewinn),))
        return Ergebnis(z, gewinn, sum(e.stunden for e in ergs), geplant=any(e.geplant for e in ergs),
                        go=any(e.go for e in ergs if e.go is not None) if any(e.go is not None for e in ergs) else None,
                        abbruch=any(e.abbruch for e in ergs))


# --------------------------------------------------------------------------
# Rechnung
# --------------------------------------------------------------------------

def vergleich(option: Option, i: int, seed: int = 2027, a: v.Annahmen | None = None, kv: KV = KV()) -> dict:
    """Ein Lauf: Job-Weg und Job-Weg mit Option, mit denselben Zufallszahlen."""
    a = a or v.Annahmen()
    s = seed * 1_000_003 + i
    rng_o = random.Random(s * 7 + 3)
    a_lauf, zustand = option.vorbereiten(rng_o, a)
    basis = v.ein_verlauf(random.Random(s), a_lauf, v.Zusatz())
    erg = option.ziehen(rng_o, basis, zustand)
    mit = v.ein_verlauf(random.Random(s), a_lauf, erg.zusatz)
    verloren = famv_verloren(mit["pruef"][2027], a_lauf)
    kv_bis, kv_danach = kv_kosten(rng_o, verloren, erg.geplant, kv)
    netto = mit["netto"] - kv_bis
    return {"basis": basis["netto"], "netto": netto, "mehr": netto - basis["netto"],
            "kontostand": mit["kontostand"] - kv_bis, "gewinn": erg.gewinn, "stunden": erg.stunden,
            "go": erg.go, "abbruch": erg.abbruch, "famv_weg": verloren, "kv": kv_bis, "kv_danach": kv_danach,
            "dual": basis["dual"], "info": erg.info}


def _q(xs: list, p: float) -> float:
    return xs[min(len(xs) - 1, int(len(xs) * p))]


def auswerten(option: Option, n: int = 10_000, seed: int = 2027, a: v.Annahmen | None = None,
              kv: KV = KV(), nur: str | None = None) -> dict:
    """Verteilungen; ``nur``: "fh" oder "dual" filtert die Läufe nach dem Weg nach dem Abitur."""
    laeufe = [vergleich(option, i, seed, a, kv) for i in range(n)]
    if nur:
        laeufe = [x for x in laeufe if x["dual"] == (nur == "dual")]
    m = len(laeufe)
    netto = sorted(x["netto"] for x in laeufe)
    basis = sorted(x["basis"] for x in laeufe)
    mehr = sorted(x["mehr"] for x in laeufe)
    gewinn = sorted(x["gewinn"] for x in laeufe)
    go = [x for x in laeufe if x["go"]]
    return {
        "name": option.name, "n": m,
        "p10": _q(netto, 0.10), "median": _q(netto, 0.5), "p90": _q(netto, 0.90), "p99": _q(netto, 0.99),
        "mittel": sum(netto) / m,
        "basis_p10": _q(basis, 0.10), "basis_median": _q(basis, 0.5), "basis_p90": _q(basis, 0.90),
        "basis_p99": _q(basis, 0.99), "basis_mittel": sum(basis) / m,
        "mehr_p10": _q(mehr, 0.10), "mehr_median": _q(mehr, 0.5), "mehr_p90": _q(mehr, 0.90),
        "mehr_p99": _q(mehr, 0.99), "mehr_mittel": sum(mehr) / m,
        "p_besser": sum(1 for x in mehr if x > 0) / m,
        "p_deutlich_besser": sum(1 for x in mehr if x > 2_000) / m,
        "p_deutlich_schlechter": sum(1 for x in mehr if x < -2_000) / m,
        "gewinn_median": _q(gewinn, 0.5), "gewinn_p90": _q(gewinn, 0.90),
        "p_geschaeftsverlust": sum(1 for x in gewinn if x < 0) / m,
        "p_go": len(go) / m if any(x["go"] is not None for x in laeufe) else None,
        "mehr_median_go": _q(sorted(x["mehr"] for x in go), 0.5) if go else None,
        "p_besser_go": sum(1 for x in go if x["mehr"] > 0) / len(go) if go else None,
        "p_abbruch": sum(1 for x in laeufe if x["abbruch"]) / m,
        "p_famv_weg": sum(1 for x in laeufe if x["famv_weg"]) / m,
        "kv_mittel": sum(x["kv"] for x in laeufe) / m,
        "kv_danach_mittel": sum(x["kv_danach"] for x in laeufe) / m,
        "stunden_median": _q(sorted(x["stunden"] for x in laeufe), 0.5),
        "kontostand_median": _q(sorted(x["kontostand"] for x in laeufe), 0.5),
    }


def optionen() -> list[Option]:
    web = WebSommer(1_500.0)
    return [
        WebSommer(None),
        web,
        WebSommer(1_500.0, tage_woche=2.0),
        Umzug(stufenplan=False),
        Umzug(stufenplan=True),
        Umzug(stufenplan=True, hybrid=True),
        Fotobox(),
        Flipping(),
        StartupTeens(),
        Kombination("Kombination: Web-Stufenplan (>= 1.500 EUR) + Startup Teens", "kombi_web_startup",
                    (WebSommer(1_500.0), StartupTeens())),
    ]


def _eur(x: float) -> str:
    return f"{x:7,.0f}".replace(",", ".")


def _pz(x: float | None) -> str:
    return "   –" if x is None else f"{100 * x:3.0f} %"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--n", type=int, default=10_000)
    args = ap.parse_args()
    print(f"Netto bis 31.08.2027 nach Steuer, Abgaben und Krankenversicherung – je Option gegen denselben "
          f"Job-Weg ({args.n} Läufe)")
    print("-" * 118)
    for o in optionen():
        r = auswerten(o, args.n)
        print(f"{o.name}")
        print(f"  gesamt        P10 {_eur(r['p10'])}  Median {_eur(r['median'])}  P90 {_eur(r['p90'])}  "
              f"P99 {_eur(r['p99'])}   (Job-Weg: {_eur(r['basis_p10'])} / {_eur(r['basis_median'])} / "
              f"{_eur(r['basis_p90'])} / {_eur(r['basis_p99'])})")
        print(f"  mehr als Job  P10 {_eur(r['mehr_p10'])}  Median {_eur(r['mehr_median'])}  P90 {_eur(r['mehr_p90'])}  "
              f"P99 {_eur(r['mehr_p99'])}  Mittel {_eur(r['mehr_mittel'])}   besser in {_pz(r['p_besser'])}, "
              f">2.000 besser {_pz(r['p_deutlich_besser'])}, >2.000 schlechter {_pz(r['p_deutlich_schlechter'])}")
        print(f"  Geschäft      Gewinn Median {_eur(r['gewinn_median'])}, P90 {_eur(r['gewinn_p90'])}, Verlust "
              f"{_pz(r['p_geschaeftsverlust'])}; Go {_pz(r['p_go'])}, Abbruch {_pz(r['p_abbruch'])}; "
              f"Familienversicherung weg {_pz(r['p_famv_weg'])}, KV bis 31.08. Ø {_eur(r['kv_mittel'])}, "
              f"danach Ø {_eur(r['kv_danach_mittel'])}; Stunden Median {r['stunden_median']:.0f}")
        if r["p_go"] is not None and r["mehr_median_go"] is not None:
            print(f"  wenn Go       mehr als Job Median {_eur(r['mehr_median_go'])}, besser in {_pz(r['p_besser_go'])}")


if __name__ == "__main__":
    main()
