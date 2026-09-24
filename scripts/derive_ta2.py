#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure quoted in the Technical Analysis Module 2 posts
(Bollinger Bands & ATR, relative strength vs the index, multiple timeframes,
honest backtesting) and write them to _data/ta2.yml.

    python3 scripts/derive_ta2.py            # rewrites _data/ta2.yml

WHY A SCRIPT: the posts render numbers from _data/ta2.yml via Liquid, and the
charts (scripts/make_ta2_charts.py) are drawn from the same CSVs. Nothing in
the prose is typed by hand, so a figure in a table can never disagree with the
chart beside it. Same discipline as _data/ta.yml (see its header).

DATA
  assets/data/britannia-ohlcv-2024-04-to-2026-03.csv  Yahoo Finance BRITANNIA.NS
  assets/data/nifty50-price-index.csv                  Yahoo Finance ^NSEI (PRI)
Both end 30 March 2026. The first Module 2 post publishes 18 December 2026,
eight and a half months later — well past the 3-month lag rule in CLAUDE.md.

CONVENTIONS (match _data/ta.yml): SMA = simple rolling mean; RSI = 14-period
Wilder smoothing (EWM alpha = 1/14); ATR = 14-period Wilder smoothing of true
range; Bollinger = 20-day SMA ± 2 population standard deviations (ddof=0, as
Bollinger specified). Indicator values are never quoted from inside their
warmup window.

Needs pandas, numpy, pyyaml (not in the system python on this machine — use
the venv noted in TODO.md).
"""
from __future__ import annotations

import itertools
from pathlib import Path

import numpy as np
import pandas as pd
import yaml


class _NoAlias(yaml.SafeDumper):
    """Jekyll's YAML loader is safest without anchors/aliases; repeat values instead."""
    def ignore_aliases(self, data):
        return True

ROOT = Path(__file__).resolve().parents[1]
PX_CSV = ROOT / "assets/data/britannia-ohlcv-2024-04-to-2026-03.csv"
NIFTY_CSV = ROOT / "assets/data/nifty50-price-index.csv"
OUT = ROOT / "_data/ta2.yml"

COST_PER_SIDE = 0.001      # 0.1% per side, illustrative all-in (brokerage + STT + charges)
START_CAPITAL = 100000     # Rs 1,00,000


def r(x, nd=1):
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), nd)


def d(ts):
    return pd.Timestamp(ts).strftime("%Y-%m-%d")


# ---------------------------------------------------------------- indicators
def rsi_wilder(close: pd.Series, n: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    ag = gain.ewm(alpha=1 / n, adjust=False).mean()
    al = loss.ewm(alpha=1 / n, adjust=False).mean()
    return 100 - 100 / (1 + ag / al)


def atr_wilder(df: pd.DataFrame, n: int = 14) -> pd.Series:
    prev = df.close.shift()
    tr = pd.concat([df.high - df.low, (df.high - prev).abs(), (df.low - prev).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def max_drawdown(equity: pd.Series) -> float:
    return float((equity / equity.cummax() - 1).min() * 100)


def cagr(equity: pd.Series) -> float:
    years = (equity.index[-1] - equity.index[0]).days / 365.25
    return float(((equity.iloc[-1] / equity.iloc[0]) ** (1 / years) - 1) * 100)


# ---------------------------------------------------------------- load
px = pd.read_csv(PX_CSV, parse_dates=["date"]).set_index("date").sort_index()
nifty = pd.read_csv(NIFTY_CSV, parse_dates=["date"]).set_index("date").sort_index()["nifty50_pri_close"]

out: dict = {
    "dataset": {
        "symbol": "BRITANNIA.NS",
        "bars": int(len(px)),
        "start": d(px.index[0]),
        "end": d(px.index[-1]),
        "as_of": "Daily bars, 1 April 2024 to 30 March 2026",
        "csv_path": "/assets/data/britannia-ohlcv-2024-04-to-2026-03.csv",
        "source_url": "https://finance.yahoo.com/quote/BRITANNIA.NS/history/",
        "index_csv_path": "/assets/data/nifty50-price-index.csv",
        "index_source_url": "https://finance.yahoo.com/quote/%5ENSEI/history/",
        "first_post_date": "2026-12-18",
        "lag_months": 8.5,
    }
}

# ---------------------------------------------------------------- 1. Bollinger + ATR
n_bb = 20
mid = px.close.rolling(n_bb).mean()
sd = px.close.rolling(n_bb).std(ddof=0)
upper, lower = mid + 2 * sd, mid - 2 * sd
pct_b = (px.close - lower) / (upper - lower)
bandwidth = (upper - lower) / mid * 100
atr = atr_wilder(px)
atr_pct = atr / px.close * 100

valid = px.index[n_bb:]  # after warmup
above = (px.close > upper).loc[valid]
below = (px.close < lower).loc[valid]

fwd10 = px.close.shift(-10) / px.close - 1
after_upper = fwd10.loc[valid][above]
after_lower = fwd10.loc[valid][below]

# Squeezes: bandwidth at a 120-bar low. Take the first bar of each squeeze
# episode (bars where bandwidth == rolling 120 min), then the 20-bar forward move.
roll_min = bandwidth.rolling(120).min()
is_sq = (bandwidth <= roll_min + 1e-9) & roll_min.notna()
sq_dates = [t for t in px.index[is_sq] if t >= px.index[140]]
# collapse consecutive squeeze days into episodes (gap > 10 bars starts a new one)
episodes = []
for t in sq_dates:
    if not episodes or (px.index.get_loc(t) - px.index.get_loc(episodes[-1][-1])) > 10:
        episodes.append([t])
    else:
        episodes[-1].append(t)
sq_rows = []
for ep in episodes:
    t = ep[-1]  # tightest/last day of the episode
    i = px.index.get_loc(t)
    if i + 20 >= len(px):
        continue
    later = px.index[i + 20]
    move = px.close.iloc[i + 20] / px.close.iloc[i] - 1
    sq_rows.append({"date": d(t), "bandwidth_pct": r(bandwidth.iloc[i], 1), "close": r(px.close.iloc[i], 1),
                    "close_20_bars_later": r(px.close.iloc[i + 20], 1), "later_date": d(later),
                    "move_20_bars_pct": r(move * 100, 1)})
sq_sorted = sorted(sq_rows, key=lambda x: abs(x["move_20_bars_pct"]))
squeeze_big = sq_sorted[-1]
squeeze_nothing = sq_sorted[0]

# ATR stop example: the golden-cross day from ta.yml (2025-06-04) for continuity
stop_day = pd.Timestamp("2025-06-04")
i_stop = px.index.get_loc(stop_day)
out["bollinger"] = {
    "period": n_bb, "std_mult": 2, "std_ddof": 0,
    "bars_after_warmup": int(len(valid)),
    "closes_above_upper": int(above.sum()),
    "closes_below_lower": int(below.sum()),
    "pct_bars_inside_bands": r(100 - (above.sum() + below.sum()) / len(valid) * 100, 1),
    "avg_10d_return_after_close_above_upper_pct": r(after_upper.mean() * 100, 2),
    "avg_10d_return_after_close_below_lower_pct": r(after_lower.mean() * 100, 2),
    "share_positive_10d_after_upper_pct": r((after_upper > 0).mean() * 100, 0),
    "share_positive_10d_after_lower_pct": r((after_lower > 0).mean() * 100, 0),
    "bandwidth_min_pct": r(bandwidth.min(), 1), "bandwidth_min_date": d(bandwidth.idxmin()),
    "bandwidth_max_pct": r(bandwidth.max(), 1), "bandwidth_max_date": d(bandwidth.idxmax()),
    "bandwidth_median_pct": r(bandwidth.median(), 1),
    "squeeze_lookback_bars": 120,
    "squeeze_episodes": len(sq_rows),
    "squeeze_then_big_move": squeeze_big,
    "squeeze_then_nothing": squeeze_nothing,
    "all_squeezes": sq_rows,
}
out["atr"] = {
    "period": 14,
    "atr_end": r(atr.iloc[-1], 1), "atr_end_pct": r(atr_pct.iloc[-1], 2),
    "atr_min": r(atr.iloc[14:].min(), 1), "atr_min_date": d(atr.iloc[14:].idxmin()),
    "atr_max": r(atr.iloc[14:].max(), 1), "atr_max_date": d(atr.iloc[14:].idxmax()),
    "atr_pct_median": r(atr_pct.iloc[14:].median(), 2),
    "stop_example": {
        "date": d(stop_day), "close": r(px.close.iloc[i_stop], 1), "atr": r(atr.iloc[i_stop], 1),
        "stop_2atr": r(px.close.iloc[i_stop] - 2 * atr.iloc[i_stop], 1),
        "stop_distance_pct": r(2 * atr.iloc[i_stop] / px.close.iloc[i_stop] * 100, 1),
        "risk_budget": 2000,  # Rs, illustrative 2% of a Rs 1,00,000 account
        "shares_for_budget": int(2000 // (2 * atr.iloc[i_stop])),
        "lowest_low_next_20_bars": r(px.low.iloc[i_stop + 1:i_stop + 21].min(), 1),
        "stop_hit_within_20_bars": bool(px.low.iloc[i_stop + 1:i_stop + 21].min() < px.close.iloc[i_stop] - 2 * atr.iloc[i_stop]),
    },
}

# ---------------------------------------------------------------- 2. Relative strength vs Nifty
both = pd.concat([px.close.rename("stock"), nifty.rename("nifty")], axis=1).dropna()
ratio = both.stock / both.nifty
rs = ratio / ratio.iloc[0] * 100
rs_ma = rs.rolling(50).mean()
stock_ret = both.stock.iloc[-1] / both.stock.iloc[0] - 1
index_ret = both.nifty.iloc[-1] / both.nifty.iloc[0] - 1
# the major decline window from ta.yml
w0, w1 = pd.Timestamp("2024-10-03"), pd.Timestamp("2025-03-04")
s_w = both.stock.loc[w0:w1]; i_w = both.nifty.loc[w0:w1]
# RS above/below its MA: fraction of bars, and the longest stretch below
rs_above = (rs > rs_ma).loc[rs_ma.dropna().index]
stretches = [(k, len(list(g))) for k, g in itertools.groupby(rs_above)]
longest_below = max((n for k, n in stretches if not k), default=0)
longest_above = max((n for k, n in stretches if k), default=0)
# best/worst 60-day relative performance
rel60 = rs / rs.shift(60) - 1
out["relative_strength"] = {
    "common_start": d(both.index[0]), "common_end": d(both.index[-1]), "common_bars": int(len(both)),
    "rs_start": 100.0, "rs_end": r(rs.iloc[-1], 1),
    "rs_high": r(rs.max(), 1), "rs_high_date": d(rs.idxmax()),
    "rs_low": r(rs.min(), 1), "rs_low_date": d(rs.idxmin()),
    "stock_total_return_pct": r(stock_ret * 100, 1), "index_total_return_pct": r(index_ret * 100, 1),
    "stock_minus_index_pp": r((stock_ret - index_ret) * 100, 1),
    "ma_period": 50,
    "pct_bars_rs_above_ma": r(rs_above.mean() * 100, 0),
    "longest_stretch_below_ma_bars": int(longest_below), "longest_stretch_above_ma_bars": int(longest_above),
    "decline_window": {
        "start": d(w0), "end": d(w1),
        "stock_pct": r((s_w.iloc[-1] / s_w.iloc[0] - 1) * 100, 1),
        "index_pct": r((i_w.iloc[-1] / i_w.iloc[0] - 1) * 100, 1),
    },
    "best_60d_relative": {"date": d(rel60.idxmax()), "pct": r(rel60.max() * 100, 1)},
    "worst_60d_relative": {"date": d(rel60.idxmin()), "pct": r(rel60.min() * 100, 1)},
}

# ---------------------------------------------------------------- 3. Multiple timeframes
wk = px.resample("W-FRI").agg({"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}).dropna()
wk_ma = wk.close.rolling(20).mean()
wk_trend_up = (wk.close > wk_ma)
wk_rsi = rsi_wilder(wk.close)
daily_rsi = rsi_wilder(px.close)
# map each daily bar to the trend of the PREVIOUS completed week (no look-ahead)
prev_week_trend = wk_trend_up.shift(1).reindex(px.index, method="ffill")
oversold = (daily_rsi < 30) & (daily_rsi.shift() >= 30)  # first day of an oversold episode
oversold = oversold[px.index[14:]]
ev = []
for t in px.index[14:][oversold]:
    i = px.index.get_loc(t)
    if i + 20 >= len(px) or pd.isna(prev_week_trend.loc[t]):
        continue
    ev.append({"date": d(t), "rsi": r(daily_rsi.iloc[i], 1), "close": r(px.close.iloc[i], 1),
               "weekly_trend": "up" if prev_week_trend.loc[t] else "down",
               "fwd_20_bars_pct": r((px.close.iloc[i + 20] / px.close.iloc[i] - 1) * 100, 1),
               "lowest_low_next_20_bars": r(px.low.iloc[i + 1:i + 21].min(), 1)})
ev_up = [e for e in ev if e["weekly_trend"] == "up"]
ev_dn = [e for e in ev if e["weekly_trend"] == "down"]
out["multi_timeframe"] = {
    "weekly_bars": int(len(wk)), "weekly_ma_period": 20, "weekly_ma_first_date": d(wk_ma.dropna().index[0]),
    "weeks_in_uptrend": int(wk_trend_up.loc[wk_ma.dropna().index].sum()),
    "weeks_in_downtrend": int((~wk_trend_up.loc[wk_ma.dropna().index]).sum()),
    "weekly_rsi_min": r(wk_rsi.iloc[14:].min(), 1), "weekly_rsi_min_date": d(wk_rsi.iloc[14:].idxmin()),
    "weekly_rsi_max": r(wk_rsi.iloc[14:].max(), 1), "weekly_rsi_max_date": d(wk_rsi.iloc[14:].idxmax()),
    "daily_oversold_events": len(ev),
    "in_weekly_uptrend": {"count": len(ev_up), "avg_fwd_20_bars_pct": r(np.mean([e["fwd_20_bars_pct"] for e in ev_up]) if ev_up else None, 1),
                          "share_positive_pct": r(np.mean([e["fwd_20_bars_pct"] > 0 for e in ev_up]) * 100 if ev_up else None, 0)},
    "in_weekly_downtrend": {"count": len(ev_dn), "avg_fwd_20_bars_pct": r(np.mean([e["fwd_20_bars_pct"] for e in ev_dn]) if ev_dn else None, 1),
                            "share_positive_pct": r(np.mean([e["fwd_20_bars_pct"] > 0 for e in ev_dn]) * 100 if ev_dn else None, 0)},
    "events": ev,
    "example_downtrend_kept_falling": min(ev_dn, key=lambda e: e["fwd_20_bars_pct"]) if ev_dn else None,
    "example_uptrend_bounced": max(ev_up, key=lambda e: e["fwd_20_bars_pct"]) if ev_up else None,
    "example_uptrend_failed": min(ev_up, key=lambda e: e["fwd_20_bars_pct"]) if ev_up else None,
    "example_downtrend_bounced": max(ev_dn, key=lambda e: e["fwd_20_bars_pct"]) if ev_dn else None,
}

# ---------------------------------------------------------------- 4. Backtests
START_BAR = 200  # every strategy and the benchmark start once the slowest SMA exists
bt_px = px.iloc[START_BAR:]
bt_start, bt_end = bt_px.index[0], bt_px.index[-1]


def run(signal: pd.Series, exec_lag: int, cost: float):
    """Long-only. signal[t]=1 means 'want to be long' decided on bar t's close.
    exec_lag=0 trades at bar t's close (look-ahead: the decision uses a price
    you could not have traded at); exec_lag=1 trades at bar t+1's close."""
    pos = signal.shift(exec_lag).fillna(0).astype(int).loc[bt_start:bt_end]
    close = px.close.loc[bt_start:bt_end]
    ret = close.pct_change().fillna(0)
    strat = pos.shift(1).fillna(0) * ret  # position held over the bar earns the bar's return
    turns = pos.diff().abs().fillna(pos.iloc[0])
    strat = strat - turns * cost
    eq = START_CAPITAL * (1 + strat).cumprod()
    trades = int((pos.diff() == 1).sum() + (pos.iloc[0] == 1))
    return {"final_value": r(eq.iloc[-1], 0), "cagr_pct": r(cagr(eq), 1), "max_drawdown_pct": r(max_drawdown(eq), 1),
            "trades": trades, "pct_time_invested": r(pos.mean() * 100, 0)}, eq


def sma_signal(fast, slow):
    return (px.close.rolling(fast).mean() > px.close.rolling(slow).mean()).astype(int)


def rsi_signal(lo=30, hi=70):
    rsi = daily_rsi
    sig = pd.Series(np.nan, index=px.index)
    sig[rsi < lo] = 1
    sig[rsi > hi] = 0
    return sig.ffill().fillna(0).astype(int)


bh_eq = START_CAPITAL * bt_px.close / bt_px.close.iloc[0]
buy_hold = {"final_value": r(bh_eq.iloc[-1], 0), "cagr_pct": r(cagr(bh_eq), 1), "max_drawdown_pct": r(max_drawdown(bh_eq), 1),
            "trades": 1, "pct_time_invested": 100}

strategies = {"sma_50_200": sma_signal(50, 200), "sma_20_50": sma_signal(20, 50), "rsi_30_70": rsi_signal()}
results = {}
for name, sig in strategies.items():
    results[name] = {
        "lookahead_no_cost": run(sig, 0, 0.0)[0],
        "next_day_no_cost": run(sig, 1, 0.0)[0],
        "next_day_with_cost": run(sig, 1, COST_PER_SIDE)[0],
    }

# parameter grid on next-day execution with costs
grid = []
for fast, slow in itertools.product([10, 20, 30, 50], [50, 100, 150, 200]):
    if fast >= slow:
        continue
    res, _ = run(sma_signal(fast, slow), 1, COST_PER_SIDE)
    grid.append({"fast": fast, "slow": slow, **res})
grid_sorted = sorted(grid, key=lambda g: g["cagr_pct"])
out["backtest"] = {
    "start": d(bt_start), "end": d(bt_end), "bars": int(len(bt_px)),
    "years": r((bt_end - bt_start).days / 365.25, 2),
    "start_capital": START_CAPITAL, "cost_per_side_pct": COST_PER_SIDE * 100,
    "why_start_at_bar_200": "every strategy and the benchmark begin on the first bar where the 200-day SMA exists, so they are compared over the same window",
    "buy_and_hold": buy_hold,
    "strategies": results,
    "grid": grid, "grid_best": grid_sorted[-1], "grid_worst": grid_sorted[0],
    # pre-shaped for a plain Liquid table: one row per fast length, one cell per slow length
    "grid_table": {
        "slows": [50, 100, 150, 200],
        "rows": [
            {"fast": f, "cells": [
                (next((f"{g['cagr_pct']:+.1f}%" for g in grid if g["fast"] == f and g["slow"] == sl), "—"))
                for sl in [50, 100, 150, 200]]}
            for f in [10, 20, 30, 50]],
    },
    "grid_spread_pp": r(grid_sorted[-1]["cagr_pct"] - grid_sorted[0]["cagr_pct"], 1),
    "grid_beating_buy_and_hold": int(sum(g["cagr_pct"] > buy_hold["cagr_pct"] for g in grid)),
    "grid_size": len(grid),
}

# ---------------------------------------------------------------- write
header = (
    "# Technical Analysis — Module 2: every figure quoted in the Bollinger/ATR,\n"
    "# relative-strength, multiple-timeframe and backtesting posts.\n#\n"
    "# GENERATED by scripts/derive_ta2.py from the two committed CSVs — do not\n"
    "# edit by hand; re-run the script. Conventions and the lag check are in the\n"
    "# script's docstring. Data ends 2026-03-30; first Module 2 post publishes\n"
    "# 2026-12-18 (8.5 months later, well past the 3-month rule in CLAUDE.md).\n#\n"
    "# HONESTY NOTE baked into backtest: 'lookahead_no_cost' deliberately trades\n"
    "# at the same close the signal was computed from (a bias every beginner's\n"
    "# first backtest has); 'next_day_with_cost' is the fair version. The grid of\n"
    "# SMA pairs exists to show how much the answer depends on parameters chosen\n"
    "# after seeing the data. Two years of one stock proves nothing either way.\n\n"
)
OUT.write_text(header + yaml.dump(out, Dumper=_NoAlias, sort_keys=False, allow_unicode=True, default_flow_style=False), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
print(yaml.safe_dump({"buy_and_hold": buy_hold, "strategies": results, "grid_best": grid_sorted[-1], "grid_worst": grid_sorted[0]}, sort_keys=False))
print("squeeze big:", squeeze_big, "\nsqueeze nothing:", squeeze_nothing)
print("RS:", {k: v for k, v in out["relative_strength"].items() if not isinstance(v, dict)})
print("MTF:", {k: v for k, v in out["multi_timeframe"].items() if k != "events"})
