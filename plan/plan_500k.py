"""500.000 EUR bis 31.08.2027: das Muster der echten Fälle, Woche für Woche gerechnet.

Die belegten Fälle junger Gründer mit >= 500.000 in <= 12-18 Monaten (Cal AI,
Quittr, Summly, Roblox-Hits) folgen einem Muster: eine Consumer-App mit Abo
(KI-Utility, harte Paywall), Vertrieb über Kurzvideos und Creator, Werbung aus
dem laufenden Umsatz bezahlt, viele schnelle Versuche, Vermögen am Ende oft über
einen Verkauf. Dieses Modell rechnet genau diesen Weg für einen 18-Jährigen mit
höchstens ~5.000 EUR Einsatz und Abitur 2027 (Stundenbudget nach Kalender, Abitur
geschützt). Die ersten Szenarien nehmen Bayern und Programmierkenntnisse an; die
Szenarien „Deine Angaben“ rechnen mit den echten Angaben (Niedersachsen, keine
Programmierkenntnisse, Videos ohne Gesicht, Gesamtverlust einschließlich Auflösung
höchstens 5.000 EUR):

- mehrere Apps (Bau, App Review, Test mit Kurzvideos und Creatorn); die nächste App
  entsteht in den Stunden, die der Test der vorigen übrig lässt,
- je App eine latente Spitzen-MRR (Stufen 1k/10k/100k/1 Mio. USD, darüber Pareto;
  Fehlschläge rechtsschief nahe null wie bei RevenueCat),
- Wachstum eines Treffers bis zur Spitze, Plateau, Abfall, Risiko eines Einbruchs,
- Kosten (Creator inkl. Künstlersozialabgabe, später Paid Ads), Apple-Gebühr 15 % bzw. 30 %,
- Cashflow: Apple zahlt 5-9 Wochen später, Werbung ist nach 0-3 Wochen fällig. Ohne
  Kredit darf keine Ausgabe die Kasse unter die Reserve drücken; fehlt Geld, wird
  das Wachstum gedrosselt, notfalls die Werbung gekürzt (dann sinkt der Umsatz).
  Der US-Web-Checkout verkürzt den Verzug; ein Business Angel kann einen Treffer
  gegen Anteile finanzieren,
- Verkauf der App ab 16 Wochen Alter zum Vielfachen des Gewinns, abzüglich
  Transaktionskosten.

Ziel: Gewinn plus Verkaufserlös (Anteil des Gründers) >= 720.000 EUR bis 31.08.2027.
In einer UG bleiben davon nach ~30,7 % Steuer (KSt + Soli + GewSt bei ~425 % Hebesatz)
~500.000 EUR Eigenkapital; privat verfügbar wären ~965.000-980.000 EUR Gewinn nötig
(als UG wegen der 25-%-Rücklage ohne Kapitalerhöhung sogar ~1,3 Mio. EUR).

Regeln des Plans im Modell: Stunden nach dem Wochenplan (Abiturschutz) abzüglich
Partnersuche, Gründung und Sicherheitsnetz, Tests bis G3 zusammen höchstens 1.500 EUR,
Ausgaben nie unter die Reserve, kein Kredit, keine Fremdfinanzierung, Abbruch der Jagd
an den Toren G3 (28.02.: beste App < 5.000 USD MRR) und G4 (31.03.: < 10.000 USD),
danach keine neuen Versuche, kein Testbudget und nur noch Mindestkosten.

Verluste werden aus Sicht des Gründers gerechnet: Er bringt das ganze Geld ein, ein
Partner nur Arbeit; ihm gehört sein Anteil am Eigenkapital der UG.

Herkunft: Recherche-Runde zum 500k-Plan (Modell der Recherche, strengere
Kalibrierung und Lernkurve aus der Gegenprüfung, zwei Prüfrunden). B = belegt,
S = Schätzung.

Aufruf:

    python3 plan/plan_500k.py                 # Szenarien und Meilensteine (60.000 Läufe)
    python3 plan/plan_500k.py --n 300000      # wie im Dokument (auf 4 Kernen je Szenario einzeln
                                              # mit --nur starten: rund 20 Minuten)

Eingaben mit Quellen: docs/500K_BIS_SOMMER_2027.md.
"""
import math
import random
import sys
from datetime import date, timedelta

START = date(2026, 11, 30)          # Montag, Start Dezember 2026
END = date(2027, 8, 31)
WEEKS = (END - START).days // 7      # 39 volle Wochen bis 29.08.2027
WPM = 4.33                           # Wochen je Monat
FX = 0.87                            # EUR je USD (Schaetzung)


def tri(rng, lo, mode, hi):
    return rng.triangular(lo, hi, mode)


# ---------------------------------------------------------------------------
# Parameter (lo, mode, hi) = Dreiecksverteilung; B = belegt, S = Schaetzung
# ---------------------------------------------------------------------------
BASE = dict(
    start_cash=5000.0,                 # B (Angabe der Person)
    setup_cost=(600, 800, 1100),       # B/S: UG-Gruendung ~505-555 (Notar ~150-200, Handelsregister 300
                                       #      inkl. Bereitstellung, Gewerbe ~55), Website und Rechtstexte
                                       #      ~50-200, ggf. gebrauchtes Testgeraet 0-350
    fixed_month=(245, 320, 500),       # S: Werkzeuge (~100), Buchhaltung/Steuerberater anteilig
                                       #    (~1.500-3.000 EUR/Jahr = 125-250/Monat), Konto, IHK, Server
    fixed_stop=(145, 195, 280),        # S: nach Abbruch: UG-Pflichtkosten (Steuerberater 125-250/Monat),
                                       #    Apple-Konto ~7, IHK ~7, Konto
    # Arbeitsstunden je Woche nach Phase (S)
    h_school=(8, 15, 22),
    h_holiday=(20, 32, 45),
    h_abiprep=(3, 8, 15),
    h_abi=(0, 3, 8),
    h_oral=(5, 12, 20),
    h_gap=(15, 25, 40),
    h_full=(40, 55, 70),
    # Versuche
    n_attempts=(3, 8),                 # Aufgabe: 3-8 Apps (ganzzahlig gleichverteilt)
    build_first=(60, 100, 160),        # S: Stunden bis MVP inkl. Paywall/Onboarding
    build_next=(30, 55, 90),           # S: Lernkurve, Code-Wiederverwendung
    review_weeks=(0.3, 1.0, 3.0),      # S: App Review inkl. moeglicher Ablehnung
    test_hours=(30, 50, 80),           # S: 20-60 eigene Videos + Creator-Deals
    test_min_weeks=(2, 3, 5),          # S
    test_cost=(200, 500, 1200),        # S: Micro-Creator-Tests (Blake Anderson: 50 USD/Creator,
                                       #    Halo AI: 20 USD Probevideo; Cal AI: 2.000 USD 1. Story)
    test_cap=1500.0,                   # Plan: Tests bis G3 (28.02.) zusammen hoechstens 1.500 EUR,
                                       #       danach nur aus Umsatz (hoechstens Umsatz der letzten 4 Wochen)
    test_cap_bis=date(2027, 2, 28),    # Plan: Stichtag, bis zu dem Tests aus dem Startgeld bezahlt werden
    ksk=0.04,                          # B/S: Kuenstlersozialabgabe 2027 5,0 % auf Honorare an selbstaendige
                                       #      Creator (~80 % der Creator-Kosten an Privatpersonen)
    # Erfolgswahrscheinlichkeit je Versuch (Spitzen-MRR), mit Unsicherheit je Lauf
    p1k=(0.15, 0.25, 0.40),            # S, Basis RevenueCat 2026: 17,3 % neuer Apps >=1k in 2 J.
    p10k=(0.03, 0.07, 0.15),           # S, Basis RevenueCat 2026: 4,6 % >=10k in 2 J.
    q100k=(0.10, 0.20, 0.30),          # S, P(>=100k | >=10k); RevenueCat: ~25 % von 1k->10k
    q1m=(0.05, 0.12, 0.20),            # S, P(>=1M | >=100k)
    pareto_alpha=1.5,                  # S, Spitzen-MRR oberhalb 1 Mio USD
    flop_power=4.0,                    # B/S: Fehlschlag (< 1k USD) = 1.000 x u^4 USD MRR (Median ~60, Mittel
                                       #      200); RevenueCat 2025: Median-App < 50 USD/Monat nach 12 Monaten
    # Wachstum
    m0=(1000, 3000, 8000),             # S: MRR (USD) in den ersten Wochen eines Treffers
    g_demand=(1.5, 2.2, 3.0),          # S/B: Monatsfaktor; Cal AI 30k->100k->300k->500k->1M (M1-M6)
    h_need=(15, 25, 35),               # S: Stunden/Woche, die Skalierung braucht
    team_threshold=20000.0,            # S: ab 20k EUR MRR Freelancer/Creator-Manager
    team_hours=(10, 20, 40),           # S
    team_rate=(15, 18, 25),            # S: EUR je Helferstunde (Minijob mit Abgaben oder freie Mitarbeit),
                                       #    bezahlt werden nur genutzte Stunden, Einstellung erst nach G3
    plateau_weeks=(4, 10, 26),         # S
    decay_month=(0.02, 0.06, 0.15),    # S: RizzGPT 250k -> 150-200k MRR (B, Starter Story)
    p_kill=(0.05, 0.10, 0.20),         # S: Entfernung/Kopie/Plattformaenderung je Treffer
    kill_drop=(0.6, 0.75, 0.9),        # S
    # Kosten (Anteil am Bruttoumsatz, ohne Apple-Gebuehr)
    c_early=(0.30, 0.45, 0.65),        # S/B: Wachstum bis 100k USD MRR ueber eigenes UGC/Influencer;
                                       #      Blake Anderson: Marge UGC 50-80 %, Influencer 25-70 %
    c_growth=(0.55, 0.70, 0.85),       # S/B: Wachstum >100k USD MRR mit Paid Ads (Marge 0-30 %);
                                       #      CNBC: Cal AI "expenses nearly match revenue"
    cost_lag_weeks=(0, 1, 3),          # S: Creator zahlbar nach Posting, Kreditkarten-/Werbekonto-Ziel
    churn_stop=(0.05, 0.10, 0.15),     # S: Umsatzrueckgang je Woche ohne Werbung (Kuendigungen, keine
                                       #    Neukunden; Wochenabos kuendigen schneller als Jahresabos)
    c_plateau=(0.35, 0.47, 0.60),      # S/B: Umax ~5 Mio USD Umsatz, >100k USD/Monat Gewinn
    apple_low=0.15, apple_high=0.30,   # B: Small Business Program, 30 % ueber 1 Mio USD Proceeds
    apple_threshold_eur=870000.0,      # B: 1 Mio USD Proceeds je Kalenderjahr (x FX)
    # Cashflow
    apple_lag_weeks=(5, 7, 9),         # B/S: Zahlung ~33-45 Tage nach Ende des Fiskalmonats
    web_share=(0.0, 0.10, 0.30),       # S: Web-Checkout (Stripe) USA, Lag ~1 Woche
    web_net=(0.86, 0.89, 0.93),        # S/B: nach Stripe (int. Karten 3,25 % + 0,25 EUR, Umrechnung 2 %,
                                       #      Billing 0,7 %, Tax 0,5 %) bzw. Merchant of Record (~5 % + 0,50 USD)
    reserve=1000.0,                    # Plan: Ausgaben (Tests, Wachstum) nie unter diese Reserve; Tests
                                       #       zusaetzlich nur, wenn die Pflichtkosten bis 31.08. gedeckt bleiben
    credit0=(0, 0, 0),                 # Plan: kein Kredit (Zahlungsziele stecken in cost_lag_weeks)
    fin_weeks=(26, 26, 30),            # B: umsatzbasierte Finanzierung braucht >= 6 Monate Historie
    p_fin=(0.0, 0.0, 0.0),             # B: Silvr (jetzt Karmen) nur fuer Firmen in Frankreich, Pollen VC
                                       #    und Uncapped ohne RBF: fuer die junge UG keine Finanzierung
    fin_k=(0.5, 1.0, 2.0),             # S: Kreditrahmen in Monatsumsaetzen
    fin_fee_month=0.015,               # S
    # Exit
    exit_min_age_weeks=16,             # S: Kaeufer wollen mind. ~4 Monate Daten
    exit_multiple=(1.0, 2.0, 3.5),     # S/B: Flippa H1 2026 Apps 2,62x Jahresgewinn (Schnitt),
                                       #      FE Intl. 3,5-6x bei belegter Retention; Abschlag <1 J.
    exit_close_weeks=(4, 8, 14),       # B: FE Intl. 4-8 Wo. (<500k), 3-6 Mon. (1-10 Mio)
    p_close=(0.3, 0.5, 0.7),           # S
    deal_cost=(0.03, 0.05, 0.10),      # S: Makler, Anwalt, Due Diligence, Steuerberater (Anteil am Kaufpreis)
    angel=False,                       # Szenario: Business Angel / Pre-Seed bei Traktion
    angel_trigger_mrr=20000.0,         # S: ab 20k EUR MRR ueber 4 Wochen
    p_angel=(0.2, 0.4, 0.6),           # S
    angel_amount=(50000, 100000, 250000),  # S
    angel_dilution=(0.08, 0.15, 0.25),  # S
    angel_delay_weeks=(3, 6, 10),      # S
    profit_target=720000.0,
    stopps=(),                         # Tore: ((Datum, Schwelle USD MRR der besten App), ...)
    neu_stopp=(),                      # Messpunkte, unter denen nur neue Versuche enden (G5)
    nebenaufgaben=False,               # Plan: Stunden fuer Partnersuche, Gruendung, Sicherheitsnetz abziehen
    partnersuche=True,                 # False: bewusst allein, keine Stunden fuer die Partnersuche
    extra_fix_monat=(0, 0, 0),         # S: Zusatzkosten je Monat waehrend der Jagd (z. B. Claude-Abo, KI-Werkzeuge)
    p_faktor=(1.0, 1.0, 1.0),          # S: Faktor auf die Trefferquoten (z. B. Konkurrenz durch KI-Apps)
    einmal_stunden=(0, 0, 0),          # S: einmalige Einrichtung (z. B. Claude-Abläufe, Agenten), verteilt auf
                                       #    die ersten 8 Wochen
    pflege_h_woche=(0, 0, 0),          # S: laufende Pflege (z. B. Agenten prüfen) je Woche, solange die Jagd läuft
    agent_ab_start=False,              # Agent (und sein Abo) läuft ab Start; bei einem Treffer auch nach einem Tor weiter
    agent_bei_treffer=None,            # dict: Agent erst, wenn ein Treffer erkannt ist: h_need, einmal (Stunden über
                                       #       4 Wochen), extra_monat (EUR), pflege (h/Woche)
    partner_vertrag=(0, 0, 0),         # S: Notar/Anwalt fuer Partnervertrag (bei Zusage faellig)
    # ---- echte Angaben (November 2026): Niedersachsen, ohne Programmierkenntnisse, anonym ----
    kalender='BY',                     # 'BY' Bayern (fruehere Annahme) oder 'NI' Niedersachsen
    h_q4=(3, 5, 7),                    # Plan (NI): Q4 03.02.-18.03. hoechstens 6-7 h je Woche, in Wochen mit
                                       #            mehreren Klausuren nur Samstag 3 h
    neben='BY',                        # Nebenaufgaben des Wochenplans: 'BY' (frueher) oder 'NI' (ETH-Bewerbung)
    apple_ab=(0, 0, 0),                # S/B: Woche ab Start, ab der das Apple-Konto aktiv ist (UG: Notar,
                                       #      Register, D-U-N-S, Pruefung); vorher keine Einreichung
    abwicklung=(0, 0, 0),              # S/B: Kosten nach dem 31.08. fuer Aufloesung bzw. Abmeldung (EUR)
    m0_ohne_test=(1, 1, 1),            # S: Faktor auf den Startumsatz eines Treffers ohne bezahlten Test (Signal
                                       #    damit unsicher: auch ein Treffer kann unter der Schwelle starten)
    kein_testgeld=False,               # Gegenprobe: gar kein Testgeld, auch nicht aus Umsatz
    frei_ab=None,                      # Kalender NI: Montag nach der letzten eigenen Pruefung (Standard 07.06.)
    restwert=None,                     # dict(monate, p[, min_monat, min_alter_w, kosten, verkauf, stichtag,
                                       # uebertragung, anmeldung]): Wert laufender Apps nach dem 31.08.:
                                       # Monatsgewinn der letzten 4 Wochen x Monate, mit Wahrscheinlichkeit p
                                       # (Uebergabe an ein Elternteil, abzueglich kosten);
                                       # verkauf=dict(ab_umsatz_usd, min_alter_w, p, monate): zuerst Verkaufsversuch;
                                       # stichtag: entschieden wird mit dem Stand bis zu diesem Tag (nicht mit den
                                       # Augustzahlen); uebertragung: ab diesem Tag gehoeren die Erloese dem
                                       # Nachfolger; anmeldung=dict(am, ab_mrr_usd): das Elternteil meldet sich nur
                                       # an, wenn eine App am Messtag so viel MRR zeigt (sonst keine Uebergabe);
                                       # bleibt die Uebergabe dann aus, sind seine Kosten verloren (Geld der Familie)
    ferienjob=None,                    # dict(ab, netto_woche, max_app_h[, p, immer, frueh_ab, frueh_wenn, bis,
                                       # vorentscheid, zeitarbeit_p]):
                                       # Vollzeit-Ferienjob, sobald die Jagd an einem Tor beendet ist (kurzfristige
                                       # Beschaeftigung vor dem Studium); p = Chance, den Job zu bekommen;
                                       # immer=True: Job ab dem Datum auch ohne Tor (App nur noch abends);
                                       # frueh_ab: Stichtag am Vortag (ohne App im Store endet die Jagd dort, mit
                                       # oder ohne Job; der Job beginnt dann schon an diesem Tag); frueh_wenn=
                                       # 'eingereicht': nur ohne App im Store und ohne App im Review; bis: letzter
                                       # Arbeitstag nach dem Ende des Modells (Lohn fuer die Werktage ab 30.08.);
                                       # vorentscheid: Stand am Ende dieser Woche (App im Store oder im Review ->
                                       # dem Arbeitgeber den 19.07. genannt); ist dann am Stichtag trotzdem keine
                                       # App im Store, gibt es den fruehen Beginn nur mit der Chance zeitarbeit_p
                                       # (kurzfristig angefragte Zeitarbeit), sonst beginnt der Job am 19.07.;
                                       # zeitarbeit_vorlauf_p: ebenso ohne Nennung des 19.07. (im Vertrag steht der
                                       # 19.07., die zwei Wochen ab 05.07. gibt es nur ueber Zeitarbeit mit Vorlauf)
    fix_vor_start=None,                # (lo, mode, hi): Kosten je Monat zwischen Gruendung und erstem Start (noch
                                       # kein Server-Tarif, keine Build-Abos); danach gilt fixed_month
    stilllegung=None,                  # dict(verkauf_bis): Endet die Jagd ohne Verkauf oder Uebergabe, gehen alle
                                       # Abos an diesem Tag aus dem Verkauf (Apple: mindestens 31 Tage zwischen
                                       # Verkaufsstopp und Dienstende); Erloese danach entfallen
    fix_ruhe=None,                     # dict(von, bis, monat, max_h[, kosten_ab, nur_betrieb, monat_live]):
                                       # Ruhezeit (Abitur) ohne App im Store und ohne App im Review: Abos pausiert
                                       # (Kosten je Monat ab kosten_ab), hoechstens max_h je Woche; nur_betrieb:
                                       # mit App im Store oder im Review in diesen Wochen weder Bau noch Tests;
                                       # monat_live: dann mindestens diese Kosten je Monat (Supabase Pro)
    kv_grenze=None,                    # dict(monatsgewinn, beitrag): Einzelunternehmen; Gewinn ueber der Grenze
                                       # beendet die Familienversicherung (eigene Beitraege, privat)
    harte_grenze=False,                # Plan: freiwillige Ausgaben nur, solange danach alle Pflichtkosten bis
                                       #       31.08. UND die Aufloesung bezahlt sind (Gesamtverlust <= Einsatz)
    vorlage_h=None,                    # Stunden: App 2 beginnt erst, wenn App 1 freigegeben ist, aus der Vorlage
                                       # (diese Stunden kommen zum Bau von App 2 dazu); None: App 2 sofort
    vorlage_vorab_h=None,              # mit vorlage_h: so viele Stunden darf App 2 schon während des Reviews von
                                       # App 1 bekommen (Idee, SPEC, Texte, ohne Code); den Rest erst nach der Freigabe
    post_deckel=None,                  # (vor, nach): hoechstens so viele Stunden je Woche fuer Posts und Tests vor
                                       # dem Beginn der Pruefungszeit (Q4) und danach; der Rest baut weiter
    kasse_ab_gruendung=0.0,            # Stunden je Woche fuer die Kassenpruefung ab der Gruendung bis zum ersten
                                       # Start (danach steckt sie in pflege_h_woche)
    konten_je_einreichung=0.0,         # Stunden je Einreichung fuer Markenkonten und Featuring-Nominierung (in
                                       # den Wochen danach, nicht in der Ruhezeit)
    signal_pause=None,                 # (von, bis): Pruefungszeit fuer die Signal- und Creator-Regeln; Standard:
                                       # die Startpause (ohne Startpause gelten die Regeln dann trotzdem)
    c_organisch=None,                  # (lo, mode, hi): Anteil am Bruttoumsatz je App unter 5.000 USD MRR statt
                                       # c_early/c_plateau (Plan: keine Werbung aus dem Umsatz; Umsatzsteuer im
                                       # Preis, KI-API, Erstattungen); darueber gelten c_early/c_growth weiter
    vorb_nach_einreichung1=0.0,        # Stunden fuer die Vorbereitung der Posts (V1-V4) nach der Einreichung von
                                       # App 1 (in den Wochen danach, wie konten_je_einreichung)
)


def hours_level(d, lv, kalender='BY', frei_ab=None):
    """Arbeitsstunden-Phase der Woche, die am Montag d beginnt.

    kalender 'BY' (fruehere Annahme, Ferien Bayern 2026/27): Weihnachtsferien 24.12.2026-08.01.2027
    (die Woche ab 21.12. hat drei Schultage und drei Feiertage, sie zaehlt als Schulwoche),
    Fruehjahrsferien 08.-12.02.2027, Osterferien 22.03.-02.04., Pfingstferien 18.-28.05., Abitur bis
    Mitte Juni. kalender 'NI': siehe stunden_ni.
    """
    if kalender == 'NI':
        return stunden_ni(d, lv, frei_ab)
    if d < date(2026, 12, 28):
        return lv['h_school']
    if d < date(2027, 1, 11):
        return lv['h_holiday']
    if d < date(2027, 2, 8):
        return lv['h_school']
    if d < date(2027, 2, 15):
        return lv['h_holiday']
    if d < date(2027, 3, 22):
        return lv['h_school']
    if d < date(2027, 4, 19):
        return lv['h_abiprep']
    if d < date(2027, 5, 17):
        return lv['h_abi']
    if d < date(2027, 6, 14):
        return lv['h_oral']
    if d < date(2027, 6, 28):
        return lv['h_gap']
    return lv['h_full']


def stunden_ni(d, lv, frei_ab=None):
    """Arbeitsstunden der Woche ab Montag d nach dem Kalender Niedersachsen 2026/27 (B).

    Ferienordnung 2024/25-2029/30 (RdErl. MK 18.11.2022) und Abiturtermine 2027 (Bek. MK 28.04.2025):
    Weihnachtsferien Mi 23.12.2026-Sa 09.01.2027 (die Woche ab 21.12. hat zwei Schultage mit je 1 h,
    einen Ferientag und die freien Tage 24.-27.12.; Neujahr frei; der 06.01. ist in Niedersachsen kein
    Feiertag), Halbjahreszeugnis Fr 29.01., Halbjahresferien Mo 01.-Di 02.02. (zwei Ferientage, ab
    Mi 03.02. Q4), Q4 bis Do 18.03. mit je einer Klausur in jedem Fach (eigene Stufe h_q4; die Woche
    ab 15.03. mit den letzten Q4-Tagen zählt schon als Abiturvorbereitung), Osterferien
    22.03.-03.04., schriftliches Abitur 06.04.-13.05., Prüfung im 5. Fach und Nachschreibtermine
    19.05.-07.06. (die Woche ab 07.06. zählt als frei, der 07.06. kann noch Prüfungstag sein),
    danach frei bis auf mögliche Nachprüfungen 28.-30.06. und die Zeugnisse 01.-03.07.; Sommer
    ab 05.07.
    """
    if d < date(2026, 12, 21):
        return lv['h_school']
    if d < date(2026, 12, 28):
        # Mo/Di je 1 h Schulwoche, Mi 23.12. erster Ferientag, 24.-27.12. frei
        return 2 + (lv['h_holiday'] - 3) / 5
    if d < date(2027, 1, 4):
        # Neujahr (Fr 01.01.) frei: vier Ferientage und Samstag
        return 3 + (lv['h_holiday'] - 3) * 4 / 5
    if d < date(2027, 1, 11):
        return lv['h_holiday']
    if d < date(2027, 2, 1):
        return lv['h_school']
    if d < date(2027, 2, 8):
        # Mo/Di Halbjahresferien mit Ferienstunden, ab Mi 03.02. Q4
        return 2 * (lv['h_holiday'] - 3) / 5 + lv['h_q4']
    if d < date(2027, 3, 15):
        return lv['h_q4']
    if d < date(2027, 4, 5):
        return lv['h_abiprep']
    if d < date(2027, 5, 17):
        return lv['h_abi']
    if d < (frei_ab or date(2027, 6, 7)):
        return lv['h_oral']         # bis zum Montag nach der letzten eigenen Prüfung (5. Fach)
    if d < date(2027, 7, 5):
        return lv['h_gap']
    return lv['h_full']


def nebenstunden(d, mit_partner, partnersuche=True, variante='BY'):
    """Stunden der Woche ab Montag d, die nicht in Apps fließen (Wochenplan, Abschnitt 4).

    variante 'BY' (frühere Annahme): Partnersuche 2,5 h je Woche bis 31.01. (entfällt, sobald ein
    Partner zugesagt hat oder wer bewusst allein arbeitet), Gründung, Konten und Ideenvideos vor dem
    Bau ~10 h (KW 49/50), Sicherheitsnetz (Bewerbungen) 12 h in den Weihnachtsferien.
    variante als dict {Montag: Stunden}: die Nebenaufgaben des Wochenplans mit den echten Angaben
    (Gründung je nach Rechtsform, ETH-Bewerbung, Rückfall-Bewerbung), dazu wie oben die Partnersuche.
    """
    h = 0.0
    if isinstance(variante, dict):
        if d < date(2027, 2, 1) and not mit_partner and partnersuche:
            h += 2.5
        return h + variante.get(d, 0.0)
    if d < date(2027, 2, 1) and not mit_partner and partnersuche:
        h += 2.5
    if d < date(2026, 12, 14):
        h += 5.0
    if d in (date(2026, 12, 28), date(2027, 1, 4)):
        h += 6.0
    return h


def woche_ab(tag: date) -> int:
    """Modellwoche, die den Tag `tag` enthält."""
    return (tag - START).days // 7


def bis_woche(tag: date) -> int:
    """Letzte Modellwoche, die am Tag `tag` vollständig vorbei ist."""
    return ((tag - START).days + 1) // 7 - 1


def draw_peak(rng, p1k, p10k, q100k, q1m, alpha, flop_power=1.0):
    """Latente Spitzen-MRR in USD (Fehlschläge unter 1.000 USD: 1.000 x u^flop_power)."""
    u = rng.random()
    p100k = p10k * q100k
    p1m = p100k * q1m
    if u < p1m:
        x = 1e6 * (1 - rng.random()) ** (-1 / alpha)
        return min(x, 5e6)
    if u < p100k:
        return math.exp(rng.uniform(math.log(1e5), math.log(1e6)))
    if u < p10k:
        return math.exp(rng.uniform(math.log(1e4), math.log(1e5)))
    if u < p1k:
        return math.exp(rng.uniform(math.log(1e3), math.log(1e4)))
    return 1000.0 * rng.random() ** flop_power


def simulate(rng, P):
    t = lambda k: tri(rng, *P[k])
    # neue Parameter nur ziehen, wenn gesetzt (sonst bleibt der Zufallsstrom der bisherigen Szenarien gleich)
    t_neu = lambda k: tri(rng, *P[k]) if P[k][0] != P[k][2] else P[k][0]
    lv = {k: t(k) for k in ('h_school', 'h_holiday', 'h_abiprep', 'h_abi',
                            'h_oral', 'h_gap', 'h_full')}
    if P['kalender'] == 'NI':
        lv['h_q4'] = t('h_q4')          # Q4 mit Klausuren in jedem Fach (nur Kalender Niedersachsen)
    n_max = rng.randint(*P['n_attempts'])
    p1k, p10k, q100k, q1m = t('p1k'), t('p10k'), t('q100k'), t('q1m')
    _pf = t_neu('p_faktor')
    p1k, p10k = min(1.0, p1k * _pf), min(1.0, p10k * _pf)
    p1k = max(p1k, p10k)
    ksk = P['ksk']
    c_g, c_p, c_e = t('c_growth'), t('c_plateau') * (1 + ksk), t('c_early') * (1 + ksk)
    c_org = t_neu('c_organisch') if P['c_organisch'] else None   # Plan: unter 5.000 USD MRR keine Werbung aus dem Umsatz
    cost_lag = int(round(t('cost_lag_weeks')))
    cost_queue = []
    lag = int(round(t('apple_lag_weeks')))
    web = t('web_share')
    web_net = t('web_net')
    deal_cost = t('deal_cost')
    churn_stop = t('churn_stop')
    _fix_monat = t('fixed_month')
    extra_w = t_neu('extra_fix_monat') / WPM
    fixed_w = _fix_monat / WPM + extra_w
    einmal_rest = t_neu('einmal_stunden')
    einmal_w = einmal_rest / 8.0
    pflege_w = t_neu('pflege_h_woche')
    apple_ab = t_neu('apple_ab')        # vor dieser Woche keine Einreichung (Apple-Konto noch nicht aktiv)
    abw = t_neu('abwicklung')           # Aufloesung bzw. Abmeldung nach dem 31.08.
    ag_rest = 0.0
    AG = P.get('agent_bei_treffer')
    if AG:
        ag_h_need, ag_einmal = tri(rng, *AG['h_need']), tri(rng, *AG['einmal'])
        ag_extra_w, ag_pflege = tri(rng, *AG['extra_monat']) / WPM, tri(rng, *AG['pflege'])
    agent_aktiv = False
    credit0 = t('credit0')
    fin_weeks = t('fin_weeks')
    fin_ok = rng.random() < t('p_fin')
    fin_k = t('fin_k')
    h_need = t('h_need')
    team_h = t('team_hours')
    mult = t('exit_multiple')
    p_close = t('p_close')
    no_cash_limit = P.get('no_cash_limit', False)
    share = P.get('founder_share', 1.0)
    fixed_stop_w = t('fixed_stop') / WPM
    stopp_wochen = [(bis_woche(tag), schwelle * FX) for tag, schwelle in P['stopps']]
    neu_stopp_wochen = [(bis_woche(tag), schwelle * FX) for tag, schwelle in P['neu_stopp']]
    team_rate = t('team_rate')
    max_ueber = 0.0      # groesste Ueberschreitung des Budgets durch freiwillige Ausgaben (Pruefgroesse)
    g3_woche = bis_woche(P['test_cap_bis'])   # bis hierher Tests aus dem Startgeld (test_cap)
    sp = P.get('startpause')                   # (von, bis): kein Start in der Abiturzeit
    startpause = (woche_ab(sp[0]), woche_ab(sp[1])) if sp else None
    _spz = P.get('signal_pause') or sp         # Signal- und Creator-Regeln: Prüfungszeit (Standard: Startpause)
    sig_pause = (woche_ab(_spz[0]), woche_ab(_spz[1])) if _spz else None
    gestoppt = False
    stopp_woche = None
    best_mrr = 0.0      # hoechster Monatsumsatz (EUR) einer einzelnen App bisher
    # Partner mit Vertrieb: arbeitet ab Woche pw mit (Zusage bis spaetestens 31.01.)
    PP = P.get('partner')
    pw = None
    if PP:
        pw = rng.uniform(*P['partner_week'])
        pp = {k: tri(rng, *PP[k]) for k in ('p1k', 'p10k', 'q100k', 'q1m', 'c_early', 'team_hours')}
        pp['p1k'] = max(pp['p1k'], pp['p10k'])
        pp['c_early'] *= (1 + ksk)
    partner_vertrag = t('partner_vertrag') if PP else 0.0
    partner_bezahlt = False
    rev_share = P.get('partner_rev_share', 0.0)
    angel_state = None   # None | ('pending', week, amount, dil) | 'done' | 'no'
    weeks_over_20k = 0

    # Gruendung: sofort (bisherige Szenarien) oder erst, wenn App 1 zu einem Anteil gebaut ist
    # ("erst bauen, dann gruenden"); vorher fallen nur die Werkzeuge an, das Apple-Konto fehlt noch
    GR = P.get('gruendung')
    FJ = P['ferienjob']
    job_wochen = 0
    job_ok = rng.random() < tri(rng, *FJ['p']) if FJ and 'p' in FJ else True
    VS = P['fix_vor_start']
    vor_start_w = ((tri(rng, *VS) if VS[0] != VS[2] else VS[0]) / WPM + extra_w) if VS else None
    job_frueh = False
    stichtag_stopp = False
    RW = P['restwert']
    rw_stand = None      # (Monatsgewinn, (Umsatz der besten App, ihre Startwoche)) am Entscheidungstag
    eltern_konto = False  # Elternteil hat sich nach dem Messtag angemeldet (eigenes Gewerbe und Apple-Konto)
    abitur_h = 0.0       # Stunden für Bau und Tests in den Wochen der Ruhezeit (nur mit fix_ruhe, Prüfgröße)
    app1_frei = False    # App 1 ist von Apple freigegeben (mit vorlage_h beginnt App 2 erst danach)
    frei1_w = None       # Woche der Freigabe von App 1 (Prüfgröße)
    bau2_w = None        # Woche, in der der Bau von App 2 beginnt (Prüfgröße)
    konten_rest = 0.0    # offene Stunden für Markenkonten und Featuring nach einer Einreichung
    genannt_19 = False   # Vorentscheidung: App im Store oder im Review -> dem Arbeitgeber den 19.07. genannt
    post_max = 0.0       # größte Zahl an Post- und Teststunden in einer Woche (Prüfgröße)
    vorab_h = 0.0        # Stunden, die App 2 vor der Freigabe von App 1 bekommen hat (Vorbereitung ohne Code)
    FR = P['fix_ruhe']
    if FR:
        ruhe_w = (tri(rng, *FR['monat']) if FR['monat'][0] != FR['monat'][2] else FR['monat'][0]) / WPM
        ruhe = (woche_ab(FR['von']), woche_ab(FR['bis']))
        ruhe_kosten_ab = woche_ab(FR.get('kosten_ab', FR['von']))
    KV = P.get('kv_grenze')
    kv_kosten = 0.0
    kv_hist = []
    gr_rest = 0.0
    zu_teuer = False
    bh1 = None
    einreichung1 = None  # Woche, in der App 1 fertig gebaut ist (Einreichung, sobald das Apple-Konto aktiv ist)
    if GR:
        gr_setup = tri(rng, *GR['setup'])
        gr_apple = tri(rng, *GR['apple_dauer'])
        gr_vorher_w = tri(rng, *GR['fix_vorher']) / WPM
        gegruendet = False
        gruendung_woche = None
        apple_ab = float(WEEKS + 99)
        cash = P['start_cash']
    else:
        gegruendet = True
        gruendung_woche = 0
        cash = P['start_cash'] - t('setup_cost')
    profit = -(P['start_cash'] - cash)  # Gruendungskosten als Aufwand
    nachschuss = 0.0     # privates Geld, das der Gruender nachlegen muss, wenn die Kasse leer ist
    angel_geld = 0.0     # Einlage eines Business Angels (Eigenkapital, kein Gewinn)
    min_kasse = cash
    testkosten_g3 = 0.0
    test_log = []        # (Woche, Testkosten) je gestarteter App
    bau_nach_stopp = 0
    apps = []
    attempts = 0
    bau = None       # [Reststunden, Versuchsnummer] der App im Bau
    reviews = []     # [Restwochen, Versuchsnummer] je App im App Review
    tests = []       # [Reststunden, Restwochen, App-Index] je App im Test
    focus = False
    rev_hist = []        # (Bruttoumsatz, Apple-Erloes) je Woche (EUR)
    profit_hist = []
    deckung_hist = []    # Wochenergebnis vor Fixkosten (Erlös minus umsatzabhängige Kosten)
    cum_proceeds_year = 0.0
    weeks_over_10k = 0
    cash_squeeze = 0
    exit_state = None    # None | ('listing', close_week, value) | ('done', value)
    exit_value = 0.0
    relist_after = -1
    first10k_week = None
    first100k_week = None
    max_mrr = 0.0
    chk = {}

    def pflicht_bis_ende(wk):
        """Pflichtkosten der gegründeten Firma von Woche wk bis 31.08. (bis zum nächsten Tor voll)."""
        naechstes = next((sw + 1 for sw, _ in stopp_wochen if sw + 1 > wk), None)
        if gestoppt:
            return (WEEKS - wk) * fixed_stop_w
        if naechstes is None:
            return (WEEKS - wk) * fixed_w
        return (naechstes - wk) * fixed_w + (WEEKS - naechstes) * fixed_stop_w

    def gruenden_erlaubt(wk):
        """Ist M2 bis zur Woche ab spaet[0] nicht erreicht, wird erst ab der Woche ab spaet[1] gegründet (am Tag
        nach der letzten Prüfung, 03, Abschnitt 5)."""
        SPG = GR.get('spaet') if GR else None
        return not (SPG and woche_ab(SPG[0]) < wk < woche_ab(SPG[1]))

    def gruenden(wk):
        """Gründung in Woche wk: Kosten, Stunden, Wartezeit bis zum aktiven Apple-Konto."""
        nonlocal cash, profit, gegruendet, apple_ab, gr_rest, gruendung_woche, zu_teuer
        if P['harte_grenze'] and gr_setup + pflicht_bis_ende(wk) + abw > cash - sum(c for (_, c) in cost_queue):
            # Pflichtkosten und Auflösung passten nicht mehr in den Einsatz: nicht gründen
            zu_teuer = True
            return False
        cash -= gr_setup
        profit -= gr_setup
        gegruendet = True
        apple_ab = wk + gr_apple
        gr_rest = GR['stunden']
        gruendung_woche = wk
        return True

    for w in range(WEEKS):
        d = START + timedelta(weeks=w)
        if d.year == 2027 and (d - timedelta(weeks=1)).year == 2026:
            cum_proceeds_year = 0.0
        if exit_state and exit_state[0] == 'done':
            break
        mit_partner = pw is not None and w >= pw
        hours = hours_level(d, lv, P['kalender'], P['frei_ab']) * rng.uniform(0.8, 1.2)
        if P['nebenaufgaben']:
            hours = max(0.0, hours - nebenstunden(d, mit_partner, P.get('partnersuche', True), P['neben']))
        # Ruhezeit (Abitur): ohne App im Store oder im Review ruhen die Abos, gebaut wird nicht
        in_ruhe = bool(FR) and ruhe[0] <= w < ruhe[1] and not gestoppt and not focus and not apps and not reviews
        if in_ruhe:
            hours = min(hours, FR['max_h'])
        if konten_rest > 1e-9 and not in_ruhe:
            # Markenkonten und Featuring-Nominierung nach einer Einreichung (05, Abschnitt 1.1)
            use = min(hours, konten_rest)
            hours -= use
            konten_rest -= use
        if einmal_rest > 1e-9:
            # Einrichtung in den ersten 8 Wochen; was dort keinen Platz fand, wird nachgeholt
            use = min(hours, einmal_rest, einmal_w if w < 8 else einmal_rest)
            hours -= use
            einmal_rest -= use
        _akt = max((a['R'] for a in apps), default=0.0) * WPM
        tor_stoppt = not gestoppt and any(w == sw + 1 and _akt < sch for sw, sch in stopp_wochen)
        # später Fall: am Tag nach der letzten Prüfung gründen, parallel zum restlichen Bau (03, Abschnitt 5)
        spaet_jetzt = bool(GR) and bool(GR.get('spaet')) and w >= woche_ab(GR['spaet'][1])
        if GR and not gegruendet and not zu_teuer and not tor_stoppt and bau is not None and bau[1] == 1 \
                and bh1 and (bh1 - bau[0] >= GR['bei'] * bh1 or spaet_jetzt) and gruenden_erlaubt(w):
            if not gruenden(w):
                bau = None                  # ohne bezahlbare Firma kein Start: Versuch endet
                attempts -= 1
                n_max = attempts
        if gr_rest > 1e-9:
            # Gründungsaufgaben (Notar, Konto, Anmeldungen, Apple) über mindestens zwei Wochen
            use = min(hours, gr_rest, GR['stunden'] / 2)
            hours -= use
            gr_rest -= use
        agent_laeuft = agent_aktiv or (P['agent_ab_start'] and focus)
        if apps and (not gestoppt or agent_laeuft):
            hours = max(0.0, hours - pflege_w)
        elif P['kasse_ab_gruendung'] and gegruendet and not gestoppt and not in_ruhe:
            hours = max(0.0, hours - P['kasse_ab_gruendung'])   # Kassenprüfung ab der Gründung (03, 7.3)
        if mit_partner and not partner_bezahlt:
            # Notar/Anwalt fuer Gesellschaftervereinbarung bzw. Kooperationsvertrag
            cash -= partner_vertrag
            profit -= partner_vertrag
            partner_bezahlt = True
        # ---------------- Tore: Abbruch der Jagd ----------------
        aktuell = max((a['R'] for a in apps), default=0.0) * WPM   # Stand am Ende der Vorwoche
        for sw, schwelle in neu_stopp_wochen:
            if w == sw + 1 and aktuell < schwelle:
                n_max = min(n_max, attempts)       # keine neuen Versuche, ein laufender Bau wird fertig
        for sw, schwelle in stopp_wochen:
            if w == sw + 1 and aktuell < schwelle and not gestoppt:
                gestoppt = True
                stopp_woche = w
                if bau is not None:
                    bau = None
                    attempts -= 1           # abgebrochener Bau zaehlt nicht als Versuch
                n_max = attempts            # keine neuen Versuche
        if FJ and FJ.get('frueh_ab') and not gestoppt and not apps and w == woche_ab(FJ['frueh_ab']) \
                and not (FJ.get('frueh_wenn') == 'eingereicht' and reviews):
            # Stichtag (Vortag): noch keine App im Store -> die Jagd endet (keine neue App mehr), mit oder ohne Job;
            # eine eingereichte App darf noch erscheinen. Mit Job beginnt er schon an diesem Tag.
            gestoppt = True
            stopp_woche = w
            stichtag_stopp = True
            job_frueh = job_ok
            if job_ok:
                # Im Vertrag steht der 19.07. (06, 2.4): die zwei Wochen ab 05.07. gibt es nur über Zeitarbeit, kurzfristig
                # angefragt (19.07. genannt, 06, 2.10) oder mit Vorlauf (Anfrage Mo 21.06., Festlegung Fr 25.06.);
                # klappt das nicht, gehören sie Zürich, Mathe und der eingereichten App
                p_za = FJ.get('zeitarbeit_p') if genannt_19 else FJ.get('zeitarbeit_vorlauf_p')
                if p_za:
                    job_frueh = rng.random() < tri(rng, *p_za)
            if bau is not None:
                bau = None
                attempts -= 1
            n_max = attempts
        if FJ and job_ok and (gestoppt or FJ.get('immer')) and d >= (FJ['frueh_ab'] if job_frueh else FJ['ab']):
            # Jagd beendet (oder Job hat Vorrang): Vollzeit-Ferienjob, für die Apps bleiben wenige Stunden je Woche
            job_wochen += 1
            hours = min(hours, FJ['max_app_h'])
        if gegruendet:
            fix_basis = fixed_stop_w if gestoppt else fixed_w
            if VS and not gestoppt and not apps:
                fix_basis = min(fix_basis, vor_start_w)      # vor dem ersten Start: nur Claude, Domain, Nummer
        else:
            fix_basis = 0.0 if gestoppt else gr_vorher_w + extra_w   # nur Werkzeuge (Claude)
        if in_ruhe and w >= ruhe_kosten_ab:
            fix_basis = min(fix_basis, ruhe_w)      # Abos pausiert (Claude Pro erst nach dem bezahlten Monat)
        elif FR and FR.get('monat_live') and ruhe[0] <= w < ruhe[1] and gegruendet \
                and (apps or any(rv[0] > 0 for rv in reviews)):
            # App im Store oder im Review: Server auf dem bezahlten Tarif (die Wachregel geht im Abitur nicht)
            fix_basis = max(fix_basis, FR['monat_live'] / WPM + extra_w)
        if gestoppt and agent_laeuft:
            # Treffer nach dem Tor: Abo für den Agenten läuft weiter
            fix_basis += ag_extra_w if agent_aktiv else extra_w
        # ---------------- App-Arbeit (neue Versuche) ----------------
        mrr_now = sum(a['R'] for a in apps) * WPM
        if mit_partner:
            team = pp['team_hours']
        else:
            team = team_h if (mrr_now >= P['team_threshold'] and w > g3_woche) else 0.0
        c_e_w = pp['c_early'] if mit_partner else c_e
        h_free = hours + (team if mit_partner else 0.0)
        hit = [a for a in apps if a['peak'] * FX >= 50000 and a['revealed']]
        if hit:
            focus = True
        if AG and focus and not agent_aktiv:
            # Treffer erkannt: jetzt erst Max/Ultra und Agent einrichten
            agent_aktiv = True
            ag_rest = ag_einmal
            fixed_w += ag_extra_w
            pflege_w += ag_pflege
        if agent_aktiv and ag_rest > 1e-9:
            # höchstens ein Viertel der Einrichtung je Woche, Rest in den Folgewochen; erst danach wirkt der Agent
            use = min(hours, ag_rest, ag_einmal / 4.0)
            hours -= use
            ag_rest -= use
            if ag_rest <= 1e-9:
                h_need = min(h_need, ag_h_need)      # der Agent senkt den Bedarf, erhöht ihn nie
        # Effort-Faktor fuer das Wachstum grosser Apps: Skalieren braucht h_need Stunden je Woche,
        # ob die App schon als Treffer erkannt ist oder nicht
        eff = min(1.0, (hours + team) / h_need)
        helfer_kosten = 0.0
        if not mit_partner and team > 0 and (
                focus or any(a['peak'] * FX >= 50000 and a['phase'] == 'grow' for a in apps)):
            # Helfer arbeiten am Wachstum einer großen App: bezahlt werden die genutzten Stunden
            helfer_kosten = min(team, max(0.0, h_need - hours)) * team_rate
        if focus:
            # Gruender skaliert den Treffer, keine neuen Apps
            h_free = 0.0
        if FR and FR.get('nur_betrieb') and ruhe[0] <= w < ruhe[1] and not in_ruhe:
            # Abitur mit App im Store oder im Review: nur Zahlen, Notfälle, Antworten an das Review;
            # kein Bau, keine Posts (die Stunden fließen weder in Tests noch in die nächste App)
            h_free = 0.0
        h_start = h_free
        if not focus:
            # 1. Testarbeit (Videos, Creator) für gestartete Apps hat Vorrang, mit post_deckel nur bis zum
            #    Wochendeckel des Plans (05, 6.1/6.2: vor dem Abitur ein Samstagsblock, im Sommer höchstens 10 h)
            PD = P['post_deckel']
            rest = None if not PD else (PD[0] if sig_pause and w < sig_pause[0] else PD[1])
            h_vor_tests = h_free
            for tst in tests:
                use = min(h_free, tst[0]) if rest is None else max(0.0, min(h_free, tst[0], rest))
                tst[0] -= use
                h_free -= use
                if rest is not None:
                    rest -= use
            post_max = max(post_max, h_vor_tests - h_free)
            # 2. Übrige Stunden bauen die nächste App, auch während Review und Test der vorigen
            while h_free > 0:
                if bau is None:
                    if attempts >= n_max:
                        break
                    if P['vorlage_h'] is not None and attempts >= 1 and not (
                            app1_frei or any(rv[1] == 1 and rv[0] <= 1.0 for rv in reviews)) and not (
                            P['vorlage_vorab_h'] and attempts == 1 and any(rv[1] == 1 for rv in reviews)):
                        break   # App 2 erst nach der Freigabe von App 1, aus der Vorlage (02, Abschnitt 9; 06, KW 24)
                    attempts += 1
                    if gestoppt:
                        bau_nach_stopp += 1
                    if mit_partner:
                        bh = tri(rng, *PP['build_next'])
                    else:
                        bh = t('build_first') if attempts == 1 else t('build_next')
                        if attempts == 1:
                            bh1 = bh
                        elif attempts == 2 and P['vorlage_h']:
                            bh += P['vorlage_h']        # Vorlage ziehen, Review-Log einarbeiten (3-4 h)
                    if attempts == 2:
                        bau2_w = w
                    bau = [bh, attempts]
                vorab = P['vorlage_h'] is not None and P['vorlage_vorab_h'] and bau[1] == 2 and not (
                    app1_frei or any(rv[1] == 1 and rv[0] <= 1.0 for rv in reviews))
                use = min(h_free, bau[0], max(0.0, P['vorlage_vorab_h'] - vorab_h)) if vorab else min(h_free, bau[0])
                bau[0] -= use
                h_free -= use
                if vorab:
                    vorab_h += use
                    if bau[0] > 0:
                        break       # vor der Freigabe nur Vorbereitung; der Rest der Woche geht nicht in App 2
                if bau[0] <= 0:
                    if GR and not gegruendet and not gruenden_erlaubt(w):
                        break                       # fertig, gegründet wird erst nach der letzten Prüfung
                    if GR and not gegruendet and not gruenden(w):
                        bau = None                  # ohne bezahlbare Firma kein Start
                        attempts -= 1
                        n_max = attempts
                        break
                    # Einreichung im Lauf der Woche: das Review zählt ab der Folgewoche; ist das
                    # Apple-Konto noch nicht aktiv, wartet die fertige App bis dahin
                    if bau[1] == 1:
                        einreichung1 = max(float(w), apple_ab)
                    reviews.append([t('review_weeks') + 1.0 + max(0.0, apple_ab - w), bau[1]])
                    konten_rest += P['konten_je_einreichung']
                    if bau[1] == 1:
                        konten_rest += P['vorb_nach_einreichung1']   # V1-V4 vor dem ersten Post (05, Abschnitt 4)
                    bau = None
                else:
                    break
        if FR and ruhe[0] <= w < ruhe[1]:
            abitur_h += h_start - h_free         # Stunden für Bau und Tests in den Abiturwochen (Prüfgröße)
        # Review-Zeit laeuft kalendarisch
        fertig = []
        in_pause = startpause is not None and startpause[0] <= w < startpause[1]
        for rv in reviews:
            rv[0] -= 1.0
            if rv[0] <= 0 and rv[1] == 1 and not app1_frei:
                app1_frei = True            # freigegeben (in der Startpause noch nicht veröffentlicht)
                frei1_w = w
            if rv[0] <= 0 and not in_pause:
                fertig.append(rv)          # in der Startpause bleibt eine freigegebene App unveröffentlicht
        def testgeld(wunsch):
            """Testgeld, das diese Woche höchstens ausgegeben werden darf (Deckel, Reserve, Pflichtkosten)."""
            if w <= g3_woche:
                deckel = max(0.0, P['test_cap'] - testkosten_g3)
            else:
                # nur aus Umsatz: Umsatz der letzten 4 Wochen minus Tests, die schon daraus bezahlt sind
                deckel = max(0.0, sum(g for (g, _) in rev_hist[-4:])
                             - sum(c for (ww, c) in test_log if ww > max(w - 4, g3_woche)))
            # Reserve fuer Tests: mindestens 1.000 EUR und alle Pflichtkosten bis 31.08.
            # (bis zum naechsten Tor volle Fixkosten, danach die nach einem Abbruch;
            # ohne weiteres Tor laufen die vollen Fixkosten bis zum Ende)
            naechstes = next((sw + 1 for sw, _ in stopp_wochen if sw + 1 > w), None)
            if naechstes is None:
                pflicht = (WEEKS - w) * fixed_w
            else:
                pflicht = (naechstes - w) * fixed_w + (WEEKS - naechstes) * fixed_stop_w
            frei = cash - max(P['reserve'], pflicht + (abw if gegruendet else 0.0)) + credit0 - sum(c for (_, c) in cost_queue)
            return max(0.0, min(frei, wunsch, deckel))

        SIG = P.get('signal')
        if SIG:
            # Testgeld erst, wenn eine App ohne bezahlte Werbung ein Signal zeigt (Monatsumsatz nach x Wochen)
            sig_in_pause = sig_pause is not None and sig_pause[0] <= w < sig_pause[1]
            for a in apps:
                if a.get('signal_w') == w:
                    if sig_in_pause:
                        a['signal_w'] = sig_pause[1]    # in der Prüfungszeit erst ab ihrem Ende buchen
                        continue
                    a['signal_w'] = None
                    bestanden = a.pop('bestanden', False)
                    if SIG.get('creator_nach_pause') and not bestanden and sig_pause and w < sig_pause[0] \
                            and not gestoppt and a['R'] * WPM >= SIG['schwelle_usd'] * FX:
                        # vor der Prüfungszeit bestanden: zählt, Creator aber erst nach der letzten Prüfung
                        a['signal_w'] = sig_pause[1]
                        a['bestanden'] = True
                        continue
                    zweite = SIG.get('zweite')      # zweite Prüfung für Apps, die vor der Startpause starteten
                    if zweite and not bestanden and sig_pause and a['launch'] < sig_pause[0] \
                            and w < woche_ab(zweite) and a['R'] * WPM < SIG['schwelle_usd'] * FX:
                        a['signal_w'] = woche_ab(zweite)   # vor dem Abitur zu wenige Posts für ein Urteil
                        continue
                    if not gestoppt and a['phase'] != 'decay' and (bestanden or a['R'] * WPM >= SIG['schwelle_usd'] * FX):
                        cost = testgeld(a['wunsch'])
                        if cost >= 100:
                            if w <= g3_woche:
                                testkosten_g3 += cost
                            test_log.append((w, cost))
                            cash -= cost
                            profit -= cost
                            # Spitze wiederhergestellt, mit Abschlag für die verlorenen Wochen
                            abschlag = tri(rng, *SIG['abschlag']) if 'abschlag' in SIG else 1.0
                            a['peak'] = max(a['peak'], a['latent'] * abschlag)
                            if a['phase'] == 'plateau':
                                a['phase'] = 'grow'
        for rv in fertig:
            reviews.remove(rv)
            versuch = rv[1]
            wunsch = t('test_cost') * (1 + ksk)
            if gestoppt or SIG or P['kein_testgeld']:
                cost = 0.0                      # nach dem Tor kein Testbudget; mit Signalregel erst später
            else:
                cost = testgeld(wunsch)
            if w <= g3_woche:
                testkosten_g3 += cost
            test_log.append((w, cost))
            cash -= cost
            profit -= cost
            if mit_partner:
                # Partner bringt Playbook und Creator-Netzwerk: eigene Quoten, keine Lernkurve
                peak = draw_peak(rng, pp['p1k'], pp['p10k'], pp['q100k'], pp['q1m'], P['pareto_alpha'],
                                 P['flop_power'])
            else:
                _lf = P.get('learn'); _f = _lf[min(versuch - 1, len(_lf) - 1)] if _lf else 1.0
                peak = draw_peak(rng, p1k * _f, p10k * _f, q100k, q1m, P['pareto_alpha'], P['flop_power'])
            erzwungen = versuch == P.get('force_attempt', 1)
            if erzwungen and P.get('force_first_peak'):
                peak = P['force_first_peak']
            latent = peak
            if cost < 100:
                peak *= 0.5
            if erzwungen and P.get('force_m0'):
                m0 = min(peak, P['force_m0'])
            elif mit_partner:
                m0 = min(peak, tri(rng, *PP['m0']))
            else:
                m0 = min(peak, t('m0'))
            R0 = m0 * FX / WPM if peak >= 1000 else peak * FX / WPM
            if cost < 100:
                R0 *= t_neu('m0_ohne_test')     # ohne bezahlten Test startet auch ein Treffer schwächer
            apps.append(dict(peak=peak, R=R0,
                             g=(P['force_g'] if (erzwungen and P.get('force_g')) else t('g_demand')),
                             launch=w, phase='grow',
                             plateau=t('plateau_weeks'), decay=t('decay_month'),
                             killw=(w + rng.randint(4, 40)) if rng.random() < t('p_kill') else None,
                             kdrop=t('kill_drop'), revealed=False, test_end=None))
            if SIG:
                apps[-1].update(latent=latent, wunsch=wunsch,
                                signal_w=(w + SIG['wochen']) if not gestoppt else None)
            tests.append([t('test_hours'), t('test_min_weeks'), len(apps) - 1])
        for tst in list(tests):
            tst[1] -= 1.0
            if tst[0] <= 0 and tst[1] <= 0:
                apps[tst[2]]['revealed'] = True
                tests.remove(tst)
        # ---------------- Umsatzdynamik ----------------
        planned = []
        for a in apps:
            if a['launch'] == w:
                planned.append(a['R'])
                continue
            R = a['R']
            if a['phase'] == 'grow':
                gw = a['g'] ** (1 / WPM)
                e = eff if a['peak'] * FX >= 50000 else 1.0
                gw = 1 + (gw - 1) * e
                Rn = min(R * gw, a['peak'] * FX / WPM)
                if Rn >= a['peak'] * FX / WPM * 0.999:
                    a['phase'] = 'plateau'
                    a['pl_left'] = a['plateau']
            elif a['phase'] == 'plateau':
                Rn = R
                a['pl_left'] -= 1
                if a['pl_left'] <= 0:
                    a['phase'] = 'decay'
            else:
                Rn = R * (1 - a['decay']) ** (1 / WPM)
            if a['killw'] is not None and w == a['killw']:
                Rn *= (1 - a['kdrop'])
                a['phase'] = 'decay'
            planned.append(Rn)
        # Kosten und Cash-Limit
        fix_w = fix_basis + helfer_kosten
        grow_mask = [a['phase'] == 'grow' for a in apps]
        rs = rev_share if mit_partner else 0.0

        def rate(Rn, gm):
            if c_org is not None and Rn * WPM < 5000 * FX:
                return c_org        # Plan: keine Werbung aus dem Umsatz (06, Abschnitt 3: von 1 EUR bleiben ~0,71 EUR)
            if not gm:
                return c_p
            return c_e_w if Rn * WPM < 100000 * FX else c_g

        def kosten(pl, erhalt=None):
            """Variable Kosten (ohne Umsatzanteil); erhalt[i]: App i nur mit Erhaltungssatz."""
            sp = 0.0
            for i, (Rn, gm) in enumerate(zip(pl, grow_mask)):
                r = rate(Rn, gm)
                sp += Rn * (min(c_p, r) if (erhalt and erhalt[i]) else r)
            return sp
        spend = kosten(planned)
        cost_plan = spend + rs * sum(planned) + fix_w
        # Zufluss dieser Woche
        inflow = 0.0
        if len(rev_hist) >= lag:
            inflow += rev_hist[-lag][1]          # Apple-Erlös (schon ohne Web-Anteil und Gebühr)
        if rev_hist:
            inflow += rev_hist[-1][0] * web * web_net
        mrr_eur = sum(planned) * WPM
        if mrr_eur >= 10000:
            weeks_over_10k += 1
        floor = P['reserve'] - credit0
        if P['harte_grenze']:
            # Werbung nur, solange danach alle Pflichtkosten bis 31.08. und die Aufloesung bezahlt sind
            naechstes = next((sw + 1 for sw, _ in stopp_wochen if sw + 1 > w), None)
            if gestoppt or naechstes is None:
                pflicht_rest = (WEEKS - w) * fix_basis
            else:
                pflicht_rest = (naechstes - w) * fixed_w + (WEEKS - naechstes) * fixed_stop_w
            floor = max(floor, pflicht_rest + (abw if gegruendet else 0.0) - credit0)
        if fin_ok and weeks_over_10k >= fin_weeks:
            floor -= fin_k * mrr_eur
        # Die Kosten dieser Woche werden nach cost_lag Wochen fällig. Bis dahin zählen nur sichere
        # Zuflüsse: Apple-Erlöse vergangener Wochen, die in diesen Wochen ausgezahlt werden.
        n_h = len(rev_hist)
        sicher = sum(rev_hist[n_h - lag + k][1] for k in range(1, cost_lag + 1) if 0 <= n_h - lag + k < n_h)
        offen = sum(c for (_, c) in cost_queue)            # alle bis dahin fälligen alten Kosten
        budget = cash + inflow + sicher - offen - floor
        if not no_cash_limit and cost_plan > budget:
            cash_squeeze += 1
            # 1. Wachstum nur so weit, wie das Geld reicht: gedrosselte Apps wachsen um den Anteil f,
            #    der Rest ihres Umsatzes kostet nur den Erhaltungssatz
            gedrosselt = [grow_mask[i] and a['launch'] != w and planned[i] > a['R'] for i, a in enumerate(apps)]
            flach = [a['R'] if gedrosselt[i] else planned[i] for i, a in enumerate(apps)]
            k_flach = kosten(flach, gedrosselt) + rs * sum(flach) + fix_w
            if k_flach <= budget:
                f_w = (budget - k_flach) / (cost_plan - k_flach) if cost_plan > k_flach else 0.0
                planned = [fl + f_w * (pl - fl) for fl, pl in zip(flach, planned)]
                cost_plan = k_flach + f_w * (cost_plan - k_flach)
                max_ueber = max(max_ueber, cost_plan - budget)
            else:
                planned = flach
                # 2. Nur Erhaltungsbudget für alle Apps
                alle = [True] * len(apps)
                spend = kosten(planned, alle)
                cost_plan = spend + rs * sum(planned) + fix_w
                if cost_plan <= budget:
                    max_ueber = max(max_ueber, cost_plan - budget)
                else:
                    # 3. Werbung auf das Verfügbare kürzen (Anteil k); ohne Werbung kommen keine
                    #    Neukunden, der Umsatz sinkt um churn_stop je Woche (S)
                    tot = sum(planned)
                    z = budget - fix_w - rs * tot * (1 - churn_stop)
                    nn = spend + rs * tot * churn_stop
                    k = min(1.0, max(0.0, z / nn)) if nn > 0 else 0.0
                    planned = [Rn * (1 - churn_stop * (1 - k)) for Rn in planned]
                    cost_plan = k * spend + rs * sum(planned) + fix_w
                    if k > 0:
                        max_ueber = max(max_ueber, cost_plan - budget)
        for i, a in enumerate(apps):
            a['R'] = planned[i]
        gross = sum(planned)
        fee = P['apple_low'] if cum_proceeds_year < P['apple_threshold_eur'] else P['apple_high']
        apple_part = gross * (1 - web)
        proceeds = apple_part * (1 - fee)
        cum_proceeds_year += proceeds
        rev_hist.append((gross, proceeds))
        fin_cost = (-credit0 - cash) * P['fin_fee_month'] / WPM if (cash < -credit0 and (credit0 > 0 or fin_ok)) else 0.0
        wk_profit = proceeds + gross * web * web_net - cost_plan - fin_cost
        profit += wk_profit
        profit_hist.append(wk_profit)
        deckung_hist.append(wk_profit + fix_w)
        if KV:
            # Familienversicherung: Die Kasse schätzt den regelmäßigen Monatsgewinn vorausschauend (Jahr 2027).
            # Gewinn der letzten 4 Wochen einschließlich Testgeld, hochgerechnet; zählt nur, wenn auch die
            # Prognose für das Jahr über der Grenze liegt.
            kv_hist.append(wk_profit - sum(c for (ww, c) in test_log if ww == w))
            rate = sum(kv_hist[-4:]) * WPM / 4
            rest = (date(2027, 12, 31) - d).days / 30.4
            if rate > KV['monatsgewinn'] and (profit + rate * rest) / 12 > KV['monatsgewinn']:
                kv_kosten += KV['beitrag'] / WPM      # eigene Kranken- und Pflegeversicherung (privat)
        cost_queue.append((w + cost_lag, cost_plan))
        due_now = sum(c for (wk, c) in cost_queue if wk <= w)   # inkl. dieser Woche bei Ziel 0
        cash += inflow - due_now - fin_cost
        cost_queue = [(wk, c) for (wk, c) in cost_queue if wk > w]
        min_kasse = min(min_kasse, cash)
        if cash < 0 and credit0 <= 0 and not fin_ok:
            # Kasse leer (nur durch Pflichtkosten möglich): der Gründer legt privat nach
            nachschuss += -cash
            cash = 0.0
        mrr_eur = gross * WPM
        max_mrr = max(max_mrr, mrr_eur)
        best_mrr = max(best_mrr, max((a['R'] for a in apps), default=0.0) * WPM)
        chk[w] = best_mrr
        if FJ and FJ.get('vorentscheid') and w == woche_ab(FJ['vorentscheid']):
            # Vorentscheidung (Fr 25.06.; Stand am Ende dieser Woche, also leicht vorsichtig): App im Store oder im
            # Review -> dem Arbeitgeber den 19.07. genannt (06, 2.2 und 2.10)
            genannt_19 = bool(apps) or bool(reviews)
        if RW:
            AN = RW.get('anmeldung')
            if AN and w == woche_ab(AN['am']) - 1:
                # Messtag (Mo 28.06.): Stand am Ende der Vorwoche; nur dann meldet sich das Elternteil an
                eltern_konto = max((a['R'] for a in apps), default=0.0) * WPM >= AN['ab_mrr_usd'] * FX
            if RW.get('stichtag') and w == bis_woche(RW['stichtag']):
                rw_stand = (sum(profit_hist[-4:]) * WPM / 4,
                            max(((a['R'], a['launch']) for a in apps), default=(0.0, WEEKS)))
        if P['angel']:
            weeks_over_20k = weeks_over_20k + 1 if mrr_eur >= P['angel_trigger_mrr'] else 0
            if angel_state is None and weeks_over_20k >= 4:
                if rng.random() < t('p_angel'):
                    angel_state = ('pending', w + int(round(t('angel_delay_weeks'))),
                                   t('angel_amount'), t('angel_dilution'))
                else:
                    angel_state = 'no'
            if isinstance(angel_state, tuple) and w >= angel_state[1]:
                cash += angel_state[2]
                angel_geld += angel_state[2]
                share *= (1 - angel_state[3])
                angel_state = 'done'
        if first10k_week is None and mrr_eur >= 10000 * FX:
            first10k_week = w
        if first100k_week is None and mrr_eur >= 100000 * FX:
            first100k_week = w
        # ---------------- Exit ----------------
        if exit_state is None and w > relist_after and apps:
            best = max(apps, key=lambda a: a['R'])
            age = w - best['launch']
            if age >= P['exit_min_age_weeks'] and len(profit_hist) >= 13:
                p13 = sum(profit_hist[-13:])
                val = mult * 4 * p13 * (1 - deal_cost)      # Kaufpreis nach Transaktionskosten
                close_w = w + int(round(t('exit_close_weeks')))
                # Verkauf nur, wenn er das Ziel erreicht (Anteil des Gruenders an Gewinn + Erloes)
                if share * (profit + val) >= P['profit_target'] and close_w < WEEKS:
                    exit_state = ('listing', close_w, val)
        elif exit_state and exit_state[0] == 'listing' and w >= exit_state[1]:
            p13 = sum(profit_hist[-13:])
            val = min(exit_state[2], mult * 4 * p13 * (1 - deal_cost))
            if rng.random() < p_close and share * (profit + val) >= P['profit_target']:
                exit_state = ('done', val)
                exit_value = val
            else:
                exit_state = None
                relist_after = w + 4
    p13 = sum(profit_hist[-13:]) if profit_hist else 0.0
    paper = max(0.0, 2.0 * 4 * p13) if exit_value == 0 else 0.0
    # Offene Posten fuer die Kassenprobe: Gewinn = Kasse - Start - Nachschuss + Forderungen - offene Kosten
    forderungen = sum(pr for (_, pr) in rev_hist[-lag:]) if lag > 0 else 0.0
    if rev_hist:
        forderungen += rev_hist[-1][0] * web * web_net
    # Vermoegensaenderung des Gruenders: Er bringt das ganze Geld ein (Rest des Startkapitals als
    # Kapitalruecklage), der Partner nur Arbeit; ihm gehoert der Anteil `share` am Eigenkapital.
    # Ist das Eigenkapital am Ende negativ, zahlt er die offenen Rechnungen allein. Ein Angel hat
    # die übliche 1x-Liquidationspräferenz ohne Beteiligung: Er bekommt seine Einlage zurück oder
    # seinen Anteil, was mehr ist; der Rest gehört dem Gründer (und Partner) im alten Verhältnis.
    einsatz = P['start_cash'] + nachschuss
    eigenkapital = einsatz + angel_geld + profit + exit_value
    s0 = P.get('founder_share', 1.0)
    ekp = max(0.0, eigenkapital)
    angel_teil = max(min(ekp, angel_geld), (1 - share / s0) * ekp) if angel_geld else 0.0
    abw_eff = abw if gegruendet else 0.0      # ohne Gründung nichts aufzulösen
    ergebnis = s0 * (ekp - angel_teil) + min(0.0, eigenkapital) - einsatz - abw_eff - kv_kosten
    # Wert nach dem 31.08.: Verkauf oder Übergabe laufender Apps (Monatsgewinn der letzten 4 Wochen x Monate)
    restwert = 0.0
    art = None           # 'verkauf' | 'uebergabe' | None
    if RW and apps and exit_value == 0:
        monatsgewinn = sum(profit_hist[-4:]) * WPM / 4
        # Käufer und Nachfolger wollen Daten: beste App seit mindestens min_alter_w Wochen im Store,
        # Monatsgewinn über min_monat
        beste = max(apps, key=lambda a: a['R'])
        if RW.get('stichtag'):
            # entschieden wird mit dem Stand am Entscheidungstag, nicht mit den Zahlen aus dem August
            mg_ent, (R_best, l_best) = rw_stand if rw_stand else (0.0, (0.0, WEEKS))
            alter = woche_ab(RW['stichtag']) - l_best    # volle Wochen bis zum Umschalttag (Start bis So 13.06.: 8)
        else:
            mg_ent, R_best, l_best = monatsgewinn, beste['R'], beste['launch']
            alter = WEEKS - l_best
        if mg_ent > RW.get('min_monat', 0.0) and alter >= RW.get('min_alter_w', 0):
            VK = RW.get('verkauf')
            if VK and alter >= VK['min_alter_w'] and R_best * WPM >= VK['ab_umsatz_usd'] * FX \
                    and rng.random() < tri(rng, *VK['p']):
                restwert = mg_ent * tri(rng, *VK['monate'])     # Verkauf (netto nach Gebühren), Preis nach dem Stand
                art = 'verkauf'
            elif (eltern_konto or not RW.get('anmeldung')) and rng.random() < tri(rng, *RW['p']):
                restwert = max(0.0, monatsgewinn) * tri(rng, *RW['monate'])   # Übergabe (Geld des Elternteils)
                art = 'uebergabe'
                if 'kosten' in RW:
                    restwert = max(0.0, restwert - tri(rng, *RW['kosten']))
    # Ab der Übertragung gehören die Erlöse dem Nachfolger (Elternteil oder Käufer), nicht mehr dir. Bei einer
    # Übergabe stecken sie schon in den 0,7/2/5 Monatsgewinnen der zwölf Monate ab der Übertragung (06, 4.7).
    nach_uebertragung = 0.0
    if art and RW.get('uebertragung'):
        nach_uebertragung = sum(deckung_hist[woche_ab(RW['uebertragung']):])
    # Angemeldet, aber nichts übernommen: die Kosten des Elternteils sind verloren (Geld der Familie)
    eltern_kosten = 0.0
    if RW and RW.get('anmeldung') and eltern_konto and art != 'uebergabe':
        eltern_kosten = tri(rng, *RW['kosten'])
    # Stilllegung ohne Nachfolger: Ab dem Verkaufsstopp gibt es weder Neuabschlüsse noch Verlängerungen; es
    # entfällt das Ergebnis dieser Wochen vor Fixkosten (Erlös minus Werbung und andere umsatzabhängige Kosten)
    abschalt_abzug = 0.0
    ST = P['stilllegung']
    if ST and gestoppt and apps and art is None and exit_value == 0:
        ab_w = woche_ab(ST['verkauf_bis']) + 1       # erste Woche, die nach dem Verkaufsstopp beginnt
        abschalt_abzug = sum(deckung_hist[ab_w:])
    # Ferienjob nach dem Ende der Jagd (netto, kurzfristige Beschäftigung vor dem Studium); läuft er bis zum Ende des
    # Modells, zählen auch die Werktage danach bis zum letzten Arbeitstag (z. B. Fr 10.09.)
    job_nach_w = 0.0
    if FJ and job_wochen and FJ.get('bis'):
        nach_modell = START + timedelta(weeks=WEEKS)          # Mo 30.08.2027, erster Tag nach dem Modell
        job_nach_w = sum(1 for k in range((FJ['bis'] - nach_modell).days + 1)
                         if (nach_modell + timedelta(days=k)).weekday() < 5) / 5.0
    job_netto = (job_wochen + job_nach_w) * tri(rng, *FJ['netto_woche']) if FJ and job_wochen else 0.0
    ergebnis -= abschalt_abzug + nach_uebertragung
    ergebnis_app = ergebnis
    verkauf = restwert if art == 'verkauf' else 0.0
    ergebnis_dein = ergebnis_app + verkauf + job_netto         # dein Geld: App, Verkaufspreis, Lohn
    ergebnis += restwert + job_netto - eltern_kosten            # mit dem Geld des Elternteils (Übergabe)
    g3 = bis_woche(P["test_cap_bis"])
    return dict(launch1=(apps[0]['launch'] if apps else 99), profit=profit * share,
                exit=exit_value * share, paper=paper * share, attempts=attempts,
                gestartet=len(apps), gestartet_g3=sum(a['launch'] <= g3 for a in apps), max_ueber=max_ueber,
                max_mrr=max_mrr, f10=first10k_week, f100=first100k_week,
                squeeze=cash_squeeze, peaks=[a['peak'] for a in apps], launches=[a['launch'] for a in apps], chk=chk,
                profit_firma=profit, cash=cash, forderungen=forderungen,
                offene_kosten=sum(c for (_, c) in cost_queue), gestoppt=gestoppt,
                stopp_woche=stopp_woche, bau_nach_stopp=bau_nach_stopp, test_log=test_log,
                testkosten_g3=testkosten_g3, min_kasse=min_kasse, nachschuss=nachschuss,
                ergebnis=ergebnis, angel_geld=angel_geld, agent_aktiv=agent_aktiv,
                einmal_offen=einmal_rest + ag_rest,
                offene_versuche=(bau is not None) + len(reviews),
                partner_woche=pw, abwicklung=abw_eff, apple_ab=apple_ab,
                gegruendet=gegruendet, gruendung_woche=gruendung_woche, zu_teuer=zu_teuer, kv_kosten=kv_kosten,
                einreichung1=einreichung1, restwert=restwert, job_netto=job_netto, job_wochen=job_wochen,
                ergebnis_app=ergebnis_app, abschalt_abzug=abschalt_abzug, job_frueh=job_frueh,
                stichtag_stopp=stichtag_stopp, art=art, verkauf=verkauf,
                uebergabe=(restwert if art == 'uebergabe' else 0.0), nach_uebertragung=nach_uebertragung,
                eltern_konto=eltern_konto, eltern_kosten=eltern_kosten, ergebnis_dein=ergebnis_dein,
                abitur_h=abitur_h, job_nach_w=job_nach_w, frei1_w=frei1_w, bau2_w=bau2_w, post_max=post_max,
                genannt_19=genannt_19, vorab_h=vorab_h)


def scen(**kw):
    P = dict(BASE)
    P.update(kw)
    return P


# --------------------------------------------------------------------------
# Szenarien
# --------------------------------------------------------------------------

# Regeln des Plans (docs/500K_BIS_SOMMER_2027.md, Abschnitte 3, 4 und 11):
# Schulwochen 10 h (in Wochen mit Schulaufgaben nur Samstag 3 h, hoechstens 15 h), Ferien 25-50 h,
# Abiturzeit nach Tabelle F (Osterzeit 1-5 h, schriftlich 0-1 h, Pfingsten/Kolloquium 1-5 h),
# Uebergang 15-40 h, Sommer 45-65 h; je Woche zusaetzlich x0,8-1,2.
PLAN_STUNDEN = dict(h_school=(3, 10, 13), h_holiday=(25, 38, 50), h_abiprep=(1, 2.5, 5),
                    h_abi=(0, 0.5, 1), h_oral=(1, 3, 5), h_gap=(15, 28, 40), h_full=(45, 55, 65))
# Tore G3 und G4: beste App unter 5.000 bzw. 10.000 USD MRR -> Jagd beenden
TORE = ((date(2027, 2, 28), 5_000), (date(2027, 3, 31), 10_000))
# Nebenaufgaben des Wochenplans (Partnersuche, Gründung, Sicherheitsnetz) kosten App-Stunden
# G5 (30.04.: beste App unter 50.000 USD MRR): keine neuen Versuche mehr, die Apps laufen weiter
G5 = ((date(2027, 4, 30), 50_000),)
PLAN_REGELN = dict(PLAN_STUNDEN, stopps=TORE, neu_stopp=G5, nebenaufgaben=True)
# Mehr Stunden, als der Abiturschutz erlaubt (frühere Annahme des Modells); Übergang und Sommer wie im Plan
MEHR_STUNDEN = dict(h_school=(8, 15, 22), h_abiprep=(3, 8, 15), h_abi=(0, 3, 8), h_oral=(5, 12, 20))
# Strengere Trefferquoten (Gegenprüfung): RevenueCat 4,6 % der neuen Apps >= 10k USD MRR in zwei
# Jahren, 2026/27 deutlich mehr Konkurrenz (14.700 neue Abo-Apps im Januar 2026), Appfigures-Tail dünn
KRITIKER = dict(p1k=(0.10, 0.18, 0.30), p10k=(0.02, 0.04, 0.08), q100k=(0.05, 0.12, 0.22),
                q1m=(0.03, 0.08, 0.15))
# Lernkurve: Treffer kommen selten beim ersten Versuch (Cal AI war die 7. App, Halo AI nach 18 Monaten)
LERNKURVE = [0.3, 0.6, 0.85, 1.0]
# Der Plan: Vorlagen-Code und schnelle MVPs, US-Web-Checkout neben dem In-App-Kauf, Ferien voll genutzt.
# Web-Anteil am Gesamtumsatz 5-40 % (S): nur US-Storefront (~55-70 % des Umsatzes englischsprachiger
# Apps), dort wählt nur ein Teil den Web-Kauf; RevenueCat (Mai 2025): Link-out konvertierte mit 18 %
# statt 28 % beim In-App-Kauf.
# Wachstumsfinanzierung ohne Kredit: Bremst die Kasse einen Treffer (>= 20.000 EUR MRR über 4 Wochen),
# sucht der Gründer einen Business Angel (Eigenkapital gegen 8-25 % der Anteile, S).
BESTER_PLAN = dict(PLAN_REGELN, **KRITIKER, learn=LERNKURVE, web_share=(0.05, 0.20, 0.40),
                   build_first=(50, 80, 130), build_next=(25, 45, 70), angel=True)
# Partner mit Vertrieb (Creator-Netzwerk, Playbook) – Wirkung geschätzt. Er arbeitet ab einer Woche
# zwischen Start und 31.01. (Partner-Tor) mit: eigene Trefferquoten ohne Lernkurve, höherer Startumsatz,
# günstigere Creator, 20-50 Stunden je Woche für Bau, Test und Skalierung.
PARTNER = dict(p1k=(0.15, 0.25, 0.40), p10k=(0.03, 0.065, 0.13), q100k=(0.07, 0.15, 0.25),
               q1m=(0.03, 0.08, 0.15), m0=(2000, 5000, 12000), c_early=(0.25, 0.38, 0.55),
               team_hours=(20, 30, 50), build_next=(25, 45, 70))
PARTNER_PLAN = dict(BESTER_PLAN, partner=PARTNER, partner_week=(0, bis_woche(date(2027, 1, 31)) + 1))
# Gesellschaftervereinbarung mit Vesting (Notar, Entwurf durch Anwalt) bzw. Kooperationsvertrag (S)
VERTRAG_ANTEILE = (300, 800, 2000)
VERTRAG_UMSATZ = (150, 400, 800)

# ---- Allein mit Claude: Stufen der Abgabe (Recherche November 2026, Schätzungen mit Belegen) ----
# Stufe 0: allein, ohne Stunden für die Partnersuche; Claude Pro ist schon in den Werkzeugkosten.
ALLEIN = dict(BESTER_PLAN, partnersuche=False)
# Stufe 1: Claude Code schreibt den ganzen Code (Max statt Pro: +0-160 EUR/Monat). Erste App: Modus gleich,
# oberes Ende weiter (Fehlersuche, wenn man den Code nicht versteht; METR 2025/2026, Anthropic-RCT 2026);
# weitere Apps etwas schneller (Vorlage, CLAUDE.md mit Review-Lösungen).
CLAUDE_1 = dict(ALLEIN, build_first=(50, 80, 160), build_next=(22, 40, 75), extra_fix_monat=(0, 70, 160))
# Stufe 2: + Hooks, Skripte, Schnittlisten, Creator-Recherche, Anfrage-Entwürfe, Briefings, Auswertung
# (~15 % weniger Teststunden; P&G 16 %, BCG ~25 %, Praxis 3-7 %); 3-12 h einmalige Einrichtung.
CLAUDE_2 = dict(CLAUDE_1, test_hours=(23, 42, 72), einmal_stunden=(3, 6, 12))
# Stufe 3: + Agent im Betrieb (RevenueCat-/App-Store-Auswertungen, Paywall-Tests, Support-Entwürfe,
# Releases): Skalieren 10-32 statt 15-35 h je Woche; 10-35 h Einrichtung, 1 h Pflege je Woche; Max/Ultra.
CLAUDE_3 = dict(CLAUDE_2, h_need=(10, 20, 32), einmal_stunden=(13, 26, 47), pflege_h_woche=(0.5, 1.0, 2.0),
                extra_fix_monat=(70, 90, 200), agent_ab_start=True)
# Stufe 4: Vollabgabe: Claude baut ohne eigene Prüfung, KI-Avatar-Videos statt eigener (kennzeichnungs-
# pflichtig nach Art. 50 KI-VO, gekennzeichnet bis -31,5 % CTR; ein Fall mit 0,4-0,6x ROAS), Wer alles
# abgibt, lernt weniger (Anthropic-RCT 2026: 50 statt 67 %): Lernkurve langsamer.
CLAUDE_4 = dict(CLAUDE_3, build_first=(45, 80, 180), build_next=(18, 35, 75), test_hours=(20, 35, 60),
                h_need=(10, 18, 30), learn=[0.25, 0.50, 0.80, 1.0], p_faktor=(0.6, 0.8, 1.0),
                pflege_h_woche=(0.3, 0.5, 1.0), extra_fix_monat=(110, 130, 240))
# Gestaffelt: Claude schreibt den Code und erklärt ihn (er prüft mit Checkliste; erste App wie im Plan,
# weitere schneller), Marketing-Vorarbeit ab Start; bei Claude Pro bleiben, Max nur, wenn das Limit wirklich
# bremst (+0-70 EUR/Monat, meist 0). Der Agent für den Betrieb (Max/Ultra, 10-35 h Einrichtung) kommt erst,
# wenn ein Treffer erkannt ist.
CLAUDE_GESTAFFELT = dict(ALLEIN, build_next=(22, 40, 75), test_hours=(23, 42, 72), einmal_stunden=(3, 6, 12),
                         extra_fix_monat=(0, 10, 70),
                         agent_bei_treffer=dict(h_need=(10, 20, 32), einmal=(10, 20, 35), extra_monat=(40, 60, 150),
                                                pflege=(0.5, 1.0, 2.0)))
# Strengerer Markt 2027 (Gegenprobe): Angebot neuer Apps verdoppelt (Sensor Tower H1 2026), RevenueCat-Quoten
# gesunken, KI-Apps verlieren Abonnenten 30 % schneller, Kopien in Tagen, längere Reviews, teurere Anzeigen.
MARKT_2027 = dict(p_faktor=(0.65, 0.85, 1.0), churn_stop=(0.05, 0.13, 0.20), decay_month=(0.03, 0.07, 0.18),
                  p_kill=(0.07, 0.12, 0.22), review_weeks=(0.3, 1.0, 4.0), c_growth=(0.58, 0.74, 0.88))

# ---- Deine Angaben (November 2026): Niedersachsen, keine Programmierkenntnisse, anonym, <= 5.000 EUR ----
# Recherche November 2026 (docs/APP_PLAN_ALLEIN_MIT_CLAUDE.md, Quellen dort). Erst bauen, dann gründen: App 1
# entsteht in Expo Go ohne Firma; gegründet wird, wenn sie zur Hälfte steht. Kein Start in der Abiturzeit
# (15.03.-06.06.): eine freigegebene App bleibt bis 07.06. unveröffentlicht. Freiwillige Ausgaben nur, solange
# Pflichtkosten bis 31.08. und die Auflösung bezahlt sind (Gesamtverlust höchstens 5.000 EUR).
STARTPAUSE_NI = (date(2027, 3, 15), date(2027, 6, 7))


def _nebenaufgaben_ni():
    """Nebenaufgaben nach Wochenplan: ETH-Bewerbung (eApply 01.12.-31.03., ~1 Tag) in den Weihnachtsferien,
    Rückfall-Bewerbung (LUH bis 15.07.), Abiturzeugnis hochladen, ab Juli Zimmersuche, Unterlagen für
    Zürich und Mathe-Auffrischung (~6 h je Woche)."""
    m = {date(2026, 12, 28): 6.0, date(2027, 6, 14): 2.0, date(2027, 6, 28): 1.0}
    d = date(2027, 7, 5)
    while d < END:
        m[d] = m.get(d, 0.0) + 6.0
        d += timedelta(weeks=1)
    return m


NEBEN_NI = _nebenaufgaben_ni()
# Ohne Programmierkenntnisse (S): keine Studie misst den Abstand zu Profis; Debugging (61 % der Anfänger-
# Prompts), Signierung, Deployment und Review sind die Engpässe, Puffer 2-3x (Recherche). Erste App 80/140/280 h
# statt 50/80/130, weitere 35/60/120 statt 22/40/75; Grundlagen (Expo-Tutorials, Shell/Git, JavaScript lesen)
# 20-40 h; 1-2 Ablehnungen bei der ersten App; Claude Pro, Max nur in einzelnen Monaten.
OHNE_PROGRAMMIEREN = dict(build_first=(80, 140, 280), build_next=(35, 60, 120), einmal_stunden=(20, 30, 40),
                          review_weeks=(0.5, 1.5, 4.0), extra_fix_monat=(0, 10, 70))
# Tore im Sommer: vor dem Abitur gibt es kaum Teststunden (Q4 3-7 h, Abitur 0-5 h); die Jagd endet am
# 18.07. unter 5.000 USD und am 08.08. unter 10.000 USD MRR, Tests aus dem Startgeld bis 18.07.
TORE_SOMMER = ((date(2027, 7, 18), 5_000), (date(2027, 8, 8), 10_000))
# Signalregel: Creator-Geld erst, wenn eine App drei Wochen nach dem Start ohne bezahlte Werbung mindestens
# 300 USD Monatsumsatz zeigt (bis 18.07. höchstens 750 EUR aus dem Startgeld, danach nur aus Umsatz); vorher
# laufen nur eigene Videos ohne Gesicht. Gegenproben: Tests sofort beim Start, ganz ohne Testgeld.
# Das Signal ist unsicher: Ohne bezahlten Test startet auch ein Treffer nur mit 20-70 % des Startumsatzes und
# kann unter der Schwelle bleiben; nach dem Signal kommt die Spitze mit 70-100 % zurück (verlorene Wochen). Ein
# Signal in der Startpause (Abitur) wird erst ab 07.06. gebucht. Kein Web-Kauf und kein Business Angel (beim
# Einzelunternehmen gibt es keine Anteile zu verkaufen).
SIGNAL = dict(wochen=3, schwelle_usd=300, abschlag=(0.7, 0.85, 1.0))
DEINE_ANGABEN = dict(CLAUDE_GESTAFFELT, **OHNE_PROGRAMMIEREN, kalender='NI', neben=NEBEN_NI, harte_grenze=True,
                     startpause=STARTPAUSE_NI, stopps=TORE_SOMMER, neu_stopp=(), test_cap_bis=date(2027, 7, 18),
                     test_cap=750.0, signal=SIGNAL, m0_ohne_test=(0.2, 0.4, 0.7), web_share=(0.0, 0.0, 0.0),
                     angel=False)
# Rechtsformen (Recherche November 2026; Kosten je Monat ab der Gründung, nach dem Tor, Gründung, Auflösung bzw.
# Abmeldung nach dem 31.08.; B/S):
# Einzelunternehmen: Gewerbeanmeldung 20-65 EUR, Apple 99 USD/Jahr, Erstberatung beim Steuerberater 0-250 EUR
# (Kleinunternehmer oder Verzicht), IHK 0 EUR (Gründer, Gewerbeertrag < 25.000 EUR); laufend Claude Pro
# (~21 EUR brutto), Server 0-25 USD, Domain/E-Mail; EÜR und Steuererklärung 2027 selbst über ELSTER oder mit
# Steuerberater (0-800 EUR), Abmeldung 0-32,50 EUR vor dem Umzug. Dein Name steht als Verkäufer im App Store.
# Gewinn über 590 EUR im Monat (Grenze 2027) beendet die Familienversicherung: dann ~280 EUR/Monat privat.
EINZEL = dict(gruendung=dict(bei=0.5, setup=(150, 250, 450), apple_dauer=(0.3, 0.6, 1.5), fix_vorher=(20, 22, 25),
                             stunden=4.0),
              fixed_month=(35, 60, 110), fixed_stop=(10, 25, 50), abwicklung=(0, 300, 800), profit_target=970000.0,
              kv_grenze=dict(monatsgewinn=590.0, beitrag=280.0))
# UG mit registertauglicher Geschäftsadresse (49-130 EUR/Monat): im App Store nur der Firmenname, im Impressum
# und Handelsregister trotzdem dein Name. Notar ~165-205 EUR, Register 300 EUR, Gewerbe; Steuerberater für
# Jahresabschluss und Erklärungen ~600-2.400 EUR/Jahr (Gegenprüfung: Online-Festpreis 499,95 EUR netto),
# IHK ~130 EUR, Transparenz- und Unternehmensregister ~40 EUR, Konto ~9-12 EUR/Monat; Auflösung mit Sperrjahr
# ~3.000-5.000 EUR (Löschung frühestens Ende 2028, während du in Zürich lebst); D-U-N-S und Apple-Prüfung
# (Foren 2026: 3 bis über 8 Wochen).
UG_ADRESSE = dict(gruendung=dict(bei=0.5, setup=(500, 560, 700), apple_dauer=(3, 6, 10), fix_vorher=(20, 22, 25),
                                 stunden=10.0),
                  fixed_month=(160, 300, 470), fixed_stop=(130, 240, 390), abwicklung=(3000, 3800, 5000))
# UG mit der Anschrift der Eltern als Geschäftsanschrift (öffentlich im Handelsregister und in der EU-Anzeige).
UG_ELTERN = dict(UG_ADRESSE, fixed_month=(110, 210, 340), fixed_stop=(80, 150, 260))

# ---- Hebel (Recherche und Gegenprüfung vom 24.11.2026, docs/details/07_HEBEL.md) ----
# Angesetzt sind die von der Gegenprüfung korrigierten, vorsichtigen Werte; S = Schätzung, B = belegt.


def _mix(*teile):
    """Fügt Parameterblöcke zusammen (spätere überschreiben frühere)."""
    out = {}
    for t in teile:
        out.update(t)
    return out


# Pflicht, kein Hebel: Stunden und Regeln, die die Detailpläne verlangen (Prüfung des Modells, 25.11.). Nebenaufgaben
# vor und bei der Gründung, die nicht in den Bau fließen: Ideenwahl ab Mo 30.11. typisch 10 h (04, Abschnitt 2: KW 49
# 2,75 h, KW 50 2,25 h, KW 51 5 h; der Sa 28.11. liegt vor dem Start des Modells), Verwaltung und ELSTER 1 h,
# Entscheidung mit den Eltern 1 h (Fr 11.12.), Apple Developer Program 1 h (Mo 14.12.), Bankkonto 0,75 h und
# Bewerbungen für den Ferienjob 1,5 h (Weihnachtsferien), Gründungsberatung 2,5 h (bis Mi 06.01.), Vorbereitung fürs
# Marketing 3,5 h (05, Abschnitt 4), Zusage des Elternteils und Frage an die Oberstufenkoordination 1 h (Januar).
# Die Gründung selbst kostet 6 statt 4 h (03, Abschnitt 5.1; zusammen mit Bankkonto und Beratung rund 9 h). Ist M2
# (halb fertig) bis Mo 01.03. nicht erreicht, wird erst nach der letzten Prüfung gegründet (03, Abschnitt 5).
# Kassenprüfung, Wochenauswertung und Support-Postfach: 0,4/0,5/0,6 h je Woche, solange eine App läuft (S); die
# Kassenprüfung (10 min) schon ab der Gründung (03, 7.3). Ein Signal vor dem Abitur zählt, Creator bucht der Plan aber
# erst nach der letzten Prüfung (Prüfung des Modells, 25.11. abends):
# - App 2 beginnt erst, wenn App 1 freigegeben ist, aus der Vorlage (+3,5 h; 02, Abschnitt 9; 06, KW 24).
# - Posts und Tests haben Vorrang, aber nur im Umfang des Wochenprogramms: vor dem Abitur ein Samstagsblock (1,5 h,
#   05, 6.2), danach 2 Posts am Tag mit rund 6,5 h je Woche (05, 6.1 und 6.4); der Rest baut weiter. Der Deckel von
#   10 h (05, 6.1) ist die Obergrenze, voll nur mit Creator-Arbeit (Gegenprobe).
# - Markenkonten und Featuring-Nominierung je Einreichung 1,83 h (05, Abschnitt 1.1); die Vorbereitung der Posts
#   (V1-V4, 3,5 h) nach der Einreichung von App 1 (05, Abschnitt 4; 01, Di 02.02.).
# - Weitere Termine: Sozialversicherungsnummer 0,25 h (Januar), Halbjahreszeugnis in eApply 0,25 h (Fr 29.01.),
#   Gespräche zum Ferienjob in Q4 1 h, Vertrag und Anfrage an die Krankenkasse 1,25 h (06, 2.2), Zimmersuche in
#   Zürich 2 h (KW 24) und Finanzierungsbrief 1 h (KW 25; 06, 1.2, Schätzung); die Bewerbung in Hannover (2 h) in
#   KW 28 (06, 1.2) statt in KW 24.
# - Umsatzabhängige Kosten nach dem Plan: unter 5.000 USD MRR keine Werbung aus dem Umsatz, nur Umsatzsteuer im Preis
#   (0,85 x 0,16 = 0,136), KI-API (~0,01) und Erstattungen (2-8 %): 15/20/25 % vom Umsatz (06, Abschnitt 3: von 1 EUR
#   Preis bleiben ~0,71 EUR). Darüber gelten die Sätze für bezahltes Wachstum (c_early/c_growth) weiter.
def _nebenaufgaben_plan():
    m = dict(NEBEN_NI)
    for tag, h in ((date(2026, 11, 30), 3.75), (date(2026, 12, 7), 3.25), (date(2026, 12, 14), 6.0),
                   (date(2026, 12, 28), 2.25), (date(2027, 1, 4), 2.5),
                   (date(2027, 1, 25), 1.0),
                   (date(2027, 1, 11), 0.25), (date(2027, 1, 25), 0.25), (date(2027, 2, 15), 1.0),
                   (date(2027, 3, 1), 1.25), (date(2027, 6, 14), 2.0), (date(2027, 6, 21), 1.0)):
        m[tag] = m.get(tag, 0.0) + h
    # Bewerbung in Hannover (2 h aus NEBEN_NI) nach 06 in KW 28 (Do 15.07. abgeschickt) statt KW 24
    m[date(2027, 6, 14)] -= 2.0
    m[date(2027, 7, 12)] = m.get(date(2027, 7, 12), 0.0) + 2.0
    return m


NEBEN_PLAN = _nebenaufgaben_plan()
GRUENDUNG_PLAN = dict(EINZEL['gruendung'], stunden=6.0, spaet=(date(2027, 3, 1), date(2027, 6, 7)))
SIGNAL_PLAN = dict(SIGNAL, creator_nach_pause=True)
AUFWAND_PLAN = dict(neben=NEBEN_PLAN, gruendung=GRUENDUNG_PLAN, pflege_h_woche=(0.4, 0.5, 0.6), signal=SIGNAL_PLAN,
                    vorlage_h=3.5, post_deckel=(1.5, 6.5), kasse_ab_gruendung=10 / 60, konten_je_einreichung=1.83,
                    vorb_nach_einreichung1=3.5, c_organisch=(0.15, 0.20, 0.25))
# Ausgangslage aller Hebel: Plan vom 23.11. mit den Stunden und Regeln der Detailpläne
BASIS_HEBEL = _mix(DEINE_ANGABEN, EINZEL, AUFWAND_PLAN)

# Markt: App zweisprachig, Videos auf Deutsch (Reichweite ist an SIM und IP gebunden): DACH-Abschlag auf die
# Trefferquoten x0,8/0,9/1,0 (S). Ideenwahl mit K.-o.-Fragen und Nachfrageprüfung: x1,0/1,05/1,2 für die ganze
# Hebelklasse (S, kein Messbeleg). Zusammen x0,8/0,95/1,2. Slideshow-Filter der Ideenwahl (04, Abschnitt 8;
# Gegenprüfung idee-nische): Startumsatz ohne Test 0,40 -> 0,42 (S); Format-Raster und Wiederverwendung mit 0
# angesetzt. Die Stunden für die zweite Sprache stecken in den Arbeitspaketen von 02 (Gegenprobe unten).
HEBEL_MARKT = dict(p_faktor=(0.8, 0.95, 1.2), m0_ohne_test=(0.2, 0.42, 0.7))
# Bau: Expo-Gerüst mit Plugin, fertige RevenueCat-Paywall, Durchstich zuerst, Arbeitsweise mit Prüfbefehl, eigene
# Vorlage ab App 2 (S, Herstellerangaben ohne Zeitmessung): 78/130/260 statt 80/140/280 h, weitere Apps 33/55/110;
# Lernstunden 20/28/40. Review-fest geplant (geführter Ablauf, Meldeknopf, Einwilligung): 0,4/1,2/3,0 Wochen.
HEBEL_BAU = dict(build_first=(78, 130, 260), build_next=(33, 55, 110), einmal_stunden=(20, 28, 40),
                 review_weeks=(0.4, 1.2, 3.0))
# Kosten (B/S): Kleinunternehmer, Abschluss selbst über ELSTER (20/80/500 EUR statt 0/300/800), kostenlose
# Gründungsberatung (Gründung 140/200/380), vor dem ersten Start nur Claude Pro, Domain, Nummer (23/28/45 EUR je
# Monat), danach Supabase Free, EAS Free (23/30/75), nach dem Tor alles kündigen (5/12/35), Max höchstens für
# einen einzelnen Monat (0/0/12 statt 0/10/70).
HEBEL_KOSTEN = dict(fix_vor_start=(23, 28, 45), fixed_month=(23, 30, 75), fixed_stop=(5, 12, 35),
                    abwicklung=(20, 80, 500), extra_fix_monat=(0, 0, 12),
                    gruendung=dict(GRUENDUNG_PLAN, setup=(140, 200, 380)))
# Ruhezeit im Abitur (15.03.-06.06.): Ist keine App im Store oder im Review, ruht Claude Pro (2/5/30 EUR je Monat
# für Domain, Nummer und einen Notfall-Monat; Claude Pro ist bis ~27.03. bezahlt, die Ersparnis beginnt am 29.03.)
# und es wird nicht gebaut. Ist eine App im Store oder im Review, gibt es in diesen Wochen nur Betrieb (Zahlen,
# Notfälle, Antworten an das Review), keinen Bau und keine Posts; dann läuft Supabase Pro (zusammen mit Claude Pro,
# Domain und Nummer mindestens ~50 EUR je Monat).
HEBEL_RUHE = dict(fix_ruhe=dict(von=date(2027, 3, 15), kosten_ab=date(2027, 3, 29), bis=date(2027, 6, 7),
                                monat=(2, 5, 30), max_h=0.0, nur_betrieb=True, monat_live=50.0))
# Signal: zweite, gültige Prüfung Ende Juni (Modellwoche ab 28.06.; drei Wochen nach Wiederbeginn der täglichen
# Posts) für Apps, die vor dem Abitur gestartet sind.
HEBEL_SIGNAL = dict(signal=dict(SIGNAL_PLAN, zweite=date(2027, 6, 28)))
# Pflicht, kein Hebel (B): Apple verlangt mindestens 31 Tage zwischen Verkaufsstopp und Dienstende ("A minimum of
# 31 days is required from the date subscription is removed from sale and service is stopped"). Endet die Jagd
# ohne Nachfolger, gehen alle Abos am So 15.08. aus dem Verkauf; der Dienst läuft bis Mi 15.09. (vor dem Umzug).
# Gegenproben: Verkaufsstopp 31.07. (Dienstende 31.08.) und 31.08. (Dienst bis 01.10., nur nach Beratung).
STILLLEGUNG = dict(stilllegung=dict(verkauf_bis=date(2027, 8, 15)))
# Wert nach dem 31.08. (S): ab 150 EUR Monatsgewinn. Verkauf (ab 300 USD Monatsumsatz, App mindestens 8 Wochen
# im Store): Abschluss in 10/25/45 von 100 Fällen, netto 1,7/4,3/10,3 Monatsgewinne. Sonst Übergabe an ein
# Elternteil, das vorab zugesagt hat: Chance, dass ein vorhandener Wert rechtzeitig realisiert wird, 25/40/60 von 100
# (Gegenprüfung; ohne Zusage 10/25/45), 0,7/2/5 Monatsgewinne in den zwölf Monaten ab der Übertragung (06, 4.7),
# abzüglich 120-165 EUR (Gewerbe 20-65 EUR und Apple-Konto 99 EUR des Elternteils). Entschieden wird mit dem Stand bis
# Sa 07.08. (Monatsgewinn der vier Wochen bis 01.08., volle Wochen im Store bis zum Umschalttag So 08.08., also Start
# spätestens So 13.06. für die 8 Wochen eines Verkaufs); ab der Übertragung (Mo 09.08.) gehören die Erlöse dem
# Nachfolger.
# Das Elternteil meldet sich nur an, wenn am Mo 28.06. eine App mindestens ~100 USD MRR zeigt (06, Abschnitt 4.4);
# ohne diese Anmeldung keine Übergabe, und bleibt die Übergabe aus, sind seine Kosten verloren.
RESTWERT = dict(restwert=dict(min_monat=150.0, p=(0.25, 0.4, 0.6), monate=(0.7, 2.0, 5.0), kosten=(120, 140, 165),
                              stichtag=date(2027, 8, 7), uebertragung=date(2027, 8, 9),
                              anmeldung=dict(am=date(2027, 6, 28), ab_mrr_usd=100),
                              verkauf=dict(ab_umsatz_usd=300, min_alter_w=8, p=(0.10, 0.25, 0.45),
                                           monate=(1.7, 4.3, 10.3))))
# Ferienjob (B/S): kurzfristige Beschäftigung ab Mo 19.07., wenn die Jagd am 18.07. endet: 40 h je Woche zu
# 14,60 EUR (Mindestlohn 2027) bis ~17,30 EUR, nach Fahrtkosten 560/600/690 EUR je Woche endgültig (Lohnsteuer
# kommt 2028 zurück); Chance auf einen Job über die ganze Zeit 70-85 von 100 (S). Befristet bis Fr 10.09. (lange
# Variante aus 06, Abschnitt 2: 40 Arbeitstage ab 19.07.); gezählt werden die 6 vollen Wochen bis 29.08. und die
# 10 Werktage danach. Stichtag: Ist am 04.07. noch keine App im Store, endet die Jagd (keine neue App mehr, mit
# oder ohne Job); mit Job beginnt er am 05.07. Vorentscheidung (06, 2.2 und 2.10): Ist am Fr 25.06. eine App im Store
# oder im Review (Modell: Stand am Ende dieser Woche), nennst du dem Arbeitgeber den 19.07. Ist am 04.07. dann trotzdem
# keine App im Store, gibt es die zwei Wochen ab 05.07. nur über eine kurzfristig angefragte Zeitarbeitsfirma: Chance
# 30/50/70 von 100 (S, 06 nennt keine Zahl); sonst gehören sie Zürich, Mathe und der eingereichten App. Auch ohne
# Nennung des 19.07. steht im Vertrag der 19.07. (06, 2.4): Die zwei Wochen ab 05.07. kommen dann über eine
# Zeitarbeitsfirma mit Vorlauf (angefragt Mo 21.06.), Chance 50/70/85 von 100 (S).
FERIENJOB = dict(ferienjob=dict(ab=date(2027, 7, 19), netto_woche=(560, 600, 690), max_app_h=5,
                                p=(0.70, 0.78, 0.85), bis=date(2027, 9, 10)))
FERIENJOB_FRUEH = dict(ferienjob=dict(FERIENJOB['ferienjob'], frueh_ab=date(2027, 7, 5), vorentscheid=date(2027, 6, 25),
                                      zeitarbeit_p=(0.3, 0.5, 0.7), zeitarbeit_vorlauf_p=(0.5, 0.7, 0.85)))
# Plan mit den Hebeln (Stand 25.11.2026); DEIN PLAN = PLAN_HEBEL + RESTWERT + FERIENJOB_FRUEH
PLAN_HEBEL = _mix(BASIS_HEBEL, HEBEL_MARKT, HEBEL_BAU, HEBEL_KOSTEN, HEBEL_RUHE, HEBEL_SIGNAL, STILLLEGUNG)

SZENARIEN = {
    "Recherche-Quoten (Regeln des Plans)": scen(**PLAN_REGELN),
    "Strengere Quoten (Gegenprüfung)": scen(**PLAN_REGELN, **KRITIKER),
    "Strengere Quoten + Lernkurve": scen(**PLAN_REGELN, **KRITIKER, learn=LERNKURVE),
    "DER PLAN: strengere Quoten + Lernkurve + Web-Checkout + schneller Bau": scen(**BESTER_PLAN),
    "Der Plan, optimistischer Rand (Quoten x1,5)": scen(**dict(
        BESTER_PLAN, p1k=(0.15, 0.27, 0.45), p10k=(0.03, 0.06, 0.12), q100k=(0.08, 0.18, 0.33),
        q1m=(0.05, 0.12, 0.22))),
    "Der Plan mit sehr gutem Web-Checkout (Web-Anteil 30-60 %, ohne Beleg)":
        scen(**dict(BESTER_PLAN, web_share=(0.3, 0.45, 0.6))),
    "Der Plan + Partner (Zusage bis 31.01.), Partner erhält 25 % der Anteile":
        scen(**PARTNER_PLAN, founder_share=0.75, partner_vertrag=VERTRAG_ANTEILE),
    "Der Plan + Partner (Zusage bis 31.01.), Partner erhält 40 % der Anteile":
        scen(**PARTNER_PLAN, founder_share=0.6, partner_vertrag=VERTRAG_ANTEILE),
    "Der Plan + Partner (Zusage bis 31.01.), Partner erhält 10 % vom Umsatz":
        scen(**PARTNER_PLAN, partner_rev_share=0.10, partner_vertrag=VERTRAG_UMSATZ),
    "Der Plan mit mehr Stunden (Schulwochen 8-22 h, Abiturzeit 0-20 h)":
        scen(**dict(BESTER_PLAN, **MEHR_STUNDEN)),
    "Obergrenze: erste App ist ein Cal-AI-Treffer (Start 30k, Spitze 1,5 Mio. USD MRR)": scen(
        **BESTER_PLAN, force_first_peak=1.5e6, force_g=3.0, force_m0=30000),
    "Der Plan ohne Tore (weiter bis August, Vergleich)": scen(**dict(BESTER_PLAN, stopps=(), neu_stopp=())),
    "Der Plan + Partner für 25 % + mehr Stunden (ohne Abiturschutz, Vergleich)":
        scen(**dict(PARTNER_PLAN, **MEHR_STUNDEN), founder_share=0.75, partner_vertrag=VERTRAG_ANTEILE),
    # ---- Allein mit Claude (docs/500K_BIS_SOMMER_2027.md, Abschnitt 16) ----
    "Claude-Stufe 0: allein, ohne Partnersuche (Claude Pro hilft wie im Plan)": scen(**ALLEIN),
    "Claude-Stufe 1: Claude schreibt den ganzen Code": scen(**CLAUDE_1),
    "Claude-Stufe 2: + Marketing-Vorarbeit (Hooks, Skripte, Creator-Recherche, Auswertung)": scen(**CLAUDE_2),
    "Claude-Stufe 3: + Agent im Betrieb (Auswertungen, Paywall-Tests, Support-Entwürfe, Releases)":
        scen(**CLAUDE_3),
    "Claude-Stufe 4: Vollabgabe (KI-Avatar-Videos, kaum eigene Prüfung)": scen(**CLAUDE_4),
    "Claude gestaffelt: Code mit Erklärung und Marketing-Vorarbeit ab Start, Agent erst bei einem Treffer":
        scen(**CLAUDE_GESTAFFELT),
    "Claude gestaffelt, falls Claude als Lehrer die Lernkurve verkürzt (unbelegt)":
        scen(**dict(CLAUDE_GESTAFFELT, learn=[0.35, 0.65, 0.90, 1.0])),
    "Claude gestaffelt im strengeren Markt 2027 (mehr Konkurrenz, Abwanderung, Kopien)":
        scen(**dict(CLAUDE_GESTAFFELT, **MARKT_2027)),
    # ---- Deine Angaben (docs/APP_PLAN_ALLEIN_MIT_CLAUDE.md) ----
    "Deine Angaben: Einzelunternehmen, Creator-Geld nur nach Signal, bis 750 EUR (DEIN PLAN)": scen(**dict(DEINE_ANGABEN, **EINZEL)),
    "Deine Angaben: UG mit gemieteter Geschäftsadresse":
        scen(**dict(DEINE_ANGABEN, **UG_ADRESSE)),
    "Deine Angaben: UG mit Anschrift der Eltern": scen(**dict(DEINE_ANGABEN, **UG_ELTERN)),
    "Deine Angaben: Einzelunternehmen, ganz ohne Testgeld": scen(**dict(DEINE_ANGABEN, **EINZEL, test_cap=0.0,
                                                                           signal=None, kein_testgeld=True)),
    "Deine Angaben: Einzelunternehmen, Tests sofort beim Start (ohne Signalregel)":
        scen(**dict(DEINE_ANGABEN, **EINZEL, signal=None)),
    "Deine Angaben: Einzelunternehmen, Signalregel mit bis zu 1.500 EUR":
        scen(**dict(DEINE_ANGABEN, **EINZEL, test_cap=1500.0)),
    "Deine Angaben: Einzelunternehmen, Tore wie bisher (28.02./31.03.)":
        scen(**dict(DEINE_ANGABEN, **EINZEL, stopps=TORE, neu_stopp=G5, test_cap_bis=date(2027, 2, 28))),
    "Deine Angaben: Einzelunternehmen, ohne Tore": scen(**dict(DEINE_ANGABEN, **EINZEL, stopps=(),
                                                                 test_cap_bis=date(2027, 8, 31))),
    "Deine Angaben: Einzelunternehmen, gründen schon im Dezember":
        scen(**dict(DEINE_ANGABEN, **dict(EINZEL, gruendung=dict(EINZEL['gruendung'], bei=0.0)))),
    "Deine Angaben: Einzelunternehmen, ohne Startpause im Abitur":
        scen(**dict(DEINE_ANGABEN, **EINZEL, startpause=None)),
    "Deine Angaben: Einzelunternehmen, falls du schneller baust (wie mit Programmierkenntnissen)":
        scen(**dict(DEINE_ANGABEN, **EINZEL, build_first=(50, 80, 130), build_next=(22, 40, 75),
                    einmal_stunden=(3, 6, 12))),
    "Deine Angaben: Einzelunternehmen im strengeren Markt 2027":
        scen(**dict(DEINE_ANGABEN, **EINZEL, **MARKT_2027)),
    "Deine Angaben: Einzelunternehmen, falls Videos ohne Gesicht schlechter wirken (Trefferquoten -25 %)":
        scen(**dict(DEINE_ANGABEN, **EINZEL, p_faktor=(0.6, 0.75, 0.9))),
    # ---- Hebel (docs/details/07_HEBEL.md): Ausgangslage ist der Plan vom 23.11. mit Verkaufsstopp ----
    "Hebel: Plan vom 23.11. mit Verkaufsstopp am 15.08. (Pflicht, bisher nicht gerechnet)":
        scen(**_mix(DEINE_ANGABEN, EINZEL, STILLLEGUNG)),
    "Hebel: Plan vom 23.11. mit Verkaufsstopp und allen Nebenaufgaben der Detailpläne (Ausgangslage)":
        scen(**_mix(BASIS_HEBEL, STILLLEGUNG)),
    "Hebel: nur Kosten senken (mit Ruhezeit im Abitur)":
        scen(**_mix(BASIS_HEBEL, STILLLEGUNG, HEBEL_KOSTEN, HEBEL_RUHE)),
    "Hebel: nur schneller bauen und review-fest planen":
        scen(**_mix(BASIS_HEBEL, STILLLEGUNG, HEBEL_BAU)),
    "Hebel: nur Markt (Deutsch zuerst) und Ideenwahl":
        scen(**_mix(BASIS_HEBEL, STILLLEGUNG, HEBEL_MARKT)),
    "Hebel: nur zweite Signalprüfung Ende Juni":
        scen(**_mix(BASIS_HEBEL, STILLLEGUNG, HEBEL_SIGNAL)),
    "Hebel: PLAN MIT HEBELN (Kosten, Bau, Markt, Signal; Verkaufsstopp 15.08.)": scen(**PLAN_HEBEL),
    "Hebel: Plan mit Hebeln, Verkaufsstopp schon am 31.07. (Dienstende 31.08.)":
        scen(**_mix(PLAN_HEBEL, dict(stilllegung=dict(verkauf_bis=date(2027, 7, 31))))),
    "Hebel: Plan mit Hebeln, Verkauf bis 31.08. (Dienst bis 01.10., nur nach Beratung)":
        scen(**_mix(PLAN_HEBEL, dict(stilllegung=dict(verkauf_bis=date(2027, 8, 31))))),
    "Hebel: Plan mit Hebeln + Übergabe oder Verkauf (Elternteil hat zugesagt)":
        scen(**_mix(PLAN_HEBEL, RESTWERT)),
    "Hebel: Plan mit Hebeln + Verkaufsversuch und Übergabe ohne feste Zusage":
        scen(**_mix(PLAN_HEBEL, dict(restwert=dict(RESTWERT['restwert'], p=(0.10, 0.25, 0.45))))),
    "Hebel: Plan mit Hebeln + Ferienjob ab 19.07.": scen(**_mix(PLAN_HEBEL, FERIENJOB)),
    "Hebel: Plan mit Hebeln + Ferienjob ab 19.07., ab 05.07. ohne App im Store":
        scen(**_mix(PLAN_HEBEL, FERIENJOB_FRUEH)),
    "Hebel: Plan mit Hebeln + Übergabe oder Verkauf + Ferienjob (DEIN PLAN, Stand 25.11.)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH)),
    "Hebel: wie DEIN PLAN, aber Job schon ab 05.07., wenn am 04.07. keine App 300 USD MRR zeigt (Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, dict(ferienjob=dict(FERIENJOB['ferienjob'], ab=date(2027, 7, 5)),
                                               stopps=((date(2027, 7, 4), 300),) + TORE_SOMMER))),
    "Hebel: wie DEIN PLAN, aber ganz ohne Creator-Geld (Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(test_cap=0.0, signal=None, kein_testgeld=True))),
    "Hebel: Plan mit Hebeln + Übergabe oder Verkauf, ganz ohne Creator-Geld (Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, dict(test_cap=0.0, signal=None, kein_testgeld=True))),
    "Hebel: Plan mit Hebeln ohne Testgeld":
        scen(**_mix(PLAN_HEBEL, dict(test_cap=0.0, signal=None, kein_testgeld=True))),
    "Hebel: Plan mit Hebeln, Bau wie bisher angesetzt (80/140/280 h)":
        scen(**_mix(PLAN_HEBEL, dict(build_first=(80, 140, 280), build_next=(35, 60, 120),
                                     einmal_stunden=(20, 30, 40)))),
    "Hebel: Plan mit Hebeln im strengeren Markt 2027":
        scen(**_mix(PLAN_HEBEL, MARKT_2027, dict(p_faktor=(0.52, 0.8, 1.2), review_weeks=(0.4, 1.2, 4.0)))),
    "Hebel: DEIN PLAN, aber Stichtag 04.07. nur, wenn noch keine App eingereicht ist (Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, dict(ferienjob=dict(FERIENJOB_FRUEH['ferienjob'],
                                                              frueh_wenn='eingereicht')))),
    "Hebel: DEIN PLAN ohne Stichtag 04.07. (Job erst ab 19.07., Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB)),
    "Hebel: DEIN PLAN mit kurzem Job bis Di 31.08. (Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, dict(ferienjob=dict(FERIENJOB_FRUEH['ferienjob'],
                                                              bis=date(2027, 8, 31))))),
    "Hebel: DEIN PLAN ohne Startpause (eine freigegebene App erscheint auch im Abitur, ohne Arbeit daran)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(startpause=None, signal_pause=STARTPAUSE_NI))),
    "Hebel: nur Ferienjob ab 05.07., keine App, keine Gründung (Vergleich)":
        scen(**_mix(PLAN_HEBEL, dict(ferienjob=dict(FERIENJOB['ferienjob'], ab=date(2027, 7, 5), immer=True),
                                     n_attempts=(0, 0), extra_fix_monat=(0, 0, 0),
                                     gruendung=dict(GRUENDUNG_PLAN, bei=2.0, fix_vorher=(0, 0, 0))))),
    "Hebel: Plan mit Hebeln, falls die zweite Sprache zusätzlich Stunden kostet (+3/+6/+12 h, Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, dict(build_first=(81, 136, 272), build_next=(34, 57, 114)))),
    "Hebel: DEIN PLAN, falls die zweite Sprache zusätzlich Stunden kostet (Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(build_first=(81, 136, 272),
                                                                build_next=(34, 57, 114)))),
    # ---- Gegenproben zur Prüfung vom 25.11. (abends) ----
    "Hebel: DEIN PLAN, App 2 schon während des Reviews von App 1 (ohne Vorlage nach der Freigabe, Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(vorlage_h=None))),
    "Hebel: DEIN PLAN, App 2 im Review von App 1 vorbereiten (bis 6 h ohne Code, Code erst nach der Freigabe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(vorlage_vorab_h=6.0))),
    "Hebel: DEIN PLAN, Posts bis zum Deckel von 10 h je Woche (Obergrenze aus 05, Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(post_deckel=(1.5, 10.0)))),
    "Hebel: DEIN PLAN ohne Wochendeckel für Posts (Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(post_deckel=None))),
    "Hebel: DEIN PLAN, falls die Zeitarbeit ab 05.07. immer klappt (Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, dict(ferienjob=dict(FERIENJOB_FRUEH['ferienjob'], zeitarbeit_p=(1, 1, 1),
                                                              zeitarbeit_vorlauf_p=(1, 1, 1))))),
    # ---- Hebel und Gegenproben zur dritten Prüfung (25.11. spät) ----
    "Hebel: DEIN PLAN mit den alten umsatzabhängigen Kosten (Werbung aus dem Umsatz wie im 500k-Modell, Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(c_organisch=(0.30, 0.45, 0.65)))),
    "Hebel: DEIN PLAN, App 1 um 15 % kleiner (in Version 1.0 nur das Nötigste)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(build_first=(66, 110, 221)))),
    "Hebel: DEIN PLAN, App 1 um 30 % kleiner (kleinste Idee und nur das Nötigste)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(build_first=(55, 91, 182)))),
    "Hebel: DEIN PLAN, App 1 um 15 % kleiner und App 2 im Review vorbereiten":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(build_first=(66, 110, 221), vorlage_vorab_h=6.0))),
    "Hebel: DEIN PLAN mit Ferienjob zum Tariflohn (16,70-18,50 EUR je Stunde)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, dict(ferienjob=dict(FERIENJOB_FRUEH['ferienjob'], netto_woche=(620, 670, 740))))),
    "Hebel: nur Ferienjob zum Tariflohn ab 05.07., keine App (Vergleich)":
        scen(**_mix(PLAN_HEBEL, dict(ferienjob=dict(FERIENJOB['ferienjob'], ab=date(2027, 7, 5), immer=True,
                                                    netto_woche=(620, 670, 740)),
                                     n_attempts=(0, 0), extra_fix_monat=(0, 0, 0),
                                     gruendung=dict(GRUENDUNG_PLAN, bei=2.0, fix_vorher=(0, 0, 0))))),
    "Hebel: DEIN PLAN mit der kürzeren Lernzeit aus 01 (12/18/28 statt 20/28/40 h, Gegenprobe)":
        scen(**_mix(PLAN_HEBEL, RESTWERT, FERIENJOB_FRUEH, dict(einmal_stunden=(12, 18, 28)))),
}


def woche(d: date) -> int:
    return (d - START).days // 7


MEILENSTEINE = (
    ("31.01.", date(2027, 1, 31), 1_000), ("31.01.", date(2027, 1, 31), 5_000),
    ("28.02.", date(2027, 2, 28), 5_000), ("28.02.", date(2027, 2, 28), 10_000),
    ("31.03.", date(2027, 3, 31), 10_000), ("31.03.", date(2027, 3, 31), 30_000),
    ("30.04.", date(2027, 4, 30), 50_000), ("30.04.", date(2027, 4, 30), 100_000),
    ("15.06.", date(2027, 6, 15), 150_000), ("15.07.", date(2027, 7, 15), 300_000),
)


def _bis(chk: dict, w: int) -> float:
    werte = [x for k, x in chk.items() if k <= w]
    return max(werte) if werte else 0.0


def auswerten(P: dict, n: int, seed: int = 2027) -> dict:
    """P(Ziel), Verteilung des Gewinns und P(Ziel | Meilenstein erreicht / verfehlt)."""
    rng = random.Random(seed)
    res = [simulate(rng, P) for _ in range(n)]
    ziel = [r["profit"] + r["exit"] >= P["profit_target"] for r in res]
    # Verluste und Quantile aus Sicht des Gründers (Vermögensänderung, nicht Anteil am Firmengewinn)
    gewinne = sorted(r["ergebnis"] for r in res)
    q = lambda p: gewinne[min(n - 1, int(p * n))]  # noqa: E731
    meilensteine = []
    for name, tag, schwelle in MEILENSTEINE:
        w = bis_woche(tag)
        erreicht = [_bis(r["chk"], w) >= schwelle * FX for r in res]
        m = sum(erreicht)
        treffer = sum(1 for e, z in zip(erreicht, ziel) if e and z)
        sonst = sum(1 for e, z in zip(erreicht, ziel) if (not e) and z)
        meilensteine.append({
            "bis": name, "mrr_usd": schwelle, "p": m / n,
            "p_ziel_wenn": treffer / m if m else None, "treffer": treffer, "n": m,
            "p_ziel_sonst": sonst / (n - m) if n > m else None})
    return {
        "p_ziel": sum(ziel) / n, "n": n, "treffer": sum(ziel),
        "p_gewinn": sum(r["exit"] == 0 and r["profit"] >= P["profit_target"] for r in res) / n,
        "p_verkauf": sum(r["exit"] > 0 and z for r, z in zip(res, ziel)) / n,
        "p_verlust_3000": sum(r["ergebnis"] < -3000 for r in res) / n,
        "p_verlust_5000": sum(r["ergebnis"] < -5000 for r in res) / n,
        "p_nachschuss": sum(r["nachschuss"] > 0 for r in res) / n,
        "p_gestoppt": sum(r["gestoppt"] for r in res) / n,
        "firma_median": sorted(r["profit_firma"] for r in res)[n // 2],
        "p_papier": sum(r["profit"] + r["exit"] + r["paper"] >= P["profit_target"] for r in res) / n,
        "gewinn_median": q(0.5), "gewinn_p10": q(0.1), "gewinn_p90": q(0.9), "gewinn_p99": q(0.99),
        "gewinn_mittel": sum(gewinne) / n,
        "p_plus": sum(r["ergebnis"] > 0 for r in res) / n,
        "p_10k": sum(r["ergebnis"] >= 10_000 for r in res) / n,
        "p_100k": sum(r["ergebnis"] >= 100_000 for r in res) / n,
        "p_mrr_10k": sum(r["max_mrr"] >= 10_000 * FX for r in res) / n,
        "p_mrr_100k": sum(r["max_mrr"] >= 100_000 * FX for r in res) / n,
        "versuche_median": sorted(r["attempts"] for r in res)[n // 2],
        "apps_median": sorted(r["gestartet"] for r in res)[n // 2],
        "p_keine_bis_g3": sum(r["gestartet_g3"] == 0 for r in res) / n,
        "p_eine_bis_g3": sum(r["gestartet_g3"] == 1 for r in res) / n,
        "p_zwei_bis_g3": sum(r["gestartet_g3"] >= 2 for r in res) / n,
        "test_g3_median": sorted(r["testkosten_g3"] for r in res)[n // 2],
        "p_gegruendet": sum(r["gegruendet"] for r in res) / n,
        "p_zu_teuer": sum(r["zu_teuer"] for r in res) / n,
        "erster_launch_woche": sorted(r["launch1"] for r in res)[n // 2],
        "meilensteine": meilensteine,
    }


def _pz(x) -> str:
    if x is None:
        return "    –"
    return f"{100 * x:7.3f} %"


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--n", type=int, default=60_000)
    ap.add_argument("--nur", default=None, help="nur Szenarien, deren Name diesen Text enthält")
    ap.add_argument("--seed", type=int, default=2027, help="Startwert; Szenario i rechnet mit seed + i")
    args = ap.parse_args()
    for i, (name, P) in enumerate(SZENARIEN.items()):
        if args.nur and args.nur not in name:
            continue
        r = auswerten(P, args.n, seed=args.seed + i)
        stichtag = P['test_cap_bis'].strftime('%d.%m.')
        print(f"== {name}  ({args.n} Läufe)")
        print(f"   P(Ziel: Gewinn + Verkauf >= {P['profit_target']:,.0f} EUR)".replace(",", ".")
              + f"  {_pz(r['p_ziel'])}  [{r['treffer']} Treffer]"
              f"   davon ohne Verkauf {_pz(r['p_gewinn'])}   mit Verkauf {_pz(r['p_verkauf'])}"
              f"   mit Papierwert {_pz(r['p_papier'])}")
        print(f"   Verlust > 3.000 EUR {_pz(r['p_verlust_3000'])}   > 5.000 EUR {_pz(r['p_verlust_5000'])}"
              f"   Nachschuss nötig {_pz(r['p_nachschuss'])}   Jagd an einem Tor beendet {_pz(r['p_gestoppt'])}")
        print(f"   Ergebnis > 0 {_pz(r['p_plus'])}   >= 10.000 EUR {_pz(r['p_10k'])}   >= 100.000 EUR {_pz(r['p_100k'])}")
        print(f"   Ergebnis für dich: Median {r['gewinn_median']:,.0f}  P10 {r['gewinn_p10']:,.0f}  "
              f"P90 {r['gewinn_p90']:,.0f}  P99 {r['gewinn_p99']:,.0f}  Mittel {r['gewinn_mittel']:,.0f} EUR"
              f"   (Firma Median {r['firma_median']:,.0f})".replace(",", "."))
        print(f"   MRR >= 10k USD {_pz(r['p_mrr_10k'])}, >= 100k USD {_pz(r['p_mrr_100k'])}; Versuche Median "
              f"{r['versuche_median']}; gestartete Apps bis 31.08. Median {r['apps_median']}; bis {stichtag}: keine "
              f"{_pz(r['p_keine_bis_g3'])}, genau eine {_pz(r['p_eine_bis_g3'])}, zwei oder mehr "
              f"{_pz(r['p_zwei_bis_g3'])}; erster Launch Woche {r['erster_launch_woche']} "
              f"ab 30.11.2026; Tests bis {stichtag} Median {r['test_g3_median']:,.0f} EUR".replace(",", "."))
        for m in r["meilensteine"]:
            print(f"     MRR >= {m['mrr_usd']:>7,} USD bis {m['bis']}: erreicht {_pz(m['p'])}   P(Ziel | erreicht) "
                  f"{_pz(m['p_ziel_wenn'])}   P(Ziel | verfehlt) {_pz(m['p_ziel_sonst'])}   "
                  f"[{m['treffer']}/{m['n']}]".replace(",", "."))


if __name__ == "__main__":
    main()
