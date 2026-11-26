# Hebel: Was Chance und Ergebnis wirklich erhöht

Gehört zu [`../APP_PLAN_ALLEIN_MIT_CLAUDE.md`](../APP_PLAN_ALLEIN_MIT_CLAUDE.md).
Hier steht, **welche Stellschrauben das Ergebnis verbessern, um wie viel, und
was du dafür tun musst.** Die Schritte selbst stehen in den anderen
Detailplänen (Verweise jeweils am Hebel).

**Stand: Mi 25.11.2026 (spät), Modell nach vier Prüfungen.** Gerechnet mit
[`plan/plan_500k.py`](../../plan/plan_500k.py) (Stand von Commit 280b3eb),
Szenarien „Hebel: …“, je 300.000 Läufe; die Ranglisten in Abschnitt 4 mit je
100.000 gepaarten Läufen. Alle Zahlen sind neu: Vier Prüfungen haben das
Modell am 25.11. korrigiert (Abschnitt 2.2). Die Zahlen vom 24.11. waren zu
günstig. Eine fünfte Prüfung des Codes hat danach drei kleine Abweichungen
gefunden; sie sind noch nicht eingearbeitet und stehen in Abschnitt 15.

Inhalt:
1. [Das Ergebnis in Kürze](#1-das-ergebnis-in-kürze)
2. [Korrekturen vorweg: Verkaufsstopp und Prüfungen vom 25.11.](#2-korrekturen-vorweg-verkaufsstopp-und-prüfungen-vom-2511)
3. [So wurde gesucht und gerechnet](#3-so-wurde-gesucht-und-gerechnet)
4. [Die Rangliste](#4-die-rangliste)
5. [Hebel 1: Kosten senken](#5-hebel-1-kosten-senken)
6. [Hebel 2: Den Abschluss regeln – Nachfolger oder Verkauf](#6-hebel-2-den-abschluss-regeln--nachfolger-oder-verkauf)
7. [Hebel 3: Ferienjob, sobald die Jagd endet](#7-hebel-3-ferienjob-sobald-die-jagd-endet)
8. [Hebel 4: Schneller bauen, review-fest planen](#8-hebel-4-schneller-bauen-review-fest-planen)
9. [Was im Modell nichts ändert, aber Fehler vermeidet](#9-was-im-modell-nichts-ändert-aber-fehler-vermeidet)
10. [Was nichts bringt oder verworfen wurde](#10-was-nichts-bringt-oder-verworfen-wurde)
11. [Der ganze Plan in Zahlen](#11-der-ganze-plan-in-zahlen)
12. [Gegenproben](#12-gegenproben)
13. [Was du dafür tun musst – die Liste](#13-was-du-dafür-tun-musst--die-liste)
14. [Die Werte im Modell](#14-die-werte-im-modell)
15. [Grenzen dieser Rechnung](#15-grenzen-dieser-rechnung)

---

## 1. Das Ergebnis in Kürze

| Stufe | nur die App: Gewinn in … von 100 Läufen | dein Geld im Plus in … von 100 | dein Geld im Median | im Mittel |
|---|---:|---:|---:|---:|
| Plan vom 23.11., wie er dastand | 6,2 | 6,2 | −1.136 € | −954 € |
| derselbe Plan mit Verkaufsstopp am 15.08. (Pflicht von Apple, Abschnitt 2.1) | 2,7 | 2,7 | −1.184 € | −1.074 € |
| dazu alle Stunden und Regeln der Detailpläne (**Ausgangslage**, Abschnitt 2.2) | 0,6 | 0,6 | −1.174 € | −1.158 € |
| + geprüfte Hebel: Kosten, Bau, Markt, Signal (**PLAN MIT HEBELN**) | 3,7 | 3,7 | −564 € | −528 € |
| + Nachfolger (Elternteil hat zugesagt, sonst Verkaufsversuch) | 3,5 | 3,7 (mit dem Geld des Elternteils 4,3) | −564 € | −524 € |
| + Ferienjob ab 19.07., ab 05.07. ohne App im Store = **DEIN PLAN, Stand 25.11.** | **3,7** | **78,5** | **+4.344 €** | **+3.518 €** |
| zum Vergleich: nur Ferienjob ab 05.07., keine App | – | 77,5 | +6.031 € | +4.778 € |

„Dein Geld“ ist, was die App bringt oder kostet, dazu ein Verkaufspreis und
dein Lohn. Eine Übergabe an ein Elternteil zählt nicht dazu, denn dieses Geld
gehört dem Elternteil. Rechnet man es mit, ist DEIN PLAN in 78,7 von 100
Läufen im Plus, im Median mit +4.340 €, im Mittel mit +3.525 €.

**Was das heißt:**

- **Die App ist ein Lernprojekt.** Gewinn aus der App gibt es in 3,7 von 100
  Läufen, also in etwa 4 von 100. Selbst dann sind es meist nur ein paar
  hundert Euro: Mehr als 409 € bringt die App nur in 1 von 100 Läufen. Im
  Median kostet sie dich 567 €. Mehr als 1.000 € Verlust gibt es in 0,5 von
  100 Läufen, mehr als 5.000 € nie.
- **App 1 kommt typisch erst nach dem Abitur.** Bis Di 02.02. ist sie in 0,6
  von 100 Läufen eingereicht, bis So 14.03. in 14,7. Im Median reichst du sie
  in der Woche ab Mo 14.06. ein, und sie ist ab der Woche ab Mo 28.06. im
  Store. Der Kalender in [01](01_TAG_FUER_TAG_BIS_FEBRUAR.md) ist der beste
  Fall: Er rechnet mit den typischen 113 Stunden aus 02 und wenig eigener
  Lernzeit. Das Modell rechnet vorsichtiger: Bauzeit 78/130/260 Stunden,
  Lernen 20/28/40 Stunden, alle Nebenaufgaben. Das ist kein Scheitern, der
  Plan rechnet damit.
- **Die Jagd endet praktisch immer spätestens am So 18.07.** Weg A gilt in
  100,0 von 100 Läufen; nur 2 von 300.000 Läufen enden anders. In 37,5 von 100
  Läufen endet sie schon am Stichtag So 04.07., weil keine App im Store ist.
  Eine App mit 5.000 $ MRR gibt es in 0,0 von 100 Läufen.
- **Das Geld kommt aus dem Ferienjob.** Lohn gibt es in 77,7 von 100 Läufen.
  Verlust machst du nur in Läufen ohne Job (21,5 von 100).
- **Rein nach Geld wäre „nur Ferienjob, keine App“ besser:** im Mittel um
  1.260 €, im Median um rund 1.690 €. Dafür bekommst du eine eigene App im
  Store, Erfahrung im Programmieren und im Marketing vor dem Studium und eine
  kleine Chance auf mehr.
- **500.000 € erreicht kein Lauf.** 10.000 € oder mehr hast du am Ende in rund
  3 von 10.000 Läufen.
- **Die Zahl ist empfindlich.** Mit anderen Annahmen, die niemand messen kann,
  liegt die Gewinnchance der App grob zwischen 1 und 8 von 100 (Abschnitt 12).
  Lies 3,7 als Größenordnung, nicht als genaue Zahl. Drei kleine, noch nicht
  eingearbeitete Abweichungen aus der fünften Prüfung sprechen eher für 3,3
  (Abschnitt 15).

**Was Chance oder Geld erhöht** (gepaarte Rangliste gegen DEIN PLAN mit 3,64
von 100, Abschnitt 4.1):

| Empfehlung | Wirkung | Stand |
|---|---|---|
| Creator-Geld weglassen | Gewinnchance der App 3,64 → 4,58 von 100, dein Geld gleich (im Mittel +18 €); du sparst bis zu 750 € Einsatz | deine Entscheidung; behältst du es, gelten die Regeln aus [05](05_START_UND_MARKETING.md), Abschnitt 10 |
| Schnittliste aus [02](02_BAUPLAN_APP1.md), Abschnitt 8 von Anfang an | +0,28 Punkte | planbar, spart ~7 der 113 Stunden |
| mehr am eigenen Projekt lernen statt mit Tutorials (Lernzeit wie in 01) | +0,86 Punkte | nur, wenn es reicht |
| App 2 im Review ohne Code vorbereiten | +0,16 Punkte | schon im Plan (02, Abschnitt 9) |
| Betriebe mit Tariflohn bevorzugen | +311 € im Mittel, wenn einer ab 19.07. zusagt | schon im Plan ([06](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 2.3) |
| Job bis Fr 10.09. statt Di 31.08. | +767 € im Mittel | schon im Plan (06, Abschnitt 2.4) |

Zusammen bringen die drei planbaren Schritte – Schnittliste, Lernen am Projekt
und kein Creator-Geld – 6,21 statt 3,64 von 100 Läufen mit Gewinn aus der App.
Dein Geld bleibt dabei fast gleich (im Mittel −18 €).

---

## 2. Korrekturen vorweg: Verkaufsstopp und Prüfungen vom 25.11.

### 2.1 Der Verkaufsstopp (Pflicht von Apple)

Die Gegenprüfung vom 24.11. hat eine Pflicht gefunden, die der Plan vom 23.11.
nicht gerechnet hatte.

**Die Regel.** Apple schreibt für Abos vor: „A minimum of 31 days is required
from the date subscription is removed from sale and service is stopped.“
([Apple, Verfügbarkeit von Abos](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription/))
Nimmst du ein Abo aus dem Verkauf, gibt es keine neuen Abschlüsse und keine
Verlängerungen mehr. Danach muss der Dienst noch mindestens 31 Tage laufen.

**Die Folge.** Du ziehst vor dem 20.09. nach Zürich und beendest das Gewerbe
vorher. Dann kannst du nicht bis 31.08. verkaufen und am 31.08. abschalten.
Der Plan vom 23.11. hatte aber die Einnahmen bis 31.08. voll gezählt.

**Was jetzt gilt** (wenn es keinen Nachfolger gibt):

| Schritt | Tag |
|---|---|
| Alle Abos aus dem Verkauf nehmen | So 15.08.2027 |
| Dienst läuft weiter (Server, KI), ohne neue Einnahmen | bis Mi 15.09.2027 |
| App entfernen, Gewerbe abmelden | Do 16.09. oder Fr 17.09., vor dem Umzug |

Ziehst du früher um, liegt das Dienstende spätestens am Tag vor dem Umzug und
der Verkaufsstopp 31 Tage davor. Mit dem Verkaufsstopp rücken alle Termine ab
der Entscheidung je App um dieselbe Zahl Tage vor; die Entscheidung fällt aber
frühestens am Mo 19.07. Den Umzugstag legst du bis Sa 31.07. fest, bei einem
Umzug vor Sa 18.09. schon bis Mo 19.07. Die Tage dazu stehen in
[`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 1.4.

**Wie viel der Stichtag ausmacht** (PLAN MIT HEBELN, ohne Nachfolger und ohne
Job):

| Verkaufsstopp | Dienstende | Gewinn aus der App in … von 100 | Median | Mittel |
|---|---|---:|---:|---:|
| Sa 31.07. | Di 31.08. | 1,2 | −602 € | −594 € |
| **So 15.08.** | **Mi 15.09.** | **3,7** | **−564 €** | **−528 €** |
| Di 31.08. | Fr 01.10. (Betrieb nach dem Umzug, nur nach Beratung) | 8,8 | −529 € | −450 € |

In DEIN PLAN kostet der Verkaufsstopp im Mittel 69 €; einen Abzug gibt es in
90,0 von 100 Läufen. Jede Woche, die du länger verkaufen darfst, zählt, weil
dein Zeitfenster erst im Juni beginnt. Ein Nachfolger hebt den Stopp für
seine App auf; im Modell kommt das aber selten vor (Abschnitt 6).

### 2.2 Die Prüfungen vom 25.11.

Am 24.11. stand hier eine Gewinnchance der App von 9 bis 12 von 100 Läufen.
Sie war zu günstig. Vier unabhängige Prüfungen haben am 25.11. die folgenden
Fehler und Lücken gefunden; alle sind im Modell behoben. „Ohne die Korrektur“
nennt jeweils die Gegenprobe aus Abschnitt 12 (DEIN PLAN liegt bei 3,70 von
100).

**1. Stunden und Regeln der Detailpläne** (Pflicht, kein Hebel).
- **Nebenaufgaben aus 01–06:** Ideenwahl, Verwaltung, Bewerbungen,
  Gründungsberatung, Kassenprüfung ab der Gründung, Markenkonten je
  Einreichung, Vorbereitung der Posts nach der Einreichung, Termine zum
  Ferienjob, Zürich im Juni, Hannover in KW 28 und die Zeitarbeitsanfrage am
  Mo 21.06. (Liste in Abschnitt 14.2). Grund: Diese Stunden stehen in den
  Kalendern von 01, 04 und 06 und fehlen dem Bau. Ohne diese Stunden läge
  PLAN MIT HEBELN bei 6,19 statt 3,71 von 100 (Rangliste, nur zum
  Verständnis).
- **App 2 erst nach der Freigabe von App 1, aus der Vorlage (+3,5 Stunden).**
  Grund: 02, Abschnitt 9: „Sobald App 1 freigegeben ist, nicht früher
  (3–4 Stunden)“; ebenso 06, Abschnitt 1.2, KW 24. Ohne die Korrektur: 4,79.
- **Posts im Wochenprogramm:** vor dem Abitur höchstens 1,5 Stunden, danach
  6,5 Stunden je Woche; die übrigen Stunden bauen weiter. Grund: 05,
  Abschnitt 6.2 (ein Samstagsblock von 90 Minuten) und 6.4 (zwei Posts am Tag);
  der Deckel von 10 Stunden aus 6.1 ist eine Obergrenze. Ohne Wochendeckel:
  2,92; bis zum Deckel von 10 Stunden: 3,47.
- **Vorentscheidung am Fr 25.06.:** Den frühen Jobbeginn am Mo 05.07. gibt es
  nur über Zeitarbeit, kurzfristig angefragt mit einer Chance von 30/50/70 von
  100, mit Vorlauf (Anfrage Mo 21.06.) mit 50/70/85 von 100. Grund: Im Vertrag
  steht der 19.07. (06, Abschnitte 2.2, 2.4 und 2.10); die Chancen sind
  Schätzungen, 06 nennt keine Zahl. Klappte die Zeitarbeit immer, läge dein
  Geld im Mittel bei 3.660 € statt 3.518 €.
- **Späte Gründung:** Ist M2 bis Mo 01.03. nicht erreicht, gründest du am Tag
  nach deiner letzten Prüfung. Grund: 03, Abschnitt 5: „Du gründest dann am
  Tag nach deiner letzten Prüfung, parallel zum restlichen Bau“.

**2. Kosten nach dem Plan statt alter Werbekosten.** Das Modell zog von jedem
Euro Umsatz 45–49 % als Werbung ab, ein Rest aus dem alten 500k-Modell. Jetzt
sind es 15/18/20 %: Umsatzsteuer im Preis, KI-API und Erstattungen. Grund: Im
Plan gibt es keine Werbung aus dem Umsatz, Creator-Geld nur nach dem Signal und
kein bezahltes Verstärken (Hauptplan, Abschnitt 4; 05, Abschnitt 11); von 1 €
Preis bleiben dir rund 0,71 € (06, Abschnitt 3; 05, Abschnitt 2.1), dazu
kommen 2–8 % Erstattungen (05, Abschnitt 2.8). Ohne die Korrektur: 0,66.

**3. Umsatz ohne Posts.** Im Abitur und nach dem Ende der Jagd wuchs der Umsatz
im Modell einfach weiter. Jetzt bringen Wochen ohne Posts kaum Neukunden: In
der Prüfungszeit sinkt der Umsatz um 5/10/15 % je Woche, nach dem Ende der
Jagd um die Hälfte davon. Grund: 05, Abschnitt 6.3 (im Abitur keine Posts) und
6.4 (mit Ferienjob höchstens ein Post am Tag, nach dem Verkaufsstopp keiner);
06, Abschnitt 4.7: „Der Umsatz fällt“. Ohne die Korrektur: 5,92.

**4. Start eines Treffers an 05, Abschnitt 8.4 kalibriert:** 300/1.000/3.000 $
MRR in den ersten Wochen statt 1.000/3.000/8.000 $. Grund: Eine App ohne
Gesicht und ohne Werbung braucht für 1.000 $ MRR 1.000–3.000 Installationen im
Monat, und 100.000 Aufrufe bringen rund 20–70 $ MRR (05, Abschnitt 8.4). Ohne
die Korrektur: 8,32.

**5. Kleinere Korrekturen**
- **Creator-Geld hebt die Spitze einer App nur um 5–15 %,** statt sie auf
  70–100 % der möglichen Spitze zurückzuholen. Grund: 4–12 Creator-Videos
  stehen neben 50–110 eigenen Posts bis Tor 1 (05, Abschnitte 6.1 und 10).
  Ohne die Korrektur: 3,65.
- **Stunden-Messpunkt mit Schnittliste:** Brauchen AP1–AP9 am Di 29.12. mehr
  als ~40 Stunden, gilt die Schnittliste: −6,2 % der Stunden, dafür
  3 Stunden für Version 1.1 nach dem Start. Grund: 02, Abschnitt 8, und 01,
  Abschnitt 11 („das spart ~7 der 113 Stunden, nach dem Start kommen
  ~3 Stunden für Version 1.1 dazu“).
- **Familienversicherung nach dem Jahresgewinn;** das Modell rechnet ihn bis
  zum Dienstende hoch. Grund: Maßgeblich ist der Steuerbescheid, die Grenze
  liegt bei ~7.080 € im Jahr (Hauptplan, Abschnitt 4).
- **Der alte Verkauf der Firma** zum Vielfachen des Jahresgewinns ist
  abgeschaltet. Grund: Verkauft wird nur so, wie es 06, Abschnitt 5 beschreibt
  (netto 1,7/4,3/10,3 Monatsgewinne).
- **Übergabe und Verkauf nach dem Stand am Entscheidungstag** statt mit den
  Augustzahlen; ein Verkauf nur bei 8 vollen Wochen im Store bis So 08.08.; ab
  Mo 09.08. gehören die Erlöse dem Nachfolger. Grund: 06, Abschnitte 3
  und 4.5.
- **Das Elternteil meldet sich nur an, wenn am Mo 28.06. eine App ~100 $ MRR
  zeigt;** sonst gibt es keine Übergabe. Die Chance einer Übergabe sinkt auf
  25/40/60 statt 30/55/80 von 100. Grund: 06, Abschnitt 4.4; die Chance ist
  eine Schätzung der Gegenprüfung.
- **Lohn bis zum letzten Arbeitstag Fr 10.09.** Grund: lange Variante aus 06,
  Abschnitte 2.4 und 2.8. Mit Job nur bis Di 31.08. läge dein Geld im Mittel
  bei 2.754 €.
- **Stichtag So 04.07. ohne Bedingung:** Ohne App im Store endet die Jagd, mit
  oder ohne Job. Grund: 06, Abschnitt 2.10. Ganz ohne Stichtag läge dein Geld
  im Mittel bei 3.307 €.
- **Im Abitur mit App im Store oder im Review nur Betrieb,** kein Bau und keine
  Posts. Grund: 05, Abschnitte 1.2 und 6.3.
- **Ein Signal vor dem Abitur zählt;** Creator bucht der Plan erst nach der
  letzten Prüfung. Grund: 05, Abschnitt 9.3: „Das Ergebnis zählt. Creator
  buchst du trotzdem erst am Tag nach deiner letzten Prüfung“.
- **App 2 im Review ohne Code vorbereiten,** bis 6 Stunden: `SPEC.md` aus der
  Reserve-Idee, Fragenliste, Store-Texte, Icon-Entwurf. Grund: 02, Abschnitt 9:
  Solange App 1 im Review ist, bereitest du App 2 ohne Code vor, höchstens
  ~6 Stunden; den Code gibt es erst nach der Freigabe. Die zweitbeste Idee ist
  seit dem Ideen-Tor als Reserve gemerkt (01, Sa 19.12.). Ohne die
  Vorbereitung: 3,52.
- **Gegenproben sind gepaart:** Sie ziehen dieselben Zufallszahlen wie
  DEIN PLAN. Grund: Dann zeigt eine Gegenprobe nur die Wirkung der Annahme,
  die sie ändert, und keinen verschobenen Zufall (Abschnitt 3).

---

## 3. So wurde gesucht und gerechnet

1. **Recherche in acht Hebelklassen:** Markt und Sprache, schneller bauen,
   Kosten, Wert nach dem Sommer, Idee und Nische, Zeit und Ferienjob,
   Marketing ohne Gesicht, Preis und Paywall. Zusammen rund 95 einzelne
   Vorschläge, jeder mit Quelle, Kosten, Stunden und Risiko.
2. **Gegenprüfung:** Jede Klasse wurde von einem zweiten, unabhängigen
   Durchgang geprüft, der die Quellen nachgelesen hat. Er hat fast alle
   Wirkungen nach unten korrigiert und einige Vorschläge verworfen.
3. **Modell:** Angesetzt sind nur die korrigierten, vorsichtigen Werte
   (Abschnitt 14). Jede Variante läuft 300.000-mal über die 39 Wochen von
   Mo 30.11.2026 bis So 29.08.2027; danach zählen noch der Lohn bis Fr 10.09.
   und der Abschluss.
4. **Ranglisten** (Abschnitt 4): 100.000 Läufe je Variante, gepaart. Lauf 1
   rechnet in jeder Variante mit demselben Startwert, Lauf 2 ebenso, und so
   weiter. Der Unterschied zweier Varianten zeigt dann ihre Wirkung und kaum
   Zufall. Die 300.000 Läufe haben dagegen je Szenario einen eigenen
   Startwert. Dieselbe Variante weicht zwischen beiden Rechnungen um bis zu
   0,15 Punkte ab (Lernzeit aus 01: 4,50 und 4,65 von 100; DEIN PLAN: 3,64 und
   3,70). Unterschiede dieser Größe zwischen zwei Zeilen mit 300.000 Läufen
   sind Zufall.
5. **Geprüft:** Vier unabhängige Prüfungen am 25.11. haben Modell und Pläne
   gegeneinander gelesen und nachgerechnet (Abschnitt 2.2). 227 Tests laufen
   grün. Die alten Szenarien (Stände 7cb0468, e2b0430 und bcad479) rechnen
   Lauf für Lauf wie vorher.
6. **Nur erlaubte Wege.** Nichts, was das Abitur gefährdet, täuscht, gegen
   Regeln der Plattformen verstößt oder mehr als 5.000 € kosten kann.

**Begriffe**
- **„Gewinn aus der App“:** deine Vermögensänderung aus der App bis zum
  Schluss, einschließlich Abmeldung und Steuererklärung, vor Einkommensteuer.
  Erlöse nach einer Übertragung gehören dem Nachfolger und zählen nicht.
- **„Dein Geld“:** App, Verkaufspreis und Lohn.
- **„Mit dem Geld des Elternteils“:** dazu der Wert einer Übergabe, abzüglich
  der Kosten, die das Elternteil verliert, wenn es sich anmeldet und dann
  nichts übernimmt. Dieses Geld gehört nicht dir.

---

## 4. Die Rangliste

In 4.1 und 4.2 läuft jede Variante gegen dieselbe Ausgangslage, Lauf für Lauf
gepaart, mit 100.000 Läufen. 4.3 zeigt die Stufen mit je 300.000 Läufen.

### 4.1 Gegen DEIN PLAN

DEIN PLAN in dieser Rangliste: Gewinn aus der App in 3,64 von 100 Läufen, dein
Geld im Median 4.345 €, im Mittel 3.521 €.

**Planbar – das entscheidest du:**

| Hebel | Gewinn aus der App in … von 100 | dein Geld im Median | im Mittel | Hinweis |
|---|---:|---:|---:|---|
| **Creator-Geld weglassen** | 4,58 | 4.356 € | 3.539 € | mehr Chance, nicht weniger Geld; du sparst bis zu 750 € Einsatz |
| Schnittliste aus 02, Abschnitt 8 von Anfang an | 3,92 | 4.341 € | 3.518 € | Onboarding mit 3 Fragen, kein eigenes Design, keine Bewertungsabfrage, Favoriten in Version 1.1; spart ~7 der 113 Stunden |
| mehr am eigenen Projekt lernen (Lernzeit wie in 01: 12/15/20 statt 20/28/40 Stunden) | 4,50 | 4.322 € | 3.475 € | nur, wenn das Lernen am Projekt wirklich reicht |
| Schnittliste und Lernen am Projekt | 4,92 | 4.320 € | 3.480 € | |
| **Schnittliste, Lernen am Projekt, ohne Creator-Geld** | **6,21** | 4.332 € | 3.503 € | beste planbare Kombination |
| App 2 im Review ohne Code vorbereiten (bis 6 Stunden) | 3,64 | 4.345 € | 3.521 € | schon im Plan (02, Abschnitt 9); ohne die Vorbereitung 3,48 von 100, 4.341 € und 3.516 € |
| Betriebe mit Tariflohn bevorzugen, falls einer ab 19.07. zusagt | 3,64 | 4.752 € | 3.832 € | schon im Plan (06, Abschnitt 2.3); +311 € im Mittel, ob einer zusagt, entscheidet der Betrieb |
| Job bis Fr 10.09. statt Di 31.08. | 3,64 | 4.345 € | 3.521 € | schon im Plan; mit Ende am Di 31.08. nur 3.363 € und 2.754 €, also −767 € im Mittel |

**Geld gegen Chance:**

| Variante | Gewinn aus der App in … von 100 | dein Geld im Median | im Mittel | Hinweis |
|---|---:|---:|---:|---|
| Job ab Mo 05.07., wenn am So 04.07. keine App 300 $ MRR zeigt | 2,79 | 5.413 € | 4.191 € | +670 € im Mittel, +1.068 € im Median, dafür −0,85 Punkte; setzt einen Vertrag ab 05.07. voraus |

**Gegen eine Regel des Plans oder nicht planbar:**

| Variante | Gewinn aus der App in … von 100 | dein Geld im Median | im Mittel | warum nicht |
|---|---:|---:|---:|---|
| App 2 schon während des Reviews, mit Code | 4,81 | 4.370 € | 3.544 € | gegen 02, Abschnitt 9: Die Lehren aus dem Review-Log fehlen sonst in der Vorlage |
| App 1 um 15 % kleiner | 4,29 | 4.316 € | 3.478 € | nur mit einer kleineren Idee; die Schnittliste deckt das nicht; gerechnet mit mehr Review-Risiko |
| ohne Ruhezeit im Abitur | 4,34 | 4.291 € | 3.440 € | gegen die Abiturregel (Hauptplan, Abschnitt 4); kostet dein Geld 81 € im Mittel |
| frei ab Mo 31.05. statt Mo 07.06. | 4,87 | 4.319 € | 3.448 € | hängt am Prüfungsplan; frag im Januar nur, wann die Prüfung liegt |
| Zeitarbeit ab 05.07. klappt immer | 3,64 | 4.451 € | 3.669 € | entscheidet die Zeitarbeitsfirma; +148 € im Mittel |
| Bauzeiten wie mit Programmierkenntnissen | 20,55 | 4.384 € | 3.640 € | Empfindlichkeit, kein Hebel (Abschnitt 8) |

**Schlechter:** höchstens eine App (alles in App 1): 1,95 von 100, dein Geld im
Median 4.277 €, im Mittel 3.455 €. Jede weitere App ist ein weiterer Versuch
mit besserer Lernkurve.

### 4.2 Gegen PLAN MIT HEBELN: nur die App

Ohne Nachfolger und ohne Job. PLAN MIT HEBELN in dieser Rangliste: Gewinn in
3,71 von 100 Läufen, Median −563 €, Mittel −529 €.

| Variante | Gewinn in … von 100 | Median | Mittel | Hinweis |
|---|---:|---:|---:|---|
| Bauzeiten wie mit Programmierkenntnissen (50/80/130 Stunden, weitere Apps 22/40/75, Lernen 3/6/12) | 21,58 | −419 € | −249 € | Empfindlichkeit, kein Hebel |
| ohne die Nebenaufgaben der Detailpläne | 6,19 | −550 € | −491 € | nicht möglich, nur zum Verständnis |
| App 2 schon während des Reviews, mit Code | 5,27 | −536 € | −491 € | gegen 02, Abschnitt 9 |
| frei ab Mo 31.05. | 5,18 | −545 € | −497 € | hängt am Prüfungsplan |
| ohne Ruhezeit | 4,64 | −586 € | −537 € | gegen die Abiturregel; kostet Geld |
| Ideenwahl kürzer (5 statt 10 Stunden ab 30.11.) | 4,03 | −562 € | −525 € | spart Stunden, aber die Ideenwahl vermeidet sichere Verluste ([04](04_IDEENWAHL.md), Abschnitt 1) |
| gründen bei 85 % statt bei M2 | 3,85 | −553 € | −519 € | kaum Unterschied |
| Ruhezeit, aber mit App im Store im Abitur weiterbauen | 3,79 | −562 € | −527 € | kaum Unterschied; gegen die Abiturregel |
| Creator-Geld bis 1.500 € statt 750 € | 3,65 | −564 € | −531 € | kein Unterschied |
| höchstens 3 Apps | 3,62 | −565 € | −531 € | kein Unterschied |
| Tor 1 am So 11.07. | 3,54 | −576 € | −542 € | schlechter |
| Tor 1 am So 01.08. | 3,38 | −557 € | −526 € | schlechter |
| Posts bis zum Deckel von 10 Stunden je Woche | 3,37 | −568 € | −536 € | schlechter |
| Signal schon ab 150 $ | 3,18 | −579 € | −557 € | schlechter |
| Signal schon nach 2 Wochen | 3,18 | −565 € | −535 € | schlechter |
| höchstens 2 Apps | 2,86 | −577 € | −550 € | schlechter |
| ohne Wochendeckel für Posts | 2,80 | −581 € | −554 € | schlechter |
| Tor 1 am So 04.07. | 2,69 | −593 € | −570 € | schlechter |

### 4.3 Die Hebel Schritt für Schritt

300.000 Läufe je Zeile. Die ersten vier Hebel laufen einzeln gegen die
Ausgangslage, Nachfolger und Ferienjob gegen PLAN MIT HEBELN.

| Stufe | Gewinn aus der App in … von 100 | dein Geld im Plus in … von 100 | Median | Mittel | Wirkung im Mittel |
|---|---:|---:|---:|---:|---:|
| Ausgangslage | 0,59 | 0,59 | −1.174 € | −1.158 € | – |
| nur Kosten senken, mit Ruhezeit im Abitur (Abschnitt 5) | 2,19 | 2,19 | −585 € | −565 € | **+593 €** |
| nur schneller bauen und review-fest planen (Abschnitt 8) | 0,93 | 0,93 | −1.149 € | −1.122 € | +36 € |
| nur Markt (Deutsch zuerst) und Ideenwahl | 0,60 | 0,60 | −1.174 € | −1.157 € | +1 € |
| nur zweite Signalprüfung Ende Juni | 0,56 | 0,56 | −1.174 € | −1.158 € | 0 € |
| **alle vier: PLAN MIT HEBELN** | **3,73** | **3,73** | **−564 €** | **−528 €** | **+630 €** |
| + Übergabe oder Verkauf, Elternteil hat zugesagt (Abschnitt 6) | 3,53 | 3,70 | −564 € | −524 € | +4 € |
| + Verkaufsversuch und Übergabe ohne feste Zusage | 3,56 | 3,72 | −564 € | −524 € | +4 € |
| + Ferienjob ab 19.07. (Abschnitt 7) | 3,70 | 78,54 | +4.260 € | +3.306 € | **+3.834 €** |
| + Ferienjob ab 19.07., ab 05.07. ohne App im Store | 3,91 | 78,55 | +4.346 € | +3.513 € | +4.041 € |
| **+ Übergabe oder Verkauf + Ferienjob = DEIN PLAN** | 3,70 | 78,53 | +4.344 € | +3.518 € | +4.046 € |

Alle vier zusammen bringen mehr als die Summe der einzelnen Wirkungen, weil
erst die niedrigeren Kosten kleine Erfolge zu Gewinnen machen. Die Reihenfolge
nach Wirkung ist: **Ferienjob, Kosten, Bau.** Nachfolger, Markt und Signal
ändern das Ergebnis kaum.

---

## 5. Hebel 1: Kosten senken

**Wirkung** (gegen die Ausgangslage, 300.000 Läufe): Gewinnchance der App
0,6 → 2,2 von 100. Median −1.174 € → −585 €, Mittel −1.158 € → −565 €, im
Mittel also +593 €. Mehr als 1.000 € Verlust gibt es nur noch in 0,3 statt
73,4 von 100 Läufen. Die Erfolgsquote der Apps ändert sich nicht. Die Schwelle,
ab der ein kleiner Erfolg ein Gewinn ist, sinkt aber um rund 590 €.

**Zum Hebel gehört die Ruhezeit im Abitur:** Ist vom 15.03. bis zur letzten
Prüfung keine App im Store oder im Review, ruht Claude Pro, und es wird nicht
gebaut. Das spart Geld, kostet aber Chance: Ohne Ruhezeit läge PLAN MIT HEBELN
bei 4,64 statt 3,71 von 100, und dein Geld in DEIN PLAN läge im Mittel um 81 €
niedriger (Abschnitt 4). Der Plan bleibt bei der Ruhezeit, weil das Abitur
vorgeht.

| Posten | bisher angesetzt | neu | wie |
|---|---|---|---|
| Abschluss (Abmeldung, Steuererklärung 2027) | 0 / 300 / 800 € | 20 / 80 / 500 € | Belegtabelle ab dem ersten Beleg, EÜR und Erklärungen 2028 selbst über ELSTER; Steuerberater nur im Ernstfall |
| Gründung | 150 / 250 / 450 € | 140 / 200 / 380 € | kostenlose Gründungsberatung der IHK statt bezahlter Erstberatung (vorher fragen, ob sie kostenlos ist) |
| je Monat zwischen Gründung und erstem Start | 35 / 60 / 110 € | 23 / 28 / 45 € | nur Claude Pro, Domain mit Postfach, Prepaid-Nummer; kein Server-Tarif, kein Build-Abo |
| je Monat nach dem Start | 35 / 60 / 110 € | 23 / 30 / 75 € | Supabase im Gratis-Tarif, bis ein Signal da ist; EAS im Gratis-Tarif |
| je Monat im Abitur, wenn keine App im Store oder im Review ist | wie oben | 2 / 5 / 30 € | Claude Pro ruht (bezahlt bis ~27.03., die Ersparnis beginnt im Modell am Mo 29.03.); gebaut wird nicht. Mit App im Store oder im Review nur Betrieb und mindestens ~50 € je Monat (Supabase Pro) |
| Claude Max in einzelnen Monaten | 0 / 10 / 70 € je Monat | 0 / 0 / 12 € | Max höchstens für einen Monat und nur, wenn das Pro-Limit die Ferienarbeit nachweislich stoppt |
| je Monat nach dem Ende der Jagd | 10 / 25 / 50 € | 5 / 12 / 35 € | am selben Tag alles kündigen, was Betrieb und Abschluss nicht brauchen |

**Nicht verwechseln:** Dass das Modell von jedem Euro Umsatz nur noch 15–20 %
statt 45–49 % abzieht, ist kein Hebel, sondern eine Korrektur (Abschnitt 2.2).
Sie gilt schon in der Ausgangslage.

Dazu gehören zwei Entscheidungen, die im Modell kein Geld bringen, aber
Arbeit sparen: **Kleinunternehmerregelung anwenden** (kein Verzicht) und beim
Finanzamt schriftlich fragen, ob es für die kleine Umsatzsteuer auf
Auslandsrechnungen (§ 13b) Voranmeldungen will.

**Der höchste Betrag, den du im Lauf des Projekts vorstreckst** (DEIN PLAN):
im Median 481 €, in 90 von 100 Läufen höchstens 621 €, in 99 von 100
höchstens 1.269 €, nie mehr als 1.947 €. Die hohen Werte entstehen vor allem, wenn nach
einem Signal Creator-Geld fließt: Ohne Creator-Geld wären es in 99 von 100
Läufen höchstens 778 € und nie mehr als 1.299 €. Ein Nachschuss kommt in
keinem Lauf vor.

**Wo es steht:** [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md),
Abschnitt 1.2.

**Nicht wegsparen:** Apple Developer Program, Gewerbeanmeldung und Meldung an
die Krankenkasse, Impressum und Datenschutzerklärung, die Server-Funktion mit
geheimem Schlüssel und Ausgabengrenze, Claude Pro in den Bau-Monaten.

---

## 6. Hebel 2: Den Abschluss regeln – Nachfolger oder Verkauf

**Wirkung** (gegen PLAN MIT HEBELN, ohne Job, 300.000 Läufe): **fast keine.**
- Dein Geld: im Plus in 3,70 statt 3,73 von 100 Läufen, im Mittel −524 € statt
  −528 € (+4 €), im Median gleich (−564 €).
- Mit dem Geld des Elternteils: im Plus in 4,35 von 100, im Mittel −516 €
  (+12 €).
- Die Gewinnchance der App allein sinkt von 3,73 auf 3,53 von 100, weil die
  Erlöse ab der Übertragung dem Nachfolger gehören.

Der Wert vom 24.11. (+469 € im Mittel) gilt nicht mehr. Seit dem 25.11.
entscheidet das Modell mit dem Stand am Entscheidungstag statt mit den
Augustzahlen, und das Elternteil meldet sich nur nach ~100 $ MRR am Mo 28.06.
an (Abschnitt 2.2). Zusammen mit den vorsichtigeren Umsätzen erreichen nur
wenige Apps die Schwellen der Tabelle unten.

**In DEIN PLAN:**
- Übergabe in 2,0 von 100 Läufen, Verkauf in 0,3.
- Im Mittel aller Läufe bringt die Übergabe dem Elternteil 16 € und der
  Verkauf dir 7 €. Die Erlöse nach der Übertragung (im Mittel 8 €) gehören dem
  Nachfolger.
- Das Elternteil meldet sich in 8,5 von 100 Läufen an. In 6,5 von 100 übernimmt
  es danach nichts; dann sind seine 120–165 € verloren (im Mittel aller Läufe
  9 €). Meldet es sich an, geht es also in rund 3 von 4 Fällen leer aus.

**Warum der Hebel trotzdem im Plan bleibt:** Er kostet dich wenig (ein
Gespräch, eine Seite im Januar, die Übergabe-Mappe) und ist die Versicherung
für den seltenen Treffer. Für eine App, die im Juni startet, ist die Übergabe
der einzige realistische Weg, ihren Wert zu erhalten (06, Abschnitt 3). Die
Übergabe hebt außerdem den Verkaufsstopp für diese App auf. Sag dem
Elternteil vorher ehrlich, wie selten sie im Modell gelingt.

| Ausgang | Bedingung | wie oft es klappt (Schätzung) | was es bringt |
|---|---|---|---|
| einstellen | unter ~150 € Monatsgewinn | – | nichts; Verkaufsstopp So 15.08. |
| Übergabe an ein Elternteil | ab ~150 € Monatsgewinn **und** schriftliche Zusage im Januar **und** Anmeldung des Elternteils nach ~100 $ MRR am Mo 28.06. | in 25 / 40 / 60 von 100 solchen Fällen (ohne feste Zusage 10 / 25 / 45) | 0,7 / 2 / 5 Monatsgewinne in den zwölf Monaten ab der Übertragung (Mo 09.08.), abzüglich 120–165 € für Apple-Konto und Gewerbe des Elternteils. **Das Geld gehört dem Elternteil,** nicht dir |
| Verkauf (z. B. über Flippa) | ab 300 $ Monatsumsatz und mindestens 8 volle Wochen im Store bis So 08.08. (Start spätestens So 13.06.) | in 10 / 25 / 45 von 100 solchen Fällen | netto 1,7 / 4,3 / 10,3 Monatsgewinne; **das Geld gehört dir** |

Entschieden wird mit dem Monatsgewinn der vier Wochen bis So 01.08. und den
vollen Wochen im Store bis zum Umschalttag So 08.08.

**Ohne feste Zusage** eines Elternteils bleibt dein Geld gleich (−524 € im
Mittel); mit dem Geld des Elternteils ist der Plan dann in 3,95 statt 4,35 von
100 Läufen im Plus.

**Was du tun musst:**
- Im Elterngespräch am Do 26.11. und spätestens bis So 31.01. klären, ob ein
  Elternteil eine laufende App übernehmen würde (in 01 am Sa 16.01.). Eine Seite
  schriftlich: ab welchem Monatsgewinn, wer die 99 € für das Apple-Konto und
  die Gewerbeanmeldung zahlt, wie viele Stunden im Monat. Vorher prüfen, was
  dagegen spricht (Arbeitgeber oder Dienstherr, eigene Versicherung, laufende
  Leistungen; 06, Abschnitt 4.2).
- Jede App von Anfang an so bauen, dass man sie übergeben kann
  (Übergabe-Mappe, 06, Abschnitt 4.3).
- Am Mo 28.06. die MRR je App notieren. Zeigt eine App mindestens ~100 $ MRR
  (mit Nachprüfung: abgelesen am Tag nach der letzten Nachprüfung), schickt
  das Elternteil bis Fr 02.07. Gewerbe- und Apple-Anmeldung ab. Vertrag, Bank,
  Steuer, Händlerangaben und Small Business Program folgen, sobald das Konto
  frei ist. Ziel ist die Genehmigung des Small Business Program bis Sa 31.07.;
  sonst gilt im August nicht der niedrige Apple-Satz.
- Die Übergabe ist eine echte Schenkung ohne Gewinnbeteiligung, schriftlich
  und binnen drei Monaten dem Finanzamt angezeigt (§ 30 ErbStG). Das
  Elternteil wird Unternehmer mit eigenem Impressum, eigenem Gewerbe und
  eigener Steuer und beantragt das Small Business Program selbst. Ein
  Elternteil nur als Namen einzutragen, während du das Geschäft führst, ist
  nicht erlaubt.

**Wo es steht:** [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md),
Abschnitte 3 bis 5.

**Verworfen:** Weiterführen von Zürich aus (rund 3.500–5.500 CHF Mehrkosten im
Jahr, vor allem Krankenversicherung; lohnt erst bei einem echten Treffer und
nur nach Beratung zu beiden Ländern). Jahresabos und „lebenslang“, solange du
Inhaber bist (du müsstest zwölf Monate liefern oder erstatten); ein Nachfolger
entscheidet nach der Übertragung selbst. Ein Elternteil von Anfang an als
Inhaber nur wegen der Steuer (hält nicht).

---

## 7. Hebel 3: Ferienjob, sobald die Jagd endet

**Wirkung** (gegen PLAN MIT HEBELN, 300.000 Läufe):

| | dein Geld im Plus in … von 100 | Median | Mittel | Wirkung im Mittel | Gewinn aus der App in … von 100 |
|---|---:|---:|---:|---:|---:|
| PLAN MIT HEBELN, ohne Job | 3,73 | −564 € | −528 € | – | 3,73 |
| + Ferienjob ab Mo 19.07. | 78,54 | +4.260 € | +3.306 € | +3.834 € | 3,70 |
| + Ferienjob ab 19.07., ab Mo 05.07. ohne App im Store | 78,55 | +4.346 € | +3.513 € | +4.041 € | 3,91 |

Die Chance der App ändert sich dadurch kaum (3,70 bzw. 3,91 statt 3,73 von
100).

**Warum der Job die App fast nichts kostet:** Die Jagd endet ohnehin am
So 18.07. (Weg A in 100,0 von 100 Läufen) oder schon am Stichtag So 04.07.

| | |
|---|---|
| Form | **kurzfristige Beschäftigung**, von Anfang an schriftlich befristet: Mo 19.07. bis Fr 10.09.2027 (40 Arbeitstage, 320 Stunden). Passt dem Betrieb nur ein Ende am Di 31.08., nimmst du das (32 Arbeitstage, 256 Stunden) |
| Abgaben | keine Sozialabgaben; die einbehaltene Lohnsteuer (etwa 12–16 %) kommt 2028 über die ohnehin fällige Steuererklärung zurück |
| Lohn | 14,60 €/h (Mindestlohn 2027) bis 18,50 €/h: für 320 Stunden endgültig **4.672,00 € / 5.078,40 € / 5.920,00 €**, zunächst ausgezahlt 84–88 % davon (06, Abschnitt 2.8) |
| Familienversicherung | Lohn aus einer kurzfristigen Beschäftigung zählt nicht als regelmäßiges Einkommen; vor der Unterschrift bei der Krankenkasse schriftlich bestätigen lassen (06, Abschnitt 2.6) |
| Chance, einen Job über die ganze Zeit zu bekommen | 70 / 78 / 85 von 100 (Schätzung der Gegenprüfung) |
| früher Beginn | Ist am So 04.07. keine App im Store, endet die Jagd. Die zwei Wochen ab Mo 05.07. gibt es nur über eine Zeitarbeitsfirma, angefragt am Mo 21.06. in jedem Fall (unten). Galt am Fr 25.06. der 05.07., klappt es mit einer Chance von 50 / 70 / 85 von 100 (mit Vorlauf). Galt der 19.07., fragst du am Mo 05.07. kurzfristig nach, mit 30 / 50 / 70 von 100 (Schätzungen; 06 nennt keine Zahl). 10 Arbeitstage bringen zusätzlich 1.168,00 € / 1.269,60 € / 1.480,00 € |

Im Modell zählen 560 / 600 / 690 € je Woche nach Fahrtkosten, ab Mo 19.07.
(früh ab Mo 05.07.) bis Fr 10.09.: die sechs vollen Wochen bis So 29.08. und
die 10 Werktage danach.

**Was im Modell herauskommt** (DEIN PLAN):
- Lohn in 77,7 von 100 Läufen, im Median 5.001 € (Läufe mit Lohn), im Mittel
  aller Läufe 4.043 €.
- **Stichtag:** In 37,5 von 100 Läufen ist am So 04.07. keine App im Store;
  dann endet die Jagd. In 17,0 von 100 beginnt der Job am Mo 05.07., in 20,5
  nicht.
- **Vorentscheidung:** In 81,9 von 100 Läufen ist am Fr 25.06. eine App im
  Store oder im Review (im Modell der Stand am So 27.06.); dann gilt der
  19.07. In 19,4 von 100 Läufen ist am So 04.07. trotzdem keine App im Store.
  Dann gibt es die zwei Wochen nur über kurzfristig angefragte Zeitarbeit; in
  12,0 von 100 Läufen gibt es dann keinen frühen Beginn.

**Was die Einzelheiten ausmachen** (gepaart, gegen DEIN PLAN):
- Job nur bis Di 31.08. statt Fr 10.09.: dein Geld im Mittel −767 €, im Median
  −982 €.
- Betrieb mit Tariflohn ab 19.07.: +311 € im Mittel, +407 € im Median.
- Zeitarbeit ab 05.07. klappt immer: +148 € im Mittel.
- Stichtag nur, wenn noch keine App eingereicht ist: −162 € im Mittel; ganz
  ohne Stichtag (Job erst ab 19.07.): −209 €.

**Was du tun musst:**
- Am Sa 02.01. (spätestens Sa 30.01.) drei Bewerbungen mit festem Zeitraum
  19.07. bis 10.09., zuerst bei Betrieben mit Tariflohn (06, Abschnitte 2.2
  bis 2.4; in 01 sind 1 h 30 min eingeplant).
- Am Mo 21.06. in jedem Fall zwei Zeitarbeitsfirmen für einen festen Termin
  anfragen (1 Stunde): ohne unterschriebenen Vertrag für den ganzen Sommer,
  mit Vertrag ab 19.07. für Mo 05.07.–Fr 16.07. Welcher Termin gilt,
  entscheidest du am Fr 25.06. (06, Abschnitte 2.2 und 2.4).
- Am Fr 25.06. die Vorentscheidung treffen: Ist eine App im Store oder im
  Review, gilt Mo 19.07., sonst Mo 05.07. Ohne Vertrag nennst du der
  Zeitarbeitsfirma dieses Datum als Beginn. Mit Vertrag ab 19.07. sagst du ihr
  für Mo 05.07.–Fr 16.07. zu, wenn der 05.07. gilt, sonst ab (06,
  Abschnitte 2.2 und 2.10).
- Eine Kündigungsklausel oder Probezeit in den Vertrag, falls doch ein Treffer
  kommt (06, Abschnitt 2.11).

**Wo es steht:** [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md),
Abschnitt 2.

**Verworfen:** Job schon ab 14.06. (vor dem Ende der Prüfungszeit nicht
sauber möglich und nimmt der App ihr einziges Fenster), Nachhilfe neben der
App (bringt 150–250 €, kostet 15–30 App-Stunden in der knappsten Zeit), um
einen frühen Prüfungstermin bitten (Erfolgschance 5–15 von 100; nur fragen,
wann die Prüfung liegt).

---

## 8. Hebel 4: Schneller bauen, review-fest planen

**Wirkung** (gegen die Ausgangslage, 300.000 Läufe): Gewinnchance der App
0,6 → 0,9 von 100, Median −1.174 € → −1.149 €, Mittel −1.158 € → −1.122 €
(+36 €). App 1 ist bis Di 02.02. in 0,6 statt 0,3 von 100 Läufen eingereicht,
bis So 14.03. in 14,7 statt 10,5.

| | bisher | neu |
|---|---|---|
| Bauzeit App 1 | 80 / 140 / 280 h | 78 / 130 / 260 h |
| Bauzeit weitere Apps | 35 / 60 / 120 h | 33 / 55 / 110 h |
| Lernen | 20 / 30 / 40 h | 20 / 28 / 40 h |
| Review mit Ablehnungen | 0,5 / 1,5 / 4,0 Wochen | 0,4 / 1,2 / 3,0 Wochen |
| App 2 vorbereiten, solange App 1 im Review ist | – | bis 6 h, ohne Code |

Dahinter stehen: das offizielle Expo-Gerüst mit Plugin, die fertige
RevenueCat-Paywall, das Apple-Konto schon in KW 51, der Durchstich zuerst,
ein fester Funktions-Stopp am So 24.01., eine Arbeitsweise mit Prüfbefehl, ab
App 2 die eigene Vorlage und die Vorbereitung von App 2 ohne Code, solange
App 1 im Review ist (`SPEC.md` aus der Reserve-Idee, Fragenliste, Store-Texte,
Icon-Entwurf; ohne sie 3,48 statt 3,64 von 100, Abschnitt 4.1).

Die Wirkung ist klein, weil die Belege schwach sind (Herstellerangaben ohne
Zeitmessung) und die Gegenprüfung deshalb nur rund 7 % weniger Bauzeit stehen
ließ.

**Was eine gesparte Baustunde bewirkt:**
- **Ohne Job** (PLAN MIT HEBELN) hilft eine gesparte Stunde der App, und sie
  kostet nichts. Beispiel: Eine kürzere Ideenwahl (5 statt 10 Stunden) hebt
  die Chance auf 4,03 statt 3,71 von 100, das Mittel auf −525 € statt −529 €
  (Abschnitt 4.2). Die Ideenwahl kürzt du trotzdem nicht (Abschnitt 10).
- **In DEIN PLAN bringt eine gesparte Baustunde der App wenig und senkt dein
  Geld leicht.** App 1 ist dann öfter bis So 04.07. im Store. Dann kommen der
  Stichtag-Stopp und mit ihm der frühe Jobbeginn seltener. Das zeigt die
  Rangliste in Abschnitt 4.1: Mit der Schnittliste (~7 Stunden weniger) steigt
  die Chance um 0,28 Punkte, der Stichtag-Stopp kommt in 35,9 statt 37,3 von
  100 Läufen, und dein Geld sinkt im Mittel um 3 €. Mit der Lernzeit aus 01
  steigt die Chance um 0,86 Punkte, der Stichtag-Stopp kommt nur noch in 27,0
  von 100 Läufen, und dein Geld sinkt im Mittel um 46 €.
- Bezahlte Abkürzungen lohnen sich deshalb nicht.

Der eigentliche Wert liegt woanders: **Nach dem Durchstich kennst du deine
echten Stunden.** Liegst du am Stunden-Messpunkt (Di 29.12.) deutlich unter
dem Plan, ist deine Chance spürbar höher als hier gerechnet. Mit Bauzeiten wie
jemand, der programmieren kann, läge sie bei 21,58 von 100 (PLAN MIT HEBELN)
und 20,55 von 100 (DEIN PLAN). Liegst du darüber, gilt die Schnittliste aus
02, Abschnitt 8.

**Wo es steht:** [`02_BAUPLAN_APP1.md`](02_BAUPLAN_APP1.md) und
[`01_TAG_FUER_TAG_BIS_FEBRUAR.md`](01_TAG_FUER_TAG_BIS_FEBRUAR.md).

**Verworfen:** bezahlte Vorlagen (35–200 € und 5–15 Stunden Einarbeitung gegen
höchstens 15 gesparte Stunden; in DEIN PLAN bringt eine gesparte Stunde kein
Geld), App-Baukästen, fertige KI-Proxy-Dienste, Claude Max auf Verdacht, der
KI-Schlüssel in der App.

---

## 9. Was im Modell nichts ändert, aber Fehler vermeidet

Diese Punkte heben die Zahl nicht messbar. Sie verhindern, dass ein Lauf
unnötig schlecht ausgeht.

| Punkt | warum | steht in |
|---|---|---|
| **No-Go-Regel am Ideen-Tor:** Erreicht keine Idee die Mindestwerte, wird nicht gegründet und kein Apple-Konto gekauft | spart in diesem Fall alle Kosten; die Ideenwahl selbst hebt die Trefferquote nur wenig (×1,0 / 1,05 / 1,2) | [`04_IDEENWAHL.md`](04_IDEENWAHL.md) |
| K.-o.-Fragen zur Haftung und der Test gegen kostenlose Alternativen | als Einzelunternehmer haftest du persönlich; eine App, die ein kostenloser KI-Chat ersetzt, zahlt niemand | [`04_IDEENWAHL.md`](04_IDEENWAHL.md) |
| App zweisprachig, Videos auf allen drei Plattformen auf Deutsch, kein Englisch-Test vor Tor 1 | Reichweite ist an SIM und IP gebunden; der deutsche Markt ist kleiner (×0,8 / 0,9 / 1,0 auf die Trefferquote); ein Englisch-Test mit wenigen Posts misst nichts und kostet Zeit. Markt und Ideenwahl zusammen: 0,60 statt 0,59 von 100 | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md) |
| Wochenabo 6,99 € vorausgewählt, Monatsabo 14,99 €, keine Testphase, kein Jahresabo | entspricht den Marktwerten 2026; darunter zu bleiben verschenkt Umsatz, ein Jahresabo ohne Nachfolger ist eine Schuld | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md) |
| Small Business Program sofort beantragen | sonst behält Apple in den Startwochen 26 % statt 15 % (im Modell nicht gerechnet, Abschnitt 15) | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md) |
| Zweite Signalprüfung für eine App, die vor dem Abitur gestartet ist: 21 Tage nach dem ersten täglichen Post nach der letzten Prüfung, spätestens Di 29.06. (mit Nachprüfung am Tag nach der letzten Nachprüfung) | mit höchstens 3 Posts je Woche in Q4 kann eine App die 300 $ kaum zeigen; ohne zweite Prüfung würde ein Treffer zu früh abgeschrieben. Im Modell allein: 0,56 statt 0,59 von 100 | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md), Abschnitt 9.2 |
| Startpause im Abitur: Eine freigegebene App erscheint erst nach der letzten Prüfung | kostet im Modell nichts (ohne Startpause 3,73 statt 3,70 von 100) und hält das Abitur frei | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md), Abschnitt 1 |
| Keine bezahlte Verstärkung eigener Posts | je 50 € Einsatz bleiben netto −50 / −44 / −5 € | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md), Abschnitt 11 |
| Apps, die nach dem 04.07. erscheinen, nur mit Wochenabo | hält den Abschluss in jedem Fall möglich | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 3 |
| Automatische Verlängerung der Apple-Mitgliedschaft abschalten | sonst gehen im Winter 2027/28 noch einmal 99 € ab | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 4.4 |

---

## 10. Was nichts bringt oder verworfen wurde

Geprüft und im Modell ohne Wirkung oder schlechter (gepaarte Rangliste gegen
PLAN MIT HEBELN mit 3,71 von 100, Abschnitt 4.2):

| Idee | Gewinn in … von 100 | Ergebnis |
|---|---:|---|
| Tor 1 später (So 01.08. statt So 18.07.) | 3,38 | schlechter: späte Starts verdienen bis zum Verkaufsstopp kaum noch etwas |
| Tor 1 früher (So 04.07. / So 11.07.) | 2,69 / 3,54 | schlechter: der App fehlen ihre stärksten Wochen |
| höchstens zwei Apps | 2,86 | schlechter: die dritte App ist ein weiterer Versuch mit besserer Lernkurve |
| höchstens drei Apps | 3,62 | kein Unterschied |
| höchstens eine App (gegen DEIN PLAN mit 3,64) | 1,95 | deutlich schlechter |
| Signal schon ab 150 $ oder schon nach 2 Wochen | 3,18 / 3,18 | schlechter: Creator-Geld fließt öfter, bringt aber wenig |
| Creator-Geld bis 1.500 € statt 750 € | 3,65 | kein Unterschied |
| mehr Posts: bis zum Deckel von 10 Stunden je Woche statt 6,5 | 3,37 | schlechter: die Stunden fehlen dem Bau der nächsten App |
| ohne Wochendeckel für Posts | 2,80 | schlechter, aus demselben Grund |
| später gründen (bei 85 % fertiger App statt bei M2) | 3,85 | kaum Unterschied |
| Ruhezeit, aber mit App im Store im Abitur weiterbauen | 3,79 | kaum Unterschied; gegen die Abiturregel |
| Ideenwahl kürzer (5 statt 10 Stunden) | 4,03 | etwas besser, aber nicht empfohlen: Die Ideenwahl vermeidet sichere Verluste und spart bei einem No-Go alle Kosten (04, Abschnitt 1) |

Von der Gegenprüfung verworfen oder stark gekürzt:

- **Marketing:** Format-Raster, Wiederverwendung auf Reels und Shorts,
  Kommentare als Marke, klickbarer Download-Link, zweites Markenkonto. Alles
  sinnvolle Arbeitsweise, aber ohne belegte Wirkung; im Modell mit null
  angesetzt. Ein Post mit 100.000 Aufrufen bringt nach den korrigierten Werten
  etwa 50–150 Downloads und 20–70 $ Monatsumsatz (05, Abschnitt 8.4).
- **Paywall:** Exit-Angebot (Ablehnungsrisiko, +0–6 %), Testphase (Vorzeichen
  unbekannt), Paywall-Tests (unter etwa 1.000 Installationen je Variante
  messen sie nichts).
- **Idee:** rein deutsche Nische als eigener Hebel (kleinerer Markt, Chance
  auf große Ergebnisse sinkt), Saison (dünne Quellen; ganzjährige Themen sind
  die robuste Wahl), Vorab-Punkte für Beispielideen.
- **Zeit:** Nachhilfe, Wettbewerbe (Jugend forscht, Startup Teens, Jugend
  gründet, Shipaton), Job ab 14.06., Bitte um einen frühen Prüfungstermin.
- **Regelverstöße** (nicht tun, auch wenn sie naheliegen): Konten, die wie
  unabhängige Nutzer wirken; VPN oder Zweitgerät für andere Länder;
  automatisches Posten über inoffizielle Werkzeuge; gekaufte Aufrufe oder
  Bewertungen; erfundene Ergebnisse; Schalter „Testphase an/aus“; erfundene
  Dringlichkeit auf der Paywall; ein Elternteil nur als Name; Gewerbe erst
  nach den ersten Verkäufen anmelden; Bewertungen von dir, deiner Familie oder
  Freunden oder gegen eine Gegenleistung; Creator je Aufruf bezahlen;
  Ausgaben erfinden oder verschieben, um unter ~590 € Monatsgewinn zu
  bleiben; Abos nach der Gewerbeabmeldung weiterlaufen lassen; in App Store
  Connect „kein Händler“ angeben.

---

## 11. Der ganze Plan in Zahlen

DEIN PLAN, Stand 25.11.: Plan mit Hebeln, Übergabe oder Verkauf, Ferienjob ab
19.07. (ab 05.07., wenn keine App im Store ist). 300.000 Läufe.

**Geld nur aus der App** (einschließlich Abmeldung und Steuererklärung):

| | |
|---|---|
| Gewinn | in 3,7 von 100 Läufen |
| Median | −567 € |
| Mittel | −533 € |
| in 10 von 100 Läufen weniger als | −786 € |
| in 10 von 100 Läufen mehr als | −269 € |
| in 1 von 100 Läufen mehr als | +409 € |
| mehr als 500 € Verlust | in 65,3 von 100 Läufen |
| mehr als 1.000 € Verlust | in 0,5 von 100 Läufen |
| mehr als 5.000 € Verlust | in keinem Lauf |
| 10.000 € oder mehr | in 1 von 300.000 Läufen |

**Dein Geld** (App, Verkaufspreis, Lohn):

| | |
|---|---|
| im Plus | in 78,5 von 100 Läufen |
| mindestens 1.000 € | in 77,8 von 100 |
| mindestens 5.000 € | in 19,9 von 100 |
| mindestens 10.000 € | in 0,0 von 100 (rund 3 von 10.000) |
| 500.000 € | in keinem Lauf |
| in 10 von 100 Läufen weniger als | −590 € |
| in 25 von 100 Läufen weniger als | +3.920 € |
| **Median** | **+4.344 €** |
| in 25 von 100 Läufen mehr als | +4.775 € |
| in 10 von 100 Läufen mehr als | +5.515 € |
| in 1 von 100 Läufen mehr als | +6.167 € |
| Mittel | +3.518 € |
| unter 0 | in 21,5 von 100 Läufen |
| mehr als 500 € Verlust | in 14,6 von 100 Läufen |
| mehr als 1.000 € Verlust | in 0,1 von 100 Läufen |

Die schlechten Läufe sind die ohne Ferienjob (Lohn gibt es in 77,7 von 100
Läufen), in denen die App nichts einbringt.

**Mit dem Geld des Elternteils** (dazu eine Übergabe, abzüglich seiner
verlorenen Kosten): im Plus in 78,7 von 100 Läufen, Median +4.340 €, Mittel
+3.525 €; in 10 von 100 Läufen weniger als −592 €, in 10 von 100 mehr als
+5.530 €, in 1 von 100 mehr als +6.216 €.

**Woraus es sich zusammensetzt:**

| Teil | wie oft | wie viel |
|---|---|---|
| App allein | Gewinn in 3,7 von 100 Läufen | Median −567 €, Mittel −533 € |
| Ferienjob | Lohn in 77,7 von 100 Läufen | Median 5.001 € (Läufe mit Lohn), im Mittel aller Läufe 4.043 €; früher Beginn am Mo 05.07. in 17,0 von 100 |
| Verkauf | in 0,3 von 100 Läufen | im Mittel aller Läufe 7 € (dein Geld) |
| Übergabe | in 2,0 von 100 Läufen | im Mittel aller Läufe 16 € (Geld des Elternteils) |
| Anmeldung des Elternteils | in 8,5 von 100 Läufen | in 6,5 von 100 sind seine Kosten verloren, im Mittel aller Läufe 9 € |
| Creator-Geld | fließt in 2,9 von 100 Läufen | im Mittel aller Läufe 18 € |
| Verkaufsstopp | Abzug in 90,0 von 100 Läufen | im Mittel 69 € |

**Zeitpunkte:**

| | |
|---|---|
| Gründung | im Median in der Woche ab Mo 01.02.; in 10 von 100 Läufen schon bis zur Woche ab Mo 11.01., in 10 von 100 erst in der Woche ab Mo 07.06.; erst nach dem 31.01. in 57,3 von 100 Läufen; späte Gründung in der Woche ab Mo 07.06. in 10,2 von 100 |
| App 1 eingereicht | bis Di 02.02. in 0,6 von 100 Läufen, bis So 14.03. in 14,7, bis So 04.07. in 92,3; im Median in der Woche ab Mo 14.06. (unter den eingereichten Apps in 10 von 100 bis zur Woche ab Mo 22.02., in 25 bis zur Woche ab Mo 07.06., in 75 bis zur Woche ab Mo 21.06., in 90 bis zur Woche ab Mo 28.06.); in 7,7 von 100 Läufen nie, weil die Jagd am Stichtag endet |
| App 1 im Store | bis 14.03. in 9,3 von 100 Läufen, bis So 04.07. in 62,5; im Median ab der Woche ab Mo 28.06., unter den gestarteten Apps in 90 von 100 bis zur Woche ab Mo 12.07. |
| zweite App | startet in 61,9 von 100 Läufen, im Median in der Woche ab Mo 19.07.; bis Tor 1 im Store in 20,6 von 100 |
| Apps je Lauf | keine in 7,7, eine in 30,4, zwei in 33,4, drei oder mehr in 28,5 von 100 Läufen |
| eine App mit mindestens 300 $ MRR | in 28,7 von 100 Läufen |
| mit mindestens 1.000 $ MRR | in 8,2 von 100 |
| mit mindestens 5.000 $ MRR | in 0,0 von 100 |
| Wege ab Juli | Weg A in 100,0 von 100 Läufen; nur 2 von 300.000 Läufen enden anders |

**Geldeinsatz** (höchster Betrag, den du vorstreckst): Median 481 €, in 90 von
100 Läufen höchstens 621 €, in 99 von 100 höchstens 1.269 €, größter Wert
1.947 €. Die Grenze von 5.000 € hält in jedem Lauf, ein Nachschuss kommt nicht
vor. Die Familienversicherung endet in 1 von 300.000 Läufen.

---

## 12. Gegenproben

### 12.1 Wie empfindlich das Modell ist

Die Gewinnchance der App hängt stark an Annahmen, die niemand messen kann.
Jede Zeile ändert eine Annahme gegen DEIN PLAN (300.000 Läufe):

| Annahme in der Gegenprobe | Gewinn aus der App in … von 100 | dein Geld im Median | im Mittel |
|---|---:|---:|---:|
| **DEIN PLAN** | **3,70** | **4.344 €** | **3.518 €** |
| alter, schneller Start eines Treffers (1.000/3.000/8.000 $ MRR) | 8,32 | 4.356 € | 3.597 € |
| Umsatz läuft ohne Posts weiter (wie bisher) | 5,92 | 4.371 € | 3.609 € |
| Spitze ohne bezahlten Test nur um ein Viertel kleiner statt halb | 4,96 | 4.374 € | 3.557 € |
| Creator-Geld wirkt wie bisher angenommen (Spitze auf 70–100 %) | 3,65 | 4.342 € | 3.516 € |
| nach dem Ende der Jagd gar keine Posts mehr | 3,51 | 4.343 € | 3.520 € |
| die zweite Sprache kostet zusätzlich Stunden (+3/+6/+12 h) | 3,31 | 4.352 € | 3.526 € |
| langsameres Wachstum eines Treffers (×1,2/1,6/2,2 je Monat) | 2,77 | 4.334 € | 3.495 € |
| alte Werbekosten (45–49 % vom Umsatz) | 0,66 | 4.282 € | 3.433 € |

Für die Ehrlichkeit heißt das: **Die Gewinnchance der App liegt je nach
Annahmen grob zwischen 1 und 8 von 100.** 3,7 ist der Wert mit den Annahmen,
die am besten zu den Plänen und zu 05, Abschnitt 8.4 passen. Gemessen ist
keine davon. Dein Geld ändert sich dabei kaum, weil es am Ferienjob hängt.

### 12.2 Weitere Gegenproben zu DEIN PLAN

| Gegenprobe | Gewinn aus der App in … von 100 | dein Geld im Plus in … von 100 | Median | Mittel |
|---|---:|---:|---:|---:|
| **DEIN PLAN** | **3,70** | **78,53** | **4.344 €** | **3.518 €** |
| ganz ohne Creator-Geld | 4,54 | 78,79 | 4.356 € | 3.537 € |
| App 2 schon während des Reviews, mit Code | 4,79 | 78,64 | 4.367 € | 3.535 € |
| ohne Vorbereitung von App 2 im Review | 3,52 | 78,44 | 4.339 € | 3.510 € |
| Schnittliste von Anfang an | 3,95 | 78,71 | 4.342 € | 3.521 € |
| App 1 um 15 % kleiner (nicht planbar) | 4,37 | 78,67 | 4.316 € | 3.475 € |
| kürzere Lernzeit aus 01 (12/15/20 statt 20/28/40 h) | 4,65 | 78,66 | 4.320 € | 3.470 € |
| ohne Startpause (eine freigegebene App erscheint auch im Abitur) | 3,73 | 78,61 | 4.341 € | 3.515 € |
| Posts bis zum Deckel von 10 h je Woche | 3,47 | 78,51 | 4.337 € | 3.513 € |
| ohne Wochendeckel für Posts | 2,92 | 78,43 | 4.324 € | 3.501 € |
| Zeitarbeit ab 05.07. klappt immer | 3,79 | 78,47 | 4.448 € | 3.660 € |
| Stichtag 04.07. nur, wenn noch keine App eingereicht ist | 3,51 | 78,50 | 4.276 € | 3.355 € |
| ohne Stichtag 04.07. (Job erst ab 19.07.) | 3,53 | 78,46 | 4.260 € | 3.307 € |
| kurzer Job bis Di 31.08. | 3,70 | 78,62 | 3.363 € | 2.754 € |
| Job ab 05.07., wenn am 04.07. keine App 300 $ MRR zeigt | 2,85 | 78,34 | 5.413 € | 4.188 € |
| falls ein Betrieb mit Tariflohn ab 19.07. zusagt | 3,76 | 78,58 | 4.753 € | 3.831 € |
| **nur Ferienjob ab 05.07., keine App, keine Gründung** | – | 77,49 | 6.031 € | 4.778 € |
| nur Ferienjob, falls ein Betrieb mit Tariflohn zusagt | – | 77,56 | 6.561 € | 5.170 € |

### 12.3 Nur die App: PLAN MIT HEBELN

Ohne Nachfolger und ohne Job (300.000 Läufe):

| Gegenprobe | Gewinn in … von 100 | Median | Mittel |
|---|---:|---:|---:|
| **PLAN MIT HEBELN** | **3,73** | **−564 €** | **−528 €** |
| ohne Testgeld (kein Creator-Geld) | 4,63 | −558 € | −511 € |
| Bauzeiten wie bisher angesetzt (80/140/280 h) | 2,91 | −573 € | −545 € |
| strengerer Markt 2027 | 2,56 | −578 € | −554 € |
| die zweite Sprache kostet zusätzlich Stunden | 3,25 | −568 € | −537 € |
| Verkaufsstopp schon am Sa 31.07. (Dienstende Di 31.08.) | 1,18 | −602 € | −594 € |
| Verkauf bis Di 31.08. (Dienst bis Fr 01.10., nur nach Beratung) | 8,77 | −529 € | −450 € |

Mit Übergabe oder Verkauf, aber ganz ohne Creator-Geld: Gewinn aus der App in
4,57 von 100 Läufen; dein Geld im Plus in 4,68 von 100, Median −558 €, Mittel
−506 €; mit dem Geld des Elternteils im Plus in 5,14 von 100, Mittel −499 €.

### 12.4 So liest du das

- **Creator-Geld kannst du weglassen.** Ohne ist die Gewinnchance der App
  höher (4,54 statt 3,70 von 100; gepaart 4,58 statt 3,64), und dein Geld ist
  gleich oder etwas höher. Auch die seltenen großen Ergebnisse werden ohne
  Creator-Geld nicht seltener (10.000 € oder mehr mit dem Geld des
  Elternteils: 0,06 statt 0,04 von 100). Der Grund: Creator-Geld hebt die
  Spitze nur um 5–15 %, kostet aber 60–150 € je Video (05, Abschnitt 10). Die
  Entscheidung liegt bei dir. Behältst du es, gelten die Regeln aus 05,
  Abschnitt 10: nur nach bestandenem Signal, für alle Apps zusammen bis
  So 18.07. höchstens 750 €.
- **Geld gegen Chance.** Beginnst du den Job schon am Mo 05.07., sobald keine
  App 300 $ MRR zeigt, hast du im Mittel 670 € mehr (im Median 1.069 €). Dafür
  sinkt die Gewinnchance der App von 3,70 auf 2,85 von 100, weil ihr die zwei
  Wochen mit den meisten Stunden fehlen. Das setzt einen Vertrag ab 05.07.
  voraus. Der Plan bleibt beim Stichtag ohne Schwelle.
- **Was das Projekt kostet.** Ohne App und ohne Gründung brächte ein Job ab
  05.07. im Mittel 4.778 €, im Median 6.031 €. Dein Plan bringt im Mittel
  3.518 €, im Median 4.344 €. Der Unterschied von 1.260 € im Mittel (im
  Median rund 1.690 €) ist der Preis für das Lernprojekt samt der kleinen
  Chance auf mehr. Mit Tariflohn ist der Unterschied im Mittel etwa gleich
  groß, rund 1.260 € (gerechnet 1.339 €; der Vergleich ohne App ist dort um
  rund 78 € zu günstig, Abschnitt 15).
- **Die Hebel halten auch im schlechteren Fall:** Mit den alten Bauzeiten oder
  im strengeren Markt sinkt die Chance der App auf 2,91 bzw. 2,56 von 100; der
  Medianverlust bleibt bei 573 € bzw. 578 €.
- **Die Startpause kostet nichts** (3,73 ohne, 3,70 mit). Auch ganz ohne Posts
  nach dem Ende der Jagd ändert sich wenig (3,51 von 100).

---

## 13. Was du dafür tun musst – die Liste

| wann | was | Stunden | steht in |
|---|---|---|---|
| Do 26.11. | Elterngespräch: Namensfrage ansprechen und fragen, ob ein Elternteil eine laufende App im Sommer übernehmen würde | 1 | Hauptplan, Abschnitte 3 und 11 |
| Sa 28.11.–Sa 19.12. | fünf Ideen prüfen mit K.-o.-Fragen, Nachfrageprüfung, Bewertungstabelle, Slideshow-Test und Ablauf-Test | 10–16, typisch 12 | [`04_IDEENWAHL.md`](04_IDEENWAHL.md), Abschnitt 2 |
| Sa 12.12. | Zwischenstand: erfüllt eine Idee alle Mindestwerte? | in den 12 Stunden | [`04_IDEENWAHL.md`](04_IDEENWAHL.md), Abschnitt 7 |
| bis So 13.12. | Namensfrage entscheiden (Entscheidung mit den Eltern am Fr 11.12.) | 1 | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 2 |
| Mo 14.–Mi 16.12. | Apple Developer Program kaufen (99 €), automatische Verlängerung abschalten – nur wenn der Zwischenstand passt, die Namensfrage entschieden ist und IHK oder Gewerbeamt zugestimmt haben ([03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 4.1) | 1 | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 4 |
| Sa 19.12. | Ideen-Tor mit No-Go-Regel; die zweitbeste Idee als Reserve für App 2 merken | in den 12 Stunden | [`04_IDEENWAHL.md`](04_IDEENWAHL.md), Abschnitt 7 |
| Di 29.12. | **Stunden-Messpunkt** nach dem Durchstich: Stunden für AP1–AP9 notieren. Über ~40 Stunden gilt die Schnittliste. Darunter entscheidest du, ob du sie trotzdem von Anfang an nimmst (+0,28 Punkte, Abschnitt 4.1) | 0,25 | [`02_BAUPLAN_APP1.md`](02_BAUPLAN_APP1.md), Abschnitt 8 |
| Sa 02.01. (spätestens Sa 30.01.) | drei Bewerbungen für den Ferienjob, befristet 19.07.–10.09., zuerst Betriebe mit Tariflohn | 1–2 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitte 2.2 und 2.3 |
| Januar | schriftliche Zusage des Elternteils (eine Seite, bis So 31.01.; in 01 am Sa 16.01.); Oberstufenkoordination fragen, wann die mündlichen Prüfungen liegen | 1 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitte 2.2 und 4.1 |
| Dezember bis Februar | Gründung: Kleinunternehmer im Fragebogen, Gründungsberatung (wenn kostenlos), Frage ans Finanzamt, Small Business Program am selben Tag wie der Vertrag für bezahlte Apps | ~9 (davon ~3,5 am Gründungstag und bei Apple) | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 5 |
| ab KW 48, am ersten Samstag jedes Monats | Belegtabelle führen | 20–30 Minuten je Monat | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 7.1 |
| ab der Gründung, jeden Sonntag | Kassenprüfung; ab dem Start mit Wochenauswertung und Support | 10 Minuten je Woche, ab dem Start 0,4–0,6 Stunden | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 7.3 |
| So 14.03. | Ruhezeit entscheiden: keine App im Store oder im Review → Claude Pro ruht bis nach der letzten Prüfung | 0,2 | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 7.4 |
| solange App 1 im Review ist (typisch Mitte bis Ende Juni; nicht in der Prüfungszeit) | **App 2 ohne Code vorbereiten:** `SPEC.md` aus der Reserve-Idee, Fragenliste, Store-Texte, Icon-Entwurf. Den Code beginnst du erst nach der Freigabe aus der Vorlage | bis 6 | [`02_BAUPLAN_APP1.md`](02_BAUPLAN_APP1.md), Abschnitt 9; [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 1.2 (KW 24) |
| vor der ersten Creator-Buchung | **Entscheidung zum Creator-Geld:** ganz weglassen (im Modell besser, Abschnitt 4.1) oder nach den Regeln aus 05 nutzen | – | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md), Abschnitt 10 |
| Mo 21.06. | **Zeitarbeitsanfrage, in jedem Fall:** zwei Zeitarbeitsfirmen für einen festen Termin anfragen – ohne unterschriebenen Vertrag für den ganzen Sommer, mit Vertrag ab 19.07. für Mo 05.07.–Fr 16.07. Welcher Termin gilt, entscheidest du am Fr 25.06. | 1 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitte 2.2 und 2.4 |
| Fr 25.06. | Vorentscheidung: App im Store oder im Review → Beginn Mo 19.07., sonst Mo 05.07. | 10 Minuten | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitte 2.2 und 2.10 |
| Mo 28.06., spätestens Di 29.06. | MRR je App notieren (für die Anmeldung des Elternteils); zweite Signalprüfung für eine App, die vor dem Abitur gestartet ist (21 Tage nach dem ersten täglichen Post nach der letzten Prüfung; mit Nachprüfung am Tag nach der letzten Nachprüfung) | 0,2 | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md), Abschnitt 9.2; 06, Abschnitt 4.4 |
| bis Fr 02.07. | zeigt eine App am Mo 28.06. ~100 $ MRR und liegt die Zusage vor: Elternteil schickt Gewerbe- und Apple-Anmeldung ab | 2–4 (Elternteil) | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 4.4 |
| So 04.07. | Stichtag: keine App im Store → die Jagd endet, Job ab Mo 05.07. über die Zeitarbeitsfirma | – | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 2.10 |
| So 18.07. | Tor 1; am Mo 19.07. Jobbeginn und alles kündigen, was nicht gebraucht wird | 1 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 1 |
| bis Sa 31.07. | je App entscheiden: einstellen, übergeben oder verkaufen | 1 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 3 |
| So 15.08. | ohne Nachfolger: alle Abos aus dem Verkauf nehmen | 0,5 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 6 |
| Mi 15.09. und Do 16.09./Fr 17.09. | Dienstende; danach App entfernen, Gewerbe abmelden | 4–6 (Schätzung) | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 6 |
| Frühjahr 2028 | EÜR und Steuererklärung 2027 über ELSTER; die Lohnsteuer kommt zurück | 6–12 | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 8.2 |

---

## 14. Die Werte im Modell

Alle Werte sind Dreiecke aus niedrigstem, typischem und höchstem Wert.
B = belegt, S = Schätzung, P = Regel aus den Plänen.

### 14.1 Was die Hebel ändern

| Größe | Ausgangslage | PLAN MIT HEBELN | Quelle |
|---|---|---|---|
| Faktor auf die Trefferquoten | 1,0 | 0,8 / 0,95 / 1,2 (deutscher Markt ×0,8 / 0,9 / 1,0, Ideenwahl ×1,0 / 1,05 / 1,2) | S |
| Startumsatz ohne bezahlten Test (Anteil) | 0,2 / 0,4 / 0,7 | 0,2 / 0,42 / 0,7 (Slideshow-Filter der Ideenwahl) | S |
| Bauzeit App 1 (Stunden) | 80 / 140 / 280 | 78 / 130 / 260 | S |
| Bauzeit weitere Apps | 35 / 60 / 120 | 33 / 55 / 110 | S |
| Lernstunden ab Mo 30.11. | 20 / 30 / 40 | 20 / 28 / 40, vorsichtig gerechnet; die Gegenprobe mit 12 / 15 / 20 steht in Abschnitt 12.2 | S; Hauptplan, Abschnitt 7: Lernpfad ~15–40 Stunden, 01 plant das untere Ende |
| Review in Wochen | 0,5 / 1,5 / 4,0 | 0,4 / 1,2 / 3,0 | S |
| App 2 vorbereiten, solange App 1 im Review ist | – | bis 6 Stunden, ohne Code | S; Code erst nach der Freigabe (02, Abschnitt 9) |
| Gründung (€) | 150 / 250 / 450 | 140 / 200 / 380 | B/S; 03, Abschnitt 1.2 |
| Kosten je Monat vor dem ersten Start | 35 / 60 / 110 | 23 / 28 / 45 | B; 03, Abschnitt 1.2 |
| Kosten je Monat nach dem Start | 35 / 60 / 110 | 23 / 30 / 75 | B; 03, Abschnitt 1.2 |
| Ruhezeit im Abitur (15.03.–07.06.) | keine; im Abitur wird mit wenigen Stunden weitergebaut | ohne App im Store oder im Review 0 Stunden und 2 / 5 / 30 € je Monat ab Mo 29.03.; mit App nur Betrieb, mindestens ~50 € je Monat | B/P; 03, Abschnitt 1.2; Hauptplan, Abschnitt 4 |
| Zusatzkosten Claude Max je Monat | 0 / 10 / 70 | 0 / 0 / 12 | B/S |
| Kosten je Monat nach dem Ende der Jagd | 10 / 25 / 50 | 5 / 12 / 35 | S; 03, Abschnitt 1.2 |
| Abschluss (€) | 0 / 300 / 800 | 20 / 80 / 500 | S; 03, Abschnitt 1.2 |
| zweite Signalprüfung | – | in der Woche ab Mo 28.06., für Apps mit Start vor dem 15.03. | P; 05, Abschnitt 9.2 |

### 14.2 Pflicht und Korrekturen vom 25.11.

Sie gelten in allen Hebel-Szenarien, auch in der Ausgangslage.

| Größe | Wert | Quelle |
|---|---|---|
| umsatzabhängige Kosten je App | 15 / 18 / 20 % vom Bruttoumsatz: Umsatzsteuer im Preis 0,136, KI-API 0,001–0,005, Erstattungen 0,014–0,057 (vorher 45–49 % Werbung aus dem alten 500k-Modell) | P/B; 05, Abschnitte 2.1 und 2.8; Hauptplan, Abschnitt 7; 06, Abschnitt 3 |
| Apple-Anteil | 15 % ab dem ersten Verkauf (Small Business Program) | B; der Regelsatz davor fehlt (Abschnitt 15) |
| Start eines Treffers | 300 / 1.000 / 3.000 $ MRR in den ersten Wochen (vorher 1.000 / 3.000 / 8.000) | S; an 05, Abschnitt 8.4 kalibriert |
| Spitze einer App ohne bezahlten Test | ×0,5: halb so hoch; im Plan startet jede App so (Signalregel) | S; an 05, Abschnitt 8.4 geprüft |
| Creator-Geld nach dem Signal | hebt die Spitze um 5 / 10 / 15 % (vorher auf 70–100 % der möglichen Spitze) | S; 05, Abschnitte 6.1 und 10 |
| Umsatz ohne Posts | in der Prüfungszeit 5 / 10 / 15 % weniger je Woche (Faktor 1,0 auf den Rückgang ohne Werbung), nach dem Ende der Jagd die Hälfte davon (Faktor 0,5) | S; 05, Abschnitte 6.3 und 6.4; 06, Abschnitt 4.7 |
| Wochenprogramm für Posts und Tests | vor dem Abitur höchstens 1,5 Stunden je Woche, danach 6,5; der Rest baut weiter. Im Median erreicht die größte Post-Woche genau 6,5 Stunden | P; 05, Abschnitte 6.1, 6.2 und 6.4 |
| Vorlage für App 2 | +3,5 Stunden; App 2 beginnt erst nach der Freigabe von App 1 | P; 02, Abschnitt 9 |
| Stunden-Messpunkt | braucht App 1 mindestens 141 Stunden (AP1–AP9 über ~40), gilt die Schnittliste: Stunden ×0,938 (−6,2 %), dazu 3 Stunden für Version 1.1 nach dem Start | P/S; 02, Abschnitt 8; 01, Abschnitt 11 |
| Nebenstunden | Liste unten | P; 01–06 |
| Gründung | 6 statt 4 Stunden, über mindestens zwei Wochen; ist M2 bis Mo 01.03. nicht erreicht, in der Woche ab Mo 07.06. (späte Gründung) | P; 03, Abschnitte 5 und 5.1 |
| Vorentscheidung | Stand am So 27.06. (Plan: Fr 25.06., Abschnitt 15): App im Store oder im Review → 19.07. genannt | P; 06, Abschnitte 2.2 und 2.10 |
| Zeitarbeit für die zwei Wochen ab Mo 05.07. | kurzfristig (19.07. genannt): Chance 30 / 50 / 70 von 100; mit Vorlauf (Anfrage Mo 21.06.): 50 / 70 / 85 von 100 | S; 06 nennt keine Zahl |
| Stichtag | So 04.07.: ohne App im Store endet die Jagd, mit oder ohne Job; eine eingereichte App darf noch erscheinen | P; 06, Abschnitt 2.10 |
| Familienversicherung | endet bei einem Jahresgewinn über 12 × 590 €, hochgerechnet bis zum Dienstende; dann 280 € je Monat | B/P; Hauptplan, Abschnitt 4 |
| Exit (alter Verkauf der Firma zum Vielfachen des Jahresgewinns) | aus; verkauft wird nur wie in 06, Abschnitt 5 | P |
| Verkaufsstopp ohne Nachfolger | So 15.08., Dienstende Mi 15.09. | B (Apple) |

**Nebenstunden, die dem Bau fehlen** (typische Werte):
- Ideenwahl ab Mo 30.11. 10 Stunden: KW 49 2,75, KW 50 2,25, KW 51 5 (04,
  Abschnitt 2; der Sa 28.11. liegt vor dem Start des Modells).
- Verwaltung und ELSTER 1 Stunde (KW 49), Entscheidung mit den Eltern
  1 Stunde (Fr 11.12.), Apple Developer Program 1 Stunde (Mo 14.12.).
- Weihnachtsferien: Bankkonto 0,75 Stunden, Bewerbungen für den Ferienjob
  1,5 Stunden, ETH-Bewerbung 6 Stunden.
- Gründungsberatung 2,5 Stunden (bis Mi 06.01.); Sozialversicherungsnummer
  0,25 Stunden, Zusage des Elternteils und Frage an die
  Oberstufenkoordination 1 Stunde, Halbjahreszeugnis in eApply 0,25 Stunden
  (alle im Januar).
- Gründung 6 Stunden; Kassenprüfung 10 Minuten je Woche ab der Gründung; ab
  dem ersten Start Kassenprüfung, Wochenauswertung und Support 0,4 / 0,5 / 0,6
  Stunden je Woche (03, Abschnitt 7.3).
- Markenkonten und Featuring-Nominierung 1,83 Stunden je Einreichung (05,
  Abschnitt 1.1); Vorbereitung der Posts (V1–V4) 3,5 Stunden nach der
  Einreichung von App 1 (05, Abschnitt 4).
- Ferienjob: Gespräche in Q4 1 Stunde, Vertrag und Anfrage an die
  Krankenkasse 1,25 Stunden (06, Abschnitt 2.2), Zeitarbeitsanfrage 1 Stunde
  (Mo 21.06., 06, Abschnitt 2.4).
- Zürich: Zimmersuche 2 Stunden (KW 24), Finanzierungsbrief 1 Stunde
  (KW 25), Abiturzeugnis 1 Stunde (KW 26), Bewerbung in Hannover 2 Stunden
  (KW 28; 06, Abschnitt 1.2); ab Mo 05.07. 6 Stunden je Woche für Zürich und
  Mathe.

### 14.3 Nachfolger und Ferienjob

| Größe | Wert | Quelle |
|---|---|---|
| Übergabe | ab 150 € Monatsgewinn; Anmeldung des Elternteils nur bei mindestens 100 $ MRR am Mo 28.06.; Chance 25 / 40 / 60 von 100 (ohne feste Zusage 10 / 25 / 45); 0,7 / 2 / 5 Monatsgewinne in den zwölf Monaten ab Mo 09.08.; Kosten des Elternteils 120 / 140 / 165 € | S; 06, Abschnitte 3, 4.4 und 4.7 |
| Verkauf | ab 300 $ Monatsumsatz und 8 vollen Wochen im Store bis So 08.08.; Chance 10 / 25 / 45 von 100; netto 1,7 / 4,3 / 10,3 Monatsgewinne | S; 06, Abschnitt 5 |
| Stand der Entscheidung | Monatsgewinn der vier Wochen bis So 01.08., Stand bis Sa 07.08.; ab Mo 09.08. gehören die Erlöse dem Nachfolger | P; 06, Abschnitte 3 und 4.5 |
| Ferienjob | 560 / 600 / 690 € je Woche nach Fahrtkosten, ab Mo 19.07. (früh ab Mo 05.07.) bis Fr 10.09.; Chance auf einen Job 70 / 78 / 85 von 100; neben dem Job höchstens 5 Stunden je Woche für die Apps | B/S; 06, Abschnitte 1.3, 2.3 und 2.8 |
| Betrieb mit Tariflohn (nur Gegenprobe) | 610 / 660 / 730 € je Woche ab 19.07.; die frühen Wochen zum Zeitarbeitslohn | S; 06, Abschnitt 2.3 |

### 14.4 Unverändert

5.000 € Einsatz mit harter Grenze, Kalender Niedersachsen, Stunden je Woche,
erst bauen und bei halb fertiger App gründen, Startpause vom 15.03. bis zur
letzten Prüfung, Tore am So 18.07. (5.000 $ MRR) und So 08.08. (10.000 $),
Signalregel (300 $ MRR drei Wochen nach dem Start, für alle Apps zusammen bis
18.07. höchstens 750 € Creator-Geld), strenge Trefferquoten (Chance einer App
auf mindestens 1.000 $ MRR 0,10 / 0,18 / 0,30) mit Lernkurve (×0,3 / 0,6 / 0,85
/ 1,0 für App 1 bis 4), Wachstum eines Treffers ×1,5 / 2,2 / 3,0 je Monat.

---

## 15. Grenzen dieser Rechnung

- **Am wichtigsten: Die Gewinnchance hängt stark an Annahmen, die niemand
  messen kann.** Wie schnell ein Treffer startet und wächst, wie stark der
  Umsatz ohne Posts fällt, wie hoch die Spitze ohne bezahlten Test ist und
  welche Kosten vom Umsatz abgehen, hat niemand für eine App wie deine
  gemessen. Je nach Annahme liegt die Gewinnchance der App grob zwischen 1 und
  8 von 100 (Abschnitt 12.1). Dein Geld hängt dagegen fast nur am Ferienjob.
- **Die Hebelwerte sind Schätzungen.** Belegt sind Preise, Gesetze und Apples
  Regeln. Wie viel schneller du baust, wie gut deine Ideenwahl ist und ob ein
  Elternteil am Ende wirklich übernimmt, weiß vorher niemand.
- **Die Trefferquoten stammen aus Marktberichten für alle neuen Abo-Apps**
  (RevenueCat 2026: 17,3 % erreichen in zwei Jahren 1.000 $ Monatsumsatz).
  Für einen Einzelnen ohne Erfahrung, mit deutschen Videos ohne Gesicht und
  nur einem Sommer gibt es keine Messung. Das Modell rechnet deshalb mit
  niedrigeren Quoten und einer Lernkurve.
- **Bewusst nicht oder vereinfacht gerechnet.** Die Wirkungen haben die
  Prüfungen am 25.11. mit 5.000 bis 20.000 Läufen auf Zwischenständen des
  Modells geschätzt. Die letzten drei Zeilen hat die fünfte Prüfung gefunden
  (Code von Commit 280b3eb, 5.000 gepaarte Läufe, Wirkung für DEIN PLAN); sie
  sind noch nicht eingearbeitet:

  | Punkt | im Modell | Wirkung |
  |---|---|---|
  | Lieferzeit der Creator (1–2 Wochen, 05, Abschnitt 10) | Creator-Videos wirken ohne Verzug | rund −0,01 bis −0,1 Punkte |
  | Regelsatz vor dem Small Business Program (bis zur Genehmigung behält Apple in den EU-Stores 26 %, 03, Abschnitt 6.2) | 15 % ab dem ersten Verkauf | rund 0 € (unter 1 €) |
  | Kosten nach dem 29.08. (Dienst bis Mi 15.09., Domain bis zur letzten Apple-Zahlung, Claude Pro bis zu den EÜR-Summen) | fehlen | dein Geld läge um rund 10–20 € niedriger |
  | Nebenstunden, die in ihrer Woche keinen Platz finden | verfallen, statt zu rutschen | rund ±1 € |
  | Vorentscheidung | Stand am So 27.06. statt Fr 25.06. | mit dem Freitag läge dein Geld um rund 11–14 € höher |
  | Länderpreise (Schweiz, USA) und das reine Wochenabo nach dem 04.07. | nur die deutschen Preise, beide Abos | nicht nachgerechnet; die Pläne nennen dafür keine Zahl |
  | Einkommensteuer | keine | fiele in 3 von 5.000 Läufen an, im Mittel rund 2 €. In den übrigen Läufen bleibt das zu versteuernde Einkommen (Gewinn aus dem Gewerbe mit Verkaufserlös plus Lohn, minus 1.230 € Arbeitnehmer-Pauschbetrag und weitere Abzüge) unter dem Grundfreibetrag (2026: 12.348 €, der Wert für 2027 ist offen) |
  | zweite Ideenrunde nach einem No-Go (~12 Stunden, 04, Abschnitt 7) und eine mündliche Nachprüfung (Mo 28.06.–Mi 30.06.) | nicht gerechnet | – (die Pläne nennen keine Wahrscheinlichkeit) |
  | Lernzeit: Der Hauptplan nennt für den Lernpfad ~15–40 Stunden; 01 plant das untere Ende (eigene Lernzeit ~7,5 Stunden und 10 Minuten je Sitzung) | vorsichtig 20 / 28 / 40 Stunden ab 30.11. | mit 12 / 15 / 20 Stunden: 4,65 statt 3,70 von 100, dein Geld im Mittel 3.470 € statt 3.518 € (Abschnitt 12.2) |
  | Umsatz nach dem Ende der Jagd: 05, Abschnitt 6.4 kürzt die Posts nur mit Ferienjob (höchstens ein Post am Tag) und nach dem Verkaufsstopp | der halbe Rückgang aus Abschnitt 14.2 gilt auch in Läufen ohne Job | ohne den Rückgang in diesen Läufen +0,30 Punkte und +5,5 € im Mittel; in PLAN MIT HEBELN, das keinen Job hat, +1,80 Punkte |
  | Start in Q4 mit höchstens 3 Posts je Woche (05, Abschnitte 6.1 und 8.4: 9 Posts in drei Wochen bringen rund 1–20 $ MRR) | eine App startet in Q4 so stark wie im Sommer | mit einem Viertel des Startumsatzes (Faktor 0,25) −0,56 Punkte und −16 € im Mittel; dass ein Start in Q4 auch langsamer wächst, ist darin noch nicht enthalten |
  | Nein in der gültigen Signalprüfung (05, Abschnitt 9.3: danach 1 Post am Tag für diese App) | nicht eigens geregelt; der Umsatz der App wächst weiter | −0,12 Punkte und −7 € im Mittel |

  Zusammen machen die drei neuen Zeilen etwa −0,4 Punkte aus: Die
  Gewinnchance der App läge eher bei 3,3 als bei 3,7 von 100. Das liegt
  innerhalb der Spanne, die die Gegenproben zeigen (Abschnitt 12.1).
- **Der Vergleich „nur Ferienjob, falls ein Betrieb mit Tariflohn zusagt“**
  (Abschnitt 12.2) ist nach der fünften Prüfung um rund 78 € im Mittel zu
  günstig. Dort zählen die zwei frühen Wochen ab Mo 05.07. zum Tariflohn, in
  DEIN PLAN mit Tariflohn dagegen zum Zeitarbeitslohn (Abschnitt 14.3; 06,
  Abschnitt 2.8). Ohne diesen Fehler läge sein Abstand zu DEIN PLAN mit
  Tariflohn im Mittel bei rund 1.260 € statt 1.339 €.
- **Creator-Geld weglassen** bringt bei sonst gleichen Entscheidungen
  +1,08 Punkte und +16 € im Mittel (fünfte Prüfung; in der Rangliste,
  Abschnitt 4.1, +0,94 Punkte und +18 €).

- **Der Wert nach dem Sommer** gehört bei einer Übergabe dem Elternteil. In
  „dein Geld“ steht nur ein Verkaufspreis; die Übergabe zählt nur „mit dem
  Geld des Elternteils“.
- **Der Ferienjob zählt mit dem vollen Lohn,** obwohl ein Teil (die
  Lohnsteuer) erst 2028 zurückkommt und der Augustlohn oft erst Mitte
  September ausgezahlt wird.
- **Zwei Hinweise außerhalb der App,** beide ungeprüft: Auslands-BAföG für ein
  ganzes Studium in der Schweiz und ein Stipendium über einen Schulvorschlag.
  Beides kann mehr Geld bedeuten als jeder Hebel in diesem Dokument. Näheres
  in [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 8.
