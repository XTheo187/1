# 500.000 € bis Sommer 2027 – der Plan

**Frage:** Wie komme ich – heute, am 22.11.2026, in der 13. Klasse in
Regensburg, mit ~5.000 € – bis zum **31. August 2027** auf 500.000 €
Nettovermögen? „Andere haben es auch geschafft.“

> **Ja, einzelne haben es geschafft – und fast alle auf demselben Weg.**
> Weltweit fanden sich seit 2012 rund 15–20 Fälle von höchstens
> 20-Jährigen mit ≥ 500.000 in ≤ 18 Monaten – meist als Umsatz, Preisgeld
> oder Einnahmen von Berühmtheiten, selten als Nettovermögen. Wer kein
> Publikum mitbrachte, kam fast immer über **ein Consumer-Produkt mit
> eingebautem Vertriebskanal**: eine KI-Abo-App, die über Kurzvideos und
> Creator verkauft wird (Cal AI, Quittr), oder ein Roblox-Spiel. Das Geld
> wurde aus dem laufenden Umsatz in Werbung gesteckt; ein Vermögen dieser
> Höhe in so kurzer Zeit entstand nur über einen **Verkauf** (Summly, Blue
> Lock: Rivals). Cal AI hatte nach 3–4 Monaten 500.000 $ Umsatz, verkauft
> wurde nach ~19 Monaten.
>
> **Der Plan unten kopiert dieses Muster** Woche für Woche, mit dem Abitur
> als fester Grenze: UG gründen, ab Dezember schnell hintereinander kleine
> KI-Abo-Apps bauen, jede mit Kurzvideos und Creatorn testen, den Treffer
> aus dem Umsatz skalieren und ab Juni auf einen Verkauf hinarbeiten.
> Jede Etappe hat einen festen Messpunkt.
>
> | Chance auf 500.000 € Nettovermögen am 31.08.2027 | |
> |---|---:|
> | mit diesem Plan (Modell, 300.000 Läufe) | **~0,06 % – etwa 1 zu 1.700** |
> | plausible Spanne der Annahmen | 0,01–0,2 % |
> | mit einem erfahrenen Vertriebspartner für höchstens 25 % der Anteile (Wirkung geschätzt) | **~0,17 % – etwa 1 zu 600** |
> | wenn bis 31.03. eine App 30.000 $ im Monat umsetzt | ~10 % |
> | wenn bis 30.04. eine App 100.000 $ im Monat umsetzt | ~35 % |
> | wenn am 28.02. keine App 5.000 $ im Monat umsetzt | ≈ 0 % |
> | wahrscheinlichster Ausgang (Median) | ~3.600 € Verlust, dafür eine eigene App, Daten und Erfahrung |
> | jeder zehnte Lauf / jeder hundertste | ≥ 7.600 € / ≥ 72.000 € Gewinn |
>
> **Das ist die ehrliche Zahl, keine Ausrede.** Der Weg ist echt, aber er
> ist eine Jagd nach einem Treffer: Selbst die Gründer von Cal AI hatten
> sechs Apps davor, rund zehn Jahre Programmierpraxis (seit dem 7.
> Lebensjahr) und einen erfahrenen Mitgründer. Was den Plan trotzdem vernünftig macht:
> - der Einsatz ist klein (~3.000 € plus Zeit);
> - der größte Hebel ist bekannt und planbar: ein Partner, der schon eine
>   App über Creator groß gemacht hat (Abschnitt 4, Partnersuche);
> - nach 14 Wochen weißt du am Messpunkt 28.02., ob du im Rennen bist;
> - das Abitur bleibt geschützt;
> - und im Normalfall bleiben eine App, gemessene Zahlen und Fähigkeiten,
>   die im Studium Geld bringen.

**Gilt für:** volljährig, über einen gesetzlich versicherten Elternteil
familienversichert, kann programmieren (Python; React Native/TypeScript
lernt sich in 2–3 Wochen dazu), ~5.000 € Startkapital, ein iPhone zum
Testen. „Nettovermögen“ heißt hier: Eigenkapital der eigenen UG nach
Steuerrückstellung plus privates Geld – kein reiner Papierwert.

Gerechnet mit `python3 plan/plan_500k.py`. Die Belege stammen aus einer
Recherche mit fünf Teilthemen (Fälle, App-Playbook, andere Wege, Recht und
Steuer, Zeit und Abitur) und einer Gegenprüfung, die die Trefferquoten
verschärft hat (Abschnitt 14).

## 1. Wer es geschafft hat – und was alle gemeinsam haben

| Wer | Alter | Was | Bis 500.000 (Umsatz, Gewinn oder Verkauf) | Wie belegt |
|---|---|---|---|---|
| **Cal AI** (Zach Yadegari, Henry Langmack, mit Blake Anderson, 24, und Jake Castillo, 30) | 17 | KI-Kalorienzähler: Foto vom Essen → Kalorien; Abo 29,99 $/Jahr | Umsatz nach ~3–4 Monaten (Monat 1: 28.000 $, Monat 2: 115.000 $); Gewinn wohl in ~12 Monaten; Verkauf an MyFitnessPal nach ~19 Monaten | gut: CNBC und Fortune sahen Unterlagen, Käufer bestätigt > 30 Mio. $ Jahresumsatz |
| **Quittr** (Alex Slater, mit Connor McLaren, 25) | 19 | Abo-App gegen Pornokonsum (Streaks, Panic-Button) | Umsatz nach ~4–6 Monaten; ~3 Mio. $ Umsatz 2025 erwartet | mittel: Selbstangaben; Datenleck sensibler Nutzerdaten |
| **Summly** (Nick D'Aloisio) | 15–17 | News-Zusammenfassung | Verkauf an Yahoo (~30 Mio. $) nach ~15–20 Monaten, mit Risikokapital | gut |
| **Jailbreak** (Alex Balfanz mit Schulfreund) | 17–18 | Roblox-Spiel | „siebenstelliger“ Gewinn in gut 2 Jahren, geteilt (also länger als 18 Monate) | mittel |
| **Grow a Garden** (anonym) | 16 | Roblox-Spiel, in Tagen gebaut; ein Studio stieg bei ~500 gleichzeitigen Spielern ein | Anteil des Gründers unbekannt; Spitze ~22,3 Mio. gleichzeitige Spieler (August 2025, laut Studio) | Spiel belegt, Einkommen nicht |
| **Blue Lock: Rivals** (anonym, mit Mitentwicklern) | 19 | Roblox-Spiel | Verkauf für > 3 Mio. $ wenige Monate nach dem Start | mittel; fremde Marke, Lizenz fraglich |
| **Herzenskette** (Leon Michel, Deutschland) | 18–19 | personalisierter Schmuck, TikTok-Werbung bis 20.000 €/Tag | 1 Mio. € Umsatz im ersten Jahr | Selbstangabe (OMR) |
| **Cruise Cup** (Michael Satterlee) | 18 | 3D-gedruckte Dosenhülle, Facebook-Werbung | ~570.000 $ Umsatz in 4 Monaten, danach Einbruch auf 25.000 $/Monat | Selbstangabe |

Dazu Fälle, die man nicht planen kann: TikTok-Stars 2019/20 (Addison Rae,
Charli D'Amelio), Lil Nas X, Fortnite-Weltmeister 2019 (3 Mio. $ bzw. je
1,5 Mio. $ für „aqua“), NFT-Künstler in der Blase 2021.

**Was sich wiederholt:**
1. **Ein Massenprodukt für Verbraucher**, kein B2B. Abo-App in einer
   emotionalen Nische (Abnehmen, Sucht, Aussehen) oder Roblox-Spiel.
   B2B-Software, Agenturen, Freelancing oder der Weg von `standortcheck`
   kommen in **keinem** Fall vor.
2. **Vertrieb vor Produkt.** Jeder Treffer hatte einen eingebauten Kanal:
   Kurzvideos und bezahlte Creator, App-Store-Charts oder die
   Roblox-Startseite. Werbung wurde aus dem ersten Umsatz bezahlt; der
   erste Test bei Cal AI kostete ~2.000 $, bei Quittr begann es mit 3.000 $.
3. **Viele Versuche vor dem Treffer.** Cal AI war die 7. App der Gründer
   in rund einem Jahr, Halo AI kam nach 18 Monaten Fehlschlägen, das
   Studio hinter Grow a Garden hatte 30–40 Spiele gebaut.
4. **Jahre Vorübung und meist ein älterer Partner** mit fertigem Playbook
   (Cal AI: Blake Anderson mit RizzGPT und Umax; Quittr: ein
   Marketing-Mitgründer; Roblox: ein Studio).
5. **Vermögen entsteht über einen Verkauf**, selten über angesammelten
   Gewinn: Cal AI gab im Sommer 2025 ~770.000 $ im Monat für Werbung aus
   und behielt ~274.000 $ Betriebsgewinn.

**Der Nenner:** Allein im Januar 2026 starteten ~14.700 neue Abo-Apps.
17 % der neuen Apps erreichen in zwei Jahren 1.000 $ Monatsumsatz, 4,6 %
erreichen 10.000 $ (RevenueCat 2026). Von den Nicht-Spiele-Apps mit Release
2024 kamen weltweit nur ~90 im Startjahr auf ≥ 1 Mio. $ Umsatz, im Schnitt
1,3 Mio. $ (Appfigures). Für 500.000 € netto aus Gewinn braucht es aber
2–5 Mio. $ Kundenumsatz bis August (Abschnitt 2): Das schaffen weltweit vielleicht
1–13 neue Apps im Jahr. Die bekannten Fälle sind Ausnahmen, keine
Stichprobe.

## 2. Was 500.000 € bis 31.08.2027 konkret verlangen

| Weg zum Nettovermögen | nötig bis 31.08.2027 |
|---|---|
| Gewinn bleibt in der UG (Eigenkapital nach ~30,7 % Steuer) | **~720.000 € Gewinn** |
| Gewinn wird privat ausgeschüttet | ~965.000–980.000 € Gewinn (mit Kirchensteuer ~1 Mio. €); als UG müssen 25 % des Jahresüberschusses in die Rücklage (§ 5a Abs. 3 GmbHG), ohne Kapitalerhöhung auf 25.000 € also ~1,3 Mio. € |
| Verkauf der App aus der UG (Asset-Deal), Geld bleibt in der UG | ~720.000 € Kaufpreis |
| Verkauf der UG-Anteile privat (§ 17 EStG, 60 % steuerpflichtig) | ~670.000 € Kaufpreis |
| Verkauf über eine Holding-UG (§ 8b KStG, Geld bleibt in der Holding) | ~508.000 € Kaufpreis |

Steuerlast der UG in Regensburg: Körperschaftsteuer 15 % + Soli = 15,825 %,
Gewerbesteuer 3,5 % × 425 % = 14,875 %, zusammen **30,7 %**.

**Was das für die App heißt:**
- Bei ~17–40 % Marge in der Wachstumsphase (nach 15 % Apple-Gebühr,
  KI-Kosten und 45–70 % für Creator und Werbung) sind für 720.000 € Gewinn
  **1,8–4,2 Mio. € Kundenumsatz** in rund sieben Monaten nötig. Das ist eine Kurve wie bei Cal AI: 30.000 → 100.000 → 300.000 →
  500.000 → 1 Mio. $ Monatsumsatz.
- Für einen Verkauf über ~0,7 Mio. € zahlen Käufer junger Apps 1–3,5 ×
  den Jahresgewinn. Gebraucht werden also ~200.000–700.000 €
  annualisierter Gewinn (beim typischen Faktor 2: ~350.000 €), bei gut
  einem Drittel Marge also ~50.000–160.000 € Monatsumsatz, stabil über
  mehrere Monate. Bereits angesammelter Gewinn senkt den nötigen
  Kaufpreis.
- Daraus folgt die harte Zeitgrenze: **Der Treffer muss bis etwa
  Februar/März da sein.** Kommt er im Juni, bleibt keine Zeit mehr für
  Gewinn oder Verkauf.

## 3. Der Plan auf einer Seite

| Phase | Zeitraum | Ziel | Stunden je Woche | Messpunkt |
|---|---|---|---:|---|
| **A** Gründen, Ideen testen, App 1 bauen, Partner suchen | 23.11.–23.12. | UG, Apple-Konto, 3 Ideen mit Kurzvideos getestet, App 1 im Bau, 20 Partner-Kandidaten angeschrieben | 10 (3–15) | G0 13.12., Ideen-Tor 20.12. |
| **B** Weihnachtsferien | 24.12.–10.01. (Ferien bis Fr 08.01., 24.–26.12. frei) | App 1 eingereicht, App 2 begonnen | 25–50 | G1 Fr 08.01. |
| **C** Launch | 11.01.–07.02. | Funnel messen, erste Creator, Partner-Entscheidung | 10 (3–15) | G2 und Partner-Tor 31.01. |
| **D** Frühjahrsferien | 08.–14.02. (Ferien 08.–12.02.) | Paywall-Tests, Vorrat an Videos, Helfer auswählen | 25–50 | – |
| **E** bis zur Prüfungszeit | 15.02.–21.03. | Treffer skalieren oder App 3 | 10 (3–15) | **G3 28.02. (Haupttor)**, G4 31.03. |
| **F** Abitur | 22.03.–13.06. (mündliche Zusatzprüfungen bis 18.06.) | App läuft mit Helfern und festen Regeln | 0–5 | G5 30.04. |
| **G** Übergang | 14.–27.06. | Android, Studienbewerbung als Rückfall | 15–40 | G6 15.06. |
| **H** Vollzeit | 28.06.–31.08. | Skalieren, Verkauf vorbereiten und abschließen | 45–65 | G7 15.07., G8 31.08. |

**Stundenregel in Schulwochen:** 10 Stunden (Mo–Fr je 1 Stunde, Samstag
5 Stunden), höchstens 15; in Wochen mit Schulaufgaben nur der Samstag
(3 Stunden); nie nach 22 Uhr. Bis zum Haupttor G3 sind das rund 200–250
Stunden. Wer danach weitermacht, kommt bis 31.08. auf rund 800 Stunden,
gut zwei Drittel davon nach dem Zeugnis.

## 4. Woche für Woche

### A – 23.11. bis 23.12.2026: gründen, Ideen testen, App 1 bauen

**KW 48 (23.–29.11.):**
- **UG (haftungsbeschränkt) gründen**: Online-Notartermin mit
  Musterprotokoll, Stammkapital 1.000–2.500 €. Kosten ~375–430 €
  (Notar ~150–200 € brutto mit Auslagen, Handelsregister ~225 €).
- Geschäftskonto eröffnen, Stammkapital einzahlen.
- Domain, einfache Website und Firmen-E-Mail anlegen (Apple verlangt beides
  für Organisationen), ~20–100 €.
- Steuerberater auswählen und Kosten klären: Jahresabschluss,
  Offenlegung und Steuererklärungen der UG kosten ~1.500–3.000 € im Jahr,
  auch ohne Umsatz. Die laufende Buchhaltung kann bis zum ersten Umsatz
  selbst laufen.
- **Entscheidung Holding** (am einfachsten jetzt: erst eine Holding-UG
  gründen, die dann die App-UG gründet – ohne Sperrfrist; später geht es
  nur mit Aufwand, solange die App-UG noch wenig wert ist, über einen
  Anteilstausch mit 7 Jahren Sperrfrist nach § 22 UmwStG): Eine Holding
  senkt den nötigen Kaufpreis bei einem Anteilsverkauf von ~670.000 €
  (privat, § 17 EStG) auf ~508.000 € (§ 8b KStG), kostet aber ~375–430 €
  Gründung und ~1.000–3.000 € im Jahr. Käufer kleiner Apps kaufen meist
  die App (Asset-Deal), dann bringt die Holding nichts. **Empfehlung: eine
  UG, keine Holding.**
- Markenkonten auf TikTok, Instagram und YouTube Shorts anlegen, klar als
  App-Marke erkennbar (Name und Logo der App).
- **Ideensuche** nach den Regeln aus Abschnitt 6: 10 Kandidaten
  sammeln, 3 auswählen.

**KW 49 (30.11.–06.12.):**
- Eintragung ins Handelsregister abwarten (1–3 Wochen); danach
  Gewerbeanmeldung (~55 €), Fragebogen zur steuerlichen Erfassung über
  ELSTER mit USt-IdNr. und **Verzicht auf die Kleinunternehmerregelung**
  (sonst fallen auf Werbung bei Meta und TikTok 19 % Umsatzsteuer ohne
  Vorsteuerabzug an), Transparenzregister.
- **D-U-N-S-Nummer** beantragen (kostenlos, bis 5 Werktage plus 2 bei
  Apple).
- Je Idee 5–7 Kurzvideos im eigenen Markenkonto: das Problem, ein
  „Magic Moment“, Kommentare lesen.
- Expo/React-Native-Vorlage aufsetzen: Kamera oder Eingabe → KI-Aufruf →
  Ergebnis → Paywall. Kernfunktion läuft auf dem Testgerät.

**KW 50 (07.–13.12.):**
- **Apple Developer Program als Organisation** (99 $/Jahr), Paid Apps
  Agreement, Bank- und Steuerdaten (W-8BEN-E), DSA-Händlerangaben,
  **Small Business Program sofort beantragen** (15 % statt 30 %, wirkt
  erst 15 Tage nach Ende des Fiskalmonats der Zusage).
- Google Play als Organisation (25 $ einmalig).
- Stripe-Konto für den US-Web-Checkout.
- Onboarding und Paywall (RevenueCat, Superwall) im Sandbox-Kauf
  lauffähig.
- **G0 (13.12.):** UG eingetragen oder im Verfahren, Apple-Konto
  beantragt, 3 Ideen mit je 10–20 Videos getestet.

**KW 51 (14.–20.12.):**
- Wenn Schulaufgaben anstehen, gilt die Regel: nur der Samstag (3 Stunden).
- **Ideen-Tor 20.12.:** Weiter mit der Idee, die mindestens ein Video über
  100.000 Aufrufe (oder deutlich über dem eigenen Schnitt) und echte
  Kaufabsicht in den Kommentaren hat. Ohne Signal 3 neue Ideen testen –
  aber spätestens jetzt mit dem Bau der besten beginnen.

**KW 52 (21.–23.12.):** drei Schultage, Regel für Schulwochen; ab 24.12.
Ferien.

**Partnersuche (KW 48 bis 31.01., 2–3 Stunden je Woche) – der größte
Hebel des Plans:**
- **Gesucht:** jemand, der schon eine Consumer-App über Kurzvideos und
  Creator auf ≥ 10.000 $ Monatsumsatz gebracht hat – im Gespräch belegt mit
  Zahlen aus App Store Connect oder RevenueCat, nicht nur behauptet. Er
  oder sie bringt Creator-Kontakte, erprobte Formate und 20+ Stunden je
  Woche mit. So sahen die Teams hinter Cal AI und Quittr aus.
- **Wo:** Communities und Podcasts der Abo-App-Szene (RevenueCat Sub Club,
  Superwall), Beiträge von App-Marketern auf X und LinkedIn, Gründerzentren
  der Hochschulen in Regensburg. Je Woche 5 gezielte Nachrichten mit
  eigenen Zahlen (Videos, Aufrufe, später Umsatz) – bis 20.12. also ~20.
- **Angebot:** höchstens 25 % der UG, verdient über 4 Jahre mit 1 Jahr
  Mindestzeit (Vesting über eine notarielle Gesellschaftervereinbarung mit
  Rückkaufrecht; die Übertragung von UG-Anteilen braucht ohnehin den Notar,
  § 15 GmbHG). Alternativ eine Umsatzbeteiligung ohne Anteile, z. B.
  10 % vom Umsatz, solange er oder sie mitarbeitet.
- **Nicht:** Geld vorab, „Kurse“, Agenturen mit Grundgebühr, Partner ohne
  eigene belegte App.
- **Partner-Tor 31.01.:** Wer bis dahin zugesagt hat, wird Gesellschafter
  nach dem Angebot oben. Ohne Zusage läuft der Plan allein weiter; die
  Suche geht nebenbei bis zum G3 weiter.

### B – 24.12.2026 bis 10.01.2027: Weihnachtsferien (bis Fr 08.01.)

- 24.–26.12. frei. Ab 28.12. 9–12 und 14–17 Uhr an der App, 1–1,5 h
  Schule am Tag.
- **12 Stunden für das Sicherheitsnetz:** Bewerbungen auf duale
  Studienplätze und PiBS (Unternehmen suchen ein Jahr vorher, Abschnitt 12).
- App 1 fertig: Onboarding mit Fragen, **harte Paywall** direkt danach
  (ohne Umschalter für die Testphase – Apple lehnt solche „Toggle-Paywalls“
  seit Januar 2026 ab), Wochen- und Jahresabo, Web-Kauf für US-Nutzer,
  Kontolöschung in der App, Datenschutzerklärung.
- TestFlight mit 10–20 Testern; Einreichung bis Mo 04.01.
- **G1 (Fr 08.01.):** App 1 im Review oder live; App 2 begonnen (dieselbe
  Vorlage, andere Nische).

### C – 11.01. bis 07.02.: Launch

- Täglich 1–3 Videos im Markenkonto, **ein Format**, viele Varianten.
- Funnel messen: Aufrufe → Downloads → Onboarding → Paywall → Kauf; daraus
  der **Umsatz je 1.000 Aufrufe (RPM)**.
- KW 02: 10–20 Nano-Creator (unter 10.000 Follower) anschreiben; KW 04:
  3–5 bezahlte, gekennzeichnete Posts zu 50–150 $.
- KW 02–03 (letzte Leistungsnachweise von 13/1, Zeugnis 13/1 am Mo
  25.01.): in Wochen mit Schulaufgaben nur der Samstag.
- **G2 (31.01.):** Irgendeine App ≥ 1.000 $ Monatsumsatz? Messwerte je
  Test (ab ~200.000 Aufrufen): RPM größer als die Creator-Kosten je 1.000
  Aufrufe (~1–3 $), Download → Zahler ≥ 5 %, Testphase → Zahler ≥ 25 %,
  Erstattungen < 5 %. Eine App, die nach 3 Wochen und 2–3
  Paywall-Varianten darunter liegt, wird eingestellt; App 2 startet
  spätestens 15.02.

### D – 08. bis 14.02.: Frühjahrsferien (08.–12.02.)

- Version 1.1 mit Paywall-Test und Teilen-Funktion.
- 40–60 Videos auf Vorrat.
- Helfer per Probeaufgabe auswählen (5–10 Kandidaten je 1–2 Stunden, den
  Besten behalten): Schnitt, Creator-Betreuung, Support.
- Geschlossenen Test im Google Play starten (Android später).

### E – 15.02. bis 21.03.: bis zur Prüfungszeit

- **G3 (28.02.), das Haupttor:** ≥ 5.000 $ Monatsumsatz, Wachstum ≥ 50 %
  im Monat, Werbung in ≤ 4 Wochen zurückverdient.
  - **Verfehlt:** Die 500k-Jagd endet hier. Keine neuen Versuche mehr,
    Werkzeuge kündigen; es bleiben nur das Apple-Konto und die
    Pflichtkosten der UG (~120–250 €/Monat). Die App läuft als kleines
    Projekt weiter, das Abitur hat Vorrang, im Sommer ein Job
    (Abschnitt 12).
  - **Erreicht:** Web-Anteil auf ≥ 30 %, Creator nach dem Prinzip
    „Fixpreis plus garantierte Aufrufe“, Werbung nur aus Umsatz.
- KW 11 „Autopilot“ für das Abitur: Anleitung für den Helfer, Creator
  vorab gebucht und bezahlt, Supabase Pro (pausiert nicht), Alarme bei
  Ausfall und Ablehnung, festes Wochenbudget.
- **G4 (31.03.):** ≥ 10.000 $ Monatsumsatz, besser ≥ 30.000 $. Darunter
  endet die Jagd wie bei G3. Ab 30.000 $: Kohortendaten für Käufer ab jetzt sauber
  sammeln.

### F – 22.03. bis 13.06.: Abitur (mündliche Zusatzprüfungen bis 18.06.)

| Woche | App | Schule |
|---|---:|---:|
| Osterferien (KW 12–13) | ~2 h: 2 × 20 min Zahlen, 1 h Gespräch mit dem Helfer | 35 h |
| KW 14–15 | 2 h | 30 h |
| schriftliches Abitur 21.04.–13.05. | 0–1 h, nur Notfälle | 35 h |
| Pfingstferien 18.–28.05. | 5 h | 20 h |
| Kolloquium bis 11.06. | 2 h | 15–20 h |

- Regel für Ausgaben: je Woche höchstens den Umsatz der Vorwoche.
- Keine Entscheidung darf von dir abhängen, kein Prüfungstermin wird für
  die Firma geopfert.
- **G5 (30.04.):** ≥ 50.000 $ Monatsumsatz (dann ~19 % Chance auf das
  Ziel). Darunter: Ziel beenden.

### G – 14. bis 27.06.: Übergang

- Wer eine mündliche Zusatzprüfung hat, hält die Abiturregel bis 18.06.;
  die Übergangsstunden gelten erst danach.
- Studienbewerbung als Rückfallweg (z. B. TUM Informatik bis 15.07.).
- Android-Start, wenn der geschlossene Test bestanden ist.
- **G6 (15.06.):** ≥ 150.000 $ Monatsumsatz. Dann **Verkauf
  vorbereiten**: Kohorten D1–D90, Erstattungsquote, Kanalmix, Zeitaufwand
  der Gründerin; Gespräche mit App-Portfolio-Käufern und Studios. Ziel ist
  eine Absichtserklärung (LOI). Verfehlt: App auf Gewinn statt Wachstum
  umstellen; das Ziel ist faktisch verfehlt.

### H – 28.06. bis 31.08.: Vollzeit

- Mo–Sa je ~9 Stunden, Sonntag frei.
- Erfolgreiche Creator-Formate verdoppeln, jede Woche ein Paywall-Test,
  Pauschalverträge mit den besten Creatorn, eigene Werbevideos der Creator
  als Anzeigen (Spark Ads) – nur bei Rückverdienst in ≤ 4 Wochen.
- **G7 (15.07.):** ≥ 300.000 $ Monatsumsatz **oder** eine unterschriebene
  Absichtserklärung über einen Kaufpreis, der zusammen mit dem bisherigen
  Gewinn ≥ 720.000 € ergibt (mit Partner: ≥ 720.000 € ÷ eigener Anteil),
  Abschluss bis 25.08. **oder** ≥ 300.000 € aufgelaufener Gewinn. Sonst ist das Ziel verfehlt: App
  behalten, als Geschäft weiterführen, im Herbst den Ausbildungsweg
  antreten.
- **G8 (31.08.):** Eigenkapital nach Steuerrückstellung ≥ 500.000 €
  (offene Forderungen gegen Apple zählen) oder ein abgeschlossener
  Verkauf.

## 5. Die Messpunkte und was sie für die Chance bedeuten

Wie wahrscheinlich das Ziel ist, **wenn** ein Messpunkt erreicht bzw.
verfehlt wird (höchster Monatsumsatz einer einzelnen App in $, gezählt
werden nur volle Wochen bis zum Stichtag; Modell „Der Plan“):

| Messpunkt | so oft erreicht | Chance auf das Ziel, wenn erreicht | … wenn verfehlt |
|---|---:|---:|---:|
| ≥ 1.000 $ bis 31.01. | 6 % | 0,8 % | 0,005 % |
| ≥ 5.000 $ bis 31.01. | 2 % | 2,3 % | 0,007 % |
| **≥ 5.000 $ bis 28.02. (G3)** | 5 % | 1,2 % | **0,001 %** |
| ≥ 10.000 $ bis 28.02. | 1,2 % | 4 % | 0,005 % |
| **≥ 10.000 $ bis 31.03. (G4)** | 3 % | 1,9 % | **< 0,001 %** |
| ≥ 30.000 $ bis 31.03. | 0,4 % | 10 % | 0,02 % |
| **≥ 50.000 $ bis 30.04. (G5)** | 0,2 % | 19 % | 0,01 % |
| ≥ 100.000 $ bis 30.04. | 0,03 % | ~35 % | 0,05 % |
| ≥ 150.000 $ bis 15.06. (G6) | 0,04 % | ~40 % | 0,04 % |
| ≥ 300.000 $ bis 15.07. | 0,02 % | ~37 % | 0,05 % |

**So liest man das:**
- Die Chance wird fast vollständig an den frühen Toren entschieden.
  Wer am 28.02. keine 5.000 $ Monatsumsatz hat, hat das Ziel verfehlt –
  das ist Mathematik, kein Mangel an Einsatz.
- Selbst 100.000 $ Monatsumsatz Ende April bringen das Ziel nur mit rund
  35 % (je nach Annahmen 28–52 %; nur wenige Dutzend Läufe kommen so weit): Es bleiben vier Monate, das Abitur bremst, Apple zahlt 5–9 Wochen
  später aus, und Wachstum frisst die Marge.
- Die stärksten Hebel: **ein erfahrener Vertriebspartner für höchstens
  25 %** (0,055 % → ~0,17 %; bei 40 % Abgabe fällt die Chance auf 0,03 %,
  also unter den Plan ohne Partner), **US-Web-Checkout** (schnelleres Geld,
  geringere Gebühr) und **Tempo der Versuche**. Weniger wichtig: mehr Versuche nach dem Abitur. Im Modell
  heben Web-Checkout, eine wiederverwendete App-Vorlage und volle
  Ferienwochen die Chance von 0,01 % auf 0,055 % – fast auf das Fünffache.

## 6. Die App: Idee, Produkt, Technik

**Die Idee – fünf Prüfungen, bevor gebaut wird:**
1. **Viele Creator in der Nische, wenige Markendeals.** Health & Fitness
   hat die meisten Creator (Cal AI); Astrologie nur wenige hundert, meist
   exklusiv gebunden.
2. **Ein Moment, der sich in drei Sekunden filmen lässt** („Magic
   Moment“): Essen scannen → Kalorien → Reaktion.
3. **Ein Bedürfnis, für das Menschen schon Geld ausgeben** – Aussehen,
   Abnehmen, Gewohnheiten, Lernen, Beziehungen.
4. **Validierung mit Inhalten statt mit Code:** Markenkonto in der Nische,
   5–20 Videos, Kommentare lesen („views can lie“, Kommentare nicht).
5. **Rechtlich sauber:** kein Heilversprechen, kein Medizinprodukt (keine
   Diagnose oder Behandlung von Krankheiten), keine fremden Marken,
   möglichst keine Gesundheits- oder Sexualdaten speichern (Abschnitt 10).

Kein Klon: Apple lehnt austauschbare Kopien und mehrere Bundle-IDs
derselben App ab (Richtlinie 4.3). Jede App braucht eine eigene Funktion.
**Markt:** zuerst Englisch und USA (größter Markt, Web-Checkout erlaubt),
danach Deutsch.

**Das Produkt:**
- Langes, persönliches Fragen-Onboarding, danach die Paywall – im
  Onboarding konvertiert sie fast viermal besser als später.
- Harte Paywall: Download → Zahler im Median 10,7 % (Freemium 2,1 %),
  Umsatz je Download nach 60 Tagen 3,09 $ statt 0,38 $ (RevenueCat 2026).
- Preise testen: Median 5,99 $ je Woche, 34,80 $ je Jahr; Cal AI 29 $ je
  Jahr mit 3 Tagen Test. Längere Testphasen wandeln besser, bei 3 Tagen
  fallen 55 % der Kündigungen auf Tag 0.
- Bindung: Streaks, Erinnerungen, Genauigkeit der Kernfunktion.
- US-Web-Checkout per Stripe (in den USA erlaubt; Apple verlangt
  während des laufenden Verfahrens keine Provision darauf).

**Technik und Kosten (Dezember bis August):**

| Werkzeug | Kosten |
|---|---|
| Apple Developer Program / Google Play | 99 $/Jahr / 25 $ einmalig |
| Claude Pro mit Claude Code (im Sommer Max) | 20 $/Monat (100 $) |
| Expo (Builds in der Cloud, kein Mac nötig) | 0–19 $/Monat |
| Supabase Pro (pausiert nicht) | 25 $/Monat |
| RevenueCat / Superwall | frei bis 2.500 $ bzw. 10.000 $ Monatsumsatz, dann 1 % |
| KI-Modell für Bilder (z. B. Claude Haiku 5.5) | ~10–30 $ je 1.000 aktive Nutzer und Monat |
| Schnitt (CapCut/Canva), Domain | ~12 $/Monat |
| zusammen | **~850 €** |

Teure Modelle (Sonnet-Klasse) sind für Bild-Scans zu teuer, Gratisstufen
mit Datennutzung für Nutzerfotos ungeeignet (DSGVO).

## 7. Vertrieb: Kurzvideos, Creator, Skalierung

1. **Eigene Inhalte (Marge 50–80 %).** Ein Format, viele Posts
   (Halo AI: ein Format, 1,2 Mrd. Aufrufe in 120 Tagen). Konten sind als
   App-Marke erkennbar; keine Konten, die so tun, als wären es
   unabhängige Nutzer.
2. **Creator testen (Marge 25–70 %).** Nano-Creator 50–200 $ je Video,
   Micro 200–800 $; bezahlte Aufrufe über Content-Rewards-Programme ~1 $
   je 1.000 Aufrufe. **Regel von Cal AI: nie mehr je 1.000 Aufrufe zahlen,
   als sie einbringen** (Kosten je 1.000 Aufrufe < RPM).
3. **Skalieren über Creator.** Fixpreis plus garantierte Aufrufe oder
   Videoanzahl (reine Provision lehnen die meisten ab), Wiederbuchung nach
   Ergebnis, eigene Creator-Builds. Cal AI hatte in der Spitze 250
   Creator unter Vertrag, 50–70 posteten am selben Tag.
4. **Bezahlte Anzeigen (Marge 0–30 %)** erst ab ~100.000 $ Monatsumsatz,
   mit Creator-Videos als Anzeigen.
5. **Team:** ein Vertriebspartner von Anfang an (Partnersuche in
   Abschnitt 4), sonst ab ~20.000 € Monatsumsatz ein Creator-Manager gegen
   Honorar oder Umsatzanteil je Kanal. **Keine Firmenanteile über 25 %**:
   Gibt die Gründerin 40 % ab, sinkt die Chance auf das Ziel unter die ohne
   Partner (0,03 % statt 0,055 %), weil die Firma dann 1,2 statt 0,72 Mio. €
   verdienen müsste.

Jeder bezahlte Beitrag wird als **„Werbung“** gekennzeichnet (§ 5a UWG),
mit schriftlichem Vertrag über Nutzungsrechte (Anzeigen, Spark Ads,
Dauer, Gebiet) und Freigabe vor Veröffentlichung.

## 8. Geld: Budget, Cashflow, Finanzierung

**Die 5.000 €** (dieselben Spannen rechnet das Modell):

| Posten | bis zum Haupttor G3 (28.02.) | 01.03.–31.08. |
|---|---:|---:|
| Start: Notar, Register, Gewerbe (~430 €), Website und Rechtstexte (~100–200 €), falls nötig ein gebrauchtes Testgerät (0–350 €) | ~450–1.200 € | – |
| Laufende Kosten: Werkzeuge (Tabelle oben, ~100 €/Monat), Buchhaltung und Steuerberater anteilig, Konto, IHK – zusammen 200–500 €/Monat | ~600–1.500 € | läuft die Jagd weiter, genauso; nach Abbruch nur ~120–250 €/Monat, also ~700–1.500 € |
| **Creator- und Videotests** | **200–1.200 € je App, zusammen höchstens ~1.500 €** | nur aus Umsatz |
| **Reserve** – Tests und Werbung dürfen die Kasse nie darunter drücken | **1.000 €** | |

Ohne jeden Umsatz sind bis zum G3 ~1.300–4.200 € verbraucht, bis 31.08.
nach dem Abbruch weitere ~700–1.500 €. Die Reserve schützt vor
Ausgaben für Tests und Werbung, nicht vor den Pflichtkosten der UG.

**Cashflow – das eigentliche Nadelöhr:** Apple zahlt 5–9 Wochen nach dem
Kauf aus, Creator und Werbung sind sofort fällig. Aus eigener Kraft
wächst eine App so höchstens um das 1,6- bis 2-Fache im Monat
(Werbekosten 45 % vom Umsatz) bzw. 1,15-Fache (70 % mit bezahlten
Anzeigen). Cal AI wuchs um das 2- bis 3-Fache. Ein solcher Treffer
bräuchte auf dem Höhepunkt ~0,3–0,6 Mio. € Vorfinanzierung. Deshalb:
- **Web-Checkout für US-Nutzer** (Geld nach Tagen statt Wochen);
- Creator nach dem Posten bezahlen, Zahlungsziele von Werbekonten nutzen;
- **je Woche höchstens den Umsatz der Vorwoche ausgeben**;
- **keine Kredite** – weder privat noch für die UG.

**Finanzierung, Stand November 2026:**
- Umsatzbasierte Finanzierung für Apps: Pollen VC und Uncapped bieten sie
  nicht mehr an; Lighter Capital und Founderpath sind für eine junge
  deutsche UG nicht zugänglich; Silvr (seit Ende 2025 Karmen) finanziert
  laut eigener FAQ nur in Frankreich registrierte Firmen mit mindestens
  12 Monaten Geschäftstätigkeit. Für diese UG gibt es vor dem 31.08.2027
  also keine Finanzierung; das Modell rechnet ohne.
- Business Angel ab ~20.000 € Monatsumsatz: hilft im Modell kaum, weil
  die Verwässerung den eigenen Anteil am Ziel senkt. Höchstens, wenn der
  Anteil der Gründerin bei ≥ 85 % bleibt.

## 9. Rechtsform, Steuer, Versicherung

| Thema | Regel | Was du tust |
|---|---|---|
| **Rechtsform** | UG (haftungsbeschränkt) mit 1 € bis 24.999 € Stammkapital; 25 % des Jahresüberschusses in die Rücklage (§ 5a GmbHG). GmbH braucht 25.000 €. Einzelunternehmen: unbeschränkte Haftung, Privatadresse öffentlich im EU-App-Store, und für 500.000 € privat ~915.000 € Gewinn | sofort UG mit Musterprotokoll |
| **Steuer** | 30,7 % auf den Gewinn der UG; Ausschüttung zusätzlich 26,375 % (oder Teileinkünfteverfahren); Kirchensteuer 8 % bei Mitgliedschaft | Gewinn in der UG lassen, Steuer für 2027 zurücklegen |
| **Umsatzsteuer** | Apple und Google verkaufen im eigenen Namen (Kommissionär, EuGH C-101/24); deine Leistung an sie ist in Deutschland nicht steuerbar. Eigener Web-Checkout an EU-Kunden: ab 10.000 € Auslandsumsatz OSS | auf die Kleinunternehmerregelung verzichten; Web-Checkout zuerst nur für US-Nutzer |
| **Apple-Gebühr** | 15 % im Small Business Program bis 1 Mio. $ Erlös nach Provision; darüber für den Rest des Jahres 30 % (EU seit 01.10.2026: 15 % bzw. 26 % beim In-App-Kauf) | Programm sofort beantragen |
| **Familienversicherung** | Einbehaltene Gewinne der UG zählen nicht zum Gesamteinkommen; Gehalt über ~690 €/Monat (590 € plus Arbeitnehmer-Pauschbetrag) und Ausschüttungen über ~8.080 €/Jahr schon. Ob du hauptberuflich selbstständig bist, prüft die Kasse nach Stunden **und** Arbeitseinkommen (GKV-Spitzenverband, Grundsätze vom 20.03.2019): bei mehr als 30 h/Woche in der Regel schon ab einem Arbeitseinkommen über 25 % der Bezugsgröße (2027 ~1.030 €/Monat), bei 20–30 h ab 50 % (~2.065 €), bei bis zu 20 h erst ab 75 % (~3.100 €). Einbehaltene UG-Gewinne sind kein Arbeitseinkommen; ohne Gehalt spricht die Regel also eher gegen Hauptberuflichkeit, die Kasse entscheidet aber im Einzelfall. Liegt sie vor, endet die Familienversicherung unabhängig vom Einkommen | kein Gehalt, keine Ausschüttung 2027; in Schulwochen unter 20 h; die Ferienwochen mit mehr Stunden (Weihnachten, Februar, ab Mitte Juni) und den Vollzeitsommer **vor den Weihnachtsferien** schriftlich mit der Kasse klären; für den Fall der Fälle ~280–290 €/Monat einplanen |
| **Rentenversicherung** | Geschäftsführerin mit ≥ 50 % Anteil nicht abhängig beschäftigt; Ein-Personen-GmbH mit einem Auftraggeber kann rentenversicherungspflichtig sein (ob Apple als „ein Auftraggeber“ gilt, ist offen) | Steuerberater oder DRV fragen |
| **Schule** | keine Genehmigung nötig; Unterrichtspflicht und Prüfungen gehen vor (Art. 56 BayEUG) | Termine nachmittags oder in den Ferien |
| **Kindergeld** | während der Schulzeit unabhängig vom Einkommen | – |

Laufende Kosten der UG: Jahresabschluss, Offenlegung und
Steuererklärungen ~1.500–3.000 € im Jahr auch ohne Umsatz, mit
laufender Buchhaltung bei Umsatz ~3.000–6.000 €; IHK-Beitrag: Grundbeitrag
85 € (Gewerbeertrag bis 100.000 €, darüber 125/300/500 €) plus Umlage
0,09 % des Gewerbeertrags, ohne Freibetrag für die UG.

## 10. Recht beim Wachsen

- **Werbung:** Kennzeichnung „Werbung“ oder „Anzeige“ am Anfang
  (§ 5a Abs. 4 UWG, § 22 MStV); die UG haftet für ihre Creator
  (§ 8 Abs. 2 UWG). Keine gekauften oder gefälschten Bewertungen
  (UWG Anhang Nr. 23b/c, Apple 5.6.3), keine Kaufaufforderung an Kinder
  (UWG Anhang Nr. 28), nur lizenzierte Musik.
- **Abos:** Apple-Regeln 3.1.2 (laufender Nutzen, klare Preise, kein
  Lockangebot). Bei eigenen Web-Abos: Kündigungsbutton (§ 312k BGB),
  Widerrufsbutton (§ 356a BGB seit 19.06.2026), „zahlungspflichtig
  bestellen“, Gesamtpreise; in den USA Auto-Renewal-Gesetze.
- **Datenschutz:** Datenschutzerklärung in App und App Store Connect,
  Kontolöschung in der App, Einwilligung für Tracking (§ 25 TDDDG),
  Auftragsverarbeitungsverträge. Gewicht und Gesundheitsziele können
  Gesundheitsdaten sein (Art. 9 DSGVO): ausdrückliche Einwilligung,
  Folgenabschätzung, gute Sicherheit – Quittr legte die Daten von
  Hunderttausenden offen.
- **KI-Verordnung:** seit 02.08.2026 Hinweis auf KI im Chat,
  Kennzeichnung realistischer KI-Bilder und -Videos auch in Anzeigen
  (Art. 50).
- **Gesundheitsaussagen:** Software mit medizinischer Zweckbestimmung ist
  ein Medizinprodukt (MDR); beim Abnehmen sind Gerichte streng
  (Heilmittelwerbegesetz). Keine Aussagen wie „heilt“ oder Vorher-nachher-
  Versprechen.
- **Jugendschutz:** Altersfreigabe korrekt, keine Anzeigen für unter
  16-Jährige; bei minderjährigen Creatorn die Eltern einbeziehen.

## 11. Abitur-Schutz

- **Regel:** in Schulwochen 10 Stunden (Mo–Fr je 1 Stunde, Samstag
  5 Stunden), höchstens 15; in Wochen mit Schulaufgaben nur der Samstag
  (3 h); in der Abiturzeit 0–5 h nach der Tabelle in Phase F; keine
  App-Arbeit nach 22 Uhr. In 42 von 48 Studien zeigt sich zumindest
  teilweise ein negativer Zusammenhang zwischen Nebenarbeit und
  Schulerfolg; viele finden Schaden erst ab einer Schwelle, die je nach
  Studie zwischen über 8 und über 25 h/Woche liegt (Übersicht IZA
  DP 11023). Je weniger Stunden in Schulwochen, desto kleiner das Risiko.
- **Die Note ist noch beweglich:** Am 22.11.2026 sind rund 600 von 900
  Punkten offen; 18 Punkte entsprechen 0,1 Notenstufen. Sie zählt für
  NC-Studiengänge, Eignungsverfahren (z. B. TUM Informatik) und duale
  Plätze – dauerhaft.
- **Die Kollision, ehrlich:** Die Monate, in denen ein Treffer am meisten
  Arbeit braucht (Februar bis Juni), fallen genau auf 13/2 und die
  Prüfungen. Entweder läuft die App dann mit Helfern, die sich aus dem
  Umsatz tragen, oder sie pausiert 12 Wochen.
- Im Modell kostet strenger Abiturschutz (6–10 statt 8–22 Stunden in
  Schulwochen) rund ein Drittel der Chance: ~0,04 % statt ~0,06 %
  (Abschnitt 14).

## 12. Sicherheitsnetz

Weil der Plan fast sicher das Ziel verfehlt, läuft daneben, was danach
trägt:
- **Bewerbungen in den Weihnachtsferien** (12 h): duale Studienplätze
  Informatik/Wirtschaftsinformatik und PiBS in der Schweiz; FH-Bachelor
  als Rückfall (Bewerbung bis Mitte Juli).
- **Sommer:** Ist G4 (31.03.) verfehlt, statt Vollzeit-App ein Sommerjob
  (Zeitarbeit ist kurzfristig zu bekommen; ~6.000–7.000 € netto, siehe
  [`VERDIENST_BIS_SOMMER_2027.md`](VERDIENST_BIS_SOMMER_2027.md)). Die App
  läuft abends weiter.
- **Geld:** Reserve 1.000 € bleibt, Gewinne nach der Sparregel des
  [Millionenplans](MILLIONENPLAN.md) ins Depot.

Mit dem Millionenplan (PiBS oder dual, sonst FH-Bachelor; Schweiz wenn
möglich; Sparregel) sind 500.000 € Nettovermögen so wahrscheinlich
(`python3 plan/simulation.py --zeitplan --ziel 500000`):

| Jahr (Alter) | Chance auf 500.000 € |
|---|---:|
| 2027 (19) | ≈ 0 % |
| 2038 (30) | 0,5 % |
| 2043 (35) | 9 % |
| 2048 (40) | 26 % |
| **2055–2056 (47–48)** | **50–53 %** |
| 2065 (57) | 73 % |

## 13. Andere Wege im Vergleich

| Weg | Chance auf 500.000 € bis 31.08.2027 | Was man riskiert |
|---|---:|---|
| **KI-Abo-Apps nach dem Muster (dieser Plan)** | ~0,06 % (0,01–0,2 %) | ~3.000 € und Zeit; im Normalfall ~3.600 € Verlust |
| Roblox-Spiele in Sprints (8–12 Spiele, Studio als Partner oder Käufer) | ~0,06 % (0,02–0,17 %) | Zeit, ~500–1.500 € Werbetests |
| App als Hauptweg + 2–4 Roblox-Sprints in den Ferien | ~0,04–0,05 % | teilt die Zeit, deshalb nicht mehr |
| Steam-Indie-Spiel (ein Release bis Juli) | ~0,02 % | Zeit |
| Fortnite-Inseln, Plattform-Töpfe, Bug-Bounties, TikTok-Shop-Marke | 0,001–0,05 % | Zeit bzw. Kapital |
| B2B-Software aus `standortcheck`, Agentur, Kurse, Newsletter, Chrome-Erweiterungen | < 0,01 % | Zeit |
| **Einmalige Wette mit Index-Optionen** (5.000 €, Basispreis ~40 % über dem Index) | ~0,1–0,5 % | die 5.000 € in > 99 % der Fälle |
| Roulette, kühnes Spiel, mit Tischlimit | ~0,65–0,7 % | 5.000 € in > 99 % der Fälle |
| Nur Papierwert (Anteil × Bewertung bei YC oder Angel) | 1–3 % | kein Geld: nicht verkäuflich, Vesting, Anwesenheit in San Francisco |

Die Zahlen für Roblox, Steam und die übrigen Wege stammen aus der
Recherche (Basisraten, Schätzung) und sind nicht mit den Stundenregeln
dieses Plans simuliert; mit Abiturschutz lägen sie ähnlich niedriger wie
die App-Zahl.

**Warum der App-Weg trotz kleinerer Zahl als die Wetten der Plan ist:**
Er ist der Weg, den die realen Fälle gegangen sind; im Median kostet er
gut 2.000 € statt der ganzen 5.000 €; er ist kein Glücksspiel; und im
Normalfall bleibt etwas: eine App, gemessene Zahlen, Fähigkeiten,
Referenzen. Beides gleichzeitig geht nicht – die Optionswette bräuchte
genau das Geld, das die Tests brauchen.

**Die Grenze bei Wetten** (beweisbar, Ville-Ungleichung): Bei jedem Spiel
ohne eigenen Vorteil ist die Chance, aus 5.000 € jemals 500.000 € zu
machen, höchstens 5.000 / 500.000 = 1 %. Kredit hebt sie nur scheinbar:
Dann verliert man in den übrigen 99 % mehr, als man hat. Die Optionswette
(Calls auf den S&P 500 mit Verfall nach dem Stichtag, Basispreis ~40 % über
dem Stand vom 20.11.2026; Ziel ~677.000 € brutto vor 26,375 %
Abgeltungsteuer) braucht einen Indexanstieg von ~50 % in neun Monaten; der
Markt preist das mit 0,2–0,5 %. Wer sie trotzdem will: einmal kaufen, nie
nachkaufen, nie mit Kredit, bei ~677.000 € sofort verkaufen, spätestens
am 31.08.2027 alles verkaufen. **Nicht empfohlen.**

## 14. Die Rechnung

`plan/plan_500k.py` rechnet 39 Wochen ab 30.11.2026, je Lauf bis zu 3–8
Apps nacheinander, mit den Regeln dieses Plans:
- **Zeit nach dem Wochenplan:** Schulwochen 3–13 h (Modus 10), Weihnachts-
  und Frühjahrsferien 25–50 h, Abiturzeit nach Tabelle F (Osterzeit 1–5 h,
  schriftlich 0–1 h, Pfingsten und Kolloquium 1–5 h), Übergang 15–40 h, ab
  28.06. 45–65 h; je Woche zusätzlich ±20 %. Die Woche ab 21.12. zählt als
  Schulwoche, die Frühjahrsferien liegen auf 08.–12.02.
- **Bau und Test:** erste App 50–130 h, jede weitere 25–70 h; App Review
  0,3–3 Wochen; Test 30–80 h über 2–5 Wochen mit 200–1.200 € für Creator.
- **Tore:** Hat am 28.02. (G3) keine App 5.000 $ Monatsumsatz oder am
  31.03. (G4) keine 10.000 $, endet die Jagd: keine neuen Versuche,
  laufende Kosten sinken auf 120–250 €/Monat.
- **Treffer:** je App eine latente Spitzen-MRR; Chance auf ≥ 1.000 $
  10–30 %, ≥ 10.000 $ 2–8 %, davon ≥ 100.000 $ 5–22 %, davon ≥ 1 Mio. $
  3–15 %, darüber Pareto. Lernkurve: die ersten drei Versuche mit 30 %,
  60 % und 85 % der vollen Chance.
- **Wachstum** eines Treffers mit dem 1,5- bis 3-Fachen im Monat bis zur
  Spitze, Plateau 4–26 Wochen, danach −2 bis −15 % im Monat; 5–20 %
  Risiko eines Einbruchs (Kopie, Ablehnung, Plattform).
- **Kosten:** 30–65 % vom Umsatz beim Wachstum über Creator, 55–85 % mit
  bezahlten Anzeigen, 35–60 % auf dem Plateau; Apple 15 %, über 870.000 €
  30 %; Start 450–1.200 €, laufend 200–500 €/Monat.
- **Cashflow:** Apple-Auszahlung nach 5–9 Wochen, 30–60 % Web-Checkout mit
  einer Woche, Creator und Werbung nach 0–3 Wochen fällig. Kein Kredit,
  keine Finanzierung; Tests und Wachstum dürfen die Kasse nicht unter die
  Reserve von 1.000 € drücken, sonst wird das Wachstum gedrosselt.
- **Verkauf:** ab 16 Wochen App-Alter zum 1- bis 3,5-Fachen des
  annualisierten Gewinns, aber nur, wenn er zusammen mit dem bisherigen
  Gewinn das Ziel erreicht; Abschluss nach 4–14 Wochen mit 30–70 %
  Wahrscheinlichkeit.
- **Partner:** sagt in einer Woche zwischen Start und 31.01. zu und
  arbeitet ab dann mit: Trefferquoten zwischen Recherche und Gegenprüfung
  ohne Lernkurve, höherer Startumsatz eines Treffers, günstigere Creator,
  20–50 eigene Stunden je Woche für Bau, Test und Skalierung. Bezahlt wird
  er mit Anteilen oder mit 10 % vom Umsatz.
- **Prüfungen:** In jedem Lauf gilt Gewinn = Kasse − Startkapital + offene
  Forderungen − offene Rechnungen (Test `test_kassenprobe`).

| Szenario (300.000 Läufe) | Chance auf das Ziel | Gewinn im Median |
|---|---:|---:|
| Trefferquoten der Recherche | 0,13 % | −2.000 € |
| strengere Quoten (Gegenprüfung) | 0,05 % | −3.400 € |
| strengere Quoten + Lernkurve | 0,01 % | −4.200 € |
| **Der Plan** (+ Web-Checkout, schneller Bau, volle Ferien) | **0,055 %** | −3.600 € |
| der Plan mit strengem Abiturschutz (6–10 h in Schulwochen) | 0,04 % | −4.200 € |
| der Plan, optimistischer Rand (Quoten × 1,5) | 0,10 % | −2.800 € |
| Partner mit Vertrieb (geschätzt), Anteil der Gründerin 100 % | 0,70 % | −300 € |
| … Anteil der Gründerin 75 % | **0,17 %** | −300 € |
| … Anteil der Gründerin 60 % | 0,03 % | −200 € |
| Obergrenze: die erste App ist ein Cal-AI-Treffer | 34 % | +211.000 € |

**Was die Zahlen sagen:**
- Gewinn allein schafft das Ziel praktisch nie (die Wachstumsphase frisst
  die Marge); fast alle Erfolge laufen über einen Verkauf im Sommer.
- Selbst ein Treffer der Cal-AI-Klasse als erste App bringt das Ziel nur
  mit rund einem Drittel: Zeit, Vorfinanzierung und Abitur bremsen.
- Eine unabhängige Zerlegung nach Basisraten (statt Simulation) kommt im
  Median auf ~0,014 % (P10 0,001 %, P90 0,07 %). Mit allen Hebeln zugleich
  und ohne Abgabe von Anteilen lässt sich aus Basisraten höchstens rund
  0,5 % begründen.

**Grenzen:**
- Fast alle Erfolgszahlen sind Selbstangaben (Podcasts, Interviews); sauber
  belegt ist nur Cal AI. Die Trefferquoten je Versuch sind Schätzungen,
  kalibriert an RevenueCat und Appfigures; 2027 dürfte die Konkurrenz
  größer sein als 2024.
- Die Wirkung eines erfahrenen Partners ist nicht messbar, nur geschätzt
  (Modell: Trefferquoten zwischen Recherche-Basis und Gegenprüfung ohne
  Lernkurve, höherer Startumsatz, günstigere Creator, 20–50 Partnerstunden
  je Woche). Ob sich ein solcher Partner findet, ist offen.
- Umsatz aus Jahresabos wäre nach HGB abzugrenzen (der Modellgewinn ist
  dafür nicht korrigiert); Monte-Carlo-Fehler bei 0,06 % rund ±10 %
  relativ.

## 15. Was du nicht tun solltest

- **Keine Kredite** für Werbung oder Wetten, keine Bürgschaften.
- **Keine Firmenanteile über 25 %** an Helfer oder Partner abgeben.
- **Keine Täuschung:** keine Fake-Bewertungen, keine verdeckte Werbung,
  keine Konten, die unabhängige Nutzer vortäuschen, keine geschönten
  Kennzahlen gegenüber Käufern (Roy Lee gab überhöhte Umsatzzahlen zu).
- **Keine Memecoins, kein Krypto-Hebel, keine Signalgruppen oder
  „Trading-Kurse“**, keine Glücksspielanbieter ohne deutsche Erlaubnis
  (Whitelist der GGL; schon die Teilnahme ist nach § 285 StGB strafbar),
  bei Finanz- und Kryptoprodukten nur Anbieter mit BaFin-Erlaubnis bzw.
  EU-Zulassung.
- **Keine fremden Marken** ohne Lizenz (Blue Lock), keine sensiblen Daten
  ohne Sicherheit (Quittr).
- **Nicht das Abitur riskieren** – kein Prüfungstermin für die Firma.
- Wenn der Gedanke an den „einen großen Wurf“ nicht loslässt: kostenlose
  Hilfe und Beratung gibt es bei check-dein-spiel.de. Die Spielersperre
  (OASIS) beantragst du kostenlos online beim Regierungspräsidium
  Darmstadt oder bei einem zugelassenen Anbieter; wie das geht:
  <https://www.check-dein-spiel.de/hilfe-fuer-spieler/sich-sperren/>.

## 16. Nachrechnen

```
python3 plan/plan_500k.py                      # Szenarien und Messpunkte (60.000 Läufe)
python3 plan/plan_500k.py --n 300000           # wie im Dokument (rund eine halbe Stunde)
python3 plan/plan_500k.py --nur "DER PLAN"     # nur der Plan
python3 plan/simulation.py --zeitplan --ziel 500000   # Abschnitt 12
python3 -m unittest discover -s tests
```

## 17. Quellen

**Fälle**
- Cal AI: CNBC/Benzinga <https://www.benzinga.com/news/topics/25/10/48148366/lessons-well-learned-this-18-year-old-learned-to-code-at-age-7-now-his-ai-app-makes-1-4-million-per-m>;
  Fortune <https://fortune.com/2025/09/27/gen-z-founder-treats-college-like-vacation-30-million-app-by-18/>;
  Verkauf an MyFitnessPal <https://techcrunch.com/2026/03/02/myfitnesspal-has-acquired-cal-ai-the-viral-calorie-app-built-by-teens>;
  Influencer-Playbook <https://www.netinfluencer.com/cal-ai-founder-zach-yadegari-breaks-down-the-influencer-playbook-behind-his-apps-growth/>;
  Jake Castillo (RevenueCat Sub Club) <https://www.revenuecat.com/blog/growth/jake-castillo-cal-ai-sub-club-podcast-2026>
- Blake Anderson (RizzGPT, Umax): <https://www.starterstory.com/stories/he-made-10m-with-3-iphone-apps>, <https://whop.com/blog/looksmaxxing-blake-anderson/>
- Quittr: <https://theweek.com/health/the-app-tackling-porn-addiction>; Datenleck <https://404media.co/viral-quittr-porn-addiction-app-exposed-the-masturbation-habits-of-hundreds-of-thousands-of-users>
- Halo AI (Superwall-Podcast): <https://www.buzzsprout.com/2522779/episodes/18958462-dillion-verma-0-to-300k-mo-in-45-days-with-my-ai-app-just-copy-me>
- Summly: <https://www.nbcnews.com/business/business-news/yahoo-buys-startup-run-british-teen-millions-flna1C9075778>
- Roblox: Jailbreak <https://www.cnbc.com/2019/09/23/college-student-video-game-creator-made-millions-from-jailbreak.html>;
  Grow a Garden <https://fortune.com/2025/07/30/roblox-video-game-grow-a-garden-viral-summer-hit/>, <https://gamesbeat.com/janzen-madsen-interview/>;
  Verkäufe von Spielen <https://www.thestar.com.my/tech/tech-news/2025/07/14/roblox-game-buying-frenzy-is-turning-teens-into-millionaires>;
  Auszahlungen 2026 <https://about.roblox.com/newsroom/2026/09/global-impact-of-creation-on-roblox>, <https://www.dexerto.com/roblox/robloxs-top-creators-average-65-7-million-a-year-but-most-make-far-less-3408675/>;
  DevEx <https://create.roblox.com/docs/production/monetization/developer-exchange>
- Herzenskette (OMR): <https://omr.com/de/daily/herzenskette-tiktok-leon-michel>; Cruise Cup: <https://www.entrepreneur.com/business-news/this-teen-entrepreneur-viral-product-brings-in-300000-a-month>
- Fortnite-Auszahlungen 2024: <https://www.tubefilter.com/2025/01/23/fortnite-epic-games-creator-payouts-2024/>

**Basisraten und Kennzahlen**
- RevenueCat State of Subscription Apps 2026: <https://www.revenuecat.com/state-of-subscription-apps>, <https://9to5mac.com/2026/03/04/new-report-looks-into-the-sustainability-of-the-subscription-app-market-for-2026/>;
  2025: <https://www.revenuecat.com/blog/company/the-state-of-subscription-apps-2025-launch>
- Appfigures, neue Millionäre 2024: <https://appfigures.com/resources/insights/20250124>
- Adapty 2026 (Paywalls, Erstattungen): <https://adapty.io/state-of-paywalls-2026/>, <https://adapty.io/blog/refund-rate-metrics-and-benchmarking/>
- Toggle-Paywall: <https://www.revenuecat.com/blog/growth/rip-toggle-paywall>
- Creator-Preise: <https://influencermarketinghub.com/influencer-rates/>, <https://billo.app/pricing/>, <https://whop.com/blog/content-rewards/>
- Verkauf von Apps: <https://www.feinternational.com/blog/how-to-sell-a-mobile-app>, <https://flippa.com/lps/insights-report-h12026>

**Apple, Google, Zahlungen**
- Small Business Program: <https://developer.apple.com/app-store/small-business-program/>; Auszahlungen: <https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments>
- Review-Richtlinien (3.1.2, 4.3, 5.1.1, 5.6.3): <https://developer.apple.com/app-store/review/guidelines/>
- DSA-Händlerangaben: <https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements/>
- US-Link-outs (Epic-Verfahren): <https://9to5mac.com/2026/05/04/apple-files-for-supreme-court-stay-in-epic-case-over-off-app-store-commission-dispute/>
- Google Play Tests und Gebühren: <https://support.google.com/googleplay/android-developer/answer/14151465>, <https://support.google.com/googleplay/android-developer/answer/112622>
- Silvr (Finanzierung, Bedingungen): <https://silvr.co/faq>; Uncapped ohne RBF: <https://weareuncapped.com/blog/uncapped-remove-rbf-offering>

**Recht und Steuer**
- UG: § 5a GmbHG <https://www.gesetze-im-internet.de/gmbhg/__5a.html>; Holding: § 8b KStG; Anteilsverkauf: § 17, § 3 Nr. 40 EStG; Sperrfrist § 22 UmwStG
- Körperschaftsteuer ab 2028 sinkend: § 23 KStG (BGBl. I 2025 Nr. 161); Hebesatz Regensburg 425 % (Haushaltssatzung 2026)
- Familienversicherung: § 10 SGB V <https://dejure.org/gesetze/SGB_V/10.html>; GKV-SV, Hauptberufliche Selbstständigkeit <https://files.viactiv.de/uploads/sites/11/200319-Hauptberuflich-Selbstständig.pdf>; Gesamteinkommen <https://www.vdek.com/content/vdeksite/vertragspartner/mitgliedschaftsrecht_beitragsrecht/familienversicherung/_jcr_content/par/download_1642322223/file.res/Grundsaetzliche-Hinweise-Gesamteinkommen-29092022.pdf>
- Werbung: § 5a UWG <https://www.gesetze-im-internet.de/uwg_2004/__5a.html>; FTC Endorsement Guides <https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides>
- Abos: § 312k BGB <https://www.gesetze-im-internet.de/bgb/__312k.html>
- Umsatzsteuer bei App-Stores: EuGH 09.10.2025, C-101/24 (Xyrality)

**Zeit und Abitur**
- Nebenarbeit und Schulleistung (48 Studien): <https://docs.iza.org/dp11023.pdf>
- Gesamtqualifikation und Bestehen: <https://www.gesetze-bayern.de/Content/Document/BayGSO-53>, <https://www.gesetze-bayern.de/Content/Document/BayGSO-54>
- Ferientermine Bayern: <https://www.km.bayern.de/ministerium/termine/ferientermine.html>
- KI beim Programmieren (RCTs): <https://arxiv.org/abs/2302.06590>, <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>

**Wetten und Grenzen** (frühere Fassung dieses Dokuments): Ville-Ungleichung,
Dubins & Savage, Browne (1999) – siehe Abschnitt 10 des
[Millionenplans](MILLIONENPLAN.md#10-quellenverzeichnis); SPY-Optionskette
(Abruf 20.11.2026) <https://api.nasdaq.com/api/quote/SPY/option-chain?assetclass=etf&limit=500&fromdate=2027-09-17&todate=2027-09-30&excode=oprac&callput=callput&money=all&type=all>;
Turbos (BaFin) <https://www.esma.europa.eu/sites/default/files/2025-11/ESMA35-243228190-7836_ESMA_opinion_on_BaFin_PI_measures_on_turbos.pdf>.
