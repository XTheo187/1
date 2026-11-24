# Bauplan für App 1 – Arbeitspaket für Arbeitspaket

Gehört zu [`../APP_PLAN_ALLEIN_MIT_CLAUDE.md`](../APP_PLAN_ALLEIN_MIT_CLAUDE.md).
Dort stehen Regeln, Geld und Messpunkte. Hier steht, **was du baust, in
welcher Reihenfolge, wie lange es dauert und woran du erkennst, dass ein
Schritt fertig ist.** Wann du welches Paket machst, steht in
[`01_TAG_FUER_TAG_BIS_FEBRUAR.md`](01_TAG_FUER_TAG_BIS_FEBRUAR.md).

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

App 1 ist absichtlich klein. Jede Stunde, die du vor dem Start sparst,
erhöht die Chance (im Modell bringen 10 Stunden weniger Bauzeit etwa
+0,7 Punkte Gewinnchance). Bezahlte Abkürzungen lohnen dagegen nicht: Eine
gesparte Baustunde ist im Modell nur ~4–6 € wert. Deshalb gilt für App 1:

**Drin**
- **Eine Aufgabe:** Der Nutzer gibt Text ein und bekommt ein Ergebnis in
  einem festen, eigenen Format. Kein allgemeiner Chatbot.
- **Fünf Bildschirme:** Onboarding (3–5 Fragen), Paywall, Eingabe, Ergebnis,
  Einstellungen.
- **Zwei Sprachen:** Deutsch und Englisch, von Anfang an. Die KI antwortet in
  der Sprache des Geräts.
- **Abo:** Wochen- und Monatsabo, harte Paywall nach dem Onboarding, über
  RevenueCat mit der fertigen Paywall aus dem Dashboard.
- **Ein Server-Baustein:** eine Supabase-Funktion, die das Abo prüft, zählt
  und die KI aufruft.
- **Pflichtteile:** Einwilligung vor dem ersten KI-Aufruf, Knopf „Antwort
  melden“, Impressum, Datenschutz, Nutzungsbedingungen, „Käufe
  wiederherstellen“, „Abo verwalten“.

**Nicht drin** (jedes davon kostet Tage oder Review-Runden)
- Kamera, Fotos, Mikrofon, Standort, Push-Mitteilungen
- Nutzerkonten, Anmeldung, Teilen, Profile, Inhalte für andere Nutzer
- Tracking und eigene Messereignisse
- Jahresabo, Web-Kauf, Android
- iPad-Layout (die App läuft dort im Kompatibilitätsmodus und wird dort
  getestet, bekommt aber kein eigenes Layout)
- Themen aus Gesundheit, Abnehmen, Finanzen, Dating; Zielgruppe Schüler

**Eine Foto-App** (Foto → KI-Ergebnis) ist erst App 2 oder 3, wenn die
Vorlage steht. Sie braucht Kamera-Berechtigung, Bildverkleinerung und
höhere KI-Kosten und ist beim Review empfindlicher.

---

## 2. Wie die Teile zusammenhängen

```
 iPhone-App (Expo)
   │  1. fragt RevenueCat: Hat diese App-User-ID ein aktives Abo?  → Paywall oder Eingabe
   │  2. schickt Text + App-User-ID + Sprache an deine Server-Funktion
   ▼
 Supabase-Funktion „ki“  (dein einziger Server-Code, ~100 Zeilen)
   │  a. prüft bei RevenueCat (geheimer Schlüssel), ob das Abo wirklich aktiv ist
   │  b. zählt den Aufruf in der Tabelle „nutzung“ (Tageslimit je App-User-ID)
   │  c. ruft die Claude API auf (geheimer Schlüssel, Antwortlänge gedeckelt)
   ▼
 Antwort zurück an die App  →  Ergebnis-Bildschirm
```

**Wo welcher Schlüssel liegt**

| Schlüssel | wo | darf in die App? |
|---|---|---|
| RevenueCat, öffentlicher iOS-Schlüssel | App (über `eas.json`/Umgebung) | ja |
| RevenueCat, Test-Store-Schlüssel (aus dem Dashboard kopieren) | nur im Entwicklungs-Build | ja, aber nie im Store- oder TestFlight-Build: der stürzt damit ab |
| Supabase, Publishable-Schlüssel | App | ja |
| RevenueCat, geheimer Schlüssel | Supabase-Geheimnis | **nie** |
| Claude API-Schlüssel | Supabase-Geheimnis | **nie** |
| Supabase, Secret-Schlüssel | nur in der Funktion | **nie** |

**Zwei Projekte bei Supabase:** `app1-test` und `app1-betrieb`, beide in
einer EU-Region. Claude Code bekommt nur Zugang zum Testprojekt. Den
Betrieb richtest du selbst im Dashboard ein, mit Claudes Anleitung.

---

## 3. So arbeitest du in jeder Sitzung

1. **Ein Arbeitspaket, ein Ergebnis.** Du öffnest PowerShell im Projektordner,
   startest `claude` und nennst das Paket.
2. **Vor größeren Paketen eine Spezifikation:** „Interviewe mich, bis du die
   Spezifikation schreiben kannst, und schreib sie nach `SPEC.md`.“ Danach
   `/clear` und eine neue Sitzung, die nur aus `SPEC.md` baut.
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
8. **Commit, Push, Stunden eintragen.**

**Wenn du festhängst:** Nach etwa 90 Minuten ohne Fortschritt stellst du die
Frage im Expo-Forum oder in der RevenueCat-Community, ohne Schlüssel und ohne
persönliche Angaben. Ein Spitzname ist dort in Ordnung.

**Nie:** einen Schlüssel in die App oder ins Repository; „ist behoben“
glauben, ohne es gesehen zu haben; neue Funktionen nach dem Funktions-Stopp.

---

## 4. Die Arbeitspakete im Überblick

Stunden sind deine eigenen Stunden: von/typisch/bis. Die typischen Werte
ergeben zusammen ~100 Stunden. Das ist der Fall, in dem jedes Paket ohne
längere Fehlersuche durchläuft. Das Modell rechnet vorsichtiger, mit
⟨BAU_VON⟩/⟨BAU_TYP⟩/⟨BAU_BIS⟩ Stunden, weil Fehlersuche und Lernen am
eigenen Code dazukommen. Keine Studie misst das für Anfänger. Deine echten
Stunden trägst du ein und vergleichst sie am Stunden-Messpunkt (Abschnitt 8).

| Nr. | Paket | Stunden | fertig, wenn … |
|---|---|---|---|
| **A** | **Fundament und Durchstich** | **~32** | |
| AP1 | Projekt, Plugins, `CLAUDE.md`, Prüfbefehle | 2/3/5 | das leere Projekt in Expo Go läuft und die drei Prüfbefehle ohne Fehler durchlaufen |
| AP2 | Zwei Sprachen und fünf leere Bildschirme | 3/4/7 | du auf dem iPhone durch alle fünf Bildschirme tippen kannst und sie beim Umstellen der Gerätesprache die Sprache wechseln |
| AP3 | Beschreibung von App 1 (`SPEC.md`) | 1/2/3 | eine Seite steht: Zielgruppe, Aufgabe, Ergebnisformat, Onboarding-Fragen, Preise |
| AP4 | Supabase: zwei Projekte, Funktion mit Beispielantwort, Zähltabelle | 3/5/9 | die App eine Beispielantwort vom Server zeigt und in der Tabelle ein Zähler steht |
| AP5 | Claude API: Schlüssel, Limit, echte Antwort | 1/2/4 | die App eine echte KI-Antwort zeigt und in der Konsole ein Limit von 50 $ steht |
| AP6 | RevenueCat: Projekt, Test Store, Paywall, alle nativen Pakete | 3/5/9 | Projekt, Produkte und Paywall im Dashboard stehen und alle nativen Pakete installiert sind |
| AP7 | Apple-Konto, Geräte, Entwicklungs-Build | 2/3/8 | der Entwicklungs-Build auf iPhone und iPad startet und die echte Paywall zeigt |
| AP8 | **Durchstich:** Kauf → Abo-Prüfung → KI-Antwort | 2/4/8 | ein Testkauf die Eingabe freischaltet und ein Aufruf ohne Abo vom Server abgelehnt wird |
| AP9 | Store-Build und TestFlight | 2/4/9 | die App über TestFlight auf deinem iPhone installiert ist und ohne Produkte nicht abstürzt |
| **B** | **Die App** | **~42** | |
| AP10 | Kernfunktion und Prompt | 6/10/18 | 20 Testeingaben in beiden Sprachen ein brauchbares Ergebnis im festen Format liefern |
| AP11 | Onboarding | 3/5/8 | die Antworten das Ergebnis sichtbar beeinflussen und beim zweiten Start nicht neu gefragt wird |
| AP12 | Paywall-Feinschliff | 2/4/7 | Preis, Laufzeit, Kündigungshinweis, Links und „Käufe wiederherstellen“ stimmen, in beiden Sprachen |
| AP13 | Einwilligung, „Antwort melden“, Fehlerfälle | 4/6/10 | ohne Netz, bei erreichtem Limit und bei einem KI-Fehler eine verständliche Meldung kommt |
| AP14 | Einstellungen und Rechtstexte | 2/3/5 | Impressum, Datenschutz, Nutzungsbedingungen und „Abo verwalten“ erreichbar sind |
| AP15 | Tageslimit und Kostenbremse | 2/3/5 | der 21. Aufruf am selben Tag freundlich abgelehnt wird |
| AP16 | Aussehen: Farben, Icon, Startbild, Name | 3/5/9 | Icon und Name auf dem Home-Bildschirm stimmen und die App einheitlich aussieht |
| AP17 | iPad, Gerätetests, Fehler | 3/6/14 | die Prüfliste auf iPhone und iPad ohne Fehler durchläuft |
| **C** | **Einreichung** | **~25** | |
| AP18 | Website mit Impressum, Datenschutz, Nutzungsbedingungen | 2/4/7 | die drei Seiten online sind und die Links in der App dorthin führen |
| AP19 | App Store Connect: Eintrag, Abos, Preise, Angaben, Screenshots | 5/8/14 | alle Pflichtfelder grün sind, in Deutsch und Englisch |
| AP20 | Sicherheits-Mindestprüfung | 2/3/5 | alle sieben Punkte bestanden sind und du jedes Ergebnis gesehen hast |
| AP21 | TestFlight mit der Familie | 2/4/7 | drei Tester die App ohne deine Hilfe bedient haben und ihre Fehler behoben sind |
| AP22 | Einreichen und Review-Runden | 3/6/15 | die App freigegeben ist und auf „manuell veröffentlichen“ wartet |

Die Gründung (Gewerbe, Bank- und Steuerdaten bei Apple) zählt nicht zu
diesen Paketen. Sie steht in
[`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md) und kostet ~4–5 Stunden.

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
   eintragen.
4. Das Expo-Plugin für Claude Code einrichten, wie es die Expo-Doku unter
   „Build with AI“ beschreibt. Das Gerüst legt dafür die Datei
   `.claude/settings.json` an. Fehlt sie, hilft
   `claude plugin install expo@claude-plugins-official --scope project`.
   Danach prüfen: „Lies `package.json` und nenne mir die Expo-SDK-Version.“
5. In Claude Code mit `/permissions` festlegen, dass Claude bei allem mit
   Außenwirkung nachfragt (Veröffentlichen, Einreichen, Löschen, Bezahlen).
6. `docs/checkliste-einreichung.md`, `docs/review-log.md` und
   `docs/entscheidungen.md` anlegen. Claude einen Ablauf `/einreichen`
   schreiben lassen, der die Checkliste Schritt für Schritt durchgeht und den
   nur du startest.

**Prompt:** „Richte dieses neue Expo-Projekt nach der CLAUDE.md ein. Erkläre
mir danach jede Datei im Hauptordner in einem Satz.“

**Stolperstelle:** Verbindet Expo Go nicht, starte mit `npx expo start --tunnel`.

### AP2 – Zwei Sprachen und fünf leere Bildschirme (3/4/7 h)

1. Zweisprachigkeit einrichten (`npx expo install expo-localization`, dazu
   `i18next` und `react-i18next`): alle sichtbaren Texte kommen aus `de.json`
   und `en.json`, kein Text steht fest im Code.
2. Fünf Bildschirme als leere Hüllen mit Navigation: Onboarding, Paywall,
   Eingabe, Ergebnis, Einstellungen.
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

Erst nach dem Ideen-Tor (So 20.12.). Die Pakete AP1, AP2, AP4–AP7 hängen
nicht von der Idee ab und laufen vorher.

**Prompt:** „Interviewe mich zu meiner App-Idee, bis du eine einseitige
Spezifikation schreiben kannst: Zielgruppe (Erwachsene), die eine Aufgabe,
das Ergebnisformat, 3–5 Onboarding-Fragen, Wochen- und Monatspreis,
Store-Titel und Untertitel in Deutsch und Englisch. Schreib sie nach SPEC.md.“

### AP4 – Supabase: zwei Projekte, Funktion, Zähltabelle (3/5/9 h)

1. Supabase-Konto mit einer E-Mail nur für das Projekt anlegen. Zwei Projekte
   anlegen: `app1-test` und `app1-betrieb`, Region EU, Free-Plan.
2. Im Testprojekt:
   - Tabelle `nutzung` (App-User-ID, Tag, Zähler), Zugriffsregeln (RLS) an,
     kein Zugriff für die App selbst;
   - Funktion `ki`, die zunächst nur eine feste Beispielantwort zurückgibt und
     den Zähler erhöht.
3. Die App ruft die Funktion auf und zeigt die Beispielantwort auf dem
   Ergebnis-Bildschirm.

**Prompt:** „Lege im Supabase-Testprojekt eine Edge Function ‚ki‘ an, die
eine feste Beispielantwort zurückgibt, und eine Tabelle ‚nutzung‘ mit RLS,
auf die nur die Funktion schreiben darf. Zeig mir, wie ich die Funktion ohne
Docker unter Windows veröffentliche. Erkläre mir danach, was RLS ist und
warum die App nicht selbst in die Tabelle schreiben darf.“

**Stolperstellen:**
- Braucht ein Befehl Docker, lass dir den Weg über die Supabase-API oder den
  Editor im Dashboard zeigen.
- Verbindest du Claude Code über den Supabase-MCP, dann nur mit dem
  Testprojekt: An die Adresse gehört die Kennung des Testprojekts
  (`https://mcp.supabase.com/mcp?project_ref=…`). Das Betriebsprojekt hängst
  du nie an den Agenten.
- Lass das Testprojekt in einer eigenen Free-Organisation. Supabase Pro kostet
  25 $ je Organisation, und ein zweites Projekt darin kostet extra.

### AP5 – Claude API: Schlüssel, Limit, echte Antwort (1/2/4 h)

1. In der Anthropic-Konsole ein Konto für die App anlegen, ein paar Dollar
   Guthaben aufladen, Ausgabenlimit 50 $ im Monat setzen, automatisches
   Aufladen aus.
2. Den Schlüssel als Geheimnis im Testprojekt hinterlegen:
   `supabase secrets set ANTHROPIC_API_KEY=…`. Die Datei `.env` steht in
   `.gitignore`.
3. Die Funktion ruft Claude Haiku (`claude-haiku-5-5`) über das offizielle
   Anthropic-SDK auf, mit gedeckelter Antwortlänge, und antwortet in der
   mitgeschickten Sprache.
4. Die Antwort kommt als festes Format (strukturierte Ausgabe), damit die App
   geprüfte Felder zeigt statt frei gelesenem Text. Lass Claude vorher prüfen,
   ob das Modell das unterstützt.

**Prüfung:** `git grep -i "sk-ant"` findet nichts.

**Stolperstelle:** Lass Claude in der aktuellen API-Doku nachsehen, ob beim
gewählten Modell das „Denken“ standardmäßig an ist und auf die Antwortlänge
zählt. Dann schneidet ein knapper Deckel Antworten ab. Die App behandelt
abgeschnittene und abgelehnte Antworten als eigene Fehlerfälle (AP13).

### AP6 – RevenueCat: Projekt, Test Store, Paywall (3/5/9 h)

1. RevenueCat-Konto mit dem Projekt-Postfach anlegen (kostenlos).
2. Projekt anlegen: ein Entitlement `pro`, ein Offering `default` mit den
   Paketen Woche und Monat. Zunächst im **Test Store**, der ohne App Store
   Connect auskommt.
3. Im Dashboard eine Paywall aus einer Vorlage bauen: voller Preis je
   Zeitraum, „jederzeit kündbar“, Links zu Nutzungsbedingungen und
   Datenschutz, Knopf „Käufe wiederherstellen“. Die Texte der Paywall pflegst
   du je Sprache im Dashboard, nicht in `de.json`/`en.json`.
4. **Alle nativen Pakete jetzt installieren, vor dem ersten Build:**
   `npx expo install expo-dev-client`, dann
   `npx expo install react-native-purchases react-native-purchases-ui`, dazu
   `expo-updates` (Fehler später ohne neuen Build beheben) und
   `expo-store-review` (Bewertungsabfrage). Danach reicht ein einziger
   Entwicklungs-Build; jeder weitere zählt auf die 15 im Monat.
5. Die App ruft die Paywall nach dem Onboarding auf.

**Prompt:** „Binde RevenueCat ein: Entitlement pro, Offering default mit
Woche und Monat. Zeig die Paywall aus dem Dashboard nach dem Onboarding als
harte Paywall. Der Test-Store-Schlüssel darf nur im Entwicklungs-Build
stecken, der iOS-Schlüssel in Preview und Production, gesteuert über
eas.json, nie fest im Code.“

**Stolperstelle:** In Expo Go läuft RevenueCat nur als Attrappe. Die echte
Paywall und Testkäufe siehst du erst im Entwicklungs-Build (AP7).

### AP7 – Apple-Konto, Geräte, Entwicklungs-Build (2/3/8 h)

Voraussetzung: Es steht fest, wer im App Store steht (Hauptplan,
Abschnitt 3), und das Apple-Konto ist aktiv. Kommt innerhalb von 24 Stunden
nach dem Kauf keine Bestätigung, wendest du dich an Apple.

1. `npm install -g eas-cli`, `eas login`, `eas build:configure`.
2. iPhone und iPad registrieren: `eas device:create`. Auf beiden Geräten den
   Entwicklermodus einschalten (Einstellungen → Datenschutz & Sicherheit).
3. `eas build --profile development --platform ios`. EAS legt die
   Zertifikate für dich an. Den Build per QR-Code installieren.

**Probe vorab:** Sobald das Apple-Konto aktiv ist, bringst du die
Tutorial-App „StickerSmash“ als Entwicklungs-Build aufs iPhone. So liegen
Signierung und Geräteregistrierung schon in den Schulwochen hinter dir, und
am 23.12. läuft die Kette.

**Stolperstellen:**
- Bei einem neuen Konto kann es 24–72 Stunden dauern, bis ein Gerät
  angenommen ist. Der erste Build scheitert dann; einfach später wiederholen.
- Im Free-Plan gibt es 15 iOS-Builds im Monat. Für Änderungen an der
  Oberfläche brauchst du keinen neuen Build, nur für neue native Pakete.

### AP8 – Durchstich: Kauf → Abo-Prüfung → KI-Antwort (2/4/8 h)

Das ist der wichtigste Schritt der ganzen Phase.

1. Im Entwicklungs-Build einen Testkauf machen (Test Store).
2. Die Funktion prüft bei jedem Aufruf über die REST-API von RevenueCat, ob
   die mitgeschickte App-User-ID ein aktives Abo hat. Der geheime
   RevenueCat-Schlüssel liegt als Supabase-Geheimnis.
   - **Als Erstes ausprobieren:** Meldet die REST-API einen Kauf aus dem Test
     Store als aktives Abo? Die Doku sagt das nicht ausdrücklich. Wenn nicht,
     lässt sich die Server-Prüfung erst mit Apples Sandbox testen, also nach
     der Gründung und dem Vertrag mit Apple. Dann baust du die Prüfung jetzt
     und testest sie in KW 01–02.
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

1. Eingabe-Bildschirm und Ergebnis-Bildschirm nach `SPEC.md`.
2. Den Prompt in der Server-Funktion entwickeln: Aufgabe, festes
   Ergebnisformat, Sprache, Grenzen (keine Diagnosen, keine Rechts- oder
   Finanzberatung, höfliche Ablehnung bei Missbrauch).
3. **20 Testeingaben** in einer Datei `docs/testfaelle.md` sammeln: je 8
   normale in Deutsch und Englisch, dazu 4 schwierige (leer, sehr lang,
   Unsinn, beleidigend). Nach jeder Prompt-Änderung alle 20 durchlaufen
   lassen und das Ergebnis lesen.

**Prompt:** „Lies SPEC.md. Baue Eingabe und Ergebnis. Schreib den
System-Prompt in die Edge Function, mit festem Ergebnisformat als JSON. Lege
docs/testfaelle.md mit 20 Testeingaben an und ein kleines Skript, das alle 20
gegen das Testprojekt schickt und die Antworten in eine Datei schreibt.“

### AP11 – Onboarding (3/5/8 h)

3–5 Fragen, die das Ergebnis wirklich verändern. Die Antworten liegen nur auf
dem Gerät und werden mit jeder Anfrage mitgeschickt. Kein Konto, kein
Speichern auf dem Server.

### AP12 – Paywall-Feinschliff (2/4/7 h)

- Der Preis je Zeitraum steht deutlich da, deutlicher als alles andere.
- Kein Schalter zum Ein- und Ausschalten einer Testphase.
- „Käufe wiederherstellen“ funktioniert nach Löschen und Neuinstallieren.
- In den Einstellungen führt „Abo verwalten“ zur Abo-Verwaltung von Apple.
- Alle Texte in beiden Sprachen.

Preise und Abo-Längen legst du nach
[`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md) fest.

### AP13 – Einwilligung, „Antwort melden“, Fehlerfälle (4/6/10 h)

1. **Einwilligung vor dem ersten KI-Aufruf:** ein eigener Dialog, der sagt,
   dass die Eingabe an Anthropic (Claude) geschickt wird, mit „Zustimmen“ und
   „Ablehnen“. Ohne Zustimmung kein Aufruf.
2. **„Antwort melden“:** ein Knopf am Ergebnis, der eine Mail an deine
   Support-Adresse vorbereitet.
3. **Fehlerfälle:** kein Netz, Limit erreicht, KI lehnt ab, Server-Fehler,
   Abo abgelaufen. Jeder Fall bekommt eine verständliche Meldung in beiden
   Sprachen und einen Weg zurück.

### AP14 – Einstellungen und Rechtstexte (2/3/5 h)

Einstellungen mit: Impressum, Datenschutzerklärung, Nutzungsbedingungen (ab
18), Abo verwalten, Käufe wiederherstellen, Support-Mail, Version. Die Texte
liegen auf deiner Website (AP18); die App öffnet sie im Browser.

### AP15 – Tageslimit und Kostenbremse (2/3/5 h)

- Die Funktion lehnt ab einem Tageslimit je App-User-ID ab (Start: 20).
- Die Antwortlänge ist gedeckelt.
- Im Protokoll der Funktion stehen keine Eingabetexte, nur Zeit, Länge und
  Fehlercode.

### AP16 – Aussehen: Farben, Icon, Startbild, Name (3/5/9 h)

- Ein Markenname aus einem Wort, leicht zu schreiben. Vorher im deutschen und
  im US-App-Store suchen, ob es ihn schon gibt.
- Zwei Farben, eine Schrift, große Schaltflächen. Icon und Startbild baust du
  in Canva; Claude liefert Vorschläge und die nötigen Größen.

### AP17 – iPad, Gerätetests, Fehler (3/6/14 h)

Eine Prüfliste `docs/geraetetest.md` mit ~25 Schritten: jeder Bildschirm,
jeder Fehlerfall, beide Sprachen, Hell- und Dunkelmodus, große Schrift, iPhone
und iPad. Du gehst sie selbst durch, nicht Claude.

---

## 7. Phase C – Einreichung

### AP18 – Website (2/4/7 h)

Eine einfache, statische Website auf deiner Domain mit vier Seiten: Start,
Impressum, Datenschutzerklärung, Nutzungsbedingungen. Dazu die
Support-Adresse. Inhalt und Anbieter stehen in
[`03_GRUENDUNG_UND_KONTEN.md`](03_GRUENDUNG_UND_KONTEN.md). Die Website geht
erst online, wenn feststeht, wer im Impressum steht.

### AP19 – App Store Connect (5/8/14 h)

1. App-Eintrag mit Bundle-ID, Name, Untertitel, Kategorie, Altersfreigabe.
2. Abo-Gruppe mit Wochen- und Monatsabo, Preise je Land bewusst gesetzt.
3. In RevenueCat den App Store verbinden und die Produkte den Paketen
   zuordnen. Der Store-Build nutzt jetzt den iOS-Schlüssel, nicht mehr den
   Test-Store-Schlüssel.
4. Datenschutzangaben („App-Datenschutz“), passend zu dem, was die App
   wirklich tut.
5. Screenshots vom eigenen iPhone, in den verlangten Größen.
6. Texte in Deutsch und Englisch; Hinweise für das Review: was die App tut,
   dass keine Anmeldung nötig ist, wie man die Paywall testet.
7. EU-Händlerangaben und, falls noch offen, Paid Apps Agreement, Bank- und
   Steuerdaten.

### AP20 – Sicherheits-Mindestprüfung (2/3/5 h)

Die sieben Punkte aus dem Hauptplan, Abschnitt 7. Claude führt sie aus und
zeigt Befehl und Ergebnis; du siehst dir jedes Ergebnis selbst an. Zuletzt
richtest du das Betriebsprojekt ein: dieselbe Funktion und Tabelle, eigene
Schlüssel, und der Store-Build zeigt auf den Betrieb.

### AP21 – TestFlight mit der Familie (2/4/7 h)

Drei Tester aus der Familie bekommen die App über TestFlight. Du siehst zu,
ohne zu helfen, und schreibst jede Stelle auf, an der jemand zögert. Die drei
wichtigsten behebst du.

### AP22 – Einreichen und Review-Runden (3/6/15 h)

1. Die Checkliste `docs/checkliste-einreichung.md` vollständig durchgehen.
2. Einreichen mit **„Diese Version manuell veröffentlichen“**.
3. Bei einer Ablehnung: Grund ins `docs/review-log.md`, Claude schlägt die
   kleinste Änderung vor, du reichst neu ein. Rechne mit 1–2 Runden; die
   meisten Prüfungen sind in 48 Stunden fertig.
4. Während die App wartet, übersetzt Claude den Store-Eintrag in weitere
   Sprachen (siehe [`05_START_UND_MARKETING.md`](05_START_UND_MARKETING.md)).

---

## 8. Stunden-Messpunkt und Funktions-Stopp

**Stunden-Messpunkt nach dem Durchstich (AP1–AP9, geplant ~32 h):**

| deine Stunden für AP1–AP9 | was das heißt | was du tust |
|---|---|---|
| bis ~40 | im Plan | weiter wie geplant, Einreichung bis Di 02.02. ist möglich |
| ~40–65 | langsamer, aber im Rahmen des Modells | **Umfang kürzen statt Termin schieben:** Onboarding mit 3 Fragen, kein eigenes Design, keine Bewertungsabfrage. Einreichung eher im Februar |
| über ~65 | mehr als doppelt so lang wie geplant | App 1 wird wahrscheinlich erst nach dem Abitur fertig. Das ist kein Scheitern: weiter mit 10 h je Woche bis 31.01., in Q4 nur 6–7 h, kein Druck |

Schick mir deine Stunden am Messpunkt. Dann rechne ich das Modell mit deinen
echten Zahlen neu.

**Funktions-Stopp: So 24.01.** Ab dann kommt keine neue Funktion mehr dazu,
nur noch Fehlerbehebung, Texte und Einreichung. Was fehlt, kommt in Version
1.1 nach dem Abitur.

**Einreichung bis Di 02.02.**, dem zweiten Tag der Halbjahresferien. Danach
beginnt Q4 mit höchstens 6–7 Stunden je Woche; dort passen nur noch
Review-Antworten hinein.

---

## 9. Nach App 1: deine eigene Vorlage

Sobald App 1 freigegeben ist (3–4 Stunden):
1. Zuerst die Lehren aus dem Review-Log in die `CLAUDE.md` übernehmen.
2. Aus App 1 ein privates Repository `vorlage` machen: Onboarding als
   Datenliste, Paywall-Aufruf, Einstellungen mit Rechtstexten,
   Server-Funktion, `eas.json`, Checklisten, der Ablauf `/einreichen`.
3. Claude einen zweiten Ablauf schreiben lassen, den nur du startest: „neue
   App anlegen“ (Bundle-ID, RevenueCat-Projekt, Supabase-Funktion,
   Store-Eintrag).

App 2 bekommt eine andere Aufgabe, ein anderes Ergebnisformat und ein eigenes
Aussehen. Reine Varianten lehnt Apple ab. Mit der Vorlage rechnet das Modell
für App 2 und 3 mit ⟨NEXT_VON⟩/⟨NEXT_TYP⟩/⟨NEXT_BIS⟩ Stunden.
