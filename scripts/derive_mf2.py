#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by the Mutual Funds, Minus the Marketing — Module 2
posts (debt funds, index funds vs ETFs, star ratings, STP/SWP) from the
committed NAV CSVs, and write them to _data/mf2.yml.

    python3 scripts/derive_mf2.py          # rewrites _data/mf2.yml

WHY A SCRIPT: the posts render every number from _data/mf2.yml via Liquid, and
the charts in assets/charts/mf2-*.svg are drawn from the same CSVs by
scripts/make_mf2_charts.py. Nothing is typed by hand, so a figure in a chart
can never quietly disagree with the same figure in the text. If a CSV is ever
corrected, re-run this and the charts script.

INPUTS (all AMFI NAV history via mfapi.in, truncated at 31 March 2026):
  assets/data/uti-overnight-fund-nav.csv      UTI Overnight Fund, regular growth (100814)
  assets/data/uti-money-market-fund-nav.csv   UTI Money Market Fund, regular growth (112077)
  assets/data/uti-gilt-fund-nav.csv           UTI Gilt Fund, regular (102510) and direct (120792)
  assets/data/uti-nifty50-etf-nav.csv         UTI Nifty 50 ETF (135320)
  assets/data/uti-nifty50-index-fund-nav.csv  UTI Nifty 50 Index Fund, regular (100822) and direct (120716)
  assets/data/nifty50-price-index.csv         Nifty 50 price index, Yahoo ^NSEI

DISCONTINUITIES the raw NAV series carry, detected here by looking for a
single-day change beyond any plausible market move, and corrected before any
return is computed (each one is also used as a teaching point in a post):
  * UTI Nifty 50 ETF: 1:10 unit split on 26 Sep 2023 (NAV drops ~90%).
  * UTI Overnight Fund: face value Rs 10 -> Rs 1,000 on 3 May 2018 (NAV x100).
  * UTI Money Market Fund: face value Rs 10 -> Rs 1,000 on 22 Aug 2009 (NAV x100).
The UTI Gilt Fund's -6.2% day on 7 Jan 2009 is a REAL move (the January 2009
gilt sell-off after the December 2008 rally) and is left alone.

Requires pandas, numpy, pyyaml.
"""
import math
import os
import sys

import numpy as np
import pandas as pd
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "assets", "data")
OUT = os.path.join(ROOT, "_data", "mf2.yml")

TRADING_DAYS = 252


def load(name, col):
    df = pd.read_csv(os.path.join(DATA, name), parse_dates=["date"]).set_index("date")
    return df[col].dropna().sort_index()


def fix_discontinuities(s, threshold=0.5):
    """Splice out unit splits / face-value changes: any single-day change of
    more than `threshold` (50%) in either direction is treated as a
    corporate action, not a market move, and every earlier NAV is rescaled
    so the series is continuous. Returns the fixed series and the list of
    events found."""
    s = s.copy()
    r = s.pct_change()
    events = []
    for dt in r[r.abs() > threshold].index:
        prev = s.loc[:dt].iloc[-2]
        curr = s.loc[dt]
        ratio = curr / prev
        events.append({
            "date": dt.strftime("%Y-%m-%d"),
            "nav_before": round(float(prev), 4),
            "nav_after": round(float(curr), 4),
            "ratio": round(float(ratio), 4),
        })
        s.loc[:dt].iloc[:-1]  # (no-op, clarity)
        s.loc[s.index < dt] = s.loc[s.index < dt] * ratio
    return s, events


def cagr(s, start=None, end=None):
    s = s.loc[start:end].dropna()
    years = (s.index[-1] - s.index[0]).days / 365.25
    return (s.iloc[-1] / s.iloc[0]) ** (1 / years) - 1, years


def ann_vol(s, start=None, end=None):
    r = s.loc[start:end].pct_change().dropna()
    return r.std() * math.sqrt(TRADING_DAYS)


def max_drawdown(s, start=None, end=None):
    s = s.loc[start:end].dropna()
    peak = s.cummax()
    dd = s / peak - 1
    trough = dd.idxmin()
    peak_date = s.loc[:trough].idxmax()
    after = s.loc[trough:]
    rec = after[after >= s[peak_date]]
    recovered = rec.index[0] if len(rec) else None
    return {
        "worst_pct": round(float(dd.min() * 100), 2),
        "peak_date": peak_date.strftime("%Y-%m-%d"),
        "trough_date": trough.strftime("%Y-%m-%d"),
        "recovered_date": recovered.strftime("%Y-%m-%d") if recovered is not None else None,
        "days_to_recover": int((recovered - peak_date).days) if recovered is not None else None,
    }


def window_return(s, start, end):
    """Simple return between the last NAV on/before `start` and on/before
    `end`. None when the series does not cover the window."""
    s = s.dropna()
    if s.index[0] > pd.Timestamp(start) or s.index[-1] < pd.Timestamp(start):
        return None
    a = s.loc[:start].iloc[-1]
    b = s.loc[:end].iloc[-1]
    return float(b / a - 1) * 100


def rolling_cagr(s, years):
    """Trailing N-year CAGR at every date that has a full window behind it."""
    s = s.dropna()
    out = {}
    for dt in s.index:
        start = dt - pd.DateOffset(years=years)
        if start < s.index[0]:
            continue
        a = s.loc[:start].iloc[-1]
        out[dt] = (s[dt] / a) ** (1 / years) - 1
    return pd.Series(out)


def month_starts(start, end):
    return pd.date_range(pd.Timestamp(start), pd.Timestamp(end), freq="MS")


def nav_on_or_after(s, dt):
    sub = s.loc[dt:]
    return (sub.index[0], float(sub.iloc[0])) if len(sub) else (None, None)


def nav_on_or_before(s, dt):
    sub = s.loc[:dt]
    return float(sub.iloc[-1])


# ----------------------------------------------------------------------------
overnight_raw = load("uti-overnight-fund-nav.csv", "nav_regular_growth")
mmf_raw = load("uti-money-market-fund-nav.csv", "nav_regular_growth")
gilt = load("uti-gilt-fund-nav.csv", "nav_regular_growth")
gilt_direct = load("uti-gilt-fund-nav.csv", "nav_direct_growth")
etf_raw = load("uti-nifty50-etf-nav.csv", "nav")
idx_reg = load("uti-nifty50-index-fund-nav.csv", "nav_regular_growth")
idx_dir = load("uti-nifty50-index-fund-nav.csv", "nav_direct_growth")
nifty = load("nifty50-price-index.csv", "nifty50_pri_close")

overnight, ov_events = fix_discontinuities(overnight_raw)
mmf, mm_events = fix_discontinuities(mmf_raw)
etf_split_adj, etf_events = fix_discontinuities(etf_raw)
_, gilt_events = fix_discontinuities(gilt)
assert len(ov_events) == 1 and len(mm_events) == 1 and len(etf_events) == 1 and len(gilt_events) == 0, (
    ov_events, mm_events, etf_events, gilt_events)

END = "2026-03-31"

# The ETF is not a growth plan: it can PAY OUT dividends, and on the ex-date its
# NAV drops by the payout while the index does not. Detect such days as a
# one-day gap of more than 1% between the ETF's NAV return and the Nifty's
# return, estimate the payout as the gap, and build a total-return series that
# assumes the payout was reinvested — the only fair basis for comparing it
# with a growth-plan index fund. Every detected event is written to the YAML.
def etf_total_return(etf_s, index_s, raw_s, gap=0.01):
    both = pd.concat([etf_s, index_s], axis=1).dropna()
    both.columns = ["etf", "idx"]
    r = both.pct_change()
    diff = r.etf - r.idx
    events = []
    adj = both.etf.copy()
    for dt in diff[diff < -gap].index:
        prev = both.etf.shift(1)[dt]
        expected = prev * (1 + r.idx[dt])
        payout = expected - both.etf[dt]
        scale = raw_s[dt] / both.etf[dt]          # report in the units actually published that day
        events.append({"ex_date": dt.strftime("%Y-%m-%d"),
                       "nav_before": round(float(prev * scale), 4), "nav_after": round(float(raw_s[dt]), 4),
                       "estimated_payout_per_unit": round(float(payout * scale), 2),
                       "nav_gap_vs_index_pct": round(float(diff[dt] * 100), 2),
                       "units_note": "per unit as published on that date (before the Sept 2023 split)"})
        factor = expected / both.etf[dt]
        adj.loc[adj.index >= dt] = adj.loc[adj.index >= dt] * factor
    return adj, events


etf, etf_payouts = etf_total_return(etf_split_adj, nifty, etf_raw)

# ---------------------------------------------------------------- MF2-1 debt
# THREE-FUND WINDOW starts 3 May 2018: the same day the overnight fund's face
# value changed, which is when UTI's scheme took on its present overnight
# mandate under SEBI's 2017-18 recategorisation. Its NAV history before that
# reflects a different portfolio (the daily moves in 2008-09 are far too large
# for an overnight fund), so the three funds are only compared from here.
# The gilt fund's own history runs from 2006 and is summarised separately.
DEBT_START = "2018-05-03"
debt = {}
for key, s, label in [("overnight", overnight, "UTI Overnight Fund"),
                      ("money_market", mmf, "UTI Money Market Fund"),
                      ("gilt", gilt, "UTI Gilt Fund")]:
    c, yrs = cagr(s, DEBT_START, END)
    daily = s.loc[DEBT_START:END].pct_change().dropna()
    r1 = rolling_cagr(s.loc[DEBT_START:END], 1)
    debt[key] = {
        "name": label,
        "cagr_pct": round(c * 100, 2),
        "volatility_pct": round(ann_vol(s, DEBT_START, END) * 100, 2),
        "negative_days_pct": round(float((daily < 0).mean() * 100), 1),
        "negative_days": int((daily < 0).sum()),
        "days": int(len(daily)),
        "worst_day_pct": round(float(daily.min() * 100), 2),
        "best_day_pct": round(float(daily.max() * 100), 2),
        "max_drawdown": max_drawdown(s, DEBT_START, END),
        "rolling_1y_min_pct": round(float(r1.min() * 100), 2),
        "rolling_1y_median_pct": round(float(r1.median() * 100), 2),
        "rolling_1y_max_pct": round(float(r1.max() * 100), 2),
        "rolling_1y_pct_negative": round(float((r1 < 0).mean() * 100), 1),
    }
gilt_long = {
    "start": gilt.index[0].strftime("%Y-%m-%d"), "end": END,
    "years": round(cagr(gilt, None, END)[1], 1),
    "cagr_pct": round(cagr(gilt, None, END)[0] * 100, 2),
    "volatility_pct": round(ann_vol(gilt, None, END) * 100, 2),
    "max_drawdown": max_drawdown(gilt, None, END),
}
r1g = rolling_cagr(gilt, 1)
gilt_long.update({"rolling_1y_min_pct": round(float(r1g.min() * 100), 2),
                  "rolling_1y_median_pct": round(float(r1g.median() * 100), 2),
                  "rolling_1y_max_pct": round(float(r1g.max() * 100), 2),
                  "rolling_1y_pct_negative": round(float((r1g < 0).mean() * 100), 1)})

# Rate episodes. A fund shows null where it has no history under its present
# mandate for that window (overnight before May 2018; money market before
# July 2009).
episodes = []
for label, a, b in [("2008 gilt rally into the January 2009 reversal", "2008-10-01", "2009-01-31"),
                    ("2013 taper tantrum (RBI liquidity squeeze)", "2013-05-15", "2013-08-20"),
                    ("2020 COVID rate cuts", "2020-02-01", "2020-07-31"),
                    ("2022 rate-hike cycle, first half", "2022-01-01", "2022-06-30"),
                    ("2024-25 easing", "2024-04-01", "2025-03-31")]:
    row = {"label": label, "start": a, "end": b}
    for key, s, mandate_from in [("overnight", overnight, DEBT_START), ("money_market", mmf, None), ("gilt", gilt, None)]:
        wr = window_return(s, a, b)
        if mandate_from and pd.Timestamp(a) < pd.Timestamp(mandate_from):
            wr = None
        row[key + "_pct"] = round(wr, 2) if wr is not None else None
    episodes.append(row)
# the gilt fund's single worst day
g_daily = gilt.pct_change().dropna()
gilt_worst_day = {"date": g_daily.idxmin().strftime("%Y-%m-%d"), "pct": round(float(g_daily.min() * 100), 2)}
# 2008 rally: Oct 2008 -> early Jan 2009 gilt peak
g_win = gilt.loc["2008-10-01":"2009-01-31"]
gilt_2008 = {
    "peak_date": g_win.idxmax().strftime("%Y-%m-%d"),
    "rally_pct": round(float(g_win.max() / g_win.iloc[0] - 1) * 100, 2),
    "fall_from_peak_to_31jan_pct": round(float(g_win.iloc[-1] / g_win.max() - 1) * 100, 2),
}

# ------------------------------------------------------------- MF2-2 ETF
ETF_START = etf.index[0].strftime("%Y-%m-%d")
etf_cmp = {}
for key, s, label in [("etf", etf, "UTI Nifty 50 ETF (split- and payout-adjusted)"),
                      ("index_fund_direct", idx_dir, "UTI Nifty 50 Index Fund, Direct"),
                      ("index_fund_regular", idx_reg, "UTI Nifty 50 Index Fund, Regular"),
                      ("nifty_pri", nifty, "Nifty 50 price index (PRI)")]:
    c, yrs = cagr(s, ETF_START, END)
    etf_cmp[key] = {"name": label, "cagr_pct": round(c * 100, 2),
                    "growth_of_100": round(100 * float(s.loc[:END].iloc[-1] / s.loc[ETF_START:].iloc[0]), 1)}
etf_years = round(cagr(etf, ETF_START, END)[1], 1)
# calendar-year returns
cal = []
for y in range(2016, 2026):
    a, b = f"{y-1}-12-31", f"{y}-12-31"
    cal.append({"year": y,
                "etf_pct": round(window_return(etf, a, b), 2),
                "index_fund_direct_pct": round(window_return(idx_dir, a, b), 2),
                "index_fund_regular_pct": round(window_return(idx_reg, a, b), 2),
                "nifty_pri_pct": round(window_return(nifty, a, b), 2)})
for row in cal:
    row["etf_minus_pri_pp"] = round(row["etf_pct"] - row["nifty_pri_pct"], 2)
    row["direct_minus_pri_pp"] = round(row["index_fund_direct_pct"] - row["nifty_pri_pct"], 2)
    row["regular_minus_pri_pp"] = round(row["index_fund_regular_pct"] - row["nifty_pri_pct"], 2)
avg_td = {k: round(float(np.mean([r[k] for r in cal])), 2)
          for k in ["etf_minus_pri_pp", "direct_minus_pri_pp", "regular_minus_pri_pp"]}
# tracking error: std dev of monthly return differences vs PRI, annualised
def monthly(s):
    return s.loc[ETF_START:END].resample("ME").last().pct_change().dropna()
m_pri = monthly(nifty)
te = {}
for key, s in [("etf", etf), ("index_fund_direct", idx_dir), ("index_fund_regular", idx_reg)]:
    d = (monthly(s) - m_pri).dropna()
    te[key] = round(float(d.std() * math.sqrt(12) * 100), 2)


# ------------------------------------------------------------ MF2-3 categories
# SEBI's scheme categorisation (circular SEBI/HO/IMD/DF3/CIR/P/2017/114 of
# 6 Oct 2017, as amended: flexi cap added 6 Nov 2020, multi cap redefined
# 11 Sep 2020). These are REGULATORY DEFINITIONS, typed here so the post
# renders them from one place; they are not derived from the CSVs. Market-cap
# ranks are by AMFI's half-yearly list of average full market capitalisation.
# Consolidated in SEBI's Master Circular for Mutual Funds (27 June 2024, clause
# 2.6), which SEBI's circular HO/24/13/15(2)2026-IMD-RAC4/I/5764/2026 of
# 26 Feb 2026 superseded: value, contra, dividend yield and focused funds now
# need at least 80% in equity (was 65%); a fund house may run both a value and
# a contra fund if their portfolios overlap by no more than 50%; solution-
# oriented schemes were discontinued. Checked against press summaries of the
# Feb 2026 circular (Upstox, ICICI Direct, Taxmann) in Sept 2026, not the PDF.
# VERIFY against the current circular before relying on any threshold.
categories_equity = [
    {"category": "Large cap", "rule": "At least 80% of assets in large-cap stocks", "universe": "Stocks ranked 1st to 100th by market cap"},
    {"category": "Large & mid cap", "rule": "At least 35% in large caps AND at least 35% in mid caps", "universe": "Ranks 1-100 and 101-250"},
    {"category": "Mid cap", "rule": "At least 65% in mid-cap stocks", "universe": "Ranks 101st to 250th"},
    {"category": "Small cap", "rule": "At least 65% in small-cap stocks", "universe": "Rank 251st onwards"},
    {"category": "Multi cap", "rule": "At least 75% in equity, with at least 25% EACH in large, mid and small caps", "universe": "All three bands, forced"},
    {"category": "Flexi cap", "rule": "At least 65% in equity; no minimum in any band", "universe": "Anywhere the manager likes"},
    {"category": "Focused", "rule": "At most 30 stocks; at least 80% in equity", "universe": "Any band"},
    {"category": "Value", "rule": "At least 80% in equity, following a value strategy", "universe": "Any band"},
    {"category": "Contra", "rule": "At least 80% in equity, following a contrarian strategy; a fund house running both value and contra must keep their overlap at or below 50%", "universe": "Any band"},
    {"category": "Dividend yield", "rule": "At least 80% in equity, mostly dividend-paying stocks", "universe": "Any band"},
    {"category": "Sectoral / thematic", "rule": "At least 80% in one sector or one theme", "universe": "That sector or theme only"},
    {"category": "ELSS (equity-linked savings scheme)", "rule": "At least 80% in equity, 3-year lock-in, tax deduction under the old regime", "universe": "Any"},
    {"category": "Index fund / ETF (exchange-traded fund), filed under \"Other schemes\"", "rule": "At least 95% in the securities of the index it tracks", "universe": "Whatever the index holds"},
]
categories_debt = [
    {"category": "Overnight", "rule": "Securities maturing in 1 day", "risk": "Rate: ~none. Credit: ~none."},
    {"category": "Liquid", "rule": "Debt and money-market paper maturing within 91 days", "risk": "Rate: very low. Credit: low, mostly top-rated."},
    {"category": "Ultra short duration", "rule": "Macaulay duration 3 to 6 months", "risk": "Rate: low."},
    {"category": "Low duration", "rule": "Macaulay duration 6 to 12 months", "risk": "Rate: low."},
    {"category": "Money market", "rule": "Money-market instruments maturing within 1 year", "risk": "Rate: low. Credit: depends on paper."},
    {"category": "Short duration", "rule": "Macaulay duration 1 to 3 years", "risk": "Rate: moderate."},
    {"category": "Medium duration", "rule": "Macaulay duration 3 to 4 years", "risk": "Rate: moderate to high."},
    {"category": "Medium to long duration", "rule": "Macaulay duration 4 to 7 years", "risk": "Rate: high."},
    {"category": "Long duration", "rule": "Macaulay duration above 7 years", "risk": "Rate: high."},
    {"category": "Dynamic bond", "rule": "Any duration; manager decides", "risk": "Rate: whatever the manager is betting on."},
    {"category": "Corporate bond", "rule": "At least 80% in AA+ and above rated corporate bonds", "risk": "Credit: low to moderate."},
    {"category": "Credit risk", "rule": "At least 65% in AA and below rated corporate bonds", "risk": "Credit: HIGH by design."},
    {"category": "Banking & PSU", "rule": "At least 80% in debt of banks, PSUs (public sector undertakings) and public financial institutions", "risk": "Credit: low."},
    {"category": "Gilt", "rule": "At least 80% in government securities, any maturity", "risk": "Rate: usually high. Credit: sovereign."},
    {"category": "Gilt with 10-year constant duration", "rule": "At least 80% in G-secs (government securities), Macaulay duration held at 10 years", "risk": "Rate: high and constant."},
    {"category": "Floater", "rule": "At least 65% in floating-rate instruments", "risk": "Rate: low by construction."},
]

# ------------------------------------------------------------ MF2-4 overlap
# Two HYPOTHETICAL large-cap portfolios (weights in %), invented for teaching.
port_a = {"Stock A": 9.5, "Stock B": 8.0, "Stock C": 7.5, "Stock D": 6.0, "Stock E": 5.5,
          "Stock F": 5.0, "Stock G": 4.5, "Stock H": 4.0, "Stock I": 3.5, "Stock J": 3.0}
port_b = {"Stock A": 8.0, "Stock B": 9.0, "Stock C": 4.0, "Stock D": 6.5, "Stock E": 3.0,
          "Stock K": 6.0, "Stock L": 5.0, "Stock F": 5.5, "Stock M": 4.5, "Stock N": 4.0}
common = sorted(set(port_a) & set(port_b))
overlap_rows = [{"stock": k, "weight_a": port_a[k], "weight_b": port_b[k], "min_weight": min(port_a[k], port_b[k])}
                for k in common]
overlap_pct = round(sum(r["min_weight"] for r in overlap_rows), 1)
top10_a = round(sum(port_a.values()), 1)
top10_b = round(sum(port_b.values()), 1)

# ------------------------------------------------------------ MF2-5 ratings
r3 = rolling_cagr(idx_reg, 3)
# trailing 3-year CAGR on each 31 March
snapshots = []
for y in range(2010, 2027):
    dt = pd.Timestamp(f"{y}-03-31")
    sub = r3.loc[:dt]
    if len(sub):
        snapshots.append({"as_of": sub.index[-1].strftime("%Y-%m-%d"),
                          "trailing_3y_cagr_pct": round(float(sub.iloc[-1] * 100), 2)})
# where each snapshot sits within the fund's OWN full history of 3-year windows
all3 = r3.values
for s_ in snapshots:
    v = s_["trailing_3y_cagr_pct"] / 100
    s_["percentile_within_own_history"] = round(float((all3 < v).mean() * 100), 0)
# mean reversion: trailing 3y vs the NEXT 3y, sampled at every month-end
me = r3.resample("ME").last().dropna()
pairs = []
for dt, past in me.items():
    fut_dt = dt + pd.DateOffset(years=3)
    fut = r3.loc[fut_dt:fut_dt + pd.Timedelta(days=7)]
    if len(fut):
        pairs.append((past, float(fut.iloc[0])))
pairs = np.array(pairs)
corr_past_future = round(float(np.corrcoef(pairs[:, 0], pairs[:, 1])[0, 1]), 2)
q = np.quantile(pairs[:, 0], [0.25, 0.75])
top_q_next = round(float(pairs[pairs[:, 0] >= q[1], 1].mean() * 100), 2)
bottom_q_next = round(float(pairs[pairs[:, 0] <= q[0], 1].mean() * 100), 2)
top_q_past = round(float(pairs[pairs[:, 0] >= q[1], 0].mean() * 100), 2)
bottom_q_past = round(float(pairs[pairs[:, 0] <= q[0], 0].mean() * 100), 2)

# ------------------------------------------------------------ MF2-6 STP/SWP
def lump_sum(s, amount, start, end):
    _, nav0 = nav_on_or_after(s, start)
    return amount / nav0 * nav_on_or_before(s, end)


def stp(equity, parking, amount, start, months, end):
    """Park `amount` in `parking` on `start`; on each of the next `months`
    month-starts move amount/months (at the parking fund's NAV) into `equity`.
    Value both legs at `end`."""
    park_units = amount / nav_on_or_after(parking, start)[1]
    eq_units = 0.0
    per = amount / months
    for i, dt in enumerate(month_starts(start, pd.Timestamp(start) + pd.DateOffset(months=months))[:months]):
        p_nav = nav_on_or_after(parking, dt)[1]
        e_nav = nav_on_or_after(equity, dt)[1]
        move_units = min(per / p_nav, park_units)
        park_units -= move_units
        eq_units += move_units * p_nav / e_nav
    return eq_units * nav_on_or_before(equity, end) + park_units * nav_on_or_before(parking, end)


def sip_equiv(equity, amount, start, months, end):
    per = amount / months
    units = 0.0
    for dt in month_starts(start, pd.Timestamp(start) + pd.DateOffset(months=months))[:months]:
        units += per / nav_on_or_after(equity, dt)[1]
    return units * nav_on_or_before(equity, end)


STP_AMOUNT = 1200000
stp_rows = []
for label, start in [("Jan 2008 (top of the market)", "2008-01-01"),
                     ("Jan 2015", "2015-01-01"),
                     ("Apr 2020 (COVID low)", "2020-04-01")]:
    end3 = (pd.Timestamp(start) + pd.DateOffset(years=3)).strftime("%Y-%m-%d")
    stp_rows.append({
        "label": label, "start": start, "end_3y": end3,
        "lump_sum_3y": round(lump_sum(idx_reg, STP_AMOUNT, start, end3)),
        "stp_12m_3y": round(stp(idx_reg, overnight, STP_AMOUNT, start, 12, end3)),
        "overnight_only_3y": round(lump_sum(overnight, STP_AMOUNT, start, end3)),
        "lump_sum_to_2026": round(lump_sum(idx_reg, STP_AMOUNT, start, END)),
        "stp_12m_to_2026": round(stp(idx_reg, overnight, STP_AMOUNT, start, 12, END)),
    })


def swp(s, corpus, monthly_amt, start, end):
    units = corpus / nav_on_or_after(s, start)[1]
    path = []
    ran_out = None
    months = 0
    for dt in month_starts(start, end)[1:]:
        nav = nav_on_or_after(s, dt)[1]
        need = monthly_amt / nav
        if units <= need:
            units = 0.0
            ran_out = dt
            path.append((dt, 0.0))
            break
        units -= need
        months += 1
        path.append((dt, units * nav))
    final = units * nav_on_or_before(s, end)
    return final, ran_out, months, path


SWP_CORPUS, SWP_MONTHLY = 10000000, 50000
swp_rows = []
for label, start in [("Jan 2008 (top of the market)", "2008-01-01"),
                     ("Jan 2010", "2010-01-01"),
                     ("Apr 2020 (COVID low)", "2020-04-01")]:
    fin, ran_out, months, _ = swp(idx_reg, SWP_CORPUS, SWP_MONTHLY, start, END)
    fin_ov, ran_out_ov, months_ov, _ = swp(overnight, SWP_CORPUS, SWP_MONTHLY, start, END)
    swp_rows.append({"label": label, "start": start,
                     "withdrawals": months, "withdrawn_total": months * SWP_MONTHLY,
                     "corpus_at_end_equity": round(fin), "ran_out_equity": ran_out.strftime("%Y-%m-%d") if ran_out is not None else None,
                     "corpus_at_end_overnight": round(fin_ov),
                     "withdrawals_overnight": months_ov})
# how low did the Jan 2008 equity SWP corpus get, and when
_, _, _, path08 = swp(idx_reg, SWP_CORPUS, SWP_MONTHLY, "2008-01-01", END)
p08 = pd.Series({d: v for d, v in path08})
swp_2008_low = {"date": p08.idxmin().strftime("%Y-%m-%d"), "value": round(float(p08.min()))}
swp_2008_back_above_corpus = None
above = p08[p08 >= SWP_CORPUS]
if len(above):
    swp_2008_back_above_corpus = above.index[0].strftime("%Y-%m-%d")

# ---------------------------------------------------------------- write
out = {
    "_note": "GENERATED by scripts/derive_mf2.py from the CSVs in assets/data/. Do not edit by hand.",
    "sources": {
        "label": "AMFI NAV history via mfapi.in (api.mfapi.in/mf/ followed by the scheme code)",
        "overnight": {"name": "UTI Overnight Fund - Regular Plan - Growth", "code": 100814, "csv": "/assets/data/uti-overnight-fund-nav.csv",
                      "start": overnight.index[0].strftime("%Y-%m-%d"), "end": END, "points": int(len(overnight))},
        "money_market": {"name": "UTI Money Market Fund - Regular Plan - Growth", "code": 112077, "csv": "/assets/data/uti-money-market-fund-nav.csv",
                         "start": mmf.index[0].strftime("%Y-%m-%d"), "end": END, "points": int(len(mmf))},
        "gilt": {"name": "UTI Gilt Fund - Regular Plan - Growth", "code": 102510, "direct_code": 120792, "csv": "/assets/data/uti-gilt-fund-nav.csv",
                 "start": gilt.index[0].strftime("%Y-%m-%d"), "end": END, "points": int(len(gilt))},
        "etf": {"name": "UTI Nifty 50 ETF", "code": 135320, "csv": "/assets/data/uti-nifty50-etf-nav.csv",
                "start": ETF_START, "end": END, "points": int(len(etf))},
        "index_fund": {"name": "UTI Nifty 50 Index Fund", "regular_code": 100822, "direct_code": 120716, "csv": "/assets/data/uti-nifty50-index-fund-nav.csv"},
        "nifty_pri": {"name": "Nifty 50 price index (PRI)", "source": "Yahoo Finance ^NSEI", "csv": "/assets/data/nifty50-price-index.csv"},
        "lag_note": "Every series ends 31 March 2026; the first Module 2 post publishes 8 December 2026.",
    },
    "discontinuities": {
        "etf_split": etf_events[0] | {"what": "1:10 unit split — one old unit became ten new ones; NAV per unit fell to a tenth, holders' value unchanged"},
        "etf_payouts": etf_payouts,
        "etf_payout_note": "The ETF is not a growth plan; on a dividend ex-date its NAV drops by the payout while the index does not. Payouts are estimated as the one-day gap between the ETF's NAV return and the Nifty's, and the ETF series used in every comparison assumes they were reinvested (total return).",
        "overnight_face_value": ov_events[0] | {"what": "face value changed from Rs 10 to Rs 1,000 per unit; NAV per unit multiplied by 100, holders' value unchanged"},
        "money_market_face_value": mm_events[0] | {"what": "face value changed from Rs 10 to Rs 1,000 per unit; NAV per unit multiplied by 100, holders' value unchanged"},
    },
    "debt": {
        "window_start": DEBT_START, "window_end": END,
        "years": round(cagr(mmf, DEBT_START, END)[1], 1),
        "window_note": "Three-fund comparison starts 3 May 2018, when the overnight scheme took on its present mandate under SEBI's recategorisation; its earlier NAV history reflects a different portfolio and is not used.",
        "funds": debt,
        "gilt_long_run": gilt_long,
        "episodes": episodes,
        "gilt_worst_day": gilt_worst_day,
        "gilt_2008_rally": gilt_2008,
    },
    "etf_vs_index_fund": {
        "window_start": ETF_START, "window_end": END, "years": etf_years,
        "funds": etf_cmp,
        "calendar_years": cal,
        "avg_tracking_difference_pp": avg_td,
        "tracking_error_pct": te,
        "note": "Tracking difference is measured against the PRICE index, which excludes dividends; the fund receives them, so a positive difference is mostly dividend yield minus costs, not skill. See the benchmarks post.",
    },
    "categories": {
        "circular": "SEBI/HO/IMD/DF3/CIR/P/2017/114, 6 October 2017 (categorisation and rationalisation of mutual fund schemes), as amended",
        "master_circular": "Master Circular for Mutual Funds, 27 June 2024 (clause 2.6)",
        "revision_2026": "HO/24/13/15(2)2026-IMD-RAC4/I/5764/2026, 26 February 2026",
        "equity": categories_equity,
        "debt": categories_debt,
        "note": "Regulatory definitions typed from the circular, not derived from data. Verify thresholds against the current text before relying on them.",
    },
    "overlap": {
        "portfolio_a": port_a, "portfolio_b": port_b,
        "common_holdings": overlap_rows,
        "overlap_pct": overlap_pct,
        "top10_weight_a": top10_a, "top10_weight_b": top10_b,
        "note": "Both portfolios are INVENTED for the worked example. No real fund's holdings are used.",
    },
    "ratings": {
        "trailing_3y_snapshots": snapshots,
        "trailing_3y_min_pct": round(float(r3.min() * 100), 2),
        "trailing_3y_max_pct": round(float(r3.max() * 100), 2),
        "mean_reversion": {
            "pairs": int(len(pairs)),
            "corr_past3y_next3y": corr_past_future,
            "top_quartile_past_avg_pct": top_q_past, "top_quartile_next_avg_pct": top_q_next,
            "bottom_quartile_past_avg_pct": bottom_q_past, "bottom_quartile_next_avg_pct": bottom_q_next,
            "note": "Month-end trailing 3-year CAGR of the index fund vs the CAGR over the FOLLOWING 3 years, same fund.",
        },
    },
    "stp": {"amount": STP_AMOUNT, "months": 12, "parking_fund": "UTI Overnight Fund (regular)", "equity_fund": "UTI Nifty 50 Index Fund (regular)",
            "scenarios": stp_rows},
    "swp": {"corpus": SWP_CORPUS, "monthly": SWP_MONTHLY, "end": END, "scenarios": swp_rows,
            "jan2008_low": swp_2008_low, "jan2008_back_above_corpus": swp_2008_back_above_corpus},
}


class Dumper(yaml.SafeDumper):
    pass


def _float(dumper, v):
    return dumper.represent_scalar("tag:yaml.org,2002:float", f"{v}")


Dumper.add_representer(float, _float)
Dumper.add_representer(np.float64, lambda d, v: _float(d, float(v)))

with open(OUT, "w", encoding="utf-8") as f:
    f.write("# GENERATED by scripts/derive_mf2.py — do not edit by hand; re-run the script.\n")
    f.write("# Mutual Funds, Minus the Marketing — Module 2 (debt funds, ETFs, categories,\n")
    f.write("# overlap, star ratings, STP/SWP). Sources, lag check and the discontinuities\n")
    f.write("# corrected before computing anything are documented in the script header and\n")
    f.write("# in the `sources:` / `discontinuities:` blocks below.\n")
    yaml.dump(out, f, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=120)
print(f"wrote {OUT}")
