#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by module 4 of "Risk, Leverage and Your Own Brain"
(_data/risk4.yml): protective put, fat tails, Value at Risk, margin calls and
peak margin, rebalancing, overtrading.

    python3 scripts/derive_risk4.py        # rewrites _data/risk4.yml

Posts (2026-11-10 .. 2026-11-15).

INPUTS (read-only)
  _data/risk3.yml                     hypothetical "Sample Index" contract and option premiums
  _data/fno.yml                       SEBI's F&O studies (figures already checked there)
  assets/data/nifty50-price-index.csv Yahoo Finance ^NSEI closes (price index)
  assets/data/nifty50-tri.csv         niftyindices.com Nifty 50 TRI
  assets/data/uti-gilt-fund-nav.csv   AMFI via mfapi.in, regular plan growth

HYPOTHETICAL: the Sample Index option premiums (Black-Scholes, 15% vol, 30 days,
zero rate; from risk3), the margin path in the margin-call post, the gross-return
and trade-count grid in the overtrading post. REAL, backward-looking: the Nifty
and gilt-fund series, and SEBI's published study figures.

RULES: the peak-margin post cites the snapshot count and penalty from SEBI's text (read 2 Nov 2026). Sources: SEBI
circular SEBI/HO/MRD2/DCAP/CIR/P/2020/127 of 20 July 2020 and the master circular
of 30 December 2024, Chapters 4 and 5.

LAG: first post 10 November 2026 (cut-off 10 August 2026); all series end 30-31 March 2026.

Needs pandas, numpy, pyyaml.
"""
import math
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "risk4.yml"
FIRST_POST = pd.Timestamp("2026-11-10")


class _NoAlias(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def r(x, nd=1):
    v = round(float(x), nd)
    return int(v) if v == int(v) else v


def d(ts):
    return pd.Timestamp(ts).strftime("%Y-%m-%d")


r3 = yaml.safe_load((ROOT / "_data" / "risk3.yml").read_text())
fno = yaml.safe_load((ROOT / "_data" / "fno.yml").read_text())
nifty = pd.read_csv(ROOT / "assets/data/nifty50-price-index.csv", parse_dates=["date"]).set_index("date")["nifty50_pri_close"].sort_index()
tri = pd.read_csv(ROOT / "assets/data/nifty50-tri.csv", parse_dates=["date"]).set_index("date")["nifty50_tri_close"].sort_index()
gilt = pd.read_csv(ROOT / "assets/data/uti-gilt-fund-nav.csv", parse_dates=["date"]).set_index("date")["nav_regular_growth"].dropna().sort_index()
for name, s in [("nifty", nifty), ("tri", tri), ("gilt", gilt)]:
    assert s.index[-1] <= FIRST_POST - pd.DateOffset(months=3), f"lag rule: {name}"

out = {"dataset": {
    "index_start": d(nifty.index[0]), "index_end": d(nifty.index[-1]), "index_sessions": int(len(nifty)),
    "index_source_url": "https://finance.yahoo.com/quote/%5ENSEI/history/",
    "tri_source": "NSE Indices (niftyindices.com), Nifty 50 Total Returns Index",
    "gilt_source": "UTI Gilt Fund (regular plan, growth), NAV from AMFI via mfapi.in",
}}

# ================================================================ 1. protective put (hypothetical Sample Index)
LEVEL, LOT = r3["contract"]["level"], r3["contract"]["lot"]
ATM_K, ATM_P = r3["contract"]["strike"], r3["contract"]["put_prem"]
OTM_K, OTM_P = r3["breakeven"]["otm"]["put_strike"], r3["breakeven"]["otm"]["put_prem"]
VALUE = LEVEL * LOT
rows = []
for s in [17000, 18000, 19000, 19500, 20000, 21000, 22000, 23000]:
    held = (s - LEVEL) * LOT
    atm = held + max(ATM_K - s, 0) * LOT - ATM_P * LOT
    otm = held + max(OTM_K - s, 0) * LOT - OTM_P * LOT
    rows.append({"level": s, "move_pct": r((s / LEVEL - 1) * 100, 1), "unhedged": int(held),
                 "atm_hedged": int(atm), "otm_hedged": int(otm)})
atm_cost, otm_cost = ATM_P * LOT, OTM_P * LOT
atm_floor = -atm_cost
otm_floor = (OTM_K - LEVEL) * LOT - otm_cost
assert min(x["atm_hedged"] for x in rows) == atm_floor
assert min(x["otm_hedged"] for x in rows) == otm_floor
out["put"] = {
    "level": LEVEL, "lot": LOT, "value": VALUE,
    "atm": {"strike": ATM_K, "prem": ATM_P, "cost": atm_cost, "cost_pct": r(atm_cost / VALUE * 100, 2),
            "worst_loss": -atm_floor, "worst_loss_pct": r(-atm_floor / VALUE * 100, 2),
            "rolled_12x_pct": r(atm_cost / VALUE * 100 * 12, 1)},
    "otm": {"strike": OTM_K, "prem": OTM_P, "cost": otm_cost, "cost_pct": r(otm_cost / VALUE * 100, 2),
            "worst_loss": -otm_floor, "worst_loss_pct": r(-otm_floor / VALUE * 100, 2),
            "rolled_12x_pct": r(otm_cost / VALUE * 100 * 12, 1)},
    "rows": rows, "vol_pct": 15, "days": 30,
    "breakeven_atm_level": LEVEL + ATM_P,
    "breakeven_otm_level": LEVEL + OTM_P,
}

# ================================================================ 2. fat tails (Nifty daily returns)
ret = nifty.pct_change().dropna()
mu, sd = ret.mean(), ret.std()
z = (ret - mu) / sd
n = len(ret)


def normal_two_tail(k):
    return math.erfc(k / math.sqrt(2))      # P(|Z| > k)


tails = []
for k in (3, 4, 5):
    actual = int((z.abs() > k).sum())
    expected = normal_two_tail(k) * n
    tails.append({"k": k, "actual_days": actual, "expected_days": r(expected, 1),
                  "actual_share_pct": r(actual / n * 100, 2), "normal_share_pct": r(normal_two_tail(k) * 100, 3)})
worst = ret.nsmallest(5)
best = ret.nlargest(3)
out["tails"] = {
    "days": int(n), "mean_daily_pct": r(mu * 100, 3), "sd_daily_pct": r(sd * 100, 2), "excess_kurtosis": r(ret.kurt(), 1), "rows": tails,
    "worst": [{"date": d(t), "return_pct": r(v * 100, 1), "sds": r((v - mu) / sd, 1)} for t, v in worst.items()],
    "best": [{"date": d(t), "return_pct": r(v * 100, 1), "sds": r((v - mu) / sd, 1)} for t, v in best.items()],
    "worst_day_normal_odds_text": "once in more than the age of the universe" if normal_two_tail(abs((worst.iloc[0] - mu) / sd)) < 1e-18 else "very rarely",
    "worst_day_normal_prob": f"{normal_two_tail(abs((worst.iloc[0] - mu) / sd)):.1e}",
    "days_beyond_3sd_in_2008_2009_share_pct": r(((z.abs() > 3) & (z.index.year.isin([2008, 2009]))).sum() / max((z.abs() > 3).sum(), 1) * 100, 0),
    "days_beyond_3sd_in_2020_share_pct": r(((z.abs() > 3) & (z.index.year == 2020)).sum() / max((z.abs() > 3).sum(), 1) * 100, 0),
}

# ================================================================ 3. Value at Risk (hypothetical Rs 10 lakh in the Nifty price index)
POS = 1000000
Z95, Z99 = 1.6449, 2.3263
hist95 = -np.percentile(ret, 5) * POS
hist99 = -np.percentile(ret, 1) * POS
par95 = (Z95 * sd - mu) * POS
par99 = (Z99 * sd - mu) * POS
# rolling test: VaR from the previous 250 sessions, normal approximation at 99%
W = 250
roll_sd = ret.rolling(W).std().shift()
roll_mu = ret.rolling(W).mean().shift()
var_line = -(roll_mu - Z99 * roll_sd)           # a positive loss threshold, as a fraction
test = pd.DataFrame({"ret": ret, "var": var_line}).dropna()
_px = (1 + ret).cumprod()
_peak_before = _px.loc[:test.index[0]].iloc[:-1].max()
_prior = _px.loc[:test.index[0]].iloc[-2]
fall_before_test_pct = (_prior / _peak_before - 1) * 100
breach = test["ret"] < -test["var"]
by_year = breach.groupby(test.index.year).sum()
top_year = int(by_year.idxmax())
crisis = test.index.year.isin([2008, 2009, 2020])
hist_line = (-ret.rolling(W).quantile(0.01)).shift()
_t2 = pd.DataFrame({"ret": ret, "v": hist_line}).dropna()
full_line = Z99 * sd - mu
n_months = len(set(zip(test.index.year, test.index.month)))
out["var"] = {
    "position": POS, "window": W, "days_tested": int(len(test)),
    "hist_95": int(round(hist95, -2)), "hist_99": int(round(hist99, -2)),
    "par_95": int(round(par95, -2)), "par_99": int(round(par99, -2)),
    "sd_daily_pct": r(sd * 100, 3), "mean_daily_pct": r(mu * 100, 3), "sd_daily_pct": r(sd * 100, 3), "mean_daily_pct": r(mu * 100, 3),
    "fall_before_test_pct": r(fall_before_test_pct, 0), "test_start": d(test.index[0]), "test_end": d(test.index[-1]), "months_tested": n_months,
    "breaches_crisis_years": int(breach[crisis].sum()), "breach_share_crisis_pct": r(breach[crisis].mean() * 100, 2),
    "breaches_other_years": int(breach[~crisis].sum()), "breach_share_other_pct": r(breach[~crisis].mean() * 100, 2),
    "breach_share_rolling_historical_pct": r((_t2["ret"] < -_t2["v"]).mean() * 100, 2),
    "breach_share_full_sample_normal_pct": r((test["ret"] < -full_line).mean() * 100, 2),
    "by_year": [{"year": int(y), "breaches": int(n)} for y, n in by_year.items()],
    "breaches": int(breach.sum()), "breach_share_pct": r(breach.mean() * 100, 2), "expected_share_pct": 1,
    "expected_days": r(0.01 * len(test), 0),
    "months_with_breach": int(breach[breach].groupby([breach[breach].index.year, breach[breach].index.month]).size().shape[0]),
    "worst_year": top_year, "worst_year_breaches": int(by_year.max()),
    "breaches_2008_2009": int(by_year.reindex([2008, 2009]).fillna(0).sum()),
    "breaches_2020": int(by_year.get(2020, 0)),
    "worst_day_loss": int(round(-ret.min() * POS, -2)),
    "worst_day_vs_hist99_x": r(-ret.min() * POS / hist99, 1),
}

# ================================================================ 4. margin call (hypothetical)
CONTRACT = VALUE                # 15 lakh, same Sample Index lot as risk3
FUNDS = 200000
path = [  # (label, index move %, margin % required at that day's close)
    ("Start of day 1", 0.0, 12.0),
    ("End of day 1", -3.0, 14.0),
    ("End of day 2", -4.0, 17.0),
]
rows_m = []
val = CONTRACT
cum_loss = 0.0
for lab, mv, mp in path:
    if mv:
        loss = val * mv / 100          # a long position in the index (a long future, hypothetical)
        cum_loss += loss
        val += loss
    req = val * mp / 100
    equity = FUNDS + cum_loss
    rows_m.append({"label": lab, "move_pct": mv, "position_value": int(round(val)), "margin_pct": r(mp),
                   "required": int(round(req)), "equity": int(round(equity)),
                   "shortfall": int(round(max(req - equity, 0)))})
peak = {"morning_required": 180000, "spike_required": 230000, "close_required": 180000, "funds": FUNDS}
assert peak["spike_required"] > FUNDS >= peak["close_required"]
out["margin"] = {"contract": CONTRACT, "funds": FUNDS, "rows": rows_m, "peak": peak,
                 "first_shortfall_label": next(x["label"] for x in rows_m if x["shortfall"] > 0)}

# ================================================================ 5. rebalancing (60/40, Nifty TRI and a gilt fund)
W_E = 0.6


def rebalance_window(start_ts):
    st = max(tri.index[0], gilt.index[0], pd.Timestamp(start_ts))
    idx = tri.loc[st:].index.intersection(gilt.loc[st:].index)
    e, g = tri.reindex(idx), gilt.reindex(idx)
    re_, rg = e.pct_change().fillna(0), g.pct_change().fillna(0)

    def run(rebalance):
        we, wg = W_E, 1 - W_E
        path_, last_year = [], idx[0].year
        for t, a, b in zip(idx, re_, rg):
            if rebalance and t.year != last_year:      # first session of a new year: reset to 60/40
                tot = we + wg
                we, wg = tot * W_E, tot * (1 - W_E)
            last_year = t.year
            we *= 1 + a
            wg *= 1 + b
            path_.append(we + wg)
        return pd.Series(path_, index=idx), we / (we + wg)

    s_no, w_no = run(False)
    s_re, w_re = run(True)
    yrs = (idx[-1] - idx[0]).days / 365.25
    dd = lambda s: float((s / s.cummax() - 1).min())
    cagr = lambda s: s.iloc[-1] ** (1 / yrs) - 1
    drift, we, wg, yr_end = [], W_E, 1 - W_E, {}
    for t, a, b in zip(idx, re_, rg):
        we *= 1 + a
        wg *= 1 + b
        yr_end[t.year] = (we, wg)
    for y in sorted(yr_end)[:-1]:
        drift.append({"year": y, "equity_weight_pct": r(yr_end[y][0] / sum(yr_end[y]) * 100, 0)})
    return {
        "start": d(idx[0]), "end": d(idx[-1]), "years": r(yrs, 1),
        "equity_cagr_pct": r(((e.iloc[-1] / e.iloc[0]) ** (1 / yrs) - 1) * 100, 1),
        "gilt_cagr_pct": r(((g.iloc[-1] / g.iloc[0]) ** (1 / yrs) - 1) * 100, 1),
        "none": {"cagr_pct": r(cagr(s_no) * 100, 1), "max_drawdown_pct": r(dd(s_no) * 100, 0),
                 "end_equity_weight_pct": r(w_no * 100, 0), "growth_of_100": r(s_no.iloc[-1] * 100, 0)},
        "annual": {"cagr_pct": r(cagr(s_re) * 100, 1), "max_drawdown_pct": r(dd(s_re) * 100, 0),
                   "end_equity_weight_pct": r(w_re * 100, 0), "growth_of_100": r(s_re.iloc[-1] * 100, 0)},
        "max_equity_weight_pct": r(max(x["equity_weight_pct"] for x in drift), 0),
        "min_equity_weight_pct": r(min(x["equity_weight_pct"] for x in drift), 0),
        "drift_sample": [x for x in drift if x["year"] in (2008, 2009, 2010, 2014, 2020, 2021)],
    }


# start-year scan: annual minus never, in CAGR points, to the same end date; and what the 2008 and 2009 resets did
def _scan(start_ts, skip=(), only=None):
    st = max(tri.index[0], gilt.index[0], pd.Timestamp(start_ts))
    idx = tri.loc[st:].index.intersection(gilt.loc[st:].index)
    a_, b_ = tri.reindex(idx).pct_change().fillna(0), gilt.reindex(idx).pct_change().fillna(0)
    we, wg, n1, n2, last = W_E, 1 - W_E, W_E, 1 - W_E, idx[0].year
    for t, x, y in zip(idx, a_, b_):
        if t.year != last and t.year not in skip and (only is None or t.year in only):
            tot = we + wg
            we, wg = tot * W_E, tot * (1 - W_E)
        last = t.year
        we, wg, n1, n2 = we * (1 + x), wg * (1 + y), n1 * (1 + x), n2 * (1 + y)
    yrs_ = (idx[-1] - idx[0]).days / 365.25
    return ((we + wg) ** (1 / yrs_) - (n1 + n2) ** (1 / yrs_)) * 100


_scan_rows = [{"start_year": y, "annual_minus_never_pp": r(_scan(f"{y}-01-01"), 2)} for y in range(2007, 2022)]
_scan_neg = sum(1 for x in _scan_rows if x["annual_minus_never_pp"] < 0)


def _dd2(start_ts, reb):
    st = max(tri.index[0], gilt.index[0], pd.Timestamp(start_ts))
    idx = tri.loc[st:].index.intersection(gilt.loc[st:].index)
    a_, b_ = tri.reindex(idx).pct_change().fillna(0), gilt.reindex(idx).pct_change().fillna(0)
    we, wg, last, p_ = W_E, 1 - W_E, idx[0].year, []
    for t, x, y in zip(idx, a_, b_):
        if reb and t.year != last:
            tot = we + wg
            we, wg = tot * W_E, tot * (1 - W_E)
        last = t.year
        we, wg = we * (1 + x), wg * (1 + y)
        p_.append(we + wg)
    z = pd.Series(p_)
    return float((z / z.cummax() - 1).min()) * 100


_dd_scan = [{"start_year": y, "never_pct": r(_dd2(f"{y}-01-01", False), 2), "annual_pct": r(_dd2(f"{y}-01-01", True), 2)} for y in range(2010, 2022)]

out["rebalance"] = {
    "target_equity_pct": 60,
    "start_year_scan": _scan_rows, "start_years_negative": _scan_neg, "start_years_total": len(_scan_rows),
    "isolate_2008_2009_only_pp": r(_scan("2006-04-03", only=(2008, 2009)), 2),
    "isolate_all_but_2008_2009_pp": r(_scan("2006-04-03", skip=(2008, 2009)), 2),
    "isolate_2008_only_pp": r(_scan("2006-04-03", only=(2008,)), 2),
    "isolate_2009_only_pp": r(_scan("2006-04-03", only=(2009,)), 2),
    "full_lead_pp": r(_scan("2006-04-03"), 2),
    "drawdown_scan": _dd_scan, "drawdown_scan_starts": len(_dd_scan),
    "drawdown_scan_annual_shallower_or_tied": sum(1 for x in _dd_scan if x["annual_pct"] >= x["never_pct"]),
    "drawdown_scan_max_gap_pp": r(max(x["annual_pct"] - x["never_pct"] for x in _dd_scan), 1),
    "drawdown_scan_exception": next((x for x in _dd_scan if x["annual_pct"] < x["never_pct"]), None),
    "full": rebalance_window("2006-04-03"),
    "from_2010": rebalance_window("2010-01-01"),
    # the textbook arithmetic: 60/40, equity +20%, gilt +5%
    "arith": {"equity_up_pct": 20, "gilt_up_pct": 5,
              "new_equity_weight_pct": r(60 * 1.20 / (60 * 1.20 + 40 * 1.05) * 100, 1),
              "sell_to_reset_pct_of_portfolio": r((60 * 1.20 / (60 * 1.20 + 40 * 1.05) - 0.6) * 100, 1)},
}

# ================================================================ 6. overtrading
GROSS = 12
COST_SIDE = 0.1
grid = []
for ntr in (0, 12, 52, 250):
    net = (1 + GROSS / 100) * (1 - 2 * COST_SIDE / 100) ** ntr - 1
    grid.append({"round_trips": ntr, "net_pct": r(net * 100, 1), "cost_drag_pp": r(GROSS - net * 100, 1)})
fy = fno["fy26_unverified"]
out["overtrading"] = {
    "gross_pct": GROSS, "cost_per_side_pct": COST_SIDE, "grid": grid,
    "sebi": {"loss_pct_fy26": fno["fy26"]["loss_pct"], "aggregate_loss_cr": fno["fy26"]["aggregate_loss_cr"],
             "costs_cr_per_year": fy["transaction_costs_cr_fy26"],
             "costs_share_of_loss_pct": r(fy["transaction_costs_cr_fy26"] / fno["fy26"]["aggregate_loss_cr"] * 100, 0),
             "zero_dte_share_pct": fy["zero_dte_share_of_index_options_turnover_pct"],
             "repeat_loser_pct": fy["repeat_loser_pct"],
             "avg_loss": fy["avg_loss_per_trader"]},
}

header = """# Risk — Module 4 ("Measuring and managing exposure"): every figure quoted in the
# protective put, fat tails, VaR, margin call, rebalancing and overtrading posts.
#
# GENERATED by scripts/derive_risk4.py — do not edit by hand; re-run the script.
# Hypothetical: the Sample Index options, the margin path, the cost grid.
# Real and backward-looking: Nifty / gilt-fund series (end 2026-03-30/31) and SEBI's
# published study figures (carried over from _data/fno.yml).

"""
OUT.write_text(header + yaml.dump(out, Dumper=_NoAlias, sort_keys=False, allow_unicode=True, default_flow_style=False), encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))
