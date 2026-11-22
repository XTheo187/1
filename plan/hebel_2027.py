"""Mehr als arbeiten gehen? Hebel-Wege bis 31.08.2027 gegen den Job-Weg gerechnet.

Jede Option wird Lauf für Lauf gegen denselben Job-Weg (plan/verdienst_2027.py)
gerechnet – mit denselben Zufallszahlen für Schule, Ferienjobs und Sommerjob.
So zeigt sich direkt, was die Option zusätzlich bringt oder kostet:

- Sie braucht Stunden, die im Job-Weg Nachhilfe, Webgeschäft oder Minijob
  bekommen hätten (das Stundenbudget schützt das Abitur und wächst nicht).
- Sie ersetzt ganz oder teilweise den Sommerjob oder belegt dessen Samstage.
- Ihr Gewinn zählt zur Einkommensteuer und – zusammen mit Nachhilfe und
  Webgeschäft – zur Grenze der Familienversicherung (§ 10 SGB V). Fällt sie
  weg, kostet die eigene Krankenversicherung Geld, und dann ist auch der
  Lohn des Sommerjobs beitragspflichtig (``kv_kosten``).

Stufenpläne mit Frühindikator: Wo eine Option den Sommer braucht, entscheidet
ein Signal bis 31.03.2027 (oder nach den ersten Sommertagen), ob der Sommer
ins Geschäft geht oder in den Sommerjob. Nach einem Abbruch gibt es mit einer
gewissen Wahrscheinlichkeit noch einen späten Sommerjob.

"Netto bis 31.08." zählt wie im Job-Weg, was bis dahin verdient ist (auch
geleistete, noch nicht bezahlte Arbeit). Was erst danach verdient wird
(Websites, die im September fertig werden), steht getrennt als Nachlauf.

Aufruf:

    python3 plan/hebel_2027.py            # alle Optionen
    python3 plan/hebel_2027.py --n 20000  # genauer
    python3 plan/hebel_2027.py --nur fh   # nur Studium danach (Sommerjob sozialversicherungsfrei)

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
GRENZE_JAHR = 12 * 590.0           # Familienversicherung 2027: Gewinn / 12 <= 590 EUR
KAL_ZU_ARBEITSTAGEN = 5 / 7


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


def binomial(rng: random.Random, n: int, p: float) -> int:
    return sum(1 for _ in range(max(0, int(n))) if rng.random() < p)


def negbin(rng: random.Random, mittel: float, streuung: float, obergrenze: int) -> int:
    """Gamma-Poisson: viele Neulinge mit wenig Buchungen, wenige mit vielen."""
    return min(obergrenze, poisson(rng, rng.gammavariate(streuung, mittel / streuung)))


def lognormal_quantil(median: float, sigma: float, u: float) -> float:
    u = min(max(u, 1e-9), 1 - 1e-9)
    return median * math.exp(sigma * _NORMAL.inv_cdf(u))


def sommer_tage(basis: dict) -> int:
    """Arbeitstage vom 28.06. bis 31.08. (bzw. bis Ausbildungsbeginn 01.08.)."""
    return v.SOMMER_TAGE[basis["start"]]


def monat_von_tag(t: float) -> int:
    """Sommer-Arbeitstag (0 = 28.06.) -> Kalendermonat: 3 Tage Juni, 22 Juli, 22 August."""
    return 6 if t < 3 else (7 if t < 25 else 8)


# --------------------------------------------------------------------------
# Krankenversicherung, wenn die Familienversicherung wegfällt
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class KV:
    """Freiwillige Versicherung 2027 (Recherche: SV-Rechengrößen 2027, GKV-SV, BSG B 12 KR 2/21 R)."""
    mindestbemessung: float = 4_130 / 3      # 1/90 der Bezugsgröße je Tag: 1.376,67 EUR/Monat
    satz_kv: float = 0.140                   # ermäßigt (ohne Krankengeld)
    zusatzbeitrag: tuple = (0.025, 0.031, 0.036)   # amtlich Ø 2,9 %, tatsächlich erhoben ~3,1 %
    satz_pv: float = 0.036                   # Kinderlosenzuschlag erst ab 23
    geplant_ab_monat: int = 4                # Prognose über der Grenze, gemeldet nach dem 31.03.
    # Ungeplant über der Grenze, korrekt gemeldet: kein Monat / nur August / Juli und August
    ungeplant: tuple = ((0.5, ()), (0.3, (8,)), (0.2, (7, 8)))
    # Vollzeit-Selbstständigkeit (> 30 h/Woche und > 25 % der Bezugsgröße im Monat) gilt als
    # hauptberuflich: dann entfällt die Familienversicherung für diese Zeit, egal wie viel Gewinn
    p_hauptberuflich: float = 0.7
    schwelle_hauptberuflich: float = 0.25 * 4_130
    p_september: float = 0.5                 # nach dem Stichtag: September noch freiwillig (Studium)


def famv_verloren(pruef_2027: dict, a: v.Annahmen, nachlauf: float = 0.0) -> bool:
    """§ 10 SGB V: Gewinn/12 <= 590 EUR; mit Minijob Minijob/Monat + Gewinn/12 <= 633 EUR."""
    selbst = pruef_2027["selbst"] + nachlauf
    if selbst > 12 * a.grenze_regel[2027] + 1e-6:
        return True
    mini, monate = pruef_2027["mini"], pruef_2027["mini_monate"]
    if mini > 0 and monate > 0:
        return mini / monate + selbst / 12 > a.grenze_minijob[2027] + 1e-6
    return False


def _frei_anteil(m: int, mit: dict) -> float:
    """Anteil des Monats m ohne Pflichtversicherung (nur dann kostet die freiwillige Versicherung)."""
    if not mit["dual"]:
        return 1.0
    beginn = {"01.08.": 8, "01.09.": 9, "01.10.": 10}[mit["start"]]
    if m >= beginn:
        return 0.0
    if m >= 6 and mit["sommer_lohn_monate"][m - 6] > 0:   # berufsmäßiger Sommerjob: pflichtversichert
        return 27 / 30 if m == 6 else 0.0
    return 1.0


def kv_kosten(rng: random.Random, kv: KV, mit: dict, gewinn_2027: float, verloren: bool, geplant: bool,
              hb_monate: tuple = (), gewinn_sommer: float = 0.0, wochenstunden: float = 0.0) -> tuple[float, float]:
    """(Kosten bis 31.08.2027, erwartete Kosten danach) der eigenen Kranken- und Pflegeversicherung.

    Als freiwilliges Mitglied zahlt man auf alle Einnahmen: Gewinn (Jahresgewinn auf die
    Monate mit Tätigkeit verteilt) und – im Studiums-Fall – auch den Lohn des Sommerjobs.
    """
    r = kv.satz_kv + d(rng, kv.zusatzbeitrag) + kv.satz_pv
    a_monat = max(0.0, gewinn_2027) / 8                     # Tätigkeit Januar bis August

    def beitrag(m: int, arbeitseinkommen: float) -> float:
        lohn = mit["sommer_lohn_monate"][m - 6] if (m >= 6 and not mit["dual"]) else 0.0
        return _frei_anteil(m, mit) * r * max(kv.mindestbemessung, arbeitseinkommen + lohn)

    kosten_grenze = 0.0
    if verloren:
        if geplant:
            monate = range(kv.geplant_ab_monat, 9)
        else:
            u, acc, monate = rng.random(), 0.0, ()
            for p, mm in kv.ungeplant:
                acc += p
                if u < acc:
                    monate = mm
                    break
        kosten_grenze = sum(beitrag(m, a_monat) for m in monate)
    kosten_hb = 0.0
    if hb_monate and wochenstunden > 30 and gewinn_sommer / len(hb_monate) > kv.schwelle_hauptberuflich \
            and rng.random() < kv.p_hauptberuflich:
        kosten_hb = sum(beitrag(m, gewinn_sommer / len(hb_monate)) for m in hb_monate)
    bis = max(kosten_grenze, kosten_hb)
    danach = 0.0
    if bis > 0 and not mit["dual"]:
        danach = kv.p_september * r * max(kv.mindestbemessung, a_monat)
    return bis, danach


# --------------------------------------------------------------------------
# Ergebnis einer Option in einem Lauf
# --------------------------------------------------------------------------

@dataclass
class Ergebnis:
    zusatz: v.Zusatz
    gewinn: float                 # Geschäftsgewinn bis 31.08.2027 verdient (vor Steuer), auch negativ
    stunden: float                # eigene Stunden im Geschäft
    go: bool | None = None        # Entscheidung am Frühindikator (None: kein Stufenplan)
    abbruch: bool = False
    offen: float = 0.0            # verdient, aber am 31.08. noch nicht bezahlt
    nachlauf: float = 0.0         # Gewinn 2027 aus Arbeit nach dem 31.08. (nicht im Netto bis 31.08.)
    kosten_privat: float = 0.0    # Mehrkosten, die nicht im Gewinn stehen (Verpflegung auf Reisen)
    hb_monate: tuple = ()         # Monate mit Vollzeit-Selbstständigkeit (Hauptberuflichkeit)
    gewinn_sommer: float = 0.0    # davon im Sommer (für die Hauptberuflichkeit)
    wochenstunden: float = 0.0    # eigene Stunden je Woche im Sommer
    info: dict = field(default_factory=dict)


def _spaeter_job(rng: random.Random, rest_anteil: float, p_finden: tuple) -> float:
    """Anteil des Sommers, den ein später Sommerjob nach einem Abbruch noch abdeckt."""
    return rest_anteil if rest_anteil > 0 and rng.random() < d(rng, p_finden) else 0.0


class Option:
    name = ""
    kurz = ""
    prognose = 0.0    # erwarteter Jahresgewinn bei Go (für die Prognose bei der Krankenkasse)

    def vorbereiten(self, rng: random.Random, a: v.Annahmen) -> tuple[v.Annahmen, dict]:
        return a, {}

    def ziehen(self, rng: random.Random, basis: dict, zustand: dict) -> Ergebnis:
        raise NotImplementedError


# --------------------------------------------------------------------------
# Webgeschäft im Sommer (Recherche: Quoten, Pool, Saison, Preise, Verzögerungen)
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class WebParameter:
    """Vertrieb wie in plan/simulation.py (sommer_meilensteine), korrigiert nach der Recherche."""
    p_einstieg: tuple = (0.005, 0.02, 0.05)       # je kaltem Vor-Ort-Kontakt (inkl. "Inhaber nicht da")
    p_upsell: tuple = (0.05, 0.15, 0.30)          # Einstieg -> Paket
    p_direkt: tuple = (0.0, 0.002, 0.006)         # Paket ohne Einstieg je Kontakt
    rho: float = 0.7                              # Zugkraft im Schuljahr <-> im Sommer (gleiche Person)
    saison_juli: tuple = (0.7, 0.9, 1.0)          # Juni/Juli fast normal
    saison_august: tuple = (0.4, 0.65, 0.9)       # Bayern: Ferien ab 02.08., B2B-Sommertal
    paket_preis: tuple = (800, 1_300, 2_200)      # Neuling gegen KI-Baukästen und Billiganbieter
    einstieg_preis: tuple = (69, 180, 349)
    betreuung: tuple = (49, 59, 89)
    anteil_betreuung: tuple = (0.4, 0.6, 0.8)
    paket_h: tuple = (20, 30, 50)
    einstieg_h: tuple = (1.5, 3, 5)
    kontakt_h: tuple = (0.4, 0.55, 0.9)           # inkl. Leadrecherche, Fahrt, Nachfassen
    pool: tuple = (150, 400, 900)                 # Nahbereich mit sichtbarem Mangel und erreichbarem Inhaber
    ausweichen_h: tuple = (1.4, 1.7, 2.2)         # danach weiterer Umkreis: Kontaktzeit x, Quote x 0,8
    empfehlung: tuple = (0.05, 0.15, 0.30)        # warme Leads je fertigem Paket
    warm_einstieg: tuple = (0.10, 0.25, 0.40)
    warm_paket: tuple = (0.02, 0.05, 0.10)
    uebertrag: tuple = (1.0, 1.3, 1.6)            # Einstiegskunden aus dem Schuljahr je Testkunde
    upsell_tage: tuple = (7, 21, 45)              # Kalendertage bis zur Paketentscheidung
    anzahlung: tuple = (0.0, 0.3, 0.5)
    inhalte_tage: tuple = (10, 25, 50)            # Kunde liefert Texte und Fotos
    zahlung_tage: tuple = (3, 14, 35)             # Creditreform: Zahlungsziel 26-32 Tage, Verzug 7,5
    anteil_lieferung: float = 0.7                 # höchstens 70 % des Tages für Lieferung
    stunden_tag: tuple = (6, 8, 10)
    disziplin: tuple = (0.7, 0.85, 1.0)
    kosten_kontakt: tuple = (0.5, 1.0, 2.0)
    kosten_paket: tuple = (30, 90, 150)
    fix: tuple = (100, 300, 500)
    kontakte_winter_je_h: float = 0.5 / 0.55      # Anteil Akquise an den Web-Stunden im Schuljahr / Kontaktzeit
    testwoche_kontakte: tuple = (50, 70, 90)      # Testwoche in den Frühjahrsferien statt Ferienjob
    abbruch_tag: int = 10                         # Abbruchregel: nach 10 Arbeitstagen ...
    abbruch_schwelle: int = 3                     # ... mindestens 3 Abschlüsse (Einstiege + Pakete)
    wechsel_tage: tuple = (2, 4, 8)
    abend_h_nach_abbruch: float = 1.5
    p_spaeter_job: tuple = (0.7, 0.85, 0.95)      # Zeitarbeit im Sommer meist zu bekommen


def web_welt(rng: random.Random, u: float, p: WebParameter) -> dict:
    """Die wahren (unbekannten) Werte dieser Person und dieses Markts."""
    ue = korreliert(rng, u, p.rho)
    return {
        "p_e": dreieck_quantil(p.p_einstieg, ue), "p_u": d(rng, p.p_upsell), "p_d": d(rng, p.p_direkt),
        "juli": d(rng, p.saison_juli), "august": d(rng, p.saison_august),
        "paket": d(rng, p.paket_preis), "einstieg": d(rng, p.einstieg_preis),
        "betreuung": d(rng, p.betreuung), "anteil_betreuung": d(rng, p.anteil_betreuung),
        "paket_h": d(rng, p.paket_h), "einstieg_h": d(rng, p.einstieg_h), "kontakt_h": d(rng, p.kontakt_h),
        "pool": d(rng, p.pool), "ausweichen": d(rng, p.ausweichen_h), "empfehlung": d(rng, p.empfehlung),
        "warm_e": d(rng, p.warm_einstieg), "warm_p": d(rng, p.warm_paket),
        "kosten_kontakt": d(rng, p.kosten_kontakt), "kosten_paket": d(rng, p.kosten_paket),
    }


def web_test(rng: random.Random, w: dict, kontakte: int) -> tuple[int, int]:
    """Beobachtete Einstiege und Pakete aus den Kaltkontakten bis 31.03. (Saison 1,0)."""
    e = binomial(rng, kontakte, w["p_e"])
    pk = binomial(rng, e, w["p_u"] * 0.5) + binomial(rng, kontakte, w["p_d"])
    return e, pk


def web_sommer(rng: random.Random, w: dict, p: WebParameter, tage: int, stunden_tag, kontakte_winter: float,
               testkunden: int, abbruch: bool) -> dict:
    """Sommer Tag für Tag: Akquise, Lieferung, Paketentscheidungen, Inhalte, Zahlungen.

    ``stunden_tag(t)``: Web-Stunden am Sommer-Arbeitstag t (0 = 28.06.).
    """
    pool = max(0.0, w["pool"] - kontakte_winter)
    schlange: list = []          # [Reststunden, Art, Preis]
    termine: list = []           # (Tag, Art, Preis): Upsell-Entscheidung oder Inhalte da
    verdient = bezahlt = kosten = 0.0
    einstiege = pakete = live = 0
    kontakte = 0.0
    stunden = 0.0
    abbruch_tag = None
    rest_kontakt = 0.0

    def paket_bestellt(t: float):
        nonlocal verdient, bezahlt, pakete, kosten
        pakete += 1
        preis = w["paket"] * rng.uniform(0.85, 1.15)
        anz = d(rng, p.anzahlung)
        verdient += anz * preis
        bezahlt += anz * preis
        kosten += w["kosten_paket"]
        termine.append((t + d(rng, p.inhalte_tage) * KAL_ZU_ARBEITSTAGEN, "inhalte", preis * (1 - anz)))

    def einstieg_gewonnen():
        nonlocal einstiege
        einstiege += 1
        schlange.append([w["einstieg_h"], "einstieg", w["einstieg"] * rng.uniform(0.85, 1.15)])

    # Einstiegskunden aus dem Schuljahr entscheiden sich in den ersten Sommerwochen
    for _ in range(int(testkunden * d(rng, p.uebertrag))):
        if rng.random() < w["p_u"] * 0.4:
            termine.append((rng.uniform(0, 30) * KAL_ZU_ARBEITSTAGEN, "upsell_ja", 0.0))

    for t in range(tage):
        if abbruch_tag is None:
            h = stunden_tag(t)
        else:
            h = p.abend_h_nach_abbruch if t >= abbruch_tag else stunden_tag(t)
        # fällige Termine
        for termin in [x for x in termine if x[0] <= t]:
            termine.remove(termin)
            if termin[1] == "upsell_ja":
                paket_bestellt(t)
            elif termin[1] == "inhalte":
                schlange.append([w["paket_h"], "paket", termin[2]])
        if h <= 0:
            continue
        stunden += h
        saison = w["juli"] if monat_von_tag(t) <= 7 else w["august"]
        offen_h = sum(x[0] for x in schlange)
        nach_abbruch = abbruch_tag is not None and t >= abbruch_tag
        liefer = min(offen_h, h) if nach_abbruch else min(offen_h, p.anteil_lieferung * h)
        akquise = 0.0 if nach_abbruch else h - liefer
        while liefer > 1e-9 and schlange:
            x = schlange[0]
            schritt = min(liefer, x[0])
            x[0] -= schritt
            liefer -= schritt
            if x[0] <= 1e-9:
                schlange.pop(0)
                if x[1] == "einstieg":
                    verdient += x[2]
                    bezahlt += x[2]
                    if rng.random() < w["p_u"]:
                        termine.append((t + d(rng, p.upsell_tage) * KAL_ZU_ARBEITSTAGEN, "upsell_ja", 0.0))
                else:
                    live += 1
                    verdient += x[2]
                    if t + d(rng, p.zahlung_tage) * KAL_ZU_ARBEITSTAGEN < tage:
                        bezahlt += x[2]
                    if rng.random() < w["anteil_betreuung"]:
                        monate = int((tage - t) / 21.7)
                        verdient += monate * w["betreuung"]
                        bezahlt += monate * w["betreuung"]
                    for _ in range(poisson(rng, w["empfehlung"])):
                        if rng.random() < w["warm_p"]:
                            paket_bestellt(t)
                        elif rng.random() < w["warm_e"]:
                            einstieg_gewonnen()
        # Akquise: Kaltkontakte vor Ort
        rest_kontakt += akquise
        while True:
            weit = kontakte >= pool
            h_k = w["kontakt_h"] * (w["ausweichen"] if weit else 1.0)
            if rest_kontakt < h_k:
                break
            rest_kontakt -= h_k
            kontakte += 1
            kosten += w["kosten_kontakt"] * (1.5 if weit else 1.0)
            q = saison * (0.8 if weit else 1.0)
            if rng.random() < w["p_e"] * q:
                einstieg_gewonnen()
            elif rng.random() < w["p_d"] * q:
                paket_bestellt(t)
        if abbruch and abbruch_tag is None and t + 1 == p.abbruch_tag and einstiege + pakete < p.abbruch_schwelle:
            abbruch_tag = t + 1 + int(round(d(rng, p.wechsel_tage)))
    # Was am 31.08. noch offen ist, wird im September/Oktober fertig (Nachlauf, nicht im Netto bis 31.08.)
    nachlauf = (sum(x[2] for x in schlange) + sum(x[2] for x in termine if x[1] == "inhalte"))
    return {"verdient": verdient, "bezahlt": bezahlt, "kosten": kosten, "nachlauf": nachlauf,
            "einstiege": einstiege, "pakete": pakete, "live": live, "kontakte": kontakte,
            "stunden": stunden, "abbruch_tag": abbruch_tag}


class WebSommer(Option):
    """Webgeschäft im Sommer: nebenher (abends), an 2 Tagen je Woche oder in Vollzeit."""

    ARTEN = {
        "abends": "abends neben dem Vollzeit-Sommerjob (~1,6 h je Arbeitstag)",
        "2tage": "an 2 Tagen je Woche, dazu 3-Tage-Sommerjob",
        "vollzeit": "in Vollzeit statt Sommerjob, Abbruch nach 10 Tagen ohne 3 Abschlüsse",
        "vollzeit_start": "in Vollzeit nur bei Startregel (Testwoche im Februar, >= 5 Einstiege und 1 Paket "
                          "bis 31.03.), sonst Sommerjob",
    }

    def __init__(self, art: str = "abends", p: WebParameter = WebParameter()):
        self.art, self.p = art, p
        self.name = f"Webgeschäft im Sommer {self.ARTEN[art]}"
        self.kurz = f"web_{art}"

    def vorbereiten(self, rng, a):
        # Gleiche Zugkraft im Schuljahr und im Sommer: der Web-Satz des Job-Wegs wird für diesen
        # Lauf aus demselben Anteil u gezogen (gleiche Verteilung wie im Job-Weg)
        u = rng.random()
        regel = tuple(replace(r, satz=(dreieck_quantil(r.satz, u),) * 3) if r.name == WEB else r
                      for r in a.regelmaessig)
        return replace(a, regelmaessig=regel), {"u": u}

    def ziehen(self, rng, basis, zustand):
        p = self.p
        w = web_welt(rng, zustand["u"], p)
        kontakte_winter = p.kontakte_winter_je_h * basis["stunden_je_quelle"].get(WEB, 0.0)
        e_w, pk_w = web_test(rng, w, int(kontakte_winter))
        zusatz_vorab = {}
        vorab_gewinn, vorab_h = 0.0, 0.0
        if self.art == "vollzeit_start":
            test = int(d(rng, p.testwoche_kontakte))
            e_t, pk_t = web_test(rng, w, test)
            zusatz_vorab = {"ferientage": ((PH_FRUEH, 5.0),)}
            vorab_h = 40.0
            vorab_gewinn = e_t * w["einstieg"] + pk_t * w["paket"] * 0.5 - test * w["kosten_kontakt"]
            e_w, pk_w, kontakte_winter = e_w + e_t, pk_w + pk_t, kontakte_winter + test
            # Startregel der Recherche: >= 5 bezahlte Einstiege aus >= 100 Kaltkontakten und
            # mindestens ein Paket zu einem Preis, der den Sommer tragen kann (>= 1.600 EUR)
            go = kontakte_winter >= 100 and e_w >= 5 and pk_w >= 1 and w["paket"] >= 1_600
            if not go:
                z = v.Zusatz(gewinn=((2027, vorab_gewinn),), **zusatz_vorab)
                return Ergebnis(z, vorab_gewinn, vorab_h, go=False, info={"einstiege_winter": e_w})
        tage = sommer_tage(basis)
        h_tag = d(rng, p.stunden_tag) * d(rng, p.disziplin)
        if self.art == "abends":
            h_abend = dreieck(rng, 1.0, 1.6, 2.0)
            fn, sommer_anteil, wochenstunden = (lambda t: h_abend), 1.0, 5 * h_abend
        elif self.art == "2tage":
            fn, sommer_anteil, wochenstunden = (lambda t: h_tag if t % 5 in (3, 4) else 0.0), 0.6, 2 * h_tag
        else:
            fn, sommer_anteil, wochenstunden = (lambda t: h_tag), 0.0, 5 * h_tag
        r = web_sommer(rng, w, p, tage, fn, kontakte_winter, e_w, abbruch=self.art.startswith("vollzeit"))
        gewinn = r["verdient"] - r["kosten"] - d(rng, p.fix) + vorab_gewinn
        teilzeit = True
        hb = ()
        if self.art.startswith("vollzeit"):
            hb = (7, 8) if tage > 25 else (7,)
            if r["abbruch_tag"] is not None:
                rest = max(0.0, 1 - r["abbruch_tag"] / tage)
                sommer_anteil, teilzeit = _spaeter_job(rng, rest, p.p_spaeter_job), False
                hb = (7,)
        z = v.Zusatz(sommer_anteil=sommer_anteil, sommer_teilzeit=teilzeit, gewinn=((2027, gewinn),),
                     **zusatz_vorab)
        return Ergebnis(z, gewinn, r["stunden"] + vorab_h, go=True, abbruch=r["abbruch_tag"] is not None,
                        offen=r["verdient"] - r["bezahlt"], nachlauf=r["nachlauf"], hb_monate=hb,
                        gewinn_sommer=gewinn, wochenstunden=wochenstunden,
                        info={"pakete": r["pakete"], "einstiege": r["einstiege"], "kontakte": r["kontakte"]})


# --------------------------------------------------------------------------
# Umzugs-Trageteam mit Helfern (Recherche Kategorie A, mit Korrekturen)
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class UmzugParameter:
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
        art = ("nur Fr/Sa und Monatsende, dazu 3-Tage-Sommerjob (Mo–Mi)" if hybrid else "statt Sommerjob")
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
        wochen = sommer_tage(basis) / 5
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
        sommer_gewinn = (umsatz * (1 - d(rng, p.ausfall)) - auftraege * d(rng, p.lead) - d(rng, p.fix)
                         - schaden - helfer * kosten_h)
        gewinn = vorab + sommer_gewinn
        pruefzeit = d(rng, p.pruefzeit_h)
        sommer_h = eigen + auftraege * 3.0 + wochen_aktiv * 4
        sommer_job, teilzeit = (0.6 if self.hybrid else 0.0), True
        if abbruch:
            sommer_job, teilzeit = _spaeter_job(rng, max(0.0, 1 - 3 / wochen), p.p_spaeter_job), False
        z = v.Zusatz(stunden=stunden_vorab + ((PH_PRUEF, pruefzeit),), sommer_anteil=sommer_job,
                     sommer_teilzeit=teilzeit, sommer_samstage=0.0, gewinn=((2027, gewinn),))
        return Ergebnis(z, gewinn, aufbau + pruefzeit + sommer_h, go=True, abbruch=abbruch,
                        hb_monate=() if self.hybrid else ((7,) if abbruch else (7, 8)),
                        gewinn_sommer=sommer_gewinn, wochenstunden=sommer_h / max(wochen_aktiv, 1e-9),
                        info={"anfragen": anfragen, "auftraege": auftraege, "helferstunden": helfer})


# --------------------------------------------------------------------------
# Fotobox, Flipping, Wettbewerb (Recherche Kategorien C, D und Vollständigkeitsprüfung)
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class FotoboxParameter:
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
        frei = max(0.0, 1 - events_sommer / (sommer_tage(basis) / 5))    # ein Event je belegtem Samstag
        z = v.Zusatz(stunden=((PH_DEZ, 0.3 * aufbau), (PH_JAN, 0.7 * aufbau + vor / 2), (PH_PRUEF, vor / 2)),
                     sommer_samstage=frei, gewinn=((2027, gewinn),))
        return Ergebnis(z, gewinn, aufbau + event_h, info={"events": n})


class Flipping(Option):
    """Gebrauchte Smartphones, Konsolen, Laptops aufbereiten und verkaufen."""
    name = "Technik-Flipping neben Schule und Sommerjob"
    kurz = "flipping"

    def ziehen(self, rng, basis, zustand):
        h_schule = 14 * rng.uniform(3, 7)
        h_ferien = 3 * rng.uniform(5, 20)
        h_pruef = rng.uniform(0, 15)
        h_sommer = 10 * rng.uniform(3, 8)                 # Abende neben dem Vollzeitjob
        abbruch = rng.random() < 0.35                     # JPMorgan: 71 % der Marktplatz-Verkäufer nur 1-3 Monate aktiv
        if abbruch:
            f = rng.uniform(0.15, 0.35)
            h_schule, h_ferien, h_pruef, h_sommer = h_schule * f, h_ferien * f, 0.0, 0.0
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
        gewinn = preis - reise                            # Preisgeld vermutlich Betriebseinnahme
        z = v.Zusatz(stunden=((PH_JAN, stunden),), gewinn=((2027, gewinn),))
        return Ergebnis(z, gewinn, stunden, go=True, info={"preis": preis})


# --------------------------------------------------------------------------
# Provisionsvertrieb im Sommer (Recherche: Fundraising-Agenturen, Glasfaser-Haustür)
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class ProvisionParameter:
    # Fundraising angestellt (Kober: 2.700 EUR / 5 Wochen 2026; DialogDirect 2.016 EUR / 4 Wochen)
    fixum_woche: tuple = (530, 550, 600)
    praemie_median: float = 180.0                 # volle Routine, lognormal sigma 0,8 (~15 % unter Firmenangaben)
    praemie_faktor: tuple = (0.7, 1.0, 1.3)
    praemie_sigma: float = 0.8
    ramp: tuple = (0.2, 0.6)                      # Woche 1, 2, danach 1,0
    rauschen: float = 0.35
    hazard_fundraising: tuple = (0.18, 0.12, 0.07, 0.04)   # je Woche, danach 0,04
    einsatz_wochen: int = 5
    p_zweiter: tuple = (0.35, 0.65)               # untere / obere Leistungshälfte
    startpraemie: float = 500.0
    verpflegung_woche: tuple = (40, 70, 100)
    # Glasfaser-Haustür als freier Handelsvertreter
    vertraege_tag: float = 2.0                    # Median volle Routine; Anzeigen: Ø 5 bei Durchhaltern
    vertraege_faktor: tuple = (0.6, 1.0, 1.4)
    vertraege_sigma: float = 0.75
    provision: tuple = (50, 85, 150)
    storno: tuple = (0.10, 0.20, 0.35)
    tage_woche: float = 5.5
    ramp_glasfaser: tuple = (0.35, 0.7)
    hazard_glasfaser: tuple = (0.25, 0.15, 0.10, 0.06)     # danach 0,05
    kosten_woche: tuple = (20, 50, 120)
    p_lokal: float = 0.5
    unterkunft_woche: tuple = (0, 150, 350)
    ausgezahlt: tuple = (0.5, 0.75, 0.9)          # bis 31.08. (Widerrufsfrist, Abrechnungsmonat)
    # Rückfall nach Abbruch
    suche_tage: tuple = (2, 5, 10)
    p_finden: float = 0.8


def _wochen_lauf(rng: random.Random, wochen: float, hazard: tuple, spaet: float, u: float) -> list[float]:
    """Arbeitswochen bis zum Abbruch: Liste der Wochenanteile (1,0 oder Rest)."""
    faktor = 1.8 if u < 1 / 3 else (0.5 if u > 2 / 3 else 1.0)
    meta = dreieck(rng, 0.6, 1.0, 1.5)
    gearbeitet, w = [], 0
    while w < wochen:
        anteil = min(1.0, wochen - w)
        gearbeitet.append(anteil)
        w += 1
        h = (hazard[w - 1] if w - 1 < len(hazard) else spaet) * faktor * meta
        if w < wochen and rng.random() < h:
            break
    return gearbeitet


class Provision(Option):
    """Sommer im Provisionsvertrieb statt im Industrie-Sommerjob."""

    def __init__(self, art: str = "fundraising", stopp_woche2: float | None = None,
                 p: ProvisionParameter = ProvisionParameter()):
        self.art, self.stopp, self.p = art, stopp_woche2, p
        if art == "fundraising":
            self.name = "Spendenwerbung angestellt (Reiseteam, Fixum + Prämie) statt Sommerjob"
        else:
            self.name = "Glasfaser-Haustürvertrieb als Handelsvertreter statt Sommerjob" + (
                f", Stopp nach Woche 2 unter {stopp_woche2:,.0f} EUR/Woche".replace(",", ".") if stopp_woche2 else "")
        self.kurz = art + ("_stopp" if stopp_woche2 else "")

    def _rueckfall_tage(self, rng: random.Random, rest_wochen: float, heimreise: float) -> float:
        p = self.p
        rest_tage = max(0.0, rest_wochen * 5 - heimreise - d(rng, p.suche_tage))
        if rest_tage > 0 and rng.random() < p.p_finden * (0.6 if rest_tage < 10 else 1.0):
            return rest_tage
        return 0.0

    def ziehen(self, rng, basis, zustand):
        p = self.p
        tage = sommer_tage(basis)
        wochen = tage / 5
        u = rng.random()
        if self.art == "fundraising":
            praemie = lognormal_quantil(p.praemie_median * d(rng, p.praemie_faktor), p.praemie_sigma, u)
            fixum = d(rng, p.fixum_woche)
            erster = min(p.einsatz_wochen, wochen)
            lauf = _wochen_lauf(rng, erster, p.hazard_fundraising, 0.04, u)
            if sum(lauf) >= erster - 1e-9 and wochen > p.einsatz_wochen and rng.random() < p.p_zweiter[u > 0.5]:
                lauf += _wochen_lauf(rng, wochen - p.einsatz_wochen, (0.04,), 0.04, u)
            brutto = 0.0
            for i, anteil in enumerate(lauf):
                ramp = p.ramp[i] if i < len(p.ramp) else 1.0
                rausch = math.exp(rng.gauss(-p.rauschen ** 2 / 2, p.rauschen))
                brutto += anteil * (fixum + praemie * ramp * rausch)
            if sum(lauf[:5]) >= 4 and rng.random() < 0.5:
                brutto += p.startpraemie
            gearbeitet = sum(lauf)
            kosten_privat = gearbeitet * d(rng, p.verpflegung_woche)
            rest = wochen - gearbeitet
            abbruch = rest > 1e-9
            if abbruch:   # Heimreise, Suche, später Job (30 % Industrie, sonst Aushilfe/Zeitarbeit)
                rest_tage = self._rueckfall_tage(rng, rest, 1.0)
                if rest_tage > 0:
                    satz = d(rng, v.SATZ_INDUSTRIE if rng.random() < 0.3 else v.SATZ_SONST)
                    brutto += rest_tage * dreieck(rng, 7.5, 8.0, 9.0) * satz
            z = v.Zusatz(sommer_brutto=brutto, sommer_samstage=0.0)
            return Ergebnis(z, 0.0, gearbeitet * 45, abbruch=sum(lauf[:5]) < min(5, wochen) - 1e-9,
                            kosten_privat=kosten_privat,
                            info={"brutto": brutto, "wochen": gearbeitet})
        # Glasfaser-Haustür, selbstständig
        vertraege = lognormal_quantil(p.vertraege_tag * d(rng, p.vertraege_faktor), p.vertraege_sigma, u)
        provision, storno = d(rng, p.provision), d(rng, p.storno)
        lokal = rng.random() < p.p_lokal
        lauf = _wochen_lauf(rng, wochen, p.hazard_glasfaser, 0.05, u)
        gewinn, gestoppt = -40.0, False
        for i, anteil in enumerate(lauf):
            ramp = p.ramp_glasfaser[i] if i < len(p.ramp_glasfaser) else 1.0
            rausch = math.exp(rng.gauss(-p.rauschen ** 2 / 2, p.rauschen))
            woche = vertraege * p.tage_woche * ramp * rausch * provision * (1 - storno)
            kosten = d(rng, p.kosten_woche) + (0.0 if lokal else d(rng, p.unterkunft_woche))
            gewinn += anteil * (woche - kosten)
            if self.stopp and i == 1 and len(lauf) > 2 and (gewinn + 40.0) / 2 < self.stopp:
                lauf, gestoppt = lauf[:2], True
                break
        gearbeitet = sum(lauf)
        rest = wochen - gearbeitet
        sommer_anteil = 0.0
        if rest > 1e-9:
            sommer_anteil = self._rueckfall_tage(rng, rest, 0.0 if lokal else 1.0) / tage
        offen = max(0.0, gewinn) * (1 - d(rng, p.ausgezahlt))
        z = v.Zusatz(sommer_anteil=sommer_anteil, sommer_teilzeit=False, sommer_samstage=0.0,
                     gewinn=((2027, gewinn),))
        return Ergebnis(z, gewinn, gearbeitet * p.tage_woche * 8, abbruch=rest > 1e-9, offen=offen,
                        hb_monate=(7, 8) if gearbeitet > 4.5 else (7,), gewinn_sommer=gewinn,
                        wochenstunden=p.tage_woche * 8, info={"wochen": gearbeitet, "gestoppt": gestoppt})


class Kombination(Option):
    """Mehrere Optionen zugleich: Stunden und Gewinne addieren sich, den Sommer ändert nur eine."""

    def __init__(self, name: str, kurz: str, teile: tuple):
        self.name, self.kurz, self.teile = name, kurz, teile

    @property
    def prognose(self):
        return sum(t.prognose for t in self.teile)

    def vorbereiten(self, rng, a):
        zustaende = []
        for t in self.teile:
            a, z = t.vorbereiten(rng, a)
            zustaende.append(z)
        return a, {"teile": zustaende}

    def ziehen(self, rng, basis, zustand):
        ergs = [t.ziehen(rng, basis, z) for t, z in zip(self.teile, zustand["teile"])]
        sommer = [e.zusatz for e in ergs if e.zusatz.sommer_anteil < 1 or e.zusatz.sommer_samstage < 1
                  or e.zusatz.sommer_brutto is not None]
        if len(sommer) > 1:
            raise ValueError("Nur eine Option darf den Sommer ändern")
        s = sommer[0] if sommer else v.Zusatz()
        gewinn = sum(e.gewinn for e in ergs)
        z = v.Zusatz(stunden=tuple(x for e in ergs for x in e.zusatz.stunden),
                     ferientage=tuple(x for e in ergs for x in e.zusatz.ferientage),
                     sommer_anteil=s.sommer_anteil, sommer_teilzeit=s.sommer_teilzeit,
                     sommer_samstage=s.sommer_samstage, sommer_brutto=s.sommer_brutto, gewinn=((2027, gewinn),))
        hb = max(ergs, key=lambda e: len(e.hb_monate))
        gos = [e.go for e in ergs if e.go is not None]
        return Ergebnis(z, gewinn, sum(e.stunden for e in ergs), go=any(gos) if gos else None,
                        abbruch=any(e.abbruch for e in ergs), offen=sum(e.offen for e in ergs),
                        nachlauf=sum(e.nachlauf for e in ergs), kosten_privat=sum(e.kosten_privat for e in ergs),
                        hb_monate=hb.hb_monate, gewinn_sommer=hb.gewinn_sommer, wochenstunden=hb.wochenstunden)


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
    verloren = famv_verloren(mit["pruef"][2027], a_lauf, erg.nachlauf)
    # Ehrliche Prognose bei der Kasse: Gewinn des Job-Wegs plus erwarteter Gewinn des Geschäfts
    geplant = erg.go is not False and basis["pruef"][2027]["selbst"] + option.prognose > GRENZE_JAHR
    kv_bis, kv_danach = kv_kosten(rng_o, kv, mit, mit["pruef"][2027]["selbst"] + erg.nachlauf, verloren, geplant,
                                  erg.hb_monate, erg.gewinn_sommer, erg.wochenstunden)
    netto = mit["netto"] - kv_bis - erg.kosten_privat
    return {"basis": basis["netto"], "netto": netto, "mehr": netto - basis["netto"],
            "basis_kontostand": basis["kontostand"],
            "kontostand": mit["kontostand"] - kv_bis - erg.kosten_privat - erg.offen,
            "gewinn": erg.gewinn, "nachlauf": erg.nachlauf, "stunden": erg.stunden,
            "go": erg.go, "abbruch": erg.abbruch, "famv_weg": verloren or kv_bis > 0, "kv": kv_bis,
            "kv_danach": kv_danach, "dual": basis["dual"], "info": erg.info}


def kalibrieren(option: Option, n: int = 600, seed: int = 99) -> float:
    """Erwarteter Jahresgewinn bei Go (Median) – das, was man der Krankenkasse ehrlich angibt."""
    teile = getattr(option, "teile", None)
    if teile:
        for t in teile:
            kalibrieren(t, n, seed)
        return option.prognose
    a = v.Annahmen()
    werte = []
    for i in range(n):
        s = seed * 1_000_003 + i
        rng_o = random.Random(s * 7 + 3)
        a_lauf, zustand = option.vorbereiten(rng_o, a)
        basis = v.ein_verlauf(random.Random(s), a_lauf, v.Zusatz())
        erg = option.ziehen(rng_o, basis, zustand)
        if erg.go is not False:
            werte.append(erg.gewinn + erg.nachlauf)
    option.prognose = sorted(werte)[len(werte) // 2] if werte else 0.0
    return option.prognose


def _q(xs: list, p: float) -> float:
    return xs[min(len(xs) - 1, int(len(xs) * p))]


def auswerten(option: Option, n: int = 10_000, seed: int = 2027, a: v.Annahmen | None = None,
              kv: KV = KV(), nur: str | None = None) -> dict:
    """Verteilungen; ``nur``: "fh" oder "dual" filtert die Läufe nach dem Weg nach dem Abitur."""
    kalibrieren(option)
    laeufe = [vergleich(option, i, seed, a, kv) for i in range(n)]
    if nur:
        laeufe = [x for x in laeufe if x["dual"] == (nur == "dual")]
    m = len(laeufe)
    netto = sorted(x["netto"] for x in laeufe)
    basis = sorted(x["basis"] for x in laeufe)
    mehr = sorted(x["mehr"] for x in laeufe)
    gewinn = sorted(x["gewinn"] for x in laeufe)
    go = [x for x in laeufe if x["go"]]
    mit_go = any(x["go"] is not None for x in laeufe)
    return {
        "name": option.name, "kurz": option.kurz, "n": m, "prognose": option.prognose,
        "p10": _q(netto, 0.10), "median": _q(netto, 0.5), "p90": _q(netto, 0.90), "p99": _q(netto, 0.99),
        "mittel": sum(netto) / m,
        "basis_p10": _q(basis, 0.10), "basis_median": _q(basis, 0.5), "basis_p90": _q(basis, 0.90),
        "basis_p99": _q(basis, 0.99), "basis_mittel": sum(basis) / m,
        "mehr_p10": _q(mehr, 0.10), "mehr_median": _q(mehr, 0.5), "mehr_p90": _q(mehr, 0.90),
        "mehr_p99": _q(mehr, 0.99), "mehr_mittel": sum(mehr) / m,
        "p_besser": sum(1 for x in mehr if x > 0) / m,
        "p_deutlich_besser": sum(1 for x in mehr if x > 2_000) / m,
        "p_deutlich_schlechter": sum(1 for x in mehr if x < -2_000) / m,
        "gewinn_median": _q(gewinn, 0.5), "gewinn_p90": _q(gewinn, 0.90), "gewinn_p99": _q(gewinn, 0.99),
        "p_geschaeftsverlust": sum(1 for x in gewinn if x < 0) / m,
        "nachlauf_mittel": sum(x["nachlauf"] for x in laeufe) / m,
        "p_go": len(go) / m if mit_go else None,
        "mehr_median_go": _q(sorted(x["mehr"] for x in go), 0.5) if go else None,
        "p_besser_go": sum(1 for x in go if x["mehr"] > 0) / len(go) if go else None,
        "p_abbruch": sum(1 for x in laeufe if x["abbruch"]) / m,
        "p_famv_weg": sum(1 for x in laeufe if x["famv_weg"]) / m,
        "kv_mittel": sum(x["kv"] for x in laeufe) / m,
        "kv_danach_mittel": sum(x["kv_danach"] for x in laeufe) / m,
        "stunden_median": _q(sorted(x["stunden"] for x in laeufe), 0.5),
        "kontostand_median": _q(sorted(x["kontostand"] for x in laeufe), 0.5),
        "basis_kontostand_median": _q(sorted(x["basis_kontostand"] for x in laeufe), 0.5),
    }


# Optimistische Gegenproben: die alten Annahmen bzw. Firmenangaben ohne Abschlag
WEB_OPTIMISTISCH = WebParameter(p_einstieg=(0.01, 0.03, 0.07), p_upsell=(0.10, 0.25, 0.40),
                                paket_preis=(1_400, 1_900, 2_600), saison_juli=(1.0, 1.0, 1.0),
                                saison_august=(1.0, 1.0, 1.0), inhalte_tage=(5, 10, 20), anzahlung=(0.3, 0.5, 0.5))
PROVISION_OPTIMISTISCH = ProvisionParameter(vertraege_tag=2.9, praemie_median=260.0,
                                            hazard_fundraising=(0.09, 0.06, 0.035, 0.02),
                                            hazard_glasfaser=(0.125, 0.075, 0.05, 0.03))


def gegenproben() -> list[Option]:
    web = WebSommer("vollzeit", WEB_OPTIMISTISCH)
    web.name += " – optimistisch (alte Quoten und Preise, keine Saison)"
    web_abends = WebSommer("abends", WEB_OPTIMISTISCH)
    web_abends.name += " – optimistisch"
    fund = Provision("fundraising", p=PROVISION_OPTIMISTISCH)
    fund.name += " – optimistisch (Firmenangaben, halbe Abbrüche)"
    glas = Provision("glasfaser", p=PROVISION_OPTIMISTISCH)
    glas.name += " – optimistisch (Firmenangaben, halbe Abbrüche)"
    sehr_gut = StartupTeens(qualitaet_median=8.0)
    sehr_gut.name += " – sehr starkes Projekt"
    return [web, web_abends, fund, glas, sehr_gut]


def optionen() -> list[Option]:
    return [
        WebSommer("abends"),
        WebSommer("2tage"),
        WebSommer("vollzeit"),
        WebSommer("vollzeit_start"),
        Umzug(stufenplan=False),
        Umzug(stufenplan=True),
        Umzug(stufenplan=True, hybrid=True),
        Provision("fundraising"),
        Provision("glasfaser"),
        Provision("glasfaser", stopp_woche2=250.0),
        Fotobox(),
        Flipping(),
        StartupTeens(),
        Kombination("Kombination: Webgeschäft abends im Sommer + Startup Teens (mit Beleg)", "kombi_empfohlen",
                    (WebSommer("abends"), StartupTeens())),
    ]


def _eur(x: float) -> str:
    return f"{x:7,.0f}".replace(",", ".")


def _pz(x: float | None) -> str:
    return "   –" if x is None else f"{100 * x:3.0f} %"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--n", type=int, default=10_000)
    ap.add_argument("--nur", choices=("fh", "dual"), default=None, help="nur Studium (fh) oder dual/Ausbildung")
    ap.add_argument("--gegenproben", action="store_true", help="optimistische Annahmen statt der Hauptrechnung")
    args = ap.parse_args()
    print(f"Netto bis 31.08.2027 nach Steuer, Abgaben und Krankenversicherung – je Option gegen denselben "
          f"Job-Weg ({args.n} Läufe{', nur ' + args.nur if args.nur else ''})")
    print("-" * 118)
    for o in (gegenproben() if args.gegenproben else optionen()):
        r = auswerten(o, args.n, nur=args.nur)
        print(f"{o.name}")
        print(f"  gesamt        P10 {_eur(r['p10'])}  Median {_eur(r['median'])}  P90 {_eur(r['p90'])}  "
              f"P99 {_eur(r['p99'])}   (Job-Weg: {_eur(r['basis_p10'])} / {_eur(r['basis_median'])} / "
              f"{_eur(r['basis_p90'])} / {_eur(r['basis_p99'])})")
        print(f"  mehr als Job  P10 {_eur(r['mehr_p10'])}  Median {_eur(r['mehr_median'])}  P90 {_eur(r['mehr_p90'])}  "
              f"P99 {_eur(r['mehr_p99'])}  Mittel {_eur(r['mehr_mittel'])}   besser in {_pz(r['p_besser'])}, "
              f">2.000 besser {_pz(r['p_deutlich_besser'])}, >2.000 schlechter {_pz(r['p_deutlich_schlechter'])}")
        print(f"  Geschäft      Gewinn Median {_eur(r['gewinn_median'])}, P90 {_eur(r['gewinn_p90'])}, "
              f"P99 {_eur(r['gewinn_p99'])}, Verlust {_pz(r['p_geschaeftsverlust'])}; Nachlauf Ø "
              f"{_eur(r['nachlauf_mittel'])}; Go {_pz(r['p_go'])}, Abbruch {_pz(r['p_abbruch'])}; "
              f"Stunden Median {r['stunden_median']:.0f}")
        print(f"  Versicherung  Familienversicherung weg {_pz(r['p_famv_weg'])}, KV bis 31.08. Ø {_eur(r['kv_mittel'])}, "
              f"danach Ø {_eur(r['kv_danach_mittel'])}; Prognose {_eur(r['prognose'])}; Kontostand Median "
              f"{_eur(r['kontostand_median'])} (Job-Weg {_eur(r['basis_kontostand_median'])})")
        if r["p_go"] is not None and r["mehr_median_go"] is not None:
            print(f"  wenn Go       mehr als Job Median {_eur(r['mehr_median_go'])}, besser in {_pz(r['p_besser_go'])}")


if __name__ == "__main__":
    main()
