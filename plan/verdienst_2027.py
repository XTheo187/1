"""Wie viel kann ich bis 31.08.2027 maximal erwirtschaften – neben dem Abitur?

Monte-Carlo über das Zeitbudget vom 23.11.2026 bis 31.08.2027 (Bayern,
Gymnasium, Abitur 2027, Raum Regensburg). Jede Phase hat ein Stundenbudget,
das das Abitur schützt. Die Stunden gehen an die Verdienstquellen mit dem
höchsten erwarteten Nettoerlös je Stunde, begrenzt durch

- die Nachfrage (Nachhilfeschüler, Kunden, Einsatzangebote),
- die Familienversicherung: regelmäßiges Einkommen (Minijob, Nachhilfe,
  Webgeschäft) höchstens 565 EUR (2026) bzw. 590 EUR (2027) im Monat, bei
  nur einem Minijob 603 bzw. 633 EUR,
- die kurzfristige Beschäftigung: höchstens 70 Arbeitstage je Kalenderjahr,
  zählt nicht zur Einkommensgrenze; sozialversicherungsfrei nur, wenn danach
  ein Studium folgt (vor einem dualen Studium oder einer Ausbildung
  ~21,15 % Arbeitnehmeranteil),
- das Arbeitszeitgesetz (höchstens 48 Stunden je Woche, 10 Stunden je Tag).

Am Ende wird die Einkommensteuer für 2026 und 2027 abgezogen (Tarif 2026,
also eher zu hoch, weil der Grundfreibetrag 2027 steigt).

Aufruf:

    python3 plan/verdienst_2027.py            # Ergebnis und Strategien
    python3 plan/verdienst_2027.py --n 40000  # genauer

Eingaben mit Quellen: docs/VERDIENST_BIS_SOMMER_2027.md.
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


def _z(rng: random.Random, t: tuple) -> float:
    return dreieck(rng, *t) if t[0] != t[2] else float(t[0])


def _mitte(t: tuple) -> float:
    return sum(t) / 3


# --------------------------------------------------------------------------
# Kalender (KM Bayern, BayMBl. 2025 Nr. 354; Ferien laut km.bayern.de)
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Phase:
    name: str
    wochen: float
    stunden: tuple            # Stunden je Woche, die neben Schule/Lernen frei sind (min, Mitte, max)
    jahr: int
    monate: float             # Kalendermonate (für die Einkommensgrenze)
    ferien_tage: float = 0.0  # ganze freie Arbeitstage (Mo–Fr) für einen Ferienjob
    einsatz_tage: tuple = (0, 0, 0)   # einzelne Wochenend-/Abendeinsätze (kurzfristig) in der Phase


PHASEN = (
    # 23.11.–23.12.2026: Unterricht, Q13/1
    Phase("Schulzeit 23.11.–23.12.2026", 4.5, (3, 6, 10), 2026, 1.1, einsatz_tage=(0, 1, 3)),
    # Weihnachtsferien 24.12.2026–08.01.2027: 9 Arbeitstage, davon ~4 in 2026
    Phase("Weihnachtsferien (2026)", 1.0, (0, 0, 0), 2026, 0.0, ferien_tage=4),
    Phase("Weihnachtsferien (2027)", 1.0, (0, 0, 0), 2027, 0.3, ferien_tage=5),
    # 11.01.–05.02. und 15.02.–19.03.2027: Unterricht
    Phase("Schulzeit Januar – März 2027", 9.0, (3, 6, 10), 2027, 2.2, einsatz_tage=(1, 3, 6)),
    # Frühjahrsferien 08.–12.02.2027: 5 Arbeitstage
    Phase("Frühjahrsferien", 1.0, (0, 0, 0), 2027, 0.2, ferien_tage=5),
    # 22.03.–25.06.2027: Osterferien als Lernzeit, schriftliches Abitur 21.04.–13.05.,
    # Pfingstferien, Kolloquium 31.05.–11.06., Zusatzprüfungen bis 18.06., Zeugnis 25.06.
    Phase("Lern- und Prüfungszeit 22.03.–25.06.2027", 13.5, (0, 2, 6), 2027, 3.1),
)
# Nach dem Zeugnis: 28.06.–31.08.2027 = 47 Arbeitstage (Mo–Fr), wenn die Ausbildung
# am 01.09. oder 01.10. beginnt; bei Beginn am 01.08. nur 25 (28.06.–30.07.).
SOMMER_TAGE = {"01.08.": 25, "01.09.": 47, "01.10.": 47}


# --------------------------------------------------------------------------
# Verdienstquellen
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Regelmaessig:
    """Zählt zur Einkommensgrenze der Familienversicherung."""
    name: str
    satz: tuple                 # Brutto (bzw. Umsatz) je Stunde
    max_woche: tuple            # Nachfrage: Stunden je Woche
    p_verfuegbar: tuple = (1, 1, 1)
    kosten: tuple = (0, 0, 0)   # Anteil Kosten am Umsatz (nur selbstständig)
    minijob: bool = False


REGELMAESSIG = (
    # Superprof 12/2024: Oberstufe privat 20–40 EUR/h; Schüler/Studierende eher 15–30.
    Regelmaessig("Nachhilfe (privat)", (15, 22, 30), (1, 3, 6), p_verfuegbar=(0.6, 0.8, 0.95)),
    # Eigenes Modell (sim.sommer_meilensteine): Umsatz je Arbeitsstunde P10 9, Median 26, P90 40 EUR.
    Regelmaessig("Webgeschäft (standortcheck)", (9, 26, 40), (2, 6, 12), kosten=(0.05, 0.10, 0.20)),
    # Minijob Handel/Gastro: Mindestlohn 13,90 (2026) / 14,60 EUR (2027) bis ~16 EUR.
    Regelmaessig("Minijob (Handel, Gastro)", (14.6, 15.0, 16.5), (3, 6, 10), minijob=True),
)

# Kurzfristige Beschäftigung (Ferien, Einsätze, Sommer), Brutto je Stunde.
# Lager/Kommissionierung Regensburg (InStaff 2026) Ø 18,02; Produktion BMW Regensburg
# über Randstad 18–20 (2024); Amazon 16,22–16,66; Zeitarbeit-Untergrenze 15,87 ab 04/2027;
# Mindestlohn 14,60 (2027).
SATZ_INDUSTRIE = (17.0, 18.5, 20.5)     # mit Schichtzulagen
P_INDUSTRIE = (0.5, 0.7, 0.9)           # Chance, einen Industrie-/Lagerjob zu bekommen
SATZ_SONST = (14.6, 15.9, 17.0)         # Zeitarbeit, Logistik, Aushilfe
SATZ_EINSATZ = (15.5, 18.0, 20.0)       # Event/Service/Lager-Einsätze (InStaff Regensburg)
STUNDEN_TAG = (7.5, 8.0, 10.0)          # je Arbeitstag (ArbZG: bis 10 h, Ø 8 h)
SAMSTAGE = (0.0, 0.5, 1.0)              # Anteil der Samstage, die im Sommer zusätzlich gearbeitet werden


@dataclass
class Annahmen:
    grenze_regel: dict = field(default_factory=lambda: {2026: 565.0, 2027: 590.0})
    grenze_minijob: dict = field(default_factory=lambda: {2026: 603.0, 2027: 633.0})
    sv_berufsmaessig: float = 0.2115        # AN-Anteil 2026 (KV 7,3+1,45, RV 9,3, AV 1,3, PV 1,8)
    p_dual: float = 0.55                    # danach duales Studium/PiBS/Ausbildung (sonst FH)
    start_dual: tuple = (("01.08.", 0.35), ("01.09.", 0.45), ("01.10.", 0.20))
    azubi_brutto: tuple = (1_000, 1_150, 1_300)  # August-Vergütung, falls Start 01.08.
    tage_kurzfristig: int = 70
    regelmaessig: tuple = field(default_factory=lambda: REGELMAESSIG)
    phasen: tuple = field(default_factory=lambda: PHASEN)
    satz_industrie: tuple = SATZ_INDUSTRIE
    p_industrie: tuple = P_INDUSTRIE
    satz_sonst: tuple = SATZ_SONST
    satz_einsatz: tuple = SATZ_EINSATZ
    stunden_tag: tuple = STUNDEN_TAG
    samstage: tuple = SAMSTAGE
    p_ferienjob: float = 0.85               # Ferienjob für wenige Tage gefunden
    max_stunden_woche: float = 48.0         # ArbZG: Ø 48 h; bis 60 h nur mit Ausgleich (6 Monate/24 Wochen)
    mit_webgeschaeft: bool = True
    mit_kurzfristig: bool = True
    mit_regelmaessig: bool = True


def ein_verlauf(rng: random.Random, a: Annahmen) -> dict:
    dual = rng.random() < a.p_dual
    start = "01.10."
    if dual:
        u, acc = rng.random(), 0.0
        for s, p in a.start_dual:
            acc += p
            if u < acc:
                start = s
                break
    sv_kurz = a.sv_berufsmaessig if dual else 0.0
    industrie = rng.random() < _z(rng, a.p_industrie)
    satz_ferien = _z(rng, a.satz_industrie if industrie else a.satz_sonst)
    satz_einsatz = _z(rng, a.satz_einsatz)
    h_tag = _z(rng, a.stunden_tag)

    quellen = []
    for r in a.regelmaessig:
        if not a.mit_webgeschaeft and r.name.startswith("Web"):
            continue
        quellen.append(dict(r=r, da=rng.random() < _z(rng, r.p_verfuegbar), satz=_z(rng, r.satz),
                            max_woche=_z(rng, r.max_woche), kosten=_z(rng, r.kosten),
                            netto_erwartet=_mitte(r.satz) * (1 - _mitte(r.kosten))))
    # Wer die Grenze ausschöpfen will, nimmt zuerst die Quellen mit dem höchsten erwarteten
    # Erlös je Stunde (spart Lernzeit); Minijob nur, wenn er allein bleibt (sonst 590-Grenze).
    quellen.sort(key=lambda q: q["netto_erwartet"], reverse=True)

    brutto = {2026: {"lohn": 0.0, "mini": 0.0, "selbst": 0.0}, 2027: {"lohn": 0.0, "mini": 0.0, "selbst": 0.0}}
    tage_genutzt = {2026: 0.0, 2027: 0.0}
    je_quelle: dict[str, float] = {}
    stunden_gesamt = 0.0

    def buche(name, jahr, art, betrag, stunden):
        nonlocal stunden_gesamt
        brutto[jahr][art] += betrag
        je_quelle[name] = je_quelle.get(name, 0.0) + betrag
        stunden_gesamt += stunden

    for ph in a.phasen:
        # 1. Ferientage: kurzfristiger Vollzeitjob
        if a.mit_kurzfristig and ph.ferien_tage:
            tage = min(ph.ferien_tage, a.tage_kurzfristig - tage_genutzt[ph.jahr])
            if tage > 0 and rng.random() < a.p_ferienjob:
                tage_genutzt[ph.jahr] += tage
                buche("Ferienjob (kurzfristig)", ph.jahr, "lohn", tage * h_tag * satz_ferien, tage * h_tag)
        # 2. Stundenbudget neben der Schule
        budget = _z(rng, ph.stunden) * ph.wochen
        if a.mit_regelmaessig and budget > 0 and ph.monate > 0:
            nur_minijob = all(not q["da"] or q["r"].minijob for q in quellen)
            grenze = (a.grenze_minijob if nur_minijob else a.grenze_regel)[ph.jahr] * ph.monate
            for q in quellen:
                if not q["da"] or budget <= 0 or grenze <= 0:
                    continue
                if q["r"].minijob and not nur_minijob and any(
                        x["da"] and not x["r"].minijob for x in quellen):
                    # Minijob neben selbstständigen Einkünften: zählt zur 590-Grenze mit
                    pass
                h = min(budget, q["max_woche"] * ph.wochen)
                umsatz = min(h * q["satz"], grenze / (1 - q["kosten"]))
                h = umsatz / q["satz"]
                gewinn = umsatz * (1 - q["kosten"])
                grenze -= gewinn
                budget -= h
                art = "mini" if q["r"].minijob else "selbst"
                buche(q["r"].name, ph.jahr, art, gewinn, h)
        # 3. Einzelne kurzfristige Einsätze am Wochenende (zählen zu den 70 Tagen)
        if a.mit_kurzfristig and budget > 0:
            tage = min(_z(rng, ph.einsatz_tage), budget / h_tag,
                       a.tage_kurzfristig - tage_genutzt[ph.jahr] - SOMMER_TAGE[start] * (ph.jahr == 2027))
            if tage > 0:
                tage_genutzt[ph.jahr] += tage
                buche("Einsätze am Wochenende (kurzfristig)", ph.jahr, "lohn", tage * h_tag * satz_einsatz,
                      tage * h_tag)

    # 4. Sommer nach dem Zeugnis: kurzfristiger Vollzeitjob, ggf. dazu Samstage
    if a.mit_kurzfristig:
        werktage = SOMMER_TAGE[start]
        tage = werktage + werktage / 5 * _z(rng, a.samstage)
        tage = min(tage, a.tage_kurzfristig - tage_genutzt[2027])
        stunden = tage * min(h_tag, 10.0)
        stunden = min(stunden, a.max_stunden_woche * werktage / 5)
        tage_genutzt[2027] += tage
        buche("Sommerjob nach dem Abitur (kurzfristig)", 2027, "lohn", stunden * satz_ferien, stunden)
    if start == "01.08.":
        buche("Ausbildungsvergütung August", 2027, "lohn", _z(rng, a.azubi_brutto), 0.0)

    # Abgaben
    netto = 0.0
    brutto_summe = 0.0
    for jahr in (2026, 2027):
        b = brutto[jahr]
        sv = b["lohn"] * (sv_kurz if jahr == 2027 else 0.0)
        zve = max(0.0, b["lohn"] - sv - min(1_230.0, b["lohn"]) - 36.0) + b["selbst"]
        steuer = sim.steuer(zve, 1.0)
        netto += b["lohn"] - sv + b["mini"] + b["selbst"] - steuer
        brutto_summe += b["lohn"] + b["mini"] + b["selbst"]
    regel = {j: brutto[j]["mini"] + brutto[j]["selbst"] for j in (2026, 2027)}
    return {"netto": netto, "brutto": brutto_summe, "stunden": stunden_gesamt, "je_quelle": je_quelle,
            "dual": dual, "start": start, "industrie": industrie, "tage_kurzfristig": dict(tage_genutzt),
            "regelmaessig": regel}


def auswerten(n: int = 20_000, seed: int = 2027, a: Annahmen | None = None) -> dict:
    a = a or Annahmen()
    rng = random.Random(seed)
    verlaeufe = [ein_verlauf(rng, a) for _ in range(n)]
    netto = sorted(v["netto"] for v in verlaeufe)

    def qu(p):
        return netto[min(n - 1, int(n * p))]

    quellen: dict[str, list[float]] = {}
    for v in verlaeufe:
        for k, x in v["je_quelle"].items():
            quellen.setdefault(k, []).append(x)
    return {"p10": qu(0.10), "p25": qu(0.25), "median": qu(0.50), "p75": qu(0.75), "p90": qu(0.90),
            "p99": qu(0.99), "mittel": sum(netto) / n,
            "stunden_median": sorted(v["stunden"] for v in verlaeufe)[n // 2],
            "quellen_mittel": {k: sum(x) / n for k, x in quellen.items()}}


def obergrenze(a: Annahmen | None = None) -> dict:
    """Bestmöglicher Verlauf: alles am oberen Rand, Studium danach (keine SV), Beginn 01.10."""
    a = a or Annahmen()
    hoch = replace(
        a, p_dual=0.0, p_industrie=(1, 1, 1), p_ferienjob=1.0,
        satz_industrie=(a.satz_industrie[2],) * 3, satz_einsatz=(a.satz_einsatz[2],) * 3,
        stunden_tag=(10.0,) * 3, samstage=(1.0,) * 3,
        regelmaessig=tuple(replace(r, satz=(r.satz[2],) * 3, max_woche=(r.max_woche[2],) * 3,
                                   p_verfuegbar=(1, 1, 1), kosten=(r.kosten[0],) * 3) for r in a.regelmaessig),
        phasen=tuple(replace(p, stunden=(p.stunden[2],) * 3, einsatz_tage=(p.einsatz_tage[2],) * 3)
                     for p in a.phasen))
    return ein_verlauf(random.Random(1), hoch)


STRATEGIEN = {
    "beste Mischung": {},
    "ohne Webgeschäft": {"mit_webgeschaeft": False},
    "nur kurzfristige Jobs (Ferien, Einsätze, Sommer)": {"mit_regelmaessig": False},
    "nur Nebenjobs neben der Schule (ohne Sommerjob)": {"mit_kurzfristig": False},
}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--n", type=int, default=20_000)
    args = ap.parse_args()
    print(f"Netto erwirtschaftet 23.11.2026–31.08.2027 (nach Steuer und Abgaben), {args.n} Verläufe")
    print("-" * 104)
    for titel, aend in STRATEGIEN.items():
        r = auswerten(args.n, a=replace(Annahmen(), **aend))
        print(f"  {titel:50s} sicher (90 %) {r['p10']:7,.0f}  Median {r['median']:7,.0f}"
              f"  gut (10 %) {r['p90']:7,.0f}  Spitze (1 %) {r['p99']:7,.0f}".replace(",", "."))
    r = auswerten(args.n)
    print("\n  Beste Mischung, mittlerer Beitrag je Quelle (brutto bzw. Gewinn):")
    for k, x in sorted(r["quellen_mittel"].items(), key=lambda kv: -kv[1]):
        print(f"    {k:48s} {x:7,.0f} EUR".replace(",", "."))
    o = obergrenze()
    print(f"\n  Obergrenze (alles am oberen Rand, Studium danach): {o['netto']:,.0f} EUR netto in "
          f"{o['stunden']:,.0f} Stunden".replace(",", "."))
    o60 = obergrenze(replace(Annahmen(), max_stunden_woche=60.0))
    print(f"  ... mit 60-Stunden-Wochen im Sommer (ArbZG nur mit Ausgleich): {o60['netto']:,.0f} EUR netto in "
          f"{o60['stunden']:,.0f} Stunden".replace(",", "."))


if __name__ == "__main__":
    main()
