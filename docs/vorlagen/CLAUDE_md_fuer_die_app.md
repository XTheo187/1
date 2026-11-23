# CLAUDE.md – Regeln für dieses App-Projekt

(Vorlage aus docs/APP_PLAN_ALLEIN_MIT_CLAUDE.md. Als `CLAUDE.md` in das
Hauptverzeichnis des App-Repositorys kopieren und die Teile in eckigen
Klammern ausfüllen.)

## Worum es geht
- App: [Name], Zielgruppe: [wer], Kernfunktion: [Foto oder Eingabe → Ergebnis].
- Betreiberin: [Name der UG] (haftungsbeschränkt). Ich bin Schülerin, arbeite
  ~1 Stunde am Tag und verstehe TypeScript erst teilweise.
- Technik: Expo (React Native, TypeScript, Expo Router), EAS Build,
  RevenueCat für Abos und Paywall, Supabase-Funktion für den KI-Aufruf
  (Claude Haiku 5.5 über die API der UG).

## Wie du arbeitest
- Kleine Schritte. Vor jeder Änderung: kurzer Plan (welche Dateien, was),
  dann auf mein OK warten.
- Nach jeder Änderung in zwei, drei einfachen Sätzen erklären, was du
  gemacht hast und warum, und sagen, wie ich es auf dem iPhone prüfe.
- Behaupte nie, dass etwas funktioniert oder behoben ist, bevor ich es
  getestet habe. Wenn du dir nicht sicher bist, sag es.
- Wenn derselbe Fehler zweimal auftritt: anhalten und mir den Fehler
  erklären, statt weiter zu raten.
- Keine neuen Pakete oder Dienste, die Geld kosten oder Daten an Dritte
  schicken, ohne mich zu fragen.
- Lies vor jeder Einreichung `docs/checkliste-einreichung.md` und
  `docs/review-log.md`.

## Was nie passieren darf
- Keine Schlüssel oder Passwörter in der App oder im Repository. Der
  KI-Schlüssel und der geheime RevenueCat-Schlüssel liegen nur als
  Geheimnis in der Supabase-Funktion.
- Die Server-Funktion prüft bei jedem Aufruf über die REST-API von
  RevenueCat, ob die App-User-ID ein aktives Abo hat; ohne aktives Abo
  kein KI-Aufruf.
- Keine Tabelle ohne Zugriffsregeln (Row Level Security).
- Fotos werden nach der Analyse nicht gespeichert.
- Vor dem ersten KI-Aufruf fragt die App um Erlaubnis und nennt den
  Anbieter (Apple 5.1.2(i)).
- Die Paywall ist hart (kein Umschalter für eine Testphase), nennt Preis,
  Laufzeit und Verlängerung und hat „Käufe wiederherstellen“ sowie Links zu
  Datenschutz und Nutzungsbedingungen.
- Kein Code, der in sozialen Netzwerken postet, kommentiert oder Nachrichten
  verschickt.
- Keine Gesundheitsversprechen und keine Diagnosen in Texten der App.
- Keine eigenen Messereignisse (z. B. „Paywall gesehen“) ohne Einwilligung
  der Nutzer (§ 25 TDDDG).
- Knopf oder Link zum Web-Kauf nur im US-Storefront (Storefront abfragen,
  nicht Sprache oder IP).

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
