# CLAUDE.md – Regeln für dieses App-Projekt

(Vorlage aus docs/APP_PLAN_ALLEIN_MIT_CLAUDE.md. Als `CLAUDE.md` in das
Hauptverzeichnis des App-Repositorys kopieren und die Teile in eckigen
Klammern ausfüllen.)

## Worum es geht
- App: [Name], Zielgruppe: [wer], Kernfunktion: [geführter Ablauf mit 3–6 Fragen →
  strukturiertes Text-Ergebnis]. Reine Text-App: keine Kamera, keine Fotos, kein
  Mikrofon, kein Standort, keine Push-Mitteilungen, kein Tracking.
- Beschreibung der App in `SPEC.md`; was nicht drinsteht, wird nicht gebaut.
- Anbieter: [dein Name bzw. der des Elternteils], Einzelunternehmen. Ich bin
  Schüler, arbeite in Schulwochen ~10 Stunden je Woche, in den Ferien und im
  Sommer deutlich mehr, in Q4 höchstens 6–7 und im Abitur fast gar nicht.
  Ich **kann nicht programmieren** und lerne gerade, Code zu lesen.
- Zielgruppe ab 18; keine Texte, die sich an Kinder oder Schüler richten.
- Ich arbeite unter Windows ohne Mac, teste auf iPhone und iPad.
- Technik: Expo (React Native, TypeScript, Expo Router), EAS Build und
  `eas submit`, RevenueCat für Abos und Paywall, Supabase-Funktion für den
  KI-Aufruf (Claude API mit `claude-haiku-5-5` über meinen eigenen
  API-Schlüssel), Supabase im Gratis-Tarif.
- Zwei Sprachen von Anfang an: alle Texte in zwei Sprachdateien (Deutsch und
  Englisch), deutsche Geräte sehen Deutsch, alle anderen Englisch.
- Keine Nutzerkonten, keine Inhalte, die andere Nutzer sehen. Verlauf und
  Favoriten nur auf dem Gerät; Kopieren und Teilen über das Teilen-Menü.
- Nur Wochenabo (6,99 €, vorausgewählt) und Monatsabo (14,99 €). Keine
  Testphase, kein Jahresabo, kein „lebenslang“. Apps, die nach dem 04.07.2027
  erscheinen, nur mit Wochenabo.

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
- Eingaben werden auf dem Server nicht gespeichert; der Verlauf liegt nur auf
  dem Gerät.
- Nichts Wichtiges im Schlüsselbund (z. B. `expo-secure-store`) ablegen: Nach
  einer Übertragung der App an ein anderes Apple-Konto funktioniert er nur bis
  zum nächsten Update.
- Vor dem ersten KI-Aufruf fragt die App um Erlaubnis und nennt den
  Anbieter (Apple 5.1.2(i)).
- Die Paywall ist hart und hat keine Testphase und keinen Umschalter. Sie nennt
  Preis, Laufzeit, Verlängerung und den Weg zur Kündigung und hat „Käufe
  wiederherstellen“ sowie Links zu Nutzungsbedingungen, Datenschutz und
  Impressum, alle ohne Abo erreichbar. Keine erfundene Dringlichkeit, kein
  Countdown, kein Tagespreis.
- Ein Knopf „Antwort melden“ öffnet eine E-Mail an die Support-Adresse
  (Richtlinie 1.2); die Kontaktadresse steht in der App.
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
- Tagesgrenze für KI-Aufrufe je App-User-ID, gezählt auf dem Server in der
  Tabelle „nutzung“ (Start: 30 Antworten je Abonnent und Tag). Jede Anfrage
  schreibt dort eine Zeile; das zählt auch als Aktivität, damit das
  Gratis-Projekt nicht pausiert.
- Antworten kurz halten: `max_tokens` 700–900, die Länge über den Prompt
  steuern; die Abbruchgründe `max_tokens` und `refusal` sind Fehlerfälle mit
  verständlicher Meldung.
- Die Anfrage an die API enthält nur `model`, `max_tokens`, `system` und
  `messages`. Die Modell-ID steht als Geheimnis in der Supabase-Funktion, damit
  sie sich ohne App-Update tauschen lässt.
- In der Anthropic-Konsole: vor dem Start nur 5–10 $ Guthaben ohne
  automatisches Nachladen; ab dem Start Nachladen an mit einem Monatslimit,
  das jede Woche an die Nutzerzahl angepasst wird. Bei Fehlern der API zeigt
  die App eine freundliche Meldung statt abzustürzen. Die Server-Funktion
  unterscheidet nach dem Fehlertyp der API, nicht nur nach der Nummer:
  Guthaben aufgebraucht oder Monatsgrenze erreicht (je nach Fall 400, 402 oder
  429 ohne `retry-after`, z. B. `enforced_spend_limit_reached`) und zu viele
  Anfragen (429 mit `retry-after`) bekommen je eine eigene Meldung (vor dem
  Bau in der API-Doku prüfen).
- Kein bezahlter Dienst (Supabase Pro, EAS-Abo, Max) ohne meine ausdrückliche
  Entscheidung.

## Dateien, die du pflegst
- `SPEC.md`: die Beschreibung der App (eine Seite).
- `docs/review-log.md`: jede Ablehnung durch Apple mit Grund und Lösung.
- `docs/UEBERGABE.md`: Konten, wo die Schlüssel liegen, Kosten je Monat,
  Modell-ID und wie man sie ändert, fünf Testeingaben, Schritte bei einer
  Störung – so, dass jemand ohne Programmierkenntnisse die App betreiben kann.
- Das Tabellen-Schema als Migration im Repository (im Gratis-Tarif gibt es
  keine Backups).
- `docs/checkliste-einreichung.md`: Prüfliste vor jeder Einreichung.
- `docs/entscheidungen.md`: wichtige Entscheidungen mit einem Satz Begründung.
