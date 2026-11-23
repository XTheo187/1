# CLAUDE.md – Regeln für dieses App-Projekt

(Vorlage aus docs/APP_PLAN_ALLEIN_MIT_CLAUDE.md. Als `CLAUDE.md` in das
Hauptverzeichnis des App-Repositorys kopieren und die Teile in eckigen
Klammern ausfüllen.)

## Worum es geht
- App: [Name], Zielgruppe: [wer], Kernfunktion: [Foto oder Eingabe → Ergebnis].
- Anbieter: [dein Name bzw. der des Elternteils], Einzelunternehmen. Ich bin
  Schüler, arbeite in Schulwochen ~10 Stunden je Woche, in den Ferien und im
  Sommer deutlich mehr, in Q4 höchstens 6–7 und im Abitur fast gar nicht.
  Ich **kann nicht programmieren** und lerne gerade, Code zu lesen.
- Zielgruppe ab 18; keine Texte, die sich an Kinder oder Schüler richten.
- Ich arbeite unter Windows ohne Mac, teste auf iPhone und iPad.
- Technik: Expo (React Native, TypeScript, Expo Router), EAS Build und
  `eas submit`, RevenueCat für Abos und Paywall, Supabase-Funktion für den
  KI-Aufruf (Claude Haiku 5.5 über meinen eigenen API-Schlüssel).
- Keine Nutzerkonten, keine Inhalte, die andere Nutzer sehen, nur Wochen- und
  Monatsabo (kein Jahresabo vor Juli 2027).

## Wie du arbeitest
- Ich lerne mit. Arbeite im Lernmodus: erkläre jede Entscheidung, lass mich an
  wichtigen Stellen selbst schreiben (`TODO(human)`) und frag nach, ob ich es
  verstanden habe.
- Kleine Schritte. Vor jeder Änderung: kurzer Plan (welche Dateien, was),
  dann auf mein OK warten.
- Nach jeder Änderung in zwei, drei einfachen Sätzen erklären, was du
  gemacht hast und warum, und sagen, wie ich es auf dem iPhone prüfe.
- Behaupte nie, dass etwas funktioniert oder behoben ist, bevor ich es
  getestet habe. Wenn du dir nicht sicher bist, sag es.
- Wenn derselbe Fehler zweimal auftritt: anhalten und mir den Fehler
  erklären, statt weiter zu raten.
- Für Windows: Befehle für PowerShell angeben; wenn etwas nur auf dem Mac
  geht, sag es und nenn den Weg über EAS.
- Sag mir bei jeder Änderung, ob ich sie in Expo Go prüfen kann oder einen
  neuen Development Build brauche (nur 15 iOS-Builds im Monat gratis).
- Keine neuen Pakete oder Dienste, die Geld kosten oder Daten an Dritte
  schicken, ohne mich zu fragen.
- Lies vor jeder Einreichung `docs/checkliste-einreichung.md` und
  `docs/review-log.md`.

## Was nie passieren darf
- Keine Schlüssel oder Passwörter in der App oder im Repository. Der
  KI-Schlüssel und der geheime RevenueCat-Schlüssel liegen nur als
  Geheimnis in der Supabase-Funktion (`supabase secrets set`); `.env` steht in
  `.gitignore`.
- Du bekommst nie Zugangsdaten für das Projekt im Betrieb; du arbeitest nur
  im Testprojekt.
- Die Server-Funktion prüft bei jedem Aufruf über die REST-API von
  RevenueCat, ob die App-User-ID ein aktives Abo hat; ohne aktives Abo
  kein KI-Aufruf.
- Keine Tabelle ohne Zugriffsregeln (Row Level Security), keine Regel
  `using (true)`; der Security Advisor zeigt null Fehler.
- Fotos werden nach der Analyse nicht gespeichert.
- Vor dem ersten KI-Aufruf fragt die App um Erlaubnis und nennt den
  Anbieter (Apple 5.1.2(i)).
- Die Paywall ist hart (kein Umschalter für eine Testphase), nennt Preis,
  Laufzeit und Verlängerung und hat „Käufe wiederherstellen“ sowie Links zu
  Datenschutz und Nutzungsbedingungen.
- Kein Code, der in sozialen Netzwerken postet, kommentiert oder Nachrichten
  verschickt.
- Keine Kundendaten in dieser Sitzung: keine Support-Mails, keine Fotos von
  Nutzern, keine Daten aus dem Betriebsprojekt, aus RevenueCat oder App Store
  Connect außer Summen. Will ich so etwas einfügen, halte mich auf.
- Keine Gesundheitsversprechen und keine Diagnosen in Texten der App.
- Keine eigenen Messereignisse (z. B. „Paywall gesehen“) ohne Einwilligung
  der Nutzer (§ 25 TDDDG).
- Kein Web-Kauf in App 1.
- Die App läuft auch auf dem iPad sauber (Apple prüft iPhone-Apps dort).
- Impressum in der App erreichbar (Einstellungen).

## Kosten
- Tageslimit für KI-Aufrufe je App-User-ID, gezählt auf dem Server
  (Start: [z. B. 20]).
- Bilder vor dem Senden verkleinern, Antworten kurz halten.
- In der Anthropic-Konsole ist ein Ausgabenlimit als Notbremse gesetzt und
  wird jede Woche an die Nutzerzahl angepasst; bei Fehlern der API (400 bei
  erreichtem Limit, 429 bei zu vielen Anfragen) zeigt die App eine
  freundliche Meldung statt abzustürzen.

## Dateien, die du pflegst
- `docs/review-log.md`: jede Ablehnung durch Apple mit Grund und Lösung.
- `docs/checkliste-einreichung.md`: Prüfliste vor jeder Einreichung.
- `docs/entscheidungen.md`: wichtige Entscheidungen mit einem Satz Begründung.
