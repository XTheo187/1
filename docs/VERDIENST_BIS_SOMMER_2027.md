# Wie viel kann ich bis Sommer 2027 maximal erwirtschaften?

> **Hinweis (23.11.2026): nicht mit deinen echten Angaben gerechnet.** Diese
> Rechnung nimmt Bayern und den Arbeitsmarkt im Raum Regensburg an (Löhne,
> Ferien, Kirchensteuer). Tatsächlich lebst du in Niedersachsen, und Juli und
> August gehören teils deinem Umzug nach Zürich. Die Größenordnung bleibt
> ähnlich, die Zahlen sind aber nicht neu gerechnet. Deinen gewählten Plan
> findest du in [`APP_PLAN_ALLEIN_MIT_CLAUDE.md`](APP_PLAN_ALLEIN_MIT_CLAUDE.md).

**Frage:** Wie viel Geld kann ich – heute, am 22.11.2026, in der 13. Klasse
in Bayern (Raum Regensburg) – bis zum **31. August 2027** durch eigene
Arbeit verdienen, ohne das Abitur zu gefährden?

> **Antwort: realistisch maximal rund 13.500 € netto.**
>
> | Kennzahl (netto, nach Steuer und Abgaben) | Betrag |
> |---|---:|
> | **realistisches Maximum** – nur 1 von 10 Verläufen schafft mehr | **~13.500 €** |
> | Median mit dem Plan unten | ~11.300 € |
> | sicher – 9 von 10 Verläufen schaffen mindestens | ~8.800 € |
> | absolute Obergrenze – jede Annahme am oberen Rand, ~930 Arbeitsstunden | ~21.800 € |
> | … dazu 60-Stunden-Wochen im Sommer (nur mit Ausgleich nach Arbeitszeitgesetz) | ~23.600 € |
>
> **Am 31.08.2027 auf dem Konto ist es weniger:**
> - Rund 1.500 € Lohnsteuer behalten die Arbeitgeber vor allem im Sommer
>   ein. Sie kommen erst mit der Steuererklärung 2027 zurück, also 2028.
>   Kontostand im Median: ~9.900 €.
> - Zahlt der Sommer-Arbeitgeber den Augustlohn erst im September, was bei
>   Stundenlohn üblich ist, sind es am 31.08. nur ~7.600 €.
>
> Gut die Hälfte bringt ein **Vollzeit-Sommerjob nach dem Abiturzeugnis**
> (28.06.–31.08.2027, 47 Arbeitstage). Je etwa ein Fünftel bringen
> Ferienjobs vor dem Zeugnis sowie Nachhilfe und Minijob. Am stärksten
> verschiebt das Ergebnis, was danach kommt:
> - Vor einem **FH-Studium** ab 01.10. bleibt der Sommerjob
>   sozialversicherungsfrei (Median ~12.500 €).
> - Vor einem **dualen Studium oder einer Ausbildung** gehen auf den
>   Sommerjob ~21 % Sozialabgaben ab (Median ~10.900 €).
> - Bei **Ausbildungsbeginn am 01.08.** ist der Sommer zudem kürzer
>   (Median ~8.900 €).

**Gilt für:**
- Du bist volljährig.
- Du bist über einen gesetzlich versicherten Elternteil familienversichert.
- Nach dem Abitur folgt ein Studium, ein duales Studium oder eine
  Ausbildung.

Sonst ändern sich die Regeln:
- **Unter 18** gilt das Jugendarbeitsschutzgesetz: höchstens 40 h/Woche,
  keine Nachtarbeit.
- **Keine Familienversicherung** gibt es, wenn beide Eltern privat
  versichert sind. Dasselbe gilt, wenn der andere, verheiratete Elternteil
  privat versichert ist, über der Jahresarbeitsentgeltgrenze verdient und
  mehr verdient als der gesetzlich versicherte (§ 10 Abs. 3 SGB V). Dann
  gelten andere Grenzen.
- **Vor FSJ, BFD oder freiwilligem Wehrdienst** ist der Sommerjob
  berufsmäßig, wie vor einer Ausbildung.

Gerechnet mit `python3 plan/verdienst_2027.py` (20.000 simulierte Verläufe):
- Jede Phase bis August hat ein Stundenbudget, das das Abitur schützt.
- Die Stunden gehen an die Quelle mit dem höchsten erwarteten Erlös je
  Stunde.
- Begrenzt wird das durch die Nachfrage und die Regeln in Abschnitt 4.

## 1. Was jede Strategie bringt

| Strategie (netto bis 31.08.2027) | sicher (90 %) | Median | gut (10 %) | Spitze (1 %) |
|---|---:|---:|---:|---:|
| **beste Mischung (Plan unten)** | **8.800 €** | **11.300 €** | **13.500 €** | **14.900 €** |
| ohne Webgeschäft | 8.800 € | 11.300 € | 13.500 € | 14.900 € |
| nur befristete Jobs (Ferien, Einsätze, Sommer) | 7.400 € | 9.800 € | 12.000 € | 13.200 € |
| nur Nebenjobs neben der Schule (keine Ferien- und Sommerjobs) | 1.600 € | 2.300 € | 3.200 € | 3.900 € |

**Was danach kommt und welche Jobs du bekommst, entscheidet mit** (beste Mischung):

| Szenario | sicher (90 %) | Median | gut (10 %) |
|---|---:|---:|---:|
| FH-Studium ab 01.10. (Sommerjob sozialversicherungsfrei) | 10.900 € | 12.500 € | 14.100 € |
| duales Studium / Ausbildung, Start 01.09. oder 01.10. | 9.400 € | 10.900 € | 12.300 € |
| duales Studium / Ausbildung, Start 01.08. (nur 25 Sommer-Arbeitstage, dafür August-Vergütung) | 7.700 € | 8.900 € | 10.200 € |
| Industrie- oder Lagerjob in Ferien und Sommer sicher (17–20,50 €/h) | 9.200 € | 11.800 € | 13.800 € |
| kein Industriejob, nur Aushilfe und Zeitarbeit (14,60–17 €/h) | 8.200 € | 10.300 € | 12.100 € |
| überall nur Mindestlohn (14,60 €/h) | 7.800 € | 9.800 € | 11.300 € |
| ohne Jobtage im Mai und Juni vor dem Zeugnis | 8.100 € | 10.500 € | 12.600 € |
| ohne alle Ferienjobs vor dem Zeugnis | 6.300 € | 8.700 € | 10.600 € |

Am 31.08. auf dem Konto (Median) ist es weniger, weil die Lohnsteuer erst
2028 zurückkommt und der Augustlohn oft erst im September:

| Szenario | Kontostand | … ohne Augustlohn | Lohnsteuer einbehalten |
|---|---:|---:|---:|
| FH-Studium | ~10.700 € | ~7.800 € | ~1.800 € |
| dual, Start 01.09./01.10. | ~9.600 € | ~7.100 € | ~1.300 € |
| dual, Start 01.08. | ~8.100 € | ~8.100 € | ~900 € |

Im dualen Fall ist weniger einbehalten, weil die Sozialabgaben die
Lohnsteuer mindern.

## 2. Woher das Geld kommt

| Quelle | Mittel im Plan (brutto) | in der Obergrenze |
|---|---:|---:|
| Sommerjob nach dem Zeugnis (28.06.–31.08.) | 6.980 € | 9.250 € |
| Ferienjobs vor dem Zeugnis (Weihnachten, Februar, Pfingsten, Juni) | 2.610 € | 5.535 € |
| Nachhilfe (privat) | 1.260 € | – |
| Minijob | 890 € | – |
| Webgeschäft (`standortcheck`), Gewinn | 40 € | 8.260 € |
| August-Vergütung, falls die Ausbildung am 01.08. beginnt | 220 € | – |
| Übungsleiter/Betreuer, Wochenend-Einsätze | < 10 € | – |

**Neben der Schule ist das Stundenbudget die Grenze, nicht die
Familienversicherung.** Nachhilfe (privat 15–30 €/h) bringt je Stunde am
meisten, danach der Minijob (~15 €/h). Sie füllen das Budget fast immer.

**Das Webgeschäft lohnt sich bis Sommer kaum.** Mit den Quoten, die die
Recherche für Neulinge ergab (0,5–5 % Einstieg je Kontakt, 5–30 % Upsell,
Paket 800–2.200 €; siehe [`HEBEL_BIS_SOMMER_2027.md`](HEBEL_BIS_SOMMER_2027.md)),
bringt es im Mittel ~16 € Umsatz je Stunde, nach Kosten ~14 € – sehr
ungleich verteilt: oft fast nichts, selten 30–40 €. Im Erwartungswert
schlägt es den Minijob nicht und bekommt im Modell kaum Stunden. Wer es
trotzdem macht, kauft damit Erfahrung, Referenzen und die Chance auf den
oberen Rand, nicht mehr Geld bis August. (Eine frühere Fassung rechnete
mit 26 € je Stunde aus dem eigenen, ungeprüften Modell; daher lag das
Maximum bei ~14.000 €.)

Wochenend-Einsätze (~18 €/h) und Übungsleiter kommen nur zum Zug, wenn
Nachhilfeschüler oder Minijob fehlen.

In der Obergrenze nimmt das Webgeschäft das ganze Stundenbudget, weil es
dort am oberen Rand gerechnet ist: 42 € Umsatz je Stunde. Sein Gewinn 2027
liegt mit ~6.460 € noch unter 12 × 590 € = 7.080 €.

## 3. Der Plan zum Maximum

| Wann | Was | Stunden |
|---|---|---|
| **bis 23.12.2026** | <ul><li>2–4 Nachhilfeschüler suchen (Mittel-/Oberstufe, 20–30 €/h). Nachhilfe ist freiberuflich, braucht also kein Gewerbe.</li><li>Minijob suchen (Handel, Gastro, ~15 €/h, 3–10 h/Woche); dabei die Befreiung von der Rentenversicherung beantragen.</li><li>Optional das Webgeschäft mit `standortcheck` (Gewerbe in Regensburg 45 €) – bringt im Erwartungswert weniger als der Minijob, aber Erfahrung und Referenzen. Dann innerhalb eines Monats nach dem Start den **Fragebogen zur steuerlichen Erfassung** über ELSTER abgeben und dort die Kleinunternehmerregelung wählen.</li></ul> | 3–10 h/Woche |
| **Weihnachtsferien 24.12.–08.01.** | <ul><li>Befristeter Ferienjob an bis zu 9 Arbeitstagen: 5 Tage im Jahr 2026, 4 im Jahr 2027. Zum Beispiel Inventurhilfe, Lager, Paketsortierung (~18 €/h, z. B. über InStaff) – wenn das Lernen es zulässt.</li><li>Am besten zwei Verträge: 24.–31.12. und ab 04.01. Ein durchgehender Vertrag zählt 2027 mit 8 statt 5 Kalendertagen.</li></ul> | Vollzeit |
| **Januar – März 2027** | <ul><li>Nachhilfe und Minijob (oder Webgeschäft) weiterführen.</li><li>**Sommerjob jetzt sichern:** Ferienarbeit oder Produktion bei Industriebetrieben (BMW, Krones, Infineon, Continental) oder über Zeitarbeit (Randstad u. a.), Start 28.06.</li><li>Den Juni-Job (unten) gleich mit vereinbaren.</li></ul> | 3–10 h/Woche |
| **Frühjahrsferien 08.–12.02.** | Ferienjob an 5 Arbeitstagen | Vollzeit |
| **22.03. – 13.06.2027** | <ul><li>Lernen und Prüfungen: schriftliches Abitur 21.04.–13.05., Kolloquium 31.05.–11.06.</li><li>Höchstens ein paar Nachhilfestunden.</li><li>In den Pfingstferien (18.–28.05.) höchstens 1–4 einzelne Jobtage.</li></ul> | 0–6 h/Woche |
| **14. – 24.06.2027** | <ul><li>Nach dem letzten eigenen Prüfungstermin befristeter Job an 5–9 Tagen. Mit der Schule klären; eigener Vertrag, der vor der Entlassung endet.</li><li>Als **Schülerjob** ist er sozialversicherungsfrei, auch vor einem dualen Studium.</li></ul> | Vollzeit |
| **28.06. – 31.08.2027** | <ul><li>Vollzeit-Sommerjob, Mo–Fr und einzelne Samstage.</li><li>Gern mit Nacht- und Sonntagszuschlägen: Sie bringen vor allem mehr Lohn.</li><li>Steuerfrei nach § 3b EStG sind nur Zuschläge für Arbeit von 20 bis 6 Uhr und an Sonn- und Feiertagen, keine Schichtzulagen.</li></ul> | bis 48 h/Woche |
| **bis 31.07.2027** (ein Samstag, also bis 02.08.) | **Steuererklärung 2026**, mit Anlage EÜR. Pflicht, wenn du 2026 Arbeitslohn hattest (Weihnachtsjob) und Nachhilfe und Webgeschäft zusammen mehr als 410 € Gewinn brachten. Sonst freiwillig: Sie holt die Lohnsteuer vom Weihnachtsjob zurück. | – |
| **2028** | **Steuererklärung 2027:** Die einbehaltene Lohnsteuer (~1.500 €) kommt zurück, soweit Lohn plus Gewinn unter ~14.030 € bleibt (Entwurf 2027, noch nicht beschlossen). Pflicht, sobald der Gewinn über 410 € liegt. | – |

**Wo suchen:**
- Bundesagentur für Arbeit (Jobbörse)
- Einsatz-Plattformen: InStaff, Zenjob, wo es sie gibt
- Industrie-Ferienarbeit: direkt bei den Firmen und über Zeitarbeitsfirmen
- Winter:
  - Inventur Ende Dezember / Anfang Januar
  - Christkindlmarkt bis 23.12. (Wochenenden)
  - Weihnachtsaushilfe in der Paketsortierung
- Sommer:
  - Biergarten und Sommergastronomie
  - Freibad (mit Rettungsschwimmer-Schein)
  - Feste, Dult
  - Erntehilfe

**Werkstudentenjobs** gehen erst ab der Einschreibung. Wer sich schon im
August einschreibt, kann ab dann als Werkstudent arbeiten. Für den Sommer
ändert das wenig, weil der Sommerjob ohnehin sozialversicherungsfrei ist.

**Damit der Sommerjob abgabenfrei bleibt (FH-/Uni-Fall):**
- **Als kurzfristige Beschäftigung anmelden lassen**, von vornherein
  befristet bis spätestens 31.08.
  - Die Grenze: höchstens **3 Monate oder 70 Arbeitstage im Kalenderjahr
    2027**.
  - Alle befristeten Jobs des Jahres zählen zusammen. Dabei treten
    90 Kalendertage an die Stelle der 3 Monate; volle Monate zählen mit
    30 Tagen.
  - Alle Jobs dem Arbeitgeber angeben.
  - Der Sommerjob allein zählt 63 Kalendertage (3 + 30 + 30). Für alle
    befristeten Jobs davor bleiben also ~27 Kalendertage. Im Plan sind das
    Januar 5, Februar 5, Pfingsten 1–4, Juni bis 11 und einzelne Einsätze.
- **Nicht gleichzeitig und nicht direkt im Anschluss an einen Minijob
  beim selben Arbeitgeber.** Sonst gilt es als eine einheitliche
  Beschäftigung und ist sozialversicherungspflichtig. Unschädlich ist eine
  Pause von mindestens 2 Monaten.
- **Wer studieren will:**
  - Eine Meldung als **ausbildungsuchend** bei der Agentur für Arbeit
    spätestens zum Schulende beenden und sich danach nicht neu melden.
  - Das Studium muss zum nächstmöglichen Termin beginnen.
  - Studienabsicht oder Zulassung dem Arbeitgeber nachweisen.
- **Lohn kommt erst nach dem Monat:** Stundenlohn wird oft erst im
  Folgemonat gezahlt. Wer das Geld am 31.08. braucht, vereinbart eine
  Abschlagszahlung oder wöchentliche Abrechnung.
- **Vor einem dualen Studium, PiBS, einer Ausbildung, FSJ/BFD oder
  freiwilligem Wehrdienst** ist der Sommerjob berufsmäßig.
  - Er ist dann sozialversicherungspflichtig: ~21 % Abzug, eingerechnet.
  - Dafür gilt keine Tagesgrenze.
  - Die Jobs bis zum Zeugnis bleiben Schülerjobs und frei.
- **Kurze Ferienjobs und die 25-%-Pauschalsteuer (§ 40a EStG):** Möglich
  ist sie nur bis 18 zusammenhängende Arbeitstage, höchstens 150 € je Tag
  und 19 € je Stunde, also nicht für den Sommerjob.
  - Will ein Arbeitgeber sie **auf dich abwälzen**, auf Abrechnung nach
    Steuer-ID und Klasse I bestehen. Die Pauschalsteuer kommt nicht zurück.
  - Trägt er sie selbst, ist sie für dich sogar günstig: Es wird nichts
    einbehalten.

**Der Starttermin der Ausbildung ist ein Hebel:**
- Der 01.08. statt 01.09. kostet 22 Sommer-Arbeitstage samt Samstagen
  (~3.100–4.000 € brutto, im Mittel ~3.600 €).
- Dafür kommt eine Monatsvergütung dazu (dual ~1.000–1.300 € brutto).
- Unterm Strich: Median 9.300 statt 11.300 €.

Wer die Wahl hat, nimmt den 01.09. oder 01.10.

## 4. Was den Betrag begrenzt

| Regel | Wirkung |
|---|---|
| **Familienversicherung** (§ 10 SGB V): Gesamteinkommen höchstens 565 € (2026) bzw. 590 € (2027) im Monat. Gewinne aus Nachhilfe und Webgeschäft zählen als Jahresgewinn / 12. Wer daneben einen Minijob hat, darf insgesamt (Minijob + Gewinn / 12) bis 603 bzw. 633 € | <ul><li>2027 sind neben der Schule bis ~7.000 € Gewinn drin (12 × 590 €).</li><li>Das gilt, wenn danach kein weiteres regelmäßiges Einkommen folgt (etwa ein Werkstudentenjob ab Oktober) und 2026 vorher keins da war.</li><li>Vorher bei der Krankenkasse nachfragen.</li><li>Im Plan begrenzt das Stundenbudget, nicht diese Grenze.</li><li>Darüber käme eine eigene Krankenversicherung: mindestens ~282 €/Monat (2027), und dann auch auf den Lohn des Sommerjobs (~20,5 %). Details in [`HEBEL_BIS_SOMMER_2027.md`](HEBEL_BIS_SOMMER_2027.md), Abschnitt 5.</li></ul> |
| **Übungsleiter-/Betreuerpauschale** (§ 3 Nr. 26 EStG): bis 3.300 € im Jahr steuer- und sozialversicherungsfrei, zählt nicht zum Gesamteinkommen. Gilt für Arbeit für einen Verein oder eine gemeinnützige oder öffentliche Stelle (Trainer, Betreuer, Ferienprogramm) | <ul><li>Kommt zusätzlich zur Grenze.</li><li>Hilft, sobald die Grenze drückt.</li><li>Im Plan nur ein Ersatz, weil es je Stunde weniger bringt (~10–18 €).</li></ul> |
| **Rentenversicherung für Selbstständige** (§ 2 SGB VI): Selbstständige Nachhilfe ist ab regelmäßig mehr als 603 bzw. 633 € Gewinn im Monat rentenversicherungspflichtig (18,6 %, Meldung an die DRV binnen 3 Monaten). Das Webgeschäft als Gewerbe ist es nicht | Nachhilfe im Modell auf 603/633 € je Monat begrenzt |
| **Kurzfristige Beschäftigung:** höchstens 3 Monate (mehrere Jobs: 90 Kalendertage) oder 70 Arbeitstage je Kalenderjahr, ohne Verdienstgrenze; zählt nicht zur Familienversicherung | <ul><li>Trägt Ferien- und Sommerjobs.</li><li>2027 zusammen höchstens 90 Kalendertage, davon braucht der Sommer 63.</li></ul> |
| **Sozialversicherung:** Jobs bis zum Zeugnis frei (Schülerjobs). Der Sommerjob ist frei, wenn danach ein Studium folgt. Vor einem dualen Studium oder einer Ausbildung ist er berufsmäßig (~21,15 % Arbeitnehmeranteil 2026). Beim Minijob die Befreiung von der Rentenversicherung beantragen, sonst 3,6 % | −1.100 bis −1.650 € (Median) im dualen Fall |
| **Arbeitszeitgesetz:** 8 h/Tag, bis 10 h; im Schnitt 48 h/Woche (Mo–Sa); 11 h Ruhezeit | Sommer höchstens ~450 Stunden |
| **Lohnsteuer:** Klasse I. Kurze Jobs werden nach der Tagestabelle aufs Jahr hochgerechnet und behalten deshalb viel ein; ein voller Sommermonat ~350–900 €. Zurück kommt sie über die Steuererklärung, soweit Lohn minus Pauschbeträge plus Gewinn unter dem Grundfreibetrag bleibt: 2026 Lohn − 1.266 € unter 12.348 €; im Entwurf 2027 Lohn − 1.466 € unter 12.564 € (Arbeitnehmer-Pauschbetrag 1.430 €). Lohn plus Gewinn darf 2027 also bis ~14.030 € gehen | <ul><li>Am 31.08. fehlen ~900–1.800 € auf dem Konto.</li><li>Endgültig fällt im Plan kaum Steuer an.</li></ul> |
| **Mindestlohn:** 13,90 € (2026), 14,60 € (2027). Zeitarbeit mindestens 15,33 € bis 03/2027 und 15,87 € ab 04/2027 | Untergrenze jeder Stunde |
| **Kalender:** 47 Arbeitstage nach dem Zeugnis (25, wenn die Ausbildung am 01.08. beginnt). Dazu bis zu 9 Arbeitstage zwischen letzter Prüfung und Zeugnis und einzelne Tage in den Pfingstferien | der größte Einzelposten |

## 5. Was mehr bringen würde – und warum der Plan es nicht vorsieht

- **Mehr Stunden vor dem Abitur:**
  - Jede zusätzliche Stunde pro Woche bringt bis März ~200–340 €
    (15–25 €/h × ~13,5 Wochen), kostet aber Lernzeit.
  - Wer über ~20 h/Woche neben der Schule arbeitet, hat im Schnitt
    schlechtere Noten. Ob das ursächlich ist, ist umstritten: Laut
    DIW/SOEP schadet moderates Jobben nicht.
  - Das Stundenbudget hier ist eine bewusste Vorsicht wegen der
    Prüfungsphase.
  - Die Abiturnote zählt für viele Studienplätze und für manche duale
    Plätze.
- **Familienversicherung aufgeben**, um neben der Schule mehr regelmäßig
  zu verdienen:
  - Die eigene Versicherung kostet mindestens ~282 €/Monat (2027). Als
    freiwilliges Mitglied zahlt man dann auch auf den Lohn des Sommerjobs
    (~20,5 %, im Juli und August je ~650 € mehr).
  - Im Studiums-Fall lohnt mehr Gewinn deshalb erst ab ~9.500–11.300 €
    Gesamtgewinn 2027; dazwischen bringt mehr Gewinn weniger Geld.
  - Bei Nachhilfe kommt über 633 € im Monat der Rentenbeitrag dazu
    (18,6 %).
  - Mit den Lernstunden ist das kaum zu schaffen. Was ein eigenes Geschäft
    mit Hebel bringt, steht in
    [`HEBEL_BIS_SOMMER_2027.md`](HEBEL_BIS_SOMMER_2027.md).
- **60-Stunden-Wochen im Sommer:**
  - Rechtlich nur mit Ausgleich über 6 Monate bzw. 24 Wochen, und
    körperlich belastend.
  - Brächte ~1.700 € mehr (Obergrenze 23.600 statt 21.800 €).
- **Glücksspiel, Trading:** kein Erwirtschaften und im Schnitt ein Verlust
  (siehe [`500K_BIS_SOMMER_2027.md`](500K_BIS_SOMMER_2027.md)).

## 6. Was mit dem Geld passieren sollte

Nach der Sparregel des [Millionenplans](MILLIONENPLAN.md) kommen 60 % von
allem über dem Grundbedarf in den Welt-ETF.

Beispiel mit ~11.300 €:
- Grundbedarf im Elternhaus ~300–500 € im Monat
- ergibt ~4.100–5.200 € fürs Depot
- davon ~1.500 € erst 2028 mit der Steuererstattung

## 7. Grenzen dieser Rechnung

- **Industrie-Ferienlöhne** in Regensburg sind nur indirekt belegt:
  Randstad für BMW 18–20 €/h (2024), InStaff Lager Ø 18,02 €,
  Metall-Tarif EG 1 ~18,07 €/h. Ob man einen solchen Platz bekommt, ist
  geschätzt (50–90 %).
- **Nachhilfe und Webgeschäft:**
  - Die Nachfrage nach Nachhilfe (1–6 h/Woche) und die Chance, Schüler zu
    finden (60–95 %), sind geschätzt.
  - Die Quoten des Webgeschäfts sind für Neulinge nirgends gemessen; die
    Werte stammen aus Telefon- und Haustürquoten (Recherche in
    [`HEBEL_BIS_SOMMER_2027.md`](HEBEL_BIS_SOMMER_2027.md)).
- **Die Stundenbudgets neben der Schule** (3–10 h/Woche, in der
  Prüfungszeit 0–6) sind eine Vorgabe zum Schutz des Abiturs, keine
  Messung. Das gilt auch für die Jobtage im Mai und Juni. Sie hängen von
  den eigenen Prüfungsterminen und der Schule ab; ohne sie sinkt der
  Median um ~800 €.
- **Familienversicherung:**
  - Wie eine Kasse schwankende Gewinne im Einzelfall bewertet, kann
    abweichen.
  - Einkommen von Januar bis November 2026 ist nicht bekannt und nicht
    eingerechnet.
- **Steuer:**
  - Gerechnet mit dem Tarif 2026. Für 2027 gelten die beiden Änderungen
    des Entwurfs: Grundfreibetrag 12.564 €, Arbeitnehmer-Pauschbetrag
    1.430 €.
  - Die einbehaltene Lohnsteuer ist grob geschätzt: ohne
    Vorsorgepauschale bei sozialversicherungsfreien Jobs und ohne
    Kirchensteuer (in Bayern 8 % der Lohnsteuer, kommt ebenfalls zurück).
  - Trinkgeld ist nicht eingerechnet.
- **Kontostand am 31.08.:** Unterstellt ist, dass die Erstattung 2026 (im
  Median ~100 €) bis dahin da ist. Der Augustlohn ist einmal mit und einmal
  ohne gerechnet.
- **Annahme über das Wissen vorab:** Die Quellen werden nach dem
  *erwarteten* Erlös je Stunde gewählt. Wer früh merkt, dass sein
  Webgeschäft gut läuft (deutlich über 15 € je Stunde), verlagert Stunden
  dorthin und verdient etwas mehr als hier gerechnet.

## 8. Nachrechnen

```
python3 plan/verdienst_2027.py            # Abschnitte 1, 2 und Obergrenze, Kontostand je Szenario
python3 -m unittest discover -s tests     # u. a. tests/test_verdienst.py
```

## 9. Quellen

**Löhne**
- Mindestlohn 13,90 € (2026) / 14,60 € (2027), MiLoV5:
  <https://www.bmas.de/DE/Service/Gesetze-und-Gesetzesvorhaben/fuenfte-mindestlohnanpassungsverordnung-milov5.html>
- Lohnuntergrenze Zeitarbeit: <https://lohn-info.de/mindestlohn_zeitarbeit.html>
- Produktion BMW Regensburg über Randstad, 18–20 €/h (Anzeige 2024):
  <https://europeanjobdays.eu/de/job/production-workers-mfd-bmw-regensburg>
- Metall/Elektro Bayern, EG 1: <https://tarifvertrag-online.de/entgelttabelle/metall-elektro/ig-metall/bayern>
- Amazon Logistik 16,22–16,66 €/h: <https://retail-news.de/amazon-lohnerhoehung-logistik-deutschland-2026/>
- Deutsche Post EG 1: <https://tarifvertrag-online.de/entgelttabelle/deutsche-post/2025>
- InStaff Regensburg:
  - Lager: <https://www.instaff.jobs/lagerhelfer-kommissionierer-jobs/regensburg>
  - Service: <https://www.instaff.jobs/service-kellner-jobs/regensburg>
  - Promotion: <https://www.instaff.jobs/promotion-jobs/regensburg>
- Nachhilfe:
  - privat: <https://www.superprof.de/blog/der-richtige-stundenlohn-fuer-nachhilfe/>
  - Institute: <https://www.ulmato.de/ausbildung/nachhilfelehrer>
- Website-Preise für KMU: <https://sellwerk.de/wissenswert/was-kostet-eine-website>
- Plattformarbeit (ILO): <https://www.ilo.org/global/about-the-ilo/newsroom/news/WCMS_771909/lang--en/index.htm>

**Regeln**
- Familienversicherung, § 10 SGB V (Gesamteinkommen, Grenze mit Minijob):
  <https://www.buzer.de/10_SGB_V.htm>
- GKV-Spitzenverband, Grundsätzliche Hinweise zum Gesamteinkommen (2022;
  Freibeträge darin veraltet):
  <https://www.vdek.com/content/vdeksite/vertragspartner/mitgliedschaftsrecht_beitragsrecht/familienversicherung/_jcr_content/par/download_1642322223/file.res/Grundsaetzliche-Hinweise-Gesamteinkommen-29092022.pdf>
- Zahlenwerte 2027 (Bezugsgröße 4.130 €, Minijob-Grenze 633 €):
  <https://www.krankenkassen.de/gesetzliche-krankenkassen/system-gesetzliche-krankenversicherung/sozialversicherung-rechengroessen-beitragsbemessungsgrenze-versicherungspflichtgrenze/rechengroessen-2027/>
- Geringfügigkeits-Richtlinien 2026 (Minijob, kurzfristige Beschäftigung,
  90 Kalendertage bei Zusammenrechnung, Berufsmäßigkeit, Ausbildungsuchende):
  <https://www.aok.de/fk/fileadmin/user_upload/jahreswechsel/2026/2026-geringfuegigkeits-richtlinien.pdf>
- Minijob-Zentrale:
  - kurzfristige Beschäftigung: <https://www.minijob-zentrale.de/DE/die-minijobs/kurzfristige-beschaeftigung/kurzfristige-beschaeftigung_node.html>
  - nach dem Schulabschluss: <https://magazin.minijob-zentrale.de/kurzfristiger-minijob-nach-dem-schulabschluss/>
  - Abgaben: <https://www.minijob-zentrale.de/DE/fuer-gewerbetreibende/abgaben-und-steuern>
- Rentenversicherungspflicht selbstständiger Lehrer:
  - § 2 SGB VI: <https://www.buzer.de/2_SGB_VI.htm>
  - geringfügige Selbstständigkeit, § 5 SGB VI: <https://www.buzer.de/5_SGB_VI.htm>
- Beitragssätze 2026 (TK): <https://www.tk.de/firmenkunden/versicherung/beitraege-faq-und-mehr/beitragssaetze/aktuelle-beitragssaetze-in-der-sozialversicherung-2031554>
- Steuern:
  - Übungsleiterpauschale, § 3 Nr. 26 EStG: <https://lxgesetze.de/estg/3>
  - Pauschalsteuer für Aushilfen, § 40a EStG: <https://lxgesetze.de/estg/40a>
  - steuerfreie Zuschläge, § 3b EStG: <https://lxgesetze.de/estg/3b>
- Lohnsteuer:
  - bei Ferienjobs (BdSt 2026): <https://steuerzahler.de/fileadmin/user_upload/LV_Baden-W%C3%BCrttemberg/BdSt_AN_News_fuer_Arbeitnehmer_Juli_2026_Ferienjob_NEU.pdf>
  - Grundfreibetrag-Entwurf 2027: <https://www.bundestag.de/presse/hib/kurzmeldungen-1221672>
- Arbeitszeitgesetz § 3: <https://dejure.org/gesetze/ArbZG/3.html>
- Gewerbeanmeldung Regensburg: <https://www.firma.de/gewerbeamt/regensburg/>

**Kalender und Schule**
- Abiturtermine 2027 (BayMBl. 2025 Nr. 354): <https://www.verkuendung-bayern.de/baymbl/2025-354/>
- Ferien Bayern: <https://www.km.bayern.de/termine/ferien-und-feiertage>
- Ausbildungsbeginn (IHK München): <https://www.ihk-muenchen.de/de/berufsbildung-berufszugang/auszubildende/beratung/allgemeine-informationen/ausbildungsbeginn>
- Arbeitsstunden und Schulleistung:
  - <https://pmc.ncbi.nlm.nih.gov/articles/PMC2926992>
  - SOEP/DIW: <https://www.diw.de/de/diw_01.c.10379.de/jobben_von_jugendlichen_beeintraechtigt_weder_schulleistungen_noch_freizeit.html>
