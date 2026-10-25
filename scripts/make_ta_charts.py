#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Draw the ten charts for Technical Analysis Module 1 into assets/charts/:

    ta-overview.svg            daily close, Apr 2024 - Mar 2026, peak and trough closes marked
    ta-candle-anatomy.svg      schematic bullish / bearish candle (not real data)
    ta-candles-real.svg        daily candles, mid-Dec 2025 to mid-Feb 2026
    ta-support-resistance.svg  close with the support and resistance zones and their tests
    ta-trendlines.svg          two-point down- and uptrend lines, extended until a close breaks them
    ta-moving-averages.svg     close with 50- and 200-day SMAs and the one crossover
    ta-volume.svg              close over daily volume and its 50-day average
    ta-rsi.svg                 close over Wilder-seeded RSI(14), three 63-session outcomes
    ta-macd.svg                close over MACD(12,26,9) from Jan 2025, every crossover marked
    ta-double-top.svg          the six swing highs in one band (the "double top" that isn't)

    python3 scripts/make_ta_charts.py

Inputs: assets/data/britannia-ohlcv-2024-04-to-2026-03.csv (Yahoo Finance,
BRITANNIA.NS) and _data/ta.yml. Every label is read from ta.yml or computed
from the CSV, and the script first ASSERTS that ta.yml's figures still follow
from the CSV (RSI episodes, MACD crossover counts, the golden cross, zone
tests, the double-top highs) and that the trend-line figures typed in the
trend-lines post (5 Oct 2026) reproduce. If an assertion fails, fix the data
or the post, not the chart. Same palette and indicator conventions as
make_ta2_charts.py and derive_ta2.py.
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
px = pd.read_csv(ROOT / "assets/data/britannia-ohlcv-2024-04-to-2026-03.csv", parse_dates=["date"]).set_index("date").sort_index()
ta = yaml.safe_load((ROOT / "_data/ta.yml").read_text(encoding="utf-8"))

NAVY, GREEN, RED, ORANGE, GREY, GRID, LIGHT, INK = "#2b4c7e", "#2e7d5b", "#b3403a", "#c77d21", "#555555", "#e8e8e8", "#b9c4d4", "#222222"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": GREY, "axes.labelcolor": GREY,
    "xtick.color": GREY, "ytick.color": GREY, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False, "legend.fontsize": 8,
    "svg.fonttype": "none", "svg.hashsalt": "wealthprimer-ta1", "axes.axisbelow": True,
})
SOURCE = "Britannia Industries (NSE: BRITANNIA), daily. Source: Yahoo Finance. Historical data, for illustration only."
W = 8.25  # inches; every chart is this wide so the posts' width attributes stay close to 594


def T(s):
    return pd.Timestamp(s)


def inr(x):
    """Indian grouping, no decimals: 6446.05 -> '6,446'."""
    s = f"{int(round(x))}"
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:]); head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts + [tail])


def day(d):
    return f"{T(d).day} {T(d):%b %Y}"


def rsi_wilder_seeded(close, n=14):
    """Wilder's RSI: first average = simple mean of the first n gains/losses (value at bar n), then Wilder smoothing."""
    delta = close.diff()
    gain, loss = delta.clip(lower=0).to_numpy(), (-delta.clip(upper=0)).to_numpy()
    out = np.full(len(close), np.nan)
    ag, al = gain[1:n + 1].mean(), loss[1:n + 1].mean()
    out[n] = 100 - 100 / (1 + ag / al) if al else 100.0
    for i in range(n + 1, len(close)):
        ag = (ag * (n - 1) + gain[i]) / n
        al = (al * (n - 1) + loss[i]) / n
        out[i] = 100 - 100 / (1 + ag / al) if al else 100.0
    return pd.Series(out, index=close.index)


def save(fig, name):
    fig.text(0.012, 0.012, SOURCE if name != "ta-candle-anatomy.svg" else "Schematic illustration — not real price data.",
             fontsize=7.5, color="#777777")
    fig.savefig(OUT / name, format="svg", metadata={"Date": None})
    plt.close(fig)
    print("wrote", name)


def title(ax, text):
    ax.set_title(text, loc="left", fontsize=10.5, color=INK)


def quarter_ticks(ax):
    ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 4, 7, 10)))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))


close = px.close
H = 63  # fixed forward horizon, sessions (ta.yml rsi.horizon_sessions)

# ============================================================== invariants
assert len(px) == ta["dataset"]["bars"]
assert str(px.index[0].date()) == ta["dataset"]["start"] and str(px.index[-1].date()) == ta["dataset"]["end"]
md = ta["major_decline"]
assert abs(close[md["peak_close_date"]] - md["peak_close"]) < 0.01 and close[:"2024-12-31"].idxmax() == T(md["peak_close_date"])
assert abs(close[md["trough_close_date"]] - md["trough_close"]) < 0.01 and close.idxmin() == T(md["trough_close_date"])
assert abs(px.high[md["peak_date"]] - md["peak_high"]) < 0.01 and abs(px.low[md["trough_date"]] - md["trough_low"]) < 0.01

rsi = rsi_wilder_seeded(close)
r = ta["rsi"]
assert r["horizon_sessions"] == H
assert int((rsi > 70).sum()) == r["days_above_70"] and int((rsi < 30).sum()) == r["days_below_30"]
for k in ("overbought_but_kept_rising", "overbought_then_fell", "oversold_but_kept_falling"):
    e = r[k]; i = px.index.get_loc(T(e["date"]))
    assert abs(rsi.iloc[i] - e["rsi"]) < 0.05, (k, rsi.iloc[i])
    assert str(px.index[i + H].date()) == e["later_date"], (k, px.index[i + H])
    assert abs((close.iloc[i + H] / close.iloc[i] - 1) * 100 - e["change_pct"]) < 0.05, k

ema = lambda s, n: s.ewm(span=n, adjust=False).mean()  # noqa: E731
m = ta["macd"]
macd = ema(close, m["fast"]) - ema(close, m["slow"]); sig = ema(macd, m["signal"]); hist = macd - sig
WARM = len(px) - m["bars_measured"]
above = (macd > sig).iloc[WARM:]
cross = above.ne(above.shift()).iloc[1:]
cross_dates = cross[cross].index
bull = [d for d in cross_dates if above[d]]; bear = [d for d in cross_dates if not above[d]]
assert (len(bull), len(bear)) == (m["bullish_crossovers"], m["bearish_crossovers"]), (len(bull), len(bear))
assert len([d for d in cross_dates if d >= T(m["chart_window_start"])]) == m["chart_window_crossovers"]

sma50, sma200 = close.rolling(50).mean(), close.rolling(200).mean()
sc = ta["sma_crossover"]
diff = (sma50 - sma200).dropna()
gx = diff.index[(diff > 0) & (diff.shift() <= 0)]
dx = diff.index[(diff < 0) & (diff.shift() >= 0)]
assert len(gx) == sc["golden_cross_count"] and len(dx) == sc["death_cross_count"] and str(gx[0].date()) == sc["golden_cross"]["date"]
assert str(diff.index[0].date()) == sc["sma200_first_date"]

for zone, col in (("resistance_zone", "high"), ("support_zone", "low")):
    for t in ta[zone]["tests"]:
        assert abs(px[col][t["date"]] - t[col]) <= 0.051, (zone, t)  # ta.yml rounds to 1 dp
dt = ta["apparent_double_top"]
for h in dt["all_swing_highs_in_band"]:
    assert abs(px.high[h["date"]] - h["high"]) <= 0.051, h
assert min(h["high"] for h in dt["all_swing_highs_in_band"]) == dt["band_low"]
assert max(h["high"] for h in dt["all_swing_highs_in_band"]) == dt["band_high"]

vol_avg = px.volume.rolling(50).mean()
for s in ta["volume_spikes"]:
    assert abs(px.volume[s["date"]] / vol_avg[s["date"]] - s["x_avg"]) < 0.05, s


# Trend lines: two anchors, extended in calendar days, broken by the first close beyond the line.
def trend(a_date, a_val, b_date, b_val, up):
    slope = (b_val - a_val) / (T(b_date) - T(a_date)).days
    line = a_val + slope * (px.index - T(a_date)).days
    s = pd.Series(line, index=px.index)
    after = px.index > T(b_date)
    broke = (close < s) if up else (close > s)
    brk = px.index[after & broke.to_numpy()][0]
    return slope, s, brk


# Anchors at one decimal, as the post displays them, so a reader extending the
# line from the printed figures gets the printed line value (₹4,883.0).
down_b = ("2024-11-11", round(float(px.high["2024-11-11"]), 1))
up_b = ("2025-04-07", round(float(px.low["2025-04-07"]), 1))
d_slope, d_line, d_brk = trend(md["peak_date"], md["peak_high"], *down_b, up=False)
u_slope, u_line, u_brk = trend(md["trough_date"], md["trough_low"], *up_b, up=True)
# Figures typed in _posts/2026-10-05-trend-lines.markdown:
assert round(down_b[1], 1) == 5902.1 and round(-d_slope, 1) == 14.6
assert str(d_brk.date()) == "2025-01-20" and round(close[d_brk], 1) == 4885.4 and round(d_line[d_brk], 1) == 4883.0
assert round(up_b[1], 1) == 4605.1 and round(u_slope, 1) == 2.9
assert str(u_brk.date()) == "2026-03-23" and (u_brk - T(md["trough_date"])).days == 384 and (u_brk - T(up_b[0])).days == 350

# ============================================================== 1. overview
fig, ax = plt.subplots(figsize=(W, 4.2))
ax.plot(close.index, close, color=NAVY, lw=1.2)
pk, tr = T(md["peak_close_date"]), T(md["trough_close_date"])
ax.plot([pk], [md["peak_close"]], "o", color=RED, ms=4); ax.plot([tr], [md["trough_close"]], "o", color=GREEN, ms=4)
ax.annotate(f"peak close ₹{inr(md['peak_close'])}\n{day(pk)}", (pk, md["peak_close"]), xytext=(14, -8), textcoords="offset points",
            fontsize=8.5, color=RED, va="top")
ax.annotate(f"trough close ₹{inr(md['trough_close'])}\n{day(tr)}", (tr, md["trough_close"]), xytext=(14, 4), textcoords="offset points",
            fontsize=8.5, color=GREEN, va="bottom")
ax.set_ylabel("₹ per share"); quarter_ticks(ax)
title(ax, "Britannia daily close, April 2024 – March 2026")
fig.subplots_adjust(left=0.1, right=0.98, top=0.92, bottom=0.14); save(fig, "ta-overview.svg")

# ============================================================== 2. candle anatomy (schematic)
fig, ax = plt.subplots(figsize=(5.57, 3.71))
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
for x, col, o, c, lab in ((4, GREEN, 4.2, 7.0, "Bullish\n(close > open)"), (7.2, RED, 7.0, 4.2, "Bearish\n(close < open)")):
    ax.plot([x, x], [3.2, 8.0], color=col, lw=2.2, solid_capstyle="butt")
    ax.add_patch(plt.Rectangle((x - 0.5, min(o, c)), 1.0, abs(c - o), color=col))
    for y, txt, side in ((8.0, "high", 1), (3.2, "low", 1), (c, "close", -1 if x < 5 else -1), (o, "open", -1)):
        if side > 0:
            ax.plot([x + 0.05, x + 1.0], [y, y], color="#999999", lw=0.8); ax.text(x + 1.1, y, txt, va="center", fontsize=8.5, color="#888888")
        else:
            ax.plot([x - 1.6, x - 0.55], [y, y], color="#999999", lw=0.8); ax.text(x - 1.7, y, txt, va="center", ha="right", fontsize=8.5, color="#888888")
    ax.text(x, 2.6, lab, ha="center", va="top", fontsize=9.5, color=col)
ax.set_title("Anatomy of a candlestick", loc="left", fontsize=10.5, color=INK)
fig.subplots_adjust(left=0.02, right=0.98, top=0.92, bottom=0.08); save(fig, "ta-candle-anatomy.svg")

# ============================================================== 3. real candles
win = px["2025-12-15":"2026-02-19"]
fig, ax = plt.subplots(figsize=(W, 4.08))
for d, row in win.iterrows():
    col = GREEN if row.close >= row.open else RED
    ax.vlines(d, row.low, row.high, color=col, lw=0.9)
    body = max(abs(row.close - row.open), 0.6)
    ax.add_patch(plt.Rectangle((mdates.date2num(d) - 0.32, min(row.open, row.close)), 0.64, body, color=col))
ax.set_xlim(mdates.date2num(win.index[0]) - 1.5, mdates.date2num(win.index[-1]) + 1.5)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.TU, interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%-d %b"))
ax.set_ylabel("₹ per share")
title(ax, "Reading real candles: Britannia, mid-Dec 2025 to mid-Feb 2026")
fig.subplots_adjust(left=0.1, right=0.98, top=0.92, bottom=0.14); save(fig, "ta-candles-real.svg")

# ============================================================== 4. support and resistance
rz, sz = ta["resistance_zone"], ta["support_zone"]
fig, ax = plt.subplots(figsize=(W, 4.44))
ax.axhspan(rz["low"], rz["high"], color=RED, alpha=0.1, lw=0); ax.axhspan(sz["low"], sz["high"], color=GREEN, alpha=0.1, lw=0)
ax.plot(close.index, close, color=NAVY, lw=1.1)
for t in rz["tests"]:
    ax.plot([T(t["date"])], [t["high"] + 40], "v", color=RED, ms=7)
for t in sz["tests"]:
    ax.plot([T(t["date"])], [t["low"] - 40], "^", color=GREEN, ms=7)
ax.text(T("2024-11-10"), rz["high"] + 25, f"resistance zone ₹{inr(rz['low'])}–{inr(rz['high'])}  ({len(rz['tests'])} failed attempts)", color=RED, fontsize=8.5, va="bottom")
ax.text(close.index[2], sz["low"] - 25, f"support zone ₹{inr(sz['low'])}–{inr(sz['high'])}  ({len(sz['tests'])} tests held)", color=GREEN, fontsize=8.5, va="top")
ax.set_ylim(sz["low"] - 250, rz["high"] + 250); ax.set_ylabel("₹ per share"); quarter_ticks(ax)
title(ax, "Support and resistance are zones, not lines")
fig.subplots_adjust(left=0.1, right=0.98, top=0.92, bottom=0.13); save(fig, "ta-support-resistance.svg")

# ============================================================== 5. trend lines
view = px.index >= T("2024-09-01")
fig, ax = plt.subplots(figsize=(W, 4.44))
ax.plot(close.index[view], close[view], color=NAVY, lw=1.1)
dl = d_line[(d_line.index >= T(md["peak_date"])) & (d_line.index <= d_brk + pd.Timedelta(days=35))]
ul = u_line[u_line.index >= T(md["trough_date"])]
ax.plot(dl.index, dl, color=RED, lw=1.3, ls="--"); ax.plot(ul.index, ul, color=GREEN, lw=1.3, ls="--")
ax.plot([T(md["peak_date"]), T(down_b[0])], [md["peak_high"], down_b[1]], "o", color=RED, ms=5)
ax.plot([T(md["trough_date"]), T(up_b[0])], [md["trough_low"], up_b[1]], "o", color=GREEN, ms=5)
ax.plot([d_brk, u_brk], [close[d_brk], close[u_brk]], "X", color="black", ms=9)
ax.annotate("downtrend line:\ntwo lower highs, extended", (T(down_b[0]), down_b[1]), xytext=(25, 40), textcoords="offset points",
            fontsize=8.5, color=RED, arrowprops={"arrowstyle": "->", "color": RED, "lw": 0.8})
ax.annotate(f"broken {day(d_brk)}\n(close {inr(close[d_brk])} vs line {inr(d_line[d_brk])})", (d_brk, close[d_brk]),
            xytext=(-55, -52), textcoords="offset points", fontsize=8.5, arrowprops={"arrowstyle": "->", "lw": 0.8})
mid_u = T("2025-09-01")
ax.annotate(f"uptrend line: two higher lows,\nheld for {(u_brk - T(md['trough_date'])).days} days", (mid_u, u_line[u_line.index >= mid_u].iloc[0]),
            xytext=(T("2025-05-20"), 4440), textcoords="data", fontsize=8.5, color=GREEN, arrowprops={"arrowstyle": "->", "color": GREEN, "lw": 0.8})
ax.annotate(f"broken\n{day(u_brk)}", (u_brk, close[u_brk]), xytext=(-95, -40), textcoords="offset points", fontsize=8.5,
            arrowprops={"arrowstyle": "->", "lw": 0.8})
ax.set_ylim(4350, 6650); ax.set_ylabel("₹ per share")
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 3, 5, 7, 9, 11))); ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
title(ax, "A trend line is a straight line through two swing points — extended until it breaks")
fig.subplots_adjust(left=0.1, right=0.98, top=0.92, bottom=0.13); save(fig, "ta-trendlines.svg")

# ============================================================== 6. moving averages
g = sc["golden_cross"]
fig, ax = plt.subplots(figsize=(W, 4.26))
ax.plot(close.index, close, color=LIGHT, lw=1, label="Close")
ax.plot(sma50.index, sma50, color=ORANGE, lw=1.5, label="50-day SMA")
ax.plot(sma200.index, sma200, color=NAVY, lw=1.5, label="200-day SMA")
ax.plot([T(g["date"])], [g["sma50"]], "o", mfc="none", mec=GREEN, mew=1.8, ms=9)
ax.annotate(f"the only 50/200 crossover\nin two years — {day(g['date'])}", (T(g["date"]), g["sma50"]), xytext=(-170, 95),
            textcoords="offset points", fontsize=8.5, color=GREEN, arrowprops={"arrowstyle": "->", "color": GREEN, "lw": 0.8})
ax.legend(loc="lower right"); ax.set_ylabel("₹ per share"); quarter_ticks(ax)
title(ax, "50-day and 200-day moving averages")
fig.subplots_adjust(left=0.1, right=0.98, top=0.92, bottom=0.13); save(fig, "ta-moving-averages.svg")

# ============================================================== 7. volume
up_day = close >= close.shift()
fig, (a1, a2) = plt.subplots(2, 1, figsize=(W, 4.99), sharex=True, gridspec_kw={"height_ratios": [2.3, 1]})
a1.plot(close.index, close, color=NAVY, lw=1.1); a1.set_ylabel("₹ per share")
a2.bar(px.index, px.volume / 1e6, width=1.0, color=np.where(up_day, GREEN, RED), linewidth=0)
a2.plot(vol_avg.index, vol_avg / 1e6, color=INK, lw=1, label="50-day average volume")
big = max(ta["volume_spikes"], key=lambda s: s["x_avg"])
a2.annotate(f"{day(big['date'])}: {big['x_avg']}× average,\nclose {big['change_pct']:+.1f}%".replace("-", "−"), (T(big["date"]), big["volume"] / 1e6),
            xytext=(10, -6), textcoords="offset points", fontsize=8, color=GREY, va="top")
a2.legend(loc="upper left"); a2.set_ylabel("shares (million)"); quarter_ticks(a2)
title(a1, "Price with volume underneath")
fig.subplots_adjust(left=0.1, right=0.98, top=0.93, bottom=0.11, hspace=0.08); save(fig, "ta-volume.svg")

# ============================================================== 8. RSI
fig, (a1, a2) = plt.subplots(2, 1, figsize=(W, 5.18), sharex=True, gridspec_kw={"height_ratios": [2.2, 1]})
a1.plot(close.index, close, color=NAVY, lw=1.1); a1.set_ylabel("₹ per share")
text_at = {"overbought_but_kept_rising": (T("2024-04-05"), 6560), "overbought_then_fell": (T("2024-11-25"), 6560),
           "oversold_but_kept_falling": (T("2025-02-20"), 4560)}
for k, col in (("overbought_but_kept_rising", RED), ("overbought_then_fell", RED), ("oversold_but_kept_falling", GREEN)):
    e = r[k]; d = T(e["date"])
    for a in (a1, a2):
        a.axvline(d, color=col, lw=0.8, ls=":")
    lab = (f"RSI {e['rsi']:.1f}{' (oversold)' if e['rsi'] < 30 else ''}, {day(d)}:\n"
           f"{e['change_pct']:+.1f}% after {H} sessions").replace("-", "−")
    a1.annotate(lab, (d, close[d]), xytext=text_at[k], textcoords="data", fontsize=8, color=col, va="top",
                arrowprops={"arrowstyle": "->", "color": col, "lw": 0.8})
a1.set_ylim(4350, 6650)
a2.plot(rsi.index, rsi, color=ORANGE, lw=1)
a2.axhline(70, color=RED, lw=0.9, ls="--"); a2.axhline(30, color=GREEN, lw=0.9, ls="--")
a2.fill_between(rsi.index, 70, rsi, where=rsi > 70, color=RED, alpha=0.15, lw=0)
a2.fill_between(rsi.index, 30, rsi, where=rsi < 30, color=GREEN, alpha=0.15, lw=0)
a2.set_ylim(10, 95); a2.set_ylabel("RSI (14)"); quarter_ticks(a2)
title(a1, "RSI: the same kind of signal, three different outcomes")
fig.subplots_adjust(left=0.1, right=0.98, top=0.93, bottom=0.11, hspace=0.08); save(fig, "ta-rsi.svg")

# ============================================================== 9. MACD
w0 = T(m["chart_window_start"])
cw = px.index >= w0
fig, (a1, a2) = plt.subplots(2, 1, figsize=(W, 5.18), sharex=True, gridspec_kw={"height_ratios": [1.6, 1]})
a1.plot(close.index[cw], close[cw], color=NAVY, lw=1.1); a1.set_ylabel("₹ per share")
a2.bar(px.index[cw], hist[cw], width=1.0, color=np.where(hist[cw] >= 0, GREEN, RED), alpha=0.4, linewidth=0)
a2.plot(px.index[cw], macd[cw], color=NAVY, lw=1.1, label=f"MACD ({m['fast']},{m['slow']})")
a2.plot(px.index[cw], sig[cw], color=ORANGE, lw=1.1, label=f"Signal ({m['signal']})")
for d in cross_dates:
    if d >= w0:
        a2.axvline(d, color=GREEN if above[d] else RED, lw=0.7, alpha=0.6)
a2.axhline(0, color=GREY, lw=0.6); a2.legend(loc="upper left"); a2.set_ylabel("₹")
a2.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 3, 5, 7, 9, 11))); a2.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
months = (px.index[-1].year - w0.year) * 12 + px.index[-1].month - w0.month + 1
title(a1, f"MACD over {months} months — {m['chart_window_crossovers']} crossovers, each one a vertical line")
fig.subplots_adjust(left=0.1, right=0.98, top=0.93, bottom=0.11, hspace=0.08); save(fig, "ta-macd.svg")

# ============================================================== 10. the double top that isn't
view = px["2025-08-20":]
highs = dt["all_swing_highs_in_band"]
picked = {dt["cherry_picked_peak1_date"]: '"peak 1"', dt["cherry_picked_peak2_date"]: '"peak 2"'}
fig, ax = plt.subplots(figsize=(W, 4.44))
ax.fill_between(view.index, view.low, view.high, color=LIGHT, alpha=0.5, lw=0, label="daily high–low range")
ax.plot(view.index, view.close, color=NAVY, lw=1.1, label="close")
ax.axhspan(dt["band_low"], dt["band_high"], color=RED, alpha=0.08, lw=0)
for h in highs:
    d = T(h["date"])
    if h["date"] in picked:
        ax.plot([d], [h["high"] + 45], "v", color=RED, ms=11)
        ax.text(d + pd.Timedelta(days=3), h["high"] + 45, picked[h["date"]], fontsize=8.5, color=RED, va="center")
    else:
        ax.plot([d], [h["high"] + 30], "v", mfc="none", mec=GREY, mew=1.3, ms=7)
first, last = T(highs[0]["date"]), T(highs[-1]["date"])
ax.text(T("2025-09-12"), dt["band_high"] + 70, f"six swing highs inside a {dt['band_width_pct']}% band (₹{inr(dt['band_low'])}–{inr(dt['band_high'])})",
        fontsize=8.5, color=RED)
ax.annotate("the highest of the six —\nand it came first", (first, highs[0]["high"]), xytext=(T("2025-09-12"), 5480), textcoords="data",
            fontsize=8.5, color=GREY, arrowprops={"arrowstyle": "->", "color": GREY, "lw": 0.8})
ax.annotate("and one more AFTER both picked\npeaks, before any breakdown", (last, highs[-1]["high"]), xytext=(T("2026-01-08"), 5560), textcoords="data",
            fontsize=8.5, color=GREY, arrowprops={"arrowstyle": "->", "color": GREY, "lw": 0.8})
ax.set_ylim(5330, 6480); ax.legend(loc="lower left"); ax.set_ylabel("₹ per share")
ax.xaxis.set_major_locator(mdates.MonthLocator()); ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
title(ax, "Pick two of these six highs and you have a textbook double top")
fig.subplots_adjust(left=0.1, right=0.98, top=0.92, bottom=0.13); save(fig, "ta-double-top.svg")
