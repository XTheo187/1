"""Betriebswirtschaft: Budget, Kapazität, Trichter und Ist-Kennzahlen.

Die beiden harten Grenzen sind 500 Euro Startkapital und 20 Stunden pro
Woche. Beide sind hier als Rechenmodell hinterlegt, damit jede Entscheidung
an der tatsächlichen Engstelle gemessen wird - und die ist nicht das Geld,
sondern die Umsetzungszeit.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from typing import Any

from . import db

# --------------------------------------------------------------------------
# Startbudget
# --------------------------------------------------------------------------

BUDGET_500 = [
    # (Posten, Betrag, Kategorie, Begründung)
    ("Gewerbeanmeldung", 30.0, "Formales",
     "Pflicht. Kleinunternehmerregelung nach § 19 UStG wählen: keine "
     "Umsatzsteuer auf Rechnungen, keine Voranmeldung, weniger Buchhaltung."),
    ("Domain + Hosting (12 Monate)", 60.0, "Infrastruktur",
     "Eigene Seite als Referenz. Wer Websites verkauft, wird an seiner "
     "eigenen gemessen - das ist das erste, was jeder Interessent prüft."),
    ("Berufshaftpflicht (3 Monate)", 45.0, "Absicherung",
     "Rund 15 EUR im Monat. Schützt, wenn eine Umstellung beim Kunden "
     "Schaden anrichtet. Nicht optional, sobald fremde Systeme angefasst werden."),
    ("Druck + Porto: 150 Erstanschreiben", 200.0, "Akquise",
     "Der eigentliche Motor. Rund 1,30 EUR je Brief inklusive beigelegter "
     "Analyse. Postalisch, weil Kalt-E-Mail nach § 7 UWG unzulässig ist."),
    ("Visitenkarten + Briefpapier", 40.0, "Akquise",
     "Wird im Vor-Ort-Termin gebraucht. Kleine Menge genügt."),
    ("Rechtstexte für die eigene Seite", 0.0, "Formales",
     "Impressum und Datenschutzerklärung über einen kostenfreien Generator. "
     "Später, ab dem ersten Umsatz, gegen eine geprüfte Fassung tauschen."),
    ("Reserve", 125.0, "Puffer",
     "Fahrtkosten zu Terminen, Nachdruck, unvorhergesehene Gebühren. "
     "Ohne Puffer erzwingt die erste Überraschung einen Stillstand."),
]

# Bewusst nicht im Startbudget - typische Fehlausgaben in dieser Phase.
NICHT_KAUFEN = [
    ("Bezahlte Anzeigen", "Ohne belastbare Abschlussquote wird Werbebudget "
     "verbrannt. Erst messen, dann skalieren."),
    ("Lead-Datenbank-Abo", "Die Recherche über OpenStreetMap kostet nichts "
     "und liefert für lokale Gewerke ausreichend Treffer."),
    ("Logo-Design vom Grafiker", "Beeinflusst den Abschluss bei lokalen "
     "Betrieben nicht messbar. Schrift plus Farbe genügt im ersten Halbjahr."),
    ("Buchhaltungssoftware-Abo", "Bei unter 20 Rechnungen im Jahr reicht "
     "eine Tabelle. Erst ab regelmäßigem Volumen sinnvoll."),
    ("CRM-Abo", "Genau dafür ist dieses Werkzeug da."),
]


# --------------------------------------------------------------------------
# Trichter- und Kapazitätsmodell
# --------------------------------------------------------------------------


@dataclass
class Annahmen:
    """Konservative Ausgangswerte. Nach 100 Briefen durch Ist-Werte ersetzen."""

    stunden_pro_woche: float = 20.0
    briefe_pro_woche: int = 40
    kosten_je_brief: float = 1.30
    minuten_je_brief: float = 4.0        # Personalisieren, drucken, kuvertieren
    minuten_je_anruf: float = 6.0        # inkl. Nachbereitung und Fehlversuchen
    quote_erreicht: float = 0.55         # Anteil der Briefempfänger, die ans Telefon gehen
    quote_gespraech: float = 0.22        # davon echtes Gespräch statt Abwimmeln
    minuten_je_termin: float = 60.0
    quote_angebot: float = 0.45          # Gespräche, die in ein Angebot münden
    quote_abschluss: float = 0.25        # Angebote, die zum Auftrag werden
    projektpreis: float = 1900.0
    betreuung_monatlich: float = 59.0
    umsetzungsstunden: float = 13.0      # Aufwand je gewonnenem Projekt


def trichter(a: Annahmen) -> dict[str, Any]:
    """Rechnet den Verkaufstrichter und prüft ihn gegen die Zeitgrenze."""
    briefe = a.briefe_pro_woche
    erreicht = briefe * a.quote_erreicht
    gespraeche = erreicht * a.quote_gespraech
    angebote = gespraeche * a.quote_angebot
    abschluesse = angebote * a.quote_abschluss

    # Zeitbedarf pro Woche
    zeit_briefe = briefe * a.minuten_je_brief / 60
    zeit_anrufe = briefe * a.minuten_je_anruf / 60
    zeit_termine = gespraeche * a.minuten_je_termin / 60
    zeit_umsetzung = abschluesse * a.umsetzungsstunden
    zeit_verwaltung = 2.0  # Angebote, Rechnungen, Buchhaltung

    gesamt = zeit_briefe + zeit_anrufe + zeit_termine + zeit_umsetzung + zeit_verwaltung
    umsatz = abschluesse * a.projektpreis
    kosten = briefe * a.kosten_je_brief

    return {
        "briefe": briefe,
        "erreicht": round(erreicht, 1),
        "gespraeche": round(gespraeche, 1),
        "angebote": round(angebote, 1),
        "abschluesse": round(abschluesse, 2),
        "zeit": {
            "Briefe vorbereiten": round(zeit_briefe, 1),
            "Telefonakquise": round(zeit_anrufe, 1),
            "Termine": round(zeit_termine, 1),
            "Umsetzung": round(zeit_umsetzung, 1),
            "Verwaltung": round(zeit_verwaltung, 1),
        },
        "zeit_gesamt": round(gesamt, 1),
        "zeit_verfuegbar": a.stunden_pro_woche,
        "auslastung": round(gesamt / a.stunden_pro_woche * 100) if a.stunden_pro_woche else 0,
        "umsatz_woche": round(umsatz),
        "kosten_woche": round(kosten, 2),
        "deckungsbeitrag_woche": round(umsatz - kosten),
        "stundensatz_effektiv": round((umsatz - kosten) / gesamt) if gesamt else 0,
        "umsatz_monat": round(umsatz * 4.33),
        "wiederkehrend_nach_12m": round(abschluesse * 52 * a.betreuung_monatlich),
    }


def briefe_optimieren(a: Annahmen) -> dict[str, Any]:
    """Sucht die Briefmenge, die die 20 Stunden gerade ausfüllt.

    Mehr Briefe erzeugen mehr Aufträge, aber Aufträge kosten Umsetzungszeit.
    Ab einem bestimmten Punkt kippt der Trichter in Rückstand - genau dort
    liegt das Optimum.
    """
    bester: dict[str, Any] | None = None
    for menge in range(5, 201, 5):
        probe = Annahmen(**{**a.__dict__, "briefe_pro_woche": menge})
        e = trichter(probe)
        if e["zeit_gesamt"] > a.stunden_pro_woche:
            break
        bester = e
    if bester is None:
        bester = trichter(Annahmen(**{**a.__dict__, "briefe_pro_woche": 5}))
    return bester


SZENARIEN = {
    "vorsichtig": {
        "quote_erreicht": 0.40, "quote_gespraech": 0.15,
        "quote_angebot": 0.35, "quote_abschluss": 0.18,
        "projektpreis": 1400.0,
    },
    "erwartet": {},  # die Vorgabewerte aus Annahmen
    "gut": {
        "quote_erreicht": 0.65, "quote_gespraech": 0.28,
        "quote_angebot": 0.55, "quote_abschluss": 0.32,
        "projektpreis": 2200.0,
    },
}


def szenarien(a: Annahmen) -> dict[str, dict[str, Any]]:
    """Drei Rechnungen statt einer Zahl - die Spanne ist die ehrliche Aussage."""
    ergebnis = {}
    for name, abweichung in SZENARIEN.items():
        probe = Annahmen(**{**a.__dict__, **abweichung})
        ergebnis[name] = briefe_optimieren(probe)
    return ergebnis


def startkapital_reichweite(a: Annahmen, budget_akquise: float = 200.0) -> dict[str, Any]:
    """Wie weit trägt das Akquisebudget bis zum ersten Geldeingang?"""
    briefe_moeglich = int(budget_akquise / a.kosten_je_brief)
    abschluesse = (
        briefe_moeglich * a.quote_erreicht * a.quote_gespraech
        * a.quote_angebot * a.quote_abschluss
    )
    return {
        "briefe_moeglich": briefe_moeglich,
        "erwartete_abschluesse": round(abschluesse, 1),
        "erwarteter_umsatz": round(abschluesse * a.projektpreis),
        "kosten_je_abschluss": round(budget_akquise / abschluesse) if abschluesse else 0,
        "wochen_bis_verbraucht": round(briefe_moeglich / a.briefe_pro_woche, 1)
        if a.briefe_pro_woche else 0,
        "rendite": round(abschluesse * a.projektpreis / budget_akquise, 1) if budget_akquise else 0,
    }


# --------------------------------------------------------------------------
# Ist-Kennzahlen aus der Datenbank
# --------------------------------------------------------------------------


def kennzahlen(con: sqlite3.Connection) -> dict[str, Any]:
    verteilung = {
        stufe: con.execute(
            "SELECT COUNT(*) FROM leads WHERE stage = ?", (stufe,)
        ).fetchone()[0]
        for stufe in db.STAGES
    }
    gesamt = sum(verteilung.values())

    umsatz = db.summe(con, "SELECT SUM(umsatz) FROM leads")
    ausgaben = db.summe(con, "SELECT SUM(betrag) FROM ausgaben")
    minuten = db.summe(con, "SELECT SUM(minuten) FROM aktivitaeten")
    stunden = minuten / 60

    offene_pipeline = db.summe(
        con,
        "SELECT SUM(ifnull(deal_wert,0)) FROM leads WHERE stage IN "
        "('kontaktiert','gespraech','angebot')",
    )

    kontaktiert = sum(
        verteilung[s] for s in ("kontaktiert", "gespraech", "angebot", "gewonnen", "verloren")
    )
    abgeschlossen = verteilung["gewonnen"] + verteilung["verloren"]

    zeit_nach_art = {
        r["art"]: r["m"] / 60
        for r in con.execute(
            "SELECT art, SUM(minuten) AS m FROM aktivitaeten GROUP BY art ORDER BY m DESC"
        )
    }

    return {
        "leads_gesamt": gesamt,
        "verteilung": verteilung,
        "umsatz": umsatz,
        "ausgaben": ausgaben,
        "gewinn": umsatz - ausgaben,
        "stunden": round(stunden, 1),
        "stundenlohn": round((umsatz - ausgaben) / stunden, 2) if stunden else 0,
        "offene_pipeline": offene_pipeline,
        "abschlussquote": round(verteilung["gewonnen"] / abgeschlossen * 100, 1)
        if abgeschlossen else 0.0,
        "kontaktquote": round(kontaktiert / gesamt * 100, 1) if gesamt else 0.0,
        "umsatz_je_gewonnen": round(umsatz / verteilung["gewonnen"])
        if verteilung["gewonnen"] else 0,
        "kosten_je_kontakt": round(ausgaben / kontaktiert, 2) if kontaktiert else 0,
        "zeit_nach_art": {k: round(v, 1) for k, v in zeit_nach_art.items()},
        "roi_startkapital": round(umsatz / ausgaben, 2) if ausgaben else 0,
    }


def empfehlung(k: dict[str, Any], a: Annahmen) -> list[str]:
    """Leitet aus den Ist-Zahlen die nächste Stellschraube ab."""
    rat: list[str] = []
    v = k["verteilung"]

    if k["leads_gesamt"] == 0:
        return ["Noch keine Leads. Erster Schritt: standortcheck suchen --ort <Stadt> --branche <Gewerk>"]

    ungeprueft = v["neu"]
    if ungeprueft > 0:
        rat.append(
            f"{ungeprueft} Leads ohne Audit. Das kostet nichts außer Rechenzeit: "
            "standortcheck pruefen --alle"
        )
    if v["geprueft"] >= 20:
        rat.append(
            f"{v['geprueft']} geprüfte Leads warten auf Ansprache. Der Trichter "
            "steht still, solange keine Briefe rausgehen."
        )
    if k["kontaktquote"] < 30 and k["leads_gesamt"] > 30:
        rat.append(
            f"Erst {k['kontaktquote']}% der Leads sind angesprochen. Die Engstelle "
            "liegt aktuell in der Akquise, nicht in der Datenmenge - keine neue "
            "Recherche starten."
        )
    if v["angebot"] >= 3:
        rat.append(
            f"{v['angebot']} offene Angebote. Nachfassen bringt hier mehr Umsatz "
            "je Stunde als jede Neuakquise."
        )
    if k["stunden"] > 0 and k["stundenlohn"] < 30 and v["gewonnen"] > 0:
        rat.append(
            f"Effektiver Stundenlohn bei {k['stundenlohn']:.0f} EUR. Entweder die "
            "Preise anheben oder die Umsetzung standardisieren - ein wiederverwendbares "
            "Grundgerüst halbiert typischerweise die Projektzeit."
        )
    if v["gewonnen"] >= 3 and k["abschlussquote"] > 0:
        ist = k["abschlussquote"] / 100
        soll = a.quote_abschluss
        if ist > soll * 1.3:
            rat.append(
                f"Abschlussquote bei {k['abschlussquote']}% - deutlich über der "
                "Annahme. Das ist fast immer ein Zeichen für zu niedrige Preise. "
                "Nächstes Angebot 20% höher ansetzen."
            )
        elif ist < soll * 0.5:
            rat.append(
                f"Abschlussquote bei {k['abschlussquote']}%. Vor mehr Briefen erst "
                "das Gespräch reparieren: Wird im Termin der Auftragswert eines "
                "einzelnen Neukunden konkret durchgerechnet?"
            )
    if k["ausgaben"] > 400 and k["umsatz"] == 0:
        rat.append(
            "Über 400 EUR ausgegeben, noch kein Umsatz. Vom Restbudget nichts "
            "mehr für Material ausgeben - nur noch Porto für Briefe."
        )
    if not rat:
        rat.append(
            "Der Trichter läuft. Weiterschieben: täglich Briefe raus, "
            "Anrufe drei Tage nach Zustellung."
        )
    return rat
