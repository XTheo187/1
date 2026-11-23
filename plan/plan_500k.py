"""500.000 EUR bis 31.08.2027: das Muster der echten Fälle, Woche für Woche gerechnet.

Die belegten Fälle junger Gründer mit >= 500.000 in <= 12-18 Monaten (Cal AI,
Quittr, Summly, Roblox-Hits) folgen einem Muster: eine Consumer-App mit Abo
(KI-Utility, harte Paywall), Vertrieb über Kurzvideos und Creator, Werbung aus
dem laufenden Umsatz bezahlt, viele schnelle Versuche, Vermögen am Ende oft über
einen Verkauf. Dieses Modell rechnet genau diesen Weg für eine 18-Jährige in
Regensburg mit ~5.000 EUR Startkapital und Abitur 2027 (Stundenbudget nach
Kalender, Abitur geschützt):

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

Ziel: Gewinn plus Verkaufserlös (Anteil der Gründerin) >= 720.000 EUR bis 31.08.2027.
In einer UG bleiben davon nach ~30,7 % Steuer (KSt + Soli + GewSt Regensburg 425 %)
~500.000 EUR Eigenkapital; privat verfügbar wären ~965.000-980.000 EUR Gewinn nötig
(als UG wegen der 25-%-Rücklage ohne Kapitalerhöhung sogar ~1,3 Mio. EUR).

Regeln des Plans im Modell: Stunden nach dem Wochenplan (Abiturschutz) abzüglich
Partnersuche, Gründung und Sicherheitsnetz, Tests bis G3 zusammen höchstens 1.500 EUR,
Ausgaben nie unter die Reserve, kein Kredit, keine Fremdfinanzierung, Abbruch der Jagd
an den Toren G3 (28.02.: beste App < 5.000 USD MRR) und G4 (31.03.: < 10.000 USD),
danach keine neuen Versuche, kein Testbudget und nur noch Mindestkosten.

Verluste werden aus Sicht der Gründerin gerechnet: Sie bringt das ganze Geld ein, ein
Partner nur Arbeit; ihr gehört ihr Anteil am Eigenkapital der UG.

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
    agent_bei_treffer=None,            # dict: Agent erst, wenn ein Treffer erkannt ist: h_need, einmal (Stunden über
                                       #       4 Wochen), extra_monat (EUR), pflege (h/Woche)
    partner_vertrag=(0, 0, 0),         # S: Notar/Anwalt fuer Partnervertrag (bei Zusage faellig)
)


def hours_level(d, lv):
    """Arbeitsstunden-Phase der Woche, die am Montag d beginnt (Ferien Bayern 2026/27).

    Weihnachtsferien 24.12.2026-08.01.2027 (die Woche ab 21.12. hat drei Schultage und
    drei Feiertage, sie zaehlt als Schulwoche), Fruehjahrsferien 08.-12.02.2027,
    Osterferien 22.03.-02.04., Pfingstferien 18.-28.05., Abitur bis Mitte Juni.
    """
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


def nebenstunden(d, mit_partner, partnersuche=True):
    """Stunden der Woche ab Montag d, die nicht in Apps fließen (Wochenplan, Abschnitt 4).

    Partnersuche 2,5 h je Woche bis 31.01. (entfällt, sobald ein Partner zugesagt hat oder wer
    bewusst allein arbeitet),
    Gründung, Konten und Ideenvideos vor dem Bau ~10 h (KW 49/50), Sicherheitsnetz
    (Bewerbungen) 12 h in den Weihnachtsferien.
    """
    h = 0.0
    if d < date(2027, 2, 1) and not mit_partner and partnersuche:
        h += 2.5
    if d < date(2026, 12, 14):
        h += 5.0
    if d in (date(2026, 12, 28), date(2027, 1, 4)):
        h += 6.0
    return h


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
    n_max = rng.randint(*P['n_attempts'])
    p1k, p10k, q100k, q1m = t('p1k'), t('p10k'), t('q100k'), t('q1m')
    _pf = t_neu('p_faktor')
    p1k, p10k = min(1.0, p1k * _pf), min(1.0, p10k * _pf)
    p1k = max(p1k, p10k)
    ksk = P['ksk']
    c_g, c_p, c_e = t('c_growth'), t('c_plateau') * (1 + ksk), t('c_early') * (1 + ksk)
    cost_lag = int(round(t('cost_lag_weeks')))
    cost_queue = []
    lag = int(round(t('apple_lag_weeks')))
    web = t('web_share')
    web_net = t('web_net')
    deal_cost = t('deal_cost')
    churn_stop = t('churn_stop')
    fixed_w = (t('fixed_month') + t_neu('extra_fix_monat')) / WPM
    einmal_w = t_neu('einmal_stunden') / 8.0
    pflege_w = t_neu('pflege_h_woche')
    AG = P.get('agent_bei_treffer')
    if AG:
        ag_h_need, ag_einmal = tri(rng, *AG['h_need']), tri(rng, *AG['einmal'])
        ag_extra_w, ag_pflege = tri(rng, *AG['extra_monat']) / WPM, tri(rng, *AG['pflege'])
    agent_aktiv = False
    agent_setup_wochen = 0
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
    g3_woche = bis_woche(date(2027, 2, 28))
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

    cash = P['start_cash'] - t('setup_cost')
    profit = -(P['start_cash'] - cash)  # Gruendungskosten als Aufwand
    nachschuss = 0.0     # privates Geld, das die Gruenderin nachlegen muss, wenn die Kasse leer ist
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

    for w in range(WEEKS):
        d = START + timedelta(weeks=w)
        if d.year == 2027 and (d - timedelta(weeks=1)).year == 2026:
            cum_proceeds_year = 0.0
        if exit_state and exit_state[0] == 'done':
            break
        mit_partner = pw is not None and w >= pw
        hours = hours_level(d, lv) * rng.uniform(0.8, 1.2)
        if P['nebenaufgaben']:
            hours = max(0.0, hours - nebenstunden(d, mit_partner, P.get('partnersuche', True)))
        if w < 8:
            hours = max(0.0, hours - einmal_w)
        if apps and not gestoppt:
            hours = max(0.0, hours - pflege_w)
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
        fix_basis = fixed_stop_w if gestoppt else fixed_w
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
            # Treffer erkannt: jetzt erst Max/Ultra und Agent einrichten (4 Wochen Einrichtung)
            agent_aktiv = True
            agent_setup_wochen = 4
            h_need = ag_h_need
            fixed_w += ag_extra_w
            pflege_w += ag_pflege
        if agent_aktiv and agent_setup_wochen > 0:
            hours = max(0.0, hours - ag_einmal / 4.0)
            agent_setup_wochen -= 1
        # Effort-Faktor fuer das Wachstum grosser Apps: Skalieren braucht h_need Stunden je Woche,
        # ob die App schon als Treffer erkannt ist oder nicht
        eff = min(1.0, (hours + team) / h_need)
        helfer_kosten = 0.0
        if not mit_partner and team > 0 and (
                focus or any(a['peak'] * FX >= 50000 and a['phase'] == 'grow' for a in apps)):
            # Helfer arbeiten am Wachstum einer großen App: bezahlt werden die genutzten Stunden
            helfer_kosten = min(team, max(0.0, h_need - hours)) * team_rate
        if focus:
            # Gruenderin skaliert den Treffer, keine neuen Apps
            h_free = 0.0
        if not focus:
            # 1. Testarbeit (Videos, Creator) für gestartete Apps hat Vorrang
            for tst in tests:
                use = min(h_free, tst[0])
                tst[0] -= use
                h_free -= use
            # 2. Übrige Stunden bauen die nächste App, auch während Review und Test der vorigen
            while h_free > 0:
                if bau is None:
                    if attempts >= n_max:
                        break
                    attempts += 1
                    if gestoppt:
                        bau_nach_stopp += 1
                    if mit_partner:
                        bh = tri(rng, *PP['build_next'])
                    else:
                        bh = t('build_first') if attempts == 1 else t('build_next')
                    bau = [bh, attempts]
                use = min(h_free, bau[0])
                bau[0] -= use
                h_free -= use
                if bau[0] <= 0:
                    # Einreichung im Lauf der Woche: das Review zählt ab der Folgewoche
                    reviews.append([t('review_weeks') + 1.0, bau[1]])
                    bau = None
                else:
                    break
        # Review-Zeit laeuft kalendarisch
        fertig = []
        for rv in reviews:
            rv[0] -= 1.0
            if rv[0] <= 0:
                fertig.append(rv)
        for rv in fertig:
            reviews.remove(rv)
            versuch = rv[1]
            wunsch = t('test_cost') * (1 + ksk)
            if gestoppt:
                cost = 0.0                      # nach dem Tor kein Testbudget mehr
            else:
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
                frei = cash - max(P['reserve'], pflicht) + credit0 - sum(c for (_, c) in cost_queue)
                cost = max(0.0, min(frei, wunsch, deckel))
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
            if cost < 100:
                peak *= 0.5
            if erzwungen and P.get('force_m0'):
                m0 = min(peak, P['force_m0'])
            elif mit_partner:
                m0 = min(peak, tri(rng, *PP['m0']))
            else:
                m0 = min(peak, t('m0'))
            apps.append(dict(peak=peak, R=m0 * FX / WPM if peak >= 1000 else peak * FX / WPM,
                             g=(P['force_g'] if (erzwungen and P.get('force_g')) else t('g_demand')),
                             launch=w, phase='grow',
                             plateau=t('plateau_weeks'), decay=t('decay_month'),
                             killw=(w + rng.randint(4, 40)) if rng.random() < t('p_kill') else None,
                             kdrop=t('kill_drop'), revealed=False, test_end=None))
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
        cost_queue.append((w + cost_lag, cost_plan))
        due_now = sum(c for (wk, c) in cost_queue if wk <= w)   # inkl. dieser Woche bei Ziel 0
        cash += inflow - due_now - fin_cost
        cost_queue = [(wk, c) for (wk, c) in cost_queue if wk > w]
        min_kasse = min(min_kasse, cash)
        if cash < 0 and credit0 <= 0 and not fin_ok:
            # Kasse leer (nur durch Pflichtkosten möglich): die Gründerin legt privat nach
            nachschuss += -cash
            cash = 0.0
        mrr_eur = gross * WPM
        max_mrr = max(max_mrr, mrr_eur)
        best_mrr = max(best_mrr, max((a['R'] for a in apps), default=0.0) * WPM)
        chk[w] = best_mrr
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
                # Verkauf nur, wenn er das Ziel erreicht (Anteil der Gruenderin an Gewinn + Erloes)
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
    # Vermoegensaenderung der Gruenderin: Sie bringt das ganze Geld ein (Rest des Startkapitals als
    # Kapitalruecklage), der Partner nur Arbeit; ihr gehoert der Anteil `share` am Eigenkapital.
    # Ist das Eigenkapital am Ende negativ, zahlt sie die offenen Rechnungen allein. Ein Angel hat
    # die übliche 1x-Liquidationspräferenz ohne Beteiligung: Er bekommt seine Einlage zurück oder
    # seinen Anteil, was mehr ist; der Rest gehört Gründerin (und Partner) im alten Verhältnis.
    einsatz = P['start_cash'] + nachschuss
    eigenkapital = einsatz + angel_geld + profit + exit_value
    s0 = P.get('founder_share', 1.0)
    ekp = max(0.0, eigenkapital)
    angel_teil = max(min(ekp, angel_geld), (1 - share / s0) * ekp) if angel_geld else 0.0
    ergebnis = s0 * (ekp - angel_teil) + min(0.0, eigenkapital) - einsatz
    g3 = bis_woche(date(2027, 2, 28))
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
                offene_versuche=(bau is not None) + len(reviews),
                partner_woche=pw)


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
# sucht die Gründerin einen Business Angel (Eigenkapital gegen 8-25 % der Anteile, S).
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
                extra_fix_monat=(70, 90, 200))
# Stufe 4: Vollabgabe: Claude baut ohne eigene Prüfung, KI-Avatar-Videos statt eigener (kennzeichnungs-
# pflichtig nach Art. 50 KI-VO, gekennzeichnet bis -31,5 % CTR; ein Fall mit 0,4-0,6x ROAS), Wer alles
# abgibt, lernt weniger (Anthropic-RCT 2026: 50 statt 67 %): Lernkurve langsamer.
CLAUDE_4 = dict(CLAUDE_3, build_first=(45, 80, 180), build_next=(18, 35, 75), test_hours=(20, 35, 60),
                h_need=(10, 18, 30), learn=[0.25, 0.50, 0.80, 1.0], p_faktor=(0.6, 0.8, 1.0),
                pflege_h_woche=(0.3, 0.5, 1.0), extra_fix_monat=(110, 130, 240))
# Gestaffelt: Claude schreibt den Code und erklärt ihn (sie prüft mit Checkliste; erste App wie im Plan,
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
    # Verluste und Quantile aus Sicht der Gründerin (Vermögensänderung, nicht Anteil am Firmengewinn)
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
        print(f"== {name}  ({args.n} Läufe)")
        print(f"   P(Ziel: Gewinn + Verkauf >= 720.000 EUR)  {_pz(r['p_ziel'])}  [{r['treffer']} Treffer]"
              f"   davon ohne Verkauf {_pz(r['p_gewinn'])}   mit Verkauf {_pz(r['p_verkauf'])}"
              f"   mit Papierwert {_pz(r['p_papier'])}")
        print(f"   Verlust > 3.000 EUR {_pz(r['p_verlust_3000'])}   > 5.000 EUR {_pz(r['p_verlust_5000'])}"
              f"   Nachschuss nötig {_pz(r['p_nachschuss'])}   Jagd an G3/G4 beendet {_pz(r['p_gestoppt'])}")
        print(f"   Ergebnis > 0 {_pz(r['p_plus'])}   >= 10.000 EUR {_pz(r['p_10k'])}   >= 100.000 EUR {_pz(r['p_100k'])}")
        print(f"   Ergebnis für dich: Median {r['gewinn_median']:,.0f}  P10 {r['gewinn_p10']:,.0f}  "
              f"P90 {r['gewinn_p90']:,.0f}  P99 {r['gewinn_p99']:,.0f}  Mittel {r['gewinn_mittel']:,.0f} EUR"
              f"   (Firma Median {r['firma_median']:,.0f})".replace(",", "."))
        print(f"   MRR >= 10k USD {_pz(r['p_mrr_10k'])}, >= 100k USD {_pz(r['p_mrr_100k'])}; Versuche Median "
              f"{r['versuche_median']}; gestartete Apps bis 31.08. Median {r['apps_median']}; bis 28.02.: keine "
              f"{_pz(r['p_keine_bis_g3'])}, genau eine {_pz(r['p_eine_bis_g3'])}, zwei oder mehr "
              f"{_pz(r['p_zwei_bis_g3'])}; erster Launch Woche {r['erster_launch_woche']} "
              f"ab 30.11.2026; Tests bis G3 Median {r['test_g3_median']:,.0f} EUR".replace(",", "."))
        for m in r["meilensteine"]:
            print(f"     MRR >= {m['mrr_usd']:>7,} USD bis {m['bis']}: erreicht {_pz(m['p'])}   P(Ziel | erreicht) "
                  f"{_pz(m['p_ziel_wenn'])}   P(Ziel | verfehlt) {_pz(m['p_ziel_sonst'])}   "
                  f"[{m['treffer']}/{m['n']}]".replace(",", "."))


if __name__ == "__main__":
    main()
