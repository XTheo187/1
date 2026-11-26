"""Wie viel kann ich bis 31.08.2027 maximal erwirtschaften – neben dem Abitur?

Monte-Carlo über das Zeitbudget vom 23.11.2026 bis 31.08.2027 (Bayern,
Gymnasium, Abitur 2027, Raum Regensburg). Jede Phase hat ein Stundenbudget,
das das Abitur schützt. Die Stunden gehen an die Verdienstquellen mit dem
höchsten erwarteten Nettoerlös je Stunde, begrenzt durch

- die Nachfrage (Nachhilfeschüler, Kunden, Einsatzangebote),
- die Familienversicherung (§ 10 SGB V): Gesamteinkommen höchstens 565 EUR
  (2026) bzw. 590 EUR (2027) im Monat, Gewinne aus selbstständiger Arbeit
  als Jahresgewinn / 12; wer daneben einen Minijob hat, darf insgesamt
  (Minijob + Gewinn / 12) bis 603 bzw. 633 EUR,
- die Rentenversicherungspflicht selbstständiger Nachhilfelehrer (§ 2 Satz 1
  Nr. 1 SGB VI): frei nur bis 603 bzw. 633 EUR Gewinn im Monat,
- die Übungsleiterpauschale (§ 3 Nr. 26 EStG): bis 3.300 EUR im Jahr frei,
  zählt nicht zum Gesamteinkommen,
- die kurzfristige Beschäftigung: höchstens 3 Monate (bei mehreren Jobs
  90 Kalendertage) oder 70 Arbeitstage je Kalenderjahr, zählt nicht zur
  Einkommensgrenze; Jobs bis zum Abiturzeugnis sind Schülerjobs und
  sozialversicherungsfrei; der Sommerjob danach nur, wenn ein Studium folgt
  (vor einem dualen Studium oder einer Ausbildung ist er berufsmäßig:
  ~21,15 % Arbeitnehmeranteil, dafür keine Tagesgrenze),
- das Arbeitszeitgesetz (höchstens 48 Stunden je Woche, 10 Stunden je Tag).

Am Ende wird die Einkommensteuer für 2026 und 2027 abgezogen (Tarif 2026;
für 2027 mit Grundfreibetrag 12.564 EUR und Arbeitnehmer-Pauschbetrag
1.430 EUR aus dem Entwurf). Zusätzlich
wird die Lohnsteuer geschätzt, die der Arbeitgeber 2027 einbehält und die erst
mit der Steuererklärung 2027 (also 2028) zurückkommt: Sie fehlt am 31.08.2027
auf dem Konto.

Aufruf:

    python3 plan/verdienst_2027.py            # Ergebnis, Strategien, Szenarien
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


def _oben(t: tuple) -> tuple:
    return (t[2],) * 3


# --------------------------------------------------------------------------
# Steuer
# --------------------------------------------------------------------------

AN_PAUSCHBETRAG = {2026: 1_230.0, 2027: 1_430.0}      # Entwurf 2027: 1.430 EUR (hib)
SA_PAUSCHBETRAG = 36.0                                  # Sonderausgaben-Pauschbetrag
GRUNDFREIBETRAG_PLUS = {2026: 0.0, 2027: 12_564.0 - 12_348.0}   # Entwurf 2027 (hib)


def einkommensteuer(zve: float, jahr: int) -> float:
    """Tarif 2026 (§ 32a EStG); 2027 um den höheren Grundfreibetrag verschoben."""
    return sim.steuer(max(0.0, zve - GRUNDFREIBETRAG_PLUS[jahr]), 1.0)


def lohnsteuer(lohn: float, kalendertage: float, jahr: int, vorsorge: float = 0.0) -> float:
    """Einbehaltene Lohnsteuer (Klasse I) für einen Lohnzahlungszeitraum.

    Ganzer Monat = 30 Tage (Monatstabelle); kürzere Jobs werden nach der
    Tagestabelle auf 360 Tage hochgerechnet – deshalb behalten kurze Ferienjobs
    viel ein. Ohne Vorsorgepauschale bei sozialversicherungsfreien Jobs, also
    eher zu hoch; ohne Kirchensteuer.
    """
    if lohn <= 0 or kalendertage <= 0:
        return 0.0
    faktor = 360.0 / kalendertage
    jahreslohn = lohn * (1 - vorsorge) * faktor - AN_PAUSCHBETRAG[jahr] - SA_PAUSCHBETRAG
    return einkommensteuer(jahreslohn, jahr) / faktor


# --------------------------------------------------------------------------
# Kalender (KM Bayern, BayMBl. 2025 Nr. 354; Ferien laut km.bayern.de)
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Phase:
    name: str
    wochen: float
    stunden: tuple                  # Stunden je Woche, die neben Schule/Lernen frei sind (min, Mitte, max)
    jahr: int
    monate: float                   # Kalendermonate (Minijob-/Rentenversicherungsgrenze)
    ferien_tage: tuple = (0, 0, 0)  # ganze freie Arbeitstage (Mo–Fr) für einen befristeten Ferienjob
    kalender_je_tag: float = 1.0    # Kalendertage des Vertrags je Arbeitstag (90-Tage-Regel)
    einsatz_tage: tuple = (0, 0, 0)  # einzelne Wochenend-/Abendeinsätze (kurzfristig) in der Phase


PHASEN = (
    # 23.11.–23.12.2026: Unterricht, Q13/1
    Phase("Schulzeit 23.11.–23.12.2026", 4.5, (3, 6, 10), 2026, 1.1, einsatz_tage=(0, 1, 3)),
    # Weihnachtsferien 24.12.2026–08.01.2027: 2026 fünf Arbeitstage (24., 28.–31.12.),
    # Vertrag 24.–31.12. = 8 Kalendertage; 2027 vier (04., 05., 07., 08.01.; 06.01. Feiertag)
    Phase("Weihnachtsferien (2026)", 0.0, (0, 0, 0), 2026, 0.0, ferien_tage=(5, 5, 5), kalender_je_tag=8 / 5),
    Phase("Weihnachtsferien (2027)", 0.0, (0, 0, 0), 2027, 0.3, ferien_tage=(4, 4, 4), kalender_je_tag=5 / 4),
    # 11.01.–05.02. und 15.02.–19.03.2027: Unterricht
    Phase("Schulzeit Januar – März 2027", 9.0, (3, 6, 10), 2027, 2.2, einsatz_tage=(1, 3, 6)),
    # Frühjahrsferien 08.–12.02.2027: 5 Arbeitstage
    Phase("Frühjahrsferien", 0.0, (0, 0, 0), 2027, 0.2, ferien_tage=(5, 5, 5)),
    # 22.03.–13.06.2027: Osterferien als Lernzeit, schriftliches Abitur 21.04.–13.05.,
    # Pfingstferien 18.–28.05., Kolloquium 31.05.–11.06.
    Phase("Lern- und Prüfungszeit 22.03.–13.06.2027", 12.0, (0, 2, 6), 2027, 2.75),
    # Pfingstferien: 8 Arbeitstage (17.05. Pfingstmontag, 27.05. Fronleichnam), Kolloquium
    # danach – höchstens einzelne Tage
    Phase("Einzelne Tage in den Pfingstferien", 0.0, (0, 0, 0), 2027, 0.0, ferien_tage=(0, 1, 4)),
    # Nach dem letzten Prüfungstermin bis zum Zeugnis (Fr 25.06.): 14.–24.06. = 9 Arbeitstage,
    # Vertrag bis 24.06. = 11 Kalendertage; Zusatzprüfungen bis 18.06. kosten Tage
    Phase("Nach den Prüfungen 14.–24.06.2027", 1.6, (0, 0, 0), 2027, 0.35, ferien_tage=(0, 5, 9),
          kalender_je_tag=11 / 9),
)
# Nach dem Zeugnis: 28.06.–31.08.2027 = 47 Arbeitstage (Mo–Fr; 15.08. ist ein Sonntag), wenn
# die Ausbildung am 01.09. oder 01.10. beginnt; bei Beginn am 01.08. nur 25 (28.06.–30.07.).
# Für die 90-Kalendertage-Regel zählen volle Kalendermonate mit 30 Tagen, Teilmonate mit den
# tatsächlichen Tagen (Geringfügigkeits-Richtlinien 2026): 3 + 30 + 30 = 63.
SOMMER_TAGE = {"01.08.": 25, "01.09.": 47, "01.10.": 47}
SOMMER_KALENDERTAGE = 63
# Lohnzahlungszeiträume des Sommerjobs: (Arbeitstage, Kalendertage) für Juni, Juli, August
SOMMER_MONATE = ((3, 3), (22, 30), (22, 30))


# --------------------------------------------------------------------------
# Verdienstquellen
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Regelmaessig:
    """Verdienst neben der Schule, Woche für Woche."""
    name: str
    satz: tuple                 # Brutto (bzw. Umsatz) je Stunde
    max_woche: tuple            # Nachfrage: Stunden je Woche
    p_verfuegbar: tuple = (1, 1, 1)
    kosten: tuple = (0, 0, 0)   # Anteil Kosten am Umsatz (nur selbstständig)
    art: str = "selbst"         # selbst | mini | frei (Übungsleiterpauschale)
    rv_grenze: bool = False     # selbstständige Lehrtätigkeit: rentenversicherungspflichtig über 603/633 EUR
    sortier_satz: float | None = None   # Erwartungswert für die Reihenfolge, wenn satz je Lauf fest gesetzt ist


REGELMAESSIG = (
    # Superprof 12/2024: Oberstufe privat 20–40 EUR/h; Schüler/Studierende eher 15–30.
    Regelmaessig("Nachhilfe (privat)", (15, 22, 30), (1, 3, 6), p_verfuegbar=(0.6, 0.8, 0.95), rv_grenze=True),
    # Umsatz je Arbeitsstunde inkl. Akquise, mit den Quoten der Recherche für Neulinge (Einstieg
    # 0,5-5 % je Kontakt, Upsell 5-30 %, Paket 800-2.200 EUR; plan/hebel_2027.py WebParameter):
    # sehr ungleich verteilt, im Mittel ~16 EUR/h (früher aus sim.sommer_meilensteine: 9/26/40).
    Regelmaessig("Webgeschäft (standortcheck)", (0, 6, 42), (2, 6, 12), kosten=(0.05, 0.10, 0.20)),
    # Minijob Handel/Gastro: Mindestlohn 13,90 (2026) / 14,60 EUR (2027) bis ~16 EUR.
    Regelmaessig("Minijob (Handel, Gastro)", (14.6, 15.0, 16.5), (3, 6, 10), art="mini"),
    # Trainer im Sportverein, Betreuung bei gemeinnützigem Träger, Ferienprogramm, VHS:
    # meist 10–18 EUR/h, feste Termine (abends/Wochenende), nicht überall zu bekommen.
    Regelmaessig("Übungsleiter/Betreuer (Verein, gemeinnützig)", (10, 14, 18), (1.5, 3, 4.5),
                 p_verfuegbar=(0.3, 0.5, 0.7), art="frei"),
)

# Kurzfristige Beschäftigung (Ferien, Einsätze, Sommer), Brutto je Stunde.
# Lager/Kommissionierung Regensburg (InStaff 2026) Ø 18,02; Produktion BMW Regensburg
# über Randstad 18–20 (2024); Amazon 16,22–16,66; Zeitarbeit-Untergrenze 15,87 ab 04/2027;
# Mindestlohn 14,60 (2027).
SATZ_INDUSTRIE = (17.0, 18.5, 20.5)     # mit Nacht-/Sonntagszuschlägen
P_INDUSTRIE = (0.5, 0.7, 0.9)           # Chance, einen Industrie-/Lagerjob zu bekommen
SATZ_SONST = (14.6, 15.9, 17.0)         # Zeitarbeit, Logistik, Aushilfe
SATZ_EINSATZ = (15.5, 18.0, 20.0)       # Event/Service/Lager-Einsätze (InStaff Regensburg)
STUNDEN_TAG = (7.5, 8.0, 10.0)          # je Arbeitstag (ArbZG: bis 10 h, Ø 8 h)
SAMSTAGE = (0.0, 0.5, 1.0)              # Anteil der Samstage, die im Sommer zusätzlich gearbeitet werden


@dataclass(frozen=True)
class Zusatz:
    """Ein eigenes Geschäft neben (oder statt) Teilen des Job-Wegs – für plan/hebel_2027.py.

    Es nimmt dem Job-Weg Zeit weg und bringt eigenen Gewinn. Die Zufallszahlen
    des Job-Wegs bleiben mit und ohne Zusatz dieselben, damit sich beide Läufe
    eins zu eins vergleichen lassen.
    """
    stunden: tuple = ()             # (Phasen-Präfix, Stunden), die vom Stundenbudget der Phase abgehen
    ferientage: tuple = ()          # (Phasen-Präfix, Tage), die dem Ferienjob der Phase fehlen
    sommer_anteil: float = 1.0      # Anteil der Sommer-Arbeitstage (Mo–Fr), die der Sommerjob behält
    sommer_teilzeit: bool = True    # True: weniger Tage je Woche; False: Job beginnt später (endet 31.08.)
    sommer_samstage: float = 1.0    # Anteil der Sommer-Samstage, die das Geschäft für den Job frei lässt
    gewinn: tuple = ()              # (Jahr, Gewinn aus selbstständiger Arbeit vor Steuer, auch negativ)
    sommer_brutto: float | None = None  # anderer Sommerjob (z. B. mit Provision): Brutto für den ganzen Sommer
    sommer_satz: float | None = None    # anderer Stundenlohn des Sommerjobs (z. B. Teilzeit-Ferienjob)
    sonderausgaben: tuple = ()          # (Jahr, Betrag): z. B. Beiträge einer eigenen Kranken-/Pflegeversicherung


def _summe(paare: tuple, schluessel) -> float:
    return sum(x for k, x in paare if (isinstance(k, str) and isinstance(schluessel, str)
                                       and schluessel.startswith(k)) or k == schluessel)


@dataclass
class Annahmen:
    grenze_regel: dict = field(default_factory=lambda: {2026: 565.0, 2027: 590.0})
    grenze_minijob: dict = field(default_factory=lambda: {2026: 603.0, 2027: 633.0})
    uebungsleiter_frei: float = 3_300.0     # § 3 Nr. 26 EStG je Kalenderjahr
    sv_berufsmaessig: float = 0.2115        # AN-Anteil 2026 (KV 7,3+1,45, RV 9,3, AV 1,3, PV 1,8)
    vorsorge_lohnsteuer: float = 0.1985     # Vorsorgepauschale bei SV-Pflicht (ohne AV), grob
    p_dual: float = 0.55                    # danach duales Studium/PiBS/Ausbildung (sonst FH)
    start_dual: tuple = (("01.08.", 0.35), ("01.09.", 0.45), ("01.10.", 0.20))
    azubi_brutto: tuple = (1_000, 1_150, 1_300)  # August-Vergütung, falls Start 01.08.
    tage_kurzfristig: int = 70              # Arbeitstage je Kalenderjahr ...
    kalendertage_kurzfristig: int = 90      # ... oder 90 Kalendertage (3 Monate) – je nachdem, was hilft
    regelmaessig: tuple = field(default_factory=lambda: REGELMAESSIG)
    phasen: tuple = field(default_factory=lambda: PHASEN)
    satz_industrie: tuple = SATZ_INDUSTRIE
    p_industrie: tuple = P_INDUSTRIE
    satz_sonst: tuple = SATZ_SONST
    satz_einsatz: tuple = SATZ_EINSATZ
    stunden_tag: tuple = STUNDEN_TAG
    samstage: tuple = SAMSTAGE
    p_ferienjob: float = 0.85               # Ferienjob für die freien Tage einer Phase gefunden
    max_stunden_woche: float = 48.0         # ArbZG: Ø 48 h; bis 60 h nur mit Ausgleich (6 Monate/24 Wochen)
    mit_webgeschaeft: bool = True
    mit_kurzfristig: bool = True
    mit_regelmaessig: bool = True


def ein_verlauf(rng: random.Random, a: Annahmen, zusatz: Zusatz | None = None) -> dict:
    paarweise = zusatz is not None      # Vergleichslauf für plan/hebel_2027.py
    z = zusatz or Zusatz()
    dual = rng.random() < a.p_dual
    start = "01.10."
    if dual:
        u, acc = rng.random(), 0.0
        for s, p in a.start_dual:
            acc += p
            if u < acc:
                start = s
                break
    # Vor einem dualen Studium / einer Ausbildung ist der Sommerjob berufsmäßig: keine
    # kurzfristige Beschäftigung, sondern sozialversicherungspflichtig (ohne Tagesgrenze).
    sommer_kurz = not dual
    industrie = rng.random() < _z(rng, a.p_industrie)
    satz_ferien = _z(rng, a.satz_industrie if industrie else a.satz_sonst)
    satz_einsatz = _z(rng, a.satz_einsatz)
    h_tag = _z(rng, a.stunden_tag)
    samstage = _z(rng, a.samstage)
    samstage = min(samstage, max(0.0, z.sommer_samstage))
    werktage_sommer = SOMMER_TAGE[start]
    # Arbeitstage inkl. Samstage: Teilzeit (weniger Tage je Woche) behält alle Samstage, die das Geschäft
    # frei lässt; ein späterer Beginn hat entsprechend weniger Wochen und damit weniger Samstage
    if z.sommer_teilzeit:
        sommer_voll = werktage_sommer * (z.sommer_anteil + samstage / 5) if z.sommer_anteil > 0 else 0.0
    else:
        sommer_voll = werktage_sommer * z.sommer_anteil * (1 + samstage / 5)
    # Kalendertage des Sommervertrags: Teilzeit über den ganzen Sommer oder späterer Beginn
    kal_sommer = SOMMER_KALENDERTAGE * (1.0 if z.sommer_teilzeit else z.sommer_anteil)

    quellen = []
    for r in a.regelmaessig:
        if not a.mit_webgeschaeft and r.name.startswith("Web"):
            continue
        quellen.append(dict(r=r, da=rng.random() < _z(rng, r.p_verfuegbar), satz=_z(rng, r.satz),
                            max_woche=_z(rng, r.max_woche), kosten=_z(rng, r.kosten),
                            netto_erwartet=(r.sortier_satz if r.sortier_satz is not None else _mitte(r.satz))
                            * (1 - _mitte(r.kosten))))
    # Zuerst die Quellen mit dem höchsten erwarteten Erlös je Stunde (spart Lernzeit).
    quellen.sort(key=lambda q: q["netto_erwartet"], reverse=True)

    jahre = (2026, 2027)
    lohn = {j: 0.0 for j in jahre}           # Arbeitslohn (Ferien, Einsätze, Sommer, Ausbildung)
    lohn_sv = {j: 0.0 for j in jahre}        # davon sozialversicherungspflichtig
    art_summe = {j: {"selbst": 0.0, "mini": 0.0, "frei": 0.0} for j in jahre}
    mini_monate = {j: 0.0 for j in jahre}
    nachhilfe = {j: 0.0 for j in jahre}
    nachhilfe_monate = {j: 0.0 for j in jahre}
    wt = {j: 0.0 for j in jahre}             # Arbeitstage kurzfristig
    kt = {j: 0.0 for j in jahre}             # Kalendertage kurzfristig
    abrechnungen = []                        # (jahr, lohn, kalendertage, vorsorge) für die Lohnsteuer
    je_quelle: dict[str, float] = {}
    ueberlauf: dict[str, float] = {}         # Stunden eines Zusatzgeschäfts über dem Phasenbudget
    stunden_je_quelle: dict[str, float] = {}
    je_phase: dict[str, dict[str, float]] = {}   # Phase -> Quelle -> Betrag (für Frühindikatoren)
    stunden_je_phase: dict[str, dict[str, float]] = {}   # Phase -> Quelle -> Stunden
    phase_jetzt = "Sommer"
    stunden_gesamt = 0.0

    def buche(name, betrag, stunden):
        nonlocal stunden_gesamt
        je_quelle[name] = je_quelle.get(name, 0.0) + betrag
        stunden_je_quelle[name] = stunden_je_quelle.get(name, 0.0) + stunden
        je_phase.setdefault(phase_jetzt, {})[name] = je_phase.get(phase_jetzt, {}).get(name, 0.0) + betrag
        sp = stunden_je_phase.setdefault(phase_jetzt, {})
        sp[name] = sp.get(name, 0.0) + stunden
        stunden_gesamt += stunden

    def frei_tage(jahr: int, kalender_je_tag: float) -> float:
        """Weitere kurzfristige Arbeitstage, ohne dass der Sommerjob über beide Grenzen rutscht."""
        res_w = sommer_voll if (jahr == 2027 and sommer_kurz and a.mit_kurzfristig) else 0.0
        res_k = kal_sommer if res_w else 0.0
        nach_tagen = a.tage_kurzfristig - wt[jahr] - res_w
        nach_kalender = (a.kalendertage_kurzfristig - kt[jahr] - res_k) / kalender_je_tag
        return max(0.0, nach_tagen, nach_kalender)

    def kurzfristig(name, jahr, tage, kalender_je_tag, satz):
        wt[jahr] += tage
        kt[jahr] += tage * kalender_je_tag
        betrag = tage * h_tag * satz
        lohn[jahr] += betrag
        abrechnungen.append((jahr, betrag, tage * kalender_je_tag, 0.0))
        buche(name, betrag, tage * h_tag)

    for ph in a.phasen:
        phase_jetzt = ph.name
        # 1. Freie Tage: befristeter Ferienjob (vor dem Zeugnis ein Schülerjob, SV-frei)
        if a.mit_kurzfristig and ph.ferien_tage[2] > 0 and rng.random() < a.p_ferienjob:
            tage = min(max(0.0, _z(rng, ph.ferien_tage) - _summe(z.ferientage, ph.name)),
                       frei_tage(ph.jahr, ph.kalender_je_tag))
            if tage > 0:
                kurzfristig("Ferienjobs vor dem Zeugnis (kurzfristig)", ph.jahr, tage, ph.kalender_je_tag,
                            satz_ferien)
        # 2. Stundenbudget neben der Schule (abzüglich der Stunden, die ein Zusatzgeschäft braucht)
        roh = _z(rng, ph.stunden) * ph.wochen
        abzug = _summe(z.stunden, ph.name)
        budget = max(0.0, roh - abzug)
        if abzug > roh:
            ueberlauf[ph.name] = abzug - roh     # mehr Stunden, als das Budget hergibt: geht auf Lernzeit
        if a.mit_regelmaessig and budget > 0 and ph.monate > 0:
            for q in quellen:
                if not q["da"] or budget <= 0:
                    continue
                r, j = q["r"], ph.jahr
                erloes_h = q["satz"] * (1 - q["kosten"])
                if r.art == "selbst":
                    # Familienversicherung: Jahresgewinn / 12 (ohne Minijob die niedrigere Grenze)
                    cap = 12 * a.grenze_regel[j] - art_summe[j]["selbst"]
                    if r.rv_grenze:
                        cap = min(cap, a.grenze_minijob[j] * ph.monate)
                elif r.art == "mini":
                    cap = a.grenze_minijob[j] * ph.monate
                else:
                    cap = a.uebungsleiter_frei - art_summe[j]["frei"]
                h = min(budget, q["max_woche"] * ph.wochen, max(0.0, cap) / erloes_h)
                if h <= 0:
                    continue
                gewinn = h * erloes_h
                budget -= h
                art_summe[j][r.art] += gewinn
                if r.art == "mini":
                    mini_monate[j] += ph.monate
                if r.rv_grenze:
                    nachhilfe[j] += gewinn
                    nachhilfe_monate[j] += ph.monate
                buche(r.name, gewinn, h)
        # 3. Einzelne kurzfristige Einsätze am Wochenende
        if a.mit_kurzfristig and ph.einsatz_tage[2] > 0 and (budget > 0 or paarweise):
            # Mit Zusatz (auch leerem) immer ziehen: dann bleiben die Zufallszahlen mit und ohne
            # Zusatzgeschäft dieselben, auch wenn das Zusatzgeschäft das Budget aufbraucht.
            einsatz = _z(rng, ph.einsatz_tage)
            tage = min(einsatz, budget / h_tag, frei_tage(ph.jahr, 1.0)) if budget > 0 else 0.0
            if tage > 0:
                kurzfristig("Einsätze am Wochenende (kurzfristig)", ph.jahr, tage, 1.0, satz_einsatz)

    phase_jetzt = "Jahresabschluss und Sommer"
    # Minijob neben selbstständigem Gewinn: Minijob im Monat + Jahresgewinn / 12 <= 603/633
    for j in jahre:
        mini = art_summe[j]["mini"]
        if mini > 0:
            erlaubt = mini_monate[j] * max(0.0, a.grenze_minijob[j] - art_summe[j]["selbst"] / 12)
            if mini > erlaubt:
                q = next(x for x in quellen if x["r"].art == "mini")
                zuviel = mini - erlaubt
                art_summe[j]["mini"] = erlaubt
                if erlaubt <= 0:
                    mini_monate[j] = 0.0
                buche(q["r"].name, -zuviel, -zuviel / q["satz"])

    # 4. Sommer nach dem Zeugnis: Vollzeitjob, ggf. dazu Samstage
    augustlohn_netto = 0.0
    sommer_lohn_monate = [0.0, 0.0, 0.0]     # Brutto des Sommerjobs im Juni, Juli, August
    if a.mit_kurzfristig and sommer_voll > 0:
        if sommer_kurz:
            nach_tagen = a.tage_kurzfristig - wt[2027]
            nach_kalender = sommer_voll * min(1.0, (a.kalendertage_kurzfristig - kt[2027]) / kal_sommer)
            tage = max(0.0, min(sommer_voll, max(nach_tagen, nach_kalender)))
            wt[2027] += tage
            kt[2027] += kal_sommer * tage / sommer_voll
        else:
            tage = sommer_voll
        anteil = tage / sommer_voll
        wochen_job = werktage_sommer * (1.0 if z.sommer_teilzeit else z.sommer_anteil) / 5
        stunden = min(tage * min(h_tag, 10.0), a.max_stunden_woche * wochen_job * anteil)
        satz_sommer = satz_ferien if z.sommer_satz is None else z.sommer_satz
        betrag = stunden * satz_sommer if z.sommer_brutto is None else z.sommer_brutto * anteil
        lohn[2027] += betrag
        vorsorge = 0.0 if sommer_kurz else a.vorsorge_lohnsteuer
        if not sommer_kurz:
            lohn_sv[2027] += betrag
        # Lohnzahlungszeiträume: Juni (3 Tage), Juli, August – gekürzt wird am Ende. Beginnt der Job
        # später (Zusatzgeschäft zuerst), fehlen die ersten Tage: dann von August aus rückwärts füllen.
        s = z.sommer_anteil
        tage_job = werktage_sommer * s * anteil          # Mo–Fr-Arbeitstage des Jobs
        rest = tage_job
        # bei Ausbildungsbeginn 01.08. endet der Job am 30.07.: nur Juni und Juli
        monate = list(enumerate(SOMMER_MONATE[:2] if werktage_sommer <= 25 else SOMMER_MONATE))
        if not z.sommer_teilzeit:
            monate.reverse()
        for monat, (arbeitstage, kalendertage) in monate:
            je_monat = arbeitstage * (s if z.sommer_teilzeit else 1.0)
            teil = min(rest, je_monat)
            if teil <= 0:
                break
            b_monat, k_monat = betrag * teil / tage_job, kalendertage * teil / je_monat
            abrechnungen.append((2027, b_monat, k_monat, vorsorge))
            sommer_lohn_monate[monat] += b_monat
            if monat == 2:
                # Stundenlohn ist erst nach Monatsende fällig (§ 614 BGB, § 2 MiLoG): oft im September
                sv_satz = 0.0 if sommer_kurz else a.sv_berufsmaessig
                augustlohn_netto = b_monat * (1 - sv_satz) - lohnsteuer(b_monat, k_monat, 2027, vorsorge)
            rest -= teil
        buche("Sommerjob nach dem Zeugnis" + (" (kurzfristig)" if sommer_kurz else " (sozialversicherungspflichtig)"),
              betrag, stunden)
    if start == "01.08.":
        azubi = _z(rng, a.azubi_brutto)
        lohn[2027] += azubi
        lohn_sv[2027] += azubi
        abrechnungen.append((2027, azubi, 30, a.vorsorge_lohnsteuer))
        buche("Ausbildungsvergütung August", azubi, 0.0)
    # Zusatzgeschäft: Gewinn zählt zur Einkommensteuer und zur Familienversicherung (geprüft in
    # plan/hebel_2027.py, dort auch die Kosten einer eigenen Krankenversicherung)
    for j, g in z.gewinn:
        art_summe[j]["selbst"] += g
        buche("Zusatzgeschäft", g, 0.0)

    # Abgaben
    netto = kontostand = brutto_summe = sv_summe = 0.0
    einbehalten = sum(lohnsteuer(b, k, j, v) for j, b, k, v in abrechnungen if j == 2027)
    steuer_jahr = {}
    for j in jahre:
        s = art_summe[j]
        sv = lohn_sv[j] * a.sv_berufsmaessig
        frei_ueber = max(0.0, s["frei"] - a.uebungsleiter_frei)
        zve = (max(0.0, lohn[j] - sv - min(AN_PAUSCHBETRAG[j], lohn[j]) - SA_PAUSCHBETRAG) + s["selbst"] + frei_ueber
               - _summe(z.sonderausgaben, j))
        steuer_jahr[j] = einkommensteuer(zve, j)
        brutto_j = lohn[j] + s["mini"] + s["selbst"] + s["frei"]
        netto += brutto_j - sv - steuer_jahr[j]
        brutto_summe += brutto_j
        sv_summe += sv
    # Am 31.08.2027: Steuer 2026 ist erklärt und erstattet (Median ~100 EUR), für 2027 fehlt die
    # einbehaltene Lohnsteuer; der Augustlohn des Sommerjobs ist hier schon gutgeschrieben.
    kontostand = netto + steuer_jahr[2027] - einbehalten
    pruef = {j: {"selbst": art_summe[j]["selbst"], "mini": art_summe[j]["mini"], "mini_monate": mini_monate[j],
                 "frei": art_summe[j]["frei"], "nachhilfe": nachhilfe[j], "nachhilfe_monate": nachhilfe_monate[j],
                 "arbeitstage": wt[j], "kalendertage": kt[j]} for j in jahre}
    return {"netto": netto, "kontostand": kontostand, "kontostand_ohne_augustlohn": kontostand - augustlohn_netto,
            "ueberlauf": ueberlauf,
            "einbehalten": einbehalten, "steuer": steuer_jahr, "sommer_lohn_monate": sommer_lohn_monate,
            "sv": sv_summe, "lohn_sv": sum(lohn_sv.values()), "brutto": brutto_summe, "stunden": stunden_gesamt,
            "je_quelle": je_quelle, "stunden_je_quelle": stunden_je_quelle, "je_phase": je_phase, "stunden_je_phase": stunden_je_phase, "dual": dual, "start": start, "industrie": industrie,
            "tage_kurzfristig": dict(wt), "kalendertage_kurzfristig": dict(kt), "pruef": pruef}


def auswerten(n: int = 20_000, seed: int = 2027, a: Annahmen | None = None) -> dict:
    a = a or Annahmen()
    rng = random.Random(seed)
    verlaeufe = [ein_verlauf(rng, a) for _ in range(n)]
    netto = sorted(v["netto"] for v in verlaeufe)

    def qu(p):
        return netto[min(n - 1, int(n * p))]

    def median(key):
        return sorted(v[key] for v in verlaeufe)[n // 2]

    quellen: dict[str, list[float]] = {}
    for v in verlaeufe:
        for k, x in v["je_quelle"].items():
            quellen.setdefault(k, []).append(x)
    return {"p10": qu(0.10), "p25": qu(0.25), "median": qu(0.50), "p75": qu(0.75), "p90": qu(0.90),
            "p99": qu(0.99), "mittel": sum(netto) / n,
            "stunden_median": median("stunden"), "kontostand_median": median("kontostand"),
            "kontostand_ohne_augustlohn_median": median("kontostand_ohne_augustlohn"), "sv_median": median("sv"),
            "einbehalten_median": median("einbehalten"), "einbehalten_mittel": sum(v["einbehalten"] for v in verlaeufe) / n,
            "quellen_mittel": {k: sum(x) / n for k, x in quellen.items()}}


def obergrenze(a: Annahmen | None = None) -> dict:
    """Bestmöglicher Verlauf: alles am oberen Rand, Studium danach (keine SV), Beginn 01.10."""
    a = a or Annahmen()
    hoch = replace(
        a, p_dual=0.0, p_industrie=(1, 1, 1), p_ferienjob=1.0,
        satz_industrie=_oben(a.satz_industrie), satz_einsatz=_oben(a.satz_einsatz),
        stunden_tag=(10.0,) * 3, samstage=(1.0,) * 3,
        regelmaessig=tuple(replace(r, satz=_oben(r.satz), max_woche=_oben(r.max_woche),
                                   p_verfuegbar=(1, 1, 1), kosten=(r.kosten[0],) * 3) for r in a.regelmaessig),
        phasen=tuple(replace(p, stunden=_oben(p.stunden), einsatz_tage=_oben(p.einsatz_tage),
                             ferien_tage=_oben(p.ferien_tage)) for p in a.phasen))
    return ein_verlauf(random.Random(1), hoch)


def ohne_jobtage_mai_juni(a: Annahmen) -> Annahmen:
    """Keine Jobtage in den Pfingstferien und zwischen letzter Prüfung und Zeugnis."""
    mai_juni = ("Einzelne Tage in den Pfingstferien", "Nach den Prüfungen")
    return replace(a, phasen=tuple(replace(p, ferien_tage=(0, 0, 0)) if p.name.startswith(mai_juni) else p
                                   for p in a.phasen))


STRATEGIEN = {
    "beste Mischung": {},
    "ohne Webgeschäft": {"mit_webgeschaeft": False},
    "nur befristete Jobs (Ferien, Einsätze, Sommer)": {"mit_regelmaessig": False},
    "nur Nebenjobs neben der Schule (keine Ferien-/Sommerjobs)": {"mit_kurzfristig": False},
}

MINDESTLOHN = (14.6, 14.6, 14.6)
SZENARIEN = {
    "FH-Studium ab 01.10. (Sommerjob SV-frei)": {"p_dual": 0.0},
    "dual/Ausbildung, Start 01.09. oder 01.10.": {"p_dual": 1.0, "start_dual": (("01.09.", 1.0),)},
    "dual/Ausbildung, Start 01.08.": {"p_dual": 1.0, "start_dual": (("01.08.", 1.0),)},
    "Industrie-/Lagerjob in Ferien und Sommer sicher (17–20,50 €/h)": {"p_industrie": (1, 1, 1)},
    "kein Industriejob (14,60–17 €/h)": {"p_industrie": (0, 0, 0)},
    "überall nur Mindestlohn 14,60 €/h": {"satz_industrie": MINDESTLOHN, "satz_sonst": MINDESTLOHN,
                                          "satz_einsatz": MINDESTLOHN},
    "ohne Jobtage im Mai/Juni vor dem Zeugnis": "ohne_mai_juni",
    "ohne alle Ferienjobs vor dem Zeugnis": {"p_ferienjob": 0.0},
}


def szenario(aend) -> Annahmen:
    a = Annahmen()
    if aend == "ohne_mai_juni":
        return ohne_jobtage_mai_juni(a)
    return replace(a, **aend)


def _eur(x: float) -> str:
    return f"{x:7,.0f}".replace(",", ".")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--n", type=int, default=20_000)
    args = ap.parse_args()
    print(f"Netto erwirtschaftet 23.11.2026–31.08.2027 (nach Steuer und Abgaben), {args.n} Verläufe")
    print("-" * 110)
    for titel, aend in STRATEGIEN.items():
        r = auswerten(args.n, a=replace(Annahmen(), **aend))
        print(f"  {titel:58s} sicher (90 %) {_eur(r['p10'])}  Median {_eur(r['median'])}"
              f"  gut (10 %) {_eur(r['p90'])}  Spitze (1 %) {_eur(r['p99'])}")
    print("\n  Szenarien (beste Mischung):")
    for titel, aend in SZENARIEN.items():
        r = auswerten(args.n, a=szenario(aend))
        print(f"  {titel:58s} sicher (90 %) {_eur(r['p10'])}  Median {_eur(r['median'])}"
              f"  gut (10 %) {_eur(r['p90'])}")
        if titel.startswith(("FH", "dual")):
            print(f"  {'':58s} Median: am 31.08. auf dem Konto {_eur(r['kontostand_median'])}, ohne Augustlohn "
                  f"{_eur(r['kontostand_ohne_augustlohn_median'])}; Lohnsteuer einbehalten "
                  f"{_eur(r['einbehalten_median'])}; Sozialabgaben {_eur(r['sv_median'])}")
    r = auswerten(args.n)
    print(f"\n  Beste Mischung: Stunden (Median) {r['stunden_median']:.0f}; Lohnsteuer 2027 einbehalten "
          f"(Median) {_eur(r['einbehalten_median'])} EUR, Kontostand am 31.08. (Median) "
          f"{_eur(r['kontostand_median'])} EUR, ohne Augustlohn {_eur(r['kontostand_ohne_augustlohn_median'])} EUR")
    print("  Mittlerer Beitrag je Quelle (brutto bzw. Gewinn):")
    for k, x in sorted(r["quellen_mittel"].items(), key=lambda kv: -kv[1]):
        print(f"    {k:58s} {_eur(x)} EUR")
    o = obergrenze()
    print(f"\n  Obergrenze (alles am oberen Rand, Studium danach): {_eur(o['netto'])} EUR netto in "
          f"{_eur(o['stunden']).strip()} Stunden; am 31.08. auf dem Konto {_eur(o['kontostand'])} EUR")
    for k, x in sorted(o["je_quelle"].items(), key=lambda kv: -kv[1]):
        print(f"    {k:58s} {_eur(x)} EUR")
    print(f"    Steuer 2026/2027: {_eur(o['steuer'][2026])} / {_eur(o['steuer'][2027])} EUR; "
          f"kurzfristige Arbeitstage 2027 {o['tage_kurzfristig'][2027]:.1f}, "
          f"Kalendertage {o['kalendertage_kurzfristig'][2027]:.1f}")
    o60 = obergrenze(replace(Annahmen(), max_stunden_woche=60.0))
    print(f"  ... mit 60-Stunden-Wochen im Sommer (ArbZG nur mit Ausgleich): {_eur(o60['netto'])} EUR netto in "
          f"{_eur(o60['stunden']).strip()} Stunden")


if __name__ == "__main__":
    main()
