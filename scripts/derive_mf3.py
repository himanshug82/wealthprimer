#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by the Mutual Funds, Minus the Marketing — Module 3
posts (hybrid funds, arbitrage funds, international funds, NFOs, the
riskometer, manager changes and style drift, segregated portfolios, step-up
SIPs) and write them to _data/mf3.yml.

    python3 scripts/derive_mf3.py          # rewrites _data/mf3.yml

Every number a post renders comes from _data/mf3.yml. Market figures are
COMPUTED here from the committed CSVs; regulatory facts (limits, thresholds,
dates, amounts from orders) are TYPED ONCE below, each next to the primary
source it was read from. Anything that rests on a secondary source is marked
`verify: true` in the output so the lead editor can track it.

INPUTS — AMFI NAV history via mfapi.in (https://api.mfapi.in/mf/<code>),
truncated at 31 March 2026 (the first Module 3 post publishes 18 October
2026, more than six months later):
  assets/data/uti-arbitrage-fund-nav.csv          UTI Arbitrage Fund, regular growth (104075), direct growth (120795)
  assets/data/uti-aggressive-hybrid-fund-nav.csv  UTI Aggressive Hybrid Fund, regular growth (100684), direct growth (120674)
  assets/data/uti-equity-savings-fund-nav.csv     UTI Equity Savings Fund, regular growth (144484), direct growth (144490)
  assets/data/uti-balanced-advantage-fund-nav.csv UTI Balanced Advantage Fund, regular growth (151882)
  assets/data/navi-nifty50-index-fund-nav.csv     Navi Nifty 50 Index Fund, regular growth (149040), direct growth (149039)
  assets/data/uti-nifty50-index-fund-nav.csv      (existing) UTI Nifty 50 Index Fund, regular (100822) / direct (120716)
  assets/data/uti-overnight-fund-nav.csv          (existing) UTI Overnight Fund, regular (100814); face value
                                                  Rs 10 -> Rs 1,000 on 3 May 2018, corrected here as in derive_mf2.py
Exchange rate:
  assets/data/usd-inr-fred-dexinus.csv            Rupees per US dollar, Federal Reserve Board H.10 noon buying
                                                  rates in New York, series DEXINUS via FRED
                                                  (https://fred.stlouisfed.org/series/DEXINUS), 1 Apr 2006 to 31 Mar 2026.

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
OUT = os.path.join(ROOT, "_data", "mf3.yml")
END = "2026-03-31"
TRADING_DAYS = 252


# ----------------------------------------------------------------- helpers
def load(name, col):
    df = pd.read_csv(os.path.join(DATA, name), parse_dates=["date"]).set_index("date")
    return df[col].dropna().sort_index()


def fix_face_value(s, threshold=0.5):
    """Splice out face-value changes / unit splits (any one-day move > 50%),
    rescaling earlier NAVs. Same rule as derive_mf2.fix_discontinuities."""
    s = s.copy()
    r = s.pct_change()
    events = []
    for dt in r[r.abs() > threshold].index:
        prev = s.loc[:dt].iloc[-2]
        ratio = s.loc[dt] / prev
        events.append(dt.strftime("%Y-%m-%d"))
        s.loc[s.index < dt] = s.loc[s.index < dt] * ratio
    return s, events


def r2(x, n=2):
    """Round; a whole number is returned as an int so posts never print a
    trailing ".0" (house style)."""
    if x is None:
        return None
    v = round(float(x), n)
    return int(v) if v == int(v) else v


def cagr(s, start=None, end=None):
    s = s.loc[start:end].dropna()
    years = (s.index[-1] - s.index[0]).days / 365.25
    return ((s.iloc[-1] / s.iloc[0]) ** (1 / years) - 1) * 100


def ann_vol(s, start=None, end=None):
    r = s.loc[start:end].pct_change().dropna()
    return r.std() * math.sqrt(TRADING_DAYS) * 100


def window_return(s, start, end):
    """Return from the last NAV on/before `start` to the last on/before `end`.
    Requires the series to exist on/before `start`."""
    assert s.index[0] <= pd.Timestamp(start), (s.name, start)
    a = s.loc[:start].iloc[-1]
    b = s.loc[:end].iloc[-1]
    return (b / a - 1) * 100


def max_drawdown(s, start=None, end=None):
    s = s.loc[start:end].dropna()
    dd = s / s.cummax() - 1
    trough = dd.idxmin()
    peak = s.loc[:trough].idxmax()
    after = s.loc[trough:]
    rec = after[after >= s[peak]]
    return {
        "pct": r2(dd.min() * 100, 1),
        "peak_date": peak.strftime("%Y-%m-%d"),
        "trough_date": trough.strftime("%Y-%m-%d"),
        "recovered_date": rec.index[0].strftime("%Y-%m-%d") if len(rec) else None,
    }


def rolling_1y(s, start=None, end=None):
    """Trailing one-year return at every date with a full year behind it
    (inside [start, end])."""
    s = s.loc[start:end].dropna()
    out = {}
    for dt in s.index:
        a_dt = dt - pd.DateOffset(years=1)
        if a_dt < s.index[0]:
            continue
        out[dt] = (s[dt] / s.loc[:a_dt].iloc[-1] - 1) * 100
    return pd.Series(out)


def nav_on_or_after(s, dt):
    sub = s.loc[dt:]
    return sub.index[0], float(sub.iloc[0])


def xirr(flows):
    """flows: list of (Timestamp, amount). Bisection on NPV, days/365.25 —
    the same convention as the SIP post's Python."""
    t0 = flows[0][0]

    def npv(rate):
        return sum(cf / (1 + rate) ** ((t - t0).days / 365.25) for t, cf in flows)

    lo, hi = -0.99, 10.0
    assert npv(lo) * npv(hi) < 0
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(lo) * npv(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2 * 100


# ----------------------------------------------------------------- load
arb = load("uti-arbitrage-fund-nav.csv", "nav_regular_growth")
arb_dir = load("uti-arbitrage-fund-nav.csv", "nav_direct_growth")
aggr = load("uti-aggressive-hybrid-fund-nav.csv", "nav_regular_growth")
eqs = load("uti-equity-savings-fund-nav.csv", "nav_regular_growth")
baf = load("uti-balanced-advantage-fund-nav.csv", "nav_regular_growth")
navi = load("navi-nifty50-index-fund-nav.csv", "nav_regular_growth")
navi_dir = load("navi-nifty50-index-fund-nav.csv", "nav_direct_growth")
idx = load("uti-nifty50-index-fund-nav.csv", "nav_regular_growth")
idx_dir = load("uti-nifty50-index-fund-nav.csv", "nav_direct_growth")
overnight, ov_events = fix_face_value(load("uti-overnight-fund-nav.csv", "nav_regular_growth"))
fx = load("usd-inr-fred-dexinus.csv", "usd_inr")

assert ov_events == ["2018-05-03"], ov_events
for s in (arb, arb_dir, aggr, eqs, baf, navi, navi_dir, idx, idx_dir, overnight, fx):
    assert s.index[-1] <= pd.Timestamp(END), s.index[-1]
    assert s.index[-1] >= pd.Timestamp("2026-03-27"), s.index[-1]
# None of the new NAV series carries a face-value change or split.
for s in (arb, arb_dir, aggr, eqs, baf, navi, navi_dir):
    assert s.pct_change().abs().max() < 0.2

SOURCES = {
    "label": "AMFI NAV history via mfapi.in",
    "api": "https://api.mfapi.in/mf/SCHEME_CODE",
    "end": END,
    "lag_note": "Every NAV and exchange-rate series ends 31 March 2026; the first Module 3 post publishes 18 October 2026.",
    "arbitrage": {"name": "UTI Arbitrage Fund", "regular_code": 104075, "direct_code": 120795,
                  "csv": "/assets/data/uti-arbitrage-fund-nav.csv", "start": arb.index[0].strftime("%Y-%m-%d")},
    "aggressive_hybrid": {"name": "UTI Aggressive Hybrid Fund", "regular_code": 100684, "direct_code": 120674,
                          "csv": "/assets/data/uti-aggressive-hybrid-fund-nav.csv", "start": aggr.index[0].strftime("%Y-%m-%d")},
    "equity_savings": {"name": "UTI Equity Savings Fund", "regular_code": 144484, "direct_code": 144490,
                       "csv": "/assets/data/uti-equity-savings-fund-nav.csv", "start": eqs.index[0].strftime("%Y-%m-%d")},
    "balanced_advantage": {"name": "UTI Balanced Advantage Fund", "regular_code": 151882,
                           "csv": "/assets/data/uti-balanced-advantage-fund-nav.csv", "start": baf.index[0].strftime("%Y-%m-%d")},
    "navi_index": {"name": "Navi Nifty 50 Index Fund", "regular_code": 149040, "direct_code": 149039,
                   "csv": "/assets/data/navi-nifty50-index-fund-nav.csv", "start": navi.index[0].strftime("%Y-%m-%d")},
    "index_fund": {"name": "UTI Nifty 50 Index Fund", "regular_code": 100822, "direct_code": 120716,
                   "csv": "/assets/data/uti-nifty50-index-fund-nav.csv"},
    "overnight": {"name": "UTI Overnight Fund", "regular_code": 100814, "csv": "/assets/data/uti-overnight-fund-nav.csv"},
    "fx": {"name": "Rupees per US dollar (noon buying rate, New York)",
           "source": "Federal Reserve Board H.10 release, series DEXINUS, via FRED",
           "url": "https://fred.stlouisfed.org/series/DEXINUS",
           "csv": "/assets/data/usd-inr-fred-dexinus.csv",
           "note": "Close to, but not identical with, the RBI/FBIL reference rate for the same day."},
}


# =========================================================== MF3-1 hybrids
# Fixed calendar windows (no hindsight endpoints): each fund's return over the
# same window, and each fund's worst peak-to-trough fall over a COMMON window
# that every fund in the comparison covers.
HYB_FUNDS = [("aggressive_hybrid", "Aggressive hybrid", aggr), ("balanced_advantage", "Balanced advantage", baf),
             ("equity_savings", "Equity savings", eqs), ("arbitrage", "Arbitrage", arb),
             ("index_fund", "Nifty 50 index fund", idx)]
HYB_WINDOWS = [("cy2008", "Calendar 2008", "2007-12-31", "2008-12-31"),
               ("q1_2020", "1 Jan to 31 Mar 2020", "2019-12-31", "2020-03-31"),
               ("q1_2026", "1 Jan to 31 Mar 2026", "2025-12-31", "2026-03-31")]
hyb_windows = []
for key, label, a, b in HYB_WINDOWS:
    row = {"key": key, "label": label, "start": a, "end": b}
    for fk, _, s in HYB_FUNDS:
        row[fk] = r2(window_return(s, a, b), 1) if s.index[0] <= pd.Timestamp(a) else None
    hyb_windows.append(row)

hyb_common = []
for start, label in [(aggr.index[0], "Apr 2006 to Mar 2026"), (eqs.index[0], "Aug 2018 to Mar 2026"),
                     (baf.index[0], "Aug 2023 to Mar 2026")]:
    row = {"start": start.strftime("%Y-%m-%d"), "label": label}
    for fk, _, s in HYB_FUNDS:
        if s.index[0] <= start:
            row[fk] = {"max_drawdown_pct": max_drawdown(s, start, END)["pct"], "volatility_pct": r2(ann_vol(s, start, END), 1)}
        else:
            row[fk] = None
    hyb_common.append(row)

aggr_2008 = max_drawdown(aggr)
idx_2008 = max_drawdown(idx)
assert aggr_2008["peak_date"].startswith("2008") and idx_2008["peak_date"].startswith("2008")
w = {r["key"]: r for r in hyb_windows}
# Claims the post makes, asserted:
assert w["cy2008"]["aggressive_hybrid"] < -40 and w["cy2008"]["index_fund"] < w["cy2008"]["aggressive_hybrid"]
assert abs(w["q1_2026"]["balanced_advantage"] - w["q1_2026"]["aggressive_hybrid"]) < 0.5          # BAF fell about as much
assert w["q1_2026"]["equity_savings"] > w["q1_2026"]["aggressive_hybrid"]
assert all(w[k]["arbitrage"] > 0 for k in w)
hybrid = {
    "windows": hyb_windows,
    "common_windows": hyb_common,
    "aggressive_2008_drawdown": aggr_2008,
    "index_2008_drawdown": idx_2008,
    "aggr_to_index_2008_ratio": r2(aggr_2008["pct"] / idx_2008["pct"], 2),
}

# ========================================================= MF3-2 arbitrage
# Compared with the overnight fund only from 3 May 2018, when that scheme took
# on its present overnight mandate (see derive_mf2.py). Both are PRE-TAX NAV
# returns; the two are taxed differently, which the post says.
ARB_START = "2018-05-03"
arb_r = arb.loc[ARB_START:].pct_change().dropna()
ov_r = overnight.loc[ARB_START:].pct_change().dropna()
ra = rolling_1y(arb, ARB_START, END)
ro = rolling_1y(overnight, ARB_START, END)
both = pd.concat([ra.rename("arb"), ro.rename("ov")], axis=1, sort=True).dropna()
arb_m = arb.resample("ME").last().pct_change().dropna().loc["2006-08":] * 100
arb_full_r = arb.pct_change().dropna()
arb_cal = []
for y in range(2019, 2026):
    arb_cal.append({"year": y, "arbitrage_pct": r2(window_return(arb, f"{y-1}-12-31", f"{y}-12-31")),
                    "overnight_pct": r2(window_return(overnight, f"{y-1}-12-31", f"{y}-12-31"))})

# Illustrative cash-futures trade (HYPOTHETICAL numbers, not a real stock):
TRADE = {"spot": 1000, "future": 1006, "days": 30}
trade_spread = TRADE["future"] - TRADE["spot"]
trade_pct = trade_spread / TRADE["spot"] * 100
trade_ann = trade_pct * 365 / TRADE["days"]
arbitrage = {
    "window_start": ARB_START,
    "arbitrage": {"cagr_pct": r2(cagr(arb, ARB_START, END)), "volatility_pct": r2(ann_vol(arb, ARB_START, END)),
                  "negative_days_pct": r2((arb_r < 0).mean() * 100, 1), "days": int(len(arb_r)),
                  "worst_day_pct": r2(arb_r.min() * 100), "worst_day": arb_r.idxmin().strftime("%Y-%m-%d"),
                  "rolling_1y_min_pct": r2(ra.min()), "rolling_1y_median_pct": r2(ra.median()), "rolling_1y_max_pct": r2(ra.max())},
    "overnight": {"cagr_pct": r2(cagr(overnight, ARB_START, END)), "volatility_pct": r2(ann_vol(overnight, ARB_START, END)),
                  "negative_days_pct": r2((ov_r < 0).mean() * 100, 1),
                  "rolling_1y_min_pct": r2(ro.min()), "rolling_1y_median_pct": r2(ro.median()), "rolling_1y_max_pct": r2(ro.max())},
    "rolling_1y_windows": int(len(both)),
    "rolling_1y_arb_ahead_pct": r2((both.arb > both.ov).mean() * 100, 1),
    "rolling_1y_median_gap_pp": r2((both.arb - both.ov).median()),
    "calendar_years": arb_cal,
    "full_history": {"start": arb.index[0].strftime("%Y-%m-%d"), "cagr_pct": r2(cagr(arb)),
                     "negative_days_pct": r2((arb_full_r < 0).mean() * 100, 1),
                     "months": int(len(arb_m)), "negative_months": int((arb_m < 0).sum()),
                     "worst_month_pct": r2(arb_m.min()), "worst_month": arb_m.idxmin().strftime("%Y-%m"),
                     "max_drawdown": max_drawdown(arb)},
    "q1_2020_pct": r2(window_return(arb, "2019-12-31", "2020-03-31")),
    "cy2008_pct": r2(window_return(arb, "2007-12-31", "2008-12-31")),
    "trade": {**TRADE, "spread": trade_spread, "spread_pct": r2(trade_pct), "annualised_pct": r2(trade_ann, 1)},
}
assert arbitrage["full_history"]["negative_months"] < 10 and arbitrage["arbitrage"]["negative_days_pct"] > 25

# ===================================================== MF3-3 international
fy_rows = []
for y in range(2017, 2027):
    a = fx.loc[:f"{y-1}-03-31"].iloc[-1]
    b = fx.loc[:f"{y}-03-31"].iloc[-1]
    fy_rows.append({"fy": f"FY {y-1}-{str(y)[2:]}", "start": float(a), "end": float(b), "change_pct": r2((b / a - 1) * 100)})
weakened = sum(1 for r in fy_rows if r["change_pct"] > 0)
fy26 = fy_rows[-1]
fy21 = next(r for r in fy_rows if r["fy"] == "FY 2020-21")
USD_RET = 10.0     # HYPOTHETICAL: the overseas portfolio's return in dollars
def in_rupees(usd_ret, fx_chg):
    return ((1 + usd_ret / 100) * (1 + fx_chg / 100) - 1) * 100
walk_inr = 100000
walk_usd = walk_inr / fy26["start"]
walk_usd_end = walk_usd * (1 + USD_RET / 100)
walk_inr_end = walk_usd_end * fy26["end"]
international = {
    "fy_rows": fy_rows,
    "years": len(fy_rows),
    "years_rupee_weakened": weakened,
    "years_rupee_strengthened": len(fy_rows) - weakened,
    "cagr_10y_pct": r2(cagr(fx, "2016-03-31", END)),
    "usd_return_pct": USD_RET,
    "fy26_rupee_return_pct": r2(in_rupees(USD_RET, fy26["change_pct"])),
    "fy21_rupee_return_pct": r2(in_rupees(USD_RET, fy21["change_pct"])),
    "fy21": dict(fy21), "fy26": dict(fy26),
    "walk": {"inr": walk_inr, "usd": r2(walk_usd), "usd_end": r2(walk_usd_end), "inr_end": round(walk_inr_end)},
}
assert abs(walk_inr_end / walk_inr * 100 - 100 - international["fy26_rupee_return_pct"]) < 0.01

# ============================================================== MF3-4 NFOs
# A Nifty 50 index fund launched in July 2021 at Rs 10 versus one that had
# been running since the 1990s, from the new fund's FIRST published NAV to
# 31 March 2026. Both track the same index; the point is how little the NAV
# level matters. Not a comparison of the two funds.
NFO_DAY = navi.index[0]
nfo_rows = []
for key, label, s in [("navi_regular", "Navi Nifty 50 Index Fund, regular", navi),
                      ("uti_regular", "UTI Nifty 50 Index Fund, regular", idx),
                      ("navi_direct", "Navi Nifty 50 Index Fund, direct", navi_dir),
                      ("uti_direct", "UTI Nifty 50 Index Fund, direct", idx_dir)]:
    a = float(s.loc[:NFO_DAY].iloc[-1])
    b = float(s.iloc[-1])
    units = 100000 / a
    nfo_rows.append({"key": key, "label": label, "nav_start": a, "nav_end": b, "units": r2(units, 1),
                     "value": round(units * b), "return_pct": r2((b / a - 1) * 100, 1), "cagr_pct": r2(cagr(s, NFO_DAY, END))})
nr = {r["key"]: r for r in nfo_rows}
assert abs(nr["navi_regular"]["return_pct"] - nr["uti_regular"]["return_pct"]) < 1.0
assert abs(nr["navi_direct"]["return_pct"] - nr["uti_direct"]["return_pct"]) < 1.0
nfo = {
    "first_nav_date": NFO_DAY.strftime("%Y-%m-%d"),
    "first_navs": [{"date": d.strftime("%Y-%m-%d"), "nav": float(v)} for d, v in navi.iloc[:3].items()],
    "rows": nfo_rows,
    "nav_ratio": r2(nr["uti_regular"]["nav_start"] / nr["navi_regular"]["nav_start"], 1),
    "regular_gap_value": nr["uti_regular"]["value"] - nr["navi_regular"]["value"],
    "direct_gap_value": nr["uti_direct"]["value"] - nr["navi_direct"]["value"],
    "nfo_price_value": round(100000 / 10 * float(navi.iloc[-1])),
}

# ========================================================= MF3-8 step-up SIP
def sip(s, start, end, base, step=0.0):
    """Monthly SIP on the first of each month (NAV on or after that day, via
    asof on the calendar date as in the SIP post); the instalment rises by
    `step` every 12 months, rounded to the rupee. Instalments before the
    fund's first NAV are skipped."""
    units, flows = 0.0, []
    for i, d in enumerate(pd.date_range(start, end, freq="MS")):
        px = s.asof(d)
        if pd.isna(px):
            continue
        amt = round(base * (1 + step) ** (i // 12))
        units += amt / px
        flows.append((d, -amt))
    value = units * s.asof(pd.Timestamp(end))
    invested = -sum(f for _, f in flows)
    return {"instalments": len(flows), "invested": int(invested), "value": round(value),
            "xirr_pct": r2(xirr(flows + [(pd.Timestamp(end), value)])),
            "last_instalment": int(-flows[-1][1])}


BASE = 10000
STEPS = [0.0, 0.05, 0.10]
stepup_rows = []
for start, label in [("2016-04-01", "10 years (Apr 2016 to Mar 2026)"),
                     ("2011-04-01", "15 years (Apr 2011 to Mar 2026)"),
                     ("2006-04-01", "20 years (Apr 2006 to Mar 2026)")]:
    row = {"start": start, "label": label}
    for g in STEPS:
        row[f"step_{int(g*100)}"] = sip(idx, start, END, BASE, g)
    stepup_rows.append(row)
ten = stepup_rows[0]
same_total_base = ten["step_10"]["invested"] / ten["step_10"]["instalments"]
same_total = sip(idx, "2016-04-01", END, same_total_base, 0.0)

# Every 10-year window with a monthly start from May 2006 to April 2016
# (overlapping windows; 120 of them).
roll = []
for st in pd.date_range("2006-05-01", "2016-04-01", freq="MS"):
    en = st + pd.DateOffset(years=10) - pd.DateOffset(days=1)
    f = sip(idx, st, en, BASE, 0.0)
    u = sip(idx, st, en, BASE, 0.10)
    ft = sip(idx, st, en, u["invested"] / u["instalments"], 0.0)
    roll.append((u["xirr_pct"] - f["xirr_pct"], ft["value"] > u["value"]))
gaps = pd.Series([g for g, _ in roll])

# Constant-return illustration: at a steady 12% a year, both SIPs earn 12%;
# only the rupees differ.
R = 0.12
rm = (1 + R) ** (1 / 12) - 1
def const_sip(years, step):
    v, inv = 0.0, 0
    for m in range(years * 12):
        amt = round(BASE * (1 + step) ** (m // 12))
        v = v * (1 + rm) + amt
        inv += amt
    v *= (1 + rm)           # each instalment grows one more month to the end
    return {"invested": inv, "value": round(v)}
stepup = {
    "base": BASE,
    "rows": stepup_rows,
    "same_total_10y": {"monthly": round(same_total_base), **same_total},
    "rolling_10y": {"windows": len(roll), "first_start": "2006-05-01", "last_start": "2016-04-01",
                    "step_xirr_higher": int((gaps > 0.005).sum()), "step_xirr_lower": int((gaps < -0.005).sum()),
                    "median_gap_pp": r2(gaps.median()), "min_gap_pp": r2(gaps.min()), "max_gap_pp": r2(gaps.max()),
                    "same_total_flat_ahead": int(sum(1 for _, b in roll if b))},
    "constant": {"rate_pct": 12, "years": 10, "flat": const_sip(10, 0.0), "step_10": const_sip(10, 0.10)},
}
assert ten["step_0"]["value"] < ten["step_10"]["value"] and ten["step_10"]["xirr_pct"] < ten["step_0"]["xirr_pct"]
assert same_total["value"] > ten["step_10"]["value"]
assert stepup_rows[2]["step_0"]["instalments"] == 239 and stepup_rows[2]["step_0"]["value"] == 7780190  # matches the SIP post

# ============================================ MF3-6 manager change / drift
# INVENTED factsheet snapshots of a HYPOTHETICAL flexi-cap fund ("Example
# Flexi Cap Fund"). No real fund's data. Market-cap band weights (% of the
# portfolio), top-10 weight, number of stocks and trailing-12-month portfolio
# turnover as a factsheet would print them. The manager changes in October 2024.
SNAPSHOTS = [
    {"as_of": "Mar 2024", "manager": "Manager A (since 2015)", "large": 70.0, "mid": 18.0, "small": 8.0, "cash": 4.0, "top10": 46.0, "stocks": 42, "turnover": 28},
    {"as_of": "Sep 2024", "manager": "Manager A", "large": 69.0, "mid": 19.0, "small": 8.5, "cash": 3.5, "top10": 45.0, "stocks": 44, "turnover": 30},
    {"as_of": "Mar 2025", "manager": "Manager B (since Oct 2024)", "large": 56.0, "mid": 24.0, "small": 17.0, "cash": 3.0, "top10": 40.0, "stocks": 58, "turnover": 74},
    {"as_of": "Sep 2025", "manager": "Manager B", "large": 44.0, "mid": 27.0, "small": 26.0, "cash": 3.0, "top10": 36.0, "stocks": 67, "turnover": 96},
]
BANDS = ["large", "mid", "small", "cash"]
for sn in SNAPSHOTS:
    assert abs(sum(sn[b] for b in BANDS) - 100) < 1e-9, sn


def band_shift(a, b):
    """Half the sum of absolute changes in band weights: the share of the
    portfolio that has, in net terms, moved from one band to another."""
    return 0.5 * sum(abs(b[k] - a[k]) for k in BANDS)


shifts = []
for a, b in zip(SNAPSHOTS, SNAPSHOTS[1:]):
    shifts.append({"from": a["as_of"], "to": b["as_of"], "band_shift_pp": r2(band_shift(a, b), 1),
                   "small_change_pp": r2(b["small"] - a["small"], 1), "large_change_pp": r2(b["large"] - a["large"], 1)})
drift = {
    "snapshots": SNAPSHOTS,
    "shifts": shifts,
    "total_band_shift_pp": r2(band_shift(SNAPSHOTS[0], SNAPSHOTS[-1]), 1),
    "small_multiple": r2(SNAPSHOTS[-1]["small"] / SNAPSHOTS[0]["small"], 2),
    "note": "Invented data for a hypothetical fund. Flexi cap has no band minimum, so every snapshot is within the category rule.",
}
assert shifts[0]["band_shift_pp"] < 2 and shifts[1]["band_shift_pp"] > 10

# ================================== MF3-7 segregated portfolio (hypothetical)
# A HYPOTHETICAL debt scheme. One bond is downgraded below investment grade;
# the AMC segregates it. Rs crore unless stated.
SEG = {"aum_cr": 500.0, "units_cr": 40.0, "bond_cr": 25.0, "valuation_haircut_pct": 75.0,
       "recovery_pct": 60.0, "investor_units": 10000}
nav0 = SEG["aum_cr"] / SEG["units_cr"]
main_nav = (SEG["aum_cr"] - SEG["bond_cr"]) / SEG["units_cr"]
seg_marked = SEG["bond_cr"] * (1 - SEG["valuation_haircut_pct"] / 100)
seg_nav = seg_marked / SEG["units_cr"]
no_seg_nav = (SEG["aum_cr"] - SEG["bond_cr"] + seg_marked) / SEG["units_cr"]
recovered_cr = SEG["bond_cr"] * SEG["recovery_pct"] / 100
per_unit_recovery = recovered_cr / SEG["units_cr"]
inv = SEG["investor_units"]
segregation = {
    **SEG,
    "bond_share_pct": r2(SEG["bond_cr"] / SEG["aum_cr"] * 100, 1),
    "nav_before": r2(nav0, 4), "main_nav": r2(main_nav, 4), "seg_nav": r2(seg_nav, 4),
    "no_seg_nav": r2(no_seg_nav, 4),
    "investor_before": round(inv * nav0), "investor_main": round(inv * main_nav),
    "investor_seg_marked": round(inv * seg_nav), "investor_no_seg": round(inv * no_seg_nav),
    "recovered_cr": r2(recovered_cr, 2), "per_unit_recovery": r2(per_unit_recovery, 4),
    "investor_recovery": round(inv * per_unit_recovery),
    "investor_total_after_recovery": round(inv * (main_nav + per_unit_recovery)),
    "marked_cr": r2(seg_marked, 2),
    "excess_recovery_cr": r2(recovered_cr - seg_marked, 2),
    "excess_per_unit": r2((recovered_cr - seg_marked) / SEG["units_cr"], 4),
    "no_seg_nav_after_recovery": r2(no_seg_nav + (recovered_cr - seg_marked) / SEG["units_cr"], 4),
    "no_seg_gain_pct": r2((recovered_cr - seg_marked) / SEG["units_cr"] / no_seg_nav * 100, 2),
}
assert abs(segregation["no_seg_nav_after_recovery"] - (main_nav + per_unit_recovery)) < 1e-3
assert abs(segregation["investor_main"] + segregation["investor_seg_marked"] - segregation["investor_no_seg"]) <= 1


# ======================================================= MF3-5 riskometer
# Scoring tables typed from SEBI Master Circular for Mutual Funds, 20 March
# 2026, Annexure 10 (from circular SEBI/HO/IMD/DF3/CIR/P/2020/197 of
# 5 October 2020): https://www.sebi.gov.in/legal/master-circulars/mar-2026/master-circular-for-mutual-funds_100491.html
RISK_LEVELS = [(1, "Low"), (2, "Low to Moderate"), (3, "Moderate"), (4, "Moderately High"), (5, "High"), (99, "Very High")]
def level(v):
    for cap, name in RISK_LEVELS:
        if v <= cap + 1e-12:
            return name
MCAP_VALUE = {"large": 5, "mid": 7, "small": 9}
def vol_value(daily_vol_pct):
    return 5 if daily_vol_pct <= 1 else 6
def impact_value(ic_pct):
    return 5 if ic_pct <= 1 else (7 if ic_pct <= 2 else 9)
CASH_VALUE = 1


def equity_risk(holdings, cash):
    """Annexure 10: each parameter is the AUM-weighted sum over the equity
    holdings; the equity risk value is the simple average of the three;
    cash adds weight x 1. Weights are fractions of AUM."""
    mc = sum(w * MCAP_VALUE[b] for w, b, _, _ in holdings)
    vv = sum(w * vol_value(v) for w, _, v, _ in holdings)
    iv = sum(w * impact_value(i) for w, _, _, i in holdings)
    eq = (mc + vv + iv) / 3
    total = eq + cash * CASH_VALUE
    return {"mcap": r2(mc, 3), "volatility": r2(vv, 3), "impact": r2(iv, 3), "equity_part": r2(eq, 3),
            "cash_part": r2(cash * CASH_VALUE, 3), "value": r2(total, 3), "level": level(total)}


# Cross-check against the circular's multi-asset illustration (Tables 18-24),
# which adds AUM-weighted parameter sums across asset types: equity part 2.2
# from 20% large/<=1%/<=1%, 10% large/>1%/<=1%, 10% mid/>1%/1-2%.
_m = equity_risk([(0.2, "large", 0.01, 0.2), (0.1, "large", 1.5, 0.3), (0.1, "mid", 2.5, 1.5)], 0.0)
assert _m["mcap"] == 2.2 and _m["volatility"] == 2.2 and _m["impact"] == 2.2
# (The circular's pure-equity illustration prints parameter totals rescaled to
# its 90% equity weight and then adds cash on top, which its own formulas do
# not reproduce; to stay clear of that ambiguity every portfolio in the post is
# 100% equity, where both readings give the same answer.)

# HYPOTHETICAL fully invested equity portfolios (weight, band, daily vol %, impact cost %).
PORT_A = [(1.00, "large", 0.9, 0.1)]
PORT_B = [(0.90, "large", 0.9, 0.1), (0.10, "large", 1.2, 0.1)]
PORT_C = [(0.40, "large", 1.1, 0.1), (0.35, "mid", 1.6, 0.6), (0.25, "small", 2.2, 1.4)]
risk_a = equity_risk(PORT_A, 0.0)
risk_b = equity_risk(PORT_B, 0.0)
risk_c = equity_risk(PORT_C, 0.0)
assert risk_a["level"] == "High" and risk_a["value"] == 5.0
assert risk_b["level"] == "Very High" and risk_c["level"] == "Very High" and risk_c["value"] > risk_b["value"] + 0.8
_iv = idx.loc["2024-04-01":END].pct_change().dropna()
idx_daily_vol_2y = float(_iv.std() * 100)
# Smallest possible equity score: every holding large, <=1% vol, <=1% impact -> 5 x equity weight.
min_equity_all_in = 5.0

# Debt: credit risk value (Table 1), interest-rate risk value from portfolio
# Macaulay duration (Table 2), liquidity risk value (Table 3). Risk value =
# simple average, unless liquidity alone is higher, in which case liquidity.
CRV = {"gsec_aaa": 1, "AA+": 2, "AA": 3, "AA-": 4, "A+": 5, "A": 6}
def ir_value(md):
    for cap, v in [(0.5, 1), (1, 2), (2, 3), (3, 4), (4, 5)]:
        if md <= cap:
            return v
    return 6
def debt_risk(rows, md):
    """rows: (weight, credit value, liquidity value)."""
    cr = sum(w * c for w, c, _ in rows)
    lr = sum(w * l for w, _, l in rows)
    ir = ir_value(md)
    avg = (cr + ir + lr) / 3
    v = lr if lr > avg else avg
    return {"credit": r2(cr, 3), "interest_rate": ir, "liquidity": r2(lr, 3), "average": r2(avg, 3),
            "liquidity_rule_applied": bool(lr > avg), "value": r2(v, 3), "level": level(v)}
# Official check: the circular's debt illustration gives CR 3.5, IR 3, LR 4.8 -> 4.8, High.
_d = debt_risk([(0.1, 1, 1), (0.1, 4, 7), (0.1, 6, 7), (0.1, 8, 9), (0.1, 3, 5), (0.1, 2, 5), (0.1, 6, 7),
                (0.1, 3, 4), (0.1, 1, 2), (0.1, 1, 1)], 1.41)
assert _d["credit"] == 3.5 and _d["interest_rate"] == 3 and _d["liquidity"] == 4.8 and _d["level"] == "High"
# HYPOTHETICAL short-duration debt fund: 40% G-secs/T-bills/TREPS (1,1), 40% listed AAA (1,2), 20% listed AA (3,4); MD 2.4 years
DEBT_ROWS = [(0.4, 1, 1), (0.4, 1, 2), (0.2, 3, 4)]
risk_debt = debt_risk(DEBT_ROWS, 2.4)
risk_debt_short = debt_risk(DEBT_ROWS, 0.9)       # same paper, duration cut below a year
assert risk_debt["level"] == "Moderate" and risk_debt_short["level"] == "Low to Moderate"
riskometer = {
    "master_circular": "SEBI Master Circular for Mutual Funds, 20 March 2026 (HO/24/13/11(1)2026-IMD-POD-1/I/7602/2026), paragraph 6.16 and Annexure 10",
    "master_circular_url": "https://www.sebi.gov.in/legal/master-circulars/mar-2026/master-circular-for-mutual-funds_100491.html",
    "origin_circular": "SEBI/HO/IMD/DF3/CIR/P/2020/197, 5 October 2020",
    "prc_circular": "SEBI/HO/IMD/IMD-II DOF3/P/CIR/2021/573, 7 June 2021",
    "levels": [{"value": "≤ 1", "level": "Low"}, {"value": "> 1 to ≤ 2", "level": "Low to Moderate"},
               {"value": "> 2 to ≤ 3", "level": "Moderate"}, {"value": "> 3 to ≤ 4", "level": "Moderately High"},
               {"value": "> 4 to ≤ 5", "level": "High"}, {"value": "> 5", "level": "Very High"}],
    "disclosure_days": 10,
    "ports": [{"key": k, "holdings": [{"weight_pct": round(w * 100), "band": b, "vol_pct": v, "impact_pct": i} for w, b, v, i in P], **R}
              for k, P, R in [("A", PORT_A, risk_a), ("B", PORT_B, risk_b), ("C", PORT_C, risk_c)]],
    "index_fund_daily_vol_2y_pct": r2(idx_daily_vol_2y),
    "index_fund_daily_vol_window": "1 April 2024 to 31 March 2026",
    "min_equity_value": min_equity_all_in,
    "debt_short": {"md_years": 0.9, **risk_debt_short},
    "debt": {"md_years": 2.4, "rows": [{"weight_pct": round(w * 100), "credit": c, "liquidity": l} for w, c, l in DEBT_ROWS], **risk_debt},
}

# ================================================= regulatory facts (typed)
# Typed ONCE here from the primary source named beside each. `verify: true`
# marks anything that rests on a secondary source (listed in the post as such).
MC26 = {"name": "Master Circular for Mutual Funds", "number": "HO/24/13/11(1)2026-IMD-POD-1/I/7602/2026",
        "date": "2026-03-20",
        "url": "https://www.sebi.gov.in/legal/master-circulars/mar-2026/master-circular-for-mutual-funds_100491.html"}
REGS26 = {"name": "SEBI (Mutual Funds) Regulations, 2026", "notification": "SEBI/LAD-NRO/GN/2026/294",
          "notified": "2026-01-14", "in_force": "2026-04-01",
          "url": "https://www.sebi.gov.in/legal/regulations/apr-2026/securities-and-exchange-board-of-india-mutual-funds-regulations-2026_100744.html"}
HYBRID_RULES = [  # MC26 paragraph 3.8.3 (as revised by circular HO/24/13/15(2)2026-IMD-RAC4/I/5764/2026, 26 Feb 2026)
    {"category": "Conservative hybrid", "rule": "Equity 10% to 25%; debt 75% to 90%"},
    {"category": "Balanced hybrid", "rule": "Equity 40% to 60%; debt 40% to 60%; no arbitrage allowed"},
    {"category": "Aggressive hybrid", "rule": "Equity 65% to 80%; debt 20% to 35%"},
    {"category": "Balanced advantage / dynamic asset allocation", "rule": "Equity and debt, \"managed dynamically\" — no minimum or maximum in either"},
    {"category": "Multi asset allocation", "rule": "At least three asset classes, at least 10% in each"},
    {"category": "Arbitrage", "rule": "Follows an arbitrage strategy; at least 65% in equity and equity-related instruments"},
    {"category": "Equity savings", "rule": "At least 65% in equity and equity-related instruments; net long equity 15% to 40%; at least 10% in debt"},
]
REG = {
    "reg": {
        "mc26": MC26,
        "regs26": REGS26,
        "categorisation_2017": "SEBI/HO/IMD/DF3/CIR/P/2017/114, 6 October 2017",
        "categorisation_2026": "HO/24/13/15(2)2026-IMD-RAC4/I/5764/2026, 26 February 2026",
        "categorisation_2026_url": "https://www.sebi.gov.in/legal/circulars/feb-2026/categorization-and-rationalization-of-mutual-fund-schemes_99983.html",
        "hybrid_para": "3.8.3",
        "hybrid_rules": HYBRID_RULES,
        "tax_equity_fund": {
            "rule_pct": 65,
            "section": "section 198(8) of the Income-tax Act, 2025",
            "url": "https://egazette.gov.in/WriteReadData/2025/265620.pdf",
            "text": "a minimum of 65% of the total proceeds of such fund is invested in the equity shares of domestic companies listed on a recognised stock exchange",
        },
        "overseas": {
            "circular": "SEBI/HO/IMD/IMD-II/DOF3/P/CIR/2021/571, 3 June 2021",
            "circular_url": "https://www.sebi.gov.in/legal/circulars/jun-2021/circular-on-enhancement-of-overseas-investment-limits_50415.html",
            "mc_para": "13.11.2",
            "industry_usd_bn": 7, "per_mf_usd_bn": 1, "etf_industry_usd_bn": 1, "etf_per_mf_usd_mn": 300,
            "reserved_quota_usd_mn": 50,
            "pause_2022_email": "2022-01-28",           # cited in MC 2024 footnote 467; email text not public
            "pause_2022_cap_date": "2022-02-01",        # AMFI press note, 21 June 2022 (primary)
            "resume_2022_note": "2022-06-21",
            "resume_2022_url": "https://www.amfiindia.com/Themes/Theme1/downloads/PressNote_OverseasInvestmentLimits.pdf",
            "etf_pause_2024": "2024-04-01",             # SEBI emails 19/20 Mar 2024 (cited in MC 2024 fn 467); content from press reports
            "etf_pause_2024_verify": True,
            "etf_pause_2024_secondary": "https://www.businesstoday.in/mutual-funds/story/sebi-asks-amfi-to-stop-accepting-fresh-inflows-in-overseas-etfs-from-april-1-422416-2024-03-21",
            "indian_exposure_circular": "SEBI/HO/IMD/IMD-PoD-1/P/CIR/2024/149, 4 November 2024",
            "indian_exposure_pct": 25,
            "lrs_usd": 250000,
            "lrs_url": "https://www.rbi.org.in/commonperson/english/scripts/FAQs.aspx?Id=1834",
        },
        "nfo": {
            "max_days": 15, "min_working_days": 3, "mc_para": "1.7.1",
            "allot_working_days": 5,
            "deploy_business_days": 30, "deploy_extension_days": 30, "deploy_para": "7.24",
            "deploy_circular": "SEBI/HO/IMD/IMD-PoD-1/P/CIR/2025/23, 27 February 2025",
            "expenses_reg": "Regulation 66(3)",
            "sebi_investor_url": "https://investor.sebi.gov.in/new_fund_offer.html",
            # Regulation 66(7)(c), SEBI (Mutual Funds) Regulations, 2026: base expense ratio
            # slabs for open-ended equity-oriented schemes (other than index funds/ETFs/FoFs).
            "ber_reg": "Regulation 66(7)(c)",
            "ber_slabs": [{"slab": "First ₹500 crore", "equity_pct": 2.10},
                          {"slab": "Next ₹250 crore", "equity_pct": 1.90},
                          {"slab": "Next ₹1,250 crore", "equity_pct": 1.60},
                          {"slab": "Next ₹3,000 crore", "equity_pct": 1.50},
                          {"slab": "Next ₹5,000 crore", "equity_pct": 1.40},
                          {"slab": "Next ₹40,000 crore", "equity_pct": None},
                          {"slab": "Above ₹50,000 crore", "equity_pct": 0.95}],
            "ber_first_pct": 2.10, "ber_last_pct": 0.95,
        },
        "fundamental": {"reg": "Regulation 22(9)(c)", "mc_para": "1.9.1", "exit_days": 30, "old_reg": "Regulation 18(15A)"},
        "segregation": {
            "circular": "SEBI/HO/IMD/DF2/CIR/P/2018/160, 28 December 2018",
            "circular_url": "https://www.sebi.gov.in/legal/circulars/dec-2018/creation-of-segregated-portfolio-in-mutual-fund-schemes_41462.html",
            "unrated_circular": "SEBI/HO/IMD/DF2/CIR/P/2019/127, 7 November 2019",
            "mc_para": "5.5", "listing_business_days": 10, "trustee_days": 1, "statement_days": 5, "disclosure_years": 3,
        },
    },
    # Franklin Templeton India, six debt schemes, 2020. Each fact from a court
    # order, a SEBI order, or Franklin Templeton's own disclosure.
    "franklin": {
        "schemes": ["Franklin India Ultra Short Bond Fund", "Franklin India Low Duration Fund",
                    "Franklin India Short Term Income Plan", "Franklin India Income Opportunities Fund",
                    "Franklin India Dynamic Accrual Fund", "Franklin India Credit Risk Fund"],
        "wind_up_date": "2020-04-23",
        "sebi_order": {"number": "WTM/GM/IMD/08/2021-22", "date": "2021-06-07",
                       "url": "https://www.sebi.gov.in/enforcement/orders/jun-2021/in-the-matter-of-inspection-of-six-debt-schemes-of-franklin-templeton-mutual-fund_50442.html",
                       "fees_rs": 4516317660, "interest_rs": 608774874, "refund_rs": 5125092534,
                       "penalty_cr": 5, "debt_scheme_bar_years": 2, "interest_pct": 12},
        "evoting": {"dates": "26 to 29 December 2020", "for_by_holders_min": 96.78, "for_by_holders_max": 97.97,
                    "for_by_units_min": 97.37, "for_by_units_max": 99.18},
        "sc_feb2021": {"date": "2021-02-12", "url": "https://www.sebi.gov.in/sebi_data/attachdocs/jul-2021/1627041897320.PDF"},
        "sc_jul2021": {"date": "2021-07-14", "url": "https://www.sebi.gov.in/sebi_data/attachdocs/jul-2021/1626671902864.pdf"},
        "hc_date": "2020-10-24",
        "distributed_cr": 27548.21, "distributed_pct_of_aum": 109.25, "distributed_as_of": "2025-09-30",
        "ft_page_url": "https://www.franklintempletonindia.com/market-insights/winding-up-of-specific-schemes",
        "ft_disclosure_url": "https://www.franklintempletonindia.com/download/en-in/odd-penalties/6e03f15a-bb96-4cfb-a3cf-ca14711b1a82/Penalties-and-Pending-Litigation-Section.pdf",
        "sat_pending_as_of": "2025-10-24",
        "sat_escrow_cr": 250,                     # FT disclosure (24 Oct 2025): SAT stay subject to this escrow deposit
    },
}
fr = REG["franklin"]["sebi_order"]
assert fr["fees_rs"] + fr["interest_rs"] == fr["refund_rs"]
REG["franklin"]["sebi_order"]["refund_cr"] = r2(fr["refund_rs"] / 1e7, 2)
# ================================================================== write
out = {
    "_note": "GENERATED by scripts/derive_mf3.py from the CSVs in assets/data/ and the sourced facts typed in the script. Do not edit by hand.",
    "sources": SOURCES,
    "hybrid": hybrid,
    "arbitrage": arbitrage,
    "international": international,
    "nfo": nfo,
    "drift": drift,
    "segregation": segregation,
    "stepup": stepup,
    "riskometer": riskometer,
}
out.update(REG)


def _clean(x):
    """Whole-number floats become ints everywhere (no trailing ".0" in posts)."""
    if isinstance(x, dict):
        return {k: _clean(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_clean(v) for v in x]
    if isinstance(x, (float, np.floating)) and float(x) == int(x):
        return int(x)
    if isinstance(x, np.floating):
        return float(x)
    if isinstance(x, np.integer):
        return int(x)
    return x


out = _clean(out)


class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def _float(dumper, v):
    return dumper.represent_scalar("tag:yaml.org,2002:float", f"{v}")


Dumper.add_representer(float, _float)
Dumper.add_representer(np.float64, lambda d, v: _float(d, float(v)))

with open(OUT, "w", encoding="utf-8") as f:
    f.write("# GENERATED by scripts/derive_mf3.py — do not edit by hand; re-run the script.\n")
    f.write("# Mutual Funds, Minus the Marketing — Module 3 (hybrids, arbitrage, international\n")
    f.write("# funds, NFOs, riskometer, style drift, segregated portfolios, step-up SIPs).\n")
    yaml.dump(out, f, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=120)
print(f"wrote {OUT}")
