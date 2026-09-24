#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by the "Risk, Leverage and Your Own Brain" series
(_data/risk.yml) and draw its charts (assets/charts/risk-*.svg) from the CSVs
already committed under assets/data/. Nothing in the risk posts is typed by
hand: if a number appears in a post, it was written into risk.yml by this
script.

    python3 scripts/derive_risk.py            # rewrites _data/risk.yml + charts

Inputs (all frozen at 31 March 2026 for the SEBI 3-month lag rule; see the
headers of _data/mf.yml and _data/ta.yml):
  assets/data/uti-nifty50-index-fund-nav.csv      UTI Nifty 50 Index Fund, regular growth (AMFI via mfapi.in)
  assets/data/britannia-ohlcv-2024-04-to-2026-03.csv  Britannia daily OHLCV (Yahoo Finance, BRITANNIA.NS)
  assets/data/nifty50-price-index.csv             Nifty 50 price index daily close (Yahoo Finance, ^NSEI)

Conventions shared with the MF series: SIP instalments on the 1st of the month
priced at the last available NAV on or before that date (pandas asof); a
scheduled instalment before the first NAV is skipped; ATR uses Wilder's
smoothing (alpha = 1/14) like the RSI in _data/ta.yml.

Needs pandas, numpy, pyyaml, matplotlib (not in the system python on this
machine — see TODO.md for the venv/docker note).
"""
import math
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "assets" / "data"
CHARTS = ROOT / "assets" / "charts"
OUT = ROOT / "_data" / "risk.yml"

BLUE, LIGHT, INK, GREY, RED = "#184f95", "#cde2fb", "#0b0b0b", "#52514e", "#b3261e"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "figure.dpi": 100})


def r2(x, n=2):
    return float(round(float(x), n))


# --------------------------------------------------------------------------
# Load
# --------------------------------------------------------------------------
nav = pd.read_csv(DATA / "uti-nifty50-index-fund-nav.csv", parse_dates=["date"]).set_index("date")
r = nav.nav_regular_growth.dropna()
br = pd.read_csv(DATA / "britannia-ohlcv-2024-04-to-2026-03.csv", parse_dates=["date"]).set_index("date")
nifty = pd.read_csv(DATA / "nifty50-price-index.csv", parse_dates=["date"]).set_index("date").nifty50_pri_close.dropna()

out = {"dataset": {
    "fund_name": "UTI Nifty 50 Index Fund",
    "fund_plan": "Regular Plan - Growth (AMFI scheme code 100822)",
    "fund_csv": "/assets/data/uti-nifty50-index-fund-nav.csv",
    "fund_source_url": "https://api.mfapi.in/mf/100822",
    "fund_source_label": "AMFI NAV history via mfapi.in",
    "fund_start": str(r.index.min().date()), "fund_end": str(r.index.max().date()),
    "britannia_csv": "/assets/data/britannia-ohlcv-2024-04-to-2026-03.csv",
    "britannia_source_url": "https://finance.yahoo.com/quote/BRITANNIA.NS/history/",
    "britannia_start": str(br.index.min().date()), "britannia_end": str(br.index.max().date()),
    "nifty_csv": "/assets/data/nifty50-price-index.csv",
    "nifty_source_url": "https://finance.yahoo.com/quote/%5ENSEI/history/",
    "as_of": "31 March 2026",
}}

# --------------------------------------------------------------------------
# RISK-2  The arithmetic of losses
# --------------------------------------------------------------------------
recovery = [{"loss_pct": L, "gain_needed_pct": r2(100 * (1 / (1 - L / 100) - 1), 1)} for L in (10, 20, 30, 40, 50, 60, 70, 80, 90)]

# Financial-year returns FY07..FY26 (1 Apr -> 31 Mar), the fund's full years.
fy_end = r.groupby(r.index.to_period("Q-MAR").asfreq("Y-MAR")).last()  # NAV at each FY end
fy_first = r.iloc[0]
fy_navs = pd.concat([pd.Series({pd.Period("2006", freq="Y-MAR"): fy_first}), fy_end])
fy_ret = (fy_navs.pct_change().dropna() * 100)
fy_ret.index = [f"FY{int(str(p)[-2:]):02d}" for p in fy_ret.index]  # 2007 -> FY07
years = len(fy_ret)
arith = fy_ret.mean()
geo = ((r.iloc[-1] / fy_first) ** (1 / years) - 1) * 100
sigma_annual = fy_ret.std(ddof=0)
drag_approx = (sigma_annual / 100) ** 2 / 2 * 100
out["arithmetic_of_losses"] = {
    "recovery_table": recovery,
    "fy_returns": [{"fy": k, "return_pct": r2(v, 1)} for k, v in fy_ret.items()],
    "years": years,
    "arithmetic_mean_pct": r2(arith), "geometric_mean_pct": r2(geo),
    "drag_pp": r2(arith - geo), "drag_approx_pp": r2(drag_approx),
    "fy_return_stdev_pct": r2(sigma_annual, 1),
    "best_fy": fy_ret.idxmax(), "best_fy_pct": r2(fy_ret.max(), 1),
    "worst_fy": fy_ret.idxmin(), "worst_fy_pct": r2(fy_ret.min(), 1),
    # 2008: the real recovery arithmetic behind the drawdown post's -59.7%
    "gfc_fall_pct": -59.7, "gfc_gain_needed_pct": r2(100 * (1 / (1 - 0.597) - 1), 1),
    "fy09_pct": r2(fy_ret["FY09"], 1), "fy10_pct": r2(fy_ret["FY10"], 1),
    "fy09_fy10_compound_pct": r2(((1 + fy_ret["FY09"] / 100) * (1 + fy_ret["FY10"] / 100) - 1) * 100, 1),
    "start_nav": r2(fy_first, 4), "end_nav": r2(r.iloc[-1], 4),
}
# Lump sum vs "average return" illusion: Rs 1 lakh at the arithmetic mean vs actual
out["arithmetic_of_losses"]["lakh_at_arithmetic_mean"] = int(round(100000 * (1 + arith / 100) ** years))
out["arithmetic_of_losses"]["lakh_actual"] = int(round(100000 * r.iloc[-1] / fy_first))

fig, ax = plt.subplots(figsize=(6.2, 3.3))
L = np.linspace(0, 90, 181)
ax.plot(L, 100 * (1 / (1 - L / 100) - 1), color=BLUE, lw=2)
ax.plot(L, L, color=GREY, lw=1, ls="--")
ax.annotate("gain needed to get back to even", (60, 150), color=BLUE, fontsize=8.5)
ax.annotate("if losses and gains were symmetric", (52, 38), color=GREY, fontsize=8.5)
for l, g in ((20, 25), (50, 100), (60, 150)):
    ax.plot([l], [g], "o", color=INK, ms=4); ax.annotate(f"−{l}% → +{g}%", (l + 1.5, g + 12), fontsize=8.5, color=INK)
ax.set_xlabel("Loss from peak (%)"); ax.set_ylabel("Gain needed to break even (%)")
ax.set_xlim(0, 90); ax.set_ylim(0, 900); ax.set_title("Losses and gains are not symmetric", loc="left", fontsize=10, color=INK)
fig.tight_layout(); fig.savefig(CHARTS / "risk-recovery.svg"); plt.close(fig)

# --------------------------------------------------------------------------
# RISK-3  Position sizing with ATR
# --------------------------------------------------------------------------
prev_close = br.close.shift(1)
tr = pd.concat([br.high - br.low, (br.high - prev_close).abs(), (br.low - prev_close).abs()], axis=1).max(axis=1)
atr = tr.ewm(alpha=1 / 14, adjust=False).mean()
atr_pct = atr / br.close * 100
valid = atr.iloc[14:]
capital, risk_pct, atr_mult = 1_000_000, 1.0, 2.0


def size_on(date):
    d = pd.Timestamp(date)
    c, a = float(br.close.asof(d)), float(atr.asof(d))
    stop_dist = atr_mult * a
    risk_rupees = capital * risk_pct / 100
    shares = int(risk_rupees // stop_dist)
    return {"date": str(br.index.asof(d).date()), "close": r2(c, 1), "atr": r2(a, 1), "atr_pct": r2(a / c * 100, 2),
            "stop_distance": r2(stop_dist, 1), "stop_price": r2(c - stop_dist, 1), "risk_rupees": int(risk_rupees),
            "shares": shares, "position_value": int(round(shares * c)), "position_pct_of_capital": r2(shares * c / capital * 100, 1)}


calm_date = atr_pct.iloc[14:].idxmin()
wild_date = atr_pct.iloc[14:].idxmax()
out["position_sizing"] = {
    "capital": capital, "risk_pct": risk_pct, "atr_period": 14, "atr_multiple": atr_mult,
    "atr_min": r2(valid.min(), 1), "atr_median": r2(valid.median(), 1), "atr_max": r2(valid.max(), 1),
    "atr_pct_min": r2(atr_pct.iloc[14:].min(), 2), "atr_pct_median": r2(atr_pct.iloc[14:].median(), 2), "atr_pct_max": r2(atr_pct.iloc[14:].max(), 2),
    "example_calm": size_on(calm_date), "example_wild": size_on(wild_date), "example_mid": size_on("2025-06-30"),
    # what a fixed "always buy 50 shares" rule risks instead
    "fixed_shares": 50,
}
for k in ("example_calm", "example_wild", "example_mid"):
    e = out["position_sizing"][k]
    e["fixed_50_risk_rupees"] = int(round(50 * e["stop_distance"]))
    e["fixed_50_risk_pct"] = r2(50 * e["stop_distance"] / capital * 100, 2)

fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 4.2), sharex=True, gridspec_kw={"height_ratios": [2, 1]})
a1.plot(br.index, br.close, color=BLUE, lw=1.2); a1.set_ylabel("Close (₹)")
a1.set_title("Britannia: price and 14-day ATR as % of price", loc="left", fontsize=10, color=INK)
a2.plot(atr_pct.index[14:], atr_pct.iloc[14:], color=GREY, lw=1.2); a2.set_ylabel("ATR (% of close)")
for d, c in ((calm_date, BLUE), (wild_date, RED)):
    a2.axvline(d, color=c, lw=0.8, ls=":")
a2.annotate("calmest", (calm_date, float(atr_pct[calm_date])), fontsize=8, color=BLUE, xytext=(4, 8), textcoords="offset points")
a2.annotate("wildest", (wild_date, float(atr_pct[wild_date])), fontsize=8, color=RED, xytext=(4, -12), textcoords="offset points")
fig.tight_layout(); fig.savefig(CHARTS / "risk-atr.svg"); plt.close(fig)

# --------------------------------------------------------------------------
# RISK-4  Leverage: pure arithmetic, but derived here so the tables reconcile
# --------------------------------------------------------------------------
lev_rows = []
for move in (-2, -5, -10, -15, -20, -25):
    lev_rows.append({"move_pct": move, **{f"x{L}": max(move * L, -100) for L in (1, 2, 5, 10)}})
mtf = {"own": 100000, "borrowed": 100000, "rate_pct": 12.0, "months": 6}
mtf["interest"] = int(round(mtf["borrowed"] * mtf["rate_pct"] / 100 * mtf["months"] / 12))
mtf["position"] = mtf["own"] + mtf["borrowed"]
mtf["breakeven_move_pct"] = r2(mtf["interest"] / mtf["position"] * 100)
mtf["scenarios"] = []
for move in (10, 5, 0, -5, -10, -20):
    pnl = mtf["position"] * move / 100 - mtf["interest"]
    mtf["scenarios"].append({"move_pct": move, "pnl": int(round(pnl)), "return_on_own_pct": r2(pnl / mtf["own"] * 100, 1),
                             "unlevered_return_pct": r2(move - 0.0, 1)})
mtf["wipeout_move_pct"] = r2(-(mtf["own"] - mtf["interest"]) / mtf["position"] * 100, 1)
out["leverage"] = {"table": lev_rows, "mtf": mtf,
                   "futures_margin_pct": 12, "futures_wipeout_move_pct": 12}

# --------------------------------------------------------------------------
# RISK-5  Correlation
# --------------------------------------------------------------------------
common = pd.concat([br.close.rename("brit"), nifty.rename("nifty")], axis=1).dropna()
rets = common.pct_change().dropna()
rho = rets.brit.corr(rets.nifty)
beta = rets.brit.cov(rets.nifty) / rets.nifty.var()
roll = rets.brit.rolling(60).corr(rets.nifty).dropna()
# index fund vs its index: how close to 1 a "different large-cap fund" really is
fund_vs_idx = pd.concat([r.rename("fund"), nifty.rename("nifty")], axis=1).dropna().pct_change().dropna()
rho_fund_idx = fund_vs_idx.fund.corr(fund_vs_idx.nifty)
sig_b, sig_n = rets.brit.std() * math.sqrt(252) * 100, rets.nifty.std() * math.sqrt(252) * 100
sig_5050 = math.sqrt(0.25 * sig_b**2 + 0.25 * sig_n**2 + 2 * 0.25 * rho * sig_b * sig_n)
two_asset = [{"rho": p, "portfolio_vol_pct": r2(math.sqrt(0.25 * 20**2 + 0.25 * 20**2 + 2 * 0.25 * p * 20 * 20), 1)} for p in (1.0, 0.9, 0.7, 0.5, 0.2, 0.0, -0.5)]
n_assets = [{"n": n, "portfolio_vol_pct": r2(20 * math.sqrt(1 / n + (1 - 1 / n) * 0.7), 1)} for n in (1, 2, 5, 10, 20, 50, 1000)]
out["correlation"] = {
    "window_start": str(rets.index.min().date()), "window_end": str(rets.index.max().date()), "days": int(len(rets)),
    "britannia_nifty_rho": r2(rho, 2), "britannia_beta": r2(beta, 2),
    "rolling_60d_min": r2(roll.min(), 2), "rolling_60d_max": r2(roll.max(), 2),
    "rolling_60d_min_date": str(roll.idxmin().date()), "rolling_60d_max_date": str(roll.idxmax().date()),
    "britannia_vol_pct": r2(sig_b, 1), "nifty_vol_pct": r2(sig_n, 1), "portfolio_5050_vol_pct": r2(sig_5050, 1),
    "naive_average_vol_pct": r2((sig_b + sig_n) / 2, 1),
    "index_fund_nifty_rho": r2(rho_fund_idx, 4),
    "index_fund_nifty_window_start": str(fund_vs_idx.index.min().date()),
    "two_asset_table": two_asset, "n_asset_table": n_assets, "n_asset_rho": 0.7, "n_asset_sigma": 20,
    "rho_floor_vol_pct": r2(20 * math.sqrt(0.7), 1),
}
fig, ax = plt.subplots(figsize=(5.2, 4.2))
ax.scatter(rets.nifty * 100, rets.brit * 100, s=7, color=BLUE, alpha=0.55, edgecolors="none")
x = np.linspace(rets.nifty.min() * 100, rets.nifty.max() * 100, 2)
ax.plot(x, beta * x, color=RED, lw=1.2)
ax.axhline(0, color=GREY, lw=0.6); ax.axvline(0, color=GREY, lw=0.6)
ax.set_xlabel("Nifty 50 daily return (%)"); ax.set_ylabel("Britannia daily return (%)")
ax.set_title(f"Daily returns, Apr 2024 – Mar 2026: ρ = {rho:.2f}, β = {beta:.2f}", loc="left", fontsize=10, color=INK)
fig.tight_layout(); fig.savefig(CHARTS / "risk-correlation.svg"); plt.close(fig)

# --------------------------------------------------------------------------
# RISK-6  Sequence of returns
# --------------------------------------------------------------------------
fy_list = fy_ret.values / 100  # FY07..FY26 in actual order


def sip_path(annual, monthly=10000):
    v, path = 0.0, []
    for R in annual:
        m = (1 + R) ** (1 / 12) - 1
        for _ in range(12):
            v = (v + monthly) * (1 + m)
            path.append(v)
    return path


def swp_path(annual, start=5_000_000, monthly=30000):
    v, path, dep = start, [], None
    for i, R in enumerate(annual):
        m = (1 + R) ** (1 / 12) - 1
        for j in range(12):
            v = (v - monthly) * (1 + m)
            if v <= 0 and dep is None:
                dep = i * 12 + j + 1
                v = 0.0
            path.append(max(v, 0.0))
    return path, dep


orders = {"actual": fy_list, "best_first": np.sort(fy_list)[::-1], "worst_first": np.sort(fy_list)}
invested = 10000 * 12 * years
lump = 100000 * float(np.prod(1 + fy_list))
seq = {"years": years, "first_fy": fy_ret.index[0], "last_fy": fy_ret.index[-1], "sip_monthly": 10000,
       "sip_invested": invested, "lump_sum_start": 100000, "lump_sum_end_any_order": int(round(lump)),
       "swp_start": 5_000_000, "swp_monthly": 30000, "orders": {}}
paths = {}
for k, ann in orders.items():
    p = sip_path(ann); paths[k] = p
    sw, dep = swp_path(ann)
    seq["orders"][k] = {"sip_final": int(round(p[-1])), "swp_final": int(round(sw[-1])),
                        "swp_depleted_month": dep, "swp_depleted_year": (r2(dep / 12, 1) if dep else None),
                        "first_three_fy_pct": [r2(x * 100, 1) for x in ann[:3]], "last_three_fy_pct": [r2(x * 100, 1) for x in ann[-3:]]}
seq["sip_best_minus_worst"] = seq["orders"]["best_first"]["sip_final"] - seq["orders"]["worst_first"]["sip_final"]
out["sequence_of_returns"] = seq

fig, ax = plt.subplots(figsize=(6.4, 3.6))
xs = np.arange(1, years * 12 + 1) / 12
for k, c, lab in (("worst_first", RED, "worst years first"), ("actual", BLUE, "actual order (FY07→FY26)"), ("best_first", GREY, "best years first")):
    ax.plot(xs, np.array(paths[k]) / 1e5, color=c, lw=1.5, label=lab)
ax.plot(xs, np.arange(1, years * 12 + 1) * 10000 / 1e5, color=INK, lw=0.8, ls="--", label="amount invested")
ax.set_xlabel("Years of ₹10,000-a-month SIP"); ax.set_ylabel("Value (₹ lakh)"); ax.legend(frameon=False, fontsize=8)
ax.set_title("Same 20 annual returns, three orders", loc="left", fontsize=10, color=INK)
fig.tight_layout(); fig.savefig(CHARTS / "risk-sequence.svg"); plt.close(fig)

# --------------------------------------------------------------------------
# RISK-7  Behaviour: how often you sit below a previous high
# --------------------------------------------------------------------------
peak = r.cummax(); dd = r / peak - 1
out["behaviour"] = {
    "days": int(len(r)),
    "pct_days_at_high": r2((dd >= -0.001).mean() * 100, 1),
    "pct_days_below_10": r2((dd <= -0.10).mean() * 100, 1),
    "pct_days_below_20": r2((dd <= -0.20).mean() * 100, 1),
    "median_drawdown_pct": r2(dd.median() * 100, 1),
    "worst_fy": fy_ret.idxmin(), "worst_fy_pct": r2(fy_ret.min(), 1),
    "next_fy_pct": r2(fy_ret.iloc[list(fy_ret.index).index(fy_ret.idxmin()) + 1], 1),
    "down_fys": int((fy_ret < 0).sum()), "up_fys": int((fy_ret > 0).sum()),
}

OUT.write_text("# Risk, Leverage and Your Own Brain — every figure the series quotes.\n"
               "# GENERATED by scripts/derive_risk.py from the CSVs in assets/data/ — do not\n"
               "# edit by hand; re-run the script. Sources, lag check and conventions are in\n"
               "# the script's header. All NAV/price data ends 31 March 2026; the first risk\n"
               "# post publishes 2026-11-05, over seven months later (SEBI 3-month lag rule).\n\n"
               + yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=100))
print(yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=100))
