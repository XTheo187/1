# Mehr als arbeiten gehen? Hebel bis Sommer 2027

> **Hinweis (23.11.2026): nicht mit deinen echten Angaben gerechnet.** Diese
> Rechnung baut auf dem Job-Modell für Bayern (Raum Regensburg) auf.
> Tatsächlich lebst du in Niedersachsen. Die Zahlen sind nicht neu gerechnet.
> Deinen gewählten Plan findest du in
> [`APP_PLAN_ALLEIN_MIT_CLAUDE.md`](APP_PLAN_ALLEIN_MIT_CLAUDE.md).

**Frage:** „Das kann ja nicht alles sein. Dann kann ich ja auch einfach
arbeiten gehen.“ Der Job-Weg aus
[`VERDIENST_BIS_SOMMER_2027.md`](VERDIENST_BIS_SOMMER_2027.md) bringt bis
31.08.2027 realistisch maximal ~13.500 € netto (Median ~11.300 €). Gibt es
einen Weg, der mehr bringt? Gemeint ist ein Hebel statt eigener Stunden
gegen Lohn: Mitarbeiter, Vermittlung, Kapital, Handel, Produkte, ein
höherer Stundensatz oder Provision.

> **Antwort: Bis 31.08.2027 nein – jedenfalls nicht im Erwartungswert.**
>
> Rund 30 Wege recherchiert, die stärksten 15 Lauf für Lauf gegen denselben
> Job-Weg gerechnet (gleiche Zufallszahlen, gleiches Stundenbudget, gleiche
> Steuer- und Versicherungsregeln). **Keiner schlägt den Job-Weg im
> Median.** Am nächsten kommt das Webgeschäft abends neben dem Sommerjob
> (Median ±0, im Mittel +100 €). Hebel verschieben vor allem den oberen
> Rand – und kosten dafür im Median Geld.
>
> | netto bis 31.08.2027 | Job-Weg | Job-Weg + beste Ergänzung¹ | größte Wette² |
> |---|---:|---:|---:|
> | sicher – 9 von 10 schaffen mindestens | ~8.900 € | ~8.600 € | ~5.600 € |
> | Median | ~11.300 € | ~11.300 € | ~9.000 € |
> | gut – 1 von 10 schafft mehr | ~13.500 € | ~13.800 € | ~16.400 € |
> | Spitze – 1 von 100 schafft mehr | ~14.900 € | ~18.400 € | ~32.200 € |
> | besser als der Job-Weg in | – | 35 % der Verläufe | 24 % der Verläufe |
>
> ¹ Webgeschäft abends neben dem Sommerjob + Startup-Teens-Wettbewerb nur
> mit Beleg (Abschnitt 3). ² Glasfaser-Haustürvertrieb als Handelsvertreter
> statt Sommerjob – die einzige Option mit echtem fünfstelligem Ausreißer
> nach oben, aber mit 54 % Risiko, um mehr als 2.000 € schlechter
> abzuschneiden.
>
> **Das Ergebnis:** Den Job-Weg als Boden behalten und nur billige Lose
> dazunehmen, die ihn nicht gefährden. Der echte Hebel – Stundensatz durch
> Referenzen, Kunden, die wiederkommen, Kapital, das arbeitet – entsteht in
> diesen neun Monaten, wirkt aber erst danach (Abschnitt 6). Wer trotzdem
> auf 500.000 € bis Sommer 2027 zielt, findet den einzigen Weg, der dafür
> überhaupt in Frage kommt, in [`500K_BIS_SOMMER_2027.md`](500K_BIS_SOMMER_2027.md).

**Gilt für:** die gleiche Lage wie im Job-Weg – volljährig, über einen
gesetzlich versicherten Elternteil familienversichert, danach Studium,
duales Studium oder Ausbildung. Die Zahlen oben mischen beide Fälle so wie
der Job-Weg (55 % dual/Ausbildung); getrennt in Abschnitt 2.

Gerechnet mit `python3 plan/hebel_2027.py` (20.000 Läufe je Option):
- Jede Option nimmt dem Job-Weg genau die Stunden weg, die sie braucht –
  vor dem Abitur gehen sie Nachhilfe oder Minijob verloren, im Sommer dem
  Sommerjob oder seinen Samstagen. Braucht sie mehr, als das Stundenbudget
  hergibt, gehen zuerst Ferienjob-Tage weg, der Rest von der Lernzeit
  (mit 20 €/h bewertet).
- Ihr Gewinn zählt zur Einkommensteuer und zusammen mit Nachhilfe und
  Webgeschäft zur Grenze der Familienversicherung. Reißt sie, kostet die
  eigene Krankenversicherung Geld; die Beiträge mindern dafür die Steuer
  (Abschnitt 5).
- Wo eine Option den Sommer braucht, gibt es einen Frühindikator bis
  31.03. oder eine Abbruchregel in den ersten Sommerwochen, danach mit
  einer gewissen Wahrscheinlichkeit noch einen späten Sommerjob.
- Die Verteilungen stammen aus zwei Recherche-Runden mit Belegen und
  eigenen Schätzungen, wo es keine gibt (Abschnitt 8); eine dritte
  Prüfrunde hat das Modell auf Rechenfehler durchgesehen.

## 1. Warum Hebel bis Sommer 2027 nicht greifen

**1. Der Engpass ist die Nachfrage, nicht Kapital oder Lieferkraft.**
Mitarbeiter, Vermittlung und Produkte helfen erst, wenn mehr verkauft wird,
als man selbst liefern kann. Ein Neuling ohne Bewertungen, Referenzen und
Reichweite verkauft im ersten Jahr wenig:
- Webgeschäft: belegt sind 1 Auftrag je ~100–200 Kaltanrufe und ~2 % je
  Haustür; geschätzt 0,5–5 % Einstieg je Vor-Ort-Besuch (Mitte 2 %).
  94 % der Handwerksbetriebe haben schon eine Website (Bitkom/ZDH 2026):
  Es ist ein Austauschmarkt gegen KI-Baukästen ab 10–20 €/Monat.
- Umzugs-, Garten- und Fensterteams: im ersten Sommer im Median nur
  ~200–280 verkaufte Stunden – der Mitarbeiter-Hebel greift im Median
  gar nicht.
- Produkte: Gumroad 2020 – Median 70 $ im Jahr unter allen, die überhaupt
  verkauft haben; Etsy 2026 – nur 26 % der Shops mit einem Verkauf in
  30 Tagen.
- Plattform-Freelancing: nur ~10–12 % der unerfahrenen Bewerber bekommen
  überhaupt einen Auftrag (Stanton/Thomas 2016, Pallais 2014).

**2. Der Sommerjob ist schwer zu schlagen.** Ein Industrie- oder Lagerjob
bringt in 9 Wochen ~7.000 € (17–20,50 €/h), vor einem Studium ohne
Sozialabgaben und ohne Einfluss auf die Familienversicherung, ohne
Kapital und ohne Ausfallrisiko. Ein Sommergeschäft muss das erst
einholen. Nach Kosten verdient der Inhaber eines Umzugsteams im Median
~12,50–13 € je eigener Stunde, Spendenwerbung bringt effektiv ~13–15 €/h,
das Webgeschäft im Sommer ~9 €/h.

**3. Die Stunden vor dem Abitur sind schon belegt.** Im Job-Weg füllen
Nachhilfe und Minijob das Stundenbudget fast immer (~15–22 €/h). Jede
Stunde für Aufbau, Tests und Akquise geht davon ab – 50–130 Stunden
kosten so ~800–2.500 €, bevor das Geschäft einen Euro verdient.

**4. Die Familienversicherung ist eine Klippe, keine Grenze.** Alle
Gewinne 2027 zusammen – Nachhilfe, Webgeschäft, das neue Geschäft,
ein Preisgeld – dürfen ~7.080 € nicht übersteigen (12 × 590 €). Danach:
- eigene Kranken- und Pflegeversicherung, mindestens ~282 €/Monat, und
  als freiwilliges Mitglied **auch auf den Lohn des Sommerjobs** (~20,5 %).
  Im Studiums-Fall kosten Juli und August dann je ~930 € statt 0 €.
- Wer das Überschreiten plant, muss es der Kasse melden: Wegfall ab April
  kostet bis 31.08. ~2.200–3.200 €. Mehr Gewinn lohnt sich im
  Studiums-Fall erst ab ~9.500–11.300 € Gesamtgewinn – dazwischen bringt
  mehr Gewinn weniger Geld.
- Wer im Sommer in Vollzeit selbstständig arbeitet (über 30 h/Woche und
  über ~1.030 € Gewinn im Monat), gilt meist als hauptberuflich
  selbstständig – dann entfällt die Familienversicherung für diese Zeit,
  egal wie hoch der Gewinn ist.

**5. Die Erfolgsgeschichten sind der rechte Rand.** Sichtbar sind die,
die durchgehalten haben:
- College Pro: 28 % der Franchisenehmer brachen vorzeitig ab, von den
  übrigen verfehlten 57 % das Umsatzziel. College Works: ~40 % hielten den
  Sommer nicht durch.
- Southwestern (Haustürvertrieb, USA, 2025): Erstjährige im Median ~4 €/h
  nach Kosten; beworbene 24.000–60.000 $ hat die Selbstkontrolle der
  Branche als untypisch beanstandet.
- Gründungen allgemein: ein Drittel gibt in drei Jahren auf (KfW 2025);
  ein Viertel der Selbstständigen verdiente unter Mindestlohn (DIW 2015).

## 2. Alle gerechneten Optionen gegen den Job-Weg

„Mehr als Job“ ist Lauf für Lauf der Unterschied zum Job-Weg, nach Steuer,
Sozialabgaben und Krankenversicherung. Netto zählt wie im Job-Weg, was bis
31.08. verdient ist.

| Option | Median netto | mehr als Job: Median | … Mittel | … gut (10 %) | … Spitze (1 %) | besser in |
|---|---:|---:|---:|---:|---:|---:|
| *Job-Weg allein* | *~11.300 €* | | | | | |
| **Webgeschäft abends neben dem Sommerjob** (~1,6 h je Arbeitstag, Gesamtlast ~50 h/Woche) | 11.400 € | ±0 € | +100 € | +700 € | +1.700 € | 46 % |
| … dasselbe statt der Samstagsschichten (höchstens ~48 h/Woche) | 10.900 € | −400 € | −400 € | +300 € | +1.300 € | 19 % |
| **Startup Teens mit standortcheck**, nur mit Beleg bis 31.01. | 11.200 € | ±0 € | ±0 € | ±0 € | +7.300 € | 4 % |
| **Kombination: Web abends + Startup Teens** | 11.300 € | −200 € | +100 € | +800 € | +7.900 € | 35 % |
| Technik-Flipping neben Schule und Sommerjob | 11.200 € | −400 € | ±0 € | +2.000 € | +4.700 € | 34 % |
| Fotobox-Verleih am Wochenende, neben dem Sommerjob | 10.400 € | −1.100 € | −800 € | +800 € | +3.300 € | 20 % |
| Webgeschäft Vollzeit nur bei Startregel (Test im Winter + Testwoche im Februar), sonst Sommerjob | 10.300 € | −1.100 € | −1.000 € | −300 € | +600 € | 5 % |
| Umzugsteam Fr/Sa + 3-Tage-Sommerjob, nur bei ≥ 10 Anfragen im Feb./März | 10.000 € | −1.300 € | −1.200 € | −200 € | +3.400 € | 9 % |
| Umzugsteam statt Sommerjob, nur bei ≥ 10 Anfragen im Feb./März | 9.800 € | −1.400 € | −1.600 € | −700 € | +4.400 € | 7 % |
| Spendenwerbung angestellt (Reiseteam, Fixum + Prämie) statt Sommerjob | 9.600 € | −1.500 € | −1.600 € | +400 € | +4.100 € | 14 % |
| Webgeschäft an 2 Tagen je Woche + 3-Tage-Sommerjob (16–18 €/h) | 9.300 € | −1.900 € | −1.900 € | −700 € | +600 € | 3 % |
| **Glasfaser-Haustürvertrieb als Handelsvertreter statt Sommerjob** | 9.000 € | −2.200 € | −1.000 € | **+4.900 €** | **+20.600 €** | 24 % |
| … mit Stopp nach Woche 2 unter 250 €/Woche | 9.100 € | −2.200 € | −900 € | +4.900 € | +20.600 € | 24 % |
| Webgeschäft in Vollzeit statt Sommerjob, Abbruch nach 10 Tagen ohne 3 Abschlüsse | 8.100 € | −2.500 € | −3.100 € | −1.300 € | ±0 € | 1 % |
| Umzugsteam statt Sommerjob, ohne Frühindikator | 5.600 € | −5.600 € | −5.000 € | ±0 € | +5.700 € | 10 % |

**So liest man das:**
- **Webgeschäft abends** ist die einzige Ergänzung, die im Mittel etwas
  bringt: kaum Risiko (schlechtestes Zehntel −400 €), die
  Familienversicherung bleibt. Bis 31.08. bringt es wenig, weil Websites
  erst nach Texten und Fotos des Kunden live gehen. Dazu kommen ~300 € für
  Arbeit im September, die hier nicht mitzählen, und vor allem gemessene
  Quoten für das Studium. Es setzt aber voraus, neben dem Vollzeitjob noch
  ~8 Stunden je Woche zu arbeiten; wer stattdessen die Samstagsschichten
  streicht, liegt im Median 400 € unter dem Job-Weg.
- **Startup Teens** ist ein Los: in ~96 % der Fälle 0 bis −700 € (die
  verdrängten Stunden), in ~3 % der Fälle 2.000–10.000 € Preisgeld.
- **Alles, was den Sommerjob ersetzt, verliert im Median** 1.100–5.600 €.
  Die Stufenpläne begrenzen den Schaden, weil das Signal bis 31.03. fast
  immer „Sommerjob“ sagt: beim Umzugsteam in 72 % der Fälle, beim
  Webgeschäft mit Startregel in 99,5 %. Selbst bei grünem Signal verliert
  der Sommer im Median (Umzug −2.400 €, Web −3.000 €); besser als der
  Job-Weg sind dann nur 24 % bzw. 12 % der Fälle.
- **Die Glasfaser-Wette** ist die einzige mit echtem Ausreißer: 1 von 10
  Verläufen bringt mehr als +4.900 €, 1 von 100 mehr als +20.000 €. Dafür
  bricht mehr als die Hälfte ab, und mehr als die Hälfte steht am Ende
  über 2.000 € schlechter da.

**Studium oder duales Studium danach** ändert die Abstände, aber nicht das
Bild. Vor einem dualen Studium kostet der Sommerjob ~21 % Sozialabgaben, er
ist also leichter zu schlagen:

| mehr als Job, Median (gut 10 % / Spitze 1 %) | Studium danach | dual/Ausbildung danach |
|---|---:|---:|
| Webgeschäft abends | ±0 € (+900 / +1.800) | −100 € (+600 / +1.600) |
| Kombination Web abends + Startup Teens | −200 € (+900 / +6.400) | −200 € (+700 / +8.500) |
| Glasfaser-Haustür statt Sommerjob | −2.900 € (+4.700 / +20.300) | −1.800 € (+5.200 / +20.800) |
| Spendenwerbung statt Sommerjob | −1.900 € (+500 / +4.400) | −1.300 € (+300 / +3.400) |
| Umzugsteam statt Sommerjob, Stufenplan | −1.400 € (−800 / +4.000) | −1.300 € (−600 / +4.700) |
| Webgeschäft Vollzeit statt Sommerjob | −3.000 € (−1.700 / −500) | −2.200 € (−1.000 / +200) |

**Gegenproben mit optimistischen Annahmen** (`--gegenproben`):

| Option, optimistisch | mehr als Job: Median | Mittel | gut (10 %) | Spitze (1 %) | besser in |
|---|---:|---:|---:|---:|---:|
| Webgeschäft Vollzeit mit den alten Quoten und Preisen, ohne Sommerflaute | −1.700 € | −1.400 € | +1.300 € | +4.800 € | 21 % |
| Webgeschäft abends, ebenso | +500 € | +600 € | +1.800 € | +3.100 € | 74 % |
| Spendenwerbung mit Firmenangaben und halben Abbrüchen | −1.100 € | −900 € | +1.600 € | +6.700 € | 26 % |
| Glasfaser mit Firmenangaben und halben Abbrüchen | −1.100 € | +1.500 € | +11.200 € | +33.100 € | 41 % |
| Startup Teens mit sehr starkem Projekt | −300 € | +200 € | +1.200 € | +8.700 € | 10 % |

Selbst mit den Zahlen aus der Werbung der Firmen schlägt keine Option, die
den Sommerjob ersetzt, den Job-Weg im Median. Nur die optimistische
Glasfaser-Rechnung ist im Mittel positiv – getragen von wenigen
Ausreißern. Die Spitzenwerte (1 %) der Lose schwanken zwischen Seeds um
etwa ±500 €.

## 3. Der Plan: Job-Weg plus billige Lose

Der Plan aus [`VERDIENST_BIS_SOMMER_2027.md`](VERDIENST_BIS_SOMMER_2027.md)
bleibt die Basis. Dazu kommt nur, was ihn nicht gefährdet:

| Wann | Was | Abbruchregel |
|---|---|---|
| **jetzt bis 31.03.2027** | Sommerjob sichern wie im Job-Weg (Industrie-Ferienarbeit wird Januar bis März vergeben). Unabhängig von allem anderen. | – |
| **Dezember – März** | Wer das Webgeschäft neben Nachhilfe und Minijob betreibt (bringt im Erwartungswert nicht mehr, aber Erfahrung): **jeden Kontakt zählen** – Besuche, Gespräche mit dem Inhaber, bezahlte Einstiege, Pakete, Preis, Stunden. Das ist der Datensatz für alles Weitere. | – |
| **bis 31.01.2027** | Gibt es einen zahlenden Kunden oder einen belastbaren Pilot? Dann den vorhandenen Plan ([`GESCHAEFTSPLAN.md`](GESCHAEFTSPLAN.md)) und das Werkzeug als Businessplan für **Startup Teens** aufbereiten (15–40 h). | ohne Beleg nicht einreichen |
| **März 2027** | Einreichung Bayern-Challenge (Abgabe März, Finale April, 5.000/3.000/2.000 €); denselben Plan im Mai national einreichen (7 Kategorien × 10.000 €, Finale Juni). | ohne Einladung ins Finale keine weiteren Stunden |
| **22.03. – 13.06.** | Abitur. Keine neuen Geschäfte, keine Akquise. | – |
| **28.06. – 31.08.** | Vollzeit-Sommerjob. **Abends ~1–2 h Webgeschäft**: Einstiege liefern, Kontakte pflegen, Pakete für den September annehmen. | Familienversicherung im Blick: alle Gewinne 2027 zusammen unter 7.080 € halten |
| **ab September** | Pakete aus dem Sommer fertigstellen (im Mittel ~300 €), Quoten auswerten, mit Referenzen ins Studium (Abschnitt 6). | – |

**Startregel für alles, was den Sommer kostet** (Umzugsteam, Webgeschäft in
Vollzeit, Provisionsvertrieb): Nur wenn bis 31.03. mindestens 5 bezahlte
Einstiege aus mindestens 100 Kaltkontakten (≥ 5 %), ein bezahltes Paket
ab 1.600 € und mindestens 30 € Umsatz je Stunde stehen. Das erfüllt im
Modell nur 1 von 200 Verläufen – und selbst dann verliert der Sommer im
Median ~3.000 €. Ehrlicher gesagt: den Sommer nicht ins Geschäft stecken.

**Wer bewusst auf den oberen Rand setzen will:** Die einzige Option dafür
ist der Glasfaser-Haustürvertrieb – und nur so:
- nur lokal (R-KOM und Telekom bauen in Regensburg ab 2026 aus, der
  Landkreis Cluster Nord ab Q4 2026), damit keine Unterkunft anfällt;
- nur mit Gewerbeanmeldung und schriftlichem Handelsvertretervertrag ohne
  Stornohaftung über Jahre; Reisegewerbekarte klären;
- vorher bei der Krankenkasse schriftlich klären, ob die Tätigkeit als
  hauptberuflich gilt;
- mit fester Abbruchregel nach Woche 2 und einem Zeitarbeitsjob als
  Rückfall;
- im Wissen: Median −2.200 €, in 54 % der Fälle mehr als 2.000 € weniger.

## 4. Was recherchiert, aber verworfen wurde

| Weg | Ergebnis (bis 31.08.2027) | Grund |
|---|---|---|
| Garten- und Außenpflege-Team statt Sommerjob | Gewinn Median ~4.200 € gegen ~7.000 € Sommerjob; besser in ~18 % | Mitarbeiter-Hebel greift im Median nicht; ~12,50 € je Inhaberstunde |
| Fenster- und Glasreinigung | Median ~3.900 €; besser in ~17 % | Branchenmindestlohn 18,40 € (2026), Saisonspitze in der Prüfungszeit |
| Malerteam nach College-Pro-Art | – | Malerarbeiten sind meisterpflichtig (HwO Anlage A Nr. 10) |
| Event- und Aushilfspersonal vermitteln | – | Arbeitnehmerüberlassung: Erlaubnis und 15.000 € Liquidität nötig; „freie“ Aushilfen wären scheinselbstständig |
| Webagentur, Umsetzung ausgelagert | in ~90 % der Fälle schlechter als selbst bauen | Neulinge verdienen am Bauen, nicht am Vermitteln |
| Nachhilfe-Vermittlung | Median +130 € (Verlust 41–63 %) | ~1 € je vermittelter Stunde; selbst unterrichten bringt 20–30 € |
| Vertriebspartner auf Provision für eine Agentur | Median ~760 € (~3,6 €/h) | nur als Überlauf für Großprojekte |
| Audio-Gästebuch, Gartenfest-Paket, Hüpfburg | Median −360 bis +80 €; Verlust 46–76 % | zu wenig Buchungen im ersten Jahr |
| Fahrrad-Saisonhandel, Abi-Merch für andere Schulen | Median ~140–170 € | Stunden je Rad; Merch-Saison fällt in die Prüfungszeit |
| Abi-Lernmaterial, Website-Check-Abo, digitale Vorlagen, Content | Median −40 bis +110 € | Reichweite fehlt; Verkaufsfenster für Lernzettel nur Dez.–März |
| Automatisierung/KI für Kleinbetriebe | Gewinn ~660 €, aber ~530 € weniger als die verdrängte Nachhilfe | Kaltstart; höchstens als Zusatz für Web-Kunden |
| Programmier-Ferienkurse im August | Gewinn ~1.400 €, aber ~2.150 € unter dem Augustjob | als Februar-Testwoche vertretbar |
| IT-Hilfe für Senioren, Plattform-Freelancing | Median ~350 € bzw. Verlust in 77 % | Satz auf Nachhilfe-Niveau bzw. kein Auftrag |
| Kleingruppen-Nachhilfe, Oster-Crashkurs | Median ±0, gut +280 € | Hebel auf 1,5–3 h/Woche, gedeckelt durch die Rentenversicherung |
| Jugend forscht, Jugend gründet, Gründerpreis für Schüler | erwartetes Preisgeld ~55 € bzw. nur Sachpreise | kein Geld in Bayern |
| Spendenwerbung oder Glasfaser selbstständig ohne Fixum (Wesser-, hsp-Typ) | Median ~4.100 € statt ~6.500 € Sommerjob | Storno, Status-Unsicherheit, Familienversicherung |
| Trading, Glücksspiel | im Schnitt Verlust | siehe [`500K_BIS_SOMMER_2027.md`](500K_BIS_SOMMER_2027.md) |

## 5. Regeln, die jeder Hebel trifft

| Regel | Was sie für ein eigenes Geschäft bedeutet |
|---|---|
| **Familienversicherung** (§ 10 SGB V): Gesamteinkommen höchstens 590 €/Monat (2027), Gewinne als Jahresgewinn / 12; mit Minijob zusammen 633 € | Alle Gewinne 2027 zusammen höchstens ~7.080 €. Die Kasse prognostiziert vorausschauend; ein späterer Steuerbescheid wirkt erst ab dem Folgemonat seiner Ausstellung. Wer ehrlich unter der Grenze prognostiziert und trotzdem darüber landet, verliert sie nicht rückwirkend (BSG 18.10.2022, B 12 KR 2/21 R). Nicht gemeldete, erkennbare Änderungen dagegen schon. Änderungen melden (§ 10 Abs. 6, § 206 SGB V). |
| **Hauptberufliche Selbstständigkeit** (GKV-SV 2019): mehr als 30 h/Woche und mehr als 25 % der Bezugsgröße (~1.030 €/Monat) | Ein Vollzeit-Sommergeschäft beendet die Familienversicherung für diese Zeit, unabhängig vom Gewinn. Vorher schriftlich bei der Kasse klären. |
| **Freiwillige Versicherung 2027:** Mindestbemessung 1.376,67 €/Monat × (14,0 % + Ø-Zusatzbeitrag 2,9 % + Pflege 3,6 %) | mindestens ~282 €/Monat; Beiträge auf alle Einnahmen, auch auf den Lohn einer kurzfristigen Beschäftigung. Im dualen Fall endet sie mit dem berufsmäßigen Sommerjob oder dem Ausbildungsbeginn (dann pflichtversichert). |
| **Mitarbeiter:** kurzfristige Beschäftigung nur für Abiturienten mit Studienabsicht oder Studierende; vor Ausbildung oder dualem Studium berufsmäßig (sozialversicherungspflichtig) | Mindestlohn 14,60 €, gesetzlicher Urlaub (1/12 je vollem Monat), Berufsgenossenschaft, Umlagen, Arbeitszeitaufzeichnung, Sofortmeldung in Gebäudereinigung und Transport. Gegen Industrie-Ferienjobs (18–20 €/h) muss man mitbieten. |
| **Verbraucherverträge** | 14 Tage Widerrufsrecht bei Buchung per Website, Mail oder Telefon (sonst länger). Gebrauchtware: Gewährleistung mindestens 1 Jahr (§ 476 BGB). Marktplätze melden ab 30 Verkäufen oder 2.000 € ans Finanzamt (DAC7). |
| **Steuer** | Gewinn zählt zur Einkommensteuer 2027, zusammen mit Lohn steuerfrei bis ~14.030 € (Entwurf 2027). Kleinunternehmer bis 25.000 € Vorjahresumsatz; Gewerbesteuer-Freibetrag 24.500 €. Preisgeld für einen Businessplan mit dem eigenen Gewerbe ist vermutlich Betriebseinnahme. |
| **Rentenversicherung** | Selbstständige Lehrtätigkeit über 633 €/Monat pflichtig (18,6 %); eine kurzfristige selbstständige Tätigkeit ist frei (§ 8 Abs. 3 SGB IV). |

## 6. Wo der echte Hebel liegt – nach dem 31.08.2027

Die Hebel funktionieren, nur nicht aus dem Stand. Sie brauchen
Referenzen, Kunden und Zeit, und genau die entstehen jetzt:
- **Stundensatz:** Werkstudent IT ~15–16,50 €/h ab der Einschreibung;
  freie Entwickler liegen im Median bei 80–90 €/h – aber 80 % von ihnen
  haben mehr als 10 Jahre Erfahrung (Freelancer-Kompass 2026). Jede
  fertige Website mit zufriedenem Kunden ist eine Referenz.
- **Kunden, die wiederkommen:** Betreuungsverträge (49–89 €/Monat) laufen
  weiter, wenn das Studium in Regensburg ist. Gemessene Quoten aus dem
  Schuljahr und dem Sommer zeigen, ob sich das Webgeschäft im Studium lohnt.
- **Kapital:** ~4.300–5.400 € aus diesem Jahr ins Depot nach der
  Sparregel des [Millionenplans](MILLIONENPLAN.md). Das ist der Hebel,
  der ab dem ersten Tag ohne eigene Stunden arbeitet.
- **Startup Teens:** Ein Preis bringt neben Geld vor allem Kontakte und
  Sichtbarkeit für das Webgeschäft.

## 7. Grenzen dieser Rechnung

- **Quoten und Nachfrage** sind für Neulinge nirgends gemessen. Die
  Webgeschäft-Quoten (Einstieg 0,5–5 % je Kontakt, Upsell 5–30 %, Paket
  800–2.200 €) sind aus Telefon- und Haustürquoten abgeleitet; die
  Gegenprobe mit den alten, optimistischeren Werten ändert das Ergebnis
  nicht.
- **Provisionen:** Die Verdienstangaben der Agenturen sind Eigenwerbung mit
  unbekanntem Nenner („Ø“, „ab“, „oder mehr“); Abbruchquoten sind an
  US-Daten (Southwestern, TCU) verankert. Ob im Sommer 2027 in Regensburg
  Glasfaser vor Ort vermarktet wird, ist offen.
- **Krankenversicherung:** Die Grundsätze des GKV-Spitzenverbands sind
  Empfehlungen; Kassen können abweichen, besonders bei Hauptberuflichkeit
  eines Sommergeschäfts. Die Werte 2027 (Bezugsgröße 4.130 €) sind vom
  Kabinett beschlossen, die Zustimmung des Bundesrats war nicht sicher
  bestätigt.
- **Startup Teens:** Die Zahl der bayerischen Einreichungen ist nicht
  veröffentlicht (geschätzt 150–400); der Qualitätsfaktor ist geschätzt.
- **Optionen sind einzeln gerechnet**, außer der Kombination. Alle
  konkurrieren um dieselben Stunden vor dem Abitur, dieselben
  Sommerwochenenden und denselben Spielraum der Familienversicherung –
  zusammenzählen darf man sie nicht.
- **Netto bis 31.08.** zählt verdiente Arbeit; Websites, die erst im
  September fertig werden, und spätere Betreuungsentgelte stehen getrennt
  als Nachlauf. Die Einkommensteuer auf den Geschäftsgewinn ist abgezogen,
  wird aber erst 2028 fällig.

## 8. Quellen

Zwei Recherche-Runden (rund 30 Wege, ~850 Werkzeugaufrufe), dazu eine
Vollständigkeitsprüfung und eine Prüfrunde des Modells. Die wichtigsten Belege:

**Nachfrage, Basisraten, Survivorship**
- Bitkom/ZDH, Studienbericht Handwerk 2026 (94 % mit Website): https://www.bitkom.org/sites/main/files/2026-01/bitkom-studienbericht-handwerk.pdf
- IHK Regensburg, Unternehmen 01.01.2026 (Stadt 12.386, Landkreis 13.633): https://www.ihk.de/regensburg/hauptnavigation/region/standortinformationen/statistik/der-ihk-bezirk-in-zahlen/ihk-zugehoerige-unternehmen-3814018
- Cognism, Kaltanruf-Quoten 2025: https://www.cognism.com/blog/cold-calling-success-rates
- Planet Argon, Aufträge nach Jahreszeit: https://blog.planetargon.com/entries/putting-pen-to-paper-by-season
- Gumroad 2020: https://siliconflorist.com/2021/01/12/what-happened-in-the-gumroad-creator-community-in-2020/
- Etsy-Snapshot 2026: https://www.insightagent.app/guides/average-etsy-seller-income
- TrustMRR 2026: https://techstartups.com/2026/09/28/what-percentage-of-indie-hacker-products-make-100k-in-arr/
- Linktree Creator Report 2022: https://techcrunch.com/2022/04/20/linktree-creator-economy-report-research/
- Stanton & Thomas 2016 (oDesk): https://researchonline.lse.ac.uk/id/eprint/60609/1/dp1316.pdf
- Pallais 2014 (oDesk-Feldexperiment): https://www.nber.org/papers/w18917.pdf
- Freelancer-Kompass 2026: https://www.freelancermap.de/files/survey/freelancer-kompass-2026.pdf
- JPMorgan Chase Institute, Online-Plattformen: https://www.jpmorganchase.com/institute/all-topics/labor-markets-and-workforce/report-ope-2018
- KfW-Gründungsmonitor 2025: https://www.kfw.de/Über-die-KfW/Newsroom/Aktuelles/Pressemitteilungen-Details_851968.html
- DIW 2015, Selbstständige unter Mindestlohn: https://www.diw.de/de/diw_01.c.513276.de/selbstaendige_beschaeftigung_geht_zurueck.html
- College Pro (Yale): https://thenewjournalatyale.com/2010/02/paint-and-switch/; College Works: https://www.cavalierdaily.com/article/2006/08/college-works-success-or-scam

**Provisionsvertrieb**
- Kober (Fixum 2.700 € / 5 Wochen): https://deinferienjob.com/ und https://www.campusjaeger.de/en/job/101299
- DialogDirect (angestellt, 2.016 € / 4 Wochen): https://www.dialogdirect.de/wk
- Wesser (Ø 740 €/Woche): https://www.wesser.de/faq/; hsp (Mindestprovision): https://www.hsp-derjob.de/geld
- Southwestern Advantage, Disclosure 2025: https://southwesternadvantage.com/disclosure/; DSSRC-Entscheidung: https://truthinadvertising.org/wp-content/uploads/2021/12/Southwestern-Advantage-_-DSSRC-Case-Decision.pdf
- Glasfaser-Haustür (VATM, Provisionen): https://www.teltarif.de/haustuervertrieb-glasfaser-ehrenkodex-vatm/news/92155.html, https://www.stepstone.de/jobs/glasfaser/in-bayern
- Glasfaserausbau Regensburg: https://www.regensburger-nachrichten.de/panorama/98955-glasfaser-auf-dem-vormarsch-ueber-3-000-gebaeude-in-neuen-stadtteilen

**Krankenversicherung und Recht**
- SV-Rechengrößen 2027 (Bezugsgröße 4.130 €): https://www.bmas.de/DE/Service/Gesetze-und-Gesetzesvorhaben/sozialversicherungs-rechengroessenverordnung-2027.html
- Durchschnittlicher Zusatzbeitrag 2027 (2,9 %): https://www.bundesgesundheitsministerium.de/presse/pressemitteilungen/zusatzbeitragssatz-gkv-2027-festgelegt
- GKV-SV, Grundsätzliche Hinweise Gesamteinkommen (29.09.2022): https://www.vdek.com/content/vdeksite/vertragspartner/mitgliedschaftsrecht_beitragsrecht/familienversicherung/_jcr_content/par/download_1642322223/file.res/Grundsaetzliche-Hinweise-Gesamteinkommen-29092022.pdf
- GKV-SV, Hauptberufliche Selbstständigkeit (20.03.2019): https://files.viactiv.de/uploads/sites/11/200319-Hauptberuflich-Selbstständig.pdf
- GKV-SV, Katalog der Einnahmen freiwilliger Mitglieder (26.05.2026): https://www.gkv-spitzenverband.de/media/dokumente/krankenversicherung/grundprinzipien/finanzierung/beitragsbemessung/2026-05-26-katalog-einnahmen-beitragsrechtliche-bewertung-240-sgb-v-bf.pdf
- BSG 18.10.2022, B 12 KR 2/21 R: https://gesetze.co/urteile/B_12_KR_2-21_R
- § 10, § 240 SGB V: https://dejure.org/gesetze/SGB_V/10.html, https://dejure.org/gesetze/SGB_V/240.html
- § 476 BGB (Gewährleistung Gebrauchtware): https://www.gesetze-im-internet.de/bgb/__476.html
- eBay-Gebühren gewerblich, DAC7: https://www.ebay.de/help/selling/fees-credits-invoices/fees-business-sellers?id=4809, https://www.ebay.de/help/selling/selling/eu-dac7-und-das-plattformensteuertransparenzgesetz-meldepflichten?id=5394
- Kleinunternehmerregelung (IHK Regensburg): https://www.ihk.de/regensburg/fachthemen/gruendung/recht-steuern-versicherung/kleinunternehmerregelung-in-der-umsatzsteuer-7028410

**Wettbewerbe und Nachhilfe**
- Startup Teens, Saison 2027: https://www.startupteens.de/news/die-challenge-saison-2027-ist-eroeffnet/; Basisrate 2026: https://startupvalley.news/de/startup-teens-businessplan-challenge-schuelerf/
- Studienkreis Regensburg (Kleingruppe ab 9,41 € je 45 Min.): https://www.studienkreis.de/nachhilfe-regensburg/

**Vermietung** (Angebotsdichte, Stand 22.11.2026)
- Fotobox Regensburg 30 km: https://www.kleinanzeigen.de/s-regensburg/fotobox/k0l7636r30; Gebrauchtmarkt: https://www.kleinanzeigen.de/s-fotobox-dnp/k0
