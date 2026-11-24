# Hebel: Was Chance und Ergebnis wirklich erhöht

Gehört zu [`../APP_PLAN_ALLEIN_MIT_CLAUDE.md`](../APP_PLAN_ALLEIN_MIT_CLAUDE.md).
Hier steht, **welche Stellschrauben das Ergebnis verbessern, um wie viel, und
was du dafür tun musst.** Die Schritte selbst stehen in den anderen
Detailplänen (Verweise jeweils am Hebel).

Stand: 24.11.2026. Gerechnet mit [`plan/plan_500k.py`](../../plan/plan_500k.py),
Szenarien „Hebel: …“, je 300.000 Läufe.

Inhalt:
1. [Das Ergebnis in Kürze](#1-das-ergebnis-in-kürze)
2. [Eine Korrektur vorweg: der Verkaufsstopp](#2-eine-korrektur-vorweg-der-verkaufsstopp)
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

| Stufe | nur die App: Gewinn in … von 100 Läufen | alles zusammen im Plus in … von 100 | Geld im Median | im Mittel |
|---|---:|---:|---:|---:|
| Plan vom 23.11., wie er dastand | 6,2 | 6,2 | −1.136 € | −954 € |
| derselbe Plan, richtig gerechnet (Abschnitt 2) | 2,7 | 2,7 | −1.184 € | −1.074 € |
| + geprüfte Hebel: Kosten, Bau, Ideenwahl, Signal | 8,8 | 8,8 | −558 € | −393 € |
| + Nachfolger: ein Elternteil hat die Übernahme zugesagt, sonst Verkaufsversuch | 12,0 | 17,9 | −544 € | +76 € |
| + Ferienjob ab 19.07. (ab 05.07., wenn keine App im Store ist) = **dein Plan, Stand 24.11.** | 11,1 | **81,8** | **+3.191 €** | +3.158 € |

Was das heißt:

- **Die App allein bleibt im Normalfall ein Verlust.** Die Hebel halbieren ihn
  aber: von rund 1.180 € auf rund 560 € im Median. Mehr als 1.000 € Verlust
  gibt es nur noch in etwa 1 von 100 Läufen (vorher in 73 von 100).
- **Die Gewinnchance der App steigt von 2,7 auf 9 bis 12 von 100.** Das ist
  der ehrliche Vergleich, weil die 6,2 vom 23.11. zu günstig gerechnet waren.
- **Sicheres Geld kommt nicht aus der App, sondern aus dem Ferienjob**, den du
  beginnst, sobald die Jagd endet. Mit ihm endet der Sommer in rund 82 von
  100 Läufen im Plus, im Median mit rund 3.200 €.
- **500.000 € erreicht weiterhin kein einziger Lauf.** 10.000 € oder mehr
  gibt es im ganzen Plan in 1,8 von 100 Läufen.
- **Rein nach Geld gerechnet wäre „nur Ferienjob, keine App“ besser**
  (Abschnitt 12). Die App kostet dich im Mittel rund 700 € gegenüber diesem
  Weg. Dafür bekommst du eine eigene App im Store, Programmier- und
  Marketingerfahrung vor dem Studium und eine kleine Chance auf mehr.

---

## 2. Eine Korrektur vorweg: der Verkaufsstopp

Die Gegenprüfung hat eine Pflicht gefunden, die der Plan vom 23.11. nicht
gerechnet hatte.

**Die Regel.** Apple schreibt für Abos vor: „A minimum of 31 days is required
from the date subscription is removed from sale and service is stopped.“
([Apple, Verfügbarkeit von Abos](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription/))
Nimmst du ein Abo aus dem Verkauf, gibt es keine neuen Abschlüsse und keine
Verlängerungen mehr. Danach muss der Dienst noch mindestens 31 Tage laufen.

**Die Folge.** Du ziehst vor dem 20.09. nach Zürich und beendest das Gewerbe
vorher. Dann kannst du nicht bis 31.08. verkaufen und am 31.08. abschalten.
Der Plan vom 23.11. hat aber die Einnahmen bis 31.08. voll gezählt. Viele
seiner Gewinnläufe verdienten ihr Geld erst im August.

**Was jetzt gilt** (wenn es keinen Nachfolger gibt):

| Schritt | Tag |
|---|---|
| Alle Abos aus dem Verkauf nehmen | So 15.08.2027 |
| Dienst läuft weiter (Server, KI), ohne neue Einnahmen | bis Mi 15.09.2027 |
| App entfernen, Gewerbe abmelden | Do 16.09. oder Fr 17.09., vor dem Umzug |

Ziehst du früher um, rücken beide Tage vor: Dienstende spätestens am Tag vor
dem Umzug, Verkaufsstopp 31 Tage davor.

**Wie viel der Stichtag ausmacht** (Plan mit Hebeln, ohne Nachfolger):

| Verkaufsstopp | Dienstende | Gewinn in … von 100 | Geld im Median | im Mittel |
|---|---|---:|---:|---:|
| Sa 31.07. | Di 31.08. | 3,4 | −600 € | −503 € |
| **So 15.08.** | **Mi 15.09.** | **8,8** | **−558 €** | **−393 €** |
| Di 31.08. | Fr 01.10. (Betrieb nach dem Umzug, nur nach Beratung) | 14,4 | −518 € | −261 € |

Jede Woche, die du länger verkaufen darfst, zählt, weil dein Zeitfenster erst
im Juni beginnt. Deshalb ist die Frage „Wer führt die App nach dem Sommer
weiter?“ kein Nebenthema, sondern der zweitgrößte Hebel (Abschnitt 6).

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
   (Abschnitt 14). Jede Variante läuft 300.000-mal über die 39 Wochen vom
   30.11.2026 bis 31.08.2027.
4. **Nur erlaubte Wege.** Nichts, was das Abitur gefährdet, täuscht, gegen
   Regeln der Plattformen verstößt oder mehr als 5.000 € kosten kann.

„Gewinn“ heißt hier: deine Vermögensänderung bis zum Schluss, einschließlich
Abmeldung und Steuererklärung, vor Einkommensteuer.

---

## 4. Die Rangliste

Ausgangslage ist der Plan vom 23.11. mit Verkaufsstopp am 15.08.
(Gewinn in 2,7 von 100 Läufen, Median −1.184 €, Mittel −1.074 €).

**Jeder Hebel für sich:**

| Hebel | Gewinn in … von 100 | Geld im Median | im Mittel | Wirkung im Mittel | kostet dich | Beleg |
|---|---:|---:|---:|---:|---|---|
| Kosten senken (Abschnitt 5) | 6,7 | −568 € | −450 € | **+624 €** | 0 €, etwa 10–16 Stunden bis 2028 | Preisseiten und Gesetz; Abschluss selbst ist eine Schätzung |
| schneller bauen, review-fest planen (Abschnitt 8) | 3,8 | −1.164 € | −1.009 € | +65 € | 0 €, etwa 6–10 Stunden Einrichtung | Herstellerangaben ohne Zeitmessung |
| Markt (Deutsch zuerst) und Ideenwahl | 2,7 | −1.186 € | −1.078 € | −4 € | 0 €, etwa 10–15 Stunden | Schätzung; beide Wirkungen heben sich auf |
| zweite Signalprüfung am 28.06. | 2,7 | −1.185 € | −1.074 € | 0 € | 0 € | Messung der Post-Reichweite; Wirkung im Modell null |

**Alle vier zusammen** (der „Plan mit Hebeln“): Gewinn in 8,8 von 100,
Median −558 €, Mittel −393 €. Das ist mehr als die Summe der einzelnen
Wirkungen, weil erst die niedrigeren Kosten kleine Erfolge zu Gewinnen machen.

**Darauf aufgesetzt:**

| Zusatz | nur App: Gewinn in … von 100 | alles zusammen im Plus | Geld im Median | im Mittel | Wirkung im Mittel |
|---|---:|---:|---:|---:|---:|
| Plan mit Hebeln | 8,8 | 8,8 | −558 € | −393 € | – |
| + Übergabe oder Verkauf, Elternteil hat zugesagt (Abschnitt 6) | 12,0 | 17,9 | −544 € | +76 € | **+469 €** |
| + Verkaufsversuch und Übergabe ohne feste Zusage | 10,6 | 14,3 | −550 € | −71 € | +322 € |
| + Ferienjob ab 19.07. (Abschnitt 7) | 8,7 | 79,6 | +3.053 € | +2.467 € | **+2.860 €** |
| + Ferienjob ab 19.07., ab 05.07. ohne App im Store | 8,3 | 79,5 | +3.142 € | +2.702 € | +3.095 € |
| **+ Übergabe oder Verkauf + Ferienjob (dein Plan)** | 11,1 | 81,8 | +3.191 € | +3.158 € | +3.551 € |

Die Reihenfolge nach Wirkung ist also: **Ferienjob, Kosten, Nachfolger, Bau.**
Alles andere ändert das Ergebnis kaum.

---

## 5. Hebel 1: Kosten senken

**Wirkung:** Medianverlust −1.184 € → −568 €, Gewinnchance 2,7 → 6,7 von 100.
Die Erfolgsquote der Apps ändert sich nicht. Die Schwelle, ab der ein kleiner
Erfolg ein Gewinn ist, sinkt aber um rund 600 €.

| Posten | bisher angesetzt | neu | wie |
|---|---|---|---|
| Abschluss (Abmeldung, Steuererklärung 2027) | 0 / 300 / 800 € | 20 / 80 / 500 € | Belegtabelle ab dem ersten Beleg, EÜR und Erklärungen 2028 selbst über ELSTER; Steuerberater nur im Ernstfall |
| Gründung | 150 / 250 / 450 € | 140 / 200 / 380 € | kostenlose Gründungsberatung der IHK statt bezahlter Erstberatung (vorher fragen, ob sie kostenlos ist) |
| je Monat zwischen Gründung und erstem Start | 35 / 60 / 110 € | 23 / 28 / 45 € | nur Claude Pro, Domain mit Postfach, Prepaid-Nummer; kein Server-Tarif, kein Build-Abo |
| je Monat nach dem Start | 35 / 60 / 110 € | 23 / 30 / 75 € | Supabase im Gratis-Tarif, bis ein Signal da ist; EAS im Gratis-Tarif |
| je Monat im Abitur, wenn keine App im Store oder im Review ist | wie oben | 2 / 5 / 30 € | Claude Pro ruht von Ende März bis nach der letzten Prüfung; in dieser Zeit wird nicht gebaut |
| Claude Max in einzelnen Monaten | 0 / 10 / 70 € je Monat | 0 / 0 / 12 € | Max höchstens für einen Monat und nur, wenn das Pro-Limit die Ferienarbeit nachweislich stoppt |
| je Monat nach dem Ende der Jagd | 10 / 25 / 50 € | 5 / 12 / 35 € | am selben Tag alles kündigen, was Betrieb und Abschluss nicht brauchen |

Dazu gehören zwei Entscheidungen, die im Modell kein Geld bringen, aber
Arbeit sparen: **Kleinunternehmerregelung anwenden** (kein Verzicht) und beim
Finanzamt schriftlich fragen, ob es für die kleine Umsatzsteuer auf
Auslandsrechnungen (§ 13b) Voranmeldungen will.

**Der höchste Geldbetrag, den du im Lauf des Projekts vorstreckst,** liegt
damit im Median bei rund 560–580 €, in 9 von 10 Läufen unter 1.420 € und in
keinem Lauf über 4.090 € (die hohen Werte entstehen nur, wenn nach einem
Signal Creator-Geld fließt).

**Wo es steht:** [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md).

**Nicht wegsparen:** Apple Developer Program, Gewerbeanmeldung und Meldung an
die Krankenkasse, Impressum und Datenschutzerklärung, die Server-Funktion mit
geheimem Schlüssel und Ausgabengrenze, Claude Pro in den Bau-Monaten.

---

## 6. Hebel 2: Den Abschluss regeln – Nachfolger oder Verkauf

**Wirkung:** im Mittel +469 €; Gewinnchance der App 8,8 → 12,0 von 100; mit
dem Wert nach dem Sommer zusammen in 17,9 von 100 Läufen ein Plus.

Der Hebel wirkt doppelt:

1. **Kein Verkaufsstopp.** Übernimmt jemand die App, bleiben die Abos im
   Verkauf. Die Einnahmen der letzten Augustwochen entfallen nicht.
2. **Wert nach dem Sommer.** Eine App mit Monatsgewinn ist auch nach dem 31.08.
   etwas wert.

| Ausgang | Bedingung | wie oft klappt es | was es bringt |
|---|---|---|---|
| einstellen | unter ~150 € Monatsgewinn | – | nichts; Verkaufsstopp 15.08. |
| Übergabe an ein Elternteil | ab ~150 € Monatsgewinn **und** schriftliche Zusage im Januar | in 30 / 55 / 80 von 100 solchen Fällen | 0,7 / 2 / 5 Monatsgewinne in den zwölf Monaten danach, abzüglich ~120–165 € für Apple-Konto und Gewerbe des Elternteils (im Modell mit Puffer 150–250 €). **Das Geld gehört dann dem Elternteil,** nicht dir. |
| Verkauf (z. B. über Flippa) | ab 300 $ Monatsumsatz und mindestens 8 Wochen im Store | in 10 / 25 / 45 von 100 solchen Fällen | netto 1,7 / 4,3 / 10,3 Monatsgewinne |

Im Modell kommt es in 16–18 von 100 Läufen zu einer Übergabe oder einem
Verkauf. Der Wert liegt dann im Median bei rund 1.200 €, in einem von zehn
dieser Fälle über 5.200 €.

**Ohne feste Zusage** eines Elternteils sinkt die Wirkung auf +322 € im Mittel
(Gewinnchance der App 10,6, zusammen 14,3 von 100).

**Was du tun musst:**
- Im Elterngespräch und spätestens im Januar klären, ob ein Elternteil eine
  laufende App übernehmen würde. Eine Seite schriftlich: ab welchem
  Monatsgewinn, wer die 99 € für das Apple-Konto zahlt, wie viele Stunden im
  Monat. Vorher prüfen, was dagegen spricht (Arbeitgeber oder Dienstherr,
  eigene Versicherung, laufende Leistungen).
- Jede App von Anfang an so bauen, dass man sie übergeben kann
  (Übergabe-Mappe).
- Das Elternteil braucht sein eigenes Apple-Konto mit allen Verträgen
  spätestens Anfang Juli, sonst gilt im August nicht der niedrige Apple-Satz.
- Die Übergabe ist eine echte Schenkung ohne Gewinnbeteiligung, schriftlich
  und binnen drei Monaten dem Finanzamt angezeigt (§ 30 ErbStG). Das
  Elternteil wird Unternehmer mit eigenem Impressum, eigenem Gewerbe und
  eigener Steuer und beantragt das Small Business Program selbst (Genehmigung
  bis Sa 31.07.). Ein Elternteil nur als Namen einzutragen, während du das
  Geschäft führst, ist nicht erlaubt.

**Wo es steht:** [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md).

**Verworfen:** Weiterführen von Zürich aus (rund 3.500–5.500 CHF Mehrkosten im
Jahr, vor allem Krankenversicherung; lohnt erst bei einem echten Treffer und
nur nach Beratung zu beiden Ländern). Jahresabos und „lebenslang“ ohne
Nachfolger (du müsstest zwölf Monate liefern oder erstatten). Ein Elternteil
von Anfang an als Inhaber nur wegen der Steuer (hält nicht).

---

## 7. Hebel 3: Ferienjob, sobald die Jagd endet

**Wirkung:** im Mittel +2.860 € (mit frühem Beginn +3.095 €). Der Sommer endet
dann in rund 80 von 100 Läufen im Plus. Die Chance der App sinkt dadurch
kaum (8,8 → 8,7 bzw. 8,3 von 100).

**Warum es fast nichts kostet:** In 99 von 100 Läufen endet die Jagd am
18.07. ohnehin. Die Wochen danach brachten der App im Plan nur noch wenig.

| | |
|---|---|
| Form | **kurzfristige Beschäftigung**, von Anfang an schriftlich befristet: Mo 19.07. bis Di 31.08.2027 (32 Arbeitstage, 256 Stunden), besser gleich bis Fr 10.09. (40 Arbeitstage) |
| Abgaben | keine Sozialabgaben; die einbehaltene Lohnsteuer (etwa 12–16 %) kommt 2028 über die ohnehin fällige Steuererklärung zurück |
| Lohn | 14,60 €/h (Mindestlohn 2027) bis etwa 17–18,50 €/h: endgültig **3.738 € / 4.063 € / 4.736 €** für 256 Stunden, zunächst ausgezahlt 84–88 % davon |
| Familienversicherung | Lohn aus einer kurzfristigen Beschäftigung zählt nicht als regelmäßiges Einkommen; vor der Unterschrift bei der Krankenkasse schriftlich bestätigen lassen |
| Chance, einen Job über die ganze Zeit zu bekommen | 70–85 von 100 (Schätzung der Gegenprüfung) |
| früher Beginn | Ist am So 04.07. noch keine App im Store, beginnt der Job am Mo 05.07. (trifft in rund 20 von 100 Läufen zu) |

Im Modell zählen vorsichtig nur die sechs vollen Wochen bis 29.08. mit
560 / 600 / 690 € je Woche nach Fahrtkosten. Wer einen Job hat, verdient damit
im Median rund 3.770 €.

**Was du tun musst:** in den Weihnachtsferien oder im Januar ein bis zwei
Stunden für drei Bewerbungen mit festem Zeitraum; ab Ende Juni als Rückfall
zwei Zeitarbeitsfirmen; eine Kündigungsklausel oder Probezeit in den Vertrag,
falls doch ein Treffer kommt.

**Wo es steht:** [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md).

**Verworfen:** Job schon ab 14.06. (vor dem Ende der Prüfungszeit nicht
sauber möglich und nimmt der App ihr einziges Fenster), Nachhilfe neben der
App (bringt 150–250 €, kostet 15–30 App-Stunden in der knappsten Zeit), um
einen frühen Prüfungstermin bitten (Erfolgschance 5–15 von 100; nur fragen,
wann die Prüfung liegt).

---

## 8. Hebel 4: Schneller bauen, review-fest planen

**Wirkung:** Gewinnchance 2,7 → 3,8 von 100, im Mittel +65 €. App 1 ist bis
Di 02.02. in rund 14 statt 10 von 100 Läufen fertig und bis So 14.03. in
33 statt 26 von 100.

| | bisher | neu |
|---|---|---|
| Bauzeit App 1 | 80 / 140 / 280 h | 78 / 130 / 260 h |
| Bauzeit weitere Apps | 35 / 60 / 120 h | 33 / 55 / 110 h |
| Lernen | 20 / 30 / 40 h | 20 / 28 / 40 h |
| Review mit Ablehnungen | 0,5 / 1,5 / 4,0 Wochen | 0,4 / 1,2 / 3,0 Wochen |

Dahinter stehen: das offizielle Expo-Gerüst mit Plugin, die fertige
RevenueCat-Paywall, das Apple-Konto schon in KW 51, der Durchstich zuerst,
ein fester Funktions-Stopp am 24.01., eine Arbeitsweise mit Prüfbefehl und ab
App 2 die eigene Vorlage.

Die Wirkung ist klein, weil die Belege schwach sind (Herstellerangaben ohne
Zeitmessung) und die Gegenprüfung deshalb nur rund 7 % weniger Bauzeit stehen
ließ. Der eigentliche Wert liegt woanders: **Nach dem Durchstich kennst du
deine echten Stunden.** Liegst du am Stunden-Messpunkt (Di 29.12.) deutlich
unter dem Plan, ist deine Chance spürbar höher als hier gerechnet. Mit
Bauzeiten wie jemand, der programmieren kann, läge sie im alten Modell bei
rund 23 von 100.

**Wo es steht:** [`02_BAUPLAN_APP1.md`](02_BAUPLAN_APP1.md) und
[`01_TAG_FUER_TAG_BIS_FEBRUAR.md`](01_TAG_FUER_TAG_BIS_FEBRUAR.md).

**Verworfen:** bezahlte Vorlagen (35–200 € und 5–15 Stunden Einarbeitung gegen
höchstens 15 gesparte Stunden; eine gesparte Baustunde ist im Modell nur
4–6 € wert), App-Baukästen, fertige KI-Proxy-Dienste, Claude Max auf Verdacht,
der KI-Schlüssel in der App.

---

## 9. Was im Modell nichts ändert, aber Fehler vermeidet

Diese Punkte heben die Zahl nicht messbar. Sie verhindern, dass ein Lauf
unnötig schlecht ausgeht.

| Punkt | warum | steht in |
|---|---|---|
| **No-Go-Regel am Ideen-Tor:** Erreicht keine Idee die Mindestwerte, wird nicht gegründet und kein Apple-Konto gekauft | spart in diesem Fall alle Kosten; die Ideenwahl selbst hebt die Trefferquote nur um etwa 5 % | [`04_IDEENWAHL.md`](04_IDEENWAHL.md) |
| K.-o.-Fragen zur Haftung und der Test gegen kostenlose Alternativen | als Einzelunternehmer haftest du persönlich; eine App, die ein kostenloser KI-Chat ersetzt, zahlt niemand | [`04_IDEENWAHL.md`](04_IDEENWAHL.md) |
| App zweisprachig, Videos auf Deutsch | Reichweite ist an SIM und IP gebunden; der deutsche Markt ist kleiner (Abschlag ×0,9 auf die Trefferquote), der Englisch-Test über Shorts kostet fast nichts | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md) |
| Wochenabo 6,99 € vorausgewählt, Monatsabo 14,99 €, keine Testphase, kein Jahresabo | entspricht den Marktwerten 2026; darunter zu bleiben verschenkt Umsatz, ein Jahresabo ohne Nachfolger ist eine Schuld | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md) |
| Small Business Program sofort beantragen | sonst gelten in den Startwochen 26 % statt 15 % Apple-Anteil | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md) |
| Zweite Signalprüfung (21 Tage nach dem ersten täglichen Post nach der letzten Prüfung, spätestens Di 29.06.) für eine App, die vor dem Abitur gestartet ist | mit höchstens 3 Posts je Woche in Q4 kann eine App die 300 $ kaum zeigen; ohne zweite Prüfung würde ein Treffer zu früh abgeschrieben | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md) |
| Keine bezahlte Verstärkung eigener Posts | 50 € Einsatz bringen typisch 6 € zurück | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md) |
| Apps, die nach dem 04.07. erscheinen, nur mit Wochenabo | hält den Abschluss in jedem Fall möglich | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md) |
| Automatische Verlängerung der Apple-Mitgliedschaft abschalten | sonst gehen im Winter 2027/28 noch einmal 99 € ab | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md) |

---

## 10. Was nichts bringt oder verworfen wurde

Geprüft und im Modell ohne Wirkung oder schlechter (Plan mit Hebeln, Gewinn
in 8,8 von 100 Läufen; je 100.000 Läufe, Unterschiede unter 0,3 Punkten sind
Zufall):

| Idee | Gewinn in … von 100 | Ergebnis |
|---|---:|---|
| Tor 1 später (01.08. statt 18.07.) | 7,4 | schlechter: späte Starts verdienen bis zum Verkaufsstopp kaum noch etwas |
| Tor 1 früher (04.07. / 11.07.) | 7,0 / 8,4 | schlechter für die App; sinnvoll nur zusammen mit dem Ferienjob (Abschnitt 12) |
| höchstens zwei Apps | 6,8 | schlechter: die dritte App ist ein weiterer Versuch mit besserer Lernkurve |
| Signal schon ab 150 $ | 8,3 | etwas schlechter: Creator-Geld fließt öfter an Apps ohne Nachfrage |
| Creator-Geld bis 1.500 € statt 750 € | 8,6 | kein Unterschied |
| später gründen (erst bei 85 % fertiger App) | 9,0 | kein messbarer Unterschied, seit die Kosten vor dem Start niedrig sind (Median 15 € besser) |
| Claude Pro im Abitur weiterlaufen lassen und weiterbauen | 9,0 | kein messbarer Unterschied bei der Chance, Median 37 € schlechter |
| im Abitur weiterbauen, aber sonst sparen | 9,4 | +0,6 Punkte; dafür bis zu 5 Stunden je Abiturwoche an der App. Der Plan bleibt bei der Ruhezeit, weil das Abitur vorgeht |
| früher frei nach der mündlichen Prüfung (31.05. statt 07.06.) | 9,4 | +0,6 Punkte; der Termin lässt sich aber kaum beeinflussen. Frag im Januar, wann er liegt |

Von der Gegenprüfung verworfen oder stark gekürzt:

- **Marketing:** Format-Raster, Wiederverwendung auf Reels und Shorts,
  Kommentare als Marke, klickbarer Download-Link, zweites Markenkonto. Alles
  sinnvolle Arbeitsweise, aber ohne belegte Wirkung; im Modell mit null
  angesetzt. Ein Post mit 100.000 Aufrufen bringt nach den korrigierten Werten
  etwa 50–150 Downloads und 20–70 $ Monatsumsatz.
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

Szenario „Plan mit Hebeln + Übergabe oder Verkauf + Ferienjob“.

**Geld bis zum Schluss (alles zusammen):**

| | |
|---|---|
| im Plus | in 81,8 von 100 Läufen |
| mindestens 1.000 € | in 80,1 von 100 |
| mindestens 5.000 € | in 7,3 von 100 |
| mindestens 10.000 € | in 1,8 von 100 |
| mindestens 100.000 € | in 1 von 10.000 |
| 500.000 € | in keinem Lauf |
| schlechtestes 1 % | ab −850 € |
| schlechteste 10 % | ab −567 € |
| unteres Viertel | ab +2.794 € |
| **Median** | **+3.191 €** |
| oberes Viertel | ab +4.144 € |
| beste 10 % | ab +4.688 € |
| bestes 1 % | ab +13.118 € |
| Mittel | +3.158 € |
| mehr als 500 € Verlust | in 12,9 von 100 Läufen |
| mehr als 1.000 € Verlust | in 0,1 von 100 Läufen |

Die schlechten Läufe sind die, in denen du keinen Ferienjob bekommst
(22 von 100) und die App nichts einbringt.

**Woraus es sich zusammensetzt:**

| Teil | wie oft | wie viel |
|---|---|---|
| App allein | Gewinn in 11,1 von 100 Läufen | Median −559 €, Mittel −346 €, schlechteste 10 % ab −790 €, beste 1 % ab +2.960 € |
| Ferienjob | in 77,6 von 100 Läufen | Median 3.772 €; früher Beginn am 05.07. in 20,4 von 100 |
| Übergabe oder Verkauf | in 16,1 von 100 Läufen | Median 1.190 €, in einem von zehn dieser Fälle über 5.360 € |
| Creator-Geld | fließt in 6,4 von 100 Läufen | im Schnitt aller Läufe 39 € |

**Zeitpunkte:**

| | |
|---|---|
| Gründung | im Median am 18.01. (früheste 10 %: bis 11.01., späteste 10 %: ab 15.02.); in 38 von 100 Läufen erst nach dem 31.01. |
| App 1 fertig gebaut | bis Di 02.02. in 13,5 von 100 Läufen, bis So 14.03. in 33,2 von 100; sonst nach der letzten Prüfung (Median 07.06., späteste 10 % ab 21.06.) |
| App 1 im Store | vor dem 15.03. in 24,5 von 100 Läufen; Median 21.06. |
| Apps im Store bis 31.08. | keine in 3,5, eine in 15,6, zwei in 32,9, drei oder mehr in 48,0 von 100 Läufen |
| eine App mit mindestens 300 $ MRR | in 44,6 von 100 Läufen |
| mit mindestens 1.000 $ MRR | in 18,9 von 100 |
| mit mindestens 5.000 $ MRR | in 3,7 von 100 |
| Wege ab Juli | A (kein Treffer) 99,4; B 0,4; C 0,3 von 100 |

**Geldeinsatz** (höchster Betrag, den du vorstreckst): Median 561 €,
in 9 von 10 Läufen höchstens 1.373 €, in 99 von 100 höchstens 3.499 €,
größter Wert 4.086 €. Die Grenze von 5.000 € hält in jedem Lauf.

---

## 12. Gegenproben

| Gegenprobe | nur App: Gewinn in … von 100 | alles zusammen im Plus | Geld im Median | im Mittel |
|---|---:|---:|---:|---:|
| dein Plan (Stand 24.11.) | 11,1 | 81,8 | +3.191 € | +3.158 € |
| ganz ohne Creator-Geld | 12,1 | 81,6 | +3.196 € | +3.109 € |
| Job schon ab 05.07., wenn am 04.07. keine App 300 $ MRR zeigt | 8,3 | 80,3 | +4.233 € | +3.652 € |
| **nur Ferienjob ab 05.07., keine App, keine Gründung** (einfache Rechnung, nicht simuliert) | – | 77,7 | +4.826 € | +3.835 € |

Nur die App, ohne Nachfolger und ohne Job:

| Gegenprobe | Gewinn in … von 100 | Geld im Median | im Mittel |
|---|---:|---:|---:|
| Plan mit Hebeln | 8,8 | −558 € | −393 € |
| ohne Creator-Geld | 10,1 | −548 € | −375 € |
| Bauzeiten wie bisher angesetzt (80/140/280 h) | 7,2 | −567 € | −439 € |
| strengerer Markt 2027 | 7,1 | −566 € | −434 € |

So liest du das:

- **Creator-Geld ändert fast nichts.** Ohne ist ein kleiner Gewinn etwas
  häufiger, mit der Signalregel sind die seltenen großen Ergebnisse etwas
  häufiger (10.000 € oder mehr in 1,79 statt 1,58 von 100). Die Regel bleibt:
  Geld für Creator nur nach bestandenem Signal, höchstens 750 €. Wenn du es
  ganz lässt, verlierst du nichts Messbares.
- **Geld gegen Chance.** Beginnst du den Job schon am 05.07., sobald kein
  Signal da ist, hast du im Median rund 1.000 € mehr. Dafür sinkt die
  Gewinnchance der App von 11 auf 8 von 100, weil ihr die zwei stärksten
  Wochen fehlen. Der Plan bleibt beim 18.07.; du darfst dich am 04.07. anders
  entscheiden.
- **Was das Projekt kostet.** Ohne App und ohne Gründung brächte ein Job ab
  05.07. im Mittel rund 3.800 € (wenn du einen bekommst, rund 4.800 €). Dein
  Plan bringt im Mittel rund 3.200 €. Der Unterschied von rund 700 € ist der
  Preis für das Lernprojekt samt der kleinen Chance auf mehr.
- **Die Hebel halten auch im schlechteren Fall:** Mit den alten Bauzeiten
  oder im strengeren Markt bleibt die Chance bei rund 7 von 100 und der
  Medianverlust bei rund 570 €.

---

## 13. Was du dafür tun musst – die Liste

| wann | was | Stunden | steht in |
|---|---|---|---|
| Do 26.11. | Elterngespräch: Namensfrage ansprechen und fragen, ob ein Elternteil eine laufende App im Sommer übernehmen würde | 1 | Hauptplan, Abschnitt 3 |
| Sa 28.11.–Sa 19.12. | fünf Ideen prüfen mit K.-o.-Fragen, Nachfrageprüfung, Bewertungstabelle, Slideshow-Test und Ablauf-Test | 10–15 | [`04_IDEENWAHL.md`](04_IDEENWAHL.md) |
| Sa 12.12. | Zwischenstand: erfüllt eine Idee alle Mindestwerte? Nur dann Apple in KW 51 | 0,2 | [`04_IDEENWAHL.md`](04_IDEENWAHL.md) |
| bis So 13.12. | Namensfrage entscheiden | – | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md) |
| Mo 14.–Mi 16.12. | Apple Developer Program kaufen (99 €), automatische Verlängerung abschalten – nur wenn der Zwischenstand am Sa 12.12. passt | 1 | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md) |
| Sa 19.12. / So 20.12. | Ideen-Tor mit No-Go-Regel | 1 | [`04_IDEENWAHL.md`](04_IDEENWAHL.md) |
| Weihnachtsferien | drei Bewerbungen für den Ferienjob (befristet 19.07.–31.08. oder bis 10.09.) | 1–2 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md) |
| Di 29.12. | Stunden-Messpunkt nach dem Durchstich | 0,5 | [`02_BAUPLAN_APP1.md`](02_BAUPLAN_APP1.md) |
| Januar | schriftliche Zusage des Elternteils (eine Seite); Oberstufenkoordination fragen, wann die mündlichen Prüfungen liegen | 1 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md) |
| Dezember bis Februar | Gründung: Kleinunternehmer im Fragebogen, Gründungsberatung (wenn kostenlos), Frage ans Finanzamt, Small Business Program am selben Tag wie der Vertrag für bezahlte Apps | ~9 (davon ~3,5 am Gründungstag und bei Apple) | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md) |
| ab dem ersten Beleg | Belegtabelle führen | 0,5 je Monat | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md) |
| So 14.03. | Ruhezeit entscheiden: keine App im Store oder im Review → Claude Pro ruht bis nach der letzten Prüfung | 0,2 | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md) |
| spätestens Di 29.06. | zweite Signalprüfung für eine App, die vor dem Abitur gestartet ist (21 Tage nach dem ersten täglichen Post nach der letzten Prüfung) | 0,2 | [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md) |
| Ende Juni | Rückfall für den Job: zwei Zeitarbeitsfirmen anfragen | 1 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md) |
| bis Fr 02.07. | zeigt eine App Ende Juni nennenswerten Umsatz (Richtwert ~100 $ MRR, 06 Abschnitt 4.4): Elternteil schickt Gewerbe- und Apple-Anmeldung ab | 2 (Elternteil) | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md) |
| So 04.07. | Stichtag: keine App im Store → Job ab Mo 05.07. | – | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md) |
| So 18.07. | Tor 1; am Mo 19.07. Jobbeginn und alles kündigen, was nicht gebraucht wird | 1 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md) |
| bis Sa 31.07. | je App entscheiden: einstellen, übergeben oder verkaufen | 1 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md) |
| So 15.08. | ohne Nachfolger: alle Abos aus dem Verkauf nehmen | 0,5 | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md) |
| Mi 15.09. und Do 16.09./Fr 17.09. | Dienstende; danach App entfernen, Gewerbe abmelden | 4–6 (Schätzung) | [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md) |
| Frühjahr 2028 | EÜR und Steuererklärung 2027 über ELSTER; die Lohnsteuer kommt zurück | 6–12 | [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md) |

---

## 14. Die Werte im Modell

Alle Werte sind Dreiecke aus niedrigstem, typischem und höchstem Wert.
B = belegt, S = Schätzung.

| Größe | Plan vom 23.11. | Plan mit Hebeln | Beleg |
|---|---|---|---|
| Faktor auf die Trefferquoten | 1,0 | 0,8 / 0,95 / 1,2 (deutscher Markt ×0,8/0,9/1,0, Ideenwahl ×1,0/1,05/1,2) | S |
| Bauzeit App 1 (Stunden) | 80 / 140 / 280 | 78 / 130 / 260 | S |
| Bauzeit weitere Apps | 35 / 60 / 120 | 33 / 55 / 110 | S |
| Lernstunden | 20 / 30 / 40 | 20 / 28 / 40 | S |
| Review in Wochen | 0,5 / 1,5 / 4,0 | 0,4 / 1,2 / 3,0 | S |
| Gründung (€) | 150 / 250 / 450 | 140 / 200 / 380 | B/S |
| Kosten je Monat vor dem ersten Start (€) | 35 / 60 / 110 | 23 / 28 / 45 | B |
| Kosten je Monat nach dem Start | 35 / 60 / 110 | 23 / 30 / 75 | B |
| Kosten je Monat in der Ruhezeit | wie oben | 2 / 5 / 30 | B |
| Zusatzkosten Claude Max je Monat | 0 / 10 / 70 | 0 / 0 / 12 | B/S |
| Kosten je Monat nach dem Ende der Jagd | 10 / 25 / 50 | 5 / 12 / 35 | S |
| Abschluss (€) | 0 / 300 / 800 | 20 / 80 / 500 | S |
| Startumsatz ohne bezahlten Test (Anteil) | 0,2 / 0,4 / 0,7 | 0,2 / 0,42 / 0,7 | S |
| zweite Signalprüfung | – | 21 Tage nach dem ersten täglichen Post nach der letzten Prüfung (im Modell die Woche ab Mo 28.06.) | B |
| Verkaufsstopp ohne Nachfolger | nicht gerechnet | So 15.08. | B |
| Wert nach dem Sommer | nicht gerechnet | Übergabe: ab 150 € Monatsgewinn, Chance 0,3 / 0,55 / 0,8, 0,7 / 2 / 5 Monatsgewinne minus 150–250 €; Verkauf: ab 300 $ Monatsumsatz und 8 Wochen, Chance 0,10 / 0,25 / 0,45, 1,7 / 4,3 / 10,3 Monatsgewinne | S |
| Ferienjob | nicht gerechnet | 560 / 600 / 690 € je Woche, sechs Wochen ab 19.07. (acht ab 05.07.), Chance 0,70 / 0,78 / 0,85 | B/S |

Unverändert: 5.000 € Einsatz mit harter Grenze, Kalender Niedersachsen,
Stunden je Woche, erst bauen und bei halb fertiger App gründen, Startpause
vom 15.03. bis zur letzten Prüfung, Tore am 18.07. und 08.08., Signalregel
mit höchstens 750 € Creator-Geld, strenge Trefferquoten mit Lernkurve.

---

## 15. Grenzen dieser Rechnung

- **Die Hebelwerte sind Schätzungen.** Belegt sind Preise, Gesetze und Apples
  Regeln. Wie viel schneller du baust, wie gut deine Ideenwahl ist und ob ein
  Elternteil am Ende wirklich übernimmt, weiß vorher niemand.
- **Die Trefferquoten stammen aus Marktberichten für alle neuen Abo-Apps**
  (RevenueCat 2026: 17,3 % erreichen in zwei Jahren 1.000 $ Monatsumsatz).
  Für einen Einzelnen ohne Erfahrung, mit deutschen Videos ohne Gesicht und
  nur einem Sommer gibt es keine Messung. Das Modell rechnet deshalb mit
  niedrigeren Quoten und einer Lernkurve.
- **Der Wert nach dem Sommer** gehört bei einer Übergabe dem Elternteil. In
  der Spalte „alles zusammen“ ist er trotzdem mitgezählt, als Wert für die
  Familie.
- **Der Ferienjob zählt mit dem vollen Lohn,** obwohl ein Teil (die
  Lohnsteuer) erst 2028 zurückkommt und der Augustlohn oft erst Mitte
  September ausgezahlt wird.
- **Nicht gerechnet:** Erstattungen an Nutzer (2–8 % des Umsatzes); eine
  Verlängerung des Jobs bis 10.09. (64 Stunden, rund +930 bis +1.180 €; weil
  das Modell den Lohn nur bis So 29.08. zählt, sind bis 10.09. insgesamt
  80 Stunden ungezählt, rund +1.170 bis +1.480 €); Einkommensteuer: keine,
  solange App-Gewinn (einschließlich eines Verkaufsgewinns) plus Ferienjoblohn
  minus 1.230 € unter dem Grundfreibetrag bleiben (2026: 12.348 €, 2027 noch
  offen) – mit Ferienjob also bis grob 9.000 € App-Gewinn. Darüber fällt
  Steuer an, und die Lohnsteuer kommt nicht ganz zurück.
- **Zwei Hinweise außerhalb der App,** beide ungeprüft: Auslands-BAföG für ein
  ganzes Studium in der Schweiz und ein Stipendium über einen Schulvorschlag.
  Beides kann mehr Geld bedeuten als jeder Hebel in diesem Dokument. Näheres
  in [`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md).
