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
[`plan/plan_500k.py`](../plan/plan_500k.py), Szenarien „Deine Angaben“.

> **Worauf du dich einlässt** (Modell, 300.000 Läufe je Variante):
>
> | | |
> |---|---|
> | Zeit bis 31.08. | **~750 Stunden** verfügbar, davon ~200 bis zum Ende des Abiturs (10 je Schulwoche, ~31–38 je Ferienwoche, 3–7 in Q4, 0–5 im Abitur, ab Juni 15–55). Endet die Jagd am 18.07. (der Normalfall), sind es ~400 Stunden für Lernen und App |
> | App 1 fertig | im Median am 07.06.; bis 14.03. in 26 von 100 Läufen, sonst meist erst nach dem Abitur |
> | App 1 im App Store | im Median ab 21.06. |
> | Geld bis zum Schluss (einschließlich Abmeldung und Steuererklärung) | im Median **−1.136 €**, im Mittel −952 €, nie mehr als 5.000 € |
> | überhaupt ein Gewinn | in **6,2 von 100** Läufen, meist nur wenig; die besten 1 % der Läufe enden ab +2.303 € |
> | 10.000 € oder mehr | in 0,17 von 100 Läufen |
> | 500.000 € bis 31.08.2027 | **in keinem** von 300.000 Läufen |
>
> Das ist ehrlich gesagt ein **Lernprojekt mit kleiner Gewinnchance**, kein
> Weg zu 500.000 €. Es kostet dich im Normalfall rund 1.136 € und ~400
> Stunden. Dafür hast du am Ende eine eigene App im App Store, echte
> Programmier- und Marketingerfahrung vor dem ETH-Studium und gemessene Zahlen.
> Die Regeln unten sorgen dafür, dass weder das Abitur noch die ETH-Zulassung
> noch dein Geld für Zürich darunter leiden.

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
12. [Woche für Woche bis 31.08.](#12-woche-für-woche-bis-3108)
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

---

## 2. Das Wichtigste in Kürze

1. **Bis Januar kostet es fast nichts.** Du lernst die Grundlagen und baust
   App 1 mit Claude in Expo Go, ganz ohne Firma. Ausgaben: Claude Pro
   (~21 € im Monat) und ab den Weihnachtsferien ein paar Dollar Guthaben für
   die Claude API, um die KI-Funktion zu testen.
2. **Gegründet wird erst, wenn App 1 halb steht** (im Modell im Median am
   25.01., in 47 von 100 Läufen erst im Februar oder später), und zwar
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
   endet die Jagd: keine neue App, kein Creator-Geld. Apps, die dann schon
   eingereicht sind, dürfen noch erscheinen. Vor dem Umzug nach Zürich
   meldest du das Gewerbe ab oder klärst mit einem Steuerberater, wie es
   weitergeht.

---

## 3. Die eine große Entscheidung: Rechtsform und Anonymität

Du entscheidest das, sobald App 1 etwa halb fertig ist, voraussichtlich
zwischen Mitte Januar und Februar. Bis dahin brauchst du keine Firma: Bauen
und Testen in Expo Go geht ohne.

Für echte Käufe, TestFlight und den App Store brauchst du ein Apple-Konto
(99 $ im Jahr). Apple verlangt dafür kein Gewerbe, nur ein Apple-Konto mit
Zwei-Faktor-Anmeldung, Volljährigkeit und deinen echten Namen. Sobald du Abos
verkaufst, ist das in Deutschland aber ein Gewerbe, und beim Einreichen
erklärst du dich für die EU als Händler. Bei der Anmeldung wird festgelegt,
wessen Name als Verkäufer im Store steht. Deshalb legst du das Apple-Konto
erst an, wenn das entschieden ist. Steht es nach dem Gespräch mit deinen
Eltern schon fest, kannst du dich in den Weihnachtsferien anmelden; die 99 $
gelten dann 12 Monate ab diesem Tag.

**Was öffentlich wird**

| | Einzelunternehmen (du) | Einzelunternehmen eines Elternteils | UG mit dir als Geschäftsführer |
|---|---|---|---|
| Verkäufer im App Store (weltweit) | dein voller Name (Apple erlaubt keinen anderen Namen) | Name des Elternteils | Firmenname |
| EU-Seite der App (Pflicht für Händler seit 2025) | Adresse oder Postfach (mit Nachweis), Telefon, E-Mail | dasselbe vom Elternteil | Firmenadresse aus der D-U-N-S-Nummer, Telefon, E-Mail |
| Impressum (Website, App, Markenkonten) | dein Name und eine zustellfähige Anschrift (praktisch das Elternhaus; ein Postfach reicht nicht, ein Adressdienst ist für Einzelpersonen rechtlich unsicher) | Name und Anschrift des Elternteils | Firma, Anschrift und **dein Name als Geschäftsführer** |
| Register | Gewerberegister: Name, Anschrift, Tätigkeit gibt die Gemeinde an jeden heraus | dasselbe vom Elternteil | Handelsregister kostenlos für jeden: dein Name, Geburtsdatum, Wohnort; North Data zeigt Name und Wohnort |
| Gesicht und Stimme | nie nötig | nie nötig | nie nötig |

**Was es kostet und bringt** (Modell, 300.000 Läufe je Variante, alles bis zur
Abmeldung bzw. Auflösung eingerechnet)

| | Einzelunternehmen | UG, Anschrift der Eltern | UG, gemietete Geschäftsadresse |
|---|---:|---:|---:|
| Formalkosten bis zum Ende | ~150–1.300 € (Gewerbe, Apple, Erstberatung, Steuererklärung) | ~4.000–9.000 € bis zur Löschung (frühestens Ende 2028) | dazu 50–130 € je Monat für die Adresse |
| passt in 5.000 € | ja | **nein:** in 99 von 100 Läufen lassen Pflichtkosten und Auflösung gar keine Gründung zu | **nein:** in fast allen Läufen (99,9 von 100) keine Gründung |
| überhaupt ein Gewinn | 6,2 von 100 | 0 von 100 | 0 von 100 |
| Geld im Median | −1.136 € | −357 € (nur Claude, weil meist gar nicht gegründet wird und dann auch keine App erscheint) | −355 € (ebenso) |
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
  - **Rechtlich:** App und Gewinn gehören dem Elternteil. Es haftet
    unbeschränkt, versteuert den Gewinn und meldet die Nebentätigkeit seinem
    Arbeitgeber, falls der Arbeitsvertrag das verlangt (als Beamter:
    genehmigen lassen). Geld, das es dir gibt, ist eine Schenkung (bis
    400.000 € je Elternteil steuerfrei).
  - Das geht nur, wenn das Elternteil es wirklich will und versteht. Ein
    „Strohmann“, hinter dem du nach außen die Firma führst, schützt keinen
    von euch.
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
- eine Projekt-E-Mail auf deiner Domain;
- Markenkonten ohne Gesicht und ohne Stimme, **getrennt von deiner privaten
  Identität**:
  - nur mit Projekt-E-Mail und Zweitnummer anlegen;
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
| 15.03.–05.04. (letzte Q4-Tage bis Do 18.03., Osterferien) | 0–5 | Abiturvorbereitung |
| schriftliches Abitur 06.04.–13.05. | 0–1 | an Prüfungstagen und davor gar nichts |
| 5. Prüfungsfach und Nachschreibtermine 19.05.–07.06. | 0–5 | bei einer Präsentationsprüfung zwei Wochen gar nichts; Mo 07.06. kann noch Prüfungstag sein |
| nach deiner letzten Prüfung bis 04.07. | 15–40 | mögliche mündliche Nachprüfung 28.–30.06., Zeugnis 01.–03.07. |
| ab 05.07. | Mo–Sa ~9 h, So frei | davon ~6 h je Woche für Zürich (Zimmer, Unterlagen, Mathe) |

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
- **Die 0–5 Stunden im Abitur** sind für Zahlen, Notfälle und kleine
  Bau-Schritte ohne Termindruck da, nie an Prüfungstagen und nie am Tag
  davor. Eine fertige App darfst du einreichen. Keine Posts, keine
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
- **Ausgaben in Stufen** (Abschnitt 17): bis zur Gründung nur Claude Pro und
  ein kleines Guthaben für die Claude API zum Testen (wenige Dollar,
  Ausgabenlimit 50 $), dann die Gründung, Creator-Geld erst nach einem Signal.
- Kein Kredit, kein Dispo, keine Ratenzahlung.
- Vor jeder Ausgabe über 50 €: Sind danach alle Pflichtkosten bis 31.08. und
  ~800 € für Abmeldung und Steuererklärung noch gedeckt?
- **Familienversicherung:** Entscheidend ist der Gewinn, also Einnahmen
  minus Kosten. Er muss regelmäßig unter ~590 € im Monat bleiben (Grenze
  2027, 1/7 der Bezugsgröße von 4.130 €, vorbehaltlich Bundesrat; 2026:
  565 €).
  - **So rechnet die Kasse:** Sie schätzt deinen regelmäßigen Monatsgewinn
    vorausschauend, maßgeblich ist am Ende der Steuerbescheid. Ein
    einzelner starker Monat zählt nicht, ein dauerhaft höherer Gewinn schon.
  - **Was du tust:** Zeichnet sich ab, dass dein Gewinn 2027 zusammen über
    ~7.000 € liegt, meldest du es der Kasse.
  - **Stunden:** Sie zählen nach den Hinweisen der Krankenkassen nur
    zusammen mit dem Einkommen. Als Hauptberuf gilt die App erst ab mehr als
    30 Stunden je Woche bei mehr als ~1.030 € Arbeitseinkommen im Monat, bei
    20–30 Stunden erst ab ~2.065 €. Deine Stunden nennst du der Kasse so,
    wie sie sind.
  - Keine Angestellten.

**Recht**
- Ein Markenkonto je Plattform, klar als App erkennbar, mit Link auf das
  Impressum. **Keine Konten, die unabhängige Nutzer vortäuschen**, keine
  gekauften oder gefälschten Bewertungen, keine KI-Personen, die eine
  Erfahrung mit der App bezeugen.
- Auf TikTok bei jedem Post den Schalter für kommerzielle Inhalte auf „Your
  brand“ und nur Musik aus der Commercial Music Library. Bezahlte Creator
  kennzeichnen „Werbung“ und nutzen „Paid partnership“.
- Kein automatisches Posten, Kommentieren oder Versenden über inoffizielle
  Werkzeuge; keine Massenanfragen an Creator.
- Kundendaten (Fotos, Support-Mails) nur über Dienste mit Vertrag zur
  Auftragsverarbeitung, nie über dein privates Claude-Abo.

---

## 5. Wer was macht

| Aufgabe | Claude | du |
|---|---|---|
| Grundlagen | erklärt im Lernmodus, stellt dir Übungen, lässt dich Stellen selbst schreiben | lernst ~25–40 Stunden bis Ende Januar (bis 20.12. etwa die Hälfte); fragst nach, bis du es einem Mitschüler erklären kannst |
| Code: App, Paywall, KI-Funktion, Server | schreibt alles in kleinen Schritten, erklärt jeden Schritt, führt die `CLAUDE.md` und das Review-Log | beschreibst, was du willst; testest auf iPhone und iPad; prüfst mit den Checklisten; entscheidest |
| Sicherheit und Datenschutz | Entwürfe, Prüflisten, führt die Prüfungen aus | siehst dir jedes Ergebnis selbst an; verantwortest |
| App Store | Texte, Screenshot-Entwürfe, Antworten an das Review | reichst ein, gibst frei; Verträge, Bank- und Steuerdaten nur du (bzw. das Elternteil) |
| Ideen | Recherche, 10 Kandidaten mit Konkurrenz und Risiken | wählst 3, am Ende eine |
| Videos ohne Gesicht | Hooks, Folientexte, Bildideen, Skripte für Bildschirmaufnahmen, Auswertung | baust die Slideshows (10–20 min je Stück), nimmst Bildschirm und Hände auf, postest von Hand |
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
| Supabase | Server-Funktion für den KI-Aufruf | 0 € zum Testen, Pro 25 $/Monat ab dem Start | KW 53 |
| Claude API (Haiku 5.5) | KI-Funktion der App, getrennt vom Abo | zum Testen ein paar Dollar Prepaid-Guthaben (Karte nötig); im Betrieb typisch ~30 $ je 1.000 aktive Nutzer im Monat; Ausgabenlimit in der Konsole | ab KW 53 |
| Apple Developer Program (Einzelperson) | Gerätetests mit echten Käufen, TestFlight, App Store | 99 $/Jahr; zahlst du per Kreditkarte, muss es deine eigene sein (sonst Verzögerung und Ausweiskopie), oder du meldest dich in der Apple-Developer-App an (verlängert sich automatisch, Checkliste H); ohne D-U-N-S, Konto meist nach wenigen Tagen aktiv | sobald feststeht, wer im App Store steht, spätestens bei der Gründung |
| RevenueCat | Abos, Paywall, Umsatzzahlen, Abo-Prüfung für den Server | frei bis 2.500 $ Monatsumsatz | mit dem Apple-Konto |
| Domain, Website, E-Mail | Impressum, Datenschutz, Support | ~20–60 € im Jahr | bei der Gründung |
| Zweitnummer (Prepaid) | Telefon für Apples EU-Seite | ~0–10 € im Monat | bei der Gründung |
| Canva oder CapCut (Gratisversion) | Slideshows, Untertitel | 0 € | bei der Gründung |

Bewusst **nicht** in App 1:
- **Nutzerkonten:** Dann entfällt die Pflicht zur Kontolöschung. Die
  Abo-Prüfung läuft über die anonyme App-User-ID von RevenueCat.
- **Fremde Tracking- und Analyse-SDKs:** Auch eigene Messereignisse
  („Paywall gesehen“) nur mit Einwilligung (§ 25 TDDDG). Ohne Einwilligung
  wertest du nur aus, was ohnehin anfällt: Downloads, Testphasen, Käufe, Zahl
  der KI-Aufrufe.
- **Fotos speichern:** Fotos gehen an die KI-Funktion und werden danach
  verworfen.
- **Jahresabos:** Du ziehst im September um. Ein Jahresabo verpflichtet dich,
  die App bis zu zwölf Monate weiterzubetreiben. Deshalb nur Wochen- und
  Monatsabo; ein Jahresabo erst, wenn im Juli klar ist, wie es weitergeht.
- **Nutzerinhalte, die andere sehen** (Teilen, Profile): Dann bräuchtest du
  Filter, Melden, Blockieren und veröffentlichte Kontaktdaten (Richtlinie 1.2).
- **Minderjährige als Zielgruppe:** Die App richtet sich an Erwachsene. Keine
  Apps für Schüler, Lernen oder Hausaufgaben. Die Nutzungsbedingungen sagen
  „ab 18“, die Altersfreigabe in App Store Connect beantwortest du ehrlich.
  Das vermeidet Fragen der Einwilligung Minderjähriger (DSGVO) und passt zu den
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
   und zählt ein Tageslimit je App-User-ID. Ohne diese Prüfung wird sie
   zum offenen Zugang, über den Fremde dein API-Budget leerziehen können.
   Genau diesen Fehler hatte in einer Untersuchung ein Drittel der
   betroffenen iOS-Apps mit KI-Funktion.
3. **Zugriffsregeln (RLS)** auf jeder Tabelle, keine Regel `using (true)`.
   Der Security Advisor von Supabase zeigt null Fehler.
4. **Ausgabenlimit in der Anthropic-Konsole als Notbremse:** vor dem Start
   50 $ im Monat, danach jeden Sonntag anpassen (aktive Nutzer × 0,03 $,
   vorsichtig × 0,18 $, davon das Dreifache).
5. Repository und App nach Schlüsseln durchsuchen (`git grep`, GitHub Secret
   Scanning).
6. **Getrennte Projekte für Test und Betrieb.** Der Agent bekommt keine
   Zugangsdaten für den Betrieb, und Backups sind an.
7. **Von außen testen:** Ein Aufruf ohne aktives Abo muss scheitern.
8. Ein neues Supabase-Projekt gleich mit den neuen Schlüsseln anlegen, weil
   die alten Ende 2026 wegfallen.

**Was Claude nie tun darf:** Schlüssel in die App schreiben; Zahlungen,
Verträge oder Veröffentlichungen ohne deine Freigabe; posten oder Nachrichten
verschicken; mit Zugangsdaten für den Betrieb arbeiten; Kundendaten über dein
privates Abo verarbeiten.

---

## 8. Videos ohne Gesicht

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

**Dein Ablauf**
- **Ab der Gründung:** ein Markenkonto je Plattform (TikTok, Instagram,
  YouTube Shorts), mit dem Namen der App und dem Link „Impressum“ zur Website.
  Solange TikTok keinen klickbaren Link erlaubt (meist unter 1.000
  Followern), schreibst du die Web-Adresse der Impressum-Seite als Text in die
  Bio, z. B. „Impressum: deineapp.de/impressum“, nie deine Postanschrift.
- **Format testen:** viele Varianten eines Formats, Hook in der ersten Sekunde
  bzw. auf der ersten Folie. Claude liefert je Tag 10 Hook-Varianten und die
  Folientexte, du baust die Slideshow in Canva (10–20 Minuten) und postest
  von Hand vom iPhone.
- **Menge:** in Q4 höchstens 3 je Woche, auch nach einem Start im Februar
  oder März; im Abitur keine Posts; nach dem Abitur 1–3 am Tag.
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
- **Fällt die Signal-Prüfung in die Startpause**, buchst du erst nach deiner
  letzten Prüfung.
- **Ab 19.07. buchst du keine neuen Creator.** Wer bis 18.07. gebucht ist, wird
  nach dem Posten noch bezahlt.
- **Startet App 1 erst Ende Juni,** kommen die Creator-Videos meist erst nach
  Tor 1. Das Tor misst dann im Wesentlichen ohne ihre Wirkung.
- **Preise:** UGC-Videos bei Influee im Schnitt ~83 $ je 30 Sekunden in
  Deutschland und ~93 $ in den USA; bei Collabstr wurden im Schnitt
  ~150–200 $ je Auftrag bezahlt.
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
- **Noch zu prüfen:**
  - dass du diese drei Fächer in den letzten zwei Jahren durchgehend hattest;
  - dass in den letzten drei Jahren vier weitere Fächer aus Physik, Biologie,
    Informatik, weiterer Sprache (z. B. Deutsch), Erdkunde, Geschichte und
    Wirtschaft unterrichtet wurden. Ob Politik-Wirtschaft als „Wirtschaft“
    zählt, fragst du in der Mail mit.
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

**Ferienwoche (~31–38 Stunden)**

| Tag | Zeit | was |
|---|---|---|
| Mo–Fr (ohne Feiertage) | 9–12 und 13–17 Uhr | Bau-Sitzungen, Tests auf iPhone und iPad, Store-Eintrag |
| Sa | 3 h | Wochenauswertung, Lernen |
| täglich | 1–1,5 h | Schule |

**Q4-Woche (höchstens 6–7 Stunden):** Mo–Fr frei, Sa 3 h, dazu höchstens
zweimal 1–2 h; mit zwei oder mehr Klausuren nur der Samstag.

**Abiturzeit (0–5 Stunden, im schriftlichen Abitur 0–1):** Zahlen ansehen,
Notfälle und kleine Bau-Schritte ohne Termindruck, nie an Prüfungstagen und
nie am Tag davor. Ist eine App schon gestartet: zweimal 20 Minuten je Woche.
Keine Posts, keine Creator.

**Sommerwoche ab 05.07. (~55 Stunden):** Mo–Sa 9–12, 13–17 und 18–20 Uhr,
So frei; davon ~6 Stunden für Zürich.

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
- Drei Ideen sind gewählt.

| Tag | Zeit | was | Ergebnis |
|---|---|---|---|
| Mo 23.11. | 1 h | 10 min: deine Prüfungsfächer gegen die ETH-Bedingung prüfen (Abschnitt 9) – **erledigt:** Chemie P2, Mathe P4, Englisch P5 erfüllen sie. 40 min: Git for Windows und Node.js (LTS) installieren, dann in PowerShell Claude Code (`irm https://claude.ai/install.ps1 \| iex`); mit `claude` anmelden; `/output-style learning` einschalten und Claude bitten, den Lernmodus in deinen Benutzereinstellungen einzutragen (Abschnitt 7). 5 min: Expo Go auf iPhone und iPad laden. 5 min: auf claude.ai unter Abrechnung nachsehen, wann Max endet, und danach auf Pro umstellen statt Max zu verlängern. | Prüfungsfächer geklärt, Claude Code läuft |
| Di 24.11. | 1 h | 5 min: dieses Repository auf GitHub auf privat stellen (Settings → General → Danger Zone → Change repository visibility → Private). 10 min: Mail an die ETH-Zulassungsstelle (Vorlage in Abschnitt 16), vorher aufschreiben, welche Fächer du in den Klassen 11–13 hattest. 45 min: Expo-Tutorial „Build with AI“ mit Claude Code. | Repository privat, Mail raus, erste App in Expo Go |
| Mi 25.11. | 1 h | Missing Semester: Shell (Teil 1). | Terminal-Grundlagen |
| Do 26.11. | 1 h | Gespräch mit deinen Eltern: Abschnitt 3 zeigen. Wer soll im App Store stehen, du oder ein Elternteil? Darf ihre Anschrift ins Impressum? Noch nichts entscheiden, nur verstehen. **Karte:** Hast du keine eigene Visa- oder Mastercard (Debit reicht, sie muss in US-Dollar zahlen können), beantragst du sie diese Woche bei deiner Bank zum Girokonto; sie kommt oft erst nach 1–2 Wochen. Du brauchst sie ab KW 53 für das Guthaben der Claude API und später für Apple (oder du meldest dich bei Apple über die Developer-App an). Für die ETH-Gebühr im Dezember geht notfalls die Karte deiner Eltern. | Fragen geklärt, Karte beantragt, Entscheidung im Januar |
| Fr 27.11. | 1 h | Missing Semester: Shell (Teil 2) und Git (Teil 1). | Terminal- und Git-Grundlagen |
| Sa 28.11. | 5 h | 2 h: Expo-Tutorial „StickerSmash“ mit Erklärungen von Claude. 2 h: Ideensuche mit Claude (Vorlage „Ideen“, Abschnitt 16): 10 Kandidaten, du wählst 3. 1 h: privates Repository `vorlage` auf GitHub, `CLAUDE.md` aus [`vorlagen/CLAUDE_md_fuer_die_app.md`](vorlagen/CLAUDE_md_fuer_die_app.md), [`vorlagen/checkliste_einreichung.md`](vorlagen/checkliste_einreichung.md) als `docs/checkliste-einreichung.md` kopieren, leere `docs/review-log.md` und `docs/entscheidungen.md` anlegen; solange Max noch läuft, legt Claude damit das leere Vorlagen-Projekt an. | 3 Ideen, Vorlage im Repository |
| So 29.11. | frei | – | – |

---

## 12. Woche für Woche bis 31.08.

### Phase 1 – Grundlagen und Idee (KW 49–51, 30.11.–20.12.), Schulwochen, 10 h (mit Klausuren 3 h)

- **Lernen (~5 h je Woche):**
  - Missing Semester (Git, Fehlersuche).
  - JavaScript und TypeScript lesen.
  - Expo- und EAS-Doku.
- **Idee ohne eigene Posts:** Claude recherchiert für deine 3 Ideen:
  - die Nachfrage: Wie viele Aufrufe haben Inhalte zum Thema? Verdienen
    Konkurrenz-Apps Geld?
  - drei Konkurrenten mit Preis;
  - das Risiko beim App Review.

  Eigene Markenkonten gibt es erst ab der Gründung, wegen des Impressums.
- **Ideen-Tor (So 20.12.):** eine Idee für App 1, die zweitbeste für App 2.
  Kriterien:
  - Menschen geben schon Geld dafür aus;
  - der „Magic Moment“ lässt sich ohne Gesicht zeigen;
  - keine Gesundheits-, Abnehm-, Dating- oder Finanzthemen;
  - Zielgruppe Erwachsene (keine Apps für Schüler, Lernen oder Hausaufgaben);
  - einfach zu bauen.
- **Verwaltung vorbereiten (~1 h):**
  - ELSTER-Benutzerkonto anlegen. Mit dem Online-Ausweis geht das sofort,
    sonst kommt ein Aktivierungsbrief, der bis zu zwei Wochen braucht.
  - Prüfen, ob du die PIN deines Personalausweises hast (AusweisApp auf dem
    iPhone).
  - Prüfen, wie deine Gemeinde die Gewerbeanmeldung online annimmt. Geht das
    nicht, buchst du jetzt einen Termin im Rathaus für Ende Januar, außerhalb
    einer Klausurwoche.
- **Bauen (~4 h je Woche):** eine Seite Beschreibung von App 1, dann in der
  Vorlage Eingabe oder Foto → Einwilligung → Ergebnis, zunächst mit einer
  Beispiel-Antwort in Expo Go.
- **Messpunkt M0 (So 20.12.):** Grundlagen zur Hälfte durch, Idee gewählt,
  erster Ablauf in Expo Go.

### KW 52 (21.–27.12.), ~9 h

- Mo/Di je 1 h, Mi 23.12. (erster Ferientag) 7 h: Bau weiter, ~2 h davon
  Lernen. 24.–27.12. frei.

### KW 53 (28.12.–03.01.), Weihnachtsferien, ~31 h (Neujahr frei)

- **ETH-Bewerbung (6 h):** Lebenslauf mit Claude nach der ETH-Vorlage,
  Zeugnisse der letzten drei Schuljahre scannen, Passfoto,
  Einverständniserklärung, Gebühr 150 CHF per Kreditkarte (privat, nicht aus
  dem App-Geld). **Abschicken.**
- **Lernen (~4 h).**
- **App 1 (~21 h):**
  - echte KI-Funktion: Supabase-Funktion mit Claude Haiku 5.5, Schlüssel nur
    als Geheimnis, Ausgabenlimit 50 $; dafür ein paar Dollar Prepaid-Guthaben
    in der Anthropic-Konsole mit deiner Karte;
  - Fehlerfälle: kein Netz, KI lehnt ab, Limit erreicht;
  - Onboarding mit 5–8 Fragen;
  - Paywall als Vorschau in Expo Go.

### KW 01 (04.–10.01.), Ferien, ~38 h (der 06.01. ist in Niedersachsen kein Feiertag)

- **App 1:**
  - harte Paywall (kein Umschalter für eine Testphase), Wochen- und
    Monatsabo, „Käufe wiederherstellen“, Links zu Datenschutz und
    Nutzungsbedingungen;
  - Einwilligung vor dem ersten KI-Aufruf mit Nennung des Anbieters;
  - die Abo-Prüfung in der Server-Funktion.
- **Lernen (~4 h).**
- **Sobald App 1 etwa halb steht** (Kernfunktion läuft mit echter KI,
  Onboarding und Paywall stehen als Oberfläche): **Messpunkt M2,
  Rechtsform entscheiden und gründen** (Checkliste A, ~4 h).
  - **Wann das meist ist:** Im Modell steht App 1 bis 10.01. nur in einem
    Teil der Läufe halb. Gegründet wird im Median am 25.01., in 47 von
    100 Läufen erst im Februar oder später (KW 05 oder Q4).
  - **Apple vorher:** Steht schon fest, wer im App Store steht, kannst du dich
    vorher bei Apple anmelden. Development Build und TestFlight gehen dann
    schon jetzt; echte Sandbox-Käufe erst nach Paid Apps Agreement, Bank- und
    Steuerdaten.
- **Messpunkt M1 (Fr 08.01.):** ETH-Bewerbung abgeschickt, die KI-Funktion
  läuft in Expo Go.

### KW 02–04 (11.–31.01.), Schulwochen, 10 h (Q3-Ende, mit Klausuren 3 h)

- **Gründung**, falls noch nicht geschehen.
- **Lernen (~3 h je Woche)** bis Ende Januar, dann ist der Lernpfad durch.
- **Brief an die Krankenkasse**, sobald das Gewerbe angemeldet ist: Claude
  entwirft ihn (Vorlage in Abschnitt 16), du schickst ihn ab. Inhalt:
  - Schüler mit Gewerbe;
  - deine echten Stunden: Schulwochen 3–10, Q4 höchstens 7, Ferien bis 38,
    nach der Schule bis zum Studienbeginn bis ~50 je Woche;
  - erwarteter Gewinn unter 590 € im Monat, keine Angestellten;
  - Bitte um schriftliche Bestätigung.
- **Apple-Konto:**
  - Paid Apps Agreement, Bank- und Steuerdaten;
  - Händlerangaben für die EU mit Postfach oder Adresse, Zweitnummer und
    Projekt-E-Mail;
  - Small Business Program.
- **Geräte:** iPhone und iPad registrieren, Development Build, Sandbox-Kauf
  testen.
- **Website und Konten:** Website mit Impressum und Datenschutzerklärung,
  Markenkonten anlegen.
- **Fr 29.01. Halbjahreszeugnis:** Lade es in eApply nach, falls die ETH es
  verlangt.

### KW 05 (01.–07.02.), Halbjahresferien Mo/Di, ~19 h

- Mo/Di je ~7 h, ab Mi 03.02. gilt die Q4-Regel (Sa 3 h, höchstens zweimal
  1–2 h).
- **Gründung**, falls M2 jetzt erreicht ist (Checkliste A).
- App 1: Tests nach Checkliste C; TestFlight nur mit aktivem Apple-Konto, mit
  Testern aus der Familie; Fehler beheben.
- **Einreichen, sobald die Checkliste steht**, mit „Diese Version manuell
  veröffentlichen“ (Abschnitt 4). Abo-Gruppe und Abos zusammen mit dieser
  Version einreichen.
- Erste Slideshows auf dem Markenkonto, noch ohne App-Link.

### KW 06–10 (08.02.–14.03.), Q4, höchstens 6–7 h

- **Ist App 1 eingereicht:** auf das Review reagieren. Den Grund jeder
  Ablehnung schreibst du in `docs/review-log.md`, Claude schlägt die kleinste
  Lösung vor. Rechne mit 1–2 Ablehnungen bei der ersten App; 90 % der Prüfungen
  sind in 48 Stunden fertig.
- **Ist sie bis Sa 13.03. freigegeben:** selbst veröffentlichen und starten,
  mit höchstens 3 Slideshows je Woche. Sonst bleibt sie dank der beim
  Einreichen gewählten Freigabe „manuell“ bis nach deiner letzten Prüfung
  liegen.
- **Signal in Q4:** Fällt die Signal-Prüfung (drei Wochen nach dem Start) noch
  vor den 15.03., darfst du Creator buchen (1–2 h). Fällt sie in die
  Startpause, buchst du erst nach deiner letzten Prüfung.
- **Gründung**, falls M2 erst jetzt erreicht ist (Checkliste A, ~4 h auf zwei
  Samstage verteilt).
- **Ist App 1 noch nicht eingereicht:** im Rahmen der Q4-Stunden weiterbauen,
  ohne Druck. Im Modell ist sie bis 14.03. nur in ~26 von 100 Läufen
  fertig, und das ist kein Fehler.
- **Messpunkt M3 (So 14.03.):** Ist App 1 gestartet, freigegeben oder noch im
  Bau? Davon hängt ab, was du nach dem Abitur tust.
- **ETH-Antwort (etwa Anfang März):** lesen und ablegen; bei Fragen an die
  Zulassungsstelle wenden.

### KW 11–22 (15.03.–06.06.), Ende Q4 und Abitur, 0–5 h

- **Deine Prüfungstage:** Mathe Mi 05.05., Chemie Do 13.05., Englisch (P5)
  am Termin deiner Schule zwischen 19.05. und 07.06., dazu P1 und P3. Ab einer
  Woche vor jedem dieser Tage gar nichts an der App.
- **In den 0–5 Stunden** (im schriftlichen Abitur 0–1): Zahlen, Notfälle
  (Tabelle in Abschnitt 18) und kleine Bau-Schritte ohne Termindruck, nie an
  Prüfungstagen und nie am Tag davor. Eine fertige App darfst du einreichen,
  Ablehnungen beantwortest du in diesen Stunden oder nach der letzten Prüfung.
  Keine Posts, keine Creator.
- Läuft App 1 schon: zweimal je Woche 20 Minuten Zahlen ansehen.
- **Support-Mails:** Du beschreibst Claude das Problem in eigenen Worten, ohne
  Namen, E-Mail-Adresse, Kaufdaten oder Fotos. Claude entwirft eine
  Antwortvorlage, die du selbst in dein Mailprogramm einsetzt.
- **Signal-Prüfung bei einer schon laufenden App:** drei Wochen nach dem Start.
  Liegt sie über 300 $ MRR, buchst du die Creator erst nach deiner letzten
  Prüfung.

### KW 23–26 (07.06.–04.07.), nach dem Abitur, 15–40 h

- **App 1 starten**, frühestens am Tag nach deiner letzten Prüfung
  (veröffentlichen oder fertig bauen und einreichen). Täglich 1–3 Slideshows.
- **Signal-Prüfung** drei Wochen nach dem Start: ≥ 300 $ MRR → Creator buchen
  (Checkliste F, für alle Apps zusammen bis 18.07. höchstens 750 €); sonst nur
  eigene Videos weiter. Startet App 1 erst Ende Juni, kommen die
  Creator-Videos meist erst nach Tor 1.
- **App 2** (die zweitbeste Idee) aus derselben Vorlage, mit anderer
  Kernfunktion. Reine Varianten lehnt Apple ab.
- **Bis 15.07.:** Bewerbung an der Leibniz Universität Hannover (~2 h).
- **01.–03.07.:** Abiturzeugnis in eApply hochladen, Original an die ETH.

### KW 27–29 (05.–25.07.), Sommer, ~55 h (davon ~6 h für Zürich)

- Tests nach der Signalregel, App 2 fertig, eingereicht und gestartet. Bleibt
  Zeit, beginnt App 3 (die drittbeste Idee); im Modell startet in gut der
  Hälfte der Läufe noch eine dritte App.
- Zimmer in Zürich suchen (WOKO braucht die Zulassung), Finanzierungsbrief
  der Eltern.
- **Tor 1 (So 18.07.):** Abschnitt 13.

### KW 30–35 (26.07.–31.08.), Sommer, ~55 h

- Weg A, B oder C (Abschnitt 14). Apps, die am 18.07. schon eingereicht
  waren, erscheinen jetzt noch, ohne Creator-Geld.
- Abschluss vor dem Umzug (Checkliste H).
- Endet die Jagd am 18.07., gehört die frei gewordene Zeit der
  ETH-Vorbereitung: Mathe nach den Empfehlungen der ETH (Folgen und Reihen,
  Induktion, komplexe Zahlen, Analysis, Vektorgeometrie), Java-Tutorial der
  ETH, CS50x.

---

## 13. Die Messpunkte und was du dann tust

| Messpunkt | Frage | Ja | Nein |
|---|---|---|---|
| **M0** So 20.12. | Grundlagen zur Hälfte, Idee gewählt, Ablauf in Expo Go? | weiter | Lernpfad in den Ferien fertig, Idee bis 28.12. |
| **M1** Fr 08.01. | ETH-Bewerbung abgeschickt? KI-Funktion läuft in Expo Go? | weiter | ETH-Bewerbung hat Vorrang, App danach |
| **M2** App 1 halb fertig (Kriterien in KW 01; im Median am 25.01.) | Rechtsform entschieden? | gründen (Checkliste A) | ohne Gründung kein Start: weiterbauen, Entscheidung bis spätestens 07.06. |
| **M3** So 14.03. | App 1 freigegeben? | gestartet bzw. zurückgehalten bis nach der letzten Prüfung | Pause bis nach der letzten Prüfung, dann fertig bauen |
| **Signal** 3 Wochen nach jedem Start | ≥ 300 $ MRR ohne bezahlte Werbung? Fällt der Tag in die Startpause, gilt er nach deiner letzten Prüfung | Creator-Geld, für alle Apps zusammen bis 18.07. höchstens 750 € | nur eigene Videos, nächstes Format oder nächste App |
| **Tor 1** So 18.07. | eine App am Stichtag ≥ 5.000 $ MRR? | weiter (Weg B oder C) | **Weg A:** keine neue App, keine neuen Creator; schon eingereichte Apps dürfen noch erscheinen |
| **Tor 2** So 08.08. | ≥ 10.000 $? | Weg C | Weg B endet wie Weg A |
| **31.08.** | Abschluss vor dem Umzug erledigt? | Ende | Checkliste H bis zum Umzug |

**Welche Zahl gilt:**
- **Signal und Tore:** in RevenueCat die Kennzahl **MRR**, also der
  hochgerechnete Monatsumsatz der laufenden Abos, brutto vor Apples Anteil, in
  US-Dollar. Abgelesen wird am 21. Tag nach dem Start (Signal) bzw. am
  Stichtag (Tor 1 und Tor 2).
- **Familienversicherung:** Dafür zählt dagegen der Gewinn in Euro, nach
  Apples Anteil und allen Kosten.

500.000 € bis 31.08.2027 erreicht das Modell in keinem einzigen Lauf. Das ist
keine Frage des Einsatzes: Die Zeit nach dem Abitur ist zu kurz, damit eine
App so weit wachsen kann.

---

## 14. Ab Juli: drei Wege

### Weg A – kein Treffer (~99 von 100 Läufen)

- Ab 19.07. beginnst du keine neue App und buchst keine neuen Creator.
  Apps, die am 18.07. schon fertig gebaut oder eingereicht sind, dürfen noch
  erscheinen (im Modell startet in ~84 von 100 Läufen danach noch eine
  App, meist App 2 um den 19.07., oft eine App 3 um den 26.07.). Auf solchen
  späten Starts beruhen ~3 von 10 Gewinnläufen.
- Die Apps laufen ohne Budget weiter (zweimal je Woche 20 Minuten Zahlen und
  Support), eigene Slideshows nur, wenn du Lust hast. Die übrige Zeit gehört
  der ETH-Vorbereitung (Abschnitt 7) und der Erholung vor dem Umzug.
- **Vor dem Umzug entscheiden** (Checkliste H):
  - **Einstellen:** zuerst die Abos aus dem Verkauf nehmen und den Server bis
    zum Ende der letzten bezahlten Laufzeit weiterbetreiben. Mit Wochen- und
    Monatsabos ist das in ein paar Wochen vorbei. Dann die App entfernen und
    das Gewerbe abmelden (0–32,50 €).
  - **Verkaufen:** eine kleine App lässt sich mit Umsatzzahlen auf
    Marktplätzen anbieten; die App wird zu einem anderen Apple-Konto
    übertragen.
  - **Weiterlaufen lassen:** nur nach einer Beratung zu Deutschland und der
    Schweiz. Mit Gewerbe in Zürich kommen eine Anmeldung bei der SVA,
    Schweizer Steuern und AHV-Beiträge hinzu, und dein Einkommen hebt die
    Befreiung von der Schweizer Krankenversicherung auf.
- Die letzte EÜR und Einkommensteuererklärung 2027 gibst du 2028 per ELSTER
  ab, auch aus Zürich.

### Weg B – Tor 1 bestanden, Tor 2 verfehlt (~0,3 von 100)

- Bis 08.08. Creator nur aus dem Umsatz der letzten vier Wochen, abzüglich
  der Creator, die schon daraus bezahlt sind; jede Woche ein Paywall-Test.
- Danach wie Weg A, aber Verkaufen ist hier oft die beste Wahl, weil die App
  messbaren Umsatz hat.
- Achte auf die Familienversicherung (Gewinn über ~590 € im Monat) und melde
  Gewinne der Krankenkasse.

### Weg C – ein echter Treffer (~0,2 von 100)

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
      besprochen
- [ ] Erstberatung bei einem Steuerberater (Festpreis anfragen):
      Kleinunternehmerregelung oder Verzicht? Bei reinem App-Store-Vertrieb
      zählen die Apple-Erlöse in Deutschland nicht, aber Leistungen aus dem
      Ausland (Claude API, Supabase, Werbung) kosten Kleinunternehmer 19 %
      Umsatzsteuer, die sie nicht zurückbekommen
- [ ] Gewerbe online bei deiner Gemeinde anmelden (~20–65 €), Tätigkeit z. B.
      „Entwicklung und Vertrieb von Software-Apps“
- [ ] Fragebogen zur steuerlichen Erfassung in ELSTER
- [ ] Zweitnummer, Projekt-E-Mail, Domain, Website mit Impressum und
      Datenschutzerklärung
- [ ] Apple Developer Program als Einzelperson (99 $; eigene Kreditkarte oder
      Anmeldung über die Apple-Developer-App; Zwei-Faktor-Anmeldung), falls
      nicht schon vorher angemeldet
- [ ] Brief an die Krankenkasse abgeschickt, Antwort abgelegt
- [ ] Ordner für Belege (Claude sortiert, du legst ab)
- [ ] Du weißt, welche Post nach der Anmeldung echt ist (Abschnitt 18,
      „Formularfallen“)

### B – Apple (nach der Anmeldung)

- [ ] Paid Apps Agreement, Bankverbindung, Steuerformular
- [ ] EU-Händlerangaben: Adresse oder Postfach mit Nachweis, Zweitnummer,
      E-Mail
- [ ] Small Business Program beantragt (15 % statt 30 %)
- [ ] iPhone und iPad registriert, Entwicklermodus an

### C – Vor jeder Einreichung

- [ ] Kernfunktion läuft auf iPhone **und iPad**, auch ohne Netz (Meldung
      statt Absturz)
- [ ] Einwilligung vor dem ersten KI-Aufruf mit Nennung des Anbieters
      (5.1.2(i))
- [ ] Harte Paywall ohne Umschalter, Preis deutlicher als jede Testphase,
      Laufzeit, Verlängerung und Kündigung genannt (3.1.2)
- [ ] „Käufe wiederherstellen“ (3.1.1)
- [ ] Links zu Datenschutzerklärung und Nutzungsbedingungen in der App und in
      App Store Connect
- [ ] Abo-Gruppe und Abos zusammen mit dieser Version eingereicht
- [ ] Impressum in der App erreichbar (z. B. in den Einstellungen)
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
      RevenueCat und dem Anbieter von Website und E-Mail
- [ ] Fotos werden nach der Analyse nicht gespeichert
- [ ] Eigene Messereignisse nur mit Einwilligung (§ 25 TDDDG)
- [ ] Keine Gesundheitsdaten (Art. 9 DSGVO) erheben
- [ ] Datenschutzerklärung nennt alle Dienste und dich als Verantwortlichen
- [ ] Ein KI-Support wäre als KI erkennbar (KI-Verordnung Art. 50)

### E – Videos ohne Gesicht

- [ ] Markenkonto klar als App erkennbar, Impressum-Link im Profil
- [ ] TikTok: Schalter „Your brand“, nur Commercial Music Library
- [ ] Keine erfundenen Erfahrungen, keine KI-Personen als „Nutzer“
- [ ] Realistische KI-Bilder gekennzeichnet
- [ ] Jedes Bild selbst fotografiert, aus den Gratisinhalten von Canva oder
      von Unsplash/Pexels (Lizenz geprüft) oder KI-erzeugt; nie aus Pinterest,
      der Google-Bildersuche oder fremden Posts
- [ ] Je Post notieren: Format, Hook, Bildquelle, Aufrufe nach 48 h

### F – Creator (nur nach Signal)

- [ ] Signal erreicht (≥ 300 $ MRR in RevenueCat drei Wochen nach dem Start)
- [ ] Anfrage persönlich und einzeln, mit Link auf kurze
      Datenschutzhinweise für Creator (Art. 14 DSGVO)
- [ ] Vertrag in Textform: Video, Termin, Freigabe, Kennzeichnung „Werbung“
      plus „Paid partnership“, Honorar, Zahlung **nach** dem Posten (über eine
      Plattform mit Treuhandkonto: Freigabe erst nach dem Posten),
      Nutzungsrechte nur für den Post
- [ ] Keine Spark-Ads-Rechte von Creatorn im Ausland, bevor § 50a EStG geklärt
      ist
- [ ] Honorare an selbstständige Privatpersonen mitschreiben (über 1.000 € im
      Jahr: Künstlersozialabgabe 5,0 %)
- [ ] Kennzeichnung nach dem Posten selbst geprüft

### G – Kennzahlen je App und Woche

Aufrufe, Downloads, Testphasen, Käufe, Umsatz (USD), Erstattungen,
Creator-Kosten, Umsatz je 1.000 Aufrufe, Monatsgewinn (für die
Familienversicherung). Vorlage: [`vorlagen/kennzahlen.csv`](vorlagen/kennzahlen.csv).

### H – Abschluss vor dem Umzug (bis 31.08.)

- [ ] Entscheidung je App: einstellen, verkaufen oder mit Beratung
      weiterführen
- [ ] Einstellen: zuerst die Abos aus dem Verkauf nehmen; Abonnenten
      mindestens 31 Tage vorher informieren; Server bis zum Ende der letzten
      bezahlten Laufzeit betreiben; dann App entfernen und Server abschalten
- [ ] Werkzeuge kündigen bzw. zum Laufzeitende beenden: Claude Pro, Supabase,
      EAS (falls bezahlt), Domain und E-Mail, Prepaid-Zweitnummer; in der
      Anthropic-Konsole automatisches Aufladen aus
- [ ] Apple-Mitgliedschaft: automatische Verlängerung ausschalten (sonst wieder
      99 $), erst wenn keine App mehr verkauft werden soll; mit dem Ablauf
      verschwinden die Apps aus dem Store
- [ ] Gewerbe abmelden (0–32,50 €), falls nichts weiterläuft
- [ ] Belege vollständig für die EÜR 2027
- [ ] Krankenkasse über das Ende des Gewerbes informieren und schriftlich
      klären, ob die Familienversicherung (und damit die Europäische
      Krankenversicherungskarte für die Befreiung in Zürich) beim Studium in
      der Schweiz bestehen bleibt
- [ ] Review-Log, Vorlage und Zahlen aufheben

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

**Ideen (KW 48)**
```
Suche 10 Ideen für eine iPhone-Abo-App mit einer KI-Funktion. Bedingungen:
Menschen geben dafür schon Geld aus; der Moment, in dem die App beeindruckt,
lässt sich ohne Gesicht zeigen (Bildschirmaufnahme oder Slideshow); keine
Gesundheit, kein Abnehmen, keine Finanzen, kein Dating, keine Diagnose; keine
Kopie einer bekannten App; Zielgruppe Erwachsene (keine Apps für Schüler,
Lernen oder Hausaufgaben); mit Claude Code für einen Anfänger in ~150 Stunden
baubar; keine Nutzerkonten nötig. Für jede Idee: Zielgruppe, Kernfunktion,
Magic Moment, drei Konkurrenten mit Preis, Risiko beim App Review, Aufwand.
Am Ende eine Rangliste mit Begründung.
```

**Slideshows (ab der Gründung)**
```
App: [Name], Zielgruppe: [wer]. Schreibe 10 Hooks für die erste Folie einer
TikTok-Slideshow (höchstens 8 Wörter) und für die besten 3 je 5 weitere
Folientexte, letzte Folie mit Hinweis auf die App. Keine erfundenen
Erfahrungen, keine Versprechen, keine KI-Personen. Schlag zu jeder Folie ein
Bildmotiv ohne Personen vor und sag, ob ich es selbst fotografieren kann oder
in den Gratisinhalten von Canva finde.
```

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
Nische: [Nische]. Erstelle eine Liste von 20 Creatorn mit 1.000–10.000
Followern, die regelmäßig zu diesem Thema posten (Profil, typische Aufrufe,
veröffentlichte Geschäftsadresse, falls vorhanden). Schreibe für jeden einen
kurzen, persönlichen Anfrage-Entwurf, der sich auf ein konkretes Video
bezieht, mit dem Link auf unsere Datenschutzhinweise für Creator. Ich
schicke jede Anfrage selbst und einzeln.
```

**Wochenauswertung (sonntags)**
```
Hier sind die Zahlen der Woche: [Tabelle]. Berechne Umsatz je 1.000 Aufrufe,
Download → Zahler, Testphase → Zahler, Erstattungen und den Monatsgewinn.
Vergleiche mit Signal (300 $), Tor 1 (5.000 $) und der Grenze der
Familienversicherung (590 €). Was sind die drei Dinge, die nächste Woche am
meisten bringen?
```

---

## 17. Geld: Stufen, Budget, Kassenregeln

**Ausgaben in Stufen** – jede Stufe erst, wenn die vorige erreicht ist:

| Stufe | wann | was | Kosten |
|---|---|---|---|
| 0 | KW 48 bis zur Gründung | Claude Max (bezahlt), dann Pro; ab KW 53 ein paar Dollar Guthaben für die Claude API | ~21 € im Monat, bis Ende Januar ~40–70 € |
| 1 | Gründung (im Median am 25.01.) | Gewerbe, Apple, Erstberatung beim Steuerberater, Domain, Zweitnummer | ~150–450 € einmalig |
| 2 | ab der Gründung | Claude Pro, Domain und E-Mail, Zweitnummer, ab dem Start Supabase Pro (25 $), KI-API nach Nutzung, ggf. EAS | ~35–110 € im Monat |
| 3 | nur nach Signal | Creator | für alle Apps zusammen bis 18.07. höchstens 750 € (mit Plattformgebühr), danach nur aus dem Umsatz der letzten vier Wochen |
| 4 | nach dem 31.08. | Abmeldung, EÜR und Einkommensteuererklärung 2027 (selbst über ELSTER oder mit Steuerberater) | 0–800 € |
| – | nur wenn der Gewinn über ~590 € im Monat liegt | eigene Kranken- und Pflegeversicherung | ~280 € im Monat |

**Was im Modell herauskommt** (alles bis zum Schluss eingerechnet):
- Median −1.136 €, im Mittel −952 €;
- in 9 von 10 Läufen höchstens 1.512 € Verlust;
- mehr als 5.000 € Verlust in keinem Lauf.

Creator-Geld fließt im Modell nur in 5 von 100 Läufen, im Schnitt aller Läufe ~33 €.

**Kassenregeln**
- Jeden Sonntag: Kontostand, offene Rechnungen, erwartete Zahlungen von Apple
  (5–9 Wochen nach dem Kauf), Monatsgewinn.
- Vor jeder Ausgabe über 50 €: Bleiben Pflichtkosten bis 31.08. und ~800 € für
  den Abschluss gedeckt?
- Creator direkt erst nach dem Posten bezahlen; über eine Plattform mit
  Treuhandkonto die Zahlung erst nach dem Posten freigeben. Nie im Voraus für
  Wochen.
- Ein eigenes Konto für die App, damit Belege und Umsatzsteuer sauber bleiben.
  Ein Girokonto auf deinen Namen genügt.

---

## 18. Wenn etwas schiefgeht

| Problem | was du tust |
|---|---|
| Du kommst mit den Grundlagen nicht voran | Lernmodus, kleinere Schritte, ein Thema je Woche; im Zweifel App 1 noch kleiner schneiden |
| App 1 ist am 14.03. nicht fertig | normal (in ~3 von 4 Läufen): im Abitur nur kleine Schritte, nach der letzten Prüfung in zwei bis drei Wochen fertig |
| Apple lehnt ab | Grund ins Review-Log, kleinste Änderung, neu einreichen; Ablehnungen bei der ersten App sind normal |
| Videos bekommen kaum Aufrufe | anderes Format, nicht mehr Videos desselben Formats; nach 15–20 Posts ohne Signal ein neues Format |
| Claude läuft im Kreis | Sitzung beenden, erst erklären lassen, dann ein kleineres Ziel |
| Pro-Limit bremst in den Ferien | einen Monat Max oder Usage Credits, danach zurück |
| Kosten der KI-Funktion steigen | Bild kleiner, Antworten kürzer, Tageslimit je App-User-ID senken, prüfen, ob Aufrufe ohne Abo durchkommen; Ausgabenlimit mit der Zahl der Zahler anheben |
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
und gegebenenfalls eigener Krankenversicherung (vor Einkommensteuer; bis
~12.500 € Jahresgewinn fällt keine an).

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

So liest du die Tabelle:
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

**Videos ohne Gesicht und Creator**
- Fallbeispiele: <https://www.socialgrowthengineers.com/how-to-go-viral-without-knowing-how-to-go-viral>, <https://shortimize.com/blog/20k-downloads-and-9k-mrr-in-78-days-how-this-indie-app-turned-minimalism-into-millions-of-views>
- TikTok Creator-Anzeigen: <https://ads.tiktok.com/business/en/blog/tiktok-creator-advantage>
- UGC-Preise: <https://www.netinfluencer.com/collabstr-report-tiktok-campaigns-plummet-as-brands-pivot-to-ugc/>, <https://influee.co/ugc-creator/countries/germany>
- TikTok-Regeln: <https://www.tiktok.com/community-guidelines/en/integrity-authenticity/>, <https://www.tiktok.com/legal/page/global/bc-policy/en>, <https://ads.tiktok.com/help/article/commercial-music-library>
- UWG-Anhang: <https://dejure.org/gesetze/UWG/Anhang.html>; KI-Verordnung Art. 50: <https://artificialintelligenceact.eu/article/50/>
