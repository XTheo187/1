# Checkliste vor jeder Einreichung

(Vorlage aus docs/APP_PLAN_ALLEIN_MIT_CLAUDE.md, Abschnitt 15 C und 7. Als
`docs/checkliste-einreichung.md` ins App-Repository kopieren.)

- [ ] Kernfunktion auf dem echten iPhone **und iPad** geprüft, auch ohne Netz (Meldung statt Absturz)
- [ ] Einwilligung vor dem ersten KI-Aufruf: Anbieter und Daten genannt (5.1.2(i))
- [ ] Harte Paywall ohne Umschalter und in App 1 ohne Testphase; Preis, Laufzeit, Verlängerung und Kündigung klar (3.1.2); Wochenabo vorausgewählt; keine erfundene Dringlichkeit
- [ ] „Käufe wiederherstellen“ vorhanden (3.1.1)
- [ ] Auf der Paywall vier Links, alle ohne Abo erreichbar: Nutzungsbedingungen, Datenschutz, Impressum, „Käufe wiederherstellen“; Datenschutz und Nutzungsbedingungen auch in App Store Connect (5.1.1)
- [ ] Abo-Gruppe und alle Abos angelegt und zusammen mit dieser App-Version eingereicht
- [ ] Kein Hinweis auf Käufe außerhalb der App
- [ ] Nur Wochenabo (6,99 €) und Monatsabo (14,99 €); kein Jahresabo, solange du Inhaber bist (ein Nachfolger entscheidet nach der Übertragung selbst); Apps, die nach dem 04.07. erscheinen, nur mit Wochenabo
- [ ] Länderpreise (Österreich, Schweiz, USA, Großbritannien) gesetzt und gegen die Erlös-Spalte in App Store Connect geprüft
- [ ] Abos haben Anzeigename und Beschreibung auf Deutsch und Englisch und einen Screenshot für das Review
- [ ] Impressum, Datenschutz und Nutzungsbedingungen zusätzlich in den Einstellungen erreichbar
- [ ] Nur fürs iPhone: in `app.json` `ios.supportsTablet: false`; trotzdem auf dem iPad testen (Apple prüft dort im Kompatibilitätsmodus)
- [ ] Screenshots vom eigenen iPhone, fehlende Größen in Canva auf das verlangte Format gesetzt (Inhalt bleibt die echte App)
- [ ] Exportkontrolle: nur Standardverschlüsselung, `ios.config.usesNonExemptEncryption: false`
- [ ] Altersfreigabe ehrlich beantwortet; Nutzungsbedingungen und Onboarding sagen „ab 18“; Hinweis auf die KI vor dem ersten Aufruf
- [ ] Freigabe „Diese Version manuell veröffentlichen“ gewählt (keine Veröffentlichung zwischen 15.03. und der letzten Abiturprüfung)
- [ ] Keine Platzhalter, echte Screenshots, Backend läuft während des Reviews (2.1)
- [ ] Falls Nutzerkonten: Kontolöschung in der App
- [ ] Keine Gesundheitsversprechen, keine Diagnose, keine fremden Marken
- [ ] Eigene Kernfunktion, keine Variante einer bekannten App (4.3)
- [ ] Datenschutzangaben in App Store Connect passen zur App
- [ ] Eingaben werden auf dem Server nicht gespeichert, der Verlauf liegt nur auf dem Gerät
- [ ] Review-fest: geführter Ablauf statt leerem Chat, Verlauf auf dem Gerät, Kopieren und Teilen, Knopf „Antwort melden“ als E-Mail-Link, Kontaktadresse in der App (1.2, 4.2)
- [ ] Neue Angaben in App Store Connect beantwortet (für eine Text-Schreibhilfe: „Shared Location“ und „Dating and Relationships“ jeweils nein)
- [ ] Review-Notizen: was die App tut, wo die KI läuft, dass Ausgaben nur der Nutzer selbst sieht, auf welchem Bildschirm die Paywall erscheint, wie der Prüfer mit einem Sandbox-Kauf alles sieht
- [ ] Supabase im Gratis-Tarif: die Wachregel (zweimal je Woche eine echte Anfrage aus der eigenen App) steht im Kalender; ist in den Abiturmonaten eine App im Store oder im Review, für diese Monate Pro (liegt eine freigegebene App nur bereit, darf das Gratis-Projekt pausieren; vor dem Veröffentlichen wiederherstellen und testen)

## Sicherheit (Mindestprüfung, Claude führt aus, du siehst dir das Ergebnis an)

- [ ] Kein Schlüssel in der App; KI- und RevenueCat-Schlüssel nur als Supabase-Geheimnis; `.env` in `.gitignore`
- [ ] Server-Funktion prüft bei jedem Aufruf das aktive Abo der App-User-ID über RevenueCat (den Abo-Status darf sie einige Minuten zwischenspeichern; Sandbox-Käufe des Prüfers nicht ablehnen) und zählt eine Tagesgrenze (Start: 30 Antworten je Abonnent und Tag)
- [ ] RLS auf jeder Tabelle, keine Regel `using (true)`, Security Advisor ohne Fehler
- [ ] Anthropic-Konsole: vor dem Start Guthaben ohne Nachladen; ab dem Start Nachladen mit Monatslimit passend zur Nutzerzahl
- [ ] Repository und App nach Schlüsseln durchsucht (`git grep`, GitHub Secret Scanning)
- [ ] Test- und Betriebsprojekt getrennt (Testprojekt in eigener Gratis-Organisation), Tabellen-Schema als Migration im Repository (im Gratis-Tarif keine Backups), Claude ohne Zugang zum Betrieb
- [ ] Von außen getestet: Aufruf ohne aktives Abo scheitert
- [ ] Beide Supabase-Projekte mit den neuen Schlüsseln (Publishable und Secret) angelegt; die alten fallen Ende 2026 weg

## Zum Schluss

- [ ] Eigene Messereignisse nur mit Einwilligung (§ 25 TDDDG)
- [ ] `docs/UEBERGABE.md` auf dem neuesten Stand
- [ ] docs/review-log.md gelesen
