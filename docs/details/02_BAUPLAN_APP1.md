# Bauplan für App 1 – Arbeitspaket für Arbeitspaket

Gehört zu [`../APP_PLAN_ALLEIN_MIT_CLAUDE.md`](../APP_PLAN_ALLEIN_MIT_CLAUDE.md).
Dort stehen Regeln, Geld und Messpunkte. Hier steht, **was du baust, in
welcher Reihenfolge, wie lange es dauert und woran du erkennst, dass ein
Schritt fertig ist.** Wann du welches Paket machst, steht in
[`01_TAG_FUER_TAG_BIS_FEBRUAR.md`](01_TAG_FUER_TAG_BIS_FEBRUAR.md). Konten und
Gründung stehen in [`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md),
Ideenwahl und die Gliederung von `SPEC.md` in
[`04_IDEENWAHL.md`](04_IDEENWAHL.md), Preise, Paywall-Texte und Store-Seite in
[`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md), die Übergabe-Mappe in
[`06_SOMMER_UND_ABSCHLUSS.md`](06_SOMMER_UND_ABSCHLUSS.md). Modellzahlen stehen
nur in [`07_HEBEL.md`](07_HEBEL.md).

**Stand:** Mi 25.11.2026. Neu gegenüber der Fassung vom 24.11. (Hauptplan, 01
und 03–07 enthalten diese Entscheidungen):
- App 1 ist review-fest: geführter Ablauf und neues Paket **AP10a** (Verlauf,
  Favoriten, Kopieren, Teilen); typisch ~113 statt 99 Stunden (Abschnitt 4).
- `SPEC.md` nach 04, Abschnitt 10.5 (AP3); Herkunftsfrage und
  Beispiel-Ergebnis im Onboarding (AP11).
- Claude API: vor dem Start 5–10 $ ohne Nachladen, Anfrage nur mit `model`,
  `max_tokens`, `system` und `messages`, Modell-ID als Geheimnis (AP5).
- Supabase im Gratis-Tarif mit Migrationen und Wachregel (AP4, AP20);
  Tagesgrenze zum Start 30 statt 20 (AP15).
- Keine Testphase, Wochenabo 6,99 € vorausgewählt, Monatsabo 14,99 €, drei
  Store-Sprachen schon in Version 1.0 (AP12, AP19, AP22); Übergabe-Mappe von
  Anfang an (AP1, AP20).
- Gründung ~3,5 bzw. ~9 Stunden (Abschnitt 4); Schwellen am
  Stunden-Messpunkt wie im Hauptplan (Abschnitt 8).

Inhalt:
1. [Der Schnitt von App 1](#1-der-schnitt-von-app-1)
2. [Wie die Teile zusammenhängen](#2-wie-die-teile-zusammenhängen)
3. [So arbeitest du in jeder Sitzung](#3-so-arbeitest-du-in-jeder-sitzung)
4. [Die Arbeitspakete im Überblick](#4-die-arbeitspakete-im-überblick)
5. [Phase A – Fundament und Durchstich](#5-phase-a--fundament-und-durchstich)
6. [Phase B – Die App](#6-phase-b--die-app)
7. [Phase C – Einreichung](#7-phase-c--einreichung)
8. [Stunden-Messpunkt und Funktions-Stopp](#8-stunden-messpunkt-und-funktions-stopp)
9. [Nach App 1: deine eigene Vorlage](#9-nach-app-1-deine-eigene-vorlage)

---

## 1. Der Schnitt von App 1

App 1 ist absichtlich klein. Jede Stunde, die du vor dem Start sparst, macht
einen Start vor dem Abitur wahrscheinlicher. Bezahlte Abkürzungen lohnen
trotzdem nicht: Eine gesparte Baustunde ist im Modell nur 4–6 € wert
([07](07_HEBEL.md), Abschnitt 8; alle übrigen Modellzahlen stehen ebenfalls
nur in 07). Was Apple bei einer KI-App sehen will, ist aber von Anfang an drin
([04](04_IDEENWAHL.md), Abschnitt 9), denn jede Ablehnung kostet Tage.
Deshalb gilt für App 1:

**Drin**
- **Eine Aufgabe im geführten Ablauf:** 3–6 Fragen (Auswahlknöpfe, kurze
  Textfelder), dann ein strukturiertes Ergebnis in einem festen, eigenen
  Format. Kein leeres Chatfenster, kein allgemeiner Chatbot. Die eigene
  Funktion ist auf dem ersten Bildschirm zu sehen.
- **Eigenes der App:** Verlauf und Favoriten nur auf dem Gerät, Kopieren und
  das Teilen-Menü des iPhones (AP10a). Bei knapper Zeit zuerst geführter
  Ablauf und Meldeknopf, Favoriten zuletzt.
- **Bildschirme:** die fünf aus AP2 (Onboarding mit 3–5 Fragen,
  Herkunftsfrage und Beispiel-Ergebnis; Paywall; Eingabe; Ergebnis;
  Einstellungen), dazu der Verlauf aus AP10a.
- **Zwei Sprachen:** Deutsch und Englisch, von Anfang an. Die KI antwortet in
  der Sprache der App: Deutsch auf Geräten mit Deutsch, sonst Englisch (AP2).
- **Abo:** Wochenabo 6,99 € (vorausgewählt) und Monatsabo 14,99 €, keine
  Testphase, harte Paywall nach dem Onboarding, über RevenueCat mit der
  fertigen Paywall aus dem Dashboard (Preise und Länderpreise:
  [05](05_START_UND_MARKETING.md), Abschnitt 2). Erscheint App 1 erst nach
  So 04.07., bietet sie nur das Wochenabo an (05, Abschnitt 1.4).
- **Server:** eine Supabase-Funktion `ki`, die das Abo prüft, zählt und die KI
  aufruft, dazu die kleine Funktion `herkunft`, die die Antworten auf
  „Woher kennst du die App?“ zählt (AP11).
- **Pflichtteile:** Einwilligung vor dem ersten KI-Aufruf, Knopf „Antwort
  melden“ als E-Mail-Link, Kontaktadresse in der App, Impressum, Datenschutz,
  Nutzungsbedingungen und „Käufe wiederherstellen“ (alle vier auch ohne Abo,
  direkt auf der Paywall), „Abo verwalten“.

**Nicht drin** (jedes davon kostet Tage oder Review-Runden)
- Kamera, Fotos, Mikrofon, Standort, Push-Mitteilungen
- Nutzerkonten, Anmeldung, Teilen mit anderen Nutzern in der App, Profile,
  Inhalte für andere Nutzer; kein „Mit Apple anmelden“, kein iCloud
- Tracking und eigene Messereignisse (die Herkunftsfrage zählt anonym, ohne
  App-User-ID)
- Testphase, Jahresabo, „lebenslang“, Web-Kauf, Android
- iPad-Layout (die App läuft dort im Kompatibilitätsmodus und wird dort
  getestet, bekommt aber kein eigenes Layout und keine iPad-Screenshots)
- Themen der Sperrliste ([04](04_IDEENWAHL.md), Abschnitt 11), z. B. Finanzen,
  Gesundheit, Abnehmen, Dating, Rechtsberatung im Einzelfall; Zielgruppe
  Kinder und Schüler

**Eine Foto-App** (Foto → KI-Ergebnis) ist erst App 2 oder 3, wenn die
Vorlage steht. Sie braucht Kamera-Berechtigung, Bildverkleinerung und
höhere KI-Kosten und ist beim Review empfindlicher.

---

## 2. Wie die Teile zusammenhängen

```
 iPhone-App (Expo)
   │  1. fragt RevenueCat: Hat diese App-User-ID ein aktives Abo?  → Paywall oder Eingabe
   │  2. schickt Antworten aus Formular und Onboarding + App-User-ID + Sprache
   ▼
 Supabase-Funktion „ki“  (dein wichtigster Server-Code, ~100 Zeilen)
   │  a. prüft bei RevenueCat (geheimer Schlüssel), ob das Abo wirklich aktiv ist
   │  b. zählt den Aufruf in der Tabelle „nutzung“ (zum Start 30 je App-User-ID und Tag)
   │  c. ruft die Claude API auf (Schlüssel und Modell-ID als Geheimnis; nur model,
   │     max_tokens, system, messages) und prüft Abbruchgrund und Format der Antwort
   ▼
 Antwort zurück an die App  →  Ergebnis-Bildschirm, gespeichert nur im Verlauf auf dem Gerät

 daneben: Funktion „herkunft“ zählt „Woher kennst du die App?“ (ohne App-User-ID, AP11)
```

**Wo welcher Schlüssel liegt**

| Schlüssel | wo | darf in die App? |
|---|---|---|
| RevenueCat, öffentlicher iOS-Schlüssel | App (über `eas.json`/Umgebung) | ja |
| RevenueCat, Test-Store-Schlüssel (aus dem Dashboard kopieren) | nur im Entwicklungs-Build, als Umgebungsvariable von EAS, nie im Repository | ja, aber nie im Store- oder TestFlight-Build: der stürzt damit ab. Test-Käufe schalten im selben RevenueCat-Projekt echte Berechtigungen frei; behandle ihn wie ein Geheimnis ([03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 3) |
| Supabase, Publishable-Schlüssel | App | ja |
| RevenueCat, geheimer Schlüssel | Supabase-Geheimnis | **nie** |
| Claude API-Schlüssel | Supabase-Geheimnis | **nie** |
| Supabase, Secret-Schlüssel | nur in der Funktion | **nie** |

Die Modell-ID `claude-haiku-5-5` ist kein Schlüssel, liegt aber ebenfalls als
Geheimnis in der Funktion. So tauschst du sie ohne App-Update
([06](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 4.3).

**Zwei Organisationen bei Supabase, beide im Gratis-Tarif:** `app-test` mit
dem Projekt `app1-test` und `app-betrieb` mit dem Projekt `app1-betrieb`,
Region EU (Frankfurt) ([03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 3). Claude
Code bekommt nur Zugang zum Testprojekt. Den Betrieb richtest du selbst im
Dashboard ein, mit Claudes Anleitung (AP20).

---

## 3. So arbeitest du in jeder Sitzung

1. **Ein Arbeitspaket, ein Ergebnis.** Du öffnest PowerShell im Projektordner,
   startest `claude` und nennst das Paket.
2. **Vor größeren Paketen ein Plan per Interview:** „Lies `SPEC.md`. Interviewe
   mich zu diesem Paket, bis du den Plan schreiben kannst, und schreib ihn nach
   `docs/plan.md`.“ Danach `/clear` und eine neue Sitzung, die nur aus
   `SPEC.md` und `docs/plan.md` baut. `SPEC.md` selbst (AP3) änderst du nur
   bewusst; was dort nicht steht, wird nicht gebaut.
3. **Claude plant zuerst.** Du liest den Plan und sagst Ja oder änderst ihn.
4. **Claude prüft sich selbst.** In deiner `CLAUDE.md` stehen drei Befehle,
   die Claude nach jeder Änderung laufen lässt und deren Ausgabe es dir zeigt:
   - `npx tsc --noEmit` (findet Tippfehler im Code),
   - `npx expo lint` (findet Stilfehler),
   - `npx expo-doctor` (findet Fehler in der Einrichtung).
5. **Du prüfst auf dem Gerät.** Erst auf dem iPhone, dann auf dem iPad. Bei
   einem Fehler machst du einen Screenshot und ziehst ihn in die Sitzung.
6. **Bei Fehlern den ganzen Fehlertext einfügen** und sagen, woran „behoben“
   zu erkennen ist. Nach zwei Fehlversuchen: Sitzung beenden, neu beginnen
   mit „Erkläre mir zuerst, was der Fehler bedeutet; ändere nichts“.
7. **10 Minuten Lernen am Ende:** „Erkläre mir die drei wichtigsten Stellen
   dieser Änderung und stell mir zwei Fragen dazu.“
8. **Commit, Push, Stunden eintragen.** Haben sich Konten, Schlüsselorte oder
   Kosten geändert, trägst du es in `docs/UEBERGABE.md` nach (etwa 5 Minuten
   je Woche, [06](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 4.3).

**Wenn du festhängst:** Nach etwa 90 Minuten ohne Fortschritt stellst du die
Frage im Expo-Forum oder in der RevenueCat-Community, ohne Schlüssel und ohne
persönliche Angaben. Ein Spitzname ist dort in Ordnung.

**Nie:** einen Schlüssel in die App oder ins Repository; etwas Wichtiges im
Schlüsselbund ablegen (nach einer Übertragung der App funktioniert er nur bis
zum nächsten Update); Kundendaten in dein Claude-Abo; „ist behoben“ glauben,
ohne es gesehen zu haben; neue Funktionen nach dem Funktions-Stopp;
Funktionen vor dem Review verstecken oder nach der Freigabe per Update
(`expo-updates`) freischalten (Updates ohne neues Review nur für reine
Fehlerkorrekturen und den Hinweis beim Verkaufsstopp,
[03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 7.6); eine
unfertige Version einreichen, um das Review zu testen; einen fertigen
KI-Proxy-Dienst statt der eigenen Funktion mit Abo-Prüfung; eine bezahlte
Vorlage oder einen KI-App-Baukasten.

---

## 4. Die Arbeitspakete im Überblick

Stunden sind deine eigenen Stunden: von/typisch/bis. Die typischen Werte
ergeben zusammen ~113 Stunden. Das ist der Fall, in dem jedes Paket ohne
längere Fehlersuche durchläuft. Gegenüber der Fassung vom 24.11. (99 Stunden,
dort gerundet ~100) sind es 14 Stunden mehr: AP10a (10), Beispiel-Ergebnis
und Herkunftsfrage im Onboarding (AP11, 3) und die Übergabe-Mappe (AP20, 1).
Das Modell rechnet vorsichtiger, mit 78/130/260 Stunden ([07](07_HEBEL.md),
Abschnitt 14), weil Fehlersuche und Lernen am eigenen Code dazukommen. Keine
Studie misst das für Anfänger. Deine echten Stunden trägst du ein und
vergleichst sie am Stunden-Messpunkt (Abschnitt 8).

| Nr. | Paket | Stunden | fertig, wenn … |
|---|---|---|---|
| **A** | **Fundament und Durchstich** | **~32** | |
| AP1 | Projekt, Plugins, `CLAUDE.md`, Prüfbefehle | 2/3/5 | das leere Projekt in Expo Go läuft und die drei Prüfbefehle ohne Fehler durchlaufen |
| AP2 | Zwei Sprachen und fünf leere Bildschirme | 3/4/7 | du auf dem iPhone durch alle fünf Bildschirme tippen kannst und sie beim Umstellen der Gerätesprache die Sprache wechseln |
| AP3 | Beschreibung von App 1 (`SPEC.md`) | 1/2/3 | `SPEC.md` auf einer Seite alle 16 Punkte der Gliederung aus 04, Abschnitt 10.5, enthält |
| AP4 | Supabase: zwei Organisationen mit je einem Projekt, Funktion mit Beispielantwort, Zähltabelle | 3/5/9 | die App eine Beispielantwort vom Server zeigt, in der Tabelle ein Zähler steht und das Tabellen-Schema als Migration im Repository liegt |
| AP5 | Claude API: Schlüssel, Limit, echte Antwort | 1/2/4 | die App eine echte KI-Antwort im vorläufigen festen Format zeigt, das Guthaben ohne Nachladen da ist und in der Konsole eine Grenze von höchstens 50 $ steht (gibt es keine: in `docs/konten.md` vermerkt) |
| AP6 | RevenueCat: Projekt, Test Store, Paywall, alle nativen Pakete | 3/5/9 | Projekt, Produkte und Paywall im Dashboard stehen und alle nativen Pakete installiert sind |
| AP7 | Apple-Konto, Geräte, Entwicklungs-Build | 2/3/8 | der Entwicklungs-Build auf iPhone und iPad startet und die echte Paywall zeigt |
| AP8 | **Durchstich:** Kauf → Abo-Prüfung → KI-Antwort | 2/4/8 | ein Testkauf die Eingabe freischaltet und ein Aufruf ohne Abo vom Server abgelehnt wird |
| AP9 | Store-Build und TestFlight | 2/4/9 | die App über TestFlight auf deinem iPhone installiert ist und ohne Produkte nicht abstürzt |
| **B** | **Die App** | **~55** | |
| AP10 | Kernfunktion und Prompt | 6/10/18 | 20 Testeingaben in beiden Sprachen ein brauchbares Ergebnis im festen Format liefern |
| AP10a | Verlauf, Favoriten, Kopieren, Teilen | 7/10/14 | jedes neue Ergebnis im Verlauf steht, dort ohne Netz lesbar und löschbar ist, sich kopieren und über das Teilen-Menü teilen lässt und der Verlauf (und, wenn bis zum Funktions-Stopp gebaut, die Favoriten) einen Neustart übersteht; sonst steht „Favoriten in 1.1“ in `docs/entscheidungen.md` |
| AP11 | Onboarding mit Beispiel-Ergebnis und Herkunftsfrage | 5/8/13 | die Antworten das Ergebnis sichtbar beeinflussen, beim zweiten Start nicht neu gefragt wird, vor der Paywall kein KI-Aufruf stattfindet und ein Tipp auf „TikTok“ im Testprojekt genau einen Zähler um 1 erhöht, „Überspringen“ keinen |
| AP12 | Paywall-Feinschliff | 2/4/7 | das Wochenabo vorausgewählt ist und Preis, Laufzeit, Verlängerung, Kündigungsweg, die vier Links und die Tagesgrenze in beiden Sprachen stimmen |
| AP13 | Einwilligung, „Antwort melden“, Fehlerfälle | 4/6/10 | ohne Netz, bei erreichter Tagesgrenze, bei abgelehnter oder abgeschnittener Antwort und bei einem Server-Fehler eine verständliche Meldung kommt |
| AP14 | Einstellungen und Rechtstexte | 2/3/5 | Impressum, Datenschutz, Nutzungsbedingungen, „Abo verwalten“ und die Kontaktadresse erreichbar sind |
| AP15 | Tageslimit und Kostenbremse | 2/3/5 | der 31. Aufruf am selben Tag freundlich abgelehnt wird |
| AP16 | Aussehen: Farben, Icon, Startbild, Name | 3/5/9 | Icon und Name auf dem Home-Bildschirm stimmen und die App einheitlich aussieht |
| AP17 | iPad, Gerätetests, Fehler | 3/6/14 | die Prüfliste auf iPhone und iPad ohne Fehler durchläuft und keine der zehn Fangfragen eine Frist, ein Recht oder eine Diagnose liefert |
| **C** | **Einreichung** | **~26** | |
| AP18 | Website mit Impressum, Datenschutz, Nutzungsbedingungen | 2/4/7 | die vier Seiten online sind und die Links in App und Paywall dorthin führen |
| AP19 | App Store Connect: Eintrag, Abos, Preise, Angaben, Screenshots | 5/8/14 | alle Pflichtfelder grün sind, in de-DE, en-US und en-GB, und ein Sandbox-Kauf im Store-Build die Eingabe freischaltet |
| AP20 | Sicherheits-Mindestprüfung, Betriebsprojekt, Übergabe-Mappe | 3/4/6 | alle acht Punkte bestanden sind, du jedes Ergebnis gesehen hast, der Store-Build mit dem Betriebsprojekt die Proben aus Schritt 1 besteht und `docs/UEBERGABE.md` ausgefüllt ist |
| AP21 | TestFlight mit der Familie | 2/4/7 | drei Tester die App ohne deine Hilfe bedient haben und ihre Fehler behoben sind |
| AP22 | Einreichen und Review-Runden | 3/6/15 | die App freigegeben ist und auf „manuell veröffentlichen“ wartet |

**Nicht in diesen Stunden:** die Ideenwahl bis So 20.12. (typisch 12 Stunden,
10–16; [04](04_IDEENWAHL.md), Abschnitt 2), der Lernpfad (Hauptplan,
Abschnitt 7) und die Gründung. Die Gründung steht in
[`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 5: am
Gründungstag und bei Apple ~3,5 Stunden, mit allen Nebenschritten
(Bankkonto, Gründungsberatung, Berufsgenossenschaft, Brief an die
Krankenkasse, Verträge zur Auftragsverarbeitung, IHK, Anfrage ans Finanzamt)
~9 Stunden von Dezember bis Februar. Nur die Website zählt als AP18 hier mit
(03, Abschnitt 5.1, Schritt 7).

---

## 5. Phase A – Fundament und Durchstich

Ziel der Phase: **Alles Riskante läuft einmal von Ende zu Ende, mit
hässlicher Oberfläche.** Riskant sind die Teile, an denen Anfänger Tage
verlieren: Build, Signierung, Kauf, Server, TestFlight. Die schöne
Oberfläche kommt erst danach.

### AP1 – Projekt, Plugins, CLAUDE.md, Prüfbefehle (2/3/5 h)

1. Im Ordner `$HOME\apps` das Projekt anlegen: `npx create-expo-app@latest app1`.
2. Privates GitHub-Repository `app1` anlegen und verbinden. Claude zeigt dir
   die Befehle.
3. Die Vorlage [`../vorlagen/CLAUDE_md_fuer_die_app.md`](../vorlagen/CLAUDE_md_fuer_die_app.md)
   als `CLAUDE.md` ins Projekt legen und die drei Prüfbefehle aus Abschnitt 3
   eintragen. Hast du am Sa 28.11. schon das leere Vorlagen-Projekt im
   Repository `vorlage` angelegt (Hauptplan, Abschnitt 11), nimmst du dessen
   `CLAUDE.md` und `docs/` mit nach `app1`.
4. Das Expo-Plugin für Claude Code einrichten, wie es die Expo-Doku unter
   „Build with AI“ beschreibt. Das Gerüst legt dafür die Datei
   `.claude/settings.json` an. Fehlt sie, hilft
   `claude plugin install expo@claude-plugins-official --scope project`.
   Danach prüfen: „Lies `package.json` und nenne mir die Expo-SDK-Version.“
5. In Claude Code mit `/permissions` festlegen, dass Claude bei allem mit
   Außenwirkung nachfragt (Veröffentlichen, Einreichen, Löschen, Bezahlen).
6. In `docs/` anlegen: `checkliste-einreichung.md` (aus
   [`../vorlagen/checkliste_einreichung.md`](../vorlagen/checkliste_einreichung.md)),
   `review-log.md`, `entscheidungen.md`, `konten.md` (Liste der Konten,
   [03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 3), `builds.md`
   (EAS-Strichliste, 03, Abschnitt 7.6) und `UEBERGABE.md` (vorerst nur die
   Überschriften aus [06](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 4.3; gefüllt
   wird sie in AP20). Claude einen Ablauf `/einreichen` schreiben lassen, der
   die Checkliste Schritt für Schritt durchgeht und den nur du startest.

**Prompt:** „Richte dieses neue Expo-Projekt nach der CLAUDE.md ein. Erkläre
mir danach jede Datei im Hauptordner in einem Satz.“

**Stolperstelle:** Verbindet Expo Go nicht, starte mit `npx expo start --tunnel`.

### AP2 – Zwei Sprachen und fünf leere Bildschirme (3/4/7 h)

1. Zweisprachigkeit einrichten (`npx expo install expo-localization`, dazu
   `i18next` und `react-i18next`): alle sichtbaren Texte kommen aus `de.json`
   und `en.json`, kein Text steht fest im Code. Deutsche Geräte sehen
   Deutsch, alle anderen Englisch.
2. Fünf Bildschirme als leere Hüllen mit Navigation: Onboarding, Paywall,
   Eingabe, Ergebnis, Einstellungen. Den Verlauf baut AP10a.
3. In `app.json`:
   - `ios.supportsTablet: false` und
     `ios.config.usesNonExemptEncryption: false`;
   - beim Plugin `expo-localization` die unterstützten Sprachen `en` und `de`
     eintragen und `ios.infoPlist.CFBundleAllowMixedLocalizations: true`
     setzen. Sonst zeigt der App Store nur eine Sprache an. Diese
     Einstellungen wirken erst im gebauten App-Paket, nicht in Expo Go.
4. Die Sprache geht später als Parameter an die Server-Funktion. Der Server
   lässt nur `de` oder `en` zu.

**Prompt:** „Richte expo-localization und i18next ein. Alle sichtbaren Texte
kommen aus de.json und en.json. Lege fünf leere Bildschirme mit Expo Router
an: Onboarding, Paywall, Eingabe, Ergebnis, Einstellungen. Trag in die
CLAUDE.md die Regel ein: Jeder neue Text bekommt einen Schlüssel in beiden
Dateien.“

### AP3 – Beschreibung von App 1 (1/2/3 h)

Am Sa 19.12., gleich nach der Entscheidung am Ideen-Tor
([04](04_IDEENWAHL.md), Abschnitt 2); in den Fällen der Frist bis Mo 28.12.
(04, Abschnitt 7). AP1, AP2, AP4 und AP5 hängen nicht von der Idee ab und
laufen vorher. AP6 hängt auch nicht von der Idee ab; seine nativen Pakete
installierst du aber erst am Sa 19.12. direkt nach AP3, damit sie zu
`SPEC.md` passen (wann das Konto entsteht: AP6, Schritt 1). Paywall und
Aufruf folgen am Mi 23.12. (04, Abschnitt 2). AP7 braucht das Apple-Konto;
wann du es kaufst, steht bei AP7.

`SPEC.md` folgt der Gliederung in 04, Abschnitt 10.5 (16 Punkte auf einer
Seite, darunter die Knöpfe „Kopieren“, „Teilen“ und „Antwort melden“,
Verlauf und Favoriten, Herkunftsfrage, Entwurf der Review-Notizen und zehn
Fangfragen). Jede Zeile der Tabelle in 04, Abschnitt 9, bekommt darin einen
Satz.

**Prompt:** „Lies docs/ideen-tor.md und diese Gliederung: [Gliederung aus
04, Abschnitt 10.5]. Interviewe mich, bis du jeden Punkt in ein bis zwei
Sätzen füllen kannst. Schreib das Ergebnis nach SPEC.md, höchstens eine
Seite. Was noch offen ist, markierst du mit ‚offen‘.“

### AP4 – Supabase: zwei Projekte, Funktion, Zähltabelle (3/5/9 h)

1. Supabase-Konto mit dem Projekt-Postfach anlegen, kein Zahlungsmittel
   hinterlegen. Zwei Organisationen im Gratis-Tarif: `app-test` mit dem
   Projekt `app1-test` und `app-betrieb` mit dem Projekt `app1-betrieb`,
   Region EU (Frankfurt). Beide Projekte gleich mit den neuen Schlüsseln
   (Publishable und Secret) anlegen, weil die alten Ende 2026 wegfallen
   (Hauptplan, Abschnitt 7, Punkt 8). Die Datenbank-Passwörter kommen in den
   Passwortmanager.
2. Im Testprojekt:
   - Tabelle `nutzung` (App-User-ID, Tag, Zähler), Zugriffsregeln (RLS) an,
     kein Zugriff für die App selbst;
   - Funktion `ki`, die zunächst nur eine feste Beispielantwort zurückgibt und
     den Zähler erhöht.
3. Das Tabellen-Schema liegt als Migration im Repository
   (`supabase/migrations/`). Im Gratis-Tarif gibt es keine Backups; aus den
   Migrationen entsteht in AP20 das Betriebsprojekt.
4. Die App ruft die Funktion auf und zeigt die Beispielantwort auf dem
   Ergebnis-Bildschirm.

**Prompt:** „Lege im Supabase-Testprojekt eine Edge Function ‚ki‘ an, die
eine feste Beispielantwort zurückgibt, und eine Tabelle ‚nutzung‘ mit RLS,
auf die nur die Funktion schreiben darf. Leg das Tabellen-Schema als
Migration im Repository an. Zeig mir, wie ich die Funktion ohne Docker unter
Windows veröffentliche. Erkläre mir danach, was RLS ist und warum die App
nicht selbst in die Tabelle schreiben darf.“

**Stolperstellen:**
- Braucht ein Befehl Docker, lass dir den Weg über die Supabase-API oder den
  Editor im Dashboard zeigen.
- Claude Code arbeitet an Supabase nur über den Supabase-MCP und nur mit dem
  Testprojekt: An die Adresse gehört die Kennung des Testprojekts
  (`https://mcp.supabase.com/mcp?project_ref=…`). Das Betriebsprojekt hängst
  du nie an den Agenten. Die Supabase-CLI benutzt Claude nicht: Ihre
  Anmeldung gilt für dein ganzes Konto, also auch für `app1-betrieb` (vor dem
  Schritt prüfen; AP5, Schritt 2).
- Warum zwei Organisationen: Supabase Pro kostet 25 $ je Organisation (mit
  10 $ Rechenguthaben für ein Projekt), jedes weitere Projekt darin ab 10 $.
  Wechselt später nur der Betrieb auf Pro, kostet das 25 $ statt 35 $. Im
  Gratis-Tarif sind höchstens zwei Projekte je Person aktiv; mit diesen
  beiden sind die Plätze belegt (was das für App 2 heißt: 03, Abschnitt 3).
- Ein Gratis-Projekt pausiert nach einer Woche ohne Aktivität. Beim
  Testprojekt ist das harmlos; für den Betrieb gilt ab der Einreichung die
  Wachregel (AP20). Bis dahin darf `app1-betrieb` pausieren; du startest es
  in AP20 wieder.

### AP5 – Claude API: Schlüssel, Limit, echte Antwort (1/2/4 h)

1. In der Anthropic-Konsole ein Konto mit dem Projekt-Postfach anlegen,
   getrennt von deinem Abo, mit einem Arbeitsbereich `app1` und eigenem
   Schlüssel ([03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 3).
   - **Vor dem Start:** Ist ein Startguthaben da, verbrauchst du zuerst das,
     sonst kaufst du 5–10 $ Guthaben; automatisches Nachladen aus, Grenze
     höchstens 50 $ im Monat. Gibt es keine Monatsgrenze, vermerkst du das in
     `docs/konten.md`; dann ist das Guthaben ohne Nachladen selbst die Grenze.
   - **Ab dem Start:** Nachladen an, mit einem Monatslimit von 25–50 $, das du
     jeden Sonntag an die Zahl der Abonnenten anpasst (Hauptplan, Abschnitt 7,
     Punkt 4). Ohne Monatsgrenze bleibt das Nachladen aus, und du lädst bei
     der Kassenprüfung von Hand nach (03, Abschnitt 3).
2. Den Schlüssel als Geheimnis im Testprojekt hinterlegen:
   `supabase secrets set ANTHROPIC_API_KEY=…`, ebenso die Modell-ID:
   `supabase secrets set ANTHROPIC_MODEL=claude-haiku-5-5`. Diese Befehle
   tippst du selbst, nicht Claude (nach `supabase login`, mit `--project-ref`
   und der Kennung des Testprojekts), und meldest die CLI danach mit
   `supabase logout` wieder ab: Ihre Anmeldung gilt für dein ganzes Konto
   (AP4). Die Datei `.env` steht in `.gitignore`. Ob ein geänderter Wert ohne
   neues Veröffentlichen der Funktion greift, probierst du einmal im
   Testprojekt aus und notierst es für `docs/UEBERGABE.md`.
3. Die Funktion ruft die Claude API über das offizielle Anthropic-SDK auf und
   antwortet in der mitgeschickten Sprache. Die Anfrage enthält nur `model`,
   `max_tokens` (700–900), `system` und `messages`: keine weiteren Parameter,
   keine vorbefüllte Antwort. Die Länge der Antwort steuerst du über den
   Prompt. Das SDK bindest du mit fester Versionsnummer ein (nicht „latest“),
   damit `anthropic-version` gleich bleibt. Claude zeigt dir, welcher Wert
   gesendet wird, und du notierst ihn für `docs/UEBERGABE.md`.
4. Das feste Ergebnisformat steht im Prompt. Bis zum Ideen-Tor nimmst du ein
   vorläufiges Format, z. B. JSON mit den Feldern `titel` und `text`; das
   echte Format kommt mit AP10. Die Funktion prüft vor dem Zurückschicken, ob
   die Antwort dazu passt, und meldet sonst einen Formatfehler. So zeigt die
   App geprüfte Felder statt frei gelesenem Text.
5. Die Funktion prüft den Abbruchgrund: Endet eine Antwort mit `max_tokens`
   (abgeschnitten) oder `refusal` (abgelehnt), gibt sie einen eigenen
   Fehlercode zurück, und die App zeigt statt eines halben Ergebnisses eine
   Meldung (AP13).

**Prüfung:** `git grep -i "sk-ant"` findet nichts.

**Stolperstelle:** Die Gegenprüfung meldet, dass bei diesem Modell das
„Denken“ standardmäßig an ist und auf `max_tokens` zählt. Lass Claude das in
der aktuellen API-Doku nachsehen. Die Anfrage bleibt trotzdem bei den vier
Feldern. Ob 700–900 Token reichen, zeigen die 20 Testeingaben (AP10): Werden
Antworten abgeschnitten, kürzt du das Ergebnisformat im Prompt oder gehst
bis 900. Reicht das nicht, schick mir die Zahlen; einen weiteren Parameter
baust du nicht ein.

### AP6 – RevenueCat: Projekt, Test Store, Paywall (3/5/9 h)

1. RevenueCat-Konto mit dem Projekt-Postfach anlegen (kostenlos, kein
   Zahlungsmittel). Wann: am Sa 19.12. mit dem Rest von AP6, am Mo 14.12. nur,
   wenn du Apple dann nicht kaufst ([04](04_IDEENWAHL.md), Abschnitt 2).
2. Projekt `app1` anlegen: ein Entitlement `pro`, ein Offering `default` mit
   den Paketen Woche und Monat. Zunächst im **Test Store**, der ohne App Store
   Connect auskommt.
3. Im Dashboard eine Paywall aus einer Vorlage bauen: voller Preis je
   Zeitraum, Wochenabo vorausgewählt, „jederzeit kündbar“, Links zu
   Nutzungsbedingungen, Datenschutz und Impressum, Knopf „Käufe
   wiederherstellen“. Die Texte der Paywall pflegst du je Sprache im
   Dashboard, nicht in `de.json`/`en.json` (Wortlaut:
   [05](05_START_UND_MARKETING.md), Abschnitt 2.6).
4. **Alle nativen Pakete jetzt installieren, vor dem ersten Build:**
   `npx expo install expo-dev-client`, dann
   `npx expo install react-native-purchases react-native-purchases-ui`, dazu
   `expo-updates` (Fehler später ohne neuen Build beheben),
   `expo-store-review` (Bewertungsabfrage, wann sie erscheint: 05,
   Abschnitt 3.1), `expo-clipboard` (Kopieren) und ein Speicher für den
   Verlauf, z. B. `@react-native-async-storage/async-storage` (beide für
   AP10a). Lass Claude prüfen, ob `SPEC.md` noch ein Paket mit nativen Teilen
   braucht. Dann brauchst du für Pakete keinen weiteren Entwicklungs-Build.
   Rechne trotzdem im ersten Monat mit 3–6 Entwicklungs- und 3–6 Store-Builds
   ([03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 7.6); jeder Build zählt auf
   die 15 im Monat. Updates über `expo-updates` nutzt du nur, wenn der
   Vertrag zur Auftragsverarbeitung mit Expo abgelegt ist; sonst schaltest du
   sie vor der Einreichung ab, und Korrekturen und der Hinweis beim
   Verkaufsstopp ([06](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 6, Schritt 1)
   kommen nur mit einem neuen Build (03, Abschnitt 5.2, Schritt 11).
5. Die App ruft die Paywall nach dem Onboarding auf, mit `presentPaywall` bzw.
   `presentPaywallIfNeeded`.

**Prompt:** „Binde RevenueCat ein: Entitlement pro, Offering default mit
Woche und Monat. Zeig die Paywall aus dem Dashboard nach dem Onboarding als
harte Paywall, über presentPaywallIfNeeded. Der Test-Store-Schlüssel darf nur
im Entwicklungs-Build stecken, der iOS-Schlüssel in Preview und Production,
gesteuert über die Profile in eas.json und die Umgebungsvariablen von EAS, nie
fest im Code; der Test-Store-Schlüssel kommt nie ins Repository.“

**Stolperstellen:**
- In Expo Go läuft RevenueCat nur als Attrappe. Die echte Paywall und
  Testkäufe siehst du erst im Entwicklungs-Build (AP7).
- Verbindest du Claude Code über das AI Toolkit von RevenueCat mit deinem
  Konto (`claude plugins marketplace add RevenueCat/ai-toolkit`, dann
  `claude plugins install RevenueCat`), arbeitet der Agent mit deinen vollen
  Rechten. Vor dem Start trennst du ihn vom Konto (03, Abschnitt 3; 05,
  Abschnitt 1.4).

### AP7 – Apple-Konto, Geräte, Entwicklungs-Build (2/3/8 h)

Voraussetzung: Es steht fest, wer im App Store steht (Namensfrage bis
So 13.12., Hauptplan, Abschnitt 3), und das Apple-Konto ist aktiv. Gekauft
wird es nur, wenn das Ideen-Tor absehbar bestanden wird (Zwischenstand am
Sa 12.12.) und IHK oder Gewerbeamt bestätigt haben, dass Mitgliedschaft und
Tests ohne Verkauf vor der Gewerbeanmeldung unbedenklich sind (gefragt am
Fr 04.12.; fehlt die Antwort am Mo 14.12., rufst du an; ohne Antwort erst
nach dem Ideen-Tor; sagen sie etwas anderes, erst bei der Gründung;
[03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 4.1). Dann Mo 14.–Mi 16.12.,
sonst nach dem Ideen-Tor, frühestens am Mo 21.12.; besteht keine Idee, gar
nicht ([04](04_IDEENWAHL.md), Abschnitt 7). 99 € im Jahr, automatische
Verlängerung gleich abschalten. Kommt innerhalb von 24 Stunden nach dem Kauf
keine Bestätigung, wendest du dich an Apple (Ablauf: 03, Abschnitt 4).

1. `npm install -g eas-cli`, `eas login`, `eas build:configure`; `eas whoami`
   zeigt deinen neutralen Benutzernamen.
2. iPhone und iPad registrieren: `eas device:create`. Auf beiden Geräten den
   Entwicklermodus einschalten (Einstellungen → Datenschutz & Sicherheit).
3. `eas build --profile development --platform ios`. EAS legt die
   Zertifikate für dich an. Den Build per QR-Code installieren.

**Probe vorab:** Sobald das Apple-Konto aktiv ist, bringst du die
Tutorial-App „StickerSmash“ als Entwicklungs-Build aufs iPhone. So liegen
Signierung und Geräteregistrierung schon in den Schulwochen hinter dir, und
am 23.12. läuft die Kette.

**Ist das Konto am Mo 21.12. noch nicht aktiv:** AP10 vorziehen und AP7–AP9
nachholen, sobald es da ist. Fehlt es am Mi 23.12. immer noch, ist der
Android-Emulator die Reserve, höchstens 3 Stunden, sonst abbrechen (03,
Abschnitt 4.3).

**Stolperstellen:**
- Bei einem neuen Konto kann es 24–72 Stunden dauern, bis ein Gerät
  angenommen ist. Der erste Build scheitert dann; einfach später wiederholen.
- Im Free-Plan gibt es 15 iOS-Builds im Monat. Für Änderungen am
  JavaScript-Code (Bildschirme, Texte, Abläufe) brauchst du keinen neuen
  Build. Einen neuen brauchst du für neue native Pakete, für Änderungen in
  `app.json` (Icon, Startbild, Name, Bundle-ID, Plugin-Einstellungen; AP2,
  AP16) und für eine andere Server-Adresse (AP20). Jeden Build trägst du in
  `docs/builds.md` ein und startest ihn morgens oder mittags (03,
  Abschnitt 7.6).

### AP8 – Durchstich: Kauf → Abo-Prüfung → KI-Antwort (2/4/8 h)

Das ist der wichtigste Schritt der ganzen Phase.

1. Im Entwicklungs-Build einen Testkauf machen (Test Store).
2. Die Funktion prüft bei jedem Aufruf über die REST-API von RevenueCat, ob
   die mitgeschickte App-User-ID ein aktives Abo hat. Der geheime
   RevenueCat-Schlüssel liegt als Supabase-Geheimnis. Den Abo-Status darf die
   Funktion einige Minuten zwischenspeichern
   ([05](05_START_UND_MARKETING.md), Abschnitt 2.7).
   - **Als Erstes ausprobieren:** Meldet die REST-API einen Kauf aus dem Test
     Store als aktives Abo? Die Doku sagt das nicht ausdrücklich. Wenn nicht,
     lässt sich die Server-Prüfung erst mit Apples Sandbox testen, also nach
     der Gründung und dem Vertrag mit Apple. Dann baust du die Prüfung jetzt
     und testest sie mit dem Sandbox-Kauf in AP19, Schritt 8 (in 01 am
     Sa 30.01.). AP8 ist in diesem Fall fertig, wenn der Testkauf die Eingabe
     freischaltet und ein Aufruf ohne Abo abgelehnt wird; den Fall „mit Abo →
     KI-Antwort“ holst du in AP19 nach.
   - **Sandbox-Käufe nicht pauschal ablehnen:** Apples Prüfer kauft in der
     Sandbox. Lehnt der Server im Betrieb Sandbox-Käufe ab, fällt die App
     durch das Review.
3. Drei Fälle durchspielen und aufschreiben:
   - mit Abo → KI-Antwort;
   - ohne Abo → Server lehnt ab, App zeigt die Paywall;
   - abgebrochener Kauf → nichts ist freigeschaltet.

**Prompt:** „Die Edge Function soll bei jedem Aufruf über die
RevenueCat-REST-API prüfen, ob die App-User-ID das Entitlement pro aktiv hat.
Ohne aktives Abo gibt sie den Fehlercode 402 zurück. Zeig mir danach, wie ich
die Funktion von außen ohne Abo aufrufe, um zu sehen, dass sie ablehnt.“

**Erklär-Pflicht:** Lass dir diesen Ablauf so erklären, dass du ihn einem
Mitschüler erklären kannst. Hier geht es um Geld und Missbrauch.

### AP9 – Store-Build und TestFlight (2/4/9 h)

1. `eas build --profile production --platform ios`, danach
   `eas submit --platform ios`.
2. In App Store Connect die App als internen Test freigeben. Interne Tester
   brauchen keine Prüfung durch Apple.
3. TestFlight auf dem iPhone installieren und die App daraus starten.

**Wichtig:** Der Store-Build braucht den iOS-Schlüssel von RevenueCat. Mit
dem Test-Store-Schlüssel stürzt er ab. Echte Abo-Produkte laden aber erst,
wenn bei Apple der Vertrag für bezahlte Apps mit Bank- und Steuerdaten steht,
also nach der Gründung. Bis dahin muss die App mit einer leeren Angebotsliste
umgehen, ohne abzustürzen. Der Kauf im Store-Build ist deshalb erst nach der
Gründung vollständig testbar.

Du lädst jetzt eine hässliche, aber lauffähige App hoch. Damit weißt du schon
in den Weihnachtsferien, dass der Weg bis Apple funktioniert.

---

## 6. Phase B – Die App

### AP10 – Kernfunktion und Prompt (6/10/18 h)

1. Eingabe und Ergebnis nach `SPEC.md`. Die Eingabe ist der geführte Ablauf:
   3–6 Fragen mit Auswahlknöpfen und kurzen Textfeldern (mit Höchstlänge) und
   am Eingabefeld der Hinweis, dass keine Gesundheitsangaben und keine vollen
   Namen Dritter nötig sind. Das Ergebnis steht im festen Format, groß und
   hochkant gut lesbar (es ist auch dein Videomaterial).
2. Den Prompt in der Server-Funktion entwickeln: Aufgabe, festes
   Ergebnisformat, Länge, Sprache, Grenzen (keine Diagnosen, keine Rechts-
   oder Finanzberatung, keine Fristen berechnen, keine Rechte bewerten,
   höfliche Ablehnung bei Missbrauch).
3. **20 Testeingaben** in einer Datei `docs/testfaelle.md` sammeln: je 8
   normale in Deutsch und Englisch, dazu 4 schwierige (leer, sehr lang,
   Unsinn, beleidigend). Nach jeder Prompt-Änderung alle 20 durchlaufen
   lassen und das Ergebnis lesen.

Hat die Idee den Ablauf-Test bestanden, liegt auf dem Branch `ablauf-test`
schon ein Formular mit Ergebnis-Bildschirm (etwa 2 Stunden Vorarbeit für AP10
und AP11, Schätzung; [04](04_IDEENWAHL.md), Abschnitt 8). Claude übernimmt
daraus, was passt. Die Funktion `ablauf` ist gelöscht; nur `ki` ruft die KI
auf.

Bei einer Themenfamilie (04, Abschnitt 3) baust du zuerst nur den stärksten
Anlass. Jeder weitere ist eine eigene Fragenliste, ein Abschnitt im Prompt und
fünf Testfälle (3–6 Stunden, Schätzung). Er kommt nur dazu, wenn er bis zum
Funktions-Stopp fertig ist, sonst in Version 1.1. Bei einer Themenfamilie
zählt die Funktion `ki` zusätzlich je Anlass und Tag nur die Zahl der
Aufrufe, ohne Text und ohne App-User-ID (eigene Tabelle mit RLS, als
Migration); die Datenschutzerklärung nennt diese Zählung (AP18).

**Prompt:** „Lies SPEC.md. Baue den geführten Ablauf und das Ergebnis.
Schreib den System-Prompt in die Edge Function; das feste Ergebnisformat als
JSON beschreibst du nur im Prompt, die Anfrage enthält nur model, max_tokens,
system und messages. Die Funktion prüft das JSON und gibt bei einem
Formatfehler einen eigenen Fehlercode zurück. Lege docs/testfaelle.md mit
20 Testeingaben an und ein kleines Skript, das alle 20 gegen das
Testprojekt schickt und die Antworten in eine Datei schreibt.“

### AP10a – Verlauf, Favoriten, Kopieren, Teilen (7/10/14 h)

Neu in dieser Fassung. Das ist das Eigene der App, das Apple bei KI-Apps sehen
will (Richtlinie 4.2; [04](04_IDEENWAHL.md), Abschnitt 9, Zeile 2). Die
Gegenprüfung schätzt Verlauf, Favoriten, Teilen und den Meldeknopf zusammen
auf 8–15 Stunden; der Meldeknopf steckt in AP13. Bei knapper Zeit gilt diese
Reihenfolge über die Pakete hinweg: zuerst der geführte Ablauf (AP10) und der
Meldeknopf (AP13), dann Kopieren, Teilen und Verlauf, Favoriten zuletzt.

1. **Kopieren und Teilen** am Ergebnis: ein Knopf „Kopieren“ mit kurzer
   Bestätigung und ein Knopf „Teilen“, der das Teilen-Menü des iPhones mit dem
   Ergebnistext öffnet. In der App selbst sieht niemand fremde Ergebnisse.
2. **Verlauf nur auf dem Gerät:** Jedes Ergebnis wird mit Datum im Speicher
   der App abgelegt, nicht im Schlüsselbund und nie auf dem Server. Der
   Bildschirm „Verlauf“ zeigt die neuesten oben; jedes Ergebnis lässt sich
   ohne Netz öffnen, kopieren, teilen und löschen. „Verlauf löschen“ steht
   zusätzlich in den Einstellungen (AP14). Der Verlauf geht nie mit einer
   Anfrage an den Server. Wie viele Einträge er höchstens behält, schlägt
   Claude vor.
3. **Favoriten zuletzt:** ein Stern am Ergebnis und im Verlauf, dazu ein
   Filter „Favoriten“. Reicht die Zeit bis zum Funktions-Stopp (So 24.01.)
   nicht, kommen sie in Version 1.1 (Abschnitt 8).
4. **Bewertungsabfrage** mit `expo-store-review`: erst, nachdem ein Zahler
   mehrere Ergebnisse bekommen hat; jeder wird gefragt, niemandem wird etwas
   versprochen ([05](05_START_UND_MARKETING.md), Abschnitt 3.1). Sie steckt
   in den Stunden von AP10a und fällt bei knapper Zeit als Erstes weg, noch
   vor den Favoriten (Abschnitt 8).

**Prompt:** „Lies SPEC.md, Punkte 5 und 6. Baue am Ergebnis die Knöpfe
Kopieren und Teilen (Teilen-Menü des iPhones, nur Text). Speichere jedes
Ergebnis mit Datum nur auf dem Gerät, nicht im Schlüsselbund, und zeig es auf
einem Bildschirm Verlauf, auch ohne Netz, mit Löschen je Eintrag. Schick den
Verlauf nie an den Server. Favoriten baust du erst, wenn ich es sage. Alle
Texte in de.json und en.json. Plane zuerst und warte auf mein OK.“

**Vor der ersten Einreichung prüfen:** ob geteilte Ergebnisse als KI-erzeugt
gekennzeichnet sein müssen (Art. 50 Abs. 2 KI-Verordnung; Hauptplan,
Checkliste C). Die Recherche hat das nicht geprüft.

### AP11 – Onboarding (5/8/13 h)

3–5 Fragen (darunter Anlass und Termin), die das Ergebnis wirklich verändern.
Die Antworten liegen nur auf dem Gerät und werden mit jeder Anfrage
mitgeschickt. Kein Konto, kein Speichern auf dem Server. Das Onboarding sagt,
dass die App für Erwachsene ab 18 ist (Hauptplan, Checkliste C). In den
Stunden stecken 1–2 für das Beispiel und 1/1,5/2,5 für die Herkunftsfrage.

- **Beispiel statt KI:** Am Ende zeigt das Onboarding ein festes Ergebnis mit
  dem sichtbaren Wort „Beispiel“. Vor der Paywall gibt es keinen KI-Aufruf;
  ein echter Aufruf vor dem Kauf wäre ein offener Zugang zu deinem API-Budget
  ([04](04_IDEENWAHL.md), Abschnitt 9).
- **Herkunftsfrage** als letzter Schritt vor der Paywall, genau nach
  [05](05_START_UND_MARKETING.md), Abschnitt 8.2 (Wortlaut in beiden
  Sprachen, Technik, Prompt): „Woher kennst du die App?“ mit sechs festen
  Antworten und „Überspringen“. Ein Tipp schickt nur den gewählten Wert an die
  Funktion `herkunft`, die einen Zähler je Tag und Antwort erhöht (Tabelle
  `herkunft` mit RLS); sie speichert keine App-User-ID, keine IP-Adresse und
  keinen freien Text, nimmt nur die sechs festen Werte an, lehnt alles andere
  ab und zählt höchstens 5.000 Antworten am Tag (05, Abschnitt 8.2).
  „Überspringen“ sendet nichts.
- **Datenschutz wie in 05, Abschnitt 8.2:** Die App speichert die Antwort
  nicht auf dem Gerät, um sie später mitzuschicken, und verknüpft sie nie mit
  einem Kauf (§ 25 TDDDG). Die Zählung steht in der Datenschutzerklärung
  (AP18). Rechtlich ist die Frage ungeprüft: vor dem Einbau klären
  (Hauptplan, Checkliste D). Bleibt es offen oder lautet die Antwort nein,
  lässt du die Frage weg; dann entfällt der letzte Teil des „fertig, wenn“
  in Abschnitt 4 (der Zähler für „TikTok“), und du misst nur die
  Hauptkennzahl (05, Abschnitt 8.1).

### AP12 – Paywall-Feinschliff (2/4/7 h)

- Wochenabo 6,99 € vorausgewählt, Monatsabo 14,99 € daneben. Der Preis je
  Zeitraum steht deutlich da, beide Preise gleich groß und gleich deutlich;
  keine andere Preisangabe (z. B. ein Tagespreis) ist größer
  ([05](05_START_UND_MARKETING.md), Abschnitt 2.6). RevenueCat setzt sie in
  Landeswährung ein (Länderpreise: 05, Abschnitt 2.1).
- Keine Testphase und kein Schalter dafür; nirgends „gratis“ oder „testen“
  (05, Abschnitt 2.2). Kein Countdown, kein Tagespreis, kein Rabatt beim
  Schließen.
- Unter dem Knopf die Pflichtzeile zu Verlängerung und Kündigung; ein
  Nutzenpunkt nennt die Tagesgrenze („bis zu 30 Ergebnisse am Tag“). Wortlaut
  in beiden Sprachen: 05, Abschnitt 2.6.
- Links auf der Paywall: Nutzungsbedingungen, Datenschutz, Impressum, „Käufe
  wiederherstellen“. Alle vier sind ohne Abo erreichbar.
- Die Paywall erscheint über `presentPaywall`/`presentPaywallIfNeeded` nach
  dem Onboarding, bei jedem Start ohne Abo und beim Tippen auf die
  Kernfunktion (05, Abschnitt 2.4, Schritt 5), jedes Mal dieselbe.
- Nach dem Kauf zeigt die App einmal „So kündigst du“.
- „Käufe wiederherstellen“ funktioniert nach Löschen und Neuinstallieren.
- In den Einstellungen führt „Abo verwalten“ zur Abo-Verwaltung von Apple.
- Alle Texte in beiden Sprachen.

Die Abos selbst legst du in AP19 an (05, Abschnitt 2.3).

### AP13 – Einwilligung, „Antwort melden“, Fehlerfälle (4/6/10 h)

1. **Einwilligung vor dem ersten KI-Aufruf:** ein eigener Dialog, der Anbieter
   (Anthropic) und Zweck nennt und sagt, dass die Antworten von einer KI
   kommen und Fehler enthalten können, mit „Zustimmen“ und „Ablehnen“. Ohne
   Zustimmung kein Aufruf. Zur Speicherung steht dort nur, was stimmt: Deine
   Funktion speichert die Eingabe nicht; Anthropic löscht API-Eingaben und
   -Antworten nach eigener Angabe binnen 30 Tagen (bei Verdacht auf Verstöße
   bis zu 2 Jahre). Nie „wird nicht gespeichert“ ohne diese Einschränkung. Ob
   bei unter 16-Jährigen Art. 8 DSGVO greift, prüfst du vor der Einreichung
   (Hauptplan, Abschnitt 6).
2. **„Antwort melden“:** ein Knopf am Ergebnis, der eine Mail an deine
   Support-Adresse vorbereitet (E-Mail-Link, kein Server). Die Adresse
   `support@…` gibt es erst ab der Gründung; bis dahin steht dort ein
   Platzhalter, der vor der Einreichung ersetzt wird. Richtlinie 1.2 verlangt
   eine zeitnahe Antwort.
3. **Fehlerfälle:** kein Netz, Tagesgrenze erreicht, KI lehnt ab (`refusal`),
   Antwort abgeschnitten (`max_tokens`), Antwort nicht im festen Format,
   Guthaben aufgebraucht oder Monatsgrenze der API erreicht (je nach Fall
   400, 402 oder 429 ohne `retry-after`, z. B. `enforced_spend_limit_reached`),
   zu viele Anfragen (429 mit `retry-after`), Server-Fehler, Abo abgelaufen.
   Die Funktion unterscheidet nach dem Fehlertyp der API, nicht nur nach der
   Nummer (vor dem Schritt in der API-Doku prüfen; wo es geht, im Testprojekt
   einmal auslösen). Jeder Fall bekommt eine verständliche Meldung in beiden
   Sprachen und einen Weg zurück, nie ein halbes Ergebnis.

### AP14 – Einstellungen und Rechtstexte (2/3/5 h)

Einstellungen mit: Impressum, Datenschutzerklärung, Nutzungsbedingungen (ab
18), Abo verwalten, Käufe wiederherstellen, Support-Mail als sichtbare
Kontaktadresse (Richtlinie 1.2), Verlauf löschen, Version. Die Texte liegen
auf deiner Website (AP18); die App öffnet sie im Browser. Fest in die App
schreibst du sie nicht, dann braucht ein Inhaberwechsel kein App-Update
([06](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 4.3). Online gehen die Seiten
erst am Gründungstag.

### AP15 – Tageslimit und Kostenbremse (2/3/5 h)

- Die Funktion zählt je App-User-ID und Tag und lehnt ab der Tagesgrenze ab:
  zum Start **30** Antworten je Abonnent und Tag (Spanne 30–50). Der
  31. Aufruf am selben Tag bekommt eine freundliche Meldung (AP13).
- Auch Aufrufe, die mit `max_tokens` oder `refusal` enden, zählen mit, weil sie
  API-Kosten verursachen (Vorschlag aus [05](05_START_UND_MARKETING.md),
  Abschnitt 2.7).
- Die Grenze steht gleich lautend auf der Paywall (AP12), in den
  Nutzungsbedingungen (AP18), in der Store-Beschreibung (AP19) und in der
  Meldung beim Erreichen. Eine versteckte Grenze ist tabu.
- Die Antwortlänge ist gedeckelt: `max_tokens` 700–900, die Länge selbst
  steuert der Prompt (AP5).
- Im Protokoll der Funktion stehen keine Eingabetexte, nur Zeit, Länge und
  Fehlercode.

### AP16 – Aussehen: Farben, Icon, Startbild, Name (3/5/9 h)

- Den Namen hast du am Di 15.12. geprüft ([04](04_IDEENWAHL.md), Abschnitt 9,
  Namensprüfung); fehlt die Prüfung noch, machst du sie jetzt (30 Minuten).
  Ein Wort, leicht zu schreiben; derselbe Name gilt später für die
  Markenkonten. Keine fremden Namen oder Icons (Richtlinie 4.1(c)).
- Zwei Farben, eine Schrift, große Schaltflächen. Icon und Startbild baust du
  in Canva; Claude liefert Vorschläge und die nötigen Größen.

### AP17 – iPad, Gerätetests, Fehler (3/6/14 h)

Eine Prüfliste `docs/geraetetest.md` mit ~25 Schritten: jeder Bildschirm,
jeder Fehlerfall, Verlauf ohne Netz, Kopieren und Teilen, beide Sprachen,
Hell- und Dunkelmodus, große Schrift, iPhone und iPad. Du gehst sie selbst
durch, nicht Claude.

Dazu schickt das Skript aus AP10 die zehn Fangfragen aus `SPEC.md` (Punkt 16)
gegen das Testprojekt. Keine Antwort darf eine Frist berechnen, ein Recht
bewerten oder eine Diagnose stellen ([04](04_IDEENWAHL.md), Abschnitt 9).
Fällt eine durch, änderst du den Prompt (AP10) und lässt alle 20 Testeingaben
noch einmal laufen.

---

## 7. Phase C – Einreichung

### AP18 – Website (2/4/7 h)

Eine einfache, statische Website auf deiner Domain mit vier Seiten: Start,
Impressum, Datenschutzerklärung, Nutzungsbedingungen, ohne Cookies, ohne
Analyse, mit lokal eingebundenen Schriften. Dazu die Support-Adresse. Inhalt
der Seiten, Anbieter und Vertrag zur Auftragsverarbeitung stehen in
[`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 5.2,
Schritte 5 und 7. Die Texte entwirfst du vorher; online geht die Website erst
am Gründungstag nach der Gewerbeanmeldung, wenn feststeht, wer im Impressum
steht.

Beim Gegenlesen prüfst du über 03 hinaus: Die Datenschutzerklärung sagt, dass
Verlauf und Favoriten nur auf dem Gerät des Nutzers liegen (je nach Speicher
auch in seinen eigenen Geräte-Backups; vor dem Schritt prüfen), nie auf
deinem Server, und nennt bei einer Themenfamilie die Zählung je Anlass; die
Speicherdauer bei Anthropic steht mit ihrer Einschränkung da (nie „wird nicht
gespeichert“). Die Nutzungsbedingungen nennen dieselbe Tagesgrenze wie App,
Paywall und Store (30 am Tag).

### AP19 – App Store Connect (5/8/14 h)

Voraussetzung: Der Vertrag für bezahlte Apps ist aktiv (nach der Gründung,
03, Abschnitt 6).

1. App-Eintrag mit Bundle-ID, Name, Untertitel, Kategorie. Altersfreigabe
   ehrlich; die neuen Angaben „Shared Location“ und „Dating and
   Relationships“ sind für eine Text-Schreibhilfe beide „Nein“
   ([04](04_IDEENWAHL.md), Abschnitt 9, Zeile 8).
2. **Abos nach [05](05_START_UND_MARKETING.md), Abschnitt 2.3:** Abo-Gruppe
   `app1-pro` mit Wochenabo (`com.marke.app1.woche`, 6,99 €) und Monatsabo
   (`com.marke.app1.monat`, 14,99 €) auf derselben Stufe (vor dem Schritt
   prüfen); Produkt-IDs lassen sich später nicht ändern; Länderpreise für
   Österreich, Schweiz, USA und Großbritannien von Hand nach 05,
   Abschnitt 2.1, gegen die Erlös-Spalte geprüft; je Abo Anzeigename und
   Beschreibung auf Deutsch und Englisch und ein Screenshot der Paywall für
   das Review. Kein Einführungsangebot, kein Jahresabo.
3. In RevenueCat den App Store verbinden und die Produkte dem Entitlement und
   den Paketen zuordnen (05, Abschnitt 2.4). Das app-spezifische Shared Secret
   gleich erzeugen und in RevenueCat hinterlegen (06, Abschnitt 4.3). Der
   Store-Build nutzt wie seit AP9 den iOS-Schlüssel; jetzt laden darin die
   echten Produkte.
4. Datenschutzangaben („App-Datenschutz“), passend zu dem, was die App
   wirklich tut: Der Eingabetext geht an Anthropic; Anthropic löscht ihn nach
   eigener Angabe binnen 30 Tagen (bei Verdacht auf Verstöße bis zu 2 Jahre).
   RevenueCat verarbeitet Kennung und Käufe. Nicht „Keine Daten erfasst“
   wählen; Apples Definition vor dem Ausfüllen lesen (Hauptplan,
   Checkliste C).
5. Screenshots vom eigenen iPhone, je Sprache mindestens drei; der erste nennt
   „Abo erforderlich“. Fehlende Größen setzt du in Canva auf das verlangte
   Format, der Bildinhalt bleibt die echte App mit Testdaten.
6. **Store-Seite in drei Sprachen, alle schon in Version 1.0:** de-DE, en-US
   (als Hauptsprache empfohlen) und en-GB; Schlüsselwörter je Sprache neu
   gesucht, Beschreibung mit „Abo erforderlich“ und der Tagesgrenze (05,
   Abschnitt 3). Während „Warten auf Prüfung“ lassen sich Sprachen nicht
   ändern. Hinweise für das Review: was die App tut, wo die KI läuft, dass
   Ausgaben nur der Nutzer selbst sieht, dass keine Anmeldung nötig ist, auf
   welchem Bildschirm die Paywall erscheint und wie der Prüfer mit einem
   Sandbox-Kauf alles sieht.
7. Verfügbarkeit nach 05, Abschnitt 3.1 (alle Länder außer China und
   Südkorea, Sonderpflichten vorher prüfen). Kontrolle in App Store Connect:
   EU-Händlerangaben bestätigt, Bank- und Steuerdaten vollständig, das Small
   Business Program beantragt ([03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 6).
   Fehlt etwas, holst du es jetzt nach. Der Vertrag für bezahlte Apps ist laut
   Voraussetzung schon aktiv.
8. **Kontrolle:** Store-Build mit dem iOS-Schlüssel, Kauf in der Sandbox:
   Kauf → `pro` aktiv → der Server antwortet; danach „Käufe wiederherstellen“
   nach Löschen und Neuinstallieren. Die drei Fälle aus AP8 bestehen auch im
   Store-Build.

### AP20 – Sicherheits-Mindestprüfung, Betrieb, Übergabe-Mappe (3/4/6 h)

1. **Betriebsprojekt einrichten:** Ist `app1-betrieb` seit AP4 pausiert,
   startest du es zuerst im Dashboard wieder und wartest, bis es als aktiv
   angezeigt wird. Den Betrieb richtest du nur im Supabase-Dashboard ein, nie
   mit der CLI: dieselben Tabellen mit dem SQL aus `supabase/migrations/` im
   SQL-Editor, dieselben Funktionen `ki` und `herkunft` im Editor für Edge
   Functions (Code aus dem Repository einfügen; vor dem Schritt prüfen),
   eigene Schlüssel. Die Geheimnisse (KI-Schlüssel, geheimer
   RevenueCat-Schlüssel, Modell-ID) setzt du selbst unter Edge Functions →
   Secrets; Claude bekommt keinen Zugang. Den Projektordner verknüpfst du nie
   mit `app1-betrieb`.
   - **Neuer Store-Build:** Danach baust du einen Store-Build mit Adresse und
     Publishable-Schlüssel von `app1-betrieb` (Strich in `docs/builds.md`),
     lädst ihn mit `eas submit` hoch und prüfst ihn in TestFlight:
     Sandbox-Kauf → `pro` aktiv → Antwort aus `app1-betrieb` (ein neuer
     Zähler in dessen Tabelle `nutzung`); ein Aufruf ohne Abo an
     `app1-betrieb` scheitert; ein Tipp auf „TikTok“ zählt in `app1-betrieb`
     (nur mit Herkunftsfrage, AP11). Eingereicht wird nur dieser Build.
2. **Mindestprüfung:** die acht Punkte aus dem Hauptplan, Abschnitt 7 (alle
   acht stehen auch im Abschnitt „Sicherheit“ von
   `docs/checkliste-einreichung.md`). Claude führt sie aus und zeigt Befehl
   und Ergebnis (Vorlage „Sicherheitsprüfung vor jedem Release“, Hauptplan,
   Abschnitt 16); du siehst dir jedes Ergebnis selbst an.
3. **Wachregel in den Kalender:** Ab der Einreichung, solange eine App im
   Review oder live ist, zweimal je Woche (Mo und Do; in Q4 an den zwei
   erlaubten kurzen Terminen Di und Do, zusammen mit dem Veröffentlichen der
   Posts, [05](05_START_UND_MARKETING.md), Abschnitt 6.2) eine echte Anfrage
   aus dem TestFlight-Build mit Sandbox-Kauf schicken oder das Projekt
   `app1-betrieb` im Dashboard öffnen; in Klausurwochen am Samstag und bei der
   Kassenprüfung am Sonntag. Was im Abitur gilt (Supabase Pro oder Pause),
   steht in [03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 7.5.
4. **Übergabe-Mappe füllen** (`docs/UEBERGABE.md`, ~1 Stunde): Konten und wo
   die Schlüssel liegen, Kosten je Monat, die Modell-ID mit frühestem
   Abschaltdatum (nicht vor Do 07.10.2027) und dem Weg zum Ändern
   (Supabase-Dashboard → Edge Functions → Secrets), der Wert
   `anthropic-version`, fünf Testeingaben, Schritte bei einer Störung und wie
   ein neuer Build mit dem Apple-Team eines neuen Inhabers entsteht
   ([06](06_SOMMER_UND_ABSCHLUSS.md), Abschnitt 4.3). So kann jemand ohne
   Programmierkenntnisse die App betreiben.

### AP21 – TestFlight mit der Familie (2/4/7 h)

Drei Tester aus der Familie bekommen die App über TestFlight, als externe
Tester per E-Mail-Einladung. Die erste Version braucht dafür eine kurze
Beta-Prüfung durch Apple; lade sie deshalb mindestens drei Tage vor dem
Termin ein (vor dem Schritt prüfen). Als Benutzer in App Store Connect legst
du sie nicht an. Du siehst zu, ohne zu helfen, und schreibst jede Stelle auf,
an der jemand zögert, auch bei Verlauf, Kopieren und Teilen. Die drei
wichtigsten behebst du. Die Tester bewerten die App später nicht im Store
(Hauptplan, Abschnitt 4).

### AP22 – Einreichen und Review-Runden (3/6/15 h)

1. Die Checkliste `docs/checkliste-einreichung.md` mit `/einreichen`
   vollständig durchgehen. Dazu gehört: kein Platzhalter mehr (auch nicht in
   „Antwort melden“), die Verträge zur Auftragsverarbeitung sind abgelegt
   ([03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 5.2, Schritt 11), und
   `docs/review-log.md` ist gelesen.
2. Einreichen mit **„Diese Version manuell veröffentlichen“**, bei jedem
   erneuten Einreichen wieder. Abo-Gruppe und beide Abos hängen an dieser
   Version ([05](05_START_UND_MARKETING.md), Abschnitt 2.3, Schritt 9).
3. Bei einer Ablehnung: Grund ins `docs/review-log.md`, Claude schlägt die
   kleinste Änderung vor, du reichst neu ein. Rechne mit 1–2 Runden; jede
   kostet meist 2–10 Tage, die meisten Prüfungen sind in 48 Stunden fertig.

Was nach der Einreichung kommt (Markenkonten in der Woche der Einreichung,
Posts, Vor-Start-Prüfung, Veröffentlichen), steht in 05, Abschnitte 1 und 5.

---

## 8. Stunden-Messpunkt und Funktions-Stopp

**Stunden-Messpunkt am Di 29.12. nach dem Durchstich (AP1–AP9, geplant
~32 h):**

| deine Stunden für AP1–AP9 | was das heißt | was du tust |
|---|---|---|
| bis ~40 | im Plan | weiter wie geplant. Jede Stunde über 32 schiebt die Einreichung; ab etwa 38 liegt sie in Q4 ([01](01_TAG_FUER_TAG_BIS_FEBRUAR.md), Abschnitt 11) |
| ~40–60 | langsamer, aber im Rahmen des Modells | **App 1 kleiner schneiden:** Onboarding mit 3 Fragen, kein eigenes Design, keine Bewertungsabfrage, Favoriten erst in Version 1.1. Das holt Stunden zurück; die Einreichung liegt trotzdem eher in Q4 |
| über ~60 | fast doppelt so lang wie geplant oder mehr | Einreichung erst nach dem Abitur einplanen. Das ist kein Scheitern: weiter mit 10 h je Woche bis 31.01., in Q4 höchstens 6–7 h, kein Druck. Ist am So 14.03. keine App im Store oder im Review, ruht die App bis nach deiner letzten Prüfung (Ruhezeit, Hauptplan, Abschnitt 4) |

Nie gekürzt werden: geführter Ablauf, Meldeknopf, Einwilligung, die
Pflichtteile der Paywall und die Mindestprüfung.

Schick mir deine Stunden am Messpunkt. Dann rechne ich das Modell mit deinen
echten Zahlen neu.

**Funktions-Stopp: So 24.01.** Ab dann kommt keine neue Funktion mehr dazu,
nur noch Fehlerbehebung, Texte und Einreichung. Was fehlt, kommt in Version
1.1 nach dem Abitur, z. B. Favoriten oder bei einer Themenfamilie weitere
Anlässe.

**Einreichung bis Di 02.02.**, dem zweiten Tag der Halbjahresferien. Danach
beginnt Q4 mit höchstens 6–7 Stunden je Woche: Antworten an das Review und ab
der Einreichung höchstens 3 Posts je Woche ([05](05_START_UND_MARKETING.md),
Abschnitt 6.2). Ist App 1 bis dahin nicht eingereicht, baust du im Rahmen
dieser Stunden ohne Druck weiter (Hauptplan, Abschnitt 12).

---

## 9. Nach App 1: deine eigene Vorlage

Sobald App 1 freigegeben ist, nicht früher (3–4 Stunden):
1. Zuerst die Lehren aus dem Review-Log in die `CLAUDE.md` übernehmen.
2. Aus App 1 die Vorlage machen, im privaten Repository `vorlage` (das leere
   Vorlagen-Projekt vom Sa 28.11. ersetzt du damit): Onboarding als
   Datenliste mit Herkunftsfrage, Paywall-Aufruf, Verlauf und Favoriten,
   Einstellungen mit Rechtstexten, die Server-Funktionen `ki` und `herkunft`
   mit Migrationen, `eas.json`, Checklisten, `docs/UEBERGABE.md` als
   Gliederung, der Ablauf `/einreichen`.
3. Claude einen zweiten Ablauf schreiben lassen, den nur du startest: „neue
   App anlegen“ (Bundle-ID, Store-Eintrag). Jede App bekommt ihre eigenen
   Behälter: Repository, Expo-Projekt, RevenueCat-Projekt, Supabase-Projekt,
   Arbeitsbereich in der Claude-Konsole und Produkt-IDs mit dem Namen der App
   ([03](03_GRUENDUNG_UND_KONTEN.md), Abschnitt 3). Mit zwei aktiven
   Projekten ist der Gratis-Tarif von Supabase voll; was du für App 2 tust,
   entscheidest du bei ihrer Einreichung (03, Abschnitt 3).

App 2 bekommt eine andere Aufgabe, ein anderes Ergebnisformat, andere
Bildschirme und Texte und ein eigenes Aussehen. Reine Varianten lehnt Apple ab
(Richtlinie 4.3(a); [04](04_IDEENWAHL.md), Abschnitt 9, Zeile 7). Hast du für
App 1 eine Themenfamilie gewählt (04, Abschnitt 3), kommt ein weiterer Anlass
derselben Familie als Option in App 1 (Version 1.1), nicht als eigene App.
App 2 bleibt eine eigene App mit eigener Funktion. Mit der Vorlage rechnet das
Modell für App 2 und 3 mit 33/55/110 Stunden ([07](07_HEBEL.md),
Abschnitt 14).
