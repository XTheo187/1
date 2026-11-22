# Der Millionenplan

**Frage:** Wie werde ich – heute in der 13. Klasse – mit mindestens 50 %
Wahrscheinlichkeit Millionär?

**Antwort in drei Sätzen:**

1. Bis Sommer 2027 geht es nicht: höchstens 0,5 %, und das ist beweisbar.
2. **Planziel: 1 Mio. € Nettovermögen bis Sommer 2065 (Alter ~57) – mit
   60 % Wahrscheinlichkeit** (60,5 % ± 0,5). Das Ziel hält die 50 % auch
   dann, wenn alle nicht hart belegten Annahmen gleichzeitig danebenliegen
   (55,8 %), und sogar knapp, wenn zusätzlich der KI-Druck auf Einsteiger
   sicher eintritt (50,6 % ± 0,2 über 16 unabhängige Läufe). Früheste Marke mit mindestens 50 %: Sommer 2062
   (Alter ~54, 51,9 %). Wer die Sparregel eisern hält, ist mit ~50 % schon
   mit 50 dort.
3. Das ist kein Versprechen, sondern das Ergebnis einer Rechnung mit
   realistischen, belegten Annahmen, die drei Runden unabhängiger
   Gegenprüfung überstanden hat – und dabei von „50 % mit 40“ auf „50 % mit
   54“ korrigiert wurde.

Gemessen wird 1 Mio. € **nominal**, nach der Steuer, die beim Verkauf der
ETFs fällig würde, ohne Erbschaft, ohne Vermögen eines Partners. In heutiger
Kaufkraft sind 1 Mio. € im Jahr 2062 nur etwa **460 Tsd. €**. Wer 1 Mio. € in
heutiger Kaufkraft will: Diese Quote liegt mit 54 bei rund 21 %, mit 60 bei
32 %.

Alles lässt sich nachrechnen: `python3 plan/simulation.py` (Tests:
`python3 -m unittest discover -s tests`).

---

## 1. Warum nicht bis Sommer 2027 – beweisbar

Für jedes Spiel mit Erwartungswert null oder negativ (Roulette, Lotto,
Sportwetten, Daytrading, CFDs, Optionen, Krypto-Zocken) gilt für **jede**
Strategie: Die Chance, aus S Euro jemals Z Euro zu machen, ist höchstens S / Z
(Ville-Ungleichung). Mit 5.000 € Startkapital sind das **0,5 %**.

| Weg bis 31.08.2027, Start 5.000 € | Chance auf 1 Mio. € |
|---|---:|
| Obergrenze für jede Strategie bei fairem Spiel | 0,50 % |
| Roulette, beste Strategie (alles auf einmal setzen) | 0,40 % |
| Welt-ETF mit 1-, 3- oder 10-fachem Hebel | 0,000 % |
| Beste denkbare Hebelstrategie mit Aktien-Drift (Browne 1999) | ≈ 1,1–1,4 % |

In der Praxis verlieren 74–89 % der CFD-Konten (ESMA) und 74 % der
Turbo-Anleger (BaFin 2019–2023) Geld. Und ein Geschäft? 1 Mio. € netto in
acht Monaten wären rund 1,8 Mio. € Gewinn – neben dem Abitur.

## 2. Was die Recherche gezeigt hat

| Befund | Quelle |
|---|---|
| Nur ~1,5 % der Erwachsenen haben ≥ 1 Mio. €; 77 % davon sind 50+ | DIW 2020 |
| 73 % der erwerbstätigen Millionäre sind selbstständig, 80 % davon mit Personal | DIW 2020 |
| Selbst das oberste Einkommenszehntel hat im Median nur 650 Tsd. € | Bundesbank PHF 2023 |
| Nur 38 % der Gründungen überleben 5 Jahre (ohne Beschäftigte 34 %) | IfM Bonn |
| Überlebende Vollzeit-Web-Agenturen, Jahr 3–5: nur ~20 % zahlen sich ≥ 50 Tsd. aus | Admin Bar 2026 (Rohdaten, n = 622) |
| Angestellte Entwickler DE: Median 49 Tsd. (1–3 J.), 78 Tsd. (10–13 J.) | Stack Overflow DE 2024+25 (n = 4.345) |
| IT-Freelancer Software/Web: 91 €/h, ~145 Tage/Jahr, 80 % mit > 10 J. Praxis | Freelancer-Kompass 2026 |
| SaaS-Vertrieb: nur 22–46 % der SDRs werden AE, 26 % der Beförderungen scheitern | UNIFY, Bridge Group |
| Junior-Software-Engineer Schweiz: ~80 Tsd. CHF (FH-Bachelor 81.850) | SwissICT 2026 |
| 45 % der EU-Zuwanderer verlassen die Schweiz binnen 10 Jahren wieder | SECO 2026 |
| Firmenkauf (Search Funds): 26–31 % Verlust-Deals, außerhalb USA Median-IRR 9 % | Stanford, Yale, IESE |
| Oberstes Zehntel spart ~20 % des Nettos; jeder zusätzliche Euro zu 37–60 % | SOEP 2025, EVS 2018 |
| Einsteiger in KI-exponierten Berufen: Beschäftigung −19 % ggü. Vergleichsgruppe | Stanford DEL 2026 |

**Konsequenz:** Kein Einzelweg trägt die Million früh. Was trägt, ist eine
Kombination aus (1) früh eigenem Einkommen, (2) einem Lohnniveau über dem
deutschen Median – realistisch über die **Schweiz** –, (3) einer harten,
automatisierten Sparregel und (4) Jahrzehnten Zinseszins.

## 3. Was getestet wurde

Alle Wege liefen durch **dasselbe Modell** mit denselben Risiken:
Börsencrashs, Krisenjahre mit Jobverlust und Lohnnarbe, Studienabbruch,
KI-Druck auf Einsteiger, Partnerschaft, Kinder, Scheidung, Immobilienkauf,
Berufsunfähigkeit, Rückkehr aus der Schweiz, steigende Sozialabgaben,
Konsumträgheit – und dieselbe Sparregel, die nicht jeder perfekt einhält.
4 × 10.000 simulierte Leben je Weg, Intervall ±0,5 Prozentpunkte.

| Weg | mit 40 | mit 45 | mit 50 | mit 55 | mit 60 | 50 % ab |
|---|---:|---:|---:|---:|---:|---:|
| **Plan: PiBS > dual > Bachelor, dann Schweiz/DE** | 10 % | 24 % | 40 % | 55 % | 68 % | **54** |
| … mit eiserner Sparregel (60 %) | 15 % | 33 % | 51 % | 67 % | 78 % | 50 |
| … mit typischem Elternerbe (nicht Teil des Plans) | 10 % | 24 % | 40 % | 58 % | 74 % | 53 |
| Duales Studium, dann Schweiz/DE | 9 % | 24 % | 39 % | 55 % | 68 % | 54 |
| Sicherer PiBS-Platz, dann Schweiz/DE | 10 % | 25 % | 41 % | 56 % | 68 % | 53–54 |
| Bachelor + Agentur, dann Schweiz/DE | 8 % | 21 % | 36 % | 51 % | 64 % | 55 |
| Plan, aber ohne Schweiz | 5 % | 16 % | 32 % | 49 % | 64 % | 55–56 |
| Plan, aber spart wie typische Gutverdiener | 4 % | 13 % | 25 % | 38 % | 52 % | 59–60 |
| Bachelor + Agentur, Schweiz/DE + Firmenkauf | 11 % | 21 % | 31 % | 40 % | 50 % | ≥ 60 |
| Vertrieb (SaaS) ab 2027 | 3 % | 8 % | 17 % | 28 % | 42 % | > 60 |
| 2 Jahre Agentur Vollzeit, dann Vertrieb | 3 % | 8 % | 17 % | 29 % | 44 % | > 60 |

Verworfen und warum:

- **Webagentur als Hauptweg:** Solo-Agenturen verdienen meist wenig; die
  Million bräuchte ein Team von 10+ Köpfen (in den Daten ~1 % nach 10 Jahren).
  Als Taschengeld und Verkaufsschule bis 2027 ist sie gut.
- **IT-/SaaS-Vertrieb zuerst:** Sah im ersten Entwurf wie der Sieger aus
  („50 % mit 40“). Die Gegenprüfung zeigte: Das Modell machte fast jeden zum
  Account Executive und zählte den Gehaltssprung doppelt. Mit Marktdaten fällt
  der Weg ans Ende.
- **Firmenkauf (Nachfolge):** Etwas mehr Chancen mit 40, aber deutlich
  weniger mit 55 – das Ausfallrisiko frisst den Vorteil.
- **Software-Wette, Creator, E-Commerce:** Median-Indie-Produkt 169 USD
  Monatsumsatz; nur ~4 % der Creator > 100 Tsd. USD. Als Nebenoption ok.
- **Immobilien mit Kredit:** Bauzins ~4,3 % > Bruttomietrendite ~3,3 %.
- **Trading, Krypto, Hebel:** siehe Abschnitt 1.

Neu getestet: das **praxisintegrierte Bachelorstudium (PiBS) in der
Schweiz** (4 Jahre FH, 40 % Arbeit im Schweizer Partnerbetrieb). Ergebnis:
mit Platz leicht besser als das duale Studium, aber die Plätze sind knapp
(2022 nur 128 MINT-Eintritte schweizweit) und der Lohn deckt die Schweizer
Lebenshaltung nicht. Darum steht es im Plan als erste Wahl *wenn* ein Platz
kommt – das duale Studium ist praktisch gleichwertig.

## 4. Der Plan

### Phase 0 – jetzt bis August 2027: Abitur, Bewerbungen, erstes Geld

1. **Abitur hat Vorrang.** Die Note entscheidet über duale Plätze.
2. **Bewerbungen jetzt, nicht im Sommer.** Duale Plätze für Herbst 2027
   werden oft ein Jahr vorher vergeben.
   - 20–40 Bewerbungen auf duale Studienplätze **Informatik /
     Wirtschaftsinformatik**, bis spätestens Februar 2027. Bevorzugt
     Arbeitgeber mit Standort oder Kunden in der Schweiz und ohne lange
     Bindungsklausel.
   - **PiBS** parallel: Ab Januar 2027 bei ZHAW, FHNW, BFH, HSLU, FFHS
     anmelden und direkt bei den Partnerfirmen bewerben. Zulassung mit
     deutschem Abitur vorher bei der Hochschule klären.
   - **Plan B:** Bachelor Informatik an Uni/FH (Bewerbung bis Juli).
3. **Webgeschäft als Verkaufsschule** (`standortcheck`), ~5 h/Woche bis
   März, Pause in den Prüfungen, danach bis 25 h/Woche. Siehe Abschnitt 5.
4. **Geld:** Depot eröffnen, ETF-Sparplan auf einen breiten Welt-ETF
   einrichten, Notgroschen von drei Monatsausgaben, Berufsunfähigkeits-
   versicherung prüfen (jung und gesund ist sie am günstigsten).

### Phase 1 – Herbst 2027 bis ~2031: Ausbildung mit Einkommen

- Rangfolge: **PiBS** (wenn ein Platz kommt und die Finanzierung steht:
  Lebenshaltung in der Schweiz ~25 Tsd. € im Jahr gegen ~17 Tsd. € Lohn
  netto) > **duales Studium** > **Bachelor + Webgeschäft 20 h/Woche**.
- Ab dem ersten eigenen Geld gilt die **Sparregel** (siehe unten).
- Wer in Deutschland studiert: Praktikum oder Abschlussarbeit mit Bezug zur
  Schweiz, Englisch und Deutsch fließend, Lebenslauf auf Schweizer Stellen
  ausrichten.
- **Abbruch-Regel:** Läuft das Studium im ersten Jahr schief, sofort neu
  starten (anderes Studium oder dual) statt zwei Jahre durchhalten.

### Phase 2 – ~2031 bis ~2040: Die Schweiz-Phase

- Erste Wahl: **IT-Stelle in der Schweiz** (Zürich, Basel, Bern, Zug).
  Klappt es nicht sofort: IT-Stelle in Deutschland und **nach 3–4 Jahren
  Berufserfahrung zweiter Anlauf** – mit Erfahrung steigen die Chancen.
- In der Schweiz: Wohnsitz in einer günstigen Steuergemeinde wählen,
  **Säule 3a** voll nutzen, WG oder kleine Wohnung statt großer Wohnung.
- Lebensstil wächst **nicht** mit dem Gehalt – die Sparregel sorgt dafür.
- Vor einer Heirat: Ehevertrag mit modifizierter Zugewinngemeinschaft
  überlegen (Scheidungsrisiko ~28 % der Ehen).
- Kein Eigenheim, bevor das Depot die Hälfte des Ziels erreicht hat
  (Kaufnebenkosten 5–9 % sind sofort weg).

### Phase 3 – ~2040 bis ~2062: Durchhalten

- Weiter sparen, nie verkaufen in Crashs, kein Market-Timing.
- Jedes Jahr die Kontrollwerte (Abschnitt 6) prüfen und nachsteuern.

### Die Sparregel – der wichtigste Teil

> **Grundbedarf:** ~1.500 €/Monat in Deutschland bzw. ~3.200 €/Monat in der
> Schweiz (inkl. Krankenkasse), jedes Jahr um die Inflation angehoben.
> **Von jedem Euro darüber gehen 60 % per Dauerauftrag am Zahltag ins
> ETF-Depot** – auch von jeder Gehaltserhöhung, jedem Bonus.

Das ist etwa doppelt so viel, wie typische Gutverdiener sparen. Genau
deshalb ist es Regel und Dauerauftrag, nicht Vorsatz. Die Hauptzahl dieses
Plans (50 % mit 54) rechnet bewusst damit, dass die Regel nicht perfekt
hält: im Mittel werden nur ~50 % gespart, und 15 % der Leben werden
irgendwann halbherzig. Wer sie wirklich hält, kommt auf 50; wer nur so spart
wie typische Gutverdiener, erst auf 59–60.

### Weichen mit harten Zahlen

| Wann | Wenn … | dann … |
|---|---|---|
| Feb. 2027 | kein dualer Platz und kein PiBS-Gespräch | Bachelor-Bewerbung, Webgeschäft ausbauen |
| Ende 1. Studienjahr | Prüfungen nicht bestanden / kein Interesse | sofort neu starten (dual oder anderes Fach) |
| Studienende | Schweizer Stelle angeboten | annehmen |
| 3–4 Jahre DE-Stelle | noch nicht in der Schweiz | zweiter Anlauf; parallel Gehalt verhandeln |
| ab 5 Berufsjahren | Freelance-Gewinn > 1,2 × Gehalt erreichbar | IT-Freelancing prüfen |
| bei Rückkehr nach DE | Schweiz-Phase endet (Partner, Kinder) | Sparregel weiterführen, Depot nie anfassen |
| jedes Jahr | Vermögen unter dem 25-%-Kontrollwert | Grundbedarf senken, Sparquote erhöhen |

## 5. Bis Sommer 2027 – was mit mindestens 50 % geht

Webgeschäft neben dem Abitur: Vor-Ort-Besuch mit ausgedrucktem Bericht,
zuerst eine Einzelmaßnahme (69–349 €), dann das Website-Paket. Die
Trichterwerte aus `standortcheck` sind dabei **halbiert** angesetzt, weil
sie noch nicht gemessen sind; die Kontaktzahl ist auf 80–400 begrenzt.

| Ziel bis 31.08.2027 | Wahrscheinlichkeit |
|---|---:|
| mindestens 5 zahlende Kunden | **88 %** |
| mindestens 1 komplettes Website-Paket | **80 %** |
| mindestens 3.000 € Umsatz | **75 %** |
| mindestens 5.000 € Umsatz | **52 %** |
| mindestens 10.000 € Umsatz | 14 % |

Regeln dafür:

- Gewerbe anmelden, Kleinunternehmerregelung (§ 19 UStG). Unter 18:
  Genehmigung des Familiengerichts (§ 112 BGB) nötig.
- **Gewinn 2027 unter ~7.080 € halten** – darüber endet die
  Familienversicherung, die eigene Krankenkasse kostet dann mindestens
  ~3.240 € im Jahr.
- Keine kalten Werbe-E-Mails (§ 7 UWG); Besuch, Brief, Anruf.
- „Keine Website laut OpenStreetMap“ vorher kurz nachprüfen (stimmt nur etwa
  in der Hälfte der Fälle).
- Jeden Kontakt und Abschluss eintragen (`standortcheck stufe`, `kennzahlen`)
  – das ist zugleich der Nachweis in jeder Bewerbung.

## 6. Kontrollwerte: Bin ich noch auf Kurs?

Vermögen nach Steuer, nominal (die Hälfte einer Schweizer Pensionskasse
eingerechnet). Liegst du **unter dem linken Wert**, bist du hinter dem Plan
und musst nachsteuern; über dem rechten bist du gut vorn.

| Alter | 25 % liegen darunter | Median | 25 % liegen darüber |
|---:|---:|---:|---:|
| 25 | 11 Tsd. € | 24 Tsd. € | 41 Tsd. € |
| 30 | 60 Tsd. € | 106 Tsd. € | 173 Tsd. € |
| 35 | 126 Tsd. € | 222 Tsd. € | 373 Tsd. € |
| 40 | 194 Tsd. € | 353 Tsd. € | 621 Tsd. € |
| 45 | 277 Tsd. € | 529 Tsd. € | 969 Tsd. € |
| 50 | 385 Tsd. € | 773 Tsd. € | 1,44 Mio. € |
| 55 | 551 Tsd. € | 1,12 Mio. € | 2,11 Mio. € |

## 7. Was den Plan kippt – und was nicht

50-%-Alter, wenn genau ein Faktor auf seinen schlechten bzw. guten Rand
gesetzt wird (Basis: 54).

| Faktor | schlecht | gut |
|---|---:|---:|
| Sparverhalten (typisch / eiserne Regel) | 60 | 50 |
| Aktienrendite (4 % / 8 % im Jahr) | 58 | 50 |
| Grundbedarf (22 / 13 Tsd. € im Jahr) | 56 | 50 |
| KI-Druck auf Einsteiger (sicher / nie) | 56 | 53 |
| Schweizer Stelle (nie / sicher) | 55 | 52 |
| Kinder (sicher und teuer / keine) | 55 | 52 |
| Dualer Studienplatz (nie / sicher) | 55 | 54 |
| Rückkehr aus der Schweiz (4 %/Jahr / nie) | 54 | 52 |

**Was du selbst in der Hand hast, wirkt am stärksten:** Sparregel und
Grundbedarf. Die Börse kannst du nicht steuern – nur aushalten.

**Stresstest** (`python3 plan/simulation.py --stress`): Alle Annahmen ohne
harte Quelle gleichzeitig am pessimistischen Rand – Chance auf eine Schweizer
Stelle halbiert (auch im zweiten Anlauf), nach PiBS deutlich seltener,
PiBS-Platz kaum, dualer Platz seltener, Rückkehr aus der Schweiz über dem
SECO-Wert für alle EU-Zuwanderer.

| Szenario | mit 54 | mit 55 | mit 56 | **mit 57** | mit 58 | mit 60 |
|---|---:|---:|---:|---:|---:|---:|
| Plan (Basis) | 52 % | 55 % | 58 % | **61 %** | 63 % | 68 % |
| Stress: alle Schätzungen pessimistisch | 47 % | 50 % | 53 % | **56 %** | 59 % | 64 % |
| Stress + KI-Druck sicher | 41 % | 44 % | 48 % | **51 %**¹ | 54 % | 59 % |

¹ Unabhängig nachgemessen über 16 Läufe à 10.000 Leben: 50,6 % ± 0,2 –
knapp, aber über 50 %.

Deshalb ist das Planziel **Sommer 2065** und nicht die früheste Marke 2062:
Es bleibt über 50 %, selbst wenn die unsicheren Annahmen alle danebenliegen.

## 8. Feldtest: Gibt es die Kunden fürs Webgeschäft?

`standortcheck` lief am 21.11.2026 gegen 35 echte Betriebe (OpenStreetMap,
15 km um Regensburg; 11 Elektro, 9 Maler, 15 Sanitär/Heizung).

| Ergebnis | Anzahl |
|---|---:|
| Betriebe mit Website-Eintrag | 22 von 35 |
| davon auswertbar | 20 |
| mit mindestens einem Befund | **19 von 20** |
| mit schwerem, kritischem oder Rechts-Befund | **11 von 20** |

Von Hand bestätigt: eine Domain, die **indonesische Glücksspielwerbung**
statt des Elektrobetriebs zeigt; ein abgelaufenes TLS-Zertifikat; ein
Server mit Fehler 500. Deutschlandweit haben ~35 % der Kleinstunternehmen
gar keine Website (Eurostat 2023). Der Bedarf für Kleinaufträge ist echt.

Der Test fand auch einen **Fehlalarm im Werkzeug** (responsive Seiten mit
`initial-scale=1` galten als „feste Breite“, `maximum-scale=10` als
Zoom-Sperre) – behoben, mit Tests. Und: Das Barrierefreiheitsstärkungs-
gesetz nimmt Kleinstunternehmen mit Dienstleistungen aus; als
Verkaufsargument taugt es kaum.

## 9. Wie die Zahlen entstanden und geprüft wurden

1. **Recherche:** sechs Themen, Lückenprüfung, vier Nachrecherchen;
   Primärquellen u. a. Destatis, Bundesbank, DIW, IfM, KfW, MSCI, BIBB,
   DZHW, SECO, SBFI, SwissICT, Stack-Overflow-Rohdaten, Freelancer-Kompass.
2. **Kalibrierung:** Agenturmodell gegen Überlebensraten und
   Gewinnverteilungen, Gehälter gegen Stack-Overflow- und SwissICT-Daten,
   Sparverhalten gegen EVS/SOEP.
3. **Drei Runden Gegenprüfung** (zehn unabhängige Prüfer) mit dem Auftrag,
   die Behauptung zu widerlegen. Gefunden und eingearbeitet, u. a.:
   - zu optimistisch: doppelt gezählter Gehaltssprung im Vertrieb, fehlende
     Rückwanderung aus der Schweiz, zu perfekte Sparregel, ein um ein Jahr
     verschobener Altersbezug, fehlende Studienabbrüche, ein früher Abbruch,
     der als Abschluss zählte, Steuer- und Abgabenfehler;
   - zu streng: Kinderkosten, die den eigenen Konsum nicht berührten, eine
     Lohnnarbe bei jeder Wechsellücke, ungleich behandelte
     Studienfinanzierung, ein Gehalt von null nach früher Rückkehr.
   Die Aussage wanderte von „50 % mit 40“ zu „50 % mit 54“.
   **Schlussverifikation** auf dem gepushten Stand (frischer Checkout, alle
   Tests grün): 8 von 8 unabhängigen Läufen (Seeds 2027/1/2/3 und
   101/202/303/404, je 10.000 Leben) liefern das 50-%-Alter 54;
   P(54) = 51,9 % bzw. 52,1 %, untere Intervallgrenze jeweils über 51,4 %.
   Ein zweiter, unabhängiger Prüfer hat Commit 065359f in einem frischen
   Klon mit eigenen Seeds nachgerechnet: alle Dokumentzahlen innerhalb ±1
   Prozentpunkt; Planziel 2065: Basis 60,3 %, Stress 55,5 %, Stress + KI
   50,6 % (je 160.000 Leben).
   Die Unsicherheit der geschätzten Spannen (Schweizer Stelle, PiBS-Platz,
   Rückkehrrate) steckt bereits in diesen Zahlen, weil jedes Leben seine
   Werte aus der ganzen Spanne zieht; im ungünstigsten Einzelfall (nie eine
   Schweizer Stelle) verschiebt sich die Schwelle auf 55.
4. **Grenzen:** Viele Spannen sind begründete Schätzungen (Chance auf
   Schweizer Stelle, PiBS-Platz, Rückkehrrate, KI-Szenario). Bewusst nicht in
   der Hauptzahl: Erbschaften (mit typischem Elternerbe ~1 Jahr früher), das
   Vermögen eines Partners (als Paar mit Zugewinngemeinschaft gezählt ~1–2
   Jahre früher), die Pensionskasse voll statt halb (~1 Jahr früher),
   Kirchensteuer (bei Mitgliedschaft etwas später). Wer eigene Ist-Werte hat,
   trägt sie in `plan/simulation.py` ein und rechnet neu.
