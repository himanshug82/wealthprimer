#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure quoted in the Technical Analysis Module 3 posts
("Honest tests": gaps, Fibonacci, seasonality I and II, stochastic, OBV and
VWAP, stop-loss placement, momentum vs mean reversion) and write them to
_data/ta3.yml.

    python3 scripts/derive_ta3.py            # rewrites _data/ta3.yml

WHY A SCRIPT: the posts render numbers from _data/ta3.yml via Liquid, and the
charts (scripts/make_ta3_charts.py) are drawn from the same CSVs. Nothing in
the prose is typed by hand.

DATA (both already committed, both end 30 March 2026)
  assets/data/britannia-ohlcv-2024-04-to-2026-03.csv  Yahoo Finance BRITANNIA.NS (OHLCV)
  assets/data/nifty50-price-index.csv                  Yahoo Finance ^NSEI (price index, closes only)
The first Module 3 post publishes 16 October 2026, six and a half months after
the data ends -- past the 3-month lag this blog keeps (CLAUDE.md guardrail 2).

HOUSE RULES FOR EVERY TEST (same as scripts/derive_ta2.py and the
"how to backtest honestly" post):
  * Fixed horizons (1, 5, 20 or 60 sessions; 1 month), never "to the later
    peak/trough".
  * An event whose forward window runs past the end of the data is dropped,
    and the number dropped is reported.
  * Every conditional result is printed beside its base rate (the same
    measurement on all days), with n.
  * Parameters are fixed before looking, and where a threshold is arbitrary
    the whole grid is reported, not the best cell.
  * Costs: 0.1% per side, illustrative all-in (same as ta2.yml).

Needs pandas, numpy, pyyaml (use the venv noted in TODO.md).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import yaml


class _NoAlias(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


ROOT = Path(__file__).resolve().parents[1]
PX_CSV = ROOT / "assets/data/britannia-ohlcv-2024-04-to-2026-03.csv"
NIFTY_CSV = ROOT / "assets/data/nifty50-price-index.csv"
OUT = ROOT / "_data/ta3.yml"

COST_PER_SIDE = 0.001
FIRST_POST = pd.Timestamp("2026-10-16")
RNG = np.random.default_rng(20261016)  # fixed seed: shuffle tests reproduce exactly


def r(x, nd=1):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return None
    v = round(float(x), nd)
    # whole numbers are written as ints so Liquid prints "77%", not "77.0%"
    # (CLAUDE.md: no trailing ".0"); this also turns "-0.0" into 0
    return int(v) if v == int(v) else v


def pct(x, nd=1):
    return r(x * 100, nd)


def d(ts):
    return pd.Timestamp(ts).strftime("%Y-%m-%d")


def rsi_wilder(close: pd.Series, n: int = 14) -> pd.Series:
    delta = close.diff()
    ag = delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    al = (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + ag / al)


def atr_wilder(df: pd.DataFrame, n: int = 14) -> pd.Series:
    prev = df.close.shift()
    tr = pd.concat([df.high - df.low, (df.high - prev).abs(), (df.low - prev).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def fwd_stats(x: pd.Series) -> dict:
    x = x.dropna()
    return {"n": int(len(x)), "avg_pct": pct(x.mean(), 2), "median_pct": pct(x.median(), 2),
            "share_positive_pct": pct((x > 0).mean(), 1)}


# ---------------------------------------------------------------- load
px = pd.read_csv(PX_CSV, parse_dates=["date"]).set_index("date").sort_index()
nifty = pd.read_csv(NIFTY_CSV, parse_dates=["date"]).set_index("date").sort_index()["nifty50_pri_close"]
assert px.index.is_unique and nifty.index.is_unique
assert px.index[-1] <= FIRST_POST - pd.DateOffset(months=3), "lag rule"
assert nifty.index[-1] <= FIRST_POST - pd.DateOffset(months=3), "lag rule"

out: dict = {
    "dataset": {
        "stock_as_of": "daily bars, 1 April 2024 to 30 March 2026",
        "stock_bars": int(len(px)), "stock_start": d(px.index[0]), "stock_end": d(px.index[-1]),
        "stock_csv_path": "/assets/data/britannia-ohlcv-2024-04-to-2026-03.csv",
        "stock_source_url": "https://finance.yahoo.com/quote/BRITANNIA.NS/history/",
        "index_sessions": int(len(nifty)), "index_start": d(nifty.index[0]), "index_end": d(nifty.index[-1]),
        "index_years": r((nifty.index[-1] - nifty.index[0]).days / 365.25, 1),
        "index_csv_path": "/assets/data/nifty50-price-index.csv",
        "index_source_url": "https://finance.yahoo.com/quote/%5ENSEI/history/",
        "cost_per_side_pct": COST_PER_SIDE * 100,
        "lag_months_at_first_post": int((FIRST_POST - nifty.index[-1]).days // 30),
    }
}

N = len(px)
O, H, L, C, V = (px[c].to_numpy() for c in ["open", "high", "low", "close", "volume"])

# ================================================================ 1. GAPS (Britannia)
# A gap up: today's open is above yesterday's HIGH (a visible hole in the chart).
# "Filled": price trades back to yesterday's CLOSE within the window (day 0 =
# the gap day itself, so a 1-session window means "filled the same day").
# Base rate: on every session, does price trade the same percentage distance
# back from its open within the same window?  That asks whether gaps get
# filled MORE often than any open gets revisited by the same distance.
GAP_WINDOWS = [1, 5, 20]
prev_h, prev_l, prev_c = np.r_[np.nan, H[:-1]], np.r_[np.nan, L[:-1]], np.r_[np.nan, C[:-1]]
gap_up_idx = [i for i in range(1, N) if O[i] > prev_h[i]]
gap_dn_idx = [i for i in range(1, N) if O[i] < prev_l[i]]


def touched(i, h, level, up):
    """Did price reach `level` in sessions i..i+h-1? None if the window runs past the data."""
    if i + h > N:
        return None
    return bool((L[i:i + h] <= level).any()) if up else bool((H[i:i + h] >= level).any())


def gap_block(idx, up):
    rows = {}
    sizes = np.array([abs(O[i] / C[i - 1] - 1) for i in idx])
    for h in GAP_WINDOWS:
        fills, dropped, base = [], 0, []
        for i in idx:
            f = touched(i, h, C[i - 1], up)
            if f is None:
                dropped += 1
                continue
            fills.append(f)
            dist = O[i] / C[i - 1] - 1  # signed
            hits = [touched(j, h, O[j] / (1 + dist), up) for j in range(1, N - h + 1)]
            base.append(np.mean(hits))
        rows[f"h{h}"] = {"sessions": h, "n": len(fills), "dropped_no_forward_data": dropped,
                         "fill_pct": pct(np.mean(fills), 0), "base_pct": pct(np.mean(base), 0),
                         "not_filled": int(len(fills) - sum(fills))}
    # What the stock did from the gap day's OPEN to its CLOSE, against the same
    # open-to-close move on every session (the base rate).  A round trip costs
    # 2 x 0.1%, so an average gap smaller than that is not an edge even if real.
    o2c = np.array([C[i] / O[i] - 1 for i in idx])
    return {"count": len(idx), "median_size_pct": pct(np.median(sizes), 2), "max_size_pct": pct(sizes.max(), 1),
            "windows": rows,
            "open_to_close_avg_pct": pct(o2c.mean(), 2), "open_to_close_median_pct": pct(np.median(o2c), 2),
            "open_to_close_share_up_pct": pct((o2c > 0).mean(), 0)}


gaps_up, gaps_dn = gap_block(gap_up_idx, True), gap_block(gap_dn_idx, False)
biggest_gap_i = max(gap_up_idx + gap_dn_idx, key=lambda i: abs(O[i] / C[i - 1] - 1))
bg_up = O[biggest_gap_i] > C[biggest_gap_i - 1]
bg_fill = next((k for k in range(0, N - biggest_gap_i)
                if (L[biggest_gap_i + k] <= C[biggest_gap_i - 1] if bg_up else H[biggest_gap_i + k] >= C[biggest_gap_i - 1])), None)
out["gaps"] = {
    "sessions_scanned": N - 1,
    "definition": "open beyond the previous session's high (up) or low (down); filled = trades back to the previous close",
    "up": gaps_up, "down": gaps_dn,
    "biggest": {"date": d(px.index[biggest_gap_i]), "direction": "up" if bg_up else "down",
                "prev_close": r(C[biggest_gap_i - 1], 1), "open": r(O[biggest_gap_i], 1),
                "size_pct": pct(O[biggest_gap_i] / C[biggest_gap_i - 1] - 1, 1),
                "sessions_to_fill": bg_fill, "filled_within_data": bg_fill is not None,
                "close_20_sessions_later": r(C[biggest_gap_i + 20], 1) if biggest_gap_i + 20 < N else None},
    "all_open_to_close_avg_pct": pct(np.mean(C[1:] / O[1:] - 1), 2),
    "all_open_to_close_median_pct": pct(np.median(C[1:] / O[1:] - 1), 2),
    "all_open_to_close_share_up_pct": pct(np.mean(C[1:] > O[1:]), 0),
    "round_trip_cost_pct": 2 * COST_PER_SIDE * 100,
    "all_sessions_open_vs_prev_close_abs_median_pct": pct(np.nanmedian(np.abs(O[1:] / C[:-1] - 1)), 2),
}
assert gaps_up["count"] + gaps_dn["count"] <= N - 1

# ================================================================ 2. FIBONACCI (Nifty)
# Swings from a zigzag on closes: a swing ends when price reverses by at least
# `th` from its extreme.  For consecutive pivots A -> B -> C, the retracement
# depth is (B - C) / (B - A): how much of the A->B leg the B->C leg gave back.
# Only depths below 100% are pullbacks (C did not go past A).  Test: share of
# pullback depths within +/-2 points of 38.2/50/61.8, against the same
# three-level ladder shifted by 4..10 points either way (same local density,
# levels nobody watches).  All four thresholds are reported.
FIB = np.array([38.2, 50.0, 61.8])
FIB_TOL = 2.0
FIB_SHIFTS = [s for s in range(-10, 11) if abs(s) >= 4]
FIB_THRESHOLDS = [0.03, 0.05, 0.08, 0.10]
FIB_MAIN = 0.05


def zigzag(s: pd.Series, th: float) -> list[int]:
    v = s.to_numpy(); piv = []; trend = None; ext = lo = hi = 0
    for i in range(1, len(v)):
        if trend is None:
            if v[i] >= v[lo] * (1 + th):
                trend, ext = 1, i; piv.append(lo)
            elif v[i] <= v[hi] * (1 - th):
                trend, ext = -1, i; piv.append(hi)
            else:
                lo = i if v[i] < v[lo] else lo
                hi = i if v[i] > v[hi] else hi
            continue
        if trend == 1:
            if v[i] > v[ext]:
                ext = i
            elif v[i] <= v[ext] * (1 - th):
                piv.append(ext); trend, ext = -1, i
        else:
            if v[i] < v[ext]:
                ext = i
            elif v[i] >= v[ext] * (1 + th):
                piv.append(ext); trend, ext = 1, i
    return piv  # the last, unconfirmed extreme is deliberately not a pivot


def hit_share(depths, levels):
    return float(np.mean([np.min(np.abs(levels - x)) <= FIB_TOL for x in depths]))


fib_rows, fib_main_depths = [], None
for th in FIB_THRESHOLDS:
    pv = zigzag(nifty, th); P = nifty.to_numpy()[pv]
    depth = np.array([(P[k + 1] - P[k + 2]) / (P[k + 1] - P[k]) * 100 for k in range(len(P) - 2)])
    pull = depth[depth < 100]
    fib = hit_share(pull, FIB)
    shifted = [hit_share(pull, FIB + s) for s in FIB_SHIFTS]
    fib_rows.append({"threshold_pct": int(th * 100), "swings": int(len(depth)), "pullbacks": int(len(pull)),
                     "median_depth_pct": r(np.median(pull), 0),
                     "fib_hit_pct": pct(fib, 0), "shifted_avg_hit_pct": pct(np.mean(shifted), 0),
                     "shifted_at_least_as_good": int(sum(x >= fib for x in shifted)),
                     "shifted_count": len(shifted),
                     "uniform_expectation_pct": r(len(FIB) * 2 * FIB_TOL, 0)})
    if th == FIB_MAIN:
        fib_main_depths = pull
        fib_main_pivots = pv
main = next(x for x in fib_rows if x["threshold_pct"] == int(FIB_MAIN * 100))
# one worked retracement on the main zigzag: the largest up-leg followed by a pullback
P = nifty.to_numpy(); idx = nifty.index
legs = []
for k in range(len(fib_main_pivots) - 2):
    a, b, c = fib_main_pivots[k:k + 3]
    if P[b] > P[a] and (P[b] - P[c]) / (P[b] - P[a]) < 1:
        legs.append((P[b] - P[a], a, b, c))
_, a, b, c = max(legs)
lvl = {str(f).replace(".", "_"): r(P[b] - f / 100 * (P[b] - P[a]), 0) for f in [23.6, 38.2, 50.0, 61.8, 78.6]}
out["fibonacci"] = {
    "tolerance_pts": int(FIB_TOL), "levels": [38.2, 50, 61.8],
    "shift_range": "4 to 10 points either way (14 ladders)",
    "main_threshold_pct": int(FIB_MAIN * 100),
    "main": main, "by_threshold": fib_rows,
    "depth_histogram_10pt": [int(x) for x in np.histogram(fib_main_depths, bins=range(0, 101, 10))[0]],
    "example": {"low_date": d(idx[a]), "low": r(P[a], 0), "high_date": d(idx[b]), "high": r(P[b], 0),
                "pullback_date": d(idx[c]), "pullback_low": r(P[c], 0),
                "range": r(P[b] - P[a], 0),
                "depth_pct": r((P[b] - P[c]) / (P[b] - P[a]) * 100, 1), "levels": lvl},
}
assert all(x["shifted_count"] == 14 for x in fib_rows)

# ================================================================ 3. MONTH-OF-YEAR (Nifty)
me = nifty.resample("ME").last()
me.index = me.index.to_period("M")
mret = me.pct_change().dropna()
mret = mret[mret.index >= pd.Period("2007-10", "M")]  # first complete month (data starts 17 Sep 2007)
assert mret.index[0] == pd.Period("2007-10", "M")
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
month_rows = []
for m in range(1, 13):
    x = mret[mret.index.month == m]
    month_rows.append({"month": MONTHS[m - 1][:3], "month_name": MONTHS[m - 1], "n": int(len(x)),
                       "avg_pct": pct(x.mean()), "median_pct": pct(x.median()),
                       "share_positive_pct": pct((x > 0).mean(), 0), "stdev_pct": pct(x.std()),
                       "worst_pct": pct(x.min()), "worst_year": int(x.idxmin().year),
                       "best_pct": pct(x.max()), "best_year": int(x.idxmax().year)})
by_avg = sorted(month_rows, key=lambda z: z["avg_pct"])
best_m, worst_m = by_avg[-1], by_avg[0]
spread = best_m["avg_pct"] - worst_m["avg_pct"]
# Shuffle test: scramble which month each return belongs to, 10,000 times;
# how often is the best-minus-worst month spread at least as wide as the real one?
vals = mret.to_numpy(); labels = mret.index.month.to_numpy()
cnt = 0; SHUF = 10000
for _ in range(SHUF):
    lab = RNG.permutation(labels)
    means = [vals[lab == m].mean() for m in range(1, 13)]
    cnt += (max(means) - min(means)) * 100 >= spread - 1e-9
# ...and how often does the month with the FEWEST positive years look as bad
# as the real worst one?
worst_share = min(m_["share_positive_pct"] for m_ in month_rows)
cnt2 = 0
for _ in range(2000):
    lab = RNG.permutation(labels)
    cnt2 += min((vals[lab == m] > 0).mean() for m in range(1, 13)) * 100 <= worst_share + 1e-9
# Sell in May: May-Oct of year y vs Nov(y-1)-Apr(y)
halves = []
for y in range(2008, 2026):
    s_nov, s_apr, s_oct = me[pd.Period(f"{y-1}-10", "M")], me[pd.Period(f"{y}-04", "M")], me[pd.Period(f"{y}-10", "M")]
    halves.append({"year": y, "nov_apr_pct": pct(s_apr / s_nov - 1), "may_oct_pct": pct(s_oct / s_apr - 1)})
may_oct = np.array([h["may_oct_pct"] for h in halves]); nov_apr = np.array([h["nov_apr_pct"] for h in halves])
out["seasonality"] = {
    "first_month": "October 2007", "last_month": "March 2026", "months": int(len(mret)),
    "last_month_note": "March 2026 ends on 30 March, the last row in the file",
    "all_months": {"avg_pct": pct(mret.mean()), "median_pct": pct(mret.median()),
                   "share_positive_pct": pct((mret > 0).mean(), 0), "stdev_pct": pct(mret.std())},
    "by_month": month_rows,
    "best_avg_month": best_m["month_name"], "best_avg_pct": best_m["avg_pct"],
    "worst_avg_month": worst_m["month_name"], "worst_avg_pct": worst_m["avg_pct"],
    "best_minus_worst_pp": r(spread, 1),
    "shuffle_runs": SHUF, "shuffle_share_at_least_as_wide_pct": pct(cnt / SHUF, 0),
    "fewest_positive_month": min(month_rows, key=lambda z: z["share_positive_pct"])["month_name"],
    "fewest_positive_pct": worst_share,
    "fewest_positive_count": int(sum(mret[mret.index.month == MONTHS.index(min(month_rows, key=lambda z: z["share_positive_pct"])["month_name"]) + 1] > 0)),
    "shuffle2_runs": 2000, "shuffle_share_worst_month_as_bad_pct": pct(cnt2 / 2000, 0),
    "halves": halves, "halves_years": len(halves),
    "halves_first": "May–October 2008 vs November 2007–April 2008",
    "may_oct_avg_pct": r(may_oct.mean()), "nov_apr_avg_pct": r(nov_apr.mean()),
    "may_oct_median_pct": r(np.median(may_oct)), "nov_apr_median_pct": r(np.median(nov_apr)),
    "may_oct_positive_years": int((may_oct > 0).sum()),
    "may_oct_beat_nov_apr_years": int((may_oct > nov_apr).sum()),
    "may_oct_worst": {"year": int(halves[int(np.argmin(may_oct))]["year"]), "pct": r(may_oct.min())},
    "incomplete_excluded": "November 2025–April 2026",
}
assert sum(m["n"] for m in month_rows) == len(mret)

# ================================================================ 4. BUDGET DAY AND MUHURAT (Nifty)
# Every date below is typed once, from a primary source, verified September 2026.
IB = "https://www.indiabudget.gov.in/"
NC = "https://nsearchives.nseindia.com/content/circulars/"
# Union Budget presentations (date on the cover/dateline of each Budget speech;
# 2008 from the PIB release of that day, the 2008 speech page carries no date).
BUDGETS = [
    ("2008-02-29", "Full", "https://pib.gov.in/newsite/erelcontent.aspx?relid=35836"),
    ("2009-02-16", "Interim", IB + "budget_archive/ub2009-10(I)/bs/speecha.htm"),
    ("2009-07-06", "Full", IB + "budget_archive/ub2009-10/bs/speecha.htm"),
    ("2010-02-26", "Full", IB + "budget_archive/ub2010-11/bs/speecha.htm"),
    ("2011-02-28", "Full", IB + "doc/bspeech/bs201112.pdf"),
    ("2012-03-16", "Full", IB + "doc/bspeech/bs201213.pdf"),
    ("2013-02-28", "Full", IB + "doc/bspeech/bs201314.pdf"),
    ("2014-02-17", "Interim", IB + "budget2014-2015(I)/ub2014-15/bs/bs.pdf"),
    ("2014-07-10", "Full", IB + "doc/bspeech/bs201415.pdf"),
    ("2015-02-28", "Full", IB + "doc/bspeech/bs201516.pdf"),      # Saturday; NSE live session, circular NSE/CMTR/28939 (20 Feb 2015)
    ("2016-02-29", "Full", IB + "doc/bspeech/bs201617.pdf"),
    ("2017-02-01", "Full", IB + "doc/bspeech/bs201718.pdf"),
    ("2018-02-01", "Full", IB + "doc/bspeech/bs201819.pdf"),
    ("2019-02-01", "Interim", IB + "doc/bspeech/bs201920(I).pdf"),
    ("2019-07-05", "Full", IB + "doc/bspeech/bs201920.pdf"),
    ("2020-02-01", "Full", IB + "doc/bspeech/bs202021.pdf"),      # Saturday; NSE/CMTR/43290 (22 Jan 2020)
    ("2021-02-01", "Full", IB + "doc/bspeech/bs202122.pdf"),
    ("2022-02-01", "Full", IB + "doc/bspeech/bs202223.pdf"),
    ("2023-02-01", "Full", IB + "doc/bspeech/bs2023_24.pdf"),
    ("2024-02-01", "Interim", IB + "doc/bspeech/bs2024_25(I).pdf"),
    ("2024-07-23", "Full", IB + "doc/bspeech/bs2024_25.pdf"),
    ("2025-02-01", "Full", IB + "doc/bspeech/bs2025_26.pdf"),      # Saturday; NSE/CMTR/65729 (23 Dec 2024)
    ("2026-02-01", "Full", IB + "doc/budget_speech.pdf"),          # Sunday; NSE/CMTR/72349 (16 Jan 2026)
]
WEEKEND_BUDGET_CIRCULARS = {
    "2015-02-28": ("NSE/CMTR/28939", "2015-02-20", NC + "CMTR28939.pdf"),
    "2020-02-01": ("NSE/CMTR/43290", "2020-01-22", NC + "CMTR43290.pdf"),
    "2025-02-01": ("NSE/CMTR/65729", "2024-12-23", NC + "CMTR65729.pdf"),
    "2026-02-01": ("NSE/CMTR/72349", "2026-01-16", NC + "CMTR72349.pdf"),
}
# NSE Diwali Muhurat sessions: (date, NSE equity-segment circular, circular date, normal-market window IST)
MUHURAT = [
    ("2008-10-28", "NSE/CMTR/11371", "2008-09-25", "18:15–19:15", NC + "cmtr11371.htm"),
    ("2009-10-17", "NSE/CMTR/13174", "2009-10-01", "18:15–19:15", NC + "cmtr13174.htm"),
    ("2010-11-05", "NSE/CMTR/16062", "2010-10-20", "18:15–19:00", NC + "cmtr16062.pdf"),
    ("2011-10-26", "NSE/CMTR/19187", "2011-10-20", "16:45–18:00", NC + "CMTR19187.pdf"),
    ("2012-11-13", "NSE/CMTR/22083", "2012-11-06", "15:45–17:00", NC + "CMTR22083.pdf"),
    ("2013-11-03", "NSE/CMTR/24773", "2013-10-18", "18:15–19:30", NC + "CMTR24773.pdf"),
    ("2014-10-23", "NSE/CMTR/27779", "2014-10-09", "18:30–19:30", NC + "CMTR27779.pdf"),
    ("2015-11-11", "NSE/CMTR/31047", "2015-10-30", "17:45–18:45", NC + "CMTR31047.pdf"),
    ("2016-10-30", "NSE/CMTR/33424", "2016-10-17", "18:30–19:30", NC + "CMTR33424.pdf"),
    ("2017-10-19", "NSE/CMTR/35993", "2017-10-04", "18:30–19:30", NC + "CMTR35993.pdf"),
    ("2018-11-07", "NSE/CMTR/39216", "2018-10-23", "17:30–18:30", NC + "CMTR39216.pdf"),
    ("2019-10-27", "NSE/CMTR/42483", "2019-10-23", "18:15–19:15", NC + "CMTR42483.pdf"),
    ("2020-11-14", "NSE/CMTR/46230", "2020-11-02", "18:15–19:15", NC + "CMTR46230.pdf"),
    ("2021-11-04", "NSE/CMTR/50050", "2021-10-21", "18:15–19:15", NC + "CMTR50050.pdf"),
    ("2022-10-24", "NSE/CMTR/54023", "2022-10-11", "18:15–19:15", NC + "CMTR54023.pdf"),
    ("2023-11-12", "NSE/CMTR/59124", "2023-10-27", "18:15–19:15", NC + "CMTR59124.pdf"),
    ("2024-11-01", "NSE/CMTR/64628", "2024-10-19", "18:00–19:00", NC + "CMTR64628.pdf"),
    ("2025-10-21", "NSE/CMTR/70319", "2025-09-22", "13:45–14:45", NC + "CMTR70319.pdf"),
]
WD = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

nret = nifty.pct_change()
abs_all = nret.abs().dropna()


def move(date_str):
    """Close on the event session vs the previous close in the file.  If the
    file has no row for the date, return the move from the last close before
    it to the first close after it, flagged -- that spans an extra session."""
    t = pd.Timestamp(date_str)
    before, after = nifty[nifty.index < t], nifty[nifty.index >= t]
    return {"in_file": bool(after.index[0] == t), "row_date": d(after.index[0]),
            "ret": float(after.iloc[0] / before.iloc[-1] - 1)}


def summarise(rows):
    mv = np.array([x["move_pct"] for x in rows]) / 100
    return {"n": len(rows), "avg_pct": pct(mv.mean(), 2), "median_pct": pct(np.median(mv), 2),
            "rises": int((mv > 0).sum()), "falls": int((mv < 0).sum()),
            "share_positive_pct": pct((mv > 0).mean(), 0), "avg_abs_pct": pct(np.abs(mv).mean(), 2),
            "median_abs_pct": pct(np.median(np.abs(mv)), 2),
            "biggest_rise": max(rows, key=lambda x: x["move_pct"]), "biggest_fall": min(rows, key=lambda x: x["move_pct"])}


b_in, b_out = [], []
for dt, typ, url in BUDGETS:
    m = move(dt)
    row = {"date": dt, "weekday": WD[pd.Timestamp(dt).dayofweek], "type": typ, "move_pct": pct(m["ret"], 2),
           "abs_move_percentile": int(round(float((abs_all < abs(m["ret"])).mean() * 100))), "source": url}
    if m["in_file"]:
        b_in.append(row)
    else:
        row["spans_to"] = m["row_date"]
        row["nse_special_session_circular"] = WEEKEND_BUDGET_CIRCULARS.get(dt, [None])[0]
        b_out.append(row)
mu_in, mu_out = [], []
for dt, circ, cdate, window, url in MUHURAT:
    m = move(dt)
    row = {"date": dt, "weekday": WD[pd.Timestamp(dt).dayofweek], "window": window, "circular": circ,
           "circular_date": cdate, "source": url}
    if m["in_file"]:
        row["move_pct"] = pct(m["ret"], 2)
        row["abs_move_percentile"] = int(round(float((abs_all < abs(m["ret"])).mean() * 100)))
        mu_in.append(row)
    else:
        mu_out.append(row)
b_sum, mu_sum = summarise(b_in), summarise(mu_in)
all_day = {"n": int(len(abs_all)), "avg_pct": pct(nret.mean(), 2), "median_pct": pct(nret.median(), 2),
           "share_positive_pct": pct((nret.dropna() > 0).mean(), 0), "avg_abs_pct": pct(abs_all.mean(), 2),
           "median_abs_pct": pct(abs_all.median(), 2)}
# Shuffle tests: draw the same number of random sessions 10,000 times.
pool_abs, pool_ret = abs_all.to_numpy(), nret.dropna().to_numpy()
b_sum["shuffle_share_random_as_big_pct"] = pct(np.mean(
    [RNG.choice(pool_abs, size=b_sum["n"], replace=False).mean() >= np.abs(np.array([x["move_pct"] for x in b_in])).mean() / 100 - 1e-12
     for _ in range(SHUF)]), 1)
mu_sum["shuffle_share_random_as_many_rises_pct"] = pct(np.mean(
    [(RNG.choice(pool_ret, size=mu_sum["n"], replace=False) > 0).sum() >= mu_sum["rises"] for _ in range(SHUF)]), 0)
b_sum["shuffle_share_random_as_many_falls_pct"] = pct(np.mean(
    [(RNG.choice(pool_ret, size=b_sum["n"], replace=False) < 0).sum() >= b_sum["falls"] for _ in range(SHUF)]), 0)
# Regime check: was the Budget-day move big relative to the stock market's own
# recent mood?  |move| vs the average |move| of the 20 sessions before it.
prior20 = abs_all.shift(1).rolling(20).mean()
ratio_all = (abs_all / prior20).dropna()
b_ratio = np.array([abs(x["move_pct"]) / 100 / prior20.loc[pd.Timestamp(x["date"])] for x in b_in])
b_sum["vs_prior20_median_ratio"] = r(np.median(b_ratio), 1)
b_sum["vs_prior20_share_bigger_pct"] = pct((b_ratio > 1).mean(), 0)
b_sum["vs_prior20_bigger_count"] = int((b_ratio > 1).sum())
b_sum["all_days_vs_prior20_share_bigger_pct"] = pct((ratio_all > 1).mean(), 0)
b_sum["all_days_vs_prior20_median_ratio"] = r(ratio_all.median(), 1)
b_sum["top_decile_count"] = int(sum(x["abs_move_percentile"] >= 90 for x in b_in))
b_sum["above_median_count"] = int(sum(x["abs_move_percentile"] >= 50 for x in b_in))
out["events"] = {
    "all_days": all_day,
    "budget": {"listed": len(BUDGETS), **b_sum, "first_year": BUDGETS[0][0][:4], "last_year": BUDGETS[-1][0][:4], "rows": b_in, "not_in_file": b_out, "not_in_file_count": len(b_out),
               "weekend_count": sum(pd.Timestamp(x[0]).dayofweek >= 5 for x in BUDGETS),
               "verified": "September 2026, from the dated Budget speeches on indiabudget.gov.in (2008: PIB release) and NSE circulars for weekend sessions"},
    "muhurat": {"listed": len(MUHURAT), **mu_sum, "rows": mu_in,
                "all": sorted([{**x, "in_file": True} for x in mu_in] + [{**x, "in_file": False} for x in mu_out], key=lambda x: x["date"]), "not_in_file": mu_out, "not_in_file_count": len(mu_out),
                "not_in_file_weekend": sum(pd.Timestamp(x["date"]).dayofweek >= 5 for x in mu_out),
                "verified": "September 2026, from NSE equity-segment (CMTR) circulars"},
}
assert len(b_in) + len(b_out) == len(BUDGETS) and len(mu_in) + len(mu_out) == len(MUHURAT)

# ================================================================ 5. STOCHASTIC (Britannia; Nifty from closes)
def stochastic(high, low, close, n=14, k_smooth=3, d_smooth=3):
    ll, hh = low.rolling(n).min(), high.rolling(n).max()
    fast_k = 100 * (close - ll) / (hh - ll)
    slow_k = fast_k.rolling(k_smooth).mean()
    return fast_k, slow_k, slow_k.rolling(d_smooth).mean()


HZ = 20


def cross_events(ind, lo, hi, close, warm):
    ind = ind.copy(); ind.iloc[:warm] = np.nan
    below = (ind < lo) & (ind.shift() >= lo)
    above = (ind > hi) & (ind.shift() <= hi)
    fwd = close.shift(-HZ) / close - 1
    valid_base = fwd.iloc[warm:]
    res = {}
    for name, mask in [("oversold", below), ("overbought", above)]:
        ev = fwd[mask]
        evn = ev.dropna()
        # shuffle: random sets of the same number of sessions from the scored window
        pool = valid_base.dropna().to_numpy()
        share = np.mean([RNG.choice(pool, size=len(evn), replace=False).mean() >= evn.mean() for _ in range(2000)]) if len(evn) else None
        res[name] = {**fwd_stats(ev), "raw_count": int(mask.sum()), "dropped_no_forward_data": int(ev.isna().sum()),
                     "random_sets_at_least_as_high_pct": pct(share, 0)}
    res["base"] = fwd_stats(valid_base)
    return res


fk, sk, sd_ = stochastic(px.high, px.low, px.close)
rsi_b = rsi_wilder(px.close)
# Both oscillators are scored from bar 100 on, so they share one base rate
# (RSI's unseeded-EWM warmup needs it -- see the derive_ta2 docstring).
WARM_STO = WARM_RSI = 100
sto_b = cross_events(sk, 20, 80, px.close, WARM_STO)
rsi_bt = cross_events(rsi_b, 30, 70, px.close, WARM_RSI)
both_ok = pd.concat([sk, rsi_b], axis=1).iloc[WARM_RSI:].dropna()
# Nifty: closes only, so the "high" and "low" of the window are the highest and lowest CLOSE
nk_fast, nk, nd_ = stochastic(nifty, nifty, nifty)
rsi_n = rsi_wilder(nifty)
sto_n = cross_events(nk, 20, 80, nifty, WARM_STO)
rsi_nt = cross_events(rsi_n, 30, 70, nifty, WARM_RSI)
both_n = pd.concat([nk, rsi_n], axis=1).iloc[WARM_RSI:].dropna()
# time spent at the extremes
sk_v, rsi_v = sk.iloc[WARM_RSI:].dropna(), rsi_b.iloc[WARM_RSI:].dropna()
# one worked reading (last bar of the data)
t_end = px.index[-1]; win = px.iloc[-14:]
out["stochastic"] = {
    "lookback": 14, "k_smooth": 3, "d_smooth": 3, "horizon_sessions": HZ, "lo": 20, "hi": 80,
    "britannia": {"stochastic": sto_b, "rsi": rsi_bt,
                  "corr_with_rsi": r(both_ok.corr().iloc[0, 1], 2), "corr_days": int(len(both_ok)),
                  "days_scored": int(len(sk_v)),
                  "pct_days_below_20": pct((sk_v < 20).mean(), 0), "pct_days_above_80": pct((sk_v > 80).mean(), 0),
                  "pct_days_rsi_below_30": pct((rsi_v < 30).mean(), 0), "pct_days_rsi_above_70": pct((rsi_v > 70).mean(), 0)},
    "nifty_closes": {"stochastic": sto_n, "rsi": rsi_nt,
                     "corr_with_rsi": r(both_n.corr().iloc[0, 1], 2), "corr_days": int(len(both_n))},
    "worked": {"date": d(t_end), "close": r(px.close.iloc[-1], 1),
               "lowest_low_14": r(win.low.min(), 1), "highest_high_14": r(win.high.max(), 1),
               "fast_k": r(fk.iloc[-1], 1), "slow_k": r(sk.iloc[-1], 1), "slow_d": r(sd_.iloc[-1], 1),
               "fast_k_prev1": r(fk.iloc[-2], 1), "fast_k_prev2": r(fk.iloc[-3], 1)},
}
assert abs((px.close.iloc[-1] - win.low.min()) / (win.high.max() - win.low.min()) * 100 - fk.iloc[-1]) < 1e-9
assert abs(np.mean([fk.iloc[-1], fk.iloc[-2], fk.iloc[-3]]) - sk.iloc[-1]) < 1e-9

# ================================================================ 6. OBV and VWAP (Britannia)
sign = np.sign(px.close.diff()).fillna(0)
obv = (sign * px.volume).cumsum()
LB = 20
p_chg, o_chg = px.close.pct_change(LB), obv.diff(LB)
agree = (np.sign(p_chg) == np.sign(o_chg))[LB:]
fwd = px.close.shift(-HZ) / px.close - 1
bear_div = (p_chg > 0) & (o_chg < 0)
bull_div = (p_chg < 0) & (o_chg > 0)
first_bear = bear_div & ~bear_div.shift(fill_value=False)
first_bull = bull_div & ~bull_div.shift(fill_value=False)
vol_top = px.volume.idxmax()
# anchored VWAP from the first session of FY 2025-26, approximated from daily bars
# with the "typical price" (H+L+C)/3 -- real VWAP needs every trade in the day.
anchor = px.index[px.index >= pd.Timestamp("2025-04-01")][0]
seg = px.loc[anchor:]
tp = (seg.high + seg.low + seg.close) / 3
avwap = (tp * seg.volume).cumsum() / seg.volume.cumsum()
# hypothetical intraday session to show the real calculation (not market data)
TRADES = [("9:15 am", 5000, 400), ("10:30 am", 5020, 150), ("11:45 am", 4990, 900), ("1:30 pm", 5040, 100), ("3:15 pm", 5030, 450)]
tv = sum(p * q for _, p, q in TRADES); tq = sum(q for _, _, q in TRADES)
out["obv"] = {
    "lookback": LB, "horizon_sessions": HZ,
    "obv_end_million": r(obv.iloc[-1] / 1e6, 2), "obv_min_million": r(obv.min() / 1e6, 2), "obv_min_date": d(obv.idxmin()),
    "obv_max_million": r(obv.max() / 1e6, 2), "obv_max_date": d(obv.idxmax()),
    "agree_pct": pct(agree.mean(), 0), "agree_days": int(len(agree)),
    "bearish_divergence": {**fwd_stats(fwd[first_bear]), "raw_count": int(first_bear.sum())},
    "bullish_divergence": {**fwd_stats(fwd[first_bull]), "raw_count": int(first_bull.sum())},
    "base": fwd_stats(fwd.iloc[LB:]),
    "biggest_volume_day": {"date": d(vol_top), "volume": int(px.volume.loc[vol_top]),
                           "median_volume": int(px.volume.median()),
                           "multiple_of_median": r(px.volume.loc[vol_top] / px.volume.median(), 1),
                           "close_change_pct": pct(px.close.pct_change().loc[vol_top], 2)},
    "vwap_hypothetical": {"trades": [{"time": t, "price": p, "qty": q, "value": p * q} for t, p, q in TRADES],
                          "total_value": tv, "total_qty": tq, "vwap": r(tv / tq, 2),
                          "simple_avg_price": r(np.mean([p for _, p, _ in TRADES]), 2)},
    "anchored_vwap": {"anchor": d(anchor), "end": d(seg.index[-1]), "sessions": int(len(seg)),
                      "value_end": r(avwap.iloc[-1], 1), "close_end": r(seg.close.iloc[-1], 1),
                      "simple_avg_close": r(seg.close.mean(), 1),
                      "pct_closes_above": pct((seg.close > avwap).mean(), 0),
                      "crossings": int(((seg.close > avwap) != (seg.close > avwap).shift()).iloc[1:].sum())},
}
assert abs(obv.iloc[-1] - (sign * px.volume).sum()) < 1

# ================================================================ 7. STOP-LOSS PLACEMENT (Britannia)
# Enter at the close of EVERY session that has 20 sessions of history and
# 20 sessions of future (no cherry-picked entries).  Three stops:
#   fixed 5% below entry; 2 x ATR(14) below entry; just below the lowest low of
#   the last 20 sessions (the "swing low", one tick = Rs 0.05 below it).
# A stop triggers when a later session's low reaches it; the fill is the stop
# price, or the open if the stock opened below it (a gap through the stop).
# Not stopped -> exit at the close 20 sessions later.  0.1% per side.
atr = atr_wilder(px)
SH = 20
WARM_ATR = 20
entries = range(max(SH, WARM_ATR), N - SH)
dropped_tail = N - SH  # entries from here on have no complete 20-session future


def run_stop(i, stop):
    for j in range(i + 1, i + SH + 1):
        if L[j] <= stop:
            fill = min(O[j], stop)
            return True, fill, j - i, O[j] < stop
    return False, C[i + SH], SH, False


def stop_level(kind, i):
    if kind == "fixed_5pct":
        return C[i] * 0.95
    if kind == "atr_2x":
        return C[i] - 2 * atr.iloc[i]
    if kind == "swing_low_20":
        return L[i - SH + 1:i + 1].min() - 0.05
    raise ValueError(kind)


no_stop = np.array([C[i + SH] / C[i] - 1 - 2 * COST_PER_SIDE for i in entries])
stops = {}
for kind in ["fixed_5pct", "atr_2x", "swing_low_20"]:
    hit, rets, dist, gapped, slip, whipsaw, days = [], [], [], [], [], [], []
    for i in entries:
        s = stop_level(kind, i)
        h_, fill, k_, g_ = run_stop(i, s)
        hit.append(h_); dist.append(1 - s / C[i]); rets.append(fill / C[i] - 1 - 2 * COST_PER_SIDE)
        if h_:
            days.append(k_); gapped.append(g_)
            if g_:
                slip.append(1 - fill / s)
            whipsaw.append(C[i + SH] > C[i])
    rets = np.array(rets)
    stops[kind] = {"median_distance_pct": pct(np.median(dist), 1), "min_distance_pct": pct(min(dist), 1),
                   "max_distance_pct": pct(max(dist), 1),
                   "hit_pct": pct(np.mean(hit), 0), "hits": int(sum(hit)),
                   "median_sessions_to_hit": int(np.median(days)) if days else None,
                   "gapped_through": int(sum(gapped)), "avg_extra_slippage_when_gapped_pct": pct(np.mean(slip), 2) if slip else None,
                   "whipsaw_pct": pct(np.mean(whipsaw), 0) if whipsaw else None,
                   "avg_return_pct": pct(rets.mean(), 2), "worst_return_pct": pct(rets.min(), 1),
                   "share_positive_pct": pct((rets > 0).mean(), 0)}
out["stops"] = {
    "entries": len(entries), "first_entry": d(px.index[entries[0]]), "last_entry": d(px.index[entries[-1]]),
    "horizon_sessions": SH, "atr_mult": 2, "fixed_pct": 5, "swing_lookback": SH,
    "dropped_no_forward_data": N - entries[-1] - 1,
    "no_stop": {"avg_return_pct": pct(no_stop.mean(), 2), "worst_return_pct": pct(no_stop.min(), 1),
                "share_positive_pct": pct((no_stop > 0).mean(), 0)},
    **stops,
}
assert all(stops[k]["hits"] <= len(entries) for k in stops)

# ================================================================ 8. MOMENTUM vs MEAN REVERSION (Nifty)
# Monthly: 12-1 momentum at month-end t = return from end of month t-12 to end
# of month t-1 (skipping the latest month, as Jegadeesh-Titman style studies
# do).  Next month's return is the outcome.  Short-term reversal: last month's
# own return vs next month.  Weekly and daily lag-1 autocorrelations too.
mom = me.shift(1) / me.shift(12) - 1
nxt = me.shift(-1) / me - 1
last1 = me / me.shift(1) - 1
df = pd.DataFrame({"mom": mom, "last1": last1, "next": nxt}).dropna()
pos_m, neg_m = df[df.mom > 0], df[df.mom <= 0]
up1, dn1 = df[df.last1 > 0], df[df.last1 <= 0]
q = df.last1.quantile([0.2, 0.8])
worst_q, best_q = df[df.last1 <= q.iloc[0]], df[df.last1 >= q.iloc[1]]


def blk(x):
    return {"n": int(len(x)), "avg_next_pct": pct(x.next.mean(), 2), "median_next_pct": pct(x.next.median(), 2),
            "share_next_positive_pct": pct((x.next > 0).mean(), 0), "stdev_next_pct": pct(x.next.std(), 1)}


df_ex = df[(df.index < pd.Period("2008-09", "M")) | (df.index > pd.Period("2009-12", "M"))]
wk = nifty.resample("W-FRI").last().pct_change().dropna()
dy = nifty.pct_change().dropna()
mo = me.pct_change().dropna()


def ac(x):
    return {"n": int(len(x) - 1), "autocorr": r(x.autocorr(1), 3), "noise_band": r(2 / np.sqrt(len(x) - 1), 3)}


# the 2008 and 2020 crashes: what the 12-1 signal said going in and coming out
crash = []
for per in ["2008-10", "2009-05", "2020-03", "2020-04"]:
    p_ = pd.Period(per, "M")
    prev = p_ - 1
    if prev in df.index:
        crash.append({"month": per, "signal_at_prev_month_end": "positive" if df.loc[prev, "mom"] > 0 else "negative",
                      "momentum_pct": pct(df.loc[prev, "mom"], 1), "month_return_pct": pct(df.loc[prev, "next"], 1)})
out["momentum"] = {
    "first_signal": df.index[0].strftime("%B %Y"), "last_signal": df.index[-1].strftime("%B %Y"), "months": int(len(df)),
    "base": blk(df),
    "mom_positive": blk(pos_m), "mom_negative": blk(neg_m),
    "pct_months_positive_mom": pct(len(pos_m) / len(df), 0),
    # robustness: drop every signal from September 2008 to December 2009
    # (the crash and the rebound) and re-split
    "ex_2008_09": {"mom_positive": blk(df_ex[df_ex.mom > 0]), "mom_negative": blk(df_ex[df_ex.mom <= 0]),
                   "dropped_months": int(len(df) - len(df_ex))},
    "last_month_up": blk(up1), "last_month_down": blk(dn1),
    "last_month_worst_fifth": {**blk(worst_q), "cutoff_pct": pct(q.iloc[0], 1)},
    "last_month_best_fifth": {**blk(best_q), "cutoff_pct": pct(q.iloc[1], 1)},
    "corr_mom_next": r(df.mom.corr(df.next), 2), "corr_last1_next": r(df.last1.corr(df.next), 2),
    "autocorr_daily": ac(dy), "autocorr_weekly": ac(wk), "autocorr_monthly": ac(mo),
    "crash_months": crash,
}
assert len(pos_m) + len(neg_m) == len(df)

# ---------------------------------------------------------------- write
header = (
    "# Technical Analysis — Module 3 (\"Honest tests\"): every figure quoted in the\n"
    "# gaps, Fibonacci, seasonality I/II, stochastic, OBV/VWAP, stop-loss and\n"
    "# momentum posts.\n#\n"
    "# GENERATED by scripts/derive_ta3.py from the two committed CSVs plus the\n"
    "# primary-source event dates typed in the script — do not edit by hand;\n"
    "# re-run the script. Data ends 2026-03-30; the first Module 3 post\n"
    "# publishes 2026-10-16 (6.5 months later, past the 3-month house rule).\n#\n"
    "# Every conditional figure sits beside its base rate and its n. Horizons are\n"
    "# fixed; events without a complete forward window are dropped and counted.\n\n"
)
OUT.write_text(header + yaml.dump(out, Dumper=_NoAlias, sort_keys=False, allow_unicode=True, default_flow_style=False), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
