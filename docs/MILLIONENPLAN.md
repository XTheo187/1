# Der Millionenplan

> Entwurf – Ergebnisse und Plan folgen nach der Kalibrierung.

## 1. Warum „Millionär bis Sommer 2027“ nicht geht – und zwar beweisbar

Für jedes Spiel, dessen Erwartungswert null oder negativ ist (Roulette,
Lotto, Sportwetten, Daytrading nach Kosten, Optionen, Krypto-Zocken), gilt
für **jede** denkbare Einsatzstrategie:

> Wahrscheinlichkeit, aus S Euro jemals Z Euro zu machen ≤ S / Z

(Ville-Ungleichung bzw. Optional-Stopping-Satz für Martingale.) Mit 5.000 €
Startkapital sind das höchstens **0,5 %**. Die Simulation bestätigt es
(`python3 plan/simulation.py --sommer`):

| Weg bis 31.08.2027, Start 5.000 € | Wahrscheinlichkeit für 1 Mio. € |
|---|---:|
| Obergrenze für jede Strategie bei fairem Spiel | 0,50 % |
| Roulette, beste Strategie (kühnes Spiel) | 0,40 % |
| Welt-ETF mit 1-, 3- oder 10-fachem Hebel | 0,000 % |

Auch ein Geschäft kommt nicht in die Nähe: Netto 1 Mio. € in acht Monaten
heißt bei bis zu 42 % Steuer rund 1,8 Mio. € Gewinn – neben dem Abitur.

**Was bis Sommer 2027 mit mindestens 50 % geht**, steht in Abschnitt 6.

## 2. Feldtest: Gibt es die Kunden wirklich?

Bevor ein Plan auf dem Website-Geschäft aufbaut, wurde geprüft, ob der
Bedarf echt ist. `standortcheck` lief am 21.11.2026 gegen echte Betriebe.

**Stichprobe:** 35 Betriebe aus OpenStreetMap, 15 km um Regensburg
(11 Elektro, 9 Maler, 15 Sanitär/Heizung; Dachdecker: kein Eintrag).

| Ergebnis | Anzahl |
|---|---:|
| Betriebe mit Website-Eintrag | 22 von 35 |
| davon auswertbar | 20 |
| davon mit mindestens einem Befund | **19 von 20** |
| davon mit schwerem, kritischem oder Rechts-Befund | **11 von 20** |
| ohne Website-Eintrag in OpenStreetMap | 13 von 35 |

Die drei stärksten Einzelbefunde, alle von Hand nachgeprüft:

- Die Domain eines Elektrobetriebs zeigt **indonesische Glücksspielwerbung**
  statt des Betriebs – Domain übernommen oder nach Ablauf weggeschnappt.
- Ein abgelaufenes TLS-Zertifikat: Browser zeigen Besuchern eine Warnseite.
- Ein Server antwortet mit Fehler 500 – die Seite ist schlicht kaputt.

**Was der Test auch gezeigt hat:**

1. **Das Werkzeug hatte einen Fehlalarm.** Zwei responsive Seiten wurden als
   „feste Breite“ gemeldet, weil die Prüfung nur nach `width=device-width`
   suchte; `initial-scale=1` reicht Browsern aber ebenso. Behoben, mit Tests.
   Dabei gleich mitbehoben: `maximum-scale=10` galt als Zoom-Sperre.
   Ein falscher Befund vor einem Kunden kostet mehr als zehn richtige bringen.
2. **„Keine Website“ ist nur ein Hinweis.** Von vier stichprobenartig
   geprüften Betrieben ohne Eintrag hatten zwei tatsächlich keine eigene
   Seite, bei einem deutete eine E-Mail-Domain auf eine hin, einer saß laut
   Verzeichnis gar nicht mehr im Suchgebiet. Vor jedem Kontakt: kurz suchen.
3. **OpenStreetMap allein reicht nicht für viele Kontakte.** 35 Betriebe aus
   vier Gewerken sind wenig. Die Kontaktzahl im Modell ist deshalb begrenzt
   (80–400 bis Sommer 2027), mehr Leads kosten Handrecherche.

## 3. Methode

`plan/simulation.py` spielt für jede Strategie mehrere Tausend Leben durch.
Jedes Leben zieht eigene Annahmen aus belegten Spannweiten: Marktrendite,
Inflation, Gehalt, Abschlussquoten, Risiko des Scheiterns. Gezählt wird, in
wie vielen Leben das Nettovermögen am Stichtag ≥ 1 Mio. € (nominal) ist.

Vorsichtig gerechnet:

- Steuern nach Tarif 2026, Sozialabgaben, KV für Selbstständige.
- Firmenwert zählt erst ab drei Vollzeitkräften und mit 30 % Abschlag.
- Scheitert eine Firma, geht es in eine Anstellung weiter – aber ohne Bonus.
- Sparen nur aus dem, was über dem Grundbedarf liegt.
