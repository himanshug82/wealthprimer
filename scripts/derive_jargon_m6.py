#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by Jargon, Decoded Module 6 (the twelve "terms the
other series lean on" posts) into _data/jargon_m6.yml.

WHY: the posts render numbers from that YAML via Liquid, never inline, so a
figure in a table always matches the same figure in the text and a correction
happens in one place. Nothing in jargon_m6.yml is typed by hand — re-run this.

    python3 scripts/derive_jargon_m6.py

INPUTS (all already committed, all read-only here):
  assets/data/britannia-ohlcv-2024-04-to-2026-03.csv   Yahoo Finance BRITANNIA.NS daily
  assets/data/nifty50-price-index.csv                  Yahoo Finance ^NSEI daily close (price index)
  assets/data/uti-nifty50-index-fund-nav.csv           AMFI NAV via mfapi.in (regular + direct)
  _data/case_study.yml                                 Desi Bites (fictional) model
  _data/real_company.yml                               Britannia FY25 audited results + 30 Jun 2025 price

LAG CHECK: every market series ends 30/31 March 2026; the earliest M6 post
publishes 2026-11-26, nearly eight months later. Britannia's price is the
30 June 2025 close, financials FY25. All comfortably past the 3-month rule.

Needs pandas, numpy, pyyaml (the repo's scratch venv has them; system python
may not).
"""
import math
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "jargon_m6.yml"

cs = yaml.safe_load((ROOT / "_data" / "case_study.yml").read_text())
rc = yaml.safe_load((ROOT / "_data" / "real_company.yml").read_text())

RF = cs["dcf"]["wacc"]["risk_free_rate"]  # 6.5, the illustrative G-Sec yield the WACC post used

# ---------------------------------------------------------------- data
brit = pd.read_csv(ROOT / "assets/data/britannia-ohlcv-2024-04-to-2026-03.csv", parse_dates=["date"]).set_index("date")
nifty = pd.read_csv(ROOT / "assets/data/nifty50-price-index.csv", parse_dates=["date"]).set_index("date")
nav = pd.read_csv(ROOT / "assets/data/uti-nifty50-index-fund-nav.csv", parse_dates=["date"]).set_index("date")

px = pd.concat([brit["close"].rename("brit"), nifty["nifty50_pri_close"].rename("nifty")], axis=1, sort=False).dropna()
ret = px.pct_change().dropna()


def r2(x):
    return float(round(x, 2))


def r1(x):
    return float(round(x, 1))


def ols_beta(y, x):
    cov = np.cov(x, y, ddof=1)
    beta = cov[0, 1] / cov[0, 0]
    corr = np.corrcoef(x, y)[0, 1]
    return beta, corr


def annualised(series):
    """CAGR of a price/NAV series between its first and last point."""
    years = (series.index[-1] - series.index[0]).days / 365.25
    return (series.iloc[-1] / series.iloc[0]) ** (1 / years) - 1, years


# ---------------------------------------------------------------- 1. beta
def beta_block(r, label):
    b, c = ols_beta(r["brit"].values, r["nifty"].values)
    return {
        "window": label,
        "start": str(r.index[0].date()),
        "end": str(r.index[-1].date()),
        "days": int(len(r)),
        "beta": r2(b),
        "correlation": r2(c),
        "r_squared": r2(c * c),
        "stock_vol_pct": r1(r["brit"].std() * math.sqrt(252) * 100),
        "index_vol_pct": r1(r["nifty"].std() * math.sqrt(252) * 100),
    }


beta_full = beta_block(ret, "Apr 2024 – Mar 2026 (full)")
beta_fy25 = beta_block(ret.loc["2024-04-01":"2025-03-31"], "FY25 (Apr 2024 – Mar 2025)")
beta_fy26 = beta_block(ret.loc["2025-04-01":"2026-03-31"], "FY26 (Apr 2025 – Mar 2026)")
wk = px.resample("W-FRI").last().dropna().pct_change().dropna()
bw, cw = ols_beta(wk["brit"].values, wk["nifty"].values)

# a sanity decomposition the post uses: beta = corr x (sigma_stock / sigma_index)
b_check = beta_full["correlation"] * beta_full["stock_vol_pct"] / beta_full["index_vol_pct"]

beta = {
    "full": beta_full,
    "fy25": beta_fy25,
    "fy26": beta_fy26,
    "weekly_full": {"beta": r2(bw), "correlation": r2(cw), "weeks": int(len(wk))},
    "identity_check": r2(b_check),
    "wacc_post_illustrative_beta": cs["dcf"]["wacc"]["beta"],
    "source_stock": "https://finance.yahoo.com/quote/BRITANNIA.NS/history/",
    "source_index": "https://finance.yahoo.com/quote/%5ENSEI/history/",
}

# ---------------------------------------------------------------- 2. alpha
brit_cagr, yrs2 = annualised(px["brit"])
nifty_cagr, _ = annualised(px["nifty"])
expected = RF / 100 + beta_full["beta"] * (nifty_cagr - RF / 100)
jensen = brit_cagr - expected
# calendar-year excess returns of the index fund over the PRI, last ten full years
fund = nav["nav_regular_growth"].dropna()
common = pd.concat([fund.rename("fund"), nifty["nifty50_pri_close"].rename("idx")], axis=1, sort=False).dropna()
ye = common.resample("YE").last()
yr_ret = ye.pct_change().dropna() * 100
yr_ret = yr_ret.loc["2016":"2025"]
alpha_years = [
    {"year": int(i.year), "fund_pct": r2(row["fund"]), "index_pri_pct": r2(row["idx"]), "diff_pp": r2(row["fund"] - row["idx"])}
    for i, row in yr_ret.iterrows()
]
alpha = {
    "risk_free_pct": RF,
    "window": f"{px.index[0].date()} to {px.index[-1].date()}",
    "years": r2(yrs2),
    "britannia_cagr_pct": r2(brit_cagr * 100),
    "nifty_pri_cagr_pct": r2(nifty_cagr * 100),
    "raw_excess_pp": r2((brit_cagr - nifty_cagr) * 100),
    "beta_used": beta_full["beta"],
    "capm_expected_pct": r2(expected * 100),
    "jensen_alpha_pp": r2(jensen * 100),
    "index_fund_vs_pri_years": alpha_years,
    "index_fund_vs_pri_mean_pp": r2(float(np.mean([a["diff_pp"] for a in alpha_years]))),
}

# ---------------------------------------------------------------- 3. tracking error / difference
td_rows = []
for col, label in (("nav_regular_growth", "regular"), ("nav_direct_growth", "direct")):
    s = pd.concat([nav[col].rename("fund"), nifty["nifty50_pri_close"].rename("idx")], axis=1, sort=False).dropna()
    y = s.resample("YE").last().pct_change().dropna() * 100
    y = y.loc["2016":"2025"]
    for i, row in y.iterrows():
        td_rows.append({"year": int(i.year), "plan": label, "fund_pct": r2(row["fund"]), "index_pri_pct": r2(row["idx"]), "tracking_difference_pp": r2(row["fund"] - row["idx"])})

reg = pd.concat([nav["nav_regular_growth"].rename("fund"), nifty["nifty50_pri_close"].rename("idx")], axis=1, sort=False).dropna()
last3 = reg.loc["2023-04-01":"2026-03-31"]
d_daily = last3.pct_change().dropna()
diff_daily = d_daily["fund"] - d_daily["idx"]
te_daily = diff_daily.std() * math.sqrt(252) * 100
m = last3.resample("ME").last().pct_change().dropna()
te_monthly = (m["fund"] - m["idx"]).std() * math.sqrt(12) * 100
td_3y_fund, _ = annualised(last3["fund"])
td_3y_idx, _ = annualised(last3["idx"])
reg_years = [r for r in td_rows if r["plan"] == "regular"]
dir_years = [r for r in td_rows if r["plan"] == "direct"]
tracking = {
    "window_3y": "1 Apr 2023 – 31 Mar 2026",
    "tracking_error_daily_annualised_pct": r2(te_daily),
    "tracking_error_monthly_annualised_pct": r2(te_monthly),
    "fund_cagr_3y_pct": r2(td_3y_fund * 100),
    "index_pri_cagr_3y_pct": r2(td_3y_idx * 100),
    "tracking_difference_3y_pp": r2((td_3y_fund - td_3y_idx) * 100),
    "regular_years": reg_years,
    "direct_years": dir_years,
    "regular_mean_td_pp": r2(float(np.mean([r["tracking_difference_pp"] for r in reg_years]))),
    "direct_mean_td_pp": r2(float(np.mean([r["tracking_difference_pp"] for r in dir_years]))),
    "direct_minus_regular_pp": r2(float(np.mean([r["tracking_difference_pp"] for r in dir_years])) - float(np.mean([r["tracking_difference_pp"] for r in reg_years]))),
    "pri_caveat": "The benchmark here is the *price* index, which excludes dividends. A positive tracking difference against it is mostly the roughly 1–1.5% dividend yield of the fifty stocks, minus the expense ratio — not outperformance.",
}

# ---------------------------------------------------------------- 4/5. bond: YTM and duration
FACE, COUPON, YEARS = 1000.0, 7.0, 5


def bond_price(ytm_pct, coupon_pct=COUPON, years=YEARS, face=FACE):
    y = ytm_pct / 100
    c = face * coupon_pct / 100
    return sum(c / (1 + y) ** t for t in range(1, years + 1)) + face / (1 + y) ** years


def solve_ytm(price, coupon_pct=COUPON, years=YEARS, face=FACE):
    lo, hi = 0.0, 50.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if bond_price(mid, coupon_pct, years, face) > price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def durations(ytm_pct, coupon_pct=COUPON, years=YEARS, face=FACE):
    y = ytm_pct / 100
    c = face * coupon_pct / 100
    flows = [(t, c + (face if t == years else 0)) for t in range(1, years + 1)]
    pv = [(t, cf / (1 + y) ** t) for t, cf in flows]
    price = sum(p for _, p in pv)
    mac = sum(t * p for t, p in pv) / price
    return mac, mac / (1 + y), price


BUY_PRICE = 960.0
ytm_exact = solve_ytm(BUY_PRICE)   # ~8.002% for a Rs 960 price
# Everything shown to the reader is computed at the ROUNDED yield (8.00%), so
# the PV schedule, the price ladder and the duration repricing all agree with
# each other (Rs 960.07 at 8%, Rs 1,000.00 at 7%, Rs 922.21 at 9%). The exact
# yield is kept only so the post can say it is a hair above 8%.
ytm = round(ytm_exact, 2)
price_at_ytm = bond_price(ytm)
mac, mod, _ = durations(ytm)
price_up = bond_price(ytm + 1)
price_dn = bond_price(ytm - 1)
schedule = [{"year": t, "cash_flow": r2(FACE * COUPON / 100 + (FACE if t == YEARS else 0)), "pv_at_ytm": r2((FACE * COUPON / 100 + (FACE if t == YEARS else 0)) / (1 + ytm / 100) ** t)} for t in range(1, YEARS + 1)]
ladder = [{"ytm_pct": y, "price": r2(bond_price(y))} for y in (5.0, 6.0, 7.0, 8.0, 9.0)]
comp = []
for lbl, yrs_, cpn in (("1-year, 7% coupon", 1, 7.0), ("5-year, 7% coupon", 5, 7.0), ("10-year, 7% coupon", 10, 7.0), ("10-year, zero coupon", 10, 0.0)):
    mc, md, p = durations(7.0, cpn, yrs_)
    comp.append({"bond": lbl, "macaulay": r2(mc), "modified": r2(md), "price_change_for_plus_1pct": r1(-md * 1), "price_change_actual_plus_1pct": r1((bond_price(8.0, cpn, yrs_) / p - 1) * 100)})
bond = {
    "face": FACE, "coupon_pct": COUPON, "years": YEARS, "buy_price": BUY_PRICE,
    "annual_coupon": r2(FACE * COUPON / 100),
    "current_yield_pct": r2(FACE * COUPON / 100 / BUY_PRICE * 100),
    "ytm_pct": r2(ytm),
    "ytm_exact_pct": round(ytm_exact, 3),
    "price_at_ytm": r2(price_at_ytm),
    "price_ladder": ladder,
    "schedule_at_ytm": schedule,
    "macaulay_duration": r2(mac),
    "modified_duration": r2(mod),
    "price_if_ytm_plus_1pct": r2(price_up),
    "price_if_ytm_minus_1pct": r2(price_dn),
    "pct_change_plus_1": r2((price_up / price_at_ytm - 1) * 100),
    "pct_change_minus_1": r2((price_dn / price_at_ytm - 1) * 100),
    "duration_estimate_pct": r2(-mod),
    "comparison": comp,
}

# ---------------------------------------------------------------- 6. exit load on SIP lots
SIP = 10000.0
reg_nav = nav["nav_regular_growth"].dropna()
starts = pd.date_range("2025-01-01", "2026-02-01", freq="MS")
lots = []
for d in starts:
    idx = reg_nav.index[reg_nav.index.searchsorted(d)]
    n = reg_nav.loc[idx]
    lots.append({"date": str(idx.date()), "nav": r2(n), "units": round(SIP / n, 3)})
redeem_date = reg_nav.index[-1]
redeem_nav = float(reg_nav.iloc[-1])
cutoff = redeem_date - pd.Timedelta(days=365)
LOAD = 1.0
for lot in lots:
    within = pd.Timestamp(lot["date"]) > cutoff
    lot["within_365_days"] = bool(within)
    lot["value_at_redemption"] = r2(lot["units"] * redeem_nav)
    lot["exit_load"] = r2(lot["value_at_redemption"] * LOAD / 100) if within else 0.0
total_units = sum(l["units"] for l in lots)
gross = total_units * redeem_nav
load_total = sum(l["exit_load"] for l in lots)
exit_load = {
    "sip_amount": SIP, "instalments": len(lots), "invested": r2(SIP * len(lots)),
    "load_pct": LOAD, "load_window_days": 365,
    "redeem_date": str(redeem_date.date()), "redeem_nav": r2(redeem_nav),
    "cutoff_date": str(cutoff.date()),
    "lots": lots,
    "lots_loaded": int(sum(1 for l in lots if l["within_365_days"])),
    "lots_free": int(sum(1 for l in lots if not l["within_365_days"])),
    "total_units": round(total_units, 3),
    "gross_value": r2(gross), "exit_load_total": r2(load_total), "net_value": r2(gross - load_total),
    "load_as_pct_of_gross": r2(load_total / gross * 100),
    "fund": "UTI Nifty 50 Index Fund, Regular Plan - Growth (AMFI 100822)",
    "note": "Hypothetical 1%-within-365-days load applied to real NAVs for arithmetic only; this fund's actual load structure is not being described.",
}

# ---------------------------------------------------------------- 7. AUM: market movement alone
fy26 = reg_nav.loc["2025-03-31":"2026-03-31"]
fy26_chg = (fy26.iloc[-1] / fy26.iloc[0] - 1) * 100
fy25 = reg_nav.loc["2024-03-28":"2025-03-31"]
fy25_chg = (fy25.iloc[-1] / fy25.iloc[0] - 1) * 100
aum = {
    "illustrative_aum_start_cr": 10000.0,
    "fy26_nav_change_pct": r2(fy26_chg),
    "fy26_aum_end_no_flows_cr": r2(10000 * (1 + fy26_chg / 100)),
    "fy25_nav_change_pct": r2(fy25_chg),
    "fy25_aum_end_no_flows_cr": r2(10000 * (1 + fy25_chg / 100)),
    # SEBI TER slabs for open-ended equity schemes (in force since 1 April 2019). VERIFY before publishing.
    "ter_slabs_equity": [
        {"aum_slab": "First ₹500 crore", "max_ter_pct": 2.25},
        {"aum_slab": "Next ₹250 crore", "max_ter_pct": 2.00},
        {"aum_slab": "Next ₹1,250 crore", "max_ter_pct": 1.75},
        {"aum_slab": "Next ₹3,000 crore", "max_ter_pct": 1.60},
        {"aum_slab": "Next ₹5,000 crore", "max_ter_pct": 1.50},
        # Stepped slab: no single numeric cap, so it carries a text note instead
        # of max_ter_pct (the post prints the note verbatim, % signs included).
        {"aum_slab": "Next ₹40,000 crore", "max_ter_note": "1.50%, falling 0.05% for every ₹5,000 crore"},
        {"aum_slab": "Above ₹50,000 crore", "max_ter_pct": 1.05},
    ],
    "ter_cap_index_funds_pct": 1.00,
}

# ---------------------------------------------------------------- 8. operating leverage
def dol(a, b):
    rev = (b["revenue"] / a["revenue"] - 1) * 100
    ebit = (b["ebit"] / a["ebit"] - 1) * 100
    ebitda = (b["ebitda"] / a["ebitda"] - 1) * 100
    return {"revenue_growth_pct": r1(rev), "ebit_growth_pct": r1(ebit), "ebitda_growth_pct": r1(ebitda), "dol_ebit": r2(ebit / rev), "dol_ebitda": r2(ebitda / rev)}


isd = cs["income_statement"]
isb = rc["income_statement"]
# implied fixed/variable split for Desi Bites: opex treated as fixed-ish, COGS variable
oplev = {
    "desi_fy23_fy24": dol(isd["FY23"], isd["FY24"]),
    "desi_fy24_fy25": dol(isd["FY24"], isd["FY25"]),
    "britannia_fy24_fy25": dol(isb["FY24"], isb["FY25"]),
    "desi_fy25_cogs_pct_revenue": r1(isd["FY25"]["cogs"] / isd["FY25"]["revenue"] * 100),
    "desi_fy25_fixed_costs": r2(isd["FY25"]["opex"] + isd["FY25"]["depreciation"]),
    "desi_fy25_contribution_margin_pct": r1((1 - isd["FY25"]["cogs"] / isd["FY25"]["revenue"]) * 100),
    "desi_fy25_ebit": isd["FY25"]["ebit"],
    # what-if: revenue +10% with fixed costs flat and the same contribution margin
    "whatif_revenue": r2(isd["FY25"]["revenue"] * 1.10),
    "whatif_ebit": r2(isd["FY25"]["revenue"] * 1.10 * (1 - isd["FY25"]["cogs"] / isd["FY25"]["revenue"]) - (isd["FY25"]["opex"] + isd["FY25"]["depreciation"])),
}
oplev["whatif_ebit_growth_pct"] = r1((oplev["whatif_ebit"] / oplev["desi_fy25_ebit"] - 1) * 100)
oplev["dol_from_formula"] = r2((isd["FY25"]["revenue"] - isd["FY25"]["cogs"]) / isd["FY25"]["ebit"])  # contribution / EBIT

# ---------------------------------------------------------------- 9. earnings yield / FCF yield
mk = rc["market"]
lst = cs["listing"]
yields = {
    "britannia": {
        "price": mk["price"], "price_date": mk["price_date"], "eps": isb["FY25"]["eps"],
        "earnings_yield_pct": r2(isb["FY25"]["eps"] / mk["price"] * 100),
        "pe": rc["multiples"]["pe"],
        "fcf_cr": rc["ratios"]["FY25"]["fcf"], "market_cap_cr": mk["market_cap_cr"],
        "fcf_yield_pct": r2(rc["ratios"]["FY25"]["fcf"] / mk["market_cap_cr"] * 100),
        "dividend_yield_pct": rc["multiples"]["dividend_yield"],
    },
    "desi_bites": {
        "price": lst["ipo_price"], "eps_diluted": lst["eps_diluted"],
        "earnings_yield_pct": r2(lst["eps_diluted"] / lst["ipo_price"] * 100),
        "pe": r1(lst["ipo_price"] / lst["eps_diluted"]),
        "fcf_lakh": cs["ratios"]["FY25"]["fcf"], "market_cap_lakh": lst["market_cap"],
        "fcf_yield_pct": r2(cs["ratios"]["FY25"]["fcf"] / lst["market_cap"] * 100),
    },
    "gsec_yield_pct": RF,
}

# ---------------------------------------------------------------- 10. payout ratio
payout = {
    "britannia": {
        "dps": mk["dividend_per_share_fy25"], "eps": isb["FY25"]["eps"],
        "payout_pct": r1(mk["dividend_per_share_fy25"] / isb["FY25"]["eps"] * 100),
        "retention_pct": r1(100 - mk["dividend_per_share_fy25"] / isb["FY25"]["eps"] * 100),
        "roe_pct": rc["ratios"]["FY25"]["roe"],
    },
    "desi_bites": {
        "dps": lst["dividend_per_share_fy25"], "eps_undiluted": lst["eps_undiluted"],
        "dividend_lakh": isd["FY25"]["dividend"], "pat_lakh": isd["FY25"]["pat"],
        "payout_pct": r1(isd["FY25"]["dividend"] / isd["FY25"]["pat"] * 100),
        "retention_pct": r1(100 - isd["FY25"]["dividend"] / isd["FY25"]["pat"] * 100),
        "roe_pct": cs["ratios"]["FY25"]["roe"],
    },
}
for k in ("britannia", "desi_bites"):
    payout[k]["sustainable_growth_pct"] = r1(payout[k]["roe_pct"] * payout[k]["retention_pct"] / 100)

# ---------------------------------------------------------------- 11. face value, splits, bonuses
sd = cs["share_data"]
bonus = {
    "face_value": sd["face_value"],
    "before": {"shares_lakh": lst["post_ipo_shares_lakh"], "price": lst["ipo_price"], "eps_diluted": lst["eps_diluted"], "bvps": lst["book_value_per_share"], "market_cap_lakh": lst["market_cap"], "share_capital_lakh": r2(lst["post_ipo_shares_lakh"] * sd["face_value"])},
}
bonus["after_1_1_bonus"] = {
    "shares_lakh": lst["post_ipo_shares_lakh"] * 2, "price": lst["ipo_price"] / 2, "eps_diluted": r2(lst["eps_diluted"] / 2), "bvps": r2(lst["book_value_per_share"] / 2), "market_cap_lakh": lst["market_cap"],
    "share_capital_lakh": r2(lst["post_ipo_shares_lakh"] * 2 * sd["face_value"]), "face_value": sd["face_value"],
    "reserves_capitalised_lakh": r2(lst["post_ipo_shares_lakh"] * sd["face_value"]),
}
bonus["after_1_2_split"] = {
    "shares_lakh": lst["post_ipo_shares_lakh"] * 2, "price": lst["ipo_price"] / 2, "eps_diluted": r2(lst["eps_diluted"] / 2), "bvps": r2(lst["book_value_per_share"] / 2), "market_cap_lakh": lst["market_cap"],
    "share_capital_lakh": r2(lst["post_ipo_shares_lakh"] * sd["face_value"]), "face_value": sd["face_value"] / 2,
}
bonus["pe_before"] = r1(lst["ipo_price"] / lst["eps_diluted"])
bonus["pe_after"] = r1((lst["ipo_price"] / 2) / (lst["eps_diluted"] / 2))
bonus["britannia_face_value"] = 1
bonus["britannia_price"] = mk["price"]

# ---------------------------------------------------------------- 12. enterprise value
bs25 = rc["balance_sheet"]["FY25"]
ev = {
    "desi_bites": {"market_cap_lakh": lst["market_cap"], "debt_lakh": lst["post_ipo_debt"], "cash_lakh": lst["post_ipo_cash"], "ev_lakh": lst["ev"],
                    "ev_check": r2(lst["market_cap"] + lst["post_ipo_debt"] - lst["post_ipo_cash"]),
                    "ebitda_lakh": isd["FY25"]["ebitda"], "ev_ebitda": r1(lst["ev"] / isd["FY25"]["ebitda"]), "mcap_ebitda": r1(lst["market_cap"] / isd["FY25"]["ebitda"])},
    "britannia": {"market_cap_cr": mk["market_cap_cr"], "borrowings_cr": bs25["total_borrowings"], "cash_and_bank_cr": bs25["cash_and_bank"], "current_investments_cr": bs25["current_investments"],
                   "ev_cr": mk["ev_cr"], "ev_check": r2(mk["market_cap_cr"] + bs25["total_borrowings"] - bs25["cash_and_bank"] - bs25["current_investments"]),
                   "ebitda_cr": isb["FY25"]["ebitda"], "ev_ebitda": rc["multiples"]["ev_ebitda"], "mcap_ebitda": r1(mk["market_cap_cr"] / isb["FY25"]["ebitda"]),
                   "ev_minus_mcap_cr": r2(mk["ev_cr"] - mk["market_cap_cr"])},
    # a made-up pair for the "same market cap, different EV" table
    "illustration": [
        {"company": "A (net cash)", "market_cap": 1000, "debt": 0, "cash": 300, "ev": 700},
        {"company": "B (no debt, no cash)", "market_cap": 1000, "debt": 0, "cash": 0, "ev": 1000},
        {"company": "C (levered)", "market_cap": 1000, "debt": 600, "cash": 100, "ev": 1500},
    ],
}

out = {
    "_meta": {
        "generated_by": "scripts/derive_jargon_m6.py — do not edit by hand, re-run the script",
        "market_data_end": str(px.index[-1].date()),
        "nav_data_end": str(reg_nav.index[-1].date()),
        "britannia_price_date": mk["price_date"],
        "lag_note": "All series end March 2026 or earlier; first M6 post publishes 2026-11-26.",
    },
    "beta": beta, "alpha": alpha, "tracking": tracking, "bond": bond, "exit_load": exit_load,
    "aum": aum, "operating_leverage": oplev, "yields": yields, "payout": payout, "bonus": bonus, "ev": ev,
}

def _py(o):
    """yaml.safe_dump cannot represent numpy scalars; convert recursively."""
    if isinstance(o, dict):
        return {k: _py(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_py(v) for v in o]
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


out = _py(out)
OUT.write_text(
    "# GENERATED by scripts/derive_jargon_m6.py — every figure used by the Jargon,\n"
    "# Decoded Module 6 posts. Do not edit by hand; change the script and re-run.\n"
    "# Sources and the lag check are documented in the script header.\n"
    + yaml.safe_dump(out, sort_keys=False, allow_unicode=True, width=120)
)
print(f"wrote {OUT.relative_to(ROOT)}")
print("beta", beta_full["beta"], beta_fy25["beta"], beta_fy26["beta"], "weekly", r2(bw))
print("alpha", alpha["jensen_alpha_pp"], "raw", alpha["raw_excess_pp"])
print("TE", tracking["tracking_error_daily_annualised_pct"], "TD3y", tracking["tracking_difference_3y_pp"])
print("ytm", bond["ytm_pct"], "mod dur", bond["modified_duration"], bond["pct_change_plus_1"], bond["pct_change_minus_1"])
print("exit load", exit_load["lots_loaded"], exit_load["exit_load_total"], exit_load["load_as_pct_of_gross"])
print("aum", aum["fy26_nav_change_pct"], aum["fy25_nav_change_pct"])
print("oplev", oplev)
print("yields", yields)
print("payout", payout)
