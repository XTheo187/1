"""500.000 EUR bis 31.08.2027: das Muster der echten Fälle, Woche für Woche gerechnet.

Die belegten Fälle junger Gründer mit >= 500.000 in <= 12-18 Monaten (Cal AI,
Quittr, Summly, Roblox-Hits) folgen einem Muster: eine Consumer-App mit Abo
(KI-Utility, harte Paywall), Vertrieb über Kurzvideos und Creator, Werbung aus
dem laufenden Umsatz bezahlt, viele schnelle Versuche, Vermögen am Ende oft über
einen Verkauf. Dieses Modell rechnet genau diesen Weg für eine 18-Jährige in
Regensburg mit ~5.000 EUR Startkapital und Abitur 2027 (Stundenbudget nach
Kalender, Abitur geschützt):

- nacheinander 3-8 Apps (Bau, App Review, Test mit Kurzvideos und Creatorn),
- je App eine latente Spitzen-MRR (Stufen 1k/10k/100k/1 Mio. USD, darüber Pareto),
- Wachstum eines Treffers bis zur Spitze, Plateau, Abfall, Risiko eines Einbruchs,
- Kosten (Creator, UGC, später Paid Ads), Apple-Gebühr 15 % bzw. 30 %,
- Cashflow: Apple zahlt 5-9 Wochen später, Werbung ist sofort fällig; Wachstum
  wird gedrosselt, wenn das Geld fehlt (US-Web-Checkout verkürzt den Verzug),
- Verkauf der App ab 16 Wochen Alter zum Vielfachen des Gewinns.

Ziel: Gewinn plus Verkaufserlös (Anteil der Gründerin) >= 720.000 EUR bis 31.08.2027.
In einer UG bleiben davon nach ~30,7 % Steuer (KSt + Soli + GewSt Regensburg 425 %)
~500.000 EUR Eigenkapital; privat verfügbar wären ~930.000-980.000 EUR nötig.

Herkunft: Recherche-Runde zum 500k-Plan (Modell der Recherche, strengere
Kalibrierung und Lernkurve aus der Gegenprüfung). B = belegt, S = Schätzung.

Aufruf:

    python3 plan/plan_500k.py                 # Szenarien und Meilensteine (60.000 Läufe)
    python3 plan/plan_500k.py --n 300000      # genauer (Minuten)

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
    setup_cost=(400, 700, 1200),       # S: UG-Gruendung Notar/HR, Apple 99 USD, Tools
    fixed_month=(250, 450, 800),       # S: Steuerberater, Tools, Server, Versicherung
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
    # Erfolgswahrscheinlichkeit je Versuch (Spitzen-MRR), mit Unsicherheit je Lauf
    p1k=(0.15, 0.25, 0.40),            # S, Basis RevenueCat 2026: 17,3 % neuer Apps >=1k in 2 J.
    p10k=(0.03, 0.07, 0.15),           # S, Basis RevenueCat 2026: 4,6 % >=10k in 2 J.
    q100k=(0.10, 0.20, 0.30),          # S, P(>=100k | >=10k); RevenueCat: ~25 % von 1k->10k
    q1m=(0.05, 0.12, 0.20),            # S, P(>=1M | >=100k)
    pareto_alpha=1.5,                  # S, Spitzen-MRR oberhalb 1 Mio USD
    # Wachstum
    m0=(1000, 3000, 8000),             # S: MRR (USD) in den ersten Wochen eines Treffers
    g_demand=(1.5, 2.2, 3.0),          # S/B: Monatsfaktor; Cal AI 30k->100k->300k->500k->1M (M1-M6)
    h_need=(15, 25, 35),               # S: Stunden/Woche, die Skalierung braucht
    team_threshold=20000.0,            # S: ab 20k EUR MRR Freelancer/Creator-Manager
    team_hours=(10, 20, 40),           # S
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
    c_plateau=(0.35, 0.47, 0.60),      # S/B: Umax ~5 Mio USD Umsatz, >100k USD/Monat Gewinn
    apple_low=0.15, apple_high=0.30,   # B: Small Business Program, 30 % ueber 1 Mio USD Proceeds
    apple_threshold_eur=870000.0,      # B: 1 Mio USD Proceeds je Kalenderjahr (x FX)
    # Cashflow
    apple_lag_weeks=(5, 7, 9),         # B/S: Zahlung ~33-45 Tage nach Ende des Fiskalmonats
    web_share=(0.0, 0.10, 0.30),       # S: Web-Checkout (Stripe) USA, Lag ~1 Woche
    credit0=(1000, 2000, 5000),        # S: Kreditkarte / Werbekonto-Schwelle
    fin_weeks=(13, 20, 26),            # B/S: Silvr DE: 6 Monate Historie, >=10k EUR/Monat
    p_fin=(0.2, 0.4, 0.6),             # S: Zusage fuer junge UG
    fin_k=(0.5, 1.0, 2.0),             # S: Kreditrahmen in Monatsumsaetzen
    fin_fee_month=0.015,               # S
    # Exit
    exit_min_age_weeks=16,             # S: Kaeufer wollen mind. ~4 Monate Daten
    exit_multiple=(1.0, 2.0, 3.5),     # S/B: Flippa H1 2026 Apps 2,62x Jahresgewinn (Schnitt),
                                       #      FE Intl. 3,5-6x bei belegter Retention; Abschlag <1 J.
    exit_close_weeks=(4, 8, 14),       # B: FE Intl. 4-8 Wo. (<500k), 3-6 Mon. (1-10 Mio)
    p_close=(0.3, 0.5, 0.7),           # S
    angel=False,                       # Szenario: Business Angel / Pre-Seed bei Traktion
    angel_trigger_mrr=20000.0,         # S: ab 20k EUR MRR ueber 4 Wochen
    p_angel=(0.2, 0.4, 0.6),           # S
    angel_amount=(50000, 100000, 250000),  # S
    angel_dilution=(0.08, 0.15, 0.25),  # S
    angel_delay_weeks=(3, 6, 10),      # S
    profit_target=720000.0,
    exit_target=700000.0,
)


def hours_level(d, lv):
    """Arbeitsstunden-Phase nach Kalender (Ferien Bayern ungefaehr)."""
    if d < date(2026, 12, 21):
        return lv['h_school']
    if d < date(2027, 1, 11):
        return lv['h_holiday']
    if d < date(2027, 2, 15):
        return lv['h_school']
    if d < date(2027, 2, 22):
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


def draw_peak(rng, p1k, p10k, q100k, q1m, alpha):
    """Latente Spitzen-MRR in USD."""
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
    return rng.uniform(0, 1000)


def simulate(rng, P):
    t = lambda k: tri(rng, *P[k])
    lv = {k: t(k) for k in ('h_school', 'h_holiday', 'h_abiprep', 'h_abi',
                            'h_oral', 'h_gap', 'h_full')}
    n_max = rng.randint(*P['n_attempts'])
    p1k, p10k, q100k, q1m = t('p1k'), t('p10k'), t('q100k'), t('q1m')
    p1k = max(p1k, p10k)
    c_g, c_p, c_e = t('c_growth'), t('c_plateau'), t('c_early')
    cost_lag = int(round(t('cost_lag_weeks')))
    cost_queue = []
    lag = int(round(t('apple_lag_weeks')))
    web = t('web_share')
    fixed_w = t('fixed_month') / WPM
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
    angel_state = None   # None | ('pending', week, amount, dil) | 'done' | 'no'
    weeks_over_20k = 0

    cash = P['start_cash'] - t('setup_cost')
    profit = -(P['start_cash'] - cash)  # Gruendungskosten als Aufwand
    apps = []
    attempts = 0
    task = None   # [kind, remaining_hours, min_weeks_left]
    focus = False
    rev_hist = []        # Bruttoumsatz je Woche (EUR), gesamt
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
        hours = hours_level(d, lv) * rng.uniform(0.8, 1.2)
        if exit_state and exit_state[0] == 'done':
            break
        # ---------------- App-Arbeit (neue Versuche) ----------------
        mrr_now = sum(a['R'] for a in apps) * WPM
        team = team_h if mrr_now >= P['team_threshold'] else 0.0
        h_free = hours
        hit = [a for a in apps if a['peak'] * FX >= 50000 and a['revealed']]
        if hit:
            focus = True
        if focus:
            # Gruenderin skaliert den Treffer; Effort-Faktor fuer Wachstum
            eff = min(1.0, (hours + team) / h_need)
            h_free = 0.0
        else:
            eff = 1.0
        while h_free > 0 and not focus:
            if task is None:
                if attempts >= n_max:
                    break
                attempts += 1
                bh = t('build_first') if attempts == 1 else t('build_next')
                task = ['build', bh, 0.0]
            if task[0] == 'build':
                use = min(h_free, task[1])
                task[1] -= use
                h_free -= use
                if task[1] <= 0:
                    task = ['review', 0.0, t('review_weeks')]
                else:
                    break
            if task[0] == 'review':
                break
            if task[0] == 'test':
                use = min(h_free, task[1])
                task[1] -= use
                h_free -= use
                break
        # Review-Zeit laeuft kalendarisch
        if task and task[0] == 'review':
            task[2] -= 1.0
            if task[2] <= 0:
                cost = min(max(cash + credit0, 0.0), t('test_cost'))
                cash -= cost
                profit -= cost
                _lf = P.get('learn'); _f = _lf[min(attempts - 1, len(_lf) - 1)] if _lf else 1.0
                peak = draw_peak(rng, p1k * _f, p10k * _f, q100k, q1m, P['pareto_alpha'])
                if attempts == P.get('force_attempt', 1) and P.get('force_first_peak'):
                    peak = P['force_first_peak']
                if cost < 100:
                    peak *= 0.5
                m0 = min(peak, P['force_m0'] if (attempts == P.get('force_attempt', 1) and P.get('force_m0')) else t('m0'))
                apps.append(dict(peak=peak, R=m0 * FX / WPM if peak >= 1000 else peak * FX / WPM,
                                 g=(P['force_g'] if (attempts == P.get('force_attempt', 1) and P.get('force_g')) else t('g_demand')),
                                 launch=w, phase='grow',
                                 plateau=t('plateau_weeks'), decay=t('decay_month'),
                                 killw=(w + rng.randint(4, 40)) if rng.random() < t('p_kill') else None,
                                 kdrop=t('kill_drop'), revealed=False, test_end=None))
                task = ['test', t('test_hours'), t('test_min_weeks')]
        if task and task[0] == 'test':
            task[2] -= 1.0
            if task[1] <= 0 and task[2] <= 0:
                apps[-1]['revealed'] = True
                task = None
        # ---------------- Umsatzdynamik ----------------
        planned = []
        for a in apps:
            if a['launch'] == w:
                planned.append(a['R'])
                continue
            R = a['R']
            if a['phase'] == 'grow':
                gw = a['g'] ** (1 / WPM)
                e = eff if (focus and a['peak'] * FX >= 50000) else 1.0
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
        grow_mask = [a['phase'] == 'grow' for a in apps]
        def cshare(Rn, gm):
            if not gm:
                return c_p
            return c_e if Rn * WPM < 100000 * FX else c_g
        cost_plan = sum(Rn * cshare(Rn, gm) for Rn, gm in zip(planned, grow_mask)) + fixed_w
        # Zufluss
        inflow = 0.0
        if len(rev_hist) >= lag:
            inflow += rev_hist[-lag][1] * (1 - web)
        if rev_hist:
            inflow += rev_hist[-1][0] * web * 0.95
        mrr_eur = sum(planned) * WPM
        if mrr_eur >= 10000:
            weeks_over_10k += 1
        floor = -credit0
        if fin_ok and weeks_over_10k >= fin_weeks:
            floor = -credit0 - fin_k * mrr_eur
        due_old = sum(c for (wk, c) in cost_queue if wk <= w)
        avail = cash + inflow - floor - due_old
        # Kosten dieser Woche werden erst nach cost_lag faellig; Limit: kuenftige Faelligkeiten
        pending = sum(c for (wk, c) in cost_queue if wk > w)
        avail_future = avail - pending + inflow * cost_lag
        if not no_cash_limit and cost_plan > avail_future and any(grow_mask):
            # Wachstum drosseln: wachsende Apps bleiben auf Vorwochenniveau
            cash_squeeze += 1
            for i, a in enumerate(apps):
                if grow_mask[i] and a['launch'] != w:
                    planned[i] = min(planned[i], a['R'])
            cost_plan = sum(Rn * cshare(Rn, gm) for Rn, gm in zip(planned, grow_mask)) + fixed_w
            if cost_plan > avail_future:
                # Nur Erhaltungsbudget
                cost_plan = sum(Rn * c_p for Rn in planned) + fixed_w
        for i, a in enumerate(apps):
            a['R'] = planned[i]
        gross = sum(planned)
        fee = P['apple_low'] if cum_proceeds_year < P['apple_threshold_eur'] else P['apple_high']
        apple_part = gross * (1 - web)
        proceeds = apple_part * (1 - fee)
        cum_proceeds_year += proceeds
        rev_hist.append((gross, proceeds))
        fin_cost = (-credit0 - cash) * P['fin_fee_month'] / WPM if cash < -credit0 else 0.0
        wk_profit = proceeds + gross * web * 0.95 - cost_plan - fin_cost
        profit += wk_profit
        profit_hist.append(wk_profit)
        cost_queue.append((w + cost_lag, cost_plan))
        cash += inflow - due_old - fin_cost
        cost_queue = [(wk, c) for (wk, c) in cost_queue if wk > w]
        mrr_eur = gross * WPM
        max_mrr = max(max_mrr, mrr_eur)
        chk[w] = max_mrr
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
                val = mult * 4 * p13
                close_w = w + int(round(t('exit_close_weeks')))
                if val >= P['exit_target'] and close_w < WEEKS:
                    exit_state = ('listing', close_w, val)
        elif exit_state and exit_state[0] == 'listing' and w >= exit_state[1]:
            p13 = sum(profit_hist[-13:])
            val = min(exit_state[2], mult * 4 * p13)
            if rng.random() < p_close and val >= P['exit_target']:
                exit_state = ('done', val)
                exit_value = val
            else:
                exit_state = None
                relist_after = w + 4
    p13 = sum(profit_hist[-13:]) if profit_hist else 0.0
    paper = max(0.0, 2.0 * 4 * p13) if exit_value == 0 else 0.0
    return dict(launch1=(apps[0]['launch'] if apps else 99), profit=profit * share,
                exit=exit_value * share, paper=paper * share, attempts=attempts,
                max_mrr=max_mrr, f10=first10k_week, f100=first100k_week,
                squeeze=cash_squeeze, peaks=[a['peak'] for a in apps], chk=chk)


def run(P, N, seed=1):
    rng = random.Random(seed)
    res = [simulate(rng, P) for _ in range(N)]
    A = sum(r['profit'] >= P['profit_target'] for r in res) / N
    B = sum(r['exit'] >= P['exit_target'] for r in res) / N
    C = sum(r['profit'] + r['exit'] >= P['profit_target'] for r in res) / N
    D = sum(r['profit'] + r['exit'] + r['paper'] >= P['profit_target'] for r in res) / N
    prof = sorted(r['profit'] for r in res)
    q = lambda p: prof[min(N - 1, int(p * N))]
    m10 = sum(r['max_mrr'] >= 10000 * FX for r in res) / N
    m100 = sum(r['max_mrr'] >= 100000 * FX for r in res) / N
    m1m = sum(r['max_mrr'] >= 1e6 * FX for r in res) / N
    lat100 = sum(any(p >= 1e5 for p in r['peaks']) for r in res) / N
    f10 = sorted(r['f10'] for r in res if r['f10'] is not None)
    att = sorted(r['attempts'] for r in res)
    sq = [r['squeeze'] for r in res if r['max_mrr'] >= 50000]
    out = dict(A_profit=A, B_exit=B, C_combo=C, D_paper=D,
               p50=q(0.5), p90=q(0.9), p99=q(0.99), p999=q(0.999),
               mrr10k=m10, mrr100k=m100, mrr1m=m1m, latent100k=lat100,
               f10_median_week=(f10[len(f10) // 2] if f10 else None),
               f100_median_week=(sorted(r['f100'] for r in res if r['f100'] is not None)[sum(r['f100'] is not None for r in res) // 2] if any(r['f100'] is not None for r in res) else None),
               first_launch_median_week=sorted(r['launch1'] for r in res)[N // 2],
               mean_profit=sum(prof) / N,
               attempts_median=att[N // 2], attempts_p10=att[N // 10], attempts_p90=att[9 * N // 10],
               squeeze_weeks_median_hits=(sorted(sq)[len(sq) // 2] if sq else None))
    return out


def scen(**kw):
    P = dict(BASE)
    P.update(kw)
    return P


# --------------------------------------------------------------------------
# Szenarien
# --------------------------------------------------------------------------

# Strengere Trefferquoten (Gegenprüfung): RevenueCat 4,6 % der neuen Apps >= 10k USD MRR in zwei
# Jahren, 2026/27 deutlich mehr Konkurrenz (14.700 neue Abo-Apps im Januar 2026), Appfigures-Tail dünn
KRITIKER = dict(p1k=(0.10, 0.18, 0.30), p10k=(0.02, 0.04, 0.08), q100k=(0.05, 0.12, 0.22),
                q1m=(0.03, 0.08, 0.15))
# Lernkurve: Treffer kommen selten beim ersten Versuch (Cal AI war die 7. App, Halo AI nach 18 Monaten)
LERNKURVE = [0.3, 0.6, 0.85, 1.0]
# Der Plan: Vorlagen-Code und schnelle MVPs, US-Web-Checkout 30-60 %, Ferien voll genutzt
BESTER_PLAN = dict(KRITIKER, learn=LERNKURVE, web_share=(0.3, 0.45, 0.6), build_first=(50, 80, 130),
                   build_next=(25, 45, 70), h_holiday=(25, 38, 50))
# Partner mit Vertrieb (Creator-Netzwerk, Playbook) – Wirkung geschätzt
PARTNER = dict(p1k=(0.15, 0.25, 0.40), p10k=(0.03, 0.065, 0.13), q100k=(0.07, 0.15, 0.25),
               q1m=(0.03, 0.08, 0.15), m0=(2000, 5000, 12000), c_early=(0.25, 0.38, 0.55),
               web_share=(0.15, 0.30, 0.50), team_hours=(20, 30, 50),
               build_first=(40, 70, 120), build_next=(25, 45, 70))

SZENARIEN = {
    "Recherche-Basis (Trefferquoten der Recherche)": scen(),
    "Strengere Quoten (Gegenprüfung)": scen(**KRITIKER),
    "Strengere Quoten + Lernkurve": scen(**KRITIKER, learn=LERNKURVE),
    "DER PLAN: strengere Quoten + Lernkurve + Web-Checkout + schneller Bau": scen(**BESTER_PLAN),
    "Der Plan, optimistischer Rand (Quoten x1,5)": scen(**dict(
        BESTER_PLAN, p1k=(0.15, 0.27, 0.45), p10k=(0.03, 0.06, 0.12), q100k=(0.08, 0.18, 0.33),
        q1m=(0.05, 0.12, 0.22))),
    "Partner mit Vertrieb, Anteil der Gründerin 100 %": scen(**PARTNER, founder_share=1.0),
    "Partner mit Vertrieb, Anteil der Gründerin 75 %": scen(**PARTNER, founder_share=0.75),
    "Partner mit Vertrieb, Anteil der Gründerin 60 %": scen(**PARTNER, founder_share=0.6),
    "Obergrenze: erste App ist ein Cal-AI-Treffer (Start 30k, Spitze 1,5 Mio. USD MRR)": scen(
        force_first_peak=1.5e6, force_g=3.0, force_m0=30000),
    "Der Plan mit strengem Abiturschutz (Schulwochen 6-10 h statt 8-22 h)": scen(**dict(
        BESTER_PLAN, h_school=(6, 8, 10))),
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
    gewinne = sorted(r["profit"] for r in res)
    q = lambda p: gewinne[min(n - 1, int(p * n))]  # noqa: E731
    meilensteine = []
    for name, tag, schwelle in MEILENSTEINE:
        w = woche(tag)
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
        "p_gewinn": sum(r["profit"] >= P["profit_target"] for r in res) / n,
        "p_verkauf": sum(r["exit"] >= P["exit_target"] for r in res) / n,
        "p_papier": sum(r["profit"] + r["exit"] + r["paper"] >= P["profit_target"] for r in res) / n,
        "gewinn_median": q(0.5), "gewinn_p10": q(0.1), "gewinn_p90": q(0.9), "gewinn_p99": q(0.99),
        "gewinn_mittel": sum(gewinne) / n,
        "p_mrr_10k": sum(r["max_mrr"] >= 10_000 * FX for r in res) / n,
        "p_mrr_100k": sum(r["max_mrr"] >= 100_000 * FX for r in res) / n,
        "versuche_median": sorted(r["attempts"] for r in res)[n // 2],
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
    args = ap.parse_args()
    for i, (name, P) in enumerate(SZENARIEN.items()):
        if args.nur and args.nur not in name:
            continue
        r = auswerten(P, args.n, seed=2027 + i)
        print(f"== {name}  ({args.n} Läufe)")
        print(f"   P(Ziel: Gewinn + Verkauf >= 720.000 EUR)  {_pz(r['p_ziel'])}  [{r['treffer']} Treffer]"
              f"   Gewinn allein >= 720.000 {_pz(r['p_gewinn'])}   Verkaufsanteil allein >= 700.000 {_pz(r['p_verkauf'])}"
              f"   mit Papierwert {_pz(r['p_papier'])}")
        print(f"   Gewinn: Median {r['gewinn_median']:,.0f}  P10 {r['gewinn_p10']:,.0f}  P90 {r['gewinn_p90']:,.0f}  "
              f"P99 {r['gewinn_p99']:,.0f}  Mittel {r['gewinn_mittel']:,.0f} EUR".replace(",", "."))
        print(f"   MRR >= 10k USD {_pz(r['p_mrr_10k'])}, >= 100k USD {_pz(r['p_mrr_100k'])}; Versuche Median "
              f"{r['versuche_median']}; erster Launch Woche {r['erster_launch_woche']} ab 30.11.2026")
        for m in r["meilensteine"]:
            print(f"     MRR >= {m['mrr_usd']:>7,} USD bis {m['bis']}: erreicht {_pz(m['p'])}   P(Ziel | erreicht) "
                  f"{_pz(m['p_ziel_wenn'])}   P(Ziel | verfehlt) {_pz(m['p_ziel_sonst'])}   "
                  f"[{m['treffer']}/{m['n']}]".replace(",", "."))


if __name__ == "__main__":
    main()
