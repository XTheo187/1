"""Einstiegsangebote: einzelne Maßnahmen zum Festpreis.

Warum das die bessere erste Stufe ist: Ein Auftrag über 1.700 Euro braucht
Bedenkzeit, oft eine zweite Person und eine Angebotsphase. Ein Auftrag über
149 Euro wird im Gespräch entschieden. Die Abschlusswahrscheinlichkeit je
Kontakt steigt dadurch deutlich, der Geldeingang kommt Wochen früher - und
der Kunde ist danach keine Kaltansprache mehr, sondern eine Referenz mit
offener Rechnung an Vertrauen.

Jeder Baustein ist so geschnitten, dass er in einer Sitzung fertig wird.
Nichts hier braucht Zugriff auf gewachsene Systeme oder Abstimmung mit
Dritten - das ist die Bedingung dafür, dass ein Festpreis trägt.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

# Obergrenze, bis zu der ein Betrieb erfahrungsgemäß ohne Angebotsphase
# und ohne Rücksprache zusagt.
SOFORT_GRENZE = 350.0
# Nachlass, wenn zwei Bausteine zusammen beauftragt werden.
BUENDEL_NACHLASS = 0.9


def stunden_text(h: float) -> str:
    """Aufwand in deutscher Schreibweise: 2,5 h statt 2.50 h."""
    text = f"{h:.2f}".rstrip("0").rstrip(".") or "0"
    return text.replace(".", ",") + " h"


@dataclass(frozen=True)
class Baustein:
    """Eine verkaufbare Einzelmaßnahme."""

    code: str            # zugehöriger Audit-Befund
    titel: str           # so steht es auf der Rechnung
    preis: float         # Festpreis, netto (als Kleinunternehmer = Endpreis)
    stunden: float       # realistischer Aufwand inklusive Prüfung
    zugkraft: int        # wie leicht es sich verkauft, 0-100
    haken: str           # der Satz, der im Gespräch die Zusage auslöst
    ergebnis: str        # was der Betrieb danach konkret hat

    @property
    def stundensatz(self) -> float:
        return round(self.preis / self.stunden, 2) if self.stunden else 0.0

    def as_dict(self) -> dict[str, Any]:
        d = self.__dict__.copy()
        d["stundensatz"] = self.stundensatz
        return d


# Reihenfolge egal - sortiert wird über die Zugkraft.
# Zugkraft hoch = konkretes Risiko oder sofort sichtbares Ergebnis.
KATALOG: list[Baustein] = [
    Baustein(
        "schriften_extern", "Schriftarten lokal einbinden", 149.0, 1.0, 95,
        "Ihre Seite lädt die Schriften direkt von einem Google-Server. Dabei "
        "geht die IP-Adresse jedes Besuchers ohne Einwilligung nach draußen - "
        "genau dafür gab es die Abmahnwelle. Ich stelle das um, dauert eine "
        "Stunde.",
        "Keine Übertragung an Dritte mehr beim Seitenaufruf.",
    ),
    Baustein(
        "kein_impressum", "Impressum einrichten und verlinken", 199.0, 1.5, 93,
        "Auf Ihrer Seite finde ich kein Impressum. Das ist nach § 5 DDG "
        "Pflicht, und Mitbewerber lassen so etwas abmahnen. Ich setze es "
        "auf und verlinke es aus der Fußzeile.",
        "Rechtskonforme Anbieterkennzeichnung auf jeder Seite.",
    ),
    Baustein(
        "keine_datenschutzerklaerung", "Datenschutzerklärung erstellen", 249.0, 2.0, 90,
        "Es ist keine Datenschutzerklärung verlinkt. Die verlangt Art. 13 "
        "DSGVO ab dem ersten Seitenaufruf. Ich erstelle sie passend zu dem, "
        "was Ihre Seite tatsächlich einsetzt.",
        "Datenschutzerklärung, die zu den eingesetzten Diensten passt.",
    ),
    Baustein(
        "kein_https", "Verschlüsselung einrichten", 199.0, 2.0, 88,
        "Ihre Seite zeigt im Browser „Nicht sicher“. Das sieht jeder Besucher "
        "vor Ihrem Angebot. Das Zertifikat selbst ist kostenlos, ich richte "
        "es ein und leite alles sauber um.",
        "Schloss-Symbol statt Warnung, automatische Verlängerung eingerichtet.",
    ),
    Baustein(
        "tracking_ohne_einwilligung", "Einwilligungsbanner einbauen", 349.0, 4.0, 82,
        "Ihre Seite lädt Analysedienste, bevor der Besucher zustimmen konnte. "
        "§ 25 TDDDG verlangt die Einwilligung vorher. Ich baue das Banner ein "
        "und sorge dafür, dass die Dienste erst danach starten.",
        "Einwilligung vor dem Laden, Nachweis dokumentiert.",
    ),
    Baustein(
        "kein_markup", "Google-Eintrag mit Öffnungszeiten", 199.0, 1.5, 80,
        "Ihr Eintrag bei Google zeigt keine Öffnungszeiten. Mit den richtigen "
        "Angaben im Quelltext erscheinen Adresse und Zeiten direkt im "
        "Suchergebnis - Ihr Eintrag wird größer als der vom Mitbewerber.",
        "Adresse, Telefon und Öffnungszeiten maschinenlesbar hinterlegt.",
    ),
    Baustein(
        "titel_platzhalter", "Google-Titel und Beschreibung", 149.0, 1.0, 78,
        "Über Ihrem Google-Eintrag steht nur ein Platzhalter. Das ist die "
        "Überschrift, die Suchende zuerst lesen. Ich formuliere sie mit "
        "Leistung und Ort.",
        "Aussagekräftiger Titel und Beschreibungstext im Suchergebnis.",
    ),
    Baustein(
        "ort_fehlt_im_titel", "Ort in Titel und Überschrift", 129.0, 0.5, 76,
        "Ihr Ort kommt in Ihrem Google-Eintrag gar nicht vor. Fast jede "
        "lokale Suche enthält ihn aber. Ich nehme ihn in Titel und "
        "Überschrift auf.",
        "Ortsbezug an den Stellen, die Google für die Region auswertet.",
    ),
    Baustein(
        "telefon_nicht_klickbar", "Rufnummer antippbar machen", 79.0, 0.25, 75,
        "Ihre Rufnummer steht als Text da. Auf dem Handy muss man sie "
        "abtippen - viele rufen dann beim nächsten Treffer an. Ich mache "
        "einen Anruf-Link daraus.",
        "Ein Fingertipp auf die Nummer startet den Anruf.",
    ),
    Baustein(
        "keine_telefonnummer", "Rufnummer sichtbar platzieren", 99.0, 0.5, 74,
        "Auf Ihrer Startseite finde ich keine Rufnummer. Bei Ihrem Gewerk "
        "kommt fast jede Anfrage per Anruf. Ich setze sie oben hin, als "
        "Anruf-Link.",
        "Rufnummer im Kopfbereich, auf jedem Gerät antippbar.",
    ),
    Baustein(
        "karte_ohne_einwilligung", "Karte auf Zwei-Klick umstellen", 129.0, 1.5, 72,
        "Ihre Google-Karte lädt sofort und schickt dabei Daten Ihrer Besucher "
        "an Google. Ich stelle sie so um, dass sie erst auf Klick lädt.",
        "Karte lädt erst nach ausdrücklichem Klick des Besuchers.",
    ),
    Baustein(
        "keine_https_umleitung", "HTTPS-Weiterleitung einrichten", 89.0, 0.5, 70,
        "Ihre Seite ist parallel auch unverschlüsselt erreichbar. Je nachdem, "
        "wo jemand einsteigt, landet er auf der unsicheren Variante. Eine "
        "Weiterleitung löst das dauerhaft.",
        "Jeder Aufruf landet auf der verschlüsselten Adresse.",
    ),
    Baustein(
        "verwaist", "Inhalte und Jahresangabe auffrischen", 149.0, 1.0, 68,
        "In Ihrer Fußzeile steht noch eine alte Jahreszahl. Besucher lesen "
        "daraus, dass die Seite niemand mehr betreut - und rufen dann lieber "
        "woanders an. Ich frische das auf und setze das Jahr automatisch.",
        "Aktuelle Seite, Jahresangabe pflegt sich künftig selbst.",
    ),
    Baustein(
        "keine_beschreibung", "Beschreibungstext für Google", 99.0, 0.5, 66,
        "Unter Ihrem Google-Eintrag fehlt der Beschreibungstext. Das ist "
        "Werbefläche, die Sie geschenkt bekommen. Ich schreibe sie.",
        "Beschreibungstext mit Leistung, Ort und Handlungsaufforderung.",
    ),
    Baustein(
        "bilder_ohne_alt", "Alternativtexte für Bilder", 199.0, 3.0, 62,
        "Ihre Bilder haben keine Alternativtexte. Vorleseprogramme können "
        "sie dadurch nicht beschreiben, und Google versteht sie nicht. Ich "
        "ergänze sie.",
        "Beschreibungen für alle Bilder, Grundlage für Barrierefreiheit.",
    ),
    Baustein(
        "mixed_content", "Unsichere Inhalte beheben", 129.0, 1.0, 60,
        "Auf Ihrer verschlüsselten Seite werden einzelne Inhalte "
        "unverschlüsselt geladen. Browser blockieren die teilweise - die "
        "Seite wirkt dann kaputt, ohne dass es auffällt.",
        "Alle Inhalte werden verschlüsselt ausgeliefert.",
    ),
    Baustein(
        "zoom_gesperrt", "Zoom-Sperre entfernen", 69.0, 0.25, 58,
        "Ihre Seite verhindert das Vergrößern per Fingergeste. Wer nicht "
        "mehr so gut sieht, kann Ihre Texte nicht lesen.",
        "Besucher können die Seite auf dem Handy vergrößern.",
    ),
    Baustein(
        "kein_favicon", "Symbol für den Browsertab", 69.0, 0.5, 55,
        "In der Tableiste hat Ihre Seite kein Symbol. Kleinigkeit, aber sie "
        "fällt auf, sobald jemand mehrere Betriebe vergleicht.",
        "Eigenes Symbol in Tab und Lesezeichen.",
    ),
    Baustein(
        "keine_komprimierung", "Komprimierung aktivieren", 89.0, 0.5, 52,
        "Ihr Server liefert unkomprimiert aus. Das ist eine Einstellung, die "
        "die Seite spürbar schneller macht.",
        "Deutlich kleinere Datenmenge je Seitenaufruf.",
    ),
    Baustein(
        "formular_ohne_label", "Formular beschriften", 129.0, 1.0, 50,
        "Ihre Formularfelder haben keine verknüpften Beschriftungen. Mit "
        "Vorleseprogramm ist das Formular praktisch nicht bedienbar.",
        "Jedes Feld sauber beschriftet und zuordenbar.",
    ),
]

NACH_CODE: dict[str, Baustein] = {b.code: b for b in KATALOG}


def passende_bausteine(audit: dict[str, Any] | None) -> list[Baustein]:
    """Alle Bausteine, für die das Audit einen Befund geliefert hat."""
    codes = {b.get("code") for b in (audit or {}).get("befunde", [])}
    treffer = [NACH_CODE[c] for c in codes if c in NACH_CODE]
    return sorted(treffer, key=lambda b: -b.zugkraft)


def einstieg_waehlen(
    audit: dict[str, Any] | None, grenze: float = SOFORT_GRENZE
) -> dict[str, Any] | None:
    """Wählt das Einstiegsangebot: ein Baustein, notfalls zwei im Bündel.

    Gewählt wird nach Zugkraft, nicht nach Preis - der teuerste Baustein
    nützt nichts, wenn er im Gespräch nicht zündet. Die Grenze gilt dabei
    auch für den ersten Baustein: Wer sie auf 100 Euro setzt, will kein
    Angebot über 199 Euro vorgelegt bekommen.
    """
    kandidaten = passende_bausteine(audit)
    if not kandidaten:
        return None

    passend = [b for b in kandidaten if b.preis <= grenze]
    ueber_grenze = False
    if passend:
        erster = passend[0]
    else:
        # Nichts passt in den Rahmen. Statt gar nichts anzubieten das
        # günstigste nehmen und den Aufrufer darauf hinweisen.
        erster = min(kandidaten, key=lambda b: b.preis)
        ueber_grenze = True

    gewaehlt = [erster]
    preis = erster.preis

    # Zweiten Baustein dazunehmen, solange die Zusage im Gespräch fallen kann.
    if not ueber_grenze:
        for weiterer in kandidaten:
            if weiterer is erster:
                continue
            gebuendelt = round((preis + weiterer.preis) * BUENDEL_NACHLASS, -1)
            if gebuendelt <= grenze:
                gewaehlt.append(weiterer)
                preis = gebuendelt
                break

    stunden = sum(b.stunden for b in gewaehlt)
    return {
        "bausteine": [b.as_dict() for b in gewaehlt],
        "preis": round(preis, 2),
        "einzelpreise": round(sum(b.preis for b in gewaehlt), 2),
        "stunden": round(stunden, 2),
        "stundensatz": round(preis / stunden, 2) if stunden else 0.0,
        "haken": gewaehlt[0].haken,
        "weitere_offen": len(kandidaten) - len(gewaehlt),
        "ueber_grenze": ueber_grenze,
    }
