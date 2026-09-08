# Geschäftsplan: 500 € Startkapital, 20 Stunden pro Woche

Dieses Dokument erklärt, warum das Werkzeug so gebaut ist, wie es gebaut ist.
Alle Zahlen stammen aus `standortcheck plan` und lassen sich dort mit eigenen
Ist-Werten nachrechnen.

## 1. Die Ausgangslage bestimmt das Modell

Zwei Grenzen, die nicht verhandelbar sind:

- **500 € Kapital.** Damit ist alles ausgeschlossen, was Reichweite kaufen
  muss. Bezahlte Anzeigen brauchen ein Vielfaches, bevor die erste belastbare
  Abschlussquote überhaupt messbar ist.
- **20 Stunden pro Woche.** Damit ist alles ausgeschlossen, was viele kleine
  Kunden braucht. 200 Nutzer für 9 € im Monat zu gewinnen und zu betreuen
  kostet mehr Zeit als 2 Kunden für 1.800 €.

Was übrig bleibt: **wenige Kunden, hoher Einzelwert, Direktvertrieb.**

## 2. Warum lokale Betriebe, warum Websites

| Kriterium | Bewertung |
|---|---|
| Zahlungsbereitschaft | Ein Dachdecker verdient an einem Auftrag 4.000 €. Eine Website für 1.900 € rechnet sich für ihn ab dem ersten zusätzlichen Kunden. |
| Auffindbarkeit der Kunden | Vollständig in OpenStreetMap erfasst — kostenlose Recherche. |
| Prüfbarkeit des Bedarfs | Die Website ist öffentlich. Der Bedarf lässt sich **vor** dem ersten Kontakt messen, nicht erst im Gespräch. |
| Wettbewerb | Agenturen ignorieren Aufträge unter 5.000 €. Der Bereich darunter ist unterversorgt. |
| Wiederkehrender Umsatz | Betreuung 49–89 €/Monat. Nach 12 Monaten trägt das die Fixkosten. |

Der entscheidende Punkt ist die dritte Zeile. Weil der Bedarf messbar ist,
wird aus Kaltakquise eine **Rückmeldung zu einem konkreten Befund**. Das ist
ein anderes Gespräch — und der Grund, warum das Werkzeug überhaupt existiert.

## 3. Aufteilung der 500 €

| Posten | Betrag | Warum |
|---|---:|---|
| Gewerbeanmeldung | 30 € | Pflicht. Kleinunternehmerregelung nach § 19 UStG wählen. |
| Domain + Hosting, 12 Monate | 60 € | Eigene Seite als Referenz — wird von jedem Interessenten geprüft. |
| Berufshaftpflicht, 3 Monate | 45 € | Sobald fremde Systeme angefasst werden, nicht optional. |
| Druck + Porto, 150 Anschreiben | 200 € | Der eigentliche Motor. ~1,30 € je Brief inkl. beigelegter Analyse. |
| Visitenkarten + Briefpapier | 40 € | Für den Vor-Ort-Termin. |
| Rechtstexte eigene Seite | 0 € | Kostenfreier Generator, später gegen geprüfte Fassung tauschen. |
| Reserve | 125 € | Fahrtkosten, Nachdruck. Ohne Puffer erzwingt die erste Überraschung Stillstand. |

**Bewusst nicht gekauft:** Anzeigen, Lead-Datenbank-Abo, Logo vom Grafiker,
Buchhaltungs-Abo, CRM-Abo. Begründungen in `standortcheck plan`.

## 4. Der Trichter und die eigentliche Engstelle

Aufträge kosten Umsetzungszeit. Mehr Briefe erzeugen mehr Aufträge — bis die
20 Stunden voll sind. **Der Engpass ist nicht die Nachfrage, sondern die
Umsetzung.** Deshalb rechnet `standortcheck plan` die optimale Briefmenge aus,
statt eine feste Zahl vorzugeben.

Im mittleren Szenario: 35 Briefe pro Woche, davon rund 19 telefonisch erreicht,
4 echte Gespräche, 2 Angebote, 0,5 Aufträge. Zeitbedarf 18,3 von 20 Stunden.

| Szenario | Briefe/Woche | Aufträge/Woche | Umsatz/Monat | Effektiv €/h |
|---|---:|---:|---:|---:|
| vorsichtig | 65 | 0,25 | ~1.500 € | ~13 € |
| erwartet | 35 | 0,48 | ~3.900 € | ~47 € |
| gut | 20 | 0,64 | ~6.100 € | ~80 € |

**Planen Sie mit „vorsichtig".** Dort liegt der effektive Stundenlohn bei
13 € — unter Mindestlohn. Das ist die ehrliche Aussage über die Anfangsphase
und der Grund, warum die ersten drei Monate über das Gespräch entschieden
werden, nicht über die Briefmenge.

## 5. Die ersten zwölf Wochen

**Woche 1–2 — Aufbau (kein Umsatz).**
Gewerbe anmelden. Eigene Website bauen: Sie ist Referenz und Übungsstück
zugleich. Rechtstexte auf der eigenen Seite mustergültig umsetzen — Sie
verkaufen später genau das. Danach `suchen` und `pruefen` für den eigenen
Landkreis laufen lassen, 150–300 Leads sammeln.

**Woche 3–6 — Erste Welle (35 Briefe/Woche).**
Briefe raus, drei Tage nach Zustellung anrufen. Jedes Gespräch eintragen.
Ziel dieser Phase ist **nicht Umsatz, sondern Datenerhebung**: Nach 100 Briefen
kennen Sie Ihre echten Quoten. Bis dahin: nicht am Preis drehen, nicht das
Gewerk wechseln, nicht die Vorlage umschreiben. Sonst messen Sie nichts.

**Woche 7 — Auswertung.**
`standortcheck kennzahlen`. Die Ist-Quoten in `planner.Annahmen` eintragen und
`plan` neu rechnen. Jetzt entscheidet sich, welche Schraube dran ist:

- Erreichquote unter 40 % → andere Anrufzeiten (Handwerk: 7–8 Uhr, ab 16 Uhr).
- Gesprächsquote unter 15 % → der Einstiegssatz trägt nicht.
- Angebotsquote unter 35 % → Sie verkaufen die Lösung statt des Problems.
- Abschlussquote über 45 % → **Preis zu niedrig.** Nächstes Angebot +20 %.

**Woche 8–12 — Verdichten.**
Das Gewerk mit der besten Abschlussquote verdoppeln. Referenzen einsammeln:
jeder gewonnene Kunde wird nach zwei zufriedenen Wochen um eine Empfehlung
gebeten — Empfehlungen schlagen jeden Brief.

## 6. Wann es funktioniert und wann nicht

Der Plan trägt, wenn nach zwölf Wochen zwei bis vier Aufträge stehen und die
Betreuungsverträge anlaufen. Ab dann ist der monatliche Sockel real und die
Akquise finanziert sich selbst.

Er trägt **nicht**, wenn die Telefonakquise nicht stattfindet. Der Brief allein
erzeugt kaum Rückläufer; er ist der Anlass für den Anruf, nicht der Ersatz.
Wer die Anrufe nicht macht, verbrennt 200 € Porto ohne Ergebnis. Das ist die
realistischste Art, an diesem Modell zu scheitern — und sie hat nichts mit
dem Werkzeug zu tun.

## 7. Grenzen, die offen benannt gehören

- **Die Ertragszahlen sind Modellannahmen, keine Zusage.** Erst die eigenen
  Ist-Quoten aus `kennzahlen` machen daraus eine Prognose.
- **Die Datenlage ist unvollständig.** In OpenStreetMap sind längst nicht alle
  Betriebe erfasst. Für dünn besiedelte Regionen den Radius erhöhen.
- **Die Rechtsprüfungen sind technische Indizien, keine Rechtsberatung.** Ob
  ein Betrieb etwa unter die Kleinstunternehmer-Ausnahme des
  Barrierefreiheitsstärkungsgesetzes fällt, kann das Werkzeug nicht wissen.
  Der Bericht sagt das an Ort und Stelle.
- **Die Ansprache ist rechtlich geregelt.** Brief und Anruf sind vertretbar,
  die kalte Werbe-E-Mail nicht (§ 7 Abs. 2 Nr. 2 UWG). Vor der ersten größeren
  Kampagne lohnt eine einmalige anwaltliche Durchsicht der Vorlagen —
  einmalige Kosten, dauerhafte Sicherheit.
- **Es bleibt Handarbeit.** Das Werkzeug erzeugt Leads, Befunde und
  Verkaufsmaterial. Es führt keine Gespräche und baut keine Websites.
