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

**Stand 25.11.2026 (spät).** Die Zahl vom 24.11. (Gewinn aus der App in 9 bis
12 von 100 Läufen) war zu günstig. Am 25.11. haben vier unabhängige Prüfungen
die Stunden und Regeln der Detailpläne ins Modell gebracht und drei Altlasten
aus dem alten 500k-Modell entfernt: zu hohe Kosten vom Umsatz (Werbung, die es
im Plan nicht gibt), einen Umsatz, der ohne Posts einfach weiterwuchs, und
einen zu schnellen Start eines Treffers. Alle Modellzahlen hier sind deshalb
neu (Modell im Stand von Commit 280b3eb; Abschnitt 1 und
[`details/07_HEBEL.md`](details/07_HEBEL.md), Abschnitt 2).

> **Worauf du dich einlässt** (DEIN PLAN, Modell vom 25.11., 300.000 Läufe je
> Variante):
>
> | | |
> |---|---|
> | Zeit bis 31.08. | **~750 Stunden** verfügbar, davon ~180 bis zum 14.03. (10 je Schulwoche, ~31–38 je Ferienwoche, 3–7 in Q4). Ist am 14.03. keine App im Store oder im Review, ruht die App im Abitur. Ab Juni 15–55 je Woche. Endet die Jagd am So 18.07. (in 62,5 von 100 Läufen), sind es bis dahin ~400 Stunden; ~60 davon brauchen Ideenwahl, Verwaltung, Bewerbungen, Gründung und Zürich, ~340 bleiben für Lernen und App. Endet sie schon am Stichtag So 04.07. (in 37,5 von 100), bleiben ~250 |
> | App 1 eingereicht | bis Di 02.02. in 0,6 von 100 Läufen, bis So 14.03. in 14,7, bis So 04.07. in 92,3. Typisch reichst du sie erst nach dem Abitur ein (im Median in der Woche ab Mo 14.06.); das ist kein Scheitern, der Plan rechnet damit. In 7,7 von 100 Läufen nie, weil die Jagd am Stichtag endet. Der Kalender in [01](details/01_TAG_FUER_TAG_BIS_FEBRUAR.md) mit der Einreichung am Di 02.02. ist der **beste Fall**: Er rechnet mit den typischen 113 Baustunden aus 02 und wenig eigener Lernzeit, das Modell vorsichtiger mit 78/130/260 Stunden Bau, 20/28/40 Stunden Lernen und allen Nebenaufgaben |
> | App 1 im App Store | bis So 14.03. in 9,3 von 100 Läufen, bis So 04.07. in 62,5, überhaupt in 92,3; im Median ab der Woche ab Mo 28.06. |
> | Geld nur aus der App (einschließlich Abmeldung und Steuererklärung) | im Median **−567 €**, im Mittel −533 €; in 90 von 100 Läufen höchstens 786 € Verlust, mehr als 1.000 € Verlust in 0,5 von 100, nie mehr als 5.000 € |
> | Gewinn aus der App | in **3,7 von 100** Läufen, also in etwa 4 von 100. Dann meist nur ein paar hundert Euro: Mehr als 409 € bringt die App nur in 1 von 100 Läufen |
> | dein Geld (App, Verkaufspreis, Lohn) mit Ferienjob ab 19.07., ab 05.07. ohne App im Store | im Plus in **78,5 von 100** Läufen, im Median **+4.344 €**, im Mittel +3.518 €. Das Geld kommt aus dem Lohn (Lohn in 77,7 von 100 Läufen); Verlust machst du nur in Läufen ohne Job (21,5 von 100). Nicht dabei ist eine Übergabe an ein Elternteil: Dieses Geld gehört dem Elternteil (mit ihm im Plus in 78,7 von 100 Läufen, Median +4.340 €) |
> | 10.000 € oder mehr | dein Geld in 0,03 von 100 Läufen (rund 3 von 10.000), nur aus der App in 1 von 300.000 Läufen |
> | 500.000 € bis 31.08.2027 | **in keinem** von 300.000 Läufen |
> | zum Vergleich: nur Ferienjob ab 05.07., keine App | im Plus in 77,5 von 100 Läufen, im Median +6.031 €, im Mittel +4.778 €: rein nach Geld im Mittel rund 1.260 € und im Median rund 1.690 € mehr als dein Plan |
>
> Das ist ehrlich gesagt ein **Lernprojekt mit kleiner Gewinnchance**, kein
> Weg zu 500.000 €. Gewinn aus der App gibt es in etwa 4 von 100 Läufen, und
> dann meist nur ein paar hundert Euro. Die Jagd endet praktisch immer
> spätestens am So 18.07. (Weg A; nur 2 von 300.000 Läufen enden anders), in
> 37,5 von 100 Läufen schon am Stichtag So 04.07. Die App kostet dich im
> Median rund 570 € und ~250–340 Stunden. Dein Geld kommt aus dem Ferienjob:
> Rein nach Geld wäre „nur Ferienjob, keine App“ im Mittel rund 1.260 € und im
> Median rund 1.690 € besser. Dafür hast du in 92 von 100 Läufen eine eigene
> App im App Store, echte Programmier- und Marketingerfahrung vor dem
> ETH-Studium, gemessene Zahlen und eine kleine Chance auf mehr. Die Zahl ist
> empfindlich: Mit anderen Annahmen, die niemand messen kann, liegt die
> Gewinnchance der App grob zwischen 1 und 8 von 100 (Abschnitt 20). Drei
> kleine, noch nicht eingearbeitete Abweichungen aus einer fünften Prüfung
> sprechen eher für 3,3 als für 3,7 von 100
> ([`details/07_HEBEL.md`](details/07_HEBEL.md), Abschnitt 15). Die Regeln
> unten sorgen dafür, dass weder das Abitur noch die ETH-Zulassung noch dein
> Geld für Zürich darunter leiden.
>
> **Was die Chance erhöht:** Lässt du das Creator-Geld weg, steigt die
> Gewinnchance der App im Modell von 3,6 auf 4,6 von 100 (gepaarte
> Rangliste), dein Geld bleibt gleich, und du setzt bis zu 750 € weniger ein;
> die Entscheidung liegt bei dir. Nimmst du dazu die Schnittliste aus 02 von
> Anfang an und lernst mehr am eigenen Projekt als mit Tutorials, sind es
> zusammen etwa 6 von 100 Läufen, bei fast gleichem Geld (Abschnitt 1;
> [`details/07_HEBEL.md`](details/07_HEBEL.md), Abschnitt 4.1).

**Die Detailpläne.** Dieses Dokument ist der Überblick mit Regeln,
Messpunkten und Checklisten. Die einzelnen Schritte stehen hier:

| Datei | Inhalt |
|---|---|
| [`details/01_TAG_FUER_TAG_BIS_FEBRUAR.md`](details/01_TAG_FUER_TAG_BIS_FEBRUAR.md) | jeder Tag vom 23.11. bis zur Einreichung von App 1 |
| [`details/02_BAUPLAN_APP1.md`](details/02_BAUPLAN_APP1.md) | App 1 in 23 Arbeitspaketen (AP1–AP22 und AP10a) mit Stunden und „fertig, wenn …“ |
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

**Was sich am 24.11. geändert hat** (Hebel-Recherche mit Gegenprüfung; die
Zahlen in der rechten Spalte sind vom 25.11., Einzelheiten in
[`details/07_HEBEL.md`](details/07_HEBEL.md)):

| Stand 23.11. | jetzt | Folge |
|---|---|---|
| Einnahmen bis 31.08. voll gezählt | Apple verlangt mindestens 31 Tage zwischen „Abo aus dem Verkauf nehmen“ und dem Ende des Dienstes | ohne Nachfolger: Verkaufsstopp So 15.08., Dienstende Mi 15.09. Richtig gerechnet lag der Plan vom 23.11. bei 2,7 statt 6,2 von 100 Läufen mit Gewinn; in DEIN PLAN kostet der Stopp im Mittel 69 € |
| Erstberatung beim Steuerberater, Abschluss für 0–800 € | Gründungsberatung der IHK statt Steuerberater (ob kostenlos, vorher fragen), Kleinunternehmer, Abschluss selbst über ELSTER (20–500 €) | zusammen mit den nächsten drei Zeilen (Hebel „Kosten“, gegen die Ausgangslage): Medianverlust der App −585 € statt −1.174 €, Gewinn aus der App in 2,2 statt 0,6 von 100 Läufen |
| Supabase Pro ab dem Start | Supabase im Gratis-Tarif, bis ein Signal da ist | ~27 € je Monat weniger nach dem Start |
| Claude Pro durchgehend, Max in einzelnen Monaten | Ruhezeit im Abitur (Entscheidung am So 14.03.), Max höchstens einen Monat | ~40–60 € weniger, kein Bau im Abitur; das kostet im Modell etwas Chance (ohne Ruhezeit 4,3 statt 3,6 von 100, Abschnitt 4) |
| nach dem Ende der Jagd laufen die Abos weiter | am selben Tag alles kündigen, was Betrieb und Abschluss nicht brauchen | ~15 € je Monat weniger |
| Apple-Konto bei der Gründung | Apple-Konto schon in KW 51 (Mo 14.–Mi 16.12.), wenn die Idee steht | Durchstich mit echtem Gerät und Testkauf in den Weihnachtsferien |
| Abschluss: einstellen oder verkaufen | dazu: Übergabe an ein Elternteil, das im Januar schriftlich zugesagt hat | im Modell fast keine Wirkung (dein Geld im Mittel +4 €): Übergabe in 2,0 von 100 Läufen, Verkauf in 0,3. Die Übergabe bleibt als Versicherung für den seltenen Treffer und hebt für diese App den Verkaufsstopp auf |
| nach dem 18.07. nur ETH-Vorbereitung und Erholung | Ferienjob ab Mo 19.07., befristet bis Fr 10.09. oder Di 31.08., als kurzfristige Beschäftigung (ab Mo 05.07. über Zeitarbeit, wenn dann keine App im Store ist) | dein Geld im Plus in 78,5 von 100 Läufen, im Median +4.344 €; der Job bringt im Mittel +4.041 € |
| eine Signalprüfung drei Wochen nach dem Start | für eine App, die vor dem Abitur startet, eine zweite: 21 Tage nach dem ersten täglichen Post nach der letzten Prüfung (spätestens Di 29.06.) | ein Treffer wird nicht wegen zu weniger Posts in Q4 abgeschrieben |
| Ideen-Tor mit fünf Kriterien | K.-o.-Fragen, Nachfrageprüfung, Bewertungstabelle, No-Go-Regel | erreicht keine Idee die Mindestwerte, wird nicht gegründet |
| Preise offen | Wochenabo 6,99 € vorausgewählt, Monatsabo 14,99 €, keine Testphase, kein Jahresabo | [`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md) |

**Was sich am 25.11. geändert hat** (vier unabhängige Prüfungen des Modells;
Gründe und Belege in [`details/07_HEBEL.md`](details/07_HEBEL.md),
Abschnitt 2.2). Am 24.11. stand hier eine Gewinnchance der App von 9 bis 12 von
100 Läufen. Sie war zu günstig:
- **Stunden und Regeln der Detailpläne** (Pflicht, kein Hebel): Ideenwahl,
  Verwaltung, Bewerbungen, Gründung, Kassenprüfung, Markenkonten, Vorbereitung
  der Posts, Zürich und die Zeitarbeitsanfrage kosten Stunden, die dem Bau
  fehlen. App 2 beginnt erst nach der Freigabe von App 1, Posts laufen nach dem
  Wochenprogramm (vor dem Abitur 1,5, danach 6,5 Stunden je Woche), und den
  frühen Jobbeginn am 05.07. gibt es nur über Zeitarbeit. Ohne die
  Nebenaufgaben läge PLAN MIT HEBELN bei 6,2 statt 3,7 von 100 (nur zum
  Verständnis).
- **Kosten nach dem Plan:** Das alte 500k-Modell zog von jedem Euro Umsatz
  45–49 % als Werbung ab. Im Plan gibt es keine Werbung aus dem Umsatz; jetzt
  sind es 15–20 % (Umsatzsteuer im Preis, KI-API, Erstattungen). Mit den alten
  Kosten läge DEIN PLAN bei 0,7 statt 3,7 von 100.
- **Umsatz ohne Posts:** Im Abitur und nach dem Ende der Jagd wuchs der Umsatz
  bisher einfach weiter. Jetzt sinkt er in der Prüfungszeit um 5–15 % je
  Woche, nach der Jagd um die Hälfte davon. Sonst läge DEIN PLAN bei 5,9.
- **Start eines Treffers:** 300–3.000 $ MRR in den ersten Wochen statt
  1.000–8.000 $, an 05, Abschnitt 8.4 kalibriert. Sonst läge DEIN PLAN bei 8,3.
- **Kleinere Korrekturen:** Creator-Geld hebt die Spitze einer App nur um
  5–15 %; am Stunden-Messpunkt gilt die Schnittliste; die Familienversicherung
  richtet sich nach dem Jahresgewinn; der alte Verkauf der Firma ist
  abgeschaltet; Übergabe und Verkauf richten sich nach dem Stand am
  Entscheidungstag; die Gegenproben sind gepaart.

So entsteht das Ergebnis Schritt für Schritt (300.000 Läufe je Zeile; „dein
Geld“ ist App, Verkaufspreis und Lohn, ohne das Geld des Elternteils; mehr
Spalten und alle Gegenproben in Abschnitt 20):

| Stufe | nur die App: Gewinn in … von 100 Läufen | dein Geld im Plus in … von 100 | dein Geld im Median | im Mittel |
|---|---:|---:|---:|---:|
| Plan vom 23.11., wie er dastand | 6,2 | 6,2 | −1.136 € | −954 € |
| derselbe Plan mit Verkaufsstopp am 15.08. (Pflicht von Apple) | 2,7 | 2,7 | −1.184 € | −1.074 € |
| dazu alle Stunden und Regeln der Detailpläne (**Ausgangslage**) | 0,6 | 0,6 | −1.174 € | −1.158 € |
| + geprüfte Hebel: Kosten, Bau, Markt, Signal (**PLAN MIT HEBELN**) | 3,7 | 3,7 | −564 € | −528 € |
| + Nachfolger (Elternteil hat zugesagt, sonst Verkaufsversuch) | 3,5 | 3,7 (mit dem Geld des Elternteils 4,3) | −564 € | −524 € |
| + Ferienjob ab 19.07., ab 05.07. ohne App im Store = **DEIN PLAN, Stand 25.11.** | **3,7** | **78,5** | **+4.344 €** | **+3.518 €** |
| zum Vergleich: nur Ferienjob ab 05.07., keine App | – | 77,5 | +6.031 € | +4.778 € |

**Wie du Chance und Geld noch erhöhen kannst** (gepaarte Rangliste gegen DEIN
PLAN, der dort bei 3,6 von 100 liegt;
[`details/07_HEBEL.md`](details/07_HEBEL.md), Abschnitt 4):

| was du tust | Wirkung im Modell |
|---|---|
| Creator-Geld weglassen (deine Entscheidung; behältst du es, gelten die Regeln aus 05, Abschnitt 10) | Gewinn aus der App in 4,6 statt 3,6 von 100 Läufen, dein Geld gleich, bis zu 750 € weniger Einsatz |
| Schnittliste aus 02, Abschnitt 8 von Anfang an | 3,9 statt 3,6 von 100; spart ~7 der 113 Stunden |
| mehr am eigenen Projekt lernen als mit Tutorials (Lernzeit wie in 01) | 4,5 statt 3,6 von 100, nur wenn das Lernen am Projekt reicht |
| **alle drei zusammen** | **6,2 statt 3,6 von 100**, dein Geld fast gleich (im Mittel −18 €) |
| schon im Plan: App 2 im Review ohne Code vorbereiten, Betriebe mit Tariflohn bevorzugen, Job bis Fr 10.09. statt Di 31.08. | ohne die Vorbereitung 3,5 statt 3,6 von 100; Tariflohn +311 € im Mittel, wenn ein solcher Betrieb ab 19.07. zusagt; Job bis 10.09. +767 € im Mittel |

---

## 2. Das Wichtigste in Kürze

1. **Bis Januar kostet es wenig.** Du lernst die Grundlagen und baust
   App 1 mit Claude, zuerst in Expo Go und ab KW 52 als Entwicklungs-Build auf
   deinem iPhone, noch ohne Gewerbe. Ausgaben: Claude Pro (~21 € im Monat),
   ein paar Dollar Guthaben für die Claude API und in KW 51 das Apple-Konto
   (99 €) – das aber nur, wenn deine Idee das Ideen-Tor absehbar besteht.
2. **Gegründet wird erst, wenn App 1 halb steht** (im Modell im Median in der
   Woche ab Mo 01.02., in 57,3 von 100 Läufen erst im Februar oder später, in
   10,2 von 100 erst nach dem Abitur), und zwar als **Einzelunternehmen**.
   Eine UG frisst dein ganzes Geld (Abschnitt 3).
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
   höchstens 750 €. Im Modell fließt es nur in 2,9 von 100 Läufen (im Mittel
   aller Läufe 18 €). Ganz ohne Creator-Geld ist die Gewinnchance der App
   sogar höher (4,6 statt 3,6 von 100, gepaart) und dein Geld gleich; ob du es
   nutzt, entscheidest du (Abschnitt 1).
6. **Am 18.07. entscheidet eine Zahl.** Liegt keine App über 5.000 $ MRR,
   endet die Jagd: keine neue App, kein Creator-Geld, und am Mo 19.07.
   beginnt dein **Ferienjob**. Apps, die dann schon eingereicht sind, dürfen
   noch erscheinen. Im Modell endet die Jagd praktisch immer so (nur 2 von
   300.000 Läufen enden anders), in 37,5 von 100 Läufen schon am Stichtag
   So 04.07., weil dann keine App im Store ist.
7. **Der Abschluss braucht Vorlauf.** Apple verlangt 31 Tage zwischen
   Verkaufsstopp und Dienstende. Ohne Nachfolger nimmst du am So 15.08. alle
   Abos aus dem Verkauf, der Dienst läuft bis Mi 15.09., und am Do 16.09.
   oder Fr 17.09. entfernst du die App und meldest das Gewerbe ab. Mit einem
   Nachfolger entfällt der Stopp für seine App: Ein Elternteil sagt im Januar
   schriftlich zu, eine laufende App zu übernehmen, oder du verkaufst sie
   (Abschnitt 14). Im Modell kommt das selten vor (Übergabe in 2,0 von 100
   Läufen, Verkauf in 0,3); sag das dem Elternteil vorher ehrlich.
8. **Die Kosten sind halbiert.** Kleinunternehmer, Gründungsberatung der IHK
   statt Steuerberater (ob kostenlos, vorher fragen), Abschluss selbst über
   ELSTER, Server im Gratis-Tarif,
   Ruhezeit im Abitur. Die App kostet im Median rund 570 € statt rund
   1.170 € (Abschnitt 17).

**Wie du Chance und Geld noch erhöhen kannst:** Drei Schritte liegen bei dir:
Creator-Geld weglassen, die Schnittliste aus 02 von Anfang an nehmen und mehr
am eigenen Projekt lernen als mit Tutorials. Zusammen heben sie die
Gewinnchance der App im Modell von 3,6 auf 6,2 von 100 Läufen, dein Geld bleibt
fast gleich. Mehr Geld bringen der Job bis Fr 10.09. und ein Betrieb mit
Tariflohn; beides steht schon im Plan (Abschnitt 1;
[`details/07_HEBEL.md`](details/07_HEBEL.md), Abschnitt 4).

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
Mo 14.–Mi 16.12., wenn deine Idee das Ideen-Tor absehbar besteht und IHK
oder Gewerbeamt bestätigt haben, dass Mitgliedschaft und Tests ohne Verkauf
vor der Gewerbeanmeldung unbedenklich sind (gefragt am Fr 04.12.,
[`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md),
Abschnitt 4.1). Die 99 €
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
Abmeldung bzw. Auflösung eingerechnet; die Spalte Einzelunternehmen stammt aus
der Rechnung vom 25.11., die UG-Spalten aus der vom 23.11.)

| | Einzelunternehmen | UG, Anschrift der Eltern | UG, gemietete Geschäftsadresse |
|---|---:|---:|---:|
| Formalkosten bis zum Ende | ~160–880 € (Gewerbe, Apple, Domain, Abmeldung, Steuererklärung selbst über ELSTER) | ~4.000–9.000 € bis zur Löschung (frühestens Ende 2028) | dazu 50–130 € je Monat für die Adresse |
| passt in 5.000 € | ja | **nein:** in 99 von 100 Läufen lassen Pflichtkosten und Auflösung gar keine Gründung zu | **nein:** in fast allen Läufen (99,9 von 100) keine Gründung |
| überhaupt ein Gewinn | 3,7 von 100 (PLAN MIT HEBELN, nur die App) | 0 von 100 | 0 von 100 |
| Geld im Median | −564 € | −357 € (nur Claude, weil meist gar nicht gegründet wird und dann auch keine App erscheint) | −355 € (ebenso) |
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
| Halbjahresferien Mo 01.–Di 02.02. | ~18 in dieser Woche | Mo/Di je ~7 h, ab Mi 03.02. die Q4-Regel |
| Q4, Mi 03.02.–So 14.03. | **höchstens 6–7**, in Wochen mit zwei oder mehr Klausuren nur Sa 3 h | Q4-Noten zählen fürs Abitur; keine neue Kampagne |
| 15.03.–05.04. (letzte Q4-Tage bis Do 18.03., Osterferien) | 0–5, in der Ruhezeit 0 | Abiturvorbereitung |
| schriftliches Abitur 06.04.–13.05. | 0–1, in der Ruhezeit 0 | an Prüfungstagen und ab einer Woche davor gar nichts |
| 5. Prüfungsfach und Nachschreibtermine 19.05.–07.06. | 0–5, in der Ruhezeit 0 | bei einer Präsentationsprüfung zwei Wochen gar nichts; Mo 07.06. kann noch Prüfungstag sein |
| nach deiner letzten Prüfung bis 04.07. | 15–40 | mögliche mündliche Nachprüfung 28.–30.06., Zeugnis 01.–03.07. |
| 05.07. bis zum Ende der Jagd (meist So 18.07.) | Mo–Sa ~9 h, So frei bis auf die Ausnahmen in Abschnitt 10 | davon ~6 h je Woche für Zürich (Zimmer, Unterlagen, Mathe) |
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
  Claude Pro pausiert. Das spart Geld und schützt das Abitur. Im Modell
  kostet die Ruhezeit Chance: Ohne sie läge die Gewinnchance der App bei 4,3
  statt 3,6 von 100 (gepaart), dein Geld aber im Mittel um 81 € niedriger
  (Abschnitt 20). Das Abitur geht vor.
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
| Grundlagen | erklärt im Lernmodus, stellt dir Übungen, lässt dich Stellen selbst schreiben | lernst nach dem Lernpfad ~15–40 Stunden (Abschnitt 7); 01 plant das untere Ende (eigene Lernzeit ~7,5 h und 10 Minuten am Ende jeder Sitzung), mehr Lernen schiebt die Einreichung; fragst nach, bis du es einem Mitschüler erklären kannst |
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
| Apple Developer Program (Einzelperson) | Entwicklungs-Build auf dem eigenen Gerät, TestFlight, App Store | 99 €/Jahr (99 USD oder Betrag in Landeswährung); zahlst du per Kreditkarte, muss es deine eigene sein (sonst Verzögerung und Ausweiskopie), oder du meldest dich in der Apple-Developer-App an; **automatische Verlängerung gleich abschalten**; ohne D-U-N-S, Konto meist nach wenigen Tagen aktiv, nach 24 Stunden ohne Bestätigung bei Apple nachfragen | KW 51 (Mo 14.–Mi 16.12.), wenn die Namensfrage entschieden ist, das Ideen-Tor absehbar bestanden wird (Zwischenstand Sa 12.12.) und IHK oder Gewerbeamt bestätigt haben, dass Mitgliedschaft und Tests ohne Verkauf vor der Gewerbeanmeldung unbedenklich sind (03, Abschnitt 4.1); sonst nach dem Ideen-Tor, frühestens Mo 21.12.; sagen IHK oder Gewerbeamt etwas anderes, wartet Apple bis zur Gründung |
| RevenueCat | Abos, Paywall, Umsatzzahlen, Abo-Prüfung für den Server | frei bis 2.500 $ Monatsumsatz | Sa 19.12. mit AP6 (Mo 14.12., wenn du Apple dann nicht kaufst) |
| Domain, Website, E-Mail | Impressum, Datenschutz, Support | ein monatlich kündbares Paket eines deutschen Anbieters mit Postfach und Webspace, ~2–5 € im Monat | bei der Gründung |
| Zweitnummer (Prepaid) | Telefon für Apples EU-Seite | Prepaid ohne Grundgebühr, ~10 € Startpaket | bei der Gründung |
| Canva oder CapCut (Gratisversion) | Icon und Startbild, Slideshows, Untertitel | 0 € | ab AP16 (Icon und Startbild, in 01 Fr 15.01.) und für die Vorbereitung der Posts ([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md), Abschnitt 4; in 01 Di 02.02.) |

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

**Lernpfad (~15–40 Stunden; 01 plant das untere Ende: eigene Lernzeit ~7,5 h und 10 Minuten je Sitzung; mehr Lernen schiebt die Einreichung)**
1. Expo-Tutorial „Build with AI“ (für Menschen ohne Programmierhintergrund,
   ~1 h, mit Claude Code, iPhone mit Expo Go).
2. Expo-Standard-Tutorial „StickerSmash“ (~2 h).
3. MIT „Missing Semester“ 2026: Shell, Git, Fehlersuche (~6–10 h mit
   Übungen).
4. JavaScript und TypeScript lesen lernen, nicht schreiben (~10–20 h, z. B. die
   ersten Abschnitte von freeCodeCamp).
5. Expo- und EAS-Doku zu Development Builds und `eas submit` (~3–5 h).
6. Fehlermeldungen lesen üben, an deinen eigenen echten Fehlern.

**Was 01 davon plant:** eigene Lernzeit ~7,5 Stunden, bis So 20.12. gut 5½,
ab Mo 30.11. ~3. Das sind Punkt 1 (Di 24.11.) und Punkt 2 (Sa 28.11.), aus
Punkt 3 je eine Übungsstunde zu Shell und Git (Mi 25.11. und Fr 27.11.),
Punkt 6 (Mi 02.12.) und zweimal 1 Stunde Lernen am eigenen Code (Sa 02.01.
und Sa 09.01.). Dazu kommen 10 Minuten Lernen am Ende jeder Sitzung
([`details/02_BAUPLAN_APP1.md`](details/02_BAUPLAN_APP1.md), Abschnitt 3),
bis zur Einreichung mindestens ~12 Stunden. Zusammen sind das ~20 Stunden,
ab Mo 30.11. ~15. Du trägst die 10 Minuten als Lernzeit ein, nicht als
Bauzeit. Die Punkte 4 und 5 und der Rest von Punkt 3 kommen nur dazu, wenn du
mehr lernen willst; jede Stunde mehr schiebt die Einreichung
([`details/01_TAG_FUER_TAG_BIS_FEBRUAR.md`](details/01_TAG_FUER_TAG_BIS_FEBRUAR.md),
Abschnitt 1). Das Modell rechnet vorsichtiger, mit 20/28/40 Lernstunden ab
Mo 30.11. Mit der Lernzeit aus 01 läge die Gewinnchance der App bei 4,5 statt
3,6 von 100 (gepaart), wenn das Lernen am eigenen Projekt reicht
([`details/07_HEBEL.md`](details/07_HEBEL.md), Abschnitt 4.1).

CS50x (10–20 Stunden je Woche) machst du nicht neben der 55-Stunden-Woche,
sondern ab dem Tag, an dem die Jagd endet (im Modell in 62,5 von 100 Läufen
ab Mo 19.07., in 37,5 schon ab Mo 05.07.).
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
- **Vorbereitung** (3–4 Stunden): Hook-Liste, drei Vorlagen in Canva,
  Messtabelle. Das darfst du schon vor der Gründung; 01 legt es auf den
  Di 02.02., nach der Einreichung. Vor der Gründung kein Konto.
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
  Tag bis zum Ende der Jagd, danach höchstens einer am Tag, und nur, wenn du
  willst (05, Abschnitt 6.4).
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
nicht. Ob du dieses Geld überhaupt nutzt, entscheidest du vor der ersten
Buchung: Im Modell ist die Gewinnchance der App ganz ohne Creator-Geld höher
(Abschnitt 1).
- **Fällt die Signal-Prüfung in die Startpause**, siehst du am Tag nach deiner
  letzten Prüfung nach: Liegt die App dann über 300 $ MRR, zählt das, und du
  buchst. Sonst gilt die zweite Prüfung, 21 Tage nach dem ersten täglichen Post
  (spätestens Di 29.06.; mit mündlicher Nachprüfung am Tag nach der letzten
  Nachprüfung, Abschnitt 13).
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
| Sa | 5 h, z. B. 10–13 und 14–16 Uhr | 3 h Bau-Sitzung, 2 h Lernen oder Bau (Slideshows erst ab der Einreichung, 05, Abschnitt 6.2) |
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
13–17 und 18–20 Uhr, So frei bis auf die Ausnahmen oben; davon ~6 Stunden
für Zürich.

**Woche mit Ferienjob (ab 19.07., oder ab 05.07. ohne App im Store):**
40 Stunden Arbeit; für die Apps an zwei Werktagen je 20 Minuten Zahlen und
Support, samstags bis zu 3 Stunden; ~6 Stunden für Zürich. Posts höchstens
einer am Tag aus dem Vorrat vom Samstag, und nur, wenn du willst
([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md),
Abschnitt 6.4). Ohne Posts kommen kaum neue Zahler, und der Umsatz fällt
(06, Abschnitt 4.7). Im August kommen einmalig die Schritte für Übergabe,
Verkauf oder Stilllegung dazu
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
- Das Projekt-Postfach für alle Konten ist eingerichtet.

| Tag | Zeit | was | Ergebnis |
|---|---|---|---|
| Mo 23.11. | 1 h | 10 min: deine Prüfungsfächer gegen die ETH-Bedingung prüfen (Abschnitt 9) – **erledigt:** Chemie P2, Mathe P4, Englisch P5 erfüllen sie. 40 min: Git for Windows und Node.js (LTS) installieren, dann in PowerShell Claude Code (`irm https://claude.ai/install.ps1 \| iex`); mit `claude` anmelden; `/output-style learning` einschalten und Claude bitten, den Lernmodus in deinen Benutzereinstellungen einzutragen (Abschnitt 7). 5 min: Expo Go auf iPhone und iPad laden. 5 min: auf claude.ai unter Abrechnung nachsehen, wann Max endet, und danach auf Pro umstellen statt Max zu verlängern. | Prüfungsfächer geklärt, Claude Code läuft |
| Di 24.11. | 1 h | 5 min: dieses Repository auf GitHub auf privat stellen (Settings → General → Danger Zone → Change repository visibility → Private). 10 min: Mail an die ETH-Zulassungsstelle (Vorlage in Abschnitt 16), vorher aufschreiben, welche Fächer du in den Klassen 11–13 hattest. 45 min: Expo-Tutorial „Build with AI“ mit Claude Code. | Repository privat, Mail raus, erste App in Expo Go |
| Mi 25.11. | 1 h | Missing Semester: Shell (Teil 1). | Terminal-Grundlagen |
| Do 26.11. | 1 h | Gespräch mit deinen Eltern: Abschnitt 3 zeigen. Wer soll im App Store stehen, du oder ein Elternteil? Darf ihre Anschrift ins Impressum? Würde ein Elternteil im Sommer eine laufende App übernehmen (Abschnitt 14)? Noch nichts entscheiden, nur verstehen; die Namensfrage entscheidet ihr bis So 13.12. **Karte:** Hast du keine eigene Visa- oder Mastercard (Debit reicht, sie muss in US-Dollar zahlen können), beantragst du sie diese Woche bei deiner Bank zum Girokonto; sie kommt oft erst nach 1–2 Wochen. Du brauchst sie ab KW 50 für das Guthaben der Claude API und in KW 51 für Apple (oder du meldest dich bei Apple über die Developer-App an). Für die ETH-Gebühr im Dezember geht notfalls die Karte deiner Eltern. | Fragen geklärt, Karte beantragt, Namensfrage bis 13.12., Zusage zur Übernahme im Januar |
| Fr 27.11. | 1 h | Missing Semester: Shell (Teil 2) und Git (Teil 1). | Terminal- und Git-Grundlagen |
| Sa 28.11. | 5 h | 2 h: Expo-Tutorial „StickerSmash“ mit Erklärungen von Claude. 2 h 15 min: Ideen nach [`details/04_IDEENWAHL.md`](details/04_IDEENWAHL.md): etwa 20 Kandidaten sammeln (12 von Claude, deine eigenen, der Pool aus 04), K.-o.-Fragen und 60-Sekunden-Test für höchstens sechs; 5 gehen in die Prüfung. Bestehen weniger als fünf den Test, folgt am Mo 30.11. ein Nachtest mit weiteren Kandidaten (30 min). 30 min: Projekt-Postfach bei einem E-Mail-Anbieter (neutraler Name, nicht dein eigener) mit Zwei-Faktor-Anmeldung und einen Passwortmanager einrichten, Wiederherstellungscodes ausdrucken ([`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md), Abschnitt 3). 15 min: Beginn AP1: privates Repository `vorlage` auf GitHub, `CLAUDE.md` aus [`vorlagen/CLAUDE_md_fuer_die_app.md`](vorlagen/CLAUDE_md_fuer_die_app.md), [`vorlagen/checkliste_einreichung.md`](vorlagen/checkliste_einreichung.md) als `docs/checkliste-einreichung.md` kopieren, leere `docs/review-log.md` und `docs/entscheidungen.md` anlegen; solange Max noch läuft, legt Claude damit das leere Vorlagen-Projekt an. | 5 Ideen für die Prüfung markiert, jede mit dem Punkt, in dem sie den kostenlosen Weg schlägt (sonst Nachtest Mo 30.11.); im Projekt-Postfach kommt eine Test-Mail an; Vorlage im Repository |
| So 29.11. | frei | – | – |

---

## 12. Woche für Woche bis zum Abschluss

Bis zur Einreichung von App 1 steht jeder Tag in
[`details/01_TAG_FUER_TAG_BIS_FEBRUAR.md`](details/01_TAG_FUER_TAG_BIS_FEBRUAR.md),
jedes Arbeitspaket (AP1–AP22 und AP10a) in
[`details/02_BAUPLAN_APP1.md`](details/02_BAUPLAN_APP1.md). Hier steht der
Überblick. Rutscht etwas, überspringst du nichts, sondern schiebst.

### Phase 1 – Grundlagen, Projekt und Idee (KW 49–51, 30.11.–20.12.), Schulwochen, 10 h (mit Klausuren 3 h)

- **Lernen (in 01 ~1 h in diesen drei Wochen):** Fehlermeldungen lesen am
  Mi 02.12., dazu 10 Minuten am Ende jeder Sitzung. Die Stunde „Lernen am
  eigenen Code“ vom Sa 12.12. rutscht für die Ideen auf den Sa 09.01. Mehr
  Lernen (Lernpfad, Abschnitt 7) schiebt die Einreichung.
- **Bauen (~5–7 h je Woche):** Projekt mit dem Expo-Gerüst, zwei Sprachdateien
  und fünf leere Bildschirme (AP1–AP2), Supabase-Funktion mit echter
  KI-Antwort (AP4–AP5), `SPEC.md` (AP3) und das RevenueCat-Konto mit allen
  nativen Paketen (AP6), beides am Sa 19.12., noch ohne Paywall.
- **Ideenwahl (~10–16 h, typisch 12 h, von Sa 28.11. bis Sa 19.12.):** fünf Ideen mit
  K.-o.-Fragen, Nachfrageprüfung und Bewertungstabelle, dazu Slideshow-Test,
  Namensprüfung und ein Ablauf-Test in Expo Go mit fünf Erwachsenen
  ([`details/04_IDEENWAHL.md`](details/04_IDEENWAHL.md)); für den Ablauf-Test
  kommen in KW 51 fünfmal 10 Minuten dazu, zusammen 10 h 50 min (01,
  Abschnitt 5; erlaubt sind höchstens 15). Eigene Markenkonten gibt es erst
  ab der Gründung, wegen des Impressums.
- **Namensfrage bis So 13.12.:** du oder ein Elternteil (Abschnitt 3).
- **Apple Developer Program Mo 14.–Mi 16.12.** (99 €), wenn die Namensfrage
  entschieden ist, das Ideen-Tor absehbar bestanden wird (am Sa 12.12.
  erfüllt mindestens eine Idee alle Mindestwerte) und IHK oder Gewerbeamt
  bestätigt haben, dass Mitgliedschaft und Tests ohne Verkauf vor der
  Gewerbeanmeldung unbedenklich sind (03, Abschnitt 4.1). Fehlt eine dieser
  Bedingungen, kaufst du erst nach dem Ideen-Tor, frühestens Mo 21.12., und
  legst am Mo 14.12. das RevenueCat-Konto an (AP6); sagen IHK oder Gewerbeamt
  etwas anderes, wartet Apple bis zur Gründung. Automatische Verlängerung
  gleich abschalten. Kommt nach 24 Stunden keine Bestätigung, wendest du dich
  an Apple.
- **Verwaltung vorbereiten (~1 h, in 01 Fr 04.12.):** ELSTER-Benutzerkonto
  anlegen (mit dem Online-Ausweis sofort, sonst kommt ein Brief, der bis zu
  zwei Wochen braucht); PIN des Personalausweises prüfen; nachsehen, wie deine
  Gemeinde die Gewerbeanmeldung online annimmt; bei der IHK oder dem
  Gewerbeamt fragen, ob Mitgliedschaft bei Apple und Tests ohne Verkauf vor
  der Gewerbeanmeldung unbedenklich sind (Antwort bis So 13.12.); Termin der
  kostenlosen Gründungsberatung anfragen.
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
- **Durchstich (AP7–AP8, dazu der Rest von AP6):** Paywall aus dem Dashboard
  mit vier Links (Mi 23.12.), Entwicklungs-Build auf iPhone und iPad, Testkauf
  im RevenueCat Test Store, die Server-Funktion prüft das Abo und liefert die
  KI-Antwort. Alles mit hässlicher Platzhalter-Oberfläche: erst das Riskante,
  dann das Schöne.

### KW 53 (28.12.–03.01.), Weihnachtsferien, ~31 h (Neujahr frei)

- **ETH-Bewerbung (6 h, Mo 28.12.):** Lebenslauf mit Claude nach der
  ETH-Vorlage, Zeugnisse der letzten drei Schuljahre scannen, Passfoto,
  Einverständniserklärung, Gebühr 150 CHF per Kreditkarte (privat, nicht aus
  dem App-Geld). **Abschicken.**
- **Store-Build und TestFlight (AP9, Mo 28.12. und Di 29.12.),** dann am
  **Di 29.12. der Stunden-Messpunkt** (Abschnitt 13): Wie viele Baustunden
  haben AP1–AP9 gebraucht (geplant ~32)? Bis ~40 weiter wie geplant; jede
  Stunde über 32 schiebt die Einreichung, ab etwa 38 liegt sie in Q4, mit den
  10 Minuten Lernen je Sitzung auch darunter. Über ~40 gilt die Schnittliste:
  bei 40–60 liegt die Einreichung eher in Q4, über 60 planst du sie erst nach
  dem Abitur ein.
- **App 1:** Kernfunktion mit Prompt und 20 Testfällen (AP10, Di 29.12. bis
  Do 31.12.), dann der Beginn des Onboardings (AP11, Do 31.12.).
- **Ferienjob:** drei Bewerbungen für Mo 19.07.–Fr 10.09., zuerst bei
  Betrieben mit Tariflohn; passt einem Betrieb nur ein Ende am Di 31.08.,
  nimmst du das (Sa 02.01., 1–2 h,
  [`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md),
  Abschnitte 2.2 und 2.3).

### KW 01 (04.–10.01.), Ferien, ~38 h (der 06.01. ist in Niedersachsen kein Feiertag)

- **App 1:** Rest des Onboardings (AP11), Paywall-Feinschliff (AP12; harte
  Paywall ohne Umschalter, Wochen- und Monatsabo, vier Links:
  Nutzungsbedingungen, Datenschutz, Impressum, „Käufe wiederherstellen“),
  Einwilligung, „Antwort melden“ und Fehlerfälle (AP13), Verlauf, Kopieren
  und Teilen (AP10a; die Favoriten kommen erst am Sa 23.01.), Einstellungen
  und Rechtstexte (AP14).
- **Messpunkt M2 – gründen, sobald App 1 etwa halb steht** (Kernfunktion
  läuft mit echter KI, Onboarding und Paywall stehen: AP10, AP11 und AP12;
  AP10a ist dafür nicht nötig). Dann Checkliste A in zwei Teilen (~4 h):
  Gewerbe, Fragebogen in ELSTER, Domain-Paket, Prepaid-Nummer; am nächsten
  Tag bei Apple der Vertrag für bezahlte Apps,
  Bank- und Steuerdaten, Händlerangaben und das Small Business Program
  ([`details/03_GRUENDUNG_UND_KONTEN.md`](details/03_GRUENDUNG_UND_KONTEN.md)).
  - **Wann das meist ist:** Im Kalender (01), dem besten Fall, gründest du am
    Do 07.01. Im Modell wird im Median in der Woche ab Mo 01.02. gegründet, in
    57,3 von 100 Läufen erst im Februar oder später, in 10,2 von 100 erst nach
    dem Abitur (später Fall).
  - **Später Fall:** Ist M2 bis Mo 01.03. nicht erreicht, gründest du am Tag
    nach deiner letzten Prüfung, parallel zum Rest-Bau.
- **Website (AP18):** Entwürfe ohne Gewerbe am Mi 06.01., online nach der
  Gründung (in 01 Do 07.01.).
- **Messpunkt M1 (Sa 09.01.):** ETH-Bewerbung abgeschickt, AP10–AP17 und
  AP10a fertig? Im Kalender (01, bester Fall) fehlen dann noch AP15–AP17 und
  die Favoriten; sie folgen bis Sa 23.01.

### KW 02–04 (11.–31.01.), Schulwochen, 10 h (Q3-Ende, mit Klausuren 3 h)

- **Gründung**, falls noch nicht geschehen.
- **Brief an die Krankenkasse**, sobald das Gewerbe angemeldet ist (in 01 am
  Fr 08.01.; Vorlage in Abschnitt 16): Schüler mit Gewerbe; deine echten
  Stunden (Schulwochen 3–10, Q4 höchstens 7, Ferien bis 38, nach der Schule
  bis ~50 je Woche); erwarteter Gewinn unter 590 € im Monat, keine
  Angestellten; Bitte um schriftliche Bestätigung.
- **Zusage des Elternteils** für eine mögliche Übergabe im Sommer, eine
  Seite schriftlich (Abschnitt 14). **Oberstufenkoordination fragen,** wann
  die mündlichen Prüfungen liegen.
- **App 1 fertig bauen:** Tageslimit und Kostenbremse (AP15), Aussehen mit
  Icon, Startbild und Name (AP16), iPad und Gerätetests (AP17), zuletzt die
  Favoriten (Rest von AP10a, Sa 23.01.).
- **Funktions-Stopp So 24.01.:** danach nur noch Fehler, Texte, Einreichung;
  was fehlt, z. B. die Favoriten, kommt in Version 1.1.
- **Store-Eintrag (AP19, Sa 23.01. bis Sa 30.01.):** Abo-Gruppe mit beiden
  Abos, Preise, Datenschutzangaben, Store-Seite in de-DE, en-US und en-GB,
  zum Schluss ein Sandbox-Kauf im Store-Build.
- **TestFlight mit der Familie (AP21):** Store-Build am Mo 25.01., die drei
  Tester am Sa 30.01., Fehler beheben.
- **Betriebsprojekt einrichten (Beginn von AP20, Sa 30.01.);** der Rest von
  AP20 mit der Sicherheits-Mindestprüfung folgt am Mo 01.02.
- **Fr 29.01. Halbjahreszeugnis:** Lade es in eApply nach, falls die ETH es
  verlangt.

### KW 05 (01.–07.02.), Halbjahresferien Mo/Di, ~18 h

- Mo/Di je ~7 h, ab Mi 03.02. gilt die Q4-Regel (Sa 3 h, höchstens zweimal
  1–2 h); 01 plant Mi–Fr zusammen höchstens 1 h, dazu So 10 min
  Kassenprüfung.
- **Mo 01.02.: Rest von AP20:** Betriebsprojekt fertig einrichten, neuer
  Store-Build damit, Sicherheits-Mindestprüfung mit allen acht Punkten
  (Abschnitt 7).
- **Einreichen bis Di 02.02. (AP22),** sobald Checkliste C steht, mit „Diese
  Version manuell veröffentlichen“ (Abschnitt 4). Abo-Gruppe und Abos
  zusammen mit dieser Version einreichen.
- **Markenkonten** in der Woche der Einreichung anlegen, mit Link
  „Impressum“ ([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md));
  in 01 am Di 02.02., danach die Vorbereitung der Posts.

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
  nach der letzten Prüfung (spätestens Di 29.06.; mit mündlicher Nachprüfung
  am Tag nach der letzten Nachprüfung, Abschnitt 13).
- **App 2 ohne Code vorbereiten:** Solange App 1 im Review ist, darfst du in
  den Q4-Stunden damit beginnen, höchstens ~6 Stunden für alles (was dazu
  gehört, steht in KW 23–26). Eine Antwort an das Review geht vor.
- **Gründung**, falls M2 bis Mo 01.03. erreicht ist (Checkliste A; in Q4 auf
  zwei Samstage verteilt). Danach erst wieder nach der letzten Prüfung.
- **Ist App 1 noch nicht eingereicht:** im Rahmen der Q4-Stunden weiterbauen,
  ohne Druck. Im Modell ist sie bis So 14.03. nur in 14,7 von 100 Läufen
  eingereicht und in 9,3 im Store; typisch reichst du sie erst nach dem
  Abitur ein (im Median in der Woche ab Mo 14.06.). Das ist kein Fehler, der
  Plan rechnet damit.
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
  weiter. **Mit mündlicher Nachprüfung** (Mo 28.06.–Mi 30.06.) machst du ab
  einer Woche davor gar nichts an der App, auch keine Posts (06,
  Abschnitt 1.2, KW 25). Eine Signalprüfung, die auf ihren Tag oder in die
  Woche davor fällt, liest du erst am Tag nach deiner letzten Nachprüfung ab,
  spätestens am Do 01.07.
  ([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md),
  Abschnitt 9.2).
- **App 2** (die zweitbeste Idee, die Reserve vom Ideen-Tor): Solange App 1
  im Review ist, darfst du App 2 ohne Code vorbereiten, höchstens ~6 Stunden:
  `SPEC.md` nach [`details/04_IDEENWAHL.md`](details/04_IDEENWAHL.md),
  Abschnitt 10.5, die Fragenliste für den geführten Ablauf, die Store-Texte
  und ein Icon-Entwurf in Canva. Eine Antwort an das Review geht vor, und in
  der Prüfungszeit bereitest du nichts vor. Den Code beginnst du erst nach
  der Freigabe von App 1, aus der Vorlage
  ([`details/02_BAUPLAN_APP1.md`](details/02_BAUPLAN_APP1.md), Abschnitt 9).
  Nach der Freigabe arbeitest du zuerst das Review-Log von App 1 in die
  `CLAUDE.md` und in die `SPEC.md` von App 2 ein. App 2 bekommt eine andere
  Kernfunktion; reine Varianten lehnt Apple ab. Im Modell startet eine
  zweite App in 61,9 von 100 Läufen, im Median in der Woche ab Mo 19.07., also
  meist erst nach Tor 1; bis Tor 1 ist sie nur in 20,6 von 100 Läufen im
  Store.
- **Zürich, aus den 15–40 h:** Zimmer suchen ab KW 24 (~2 h),
  Finanzierungsbrief der Eltern in KW 25 (~1 h, 1.750 CHF im Monat; beides
  Schätzungen, [`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md),
  Abschnitt 1.2).
- **Mo 21.06., in jedem Fall: Zeitarbeit anfragen (1 h).** Ein Vertrag aus
  dem Winter beginnt am 19.07. (06, Abschnitt 2.4); die zwei Wochen ab
  Mo 05.07. gibt es nur über eine Zeitarbeitsfirma. Du fragst deshalb zwei
  Zeitarbeitsfirmen für einen festen Termin an: ohne unterschriebenen Vertrag
  für den ganzen Sommer, mit Vertrag ab 19.07. für Mo 05.07.–Fr 16.07. Fertig,
  wenn zwei Anfragen raus sind und ein Gesprächstermin steht.
- **Fr 25.06.: Vorentscheidung zum Jobbeginn** (06, Abschnitte 2.2 und 2.10):
  Ist eine App im Store oder im Review, gilt Mo 19.07., sonst Mo 05.07. Ohne
  Vertrag nennst du der Zeitarbeitsfirma dieses Datum als Beginn; mit Vertrag
  ab 19.07. sagst du ihr für Mo 05.07.–Fr 16.07. zu (bei Mo 05.07.) oder ab
  (bei Mo 19.07.). Fertig, wenn die Zeitarbeitsfirma das Datum oder deine
  Absage hat.
- **Zeigt eine App Ende Juni nennenswerten Umsatz** (Richtwert ~100 $ MRR;
  genauer Auslöser in [`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md),
  Abschnitt 4.4): Das Elternteil, das zugesagt hat, schickt bis Fr 02.07.
  Gewerbe- und Apple-Anmeldung ab; Vertrag, Bank, Steuer, Händlerangaben und
  Small Business Program folgen, sobald das Konto frei ist (Abschnitt 14).
- **Bis 15.07.:** Bewerbung an der Leibniz Universität Hannover (~2 h).
- **01.–03.07.:** Abiturzeugnis in eApply hochladen, Original an die ETH.
- **Stichtag So 04.07.:** Ist noch keine App im Store, beginnt der Ferienjob
  am Mo 05.07., und du beginnst keine neue App mehr. Eine eingereichte App
  darf noch erscheinen. Im Modell trifft das in 37,5 von 100 Läufen zu; in
  17,0 von 100 beginnt der Job dann am Mo 05.07., in 20,5 nicht. Galt am
  Fr 25.06. der 19.07., fragst du am Mo 05.07. die Zeitarbeitsfirmen vom
  Mo 21.06., ob du sofort beginnen kannst. Das ist unsicher (im Modell kommt
  dieser Fall in 19,4 von 100 Läufen vor, und in 12,0 von 100 klappt der
  frühe Beginn dann nicht); plane den Lohn dieser zwei Wochen nicht fest ein
  (06, Abschnitt 2.10). Hast du den 05.07. zugesagt und ist doch eine App im
  Store, hältst du die Zusage ein und betreust die App abends.

### KW 27–28 (05.–18.07.), Sommer, ~55 h (davon ~6 h für Zürich)

- Posts, Auswertung, App 2 fertig, eingereicht und gestartet. Apps, die nach
  dem 04.07. erscheinen, bieten nur das Wochenabo an. Bleibt Zeit, beginnt
  App 3; sie muss bis 18.07. eingereicht sein.
- Zimmer in Zürich weiter suchen (WOKO braucht die Zulassung).
- **Tor 1 (So 18.07.):** Abschnitt 13.

### KW 29–37 (19.07.–15.09.), Ferienjob und Abschluss

- **Weg A, B oder C** (Abschnitt 14). Im Modell ist es in 100,0 von 100
  Läufen Weg A (nur 2 von 300.000 Läufen enden anders):
  - **Mo 19.07.:** Ferienjob beginnt. Am selben Tag kündigst du alles, was
    Betrieb und Abschluss nicht brauchen.
  - Apps, die am 18.07. schon eingereicht waren, erscheinen noch, ohne
    Creator-Geld (im Modell startet allein die zweite App in 41,3 von 100
    Läufen erst nach Tor 1; drei oder mehr Apps gibt es in 28,5 von 100).
    Für die Apps bleiben 2–5 Stunden je Woche: an zwei Werktagen je
    20 Minuten Zahlen und Support, samstags bis 3 Stunden. Posts
    höchstens einer am Tag, und nur, wenn du willst
    ([`details/05_START_UND_MARKETING.md`](details/05_START_UND_MARKETING.md),
    Abschnitt 6.4).
  - **Bis Sa 31.07.:** je App entscheiden: einstellen, übergeben oder
    verkaufen (für eine App, die erst nach Mo 19.07. erscheint, bis
    Sa 07.08.), und den Umzugstag festlegen (bei einem Umzug vor Sa 18.09.
    schon bis Mo 19.07.; dann rücken die Tage unten vor, Abschnitt 14).
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
| **Namensfrage** So 13.12. | Steht fest, wer im App Store steht? | Apple-Anmeldung Mo 14.–Mi 16.12., wenn auch der Zwischenstand passt und IHK oder Gewerbeamt zugestimmt haben (03, Abschnitt 4.1) | Apple-Anmeldung und Durchstich rutschen |
| **Zwischenstand Ideen** Sa 12.12. | Erfüllt mindestens eine Idee alle Mindestwerte? | Apple-Anmeldung Mo 14.–Mi 16.12., wenn die Namensfrage entschieden ist und IHK oder Gewerbeamt zugestimmt haben | Apple erst nach dem Ideen-Tor, frühestens Mo 21.12.; am Mo 14.12. das RevenueCat-Konto (AP6) |
| **M0 / Ideen-Tor** Sa 19.12. / So 20.12. | Besteht eine Idee (Mindestwerte, Slideshow-Test, Ablauf-Test)? `SPEC.md` und echte KI-Antwort in der App? | weiter; fehlt `SPEC.md` oder die KI-Antwort, holst du sie am Mi 23.12. zuerst nach | **No-Go** (keine Idee besteht): nicht gründen, kein Apple-Konto; weiter lernen; fünf neue Ideen nach der ETH-Bewerbung, Entscheidung bis Sa 09.01. |
| **Stunden-Messpunkt** Di 29.12. | Wie viele Stunden haben AP1–AP9 gebraucht (geplant ~32; nur Baustunden, die 10 Minuten Lernen je Sitzung zählen als Lernzeit)? | bis ~40: weiter wie geplant. Jede Stunde über 32 schiebt die Einreichung; ab etwa 38 liegt sie in Q4, mit den 10 Minuten Lernen je Sitzung auch darunter (01, Abschnitt 1). Ob du die Schnittliste trotzdem nimmst, entscheidest du; im Modell hebt sie die Gewinnchance der App von 3,6 auf 3,9 von 100 (Abschnitt 1) | über ~40 gilt die **Schnittliste**, bei 40–60 und ebenso über 60: Onboarding mit 3 Fragen, kein eigenes Design, keine Bewertungsabfrage, Favoriten erst in Version 1.1. Das spart ~7 der 113 Stunden; nach dem Start kommen ~3 Stunden für Version 1.1 dazu. Bei 40–60 liegt die Einreichung eher in Q4; über 60 planst du sie erst nach dem Abitur ein. Mehr lässt sich nicht kürzen, ohne Verlauf, Kopieren oder Teilen (Richtlinie 4.2), die zweite Sprache oder den iPad-Test anzufassen. Nie gekürzt werden geführter Ablauf, Meldeknopf, Einwilligung, die Pflichtteile der Paywall und die Mindestprüfung (02, Abschnitt 8) |
| **M1** Sa 09.01. | ETH-Bewerbung abgeschickt? AP10–AP17 und AP10a fertig? | weiter | ETH-Bewerbung hat Vorrang, fehlende Pakete in KW 02–04. Im Kalender (01, bester Fall) fehlen am Sa 09.01. noch AP15–AP17 und die Favoriten; sie folgen bis Sa 23.01. |
| **M2** App 1 halb fertig (Kriterien in KW 01; im Modell im Median in der Woche ab Mo 01.02.) | Rechtsform entschieden? | gründen (Checkliste A) | ohne Gründung kein Start: weiterbauen. Ist M2 bis Mo 01.03. nicht erreicht, gründest du am Tag nach deiner letzten Prüfung, parallel zum Rest-Bau |
| **Funktions-Stopp** So 24.01. | – | nur noch Fehler, Texte, Einreichung | – |
| **Einreichung** bis Di 02.02. | Checkliste C grün? | einreichen mit „manuell veröffentlichen“ | in Q4 mit 6–7 Stunden je Woche fertig machen, ohne Druck |
| **M3** So 14.03. | App 1 im Store oder im Review? | 0–5 Stunden im Abitur für Zahlen und Notfälle, Claude Pro läuft weiter | **Ruhezeit:** Claude Pro ruht, kein Bau bis nach der letzten Prüfung |
| **Signal** 3 Wochen nach jedem Start | ≥ 300 $ MRR ohne bezahlte Werbung? Fällt der Tag in die Startpause, siehst du am Tag nach deiner letzten Prüfung nach; bestanden zählt, sonst gilt die zweite Prüfung. Fällt er auf den Tag einer mündlichen Nachprüfung oder in die Woche davor, liest du am Tag nach deiner letzten Nachprüfung ab (05, Abschnitt 9.2) | Creator-Geld, für alle Apps zusammen bis 18.07. höchstens 750 € | nur eigene Posts, nächstes Format oder nächste App |
| **Zweite Signalprüfung** 21 Tage nach dem ersten täglichen Post nach der letzten Prüfung, spätestens Di 29.06. (nur für eine App, die vor dem 15.03. gestartet ist); mit mündlicher Nachprüfung am Tag nach der letzten Nachprüfung, spätestens Do 01.07. | ≥ 300 $ MRR? | wie Signal | wie Signal |
| **Zeitarbeit** Mo 21.06., in jedem Fall | Liegt ein unterschriebener Vertrag aus dem Winter vor (Beginn 19.07.)? | zwei Zeitarbeitsfirmen anfragen, fester Termin Mo 05.07.–Fr 16.07. (1 h) | zwei Zeitarbeitsfirmen anfragen, fester Termin für den ganzen Sommer (1 h) |
| **Vorentscheidung Jobbeginn** Fr 25.06. | Ist eine App im Store oder im Review? | Jobbeginn Mo 19.07.: ohne Vertrag nennst du der Zeitarbeitsfirma dieses Datum, mit Vertrag sagst du ihr für Mo 05.07.–Fr 16.07. ab | Jobbeginn Mo 05.07.: ohne Vertrag nennst du der Zeitarbeitsfirma dieses Datum, mit Vertrag sagst du ihr für Mo 05.07.–Fr 16.07. zu (06, Abschnitte 2.2 und 2.10) |
| **Stichtag** So 04.07. | Ist eine App im Store? | weiter bis Tor 1; hast du am Fr 25.06. den 05.07. zugesagt, hältst du die Zusage ein und betreust die App abends | Ferienjob ab Mo 05.07., keine neue App mehr. Galt am Fr 25.06. der 19.07., fragst du am Mo 05.07. die Zeitarbeitsfirmen vom Mo 21.06., ob du sofort beginnen kannst; das ist unsicher (06, Abschnitt 2.10) |
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
Tage vor, auch Umschalttag und Übertragung (bei Umzug Sa 11.09. um 7, bei
Sa 04.09. um 14); die Entscheidung fällt aber frühestens am Mo 19.07. Den
Umzugstag legst du bis Sa 31.07. fest, bei einem Umzug vor Sa 18.09. schon bis
Mo 19.07. Alle Schritte stehen in
[`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md)
(früherer Umzug: Abschnitt 1.4).

### Weg A – kein Treffer (100,0 von 100 Läufen)

- **Ab Mo 19.07. Ferienjob** als kurzfristige Beschäftigung, von Anfang an
  schriftlich befristet bis Di 31.08. (32 Arbeitstage, 256 Stunden) oder,
  besser, gleich bis Fr 10.09. (40 Arbeitstage, 320 Stunden).
  - **Geld:** bei 14,60 € je Stunde (Mindestlohn 2027) 3.738 € bis Di 31.08.
    und 4.672 € bis Fr 10.09., bei 15,87 € 4.063 € bzw. 5.078 €, bei 18,50 €
    4.736 € bzw. 5.920 €. Sozialabgaben fallen nicht an, wenn der
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
  - **Im Modell** (Job bis Fr 10.09.) gibt es Lohn in 77,7 von 100 Läufen
    (angesetzt ist eine Chance von 70–85 von 100), im Median 5.001 € nach
    Fahrtkosten. Mit Ende am Di 31.08. läge dein Geld im Mittel um 767 €
    niedriger.
- **Keine neue App, keine neuen Creator.** Apps, die am 18.07. schon fertig
  gebaut oder eingereicht sind, dürfen noch erscheinen, nur mit Wochenabo.
- **Am selben Tag kündigst du,** was Betrieb und Abschluss nicht brauchen.
  Claude Pro erst, wenn die Zwischensummen für die Anlage EÜR erstellt sind,
  keine App mehr im Review ist, jede Übertragung durch ist und das
  Hinweis-Update vom So 15.08. ausgeliefert ist; bei Abrechnungstag am 8. also
  bis Di 07.09. Steht weder Übergabe noch Verkauf an und ist das
  Hinweis-Update am Fr 06.08. fertig vorbereitet, kündigst du schon bis
  Sa 07.08. ([`details/06_SOMMER_UND_ABSCHLUSS.md`](details/06_SOMMER_UND_ABSCHLUSS.md),
  Abschnitt 6, Schluss).
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

### Weg B – Tor 1 bestanden, Tor 2 verfehlt (in keinem von 300.000 Läufen)

- Bis 08.08. Creator nur aus dem Umsatz der letzten vier Wochen, abzüglich
  der Creator, die schon daraus bezahlt sind; jede Woche ein Paywall-Test.
- Kein Ferienjob vor Tor 2. Hast du einen Vertrag unterschrieben, brauchst du
  dafür die Kündigungsklausel oder Probezeit, die du hineingeschrieben hast.
- Danach wie Weg A. Verkaufen oder Übergeben ist hier meist die beste Wahl,
  weil die App messbaren Umsatz hat.
- Achte auf die Familienversicherung (Jahresgewinn 2027 über ~7.080 €, also
  im Schnitt über ~590 € im Monat) und melde Gewinne der Krankenkasse.

### Weg C – ein echter Treffer (2 von 300.000 Läufen)

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
      App: Eingabetext geht an Anthropic, das ihn nach eigener Angabe binnen
      30 Tagen löscht (bei Verdacht auf Verstöße bis zu 2 Jahre),
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
      nach eigener Angabe binnen 30 Tagen, bei Verdacht auf Verstöße bis zu
      2 Jahre) und dich als Verantwortlichen
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
      bzw. bei der zweiten Prüfung, spätestens Di 29.06.; mit mündlicher
      Nachprüfung am Tag nach der letzten Nachprüfung, Abschnitt 13)
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
      verkaufen (Abschnitt 14); Umzugstag festgelegt (bei einem Umzug vor
      Sa 18.09. schon bis Mo 19.07.; dann rücken die Tage unten vor,
      Abschnitt 14)
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
      wenn die Zwischensummen für die Anlage EÜR erstellt sind, keine App mehr
      im Review ist, jede Übertragung durch ist und das Hinweis-Update vom
      So 15.08. ausgeliefert ist, bei Abrechnungstag am 8. also bis Di 07.09.;
      ohne Übergabe und Verkauf und mit fertig vorbereitetem Hinweis-Update
      schon bis Sa 07.08., 06, Abschnitt 6, Schluss), Supabase, EAS (falls
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
| 1 | Gründung (im Modell im Median in der Woche ab Mo 01.02.) | Gewerbe, Domain-Paket, Prepaid-Nummer; Gründungsberatung der IHK, wenn sie kostenlos ist (vorher fragen; sonst Fragen schriftlich ans Finanzamt) | mit Apple zusammen 140–380 €, typisch ~200 € |
| 2a | von der Gründung bis zum ersten Start | Claude Pro, Domain mit Postfach, Prepaid-Nummer | 23–45 € im Monat, typisch ~28 € |
| 2b | ab dem ersten Start | dazu KI-API nach Nutzung; Supabase und EAS im Gratis-Tarif, bis ein Signal da ist | 23–75 € im Monat, typisch ~30 € |
| 2c | Ruhezeit im Abitur, wenn keine App im Store oder im Review ist | nur Domain und Nummer; Claude Pro ruht | 2–30 € im Monat, typisch ~5 € |
| 3 | nur nach Signal | Creator | für alle Apps zusammen bis 18.07. höchstens 750 € (mit Plattformgebühr), danach nur aus dem Umsatz der letzten vier Wochen |
| 4 | nach dem Ende der Jagd | Server und Domain bis zum Dienstende | 5–35 € im Monat, typisch ~12 € |
| 5 | Abschluss | Abmeldung, nicht abziehbare Umsatzsteuer auf Auslandsrechnungen, EÜR und Einkommensteuererklärung 2027 selbst über ELSTER; Steuerberater nur im Ernstfall | 20–500 €, typisch ~80 € |
| – | nur wenn der Gewinn über ~590 € im Monat liegt | eigene Kranken- und Pflegeversicherung | ~280 € im Monat |

**Was im Modell herauskommt** (DEIN PLAN, nur die App, alles bis zum Schluss
eingerechnet, 300.000 Läufe):
- Median −567 €, im Mittel −533 €; Gewinn in 3,7 von 100 Läufen;
- in 90 von 100 Läufen höchstens 786 € Verlust, mehr als 1.000 € Verlust in
  0,5 von 100;
- der höchste Betrag, den du im Lauf des Projekts vorstreckst: im Median
  481 €, in 90 von 100 Läufen höchstens 621 €, in 99 von 100 höchstens
  1.269 €, nie mehr als 1.947 €; ein Nachschuss kommt nicht vor;
- mehr als 5.000 € Verlust in keinem Lauf; die Familienversicherung endet in
  1 von 300.000 Läufen.

Creator-Geld fließt im Modell nur in 2,9 von 100 Läufen, im Mittel aller
Läufe 18 €. Die hohen Einsätze entstehen vor allem, wenn es fließt: Ohne
Creator-Geld wären es in 99 von 100 Läufen höchstens 778 € und nie mehr als
1.299 €. Mit
Ferienjob und Übergabe steht alles zusammen in
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
| Du kommst mit den Grundlagen nicht voran | Lernmodus, kleinere Schritte, ein Thema je Woche; im Zweifel App 1 nach der Schnittliste kleiner schneiden (Abschnitt 13, Stunden-Messpunkt); mehr lässt sich nicht kürzen |
| App 1 ist am 14.03. nicht eingereicht | normal (im Modell in 85 von 100 Läufen): Ruhezeit im Abitur; nach der letzten Prüfung fertig bauen und einreichen, im Median in der Woche ab Mo 14.06., im Store im Median ab der Woche ab Mo 28.06. |
| Am 20.12. besteht keine Idee | No-Go-Regel: nicht gründen, kein Apple-Konto kaufen, weiter lernen; nach der ETH-Bewerbung fünf neue Ideen prüfen, Entscheidung bis Sa 09.01.; besteht auch dann keine, erst nach dem Abitur weiter ([`details/04_IDEENWAHL.md`](details/04_IDEENWAHL.md), Abschnitt 7) |
| Du bekommst keinen Ferienjob | am Mo 21.06. fragst du ohnehin zwei Zeitarbeitsfirmen für einen festen Termin an (Abschnitt 12, KW 23–26); hast du am Fr 02.07. noch keine Zusage, fragst du zwei weitere an und gehst zu ihrer Sprechzeit hin (06, Abschnitt 2.2); im Modell gibt es Lohn in 77,7 von 100 Läufen (angesetzt 70–85 von 100) |
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

Modell [`plan/plan_500k.py`](../plan/plan_500k.py) im Stand von Commit
280b3eb. „Dein Geld“ ist, was die App bringt oder kostet, dazu ein
Verkaufspreis und dein Lohn, jeweils bis zum Schluss, einschließlich
Abmeldung, Steuererklärung und gegebenenfalls eigener Krankenversicherung.
Eine Übergabe an ein Elternteil zählt nicht dazu, dieses Geld gehört dem
Elternteil. Einkommensteuer ist nicht abgezogen; sie fiele nur in 3 von 5.000
Läufen an, im Mittel rund 2 € ([`details/07_HEBEL.md`](details/07_HEBEL.md),
Abschnitt 15).

### Stand 25.11.: die Stufen

300.000 Läufe je Zeile. Die vier einzelnen Hebel laufen gegen die
Ausgangslage, Nachfolger und Ferienjob gegen PLAN MIT HEBELN
([`details/07_HEBEL.md`](details/07_HEBEL.md), Abschnitte 1 und 4.3).
Unterschiede bis etwa 0,15 zwischen zwei Zeilen sind Zufall.

| Stufe | nur App: Gewinn in … von 100 | dein Geld im Plus in … von 100 | dein Geld ≥ 10.000 € in … von 100 | Median | Mittel | schlechteste 10 % ab | beste 1 % ab | 500.000 € erreicht |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Plan vom 23.11., wie er dastand | 6,21 | 6,21 | 0,18 | −1.136 € | −954 € | −1.514 € | +2.252 € | 0 |
| derselbe Plan mit Verkaufsstopp am 15.08. (Pflicht von Apple) | 2,71 | 2,71 | 0,16 | −1.184 € | −1.074 € | −1.545 € | +1.049 € | 0 |
| dazu alle Stunden und Regeln der Detailpläne (**Ausgangslage**) | 0,59 | 0,59 | 0 | −1.174 € | −1.158 € | −1.524 € | −201 € | 0 |
| … nur Kosten senken (mit Ruhezeit im Abitur) | 2,19 | 2,19 | 0 | −585 € | −565 € | −792 € | +225 € | 0 |
| … nur schneller bauen und review-fest planen | 0,93 | 0,93 | 0 | −1.149 € | −1.122 € | −1.510 € | −30 € | 0 |
| … nur Markt (Deutsch zuerst) und Ideenwahl | 0,60 | 0,60 | 0 | −1.174 € | −1.157 € | −1.522 € | −205 € | 0 |
| … nur zweite Signalprüfung Ende Juni | 0,56 | 0,56 | 0 | −1.174 € | −1.158 € | −1.523 € | −202 € | 0 |
| **PLAN MIT HEBELN** (alle vier zusammen) | 3,73 | 3,73 | 0 | −564 € | −528 € | −783 € | +395 € | 0 |
| + Übergabe oder Verkauf (Elternteil hat zugesagt) | 3,53 | 3,70 | 0,01 | −564 € | −524 € | −784 € | +427 € | 0 |
| + Ferienjob ab 19.07. | 3,70 | 78,54 | unter 0,01 | +4.260 € | +3.306 € | −584 € | +5.337 € | 0 |
| + Ferienjob ab 19.07., ab 05.07. ohne App im Store | 3,91 | 78,55 | unter 0,01 | +4.346 € | +3.513 € | −590 € | +6.146 € | 0 |
| **+ Übergabe oder Verkauf + Ferienjob = DEIN PLAN, Stand 25.11.** | **3,70** | **78,53** | **0,03** | **+4.344 €** | **+3.518 €** | **−590 €** | **+6.167 €** | **0** |
| zum Vergleich: nur Ferienjob ab 05.07., keine App, keine Gründung | – | 77,49 | 0 | +6.031 € | +4.778 € | 0 € | +6.776 € | 0 |

### Stand 25.11.: was Chance und Geld erhöht

Jede Zeile läuft gegen DEIN PLAN, Lauf für Lauf gepaart, mit 100.000 Läufen.
DEIN PLAN liegt in dieser Rechnung bei 3,64 statt 3,70 von 100; der
Unterschied ist Zufall ([`details/07_HEBEL.md`](details/07_HEBEL.md),
Abschnitt 4.1).

| Variante | nur App: Gewinn in … von 100 | dein Geld im Median | im Mittel | Hinweis |
|---|---:|---:|---:|---|
| **DEIN PLAN** | **3,64** | **4.345 €** | **3.521 €** | |
| Creator-Geld weglassen | 4,58 | 4.356 € | 3.539 € | planbar, deine Entscheidung; bis zu 750 € weniger Einsatz |
| Schnittliste aus 02, Abschnitt 8 von Anfang an | 3,92 | 4.341 € | 3.518 € | planbar; spart ~7 der 113 Stunden |
| mehr am eigenen Projekt lernen (Lernzeit wie in 01: 12/15/20 statt 20/28/40 Stunden) | 4,50 | 4.322 € | 3.475 € | nur, wenn das Lernen am Projekt reicht |
| **alle drei zusammen** | **6,21** | 4.332 € | 3.503 € | beste planbare Kombination |
| ohne Vorbereitung von App 2 im Review | 3,48 | 4.341 € | 3.516 € | die Vorbereitung (bis 6 Stunden, ohne Code) ist im Plan |
| falls ein Betrieb mit Tariflohn ab 19.07. zusagt | 3,64 | 4.752 € | 3.832 € | die Bewerbung dort ist im Plan; ob einer zusagt, entscheidet der Betrieb |
| Job nur bis Di 31.08. statt Fr 10.09. | 3,64 | 3.363 € | 2.754 € | −767 € im Mittel |
| ohne Stichtag 04.07. (Job erst ab 19.07.) | 3,54 | 4.260 € | 3.312 € | −209 € im Mittel; der Stichtag lohnt sich |
| Job ab 05.07., wenn am 04.07. keine App 300 $ MRR zeigt | 2,79 | 5.413 € | 4.191 € | Geld gegen Chance; setzt einen Vertrag ab 05.07. voraus |
| App 2 schon während des Reviews, mit Code | 4,81 | 4.370 € | 3.544 € | gegen 02, Abschnitt 9: die Lehren aus dem Review-Log fehlen sonst in der Vorlage |
| ohne Ruhezeit im Abitur | 4,34 | 4.291 € | 3.440 € | gegen die Abiturregel (Abschnitt 4) |
| höchstens eine App | 1,95 | 4.277 € | 3.455 € | deutlich schlechter |
| Bauzeiten wie mit Programmierkenntnissen | 20,55 | 4.384 € | 3.640 € | Empfindlichkeit, kein Hebel |

### Stand 25.11.: Gegenproben

Jede Zeile ändert eine Annahme, 300.000 Läufe. Die Gewinnchance der App hängt
stark an Annahmen, die niemand messen kann; dein Geld kaum, weil es am
Ferienjob hängt ([`details/07_HEBEL.md`](details/07_HEBEL.md), Abschnitt 12).

| Gegenprobe zu DEIN PLAN | nur App: Gewinn in … von 100 | dein Geld im Mittel | Hinweis |
|---|---:|---:|---|
| **wie gerechnet** | **3,70** | **3.518 €** | |
| alter, schneller Start eines Treffers (1.000/3.000/8.000 $ MRR) | 8,32 | 3.597 € | so bis 24.11. |
| Umsatz läuft ohne Posts weiter | 5,92 | 3.609 € | so bis 24.11. |
| Spitze ohne bezahlten Test nur um ein Viertel kleiner statt halb | 4,96 | 3.557 € | |
| Creator-Geld holt die Spitze auf 70–100 % zurück | 3,65 | 3.516 € | so bis 24.11. |
| ohne Startpause (eine freigegebene App erscheint auch im Abitur) | 3,73 | 3.515 € | die Startpause kostet nichts |
| nach dem Ende der Jagd gar keine Posts mehr | 3,51 | 3.520 € | |
| die zweite Sprache kostet zusätzlich Stunden (+3/+6/+12 h) | 3,31 | 3.526 € | |
| langsameres Wachstum eines Treffers (×1,2/1,6/2,2 je Monat) | 2,77 | 3.495 € | |
| alte Werbekosten (45–49 % vom Umsatz) | 0,66 | 3.433 € | so bis 24.11. |

| Gegenprobe zu PLAN MIT HEBELN (ohne Nachfolger und ohne Job) | Gewinn in … von 100 | Median | Mittel |
|---|---:|---:|---:|
| **wie gerechnet** | **3,73** | **−564 €** | **−528 €** |
| Bauzeiten ohne den Hebel „Bau“ (80/140/280 h) | 2,91 | −573 € | −545 € |
| strengerer Markt 2027 | 2,56 | −578 € | −554 € |
| Verkaufsstopp schon am Sa 31.07. (Dienstende Di 31.08.) | 1,18 | −602 € | −594 € |
| Verkauf bis Di 31.08. (Dienst bis Fr 01.10., nur nach Beratung) | 8,77 | −529 € | −450 € |

So liest du die Tabellen (ausführlich in
[`details/07_HEBEL.md`](details/07_HEBEL.md)):
- **Die App ist ein Lernprojekt.** Gewinn aus der App gibt es in etwa 4 von
  100 Läufen, und dann meist nur ein paar hundert Euro (mehr als 409 € nur in
  1 von 100 Läufen). 500.000 € erreicht kein Lauf.
- **Zwei Pflichten drücken die Chance:** Apples 31-Tage-Regel senkt den Plan
  vom 23.11. von 6,2 auf 2,7 von 100, die Stunden der Detailpläne senken ihn
  weiter auf 0,6. Beides ist keine Wahl.
- **Jede Woche länger verkaufen zählt:** Mit Verkaufsstopp am 31.07. statt am
  15.08. läge PLAN MIT HEBELN bei 1,2 statt 3,7 von 100, mit Verkauf bis
  31.08. bei 8,8. Das geht aber nur nach Beratung, weil der Dienst dann bis
  01.10. läuft, also nach deinem Umzug.
- **Kosten senken** ist der stärkste Hebel für die App selbst: Der
  Medianverlust halbiert sich, die Chance steigt von 0,6 auf 2,2 von 100. Erst
  mit niedrigen Kosten werden kleine Erfolge zu Gewinnen; deshalb bringen alle
  vier Hebel zusammen (3,7 von 100) mehr als die Summe der einzelnen.
- **Schneller bauen** bringt nach den vorsichtigen Werten wenig (0,9 statt 0,6
  von 100). Mit Bauzeiten wie mit Programmierkenntnissen läge die Chance bei
  rund 21 von 100. Deine echten Stunden am Stunden-Messpunkt (Di 29.12.) sagen
  mehr als jede Schätzung.
- **Markt und Ideenwahl** heben sich auf: Der deutsche Markt ist kleiner, eine
  sorgfältige Ideenwahl gleicht das etwa aus.
- **Ein Nachfolger** ändert im Modell fast nichts (dein Geld im Mittel +4 €).
  Er bleibt als Versicherung für den seltenen Treffer.
- **Der Ferienjob** macht aus dem Sommer in 78,5 von 100 Läufen ein Plus. Er
  kostet die App kaum etwas, weil die Jagd ohnehin am 18.07. oder schon am
  Stichtag 04.07. endet. Rein nach Geld wäre „nur Ferienjob“ im Mittel rund
  1.260 € und im Median rund 1.690 € besser; das ist der Preis für das
  Lernprojekt samt der kleinen Chance.
- **Creator-Geld** kannst du weglassen: Ohne ist die Chance höher (4,58 statt
  3,64 von 100), dein Geld gleich, und auch 10.000 € oder mehr werden nicht
  seltener. Mehr Creator-Geld (bis 1.500 €) ändert nichts. Der Grund: Es hebt
  die Spitze einer App nur um 5–15 %, kostet aber 60–150 € je Video.
- **Geld gegen Chance:** Ein Jobstart schon am 05.07., sobald keine App 300 $
  MRR zeigt, bringt im Mittel 670 € mehr und senkt die Chance von 3,64 auf
  2,79 von 100. Er setzt einen Vertrag ab 05.07. voraus; der Plan bleibt beim
  Stichtag ohne Schwelle.
- **Die Zahl ist empfindlich:** Je nach Annahmen liegt die Chance der App grob
  zwischen 1 und 8 von 100. Lies 3,7 als Größenordnung, nicht als genaue Zahl.
  Eine fünfte Prüfung hat danach drei kleine Abweichungen gefunden, die noch
  nicht eingearbeitet sind; mit ihnen läge die Chance eher bei 3,3 als bei 3,7
  von 100 ([`details/07_HEBEL.md`](details/07_HEBEL.md), Abschnitt 15).
- **Was nicht hilft:** höchstens eine oder zwei Apps, Tor 1 früher oder
  später, eine niedrigere Signalschwelle, mehr Creator-Geld, mehr Posts als
  6,5 Stunden je Woche ([`details/07_HEBEL.md`](details/07_HEBEL.md),
  Abschnitt 10).

### Stand 23.11.: Rechtsformen, Tore und Creator-Geld

Diese Tabelle ist mit dem Modell vom 23.11. gerechnet: alte Kosten, **ohne
Verkaufsstopp** und ohne die Korrekturen vom 25.11. Die Zahlen sind deshalb
viel zu günstig. Wo die Rechnung vom 25.11. eine Variante wieder geprüft hat,
steht das neue Ergebnis unten dabei.

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
- **Creator-Geld:** Am 23.11. lagen Signalregel, ganz ohne Testgeld und bis zu
  1.500 € fast gleich (Gewinn in ~6 von 100 Läufen, im Mittel ~−950 €). Tests
  gleich beim Start verdoppelten die seltenen Ergebnisse ab 10.000 € (0,31
  statt 0,17 von 100), kosteten aber im Median ~500 € mehr. **Stand 25.11.:**
  Ganz ohne Creator-Geld ist die Chance höher (4,58 statt 3,64 von 100), dein
  Geld gleich; bis zu 1.500 € ändern nichts. Der Grund ist eine Korrektur:
  Creator-Geld hebt die Spitze einer App nur um 5–15 %. Behältst du das Geld,
  gilt die Signalregel; Tests gleich beim Start sind nicht neu gerechnet.
- **UG:** In keiner Form passt sie zu deinen 5.000 €. In 99 von 100 Läufen
  lassen Pflichtkosten und Auflösung gar keine Gründung zu. Das liegt an den
  festen Kosten von 4.000–9.000 € bis zur Löschung, nicht an den Annahmen,
  die am 25.11. korrigiert wurden.
- **Frühe Tore** (28.02.) hätten App 1 meist abgebrochen, bevor sie fertig
  ist: Gewinn nur in ~1 von 100 Läufen. **Stand 25.11.:** Auch ein Tor 1 am
  04.07. oder 11.07. ist schlechter (2,69 bzw. 3,54 statt 3,71 von 100, PLAN
  MIT HEBELN, gepaart), ebenso eines am 01.08. (3,38).
- **Ganz ohne Tore** war es schlechter als mit den Sommer-Toren (4,2 statt
  6,2 von 100): Späte Apps und weitere Ausgaben kosten mehr, als sie bringen.
  Nicht neu gerechnet.
- **Gründen schon im Dezember** war schlechter als „erst bauen, dann gründen“
  (5,8 statt 6,2 von 100, im Mittel ~80 € mehr Verlust). **Stand 25.11.:**
  Noch später zu gründen (bei 85 % statt bei halb fertiger App) macht kaum
  einen Unterschied (3,85 statt 3,71 von 100).
- **Schneller bauen** ist der größte Hebel. **Stand 25.11.:** Mit den
  Bauzeiten von jemandem, der programmieren kann, wäre App 1 in 95,9 von 100
  Läufen bis So 14.03. eingereicht, und die Chance läge bei 21,58 statt 3,71
  von 100 (PLAN MIT HEBELN, gepaart); im Mittel bliebe aber ein Verlust
  (−249 €). Deshalb soll App 1 so klein wie möglich sein, und deshalb lernst
  du vor allem am eigenen Projekt.
- **Startpause im Abitur:** Am 23.11. kostete sie etwas (6,7 statt 6,2 von 100
  Läufen mit Gewinn). **Stand 25.11.:** Sie kostet nichts (ohne sie 3,73 statt
  3,70 von 100). Im Modell gewinnt eine App im Abitur ohne Posts kaum neue
  Kunden; früher zu erscheinen bringt ihr deshalb fast nichts. Dafür musst du
  im Abitur weder Posts machen noch auf Bewertungen reagieren.
- **Gegenproben:** Wirkten Videos ohne Gesicht schlechter, sank die Chance am
  23.11. auf ~4,6 von 100 (nicht neu gerechnet). **Stand 25.11.:** Im
  strengeren Markt 2027 sinkt sie auf 2,56 statt 3,73 von 100 (PLAN MIT
  HEBELN). Die Grenze von 5.000 € hält in jedem Fall.
- **Späte Starts:** Am 23.11. erschien in ~84 von 100 Läufen nach Tor 1 noch
  eine App, die vorher eingereicht war. **Stand 25.11.:** Allein die zweite
  App startet in 41,3 von 100 Läufen erst nach Tor 1. Auf Apps, die erst nach
  Tor 1 erscheinen, beruhen 32,5 von 100 Gewinnläufen der App, also rund 3 von
  10 (DEIN PLAN).

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
