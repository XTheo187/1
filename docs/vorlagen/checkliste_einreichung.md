# Checkliste vor jeder Einreichung

(Vorlage aus docs/APP_PLAN_ALLEIN_MIT_CLAUDE.md, Abschnitt 10 C. Als
`docs/checkliste-einreichung.md` ins App-Repository kopieren.)

- [ ] Kernfunktion auf dem echten iPhone geprüft, auch ohne Netz (Meldung statt Absturz)
- [ ] Einwilligung vor dem ersten KI-Aufruf: Anbieter und Daten genannt (5.1.2(i))
- [ ] Harte Paywall ohne Umschalter; Preis, Laufzeit, Verlängerung klar (3.1.2)
- [ ] „Käufe wiederherstellen“ vorhanden (3.1.1)
- [ ] Links zu Datenschutz und Nutzungsbedingungen auf der Paywall und in App Store Connect (5.1.1)
- [ ] Abo-Gruppe und alle Abos angelegt und zusammen mit dieser App-Version eingereicht
- [ ] Knopf oder Link zum Web-Kauf nur im US-Storefront sichtbar; sonst kein Hinweis auf Käufe außerhalb der App
- [ ] Falls Nutzerkonten: Kontolöschung in der App
- [ ] Keine Gesundheitsversprechen, keine Diagnose, keine fremden Marken
- [ ] Eigene Kernfunktion, keine Variante einer bekannten App (4.3)
- [ ] Datenschutzangaben in App Store Connect passen zur App
- [ ] Kein Schlüssel in der App; Zugriffsregeln auf jeder Tabelle; Fotos werden nicht gespeichert
- [ ] Supabase Pro aktiv; Abo-Prüfung über RevenueCat und Tageslimit je App-User-ID auf dem Server; Ausgabenlimit der KI-API passend zur erwarteten Nutzerzahl
- [ ] Eigene Messereignisse nur mit Einwilligung (§ 25 TDDDG)
- [ ] Hinweise für das Review: was die App tut, wie man die Paywall testet
- [ ] docs/review-log.md gelesen
