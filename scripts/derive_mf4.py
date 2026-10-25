#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by the Mutual Funds, Minus the Marketing — Module 4
posts (capture ratios, Sortino and information ratio, portfolio turnover,
survivorship bias, liquid and overnight funds, growth vs IDCW) and write them
to _data/mf4.yml.

    python3 scripts/derive_mf4.py          # rewrites _data/mf4.yml

Every number a post renders comes from _data/mf4.yml. Market figures are
COMPUTED here from the committed CSVs; regulatory facts are TYPED ONCE below,
each next to the primary source it was read from. Illustrative inputs for
generic funds (turnover, IDCW) and the survivorship simulation are labelled as
such in the output.

INPUTS (all end on or before 31 March 2026; the first Module 4 post publishes
26 October 2026, so the 3-month cutoff is 26 July 2026):
  assets/data/nifty50-tri.csv        Nifty 50 total return index (TRI), daily, from NSE Indices'
                                     historical-data service (niftyindices.com), fetched 25 Oct 2026.
                                     2006-01-02 to 2026-03-30.
  assets/data/nifty50-price-index.csv  Nifty 50 price index (PRI), Yahoo Finance ^NSEI (existing)
  assets/data/uti-nifty50-index-fund-nav.csv     UTI Nifty 50 Index Fund, AMFI via mfapi.in (direct growth, 120716)
  assets/data/uti-aggressive-hybrid-fund-nav.csv UTI Aggressive Hybrid Fund (direct growth, 120674)
  assets/data/uti-overnight-fund-nav.csv         UTI Overnight Fund, regular growth (face value Rs 10 -> Rs 1,000 on 3 May 2018, spliced)
  assets/data/uti-money-market-fund-nav.csv      UTI Money Market Fund, regular growth (face value change 22 Aug 2009, spliced)
  assets/data/uti-gilt-fund-nav.csv              UTI Gilt Fund, regular growth
  assets/data/uti-liquid-fund-nav.csv            UTI Liquid Fund, regular growth (102012); AMFI via mfapi.in, fetched 25 Oct 2026, truncated 31 Mar 2026
  _data/mf2.yml                                  ETF payout estimate of 25 Feb 2021 (derive_mf2.py)

COMPLIANCE: every named fund is used only to show a mechanism. Nothing here
ranks funds, compares managers or assesses whether any fund is worth owning.

Requires pandas, numpy, pyyaml.
"""
import math
import os

import numpy as np
import pandas as pd
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "assets", "data")
OUT = os.path.join(ROOT, "_data", "mf4.yml")
END = "2026-03-31"
TD = 252
RF = 0.065  # same risk-free rate as the Sharpe post (_data/mf.yml volatility_and_sharpe.risk_free_pct)


# ----------------------------------------------------------------- helpers
def load(name, col):
    df = pd.read_csv(os.path.join(DATA, name), parse_dates=["date"]).set_index("date")
    return df[col].dropna().sort_index()


def fix_face_value(s, threshold=0.5):
    """Splice out face-value changes (any one-day move > 50%), rescaling earlier NAVs."""
    s = s.copy()
    r = s.pct_change()
    for dt in r[r.abs() > threshold].index:
        prev = s.loc[:dt].iloc[-2]
        s.loc[s.index < dt] = s.loc[s.index < dt] * (s.loc[dt] / prev)
    return s


def r2(x, n=2):
    if x is None:
        return None
    v = round(float(x), n)
    return int(v) if v == int(v) else v


def ymd(ts):
    return pd.Timestamp(ts).strftime("%Y-%m-%d")


def cagr(s):
    yrs = (s.index[-1] - s.index[0]).days / 365.25
    return (s.iloc[-1] / s.iloc[0]) ** (1 / yrs) - 1


def month_end(s):
    return s.groupby(s.index.to_period("M")).last()


def window_return(s, start, end):
    assert s.index[0] <= pd.Timestamp(start), (s.name, start)
    return (s.loc[:end].iloc[-1] / s.loc[:start].iloc[-1] - 1) * 100


def max_drawdown(s):
    dd = s / s.cummax() - 1
    trough = dd.idxmin()
    peak = s.loc[:trough].idxmax()
    rec = s.loc[trough:]
    rec = rec[rec >= s[peak]]
    return {"pct": r2(dd.min() * 100, 2), "peak_date": ymd(peak), "trough_date": ymd(trough),
            "recovered_date": ymd(rec.index[0]) if len(rec) else None}


# ----------------------------------------------------------------- inputs
tri = load("nifty50-tri.csv", "nifty50_tri_close")
pri = load("nifty50-price-index.csv", "nifty50_pri_close")
idx_fund = load("uti-nifty50-index-fund-nav.csv", "nav_direct_growth")
hybrid = load("uti-aggressive-hybrid-fund-nav.csv", "nav_direct_growth")
overnight = fix_face_value(load("uti-overnight-fund-nav.csv", "nav_regular_growth"))
money = fix_face_value(load("uti-money-market-fund-nav.csv", "nav_regular_growth"))
gilt = load("uti-gilt-fund-nav.csv", "nav_regular_growth")
liquid = load("uti-liquid-fund-nav.csv", "nav_regular_growth")
for s in (tri, pri, idx_fund, hybrid, overnight, money, gilt, liquid):
    assert s.index[-1] <= pd.Timestamp(END), (s.name, s.index[-1])
idx_fund, hybrid = fix_face_value(idx_fund), fix_face_value(hybrid)

# TRI sanity: a total-return index must out-run the price index on the same days,
# and its daily returns must track the price index closely.
_j = pd.concat([tri, pri], axis=1, join="inner").dropna()
_j.columns = ["tri", "pri"]
_r = _j.pct_change().dropna()
assert _r.corr().iloc[0, 1] > 0.999
assert _j.tri.iloc[-1] / _j.pri.iloc[-1] > _j.tri.iloc[0] / _j.pri.iloc[0]
tri_vs_pri_gap = (cagr(_j.tri) - cagr(_j.pri)) * 100

out = {
    "_note": "GENERATED by scripts/derive_mf4.py from the CSVs in assets/data/ and the sourced facts typed in the script. Do not edit by hand.",
}

# ------------------------------------------------- 0. sources and TRI check
out["sources"] = {
    "label": "AMFI NAV history via mfapi.in; Nifty 50 TRI from NSE Indices; Nifty 50 PRI from Yahoo Finance",
    "end": END,
    "lag_note": "Every NAV and index series ends 30 or 31 March 2026; the first Module 4 post publishes 26 October 2026, so the 3-month cutoff is 26 July 2026.",
    "tri": {
        "name": "Nifty 50 Total Returns Index (TRI)",
        "source": "NSE Indices Ltd, historical data service",
        "url": "https://niftyindices.com/reports/historical-data",
        "fetched": "2026-10-25",
        "csv": "/assets/data/nifty50-tri.csv",
        "start": ymd(tri.index[0]),
        "end": ymd(tri.index[-1]),
        "days": int(len(tri)),
        "overlap_days_with_pri": int(len(_j)),
        "daily_return_correlation_with_pri": r2(_r.corr().iloc[0, 1], 5),
        "tri_minus_pri_cagr_pts": r2(tri_vs_pri_gap, 2),
        "tri_minus_pri_window": f"{ymd(_j.index[0])} to {ymd(_j.index[-1])}",
    },
    "funds": {
        "index_fund": {"name": "UTI Nifty 50 Index Fund", "plan": "direct growth", "code": 120716},
        "hybrid": {"name": "UTI Aggressive Hybrid Fund", "plan": "direct growth", "code": 120674},
        "overnight": {"name": "UTI Overnight Fund", "plan": "regular growth", "code": 100814},
        "money_market": {"name": "UTI Money Market Fund", "plan": "regular growth"},
        "gilt": {"name": "UTI Gilt Fund", "plan": "regular growth"},
        "liquid": {"name": "UTI Liquid Fund", "plan": "regular growth", "code": 102012},
    },
}

# ------------------------------------------------- 1. capture ratios
def capture_stats(fund_m, bm_m):
    """fund_m, bm_m: month-end series covering base month + the months to score."""
    f = fund_m.pct_change().dropna()
    b = bm_m.pct_change().dropna()
    j = pd.concat([f, b], axis=1, join="inner").dropna()
    j.columns = ["f", "b"]
    up, dn = j[j.b > 0], j[j.b < 0]
    zero = int((j.b == 0).sum())

    def comp_cap(d):
        n = len(d)
        fa = (1 + d.f).prod() ** (12 / n) - 1
        ba = (1 + d.b).prod() ** (12 / n) - 1
        return fa / ba * 100

    # Averages are stored to 3 decimals and the capture ratios computed FROM those, so the table reproduces on a calculator.
    fu, bu = r2(up.f.mean() * 100, 3), r2(up.b.mean() * 100, 3)
    fd, bd = r2(dn.f.mean() * 100, 3), r2(dn.b.mean() * 100, 3)
    res = {
        "months": int(len(j)), "up_months": int(len(up)), "down_months": int(len(dn)), "zero_months": zero,
        "first_month": str(j.index[0]), "last_month": str(j.index[-1]),
        "up_capture_avg": r2(fu / bu * 100, 1), "down_capture_avg": r2(fd / bd * 100, 1),
        "up_capture_comp": r2(comp_cap(up), 1), "down_capture_comp": r2(comp_cap(dn), 1),
        "bm_avg_up_month_pct": bu, "bm_avg_down_month_pct": bd,
        "fund_avg_up_month_pct": fu, "fund_avg_down_month_pct": fd,
    }
    res["capture_ratio_avg"] = r2(res["up_capture_avg"] / res["down_capture_avg"], 2)
    return res


def paired_month_end(fund, bm):
    """Month-end values of both series taken on the SAME last common trading day of each month."""
    j = pd.concat([fund, bm], axis=1, join="inner").dropna()
    j.columns = ["f", "b"]
    m = j.groupby(j.index.to_period("M")).last()
    return m.f, m.b


W10 = ("2016-03", "2026-03")   # base month .. last month  -> 120 monthly returns
W5 = ("2021-03", "2026-03")    # 60 monthly returns


def cap_for(fund, bm, w):
    f, b = paired_month_end(fund, bm)
    assert f.index.min() <= pd.Period(w[0]) and f.index.max() >= pd.Period(w[1])
    return capture_stats(f.loc[pd.Period(w[0]):pd.Period(w[1])], b.loc[pd.Period(w[0]):pd.Period(w[1])])


cap = {
    "window_10y": {"base_month": W10[0], "last_month": W10[1]},
    "window_5y": {"base_month": W5[0], "last_month": W5[1]},
    "hybrid_vs_tri_10y": cap_for(hybrid, tri, W10),
    "hybrid_vs_tri_5y": cap_for(hybrid, tri, W5),
    "hybrid_vs_pri_10y": cap_for(hybrid, pri, W10),
    "index_vs_tri_10y": cap_for(idx_fund, tri, W10),
    "index_vs_pri_10y": cap_for(idx_fund, pri, W10),
}
assert cap["hybrid_vs_tri_10y"]["months"] == 120 and cap["hybrid_vs_tri_5y"]["months"] == 60
assert cap["hybrid_vs_tri_10y"]["up_months"] + cap["hybrid_vs_tri_10y"]["down_months"] + cap["hybrid_vs_tri_10y"]["zero_months"] == 120
out["capture"] = cap

# ------------------------------------------------- 2. Sharpe, Sortino, information ratio
def risk_row(fund, bm, start, end):
    j = pd.concat([fund, bm], axis=1, join="inner").dropna().loc[start:end]
    j.columns = ["f", "b"]
    r = j.pct_change().dropna()
    mar_d = (1 + RF) ** (1 / TD) - 1
    c_f, c_b = cagr(j.f), cagr(j.b)
    vol = r.f.std() * math.sqrt(TD)
    dd = math.sqrt((np.minimum(r.f - mar_d, 0) ** 2).mean()) * math.sqrt(TD)
    te = (r.f - r.b).std() * math.sqrt(TD)
    # Every ratio is computed from the ROUNDED inputs a reader sees, so it reproduces on a calculator.
    c_f2, c_b2 = r2(c_f * 100, 2), r2(c_b * 100, 2)
    vol2, dd2 = r2(vol * 100, 2), r2(dd * 100, 2)
    act3, te3 = r2(c_f2 - c_b2, 2), r2(te * 100, 3)   # active return = difference of the two DISPLAYED CAGRs
    return {
        "start": ymd(j.index[0]), "end": ymd(j.index[-1]), "days": int(len(r)),
        "cagr_pct": c_f2, "bm_cagr_pct": c_b2,
        "vol_pct": vol2, "downside_dev_pct": dd2,
        "sharpe": r2((c_f2 - RF * 100) / vol2, 2), "sortino": r2((c_f2 - RF * 100) / dd2, 2),
        "active_return_pct": act3,
        "tracking_error_pct": te3,
        "information_ratio": r2(act3 / te3, 2),
        "down_days_share_pct": r2((r.f < mar_d).mean() * 100, 1),
    }


RS, RE = "2016-03-31", "2026-03-30"
out["risk_ratios"] = {
    "risk_free_pct": r2(RF * 100, 2),
    "mar_note": "Minimum acceptable return set equal to the risk-free rate, so Sharpe and Sortino share a numerator.",
    "window": f"{RS} to {RE}",
    "index_fund_vs_tri": risk_row(idx_fund, tri, RS, RE),
    "hybrid_vs_tri": risk_row(hybrid, tri, RS, RE),
}
irx = out["risk_ratios"]["index_fund_vs_tri"]
assert irx["active_return_pct"] < 0 and irx["tracking_error_pct"] < 1.0, irx   # an index fund trails its TRI by costs, tracks closely

# ------------------------------------------------- 3. portfolio turnover (illustrative generic funds)
AUM = 2000.0  # Rs crore, average
fa = {"purchases": 520.0, "sales": 400.0}
fb = {"purchases": 5100.0, "sales": 5000.0}
TER = 0.01
GROSS = 0.12
YEARS = 10
START_AMT = 100000


def turnover_case(f, cost_side):
    """cost_side = market impact per side (the part of trading cost that is NOT an expense line). Brokerage and
    transaction charges are inside the TER (Master Circular para 11.2.4(a)), so the TER input below already covers them."""
    turn = min(f["purchases"], f["sales"]) / AUM
    hidden = (f["purchases"] + f["sales"]) * cost_side / AUM
    hid3 = r2(hidden * 100, 3)
    net3 = r2(GROSS * 100 - TER * 100 - hid3, 3)          # computed from the displayed drag, so it reproduces
    return {
        "purchases_cr": r2(f["purchases"], 0), "sales_cr": r2(f["sales"], 0),
        "turnover_pct": r2(turn * 100, 0), "impact_drag_pct_of_aum": hid3,
        "net_return_pct": net3,
        "ten_year_value": r2(START_AMT * (1 + net3 / 100) ** YEARS, 0),
    }


zero_cost_value = START_AMT * (1 + GROSS - TER) ** YEARS
tcases = {}
for label, c in (("low", 0.0005), ("base", 0.001), ("high", 0.002)):
    tcases[label] = {"impact_per_side_pct": r2(c * 100, 2), "fund_a": turnover_case(fa, c), "fund_b": turnover_case(fb, c)}
out["turnover"] = {
    "illustrative": True,
    "note": "TER (1.0% here) is taken to include brokerage and transaction charges; the only extra drag modelled is market impact per side.",
    "avg_aum_cr": r2(AUM, 0), "gross_return_pct": r2(GROSS * 100, 1), "ter_pct": r2(TER * 100, 1),
    "years": YEARS, "start_amount": START_AMT,
    "value_ignoring_impact": r2(zero_cost_value, 0),
    "cases": tcases,
}
assert tcases["base"]["fund_b"]["ten_year_value"] < tcases["base"]["fund_a"]["ten_year_value"] < zero_cost_value
assert out["turnover"]["cases"]["base"]["fund_a"]["turnover_pct"] == 20 and out["turnover"]["cases"]["base"]["fund_b"]["turnover_pct"] == 250

# ------------------------------------------------- 4. survivorship bias (seeded simulation, zero skill)
rng = np.random.default_rng(2026)
N, M = 500, 120
bm = rng.normal(0.009, 0.045, size=M)
cost_m = 0.0008
noise = rng.normal(-cost_m, 0.012, size=(N, M))      # every fund: benchmark + costs + luck, NO skill
fr = (bm + noise)                                    # monthly fund returns
growth = np.cumprod(1 + fr, axis=1)
bm_growth = np.cumprod(1 + bm)
ann = lambda g, m: g ** (12 / m) - 1
excess = ann(growth[:, -1], M) - ann(bm_growth[-1], M)
alive = np.ones(N, dtype=bool)
alive_counts = []
for review in range(36, 109, 12):                    # annual reviews from month 36 to 108
    trail = growth[:, review - 1] / np.where(review - 37 >= 0, growth[:, review - 37], 1.0)
    cand = np.where(alive)[0]
    k = int(round(len(cand) * 0.10))
    worst = cand[np.argsort(trail[cand])[:k]]
    alive[worst] = False
    alive_counts.append({"month": review, "closed": int(k), "alive_after": int(alive.sum())})
surv = excess[alive]
out["survivorship"] = {
    "simulated": True, "seed": 2026, "funds": N, "months": M, "years": 10,
    "skill": "none: every fund earns the benchmark return less costs plus random noise",
    "cost_per_month_pct": r2(cost_m * 100, 2), "noise_sd_monthly_pct": 1.2,
    "benchmark_cagr_pct": r2(ann(bm_growth[-1], M) * 100, 2),
    "rule": "At the end of years 3 to 9, the worst 10% of the surviving funds by trailing 3-year return are closed or merged away.",
    "reviews": alive_counts,
    "survivors": int(alive.sum()),
    "survivors_share_pct": r2(alive.mean() * 100, 1),
    "all_mean_excess_pct": r2(excess.mean() * 100, 2),
    "all_median_excess_pct": r2(np.median(excess) * 100, 2),
    "all_ahead_share_pct": r2((excess > 0).mean() * 100, 1),
    "survivor_mean_excess_pct": r2(surv.mean() * 100, 2),
    "survivor_median_excess_pct": r2(np.median(surv) * 100, 2),
    "survivor_ahead_share_pct": r2((surv > 0).mean() * 100, 1),
}
sv = out["survivorship"]
assert sv["survivors"] < N and sv["survivor_mean_excess_pct"] > sv["all_mean_excess_pct"]
assert sv["all_mean_excess_pct"] < 0   # no skill, positive costs -> the full cohort trails

# ------------------------------------------------- 5. liquid and overnight funds
ST_5Y, FY_ENDS = "2021-03-31", ["2021-03-31", "2022-03-31", "2023-03-31", "2024-03-31", "2025-03-31", "2026-03-31"]
assert overnight.index[0] < pd.Timestamp("2018-05-03")  # history exists, but we only use it from FY22
lo = {}
for key, s in (("overnight", overnight), ("liquid", liquid), ("money_market", money), ("gilt", gilt)):
    w = s.loc[ST_5Y:END]
    d = w.pct_change().dropna()
    # worst 3-calendar-month return: the overnight and liquid funds have weekend NAV dates, the others only business days
    back = [s.loc[:dt - pd.DateOffset(months=3)] for dt in w.index]
    roll3m = pd.Series({dt: w[dt] / b.iloc[-1] - 1 for dt, b in zip(w.index, back) if len(b) and dt - pd.DateOffset(months=3) >= w.index[0]})
    lo[key] = {
        "fy_returns_pct": [r2(window_return(s, FY_ENDS[i], FY_ENDS[i + 1]), 2) for i in range(5)],
        "cagr_5y_pct": r2(cagr(w) * 100, 2),
        "down_days": int((d < 0).sum()), "days": int(len(d)),
        "down_days_share_pct": r2((d < 0).mean() * 100, 1),
        "worst_day_pct": r2(d.min() * 100, 2), "worst_day_date": ymd(d.idxmin()),
        "worst_3m_pct": r2(roll3m.min() * 100, 2), "worst_3m_end": ymd(roll3m.idxmin()),
        "max_drawdown": max_drawdown(w),
    }
out["liquid_overnight"] = {
    "window": f"{ST_5Y} to {END}", "fy_labels": ["FY22", "FY23", "FY24", "FY25", "FY26"], "funds": lo,
}
assert lo["overnight"]["down_days"] <= lo["liquid"]["down_days"] <= lo["gilt"]["down_days"]
assert lo["overnight"]["worst_day_pct"] > lo["gilt"]["worst_day_pct"]

# ------------------------------------------------- 6. growth vs IDCW (illustrative) + real ETF payout
G, PAY, NAV0 = 0.10, 0.03, 100.0
nav_g = NAV0
nav_p, cash = NAV0, 0.0
units_r, nav_r = 1000.0, NAV0
years = []
for y in range(1, 11):
    nav_g = nav_g * (1 + G)
    pre = nav_p * (1 + G)
    payout = PAY * nav_p            # 3% of the opening NAV, paid at year end
    nav_p = pre - payout
    cash += payout
    pre_r = nav_r * (1 + G)
    pay_r = PAY * nav_r
    nav_r = pre_r - pay_r
    units_r += units_r * pay_r / nav_r      # payout reinvested at the ex-payout NAV
    years.append({"year": y, "growth_nav": r2(nav_g, 2), "payout_nav": r2(nav_p, 2), "payout_cum": r2(cash * 1000, 0),
                  "reinvest_units": r2(units_r, 2), "reinvest_value": r2(units_r * nav_r, 0)})
units0 = 1000.0   # Rs 1,00,000 at NAV 100
growth_val = units0 * nav_g
payout_val_nav = units0 * nav_p
payout_val_cash = units0 * cash
reinvest_val = units_r * nav_r
assert abs(reinvest_val - growth_val) < 1e-6 * growth_val   # pre-tax, reinvesting the payout reproduces the growth plan
assert abs((payout_val_nav + payout_val_cash) - growth_val) > 0.0   # uninvested payouts do not compound
mf2 = yaml.safe_load(open(os.path.join(ROOT, "_data", "mf2.yml"), encoding="utf-8"))
etf = mf2["discontinuities"]["etf_payouts"][0]
assert etf["ex_date"] == "2021-02-25"
ex = {"nav_before": 100.0, "idcw": 5.0, "units": 1000.0}
ex["nav_after"] = ex["nav_before"] - ex["idcw"]
ex["value_before"] = ex["units"] * ex["nav_before"]
ex["value_after_nav"] = ex["units"] * ex["nav_after"]
ex["cash_received"] = ex["units"] * ex["idcw"]
assert ex["value_after_nav"] + ex["cash_received"] == ex["value_before"]
rein_units = ex["cash_received"] / ex["nav_after"]
ex["reinvest_new_units"] = r2(rein_units, 2)
ex["reinvest_total_units"] = r2(ex["units"] + rein_units, 2)
ex["reinvest_value"] = r2((ex["units"] + rein_units) * ex["nav_after"], 0)
out["idcw"] = {
    "illustrative": True,
    "example": ex,
    "ten_year": {
        "start_amount": int(units0 * NAV0), "gross_return_pct": r2(G * 100, 0), "idcw_pct_of_opening_nav": r2(PAY * 100, 0),
        "growth_value": r2(growth_val, 0), "payout_nav_value": r2(payout_val_nav, 0),
        "payout_cash_cumulative": r2(payout_val_cash, 0), "payout_total": r2(payout_val_nav + payout_val_cash, 0),
        "reinvest_value": r2(reinvest_val, 0), "years": years,
    },
    "etf_observed": {
        "ex_date": etf["ex_date"], "nav_before": etf["nav_before"], "nav_after": etf["nav_after"],
        "estimated_payout_per_unit": etf["estimated_payout_per_unit"], "nav_gap_vs_index_pct": etf["nav_gap_vs_index_pct"],
        "note": "Estimated in derive_mf2.py as the one-day gap between the ETF's NAV return and the Nifty 50 price index's; not an amount read from the fund's notice.",
    },
}

# ------------------------------------------------- regulatory facts, typed once, with their source
MC = {
    "number": "HO/24/13/11(1)2026-IMD-POD-1/I/7602/2026",
    "date": "2026-03-20",
    "title": "SEBI Master Circular for Mutual Funds",
    "url": "https://www.sebi.gov.in/legal/master-circulars/mar-2026/master-circular-for-mutual-funds_100491.html",
    "read": "Full text downloaded from sebi.gov.in and read on 25 October 2026. It applies alongside the SEBI (Mutual Funds) Regulations, 2026, in force from 1 April 2026. Later circulars may amend it: check the current text.",
}
out["regulation"] = {
    "master_circular": MC,
    "turnover_definition": {"para": "Formats annex, Key Statistics table, note 3",
                            "text": "Portfolio turnover = lower of sales or purchases divided by the average AuM for the year or period."},
    "turnover_disclosure": {"para": "Scheme Information Document format, investment strategy section",
                            "text": "Equity-oriented schemes must disclose a portfolio turnover policy and, where significant, the probable effect of their strategy on turnover, including higher brokerage and transaction costs."},
    "distributor_turnover": {"para": "6.7.3", "text": "The Master Circular also uses 'portfolio turnover ratio' for a distributor's churn of client money (flagged at more than twice the industry average): a different thing from a fund's turnover."},
    "overnight": {"para": "3.8.2 (Debt Schemes, category table)",
                  "text": "Investment in overnight securities having maturity of 1 day; up to 5% of net assets may sit in G-secs or T-bills of residual maturity up to 30 calendar days as margin and collateral."},
    "liquid": {"para": "3.8.2 (Debt Schemes, category table)", "text": "Investment in only debt and money market securities with maturity of up to 91 calendar days."},
    "money_market": {"para": "3.8.2 (Debt Schemes, category table)", "text": "Investment in money market instruments having maturity up to 1 year."},
    "liquid_framework": {"para": "5.6.1 to 5.6.5",
                         "liquid_assets_min_pct": 20,
                         "text": "Liquid funds hold at least 20% of net assets in liquid assets (cash, government securities, T-bills, repo on government securities); liquid and overnight funds may not park money in short-term bank deposits or buy structured-obligation or credit-enhanced debt (government-guaranteed excepted); an exit load applies on exit within 7 calendar days, graded as AMFI prescribes with the Board."},
    "idcw_names": {"para": "12.1", "text": "Options are named 'Payout of Income Distribution cum capital withdrawal option', 'Reinvestment of Income Distribution cum capital withdrawal option' and 'Transfer of Income Distribution cum capital withdrawal plan'."},
    "idcw_capital": {"para": "12.2 and 12.3", "text": "Offer documents must disclose that amounts can be distributed out of investors' capital (equalisation reserve); the account statement must separate income distribution (NAV appreciation) from capital distribution."},
    "idcw_payment": {"para": "12.4", "days": 7, "text": "IDCW is paid within 7 working days of the record date."},
    "idcw_nav_fall": {"para": "12.5.1(b) and (e)",
                      "text": "The NAV is adjusted for the IDCW and statutory levy at close of business on the record date; the notice must state that the NAV will fall to the extent of the payout and statutory levy."},
    "idcw_advert": {"para": "14.1.3", "text": "Advertisements of payouts must state, immediately below the payout figure, that the NAV will fall to the extent of the payout and statutory levy."},
}


def _clean(x):
    if isinstance(x, dict):
        return {k: _clean(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_clean(v) for v in x]
    if isinstance(x, (np.floating, float)):
        return int(x) if float(x) == int(x) else float(x)
    if isinstance(x, np.integer):
        return int(x)
    return x


out = _clean(out)


class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


with open(OUT, "w", encoding="utf-8") as f:
    f.write("# GENERATED by scripts/derive_mf4.py — do not edit by hand; re-run the script.\n")
    f.write("# Mutual Funds, Minus the Marketing — Module 4 (capture ratios, Sortino and information\n")
    f.write("# ratio, portfolio turnover, survivorship bias, liquid and overnight funds, growth vs IDCW).\n")
    yaml.dump(out, f, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=120)
print(f"wrote {OUT}")
