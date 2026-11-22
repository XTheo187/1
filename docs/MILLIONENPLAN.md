# Der Millionenplan

**Frage:** Wie werde ich – heute in der 13. Klasse – mit mindestens 50 %
Wahrscheinlichkeit Millionär?

**Antwort:**

> **Festgelegtes Ziel: 1 Mio. € Nettovermögen am 31. August 2065
> (Alter ~57). Erfolgswahrscheinlichkeit mit diesem Plan: 51 %.**
> Dieses Datum ist das Planziel und wird nicht mehr verschoben.

Alle folgenden Zahlen gelten für **dasselbe Datum, 31.08.2065**:

| Fall | Chance auf 1 Mio. € am 31.08.2065 |
|---|---:|
| Plan, Sparregel realistisch nicht perfekt gehalten | **51 %** |
| Plan mit eiserner Sparregel (60 %, nie aufgegeben) | 65 % |
| die drei großen Schätzungen (Schweizer Stelle, Studienplatz, Rückkehrquote) gleichzeitig pessimistisch | 47 % |
| dazu KI-Druck auf Einsteiger sicher | 42 % |
| ganz ohne Schweiz und PiBS | 45 % |

**Ehrlich gesagt:** 51 % erfüllen die Forderung „mindestens 50 %“ – aber nur
knapp. Der Puffer liegt bei gut einem Punkt (über 16 Läufe 51,7 %), fast
jeder zweite Lebensweg verfehlt das Ziel am Stichtag, und **jeder einzelne**
der neun getesteten Faktoren drückt die Quote auf seinem ungünstigen Wert
unter 50 %: Sparen nur wie typische Gutverdiener (35 %), Aktien das ganze
Berufsleben über nur 4 % im Jahr (40 %), nie eine Schweizer Stelle (44 %),
Grundbedarf 22 statt ~18 Tsd. € (44 %), Kinder sicher und teuer (45 %),
KI-Druck sicher (46 %), Rückkehr aus der Schweiz deutlich über SECO (49 %),
kein dualer Platz (49,7 %), keine Schweizer Stelle im ersten Anlauf
(49,9 %); ebenso die drei großen Schätzungen zusammen (47 %). Diese Fälle
erreichen die 50 % mit 57–64. Der stärkste Hebel liegt bei dir: **Wer die
Sparregel wirklich hält, kommt auf 65 %** – darum ist sie der Kern des Plans.

- **Bis Sommer 2027 geht es nicht.** Mit Glücksspiel, Wetten oder Trading
  ohne Vorteil ist beweisbar höchstens 0,5 % drin; selbst die beste
  Hebelstrategie mit Aktien kommt theoretisch nur auf rund 1 % und ist in
  der Praxis chancenlos; ein Geschäft bräuchte ~1,9 Mio. € Gewinn neben dem
  Abitur (Abschnitt 1).
- **Nicht verhandelbar:** die Sparregel (Abschnitt 4) und Märkte, die nicht
  das ganze Berufsleben über schwach bleiben.
- Alle Härtefälle stehen in Abschnitt 7 – das sind Einordnungen, keine
  anderen Ziele. Im härtesten getesteten Fall, in dem Sparregel und Märkte
  noch halten, trägt der Plan auch mit 65 nicht (48 %).
- **Quellen:** Jede Quelle, auf der eine Zahl des Plans beruht, steht mit
  Link in Abschnitt 10; was nur geschätzt ist, steht dort und in Abschnitt 7
  als Schätzung. 42 Belege wurden einzeln gegen die Originalquelle geprüft,
  dazu 23 Angaben, die vorher nur im Code standen (10 bestätigt,
  11 korrigiert, 2 als Schätzung gekennzeichnet). Wo die Quelle etwas
  anderes sagt, sind Text und Modell korrigiert – unter anderem
  Einstiegsgehalt in Deutschland und in der Schweiz (jetzt um den
  swissICT-Median gelegt),
  Gehalt ohne Abschluss, Rückkehr aus der Schweiz (jetzt wie beim SECO),
  Berufsunfähigkeit (jetzt nach Alter), Sozialabgaben. Dadurch fiel die
  Hauptzahl von 60 % unter 50 % (48,8 %). Eine Änderung am Plan – Plan B
  ist ein Bachelor an einer FH statt an einer Uni (deutlich weniger
  Abbrüche, ~+1,2 Punkte) – und eine Änderung am Modell – die schon
  bestehende Abbruch-Regel (sofort neu starten) ist jetzt auch für den
  Bachelor eingerechnet (~+1,2 Punkte) – bringen sie auf 51 %. Ohne eine
  der beiden läge sie bei 50,0–50,3 %.
- Frühere Fassungen haben drei Runden Gegenprüfung durch zehn unabhängige
  Prüfer überstanden; dabei wurde die erste Aussage „50 % mit 40“
  korrigiert. Die fünf Werte der Kopftabelle und die Hauptzahl prüft ein
  Test bei jedem Lauf gegen die Simulation (±2 Punkte, 10.000 Leben); alle
  übrigen Zahlen erzeugen die Befehle direkt unter dieser Liste.

Gemessen wird 1 Mio. € **nominal**, nach der Steuer, die beim Verkauf der
ETFs fällig würde, ohne Erbschaft, ohne Vermögen eines Partners; eingerechnet
ist die Hälfte einer Schweizer Pensionskasse (sie lässt sich bei Rückkehr in
die EU nur teilweise auszahlen). In heutiger Kaufkraft sind 1 Mio. € am
31.08.2065 nur etwa **440 Tsd. €** (bei 2,1 % Inflation im Jahr). Wer
1 Mio. € in heutiger Kaufkraft will: Diese Quote liegt am Zieldatum bei rund
20 %, mit 60 bei 25 %.

Alles lässt sich nachrechnen (je 4 × 10.000 Leben, wie im Dokument):
`python3 plan/simulation.py` (Abschnitt 1 und 3, einige Minuten),
`--sommer` (Abschnitt 1 und 5), `--stress` (Stress- und Härtefälle),
`--sens` (Sensitivität), `--kontrolle` (Kontrollwerte), `--extra` (alle
übrigen Einzelzahlen, auch die 16-Lauf-Werte; nur der Median mit eiserner
Regel in Abschnitt 7 und der Agentur-Wert in Abschnitt 3 entstehen über
`sim.simulieren` bzw. `sim.kalibrierung_agentur()`); Tests:
`python3 -m unittest discover -s tests`. Alle Ergebnisse sind Modellwerte:
Die ±-Angaben sind nur das Rechenrauschen der Simulation – wie unsicher
die Annahmen sind, zeigt die Sensitivitätstabelle in Abschnitt 7.

**Zur Person:** Gerechnet ist für dich als Schüler der 13. Klasse mit Abitur
im Frühjahr 2027, also 19 Jahre alt im Sommer 2027. Bist du ein Jahr älter,
bleibt das Zieldatum der 31.08.2065, du bist dann nur 58 statt 57.

---

## 1. Warum nicht bis Sommer 2027 – und wo das beweisbar ist

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
gut neun Monaten wären rund 1,9 Mio. € Gewinn – neben dem Abitur. Für
Spiele ohne Vorteil ist die Grenze ein Beweis; für Aktien mit Hebel und für
ein Geschäft ist sie eine Rechnung, kein Beweis.

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
| Vertrieb (US-Daten, alle Branchen, ~180.000 SDRs, Start 2021–26): bis 07/2026 nur 22 % zum AE befördert (vorläufig); bei kleineren Software-Firmen 32 %, bei großen KI-Firmen 46,5 % (ausgewählte Branchen mit hoher Quote); 26 % der Beförderten bleiben höchstens 6 Monate | UNIFY 2026, Bridge Group 2017 |
| Schweizer ICT, Neueinstellung Junior-Stufe: ~80 Tsd. CHF (2026); FH-Bachelor-Einstieg Median 81.850 CHF (2025) | swissICT-Salärstudien 2025/2026 |
| 45 % der EU/EFTA-Zuwanderer verlassen die Schweiz binnen 10 Jahren wieder | SECO 2026 |
| Firmenkauf (Search Funds): 26–31 % Verlust-Deals, außerhalb USA/Kanada Median-IRR 9 % | Stanford 2024, IESE 2024, Yale 2026 |
| Oberstes Einkommenszehntel spart 20 % des Nettos | DIW/SOEP 2025 |
| Haushalte mit 5–10 Tsd. € netto im Monat: von jedem zusätzlichen Euro Netto 38 % gespart, 58 % nicht konsumiert | EVS 2018 (eigene Herleitung) |
| Einsteiger (22–25 J.) in stark KI-exponierten Berufen: Beschäftigung ~19 % unter der Vergleichsgruppe (USA, relativ) | Stanford Digital Economy Lab, 08/2026 (ADP-Lohndaten bis 06/2026) |
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
| **Plan: PiBS oder dual, sonst Bachelor; dann Schweiz/DE** | 7 % | 18 % | 31 % | 46 % | **51 %** | 59 % | **57** |
| … mit eiserner Sparregel (60 %, nie aufgegeben) | 12 % | 28 % | 44 % | 60 % | **65 %** | 71 % | 52 |
| … mit typischem Elternerbe (nicht Teil des Plans) | 6 % | 18 % | 32 % | 51 % | **59 %** | 68 % | 55 |
| Duales Studium, dann Schweiz/DE | 6 % | 17 % | 31 % | 46 % | **52 %** | 59 % | 57 |
| Sicherer PiBS-Platz, dann Schweiz/DE | 8 % | 20 % | 34 % | 48 % | **53 %** | 60 % | 56–57 |
| Bachelor + Agentur, dann Schweiz/DE | 6 % | 17 % | 30 % | 44 % | **49 %** | 57 % | 58 |
| Plan, aber ohne Schweiz (außer über PiBS) | 3 % | 11 % | 25 % | 41 % | **47 %** | 55 % | 58–59 |
| Bachelor + Agentur, nur Deutschland | 2 % | 9 % | 22 % | 37 % | **43 %** | 52 % | 60 |
| Plan, aber spart wie typische Gutverdiener | 2 % | 9 % | 19 % | 31 % | **35 %** | 43 % | 63–64 |
| Bachelor + Agentur, Schweiz/DE + Firmenkauf | 8 % | 18 % | 27 % | 35 % | **38 %** | 43 % | 64–65 |
| Vertrieb (SaaS) ab 2027 | 2 % | 6 % | 14 % | 25 % | **30 %** | 38 % | 65 |
| 2 Jahre Agentur Vollzeit, dann Vertrieb | 2 % | 4 % | 10 % | 20 % | **24 %** | 32 % | > 65 |

Verworfen und warum:

- **Webagentur als Hauptweg:** Solo-Agenturen verdienen meist wenig; die
  Million bräuchte ein Team von 10+ Köpfen (im auf IfM- und Admin-Bar-Daten
  kalibrierten Modell nur ~0,3 % nach 10 Jahren).
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
mit Platz knapp vor dem dualen Studium (53 % gegen 52 % am Zieldatum), aber
die Plätze sind knapp (2022 erst 128 Eintritte schweizweit; laut Bund sind
die Plätze in Unternehmen das Nadelöhr) und der Lohn deckt die Schweizer
Lebenshaltung nicht. Darum steht es im Plan gleichberechtigt neben dem
dualen Studium: Nimm, was zuerst sicher zusagt. Der Plan mit beiden
Optionen liegt bei 51 %, kaum unter dem dualen Weg. Der Abstand entsteht,
weil das Modell annimmt, dass parallele PiBS-Bewerbungen die Chance auf
einen dualen Platz um 15 % senken (Schätzung, Termine kollidieren).

## 4. Der Plan

### Phase 0 – jetzt bis August 2027: Abitur, Bewerbungen, erstes Geld

1. **Abitur hat Vorrang.** Die Note entscheidet über duale Plätze.
2. **Bewerbungen jetzt, nicht im Sommer.** Duale Plätze für Herbst 2027
   werden oft ein Jahr vorher vergeben.
   - 20–40 Bewerbungen auf duale Studienplätze **Informatik /
     Wirtschaftsinformatik**, bis spätestens Februar 2027. Bevorzugt
     Arbeitgeber mit Standort oder Kunden in der Schweiz und ohne lange
     Bindungsklausel.
   - **PiBS** parallel und **sofort, noch im Dezember 2026:** direkt bei
     den Partnerfirmen von ZHAW, FHNW, BFH, HSLU, FFHS bewerben (die Firma
     stellt ein, die Hochschule lässt zu). Zulassung mit deutschem Abitur
     vorher bei der Hochschule klären.
   - **Plan B:** Bachelor Informatik an einer **FH/HAW**, nicht an einer Uni
     (Bewerbung bis Juli): Dort brechen deutlich weniger ab (DZHW: 30–37 %
     gegen 42–47 %), und Schweizer Arbeitgeber kennen den FH-Abschluss gut.
     Gerechnet ist mit 6 Semestern – bevorzuge einen Studiengang mit 6
     Semestern; viele bayerische HAWs haben 7 (mit Praxissemester). Ein
     vierjähriger Bachelor kostet im Modell knapp einen Punkt, 7 Semester
     also etwa einen halben.
3. **Webgeschäft als Verkaufsschule** (`standortcheck`), ~5 h/Woche bis
   März, Pause in den Prüfungen, danach bis 25 h/Woche. Siehe Abschnitt 5.
4. **Geld:** Depot eröffnen, ETF-Sparplan auf einen breiten Welt-ETF
   einrichten, Notgroschen von drei Monatsausgaben, Berufsunfähigkeits-
   versicherung prüfen (jung und gesund ist sie am günstigsten).

### Phase 1 – Herbst 2027 bis ~2031: Ausbildung mit Einkommen

- Rangfolge: **PiBS oder duales Studium** – gleichwertig, nimm, was zuerst
  sicher zusagt (PiBS nur, wenn die Finanzierung steht: Lebenshaltung in
  der Schweiz ~25 Tsd. € im Jahr gegen ~17 Tsd. € Lohn netto) >
  **Bachelor an einer FH + Webgeschäft 20 h/Woche**.
- **Wie das Studium finanziert ist (so rechnet das Modell):** Im deutschen
  Studium braucht man ~1.000 €/Monat; ~500 € kommen aus Nebenjob oder
  Webgeschäft, die Lücke tragen Eltern oder BAföG (Höchstsatz 2026: 992 €).
  Bei PiBS fehlen ~8 Tsd. € im Jahr; gerechnet ist mit ~500 €/Monat
  Unterstützung, der Rest (~2 Tsd. € im Jahr) wird Studienkredit. Fehlt die
  Unterstützung, ist das duale Studium die bessere Wahl. Im Modell wird
  PiBS bei einer Zusage immer vorgezogen – das Ergebnis ist praktisch
  dasselbe.
- Ab dem ersten eigenen Geld gilt die **Sparregel** (siehe unten).
- Wer in Deutschland studiert: Praktikum oder Abschlussarbeit mit Bezug zur
  Schweiz, Englisch und Deutsch fließend, Lebenslauf auf Schweizer Stellen
  ausrichten.
- **Abbruch-Regel:** Läuft das Studium schon im ersten Semester schlecht,
  bis Februar parallel auf duale Plätze für den nächsten Herbst bewerben;
  bleibt es am Ende des ersten Jahres schlecht, sofort neu starten (dual,
  sonst ein anderes Informatik- oder Wirtschaftsinformatik-Studium) statt
  zwei Jahre durchhalten. Im Modell ist die Regel so eingerechnet: Die
  Hälfte derer, die im ersten Jahr abbrechen, startet einmal neu, die andere
  Hälfte geht ohne Abschluss in den Beruf. Der zweite Versuch hat dort
  dasselbe Abbruchrisiko und dieselbe Chance auf einen dualen Platz wie ein
  Erstversuch – das ist eher günstig gerechnet, und ohne diese Regel läge
  der Plan bei 50,1 %.

### Phase 2 – ~2031 bis ~2040: Die Schweiz-Phase

- Erste Wahl: **IT-Stelle in der Schweiz** (Zürich, Basel, Bern, Zug).
  Klappt es nicht sofort: IT-Stelle in Deutschland und **nach 4 Jahren
  Berufserfahrung zweiter Anlauf** – mit Erfahrung steigt das Gehaltsangebot
  (im Modell +10 %); die Chance auf eine Stelle ist für diesen einen
  zweiten Versuch vorsichtig mit 20–30 % angesetzt.
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
> **Im Studium** (dual, PiBS, Bachelor): Grundbedarf ~1.000 €/Monat, 40 % von
> allem darüber ins Depot.

Das ist gut das 1,5-Fache dessen, was typische Gutverdiener von jedem
zusätzlichen Euro sparen (~38 %). Genau
deshalb ist es Regel und Dauerauftrag, nicht Vorsatz. Die Hauptzahl dieses
Plans (51 % am 31.08.2065) rechnet bewusst damit, dass die Regel nicht
perfekt hält: im Mittel werden nur ~50 % gespart, und 15 % der Leben werden
irgendwann halbherzig. Wer sie wirklich hält – auch mit Partner –, hat am
Zieldatum **65 %**; wer nur so spart wie typische Gutverdiener, **35 %** –
dann trägt der Plan nicht. (Im Studium rechnet das Modell mit 1.000 €/Monat
Grundbedarf und spart 40 % von allem darüber.)

### Weichen mit harten Zahlen

| Wann | Wenn … | dann … |
|---|---|---|
| Feb. 2027 | kein dualer Platz | Bachelor-Bewerbung vorbereiten, PiBS weiter verfolgen |
| Ende April 2027 | auch kein PiBS-Vertrag | Bachelor-Bewerbung abschicken, Webgeschäft ausbauen |
| 1. Semester (bis Februar) | Studium läuft schlecht | parallel auf duale Plätze für den nächsten Herbst bewerben |
| Ende 1. Studienjahr | Prüfungen nicht bestanden / kein Interesse | sofort neu starten: dual oder ein anderes Informatik-/Wirtschaftsinformatik-Studium (fachfremder Wechsel ist nicht eingerechnet) |
| Studienende | Schweizer Stelle angeboten | annehmen |
| nach 4 Jahren DE-Stelle | noch nicht in der Schweiz | zweiter Anlauf; parallel Gehalt verhandeln |
| ab 5 Berufsjahren | Freelance-Gewinn > 1,2 × Gehalt erreichbar | IT-Freelancing prüfen |
| bei Rückkehr nach DE | Schweiz-Phase endet (Partner, Kinder) | Sparregel weiterführen, Depot nie anfassen |
| jedes Jahr am 31.08. | Vermögen unter dem 25-%-Kontrollwert (Abschnitt 6, zwischen den Altern linear interpolieren) | Grundbedarf senken, Sparquote erhöhen |

## 5. Bis Sommer 2027 – was mit mindestens 50 % geht

Webgeschäft neben dem Abitur: Vor-Ort-Besuch mit ausgedrucktem Bericht,
zuerst eine Einzelmaßnahme (69–349 €, eigene Preisliste aus `standortcheck`), dann
das Website-Paket (zum Vergleich: Onepager am Markt 1.500–4.000 €). Die
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
eingerechnet), Stichtag jeweils 31.08.; **nach Datum lesen, nicht nach
Alter** (wer ein Jahr älter ist, nimmt trotzdem die Zeile seines Datums);
für Jahre zwischen den Zeilen linear interpolieren. In der Ausbildung (bis
~2030/31) wächst das Vermögen kaum – das ist eingeplant. Bei PiBS ist es bis
~2031 sogar negativ (Studienkredit, bis etwa −9 Tsd. €); dort gilt die
Weiche „unter dem 25-%-Wert“ erst ab dem ersten Vollzeitjahr. Liegst du **unter dem linken Wert**, bist du hinter dem Plan
und musst nachsteuern; über dem rechten bist du gut vorn
(`python3 plan/simulation.py --kontrolle`).

| Stichtag | Alter (Abitur 2027) | 25 % liegen darunter | Median | 25 % liegen darüber |
|---|---:|---:|---:|---:|
| 31.08.2030 | 22 | 1 Tsd. € | 1 Tsd. € | 2 Tsd. € |
| 31.08.2033 | 25 | 10 Tsd. € | 21 Tsd. € | 35 Tsd. € |
| 31.08.2038 | 30 | 49 Tsd. € | 91 Tsd. € | 149 Tsd. € |
| 31.08.2043 | 35 | 102 Tsd. € | 188 Tsd. € | 315 Tsd. € |
| 31.08.2048 | 40 | 151 Tsd. € | 288 Tsd. € | 519 Tsd. € |
| 31.08.2053 | 45 | 208 Tsd. € | 431 Tsd. € | 810 Tsd. € |
| 31.08.2058 | 50 | 283 Tsd. € | 624 Tsd. € | 1,20 Mio. € |
| 31.08.2063 | 55 | 402 Tsd. € | 897 Tsd. € | 1,75 Mio. € |

## 7. Was den Plan kippt – und was nicht

Jeweils genau ein Faktor auf einem ungünstigen bzw. günstigen Wert, alle
anderen bleiben unsicher (4 × 10.000 Leben, `python3 plan/simulation.py
--sens`). Basis: **51 %** am 31.08.2065, 50 % ab 57.

| Faktor (schlecht / gut) | Chance am 31.08.2065 | 50-%-Alter |
|---|---:|---:|
| Sparverhalten (typisch / eiserne Regel: 60 %, nie aufgegeben) | 35 % / 65 % | 63–64 / 52 |
| Aktienrendite über das ganze Berufsleben (4 % / 8 % im Jahr) | 40 % / 65 % | 61–62 / 52–53 |
| Grundbedarf (DE 22 / 13, CH 40 / 30 Tsd. € im Jahr) | 44 % / 65 % | 60 / 53 |
| Kinder (sicher und teuer: 12 Tsd. € im Jahr / keine) | 45 % / 58 % | 59–60 / 54–55 |
| Nie eine Schweizer Stelle (kein Anlauf, auch nicht nach PiBS; PiBS findet trotzdem statt) / – | 44 % / – | 59–60 / – |
| KI-Druck auf Einsteiger (sicher / nie) | 46 % / 54 % | 59 / 56 |
| Schweizer Stelle im ersten Anlauf (nie / immer angeboten) | 49,9 % / 55 % | 57–58 / 55–56 |
| Dualer Studienplatz (nie / immer angeboten) | 49,7 % / 53 % | 57–58 / 56–57 |
| Rückkehr aus der Schweiz (13 % je Jahr in den ersten 5 Jahren, deutlich über SECO / nie) | 49 % / 60 % | 58 / 53–54 |

„Immer angeboten“ heißt: ohne KI-Druck sicher; in den Leben mit KI-Druck
(25–50 %) 80 %. Für „ohne Schweiz“ stehen im Dokument drei verschiedene
Fälle: nie eine Schweizer Stelle, aber PiBS möglich (44 % – vier teure
Schweizer Studienjahre ohne Schweizer Stelle danach), ganz ohne Schweiz und
PiBS (45 %) und ohne Schweizer Stelle nach einem deutschen Studium, PiBS
mit Stelle möglich (Abschnitt 3, 47 %).

**Von dem, was du selbst steuerst, wirken Sparregel und Grundbedarf am
stärksten.** Neun von neun Einzelfaktoren drücken auf ihrem ungünstigen Wert
das Zieldatum unter 50 % – der Plan hat nur 1,3 Punkte Puffer. Darum sind
Sparregel und Grundbedarf Regeln mit Dauerauftrag, keine Vorsätze. Die
Börse kannst du nicht steuern – nur aushalten.

**Stresstest** (`python3 plan/simulation.py --stress`): die drei großen
Schätzungen gleichzeitig am pessimistischen Rand – Chance auf eine Schweizer
Stelle halbiert (auch im zweiten Anlauf), nach PiBS deutlich seltener,
PiBS-Platz kaum, dualer Platz seltener, Rückkehr aus der Schweiz deutlich
über dem SECO-Wert (dort 35 % nach 5 und 45 % nach 10 Jahren; im Modell
sonst ~35 % / ~45 %, je nach Zählweise 34–36 % / 44–45 %; im Stress 50 % / 60 %).

| Szenario | mit 54 | mit 56 | **mit 57** | mit 60 | mit 62 | mit 65 |
|---|---:|---:|---:|---:|---:|---:|
| Plan (Basis) | 43 % | 49 % | **51 %**¹ | 59 % | 63 % | 69 % |
| Stress: die drei großen Schätzungen pessimistisch | 38 % | 44 % | **47 %**¹ | 55 % | 60 % | 66 % |
| Stress + KI-Druck sicher | 33 % | 39 % | **42 %** | 50,5 % | 56 % | 62 % |

¹ Nachgemessen über 16 Läufe à 10.000 Leben: Plan
51,7 % ± 0,2, Stress 46,8 % ± 0,2 (nur Rechenrauschen der Simulation;
wie unsicher die Annahmen sind, zeigt die Sensitivitätstabelle oben). Die
50-%-Alter gelten je Lauf (Seeds 2027/1/2/3); Werte auf der Grenze können
mit anderen Seeds ein Jahr abweichen.

Das Planziel bleibt **der 31. August 2065**. Es ist zugleich die früheste
Marke mit mindestens 50 % (51 %; ein Jahr früher, mit 56, sind es erst
48,5 %). Liegen alle drei großen Schätzungen daneben, reicht es am
Zieldatum nicht (47 %); dieser Fall erreicht die 50 % mit 58–59 (Sommer 2066–2067),
mit zusätzlich sicherem KI-Druck mit 60–61 (Sommer 2068–2069). Die Jahre 2068 bis
2073 in der folgenden Tabelle zeigen nur, ab wann auch noch härtere Fälle
über 50 % liegen.

**Härtefälle bis zum Äußersten** (`python3 plan/simulation.py --stress`,
4 × 10.000 Leben). **Fall A**: ohne Schweiz, ohne PiBS, ohne dualen Platz,
KI-Druck sicher – also Bachelor (mit Webgeschäft) und Arbeit in Deutschland.
„Äußere Kleinannahmen pessimistisch“: kein Freelancing, harte Lohnnarbe nach
Arbeitslosigkeit, träger Konsum, keine weiterlaufenden Betreuungsverträge.

| Szenario | mit 57 (2065) | mit 60 (2068) | mit 62 (2070) | mit 64 (2072) | mit 65 (2073) | 50 % ab |
|---|---:|---:|---:|---:|---:|---:|
| Plan (Basis) | 51 % | 59 % | 63 % | 67 % | 69 % | 57 |
| äußere Kleinannahmen pessimistisch | 46 % | 53 % | 57 % | 61 % | 63 % | 59 |
| + die drei großen Schätzungen pessimistisch | 39 % | 47 % | 51 % | 56 % | 58 % | 62 |
| ganz ohne Schweiz und PiBS | 45 % | 54 % | 59 % | 64 % | 66 % | 59 |
| Fall A | 38 % | 47 % | 52 % | 57 % | 59 % | 62 |
| Fall A + äußere Kleinannahmen pessimistisch | 30 % | 37 % | 42 % | 46 % | **48 %** | **> 65** |
| … dabei ohne Hauskauf und ohne Aufgeben (Sparquote weiter gestreut) | 34 % | 42 % | 47 % | 52 % | 54 % | 64 |

Die Schweiz und die Studienform machen die Million **früher** erreichbar.
Ohne sie und mit sicherem KI-Druck (Fall A) liegt der Plan ab 62
(Sommer 2070) über 50 %. Kommen zusätzlich alle äußeren Kleinannahmen ungünstig,
**reicht es bis 65 nicht** (48 % mit 65), und dort trägt der Plan nicht. Das ist der härteste getestete Fall, in dem
Sparregel und Märkte noch halten; mit typischem Sparen oder 4 % Rendite liegt
er noch tiefer (siehe unten). Nur wenn dabei weder ein Haus gekauft noch
die Sparregel aufgegeben wird, liegt er ab 64 (Sommer 2072, 52 %) über 50 %.
Was nicht verhandelbar bleibt:
die Sparregel (bei Sparen wie typische Gutverdiener mit 60: Fall A
30 %, Fall A + äußere 22 %) und Märkte, die nicht das ganze
Berufsleben über nur 4 % liefern (dann mit 60: Fall A 34 %, Fall A + äußere
25 %).

**Welche Eingaben in Fall A noch wirken – und woher sie stammen** (Links in
Abschnitt 10):

| Eingabe | Wert im Modell | Quelle |
|---|---|---|
| Schweizer Stelle, PiBS-Platz, dualer Platz | **0** (abgeschaltet) | – |
| Einstiegsgehalt IT mit Bachelor | 43–50 Tsd. € (Mitte 46,3), ×0,92 KI-Abschlag | get in IT 2026 (42,4–49,4, typisch 46,3), Stepstone 2026 (~43,7) |
| Gehaltsverlauf IT | real +2,5–7,5 % je Jahr (Mitte 4,2 %) bis Jahr 10, danach 0–2 %; ergibt Median ~51 / 63 / 75 Tsd. nach 1–3 / 5–8 / 10–13 J., mit KI-Abschlag ~47 / 57 / 68 | in den ersten Jahren gleichauf mit Stack Overflow DE 2024+25 (Median ~50 / 66 / 78 Tsd., n ≈ 4.250), danach bewusst darunter |
| Gehalt ohne Abschluss (31 % der Leben in Fall A) | 34–45 Tsd. € Einstieg, real +1–4,5 % je Jahr bis Jahr 10, danach 0–1,5 %; Median ~41 / 47 / 52 Tsd. nach 1–3 / 5–8 / 10–13 J., mit KI-Abschlag ~38 / 43 / 47 | Stepstone 2026, Web-Entwickler: Einstieg ~37 Tsd., Median über alle Stufen 41,8 Tsd. (Verlauf darüber hinaus geschätzt) |
| Steuern, Sozialabgaben | Tarif 2026, BBG 2026, Arbeitnehmeranteil +3,65 Pp. bis 2035; Selbstständige voller KV/PV-Satz (21,1 %, +4 Pp.) | § 32a EStG, Rechengrößen 2026, IGES für die DAK 2026 (42,7 % → 50 %) |
| Studienabbruch Bachelor Informatik | 30–42 % (FH/HAW, mit Webgeschäft nebenher); die Hälfte der Abbrecher im 1. Jahr startet neu | DZHW 2022 (HAW 30–37 %, Uni 42–47 %); Neustart-Quote geschätzt |
| Arbeitslosigkeit, Krisen | 2–5 % je Jahr, in Krisen 5–18 %; Lohnnarbe 2–8 % je Arbeitslosigkeit | IAB 1998–2019: Akademiker 2,0–4,1 % (Modell im oberen Bereich); Schmieder et al. 2023 |
| Berufsunfähigkeit | je Jahr nach DAV-Tafel 2021 I × 0,5–0,75 (≈ 0,1 % mit 25, 0,3 % mit 50, 0,6 % mit 57); BU-Rente 45–65 % des Nettos; Prämie 3,5 % der versicherten Jahresrente | DAV 2021 I (Gruppe Informatiker 58 % der Tafelerwartung), Finanztip 2026 |
| Kinder, Partnerschaft, Scheidung | eigener Anteil 5–12 Tsd. €/Jahr für alle Kinder zusammen (1–2), 18 Jahre ab dem ersten (Hälfte der Kosten nach Kindergeld); Väter bei Geburt des 1. Kindes der Mutter 33,3; 28 % Scheidungen (Ehedauer bis 25 J.) | EVS 2018 (424–1.212 €/Monat für ein Kind nach Einkommen), Destatis 2025 |
| Kaufnebenkosten Haus | 5–12 % | Grunderwerbsteuer 3,5–6,5 %, Notar/Grundbuch 1,5–2 %, Makler bis 3,57 % |
| Sparverhalten | 38–62 % jedes Euros über dem Grundbedarf | EVS 2018 (38 % gespart bzw. 58 % nicht konsumiert bei 5–10 Tsd. € netto), DIW/SOEP 2025 |
| Aktienrendite | 3,5–8 % geometrisch, Vola 13–18 %, dicke Ränder | MSCI World Net seit Ende 2000: 6,7 %; Prognosen Vanguard/Morningstar 4,8–7,5 % nominal (USD) |
| Steuer beim Verkauf | 18,46 % auf ETF-Gewinne | § 20 InvStG, § 32d EStG |

Ebenfalls wirksam, aber **geschätzt** (ohne harte Quelle), die wichtigsten
im ganzen Plan: Grundbedarf 15–22 Tsd. € (aus WG-Mieten abgeleitet: München
849 €, Berlin 659 € warm), Inflation 1,5–3 %, Vergütung im dualen Studium
und bei PiBS, Vorsprung des dualen Studiums beim Einstieg (~1 Tsd. €),
Schweizer Stelle (18–50 %, mit Partner ×0,7; zweiter Anlauf 20–30 %),
PiBS- und dualer Platz, Einstieg nach PiBS (75–95 Tsd. CHF), Schweizer
Lohnwachstum, Lohn nach Rückkehr (60–75 % des Schweizer Gehalts),
Bindungsklausel nach dem dualen Studium (2/3), weniger Chance auf einen
dualen Platz bei parallelen PiBS-Bewerbungen (×0,85), Dauer des
FH-Bachelors (6 Semester), Kita-Kosten in der Schweiz
(×1,7), Anteil früher Abbrüche (50 %), Schweizer Steuerkurve
(6–30 % effektiv je nach Einkommen, +1,5 Punkte für Zürich/Basel/Bern –
nicht gegen den ESTV-Rechner geprüft), Agentur während des Bachelors,
Freelancing (Chance 30–60 %), Hauskauf trotz Rat (20–40 %), Aufgeben der
Sparregel (15 %), Neustart nach Abbruch im ersten Jahr (50 %),
Konsumträgheit, Lebensstil mit Partner, KI-Szenario, Partnerschaft und Heirat. Die Härtefall-Tabelle variiert davon nur
Freelancing, Konsumträgheit und weiterlaufende Betreuungsverträge (dazu
die belegte Lohnnarbe); Grundbedarf, Sparverhalten und KI zeigt die
Sensitivitätstabelle, Schweiz und Studienplatz der Stresstest.

**Gegenrechnung ohne Simulation** (unabhängiger Prüfer, typischer Lebensweg
in Fall A: Bachelor, IT-Stelle in Deutschland ab 46 Tsd. € real, Sparregel,
Kinder, BU-Prämie; Sparregel eisern, ohne KI-Abschlag): Depot mit 60,
nominal nach Steuer. Gerechnet noch mit
dem früheren Stand (Abgaben +3 statt +3,65 Punkte, BU-Prämie 900 statt
750 €, höheres Gehalt ohne Abschluss) – die Spalte „ohne Abschluss“ ist
deshalb eher zu hoch.

| Rendite im Jahr | mit Abschluss | ohne Abschluss (31 % der Leben) |
|---|---:|---:|
| 8,6 % (MSCI-World-Sparplan, Durchschnitt laut DAI) | 2,65 Mio. € | 2,26 Mio. € |
| 6 % | 1,57 Mio. € | 1,31 Mio. € |
| 4 % | 1,11 Mio. € | 0,91 Mio. € |

Für die Million reichen damit – eiserne Sparregel, ohne KI-Abschlag, mit
60 – mit Abschluss 3,4 % Rendite, ohne Abschluss gut 4,4 %. Die Simulation liegt in Fall A mit 60 im Median bei
0,92 Mio. € – niedriger als die Gegenrechnung, vor allem weil sie die
Sparregel nicht perfekt hält (im Mittel ~51 % statt 60 %, 15 % geben auf)
und in Fall A der KI-Abschlag sicher ist; mit eiserner Regel und ohne KI
liegt ihr Median bei 1,61 Mio. € (eigene Rechnung mit `sim.simulieren`). Märkte, Arbeitslosigkeit, Abbrüche,
Berufsunfähigkeit und Hauskäufe machen nur einen kleineren Teil aus.

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
   Die Aussage wanderte von „50 % mit 40“ zu „50 % mit 54“ – und durch die
   Quellenprüfung (Punkt 4) zu den Zahlen im Kopf dieses Dokuments.
   *Die folgenden Prüfberichte beziehen sich auf frühere Commits, also auf
   die Zahlen vor der Quellenprüfung; ihre Werte sind überholt.*
   **Frühere Schlussverifikation** (vor der Quellenprüfung; frischer Checkout, alle
   Tests grün): 8 von 8 unabhängigen Läufen (Seeds 2027/1/2/3 und
   101/202/303/404, je 10.000 Leben) liefern das 50-%-Alter 54;
   P(54) = 51,9 % bzw. 52,1 %, untere Intervallgrenze jeweils über 51,4 %
   (seit dem Horizont bis 65, wegen anderer Zufallsfolge: 51,6 %).
   Ein vierter unabhängiger Prüfer hat Commit e6d0f7c geprüft: Zahlen und
   Kalenderjahre stimmig; seine Kritik, dass im damals härtesten Fall noch weitere
   geschätzte Eingaben wirken, ist in die Härtefall-Tabelle eingeflossen.
   Ein dritter unabhängiger Prüfer hat Commit 878be02 (Härtefälle) im
   frischen Klon geprüft: 92 Tests grün, damals härtester Fall mit 60 bei
   56,0–56,3 % (12 Seeds), in diesem Fall kommen Schweiz, PiBS und dual
   nachweislich nie vor; dazu die Gegenrechnung ohne Simulation (Abschnitt 7).
   Ein zweiter, unabhängiger Prüfer hat Commit 065359f in einem frischen
   Klon mit eigenen Seeds nachgerechnet: alle Dokumentzahlen innerhalb ±1
   Prozentpunkt; Planziel 2065: Basis 60,3 %, Stress 55,5 %, Stress + KI
   50,6 % (je 160.000 Leben).
   Die Unsicherheit der geschätzten Spannen (Schweizer Stelle, PiBS-Platz,
   Rückkehrrate) steckt bereits in diesen Zahlen, weil jedes Leben seine
   Werte aus der ganzen Spanne zieht (damals: im ungünstigsten Einzelfall,
   nie eine Schweizer Stelle, verschob sich die Schwelle auf 55; die
   heutigen Werte stehen in Abschnitt 7).
4. **Quellenprüfung (22.11.2026), zwei Runden, und zwei Schlussprüfungen:**
   42 Belege einzeln gegen die Originalquelle geprüft (Abschnitt 10):
   24 bestätigt, 18 präzisiert oder korrigiert; eine unabhängige Gegenprobe
   von 8 bestätigten Belegen fand keinen Fehler. Danach 23 Angaben, die
   vorher nur im Code standen: 10 bestätigt, 11 korrigiert, 2 als Schätzung
   gekennzeichnet. Zwei weitere Prüfer haben alle Links abgerufen und die
   Zahlen erneut gegen die Originale gehalten. Im Modell geändert, weil die
   Quelle es verlangte: Einstiegsgehalt Bachelor 43–50 statt 44–58 Tsd. €
   (get in IT), Schweizer Einstieg mit Modus 81.850 CHF (swissICT-Median;
   Median im Modell ~83,5 Tsd.) statt 88.000, Gehalt ohne Abschluss 34–45 Tsd. € Einstieg mit flacherem Verlauf
   (Stepstone), Rückkehr aus der Schweiz auf den SECO-Wert (35 % nach 5,
   45 % nach 10 Jahren; vorher ~28 % nach 10), Berufsunfähigkeit nach Alter
   (DAV 2021 I) statt konstant 0,1–0,2 %, BU-Prämie als Anteil der
   versicherten Rente, Sozialabgaben +3,65 statt +3 Punkte (IGES 2026;
   Selbstständige voller KV/PV-Satz), Schweizer ALV/NBU nur bis CHF
   148.200, Kaufnebenkosten 5–12 statt 5–9 %, Aufstieg im Vertrieb 22–46 %
   statt 35–55 % (UNIFY). Ergebnis: Hauptzahl von 60 % auf 48,8 %, also
   **unter das Ziel**. Dann eine Änderung am Plan (Plan B an einer FH,
   DZHW: weniger Abbrüche) und eine am Modell (die schon im Plan stehende
   Abbruch-Regel jetzt auch für den Bachelor eingerechnet: die Hälfte der
   Abbrecher im ersten Jahr startet einmal neu). Ergebnis: **51 %** am
   31.08.2065 (16 Läufe: 51,7 % ± 0,2), Stress 47 %. Die beiden
   unabhängigen Schlussprüfer (frische Klone, eigene Seeds) bestätigten auf
   dem vorletzten Stand alle Tabellen innerhalb ±1,5 Punkten und fanden die
   zu hohe Schweizer Einstiegszahl, die danach korrigiert wurde. Ein Test
   prüft bei jedem Lauf das Zieldatum, die fünf Werte der Kopftabelle (±2
   Punkte, 10.000 Leben) und dass die Hauptzahl in der Simulation über 50 %
   liegt (`python3 plan/simulation.py --extra` gibt die Zwischenstände
   aus).
5. **Grenzen:** Viele Spannen sind begründete Schätzungen (Chance auf
   Schweizer Stelle, PiBS-Platz, Neustart nach Abbruch, KI-Szenario).
   Schweizer Beträge zählt das Modell 1:1 als Euro (bei ~0,93 CHF je Euro
   eher vorsichtig); ein Wechselkursrisiko ist nicht modelliert. Bewusst
   nicht in der Hauptzahl: Erbschaften (mit typischem Elternerbe 50 % schon
   mit 55 statt 57), das Vermögen eines Partners (früher gemessen: als Paar
   mit Zugewinngemeinschaft ~1–2 Jahre früher; nicht neu gerechnet), die
   Pensionskasse voll statt halb (53 % statt 51 % am Zieldatum),
   Kirchensteuer (bei Mitgliedschaft etwas später). Wer eigene Ist-Werte
   hat, trägt sie in `plan/simulation.py` ein und rechnet neu.

## 10. Quellenverzeichnis

Die Belege unten wurden am 22.11.2026 einzeln gegen die verlinkte
Originalquelle geprüft (acht Prüfer, je einer pro Themengruppe, danach eine
unabhängige Gegenprobe von 8 der bestätigten Belege: alle 8 halten; zwei
weitere Prüfer haben alle Links abgerufen – alle erreichbar – und rund 50
Zahlen erneut gegen die Originale gehalten). Wo die Quelle etwas anderes
sagte als die frühere Fassung dieses Plans, steht hier der korrigierte Wert,
und der Plan rechnet damit. Live-Seiten (Interhyp, Stepstone, get in IT,
Vanguard) können sich seitdem geändert haben.

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
  Makler bis 3,57 %, zusammen 5–12 % (Baufi24). <https://www.baufi24.de/nebenkosten-hauskauf/>

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
- Freelancer-Kompass 2026 (5.412 Befragte): Software/Web 91 €/h (S. 32/33);
  80 % aller Befragten > 10 Jahre Praxis (S. 7); fakturierte Tage nur als
  Verteilung (S. 14/15).
  <https://www.freelancermap.de/files/survey/freelancer-kompass-2026.pdf>
- UNIFY, „The Path to AE“ (2026; ~180.000 US-SDRs aller Branchen, Start
  2021–26, Stand 07/2026, jüngere Kohorten unvollständig): 22,3 %
  erreichen AE; in den ausgewählten Branchen mit hoher Quote 32,0 %
  (kleinere Software-Firmen) bzw. 46,5 % (große KI-Firmen).
  <https://www.unifygtm.com/the-jump/report/the-path-to-ae>
  – Bridge Group (2017): 26 % von 205 beförderten SDRs nach ≤ 6 Monaten als
  AE gescheitert.
  <https://blog.bridgegroupinc.com/failure-rate-of-sdr-to-ae-promotions>
- Stanford Digital Economy Lab, Update „Canaries in the Coal Mine“
  (12.08.2026, US-Lohndaten von ADP bis 06/2026): 22–25-Jährige in stark
  KI-exponierten Berufen ~19 % unter dem Verlauf weniger exponierter Berufe
  (relativ, deskriptiv).
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
- DHBW Studienverlaufspanel 2/2018, S. 14–15: Abbruchquote Fakultät
  Technik (dort liegt Informatik) 18,1 % (Jahrgang 2015, vorläufig);
  einzelne Standorte 10–20 %; DHBW gesamt Jahrgang 2016 12,0 % nach zwei
  Jahren, davon 9,4 % im ersten Jahr.
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
  Monat, bezogen auf das Haushaltsnetto: 38 % (Ersparnis) bzw. 58 % (nicht
  konsumiert); in den Klassen 1,7–5 Tsd. € nur 2–23 %.
  <https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/DEHeft_derivate_00057921/2152604189004_korr19112020.pdf>
- Destatis, Konsumausgaben von Familien für Kinder (EVS 2018): Paare mit
  einem Kind im Schnitt 763 €/Monat, nach Einkommen 424–1.212 €.
  <https://www.statistischebibliothek.de/mir/servlets/MCRFileNodeServlet/DEHeft_derivate_00061567/5632202189004.pdf>
- Destatis, Alter der Eltern 2025: Väter bei der Geburt des ersten Kindes
  der Mutter 33,3 Jahre (alle Geburten 34,8).
  <https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Geburten/Tabellen/geburten-eltern-biologischesalter.html>
- Destatis, Maßzahlen Ehescheidungen: zusammengefasste Scheidungsziffer
  2025 284,3 je 1.000 Ehen (≈ 28 % bei einer Ehedauer bis 25 Jahre).
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

**Quellen, die vorher nur im Code standen** (zweite Prüfrunde, 22.11.2026)

- SBFI-Wirkungsanalyse PiBS 2023 (im WBF-Bericht HFKG, S. 4–5): 50 % der
  befragten PiBS-Absolventen blieben im Partnerunternehmen (2019–2022
  insgesamt 117 Absolvierende). Link wie
  oben (WBF-Bericht).
- BFS, Hochschulabsolventenbefragung (Medienmitteilung 27.08.2026):
  FH-Bachelor Technik und IT, Jahrgang 2024, ein Jahr nach Abschluss 6,4 %
  erwerbslos (2022: 3,0 %). <https://www.admin.ch/de/newnsb/pikqMhNDHIm85DtBKpkd->
- BSV, Beitragssätze 2026: AHV/IV/EO 5,3 %, ALV 1,1 % (Arbeitnehmer);
  BVG-Altersgutschriften 7/10/15/18 %.
  <https://sozialversicherungen.admin.ch/de/d/6877/download> – BVG-Mindestzins
  1,25 % (2026), 2 % ab 2027: <https://www.admin.ch/de/newnsb/8DF8zxcfvu7l>
- BAG, mittlere Krankenkassenprämie 2026: Erwachsene CHF 465/Monat
  (Zürich 452), junge Erwachsene 326.
  <https://www.bag.admin.ch/dam/de/sd-web/A6f1lR0Ue5yX/kantonale%20monatliche%20mittlere%20Pr%C3%A4mie%20pro%20Altersklasse_PG2026.pdf>
- ETH Zürich: Studien- und Lebenshaltungskosten CHF 20–26 Tsd. im Jahr (das
  Modell setzt für PiBS ~25 Tsd. € an, also eher mehr).
  <https://ethz.ch/de/studium/finanzielles.html>
- MLP Studentenwohnreport 2026 (IW Köln), S. 59–60: WG-Zimmer 20 m² warm
  München 849 €, Berlin 659 €.
  <https://www.iwkoeln.de/fileadmin/user_upload/Studien/Gutachten/PDF/2026/MLP_Studentenwohnreport_2026.pdf>
- 22. Sozialerhebung (DZHW/DSW, Erhebung 2021): Studierende (Vollzeit,
  nicht bei den Eltern) geben 850 € im Monat aus; 68 % jobben, im Mittel
  516 € (Median 450 €).
  <https://www.bmbf.de/SharedDocs/Publikationen/de/bmbf/4/31790_22_Sozialerhebung_2021.pdf?__blob=publicationFile&v=4>
- §§ 13, 13a BAföG: Höchstsatz 2026 475 + 380 + 102 + 35 = 992 € im Monat.
  <https://www.gesetze-im-internet.de/baf_g/__13.html>,
  <https://www.gesetze-im-internet.de/baf_g/__13a.html>
- BIBB: tarifliche Ausbildungsvergütung 2025 im Schnitt 1.209 € im Monat
  (Azubis; für das duale Studium gibt es keinen amtlichen Durchschnitt – die
  Vergütung im Modell ist eine Schätzung).
  <https://www.bibb.de/de/pressemitteilung_218108.php>
- Kindergeld 2026: 259 € je Kind (BMBFSFJ).
  <https://www.bmbfsfj.bund.de/bmbfsfj/themen/familie/familienleistungen/kindergeld/kindergeld-73892>
  – Verbraucherpreise 2018 → Oktober 2026: ×1,29 (Destatis, 98,1 → 126,5);
  das Modell rechnet die EVS-Kinderkosten mit ×1,27 hoch. Oktober 2026:
  <https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/11/PD26_392_611.html>;
  Jahreswert 2018: <https://www.destatis.de/DE/Themen/Wirtschaft/Preise/Verbraucherpreisindex/Publikationen/Downloads-Verbraucherpreise/statistischer-bericht-verbraucherpreisindex-lange-reihen-5611103.xlsx?__blob=publicationFile&v=29>
- Destatis: Kinderlosenquote der Frauen mit 45–49 Jahren 20 %.
  <https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Geburten/kinderlosigkeit-und-mutterschaft.html>
- DIW Wochenbericht 5/2021: ~10 % der Erwachsenen erbten oder bekamen in 15
  Jahren eine Schenkung; Erbschaften Median 32 Tsd. €, Mittel 85 Tsd. €
  (Preise 2015; das Modell rechnet sie mit ×1,34 auf heute um).
  <https://www.diw.de/de/diw_01.c.809832.de/publikationen/wochenberichte/2021_05_1/haelfte_aller_erbschaften_und_schenkungen_geht_an_die_reichsten_zehn_prozent_aller_beguenstigten.html>
- Stepstone 2026, Web-Entwickler/in: Einstieg ~37.000 €, Median 41.800 €
  (Grundlage für das Gehalt ohne Abschluss, Einstieg und flacherer Verlauf).
  <https://www.stepstone.de/gehalt/Web-Entwickler-in.html> – Web Developer:
  Einstieg ~40.000 €. <https://www.stepstone.de/gehalt/Web-Developer.html>
- Schmieder, von Wachter, Heining (AER 2023): nach Massenentlassung in der
  Rezession ~15 % weniger Jahresverdienst über 15 Jahre, Tageslohn
  langfristig ~6 % weniger (das Modell: 2–8 % bleibende Lohneinbuße je
  Arbeitslosigkeit). <https://www.nber.org/system/files/working_papers/w30162/w30162.pdf>
- Freelancer-Kompass 2026: monatlicher Projektumsatz 8.022 → 6.653 €
  (−17 %; laut Quelle bei stabilen Stundensätzen, es fehlen Aufträge). <https://www.freelancermap.de/blog/freelancer-einkommen-projektumsatz/>
- Bridge Group 2025 SDR Report (351 B2B-Firmen, Daten 2024): 13 % der SDRs
  gehen unfreiwillig.
  <https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group>
- Jobrise 2026 (Jobportal): Customer Success Manager Software DE Junior
  42–55, Mid 55–75, Senior 75–95 Tsd. €.
  <https://jobrise.io/de/blog/customer-success-jobs-deutschland-2026/>
- Finanztip 2026: BU-Versicherung für eine Fachinformatikerin ~63 € im
  Monat (1.800 € Rente, Eintritt 30) – also ~3,5 % der versicherten
  Jahresrente; so rechnet das Modell die Prämie.
  <https://www.finanztip.de/berufsunfaehigkeitsversicherung/bu-kosten/>
- Deutsche Aktuarvereinigung, Tafel DAV 2021 I: BU-Inzidenz je Jahr (Männer)
  0,17 % mit 25, 0,24 % mit 40, 0,50 % mit 50, 1,30 % mit 60; Gruppe
  Rechnungskaufleute/Informatiker 58 % der Tafelerwartung (Vertragsjahr
  5+, laut DAV nur ein Anhaltspunkt). Eigene Rechnung daraus: bis 65 werden
  im Schnitt ~22 % berufsunfähig, mit dem Faktor 0,58 ~13 %.
  <https://aktuar.de/content/PDF/Fachwissen/2022-01-26_DAV-Hinweis-BU-RGen-2021.pdf>
- Sellwerk (Agentur-Ratgeber): Website für KMU, Onepager 1.500–4.000 €,
  5–10 Seiten 3.500–8.000 € (Marktpreise zum Vergleich).
  <https://sellwerk.de/wissenswert/was-kostet-eine-website>

**Nicht primär belegt** (bewusst als Schätzung geführt): PiBS-Lohn (Post-
Seite war nicht abrufbar; laut Suchauszug CHF 10.400 / 17.550 / 22.100 je
Jahr), NBU/Krankentaggeld ~0,8 %, die Einzelpreise 69–349 € (eigene
Preisliste aus `standortcheck`, kein Marktwert).
