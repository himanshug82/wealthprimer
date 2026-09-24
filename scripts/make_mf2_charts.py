#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Draw the charts for Mutual Funds, Minus the Marketing — Module 2 as SVG into
assets/charts/mf2-*.svg, from the same CSVs scripts/derive_mf2.py reads.

    python3 scripts/make_mf2_charts.py

The series adjustments (ETF 1:10 split, ETF dividend payout, the two debt
funds' face-value changes) are applied here EXACTLY as in derive_mf2.py — the
functions are imported from it — so a chart can never disagree with the
number rendered beside it. Re-run after any CSV correction, together with
derive_mf2.py. Matches the palette of the existing mf-*.svg charts.

Requires pandas, numpy, matplotlib.
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import derive_mf2 as d  # noqa: E402  (runs the derivation; cheap)

OUT = os.path.join(d.ROOT, "assets", "charts")
BLUE, RED, GREEN, GREY, INK, RULE = "#2b4c7e", "#b3403a", "#2e7d5b", "#777777", "#555555", "#e8e8e8"

plt.rcParams.update({
    "font.size": 9, "text.color": INK, "axes.labelcolor": INK, "axes.edgecolor": INK,
    "xtick.color": INK, "ytick.color": INK, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": RULE, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "legend.frameon": False, "svg.fonttype": "path",
})


def growth(s, start, end):
    s = s.loc[start:end].dropna()
    return s / s.iloc[0] * 100


def save(fig, name):
    fig.tight_layout()
    path = os.path.join(OUT, name)
    fig.savefig(path, format="svg", metadata={"Date": None})
    plt.close(fig)
    print("wrote", path)


# 1. Debt funds: growth of Rs 100 (three funds, 2018-) and the gilt fund's 1-year rolling return (2007-)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.26, 6.2), gridspec_kw={"height_ratios": [1.1, 1]})
for s, c, lab in [(d.overnight, GREY, "Overnight fund"), (d.mmf, BLUE, "Money market fund"), (d.gilt, RED, "Gilt fund")]:
    g = growth(s, d.DEBT_START, d.END)
    ax1.plot(g.index, g.values, color=c, lw=1.3, label=lab)
ax1.set_title("Growth of ₹100, 3 May 2018 to 31 Mar 2026 — three UTI debt funds, regular plans", loc="left", fontsize=9.5)
ax1.legend(loc="upper left")
ax1.set_ylabel("₹")
r1 = d.rolling_cagr(d.gilt, 1) * 100
ax2.fill_between(r1.index, 0, r1.values, where=r1.values < 0, color=RED, alpha=0.5, lw=0)
ax2.plot(r1.index, r1.values, color=RED, lw=1.0)
ax2.axhline(0, color=INK, lw=0.8)
ax2.set_title("Gilt fund: trailing 1-year return at every date, Apr 2007 to Mar 2026 (%)", loc="left", fontsize=9.5)
ax2.set_ylabel("%")
for dt, txt in [("2009-03-12", "Jan–Mar 2009\nreversal"), ("2013-08-19", "2013 taper\ntantrum")]:
    ax2.annotate(txt, xy=(pd.Timestamp(dt), float(r1.loc[:dt].iloc[-1])), xytext=(pd.Timestamp(dt) + pd.Timedelta(days=200), -9),
                 fontsize=8, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
save(fig, "mf2-debt-funds.svg")

# 2. ETF vs index fund vs price index
fig, ax = plt.subplots(figsize=(8.26, 3.9))
for s, c, lab, lw in [(d.nifty, GREY, "Nifty 50 price index (no dividends)", 1.0),
                      (d.idx_reg, RED, "Index fund, regular plan", 1.1),
                      (d.idx_dir, BLUE, "Index fund, direct plan", 1.1),
                      (d.etf, GREEN, "ETF (split- and payout-adjusted)", 1.3)]:
    g = growth(s, d.ETF_START, d.END)
    ax.plot(g.index, g.values, color=c, lw=lw, label=lab)
split = pd.Timestamp(d.etf_events[0]["date"])
pay = pd.Timestamp(d.etf_payouts[0]["ex_date"])
g_etf = growth(d.etf, d.ETF_START, d.END)
ax.annotate("25 Feb 2021: ETF pays out ₹40.89/unit;\nNAV drops, value doesn't", xy=(pay, float(g_etf.loc[:pay].iloc[-1])),
            xytext=(pd.Timestamp("2017-03-01"), 290), fontsize=8, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.annotate("26 Sep 2023: 1:10 unit split;\nNAV ÷ 10, value unchanged", xy=(split, float(g_etf.loc[:split].iloc[-1])),
            xytext=(pd.Timestamp("2021-06-01"), 90), fontsize=8, arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.set_title("Growth of ₹100, 2 Sep 2015 to 31 Mar 2026 — same fifty stocks, three wrappers", loc="left", fontsize=9.5)
ax.set_ylabel("₹")
ax.legend(loc="upper left")
save(fig, "mf2-etf-vs-index-fund.svg")

# 3. Trailing 3-year CAGR of the index fund through time
fig, ax = plt.subplots(figsize=(8.26, 3.9))
r3 = d.r3 * 100
ax.plot(r3.index, r3.values, color=BLUE, lw=1.1, label="Trailing 3-year CAGR, index fund regular plan")
ax.axhline(r3.median(), color=GREY, lw=0.9, ls="--", label=f"Median of all 3-year windows ({r3.median():.1f}%)")
ax.axhline(0, color=INK, lw=0.8)
snaps = pd.Series({pd.Timestamp(s["as_of"]): s["trailing_3y_cagr_pct"] for s in d.snapshots})
ax.scatter(snaps.index, snaps.values, color=RED, s=14, zorder=3, label="Reading on 31 March each year")
for dt, v in snaps.items():
    if dt.year in (2013, 2020, 2023):
        ax.annotate(f"{v:.1f}%", xy=(dt, v), xytext=(4, 6 if v > 10 else -12), textcoords="offset points", fontsize=8, color=RED)
ax.set_title("The same fund's 'three-year return' depended entirely on the day you looked", loc="left", fontsize=9.5)
ax.set_ylabel("% a year")
ax.legend(loc="upper left", fontsize=8)
save(fig, "mf2-trailing-3y.svg")

# 4. STP vs lump sum, Jan 2008 start, three years
fig, ax = plt.subplots(figsize=(8.26, 3.9))
start, end = "2008-01-01", "2011-01-01"
amt = d.STP_AMOUNT
nav0 = d.nav_on_or_after(d.idx_reg, start)[1]
ls_path = d.idx_reg.loc[start:end] / nav0 * amt
ov_path = d.overnight.loc[start:end] / d.nav_on_or_after(d.overnight, start)[1] * amt
# STP path: rebuild month by month
park_units = amt / d.nav_on_or_after(d.overnight, start)[1]
eq_units, per = 0.0, amt / 12
moves = list(d.month_starts(start, pd.Timestamp(start) + pd.DateOffset(months=12))[:12])
dates = d.idx_reg.loc[start:end].index
vals = []
mi = 0
for dt in dates:
    while mi < len(moves) and moves[mi] <= dt:
        p_nav = d.nav_on_or_after(d.overnight, moves[mi])[1]
        e_nav = d.nav_on_or_after(d.idx_reg, moves[mi])[1]
        mv = min(per / p_nav, park_units)
        park_units -= mv
        eq_units += mv * p_nav / e_nav
        mi += 1
    vals.append(eq_units * d.idx_reg[dt] + park_units * d.nav_on_or_before(d.overnight, dt))
stp_path = pd.Series(vals, index=dates)
ax.plot(ls_path.index, ls_path.values / 1e5, color=RED, lw=1.2, label="₹12 lakh lump sum into the index fund, 1 Jan 2008")
ax.plot(stp_path.index, stp_path.values / 1e5, color=BLUE, lw=1.2, label="Same ₹12 lakh parked in the parking fund, moved in over 12 months")
ax.plot(ov_path.index, ov_path.values / 1e5, color=GREY, lw=1.0, label="Left in the parking fund")
ax.axhline(amt / 1e5, color=INK, lw=0.8, ls=":")
ax.set_title("Same money, same start date, same funds — only the pace of entry differs", loc="left", fontsize=9.5)
ax.set_ylabel("₹ lakh")
ax.legend(loc="lower right", fontsize=8)
save(fig, "mf2-stp.svg")

# 5. SWP corpus paths
fig, ax = plt.subplots(figsize=(8.26, 3.9))
for start, c, lab in [("2008-01-01", RED, "₹1 crore in the index fund, ₹50,000/month from Jan 2008"),
                      ("2010-01-01", BLUE, "Same, starting Jan 2010"),
                      ("2020-04-01", GREEN, "Same, starting Apr 2020")]:
    _, _, _, path = d.swp(d.idx_reg, d.SWP_CORPUS, d.SWP_MONTHLY, start, d.END)
    p = pd.Series({dt: v for dt, v in path}) / 1e7
    ax.plot(p.index, p.values, color=c, lw=1.2, label=lab)
_, _, _, path = d.swp(d.overnight, d.SWP_CORPUS, d.SWP_MONTHLY, "2008-01-01", d.END)
p = pd.Series({dt: v for dt, v in path}) / 1e7
ax.plot(p.index, p.values, color=GREY, lw=1.0, label="₹1 crore in the parking fund, ₹50,000/month from Jan 2008")
ax.axhline(1.0, color=INK, lw=0.8, ls=":")
ax.set_title("Corpus remaining after each monthly withdrawal (₹ crore)", loc="left", fontsize=9.5)
ax.set_ylabel("₹ crore")
ax.legend(loc="upper left", fontsize=8)
save(fig, "mf2-swp.svg")
