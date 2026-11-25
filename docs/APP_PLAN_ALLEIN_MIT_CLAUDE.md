# App-Plan allein mit Claude – mit deinen echten Angaben

**Für wen:** dich. Du bist 18 und wirst im Dezember 19, gehst in die
13. Klasse eines Gymnasiums in Niedersachsen und machst 2027 Abitur. Danach
willst du Informatik an der ETH Zürich studieren (Studienbeginn 20.09.2027).
Du setzt **insgesamt höchstens 5.000 €** ein, lieber weniger, und zwar
einschließlich allem, was nach dem Sommer noch kommt. Programmieren kannst
du nicht. Du hast ein iPhone, ein iPad und einen Windows-PC. Dein Claude-Max-Abo
läuft noch ein paar Tage. Du willst dich nicht zeigen und deine Identität so
wenig wie möglich preisgeben. Du wohnst bei deinen Eltern, sie wissen
Bescheid, und du bist über sie gesetzlich familienversichert.

Claude schreibt den Code und erklärt ihn dir, macht Texte, Recherche und
Auswertungen. Du lernst die Grundlagen, prüfst, testest, entscheidest und
trägst die Verantwortung. Gerechnet ist alles mit
[`plan/plan_500k.py`](../plan/plan_500k.py), Szenarien „Deine Angaben“ und
„Hebel“.

**Stand 24.11.2026.** Die Zahlen sind neu gerechnet: mit den geprüften Hebeln
(Kosten, Bau, Nachfolger, Ferienjob) und mit einer Pflicht von Apple, die der
Stand vom 23.11. nicht enthielt (Abschnitt 1 und
[`details/07_HEBEL.md`](details/07_HEBEL.md)).

> **Worauf du dich einlässt** (Modell, 300.000 Läufe je Variante):
>
> | | |
> |---|---|
> | Zeit bis 31.08. | **~750 Stunden** verfügbar, davon ~180 bis zum 14.03. (10 je Schulwoche, ~31–38 je Ferienwoche, 3–7 in Q4). Im Abitur ruht die App, solange keine im Store ist. Ab Juni 15–55 je Woche. Endet die Jagd am 18.07. (der Normalfall), sind es ~400 Stunden für Lernen und App |
> | App 1 fertig | bis Di 02.02. in 14 von 100 Läufen, bis So 14.03. in 33 von 100, sonst erst nach dem Abitur (Median 07.06.) |
> | App 1 im App Store | vor dem 15.03. in 24 von 100 Läufen, sonst im Median ab 21.06. |
> | Geld nur aus der App (einschließlich Abmeldung und Steuererklärung) | im Median **−558 €**, im Mittel −393 €; mehr als 1.000 € Verlust in 1 von 100 Läufen, nie mehr als 5.000 € |
> | ein Gewinn aus der App | in **9 von 100** Läufen; in 12 von 100, wenn ein Elternteil eine laufende App im Sommer übernehmen würde |
> | alles zusammen, mit Ferienjob ab 19.07. | im Plus in **82 von 100** Läufen, im Median **+3.191 €** |
> | 10.000 € oder mehr | in 1,8 von 100 Läufen (nur aus der App: 0,25) |
> | 500.000 € bis 31.08.2027 | **in keinem** von 300.000 Läufen |
>
> Das ist ehrlich gesagt ein **Lernprojekt mit kleiner Gewinnchance**, kein
> Weg zu 500.000 €. Die App kostet dich im Normalfall rund 560 € und ~400
> Stunden. Sicheres Geld bringt nicht die App, sondern der Ferienjob, den du
> beginnst, sobald die Jagd endet. Rein nach Geld gerechnet wäre „nur
> Ferienjob, keine App“ sogar etwas besser (im Mittel rund 700 €). Dafür hast
> du am Ende eine eigene App im App Store, echte Programmier- und
> Marketingerfahrung vor dem ETH-Studium und gemessene Zahlen. Die Regeln
> unten sorgen dafür, dass weder das Abitur noch die ETH-Zulassung noch dein
> Geld für Zürich darunter leiden.

**Die Detailpläne.** Dieses Dokument ist der Überblick mit Regeln,
Messpunkten und Checklisten. Die einzelnen Schritte stehen hier:

| Datei | Inhalt |
|---|---|
| [`details/01_TAG_FUER_TAG_BIS_FEBRUAR.md`](details/01_TAG_FUER_TAG_BIS_FEBRUAR.md) | jeder Tag vom 23.11. bis zur Einreichung von App 1 |
| [`details/02_BAUPLAN_APP1.md`](details/02_BAUPLAN_APP1.md) | App 1 in 22 Arbeitspaketen mit Stunden und „fertig, wenn …“ |
| [`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md) | Namensfrage, Apple-Konto, Gewerbe, Steuer, Krankenkasse, Kosten Monat für Monat |
| [`details/04_IDEENWAHL.md`](details/04_IDEENWAHL.md) | fünf Ideen prüfen, eine bauen: K.-o.-Fragen, Nachfrageprüfung, Bewertungstabelle |
| [`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md) | Preis, Paywall, Store-Seite, Posts ohne Gesicht, Signalprüfung, Creator |
| [`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md) | Sommer Woche für Woche, Ferienjob, Übergabe, Verkauf, Stilllegung |
| [`details/07_HEBEL.md`](details/07_HEBEL.md) | was Chance und Ergebnis erhöht, mit allen Zahlen und Gegenproben |

Inhalt:
1. [Was sich gegenüber der ersten Fassung ändert](#1-was-sich-gegenüber-der-ersten-fassung-ändert)
2. [Das Wichtigste in Kürze](#2-das-wichtigste-in-kürze)
3. [Die eine große Entscheidung: Rechtsform und Anonymität](#3-die-eine-große-entscheidung-rechtsform-und-anonymität)
4. [Die Regeln](#4-die-regeln)
5. [Wer was macht](#5-wer-was-macht)
6. [Werkzeuge, Konten, Kosten](#6-werkzeuge-konten-kosten)
7. [So arbeitest du mit Claude, ohne programmieren zu können](#7-so-arbeitest-du-mit-claude-ohne-programmieren-zu-können)
8. [Videos ohne Gesicht](#8-videos-ohne-gesicht)
9. [ETH Zürich und Rückfall](#9-eth-zürich-und-rückfall)
10. [Wochenvorlagen](#10-wochenvorlagen)
11. [Diese Woche Tag für Tag (KW 48)](#11-diese-woche-tag-für-tag-kw-48)
12. [Woche für Woche bis zum Abschluss](#12-woche-für-woche-bis-zum-abschluss)
13. [Die Messpunkte und was du dann tust](#13-die-messpunkte-und-was-du-dann-tust)
14. [Ab Juli: drei Wege](#14-ab-juli-drei-wege)
15. [Checklisten](#15-checklisten)
16. [Vorlagen für Claude](#16-vorlagen-für-claude)
17. [Geld: Stufen, Budget, Kassenregeln](#17-geld-stufen-budget-kassenregeln)
18. [Wenn etwas schiefgeht](#18-wenn-etwas-schiefgeht)
19. [Was du aufschreibst](#19-was-du-aufschreibst)
20. [Alle Varianten im Vergleich](#20-alle-varianten-im-vergleich)
21. [Quellen](#21-quellen)

---

## 1. Was sich gegenüber der ersten Fassung ändert

Die erste Fassung beruhte auf Annahmen, die nicht stimmten. Das sind die
Korrekturen und was sie bewirken:

| erste Fassung | richtig | Folge im Plan |
|---|---|---|
| Bayern (Raum Regensburg) | Niedersachsen | andere Ferien; keine Februarferien, dafür Q4 vom 03.02. bis 18.03. mit einer Klausur in jedem Fach; schriftliches Abitur 06.04.–13.05., Prüfung im 5. Fach 19.05.–07.06. |
| du kannst programmieren (Python) | du kannst nicht programmieren | App 1 braucht ~80–280 Stunden statt 50–130, dazu 20–40 Stunden Grundlagen; sie ist meist erst nach dem Abitur fertig |
| sofort eine UG gründen | erst bauen, dann gründen, als Einzelunternehmen | die UG kostet bis zu ihrer Löschung 4.000–9.000 € und passt nicht in 5.000 € (Abschnitt 3) |
| du filmst dich selbst | kein Gesicht, keine Stimme | Foto-Slideshows, Bildschirmaufnahmen, Hände mit Handy; Creator erst, wenn die App ein Signal zeigt (Abschnitt 8) |
| Rückfall: Studium in München | ETH Zürich | Bewerbung über eApply bis 31.03.2027; deine Abitur-Prüfungsfächer und 70 % in drei Fächern entscheiden (Abschnitt 9) |
| bis 31.08. höchstens 5.000 € Verlust, danach noch 1.000–3.000 € für die UG | insgesamt höchstens 5.000 € | harte Grenze: Ausgaben nur, solange alle Pflichtkosten und die Abmeldung bezahlt sind |
| Haupttor am 28.02. | Tore am 18.07. und 08.08. | ein frühes Tor hätte App 1 abgebrochen, bevor sie fertig ist; dein Zeitfenster ist der Sommer |
| Claude Pro neu abschließen | Max läuft noch ein paar Tage | die Max-Tage für die Einrichtung nutzen, danach Pro |
| „Geschäftsführerin“ | männliche Formen | – |

**Was sich am 24.11. geändert hat** (Hebel-Recherche mit Gegenprüfung,
Einzelheiten in [`details/07_HEBEL.md`](details/07_HEBEL.md)):

| Stand 23.11. | jetzt | Folge |
|---|---|---|
| Einnahmen bis 31.08. voll gezählt | Apple verlangt mindestens 31 Tage zwischen „Abo aus dem Verkauf nehmen“ und dem Ende des Dienstes | ohne Nachfolger: Verkaufsstopp So 15.08., Dienstende Mi 15.09. Richtig gerechnet lag der Plan vom 23.11. bei 2,7 statt 6,2 von 100 Läufen mit Gewinn |
| Erstberatung beim Steuerberater, Abschluss für 0–800 € | Gründungsberatung der IHK statt Steuerberater (ob kostenlos, vorher fragen), Kleinunternehmer, Abschluss selbst über ELSTER (20–500 €) | zusammen mit den nächsten drei Zeilen: Medianverlust der App −558 € statt −1.184 € |
| Supabase Pro ab dem Start | Supabase im Gratis-Tarif, bis ein Signal da ist | ~27 € je Monat weniger nach dem Start |
| Claude Pro durchgehend, Max in einzelnen Monaten | Ruhezeit im Abitur (Entscheidung am So 14.03.), Max höchstens einen Monat | ~40–60 € weniger, kein Bau im Abitur |
| nach dem Ende der Jagd laufen die Abos weiter | am selben Tag alles kündigen, was Betrieb und Abschluss nicht brauchen | ~15 € je Monat weniger |
| Apple-Konto bei der Gründung | Apple-Konto schon in KW 51 (Mo 14.–Mi 16.12.), wenn die Idee steht | Durchstich mit echtem Gerät und Testkauf in den Weihnachtsferien |
| Abschluss: einstellen oder verkaufen | dazu: Übergabe an ein Elternteil, das im Januar schriftlich zugesagt hat | Gewinn aus der App in 12 statt 9 von 100 Läufen, im Mittel +469 € |
| nach dem 18.07. nur ETH-Vorbereitung und Erholung | Ferienjob Mo 19.07.–Di 31.08. als kurzfristige Beschäftigung (ab Mo 05.07., wenn dann keine App im Store ist) | alles zusammen im Plus in 82 von 100 Läufen, Median +3.191 € |
| eine Signalprüfung drei Wochen nach dem Start | für eine App, die vor dem Abitur startet, eine zweite: 21 Tage nach dem ersten täglichen Post nach der letzten Prüfung (spätestens Di 29.06.) | ein Treffer wird nicht wegen zu weniger Posts in Q4 abgeschrieben |
| Ideen-Tor mit fünf Kriterien | K.-o.-Fragen, Nachfrageprüfung, Bewertungstabelle, No-Go-Regel | erreicht keine Idee die Mindestwerte, wird nicht gegründet |
| Preise offen | Wochenabo 6,99 € vorausgewählt, Monatsabo 14,99 €, keine Testphase, kein Jahresabo | [`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md) |

---

## 2. Das Wichtigste in Kürze

1. **Bis Januar kostet es wenig.** Du lernst die Grundlagen und baust
   App 1 mit Claude, zuerst in Expo Go und ab KW 52 als Entwicklungs-Build auf
   deinem iPhone, noch ohne Gewerbe. Ausgaben: Claude Pro (~21 € im Monat),
   ein paar Dollar Guthaben für die Claude API und in KW 51 das Apple-Konto
   (99 €) – das aber nur, wenn deine Idee das Ideen-Tor absehbar besteht.
2. **Gegründet wird erst, wenn App 1 halb steht** (im Modell im Median am
   18.01., in 38 von 100 Läufen erst im Februar oder später), und zwar
   als **Einzelunternehmen**. Eine UG frisst dein ganzes Geld (Abschnitt 3).
3. **Ganz anonym geht es nicht.** Ohne Gesicht und ohne Stimme geht es. Aber
   als Verkäufer im App Store steht der Name einer echten Person, deiner
   oder der eines Elternteils. Und im Impressum, das von jedem Markenkonto aus
   verlinkt ist, stehen dieser Name und eine Anschrift, praktisch die deines
   Elternhauses. Wer nach einem Video sucht, findet also heraus, wer
   dahintersteht und wo er wohnt (Abschnitt 3).
4. **Abitur und ETH gehen vor.** In Q4 arbeitest du höchstens 6–7 Stunden je
   Woche an der App, im Abitur höchstens 0–5 Stunden, und zwischen 15.03. und
   deiner letzten Prüfung (spätestens 07.06.) startet keine App. Die
   ETH-Bewerbung schickst du in den Weihnachtsferien ab.
5. **Geld für Creator nur nach einem Signal.** Erst wenn eine App drei Wochen
   nach dem Start ohne bezahlte Werbung mindestens 300 $ MRR (Monatsumsatz in
   RevenueCat) macht, gibt es Creator-Geld, für alle Apps zusammen bis 18.07.
   höchstens 750 €. Im Modell fließt so fast nie Geld. Das ist so gut wie gar
   kein Creator-Geld und deutlich besser als Tests gleich beim Start
   (Abschnitt 20).
6. **Am 18.07. entscheidet eine Zahl.** Liegt keine App über 5.000 $ MRR,
   endet die Jagd: keine neue App, kein Creator-Geld, und am Mo 19.07.
   beginnt dein **Ferienjob**. Apps, die dann schon eingereicht sind, dürfen
   noch erscheinen.
7. **Der Abschluss braucht Vorlauf.** Apple verlangt 31 Tage zwischen
   Verkaufsstopp und Dienstende. Ohne Nachfolger nimmst du am So 15.08. alle
   Abos aus dem Verkauf, der Dienst läuft bis Mi 15.09., und am Do 16.09.
   oder Fr 17.09. entfernst du die App und meldest das Gewerbe ab. Besser: Ein Elternteil sagt im Januar schriftlich zu, eine
   laufende App zu übernehmen, oder du verkaufst sie (Abschnitt 14).
8. **Die Kosten sind halbiert.** Kleinunternehmer, Gründungsberatung der IHK
   statt Steuerberater (ob kostenlos, vorher fragen), Abschluss selbst über
   ELSTER, Server im Gratis-Tarif,
   Ruhezeit im Abitur. Die App kostet im Median rund 560 € statt rund
   1.180 € (Abschnitt 17).

---

## 3. Die eine große Entscheidung: Rechtsform und Anonymität

Wer als Verkäufer im App Store steht, entscheidet ihr bis So 13.12.
Gegründet wird, sobald App 1 etwa halb fertig ist, voraussichtlich zwischen
Januar und Februar. Bis dahin brauchst du kein Gewerbe: Bauen und Testen
geht ohne.

Für echte Käufe, TestFlight und den App Store brauchst du ein Apple-Konto
(99 € im Jahr; Apple nennt 99 USD oder den Betrag in Landeswährung). Apple verlangt dafür kein Gewerbe, nur ein Apple-Konto mit
Zwei-Faktor-Anmeldung, Volljährigkeit und deinen echten Namen. Sobald du Abos
verkaufst, ist das in Deutschland aber ein Gewerbe, und beim Einreichen
erklärst du dich für die EU als Händler. Bei der Anmeldung wird festgelegt,
wessen Name als Verkäufer im Store steht. Deshalb entscheidet ihr die
**Namensfrage bis So 13.12.** und legst du das Apple-Konto erst danach an:
Mo 14.–Mi 16.12., wenn deine Idee das Ideen-Tor absehbar besteht. Die 99 €
(Apple nennt 99 USD oder den Betrag in Landeswährung) gelten 12 Monate ab
diesem Tag. So läuft der Durchstich mit echtem Gerät schon in den
Weihnachtsferien. Die Gewerbeanmeldung bleibt bei M2.

**Was öffentlich wird**

| | Einzelunternehmen (du) | Einzelunternehmen eines Elternteils | UG mit dir als Geschäftsführer |
|---|---|---|---|
| Verkäufer im App Store (weltweit) | dein voller Name (Apple erlaubt keinen anderen Namen) | Name des Elternteils | Firmenname |
| EU-Seite der App (Pflicht für Händler seit 2025) | Adresse oder Postfach (mit Nachweis), Telefon, E-Mail | dasselbe vom Elternteil | Firmenadresse aus der D-U-N-S-Nummer, Telefon, E-Mail |
| Impressum (Website, App, Markenkonten) | dein Name und eine zustellfähige Anschrift (praktisch das Elternhaus; ein Postfach reicht nicht, ein Adressdienst ist für Einzelpersonen rechtlich unsicher) | Name und Anschrift des Elternteils | Firma, Anschrift und **dein Name als Geschäftsführer** |
| Register | Gewerberegister: Name, Anschrift, Tätigkeit gibt die Gemeinde an jeden heraus | dasselbe vom Elternteil | Handelsregister kostenlos für jeden: dein Name, Geburtsdatum, Wohnort; North Data zeigt Name und Wohnort |
| Gesicht und Stimme | nie nötig | nie nötig | nie nötig |

**Was es kostet und bringt** (Modell, 300.000 Läufe je Variante, alles bis zur
Abmeldung bzw. Auflösung eingerechnet; die UG-Spalten stammen aus der Rechnung
vom 23.11.)

| | Einzelunternehmen | UG, Anschrift der Eltern | UG, gemietete Geschäftsadresse |
|---|---:|---:|---:|
| Formalkosten bis zum Ende | ~160–880 € (Gewerbe, Apple, Domain, Abmeldung, Steuererklärung selbst über ELSTER) | ~4.000–9.000 € bis zur Löschung (frühestens Ende 2028) | dazu 50–130 € je Monat für die Adresse |
| passt in 5.000 € | ja | **nein:** in 99 von 100 Läufen lassen Pflichtkosten und Auflösung gar keine Gründung zu | **nein:** in fast allen Läufen (99,9 von 100) keine Gründung |
| überhaupt ein Gewinn | 9 von 100 (Stand 24.11., Plan mit Hebeln) | 0 von 100 | 0 von 100 |
| Geld im Median | −558 € | −357 € (nur Claude, weil meist gar nicht gegründet wird und dann auch keine App erscheint) | −355 € (ebenso) |
| vor dem Umzug sauber beenden | ja, Abmeldung an einem Tag | nein: wegen des Sperrjahrs läuft die Auflösung, während du in Zürich lebst; führst du die UG von dort, wird sie auch in der Schweiz steuerpflichtig, und dir droht Wegzugsteuer auf die Anteile | wie links |

**Meine Empfehlung:** das **Einzelunternehmen**. Die UG versteckt deinen
Namen nur halb: im App Store ja, im Impressum und im Handelsregister nicht.
Dafür kostet sie fast dein ganzes Geld und lässt sich vor dem Umzug nicht
mehr beenden.

Ist dir dein Name im App Store zu viel, gibt es zwei ehrliche Wege:
- **Ein Elternteil meldet das Gewerbe an** und schließt den Apple-Vertrag.
  - **Was das verbirgt:** Im App Store und im Impressum steht dann sein
    Name, meist mit eurem gemeinsamen Nachnamen und eurer gemeinsamen
    Anschrift. Versteckt ist also vor allem dein Vorname.
  - **Was du dann selbst machen kannst:** Bei einem Apple-Konto für
    Einzelpersonen kann das Elternteil dich nur in App Store Connect
    einladen (Einreichen, Texte, TestFlight, Zahlen), nicht ins
    Entwicklerteam. Geräte registrieren und die Zertifikate für EAS-Builds
    anlegen geht nur mit seiner Anmeldung und seinem Zwei-Faktor-Code. Prüft
    vorher, ob ein API-Schlüssel des Elternteils für EAS das ersetzen kann.
  - **Rechtlich:** App und Gewinn gehören dem Elternteil. Es entscheidet mit,
    trägt das Risiko, zahlt die Rechnungen, haftet unbeschränkt, versteuert
    den Gewinn und meldet die Nebentätigkeit seinem Arbeitgeber, falls der
    Arbeitsvertrag das verlangt (als Beamter: genehmigen lassen). Du arbeitest
    unentgeltlich mit; eine Gewinnbeteiligung vereinbart ihr nicht. Gibt es dir
    regelmäßig Geld aus dem Gewinn, spricht das dafür, dass in Wahrheit du das
    Geschäft führst: Dann kann das Finanzamt die Einkünfte dir zurechnen, und
    die Krankenkasse zählt sie. Eine echte, freiwillige Schenkung ist vom
    Elternteil an dich bis 400.000 € je Elternteil in zehn Jahren steuerfrei
    (von dir an ein Elternteil 20.000 €) und binnen drei Monaten dem Finanzamt
    schriftlich anzuzeigen (§ 30 ErbStG). Frag vorher das Finanzamt, schon
    am Fr 04.12. (telefonisch mit Name und Datum notiert oder schriftlich):
    „Wem werden die Einkünfte zugerechnet, wenn das volljährige Kind
    unentgeltlich mitarbeitet?“ Die Gründungsberatung (Termin bis Mi 06.01.)
    käme dafür zu spät. Liegt bis Fr 11.12. keine klare Antwort vor, bist du
    Inhaber ([`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md),
    Abschnitt 2.2; die ganze Frage steht dort in Abschnitt 5, Schritt 1, als
    Frage 10).
  - Das geht nur, wenn das Elternteil es wirklich will und versteht. Ein
    Strohmann – das Elternteil steht nur auf dem Papier, während in Wahrheit
    du das Geschäft führst – schützt keinen von euch.
- **Gar nicht veröffentlichen:** App 1 als Lernprojekt bauen, im Sommer mit
  einem Organisationskonto oder dem Elternteil entscheiden. Das kostet die
  meisten Chancen, weil dann der Sommer fehlt.

Was in jedem Fall geht, damit möglichst wenig von dir sichtbar wird:
- **dieses Plan-Repository und das App-Repository privat halten.** Hier
  stehen viele Angaben über dich; sobald App-Name oder Domain dazukommen,
  wärst du darüber auffindbar. App-Name, Domain und Markenkonten erscheinen nie
  in einem öffentlichen Repository oder unter einem Benutzernamen, der zu dir
  führt;
- ein neutraler Markenname für die App;
- eine eigene Telefonnummer nur für die App, also eine Prepaid- oder
  Zweitnummer statt deiner Handynummer. Apple prüft sie mit einem Code.
- ein Postfach für die EU-Seite bei Apple (mit Nachweis);
- ein eigenes Projekt-Postfach als Anmeldeadresse für alle Konten (ab KW 48)
  und eine Support-Adresse auf deiner Domain (ab der Gründung);
- Markenkonten ohne Gesicht und ohne Stimme, **getrennt von deiner privaten
  Identität**:
  - nur mit Projekt-Postfach bzw. Support-Adresse und Zweitnummer anlegen;
  - keine Kontakte synchronisieren und bei TikTok unter Einstellungen →
    Datenschutz → „Dein Konto anderen vorschlagen“ alles ausschalten;
  - keinem privaten Kontakt folgen und das Markenkonto nicht mit deinem
    privaten Konto verknüpfen, bei Instagram auch nicht in derselben
    Kontenübersicht;
- Bildschirmaufnahmen nur im Fokus „Nicht stören“ und mit Testdaten, ohne
  eigene Fotos, Kontakte oder Mitteilungen, am besten auf dem iPad;
- TestFlight-Tester nur aus der Familie, solange es sonst niemand wissen soll.

Für das Impressum frag deine Eltern, ob ihre Anschrift darin stehen darf.
Das ist rechtlich am sichersten.

---

## 4. Die Regeln

Diese Regeln stehen über allem anderen. Unter ihnen gelten die Zahlen oben.

**Zeit (Abitur- und ETH-Schutz)** – nach der Ferienordnung Niedersachsen und
den Abiturterminen 2027:

| Zeitraum | Stunden je Woche | Hinweis |
|---|---|---|
| Schulwochen bis Di 22.12. und 11.–29.01. (Q3) | **10** (Mo–Fr je 1 h, Sa 5 h, So frei), höchstens 15 | Woche mit Klausuren: nur Samstag 3 h |
| Weihnachtsferien Mi 23.12.–Sa 09.01. | 21.–27.12.: ~9; 28.12.–03.01.: ~31; 04.–09.01.: ~38 | Mo–Fr 9–12 und 13–17 Uhr (7 h), Sa 3 h; 24.–27.12. und 01.01. frei; dazu 1–1,5 h Schule am Tag |
| Halbjahresferien Mo 01.–Di 02.02. | ~19 in dieser Woche | Mo/Di je ~7 h, ab Mi 03.02. die Q4-Regel |
| Q4, Mi 03.02.–So 14.03. | **höchstens 6–7**, in Wochen mit zwei oder mehr Klausuren nur Sa 3 h | Q4-Noten zählen fürs Abitur; keine neue Kampagne |
| 15.03.–05.04. (letzte Q4-Tage bis Do 18.03., Osterferien) | 0–5, in der Ruhezeit 0 | Abiturvorbereitung |
| schriftliches Abitur 06.04.–13.05. | 0–1, in der Ruhezeit 0 | an Prüfungstagen und ab einer Woche davor gar nichts |
| 5. Prüfungsfach und Nachschreibtermine 19.05.–07.06. | 0–5, in der Ruhezeit 0 | bei einer Präsentationsprüfung zwei Wochen gar nichts; Mo 07.06. kann noch Prüfungstag sein |
| nach deiner letzten Prüfung bis 04.07. | 15–40 | mögliche mündliche Nachprüfung 28.–30.06., Zeugnis 01.–03.07. |
| 05.07. bis zum Ende der Jagd (meist So 18.07.) | Mo–Sa ~9 h, So frei | davon ~6 h je Woche für Zürich (Zimmer, Unterlagen, Mathe) |
| danach bis zum Abschluss | Ferienjob in Vollzeit; für die Apps 2–5 h je Woche | an zwei Werktagen je 20 Minuten Zahlen und Support, samstags bis 3 h; im August für Übergabe, Verkauf oder Stilllegung einmalig mehr ([`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md)) |

Die Stunden sind Richtwerte. Das Modell streut sie je Woche um ±20 %.

- **Kein App-Start zwischen 15.03. und deiner letzten Prüfung (spätestens
  07.06.).** Die Freigabeart wählst du in App Store Connect **beim Einreichen**
  (und bei jedem erneuten Einreichen nach einer Ablehnung) unter
  „App Store-Versionsfreigabe“. Wähle immer „Diese Version manuell
  veröffentlichen“: Wird App 1 bis Sa 13.03. freigegeben, veröffentlichst du
  sie sofort, sonst nach deiner letzten Prüfung. Verlass dich nicht darauf,
  das später umzustellen; mit „automatisch“ ist die App direkt nach der
  Freigabe live. Bis sie im Store sichtbar ist, können bis zu 24 Stunden
  vergehen.
- **Ruhezeit im Abitur:** Ist am So 14.03. keine App im Store und keine im
  Review, ruht die App bis nach deiner letzten Prüfung ganz: null Stunden,
  Claude Pro pausiert. Das spart Geld und schützt das Abitur; im Modell
  kostet es fast nichts (Abschnitt 20).
- **Die 0–5 Stunden im Abitur** gelten nur, wenn eine App im Store oder im
  Review ist. Sie sind für Zahlen, Notfälle und Antworten an das Review da,
  nie an Prüfungstagen und nie ab einer Woche davor. Keine Posts, keine
  Startarbeit, keine Creator.
- **Alles zählt in diese Stunden:** Lernen, Bauen, Prüfen, Videos,
  Behördenkram, Bewerbungen.
- Nie nach 22 Uhr an der App. Kein Prüfungstermin wird für die App geopfert.
- **Schule und ETH-Grenze:** Für die ETH brauchst du in deinen drei
  ETH-Fächern **Chemie (P2), Mathe (P4) und Englisch (P5)** zusammen
  mindestens 32 von 45 Punkten in den Abiturprüfungen (Abschnitt 9). Liegt
  der Schnitt deiner letzten Klausuren in diesen drei Fächern unter
  11,5 Punkten oder eine davon unter 10, arbeitest du sofort nur noch
  3 Stunden je Woche an der App. Die frei gewordene Zeit geht in genau dieses
  Fach, bis die nächste Klausur dort wieder darüber liegt.
- **Deine Prüfungstage:** Mathe Mi 05.05., Chemie Do 13.05. (der letzte Tag
  des schriftlichen Abiturs), Englisch als P5 an einem Tag zwischen 19.05. und
  07.06., den deine Schule festlegt. Trag die Tage von P1 und P3 dazu. Ab
  einer Woche vor jedem Prüfungstag gar nichts an der App.

**Geld**
- **Insgesamt höchstens 5.000 €**, einschließlich der Abmeldung, der
  Steuererklärung 2027 und einer eigenen Krankenversicherung, falls dein
  Gewinn zu hoch wird. Das Geld für Zürich ist getrennt und wird nie
  angefasst.
- **Ausgaben in Stufen** (Abschnitt 17): bis zur Gründung nur Claude Pro, ein
  kleines Guthaben für die Claude API zum Testen (wenige Dollar,
  Ausgabenlimit 50 $) und in KW 51 das Apple-Konto, dann die Gründung,
  Creator-Geld erst nach einem Signal.
- Kein Kredit, kein Dispo, keine Ratenzahlung.
- Vor jeder Ausgabe über 50 €: Sind danach alle Pflichtkosten bis zum
  Dienstende und ~500 € für Abmeldung und Steuererklärung noch gedeckt?
- **Kein bezahltes Verstärken eigener Posts** (Promote, Spark Ads): 50 €
  Einsatz bringen typisch 6 € zurück.
- **Familienversicherung:** Entscheidend ist der Gewinn, also Einnahmen
  minus Kosten. Er muss regelmäßig unter ~590 € im Monat bleiben (Grenze
  2027, 1/7 der Bezugsgröße von 4.130 €, vorbehaltlich Bundesrat; 2026:
  565 €).
  - **So rechnet die Kasse:** Sie schätzt deinen Gewinn 2027 vorausschauend
    und teilt ihn durch 12; maßgeblich ist am Ende der Steuerbescheid. Ein
    starker Monat zählt deshalb mit seinem ganzen Gewinn im Jahreswert: Liegt
    der Jahresgewinn über ~7.080 € (12 × 590 €), endet die
    Familienversicherung, auch wenn das Geld aus einem einzigen Monat kommt.
  - **Was du tust:** Zeichnet sich ab, dass dein Gewinn 2027 zusammen über
    ~7.000 € liegt, meldest du es der Kasse.
  - **Stunden:** Sie zählen nach den Hinweisen der Krankenkassen nur
    zusammen mit dem Einkommen. Als Hauptberuf gilt die App erst ab mehr als
    30 Stunden je Woche bei mehr als ~1.030 € Arbeitseinkommen im Monat, bei
    20–30 Stunden erst ab ~2.065 €. Deine Stunden nennst du der Kasse so,
    wie sie sind.
  - Keine Angestellten.
  - **Ferienjob:** Lohn aus einer kurzfristigen Beschäftigung zählt nach den
    Hinweisen der Krankenkassen nicht als regelmäßiges Einkommen, unabhängig
    von der Höhe. Lass es dir vor der Unterschrift schriftlich bestätigen.

**Recht**
- Ein Markenkonto je Plattform (ein zweites, klar erkennbares TikTok-Konto
  erst nach einem Formatnachweis, [`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md),
  Abschnitt 7.6). Jedes Konto trägt den Namen der App und den
  Impressum-Link, und deine Konten liken oder kommentieren sich nie
  gegenseitig. **Keine Konten, die unabhängige Nutzer vortäuschen**, keine
  gekauften oder gefälschten Bewertungen und keine Bewertungen von dir, deiner
  Familie oder Freunden (auch nicht von TestFlight-Testern) oder gegen eine
  Gegenleistung, keine KI-Personen, die eine Erfahrung mit der App bezeugen.
- Keine Ausgaben erfinden oder verschieben, um unter der Grenze der
  Familienversicherung zu bleiben; in App Store Connect nie „kein Händler“
  angeben; keine Abos nach der Gewerbeabmeldung weiterlaufen lassen.
- Auf TikTok bei jedem Post den Schalter für kommerzielle Inhalte auf „Your
  brand“ und nur Musik aus der Commercial Music Library. Bezahlte Creator
  kennzeichnen „Werbung“ und nutzen „Paid partnership“.
- Kein automatisches Posten, Kommentieren oder Versenden über inoffizielle
  Werkzeuge; keine Massenanfragen an Creator.
- Kundendaten (Eingaben, Support-Mails) nur über Dienste mit Vertrag zur
  Auftragsverarbeitung, nie über dein privates Claude-Abo.

---

## 5. Wer was macht

| Aufgabe | Claude | du |
|---|---|---|
| Grundlagen | erklärt im Lernmodus, stellt dir Übungen, lässt dich Stellen selbst schreiben | lernst ~25–40 Stunden bis Ende Januar (bis 20.12. etwa die Hälfte); fragst nach, bis du es einem Mitschüler erklären kannst |
| Code: App, Paywall, KI-Funktion, Server | schreibt alles in kleinen Schritten, erklärt jeden Schritt, führt die `CLAUDE.md` und das Review-Log | beschreibst, was du willst; testest auf iPhone und iPad; prüfst mit den Checklisten; entscheidest |
| Sicherheit und Datenschutz | Entwürfe, Prüflisten, führt die Prüfungen aus | siehst dir jedes Ergebnis selbst an; verantwortest |
| App Store | Texte, Screenshot-Entwürfe, Antworten an das Review | reichst ein, gibst frei; Verträge, Bank- und Steuerdaten nur du (bzw. das Elternteil) |
| Ideen | 12 Kandidaten zusätzlich zu deinen eigenen und dem Pool aus 04 (zusammen etwa 20), Konkurrenztabellen aus der öffentlichen iTunes-Suche, vorläufige Punkte für die Kriterien, die sich ohne Messung schätzen lassen; keine Umsätze, keine Rangliste | prüfst K.-o.-Fragen und 60-Sekunden-Test, wählst 5, misst Suche, Zahlungsbeleg und Videos selbst, entscheidest am Ideen-Tor |
| Videos ohne Gesicht | Hooks, Folientexte, Bildideen, Skripte für Bildschirmaufnahmen, Auswertung | baust die Slideshows (etwa 14 Minuten je Post, 10–18), nimmst Bildschirm und Hände auf, postest von Hand |
| Creator (nach Signal) | Suche, Entwürfe für persönliche Anfragen, Briefing, Vertragsvorlage | schreibst jede Anfrage einzeln, bezahlst nach dem Posten (bzw. gibst die Zahlung auf der Plattform erst dann frei), prüfst die Kennzeichnung |
| Kennzahlen | Auswertung aus RevenueCat und App Store Connect, Vorschläge | entscheidest |
| Verwaltung | Entwürfe für Briefe und Formulare, sortiert Belege | unterschreibst, reichst ein |

---

## 6. Werkzeuge, Konten, Kosten

| Werkzeug | wofür | Kosten | wann |
|---|---|---|---|
| Claude Max (läuft aus), dann Claude Pro | Code, Texte, Auswertungen; Claude Code läuft nativ unter Windows | Max schon bezahlt; Pro ~21 € brutto je Monat | Max-Tage jetzt nutzen, nicht verlängern; danach Pro |
| Claude Code unter Windows | Installation in PowerShell: `irm https://claude.ai/install.ps1 \| iex` (ohne Adminrechte); dazu Git for Windows und Node.js (LTS) | 0 € | KW 48 |
| GitHub | Code der Apps, privates Repository | 0 € | KW 48 |
| Expo mit EAS (React Native, TypeScript) | App bauen; Builds in der Cloud, Einreichung per `eas submit` – kein Mac nötig | 0 € (15 iOS-Builds im Monat), sonst 19 $/Monat | KW 48 |
| Expo Go auf iPhone und iPad | Oberfläche testen; Käufe sind dort nur Attrappen | 0 € | KW 48 |
| Supabase | Server-Funktion für den KI-Aufruf | 0 € im Gratis-Tarif; Pro (25 $/Monat) erst bei einem Signal, an einem Limit oder für die Abiturmonate, wenn eine App im Store oder im Review ist | KW 50 |
| Claude API (Haiku 5.5) | KI-Funktion der App, getrennt vom Abo | zum Testen 5–10 $ Prepaid-Guthaben ohne Nachladen (Karte nötig); im Betrieb typisch ~30 $ je 1.000 aktive Nutzer im Monat; ab dem Start Nachladen an mit Monatslimit 25–50 $ | ab KW 50 |
| Apple Developer Program (Einzelperson) | Entwicklungs-Build auf dem eigenen Gerät, TestFlight, App Store | 99 €/Jahr (99 USD oder Betrag in Landeswährung); zahlst du per Kreditkarte, muss es deine eigene sein (sonst Verzögerung und Ausweiskopie), oder du meldest dich in der Apple-Developer-App an; **automatische Verlängerung gleich abschalten**; ohne D-U-N-S, Konto meist nach wenigen Tagen aktiv, nach 24 Stunden ohne Bestätigung bei Apple nachfragen | KW 51 (Mo 14.–Mi 16.12.), wenn die Namensfrage entschieden ist und das Ideen-Tor absehbar bestanden wird (Zwischenstand Sa 12.12.); sonst nach dem Ideen-Tor, frühestens Mo 21.12. |
| RevenueCat | Abos, Paywall, Umsatzzahlen, Abo-Prüfung für den Server | frei bis 2.500 $ Monatsumsatz | mit dem Apple-Konto |
| Domain, Website, E-Mail | Impressum, Datenschutz, Support | ein monatlich kündbares Paket eines deutschen Anbieters mit Postfach und Webspace, ~2–5 € im Monat | bei der Gründung |
| Zweitnummer (Prepaid) | Telefon für Apples EU-Seite | Prepaid ohne Grundgebühr, ~10 € Startpaket | bei der Gründung |
| Canva oder CapCut (Gratisversion) | Slideshows, Untertitel | 0 € | in der Vorbereitung vor der Gründung ([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md), Abschnitt 4) |

Bewusst **nicht** in App 1:
- **Nutzerkonten:** Dann entfällt die Pflicht zur Kontolöschung. Die
  Abo-Prüfung läuft über die pseudonyme App-User-ID von RevenueCat
  (RevenueCat nennt sie anonym).
- **Fremde Tracking- und Analyse-SDKs:** Auch eigene Messereignisse
  („Paywall gesehen“) nur mit Einwilligung (§ 25 TDDDG). Ohne Einwilligung
  wertest du nur aus, was ohnehin anfällt: Downloads, Käufe, Zahl der
  KI-Aufrufe und die freiwillige, sofort gezählte Antwort auf die
  Herkunftsfrage (Checkliste D).
- **Fotos und Kamera:** App 1 ist eine reine Text-App. Eingaben gehen über
  deine Server-Funktion an Anthropic. Deine Funktion speichert sie nicht;
  Anthropic löscht API-Eingaben und -Antworten nach eigener Angabe binnen
  30 Tagen (bei Verdacht auf Verstöße bis zu 2 Jahre). Der Verlauf liegt nur
  auf dem Gerät.
- **Testphase:** App 1 hat keine. Das Geld kommt am ersten Tag, und die
  Signalprüfung am Tag 21 misst drei volle Wochen.
- **Jahresabos:** Du ziehst im September um. Ein Jahresabo verpflichtet dich,
  die App bis zu zwölf Monate weiterzubetreiben. Deshalb nur Wochenabo
  (6,99 €, vorausgewählt) und Monatsabo (14,99 €); kein Jahresabo, solange du
  Inhaber bist (ein Nachfolger entscheidet nach der Übertragung selbst). Apps,
  die nach dem 04.07. erscheinen, bieten nur das Wochenabo an.
- **Nutzerinhalte, die andere sehen** (Teilen in der App, Profile): Dann
  bräuchtest du zusätzlich Blockieren. Richtlinie 1.2 gilt aber auch für
  KI-Apps, die Inhalte erzeugen: Filter (feste Anweisungen an das Modell,
  Längenbegrenzung), Knopf „Antwort melden“ mit zeitnaher Antwort und
  veröffentlichte Kontaktangaben braucht deshalb auch App 1.
- **Minderjährige als Zielgruppe:** Die App richtet sich an Erwachsene. Keine
  Apps für Schüler, Lernen oder Hausaufgaben. Die Nutzungsbedingungen sagen
  „ab 18“, die Altersfreigabe in App Store Connect beantwortest du ehrlich.
  Das verringert Fragen der Einwilligung Minderjähriger (DSGVO), schließt sie
  aber nicht aus: Laden kann die App, wer die Altersfreigabe im Store erfüllt.
  Ob für die Einwilligung vor dem ersten KI-Aufruf bei unter 16-Jährigen
  Art. 8 DSGVO greift, prüfst du vor der Einreichung. Die Regel passt zu den
  Nutzungsregeln der Claude API.

---

## 7. So arbeitest du mit Claude, ohne programmieren zu können

**Was die Forschung sagt:**
- **Die Fehlersuche ist der Engpass.** In einer Studie mit Studierenden
  gingen 61 % der Anfragen an einen KI-Agenten in das Reparieren von Code,
  den der Agent selbst geschrieben hatte. Anfänger stellten dabei deutlich
  öfter Anfragen ohne nützliche Angaben zum Fehler.
- **Nicht-Programmierer fragen lieber neu, statt den Fehler zu suchen**, und
  bringen seltener etwas Fertiges heraus.
- **Abgeben ohne Verstehen schadet beim Lernen.** In einem Versuch von
  Anthropic schnitt beim Verstehen am schlechtesten ab, wer alles nur abgab,
  vor allem bei der Fehlersuche. Gut schnitt ab, wer sich erklären ließ und
  nachfragte.
- **Das Gefühl täuscht.** Erfahrene Entwickler hielten sich mit KI für 20 %
  schneller und waren in Wahrheit 19 % langsamer.

Deshalb lernst du zuerst die Grundlagen, arbeitest im Lernmodus und glaubst
nur, was du selbst gesehen hast.

**Lernpfad (~25–40 Stunden, KW 48 bis Ende Januar; bis 20.12. etwa die Hälfte, danach ~3–4 h je Woche neben dem Bau)**
1. Expo-Tutorial „Build with AI“ (für Menschen ohne Programmierhintergrund,
   ~1 h, mit Claude Code, iPhone mit Expo Go).
2. Expo-Standard-Tutorial „StickerSmash“ (~2 h).
3. MIT „Missing Semester“ 2026: Shell, Git, Fehlersuche (~6–10 h mit
   Übungen).
4. JavaScript und TypeScript lesen lernen, nicht schreiben (~10–20 h, z. B. die
   ersten Abschnitte von freeCodeCamp).
5. Expo- und EAS-Doku zu Development Builds und `eas submit` (~3–5 h).
6. Fehlermeldungen lesen üben, an deinen eigenen echten Fehlern.

CS50x (10–20 Stunden je Woche) machst du nicht neben der 55-Stunden-Woche,
sondern ab dem Tag, an dem die Jagd endet (in ~99 von 100 Läufen ab 19.07.).
Dann gehen die frei gewordenen Stunden in die ETH-Vorbereitung: etwa zur
Hälfte Mathe nach den Empfehlungen der ETH, zur Hälfte Programmieren
(Java-Tutorial der ETH, CS50x).

**Lernmodus:** In Claude Code `/output-style learning` einschalten. Claude
erklärt dann seine Entscheidungen und lässt dich an wichtigen Stellen selbst
schreiben (`TODO(human)`). Für reine Erklärungen gibt es `/output-style explanatory`.
`/output-style` gilt nur für das aktuelle Projekt. Damit der Lernmodus überall
gilt, lass Claude ihn in deinen Benutzereinstellungen eintragen
(`~/.claude/settings.json`, Eintrag `outputStyle`).

**Eine Sitzung (30–90 Minuten)**
1. Ein kleines, prüfbares Ziel: „Onboarding mit 5 Fragen, danach die
   Paywall-Seite, noch ohne Kauf“, nicht „bau die App“.
2. Claude plant zuerst und sagt, welche Dateien es ändert. Du sagst Ja oder
   änderst den Plan.
3. Claude setzt um und erklärt in zwei, drei Sätzen, was es gemacht hat.
4. Du prüfst auf dem iPhone (Expo Go, später Development Build) **und auf
   dem iPad**. Apple prüft iPhone-Apps auch auf dem iPad.
5. **Glaube kein „ist behoben“, bevor du es gesehen hast.**
6. Commit mit kurzer Nachricht, Zeit und Ergebnis notieren.

**Wenn Claude im Kreis läuft** (zweimal derselbe Fehler): Sitzung beenden,
den Fehler in einem Satz aufschreiben, neue Sitzung mit „Erkläre mir zuerst,
was der Fehler bedeutet und wo er entsteht; ändere noch nichts“.

**Testweg ohne Mac**
- **Expo Go:** nur Oberfläche und Ablauf; RevenueCat zeigt dort nur
  Attrappen.
- **Ab dem Apple-Konto:** iPhone und iPad mit `eas device:create`
  registrieren, Entwicklermodus einschalten, Development Build per QR-Code
  installieren. Bei einem neuen Konto kann das 24–72 Stunden dauern.
- **TestFlight:** Production-Build per `eas submit`, dort echte Käufe mit
  einem Sandbox-Konto testen.
- Im Free-Plan gibt es nur 15 iOS-Builds im Monat. Kleine Änderungen prüfst
  du im Development Build mit Hot Reload.

**Die KI-Funktion sicher und bezahlbar** – Mindestprüfung vor jedem Release.
Claude darf sie ausführen, das Ergebnis siehst du dir selbst an:
1. **Kein Schlüssel in der App.** Der KI-Schlüssel und der geheime
   RevenueCat-Schlüssel liegen nur als Geheimnis in der Server-Funktion
   (`supabase secrets set`). Die Datei `.env` steht in `.gitignore`.
2. **Die Server-Funktion prüft bei jedem Aufruf selbst**, ob die
   mitgeschickte App-User-ID ein aktives Abo hat (REST-API von RevenueCat),
   und zählt eine Tagesgrenze je App-User-ID (zum Start 30 Antworten je
   Abonnent und Tag). Ohne diese Prüfung wird sie
   zum offenen Zugang, über den Fremde dein API-Budget leerziehen können.
   Genau diesen Fehler hatte in einer Untersuchung ein Drittel der
   betroffenen iOS-Apps mit KI-Funktion.
3. **Zugriffsregeln (RLS)** auf jeder Tabelle, keine Regel `using (true)`.
   Der Security Advisor von Supabase zeigt null Fehler.
4. **Ausgabengrenze in der Anthropic-Konsole als Notbremse:** vor dem Start
   nur 5–10 $ Prepaid-Guthaben ohne automatisches Nachladen; ab dem Start
   Nachladen an, mit einem Monatslimit (zum Start 25–50 $), das du jeden
   Sonntag anpasst (aktive Nutzer × 0,03 $, vorsichtig × 0,18 $, davon das
   Dreifache).
5. Repository und App nach Schlüsseln durchsuchen (`git grep`, GitHub Secret
   Scanning).
6. **Getrennte Projekte für Test und Betrieb** (das Testprojekt in einer
   eigenen Gratis-Organisation). Claude bekommt keine Zugangsdaten für den
   Betrieb. Im Gratis-Tarif gibt es keine Backups; das Tabellen-Schema liegt
   deshalb als Migration im Repository.
7. **Von außen testen:** Ein Aufruf ohne aktives Abo muss scheitern.
8. Ein neues Supabase-Projekt gleich mit den neuen Schlüsseln anlegen, weil
   die alten Ende 2026 wegfallen.

**Was Claude nie tun darf:** Schlüssel in die App schreiben; Zahlungen,
Verträge oder Veröffentlichungen ohne deine Freigabe; posten oder Nachrichten
verschicken; mit Zugangsdaten für den Betrieb arbeiten; Kundendaten über dein
privates Abo verarbeiten.

---

## 8. Videos ohne Gesicht

Das Wochenprogramm, die Vorlagen, die Messung und die Regeln für Creator
stehen Schritt für Schritt in
[`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md). Hier
steht der Überblick.

**Was ohne Gesicht funktioniert** (Fallberichte, alle selbst berichtet):
- **Foto-Slideshows und Karussells:** Text auf Bild, Hook auf der ersten
  Folie, letzte Folie mit Hinweis auf die App. Eine Paar-Fragen-App kam mit
  26 Konten und über 20 Formaten auf über 140 Mio. Aufrufe. Ein anderer
  Gründer schaffte in 5 Tagen 500.000 Aufrufe und rund 590 $ Monatsumsatz.
- **Bildschirmaufnahmen der App und „Hände mit Handy“:** Ein Gründer kam damit
  auf 2,4 Mio. Aufrufe, 20.000 Downloads und 9.000 $ Monatsumsatz in
  78 Tagen.
- **Gegenbeispiel:** Voll automatisierte Slideshows brachten einem anderen
  Gründer nur rund 100 Downloads.
- **Gesicht oder nicht:** Für Reichweite ohne Werbung gibt es keinen Beleg,
  dass Videos mit Gesicht besser verkaufen. Bei bezahlten Anzeigen
  schneiden Creator-Inhalte laut TikTok deutlich besser ab, rund 70 % mehr
  Klicks.
- **Was du realistisch erwarten kannst** (Gegenprüfung vom 24.11.): Die
  Fallberichte sind Ausreißer. In einer Auswertung von 11,4 Mio. TikTok-Posts
  liegt der mittlere Post bei rund 500 Aufrufen, egal wie oft ein Konto
  postet; mehr Posts heben nur die Spitze. Ein Post mit 100.000 Aufrufen
  bringt etwa 50–150 Downloads und 20–70 $ Monatsumsatz. Die Chance, bis
  18.07. mindestens einen solchen Post zu haben, liegt bei etwa 30 von 100.

**Dein Ablauf**
- **Vor der Gründung** nur Vorbereitung (3–4 Stunden): Hook-Liste, drei
  Vorlagen in Canva, Messtabelle. Kein Konto.
- **Ab der Gründung, in der Woche der Einreichung:** ein Markenkonto je
  Plattform (TikTok, Instagram, YouTube Shorts), auf Deutsch, mit dem Namen
  der App und dem Link „Impressum“ zur Website. Kein Datum versprechen („bald
  im App Store“).
  Solange TikTok keinen klickbaren Link anbietet (ohne
  Unternehmensverifizierung meist erst ab 1.000 Followern; mit Verifizierung
  steht der Name des Inhabers im Profil, siehe 05, Abschnitt 5.3), schreibst
  du die Web-Adresse der Impressum-Seite als Text in die Bio, z. B.
  „Impressum: deineapp.de/impressum“, nie deine Postanschrift. Das
  beanstandet laut Leitfaden der Landesanstalt für Kommunikation
  Baden-Württemberg eine Medienanstalt „gegenwärtig nicht“; für Niedersachsen,
  Gerichte und Mitbewerber ist das nicht verbindlich (Restrisiko einer
  Abmahnung). Bietet TikTok einen Link an, stellst du sofort um. Im Impressum
  der Website steht: „Dieses Impressum gilt auch für unsere Profile bei
  TikTok, Instagram und YouTube: @[Name].“
- **Format testen:** viele Varianten eines Formats, Hook in der ersten Sekunde
  bzw. auf der ersten Folie. Claude liefert je Tag 10 Hook-Varianten und die
  Folientexte, du baust die Slideshow in Canva (etwa 14 Minuten je Post) und
  postest von Hand vom Gerät mit den Markenkonten (das iPad, wenn du TikTok
  oder Instagram privat auf dem iPhone nutzt; 05, Abschnitt 5.1) oder planst
  sie mit den offiziellen Werkzeugen der Plattform.
- **Sieger** ist ein Post ab 15.000 Aufrufen oder dem Zehnfachen deines
  Medians (der mittlere Wert der Aufrufe nach 48 Stunden deiner letzten
  20 Posts). Bestätigt ist ein Format erst, wenn zwei von drei Varianten über
  deinem Median liegen.
- **Menge:** in Q4 erst, wenn App 1 eingereicht ist, und dann höchstens 3 je
  Woche, gebaut in einem Block von 90 Minuten am Samstag (höchstens 9, solange
  die App nicht im Store ist); im Abitur keine Posts; nach dem Abitur 2–3 am
  Tag.
- **Kein bezahltes Verstärken** eigener Posts, kein VPN, kein Zweitgerät für
  andere Länder, kein zweites Konto, bevor ein Format dreimal gewonnen hat.
- **Bilder:** nur selbst fotografiert (ohne Personen, ohne erkennbare Orte),
  aus den Gratisinhalten von Canva oder von Unsplash/Pexels (Lizenz geprüft,
  keine erkennbaren Personen oder fremden Marken) oder KI-erzeugt. Nie aus
  Pinterest, der Google-Bildersuche oder fremden Posts; fremde Bilder ohne
  Lizenz führen zu Abmahnungen. Die Quelle je Post notierst du.
- **Stimme:** keine eigene. Wenn überhaupt, die Vorlesestimme der Plattform;
  ein Stimmklon ist tabu.
- **KI-Bilder** mit realistisch wirkenden Personen oder Szenen kennzeichnen
  (TikTok-AIGC-Label, KI-Verordnung Art. 50). Am einfachsten sind Grafiken,
  Bildschirmaufnahmen und Text.
- **Kennzeichnung:** Auf einem klar erkennbaren Markenkonto brauchen Posts über
  die eigene App in der Regel kein „Werbung“, wohl aber den TikTok-Schalter
  „Your brand“. Rabattcodes immer mit „Werbung“.
- **App-Ideen, die bezahlte Creator auf TikTok nicht bewerben dürfen:**
  Abnehmen, Gesundheit und Medizin, manche Dating-Apps, schnelles Geld. Solche
  Ideen fallen weg.

**Creator nach dem Signal:** Hat eine App drei Wochen nach dem Start ohne
Werbung mindestens 300 $ MRR, gibt es Geld für Creator, für alle Apps
zusammen bis 18.07. höchstens 750 €. Die Creator zeigen sich selbst, du
nicht.
- **Fällt die Signal-Prüfung in die Startpause**, siehst du am Tag nach deiner
  letzten Prüfung nach: Liegt die App dann über 300 $ MRR, zählt das, und du
  buchst. Sonst gilt die zweite Prüfung, 21 Tage nach dem ersten täglichen Post
  (spätestens Di 29.06.).
- **Ab 19.07. buchst du keine neuen Creator.** Wer bis 18.07. gebucht ist, wird
  nach dem Posten noch bezahlt.
- **Startet App 1 erst Ende Juni,** kommen die Creator-Videos meist erst nach
  Tor 1. Das Tor misst dann im Wesentlichen ohne ihre Wirkung.
- **Preise:** UGC-Videos bei Influee ab etwa 83 € (Stand April 2025); bei
  Collabstr wurden im Schnitt ~150–200 $ je Auftrag bezahlt. Nach der
  Gegenprüfung kostet ein Video, das der Creator selbst postet, typisch
  90–110 € (60–150 €). Dein Angebot: 60–90 € fest je Video samt Posting oder
  ein Rohvideo zum Festpreis für dein Markenkonto. Aus 750 € (nach Gebühren
  und der Umsatzsteuer nach § 13b rund 630 € Leistung) werden so etwa
  6–8 Versuche, bei 60 € je Video bis zu 10.
- **Wen:** nur volljährige Creator mit Sitz in Deutschland, die eine
  Rechnung stellen.
- **Wo buchen:** TikTok One verlangt kein Mindestbudget, Collabstr nimmt eine
  Gebühr je Auftrag (~10 %, zählt zu den 750 €). Insense (650 $ Testmonat) und
  Billo (ab 1.000 $ Paket) binden zu viel Geld.
- **Bezahlen:** Direkt gebuchte Creator erst nach dem Posten. Über eine
  Plattform mit Treuhandkonto geht das Geld vorab dorthin und erst nach deiner
  Freigabe an den Creator; du gibst frei, wenn das Video mit Kennzeichnung
  online ist.
- **Lieferzeit:** rechne mit 1–2 Wochen.
- **Rechte:** Nutzungsrechte oder Spark Ads kosten meist 30–50 % extra.

---

## 9. ETH Zürich und Rückfall

**Zulassung ohne Prüfung mit deutschem Abitur** (ETH, Studienjahr 2026/27;
Änderungen erst ab Herbst 2028):
- **Fächer:** Mathematik, eine Naturwissenschaft (Physik, Chemie oder
  Biologie) und Deutsch oder eine Fremdsprache müssen in den letzten zwei
  Jahren unterrichtet worden **und Prüfungsfächer deines Abiturs** sein.
- **Note (von der ETH am 24.11.2026 per Mail bestätigt):** Es zählen deine
  Ergebnisse in den drei Abiturprüfungen, nicht die Kursnoten. Je Prüfung
  gibt es höchstens 15 Punkte, 70 % davon sind 10,5. Diesen Schnitt musst du
  in den drei Fächern erreichen. Weil Prüfungsergebnisse ganze Punkte sind,
  brauchst du zusammen mindestens **32 von 45 Punkten**, z. B. 11/11/10.
- **Schriftlich und mündlich im selben Fach (ebenfalls bestätigt):** Legst du
  in einem Prüfungsfach eine schriftliche und eine mündliche Prüfung ab,
  zählt die ETH den Durchschnitt aus beiden.
- **Gültigkeit (ebenfalls bestätigt):** Für den Studienbeginn im Herbst 2027
  gelten die Bedingungen unverändert. Maßgeblich ist der Eintrag „ETHZ“ für
  Deutschland auf der Länderseite von swissuniversities.
- **Breite:** Vier weitere Fächer aus Physik, Chemie, Biologie, Informatik,
  weiterer Sprache, Geografie, Geschichte und Wirtschaft müssen in den
  letzten drei Jahren unterrichtet worden sein.
- **Gesamtnote:** Eine Mindest-Abiturnote gibt es nicht.
- **Sonst:** Fehlt etwas, bleibt die reduzierte ETH-Aufnahmeprüfung vom 17.
  bis 27.01.2028 mit Studienbeginn am 18.09.2028. Das kostet ein Jahr. Auch
  dafür bewirbst du dich bis 31.03.2027 in eApply und meldest dich dann vom
  15.09. bis 15.10.2027 eigens zur Prüfung an.
- **Programmieren** ist keine Voraussetzung. Im ersten Jahr wird Java
  unterrichtet.

**Was das für den Plan heißt:**
- **Deine Fächer erfüllen die Bedingung (Stand 23.11.):** Chemie ist P2
  (schriftlich, Do 13.05.), Mathe P4 (schriftlich, Mi 05.05.), Englisch P5
  (mündlich oder als Präsentation, zwischen 19.05. und 07.06.). Damit sind
  Mathe, eine Naturwissenschaft und eine Fremdsprache Prüfungsfächer.
- **Der Wortlaut der Bedingung** (swissuniversities, Eintrag „ETHZ“ für
  Deutschland, Studienjahr 2026/27; laut ETH unverändert für Herbst 2027):
  „Unterricht in den Fächern 1. Mathematik 2. Physik oder Chemie oder
  Biologie und 3. Unterrichtssprache oder Fremdsprache während der letzten
  zwei Jahre vor dem Abitur. Diese drei Fächer müssen Gegenstand der
  Abiturprüfung […] sein. Der Notendurchschnitt dieser drei Prüfungsfächer
  zusammen muss mindestens 70% des Maximalwerts betragen. Zudem müssen vier
  weitere Fächer aus den folgenden Disziplinen Gegenstand der
  Gymnasialausbildung der letzten drei Jahre gewesen sein: Physik, Chemie,
  Biologie, Informatik, eine weitere Sprache, Geografie, Geschichte,
  Wirtschaft. […] Andernfalls: reduzierte ETH-Aufnahmeprüfung“.
- **Noch zu prüfen (10 Minuten mit deinen Zeugnissen der Klassen 11–13):**
  - Chemie, Mathe und Englisch hattest du in Klasse 12 und 13 durchgehend.
  - Zähle deine weiteren Fächer aus dieser Liste: Physik, Biologie,
    Informatik, eine weitere Sprache (Deutsch oder eine zweite Fremdsprache),
    Erdkunde, Geschichte, Wirtschaft. Du brauchst vier. Chemie zählt hier
    nicht noch einmal, weil es schon dein Prüfungsfach ist.
  - Kommst du nur mit Politik-Wirtschaft oder nur mit einem Fach aus Klasse
    11 auf vier, frag bei der Zulassungsstelle gezielt nach. Diese Frage hat
    die ETH in ihrer Antwort nicht einzeln beantwortet.
- **Dein Ziel:** Chemie + Mathe + Englisch zusammen mindestens 32 von
  45 Punkten in den Prüfungen, z. B. 11/11/10. Plane mit Puffer, also eher
  12/11/11.
- **Englisch als P5:** Hast du die Präsentationsprüfung gewählt (die Wahl lag
  am Ende von Q2), bekommst du die Aufgabe zwei Wochen vor dem Termin und
  gibst die Dokumentation eine Woche vorher ab. Diese zwei Wochen gehören
  ganz der Prüfung.
- **Fehlt nach den schriftlichen Ergebnissen wenig:** In Chemie und Mathe
  kannst du eine zusätzliche mündliche Prüfung beantragen (28.–30.06.). Die
  ETH rechnet dann den Durchschnitt aus schriftlich und mündlich.
  - **Beispiel:** Chemie schriftlich 9, Mathe 11, Englisch 11 ergibt
    31 Punkte, einen zu wenig. Mit 13 Punkten in der mündlichen
    Chemieprüfung zählt Chemie (9 + 13) / 2 = 11, zusammen 33.
  - **Achtung:** Eine schlechtere mündliche Prüfung zieht den Schnitt genauso
    nach unten. Beantrage sie nur, wenn dir Punkte fehlen und du dich in dem
    Fach mündlich sicher fühlst.
  - **Für dein Abiturzeugnis** rechnet die Schule anders als die ETH. Frag
    die Oberstufenkoordination vor dem Antrag, wie sich die Prüfung dort
    auswirkt.
- **Die Antwort der ETH** vom 24.11.2026 legst du zu deinen
  Bewerbungsunterlagen.
- Chemie, Mathe und Englisch haben im Abitur Vorrang vor allem in diesem
  Plan.

**Bewerbung**

| Schritt | Termin | Aufwand |
|---|---|---|
| eApply ist offen | 01.12.2026–31.03.2027, danach geht nichts mehr | – |
| Bewerbung abschicken: Passfoto, Ausweis, Lebenslauf (Vorlage der ETH), Einverständniserklärung, Zeugnisse der letzten drei Schuljahre als PDF, Gebühr 150 CHF (nicht erstattbar; nur Kreditkarte, PostFinance, TWINT oder Google Pay, also praktisch eine Kreditkarte, notfalls die deiner Eltern) | **in den Weihnachtsferien (KW 53)** | ~6 h |
| Antwort | ~8 Wochen nach Eingang, also etwa Anfang März | – |
| Abiturzeugnis hochladen, Original per Post | sofort nach der Ausgabe 01.–03.07., spätestens 31.08. | ~1 h |
| Studienbeginn | 20.09.2027 | – |

**Zürich kostet** laut ETH für internationale Studierende ~28.100 CHF im
Jahr:
- **Schulgeld und Beiträge:** 2.264 CHF je Semester.
- **Zimmer:** ~800–1.000 CHF im Monat (Richtwert der ETH). Die
  Studierendenwohnungen von WOKO sind oft günstiger; sie verlangen eine
  Aufnahmebestätigung und mindestens 6 Monate Mietdauer.
- **Kaution:** höchstens drei Monatsmieten (gesetzliche Grenze), oft vor dem
  Einzug fällig.
- **AHV:** Nichterwerbstätige Studierende mit Wohnsitz in der Schweiz zahlen
  ab dem 1. Januar nach dem 20. Geburtstag (bei dir ab 2028) 530 CHF im Jahr
  plus bis zu 5 % Verwaltungskosten. Ob du als Student dort Wohnsitz hast,
  klärt die SVA Zürich mit einem Fragebogen; plane es zur Sicherheit ein.
- **Aufenthaltsbewilligung B:** innerhalb von 14 Tagen nach der Ankunft
  beantragen. Dafür brauchst du einen Finanzierungsnachweis über 21.000 CHF;
  ein Brief deiner Eltern über 1.750 CHF im Monat reicht.
- **Krankenversicherung:** Mit der Europäischen Krankenversicherungskarte
  innerhalb von drei Monaten die Befreiung beantragen. **Jedes Einkommen in
  der Schweiz hebt sie auf.**
  - **Ausnahme:** nur in Ausnahmefällen für Erwerbstätige mit
    Krankenversicherungskarte und Wohnsitz in Deutschland (oder Frankreich,
    Italien, Österreich). Zur Selbstständigkeit sagt die ETH nichts.
  - **Wird aus dem Studienaufenthalt ein Aufenthalt zur Erwerbstätigkeit,**
    ist im Kanton Zürich keine Befreiung mehr möglich, auch keine Rückkehr
    zur Studierendenversicherung. Die Krankenkasse kostet dann mindestens
    250–300 CHF im Monat mehr.

Deshalb gehört jeder Euro, den die App nicht braucht, deinem Start in Zürich.

**Rückfall in Niedersachsen** (Fristen 2026, für 2027 erwartet gleich):
- **Leibniz Universität Hannover**, Informatik: Bewerbung 01.06.–15.07.;
  formal zulassungsbeschränkt, seit 2022 wurden aber alle zugelassen. Diese
  Bewerbung schickst du **auf jeden Fall** bis 15.07. ab (~2 h).
- **Ohne Bewerbung, nur Einschreibung:**
  - TU Braunschweig bis 15.10.
  - Göttingen (Angewandte Informatik) bis 30.09.
  - Osnabrück bis 30.09.
  - Oldenburg 16.07.–15.10.2027
  - TU Clausthal ~15.10.

---

## 10. Wochenvorlagen

**Schulwoche (10 Stunden)**

| Tag | Zeit | was |
|---|---|---|
| Mo–Fr | 1 h, z. B. 18–19 Uhr | 30 min Claudes Ergebnis prüfen und testen, 30 min kleine Sitzung oder Lernen |
| Sa | 5 h, z. B. 10–13 und 14–16 Uhr | 3 h Bau-Sitzung, 2 h Lernen bzw. ab der Gründung Slideshows auf Vorrat |
| So | frei | – |

**Woche mit Klausuren (3 Stunden):** nur Samstag. Das Wichtigste der Woche,
sonst nichts.

**Sonntag ist frei.** Ausnahmen: ab der Gründung 10 Minuten Kassenprüfung
([`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md),
Abschnitt 7.3), sobald eine App im Store ist, dazu 20 Minuten
Wochenauswertung (Vorlage in Abschnitt 16). Beides zählt in die Stunden der
Woche und entfällt in der Ruhezeit und ab einer Woche vor einem
Prüfungstag. Dazu kommen vier Stichtage im Sommer
([`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md),
Abschnitt 1.3): So 04.07. (ist eine App im Store?), So 18.07. (Tor 1),
So 08.08. (Tor 2 und Umschalttag) und So 15.08. (Verkaufsstopp). Posts, die
am Sonntag erscheinen sollen, baust du am Samstag
und planst sie mit den offiziellen Werkzeugen der Plattform ein.

**Ferienwoche (~31–38 Stunden)**

| Tag | Zeit | was |
|---|---|---|
| Mo–Fr (ohne Feiertage) | 9–12 und 13–17 Uhr | Bau-Sitzungen, Tests auf iPhone und iPad, Store-Eintrag |
| Sa | 3 h | Wochenauswertung, Lernen |
| täglich | 1–1,5 h | Schule |

**Q4-Woche (höchstens 6–7 Stunden):** Mo–Fr frei, Sa 3 h, dazu höchstens
zweimal 1–2 h; mit zwei oder mehr Klausuren nur der Samstag. Fertige Posts
(höchstens 3 je Woche, am Samstag gebaut) veröffentlichst du in diesen Zeiten
in je wenigen Minuten oder planst sie ein
([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md), Abschnitt 6.2).

**Abiturzeit:** Ist keine App im Store oder im Review, ruht alles (Ruhezeit,
Abschnitt 4). Sonst 0–5 Stunden, im schriftlichen Abitur 0–1: zweimal
20 Minuten je Woche Zahlen ansehen (einer der zwei Termine ist die
Sonntagsauswertung) und sonntags 10 Minuten Kassenprüfung, zusammen unter
1 Stunde; dazu Notfälle und Antworten an das Review. Nie an Prüfungstagen
und nie ab einer Woche davor. Keine Posts, keine Creator.

**Sommerwoche ab 05.07. bis zum Ende der Jagd (~55 Stunden):** Mo–Sa 9–12,
13–17 und 18–20 Uhr, So frei; davon ~6 Stunden für Zürich.

**Woche mit Ferienjob (ab 19.07., oder ab 05.07. ohne App im Store):**
40 Stunden Arbeit; für die Apps an zwei Werktagen je 20 Minuten Zahlen und
Support, samstags bis zu 3 Stunden; ~6 Stunden für Zürich. Im August kommen
einmalig die Schritte für Übergabe, Verkauf oder Stilllegung dazu
([`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md)).

---

## 11. Diese Woche Tag für Tag (KW 48)

Mo 23.11. bis So 29.11.2026, Schulwoche. Kosten diese Woche: 0 €, Max ist
schon bezahlt.

**Ziel der Woche:**
- Dieses Repository ist privat.
- Claude Code läuft unter Windows.
- Das erste Expo-Projekt läuft auf deinem iPhone.
- Deine Prüfungsfächer sind gegen die ETH-Bedingung geprüft, die Mail an die
  ETH ist raus.
- Eine Karte ist beantragt, falls du keine hast.
- Fünf Ideen für die Prüfung sind gewählt.

| Tag | Zeit | was | Ergebnis |
|---|---|---|---|
| Mo 23.11. | 1 h | 10 min: deine Prüfungsfächer gegen die ETH-Bedingung prüfen (Abschnitt 9) – **erledigt:** Chemie P2, Mathe P4, Englisch P5 erfüllen sie. 40 min: Git for Windows und Node.js (LTS) installieren, dann in PowerShell Claude Code (`irm https://claude.ai/install.ps1 \| iex`); mit `claude` anmelden; `/output-style learning` einschalten und Claude bitten, den Lernmodus in deinen Benutzereinstellungen einzutragen (Abschnitt 7). 5 min: Expo Go auf iPhone und iPad laden. 5 min: auf claude.ai unter Abrechnung nachsehen, wann Max endet, und danach auf Pro umstellen statt Max zu verlängern. | Prüfungsfächer geklärt, Claude Code läuft |
| Di 24.11. | 1 h | 5 min: dieses Repository auf GitHub auf privat stellen (Settings → General → Danger Zone → Change repository visibility → Private). 10 min: Mail an die ETH-Zulassungsstelle (Vorlage in Abschnitt 16), vorher aufschreiben, welche Fächer du in den Klassen 11–13 hattest. 45 min: Expo-Tutorial „Build with AI“ mit Claude Code. | Repository privat, Mail raus, erste App in Expo Go |
| Mi 25.11. | 1 h | Missing Semester: Shell (Teil 1). | Terminal-Grundlagen |
| Do 26.11. | 1 h | Gespräch mit deinen Eltern: Abschnitt 3 zeigen. Wer soll im App Store stehen, du oder ein Elternteil? Darf ihre Anschrift ins Impressum? Würde ein Elternteil im Sommer eine laufende App übernehmen (Abschnitt 14)? Noch nichts entscheiden, nur verstehen; die Namensfrage entscheidet ihr bis So 13.12. **Karte:** Hast du keine eigene Visa- oder Mastercard (Debit reicht, sie muss in US-Dollar zahlen können), beantragst du sie diese Woche bei deiner Bank zum Girokonto; sie kommt oft erst nach 1–2 Wochen. Du brauchst sie ab KW 50 für das Guthaben der Claude API und in KW 51 für Apple (oder du meldest dich bei Apple über die Developer-App an). Für die ETH-Gebühr im Dezember geht notfalls die Karte deiner Eltern. | Fragen geklärt, Karte beantragt, Namensfrage bis 13.12., Zusage zur Übernahme im Januar |
| Fr 27.11. | 1 h | Missing Semester: Shell (Teil 2) und Git (Teil 1). | Terminal- und Git-Grundlagen |
| Sa 28.11. | 5 h | 2 h: Expo-Tutorial „StickerSmash“ mit Erklärungen von Claude. 2 h 15 min: Ideen nach [`details/04_IDEENWAHL.md`](details/04_IDEENWAHL.md): etwa 20 Kandidaten sammeln (12 von Claude, deine eigenen, der Pool aus 04), K.-o.-Fragen und 60-Sekunden-Test für höchstens sechs; 5 gehen in die Prüfung. Bestehen weniger als fünf den Test, folgt am Mo 30.11. ein Nachtest mit weiteren Kandidaten (30 min). 45 min: privates Repository `vorlage` auf GitHub, `CLAUDE.md` aus [`vorlagen/CLAUDE_md_fuer_die_app.md`](vorlagen/CLAUDE_md_fuer_die_app.md), [`vorlagen/checkliste_einreichung.md`](vorlagen/checkliste_einreichung.md) als `docs/checkliste-einreichung.md` kopieren, leere `docs/review-log.md` und `docs/entscheidungen.md` anlegen; solange Max noch läuft, legt Claude damit das leere Vorlagen-Projekt an. | 5 Ideen für die Prüfung markiert, jede mit dem Punkt, in dem sie den kostenlosen Weg schlägt (sonst Nachtest Mo 30.11.); Vorlage im Repository |
| So 29.11. | frei | – | – |

---

## 12. Woche für Woche bis zum Abschluss

Bis zur Einreichung von App 1 steht jeder Tag in
[`details/01_TAG_FUER_TAG_BIS_FEBRUAR.md`](details/01_TAG_FUER_TAG_BIS_FEBRUAR.md),
jedes Arbeitspaket (AP1–AP22) in
[`details/02_BAUPLAN_APP1.md`](details/02_BAUPLAN_APP1.md). Hier steht der
Überblick. Rutscht etwas, überspringst du nichts, sondern schiebst.

### Phase 1 – Grundlagen, Projekt und Idee (KW 49–51, 30.11.–20.12.), Schulwochen, 10 h (mit Klausuren 3 h)

- **Lernen am eigenen Projekt (~3–4 h je Woche):** Missing Semester (Shell,
  Git, Fehlersuche), JavaScript und TypeScript lesen, Expo- und EAS-Doku.
- **Bauen (~4 h je Woche):** Projekt mit dem Expo-Gerüst, zwei Sprachdateien
  und fünf leere Bildschirme (AP1–AP2), Supabase-Funktion mit echter
  KI-Antwort (AP4–AP5), RevenueCat mit fertiger Paywall (AP6).
- **Ideenwahl (~10–16 h, typisch 12 h, von Sa 28.11. bis Sa 19.12.):** fünf Ideen mit
  K.-o.-Fragen, Nachfrageprüfung und Bewertungstabelle, dazu Slideshow-Test,
  Namensprüfung und ein Ablauf-Test in Expo Go mit fünf Erwachsenen
  ([`details/04_IDEENWAHL.md`](details/04_IDEENWAHL.md)). Eigene Markenkonten
  gibt es erst ab der Gründung, wegen des Impressums.
- **Namensfrage bis So 13.12.:** du oder ein Elternteil (Abschnitt 3).
- **Apple Developer Program Mo 14.–Mi 16.12.** (99 €), wenn die Namensfrage
  entschieden ist und das Ideen-Tor absehbar bestanden wird: Am Sa 12.12.
  erfüllt mindestens eine Idee alle Mindestwerte. Automatische Verlängerung
  gleich abschalten. Kommt nach 24 Stunden keine Bestätigung, wendest du dich
  an Apple.
- **Verwaltung vorbereiten (~1 h):** ELSTER-Benutzerkonto anlegen (mit dem
  Online-Ausweis sofort, sonst kommt ein Brief, der bis zu zwei Wochen
  braucht); PIN des Personalausweises prüfen; nachsehen, wie deine Gemeinde
  die Gewerbeanmeldung online annimmt; Termin der kostenlosen
  Gründungsberatung anfragen.
- **Ideen-Tor (Entscheidung Sa 19.12.) und Messpunkt M0 (So 20.12.):** eine
  Idee für App 1, die zweitbeste als Reserve für App 2; `SPEC.md` steht; die
  App zeigt eine echte KI-Antwort. Die Paywall kommt im Durchstich am
  Mi 23.12. dazu. In den Fällen, die 04 in Abschnitt 7 nennt (z. B. eine
  Klausurwoche hat die Prüfung verschoben), liegt das Ideen-Tor spätestens am
  Mo 28.12.
- **No-Go-Regel:** Besteht keine Idee, wird nicht gegründet und kein
  Apple-Konto gekauft. Du lernst weiter, baust nur die Pakete, die keine Idee
  brauchen, und prüfst nach der ETH-Bewerbung fünf neue Ideen (Entscheidung bis
  Sa 09.01.). Besteht auch dann keine, gründest du nicht vor dem Abitur
  ([`details/04_IDEENWAHL.md`](details/04_IDEENWAHL.md), Abschnitt 7).

### KW 52 (21.–27.12.), ~9 h – Durchstich

- Mo/Di je 1 h, Mi 23.12. (erster Ferientag) 7 h; 24.–27.12. frei.
- **Durchstich (AP7–AP8):** Entwicklungs-Build auf iPhone und iPad, Testkauf
  im RevenueCat Test Store, die Server-Funktion prüft das Abo und liefert die
  KI-Antwort. Alles mit hässlicher Platzhalter-Oberfläche: erst das Riskante,
  dann das Schöne.

### KW 53 (28.12.–03.01.), Weihnachtsferien, ~31 h (Neujahr frei)

- **ETH-Bewerbung (6 h, Mo 28.12.):** Lebenslauf mit Claude nach der
  ETH-Vorlage, Zeugnisse der letzten drei Schuljahre scannen, Passfoto,
  Einverständniserklärung, Gebühr 150 CHF per Kreditkarte (privat, nicht aus
  dem App-Geld). **Abschicken.**
- **Store-Build und TestFlight (AP9),** dann am **Di 29.12. der
  Stunden-Messpunkt:** Wie viele Stunden haben AP1–AP9 gebraucht (geplant
  ~32)? Bis ~40 weiter wie geplant; 40–60: App 1 kleiner schneiden; über 60:
  Einreichung erst nach dem Abitur einplanen.
- **App 1:** Kernfunktion mit Prompt und 20 Testfällen (AP10), Onboarding
  (AP11), Einwilligung, „Antwort melden“ und Fehlerfälle (AP13).
- **Ferienjob:** drei Bewerbungen für Mo 19.07.–Di 31.08. oder bis Fr 10.09.
  (1–2 h, [`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md)).

### KW 01 (04.–10.01.), Ferien, ~38 h (der 06.01. ist in Niedersachsen kein Feiertag)

- **App 1:** Paywall-Feinschliff (AP12; harte Paywall ohne Umschalter,
  Wochen- und Monatsabo, „Käufe wiederherstellen“, Links zu Datenschutz und
  Nutzungsbedingungen), Einstellungen (AP14), Tageslimit und Kostenbremse
  (AP15), Aussehen und Name (AP16), Tests auf iPhone und iPad (AP17).
- **Messpunkt M2 – gründen, sobald App 1 etwa halb steht** (Kernfunktion
  läuft mit echter KI, Onboarding und Paywall stehen). Dann Checkliste A in
  zwei Teilen (~4 h): Gewerbe, Fragebogen in ELSTER, Domain-Paket,
  Prepaid-Nummer; am nächsten Tag bei Apple der Vertrag für bezahlte Apps,
  Bank- und Steuerdaten, Händlerangaben und das Small Business Program
  ([`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md)).
  - **Wann das meist ist:** Im Kalender (01) frühestens am Do 07.01.,
    typisch Mitte bis Ende Januar. Im Modell wird im Median in der Woche ab
    Mo 18.01. gegründet, in 38 von 100 Läufen erst im Februar oder später.
  - **Später Fall:** Ist M2 bis Mo 01.03. nicht erreicht, gründest du am Tag
    nach deiner letzten Prüfung, parallel zum Rest-Bau.
- **Website und Store-Eintrag (AP18–AP19),** Sicherheits-Mindestprüfung
  (AP20).
- **Messpunkt M1 (Sa 09.01.):** ETH-Bewerbung abgeschickt, AP10–AP17 fertig.

### KW 02–04 (11.–31.01.), Schulwochen, 10 h (Q3-Ende, mit Klausuren 3 h)

- **Gründung**, falls noch nicht geschehen.
- **Brief an die Krankenkasse**, sobald das Gewerbe angemeldet ist (Vorlage
  in Abschnitt 16): Schüler mit Gewerbe; deine echten Stunden (Schulwochen
  3–10, Q4 höchstens 7, Ferien bis 38, nach der Schule bis ~50 je Woche);
  erwarteter Gewinn unter 590 € im Monat, keine Angestellten; Bitte um
  schriftliche Bestätigung.
- **Zusage des Elternteils** für eine mögliche Übergabe im Sommer, eine
  Seite schriftlich (Abschnitt 14). **Oberstufenkoordination fragen,** wann
  die mündlichen Prüfungen liegen.
- **TestFlight mit der Familie (AP21),** Sandbox-Kauf im Store-Build, Fehler
  beheben.
- **Funktions-Stopp So 24.01.:** danach nur noch Fehler, Texte, Einreichung.
- **Fr 29.01. Halbjahreszeugnis:** Lade es in eApply nach, falls die ETH es
  verlangt.

### KW 05 (01.–07.02.), Halbjahresferien Mo/Di, ~19 h

- Mo/Di je ~7 h, ab Mi 03.02. gilt die Q4-Regel (Sa 3 h, höchstens zweimal
  1–2 h).
- **Einreichen bis Di 02.02. (AP22),** sobald Checkliste C steht, mit „Diese
  Version manuell veröffentlichen“ (Abschnitt 4). Abo-Gruppe und Abos
  zusammen mit dieser Version einreichen.
- **Markenkonten** in der Woche der Einreichung anlegen, mit Link
  „Impressum“ ([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md)).

### KW 06–10 (08.02.–14.03.), Q4, höchstens 6–7 h

- **Ist App 1 eingereicht:** auf das Review reagieren. Den Grund jeder
  Ablehnung schreibst du in `docs/review-log.md`, Claude schlägt die kleinste
  Lösung vor. Rechne mit 1–2 Ablehnungen bei der ersten App; 90 % der Prüfungen
  sind in 48 Stunden fertig.
- **Posts seit der Einreichung:** höchstens 3 je Woche, gebaut in einem Block
  von 90 Minuten am Samstag; höchstens 9, solange die App nicht im Store ist.
  In Q4 übst du nur und misst einen Ausgangswert; über Formate entscheidest du
  im Sommer.
- **Ist sie bis Sa 13.03. freigegeben:** selbst veröffentlichen und starten.
- **Ist sie nicht freigegeben,** bleibt sie dank der Freigabe „manuell“ bis
  nach deiner letzten Prüfung liegen.
- **Signal in Q4:** Die Prüfung drei Wochen nach dem Start ist für eine App,
  die vor dem Abitur startet, nur ein Vorab-Blick. Wird sie bestanden, zählt
  sie (Creator buchst du trotzdem erst nach deiner letzten Prüfung). Wird sie
  verfehlt, gilt die zweite Prüfung, 21 Tage nach dem ersten täglichen Post
  nach der letzten Prüfung (spätestens Di 29.06.).
- **Gründung**, falls M2 bis Mo 01.03. erreicht ist (Checkliste A; in Q4 auf
  zwei Samstage verteilt). Danach erst wieder nach der letzten Prüfung.
- **Ist App 1 noch nicht eingereicht:** im Rahmen der Q4-Stunden weiterbauen,
  ohne Druck. Im Modell ist sie bis 14.03. nur in 33 von 100 Läufen
  fertig, und das ist kein Fehler.
- **Messpunkt M3 (So 14.03.):** Ist App 1 gestartet, freigegeben, im Review
  oder noch im Bau? Davon hängt die Ruhezeit ab (nächster Abschnitt).
- **ETH-Antwort (etwa Anfang März):** lesen und ablegen; bei Fragen an die
  Zulassungsstelle wenden.

### KW 11–22 (15.03.–06.06.), Ende Q4 und Abitur

- **Deine Prüfungstage:** Mathe Mi 05.05., Chemie Do 13.05., Englisch (P5)
  am Termin deiner Schule zwischen 19.05. und 07.06., dazu P1 und P3. Ab einer
  Woche vor jedem dieser Tage gar nichts an der App.
- **Ruhezeit (Entscheidung am So 14.03.):**
  - **Keine App im Store und keine im Review:** Die App ruht ganz. Du
    kündigst Claude Pro am 14.03. zum Ende des bezahlten Monats (es läuft dann
    bis Ende März aus) und buchst es erst nach deiner letzten Prüfung wieder.
    Null Stunden, null Posts.
  - **Eine App ist im Store oder im Review:** 0–5 Stunden je Woche (im
    schriftlichen Abitur 0–1) für Zahlen, Notfälle (Abschnitt 18) und
    Antworten an das Review, nie an Prüfungstagen und nie ab einer Woche
    davor. Claude Pro läuft weiter. Ist eine App live oder im Review, läuft
    für diese Monate Supabase Pro (~27 € im Monat), damit der Server nicht
    pausiert; die Wachregel ginge ab einer Woche vor jedem Prüfungstag nicht
    ([`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md),
    Abschnitt 7.5). Liegt eine freigegebene App nur bereit, darf das
    Gratis-Projekt pausieren; vor dem Veröffentlichen stellst du es wieder her
    und testest. Keine Posts, keine Creator.
- **Support-Mails:** Du beschreibst Claude das Problem in eigenen Worten, ohne
  Namen, E-Mail-Adresse, Kaufdaten oder Fotos. Claude entwirft eine
  Antwortvorlage, die du selbst in dein Mailprogramm einsetzt.

### KW 23–26 (07.06.–04.07.), nach dem Abitur, 15–40 h

- **Am Tag nach deiner letzten Prüfung:** Claude Pro wieder buchen. Noch nicht
  gegründet → jetzt gründen, parallel zum Rest-Bau (2–3 Wochen Vorlauf bis zur
  Einreichung, [`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md)).
- **App 1 starten** (veröffentlichen oder fertig bauen und einreichen).
  Täglich 2–3 Posts ohne Gesicht, etwa 14 Minuten je Post
  ([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md)).
- **Signal-Prüfung** drei Wochen nach dem Start, für eine vor dem Abitur
  gestartete App 21 Tage nach dem ersten täglichen Post, spätestens am
  **Di 29.06.:** ≥ 300 $ MRR → Creator buchen (Checkliste F,
  für alle Apps zusammen bis 18.07. höchstens 750 €); sonst nur eigene Posts
  weiter.
- **App 2** (die zweitbeste Idee) aus deiner Vorlage, mit anderer
  Kernfunktion. Reine Varianten lehnt Apple ab. Im Modell erscheint eine
  zweite App in 81 von 100 Läufen, im Median um den 12.07.
- **Ende Juni:** Hast du noch keinen Ferienjob, fragst du zwei
  Zeitarbeitsfirmen für einen festen Beginn an.
- **Zeigt eine App Ende Juni nennenswerten Umsatz** (Richtwert ~100 $ MRR;
  genauer Auslöser in [`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md),
  Abschnitt 4.4): Das Elternteil, das zugesagt hat, schickt bis Fr 02.07.
  Gewerbe- und Apple-Anmeldung ab; Vertrag, Bank, Steuer, Händlerangaben und
  Small Business Program folgen, sobald das Konto frei ist (Abschnitt 14).
- **Bis 15.07.:** Bewerbung an der Leibniz Universität Hannover (~2 h).
- **01.–03.07.:** Abiturzeugnis in eApply hochladen, Original an die ETH.
- **Stichtag So 04.07.:** Ist noch keine App im Store, beginnt der Ferienjob
  am Mo 05.07., und du beginnst keine neue App mehr. Eine eingereichte App
  darf noch erscheinen. Im Modell trifft das in 20 von 100 Läufen zu.

### KW 27–28 (05.–18.07.), Sommer, ~55 h (davon ~6 h für Zürich)

- Posts, Auswertung, App 2 fertig, eingereicht und gestartet. Apps, die nach
  dem 04.07. erscheinen, bieten nur das Wochenabo an. Bleibt Zeit, beginnt
  App 3; sie muss bis 18.07. eingereicht sein.
- Zimmer in Zürich suchen (WOKO braucht die Zulassung), Finanzierungsbrief
  der Eltern.
- **Tor 1 (So 18.07.):** Abschnitt 13.

### KW 29–37 (19.07.–15.09.), Ferienjob und Abschluss

- **Weg A, B oder C** (Abschnitt 14). In 99 von 100 Läufen ist es Weg A:
  - **Mo 19.07.:** Ferienjob beginnt. Am selben Tag kündigst du alles, was
    Betrieb und Abschluss nicht brauchen.
  - Apps, die am 18.07. schon eingereicht waren, erscheinen noch, ohne
    Creator-Geld (im Modell in 60 von 100 Läufen, eine dritte App im Median
    um den 26.07.). Für die Apps bleiben 2–5 Stunden je Woche: an zwei
    Werktagen je 20 Minuten Zahlen und Support, samstags bis 3 Stunden, sonst
    Posts nach Lust.
  - **Bis Sa 31.07.:** je App entscheiden: einstellen, übergeben oder
    verkaufen (für eine App, die erst nach Mo 19.07. erscheint, bis
    Sa 07.08.).
  - **So 15.08.:** ohne Nachfolger alle Abos aus dem Verkauf nehmen.
  - **Mi 15.09.:** letzter Tag des Dienstes. **Do 16.09. oder Fr 17.09.:** App
    entfernen, Server aus, Gewerbe abmelden (Checkliste H).
- Daneben ~6 Stunden je Woche für Zürich: Zimmer, Unterlagen, Mathe nach den
  Empfehlungen der ETH (Folgen und Reihen, Induktion, komplexe Zahlen,
  Analysis, Vektorgeometrie), Java-Tutorial der ETH.
- **Mo 20.09.:** Studienbeginn.

---

## 13. Die Messpunkte und was du dann tust

| Messpunkt | Frage | Ja | Nein |
|---|---|---|---|
| **Namensfrage** So 13.12. | Steht fest, wer im App Store steht? | Apple-Anmeldung Mo 14.–Mi 16.12. | Apple-Anmeldung und Durchstich rutschen |
| **Zwischenstand Ideen** Sa 12.12. | Erfüllt mindestens eine Idee alle Mindestwerte? | Apple-Anmeldung Mo 14.–Mi 16.12. | Apple erst nach dem Ideen-Tor |
| **M0 / Ideen-Tor** Sa 19.12. / So 20.12. | Besteht eine Idee (Mindestwerte, Slideshow-Test, Ablauf-Test)? `SPEC.md` und echte KI-Antwort in der App? | weiter; fehlt `SPEC.md` oder die KI-Antwort, holst du sie am Mi 23.12. zuerst nach | **No-Go** (keine Idee besteht): nicht gründen, kein Apple-Konto; weiter lernen; fünf neue Ideen nach der ETH-Bewerbung, Entscheidung bis Sa 09.01. |
| **Stunden-Messpunkt** Di 29.12. | Wie viele Stunden haben AP1–AP9 gebraucht (geplant ~32)? | bis ~40: weiter wie geplant | 40–60: App 1 kleiner schneiden; über 60: Einreichung erst nach dem Abitur einplanen |
| **M1** Sa 09.01. | ETH-Bewerbung abgeschickt? AP10–AP17 fertig? | weiter | ETH-Bewerbung hat Vorrang, fehlende Pakete in KW 02–04 |
| **M2** App 1 halb fertig (Kriterien in KW 01; im Median am 18.01.) | Rechtsform entschieden? | gründen (Checkliste A) | ohne Gründung kein Start: weiterbauen. Ist M2 bis Mo 01.03. nicht erreicht, gründest du am Tag nach deiner letzten Prüfung, parallel zum Rest-Bau |
| **Funktions-Stopp** So 24.01. | – | nur noch Fehler, Texte, Einreichung | – |
| **Einreichung** bis Di 02.02. | Checkliste C grün? | einreichen mit „manuell veröffentlichen“ | in Q4 mit 6–7 Stunden je Woche fertig machen, ohne Druck |
| **M3** So 14.03. | App 1 im Store oder im Review? | 0–5 Stunden im Abitur für Zahlen und Notfälle, Claude Pro läuft weiter | **Ruhezeit:** Claude Pro ruht, kein Bau bis nach der letzten Prüfung |
| **Signal** 3 Wochen nach jedem Start | ≥ 300 $ MRR ohne bezahlte Werbung? Fällt der Tag in die Startpause, siehst du am Tag nach deiner letzten Prüfung nach; bestanden zählt, sonst gilt die zweite Prüfung | Creator-Geld, für alle Apps zusammen bis 18.07. höchstens 750 € | nur eigene Posts, nächstes Format oder nächste App |
| **Zweite Signalprüfung** 21 Tage nach dem ersten täglichen Post nach der letzten Prüfung, spätestens Di 29.06. (nur für eine App, die vor dem 15.03. gestartet ist) | ≥ 300 $ MRR? | wie Signal | wie Signal |
| **Stichtag** So 04.07. | Ist eine App im Store? | weiter bis Tor 1 | Ferienjob ab Mo 05.07., keine neue App mehr |
| **Tor 1** So 18.07. | eine App am Stichtag ≥ 5.000 $ MRR? | weiter (Weg B oder C) | **Weg A:** keine neue App, keine neuen Creator, Ferienjob ab Mo 19.07.; schon eingereichte Apps dürfen noch erscheinen |
| **Ausgang je App** bis Sa 31.07. | Monatsgewinn über ~150 €? Elternteil hat zugesagt? Ab 300 $ Monatsumsatz und 8 Wochen im Store? | übergeben oder verkaufen (Abschnitt 14) | einstellen |
| **Tor 2** So 08.08. | ≥ 10.000 $? | Weg C | Weg B endet wie Weg A |
| **Verkaufsstopp** So 15.08. | Gibt es einen Nachfolger oder Käufer? | Abos bleiben im Verkauf, Übertragung starten | alle Abos aus dem Verkauf nehmen |
| **Dienstende** Mi 15.09. | 31 Tage seit dem Verkaufsstopp vorbei? | Do 16.09. oder Fr 17.09.: App entfernen, Server aus, Gewerbe abmelden (Checkliste H) | warten, bis die Frist um ist |

**Welche Zahl gilt:**
- **Signal und Tore:** in RevenueCat die Kennzahl **MRR**, also der
  hochgerechnete Monatsumsatz der laufenden Abos, brutto vor Apples Anteil, in
  US-Dollar. Abgelesen wird am 21. Tag nach dem Start (Signal) bzw. am
  Stichtag (Tor 1 und Tor 2).
- **Ausgang je App:** der Monatsgewinn in Euro: Apples Auszahlung für die
  letzten vier Wochen minus die laufenden Kosten der App (Server, KI-API,
  Domain). Claude Pro zählt nicht mit, weil es nach der Jagd endet.
- **Familienversicherung:** Dafür zählt ebenfalls der Gewinn in Euro, nach
  Apples Anteil und allen Kosten.

500.000 € bis 31.08.2027 erreicht das Modell in keinem einzigen Lauf. Das ist
keine Frage des Einsatzes: Die Zeit nach dem Abitur ist zu kurz, damit eine
App so weit wachsen kann.

---

## 14. Ab Juli: drei Wege

**Die Pflicht, die alle Wege bestimmt:** Apple verlangt mindestens 31 Tage
zwischen „Abo aus dem Verkauf nehmen“ und dem Ende des Dienstes. Aus dem
Verkauf nehmen stoppt neue Abschlüsse und Verlängerungen. Du beendest das
Gewerbe vor dem Umzug. Ohne Nachfolger heißt das: **Verkaufsstopp So 15.08.,
Dienstende Mi 15.09.** Ziehst du früher um, liegt das Dienstende spätestens
am Tag vor dem Umzug und der Verkaufsstopp 31 Tage davor. Mit dem
Verkaufsstopp rücken alle Termine ab der Entscheidung je App um dieselbe Zahl
Tage vor; die Entscheidung fällt aber frühestens am Mo 19.07. Den Umzugstag
legst du bis Sa 31.07. fest, bei einem Umzug vor Sa 18.09. schon bis
Mo 19.07. Alle Schritte stehen in
[`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md)
(früherer Umzug: Abschnitt 1.4).

### Weg A – kein Treffer (~99 von 100 Läufen)

- **Ab Mo 19.07. Ferienjob** als kurzfristige Beschäftigung, von Anfang an
  schriftlich befristet bis Di 31.08. (32 Arbeitstage, 256 Stunden) oder
  gleich bis Fr 10.09.
  - **Geld:** bei 14,60 € je Stunde (Mindestlohn 2027) 3.738 €, bei 15,87 €
    4.063 €, bei 18,50 € 4.736 €. Sozialabgaben fallen nicht an, wenn der
    Arbeitgeber dich als kurzfristig und nicht berufsmäßig beschäftigt meldet
    (Schulentlassener mit Studienabsicht; höchstens 3 Monate oder
    70 Arbeitstage im Kalenderjahr, alle kurzfristigen Jobs 2027 zusammen). Ob
    ein Studium in der Schweiz genauso zählt, nennt keine Quelle
    ausdrücklich: vor der Unterschrift beim Arbeitgeber oder bei der
    Minijob-Zentrale schriftlich fragen. Die Lohnsteuer wird zunächst
    einbehalten (ausgezahlt 84–88 %) und kommt 2028
    über die Steuererklärung zurück.
  - **Familienversicherung:** Lohn aus einer kurzfristigen Beschäftigung
    zählt nicht als regelmäßiges Einkommen. Lass es vor der Unterschrift von
    der Krankenkasse schriftlich bestätigen (das Elternteil fragt, über das
    die Versicherung läuft).
  - **Im Modell** klappt der Job in 70–85 von 100 Fällen und bringt dann im
    Median rund 3.770 €.
- **Keine neue App, keine neuen Creator.** Apps, die am 18.07. schon fertig
  gebaut oder eingereicht sind, dürfen noch erscheinen, nur mit Wochenabo.
- **Am selben Tag kündigst du,** was Betrieb und Abschluss nicht brauchen.
  Claude Pro erst, wenn die Summen für die EÜR erstellt sind.
- **Bis Sa 31.07. entscheidest du je App:**

  | Ausgang | wann | was geschieht |
  |---|---|---|
  | **einstellen** | unter ~150 € Monatsgewinn | So 15.08. Abos aus dem Verkauf, Hinweis in App und Website, Abonnenten informieren, ab dann keine Posts und keine Werbung mehr für diese App; Server und KI laufen bis Mi 15.09. (vorher in RevenueCat prüfen, dass kein Abo mehr aktiv ist); am Do 16.09. oder Fr 17.09. App entfernen, Markenkonten schließen |
  | **übergeben** an ein Elternteil | ab ~150 € Monatsgewinn und schriftliche Zusage aus dem Januar | das Elternteil hat bis Fr 02.07. Gewerbe- und Apple-Anmeldung abgeschickt (Auslöser in 06, Abschnitt 4.4); Vertrag für bezahlte Apps, Bank-, Steuer- und Händlerangaben und Small Business Program (ein eigener Antrag; Genehmigung bis Sa 31.07., dann gilt der niedrige Satz ab Mo 16.08.) folgen, sobald das Konto frei ist; Übertragung der App gestartet bis So 15.08.; echte Schenkung ohne Gewinnbeteiligung, schriftlich, binnen drei Monaten dem Finanzamt angezeigt (§ 30 ErbStG); das Elternteil prüft vorher, ob es schon Kleinunternehmer ist, und wird Unternehmer mit eigenem Impressum, Gewerbe und Steuer. Das Geld danach gehört dem Elternteil; von Zürich aus arbeitest du nicht mit. Ob gelegentliche unbezahlte Hilfe als Erwerbstätigkeit zählt, ist nicht geklärt: Bevor du hilfst, fragt ihr die SVA Zürich schriftlich (06, Abschnitt 4.7) |
  | **verkaufen** | ab 300 $ Monatsumsatz und 8 Wochen im Store | Angebot auf einem Marktplatz mit ehrlichen Zahlen, sobald beides erfüllt ist; klappt in etwa einem von vier solchen Fällen und bringt netto etwa 1,7–10 Monatsgewinne (typisch rund 4); Rückfall am So 08.08. (Umschalttag) ist die Übergabe. Vor der Unterschrift die Krankenkasse schriftlich fragen (der Verkauf eines ganzen Betriebs zählt nach den Hinweisen der Kassen nicht als regelmäßiges Einkommen) und alles Wesentliche in einem Vorgang verkaufen, den Rest gleichzeitig aufgeben; Übergangsrechnung und Steuer klärst du in der bezahlten Einzelstunde |

- **Weiterlaufen lassen von Zürich aus: nein.** Mit Gewerbe in Zürich kommen
  eine Anmeldung bei der SVA, Schweizer Steuern und AHV-Beiträge hinzu, und
  dein Einkommen hebt die Befreiung von der Schweizer Krankenversicherung auf
  (rund 3.500–5.500 CHF Mehrkosten im Jahr). Das lohnt nur bei einem echten
  Treffer und nur nach Beratung zu beiden Ländern.
- **Mi 15.09.:** letzter Tag des Dienstes. **Do 16.09. oder Fr 17.09.:** App
  entfernen, Gewerbe abmelden (0–32,50 €), Krankenkasse informieren
  (Checkliste H).
- Die letzte EÜR und Einkommensteuererklärung 2027 gibst du 2028 per ELSTER
  ab, auch aus Zürich. Damit kommt auch die Lohnsteuer aus dem Ferienjob
  zurück.

### Weg B – Tor 1 bestanden, Tor 2 verfehlt (~0,4 von 100)

- Bis 08.08. Creator nur aus dem Umsatz der letzten vier Wochen, abzüglich
  der Creator, die schon daraus bezahlt sind; jede Woche ein Paywall-Test.
- Kein Ferienjob vor Tor 2. Hast du einen Vertrag unterschrieben, brauchst du
  dafür die Kündigungsklausel oder Probezeit, die du hineingeschrieben hast.
- Danach wie Weg A. Verkaufen oder Übergeben ist hier meist die beste Wahl,
  weil die App messbaren Umsatz hat.
- Achte auf die Familienversicherung (Jahresgewinn 2027 über ~7.080 €, also
  im Schnitt über ~590 € im Monat) und melde Gewinne der Krankenkasse.

### Weg C – ein echter Treffer (~0,3 von 100)

- Steuerberatung zu Deutschland und der Schweiz **vor** dem Umzug: verkaufen,
  ein Elternteil übernimmt, oder geordnet weiterführen.
- Erst jetzt lohnt sich, was vorher zu teuer war: Max oder Ultra mit einem
  Agenten für Berichte und Support-Entwürfe, ein Helfer auf Rechnung,
  eventuell eine UG. Die App lässt sich dann von deinem Konto auf das Konto
  der Firma übertragen (Apple „App Transfer“; Bedingungen vorher prüfen, z. B.
  der Status der Abo-Produkte).
- Das ETH-Studium hat Vorrang. Im Basisjahr gibt es keine Wachstumsphase,
  höchstens Wartung.

---

## 15. Checklisten

### A – Gründung als Einzelunternehmen (bei M2)

- [ ] Entscheidung: du oder ein Elternteil (Abschnitt 3), mit den Eltern
      besprochen (bis So 13.12.)
- [ ] Kostenlose Gründungsberatung der IHK (vorher fragen, ob sie kostenlos
      ist und Steuerfragen beantwortet); sonst die Fragen schriftlich ans
      Finanzamt. Eine bezahlte Einzelstunde beim Steuerberater nur, wenn am
      31.07. Einnahmen da sind oder Verzicht, Verkauf, Übergabe oder
      Fortführung anstehen (Festpreis vorher vereinbaren)
- [ ] **Kleinunternehmerregelung anwenden** (kein Verzicht). Die
      Apple-Erlöse zählen nicht zur Umsatzgrenze der Kleinunternehmerregelung
      (in Deutschland nicht umsatzsteuerbar); für EÜR, Einkommensteuer und
      Familienversicherung zählen sie voll. Rechnungen ausländischer Anbieter
      ohne deutsche Umsatzsteuer (z. B. Supabase Pro, Expo, Werbung; bei der
      Claude API und der Apple-Gebühr auf der Rechnung prüfen) kosten
      Kleinunternehmer 19 % Umsatzsteuer nach § 13b, die sie nicht
      zurückbekommen. Weist die Rechnung deutsche Umsatzsteuer aus, entfällt
      § 13b. Fiele § 13b auf eine Rechnung vom Dezember 2026, fragst du das
      Finanzamt, ob dafür eine Erklärung 2026 nötig ist
- [ ] Finanzamt schriftlich gefragt, ob es für § 13b Voranmeldungen verlangt
      oder die Jahreserklärung genügt; Antwort abgelegt
- [ ] Gewerbe online bei deiner Gemeinde anmelden (~20–65 €), Tätigkeit z. B.
      „Entwicklung und Vertrieb von Software-Apps“
- [ ] Fragebogen zur steuerlichen Erfassung in ELSTER (Gewinn ehrlich
      schätzen, Umsatzsteuer-Identifikationsnummer mit beantragen)
- [ ] Zweitnummer, Support-Adresse auf der Domain, Website mit Impressum und
      Datenschutzerklärung
- [ ] Apple Developer Program als Einzelperson (99 €; eigene Kreditkarte oder
      Anmeldung über die Apple-Developer-App; Zwei-Faktor-Anmeldung) ist seit
      KW 51 erledigt, automatische Verlängerung ist ausgeschaltet
- [ ] Schreiben der IHK beantwortet, Unternehmen bei der Berufsgenossenschaft
      angemeldet (ohne Beschäftigte kein Beitrag)
- [ ] Belegtabelle läuft seit KW 48 (Spalten nach
      [`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md), Abschnitt 7.1)
- [ ] Brief an die Krankenkasse abgeschickt, Antwort abgelegt
- [ ] Ordner für Belege (Claude sortiert, du legst ab)
- [ ] Du weißt, welche Post nach der Anmeldung echt ist (Abschnitt 18,
      „Formularfallen“)

### B – Apple

**Nach der Apple-Anmeldung (KW 51):**
- [ ] iPhone und iPad registriert, Entwicklermodus an

**Erst am Tag nach der Gewerbeanmeldung, nie vorher:**
- [ ] Paid Apps Agreement, Bankverbindung, Steuerformular
- [ ] EU-Händlerangaben: Adresse oder Postfach mit Nachweis, Zweitnummer,
      E-Mail
- [ ] Small Business Program am selben Tag wie das Paid Apps Agreement
      beantragt (in den EU-Stores 15 % statt 26 %, sonst 15 % statt 30 %; der
      niedrigere Satz gilt erst ab dem 16. Tag nach Ende des
      Apple-Fiskalmonats der Genehmigung)

### C – Vor jeder Einreichung

- [ ] Kernfunktion läuft auf iPhone **und iPad**, auch ohne Netz (Meldung
      statt Absturz)
- [ ] Einwilligung vor dem ersten KI-Aufruf mit Nennung des Anbieters
      (5.1.2(i))
- [ ] Harte Paywall ohne Umschalter und in App 1 ohne Testphase; Preis,
      Laufzeit, Verlängerung und Kündigung genannt (3.1.2)
- [ ] „Käufe wiederherstellen“ (3.1.1)
- [ ] Links zu Datenschutzerklärung und Nutzungsbedingungen in der App und in
      App Store Connect
- [ ] Abo-Gruppe und Abos zusammen mit dieser Version eingereicht
- [ ] Impressum, Datenschutzerklärung, Nutzungsbedingungen und „Käufe
      wiederherstellen“ ohne Abo erreichbar: als Links direkt auf der Paywall
      (zusätzlich in den Einstellungen)
- [ ] Richtlinie 1.2: feste Anweisungen und Längenbegrenzung als Filter,
      Knopf „Antwort melden“ (E-Mail-Link), Kontaktadresse in der App; in den
      Review-Notizen: Ausgaben sieht nur der Nutzer selbst, und auf welchem
      Bildschirm die Paywall erscheint
- [ ] Datenschutzangaben („App-Datenschutz“) in App Store Connect passen zur
      App: Eingabetext geht an Anthropic und bleibt dort bis zu 30 Tage,
      RevenueCat verarbeitet Kennung und Käufe – nicht „Keine Daten erfasst“
      wählen; Apples Definition vor dem Ausfüllen lesen
- [ ] Vor der ersten Einreichung geprüft, ob du als Anbieter der App nach
      Art. 50 Abs. 2 KI-Verordnung KI-erzeugte Texte maschinenlesbar
      kennzeichnen musst und wie (z. B. in geteilten Ergebnissen); die
      Recherche hat das nicht geprüft
- [ ] App 1 nur fürs iPhone: in `app.json` `ios.supportsTablet: false` (Expo-
      Vorlagen setzen teils `true`). Apple prüft sie trotzdem auf dem iPad,
      also dort weiter testen; iPad-Screenshots entfallen
- [ ] Screenshots vom eigenen iPhone; für eine fehlende Größe in Canva auf das
      verlangte Format setzen, der Bildinhalt bleibt die echte App
- [ ] Exportkontrolle: nur Standardverschlüsselung (HTTPS), in `app.json`
      `ios.config.usesNonExemptEncryption: false`
- [ ] Altersfreigabe in App Store Connect ehrlich beantwortet;
      Nutzungsbedingungen und Onboarding sagen „ab 18“; der Hinweis, dass die
      Antworten von einer KI kommen, steht vor dem ersten Aufruf
- [ ] Keine Platzhalter, echte Screenshots, Backend läuft (2.1)
- [ ] Keine Gesundheitsversprechen, keine fremden Marken, eigene
      Kernfunktion (4.3)
- [ ] Hinweise für das Review: was die App tut, wie man die Paywall testet
- [ ] Mindestprüfung Sicherheit (Abschnitt 7) bestanden
- [ ] Review-Log gelesen

### D – Datenschutz

- [ ] Verträge zur Auftragsverarbeitung mit Anthropic (API), Supabase,
      RevenueCat, Expo (wenn `expo-updates` eingebaut ist; vor dem Schritt
      prüfen, ob Expo einen Vertrag anbietet) und dem Anbieter von Website und
      E-Mail
- [ ] Eingaben werden nach der Antwort nicht auf dem Server gespeichert; der
      Verlauf liegt nur auf dem Gerät
- [ ] Eigene Messereignisse nur mit Einwilligung (§ 25 TDDDG)
- [ ] Keine Gesundheitsdaten (Art. 9 DSGVO) erheben
- [ ] Datenschutzerklärung nennt alle Dienste mit Speicherdauer (Anthropic
      bis 30 Tage) und dich als Verantwortlichen
- [ ] Onboarding-Frage „Woher kennst du die App?“: freiwillig mit
      „Überspringen“, die Antwort wird sofort und ohne App-User-ID gezählt und
      steht in der Datenschutzerklärung. Sie wird nicht auf dem Gerät
      gespeichert, um sie später mitzuschicken; eine Zuordnung zu Zahlern nur
      mit Einwilligung (§ 25 TDDDG) oder gar nicht. Rechtlich ungeprüft: vor
      dem Einbau klären
- [ ] Ein KI-Support wäre als KI erkennbar (KI-Verordnung Art. 50)

### E – Videos ohne Gesicht

- [ ] Markenkonto klar als App erkennbar, Impressum-Link im Profil (bei
      TikTok notfalls als Text), das Website-Impressum nennt die Profile
- [ ] TikTok: Schalter „Your brand“, nur Commercial Music Library
- [ ] Keine erfundenen Erfahrungen, keine KI-Personen als „Nutzer“
- [ ] Realistische KI-Bilder gekennzeichnet
- [ ] Jedes Bild selbst fotografiert, aus den Gratisinhalten von Canva oder
      von Unsplash/Pexels (Lizenz geprüft) oder KI-erzeugt; nie aus Pinterest,
      der Google-Bildersuche oder fremden Posts
- [ ] Je Post notieren: Format, Hook, Bildquelle, Aufrufe nach 48 h

### F – Creator (nur nach Signal)

- [ ] Signal erreicht (≥ 300 $ MRR in RevenueCat drei Wochen nach dem Start
      bzw. bei der zweiten Prüfung, spätestens Di 29.06.)
- [ ] Creator ist volljährig, sitzt in Deutschland und stellt eine Rechnung;
      Angebot 60–90 € fest je Video samt Posting
- [ ] Anfrage persönlich und einzeln, mit Link auf kurze
      Datenschutzhinweise für Creator (Art. 14 DSGVO)
- [ ] Vertrag in Textform: Video, Termin, Freigabe, Kennzeichnung „Werbung“
      plus „Paid partnership“, Honorar, Zahlung **nach** dem Posten (über eine
      Plattform mit Treuhandkonto: Freigabe erst nach dem Posten),
      Nutzungsrechte nur für den Post
- [ ] Keine Spark-Ads-Rechte von Creatorn im Ausland, bevor § 50a EStG geklärt
      ist
- [ ] Alle Honorare an selbstständige Kreative im Kalenderjahr zusammenzählen
      (Creator, auch Icon, Logo, Texte). Über 1.000 € fällt
      Künstlersozialabgabe auf die ganze Summe an (2026: 4,9 %, 2027 laut
      Entwurf 5,0 %), dazu die Meldung an die Künstlersozialkasse bis 31.03.
      des Folgejahres (vor dem Schritt prüfen). Ob UGC-Creator darunter fallen,
      klärst du vor der ersten Buchung
      ([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md), Abschnitt 10)
- [ ] Kennzeichnung nach dem Posten selbst geprüft

### G – Kennzahlen je App und Woche

Aufrufe, Downloads, Käufe, Umsatz (USD), Erstattungen, Creator-Kosten,
Umsatz je 1.000 Aufrufe, Antworten auf die Onboarding-Frage „Woher kennst du
die App?“, Monatsgewinn (für die Familienversicherung und für den Ausgang im
Sommer). Vorlage: [`vorlagen/kennzahlen.csv`](vorlagen/kennzahlen.csv).

### H – Abschluss vor dem Umzug

- [ ] Januar: schriftliche Zusage eines Elternteils für eine mögliche
      Übernahme (oder die klare Antwort „nein“)
- [ ] Mo 19.07. (Ende der Jagd): Ferienjob begonnen; gekündigt, was Betrieb
      und Abschluss nicht brauchen
- [ ] Bis Sa 31.07.: Entscheidung je App: einstellen, übergeben oder
      verkaufen (Abschnitt 14)
- [ ] Übergeben oder verkaufen: Übertragung der App spätestens um den 15.08.
      gestartet; Schlüssel in RevenueCat neu gesetzt; Impressum und
      Datenschutzerklärung am Tag der Übertragung umgestellt
- [ ] Einstellen: **So 15.08.** alle Abos aus dem Verkauf genommen (App Store
      Connect → Apps → App → Monetarisierung → Abonnements → Abo-Gruppe →
      Abo → Verfügbarkeit → aus dem Verkauf nehmen → Sichern); Hinweis in App
      und Website; Abonnenten informiert; ab dann keine Posts und keine Werbung
      mehr für diese App; Server und KI laufen bis zum Dienstende weiter
- [ ] **Mi 15.09.** (letzter Tag des Dienstes): in RevenueCat geprüft, dass
      kein Abo mehr aktiv ist (sonst Dienst für diesen Abonnenten weiter und
      den Entwickler-Support fragen)
- [ ] **Do 16.09. oder Fr 17.09.** (nach dem Dienstende am Mi 15.09.,
      mindestens 31 Tage nach dem Verkaufsstopp): App entfernt, Server
      abgeschaltet, Markenkonten geschlossen
- [ ] Werkzeuge gekündigt bzw. zum Laufzeitende beendet: Claude Pro (erst,
      wenn die Summen für die EÜR erstellt sind), Supabase, EAS (falls
      bezahlt), Prepaid-Zweitnummer; in der Anthropic-Konsole automatisches
      Aufladen aus; Domain und E-Mail erst, wenn App, Abos und Markenkonten
      beendet sind
- [ ] Apple-Mitgliedschaft: automatische Verlängerung ist seit dem Kauf
      ausgeschaltet (sonst wieder 99 €); mit dem Ablauf verschwinden die Apps
      aus dem Store
- [ ] Gewerbe abgemeldet (0–32,50 €), falls nichts weiterläuft
- [ ] Belege vollständig für die EÜR 2027; ELSTER-Zertifikat gesichert; ein
      Elternteil ist beim Finanzamt als Empfangsbevollmächtigter benannt
- [ ] Deutsches Konto, Apple-Vertrag und Bankverbindung bleiben, bis die
      letzte Apple-Zahlung da ist (üblich um Do 30.09.2027 und Do 28.10.2027,
      spätestens Di 12.10.2027 bzw. Di 09.11.2027); neue Vertragsfassungen bei
      Apple bis dahin annehmen. Zahlungen, die am Tag der Abmeldung noch offen
      sind, als Einnahme 2027 in die EÜR
      ([`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md), Abschnitt 8);
      mit der Mitteilung über die Aufgabe des Betriebs das Finanzamt fragen,
      wie sie zu erfassen sind
- [ ] Krankenkasse über das Ende des Gewerbes informiert und schriftlich
      geklärt, ob die Familienversicherung (und damit die Europäische
      Krankenversicherungskarte für die Befreiung in Zürich) beim Studium in
      der Schweiz bestehen bleibt
- [ ] Review-Log, Vorlage und Zahlen aufgehoben

---

## 16. Vorlagen für Claude

Kopieren, Teile in eckigen Klammern ersetzen. Claude Code liest zusätzlich
die `CLAUDE.md` des Projekts.

**Lernen (Grundlagen, KW 48 bis Ende Januar)**
```
Ich kann nicht programmieren und lerne gerade [Shell / Git / JavaScript lesen /
Expo]. Erkläre mir [Thema] in kleinen Schritten mit einem Beispiel aus meinem
Projekt. Stell mir danach drei kurze Fragen, ob ich es verstanden habe, und
gib mir eine Übung, die ich selbst mache. Schreib die Lösung erst, wenn ich
darum bitte.
```

**Ideen (Sa 28.11.) und Ideenprüfung (bis Sa 19.12.)** – die Vorlagen stehen in
[`details/04_IDEENWAHL.md`](details/04_IDEENWAHL.md), Abschnitt 10: Kandidaten
sammeln, Tabelle vorfüllen, 60-Sekunden-Test, Entscheidungsblatt und `SPEC.md`.
Claude nennt dabei keine Umsätze und keine Rangliste: Es hat keine
Umsatzdaten, und eine frühe Rangfolge verfälscht die Messung, die du selbst
machst.

**Hooks und Folientexte (Vorbereitung vor der Gründung)** – die Vorlage mit je
30 Hooks für die Formate A, B und C und den Folientexten steht in
[`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md),
Abschnitt 12.1. Keine erfundenen Erfahrungen, keine Versprechen, keine
KI-Personen; Bildmotive ohne Personen.

**Bau-Schritt**
```
Ziel dieser Sitzung: [ein prüfbares Ziel]. Plane zuerst: welche Dateien,
welche Schritte. Warte auf mein OK. Setze dann um und erkläre mir in drei
Sätzen, was du gemacht hast und warum. Sag mir, wie ich es auf iPhone und
iPad prüfe. Behaupte nicht, dass es funktioniert, bevor ich es getestet habe.
```

**Erklären (immer, wenn Geld oder Daten betroffen sind)**
```
Erkläre mir [Paywall / Abo-Prüfung / Server-Funktion / Zugriffsregeln] so,
dass ich es einem Mitschüler erklären kann: was passiert der Reihe nach, wo
liegen die Schlüssel, was kann schiefgehen und wie merke ich das. Ändere
nichts.
```

**Sicherheitsprüfung vor jedem Release**
```
Führe die Mindestprüfung aus docs/checkliste-einreichung.md (Abschnitt
Sicherheit) aus. Zeige mir für jeden Punkt den Befehl, das Ergebnis und die
Stelle im Code. Ändere nichts, bis ich es freigebe.
```

**Antwort an das Review**
```
Apple hat abgelehnt: [Text der Ablehnung]. Erkläre mir den Grund, schlage die
kleinste Änderung vor und entwirf eine kurze, höfliche Antwort. Trage den
Fall in docs/review-log.md ein.
```

**Mail an die ETH-Zulassungsstelle (KW 48)** – an zulassungsstelle@ethz.ch,
selbst abschicken:
```
Betreff: Prüfungsfreie Zulassung Bachelor Informatik HS 2027 – Frage zum
deutschen Abitur (Niedersachsen)

Guten Tag,

ich mache im Sommer 2027 Abitur an einem Gymnasium in Niedersachsen und
möchte mich für den Bachelor Informatik ab Herbstsemester 2027 bewerben.
Meine Prüfungsfächer sind unter anderem Chemie (P2, schriftlich),
Mathematik (P4, schriftlich) und Englisch (P5, mündlich). In den Klassen
11–13 hatte ich außerdem [Fächer eintragen, z. B. Deutsch, Physik,
Biologie, Geschichte, Erdkunde, Politik-Wirtschaft].

1. Zählen für den Notendurchschnitt von 70 % nur die Ergebnisse der
   Abiturprüfungen in Chemie, Mathematik und Englisch?
2. Wird eine zusätzliche mündliche Prüfung in einem schriftlichen Fach
   mitgerechnet?
3. Gelten die Zulassungsbedingungen 2026/27 auch für den Studienbeginn im
   Herbst 2027?
4. Erfüllen meine weiteren Fächer die Bedingung der vier zusätzlichen
   Fächer, und zählt Politik-Wirtschaft als „Wirtschaft“?

Vielen Dank und freundliche Grüße
[Vorname Nachname]
```

**Brief an die Krankenkasse (nach der Gewerbeanmeldung)**
```
Entwirf einen kurzen Brief an die Krankenkasse meiner Eltern: Ich bin
Schüler (13. Klasse), familienversichert und habe seit [Datum] ein Gewerbe für
eine App. Ich arbeite daran in Schulwochen 3–10 Stunden, in Q4 höchstens
7 Stunden, in den Ferien bis zu 38 Stunden und zwischen Schulende (Juli 2027)
und Studienbeginn an der ETH Zürich (20.09.2027) bis zu 50 Stunden je Woche.
Ich habe keine Angestellten und erwarte 2027 einen Gewinn unter 590 € im
Monat; das Gewerbe endet voraussichtlich vor dem Studium. Bitte um schriftliche
Bestätigung, dass die Familienversicherung bleibt, um Hinweis, welche
Nachweise sie brauchen, und darum, ob sie während des Studiums in Zürich
bestehen bleibt.
```

**Creator suchen (nur nach Signal)**
```
Nische: [Nische]. Erstelle eine Liste von 20 volljährigen Creatorn mit Sitz
in Deutschland und 1.000–10.000 Followern, die regelmäßig zu diesem Thema
posten (Profil, typische Aufrufe,
veröffentlichte Geschäftsadresse, falls vorhanden). Schreibe für jeden einen
kurzen, persönlichen Anfrage-Entwurf, der sich auf ein konkretes Video
bezieht, mit dem Link auf unsere Datenschutzhinweise für Creator. Ich
schicke jede Anfrage selbst und einzeln.
```

**Wochenauswertung (sonntags)**
```
Hier sind die Zahlen der Woche: [Tabelle]. Berechne Umsatz je 1.000 Aufrufe,
Download → Zahler, Erstattungen und den Monatsgewinn.
Vergleiche mit Signal (300 $), Tor 1 (5.000 $) und der Grenze der
Familienversicherung (590 €). Was sind die drei Dinge, die nächste Woche am
meisten bringen?
```

---

## 17. Geld: Stufen, Budget, Kassenregeln

**Ausgaben in Stufen** – jede Stufe erst, wenn die vorige erreicht ist
(Monat für Monat in
[`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md)):

| Stufe | wann | was | Kosten |
|---|---|---|---|
| 0 | KW 48 bis zur Gründung | Claude Max (bezahlt), dann Pro; ab KW 50 ein paar Dollar Guthaben für die Claude API; in KW 51 das Apple Developer Program (nur wenn die Idee steht) | ~21 € im Monat, dazu einmal 99 € für Apple |
| 1 | Gründung (im Median am 18.01.) | Gewerbe, Domain-Paket, Prepaid-Nummer; Gründungsberatung der IHK, wenn sie kostenlos ist (vorher fragen; sonst Fragen schriftlich ans Finanzamt) | mit Apple zusammen 140–380 €, typisch ~200 € |
| 2a | von der Gründung bis zum ersten Start | Claude Pro, Domain mit Postfach, Prepaid-Nummer | 23–45 € im Monat, typisch ~28 € |
| 2b | ab dem ersten Start | dazu KI-API nach Nutzung; Supabase und EAS im Gratis-Tarif, bis ein Signal da ist | 23–75 € im Monat, typisch ~30 € |
| 2c | Ruhezeit im Abitur, wenn keine App im Store oder im Review ist | nur Domain und Nummer; Claude Pro ruht | 2–30 € im Monat, typisch ~5 € |
| 3 | nur nach Signal | Creator | für alle Apps zusammen bis 18.07. höchstens 750 € (mit Plattformgebühr), danach nur aus dem Umsatz der letzten vier Wochen |
| 4 | nach dem Ende der Jagd | Server und Domain bis zum Dienstende | 5–35 € im Monat, typisch ~12 € |
| 5 | Abschluss | Abmeldung, nicht abziehbare Umsatzsteuer auf Auslandsrechnungen, EÜR und Einkommensteuererklärung 2027 selbst über ELSTER; Steuerberater nur im Ernstfall | 20–500 €, typisch ~80 € |
| – | nur wenn der Gewinn über ~590 € im Monat liegt | eigene Kranken- und Pflegeversicherung | ~280 € im Monat |

**Was im Modell herauskommt** (Plan mit Hebeln, nur die App, alles bis zum
Schluss eingerechnet):
- Median −558 €, im Mittel −393 €;
- in 9 von 10 Läufen höchstens 791 € Verlust, in 99 von 100 höchstens
  986 €;
- der höchste Betrag, den du im Lauf des Projekts vorstreckst: im Median
  ~577 €, in 9 von 10 Läufen höchstens 1.420 €, nie mehr als 4.090 €;
- mehr als 5.000 € Verlust in keinem Lauf.

Creator-Geld fließt im Modell nur in 6 von 100 Läufen, im Schnitt aller
Läufe ~39 €. Mit Ferienjob und Übergabe steht alles zusammen in
[`details/07_HEBEL.md`](details/07_HEBEL.md), Abschnitt 11.

**Kassenregeln**
- Jeden Sonntag ab der Gründung, nicht in der Ruhezeit und nicht ab einer
  Woche vor einem Prüfungstag (03, Abschnitt 7.3): Kontostand, offene
  Rechnungen, erwartete Zahlungen von Apple (5–9 Wochen nach dem Kauf),
  Monatsgewinn.
- Vor jeder Ausgabe über 50 €: Bleiben Pflichtkosten bis zum Dienstende und
  ~500 € für den Abschluss gedeckt?
- Creator direkt erst nach dem Posten bezahlen; über eine Plattform mit
  Treuhandkonto die Zahlung erst nach dem Posten freigeben. Nie im Voraus für
  Wochen.
- Ein eigenes Konto für die App, damit Belege und Umsatzsteuer sauber bleiben.
  Ein Girokonto auf deinen Namen genügt, wenn die Bank geschäftliche Nutzung
  erlaubt.
- **Belegtabelle ab dem ersten Beleg** (Datum, Betrag, Zweck, PDF). Auf
  Rechnungen aus dem Ausland ohne deutsche Umsatzsteuer rechnest du selbst
  19 % und meldest sie in der Umsatzsteuer-Voranmeldung für den Monat bzw.
  das Quartal der Rechnung (§ 18 Abs. 4a UStG), es sei denn, das Finanzamt hat
  dir schriftlich geantwortet, dass die Jahreserklärung genügt (Checkliste A).
  In jedem Fall stehen sie 2028 in der Umsatzsteuererklärung 2027.

---

## 18. Wenn etwas schiefgeht

| Problem | was du tust |
|---|---|
| Du kommst mit den Grundlagen nicht voran | Lernmodus, kleinere Schritte, ein Thema je Woche; im Zweifel App 1 noch kleiner schneiden |
| App 1 ist am 14.03. nicht fertig | normal (in 2 von 3 Läufen): Ruhezeit im Abitur, nach der letzten Prüfung in zwei bis drei Wochen fertig |
| Am 20.12. besteht keine Idee | No-Go-Regel: nicht gründen, kein Apple-Konto kaufen, weiter lernen; nach der ETH-Bewerbung fünf neue Ideen prüfen, Entscheidung bis Sa 09.01.; besteht auch dann keine, erst nach dem Abitur weiter ([`details/04_IDEENWAHL.md`](details/04_IDEENWAHL.md), Abschnitt 7) |
| Du bekommst keinen Ferienjob | ab Ende Juni zwei Zeitarbeitsfirmen für einen festen Beginn anfragen; im Modell klappt es in 70–85 von 100 Fällen |
| Der Gratis-Server pausiert | im Supabase-Dashboard wiederherstellen; war eine App im Store oder in der Prüfung betroffen, auf Pro wechseln |
| Apple lehnt ab | Grund ins Review-Log, kleinste Änderung, neu einreichen; Ablehnungen bei der ersten App sind normal |
| Videos bekommen kaum Aufrufe | anderes Format, nicht mehr Videos desselben Formats; nach 20 Posts eines Formats ohne einen Post ab 5.000 Aufrufen ein neues Format ([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md), Abschnitt 7.4) |
| Claude läuft im Kreis | Sitzung beenden, erst erklären lassen, dann ein kleineres Ziel |
| Pro-Limit bremst in den Ferien | Arbeit über den Tag verteilen. Stoppt das Limit in den ersten sieben Ferientagen (Mi 23.12.–Di 29.12.) an mindestens zwei Arbeitstagen die Arbeit: genau einen Monat Max, danach zurück auf Pro |
| Kosten der KI-Funktion steigen | Antworten kürzer (Länge über den Prompt steuern), Tagesgrenze je App-User-ID senken, prüfen, ob Aufrufe ohne Abo durchkommen; Monatslimit mit der Zahl der Zahler anheben |
| Datenpanne oder offener Schlüssel | Schlüssel sofort sperren und neu anlegen; prüfen, welche Daten betroffen sein können; Vorfall schriftlich festhalten (Art. 33 Abs. 5 DSGVO). Lässt sich ein Risiko nicht ausschließen: **binnen 72 Stunden** beim Landesbeauftragten für den Datenschutz Niedersachsen (LfD) melden (vorläufige Meldung reicht, die Frist läuft auch am Wochenende); bei hohem Risiko die Betroffenen benachrichtigen (Art. 34) |
| Ein Creator postet ohne Kennzeichnung | sofort korrigieren lassen; du haftest mit |
| Gewinn liegt dauerhaft über ~590 € im Monat | Krankenkasse informieren, eigene Versicherung einplanen (~280 € im Monat) |
| Schule wird schlechter | die ETH-Regel aus Abschnitt 4: sofort nur noch 3 Stunden je Woche, die frei gewordene Zeit in das schwache Fach |
| ETH-Antwort ist negativ oder verlangt die Aufnahmeprüfung | Rückfall-Bewerbung in Hannover sicher abschicken; das Anmeldefenster zur Aufnahmeprüfung (15.09.–15.10.2027) sofort in den Kalender eintragen; mit mir den Plan für die Prüfung im Januar 2028 rechnen |
| Nach der Gewerbeanmeldung kommen „Rechnungen“ oder Formulare für Register- oder Branchenbucheinträge (Formularfallen) | nichts unterschreiben, nichts zahlen. Echt ist nur Post vom Finanzamt, der Gemeinde, der IHK und der Berufsgenossenschaft; im Zweifel bei der IHK nachfragen. Claude prüft das Kleingedruckte, du entscheidest |

---

## 19. Was du aufschreibst

- **Stunden, jeden Tag** – Vorlage [`vorlagen/zeiterfassung.csv`](vorlagen/zeiterfassung.csv):
  Datum, Bereich (Lernen, Code, Videos, Creator, Verwaltung, ETH), App,
  Stunden, Notiz. Das ist auch dein Nachweis der tatsächlichen Stunden für
  die Krankenkasse.
- **Kennzahlen, jede Woche** – Vorlage [`vorlagen/kennzahlen.csv`](vorlagen/kennzahlen.csv).
- **Review-Log** im App-Repository.
- **Entscheidungen an den Messpunkten:** Datum, Zahl, Entscheidung, ein Satz
  Begründung.

Wenn App 1 fertig ist, rechnen wir das Modell mit deinen echten Stunden neu.
Keine Studie misst, wie lange Nicht-Programmierer mit KI wirklich brauchen.
Deine eigene Zahl ist genauer als jede Schätzung hier.

---

## 20. Alle Varianten im Vergleich

Modell `plan/plan_500k.py`, 300.000 Läufe je Variante. „Geld“ ist deine
Vermögensänderung bis zum Schluss, einschließlich Abmeldung, Steuererklärung
und gegebenenfalls eigener Krankenversicherung (vor Einkommensteuer: ohne
Ferienjob fällt bis ~12.300 € Jahresgewinn keine an, mit Ferienjob nur bis
grob 9.000 € App-Gewinn, weil der Lohn mitzählt).

### Stand 24.11.: Plan mit Hebeln

„Nur App“ zählt allein das Ergebnis der Apps. „Alles zusammen“ zählt den Wert
nach dem Sommer (Verkauf oder Übergabe) und den Lohn aus dem Ferienjob dazu.

| Variante | nur App: Gewinn in … von 100 | alles zusammen im Plus in … von 100 | ≥ 10.000 € in … von 100 | Geld im Median | im Mittel | schlechteste 10 % ab | beste 1 % ab | 500.000 € erreicht |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Plan vom 23.11., richtig gerechnet (Verkaufsstopp So 15.08.) | 2,7 | 2,7 | 0,16 | −1.184 € | −1.074 € | −1.545 € | 1.049 € | 0 |
| … nur Kosten gesenkt (mit Ruhezeit im Abitur) | 6,7 | 6,7 | 0,17 | −568 € | −450 € | −788 € | 1.409 € | 0 |
| … nur schneller gebaut und review-fest geplant | 3,8 | 3,8 | 0,25 | −1.164 € | −1.009 € | −1.537 € | 1.839 € | 0 |
| … nur Markt (Deutsch zuerst) und Ideenwahl | 2,7 | 2,7 | 0,16 | −1.186 € | −1.078 € | −1.545 € | 1.009 € | 0 |
| … nur zweite Signalprüfung am 28.06. | 2,7 | 2,7 | 0,17 | −1.185 € | −1.074 € | −1.543 € | 1.071 € | 0 |
| **Plan mit Hebeln** (Kosten, Bau, Markt, Signal) | 8,8 | 8,8 | 0,25 | −558 € | −393 € | −791 € | 2.193 € | 0 |
| Plan mit Hebeln, Verkaufsstopp schon am 31.07. (Dienstende 31.08.) | 3,4 | 3,4 | 0,23 | −600 € | −503 € | −821 € | 1.182 € | 0 |
| Plan mit Hebeln, Verkauf bis 31.08. (Dienst bis 01.10., nur nach Beratung) | 14,4 | 14,4 | 0,30 | −518 € | −261 € | −765 € | 3.392 € | 0 |
| Plan mit Hebeln, ganz ohne Creator-Geld | 10,1 | 10,1 | 0,23 | −548 € | −375 € | −778 € | 2.192 € | 0 |
| Plan mit Hebeln, Bauzeiten wie bisher angesetzt (80/140/280 h) | 7,2 | 7,2 | 0,18 | −567 € | −439 € | −790 € | 1.632 € | 0 |
| Plan mit Hebeln im strengeren Markt 2027 | 7,1 | 7,1 | 0,20 | −566 € | −434 € | −793 € | 1.675 € | 0 |
| + Übergabe oder Verkauf (Elternteil hat zugesagt) | 12,0 | 17,9 | 1,08 | −544 € | 76 € | −782 € | 10.457 € | 0 |
| + Verkaufsversuch und Übergabe ohne feste Zusage | 10,6 | 14,3 | 0,91 | −550 € | −71 € | −786 € | 9.292 € | 0 |
| + Ferienjob ab 19.07. | 8,7 | 79,6 | 0,30 | 3.053 € | 2.467 € | −581 € | 5.419 € | 0 |
| + Ferienjob ab 19.07., ab 05.07. ohne App im Store | 8,3 | 79,5 | 0,30 | 3.142 € | 2.702 € | −583 € | 5.638 € | 0 |
| **+ Übergabe oder Verkauf + Ferienjob (DEIN PLAN, Stand 24.11.)** | 11,1 | 81,8 | 1,79 | 3.191 € | 3.158 € | −567 € | 13.118 € | 0 |
| wie dein Plan, aber ganz ohne Creator-Geld | 12,1 | 81,6 | 1,58 | 3.196 € | 3.109 € | −568 € | 12.221 € | 0 |
| wie dein Plan, aber Job schon ab 05.07., wenn am 04.07. keine App 300 $ MRR zeigt | 8,3 | 80,3 | 1,77 | 4.233 € | 3.652 € | −597 € | 13.039 € | 0 |

So liest du die Tabelle (ausführlich in
[`details/07_HEBEL.md`](details/07_HEBEL.md)):
- **Der Verkaufsstopp** ist die größte Korrektur. Der Plan vom 23.11. hatte
  die Einnahmen bis 31.08. voll gezählt. Mit Apples 31-Tage-Regel lag er bei
  2,7 statt 6,2 von 100 Läufen mit Gewinn.
- **Kosten senken** ist der stärkste Hebel für die App selbst: Der
  Medianverlust halbiert sich, die Gewinnchance steigt von 2,7 auf 6,7.
- **Schneller bauen** bringt nach den vorsichtigen Werten der Gegenprüfung nur
  einen Punkt. Deine echten Stunden am Stunden-Messpunkt (Di 29.12.) sagen
  mehr als jede Schätzung.
- **Markt und Ideenwahl** heben sich auf: Der deutsche Markt ist kleiner, eine
  sorgfältige Ideenwahl gleicht das etwa aus.
- **Jede Woche länger verkaufen zählt:** Verkaufsstopp am 31.07. statt am
  15.08. kostet mehr als die Hälfte der Gewinnläufe. Ein Nachfolger hebt den
  Stopp ganz auf.
- **Der Ferienjob** macht aus dem Sommer in rund 80 von 100 Läufen ein Plus.
  Er kostet die App fast nichts, weil die Jagd am 18.07. ohnehin fast immer
  endet.
- **Creator-Geld** ändert weiterhin fast nichts. Ohne ist ein kleiner Gewinn
  etwas häufiger, mit der Signalregel sind große Ergebnisse etwas häufiger.
- **Geld gegen Chance:** Ein Jobstart schon am 05.07. ohne Signal bringt im
  Median rund 1.000 € mehr und kostet ein Viertel der Gewinnchance der App.
- **Gegenproben:** Mit den alten Bauzeiten oder im strengeren Markt bleibt
  die Chance der App bei rund 7 von 100, der Medianverlust bei rund 570 €.

### Stand 23.11.: Rechtsformen, Tore und Creator-Geld

Diese Tabelle ist mit den alten Kosten und **ohne Verkaufsstopp** gerechnet.
Die Zahlen sind deshalb zu günstig; die Reihenfolge der Varianten gilt
weiter.

| Variante | Gewinn in … von 100 | ≥ 10.000 € in … von 100 | Geld im Median | im Mittel | schlechteste 10 % ab | beste 1 % ab | gegründet | 500.000 € erreicht |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Einzelunternehmen, Creator-Geld nur nach Signal, bis 750 EUR (DEIN PLAN)** | 6,2 | 0,17 | −1.136 € | −952 € | −1.512 € | 2.303 € | 100 % | 0 |
| UG mit gemieteter Geschäftsadresse | 0,000 | 0,000 | −355 € | −378 € | −549 € | −189 € | 0 % | 0 |
| UG mit Anschrift der Eltern | 0,000 | 0,000 | −357 € | −404 € | −553 € | −189 € | 1 % | 0 |
| Einzelunternehmen, ganz ohne Testgeld | 6,5 | 0,16 | −1.128 € | −940 € | −1.506 € | 2.309 € | 100 % | 0 |
| Einzelunternehmen, Tests sofort beim Start (ohne Signalregel) | 6,8 | 0,31 | −1.645 € | −1.310 € | −2.141 € | 4.532 € | 100 % | 0 |
| Einzelunternehmen, Signalregel mit bis zu 1.500 EUR | 6,1 | 0,18 | −1.137 € | −956 € | −1.514 € | 2.244 € | 100 % | 0 |
| Einzelunternehmen, Tore wie bisher (28.02./31.03.) | 1,1 | 0,16 | −963 € | −848 € | −1.254 € | 58 € | 90 % | 0 |
| Einzelunternehmen, ohne Tore | 4,2 | 0,18 | −1.271 € | −1.134 € | −1.728 € | 2.127 € | 100 % | 0 |
| Einzelunternehmen, gründen schon im Dezember | 5,8 | 0,18 | −1.217 € | −1.030 € | −1.609 € | 2.262 € | 100 % | 0 |
| Einzelunternehmen, ohne Startpause im Abitur | 6,7 | 0,27 | −1.122 € | −901 € | −1.505 € | 3.177 € | 100 % | 0 |
| Einzelunternehmen, falls du schneller baust (wie mit Programmierkenntnissen) | 23,3 | 2,2 | −788 € | 136 € | −1.382 € | 19.046 € | 100 % | 0 |
| Einzelunternehmen im strengeren Markt 2027 | 5,3 | 0,15 | −1.147 € | −991 € | −1.518 € | 1.936 € | 100 % | 0 |
| Einzelunternehmen, falls Videos ohne Gesicht schlechter wirken (Trefferquoten -25 %) | 4,6 | 0,12 | −1.156 € | −1.020 € | −1.522 € | 1.667 € | 100 % | 0 |

So liest du diese Tabelle:
- **Creator-Geld:** Ob du es ausgibst, ändert im Erwartungswert wenig.
  - **Gleich gut:** Mit Signalregel, ganz ohne Testgeld und mit bis zu
    1.500 € liegen die Ergebnisse fast gleich: Gewinn in ~6 von 100 Läufen,
    im Mittel ~−950 €.
  - **Tests gleich beim Start** verdoppeln zwar die seltenen Ergebnisse ab
    10.000 € (0,31 statt 0,17 von 100), kosten aber im Median ~500 € mehr.
  - **Warum dann die Signalregel:** Sie gibt fast nichts aus (Creator-Geld
    fließt in ~5 von 100 Läufen) und lässt dir trotzdem die Möglichkeit, eine
    App mit echter Nachfrage zu schieben. Besser als „gar kein Creator-Geld“
    ist sie im Modell aber nicht, nur gleich gut.
  - **Annahme dahinter:** Ohne bezahlte Videos startet auch ein Treffer nur mit
    20–70 % des Umsatzes. Das Signal kann ihn also verpassen.
- **UG:** In keiner Form passt sie zu deinen 5.000 €. In 99 von 100 Läufen
  lassen Pflichtkosten und Auflösung gar keine Gründung zu.
- **Frühe Tore** (28.02.) hätten App 1 meist abgebrochen, bevor sie fertig
  ist: Gewinn nur in ~1 von 100 Läufen.
- **Ganz ohne Tore** ist es schlechter als mit den Sommer-Toren (4,2 statt
  6,2 von 100). Späte Apps und weitere Ausgaben kosten mehr, als sie bringen.
- **Gründen schon im Dezember** ist schlechter als „erst bauen, dann gründen“
  (5,8 statt 6,2 von 100, im Mittel ~80 € mehr Verlust).
- **Schneller bauen** ist der größte Hebel: Mit den Bauzeiten von jemandem,
  der programmieren kann, wäre App 1 schon im Februar draußen, und der Plan
  hätte in 23 von 100 Läufen einen Gewinn, im Mittel sogar ein kleines Plus.
  Deshalb lohnt der Lernpfad, und deshalb soll App 1 so klein wie möglich
  sein.
- **Startpause im Abitur:** Sie kostet etwas (6,7 statt 6,2 von 100 Läufen mit
  Gewinn, ≥ 10.000 € 0,27 statt 0,17 von 100). Dafür musst du im Abitur weder
  Posts machen noch auf Bewertungen reagieren. Abitur und ETH-Zulassung sind
  mehr wert als dieser Unterschied.
- **Gegenproben:** Wirken Videos ohne Gesicht schlechter oder ist der Markt
  2027 strenger, sinkt die Chance auf ~4,5–5,5 von 100, aber die Grenze von
  5.000 € hält.
- **Späte Starts:** In ~84 von 100 Läufen erscheint nach Tor 1 noch eine App,
  die vorher eingereicht war. Auf solchen späten Starts beruhen ~3 von
  10 Gewinnläufen.

---

## 21. Quellen

**Schule und Studium**
- Ferienordnung Niedersachsen 2024/25–2029/30 (RdErl. MK 18.11.2022): <https://www.mk.niedersachsen.de/download/190060/Ferienordnung_2024_25-_2029_30.pdf>
- Abiturtermine 2027 (Bek. MK 28.04.2025): <https://www.mk.niedersachsen.de/download/99040/Abiturtermine_2027.pdf>
- EB-VO-GO (Klausuren in der Qualifikationsphase): <https://www.schure.de/22410/eb-vo-go.htm>
- ETH, Termine und Bewerbung mit ausländischem Reifezeugnis: <https://ethz.ch/de/studium/bachelor/bewerbung/auslaendische-reifezeugnisse/termine.html>
- ETH, Zulassungsbedingungen (PDF): <https://ethz.ch/content/dam/ethz/main/education/admission/bachelor/andere-qual/ETH-ZulassungsbedingungenHS2026_DE.pdf>
- ETH, Studiengebühren und Lebenshaltung: <https://ethz.ch/studierende/de/studium/finanzielles/studiengebuehren.html>, <https://ethz.ch/content/dam/ethz/main/education/finanzielles/files-de/lebenshaltung_international.pdf>
- ETH, Einreise und Krankenversicherung: <https://ethz.ch/content/dam/ethz/main/education/internationales/pdf-en/immigration-to-switzerland-EU.pdf>, <https://ethz.ch/en/studies/international/after-arrival/health-insurance/exemption.html>
- Rückfall: <https://www.uni-hannover.de/de/studium/studienangebot/info/studiengang/detail/informatik>, <https://www.tu-braunschweig.de/bewerbung/>, <https://uol.de/studium/bewerben/bewerbungs-und-einschreibefristen?bachelor>

**Rechtsform, Anonymität, Steuern**
- Apple, Anmeldung und Verkäufername: <https://developer.apple.com/support/enrollment/>
- Apple, EU-Händlerangaben (DSA): <https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-european-union-digital-services-act-trader-requirements>
- § 5 DDG: <https://www.gesetze-im-internet.de/ddg/__5.html>; Impressum-Merkblatt IHK: <https://www.ihk.de/karlsruhe/fachthemen/recht/internetrecht/impressumspflichten-6266634>
- § 14 GewO: <https://www.gesetze-im-internet.de/gewo/__14.html>; § 40 GmbHG: <https://dejure.org/gesetze/GmbHG/40.html>
- UG-Kosten und Auflösung: <https://www.firma.de/firmengruendung/gruendungskosten-ug-was-kostet-die-gruendung-einer-ug-haftungsbeschraenkt>, <https://epago.de/lexikon/steuern/ug-aufloesen-ablauf-kosten>
- IHK Hannover, Wirtschaftssatzung 2026 (Beiträge): <https://www.ihk.de/blueprint/servlet/resource/blob/6929436/2859854a86e1a9c52fa1c9e06a5ddda5/wirtschaftssatzung-2026-data.pdf>; Handelsregister-Gebühren: <https://www.ihk.de/hannover/hauptnavigation/recht/aktuell3/gebuehren-fuer-eintragungen-im-handelsregister-steigen-6569774>
- Familienversicherung und Bezugsgröße 2027: <https://www.vdek.com/vertragspartner/mitgliedschaftsrecht_beitragsrecht/familienversicherung.html>, <https://www.bmas.de/DE/Service/Presse/Pressemitteilungen/2026/bundeskabinett-beschliesst-sozialversicherungsrechengroessen-2027.html>
- § 16 EStG (Betriebsaufgabe beim Wegzug): <https://dejure.org/gesetze/EStG/16.html>; § 10 AO: <https://dejure.org/gesetze/AO/10.html>

**Bauen ohne Programmierkenntnisse**
- METR 2025 und 2026: <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/>, <https://metr.org/blog/2026-02-24-uplift-update/>
- Anthropic, KI-Hilfe und Lernen: <https://www.anthropic.com/research/AI-assistance-coding-skills>
- Anfänger mit KI-Agenten: <https://arxiv.org/abs/2507.22614>; LLM-Schlüssel in iOS-Apps: <https://arxiv.org/abs/2606.12212>
- Claude Code: <https://code.claude.com/docs/en/setup>, <https://code.claude.com/docs/en/output-styles>; Preise: <https://claude.com/pricing>
- Expo: <https://docs.expo.dev/tutorial/build-with-ai/introduction/>, <https://expo.dev/pricing>, <https://docs.expo.dev/submit/ios/>, <https://docs.expo.dev/tutorial/eas/ios-development-build-for-devices/>
- RevenueCat in Expo Go: <https://www.revenuecat.com/docs/getting-started/installation/expo>
- Supabase, Geheimnisse und Sicherheit: <https://supabase.com/docs/guides/functions/secrets>, <https://supabase.com/blog/supabase-security-2025-retro>
- Apple App Review: <https://developer.apple.com/app-store/review/guidelines/>, <https://developer.apple.com/distribute/app-review/>, <https://www.apple.com/legal/app-store/transparency/2025/>
- Missing Semester: <https://missing.csail.mit.edu/2026>; CS50x: <https://cs50.harvard.edu/x/2026/>

**Hebel, Kosten, Abschluss, Ferienjob (Stand 24.11.2026)**
- Apple, Abos aus dem Verkauf nehmen (31-Tage-Regel): <https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription/>; Auszahlungen: <https://developer.apple.com/help/app-store-connect/getting-paid/overview-of-receiving-payments/>; App-Übertragung: <https://developer.apple.com/help/app-store-connect/transfer-an-app/overview-of-app-transfer/>
- Apple, Sätze in den EU-Stores seit 01.10.2026: <https://developer.apple.com/support/apps-in-the-eu/>; Small Business Program: <https://developer.apple.com/app-store/small-business-program/>
- RevenueCat, State of Subscription Apps 2026: <https://www.revenuecat.com/state-of-subscription-apps-2026/>; Adapty, Preise und Paywalls 2026: <https://adapty.io/blog/mobile-app-monetization-2026/>, <https://adapty.io/state-of-paywalls/report/>
- Supabase, Preise und Pausieren im Gratis-Tarif: <https://supabase.com/pricing>, <https://supabase.com/docs/guides/platform/free-project-pausing>
- Umsatzsteuer: § 18 UStG <https://dejure.org/gesetze/UStG/18.html>, § 18a UStG <https://dejure.org/gesetze/UStG/18a.html>
- Kurzfristige Beschäftigung und Familienversicherung: GKV-Spitzenverband, Grundsätzliche Hinweise Gesamteinkommen vom 29.09.2022 (über <https://www.vdek.com/vertragspartner/mitgliedschaftsrecht_beitragsrecht/familienversicherung.html>); TK, Beschäftigung zwischen Abitur und Studium: <https://www.tk.de/firmenkunden/service/fachthemen/versicherung-fachthema/beschaeftigung-zwischen-abitur-und-studium-2151388>
- Mindestlohn 2027: <https://www.bundesregierung.de/breg-de/aktuelles/mindestlohn-steigt-2391010>; Tarif Zeitarbeit: <https://www.dgb.de/service/weiterer-service/tarifmeldungen/tarifmeldung/tarifeinigung-in-der-leiharbeit-mehr-geld-in-3-stufen-bis-2027>
- Reichweite je Post (Buffer, 11,4 Mio. TikTok-Posts) und alle weiteren Quellen der Hebel-Recherche: in den Detailplänen an der jeweiligen Stelle

**Videos ohne Gesicht und Creator**
- Fallbeispiele: <https://www.socialgrowthengineers.com/how-to-go-viral-without-knowing-how-to-go-viral>, <https://shortimize.com/blog/20k-downloads-and-9k-mrr-in-78-days-how-this-indie-app-turned-minimalism-into-millions-of-views>
- TikTok Creator-Anzeigen: <https://ads.tiktok.com/business/en/blog/tiktok-creator-advantage>
- UGC-Preise: <https://www.netinfluencer.com/collabstr-report-tiktok-campaigns-plummet-as-brands-pivot-to-ugc/>, <https://influee.co/ugc-creator/countries/germany>
- TikTok-Regeln: <https://www.tiktok.com/community-guidelines/en/integrity-authenticity/>, <https://www.tiktok.com/legal/page/global/bc-policy/en>, <https://ads.tiktok.com/help/article/commercial-music-library>
- UWG-Anhang: <https://dejure.org/gesetze/UWG/Anhang.html>; KI-Verordnung Art. 50: <https://artificialintelligenceact.eu/article/50/>
