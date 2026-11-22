# Standortcheck

Lead-Recherche, Website-Audit und Vertriebssteuerung für einen
Ein-Personen-Betrieb, der lokalen Unternehmen Websites baut und betreut.

Gebaut für zwei harte Grenzen: **500 € Startkapital** und **20 Stunden pro
Woche**. Beide sind als Rechenmodell im Werkzeug hinterlegt, nicht nur als
Notiz im Kopf.

```
standortcheck suchen      Betriebe aus OpenStreetMap holen        (kostenfrei)
standortcheck pruefen     Websites auf 25+ Kriterien prüfen       (kostenfrei)
standortcheck liste       Leads nach Priorität sortieren
standortcheck bericht     Verkaufsfertige Analyse als HTML/PDF
standortcheck einstieg    Einzelmaßnahme zum Festpreis je Lead (kleines Ticket)
standortcheck ansprache   Gesprächsleitfaden, Brief, Nachfass-Mail
standortcheck tagesplan   Was heute zu tun ist
standortcheck kennzahlen  Umsatz, Stundenlohn, Trichter, Empfehlungen
standortcheck plan        Budget-, Trichter- und Kapazitätsmodell
```

## Warum dieses Geschäftsmodell

Bei 500 € Kapital scheidet alles aus, was Reichweite kaufen muss. Was bleibt,
ist Direktvertrieb: wenige Kunden, dafür jeder vierstellig. Eine Website für
einen Handwerksbetrieb kostet 1.500–2.600 € plus 49–89 € Betreuung im Monat.
Zwei Aufträge im Monat sind bei 20 Wochenstunden umsetzbar.

Der Engpass ist dabei nicht das Bauen, sondern **qualifizierte Leads und
überzeugendes Verkaufsmaterial**. Genau das automatisiert dieses Werkzeug:
Es findet Betriebe, prüft ihre Websites auf konkrete Mängel und erzeugt daraus
einen Bericht, der die Mängel in Euro und Rechtsrisiko übersetzt.

Der Unterschied zu kalter Akquise: Sie rufen nicht an, um etwas zu verkaufen,
sondern um einen konkreten Befund mitzuteilen. Das ändert das Gespräch.

### Zwei Stufen, nicht eine

Ein Auftrag über 1.700 € braucht Bedenkzeit, oft eine zweite Person und eine
Angebotsphase. Ein Auftrag über 149 € wird im Gespräch entschieden. Deshalb
gibt es zwei Verkaufsstufen aus demselben Audit:

| Stufe | Was | Preis | Schließt |
|---|---|---:|---:|
| **Einstieg** (`einstieg`) | eine Einzelmaßnahme, in einer Sitzung erledigt | 69–349 € | ~6 % je Vor-Ort-Kontakt |
| **Paket** (`bericht`) | alle Befunde in einem Durchgang + Betreuung | 1.400–2.600 € | ~2 % je Vor-Ort-Kontakt |

Der Einstieg ist nicht das Geschäft, sondern der Weg hinein: Nach einer
gelieferten Maßnahme sind Sie keine Kaltansprache mehr. `standortcheck plan`
rechnet beide Wege gegeneinander.

## Der größere Plan: Millionär mit mindestens 50 %

Das Webgeschäft ist der Einstieg, nicht das Ziel. Wie man aus der 13. Klasse
heraus mit mindestens 50 % Wahrscheinlichkeit 1 Mio. EUR Nettovermögen
erreicht – und warum das nicht bis Sommer 2027, sondern bis Sommer 2065 mit
~60 % geht, und wie robust das ist –, steht in
[`docs/MILLIONENPLAN.md`](docs/MILLIONENPLAN.md).
Die Rechnung dahinter: `python3 plan/simulation.py` (Monte-Carlo, belegte
Spannweiten, drei Runden Gegenprüfung).

## Installation

Kein Fremdpaket, keine Abhängigkeit, keine laufenden Kosten. Nur Python 3.9+.

```bash
git clone <repo> && cd 1
pip install -e .          # optional, für den Befehl "standortcheck"
python3 -m standortcheck --help   # geht auch ohne Installation
```

## Erste Schritte

```bash
standortcheck einrichten                    # Absenderdaten, Budget anlegen
standortcheck plan                          # Budget und Wochenmodell durchrechnen
standortcheck branchen                      # Katalog mit Preisen ansehen

standortcheck suchen --ort Regensburg --branche dachdecker sanitaer elektriker
standortcheck pruefen --alle                # Audit für alle neuen Leads
standortcheck liste                         # Rangliste ansehen

standortcheck bericht --limit 20            # 20 Analysen als HTML
standortcheck einstieg                      # kleines Ticket je Lead ansehen
standortcheck ansprache --art einstieg --limit 20   # Türgespräche dazu
standortcheck ansprache --art alle --limit 20       # Briefe und Leitfäden
```

Danach: Briefe drucken (Analyse als PDF beilegen), verschicken, drei Tage
nach Zustellung anrufen. Jedes Ergebnis eintragen:

```bash
standortcheck stufe 12 gespraech --notiz "Termin Do 10 Uhr" --faellig 2026-09-15
standortcheck zeit akquise 90 --lead 12
standortcheck stufe 12 gewonnen --umsatz 1790
standortcheck kennzahlen
```

## Was das Audit prüft

| Bereich | Prüfungen |
|---|---|
| **Recht** | Impressum, Datenschutzerklärung, Tracking ohne Einwilligung, extern geladene Schriften, Karten ohne Zwei-Klick-Lösung |
| **Technik** | HTTPS, HTTP→HTTPS-Umleitung, TLS-Fehler, Mixed Content, Viewport, Ladezeit, Seitengröße, Komprimierung, veraltete Bibliotheken, Frames |
| **Sichtbarkeit** | Seitentitel, Ort im Titel, Meta-Beschreibung, H1-Struktur, LocalBusiness-Markup |
| **Vertrauen** | Telefonnummer sichtbar und anklickbar, Kontaktweg, Favicon, veraltete Jahresangabe |
| **Barrierefreiheit** | Alternativtexte, Formularbeschriftungen, Sprachauszeichnung, Zoom-Sperre |

Jeder Befund trägt Auswirkung, Empfehlung und Aufwandsschätzung. Daraus
entstehen Schmerz-Score, Maßnahmenplan und Festpreis — alle drei aus derselben
Quelle, damit Bericht und Angebot nie unterschiedliche Zahlen nennen.

## Rechtlicher Rahmen der Ansprache

Das Werkzeug ist bewusst konservativ eingestellt. Kurz zusammengefasst:

| Weg | Bewertung |
|---|---|
| **Brief** | Zulässig. Datenherkunft und Widerspruchsrecht nach Art. 14 DSGVO stehen im erzeugten Anschreiben. |
| **Anruf bei Gewerbetreibenden** | Nach § 7 Abs. 2 Nr. 1 UWG bei mutmaßlicher Einwilligung möglich. Der Leitfaden stellt den sachlichen Bezug im ersten Satz her. |
| **Kalte Werbe-E-Mail** | **Unzulässig** nach § 7 Abs. 2 Nr. 2 UWG, auch gegenüber Unternehmen. Die E-Mail-Vorlage ist deshalb ein reiner Nachfass-Text nach einem geführten Gespräch. |

Widerspricht jemand: Lead auf `verloren` setzen, Notiz hinterlegen, nie wieder
kontaktieren. Das ist keine Rechtsberatung — vor der ersten größeren Kampagne
lohnt eine einmalige anwaltliche Durchsicht der Vorlagen.

Die Lead-Daten stammen aus OpenStreetMap und stehen unter der ODbL. Die
Overpass-Instanzen werden von Freiwilligen betrieben; der Client pausiert
zwischen Abfragen und bricht bei Überlastmeldungen ab.

## Tests

```bash
python3 -m unittest discover -s tests -v     # 89 Tests, kein Netzzugriff nötig
```

## Aufbau

```
standortcheck/
  audit.py      Website-Prüfung (eigener HTML-Parser, nur Standardbibliothek)
  branchen.py   Katalog: OSM-Tags, Projektpreise, Kundenwerte
  angebote.py   Festpreis-Bausteine für den Einstieg
  cli.py        Kommandozeile
  db.py         SQLite: Leads, Audits, Zeiten, Ausgaben
  discover.py   OpenStreetMap-Recherche über Overpass
  konfig.py     Absenderdaten
  outreach.py   Leitfaden, Brief, Nachfass-Mail
  planner.py    Budget, Trichter, Kapazität, Ist-Kennzahlen
  report.py     Auditbericht als eigenständiges HTML
  scoring.py    Priorisierung und Preisbildung
```

Siehe [`docs/GESCHAEFTSPLAN.md`](docs/GESCHAEFTSPLAN.md) für das
Zahlenmodell und den Ablauf der ersten zwölf Wochen.
