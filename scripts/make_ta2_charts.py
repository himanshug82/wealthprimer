#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Draw the four charts for Technical Analysis Module 2 into assets/charts/:

    ta2-bollinger-atr.svg        price with 20-day Bollinger Bands, bandwidth, ATR(14)
    ta2-relative-strength.svg    Britannia / Nifty 50 ratio rebased to 100, with 50-day MA
    ta2-multi-timeframe.svg      weekly closes + 20-week SMA over daily RSI(14)
    ta2-backtest.svg             equity curves: buy & hold vs the three rules (next-day, costs)

    python3 scripts/make_ta2_charts.py

Same CSVs, same indicator conventions and the same palette as the series-1
ta-*.svg charts and scripts/derive_ta2.py, so the picture can never disagree
with the number printed beside it. Re-run after re-running derive_ta2.py.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/charts"
px = pd.read_csv(ROOT / "assets/data/britannia-ohlcv-2024-04-to-2026-03.csv", parse_dates=["date"]).set_index("date").sort_index()
nifty = pd.read_csv(ROOT / "assets/data/nifty50-price-index.csv", parse_dates=["date"]).set_index("date").sort_index()["nifty50_pri_close"]

NAVY, GREEN, RED, ORANGE, GREY, GRID, LIGHT = "#2b4c7e", "#2e7d5b", "#b3403a", "#c77d21", "#555555", "#e8e8e8", "#b9c4d4"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": GREY, "axes.labelcolor": GREY,
    "xtick.color": GREY, "ytick.color": GREY, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False, "legend.fontsize": 8,
    "svg.fonttype": "none",
})


def rsi_wilder(close, n=14):
    delta = close.diff(); g = delta.clip(lower=0); l = -delta.clip(upper=0)
    return 100 - 100 / (1 + g.ewm(alpha=1 / n, adjust=False).mean() / l.ewm(alpha=1 / n, adjust=False).mean())


def atr_wilder(df, n=14):
    prev = df.close.shift()
    tr = pd.concat([df.high - df.low, (df.high - prev).abs(), (df.low - prev).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def fmt_dates(ax):
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, format="svg", metadata={"Date": None})
    plt.close(fig)
    print("wrote", name)


# ------------------------------------------------------------ 1. Bollinger + ATR
mid = px.close.rolling(20).mean(); sd = px.close.rolling(20).std(ddof=0)
up, lo = mid + 2 * sd, mid - 2 * sd
bw = (up - lo) / mid * 100
atr = atr_wilder(px)
fig, (a1, a2, a3) = plt.subplots(3, 1, figsize=(8.5, 6.4), sharex=True, gridspec_kw={"height_ratios": [3, 1, 1]})
a1.fill_between(px.index, lo, up, color=LIGHT, alpha=0.35, linewidth=0)
a1.plot(px.index, up, color=GREY, lw=0.7); a1.plot(px.index, lo, color=GREY, lw=0.7)
a1.plot(px.index, mid, color=ORANGE, lw=1, label="20-day SMA")
a1.plot(px.index, px.close, color=NAVY, lw=1.1, label="Close")
for t, lab in [("2025-01-06", "squeeze → +8.6%"), ("2025-12-11", "squeeze → +2.2%")]:
    t = pd.Timestamp(t); a1.axvline(t, color=RED, lw=0.8, ls="--"); a2.axvline(t, color=RED, lw=0.8, ls="--")
    a1.annotate(lab, (t, px.close.loc[t]), xytext=(8, -28), textcoords="offset points", fontsize=8, color=RED)
a1.set_ylabel("₹"); a1.legend(loc="upper left"); a1.set_title("Britannia: 20-day Bollinger Bands (±2σ), bandwidth and ATR(14)", loc="left", fontsize=10, color="#222222")
a2.plot(px.index, bw, color=GREEN, lw=1); a2.set_ylabel("Bandwidth %")
a3.plot(px.index, atr, color=RED, lw=1); a3.set_ylabel("ATR ₹")
fmt_dates(a3); save(fig, "ta2-bollinger-atr.svg")

# ------------------------------------------------------------ 2. Relative strength
both = pd.concat([px.close.rename("stock"), nifty.rename("nifty")], axis=1).dropna()
rs = both.stock / both.nifty; rs = rs / rs.iloc[0] * 100
fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.5, 5.6), sharex=True, gridspec_kw={"height_ratios": [2, 2]})
a1.plot(both.index, both.stock / both.stock.iloc[0] * 100, color=NAVY, lw=1.1, label="Britannia (rebased 100)")
a1.plot(both.index, both.nifty / both.nifty.iloc[0] * 100, color=GREY, lw=1.1, label="Nifty 50 PRI (rebased 100)")
a1.legend(loc="upper left"); a1.set_title("Britannia vs Nifty 50, and the ratio between them", loc="left", fontsize=10, color="#222222")
a2.plot(rs.index, rs, color=GREEN, lw=1.2, label="Relative strength = Britannia ÷ Nifty, rebased 100")
a2.plot(rs.index, rs.rolling(50).mean(), color=ORANGE, lw=1, label="50-day MA of the ratio")
a2.axhline(100, color=GREY, lw=0.7, ls=":")
a2.annotate("low 89.3\n10 Dec 24", (rs.idxmin(), rs.min()), xytext=(6, -22), textcoords="offset points", fontsize=8, color=RED)
a2.annotate("high 115.6\n11 Sep 25", (rs.idxmax(), rs.max()), xytext=(6, 4), textcoords="offset points", fontsize=8, color=GREEN)
a2.legend(loc="lower right"); fmt_dates(a2); save(fig, "ta2-relative-strength.svg")

# ------------------------------------------------------------ 3. Multiple timeframes
wk = px.resample("W-FRI").agg({"open": "first", "high": "max", "low": "min", "close": "last"}).dropna()
wk_ma = wk.close.rolling(20).mean()
drsi = rsi_wilder(px.close)
fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.5, 5.8), sharex=True, gridspec_kw={"height_ratios": [3, 1.4]})
a1.plot(px.index, px.close, color=LIGHT, lw=0.8, label="Daily close")
a1.plot(wk.index, wk.close, color=NAVY, lw=1.3, label="Weekly close")
a1.plot(wk_ma.index, wk_ma, color=ORANGE, lw=1.2, label="20-week SMA (weekly trend)")
a1.legend(loc="upper left"); a1.set_ylabel("₹")
a1.set_title("Weekly trend on top, daily RSI(14) underneath", loc="left", fontsize=10, color="#222222")
a2.plot(px.index, drsi, color=GREEN, lw=0.9); a2.axhline(70, color=GREY, lw=0.7, ls=":"); a2.axhline(30, color=GREY, lw=0.7, ls=":")
a2.set_ylim(0, 100); a2.set_ylabel("Daily RSI")
for t, lab in [("2024-10-24", "oversold, weekly 'up'\n→ −12.6%"), ("2025-02-28", "oversold, weekly 'down'\n→ +6.6%")]:
    t = pd.Timestamp(t); a1.axvline(t, color=RED, lw=0.8, ls="--"); a2.axvline(t, color=RED, lw=0.8, ls="--")
    a2.annotate(lab, (t, 30), xytext=(6, 30), textcoords="offset points", fontsize=8, color=RED)
fmt_dates(a2); save(fig, "ta2-multi-timeframe.svg")

# ------------------------------------------------------------ 4. Backtest equity curves
START = 200; bt = px.iloc[START:]
def equity(signal, lag=1, cost=0.001):
    pos = signal.shift(lag).fillna(0).astype(int).loc[bt.index]
    ret = bt.close.pct_change().fillna(0)
    strat = pos.shift(1).fillna(0) * ret - pos.diff().abs().fillna(pos.iloc[0]) * cost
    return 100000 * (1 + strat).cumprod()
sma = lambda f, s: (px.close.rolling(f).mean() > px.close.rolling(s).mean()).astype(int)
sig = pd.Series(np.nan, index=px.index); sig[drsi < 30] = 1; sig[drsi > 70] = 0; rsi_sig = sig.ffill().fillna(0).astype(int)
fig, ax = plt.subplots(figsize=(8.5, 4.4))
ax.plot(bt.index, 100000 * bt.close / bt.close.iloc[0], color=NAVY, lw=1.4, label="Buy & hold")
ax.plot(bt.index, equity(sma(50, 200)), color=ORANGE, lw=1.1, label="SMA 50/200 crossover")
ax.plot(bt.index, equity(sma(20, 50)), color=RED, lw=1.1, label="SMA 20/50 crossover")
ax.plot(bt.index, equity(rsi_sig), color=GREEN, lw=1.1, label="RSI: long below 30, flat above 70")
ax.axhline(100000, color=GREY, lw=0.7, ls=":")
ax.set_ylabel("₹ (start ₹1,00,000)"); ax.legend(loc="lower left")
ax.set_title("Same stock, same window, four rules — next-day execution, 0.1% per side", loc="left", fontsize=10, color="#222222")
fmt_dates(ax); save(fig, "ta2-backtest.svg")
