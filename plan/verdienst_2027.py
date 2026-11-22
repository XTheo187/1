"""Wie viel kann ich bis 31.08.2027 maximal erwirtschaften – neben dem Abitur?

Monte-Carlo über das Zeitbudget vom 23.11.2026 bis 31.08.2027. Jede Phase
(Schulzeit, Ferien, Prüfungen, nach dem Abitur) hat ein Stundenbudget, das
das Abitur schützt. In jeder Phase werden die verfügbaren Stunden den
Verdienstquellen mit dem höchsten Nettoerlös je Stunde zugeteilt, begrenzt
durch die Nachfrage (Nachhilfeschüler, Kunden, Jobangebote) und die Regeln
(Minijob-Grenze, Arbeitszeitgesetz). Am Ende werden Steuer und Abgaben für
2026 und 2027 abgezogen.

Aufruf:

    python3 plan/verdienst_2027.py            # Ergebnis und Strategien
    python3 plan/verdienst_2027.py --n 40000  # genauer

Die Eingaben stehen mit Quelle in docs/VERDIENST_BIS_SOMMER_2027.md.
"""

from __future__ import annotations

import argparse
import random
import sys
from dataclasses import dataclass, field, replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import simulation as sim  # noqa: E402

dreieck = sim.dreieck


# --------------------------------------------------------------------------
# Kalender und Zeitbudget
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Phase:
    name: str
    wochen: float
    stunden: tuple          # verfügbare Arbeitsstunden je Woche (min, Mitte, max)
    jahr: int               # Kalenderjahr (für die Steuer)
    vollzeit: bool = False  # Ferien-/Vollzeitjob möglich (ganze Woche frei)


# Bayern, Schuljahr 2026/27 (Termine in docs/VERDIENST_BIS_SOMMER_2027.md):
# Schulzeit mit Abiturvorbereitung, Ferien, schriftliches Abitur, mündliche
# Prüfungen, danach frei bis zum Ausbildungsbeginn im Herbst.
PHASEN = (
    Phase("Schulzeit Nov.–Dez. 2026", 4.4, (3, 5, 8), 2026),
    Phase("Weihnachtsferien", 2.0, (10, 20, 35), 2026, vollzeit=True),
    Phase("Schulzeit Jan.–Feb. 2027", 6.0, (3, 5, 8), 2027),
    Phase("Frühjahrsferien", 1.0, (10, 25, 40), 2027, vollzeit=True),
    Phase("Schulzeit März 2027", 4.0, (2, 4, 6), 2027),
    Phase("Osterferien und schriftliches Abitur", 7.0, (0, 1, 4), 2027),
    Phase("nach dem schriftlichen Abitur bis Ende Juni", 6.0, (15, 25, 35), 2027),
    Phase("Juli – August", 9.0, (35, 40, 48), 2027, vollzeit=True),
)


# --------------------------------------------------------------------------
# Verdienstquellen
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Quelle:
    name: str
    satz: tuple                 # Brutto je Stunde (min, Mitte, max), EUR
    max_woche: tuple            # Nachfrage: höchstens so viele Stunden je Woche
    art: str                    # "minijob", "ferienjob", "selbststaendig"
    nur_vollzeit: bool = False  # nur in Ferien/Vollzeit-Phasen
    p_verfuegbar: tuple = (1, 1, 1)   # Chance, so eine Stelle/Nachfrage überhaupt zu bekommen
    kosten: tuple = (0, 0, 0)   # Anteil Kosten am Umsatz (Fahrt, Software), nur selbstständig
    max_gesamt: tuple | None = None   # Obergrenze Stunden insgesamt (z. B. Leads)


QUELLEN = (
    # Werte werden nach der Recherche eingesetzt (siehe Dokument).
    Quelle("Ferienjob Industrie/Logistik (Schicht)", (14.6, 17.0, 21.0), (35, 40, 48), "ferienjob",
           nur_vollzeit=True, p_verfuegbar=(0.6, 0.8, 0.95)),
    Quelle("Aushilfe Mindestlohn (Lager, Gastro, Handel)", (14.6, 15.0, 16.5), (35, 40, 48), "ferienjob",
           nur_vollzeit=True),
    Quelle("Minijob während der Schulzeit", (13.9, 14.6, 15.5), (3, 6, 10), "minijob"),
    Quelle("Nachhilfe (privat)", (15, 20, 25), (1, 3, 6), "selbststaendig", p_verfuegbar=(0.6, 0.8, 0.95)),
    Quelle("Webgeschäft (standortcheck)", (9, 26, 40), (5, 15, 30), "selbststaendig",
           kosten=(0.05, 0.10, 0.20), max_gesamt=(60, 180, 400)),
)


@dataclass
class Annahmen:
    mindestlohn_2026: float = 13.90
    mindestlohn_2027: float = 14.60
    minijob_grenze_monat: float = 633.0      # 2027 (2026: 603)
    sv_ferienjob: tuple = (0.0, 0.0, 0.21)   # Anteil SV: kurzfristig 0, sonst ~21 %
    grundfreibetrag_2027: float = 12_348.0
    werbungskosten: float = 1_230.0
    familienversicherung_grenze_monat: float = 590.0  # 2027
    kv_selbst_monat: float = 0.0             # eigene KV, falls Familienversicherung endet
    quellen: tuple = field(default_factory=lambda: QUELLEN)
    phasen: tuple = field(default_factory=lambda: PHASEN)


def _ziehen(rng: random.Random, t: tuple) -> float:
    return dreieck(rng, *t) if t[0] != t[2] else float(t[0])


def ein_leben(rng: random.Random, a: Annahmen, strategie: str = "optimal") -> dict:
    """Ein simulierter Verlauf bis 31.08.2027. Rückgabe: Brutto und Netto je Quelle."""
    q = {}
    for quelle in a.quellen:
        verfuegbar = rng.random() < _ziehen(rng, quelle.p_verfuegbar)
        q[quelle.name] = dict(
            quelle=quelle, verfuegbar=verfuegbar, satz=_ziehen(rng, quelle.satz),
            max_woche=_ziehen(rng, quelle.max_woche), kosten=_ziehen(rng, quelle.kosten),
            rest=_ziehen(rng, quelle.max_gesamt) if quelle.max_gesamt else float("inf"),
            brutto={2026: 0.0, 2027: 0.0}, stunden=0.0)
    sv_satz = _ziehen(rng, a.sv_ferienjob)

    def netto_je_stunde(e: dict) -> float:
        s = e["quelle"]
        if s.art == "selbststaendig":
            return e["satz"] * (1 - e["kosten"])
        if s.art == "ferienjob":
            return e["satz"] * (1 - sv_satz)
        return e["satz"]

    erlaubt = {
        "optimal": None,
        "nur_ferienjob": {"Ferienjob Industrie/Logistik (Schicht)", "Aushilfe Mindestlohn (Lager, Gastro, Handel)"},
        "nur_webgeschaeft": {"Webgeschäft (standortcheck)"},
        "ohne_webgeschaeft": None,
    }[strategie]
    for ph in a.phasen:
        budget = _ziehen(rng, ph.stunden)
        kandidaten = [e for e in q.values() if e["verfuegbar"]
                      and (erlaubt is None or e["quelle"].name in erlaubt)
                      and not (strategie == "ohne_webgeschaeft" and e["quelle"].name.startswith("Web"))
                      and (ph.vollzeit or not e["quelle"].nur_vollzeit)]
        kandidaten.sort(key=netto_je_stunde, reverse=True)
        minijob_stunden_woche = a.minijob_grenze_monat * 12 / 52
        for e in kandidaten:
            if budget <= 0:
                break
            cap = e["max_woche"]
            if e["quelle"].art == "minijob":
                cap = min(cap, minijob_stunden_woche / e["satz"])
            h_woche = min(budget, cap)
            h = min(h_woche * ph.wochen, e["rest"])
            if h <= 0:
                continue
            e["rest"] -= h
            e["stunden"] += h
            e["brutto"][ph.jahr] += h * e["satz"]
            budget -= h / ph.wochen

    # Abgaben
    ergebnis = {"brutto": 0.0, "netto": 0.0, "stunden": 0.0, "je_quelle": {}}
    for jahr in (2026, 2027):
        lohn = sum(e["brutto"][jahr] for e in q.values() if e["quelle"].art == "ferienjob")
        mini = sum(e["brutto"][jahr] for e in q.values() if e["quelle"].art == "minijob")
        selbst = sum(e["brutto"][jahr] * (1 - e["kosten"]) for e in q.values()
                     if e["quelle"].art == "selbststaendig")
        sv = lohn * sv_satz
        zve = max(0.0, lohn - sv - min(a.werbungskosten, lohn)) + selbst   # Minijob pauschal versteuert
        steuer = sim.steuer(zve, 1.0)
        netto = lohn - sv + mini + selbst - steuer
        ergebnis["brutto"] += lohn + mini + sum(e["brutto"][jahr] for e in q.values()
                                                if e["quelle"].art == "selbststaendig")
        ergebnis["netto"] += netto
    for name, e in q.items():
        ergebnis["je_quelle"][name] = e["brutto"][2026] + e["brutto"][2027]
        ergebnis["stunden"] += e["stunden"]
    return ergebnis


def auswerten(n: int = 20_000, seed: int = 2027, strategie: str = "optimal",
              a: Annahmen | None = None) -> dict:
    a = a or Annahmen()
    rng = random.Random(seed)
    netto, brutto, stunden = [], [], []
    for _ in range(n):
        e = ein_leben(rng, a, strategie)
        netto.append(e["netto"]); brutto.append(e["brutto"]); stunden.append(e["stunden"])
    netto.sort()

    def qu(p):
        return netto[min(n - 1, int(n * p))]

    return {"p10": qu(0.10), "p25": qu(0.25), "median": qu(0.5), "p75": qu(0.75), "p90": qu(0.90),
            "p99": qu(0.99), "mittel": sum(netto) / n, "stunden_median": sorted(stunden)[n // 2],
            "brutto_median": sorted(brutto)[n // 2]}


def obergrenze(a: Annahmen | None = None) -> dict:
    """Theoretisches Maximum: jede Phase mit dem höchsten Stundenbudget, jede Quelle mit dem
    höchsten Satz und voller Nachfrage, alles verfügbar."""
    a = a or Annahmen()
    hoch = Annahmen(**{**a.__dict__,
                       "phasen": tuple(replace(p, stunden=(p.stunden[2],) * 3) for p in a.phasen),
                       "quellen": tuple(replace(s, satz=(s.satz[2],) * 3, max_woche=(s.max_woche[2],) * 3,
                                                p_verfuegbar=(1, 1, 1), kosten=(s.kosten[0],) * 3,
                                                max_gesamt=(s.max_gesamt[2],) * 3 if s.max_gesamt else None)
                                        for s in a.quellen),
                       "sv_ferienjob": (a.sv_ferienjob[0],) * 3})
    return ein_leben(random.Random(1), hoch)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--n", type=int, default=20_000)
    args = ap.parse_args()
    print("Netto erwirtschaftet bis 31.08.2027 (nach Steuer und Abgaben), "
          f"{args.n} simulierte Verläufe")
    print("-" * 96)
    for strategie, titel in (("optimal", "Beste Mischung (je Phase die besten Quellen)"),
                             ("ohne_webgeschaeft", "ohne Webgeschäft"),
                             ("nur_ferienjob", "nur Ferien-/Vollzeitjobs"),
                             ("nur_webgeschaeft", "nur Webgeschäft")):
        r = auswerten(args.n, strategie=strategie)
        print(f"  {titel:46s} sicher (90 %) {r['p10']:7,.0f}  Median {r['median']:7,.0f}"
              f"  gut (10 %) {r['p90']:7,.0f}  Spitze (1 %) {r['p99']:7,.0f} EUR".replace(",", "."))
    o = obergrenze()
    print(f"\n  Theoretische Obergrenze (alles am oberen Rand): {o['netto']:,.0f} EUR netto, "
          f"{o['stunden']:,.0f} Stunden".replace(",", "."))


if __name__ == "__main__":
    main()
