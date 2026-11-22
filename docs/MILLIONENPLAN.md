# Der Millionenplan

**Ziel:** 1.000.000 € Nettovermögen (nominal, nach Steuer beim Verkauf),
erreicht mit **mindestens 50 % Wahrscheinlichkeit**.

**Ergebnis in einem Satz:** Bis Sommer 2027 ist das nicht möglich (≤ 0,5 %,
beweisbar). Mit dem Plan unten liegt die Chance bis **Sommer {ZIEL_JAHR} (Alter
~{ZIEL_ALTER})** bei **{P_ZIEL}** – unter realistischen Annahmen, die drei
unabhängige Gegenprüfungen überstanden haben. Mit 40 sind es {P_40}.

Alle Zahlen stammen aus `python3 plan/simulation.py` (Monte-Carlo, Tausende
simulierte Leben je Weg) und lassen sich dort nachrechnen und verändern.

---

## 1. Warum nicht bis Sommer 2027 – und zwar beweisbar

Für jedes Spiel mit Erwartungswert null oder negativ (Roulette, Lotto,
Sportwetten, Daytrading, CFDs, Optionen, Krypto-Zocken) gilt für **jede**
Strategie: Die Chance, aus S Euro jemals Z Euro zu machen, ist höchstens S / Z
(Ville-Ungleichung). Mit 5.000 € Startkapital sind das **0,5 %**.

| Weg bis 31.08.2027, Start 5.000 € | Chance auf 1 Mio. € |
|---|---:|
| Obergrenze für jede Strategie bei fairem Spiel | 0,50 % |
| Roulette, beste Strategie (alles auf einmal setzen) | 0,40 % |
| Welt-ETF mit 1-, 3- oder 10-fachem Hebel | 0,000 % |
| Theoretisch beste Hebelstrategie mit Aktien-Drift (Browne 1999) | ≈ 1,1–1,4 % |

Real verlieren 74–89 % der CFD-Konten (ESMA) und 74 % der Turbo-Anleger
(BaFin 2019–2023) Geld. Ein Geschäft kommt auch nicht in die Nähe: 1 Mio. €
netto in acht Monaten heißt rund 1,8 Mio. € Gewinn – neben dem Abitur.

## 2. Was die Recherche gezeigt hat

| Befund | Quelle |
|---|---|
| Nur ~1,5 % der Erwachsenen haben ≥ 1 Mio. €; 77 % davon sind 50+ | DIW 2020 |
| 73 % der erwerbstätigen Millionäre sind selbstständig, 80 % davon mit Personal | DIW 2020 |
| Selbst das oberste Einkommenszehntel hat im Median nur 650 Tsd. € Vermögen | Bundesbank PHF 2023 |
| Nur 38 % der Gründungen überleben 5 Jahre, Solo-Gründungen 34 % | IfM Bonn |
| Von überlebenden Vollzeit-Web-Agenturen zahlen sich in Jahr 3–5 nur ~20 % ≥ 50 Tsd. aus | Admin Bar 2026 (Rohdaten, n = 622) |
| Angestellte Entwickler in DE: Median 49 Tsd. (1–3 J.), 78 Tsd. (10–13 J.) | Stack Overflow DE 2024+25 (n = 4.345) |
| IT-Freelancer Software/Web: 91 €/h, ~145 Tage/Jahr, 80 % mit > 10 J. Praxis | Freelancer-Kompass 2026 |
| SaaS-Vertrieb: nur 22–46 % der SDRs werden AE, 26 % der Beförderungen scheitern | UNIFY, Bridge Group |
| Junior-Software-Engineer Schweiz: CHF 75–88 Tsd. | Payscale, Lohncheck 2026 |
| Firmenkauf (Search Funds): 26–31 % Verlust-Deals, außerhalb USA Median-IRR 9 % | Stanford, Yale, IESE |
| Oberstes Zehntel spart ~20 % des Nettos | SOEP 2025 (DIW 47/2026) |

**Konsequenz:** Kein einzelner Weg trägt die Million früh. Was trägt, ist
eine Kombination aus (1) früh eigenem Einkommen, (2) einem Lohnniveau
deutlich über dem deutschen Median – realistisch nur über die **Schweiz** –,
(3) einer harten, automatisierten Sparregel und (4) 20+ Jahren Zinseszins.

## 3. Was getestet und verworfen wurde

Alle Wege liefen durch **dasselbe Modell** mit denselben Risiken
(Börsencrashs, Krisenjahre mit Jobverlust, Studienabbruch, Partnerschaft,
Kinder, Scheidung, Immobilienkauf, Konsumträgheit) und derselben Sparregel.

{TABELLE_KANDIDATEN}

Verworfen und warum:

- **Webagentur als Hauptweg:** Solo-Agenturen verdienen meist wenig; die
  Million braucht ein Team von 10+ Köpfen (in den Daten ~1 % nach 10 Jahren).
- **IT-/SaaS-Vertrieb zuerst:** Sah zuerst wie der Sieger aus. Die
  Gegenprüfung zeigte: Das Modell hatte fast jeden zum Account Executive
  gemacht und den Gehaltssprung doppelt gezählt. Mit Marktdaten fällt der Weg
  ans Ende.
- **Firmenkauf (Nachfolge):** Verschiebt die Schwelle nicht nach vorn, erhöht
  aber das Risiko. Typischer Kleinbetrieb = gekaufter Arbeitsplatz.
- **Software-/SaaS-Wette, Creator, E-Commerce:** Median-Indie-Produkt 169 USD
  Monatsumsatz; nur ~4 % der Creator > 100 Tsd. USD. Als Nebenoption ok, als
  Plan nicht.
- **Immobilien mit Kredit:** Bauzins ~4,3 % > Bruttomietrendite ~3,3 %.
- **Trading, Krypto, Hebel:** Siehe Abschnitt 1.

Neu getestet und **übernommen**: das **praxisintegrierte Bachelorstudium
(PiBS) in der Schweiz** – vier Jahre FH-Studium mit 40 % Arbeit im Schweizer
Partnerbetrieb. Danach ist man schon im Schweizer Arbeitsmarkt.

## 4. Der Plan

{PLAN_TEXT}

## 5. Bis Sommer 2027 – was mit mindestens 50 % geht

{SOMMER_TEXT}

## 6. Kontrollwerte: Bin ich noch auf Kurs?

{KONTROLLWERTE}

## 7. Was den Plan kippt – und was nicht

{SENSITIVITAET}

## 8. Feldtest: Gibt es die Kunden für das Webgeschäft wirklich?

`standortcheck` lief am 21.11.2026 gegen 35 echte Betriebe (OpenStreetMap,
15 km um Regensburg; 11 Elektro, 9 Maler, 15 Sanitär/Heizung).

| Ergebnis | Anzahl |
|---|---:|
| Betriebe mit Website-Eintrag | 22 von 35 |
| davon auswertbar | 20 |
| mit mindestens einem Befund | **19 von 20** |
| mit schwerem, kritischem oder Rechts-Befund | **11 von 20** |

Von Hand bestätigt: eine Domain, die **indonesische Glücksspielwerbung** statt
des Elektrobetriebs zeigt; ein abgelaufenes TLS-Zertifikat; ein Server mit
Fehler 500. Der Bedarf ist echt – für Kleinaufträge bis Sommer 2027.

Der Test fand auch einen **Fehlalarm im Werkzeug** (responsive Seiten mit
`initial-scale=1` galten als „feste Breite“, `maximum-scale=10` als
Zoom-Sperre) – behoben, mit Tests. Und: „Keine Website“ laut OpenStreetMap
stimmt nur etwa in der Hälfte der Fälle; vor jedem Kontakt kurz suchen.

## 9. Wie die Zahlen geprüft wurden

1. **Recherche** in sechs Themen plus Lückenprüfung und drei
   Nachrecherchen (Primärquellen: Destatis, Bundesbank, DIW, IfM, KfW, MSCI,
   BIBB, DZHW, Stack-Overflow-Rohdaten, Freelancer-Kompass).
2. **Kalibrierung:** Das Agenturmodell wurde gegen Überlebensraten und
   Gewinnverteilungen eingestellt, Gehälter gegen Stack-Overflow-Rohdaten.
3. **Zwei Runden Gegenprüfung** mit unabhängigen Prüfern, deren Auftrag war,
   die Behauptung zu widerlegen. Sie haben es geschafft – die erste
   Empfehlung (Vertrieb, „50 % mit 40“) fiel durch und wurde ersetzt.
   {PRUEFUNG_2}
4. **Grenzen:** Das Modell ist eine Rechnung, keine Prophezeiung. Viele
   Spannen (Chance auf Schweizer Stelle, PiBS-Platz) sind begründete
   Schätzungen. Wer die eigenen Ist-Werte kennt, sollte sie in
   `plan/simulation.py` eintragen und neu rechnen.
