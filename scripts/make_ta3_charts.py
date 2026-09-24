#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Draw the charts for Technical Analysis Module 3 ("Honest tests") into
assets/charts/:

    ta3-gaps.svg             gap fill rates vs the matched base rate (Britannia)
    ta3-fibonacci.svg        where Nifty pullbacks actually ended, Fibonacci bands shaded
    ta3-month-of-year.svg    every monthly Nifty return by calendar month, with the average
    ta3-budget-days.svg      Nifty's move on each Budget day vs a typical day
    ta3-stochastic.svg       Britannia price, slow stochastic and RSI(14)
    ta3-obv-vwap.svg         Britannia price with anchored VWAP (approx.), and OBV
    ta3-stops.svg            how far each stop rule sat from the entry (Britannia)
    ta3-momentum.svg         Nifty 12-1 month momentum vs the next month's return

    python3 scripts/make_ta3_charts.py

Reads the same CSVs and _data/ta3.yml written by scripts/derive_ta3.py (run
that first), same palette as the ta/ta2 charts. matplotlib's font lacks the
rupee sign, so chart text says "Rs".
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import yaml  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/charts"
D = yaml.safe_load((ROOT / "_data/ta3.yml").read_text(encoding="utf-8"))
px = pd.read_csv(ROOT / "assets/data/britannia-ohlcv-2024-04-to-2026-03.csv", parse_dates=["date"]).set_index("date").sort_index()
nifty = pd.read_csv(ROOT / "assets/data/nifty50-price-index.csv", parse_dates=["date"]).set_index("date").sort_index()["nifty50_pri_close"]

NAVY, GREEN, RED, ORANGE, GREY, GRID, LIGHT = "#2b4c7e", "#2e7d5b", "#b3403a", "#c77d21", "#555555", "#e8e8e8", "#b9c4d4"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": GREY, "axes.labelcolor": GREY,
    "xtick.color": GREY, "ytick.color": GREY, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False, "legend.fontsize": 8,
    "svg.fonttype": "none", "svg.hashsalt": "ta3",
})


def title(ax, t):
    ax.set_title(t, loc="left", fontsize=10, color="#222222")


def fmt_dates(ax, interval=3):
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=interval))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, format="svg", metadata={"Date": None})
    plt.close(fig)
    print("wrote", name)


# ------------------------------------------------------------ 1. gaps
g = D["gaps"]
fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.6), sharey=True)
for ax, key, lab in [(axes[0], "up", "Gap ups"), (axes[1], "down", "Gap downs")]:
    w = g[key]["windows"]
    xs = np.arange(3)
    fills = [w[f"h{h}"]["fill_pct"] for h in (1, 5, 20)]
    base = [w[f"h{h}"]["base_pct"] for h in (1, 5, 20)]
    ax.bar(xs - 0.18, fills, 0.36, color=NAVY, label="Gap filled")
    ax.bar(xs + 0.18, base, 0.36, color=LIGHT, label="Base rate: any open revisited by the same distance")
    for x, f, b in zip(xs, fills, base):
        ax.text(x - 0.18, f + 1.5, f"{f:.0f}%", ha="center", fontsize=8, color=NAVY)
        ax.text(x + 0.18, b + 1.5, f"{b:.0f}%", ha="center", fontsize=8, color=GREY)
    ax.set_xticks(xs, ["same day", "within\n5 sessions", "within\n20 sessions"])
    ax.set_ylim(0, 110)
    title(ax, f"{lab} (n = {g[key]['count']})")
axes[0].set_ylabel("% of events")
axes[0].legend(loc="upper left", bbox_to_anchor=(0, -0.12), ncol=2)
save(fig, "ta3-gaps.svg")

# ------------------------------------------------------------ 2. Fibonacci
# rebuild the pullback depths exactly as derive_ta3.py does (same zigzag)
src = (ROOT / "scripts/derive_ta3.py").read_text(encoding="utf-8")
zz_src = src[src.index("def zigzag"):src.index("def hit_share")]
ns: dict = {"np": np, "pd": pd}
exec(zz_src, ns)
pv = ns["zigzag"](nifty, D["fibonacci"]["main_threshold_pct"] / 100)
P = nifty.to_numpy()[pv]
depth = np.array([(P[k + 1] - P[k + 2]) / (P[k + 1] - P[k]) * 100 for k in range(len(P) - 2)])
pull = depth[depth < 100]
assert len(pull) == D["fibonacci"]["main"]["pullbacks"]
fig, ax = plt.subplots(figsize=(8.5, 3.8))
for f in (38.2, 50.0, 61.8):
    ax.axvspan(f - 2, f + 2, color=ORANGE, alpha=0.25, lw=0)
    ax.text(f, 8.6, f"{f:g}%", ha="center", fontsize=8, color=ORANGE)
ax.hist(pull, bins=np.arange(0, 102, 2), color=NAVY, edgecolor="white", linewidth=0.5)
ax.set_xlim(0, 100); ax.set_ylim(0, 9.5)
ax.set_xlabel("How much of the previous swing the pullback gave back (%)")
ax.set_ylabel("Pullbacks")
title(ax, f"Nifty 50, 2007–2026: where {len(pull)} pullbacks ended (5% zigzag); shaded = Fibonacci ±2 points")
save(fig, "ta3-fibonacci.svg")

# ------------------------------------------------------------ 3. month of year
me = nifty.resample("ME").last(); me.index = me.index.to_period("M")
mret = me.pct_change().dropna(); mret = mret[mret.index >= pd.Period("2007-10", "M")] * 100
fig, ax = plt.subplots(figsize=(8.5, 4.2))
rng = np.random.default_rng(1)
for m in range(1, 13):
    x = mret[mret.index.month == m]
    ax.scatter(m + rng.uniform(-0.18, 0.18, len(x)), x, s=12, color=NAVY, alpha=0.6, lw=0)
    ax.plot([m - 0.3, m + 0.3], [x.mean()] * 2, color=RED, lw=2)
ax.axhline(0, color=GREY, lw=0.8)
ax.set_xticks(range(1, 13), [r["month"] for r in D["seasonality"]["by_month"]])
ax.set_ylabel("Monthly return, %")
title(ax, "Nifty 50 price index: every month from Oct 2007 to Mar 2026 (dots), and each month's average (red)")
save(fig, "ta3-month-of-year.svg")

# ------------------------------------------------------------ 4. Budget days
b = D["events"]["budget"]; allabs = D["events"]["all_days"]["avg_abs_pct"]
rows = b["rows"]
fig, ax = plt.subplots(figsize=(8.5, 3.8))
xs = np.arange(len(rows))
ax.bar(xs, [r["move_pct"] for r in rows], color=[GREEN if r["move_pct"] > 0 else RED for r in rows])
ax.axhspan(-allabs, allabs, color=LIGHT, alpha=0.4, lw=0)
ax.text(len(rows) - 0.5, allabs + 0.15, f"±{allabs}% = average size of any day's move", ha="right", fontsize=8, color=GREY)
ax.set_xticks(xs, [pd.Timestamp(r["date"]).strftime("%b %y") for r in rows], rotation=60, fontsize=7.5)
ax.set_ylabel("Nifty close-to-close, %")
ax.axhline(0, color=GREY, lw=0.8)
title(ax, f"Nifty 50 on the {len(rows)} Budget days with a row in the file")
save(fig, "ta3-budget-days.svg")

# ------------------------------------------------------------ 5. stochastic
def rsi_wilder(close, n=14):
    delta = close.diff()
    return 100 - 100 / (1 + delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean() / (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean())


ll, hh = px.low.rolling(14).min(), px.high.rolling(14).max()
sk = (100 * (px.close - ll) / (hh - ll)).rolling(3).mean()
rsi = rsi_wilder(px.close)
s = slice(px.index[100], None)
fig, (a1, a2, a3) = plt.subplots(3, 1, figsize=(8.5, 6.2), sharex=True, gridspec_kw={"height_ratios": [2.2, 1, 1]})
a1.plot(px.index[100:], px.close[s], color=NAVY, lw=1.1); a1.set_ylabel("Rs")
title(a1, "Britannia: slow stochastic (14,3,3) and RSI(14) — same story, stochastic at the extremes far more often")
a2.plot(px.index[100:], sk[s], color=ORANGE, lw=0.9); a2.axhline(80, color=GREY, ls=":", lw=0.8); a2.axhline(20, color=GREY, ls=":", lw=0.8)
a2.set_ylim(0, 100); a2.set_ylabel("Slow %K")
a3.plot(px.index[100:], rsi[s], color=GREEN, lw=0.9); a3.axhline(70, color=GREY, ls=":", lw=0.8); a3.axhline(30, color=GREY, ls=":", lw=0.8)
a3.set_ylim(0, 100); a3.set_ylabel("RSI(14)")
fmt_dates(a3); save(fig, "ta3-stochastic.svg")

# ------------------------------------------------------------ 6. OBV + anchored VWAP
obv = (np.sign(px.close.diff()).fillna(0) * px.volume).cumsum() / 1e5
av = D["obv"]["anchored_vwap"]; seg = px.loc[av["anchor"]:]
tp = (seg.high + seg.low + seg.close) / 3
avwap = (tp * seg.volume).cumsum() / seg.volume.cumsum()
big = pd.Timestamp(D["obv"]["biggest_volume_day"]["date"])
fig, (a1, a2) = plt.subplots(2, 1, figsize=(8.5, 5.4), sharex=True, gridspec_kw={"height_ratios": [2, 1.4]})
a1.plot(px.index, px.close, color=NAVY, lw=1.1, label="Close")
a1.plot(avwap.index, avwap, color=ORANGE, lw=1.2, label="Anchored VWAP from 1 Apr 2025 (approx., daily bars)")
a1.set_ylabel("Rs"); a1.legend(loc="upper left")
title(a1, "Britannia: price with an anchored VWAP, and on-balance volume")
a2.plot(obv.index, obv, color=GREEN, lw=1.1); a2.set_ylabel("OBV, lakh shares")
a2.axvline(big, color=RED, lw=0.8, ls="--")
a2.annotate(f"{pd.Timestamp(big).strftime('%-d %b %Y')}: {D['obv']['biggest_volume_day']['multiple_of_median']}x median volume,\nprice {str(D['obv']['biggest_volume_day']['close_change_pct']).replace('-', '−')}%",
            (big, obv.loc[big]), xytext=(30, -38), textcoords="offset points", fontsize=8, color=RED)
fmt_dates(a2); save(fig, "ta3-obv-vwap.svg")

# ------------------------------------------------------------ 7. stop distances
def atr_wilder(df, n=14):
    prev = df.close.shift()
    tr = pd.concat([df.high - df.low, (df.high - prev).abs(), (df.low - prev).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


atr = atr_wilder(px)
N = len(px); SH = 20
ent = range(SH, N - SH)
C, L = px.close.to_numpy(), px.low.to_numpy()
dist_atr = [2 * atr.iloc[i] / C[i] * 100 for i in ent]
dist_sw = [(1 - (L[i - SH + 1:i + 1].min() - 0.05) / C[i]) * 100 for i in ent]
assert len(dist_atr) == D["stops"]["entries"]
fig, ax = plt.subplots(figsize=(8.5, 3.6))
bins = np.arange(0, 18, 0.5)
ax.hist(dist_sw, bins=bins, color=LIGHT, edgecolor="white", label="Below the 20-session low")
ax.hist(dist_atr, bins=bins, color=ORANGE, alpha=0.8, edgecolor="white", label="2 × ATR(14)")
ax.axvline(5, color=NAVY, lw=1.6, label="Fixed 5%")
ax.set_xlabel("Distance from entry to stop, % of the entry price"); ax.set_ylabel("Entries")
ax.legend(loc="upper right")
title(ax, f"Britannia, {len(dist_atr)} entries: how far away each stop rule put the stop")
save(fig, "ta3-stops.svg")

# ------------------------------------------------------------ 8. momentum scatter
mom = me.shift(1) / me.shift(12) - 1; nxt = me.shift(-1) / me - 1
df = pd.DataFrame({"mom": mom, "next": nxt}).dropna() * 100
assert len(df) == D["momentum"]["months"]
fig, ax = plt.subplots(figsize=(8.5, 4.2))
ax.scatter(df.mom, df.next, s=14, color=NAVY, alpha=0.6, lw=0)
ax.axhline(0, color=GREY, lw=0.8); ax.axvline(0, color=GREY, lw=0.8)
for per, lab in [("2009-04", "Apr 09 → May 09"), ("2020-02", "Feb 20 → Mar 20"), ("2008-09", "Sep 08 → Oct 08")]:
    p_ = pd.Period(per, "M")
    ax.annotate(lab, (df.loc[p_, "mom"], df.loc[p_, "next"]), xytext=(6, 0), textcoords="offset points", fontsize=8, color=RED)
ax.set_xlabel("12-1 month momentum at month-end, %"); ax.set_ylabel("Next month's return, %")
title(ax, f"Nifty 50, {D['momentum']['months']} month-ends: past-year trend vs the month that followed (correlation {D['momentum']['corr_mom_next']})")
save(fig, "ta3-momentum.svg")
