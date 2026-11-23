# Checkliste vor jeder Einreichung

(Vorlage aus docs/APP_PLAN_ALLEIN_MIT_CLAUDE.md, Abschnitt 15 C und 7. Als
`docs/checkliste-einreichung.md` ins App-Repository kopieren.)

- [ ] Kernfunktion auf dem echten iPhone **und iPad** geprüft, auch ohne Netz (Meldung statt Absturz)
- [ ] Einwilligung vor dem ersten KI-Aufruf: Anbieter und Daten genannt (5.1.2(i))
- [ ] Harte Paywall ohne Umschalter; Preis deutlicher als jede Testphase; Laufzeit, Verlängerung und Kündigung klar (3.1.2)
- [ ] „Käufe wiederherstellen“ vorhanden (3.1.1)
- [ ] Links zu Datenschutz und Nutzungsbedingungen auf der Paywall und in App Store Connect (5.1.1)
- [ ] Abo-Gruppe und alle Abos angelegt und zusammen mit dieser App-Version eingereicht
- [ ] Kein Hinweis auf Käufe außerhalb der App
- [ ] Nur Wochen- und Monatsabo (kein Jahresabo vor Juli 2027)
- [ ] Impressum in der App erreichbar
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
- [ ] Fotos werden nach der Analyse nicht gespeichert
- [ ] Supabase Pro aktiv (ab dem Start)

## Sicherheit (Mindestprüfung, Claude führt aus, du siehst dir das Ergebnis an)

- [ ] Kein Schlüssel in der App; KI- und RevenueCat-Schlüssel nur als Supabase-Geheimnis; `.env` in `.gitignore`
- [ ] Server-Funktion prüft bei jedem Aufruf das aktive Abo der App-User-ID über RevenueCat und zählt ein Tageslimit
- [ ] RLS auf jeder Tabelle, keine Regel `using (true)`, Security Advisor ohne Fehler
- [ ] Ausgabenlimit in der Anthropic-Konsole passend zur Nutzerzahl
- [ ] Repository und App nach Schlüsseln durchsucht (`git grep`, GitHub Secret Scanning)
- [ ] Test- und Betriebsprojekt getrennt, Backups an, Claude ohne Zugang zum Betrieb
- [ ] Von außen getestet: Aufruf ohne aktives Abo scheitert

## Zum Schluss

- [ ] Eigene Messereignisse nur mit Einwilligung (§ 25 TDDDG)
- [ ] Hinweise für das Review: was die App tut, wie man die Paywall testet
- [ ] docs/review-log.md gelesen
