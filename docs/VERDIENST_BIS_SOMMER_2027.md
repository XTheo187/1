# Wie viel kann ich bis Sommer 2027 maximal erwirtschaften?

**Frage:** Wie viel Geld kann ich – heute, am 22.11.2026, in der 13. Klasse
in Bayern (Raum Regensburg) – bis zum **31. August 2027** durch eigene
Arbeit verdienen, ohne das Abitur zu gefährden?

> **Antwort: realistisch maximal rund 13.000 € netto.**
>
> | Kennzahl (netto, nach Steuer und Abgaben) | Betrag |
> |---|---:|
> | **realistisches Maximum** – nur 1 von 10 Verläufen schafft mehr | **~13.100 €** |
> | Median mit dem Plan unten | ~10.700 € |
> | sicher – 9 von 10 Verläufen schaffen mindestens | ~8.200 € |
> | absolute Obergrenze – jede Annahme am oberen Rand, ~770 Arbeitsstunden | ~17.300 € |
> | … dazu 60-Stunden-Wochen im Sommer (nur mit Ausgleich nach Arbeitszeitgesetz) | ~18.800 € |
>
> Zwei Drittel davon bringt ein **Vollzeit-Sommerjob nach dem Abiturzeugnis**
> (28.06.–31.08.2027, 47 Arbeitstage). Am stärksten verschiebt das Ergebnis,
> was danach kommt: vor einem FH-Studium ab 01.10. bleibt der Sommerjob
> abgabenfrei (Median ~12.100 €), vor einem dualen Studium oder einer
> Ausbildung gehen ~21 % Sozialabgaben ab und der Sommer ist oft kürzer
> (Median ~9.500 €, bei Start am 01.08. ~8.200 €).

Gerechnet mit `python3 plan/verdienst_2027.py` (20.000 simulierte Verläufe):
Jede Phase bis August hat ein Stundenbudget, das das Abitur schützt; die
Stunden gehen an die Quelle mit dem höchsten erwarteten Erlös je Stunde,
begrenzt durch Nachfrage und die Regeln in Abschnitt 4.

## 1. Was jede Strategie bringt

| Strategie (netto bis 31.08.2027) | sicher (90 %) | Median | gut (10 %) | Spitze (1 %) |
|---|---:|---:|---:|---:|
| **beste Mischung (Plan unten)** | **8.200 €** | **10.700 €** | **13.100 €** | **14.400 €** |
| ohne Webgeschäft | 7.900 € | 10.400 € | 12.700 € | 13.900 € |
| nur kurzfristige Jobs (Ferien, Einsätze, Sommer) | 6.300 € | 8.800 € | 11.000 € | 12.100 € |
| nur Nebenjobs neben der Schule (kein Sommerjob) | 1.900 € | 2.600 € | 3.500 € | 4.200 € |

**Was danach kommt, entscheidet mit** (beste Mischung):

| Danach … | sicher (90 %) | Median | gut (10 %) |
|---|---:|---:|---:|
| FH-Studium ab 01.10. (Sommerjob sozialversicherungsfrei) | 10.500 € | 12.100 € | 13.600 € |
| duales Studium / Ausbildung, Start 01.09. | 8.900 € | 10.200 € | 11.400 € |
| duales Studium / Ausbildung, Start 01.08. (nur 25 Sommer-Arbeitstage, dafür August-Vergütung) | 7.200 € | 8.200 € | 9.300 € |
| Industrie-/Lagerjob im Sommer sicher (18–20 €/h) | 8.500 € | 11.200 € | 13.300 € |
| nur Mindestlohn-Jobs (14,60 €/h) | 7.700 € | 9.900 € | 11.700 € |
| ohne Ferienjob in den Weihnachts- und Frühjahrsferien | 6.700 € | 9.100 € | 11.100 € |

## 2. Woher das Geld kommt

| Quelle | Mittel im Plan | in der Obergrenze |
|---|---:|---:|
| Sommerjob nach dem Abitur (kurzfristig, 28.06.–31.08.) | 7.000 € | 9.250 € |
| Ferienjob in den Weihnachts- und Frühjahrsferien (14 Arbeitstage) | 1.800 € | 2.870 € |
| Nachhilfe (privat) | 1.330 € | – |
| Webgeschäft (`standortcheck`) | 1.120 € | 3.750 € |
| Einsätze am Wochenende (Event, Lager; kurzfristig) | 130 € | 1.690 € |
| August-Vergütung, falls die Ausbildung am 01.08. beginnt | 220 € | – |
| Minijob | 30 € | – |

Nachhilfe und Webgeschäft schlagen den Minijob, weil sie je Stunde mehr
bringen (Nachhilfe privat 15–30 €/h, Webgeschäft im Modell Median ~26 €
Umsatz je Stunde) und unter derselben Einkommensgrenze (Abschnitt 4) mit
weniger Lernzeit auskommen. In der Obergrenze verdrängt das Webgeschäft
die Nachhilfe, weil es dort am oberen Rand gerechnet ist.

## 3. Der Plan zum Maximum

| Wann | Was | Stunden |
|---|---|---|
| **bis 23.12.2026** | 2–4 Nachhilfeschüler (Mittel-/Oberstufe, 20–30 €/h) suchen; Webgeschäft mit `standortcheck` starten (Gewerbe 45 € in Regensburg) | 3–10 h/Woche |
| **Weihnachtsferien 24.12.–08.01.** | kurzfristiger Ferienjob (Lager, Event; ~18 €/h, z. B. über InStaff) an den 9 Arbeitstagen – wenn das Lernen es zulässt | Vollzeit |
| **Januar – März 2027** | Nachhilfe und Webgeschäft weiter; einzelne Wochenend-Einsätze; **Sommerjob jetzt sichern**: Ferienarbeit/Produktion bei Industriebetrieben (BMW, Krones, Infineon, Continental) oder über Zeitarbeitsfirmen (Randstad u. a.), Start 28.06. | 3–10 h/Woche |
| **Frühjahrsferien 08.–12.02.** | Ferienjob an 5 Arbeitstagen | Vollzeit |
| **22.03. – 25.06.2027** | Lernen und Prüfungen: schriftliches Abitur 21.04.–13.05., Kolloquium 31.05.–11.06., Zeugnis 25.06. Höchstens ein paar Nachhilfestunden | 0–6 h/Woche |
| **28.06. – 31.08.2027** | Vollzeit-Sommerjob, gern mit Schicht- und Nachtzulagen (steuerfrei nach § 3b EStG), Mo–Fr und einzelne Samstage | bis 48 h/Woche |
| **Frühjahr 2028** | Steuererklärung 2027: Die einbehaltene Lohnsteuer kommt zurück, solange der Jahreslohn unter ~13.600 € (Tarif 2026) bzw. ~14.000 € (Entwurf 2027) bleibt | – |

**Damit der Sommerjob abgabenfrei bleibt:**
- als **kurzfristige Beschäftigung** anmelden lassen – höchstens **70
  Arbeitstage im Kalenderjahr 2027**, Ferienjobs und Einsätze zählen mit;
- **nicht beim selben Arbeitgeber wie ein Minijob** (sonst wird es als eine
  Dauerbeschäftigung gewertet);
- sich nach dem Abitur **nicht als ausbildungsuchend melden** (dann gilt
  der Job als berufsmäßig);
- vor einem **dualen Studium, PiBS oder einer Ausbildung** ist der Job
  ohnehin berufsmäßig und sozialversicherungspflichtig (~21 % Abzug) –
  eingerechnet.

**Der Starttermin der Ausbildung ist ein Hebel:** Jeder Monat früher kostet
etwa 22 Sommer-Arbeitstage (~3.000 € brutto) und bringt dafür einen Monat
Vergütung (dual ~1.000–1.300 € brutto). Wer die Wahl hat, nimmt den
01.09. oder 01.10.

## 4. Was den Betrag begrenzt

| Regel | Wirkung |
|---|---|
| **Familienversicherung:** regelmäßiges Einkommen (Minijob, Nachhilfe, Webgeschäft) höchstens 565 € (2026) bzw. 590 € (2027) im Monat, bei nur einem Minijob 603 bzw. 633 € | Neben der Schule sind höchstens ~4.000–4.500 € drin; darüber käme eine eigene Krankenversicherung (~250–280 €/Monat) |
| **Kurzfristige Beschäftigung:** höchstens 3 Monate oder 70 Arbeitstage je Kalenderjahr, ohne Verdienstgrenze; zählt nicht zur Familienversicherung | trägt Ferien- und Sommerjobs; deckelt die Zahl der Arbeitstage |
| **Sozialversicherung:** frei, wenn danach ein Studium folgt; vor dualem Studium/Ausbildung berufsmäßig (~21,15 % Arbeitnehmeranteil 2026) | −1.500 bis −2.000 € im dualen Fall |
| **Arbeitszeitgesetz:** 8 h/Tag, bis 10 h; im Schnitt 48 h/Woche (Mo–Sa); 11 h Ruhezeit | Sommer höchstens ~450 Stunden |
| **Lohnsteuer:** Klasse I, kommt über die Steuererklärung zurück bis ~13.600 € Jahreslohn (2026) | im Plan fällt praktisch keine Steuer an |
| **Mindestlohn:** 13,90 € (2026), 14,60 € (2027); Zeitarbeit mind. 15,33 € bis 03/2027 und 15,87 € ab 04/2027 | Untergrenze jeder Stunde |
| **Kalender:** 47 Arbeitstage nach dem Zeugnis (25, wenn die Ausbildung am 01.08. beginnt) | der größte Einzelposten |

## 5. Was mehr bringen würde – und warum der Plan es nicht vorsieht

- **Mehr Stunden vor dem Abitur:** Jede zusätzliche Wochenstunde bringt
  ~15–25 €, kostet aber Lernzeit; Studien finden ab ~15–20 Stunden pro Woche
  schlechtere Noten. Die Abiturnote entscheidet über duale Plätze – und
  damit über viel mehr Geld als ein paar Hundert Euro.
- **Familienversicherung aufgeben**, um neben der Schule mehr regelmäßig zu
  verdienen: lohnt sich erst ab ~850 € im Monat, das ist mit den
  Lernstunden kaum zu schaffen.
- **60-Stunden-Wochen im Sommer:** rechtlich nur mit Ausgleich über
  6 Monate bzw. 24 Wochen, körperlich belastend; brächte ~1.500 € mehr
  (Obergrenze 18.800 statt 17.300 €).
- **Glücksspiel, Trading:** kein Erwirtschaften und im Schnitt ein Verlust
  (siehe [`500K_BIS_SOMMER_2027.md`](500K_BIS_SOMMER_2027.md)).

## 6. Was mit dem Geld passieren sollte

Nach der Sparregel des [Millionenplans](MILLIONENPLAN.md): 60 % von allem
über dem Grundbedarf in den Welt-ETF. Bei ~10.700 € und einem Grundbedarf
im Elternhaus von ~300–500 € im Monat sind das ~4.000–5.000 € fürs Depot
bis Ende August.

## 7. Grenzen dieser Rechnung

- Industrie-Ferienlöhne in Regensburg sind nur indirekt belegt (Randstad für
  BMW 18–20 €/h von 2024, InStaff Lager Ø 18,02 €, Metall-Tarif EG 1
  ~18,07 €/h); ob man einen solchen Platz bekommt, ist geschätzt (50–90 %).
- Die Nachfrage nach Nachhilfe (1–6 h/Woche) und die Chance, Schüler zu
  finden (60–95 %), sind geschätzt; die Werte des Webgeschäfts stammen aus
  dem eigenen, noch nicht gemessenen Modell (`plan/simulation.py`).
- Die Stundenbudgets neben der Schule (3–10 h/Woche, in der Prüfungszeit
  0–6) sind eine Vorgabe zum Schutz des Abiturs, keine Messung.
- Steuer mit dem Tarif 2026 gerechnet (2027 steigt der Grundfreibetrag
  voraussichtlich) – eher zu vorsichtig. Trinkgeld ist nicht eingerechnet.

## 8. Nachrechnen

```
python3 plan/verdienst_2027.py            # Abschnitte 1, 2 und Obergrenze
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
- InStaff Regensburg: Lager <https://www.instaff.jobs/lagerhelfer-kommissionierer-jobs/regensburg>,
  Service <https://www.instaff.jobs/service-kellner-jobs/regensburg>,
  Promotion <https://www.instaff.jobs/promotion-jobs/regensburg>
- Nachhilfe privat: <https://www.superprof.de/blog/der-richtige-stundenlohn-fuer-nachhilfe/>;
  Institute: <https://www.ulmato.de/ausbildung/nachhilfelehrer>
- Website-Preise für KMU: <https://sellwerk.de/wissenswert/was-kostet-eine-website>
- Plattformarbeit (ILO): <https://www.ilo.org/global/about-the-ilo/newsroom/news/WCMS_771909/lang--en/index.htm>

**Regeln**
- Geringfügigkeits-Richtlinien 2026 (Minijob, kurzfristige Beschäftigung,
  Berufsmäßigkeit, Ausbildungsuchende):
  <https://www.aok.de/fk/fileadmin/user_upload/jahreswechsel/2026/2026-geringfuegigkeits-richtlinien.pdf>
- Kurzfristige Beschäftigung (70 Tage): <https://www.minijob-zentrale.de/DE/die-minijobs/kurzfristige-beschaeftigung/kurzfristige-beschaeftigung_node.html>;
  nach dem Schulabschluss: <https://magazin.minijob-zentrale.de/kurzfristiger-minijob-nach-dem-schulabschluss/>
- Minijob-Abgaben: <https://www.minijob-zentrale.de/DE/fuer-gewerbetreibende/abgaben-und-steuern>
- Familienversicherung, Gesamteinkommen (vdek):
  <https://www.vdek.com/content/vdeksite/vertragspartner/mitgliedschaftsrecht_beitragsrecht/familienversicherung/_jcr_content/par/download_1642322223/file.res/Grundsaetzliche-Hinweise-Gesamteinkommen-29092022.pdf>;
  Grenzen 2027: <https://www.krankenkassen.de/gesetzliche-krankenkassen/system-gesetzliche-krankenversicherung/sozialversicherung-rechengroessen-beitragsbemessungsgrenze-versicherungspflichtgrenze/rechengroessen-2027/>
- Beitragssätze 2026 (TK): <https://www.tk.de/firmenkunden/versicherung/beitraege-faq-und-mehr/beitragssaetze/aktuelle-beitragssaetze-in-der-sozialversicherung-2031554>
- Lohnsteuer bei Ferienjobs (BdSt 2026): <https://steuerzahler.de/fileadmin/user_upload/LV_Baden-W%C3%BCrttemberg/BdSt_AN_News_fuer_Arbeitnehmer_Juli_2026_Ferienjob_NEU.pdf>;
  Entwurf 2027: <https://www.bundestag.de/presse/hib/kurzmeldungen-1221672>
- Arbeitszeitgesetz § 3: <https://dejure.org/gesetze/ArbZG/3.html>;
  steuerfreie Zuschläge § 3b EStG: <https://lxgesetze.de/estg/3b>
- Gewerbeanmeldung Regensburg: <https://www.firma.de/gewerbeamt/regensburg/>

**Kalender und Schule**
- Abiturtermine 2027 (BayMBl. 2025 Nr. 354): <https://www.verkuendung-bayern.de/baymbl/2025-354/>
- Ferien Bayern: <https://www.km.bayern.de/termine/ferien-und-feiertage>
- Ausbildungsbeginn (IHK München): <https://www.ihk-muenchen.de/de/berufsbildung-berufszugang/auszubildende/beratung/allgemeine-informationen/ausbildungsbeginn>
- Arbeitsstunden und Schulleistung: <https://pmc.ncbi.nlm.nih.gov/articles/PMC2926992>;
  SOEP/DIW: <https://www.diw.de/de/diw_01.c.10379.de/jobben_von_jugendlichen_beeintraechtigt_weder_schulleistungen_noch_freizeit.html>
