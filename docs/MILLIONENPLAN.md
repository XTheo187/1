# Der Millionenplan

**Frage:** Wie werde ich – heute in der 13. Klasse – mit mindestens 50 %
Wahrscheinlichkeit Millionär?

**Antwort:**

> **Festgelegtes Ziel: 1 Mio. € Nettovermögen am 31. August 2065
> (Alter ~57). Erfolgswahrscheinlichkeit mit diesem Plan: 57 %.**
> Dieses Datum ist das Planziel und wird nicht mehr verschoben.

Alle folgenden Zahlen gelten für **dasselbe Datum, 31.08.2065**:

| Fall | Chance auf 1 Mio. € am 31.08.2065 |
|---|---:|
| Plan wie vorgesehen | **57 %** |
| alle drei Annahmen ohne harte Quelle (Schweizer Stelle, Studienplatz, Rückkehrquote) gleichzeitig pessimistisch | 51 % |
| dazu KI-Druck auf Einsteiger sicher | 46 % |
| ganz ohne Schweiz und PiBS | 49 % |

- **Bis Sommer 2027 geht es nicht** – höchstens 0,5 %, und das ist
  beweisbar (Abschnitt 1).
- **Nicht verhandelbar:** die Sparregel (Abschnitt 4) und Märkte, die nicht
  30 Jahre lang schwach bleiben.
- **Unter 50 % am Zieldatum** liegt der Plan, wenn zu den pessimistischen
  Schätzungen der KI-Druck sicher dazukommt (46 %) oder die Schweiz ganz
  wegfällt (49 %). Diese Fälle erreichen die 50 % mit 58–59, also ein bis
  zwei Jahre später. Alle Härtefälle stehen in Abschnitt 7 – das sind
  Einordnungen, keine anderen Ziele.
- **Jede Quelle mit Link** steht in Abschnitt 10. 42 Zahlen wurden einzeln
  gegen die Originalquelle geprüft; wo die Quelle etwas anderes sagt, sind
  Text und Modell korrigiert (Einstiegsgehalt, Kaufnebenkosten,
  Sozialabgaben, Aufstieg im Vertrieb). Dadurch sank die Hauptzahl von 60 %
  auf 57 %.
- Die Zahlen haben drei Runden Gegenprüfung durch zehn unabhängige Prüfer
  und mehrere unabhängige Nachrechnungen überstanden; dabei wurde die erste
  Aussage „50 % mit 40“ auf diese Werte korrigiert.

Gemessen wird 1 Mio. € **nominal**, nach der Steuer, die beim Verkauf der
ETFs fällig würde, ohne Erbschaft, ohne Vermögen eines Partners. In heutiger
Kaufkraft sind 1 Mio. € am 31.08.2065 nur etwa **440 Tsd. €** (bei 2,1 %
Inflation im Jahr). Wer 1 Mio. € in heutiger Kaufkraft will: Diese Quote
liegt am Zieldatum bei rund 24 %, mit 60 bei 30 %.

Alles lässt sich nachrechnen: `python3 plan/simulation.py` und
`python3 plan/simulation.py --stress` (Tests:
`python3 -m unittest discover -s tests`).

**Zur Person:** Gerechnet ist für dich als Schüler der 13. Klasse mit Abitur
im Frühjahr 2027, also 19 Jahre alt im Sommer 2027. Bist du ein Jahr älter,
bleibt das Zieldatum der 31.08.2065, du bist dann nur 58 statt 57.

---

## 1. Warum nicht bis Sommer 2027 – beweisbar

Für jedes Spiel mit Erwartungswert null oder negativ (Roulette, Lotto,
Sportwetten, Daytrading, CFDs, Optionen, Krypto-Zocken) gilt für **jede**
Strategie, solange das Vermögen nicht unter null fallen kann (also ohne
Kredit): Die Chance, aus S Euro jemals Z Euro zu machen, ist höchstens S / Z
(Ville-Ungleichung für nichtnegative Supermartingale). Mit 5.000 €
Startkapital sind das **0,5 %**.

| Weg bis 31.08.2027, Start 5.000 € | Chance auf 1 Mio. € |
|---|---:|
| Obergrenze für jede Strategie bei fairem Spiel | 0,50 % |
| Roulette, beste Strategie ohne Tischlimit (kühnes Spiel, Dubins & Savage) | 0,40 % |
| Welt-ETF mit 1-, 3- oder 10-fachem Hebel | 0,000 % |
| Beste Strategie für ein Vermögensziel bis zu einer Frist, mit Aktien-Drift (Browne 1999) | ≈ 1,1–1,4 % |

In der Praxis verlieren 74–89 % der CFD-Konten von Privatkunden (ESMA 2018)
und 74 % der Turbo-Anleger (BaFin, 2019–2023) Geld. Und ein Geschäft? 1 Mio. € netto in
acht Monaten wären rund 1,8 Mio. € Gewinn – neben dem Abitur.

## 2. Was die Recherche gezeigt hat

| Befund | Quelle |
|---|---|
| Nur ~1,5 % der Erwachsenen haben ≥ 1 Mio. €; 77 % davon sind 50+ | DIW 2020 |
| 73 % der erwerbstätigen Millionäre sind selbstständig, 80 % davon mit Personal | DIW 2020 |
| Selbst das oberste Einkommenszehntel hat im Median nur 650 Tsd. € | Bundesbank PHF 2023 |
| Nur 38 % der Gründungen überleben 5 Jahre (ohne Beschäftigte 34 %) | IfM Bonn |
| Vollzeit-Web-Agenturen im Jahr 3–5: nur 21 % zahlen sich ≥ 50 Tsd. US-$ aus (16 von 76) | Admin Bar 2026 (Rohdaten, n = 622, eigene Auswertung) |
| Angestellte Entwickler DE: Median ~50 Tsd. € (1–3 J.), 66 Tsd. (5–8 J.), 78 Tsd. (10–13 J.) | Stack Overflow 2024+25 (Rohdaten, n ≈ 4.250, eigene Auswertung) |
| Einstiegsgehalt Informatik mit Bachelor: 42,4–49,4 Tsd. €, typisch 46,3 Tsd. | get in IT 2026; Stepstone 2026: ~43,7 Tsd. |
| IT-Freelancer Software/Web: 91 €/h; abgerechnete Tage stark gestreut (24 % unter 50, ~⅓ über 200); 80 % aller Befragten mit > 10 J. Praxis | Freelancer-Kompass 2026 |
| SaaS-Vertrieb: nur 22 % der SDR-Starter werden AE (je nach Segment 32–46,5 %); 26 % der Beförderten bleiben höchstens 6 Monate | UNIFY 2026, Bridge Group 2017 |
| Schweizer ICT, Neueinstellung Junior-Stufe: ~80 Tsd. CHF (2026); FH-Bachelor-Einstieg Median 81.850 CHF (2025) | swissICT-Salärstudien 2025/2026 |
| 45 % der EU/EFTA-Zuwanderer verlassen die Schweiz binnen 10 Jahren wieder | SECO 2026 |
| Firmenkauf (Search Funds): 26–31 % Verlust-Deals, außerhalb USA/Kanada Median-IRR 9 % | Stanford 2024, IESE 2024, Yale 2026 |
| Oberstes Einkommenszehntel spart 20 % des Nettos | DIW/SOEP 2025 |
| Haushalte mit 5–10 Tsd. € netto im Monat: von jedem zusätzlichen Euro 37 % gespart, 59 % nicht konsumiert | EVS 2018 (eigene Herleitung) |
| Einsteiger (22–25 J.) in stark KI-exponierten Berufen: Beschäftigung ~19 % unter der Vergleichsgruppe | Stanford Digital Economy Lab, Juni 2026 |
| Sozialabgaben gesamt: 42,7 % (2026) → 50 % (2035, Basisszenario; günstig 47 %) | IGES für die DAK 2026 |

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
4 × 10.000 simulierte Leben je Weg, Intervall ±0,5 Prozentpunkte. Die
Eingaben stehen mit Quelle in Abschnitt 7 und 10.

| Weg | mit 40 | mit 45 | mit 50 | mit 55 | **am Zieldatum (57)** | mit 60 | 50 % ab |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Plan: PiBS > dual > Bachelor, dann Schweiz/DE** | 9 % | 22 % | 36 % | 52 % | **57 %** | 64 % | **55** |
| … mit eiserner Sparregel (60 %) | 14 % | 30 % | 47 % | 63 % | 69 % | 75 % | 51 |
| … mit typischem Elternerbe (nicht Teil des Plans) | 9 % | 22 % | 37 % | 55 % | 62 % | 71 % | 54 |
| Duales Studium, dann Schweiz/DE | 9 % | 21 % | 36 % | 51 % | 57 % | 65 % | 55 |
| Sicherer PiBS-Platz, dann Schweiz/DE | 10 % | 24 % | 38 % | 53 % | 58 % | 65 % | 54–55 |
| Bachelor + Agentur, dann Schweiz/DE | 8 % | 19 % | 33 % | 48 % | 54 % | 62 % | 56 |
| Plan, aber ohne Schweiz (außer über PiBS) | 4 % | 13 % | 28 % | 44 % | 51 % | 59 % | 57 |
| Bachelor + Agentur, nur Deutschland | 3 % | 10 % | 24 % | 40 % | 47 % | 56 % | 58–59 |
| Plan, aber spart wie typische Gutverdiener | 4 % | 12 % | 23 % | 35 % | 41 % | 48 % | 61 |
| Bachelor + Agentur, Schweiz/DE + Firmenkauf | 10 % | 20 % | 29 % | 38 % | 42 % | 47 % | 62 |
| Vertrieb (SaaS) ab 2027 | 2 % | 7 % | 14 % | 25 % | 30 % | 38 % | 65 |
| 2 Jahre Agentur Vollzeit, dann Vertrieb | 2 % | 7 % | 16 % | 27 % | 33 % | 41 % | 64 |

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
- **Software-Wette, Creator, E-Commerce:** Von gut 10.000 gelisteten
  Indie-Produkten hatte nur knapp die Hälfte im Monat überhaupt Umsatz, und
  davon lag der Median bei 169 USD (TrustMRR); nur ~4 % der Creator
  verdienen > 100 Tsd. USD im Jahr. Als Nebenoption ok.
- **Immobilien mit Kredit:** Bauzins ~4,3 % (10 Jahre) gegen eine
  Bruttomietrendite von 3,4 % in den sieben größten Städten bzw. 4,2 % im
  Schnitt der 52 größten – vor Instandhaltung, Leerstand und Kaufnebenkosten
  bleibt mit Kredit kein Hebel.
- **Trading, Krypto, Hebel:** siehe Abschnitt 1.

Neu getestet: das **praxisintegrierte Bachelorstudium (PiBS) in der
Schweiz** (4 Jahre FH, 40 % Arbeit im Schweizer Partnerbetrieb). Ergebnis:
mit Platz leicht besser als das duale Studium, aber die Plätze sind knapp
(2022 erst 128 Eintritte schweizweit; laut Bund sind die Plätze in
Unternehmen das Nadelöhr) und der Lohn deckt die Schweizer Lebenshaltung
nicht. Darum steht es im Plan als erste Wahl *wenn* ein Platz
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
  (Kaufnebenkosten 5–12 % je nach Bundesland und Makler sind sofort weg).

### Phase 3 – ~2040 bis 31.08.2065: Durchhalten

- Weiter sparen, nie verkaufen in Crashs, kein Market-Timing.
- Jedes Jahr die Kontrollwerte (Abschnitt 6) prüfen und nachsteuern.

### Die Sparregel – der wichtigste Teil

> **Grundbedarf:** ~1.500 €/Monat in Deutschland bzw. ~3.200 €/Monat in der
> Schweiz (inkl. Krankenkasse), jedes Jahr um die Inflation angehoben.
> **Von jedem Euro darüber gehen 60 % per Dauerauftrag am Zahltag ins
> ETF-Depot** – auch von jeder Gehaltserhöhung, jedem Bonus.

Das ist etwa doppelt so viel, wie typische Gutverdiener sparen. Genau
deshalb ist es Regel und Dauerauftrag, nicht Vorsatz. Die Hauptzahl dieses
Plans (57 % am 31.08.2065) rechnet bewusst damit, dass die Regel nicht
perfekt hält: im Mittel werden nur ~50 % gespart, und 15 % der Leben werden
irgendwann halbherzig. Wer sie wirklich hält, hat am Zieldatum **69 %**; wer
nur so spart wie typische Gutverdiener, **41 %** – dann trägt der Plan nicht.

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
- **Gewinn 2027 unter ~7.080 € halten** (ein Siebtel der Bezugsgröße 2027,
  590 € im Monat; Rechengrößen 2027 noch Entwurf) – darüber endet die
  Familienversicherung, die eigene Kranken- und Pflegeversicherung kostet
  dann mindestens ~3.400 € im Jahr.
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
| 25 | 10 Tsd. € | 22 Tsd. € | 38 Tsd. € |
| 30 | 55 Tsd. € | 99 Tsd. € | 165 Tsd. € |
| 35 | 117 Tsd. € | 209 Tsd. € | 352 Tsd. € |
| 40 | 175 Tsd. € | 325 Tsd. € | 583 Tsd. € |
| 45 | 247 Tsd. € | 494 Tsd. € | 912 Tsd. € |
| 50 | 348 Tsd. € | 719 Tsd. € | 1,35 Mio. € |
| 55 | 504 Tsd. € | 1,04 Mio. € | 1,98 Mio. € |

## 7. Was den Plan kippt – und was nicht

Jeweils genau ein Faktor auf seinem schlechten bzw. guten Rand, alle anderen
bleiben unsicher (4 × 10.000 Leben). Basis: **57 %** am 31.08.2065,
50 % ab 55.

| Faktor (schlecht / gut) | Chance am 31.08.2065 | 50-%-Alter |
|---|---:|---:|
| Sparverhalten (typisch / eiserne Regel) | 41 % / 69 % | 61 / 51 |
| Aktienrendite (4 % / 8 % im Jahr) | 45 % / 70 % | 59–60 / 51 |
| Grundbedarf (22 / 13 Tsd. € im Jahr) | 49 % / 69 % | 58 / 51 |
| KI-Druck auf Einsteiger (sicher / nie) | 51 % / 60 % | 57 / 54 |
| Schweizer Stelle (nie / sicher) | 54 % / 63 % | 56 / 52–53 |
| Kinder (sicher und teuer / keine) | 55 % / 64 % | 56 / 53 |
| Dualer Studienplatz (nie / sicher) | 55 % / 59 % | 56 / 54–55 |
| Rückkehr aus der Schweiz (4 %/Jahr / nie) | 57 % / 63 % | 55 / 52–53 |

**Was du selbst in der Hand hast, wirkt am stärksten:** Sparregel und
Grundbedarf. Fällt einer der beiden schlecht aus, liegt das Zieldatum unter
50 % – darum sind sie Regeln mit Dauerauftrag, keine Vorsätze. Die Börse
kannst du nicht steuern – nur aushalten.

**Stresstest** (`python3 plan/simulation.py --stress`): Alle Annahmen ohne
harte Quelle gleichzeitig am pessimistischen Rand – Chance auf eine Schweizer
Stelle halbiert (auch im zweiten Anlauf), nach PiBS deutlich seltener,
PiBS-Platz kaum, dualer Platz seltener, Rückkehr aus der Schweiz über dem
SECO-Wert für alle EU/EFTA-Zuwanderer.

| Szenario | mit 54 | mit 56 | **mit 57** | mit 60 | mit 64 | mit 65 |
|---|---:|---:|---:|---:|---:|---:|
| Plan (Basis) | 48 % | 54 % | **57 %** | 65 % | 73 % | 75 % |
| Stress: alle Schätzungen pessimistisch | 41 % | 48 % | **51 %**¹ | 59 % | 69 % | 71 % |
| Stress + KI-Druck sicher | 37 % | 43 % | **46 %** | 55 % | 65 % | 67 % |

¹ Nachgemessen über 16 Läufe à 10.000 Leben: 51,2 % ± 0,2 – knapp, aber
über 50 %. Basis im selben Lauf: 56,9 % ± 0,2.

Das Planziel bleibt **der 31. August 2065**. Die früheste Marke mit
mindestens 50 % liegt bei 55 (Sommer 2063, 51,6 %); das Zieldatum zwei
Jahre später hält die 50 % auch dann, wenn alle drei unsicheren Annahmen
gleichzeitig danebenliegen – knapp. Kommt zusätzlich der KI-Druck sicher,
reicht es am Zieldatum nicht (46 %); dann wird die 50-%-Marke mit 59
erreicht. Die Jahre 2068 und 2072 in der folgenden Tabelle zeigen nur, ab
wann auch noch härtere Fälle über 50 % liegen.

**Härtefälle bis zum Äußersten** (`python3 plan/simulation.py --stress`,
4 × 10.000 Leben). „Äußere Kleinannahmen pessimistisch“: kein Freelancing,
harte Lohnnarbe nach Arbeitslosigkeit, träger Konsum, keine weiterlaufenden
Betreuungsverträge.

| Szenario | mit 57 (2065) | mit 60 (2068) | mit 64 (2072) | 50 % ab |
|---|---:|---:|---:|---:|
| Plan (Basis) | 57 % | 65 % | 73 % | 55 |
| äußere Kleinannahmen pessimistisch | 50 % | 57 % | 66 % | 57–58 |
| + die drei großen Annahmen ohne Quelle pessimistisch | 43 % | 51 % | 61 % | 60 |
| ganz ohne Schweiz und PiBS | 49 % | 58 % | 68 % | 58 |
| ohne Schweiz, PiBS, dualen Platz, KI-Druck sicher | 43 % | 52 % | 62 % | 60 |
| … + äußere Kleinannahmen pessimistisch | 33 % | 42 % | **52 %** | **64** |
| … und die Regeln des Plans eisern gehalten (kein Hauskauf, nie aufgeben) | 38 % | 47 % | 57 % | 62 |

Die Schweiz und die Studienform machen die Million **früher** erreichbar.
Ohne sie trägt der Plan ab 2068 über 50 %, solange nicht zusätzlich alles
Äußere schiefgeht – dann mit eiserner Regeltreue ab 2070 (52 %) und **ab
Sommer 2072 auch ohne** (52 %): Das ist der härteste Fall, der hier getestet
wurde. Was nicht verhandelbar bleibt: die Sparregel (bei Sparen wie
typische Gutverdiener im härtesten Fall: 33 % mit 60) und Märkte, die nicht
30 Jahre lang nur 4 % liefern (dann: 38 %).

**Welche Eingaben im härtesten Fall noch wirken – und woher sie stammen**
(der härteste Fall: ohne Schweiz, PiBS, dualen Platz, KI-Druck sicher;
Links in Abschnitt 10):

| Eingabe | Wert im Modell | Quelle |
|---|---|---|
| Schweizer Stelle, PiBS-Platz, dualer Platz | **0** (abgeschaltet) | – |
| Einstiegsgehalt IT mit Bachelor | 43–50 Tsd. € (Mitte 46,3), ×0,92 KI-Abschlag | get in IT 2026 (42,4–49,4, typisch 46,3), Stepstone 2026 (~43,7) |
| Gehaltsverlauf IT | real +2,5–7,5 % je Jahr (Mitte 4,2 %) bis Jahr 10, danach 0–2 %; ergibt Median ~51 / 63 / 74 Tsd. nach 1–3 / 5–8 / 10–13 J., mit KI-Abschlag ~47 / 58 / 69 | liegt bewusst etwas unter Stack Overflow DE 2024+25 (Median ~50 / 66 / 78 Tsd., n ≈ 4.250) |
| Steuern, Sozialabgaben | Tarif 2026, BBG 2026, Arbeitnehmeranteil +3,65 Pp. bis 2035 | § 32a EStG, Rechengrößen 2026, IGES für die DAK 2026 (42,7 % → 50 %) |
| Studienabbruch Bachelor Informatik | 35–50 % | DZHW 2022 (Uni 42–47 %, HAW 30–37 %) |
| Arbeitslosigkeit, Krisen | 2–5 % je Jahr, in Krisen 5–18 % | IAB 1998–2019: Akademiker 2,0–4,1 % (Modell bewusst darüber) |
| Kinder, Partnerschaft, Scheidung | eigener Anteil 5–12 Tsd. €/Jahr je Kind (Hälfte der Kosten nach Kindergeld), Väter beim 1. Kind 33,3, 28 % Scheidungen | EVS 2018 (424–1.212 €/Monat je Kind nach Einkommen), Destatis 2025 |
| Kaufnebenkosten Haus | 5,5–12 % | Grunderwerbsteuer 3,5–6,5 %, Notar/Grundbuch ~2 %, Makler bis 3,57 % |
| Sparverhalten | 38–62 % jedes Euros über dem Grundbedarf | EVS 2018 (37 % gespart bzw. 59 % nicht konsumiert bei 5–10 Tsd. € netto), DIW/SOEP 2025 |
| Aktienrendite | 3,5–8 % geometrisch, Vola 13–18 %, dicke Ränder | MSCI World Net seit Ende 2000: 6,7 %; Prognosen Vanguard/Morningstar 5–7 % nominal |
| Steuer beim Verkauf | 18,46 % auf ETF-Gewinne | § 20 InvStG, § 32d EStG |

Ebenfalls wirksam, aber **geschätzt** (ohne harte Quelle): Grundbedarf
15–22 Tsd. € (aus WG-Mieten abgeleitet), Inflation 1,5–3 %, Gehalt ohne
Abschluss 36–50 Tsd. €, Vorsprung des dualen Studiums beim Einstieg
(~1 Tsd. €), Agentur während des Bachelors, Freelancing (Chance 30–60 %),
Hauskauf trotz Rat (20–40 %), Aufgeben der Sparregel (15 %),
Konsumträgheit, Lebensstil mit Partner, Lohnnarbe 2–8 %, Berufsunfähigkeit
0,1–0,2 % je Jahr, KI-Szenario. Wie stark sie zusammen wirken, zeigt die
Härtefall-Tabelle oben.

**Gegenrechnung ohne Simulation** (unabhängiger Prüfer, typischer Lebensweg
im härtesten Fall: Bachelor, IT-Stelle in Deutschland ab 46 Tsd. € real,
Sparregel, Kinder, BU-Prämie; gerechnet mit Abgaben +3 statt jetzt +3,65
Pp., das macht rund 2 % weniger): Depot mit 60, nominal nach Steuer

| Rendite im Jahr | mit Abschluss | ohne Abschluss (42 % der Leben) |
|---|---:|---:|
| 8,6 % (MSCI-World-Sparplan, Durchschnitt laut DAI) | 2,65 Mio. € | 2,26 Mio. € |
| 6 % | 1,57 Mio. € | 1,31 Mio. € |
| 4 % | 1,11 Mio. € | 0,91 Mio. € |

Für die Million reichen mit Abschluss 3,4 % Rendite. Die Simulation liegt im
Median bei 1,03 Mio. € – niedriger als die Gegenrechnung, weil sie
schwankende Märkte, Arbeitslosigkeit, Abbrüche und Hauskäufe mitnimmt.

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
   *Die folgenden Prüfberichte beziehen sich auf frühere Commits, also auf
   die Zahlen vor der Quellenprüfung (Punkt 4).*
   **Schlussverifikation** auf dem gepushten Stand (frischer Checkout, alle
   Tests grün): 8 von 8 unabhängigen Läufen (Seeds 2027/1/2/3 und
   101/202/303/404, je 10.000 Leben) liefern das 50-%-Alter 54;
   P(54) = 51,9 % bzw. 52,1 %, untere Intervallgrenze jeweils über 51,4 %
   (seit dem Horizont bis 65, wegen anderer Zufallsfolge: 51,6 %).
   Ein vierter unabhängiger Prüfer hat Commit e6d0f7c geprüft: Zahlen und
   Kalenderjahre stimmig; seine Kritik, dass im härtesten Fall noch weitere
   geschätzte Eingaben wirken, ist in die Härtefall-Tabelle eingeflossen.
   Ein dritter unabhängiger Prüfer hat Commit 878be02 (Härtefälle) im
   frischen Klon geprüft: 92 Tests grün, härtester Fall mit 60 bei
   56,0–56,3 % (12 Seeds), in diesem Fall kommen Schweiz, PiBS und dual
   nachweislich nie vor; dazu die Gegenrechnung ohne Simulation (Abschnitt 7).
   Ein zweiter, unabhängiger Prüfer hat Commit 065359f in einem frischen
   Klon mit eigenen Seeds nachgerechnet: alle Dokumentzahlen innerhalb ±1
   Prozentpunkt; Planziel 2065: Basis 60,3 %, Stress 55,5 %, Stress + KI
   50,6 % (je 160.000 Leben).
   Die Unsicherheit der geschätzten Spannen (Schweizer Stelle, PiBS-Platz,
   Rückkehrrate) steckt bereits in diesen Zahlen, weil jedes Leben seine
   Werte aus der ganzen Spanne zieht; im ungünstigsten Einzelfall (nie eine
   Schweizer Stelle) verschiebt sich die Schwelle auf 55.
4. **Quellenprüfung (22.11.2026):** 42 Zahlen einzeln gegen die
   Originalquelle geprüft (Abschnitt 10): 24 bestätigt, 18 präzisiert oder
   korrigiert; eine unabhängige Gegenprobe von 8 bestätigten Belegen fand
   keinen Fehler. Im Modell geändert, weil die Quelle es verlangte:
   Einstiegsgehalt Bachelor 43–50 statt 44–58 Tsd. € (get in IT),
   Kaufnebenkosten 5,5–12 statt 5–9 %, Sozialabgaben +3,65 statt +3
   Punkte (neue IGES-Projektion), Aufstieg im Vertrieb 22–46 % statt
   35–55 % (UNIFY). Ergebnis: Plan am 31.08.2065 **57 %** statt 60 %, Stress
   51 % statt 56 %. Ein Test prüft seitdem bei jedem Lauf, dass Zieldatum
   und Kopfzahlen dieses Dokuments zum Code passen.
5. **Grenzen:** Viele Spannen sind begründete Schätzungen (Chance auf
   Schweizer Stelle, PiBS-Platz, Rückkehrrate, KI-Szenario). Bewusst nicht in
   der Hauptzahl: Erbschaften (mit typischem Elternerbe ~1 Jahr früher), das
   Vermögen eines Partners (als Paar mit Zugewinngemeinschaft gezählt ~1–2
   Jahre früher), die Pensionskasse voll statt halb (~1 Jahr früher),
   Kirchensteuer (bei Mitgliedschaft etwas später). Wer eigene Ist-Werte hat,
   trägt sie in `plan/simulation.py` ein und rechnet neu.

## 10. Quellenverzeichnis

Jede Zahl unten wurde am 22.11.2026 einzeln gegen die verlinkte
Originalquelle geprüft (acht Prüfer je Themengruppe, danach eine
unabhängige Gegenprobe von 8 der bestätigten Belege: alle 8 halten). Wo die
Quelle etwas anderes sagte als die frühere Fassung dieses Plans, steht hier
der korrigierte Wert, und der Plan rechnet damit.

**Vermögen und Millionäre**

- DIW Wochenbericht 29/2020, „MillionärInnen unter dem Mikroskop“: 1,5 %
  der Erwachsenen mit ≥ 1 Mio. € (S. 512); Altersanteile 37 % (50–64) +
  40 % (65+) = 77 % (Tab. 4, S. 520); 73 % Selbstständige, davon 80 % mit
  Mitarbeitenden (S. 517).
  <https://www.diw.de/documents/publikationen/73/diw_01.c.793783.de/20-29.pdf>
- Bundesbank, PHF 2023, Tabellenanhang (Tab. 2, Zeile Bruttoeinkommen
  90–100 %): Median-Nettovermögen 649.700 €.
  <https://publikationen.bundesbank.de/caas/v1/media/955436/data/dbdce1fbc3b7f0ac7fc8b3727c17112a>

**Glücksspiel, Trading, Märkte**

- Ville-Ungleichung für nichtnegative Supermartingale: Howard, Ramdas,
  McAuliffe, Sekhon (2020), Probability Surveys 17, Lemma 1,
  DOI 10.1214/18-PS321. <https://arxiv.org/pdf/1808.03204>
- Kühnes Spiel bei unfairem Rot-Schwarz ohne Tischlimit optimal: Dubins &
  Savage, *How to Gamble If You Must* (1965); mit Tischlimit nicht
  allgemein optimal (J. Appl. Probab.):
  <https://www.cambridge.org/core/journals/journal-of-applied-probability/article/on-nonoptimality-of-bold-play-for-subfair-redandblack-with-a-rationalvalued-house-limit/E791145FB807C402EB90DC1B5C6DD4A2>
- Browne (1999), „Reaching goals by a deadline“, Adv. Appl. Probab. 31(2),
  DOI 10.1239/aap/1029955147.
  <https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/reaching-goals-by-a-deadline-digital-options-and-continuoustime-active-portfolio-management/73CD9DEE7FCCD733988A72AFCE62573A>
- ESMA, Pressemitteilung ESMA71-98-128 (27.03.2018), S. 2: in 74–89 % der
  CFD-Kleinanlegerkonten Verluste.
  <https://www.esma.europa.eu/sites/default/files/library/esma71-98-128_press_release_product_intervention_de.pdf>
- BaFin, Studie Turbo-Zertifikate (21.05.2025): 74,2 % der Privatanleger
  mit Verlust, 2019–2023.
  <https://www.bafin.de/SharedDocs/Veroeffentlichungen/DE/Fachartikel/2025/Studie_250521_Turbo_Zertifikate.html>
- MSCI World (EUR) Net, Factsheet 30.10.2026: 6,68 % p. a. seit 29.12.2000.
  <https://www.msci.com/documents/10199/890dd84d-3750-4656-87f2-1229ed5a5d6e>
- Deutsches Aktieninstitut, MSCI-World-Rendite-Dreieck Sparplan (Stand
  31.12.2025): 20-jährige Sparpläne im Schnitt 8,6 % p. a. (vor Kosten und
  Steuern).
  <https://www.dai.de/fileadmin/user_upload/251231_MSCI_World-Rendite-Dreick_50_Jahre_Sparplan_Web.pdf>
- Vanguard, Renditeprognosen 10 Jahre (30.09.2026): USA 4,8–6,8 %,
  Industrieländer ex USA 5,3–7,3 %.
  <https://corporate.vanguard.com/content/corporatesite/us/en/corp/vemo/vemo-return-forecasts.html>
  – Morningstar (2026): USA 5,3 %, Industrieländer ex USA 7,5 %.
  <https://www.morningstar.com/markets/experts-forecast-stock-bond-returns-2026-edition>
- Bauzins 10 Jahre 4,3 % (Interhyp, 12.11.2026):
  <https://www.interhyp.de/ratgeber/was-muss-ich-wissen/zinsen/zins-charts/>
  – Bruttomietrendite 4,17 % im Schnitt der 52 größten Städte (H1 2026),
  Top-7 ~3,4 % (Baufi24):
  <https://www.baufi24.de/presse/pressemitteilungen/mietrendite-trend-082026/>
- Kaufnebenkosten: Grunderwerbsteuer 3,5–6,5 %, Notar/Grundbuch 1,5–2 %,
  Makler bis 3,57 % (Baufi24). <https://www.baufi24.de/nebenkosten-hauskauf/>

**Gründung, Agentur, Produkte**

- IfM Bonn, Überlebensrate (Kohorte 2017): nach 5 Jahren 38,1 %, ohne
  Beschäftigte 33,7 %.
  <https://www.ifm-bonn.org/statistiken/gruendungen-und-unternehmensschliessungen/ueberlebensrate-von-unternehmen>
- The Admin Bar, 2026 WordPress Agency Survey, Rohdaten (622 Zeilen); eigene
  Auswertung: Vollzeit, 3–5 Jahre im Geschäft: 16 von 76 zahlen sich
  ≥ 50 Tsd. US-$ (21 %).
  <https://theadminbar.com/wp-content/uploads/2026/03/The-Admin-Bar-2026-WordPress-Agency-Survey-results.csv>
- Eurostat isoc_ciweb, DE, 0–9 Beschäftigte, 2023: 65,0 % mit Website.
  <https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_ciweb?geo=DE&indic_is=E_WEB&unit=PC_ENT&size_emp=0-9&size_emp=0_1&size_emp=2-9&size_emp=GE10&time=2023&time=2025&lang=EN>
- Indie-Produkte (TrustMRR-Datensatz, 10.150 Produkte): Median-Umsatz der
  4.987 Produkte mit Umsatz 169 US-$ in 30 Tagen (TechStartups, 28.09.2026).
  <https://techstartups.com/2026/09/28/what-percentage-of-indie-hacker-products-make-100k-in-arr/>
- Creator: 4,3 % verdienen > 100 Tsd. US-$ im Jahr (Aspire-Umfrage,
  > 1.700 Creator; Marketing Brew 2022).
  <https://www.marketingbrew.com/stories/2022/09/28/only-4-3-of-creators-make-over-usd100k-per-year-survey-reveals>
- § 3 Abs. 3 BFSG: Ausnahme für Kleinstunternehmen mit Dienstleistungen.
  <https://www.gesetze-im-internet.de/bfsg/__3.html>
- Search Funds: Stanford GSB 2024 Search Fund Study, Figure I: 31 %
  Verlust (USA/Kanada)
  <https://cdn.prod.website-files.com/6455268783d6938b9451ea80/669fbcb3e5f07cc9a6093751_StanfordGSB_Study_2024.pdf>;
  IESE 2024, international: 26 % Verlust
  <https://iese.edu/media/research/pdfs/ST-0658-E>; Yale SOM (2026):
  Median-IRR außerhalb USA/Kanada 9 %
  <https://som.yale.edu/sites/default/files/2026-02/A-Detailed-Analysis-of-ETA-CEO-Demographics-and-Financial-Outcomes.pdf>

**Gehälter und Karriere**

- get in IT, Einstiegsgehalt Informatik 2026: Bachelor 42.400–49.400 €,
  typisch 46.300 €. <https://www.get-in-it.de/magazin/gehalt/statistik>
  – Stepstone, Informatiker/in: Einstieg ~43.700 €.
  <https://www.stepstone.de/gehalt/Informatiker-in.html>
- Stack Overflow Developer Survey 2024 und 2025, Rohdaten; eigene
  Auswertung (Deutschland, angestellt, Gehalt in EUR, Erfahrung = WorkExp):
  Median ~50 / 66 / 78 Tsd. € nach 1–3 / 5–8 / 10–13 Jahren, n ≈ 4.250.
  <https://media.githubusercontent.com/media/StackExchange/Survey/main/packages/archive/2025/results.csv>
  (2024: dieselbe Adresse mit `2024`)
- Freelancer-Kompass 2026 (5.412 Befragte): Software/Web 91 €/h (S. 34/35);
  80 % aller Befragten > 10 Jahre Praxis (S. 9); fakturierte Tage nur als
  Verteilung (S. 15).
  <https://www.freelancermap.de/files/survey/freelancer-kompass-2026.pdf>
- UNIFY, „The Path to AE“ (2026): 22,3 % aller SDR-Starter erreichen AE,
  32,0 % bei kleineren Software-Firmen, 46,5 % bei großen KI-Firmen.
  <https://www.unifygtm.com/the-jump/report/the-path-to-ae>
  – Bridge Group (2017): 26 % von 205 beförderten SDRs nach ≤ 6 Monaten als
  AE gescheitert.
  <https://blog.bridgegroupinc.com/failure-rate-of-sdr-to-ae-promotions>
- Stanford Digital Economy Lab, Update „Canaries in the Coal Mine“
  (12.08.2026): 22–25-Jährige in stark KI-exponierten Berufen ~19 % unter
  dem Verlauf weniger exponierter Berufe (relativ, deskriptiv).
  <https://digitaleconomy.stanford.edu/news/canariesaug26/>
- IAB, Qualifikationsspezifische Arbeitslosenquoten 1998–2019: mit
  Hochschulabschluss 2,0–4,1 %.
  <https://doku.iab.de/arbeitsmarktdaten/Qualo_2020.pdf>

**Schweiz und Studium**

- swissICT-Salärstudie 2025: FH-Bachelor-Einstieg Median 81.850 CHF
  <https://www.netzwoche.ch/news/2025-09-03/so-entwickeln-sich-die-loehne-der-ict-branche>;
  Salärstudie 2026: Junior-Neueinstellungen ~80.000 CHF
  <https://www.netzwoche.ch/news/2026-08-26/ict-loehne-legen-kaum-noch-zu>
- SECO, 22. Observatoriumsbericht FZA (25.06.2026), S. 9: 45 % der
  EU/EFTA-Zuwanderer nach 10 Jahren wieder ausgewandert.
  <https://www.seco.admin.ch/dam/de/sd-web/OApVoo89AUQX/22.%20Observatoriumsbericht%20zum%20FZA_SECO_2026_DE.pdf>
- PiBS: 4 Jahre, 40 % Praxis (ZHAW)
  <https://www.zhaw.ch/de/engineering/studium/bachelorstudium/praxisintegriertes-bachelorstudium>;
  ebenso FHNW <https://www.fhnw.ch/de/studium/informatik-technik-umwelt/pibs-studium>
- WBF, Erläuternder Bericht HFKG (04.09.2024), Kap. 1.4: 2022 128
  PiBS-Eintritte; „die Plätze in Unternehmen [sind] das Nadelöhr“.
  <https://www.demokratis.ch/consultazione/5ztwr23j/file/1CEuUTfmanXXY484JhnK4J/embed>
- DHBW Studienverlaufspanel 2/2018, S. 15: Abbruchquote Fakultät Technik
  (dort liegt Informatik) 18,1 %, DHBW gesamt 10–15 %.
  <https://www.dhbw.de/fileadmin/user_upload/Dokumente/Schrifterzeugnisse/Analyse_Studienabbrueche_DHBW_Stand_09.02.2018.pdf>
- DZHW Brief 05/2022, Anhang Tab. A1/A2: Studienabbruch Bachelor
  Informatik Uni 42–47 %, HAW 30–37 %.
  <https://www.dzhw.eu/pdf/pub_brief/dzhw_brief_05_2022_anhang.pdf>

**Sparen, Familie**

- DIW/SOEPv42 (2025): oberstes Einkommenszehntel spart 20 % des
  Haushaltsnettos.
  <https://www.diw.de/de/diw_01.c.1025503.de/einkommen_der_privathaushalte_steigen_wieder_____immer_mehr_menschen_sparen.html>
- Destatis, EVS 2018, Fachserie 15 Heft 4, Tab. 3.9–3.12: eigene
  Herleitung der Grenzsparquote zwischen 5–7,5 und 7,5–10 Tsd. € netto im
  Monat: 37 % (Ersparnis) bzw. 59 % (nicht konsumiert); in mittleren
  Klassen nur 7–26 %.
  <https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/DEHeft_derivate_00057921/2152604189004_korr19112020.pdf>
- Destatis, Konsumausgaben von Familien für Kinder (EVS 2018): Paare mit
  einem Kind im Schnitt 763 €/Monat, nach Einkommen 424–1.212 €.
  <https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/DEHeft_derivate_00061567/5632202189004.pdf>
- Destatis, Alter der Eltern 2025: Väter beim ersten Kind 33,3 Jahre
  (insgesamt 34,8).
  <https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Geburten/Tabellen/geburten-eltern-biologischesalter.html>
- Destatis, Maßzahlen Ehescheidungen: zusammengefasste Scheidungsziffer
  2025 284,3 je 1.000 Ehen (≈ 28 %).
  <https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Eheschliessungen-Ehescheidungen-Lebenspartnerschaften/Tabellen/masszahlen-ehescheidungen.html>

**Steuern, Abgaben, Recht**

- § 32a EStG (ab 2026): Grundfreibetrag 12.348 €, 42 % ab 69.879 €.
  <https://www.gesetze-im-internet.de/estg/__32a.html>
- § 3 SolzG: Freigrenze 20.350 €.
  <https://www.gesetze-im-internet.de/solzg_1995/__3.html>
- BMAS, Rechengrößen 2026: BBG KV/PV 69.750 €, RV/AV 101.400 €.
  <https://www.bmas.de/DE/Service/Gesetze-und-Gesetzesvorhaben/sozialversicherungs-rechengroessenverordnung-2026.html>
- BMAS, Rechengrößen 2027 (Entwurf): Bezugsgröße 4.130 €/Monat → ein
  Siebtel 590 € (Grenze der Familienversicherung nach § 10 SGB V).
  <https://www.bmas.de/DE/Service/Gesetze-und-Gesetzesvorhaben/sozialversicherungs-rechengroessenverordnung-2027.html>
- IGES für die DAK (2026), S. 22: Gesamtsozialversicherungsbeitrag 42,7 %
  (2026) → 50 % (2035, Basisszenario; günstig 47,0 %, ungünstig 53,7 %).
  <https://caas.content.dak.de/caas/v1/media/155742/data/002d8815de28a54c67bcc44e485ee16f/beitragsentwicklung-kurzbericht.pdf>
- § 20 InvStG (Teilfreistellung 30 %), § 32d EStG (25 %), § 4 SolzG
  (5,5 %) → 18,46 % auf ETF-Gewinne.
  <https://www.gesetze-im-internet.de/invstg_2018/__20.html>
- § 112 BGB <https://www.gesetze-im-internet.de/bgb/__112.html>,
  § 7 UWG <https://www.gesetze-im-internet.de/uwg_2004/__7.html>,
  § 19 UStG <https://www.gesetze-im-internet.de/ustg_1980/__19.html>
