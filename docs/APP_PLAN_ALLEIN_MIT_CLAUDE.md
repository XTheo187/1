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
> | Zeit bis 31.08. | **~760 Stunden**, davon ~200 bis zum Ende des Abiturs (10 je Schulwoche, ~31–38 je Ferienwoche, 3–7 in Q4, 0–5 im Abitur, ab Juni 15–55) |
> | App 1 fertig | im Median am 07.06.; bis 14.03. in 26 von 100 Läufen, sonst meist erst nach dem Abitur |
> | App 1 im App Store | im Median ab 21.06. |
> | Geld bis zum Schluss (einschließlich Abmeldung und Steuererklärung) | im Median **−1.095 €**, im Mittel −744 €, nie mehr als 5.000 € |
> | überhaupt ein Gewinn | in **10 von 100** Läufen, meist nur wenig; die besten 1 % der Läufe enden ab +5.110 € |
> | 10.000 € oder mehr | in 0,39 von 100 Läufen (etwa 4 von 1.000) |
> | 500.000 € bis 31.08.2027 | **in keinem** von 300.000 Läufen |
>
> Das ist ehrlich gesagt ein **Lernprojekt mit kleiner Gewinnchance**, kein
> Weg zu 500.000 €. Es kostet dich im Normalfall rund 1.095 € und ~760
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
   App 1 mit Claude in Expo Go, ganz ohne Firma. Ausgaben: nur Claude Pro
   (~21 € im Monat).
2. **Gegründet wird erst, wenn App 1 halb steht** (im Modell im Median am
   25.01.), und zwar als **Einzelunternehmen**. Eine UG frisst dein ganzes
   Geld (Abschnitt 3).
3. **Ganz anonym geht es nicht.** Ohne Gesicht und ohne Stimme geht es. Aber
   als Verkäufer im App Store steht der Name einer echten Person, deiner
   oder der eines Elternteils.
4. **Abitur und ETH gehen vor.** In Q4 arbeitest du höchstens 6–7 Stunden je
   Woche an der App, im Abitur fast gar nicht, und zwischen 15.03. und 06.06.
   startet keine App. Die ETH-Bewerbung schickst du in den Weihnachtsferien ab.
5. **Geld für Creator nur nach einem Signal.** Erst wenn eine App drei Wochen
   nach dem Start ohne bezahlte Werbung mindestens 300 $ Monatsumsatz macht,
   bekommt sie bis zu 750 €. Das ist im Modell die beste Regel (Abschnitt 20).
6. **Am 18.07. entscheidet eine Zahl.** Liegt keine App über 5.000 $
   Monatsumsatz, endet die Jagd. Vor dem Umzug nach Zürich meldest du das
   Gewerbe ab oder klärst mit einem Steuerberater, wie es weitergeht.

---

## 3. Die eine große Entscheidung: Rechtsform und Anonymität

Du entscheidest das, sobald App 1 etwa halb fertig ist, voraussichtlich
zwischen Mitte und Ende Januar. Bis dahin brauchst du keine Firma: Bauen und
Testen in Expo Go geht ohne. Für echte Käufe, TestFlight und den App Store
brauchst du ein Apple-Konto, und das setzt voraus, dass jemand die App
gewerblich anbietet.

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
| passt in 5.000 € | ja | **nein:** in 92 von 100 Läufen lassen Pflichtkosten und Auflösung gar keine Gründung zu | **nein:** in 99 von 100 Läufen keine Gründung |
| überhaupt ein Gewinn | 10 von 100 | 0,06 von 100 | 0 von 100 |
| Geld im Median | −1.095 € | −375 € (nur Claude, weil meist gar nicht gegründet wird und dann auch keine App erscheint) | −357 € (ebenso) |
| vor dem Umzug sauber beenden | ja, Abmeldung an einem Tag | nein: wegen des Sperrjahrs läuft die Auflösung, während du in Zürich lebst; führst du die UG von dort, wird sie auch in der Schweiz steuerpflichtig, und dir droht Wegzugsteuer auf die Anteile | wie links |

**Meine Empfehlung:** das **Einzelunternehmen**. Die UG versteckt deinen
Namen nur halb: im App Store ja, im Impressum und im Handelsregister nicht.
Dafür kostet sie fast dein ganzes Geld und lässt sich vor dem Umzug nicht
mehr beenden.

Ist dir dein Name im App Store zu viel, gibt es zwei ehrliche Wege:
- **Ein Elternteil meldet das Gewerbe an** und schließt den Apple-Vertrag;
  du arbeitest als Admin im Apple-Konto mit. Dann gehören App und Gewinn
  rechtlich dem Elternteil, es haftet unbeschränkt und versteuert den
  Gewinn. Geld, das es dir gibt, ist eine Schenkung (bis 400.000 € je
  Elternteil steuerfrei). Das geht nur, wenn das Elternteil es wirklich will
  und versteht. Ein „Strohmann“, hinter dem du nach außen die Firma führst,
  schützt keinen von euch.
- **Gar nicht veröffentlichen:** App 1 als Lernprojekt bauen, im Sommer mit
  einem Organisationskonto oder dem Elternteil entscheiden. Das kostet die
  meisten Chancen, weil dann der Sommer fehlt.

Was in jedem Fall geht, damit möglichst wenig von dir sichtbar wird:
- ein neutraler Markenname für die App;
- eine eigene Telefonnummer nur für die App, also eine Prepaid- oder
  Zweitnummer statt deiner Handynummer. Apple prüft sie mit einem Code.
- ein Postfach für die EU-Seite bei Apple (mit Nachweis);
- eine Projekt-E-Mail auf deiner Domain;
- Markenkonten ohne Gesicht und ohne Stimme.

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
| Weihnachtsferien Mi 23.12.–Sa 09.01. | 21.–27.12.: ~8; 28.12.–03.01.: ~31; 04.–09.01.: ~38 | Mo–Fr 9–12 und 14–17 Uhr, Sa 3 h; 24.–27.12. und 01.01. frei; dazu 1–1,5 h Schule am Tag |
| Halbjahresferien Mo 01.–Di 02.02. | ~22 in dieser Woche | zwei Ferientage für einen kurzen Bau-Block |
| Q4, Mi 03.02.–Do 18.03. | **höchstens 6–7**, in Wochen mit zwei oder mehr Klausuren nur Sa 3 h | Q4-Noten zählen fürs Abitur; keine neue Kampagne |
| 19.03.–05.04. (Ende Q4, Osterferien) | 0–5 | Abiturvorbereitung |
| schriftliches Abitur 06.04.–13.05. | 0–1, nur Notfälle | an Prüfungstagen und davor gar nichts |
| 5. Prüfungsfach und Nachschreibtermine 19.05.–07.06. | 0–5 | bei einer Präsentationsprüfung zwei Wochen gar nichts |
| 08.06.–04.07. | 15–40 | mögliche mündliche Nachprüfung 28.–30.06., Zeugnis 01.–03.07. |
| ab 05.07. | Mo–Sa ~9 h, So frei | davon ~6 h je Woche für Zürich (Zimmer, Unterlagen, Mathe) |

- **Kein App-Start zwischen 15.03. und 06.06.** Wird App 1 in Q4 von Apple
  freigegeben, stellst du in App Store Connect „Diese Version manuell
  veröffentlichen“ ein und veröffentlichst sie am 07.06.
- **Alles zählt in diese Stunden:** Lernen, Bauen, Prüfen, Videos,
  Behördenkram, Bewerbungen.
- Nie nach 22 Uhr an der App. Kein Prüfungstermin wird für die App geopfert.
- **Schule wird schlechter?** Sofort auf 3 Stunden je Woche, bis die Note
  wieder steht. Für die ETH zählen Mathe, die Naturwissenschaft und das
  Sprachfach (Abschnitt 9).

**Geld**
- **Insgesamt höchstens 5.000 €**, einschließlich der Abmeldung, der
  Steuererklärung 2027 und einer eigenen Krankenversicherung, falls dein
  Gewinn zu hoch wird. Das Geld für Zürich ist getrennt und wird nie
  angefasst.
- **Ausgaben in Stufen** (Abschnitt 17): bis zur Gründung nur Claude Pro,
  dann die Gründung, Creator-Geld erst nach einem Signal.
- Kein Kredit, kein Dispo, keine Ratenzahlung.
- Vor jeder Ausgabe über 50 €: Sind danach alle Pflichtkosten bis 31.08. und
  ~800 € für Abmeldung und Steuererklärung noch gedeckt?
- **Familienversicherung:** Gewinn im Monat unter ~590 € halten (Grenze
  2027, vorbehaltlich Bundesrat; 2026: 565 €). Gemeint ist Gewinn, also
  Einnahmen minus Kosten. Zeit für die App unter 20 Stunden je Woche im
  Schnitt, keine Angestellten.

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
| Grundlagen | erklärt im Lernmodus, stellt dir Übungen, lässt dich Stellen selbst schreiben | lernst ~25–40 Stunden bis Weihnachten; fragst nach, bis du es einem Mitschüler erklären kannst |
| Code: App, Paywall, KI-Funktion, Server | schreibt alles in kleinen Schritten, erklärt jeden Schritt, führt die `CLAUDE.md` und das Review-Log | beschreibst, was du willst; testest auf iPhone und iPad; prüfst mit den Checklisten; entscheidest |
| Sicherheit und Datenschutz | Entwürfe, Prüflisten, führt die Prüfungen aus | siehst dir jedes Ergebnis selbst an; verantwortest |
| App Store | Texte, Screenshot-Entwürfe, Antworten an das Review | reichst ein, gibst frei; Verträge, Bank- und Steuerdaten nur du (bzw. das Elternteil) |
| Ideen | Recherche, 10 Kandidaten mit Konkurrenz und Risiken | wählst 3, am Ende eine |
| Videos ohne Gesicht | Hooks, Folientexte, Bildideen, Skripte für Bildschirmaufnahmen, Auswertung | baust die Slideshows (10–20 min je Stück), nimmst Bildschirm und Hände auf, postest von Hand |
| Creator (nach Signal) | Suche, Entwürfe für persönliche Anfragen, Briefing, Vertragsvorlage | schreibst jede Anfrage einzeln, bezahlst nach dem Posten, prüfst die Kennzeichnung |
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
| Claude API (Haiku 5.5) | KI-Funktion der App, getrennt vom Abo | typisch ~30 $ je 1.000 aktive Nutzer im Monat; Ausgabenlimit in der Konsole | ab dem ersten Test mit echter KI |
| Apple Developer Program (Einzelperson) | Gerätetests mit echten Käufen, TestFlight, App Store | 99 $/Jahr, mit einer Karte auf deinen Namen; ohne D-U-N-S, Konto meist nach wenigen Tagen aktiv | bei der Gründung |
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

---

## 7. So arbeitest du mit Claude, ohne programmieren zu können

**Was die Forschung sagt:**
- **Bei Anfängern ist die Fehlersuche der Engpass.** In einer Studie gingen
  61 % der Anfragen an einen KI-Agenten in das Reparieren von Code, den der
  Agent selbst geschrieben hatte.
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

**Lernpfad (~25–40 Stunden, KW 48 bis Weihnachten)**
1. Expo-Tutorial „Build with AI“ (für Menschen ohne Programmierhintergrund,
   ~1 h, mit Claude Code, iPhone mit Expo Go).
2. Expo-Standard-Tutorial „StickerSmash“ (~2 h).
3. MIT „Missing Semester“ 2026: Shell, Git, Fehlersuche (~6–10 h mit
   Übungen).
4. JavaScript und TypeScript lesen lernen, nicht schreiben (~10–20 h, z. B. die
   ersten Abschnitte von freeCodeCamp).
5. Expo- und EAS-Doku zu Development Builds und `eas submit` (~3–5 h).
6. Fehlermeldungen lesen üben, an deinen eigenen echten Fehlern.

CS50x (10–20 Stunden je Woche) machst du erst nach dem Abitur, als
Vorbereitung auf die ETH.

**Lernmodus:** In Claude Code `/output-style learning` einschalten. Claude
erklärt dann seine Entscheidungen und lässt dich an wichtigen Stellen selbst
schreiben (`TODO(human)`). Für reine Erklärungen gibt es `/output-style explanatory`.

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
  Unter 1.000 TikTok-Followern schreibst du die Adresse als Text in die Bio.
- **Format testen:** viele Varianten eines Formats, Hook in der ersten Sekunde
  bzw. auf der ersten Folie. Claude liefert je Tag 10 Hook-Varianten und die
  Folientexte, du baust die Slideshow in Canva (10–20 Minuten) und postest
  von Hand vom iPhone.
- **Menge:** in Q4 höchstens 3 je Woche auf Vorrat; ab dem Start 1–3 am Tag.
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
Werbung mindestens 300 $ Monatsumsatz, bekommt sie bis zu 750 € für Creator.
Die zeigen sich selbst, du nicht.
- **Preise:** UGC-Videos in Deutschland im Schnitt ~83 $ je 30 Sekunden
  (Influee), auf dem US-Markt ~150–200 $ (Collabstr).
- **Wo buchen:** TikTok One verlangt kein Mindestbudget, Collabstr nimmt eine
  Gebühr je Auftrag. Insense (650 $ Testmonat) und Billo (ab 1.000 $ Paket)
  binden zu viel Geld.
- **Lieferzeit:** 1–2 Wochen.
- **Rechte:** Nutzungsrechte oder Spark Ads kosten meist 30–50 % extra.

---

## 9. ETH Zürich und Rückfall

**Zulassung ohne Prüfung mit deutschem Abitur** (ETH, Studienjahr 2026/27;
Änderungen erst ab Herbst 2028):
- **Fächer:** Mathematik, eine Naturwissenschaft (Physik, Chemie oder
  Biologie) und Deutsch oder eine Fremdsprache müssen in den letzten zwei
  Jahren unterrichtet worden **und Prüfungsfächer deines Abiturs** sein.
- **Note:** Der Schnitt dieser drei Prüfungsfächer muss mindestens 70 % des
  Höchstwerts erreichen, rechnerisch ~10,5 Punkte. Ob die ETH nur die
  Prüfungsergebnisse zählt, sagt sie nicht; frag bei zulassungsstelle@ethz.ch
  nach.
- **Breite:** Vier weitere Fächer aus Physik, Chemie, Biologie, Informatik,
  weiterer Sprache, Geografie, Geschichte und Wirtschaft müssen in den
  letzten drei Jahren unterrichtet worden sein.
- **Gesamtnote:** Eine Mindest-Abiturnote gibt es nicht.
- **Sonst:** Fehlt etwas, bleibt nur die Aufnahmeprüfung im Januar 2028 mit
  Studienbeginn im September 2028. Das kostet ein Jahr.
- **Programmieren** ist keine Voraussetzung. Im ersten Jahr wird Java
  unterrichtet.

**Was das für den Plan heißt:**
- Am Dienstag prüfst du deine fünf Prüfungsfächer (P1–P4 schriftlich, P5
  mündlich) gegen diese Bedingung.
- Mathe, die Naturwissenschaft und das Sprachfach haben im Abitur Vorrang vor
  allem in diesem Plan.

**Bewerbung**

| Schritt | Termin | Aufwand |
|---|---|---|
| eApply ist offen | 01.12.2026–31.03.2027, danach geht nichts mehr | – |
| Bewerbung abschicken: Passfoto, Ausweis, Lebenslauf (Vorlage der ETH), Einverständniserklärung, Zeugnisse der letzten drei Schuljahre als PDF, Gebühr 150 CHF | **in den Weihnachtsferien (KW 53)** | ~6 h |
| Antwort | ~8 Wochen nach Eingang, also etwa Anfang März | – |
| Abiturzeugnis hochladen, Original per Post | sofort nach der Ausgabe 01.–03.07., spätestens 31.08. | ~1 h |
| Studienbeginn | 20.09.2027 | – |

**Zürich kostet** laut ETH für internationale Studierende ~28.100 CHF im
Jahr:
- **Schulgeld und Beiträge:** 2.264 CHF je Semester.
- **Zimmer:** ~800–1.000 CHF im Monat, bei WOKO ab ~400 CHF.
- **Vor dem Einzug:** bis zu drei Monatsmieten Kaution plus die erste Miete.
- **Aufenthaltsbewilligung B:** innerhalb von 14 Tagen nach der Ankunft
  beantragen. Dafür brauchst du einen Finanzierungsnachweis über 21.000 CHF;
  ein Brief deiner Eltern über 1.750 CHF im Monat reicht.
- **Krankenversicherung:** Mit der Europäischen Krankenversicherungskarte
  innerhalb von drei Monaten die Befreiung beantragen. **Jedes Einkommen in
  der Schweiz hebt sie auf**; als Deutscher kannst du dann eine Ausnahme
  beantragen.

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
| Mo–Fr (ohne Feiertage) | 9–12 und 14–17 Uhr | Bau-Sitzungen, Tests auf iPhone und iPad, Store-Eintrag |
| Sa | 3 h | Wochenauswertung, Lernen |
| täglich | 1–1,5 h | Schule |

**Q4-Woche (höchstens 6–7 Stunden):** Mo–Fr frei, Sa 3 h, dazu höchstens
zweimal 1–2 h; mit zwei oder mehr Klausuren nur der Samstag.

**Abiturzeit (0–5 Stunden):** nur Zahlen ansehen und Notfälle. Ist eine App
schon gestartet: zweimal 20 Minuten je Woche.

**Sommerwoche ab 05.07. (~55 Stunden):** Mo–Sa 9–12, 13–17 und 18–20 Uhr,
So frei; davon ~6 Stunden für Zürich.

---

## 11. Diese Woche Tag für Tag (KW 48)

Di 24.11. bis So 29.11.2026, Schulwoche. Kosten diese Woche: 0 €, Max ist
schon bezahlt.

**Ziel der Woche:**
- Claude Code läuft unter Windows.
- Das erste Expo-Projekt läuft auf deinem iPhone.
- Deine Prüfungsfächer sind gegen die ETH-Bedingung geprüft.
- Drei Ideen sind gewählt.

| Tag | Zeit | was | Ergebnis |
|---|---|---|---|
| Di 24.11. | 1 h | 10 min: deine Prüfungsfächer P1–P5 gegen die ETH-Bedingung prüfen (Abschnitt 9). Ist eine Bedingung nicht erfüllt, sag es mir, dann planen wir die Aufnahmeprüfung oder den Rückfall. 50 min: in PowerShell Claude Code installieren (`irm https://claude.ai/install.ps1 \| iex`), dazu Git for Windows und Node.js (LTS); mit `claude` anmelden; `/output-style learning` einschalten. Das Max-Abo nicht verlängern, sondern zum Ende auf Pro umstellen. | Prüfungsfächer geklärt, Claude Code läuft |
| Mi 25.11. | 1 h | Expo-Tutorial „Build with AI“ mit Claude Code; Expo Go auf iPhone und iPad. | erste App in Expo Go |
| Do 26.11. | 1 h | Gespräch mit deinen Eltern: Abschnitt 3 zeigen. Wer soll im App Store stehen, du oder ein Elternteil? Darf ihre Anschrift ins Impressum? Noch nichts entscheiden, nur verstehen. | Fragen geklärt, Entscheidung im Januar |
| Fr 27.11. | 1 h | Missing Semester: Shell (Teil 1). | Terminal-Grundlagen |
| Sa 28.11. | 5 h | 2 h: Expo-Tutorial „StickerSmash“ mit Erklärungen von Claude. 2 h: Ideensuche mit Claude (Vorlage „Ideen“, Abschnitt 16): 10 Kandidaten, du wählst 3. 1 h: GitHub-Konto, privates Repository `vorlage`, `CLAUDE.md` aus [`vorlagen/CLAUDE_md_fuer_die_app.md`](vorlagen/CLAUDE_md_fuer_die_app.md); solange Max noch läuft, legt Claude damit das leere Vorlagen-Projekt an. | 3 Ideen, Vorlage im Repository |
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
  - keine Gesundheits-, Abnehm- oder Finanzthemen;
  - einfach zu bauen.
- **Bauen (~4 h je Woche):** eine Seite Beschreibung von App 1, dann in der
  Vorlage Eingabe oder Foto → Einwilligung → Ergebnis, zunächst mit einer
  Beispiel-Antwort in Expo Go.
- **Messpunkt M0 (So 20.12.):** Grundlagen zur Hälfte durch, Idee gewählt,
  erster Ablauf in Expo Go.

### KW 52 (21.–27.12.), ~8 h

- Mo/Di je 1 h, Mi 23.12. (erster Ferientag) 6 h: Bau weiter. 24.–27.12. frei.

### KW 53 (28.12.–03.01.), Weihnachtsferien, ~31 h (Neujahr frei)

- **ETH-Bewerbung (6 h):** Lebenslauf mit Claude nach der ETH-Vorlage,
  Zeugnisse der letzten drei Schuljahre scannen, Passfoto,
  Einverständniserklärung, Gebühr 150 CHF (privat, nicht aus dem App-Geld).
  **Abschicken.**
- **App 1 (~25 h):**
  - echte KI-Funktion: Supabase-Funktion mit Claude Haiku 5.5, Schlüssel nur
    als Geheimnis, Ausgabenlimit 50 $;
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
- **Sobald App 1 etwa halb steht** (Kernfunktion läuft mit echter KI,
  Onboarding und Paywall stehen als Oberfläche): **Messpunkt M2,
  Rechtsform entscheiden und gründen** (Checkliste A, ~4 h). Gelingt das
  nicht in den Ferien, ist es im Modell meist bis Ende Januar so weit.
- **Messpunkt M1 (Fr 08.01.):** ETH-Bewerbung abgeschickt, die KI-Funktion
  läuft in Expo Go.

### KW 02–04 (11.–31.01.), Schulwochen, 10 h (Q3-Ende, mit Klausuren 3 h)

- **Gründung**, falls noch nicht geschehen.
- **Brief an die Krankenkasse**, sobald das Gewerbe angemeldet ist: Claude
  entwirft ihn, du schickst ihn ab. Inhalt: Schüler mit Gewerbe, erwarteter
  Gewinn unter 590 € im Monat, unter 20 Stunden je Woche, keine Angestellten;
  Bitte um schriftliche Bestätigung.
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

### KW 05 (01.–07.02.), Halbjahresferien Mo/Di, ~22 h

- App 1: zwei Ferientage für Tests nach Checkliste C, TestFlight mit 5–10
  Testern aus Familie und Freundeskreis, Fehler beheben.
- **Einreichen, sobald die Checkliste steht.** Abo-Gruppe und Abos zusammen
  mit dieser Version einreichen.
- Erste Slideshows auf dem Markenkonto, noch ohne App-Link.

### KW 06–10 (08.02.–14.03.), Q4, höchstens 6–7 h

- **Ist App 1 eingereicht:** auf das Review reagieren. Den Grund jeder
  Ablehnung schreibst du in `docs/review-log.md`, Claude schlägt die kleinste
  Lösung vor. Rechne mit 1–2 Ablehnungen bei der ersten App; 90 % der Prüfungen
  sind in 48 Stunden fertig.
- **Ist sie bis Sa 13.03. freigegeben:** starten, mit 3 Slideshows je Woche.
  Sonst „manuell veröffentlichen“ einstellen und bis 07.06. warten.
- **Ist sie noch nicht eingereicht:** im Rahmen der Q4-Stunden weiterbauen,
  ohne Druck. Im Modell ist sie bis 14.03. nur in ~26 von 100 Läufen
  fertig, und das ist kein Fehler.
- **Messpunkt M3 (So 14.03.):** Ist App 1 gestartet, freigegeben oder noch im
  Bau? Davon hängt ab, was du am 07.06. tust.
- **ETH-Antwort (etwa Anfang März):** lesen und ablegen; bei Fragen an die
  Zulassungsstelle wenden.

### KW 11–22 (15.03.–06.06.), Ende Q4 und Abitur, 0–5 h

- Keine Arbeit an der App außer Notfällen (Checkliste in Abschnitt 18).
- Läuft App 1 schon: zweimal je Woche 20 Minuten Zahlen ansehen, Support-Mails
  beantworten (Claude entwirft).
- **Signal-Prüfung bei einer schon laufenden App:** drei Wochen nach dem Start.
  Liegt sie über 300 $ Monatsumsatz, buchst du die Creator erst ab 07.06.

### KW 23–26 (07.06.–04.07.), nach dem Abitur, 15–40 h

- **App 1 starten** (veröffentlichen oder fertig bauen und einreichen).
  Täglich 1–3 Slideshows.
- **Signal-Prüfung** drei Wochen nach dem Start: ≥ 300 $ Monatsumsatz →
  Creator buchen (Checkliste F, bis 750 € bis 18.07.); sonst nur eigene
  Videos weiter.
- **App 2** (die zweitbeste Idee) aus derselben Vorlage, mit anderer
  Kernfunktion. Reine Varianten lehnt Apple ab.
- **Bis 15.07.:** Bewerbung an der Leibniz Universität Hannover (~2 h).
- **01.–03.07.:** Abiturzeugnis in eApply hochladen, Original an die ETH.

### KW 27–29 (05.–25.07.), Sommer, ~55 h (davon ~6 h für Zürich)

- Tests nach der Signalregel, App 2 fertig, eingereicht und gestartet.
- Zimmer in Zürich suchen (WOKO braucht die Zulassung), Finanzierungsbrief
  der Eltern.
- **Tor 1 (So 18.07.):** Abschnitt 13.

### KW 30–35 (26.07.–31.08.), Sommer, ~55 h

- Weg A, B oder C (Abschnitt 14).
- Abschluss vor dem Umzug (Checkliste H).
- Mathe auffrischen nach den Empfehlungen der ETH (Folgen und Reihen,
  Induktion, komplexe Zahlen, Analysis, Vektorgeometrie), Java-Tutorial der
  ETH.

---

## 13. Die Messpunkte und was du dann tust

| Messpunkt | Frage | Ja | Nein |
|---|---|---|---|
| **M0** So 20.12. | Grundlagen zur Hälfte, Idee gewählt, Ablauf in Expo Go? | weiter | Lernpfad in den Ferien fertig, Idee bis 28.12. |
| **M1** Fr 08.01. | ETH-Bewerbung abgeschickt? KI-Funktion läuft in Expo Go? | weiter | ETH-Bewerbung hat Vorrang, App danach |
| **M2** App 1 halb fertig (meist Mitte/Ende Januar) | Rechtsform entschieden? | gründen (Checkliste A) | ohne Gründung kein Start: weiterbauen, Entscheidung bis spätestens 07.06. |
| **M3** So 14.03. | App 1 freigegeben? | gestartet bzw. zurückgehalten bis 07.06. | Pause bis 07.06., dann fertig bauen |
| **Signal** 3 Wochen nach jedem Start | ≥ 300 $ Monatsumsatz ohne bezahlte Werbung? | Creator-Geld, bis 18.07. zusammen höchstens 750 € | nur eigene Videos, nächstes Format oder nächste App |
| **Tor 1** So 18.07. | eine App am Stichtag ≥ 5.000 $ Monatsumsatz? | weiter (Weg B oder C) | **Weg A:** keine neue App, kein Creator-Geld |
| **Tor 2** So 08.08. | ≥ 10.000 $? | Weg C | Weg B endet wie Weg A |
| **31.08.** | Abschluss vor dem Umzug erledigt? | Ende | Checkliste H bis zum Umzug |

500.000 € bis 31.08.2027 erreicht das Modell in keinem einzigen Lauf. Das ist
keine Frage des Einsatzes: Die Zeit nach dem Abitur ist zu kurz, damit eine
App so weit wachsen kann.

---

## 14. Ab Juli: drei Wege

### Weg A – kein Treffer (~98 von 100 Läufen)

- Ab 19.07. keine neue App, kein Creator-Geld. Die Apps laufen ohne Budget
  weiter, eigene Slideshows nur, wenn du Lust hast.
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

### Weg B – Tor 1 bestanden, Tor 2 verfehlt (~1,2 von 100)

- Bis 08.08. Creator nur aus dem Umsatz der Vorwoche, jede Woche ein
  Paywall-Test.
- Danach wie Weg A, aber Verkaufen ist hier oft die beste Wahl, weil die App
  messbaren Umsatz hat.
- Achte auf die Familienversicherung (Gewinn über ~590 € im Monat) und melde
  Gewinne der Krankenkasse.

### Weg C – ein echter Treffer (~0,7 von 100)

- Steuerberatung zu Deutschland und der Schweiz **vor** dem Umzug: verkaufen,
  ein Elternteil übernimmt, oder geordnet weiterführen.
- Erst jetzt lohnt sich, was vorher zu teuer war: Max oder Ultra mit einem
  Agenten für Berichte und Support-Entwürfe, ein Helfer auf Rechnung,
  eventuell eine UG.
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
- [ ] Apple Developer Program als Einzelperson (99 $, Karte auf deinen Namen,
      Zwei-Faktor-Anmeldung)
- [ ] Brief an die Krankenkasse abgeschickt, Antwort abgelegt
- [ ] Ordner für Belege (Claude sortiert, du legst ab)

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
- [ ] Je Post notieren: Format, Hook, Aufrufe nach 48 h

### F – Creator (nur nach Signal)

- [ ] Signal erreicht (≥ 300 $ Monatsumsatz drei Wochen nach dem Start)
- [ ] Anfrage persönlich und einzeln, mit Link auf kurze
      Datenschutzhinweise für Creator (Art. 14 DSGVO)
- [ ] Vertrag in Textform: Video, Termin, Freigabe, Kennzeichnung „Werbung“
      plus „Paid partnership“, Honorar, Zahlung **nach** dem Posten,
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
- [ ] Werkzeuge kündigen (Claude Pro, Supabase, Domain bis Laufzeitende)
- [ ] Gewerbe abmelden (0–32,50 €), falls nichts weiterläuft
- [ ] Belege vollständig für die EÜR 2027
- [ ] Krankenkasse über das Ende des Gewerbes informieren
- [ ] Review-Log, Vorlage und Zahlen aufheben

---

## 16. Vorlagen für Claude

Kopieren, Teile in eckigen Klammern ersetzen. Claude Code liest zusätzlich
die `CLAUDE.md` des Projekts.

**Lernen (Grundlagen, KW 48–52)**
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
Kopie einer bekannten App; mit Claude Code für einen Anfänger in ~150 Stunden
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
Bildmotiv vor, das ohne Personen auskommt.
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

**Brief an die Krankenkasse (nach der Gewerbeanmeldung)**
```
Entwirf einen kurzen Brief an die Krankenkasse meiner Eltern: Ich bin
Schüler (13. Klasse), familienversichert, habe seit [Datum] ein Gewerbe für
eine App, arbeite daran im Schnitt unter 20 Stunden je Woche, habe keine
Angestellten und erwarte 2027 einen Gewinn unter 590 € im Monat. Bitte um
schriftliche Bestätigung, dass die Familienversicherung bleibt, und um
Hinweis, welche Nachweise sie brauchen.
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
| 0 | KW 48 bis zur Gründung | Claude Max (bezahlt), dann Pro | ~21 € im Monat, bis Ende Januar ~40–60 € |
| 1 | Gründung (meist Mitte/Ende Januar) | Gewerbe, Apple, Erstberatung beim Steuerberater, Domain, Zweitnummer | ~150–450 € einmalig |
| 2 | ab der Gründung | Claude Pro, Domain und E-Mail, Zweitnummer, ab dem Start Supabase Pro (25 $), KI-API nach Nutzung, ggf. EAS | ~35–110 € im Monat |
| 3 | nur nach Signal | Creator | bis 18.07. höchstens 750 €, danach nur aus dem Umsatz der Vorwoche |
| 4 | nach dem 31.08. | Abmeldung, EÜR und Einkommensteuererklärung 2027 (selbst über ELSTER oder mit Steuerberater) | 0–800 € |
| – | nur wenn der Gewinn über ~590 € im Monat liegt | eigene Kranken- und Pflegeversicherung | ~280 € im Monat |

**Was im Modell herauskommt** (alles bis zum Schluss eingerechnet):
- Median −1.095 €, im Mittel −744 €;
- in 9 von 10 Läufen höchstens 1.495 € Verlust;
- mehr als 5.000 € Verlust in keinem Lauf.

Creator-Geld fließt im Modell nur in 11 von 100 Läufen, im Schnitt aller Läufe ~65 €.

**Kassenregeln**
- Jeden Sonntag: Kontostand, offene Rechnungen, erwartete Zahlungen von Apple
  (5–9 Wochen nach dem Kauf), Monatsgewinn.
- Vor jeder Ausgabe über 50 €: Bleiben Pflichtkosten bis 31.08. und ~800 € für
  den Abschluss gedeckt?
- Creator nach dem Posten bezahlen, nie im Voraus.
- Ein eigenes Konto für die App, damit Belege und Umsatzsteuer sauber bleiben.
  Ein Girokonto auf deinen Namen genügt.

---

## 18. Wenn etwas schiefgeht

| Problem | was du tust |
|---|---|
| Du kommst mit den Grundlagen nicht voran | Lernmodus, kleinere Schritte, ein Thema je Woche; im Zweifel App 1 noch kleiner schneiden |
| App 1 ist am 14.03. nicht fertig | normal (in ~3 von 4 Läufen): Pause bis 07.06., dann in zwei bis drei Wochen fertig |
| Apple lehnt ab | Grund ins Review-Log, kleinste Änderung, neu einreichen; Ablehnungen bei der ersten App sind normal |
| Videos bekommen kaum Aufrufe | anderes Format, nicht mehr Videos desselben Formats; nach 15–20 Posts ohne Signal ein neues Format |
| Claude läuft im Kreis | Sitzung beenden, erst erklären lassen, dann ein kleineres Ziel |
| Pro-Limit bremst in den Ferien | einen Monat Max oder Usage Credits, danach zurück |
| Kosten der KI-Funktion steigen | Bild kleiner, Antworten kürzer, Tageslimit je App-User-ID senken, prüfen, ob Aufrufe ohne Abo durchkommen; Ausgabenlimit mit der Zahl der Zahler anheben |
| Datenpanne oder offener Schlüssel | Schlüssel sofort sperren und neu anlegen; prüfen, welche Daten betroffen sein können; Vorfall schriftlich festhalten (Art. 33 Abs. 5 DSGVO). Lässt sich ein Risiko nicht ausschließen: **binnen 72 Stunden** bei der Landesbeauftragten für den Datenschutz Niedersachsen melden (vorläufige Meldung reicht, die Frist läuft auch am Wochenende); bei hohem Risiko die Betroffenen benachrichtigen (Art. 34) |
| Ein Creator postet ohne Kennzeichnung | sofort korrigieren lassen; du haftest mit |
| Gewinn steigt über ~590 € im Monat | Krankenkasse informieren, eigene Versicherung einplanen (~280 € im Monat) |
| Schule wird schlechter | sofort nur noch 3 Stunden je Woche, bis die Note wieder steht |
| ETH-Antwort ist negativ oder verlangt die Aufnahmeprüfung | Rückfall-Bewerbung in Hannover sicher abschicken; mit mir den Plan für die Aufnahmeprüfung im Januar 2028 rechnen |

---

## 19. Was du aufschreibst

- **Stunden, jeden Tag** – Vorlage [`vorlagen/zeiterfassung.csv`](vorlagen/zeiterfassung.csv):
  Datum, Bereich (Lernen, Code, Videos, Creator, Verwaltung, ETH), App,
  Stunden, Notiz. Das ist auch dein Nachweis für die Krankenkasse
  (unter 20 Stunden je Woche).
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
| **Einzelunternehmen, Creator-Geld nur nach Signal, bis 750 EUR (DEIN PLAN)** | 10,0 | 0,39 | −1.095 € | −744 € | −1.495 € | 5.110 € | 100 % | 0 |
| UG mit gemieteter Geschäftsadresse | 0,000 | 0,000 | −357 € | −422 € | −557 € | −189 € | 1 % | 0 |
| UG mit Anschrift der Eltern | 0,060 | 0,000 | −375 € | −690 € | −631 € | −190 € | 8 % | 0 |
| Einzelunternehmen, ohne Testbudget | 10,0 | 0,26 | −1.077 € | −764 € | −1.474 € | 4.349 € | 100 % | 0 |
| Einzelunternehmen, Tests sofort beim Start (ohne Signalregel) | 8,5 | 0,35 | −1.595 € | −1.206 € | −2.118 € | 4.967 € | 100 % | 0 |
| Einzelunternehmen, Signalregel mit bis zu 1.500 EUR | 10,0 | 0,39 | −1.099 € | −753 € | −1.502 € | 5.138 € | 100 % | 0 |
| Einzelunternehmen, Tore wie bisher (28.02./31.03.) | 1,2 | 0,21 | −963 € | −826 € | −1.253 € | 187 € | 92 % | 0 |
| Einzelunternehmen, ohne Tore | 9,4 | 0,38 | −1.240 € | −908 € | −1.762 € | 5.076 € | 100 % | 0 |
| Einzelunternehmen, gründen schon im Dezember | 9,5 | 0,40 | −1.179 € | −824 € | −1.593 € | 5.031 € | 100 % | 0 |
| Einzelunternehmen, ohne Startpause im Abitur | 10,4 | 0,56 | −1.082 € | −684 € | −1.486 € | 6.037 € | 100 % | 0 |
| Einzelunternehmen, falls du schneller baust (wie mit Programmierkenntnissen) | 30,5 | 3,5 | −672 € | 839 € | −1.357 € | 31.573 € | 100 % | 0 |
| Einzelunternehmen im strengeren Markt 2027 | 8,5 | 0,33 | −1.116 € | −814 € | −1.505 € | 4.566 € | 100 % | 0 |
| Einzelunternehmen, falls Videos ohne Gesicht schlechter wirken (Trefferquoten -25 %) | 7,5 | 0,27 | −1.122 € | −859 € | −1.507 € | 4.032 € | 100 % | 0 |

So liest du die Tabelle:
- **Signalregel:** Creator-Geld nur nach einem Signal ist besser als Tests
  gleich beim Start. Es spart in den vielen Läufen ohne Treffer Geld und
  verliert bei den Treffern kaum etwas. Ganz ohne Testgeld fehlt den
  seltenen großen Treffern der Schub.
- **UG:** In keiner Form passt sie zu deinen 5.000 €.
- **Frühe Tore** (28.02.) hätten App 1 meist abgebrochen, bevor sie fertig
  ist. Dann bliebe nur der kleine Verlust ohne jede Chance.
- **Schneller bauen** ist der größte Hebel: Mit den Bauzeiten von jemandem,
  der programmieren kann, wäre App 1 schon im Winter draußen. Deshalb lohnt
  der Lernpfad, und deshalb soll App 1 so klein wie möglich sein.
- **Startpause im Abitur:** Sie kostet etwas (10,4 statt 10,0 von 100 Läufen
  mit Gewinn). Dafür musst du im Abitur weder auf Bewertungen noch auf
  Ablehnungen reagieren. Abitur und ETH-Zulassung sind mehr wert als dieser
  Unterschied.
- **Gegenproben:** Wirken Videos ohne Gesicht schlechter oder ist der Markt
  2027 strenger, sinkt die Chance etwas, aber die Grenze von 5.000 € hält.

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
