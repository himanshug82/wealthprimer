#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by module 2 of "Risk, Leverage and Your Own Brain"
(_data/risk2.yml) and draw its charts (assets/charts/risk2-*.svg).

    python3 scripts/derive_risk2.py        # rewrites _data/risk2.yml + charts

Posts (2026-10-16 .. 2026-10-23): Kelly and risk of ruin; liquidity risk;
concentration risk; currency risk; inflation and real returns; broker and
counterparty risk (Karvy); pump-and-dump (SEBI's Sadhna Broadcast orders);
insurance as risk transfer.

Inputs already in the repo (see derive_risk.py for their sources):
  assets/data/uti-nifty50-index-fund-nav.csv   UTI Nifty 50 Index Fund, regular growth (AMFI via mfapi.in, code 100822)
  assets/data/uti-gilt-fund-nav.csv            UTI Gilt Fund, regular growth (AMFI via mfapi.in, code 102510)
  assets/data/uti-overnight-fund-nav.csv       UTI Overnight Fund, regular growth (AMFI via mfapi.in)
  assets/data/britannia-ohlcv-2024-04-to-2026-03.csv   Britannia daily OHLCV (Yahoo Finance, BRITANNIA.NS; NSE volume only)
  assets/data/nifty50-price-index.csv          Nifty 50 price index (Yahoo Finance, ^NSEI)

New inputs added for this module (all truncated at 31 March 2026):
  assets/data/cpi-all-india-combined.csv
      All-India CPI (General index, Combined), MoSPI.
      cpi_base2012: base 2012=100, Jan 2013 - Dec 2025, from MoSPI's API
        https://api.mospi.gov.in/api/cpi/getCPIIndex?base_year=2012&series=Current&state_code=99&sector_code=3&group_code=0&Format=JSON&year=YYYY
      cpi_base2024: base 2024=100, Jan 2025 - Mar 2026, from
        https://api.mospi.gov.in/api/cpi/getCPIData?base_year=2024&state_code=1&year=YYYY&month_code=M
      Base change: MoSPI's first CPI release on base 2024=100 (12 February 2026),
        https://www.mospi.gov.in/uploads/latestReleases/latest_release_1770891893893_6b458c0a-c327-4fef-a554-41131ea67273_Press_Relase_of_CPI_for_Jan26.pdf
        publishes a linking factor (Combined 0.5267) for the back series. We chain
        year-on-year changes instead: FY14-FY25 inside the base-2012 series, FY26
        (March 2025 -> March 2026) inside the base-2024 series. Each year's rate
        therefore equals MoSPI's own published March inflation (asserted below
        for FY26 = 3.40%).
  assets/data/usd-inr-reference-rate.csv
      USD/INR reference rate. RBI reference rate to 9 July 2018
        (https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx), FBIL reference
        rate from 10 July 2018, when FBIL took over the benchmark
        (https://www.fbil.org.in/wasdm/refrates/fetchfiltered?fromDate=..&toDate=..).
  assets/data/amfi-small-mid-cap-stress-test-2026-03.csv
      AMFI's risk-parameter disclosures for small-cap and mid-cap schemes, March
      2026 portfolios: https://www.amfiindia.com/api/risk-parameter-data-revised?strCatId=18&date=01-Mar-2026
      (small cap) and ...strCatId=17... (mid cap); page https://www.amfiindia.com/risk-parameters

Figures typed by hand (reported facts, each with its source) live in the
REPORTED dict below: SBI one-year deposit rates, and the facts quoted from
SEBI/NSE orders in the Karvy and Sadhna Broadcast posts.

Everything else is computed. Invariants are asserted.
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
OUT = ROOT / "_data" / "risk2.yml"

BLUE, LIGHT, INK, GREY, RED, GREEN = "#184f95", "#cde2fb", "#0b0b0b", "#52514e", "#b3261e", "#2e7d5b"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False,
                     "svg.fonttype": "none", "figure.dpi": 100, "svg.hashsalt": "risk2"})


def r2(x, n=2):
    """Round; a whole-number result is returned as an int so posts never show a false '.0'."""
    v = float(round(float(x), n))
    return int(v) if v.is_integer() else v


def save(fig, name):
    fig.tight_layout()
    fig.savefig(CHARTS / name, format="svg", metadata={"Date": None})
    plt.close(fig)


# --------------------------------------------------------------------------
# Reported facts (typed once, with sources)
# --------------------------------------------------------------------------
SBI_RATES_URL = "https://sbi.bank.in/documents/26242/65574/15022023+-Historical+Retail+Term+Deposit+Rates++.w.e.f+15.02.2023.xlsx/59a5e61d-10bc-a410-77e0-a2229c8fe753?t=1677074346573"
SBI_PAGE_URL = "https://sbi.bank.in/web/interest-rates/deposit-rates/retail-domestic-term-deposits"
# SBI retail term deposit (below Rs 2 crore; below Rs 1 crore before 2019), general public,
# the rate for a one-year deposit in force on 1 April of each year: the "1 year to less than
# 2 years" bucket, or "1 year to 455 days" when SBI split it (2015-2017). Read from SBI's
# historical-rates workbook (SBI_RATES_URL); 2015, 2016, 2018 and 2020 cross-checked against
# archived copies of SBI's rate page; 2023-2025 from archived copies of SBI_PAGE_URL
# (web.archive.org snapshots of 31 Mar 2023, 21 Apr 2024, 1 May 2025).
SBI_1Y = [  # (FY the deposit runs through, rate %, SBI "w.e.f." date of that rate)
    ("FY14", 8.75, "2013-03-01"), ("FY15", 9.00, "2014-02-18"), ("FY16", 8.50, "2014-12-08"),
    ("FY17", 7.25, "2015-10-05"), ("FY18", 6.90, "2017-03-01"), ("FY19", 6.40, "2018-03-28"),
    ("FY20", 6.80, "2019-02-22"), ("FY21", 5.70, "2020-03-28"), ("FY22", 5.00, "2021-01-08"),
    ("FY23", 5.10, "2022-02-15"), ("FY24", 6.80, "2023-02-15"), ("FY25", 6.80, "2023-12-27"),
    ("FY26", 6.80, "2024-06-15"),
]

# --------------------------------------------------------------------------
# Load
# --------------------------------------------------------------------------
def nav(name, col="nav_regular_growth"):
    return pd.read_csv(DATA / name, parse_dates=["date"]).set_index("date")[col].dropna()


idx = nav("uti-nifty50-index-fund-nav.csv")
gilt = nav("uti-gilt-fund-nav.csv")
ovn = nav("uti-overnight-fund-nav.csv")
br = pd.read_csv(DATA / "britannia-ohlcv-2024-04-to-2026-03.csv", parse_dates=["date"]).set_index("date")
nifty = pd.read_csv(DATA / "nifty50-price-index.csv", parse_dates=["date"]).set_index("date").nifty50_pri_close.dropna()
cpi = pd.read_csv(DATA / "cpi-all-india-combined.csv")
fx = pd.read_csv(DATA / "usd-inr-reference-rate.csv", parse_dates=["date"]).set_index("date").usd_inr
stress = pd.read_csv(DATA / "amfi-small-mid-cap-stress-test-2026-03.csv")

for s in (idx, gilt, ovn, br.close, nifty, fx):
    assert s.index.max() <= pd.Timestamp("2026-03-31"), "lag rule: data must end by 31 March 2026"

out = {"dataset": {
    "as_of": "31 March 2026",
    "fund_source_url": "https://api.mfapi.in/mf/100822",
    "gilt_source_url": "https://api.mfapi.in/mf/102510",
    "britannia_source_url": "https://finance.yahoo.com/quote/BRITANNIA.NS/history/",
    "nifty_source_url": "https://finance.yahoo.com/quote/%5ENSEI/history/",
    "cpi_csv": "/assets/data/cpi-all-india-combined.csv",
    "cpi_source_url": "https://esankhyiki.mospi.gov.in/macroindicators?product=cpi",
    "cpi_base_change_url": "https://www.mospi.gov.in/uploads/latestReleases/latest_release_1770891893893_6b458c0a-c327-4fef-a554-41131ea67273_Press_Relase_of_CPI_for_Jan26.pdf",
    "cpi_linking_factor_combined": 0.5267,
    "fx_csv": "/assets/data/usd-inr-reference-rate.csv",
    "fx_rbi_url": "https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx",
    "fx_fbil_url": "https://www.fbil.org.in/",
    "fx_fbil_start": "2018-07-10",
    "stress_csv": "/assets/data/amfi-small-mid-cap-stress-test-2026-03.csv",
    "stress_source_url": "https://www.amfiindia.com/risk-parameters",
    "sbi_rates_url": SBI_RATES_URL, "sbi_page_url": SBI_PAGE_URL,
}}


def fy_end_values(s, first_fy_end=2006, last_fy_end=2026):
    """Value on the last available date on or before 31 March of each year. A series that
    starts in early April 2006 (the funds' first NAV is 3 April 2006) uses its first value as
    the FY06 close, as derive_risk.py does."""
    v = {y: float(s.asof(pd.Timestamp(f"{y}-03-31"))) for y in range(first_fy_end, last_fy_end + 1)}
    if math.isnan(v[first_fy_end]):
        assert s.index.min() <= pd.Timestamp(f"{first_fy_end}-04-10")
        v[first_fy_end] = float(s.iloc[0])
    return pd.Series(v)


# --------------------------------------------------------------------------
# 1. Kelly criterion and risk of ruin
# --------------------------------------------------------------------------
def g(f, p, b=1.0):
    q = 1 - p
    return p * math.log(1 + b * f) + q * math.log(1 - f)


P_BELIEF = 0.55
F_STAR = P_BELIEF - (1 - P_BELIEF)  # even-money bet: f* = p - q
assert abs(F_STAR - 0.10) < 1e-12
# fraction at which growth hits zero (bisection)
lo, hi = F_STAR, 0.99
for _ in range(200):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if g(mid, P_BELIEF) > 0 else (lo, mid)
f_zero = (lo + hi) / 2

N_BETS = 1000
growth_rows = []
for f in (0.025, 0.05, 0.075, 0.10, 0.15, 0.20, 0.25):
    gg = g(f, P_BELIEF)
    growth_rows.append({"f_pct": r2(f * 100, 1), "kelly_multiple": r2(f / F_STAR, 2), "growth_per_bet_pct": r2(gg * 100, 3),
                        "median_multiple_1000": r2(math.exp(N_BETS * gg), 1)})
half_share = g(F_STAR / 2, P_BELIEF) / g(F_STAR, P_BELIEF)

# Estimation error: you believe p = 0.55 and bet full Kelly (10%) or half (5%); the truth differs.
est_rows = []
for p_true in (0.55, 0.54, 0.53, 0.52, 0.51, 0.50):
    est_rows.append({"p_true_pct": r2(p_true * 100, 0), "true_kelly_pct": r2(max(2 * p_true - 1, 0) * 100, 1),
                     "growth_full_pct": r2(g(0.10, p_true) * 100, 3), "growth_half_pct": r2(g(0.05, p_true) * 100, 3),
                     "median_full_1000": r2(math.exp(N_BETS * g(0.10, p_true)), 2),
                     "median_half_1000": r2(math.exp(N_BETS * g(0.05, p_true)), 2)})

# Monte Carlo: chance of ever halving within 1,000 bets
rng = np.random.default_rng(20261016)
PATHS = 20000
wins = rng.random((PATHS, N_BETS)) < P_BELIEF
mc = []
for f, label in ((0.05, "half"), (0.10, "full"), (0.20, "double")):
    step = np.where(wins, math.log(1 + f), math.log(1 - f))
    path = np.cumsum(step, axis=1)
    ever_half = (path.min(axis=1) <= math.log(0.5)).mean()
    ever_70 = (path.min(axis=1) <= math.log(0.3)).mean()
    c = f / F_STAR
    mc.append({"label": label, "f_pct": r2(f * 100, 1), "p_ever_half_pct": r2(ever_half * 100, 1),
               "p_ever_lose_70_pct": r2(ever_70 * 100, 1),
               "thorp_p_half_pct": (r2(100 * 0.5 ** (2 / c - 1), 1) if c < 2 else None),
               "median_final_multiple": r2(math.exp(np.median(path[:, -1])), 1),
               "p_below_start_pct": r2((path[:, -1] < 0).mean() * 100, 1)})

# Gambler's ruin with a fixed stake: P(ruin) = (q/p)^N
ruin = []
for p in (0.50, 0.51, 0.53, 0.55):
    row = {"p_pct": r2(p * 100, 0)}
    for n in (5, 10, 20, 50):
        row[f"n{n}"] = r2(100 * (1.0 if p <= 0.5 else ((1 - p) / p) ** n), 1)
    ruin.append(row)

# Real data: the continuous Kelly fraction (mu - r) / sigma^2, re-estimated on rolling 5-FY windows.
idx_fy = fy_end_values(idx)
# The overnight fund's face value went from Rs 10 to Rs 1,000 on 3 May 2018 (a known quirk,
# see TODO.md): chain daily returns and zero out that one re-denomination day.
ovn_d = ovn.pct_change()
jumps = ovn_d[ovn_d.abs() > 0.5]
assert len(jumps) == 1 and str(jumps.index[0].date()) == "2018-05-03", jumps
ovn_d.loc[jumps.index] = 0.0
ovn_chain = (1 + ovn_d.fillna(0)).cumprod() * ovn.iloc[0]
ovn_fy = fy_end_values(ovn_chain)
idx_ret = idx_fy.pct_change().dropna()   # index 2007..2026 = FY07..FY26
ovn_ret = ovn_fy.pct_change().dropna()
excess = idx_ret - ovn_ret
kelly_windows = []
for end in range(2011, 2027):
    w = [y for y in range(end - 4, end + 1)]
    mu = excess.loc[w].mean()
    var = idx_ret.loc[w].var(ddof=1)
    kelly_windows.append({"window": f"FY{str(w[0])[-2:]}–FY{str(w[-1])[-2:]}", "mean_excess_pct": r2(mu * 100, 1),
                          "stdev_pct": r2(math.sqrt(var) * 100, 1), "kelly_fraction": r2(mu / var, 2)})
kf = [k["kelly_fraction"] for k in kelly_windows]
out["kelly"] = {
    "p": P_BELIEF, "p_pct": 55, "q_pct": 45, "b": 1, "f_star_pct": r2(F_STAR * 100, 1), "f_zero_growth_pct": r2(f_zero * 100, 1),
    "n_bets": N_BETS, "growth_table": growth_rows, "half_kelly_growth_share_pct": r2(half_share * 100, 0),
    "full_growth_per_bet_pct": r2(g(F_STAR, P_BELIEF) * 100, 3),
    "estimation_table": est_rows, "monte_carlo": {m["label"]: m for m in mc}, "mc_paths": PATHS,
    "ruin_table": ruin,
    "windows": kelly_windows, "window_min": min(kf), "window_max": max(kf),
    "windows_negative": sum(1 for k in kf if k < 0), "windows_above_one": sum(1 for k in kf if k > 1),
    "windows_count": len(kf),
    "kelly_1956_url": "https://www.princeton.edu/~wbialek/rome/refs/kelly_56.pdf",
    "thorp_url": "https://www.eecs.harvard.edu/cs286r/courses/fall12/papers/Thorpe_KellyCriterion2007.pdf",
}
assert out["kelly"]["windows_count"] == 16
assert abs(out["kelly"]["monte_carlo"]["full"]["p_ever_half_pct"] - 50) < 8, "MC should sit near Thorp's x = 50%"

fig, ax = plt.subplots(figsize=(6.2, 3.3))
F = np.linspace(0.001, 0.215, 300)
for p, c, lab in ((0.55, BLUE, "true edge = what you believed (p = 0.55)"), (0.52, RED, "true edge smaller (p = 0.52)")):
    ax.plot(F * 100, [g(f, p) * 100 for f in F], color=c, lw=1.8, label=lab)
ax.axhline(0, color=GREY, lw=0.7)
ax.axvline(10, color=INK, lw=0.8, ls=":")
ax.annotate("full Kelly for p = 0.55", (10.3, 0.55), fontsize=8, color=INK)
ax.set_xlabel("Fraction of capital bet each time (%)"); ax.set_ylabel("Growth per bet (%)")
ax.set_ylim(-1.2, 0.8); ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.set_title("Overbetting a smaller edge turns growth negative", loc="left", fontsize=10, color=INK)
save(fig, "risk2-kelly.svg")

# --------------------------------------------------------------------------
# 2. Liquidity risk
# --------------------------------------------------------------------------
sc = stress[stress.category == "Small Cap"].copy()
mcp = stress[stress.category == "Mid Cap"].copy()


def cat_stats(d):
    d = d.sort_values("aum_cr", ascending=False)
    big = d.iloc[0]
    aum = d.aum_cr.sum()
    rho = d.aum_cr.rank().corr(d.days_to_liquidate_50pct.rank())
    return {"schemes": int(len(d)), "aum_total_cr": int(round(aum)),
            "median_days_50": r2(d.days_to_liquidate_50pct.median(), 1), "median_days_25": r2(d.days_to_liquidate_25pct.median(), 1),
            "min_days_50": int(d.days_to_liquidate_50pct.min()), "max_days_50": int(d.days_to_liquidate_50pct.max()),
            "aum_weighted_days_50": r2((d.aum_cr * d.days_to_liquidate_50pct).sum() / aum, 0),
            "share_aum_over_30_days_pct": r2(d.loc[d.days_to_liquidate_50pct > 30, "aum_cr"].sum() / aum * 100, 0),
            "schemes_over_30_days": int((d.days_to_liquidate_50pct > 30).sum()),
            "largest_aum_cr": int(round(big.aum_cr)), "largest_days_50": int(big.days_to_liquidate_50pct), "largest_days_25": int(big.days_to_liquidate_25pct),
            "spearman_aum_days": r2(rho, 2)}


# Britannia: what one day's volume can absorb (NSE only — Yahoo's volume is NSE's)
traded = br[br.volume > 0]  # a few zero-volume rows in the Yahoo file are dropped
tv = (traded.close * traded.volume) / 1e7  # Rs crore traded per day
med_tv = float(tv.median())
PART = 0.10
liq = {"stress_small": cat_stats(sc), "stress_mid": cat_stats(mcp),
       "britannia_median_traded_cr": r2(med_tv, 1), "britannia_days": int(len(tv)), "britannia_zero_volume_rows": int((br.volume == 0).sum()),
       "britannia_window_start": str(br.index.min().date()), "britannia_window_end": str(br.index.max().date()),
       "participation_pct": 10}
liq["exit_rows"] = [{"position_cr": pos, "days": r2(pos / (PART * med_tv), 1)} for pos in (1, 10, 100, 500)]

# Impact cost on a hypothetical order book (NSE's definition: % mark-up vs the ideal price (best bid + best ask)/2)
bids = [(100.00, 1500), (99.95, 2000), (99.90, 2500), (99.80, 3000), (99.60, 5000)]
ask = 100.10
ideal = (bids[0][0] + ask) / 2


def sell_into(qty):
    left, value = qty, 0.0
    for px, q in bids:
        take = min(left, q); value += take * px; left -= take
        if left == 0:
            break
    assert left == 0
    avg = value / qty
    return {"qty": qty, "avg_price": f"{avg:.3f}", "impact_pct": r2((ideal - avg) / ideal * 100, 3),
            "cost_rupees": int(round((ideal - avg) * qty))}


liq["book"] = {"bids": [{"price": f"{p:.2f}", "qty": q} for p, q in bids], "best_ask": f"{ask:.2f}", "ideal": f"{ideal:.2f}",
               "orders": [sell_into(q) for q in (1000, 5000, 10000)]}

# Days to liquidate, a hypothetical four-stock fund, selling pro rata at 10% of average daily volume
fund = [("A (large cap)", 400, 800), ("B (mid cap)", 300, 60), ("C (small cap)", 200, 8), ("D (micro cap)", 100, 1)]  # Rs cr held, Rs cr ADV
rows, fund_total = [], sum(x[1] for x in fund)
for name, held, adv in fund:
    per_day = PART * adv
    rows.append({"stock": name, "held_cr": held, "adv_cr": adv, "sell_per_day_cr": r2(per_day, 1),
                 "days_25": r2(0.25 * held / per_day, 1), "days_50": r2(0.50 * held / per_day, 1), "days_100": r2(held / per_day, 1)})
liq["toy_fund"] = {"rows": rows, "total_cr": fund_total,
                   "days_25": max(r["days_25"] for r in rows), "days_50": max(r["days_50"] for r in rows),
                   "days_25_ex_d": max(r["days_25"] for r in rows[:3]), "days_50_ex_d": max(r["days_50"] for r in rows[:3])}
out["liquidity"] = liq

# --------------------------------------------------------------------------
# 3. Concentration: one stock vs the index, Apr 2024 - Mar 2026
# --------------------------------------------------------------------------
both = pd.concat([br.close.rename("brit"), nifty.rename("nifty")], axis=1, sort=True).dropna()
rel = both / both.iloc[0]
START = 10_00_000
ports = {"stock": (1.0, 0.0), "seventy": (0.7, 0.3), "half": (0.5, 0.5), "index": (0.0, 1.0)}
conc = {"start": str(both.index[0].date()), "end": str(both.index[-1].date()), "days": int(len(both)), "start_value": START, "portfolios": {}}
paths = {}
for k, (wb, wn) in ports.items():
    v = START * (wb * rel.brit + wn * rel.nifty)  # buy and hold, no rebalancing
    paths[k] = v
    dd = v / v.cummax() - 1
    trough = dd.idxmin(); peak = v.loc[:trough].idxmax()
    r = v.pct_change().dropna()
    m21 = (v / v.shift(21) - 1).dropna()
    conc["portfolios"][k] = {
        "stock_weight_pct": int(wb * 100), "end_value": int(round(v.iloc[-1])), "return_pct": r2((v.iloc[-1] / START - 1) * 100, 1),
        "vol_pct": r2(r.std() * math.sqrt(252) * 100, 1), "max_dd_pct": r2(dd.min() * 100, 1),
        "max_dd_rupees": int(round(v.loc[peak] - v.loc[trough])),
        "peak_date": str(peak.date()), "trough_date": str(trough.date()),
        "worst_21d_pct": r2(m21.min() * 100, 1), "worst_21d_end": str(m21.idxmin().date()),
        "lowest_value": int(round(v.min())), "days_below_start_pct": r2((v < START).mean() * 100, 0)}
p = conc["portfolios"]
assert p["stock"]["vol_pct"] > p["half"]["vol_pct"] > 0 and p["stock"]["max_dd_pct"] < p["index"]["max_dd_pct"]
dr = both.pct_change().dropna()
rho_bn = dr.corr().iloc[0, 1]
conc["rho"] = r2(rho_bn, 2)
conc["beta"] = r2(dr.brit.cov(dr.nifty) / dr.nifty.var(), 2)
conc["systematic_share_pct"] = r2(rho_bn ** 2 * 100, 0)       # share of the stock's daily variance the index explains
conc["specific_share_pct"] = r2((1 - rho_bn ** 2) * 100, 0)
conc["stock_minus_index_pp"] = r2(p["stock"]["return_pct"] - p["index"]["return_pct"], 1)
out["concentration"] = conc

fig, ax = plt.subplots(figsize=(6.4, 3.4))
for k, c, lab in (("stock", RED, "100% Britannia"), ("half", GREY, "50/50"), ("index", BLUE, "100% Nifty 50 (price index)")):
    dd = paths[k] / paths[k].cummax() - 1
    ax.plot(dd.index, dd * 100, color=c, lw=1.3, label=lab)
ax.set_ylabel("Below previous high (%)"); ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.set_title("Drawdowns, Apr 2024 – Mar 2026, buy and hold", loc="left", fontsize=10, color=INK)
save(fig, "risk2-concentration.svg")

# --------------------------------------------------------------------------
# 4. Currency: USD/INR at each financial-year end
# --------------------------------------------------------------------------
fx_fy = fy_end_values(fx)
fx_chg = fx_fy.pct_change().dropna() * 100
years_fx = len(fx_chg)
cagr_fx = ((fx_fy.iloc[-1] / fx_fy.iloc[0]) ** (1 / years_fx) - 1) * 100
fx_rows = []
for y in fx_chg.index:
    d = fx.index[fx.index <= pd.Timestamp(f"{y}-03-31")].max()
    fx_rows.append({"fy": f"FY{str(y)[-2:]}", "date": str(d.date()), "usd_inr": r2(fx_fy[y], 2), "change_pct": r2(fx_chg[y], 1),
                    "index_fund_pct": r2(idx_ret[y] * 100, 1)})
up = fx_chg[fx_chg < 0]
worst_idx = idx_ret.sort_values().index[:2]  # the index fund's two worst FYs
cur = {"rows": fx_rows, "start_date": str(fx.index[fx.index <= pd.Timestamp("2006-03-31")].max().date()), "start_rate": r2(fx_fy.iloc[0], 2),
       "end_date": str(fx.index.max().date()), "end_rate": r2(fx_fy.iloc[-1], 2), "years": years_fx,
       "cagr_pct": r2(cagr_fx, 1), "total_change_pct": r2((fx_fy.iloc[-1] / fx_fy.iloc[0] - 1) * 100, 0),
       "appreciation_years": int(len(up)), "depreciation_years": int((fx_chg > 0).sum()),
       "biggest_fall_fy": f"FY{str(fx_chg.idxmax())[-2:]}", "biggest_fall_pct": r2(fx_chg.max(), 1),
       "biggest_rise_fy": f"FY{str(fx_chg.idxmin())[-2:]}", "biggest_rise_pct": r2(fx_chg.min(), 1),
       "worst_index_fys": [{"fy": f"FY{str(y)[-2:]}", "index_fund_pct": r2(idx_ret[y] * 100, 1), "fx_pct": r2(fx_chg[y], 1)} for y in sorted(worst_idx)],
       "fy26_pct": r2(fx_chg[2026], 1), "fy08_pct": r2(fx_chg[2008], 1)}
down = idx_ret[idx_ret < 0].index
cur["index_down_fys"] = int(len(down))
cur["index_down_fys_rupee_weaker"] = int((fx_chg[down] > 0).sum())
cur["index_down_fy_list"] = ", ".join(f"FY{str(y)[-2:]}" for y in down)
cur["base_rate_weaker_pct"] = r2((fx_chg > 0).mean() * 100, 0)
up_years = idx_ret[idx_ret > 0].index
cur["index_up_fys"] = int(len(up_years))
cur["index_up_fys_rupee_weaker"] = int((fx_chg[up_years] > 0).sum())
cur["chance_all_down_by_base_rate_pct"] = r2(((fx_chg > 0).mean() ** len(down)) * 100, 0)
# volatility, daily, over the full series vs the Nifty over the same dates
fxv = pd.concat([fx.rename("fx"), nifty.rename("n")], axis=1, sort=True).dropna().pct_change().dropna()
cur["fx_vol_pct"] = r2(fxv.fx.std() * math.sqrt(252) * 100, 1)
cur["nifty_vol_pct"] = r2(fxv.n.std() * math.sqrt(252) * 100, 1)
cur["vol_window_start"] = str(fxv.index.min().date())
# decomposition example: hypothetical USD returns in two real years
decomp = []
for fyk in (2008, 2026):
    for usd in (10, 0, -10):
        inr = ((1 + usd / 100) * (1 + fx_chg[fyk] / 100) - 1) * 100
        decomp.append({"fy": f"FY{str(fyk)[-2:]}", "usd_return_pct": usd, "fx_pct": r2(fx_chg[fyk], 1), "inr_return_pct": r2(inr, 1)})
cur["decomp"] = decomp
out["currency"] = cur
assert cur["appreciation_years"] + cur["depreciation_years"] == years_fx

fig, ax = plt.subplots(figsize=(6.2, 3.2))
ax.plot(fx.index, fx.values, color=BLUE, lw=1.1)
ax.set_ylabel("Rupees per US dollar")
ax.set_title("USD/INR reference rate, Jan 2006 – Mar 2026 (RBI, then FBIL)", loc="left", fontsize=10, color=INK)
save(fig, "risk2-usdinr.svg")

# --------------------------------------------------------------------------
# 5. Inflation and real returns, FY14 - FY26 (pre-tax)
# --------------------------------------------------------------------------
old = cpi.set_index("month").cpi_base2012.dropna()
new = cpi.set_index("month").cpi_base2024.dropna()
infl = {}
for y in range(2014, 2027):
    ser = old if y <= 2025 else new
    infl[y] = ser[f"{y}-03"] / ser[f"{y - 1}-03"] - 1
assert abs(infl[2026] * 100 - 3.40) < 0.01, "FY26 must match MoSPI's published March 2026 inflation (3.40%)"
assert abs(infl[2025] * 100 - 3.34) < 0.01, "FY25 must match the base-2012 March 2025 inflation (3.34%)"
gilt_fy = fy_end_values(gilt)
gilt_ret = gilt_fy.pct_change().dropna()
fd = {int("20" + fy[2:]): rate for fy, rate, _ in SBI_1Y}
fd_ret = {y: (1 + fd[y] / 400) ** 4 - 1 for y in fd}  # quarterly compounding, SBI's convention for these deposits
rows = []
cum = {"idx": 1.0, "gilt": 1.0, "fd": 1.0, "cpi": 1.0}
neg_real = {"idx": 0, "gilt": 0, "fd": 0}
for y in range(2014, 2027):
    i = infl[y]
    rr = {}
    for k, nominal in (("idx", idx_ret[y]), ("gilt", gilt_ret[y]), ("fd", fd_ret[y])):
        real = (1 + nominal) / (1 + i) - 1
        rr[k] = (nominal, real)
        cum[k] *= 1 + nominal
        neg_real[k] += real < 0
    cum["cpi"] *= 1 + i
    rows.append({"fy": f"FY{str(y)[-2:]}", "cpi_pct": r2(i * 100, 1), "fd_rate_pct": r2(fd[y]),
                 **{f"{k}_nominal_pct": r2(rr[k][0] * 100, 1) for k in rr}, **{f"{k}_real_pct": r2(rr[k][1] * 100, 1) for k in rr}})
N = 13
real_summary = {}
for k in ("idx", "gilt", "fd"):
    real_summary[k] = {"nominal_cagr_pct": r2((cum[k] ** (1 / N) - 1) * 100, 1),
                       "real_cagr_pct": r2(((cum[k] / cum["cpi"]) ** (1 / N) - 1) * 100, 1),
                       "lakh_nominal": int(round(100000 * cum[k])), "lakh_real": int(round(100000 * cum[k] / cum["cpi"])),
                       "negative_real_years": int(neg_real[k])}
for k in ("idx", "gilt", "fd"):
    worst = min(rows, key=lambda r: r[f"{k}_real_pct"])
    real_summary[k]["worst_real_pct"] = worst[f"{k}_real_pct"]
    real_summary[k]["worst_real_fy"] = worst["fy"]
for k in ("idx", "gilt", "fd"):
    real_summary[k]["negative_real_fy_list"] = " and ".join(r["fy"] for r in rows if r[f"{k}_real_pct"] < 0) if neg_real[k] <= 2 else ""
cpi_cagr = (cum["cpi"] ** (1 / N) - 1) * 100
hi_y = max(infl, key=infl.get); lo_y = min(infl, key=infl.get)
out["inflation"] = {"rows": rows, "years": N, "first_fy": "FY14", "last_fy": "FY26",
                    "cpi_cagr_pct": r2(cpi_cagr, 1), "cpi_cum_pct": r2((cum["cpi"] - 1) * 100, 0),
                    "lakh_needed": int(round(100000 * cum["cpi"])),
                    "cpi_mar2013": float(old["2013-03"]), "cpi_mar2025_old": float(old["2025-03"]),
                    "cpi_mar2025_new": float(new["2025-03"]), "cpi_mar2026_new": float(new["2026-03"]),
                    "highest_fy": f"FY{str(hi_y)[-2:]}", "highest_pct": r2(infl[hi_y] * 100, 1),
                    "lowest_fy": f"FY{str(lo_y)[-2:]}", "lowest_pct": r2(infl[lo_y] * 100, 1),
                    "summary": real_summary,
                    "doubling_years_at_cagr": r2(math.log(2) / math.log(1 + cpi_cagr / 100), 1),
                    "fd_rates": [{"fy": fy, "rate_pct": r2(rt), "wef": w} for fy, rt, w in SBI_1Y]}
assert out["inflation"]["summary"]["fd"]["real_cagr_pct"] < out["inflation"]["summary"]["fd"]["nominal_cagr_pct"]

fig, ax = plt.subplots(figsize=(6.2, 3.3))
xs = ["FY13 end"] + [r["fy"] for r in rows]
for k, c, lab in (("idx", BLUE, "Index fund"), ("gilt", GREEN, "Gilt fund"), ("fd", GREY, "SBI 1-year FD, rolled")):
    v, vals = 1.0, [1.0]
    for r in rows:
        v *= (1 + r[f"{k}_real_pct"] / 100); vals.append(v)
    ax.plot(range(len(xs)), np.array(vals) * 100000 / 1e5, color=c, lw=1.6, label=lab, marker="o", ms=2.5)
ax.axhline(1, color=INK, lw=0.7, ls="--")
ax.set_xticks(range(0, len(xs), 2)); ax.set_xticklabels(xs[::2], fontsize=7.5)
ax.set_ylabel("Rs 1 lakh in March-2013 rupees (lakh)"); ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("Real value of Rs 1 lakh, pre-tax, deflated by CPI", loc="left", fontsize=10, color=INK)
save(fig, "risk2-real-returns.svg")

# --------------------------------------------------------------------------
# 6. Counterparty / broker risk: Karvy (reported facts) + the G formula on a hypothetical broker
# --------------------------------------------------------------------------
A, B, C, D = 180, 60, 300, 40   # Rs crore, hypothetical weekly submission
G = (A + B) - C
H = abs(G) - abs(D)
out["karvy"] = {
    "sources": {
        "interim_order": "https://www.sebi.gov.in/enforcement/orders/nov-2019/ex-parte-ad-interim-order-in-respect-of-karvy-stock-broking-limited_45049.html",
        "confirmatory_order": "https://www.sebi.gov.in/sebi_data/attachdocs/nov-2020/1606225007513.pdf",
        "final_order": "https://www.sebi.gov.in/enforcement/orders/apr-2023/final-order-in-the-matter-of-karvy-stock-broking-limited_70734.html",
        "nse_notice": "https://nsearchives.nseindia.com/web/sites/default/files/inline-files/Public_Notice_Karvy_stock_broking_limited.pdf",
        "nse_ipf_2024": "https://nsearchives.nseindia.com/web/sites/default/files/2024-08/PR_cc_13082024.pdf",
        "circ_2016": "https://www.sebi.gov.in/legal/circulars/sep-2016/enhanced-supervision-of-stock-brokers-and-depository-participants_33334.html",
        "circ_2019": "https://www.sebi.gov.in/legal/circulars/jun-2019/handling-of-clients-securities-by-trading-members-clearing-members_43347.html",
        "circ_2020": "https://www.sebi.gov.in/legal/circulars/feb-2020/margin-obligations-to-be-given-by-way-of-pledge-re-pledge-in-the-depository-system_46082.html",
        "circ_2022_block": "https://www.sebi.gov.in/legal/circulars/aug-2022/block-mechanism-in-demat-account-of-clients-undertaking-sale-transactions_62131.html",
        "circ_2022_running": "https://www.sebi.gov.in/legal/circulars/jul-2022/settlement-of-running-account-of-client-s-funds-lying-with-trading-member-tm-_61222.html",
        "circ_2023_upstream": "https://www.sebi.gov.in/legal/circulars/jun-2023/upstreaming-of-clients-funds-by-stock-brokers-sbs-clearing-members-cms-to-clearing-corporations-ccs-_72380.html",
        "circ_2023_upi": "https://www.sebi.gov.in/legal/circulars/jun-2023/trading-supported-by-blocked-amount-in-secondary-market_73071.html",
        "circ_2024_upi": "https://www.sebi.gov.in/legal/circulars/nov-2024/trading-supported-by-blocked-amount-in-secondary-market_88339.html",
    },
    # SEBI interim order, 22 Nov 2019
    "excess_sold_cr": 485, "excess_sold_related_clients": 9, "to_group_company_cr": 1096,
    # SEBI confirmatory order, 24 Nov 2020 (quoting NSDL's 2 Dec 2019 release and NSE's statement)
    "nsdl_clients_returned": 82559, "nse_settled_cr": 2300, "nse_settled_investors_lakh": 2.35,
    # SEBI final order, 28 Apr 2023
    "pledged_jun2017_cr": 202, "pledged_mar2018_cr": 1855, "pledged_sep2019_cr": 2700, "raised_cr": 786.93,
    "pledged_share_pct": 75, "ban_years": 7, "director_ban_years": 10,
    "unsettled_clients": 318833, "unsettled_funds_cr": 527.18, "unsettled_securities_cr": 2862.05,  # as on 22 Nov 2019, final order Table 4
    # NSE Investor Protection Fund limits
    "ipf_limit_karvy_lakh": 25, "ipf_limit_now_lakh": 35,
    "g_example": {"A": A, "B": B, "C": C, "D": D, "G": G, "H": H},
}
assert G < 0 and H > 0

# --------------------------------------------------------------------------
# 7. Pump and dump: SEBI's Sadhna Broadcast orders (reported facts) + arithmetic on them
# --------------------------------------------------------------------------
pre_close, p1_close, peak_close, later = 2.76, 12.68, 33.15, 2.60
out["pump"] = {
    "sources": {
        "interim": "https://www.sebi.gov.in/enforcement/orders/mar-2023/interim-order-in-the-matter-of-stock-recommendations-using-youtube-in-the-scrip-of-sadhna-broadcast-limited_68595.html",
        "confirmatory": "https://www.sebi.gov.in/enforcement/orders/jul-2023/confirmatory-order-in-the-matter-of-stock-recommendations-using-youtube-in-the-scrip-of-sadhna-broadcast-limited_74217.html",
        "final": "https://www.sebi.gov.in/enforcement/orders/may-2025/final-order-in-the-matter-of-sadhna-broadcast-limited_94294.html",
        "gsm_circular": "https://archives.nseindia.com/content/circulars/SURV34262.pdf",
        "gsm_faq": "https://nsearchives.nseindia.com/web/sites/default/files/inline-files/FAQs%20-%20Graded%20Surveillance%20Measure%20(GSM)_15.4.25.pdf",
        "asm_faq": "https://nsearchives.nseindia.com/web/sites/default/files/inline-files/FAQs%20-%20Additional%20Surveillance%20Measure%20(ASM)_1.pdf",
        "asm_bse_faq": "https://www.bseindia.com/downloads1/faqs_on_asm.pdf",
        "caution_2020": "https://www.sebi.gov.in/sebi_data/attachdocs/oct-2020/1602673113928.pdf",
        "caution_2025": "https://www.sebi.gov.in/media-and-notifications/press-releases/may-2025/caution-to-investors-on-stock-market-scams-through-social-media-platforms_94064.html",
    },
    # interim order, 2 March 2023 (split-adjusted prices)
    "pre_close": pre_close, "p1_close": p1_close, "peak_close": peak_close,
    "p1_rise_pct_reported": 360, "p2_rise_pct_reported": 161,
    "adv_pre": 43740, "adv_p1": 259561, "adv_p2": 1892638,
    "buyers_p1": 2319, "buyers_p2": 77293,
    "small_holders_before": 2167, "small_holders_before_pct": 3.53, "small_holders_after": 55343, "small_holders_after_pct": 25.42,
    "views": 30205655, "ad_spend": 47224967, "impounded": 418582283, "noticees_interim": 31,
    "upper_circuit_days": 39, "patch1_days": 56,
    # confirmatory order, 20 July 2023
    "impounded_modified": 406066012,
    # final order, 29 May 2025
    "later_price": later, "noticees_final": 64, "five_year_bans": 7,
    "dec2022_from": 17.90, "dec2022_to": 12.10, "dec2022_lower_circuit_days": 22,
}
pp = out["pump"]
pp["later_price_text"] = f"{later:.2f}"
pp["dec2022_from_text"] = f"{pp['dec2022_from']:.2f}"
pp["dec2022_to_text"] = f"{pp['dec2022_to']:.2f}"
pp["multiple_to_peak"] = r2(peak_close / pre_close, 1)
pp["p1_rise_pct"] = r2((p1_close / pre_close - 1) * 100, 0)
pp["p2_rise_pct"] = r2((peak_close / p1_close - 1) * 100, 0)
pp["fall_from_peak_pct"] = r2((later / peak_close - 1) * 100, 1)
pp["gain_to_recover_pct"] = r2((peak_close / later - 1) * 100, 0)
pp["adv_multiple_p2"] = r2(pp["adv_p2"] / pp["adv_pre"], 0)
pp["adv_multiple_p1"] = r2(pp["adv_p1"] / pp["adv_pre"], 1)
pp["p1_price_multiple"] = r2(p1_close / pre_close, 1)
pp["buyers_multiple"] = r2(pp["buyers_p2"] / pp["buyers_p1"], 0)
pp["dec2022_fall_pct"] = r2((pp["dec2022_to"] / pp["dec2022_from"] - 1) * 100, 1)
pp["impounded_cr"] = r2(pp["impounded"] / 1e7, 2)
pp["ad_spend_cr"] = r2(pp["ad_spend"] / 1e7, 2)
pp["views_crore"] = r2(pp["views"] / 1e7, 2)
assert abs(pp["p1_rise_pct"] - pp["p1_rise_pct_reported"]) <= 1 and abs(pp["p2_rise_pct"] - pp["p2_rise_pct_reported"]) <= 1

# --------------------------------------------------------------------------
# 8. Insurance: needs-based cover and the savings component of a bundled plan (all hypothetical)
# --------------------------------------------------------------------------
need = {"annual_expenses": 6_00_000, "years": 25, "real_rate_pct": 2, "loans": 30_00_000, "goals": 20_00_000, "existing_assets": 15_00_000}
rr_ = need["real_rate_pct"] / 100
pv_exp = need["annual_expenses"] * (1 - (1 + rr_) ** -need["years"]) / rr_
need["pv_expenses"] = int(round(pv_exp))
need["pv_multiple_of_expenses"] = r2(pv_exp / need["annual_expenses"], 1)
need["cover"] = int(round(pv_exp + need["loans"] + need["goals"] - need["existing_assets"]))
need["cover_rounded_lakh"] = int(math.ceil(need["cover"] / 25e5) * 25)  # rounded up to the next Rs 25 lakh, in lakh
q_illus = 0.001   # purely illustrative one-year probability, NOT an estimate for any real person
cover = need["cover_rounded_lakh"] * 100000
need["cover_rounded_crore"] = r2(need["cover_rounded_lakh"] / 100, 2)
need["q_illustrative"] = q_illus
need["q_one_in"] = int(round(1 / q_illus))
need["expected_claim_cost"] = int(round(q_illus * cover))
# a hypothetical bundled plan: Rs 1 lakh a year for 20 years (paid at the start of each year), Rs 30 lakh at the end of year 20
prem, yrs, maturity = 1_00_000, 20, 30_00_000
lo, hi = -0.5, 0.5
for _ in range(200):
    mid = (lo + hi) / 2
    fv = sum(prem * (1 + mid) ** (yrs - t) for t in range(yrs))
    lo, hi = (mid, hi) if fv < maturity else (lo, mid)
irr = (lo + hi) / 2
bundle = {"premium": prem, "years": yrs, "maturity": maturity, "paid": prem * yrs, "irr_pct": r2(irr * 100, 2)}
bundle["alt_rows"] = []
for alt in (6, 8):
    a = alt / 100
    bundle["alt_rows"].append({"rate_pct": alt, "fv": int(round(sum(prem * (1 + a) ** (yrs - t) for t in range(yrs))))})
out["insurance"] = {"need": need, "bundle": bundle}
assert 0 < irr < 0.06

OUT.write_text("# Risk, Leverage and Your Own Brain, module 2 — every figure these posts quote.\n"
               "# GENERATED by scripts/derive_risk2.py — do not edit by hand; re-run the script.\n"
               "# Sources and conventions are in the script's header. Market data ends 31 March\n"
               "# 2026; the first post of this module publishes 16 October 2026.\n\n"
               + yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=100))
print(yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=100))
