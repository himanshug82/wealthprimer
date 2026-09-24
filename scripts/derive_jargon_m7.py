#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by Jargon, Decoded Module 7 ("Market mechanics": the
eight posts on spreads, circuits, settlement, record dates, free float, rights
issues, OFS/delisting and surveillance) into _data/jargon_m7.yml.

WHY: the posts render numbers from that YAML via Liquid, never inline, so a
figure in a table always matches the same figure in the text and a correction
happens in one place. Nothing in jargon_m7.yml is typed by hand — re-run this.

    python3 scripts/derive_jargon_m7.py

INPUTS (all already committed, all read-only here):
  assets/data/britannia-ohlcv-2024-04-to-2026-03.csv   Yahoo Finance BRITANNIA.NS daily, UNADJUSTED
                                                       close (30 Jun 2025 close 5851 = real_company.yml)
  assets/data/nifty50-price-index.csv                  Yahoo Finance ^NSEI daily close (price index)
  _data/case_study.yml, _data/case_study_2.yml         Desi Bites (fictional)
  _data/real_company.yml                               Britannia FY25 + 30 Jun 2025 price

REPORTED FIGURES typed once below, each with its primary source:
  * Britannia final dividend for FY 2024-25: Rs 75/share, record date Monday
    4 August 2025, AGM 11 August 2025 — Britannia Annual Report 2024-25,
    Board's report ("Dividend") and General Shareholder Information,
    https://media.britannia.co.in/B_Il_Annual_Report_for_FY_2024_25_b6d95d1717.pdf
    and Britannia's Board-outcome letter to BSE/NSE of 8 May 2025,
    https://media.britannia.co.in/Intimation_of_Final_Dividend_pdf_43b8412ff2.pdf
  * Britannia final dividend for FY 2023-24: Rs 73.50/share (real_company.yml),
    record date Monday 5 August 2024, AGM 12 August 2024 — Notice of the 105th
    AGM, https://media.britannia.co.in/Notice_of_105th_Annual_General_Meeting_pdf_8f7245e7e5.pdf
  * NSE's corporate-actions data for BRITANNIA shows ex-date = record date for
    both (T+1), and ex 26 Aug 2020 / record 27 Aug 2020 for the Rs 83 interim (T+2).
  * Britannia promoter and promoter group holding at 31 March 2025:
    12,17,52,892 of 24,08,68,296 shares (50.55%) — same Annual Report,
    standalone Note 18(d) "Details of shareholding of Promoters".
  Regulatory thresholds (price bands, MWCB levels, delisting/OFS thresholds)
  are typed in the `rules` blocks with the circular they come from.

EVERYTHING ELSE for Desi Bites is a HYPOTHETICAL scenario invented here (an
order book, a price band, a rights issue, an OFS, a reverse book-building
bid ladder). None of it changes case_study.yml / case_study_2.yml; it borrows
their share count, promoter holding and listing price only.

LAG CHECK: every market series ends 30 March 2026; the earliest M7 post
publishes 14 October 2026. The Britannia dividend events are August 2024 and
August 2025. All comfortably past the 3-month rule.

Needs pandas, numpy, pyyaml.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "jargon_m7.yml"

cs = yaml.safe_load((ROOT / "_data" / "case_study.yml").read_text())
cs2 = yaml.safe_load((ROOT / "_data" / "case_study_2.yml").read_text())
rc = yaml.safe_load((ROOT / "_data" / "real_company.yml").read_text())

brit = pd.read_csv(ROOT / "assets/data/britannia-ohlcv-2024-04-to-2026-03.csv", parse_dates=["date"]).set_index("date")
nifty = pd.read_csv(ROOT / "assets/data/nifty50-price-index.csv", parse_dates=["date"]).set_index("date")["nifty50_pri_close"]

lst = cs["listing"]
sh = cs2["shareholding"]
SHARES_LAKH = lst["post_ipo_shares_lakh"]          # 12.5
PROMOTER_LAKH = sh["promoter_shares_lakh"]          # 10
PUBLIC_LAKH = sh["public_shares_lakh"]              # 2.5
assert abs(PROMOTER_LAKH + PUBLIC_LAKH - SHARES_LAKH) < 1e-9


def r2(x):
    return float(round(float(x), 2))


def r1(x):
    return float(round(float(x), 1))


def d(ts):
    return str(pd.Timestamp(ts).date())


# ======================================================== 1. bid-ask spread
# A HYPOTHETICAL Desi Bites order book (price, shares). Best five each side.
BIDS = [(628.0, 150), (625.0, 200), (620.0, 400), (615.0, 300), (610.0, 500)]
ASKS = [(632.0, 100), (636.0, 250), (640.0, 300), (648.0, 500), (655.0, 400)]
assert all(BIDS[i][0] > BIDS[i + 1][0] for i in range(len(BIDS) - 1))
assert all(ASKS[i][0] < ASKS[i + 1][0] for i in range(len(ASKS) - 1))
best_bid, best_ask = BIDS[0][0], ASKS[0][0]
mid = (best_bid + best_ask) / 2
spread = best_ask - best_bid


def walk(book, qty):
    """Fill a market order of qty shares against book; return fills and avg price."""
    left, fills = qty, []
    for p, q in book:
        take = min(left, q)
        if take > 0:
            fills.append({"price": p, "shares": take, "value": r2(p * take)})
            left -= take
    assert left == 0, "order larger than the visible book"
    val = sum(f["price"] * f["shares"] for f in fills)
    return fills, val / qty, val


def impact_block(book, qty, side):
    fills, avg, val = walk(book, qty)
    sign = 1 if side == "buy" else -1
    ic = sign * (avg - mid) / mid * 100
    return {"side": side, "shares": qty, "fills": fills, "avg_price": r2(avg), "value": r2(val),
            "impact_cost_pct": r2(ic), "cost_vs_mid_rupees": r2(sign * (avg - mid) * qty)}


buy_small = impact_block(ASKS, 100, "buy")
buy_big = impact_block(ASKS, 600, "buy")
sell_big = impact_block(BIDS, 600, "sell")
assert buy_small["avg_price"] == best_ask
# round trip on 600 shares: buy then immediately sell, at these books
rt_loss = buy_big["value"] - sell_big["value"]

# Britannia: observed daily traded value, FY26 (NSE volume on Yahoo x close)
fy26 = brit.loc["2025-04-01":"2026-03-31"]
zero_vol = int((fy26["volume"] == 0).sum())   # data gaps (holiday rows with no NSE volume)
fy26 = fy26[fy26["volume"] > 0]
tv_cr = fy26["close"] * fy26["volume"] / 1e7
spread_ask = {
    "book": {"bids": [{"price": p, "shares": q} for p, q in BIDS], "asks": [{"price": p, "shares": q} for p, q in ASKS]},
    "best_bid": best_bid, "best_ask": best_ask, "mid": r2(mid), "spread": r2(spread),
    "spread_pct_of_mid": r2(spread / mid * 100),
    "buy_small": buy_small, "buy_big": buy_big, "sell_big": sell_big,
    "round_trip_loss": r2(rt_loss),
    "round_trip_loss_pct": r2(rt_loss / buy_big["value"] * 100),
    "visible_ask_shares": sum(q for _, q in ASKS),
    "visible_ask_value_lakh": r2(sum(p * q for p, q in ASKS) / 1e5),
    "big_order_pct_of_visible_asks": r1(buy_big["shares"] / sum(q for _, q in ASKS) * 100),
    "britannia": {
        "window": "1 April 2025 – 30 March 2026",
        "sessions": int(len(fy26)),
        "median_daily_value_cr": r1(tv_cr.median()),
        "p10_daily_value_cr": r1(tv_cr.quantile(0.10)),
        "p90_daily_value_cr": r1(tv_cr.quantile(0.90)),
        "zero_volume_rows_dropped": zero_vol,
        "median_daily_shares": int(fy26["volume"].median()),
        "note": "NSE volume only (Yahoo Finance BRITANNIA.NS); BSE volume is extra.",
    },
}

# ======================================================== 2. circuits
PREV_CLOSE = 630.0          # hypothetical Desi Bites previous close
BANDS = [2, 5, 10, 20]
circuit = {
    "desi_prev_close": PREV_CLOSE,
    "desi_bands": [{"band_pct": b, "upper": r2(PREV_CLOSE * (1 + b / 100)), "lower": r2(PREV_CLOSE * (1 - b / 100))} for b in BANDS],
}
# MWCB — trigger levels computed on the last close in the dataset (illustration)
last_close_date = nifty.index[-1]
last_close = float(nifty.iloc[-1])
circuit["mwcb_base_date"] = d(last_close_date)
circuit["mwcb_base_close"] = r2(last_close)
circuit["mwcb_levels"] = [{"fall_pct": p, "trigger_level": r2(last_close * (1 - p / 100)), "points": r2(last_close * p / 100)} for p in (10, 15, 20)]
# March 2020 observables from the close series
m20 = {}
for day in ("2020-03-13", "2020-03-23"):
    i = nifty.index.get_loc(pd.Timestamp(day))
    prev, close = float(nifty.iloc[i - 1]), float(nifty.iloc[i])
    m20[day] = {"date": day, "prev_date": d(nifty.index[i - 1]), "prev_close": r2(prev), "close": r2(close),
                "close_change_pct": r2((close / prev - 1) * 100),
                "ten_pct_trigger": r2(prev * 0.9), "fifteen_pct_trigger": r2(prev * 0.85)}
assert m20["2020-03-23"]["close"] < m20["2020-03-23"]["ten_pct_trigger"]      # closed below the 10% level
assert m20["2020-03-23"]["close"] > m20["2020-03-23"]["fifteen_pct_trigger"]  # but above 15%
assert m20["2020-03-13"]["close"] > m20["2020-03-13"]["prev_close"]           # 13 Mar closed UP
circuit["march_2020"] = m20

# ======================================================== 3/4. settlement + ex-date (Britannia)
days = brit.index


def next_session(ts):
    return days[days.searchsorted(pd.Timestamp(ts), side="right")]


def prev_session(ts):
    return days[days.searchsorted(pd.Timestamp(ts), side="left") - 1]


DIVS = [
    {"label": "Final dividend for FY 2024-25", "dps": rc["market"]["dividend_per_share_fy25_declared"], "record_date": "2025-08-04",
     "source": "https://media.britannia.co.in/Intimation_of_Final_Dividend_pdf_43b8412ff2.pdf",
     "board_date": "2025-05-08", "agm_date": "2025-08-11", "paid_by": "2025-09-09"},
    {"label": "Final dividend for FY 2023-24", "dps": rc["market"]["dividend_per_share_fy25"], "record_date": "2024-08-05", "board_date": "2024-05-03", "agm_date": "2024-08-12", "paid_by": "2024-09-10",
     "source": "https://media.britannia.co.in/Notice_of_105th_Annual_General_Meeting_pdf_8f7245e7e5.pdf"},
]
exdiv = []
for dv in DIVS:
    ex = pd.Timestamp(dv["record_date"])     # T+1: ex-date = record date
    assert ex in days
    cum = prev_session(ex)
    pc = float(brit.loc[cum, "close"])
    o = float(brit.loc[ex, "open"])
    c = float(brit.loc[ex, "close"])
    n_prev, n_ex = float(nifty.loc[cum]), float(nifty.loc[ex])
    exdiv.append({
        "label": dv["label"], "dps": dv["dps"], "dps_display": f'{dv["dps"]:.2f}'.replace(".00", ""), "source": dv["source"],
        "board_date": dv["board_date"], "agm_date": dv["agm_date"], "paid_by": dv["paid_by"],
        "record_date": d(ex), "ex_date": d(ex), "last_cum_date": d(cum),
        "cum_close": r2(pc), "ex_open": r2(o), "ex_close": r2(c),
        "dividend_pct_of_cum_close": r2(dv["dps"] / pc * 100),
        "expected_ex_price": r2(pc - dv["dps"]),
        "open_gap": r2(o - pc), "open_gap_pct": r2((o / pc - 1) * 100),
        "close_change": r2(c - pc), "close_change_pct": r2((c / pc - 1) * 100),
        "total_return_pct": r2((c + dv["dps"]) / pc * 100 - 100),
        "nifty_change_pct": r2((n_ex / n_prev - 1) * 100),
    })
# how big is an ordinary day's move? FY26 daily close-to-close standard deviation
dstd = brit.loc["2025-04-01":"2026-03-31", "close"].pct_change().dropna().std() * 100
exdiv_noise = {"daily_sd_pct_fy26": r2(dstd)}
# T+1 calendar on the FY25 record date: last day to buy and be on the register
rec = pd.Timestamp(DIVS[0]["record_date"])
buy_ok = prev_session(rec)
settlement = {
    "record_date": d(rec),
    "last_buy_date_entitled": d(buy_ok),
    "settles_on": d(next_session(buy_ok)),
    "buy_on_record_date_settles": d(next_session(rec)),
    "t_plus_2_last_buy": d(prev_session(prev_session(rec))),
}
assert settlement["settles_on"] == settlement["record_date"]
# Under T+2 the ex-date came one business day BEFORE the record date. Britannia's
# interim dividend of Rs 83 in 2020: ex-date Wed 26 Aug 2020, record date Thu
# 27 Aug 2020 (NSE corporate actions, symbol BRITANNIA). Reported, no prices used.
settlement["t2_example"] = {"dps": 83.0, "ex_date": "2020-08-26", "record_date": "2020-08-27",
                            "source": "https://www.nseindia.com/companies-listing/corporate-filings-actions"}

# ======================================================== 5. free float
mk = rc["market"]
BRIT_PROMOTER_SHARES = 121752892          # Annual Report FY25, Note 18(d)
BRIT_TOTAL_SHARES = 240868296             # same, Note 18(c)
bp = BRIT_PROMOTER_SHARES / BRIT_TOTAL_SHARES * 100
assert abs(bp - 50.55) < 0.005
db_full = lst["market_cap"]
db_ff = db_full * PUBLIC_LAKH / SHARES_LAKH
# Two hypothetical companies with the same full market cap, different floats
twins = [
    {"company": "Company P (widely held)", "full_mcap": 1000, "free_float_pct": 90},
    {"company": "Company Q (promoter-heavy)", "full_mcap": 1000, "free_float_pct": 30},
]
tot = sum(t["full_mcap"] * t["free_float_pct"] / 100 for t in twins)
for t in twins:
    t["ff_mcap"] = r1(t["full_mcap"] * t["free_float_pct"] / 100)
    t["weight_full_pct"] = r1(t["full_mcap"] / sum(x["full_mcap"] for x in twins) * 100)
    t["weight_ff_pct"] = r1(t["ff_mcap"] / tot * 100)
free_float = {
    "desi": {"shares_lakh": SHARES_LAKH, "promoter_lakh": PROMOTER_LAKH, "public_lakh": PUBLIC_LAKH,
             "promoter_pct": sh["promoter_pct"], "public_pct": sh["public_pct"], "as_of": sh["as_of"],
             "price": lst["ipo_price"], "full_mcap_lakh": db_full, "ff_mcap_lakh": r2(db_ff),
             "mps_shortfall_shares": int(round((SHARES_LAKH * 0.25 - PUBLIC_LAKH) * 1e5))},
    "britannia": {"promoter_shares": BRIT_PROMOTER_SHARES, "total_shares": BRIT_TOTAL_SHARES,
                  "promoter_pct": r2(bp), "non_promoter_pct": r2(100 - bp),
                  "price": mk["price"], "price_date": mk["price_date"], "full_mcap_cr": r2(mk["market_cap_cr"]),
                  "ff_mcap_cr": r2(mk["market_cap_cr"] * (100 - bp) / 100),
                  "source": "https://media.britannia.co.in/B_Il_Annual_Report_for_FY_2024_25_b6d95d1717.pdf"},
    "twins": twins,
}

# ======================================================== 6. rights issue (FICTIONAL)
R_NEW, R_HELD = 1, 5              # 1 rights share for every 5 held
R_PRICE = 480.0                   # issue price
CUM = 600.0                       # hypothetical market price just before the ex-rights date
rights_shares = SHARES_LAKH * R_NEW / R_HELD
terp = (R_HELD * CUM + R_NEW * R_PRICE) / (R_HELD + R_NEW)
re_value = terp - R_PRICE
HOLD = 100
ent = HOLD * R_NEW / R_HELD
pat26 = cs2["fy26"]["pat"]
opts = [
    {"option": "Subscribe (pay for the rights shares)", "cash_paid": r2(ent * R_PRICE), "cash_received": 0.0, "shares_after": HOLD + ent},
    {"option": "Renounce (sell the REs at their theoretical value)", "cash_paid": 0.0, "cash_received": r2(ent * re_value), "shares_after": HOLD},
    {"option": "Do nothing (let the REs lapse)", "cash_paid": 0.0, "cash_received": 0.0, "shares_after": HOLD},
]
for o in opts:
    o["holding_value"] = r2(o["shares_after"] * terp)
    o["net_wealth_change"] = r2(o["holding_value"] + o["cash_received"] - o["cash_paid"] - HOLD * CUM)
assert abs(opts[0]["net_wealth_change"]) < 0.01 and abs(opts[1]["net_wealth_change"]) < 0.01
rights = {
    "ratio_new": R_NEW, "ratio_held": R_HELD, "issue_price": R_PRICE, "cum_price": CUM,
    "discount_pct": r1((1 - R_PRICE / CUM) * 100),
    "shares_before_lakh": SHARES_LAKH, "rights_shares_lakh": r2(rights_shares), "shares_after_lakh": r2(SHARES_LAKH + rights_shares),
    "raise_lakh": r2(rights_shares * R_PRICE),   # lakh shares x Rs = Rs lakh
    "terp": r2(terp), "re_value": r2(re_value),
    "holder_shares": HOLD, "holder_entitlement": int(ent), "holder_value_before": r2(HOLD * CUM),
    "stake_shrink_if_not_subscribing_pct": r1((1 - SHARES_LAKH / (SHARES_LAKH + rights_shares)) * 100),
    "options": opts,
    "fy26_pat_lakh": pat26, "eps_before": r2(pat26 / SHARES_LAKH), "eps_after_same_pat": r2(pat26 / (SHARES_LAKH + rights_shares)),
    "promoter_rights_lakh": r2(PROMOTER_LAKH * R_NEW / R_HELD),
    "note": "Fictional terms for teaching. Desi Bites has announced no rights issue; its FY26 cash pile means it would not need one.",
}

# ======================================================== 7. OFS vs fresh issue, delisting (FICTIONAL)
ipo_p = lst["ipo_price"]
fresh = lst["fresh_issue_shares_lakh"]
half = fresh / 2
ofs_compare = [
    {"structure": "As it happened: 100% fresh issue", "new_shares_lakh": fresh, "ofs_shares_lakh": 0.0},
    {"structure": "Hypothetical: half fresh, half OFS", "new_shares_lakh": half, "ofs_shares_lakh": half},
    {"structure": "Hypothetical: 100% OFS", "new_shares_lakh": 0.0, "ofs_shares_lakh": fresh},
]
for r in ofs_compare:
    r["to_company_lakh"] = r2(r["new_shares_lakh"] * ipo_p)
    r["to_sellers_lakh"] = r2(r["ofs_shares_lakh"] * ipo_p)
    r["shares_after_lakh"] = r2(lst["pre_ipo_shares_lakh"] + r["new_shares_lakh"])
    r["promoter_after_lakh"] = r2(lst["pre_ipo_shares_lakh"] - r["ofs_shares_lakh"])
    r["promoter_after_pct"] = r1(r["promoter_after_lakh"] / r["shares_after_lakh"] * 100)
assert ofs_compare[0]["to_company_lakh"] == lst["ipo_proceeds"]

# Reverse book building on a hypothetical delisting offer by Desi Bites' promoter
FLOOR = 650.0
LADDER = [  # (bid price, public shares in lakh tendered at that price)
    (650.0, 0.20), (700.0, 0.30), (750.0, 0.35), (800.0, 0.30), (850.0, 0.25), (900.0, 0.40), (1000.0, 0.30),
]
not_tendered = PUBLIC_LAKH - sum(q for _, q in LADDER)
assert not_tendered > 0
need = SHARES_LAKH * 0.90 - PROMOTER_LAKH
cum_q, ladder, discovered = 0.0, [], None
for p, q in LADDER:
    cum_q += q
    post = (PROMOTER_LAKH + cum_q) / SHARES_LAKH * 100
    ladder.append({"price": p, "shares_lakh": q, "cumulative_lakh": r2(cum_q), "acquirer_pct_if_accepted": r1(post)})
    if discovered is None and cum_q + 1e-9 >= need:
        discovered = p
assert discovered is not None
delist = {
    "floor_price": FLOOR, "promoter_pct": sh["promoter_pct"], "threshold_pct": 90,
    "shares_needed_lakh": r2(need), "ladder": ladder, "not_tendered_lakh": r2(not_tendered),
    "discovered_price": discovered, "premium_to_floor_pct": r1((discovered / FLOOR - 1) * 100),
    "tendered_lakh": r2(sum(q for _, q in LADDER)),
}
# Shares tendered at or below the discovered price are accepted and all paid the
# discovered price (Delisting Regs 2021, reg 21: bids "accepted as eligible bids at
# the discovered price"); bids above it are not accepted.
acc = sum(q for p, q in LADDER if p <= discovered)
delist["accepted_lakh"] = r2(acc)
delist["cost_at_discovered_lakh"] = r2(discovered * acc)
delist["acquirer_after_pct"] = r1((PROMOTER_LAKH + acc) / SHARES_LAKH * 100)
delist["remaining_public_lakh"] = r2(PUBLIC_LAKH - acc)
assert delist["acquirer_after_pct"] >= 90
# Hypothetical promoter OFS through the stock-exchange mechanism to restore 25%
# minimum public shareholding. Framework: SEBI/HO/MRD/MRD-PoD-3/P/CIR/2023/10
# (10 Jan 2023): min size Rs 25 cr EXCEPT a promoter reaching MPS in a single
# tranche (para 3.0); >=25% reserved for MFs/insurers (7.1); >=10% for retail (7.2).
OFS_FLOOR = 600.0
ofs_sh = int(round((SHARES_LAKH * 0.25 - PUBLIC_LAKH) * 1e5))
ex_ofs = {
    "shares": ofs_sh, "floor_price": OFS_FLOOR, "size_lakh": r2(ofs_sh * OFS_FLOOR / 1e5),
    "size_cr": r2(ofs_sh * OFS_FLOOR / 1e7), "min_size_cr": 25,
    "retail_min_shares": int(ofs_sh * 0.10), "mf_ins_min_shares": int(ofs_sh * 0.25),
    "promoter_after_lakh": round(PROMOTER_LAKH - ofs_sh / 1e5, 3),
    "promoter_after_pct": r1((PROMOTER_LAKH - ofs_sh / 1e5) / SHARES_LAKH * 100),
    "public_after_pct": r1((PUBLIC_LAKH + ofs_sh / 1e5) / SHARES_LAKH * 100),
    "shares_total_lakh_unchanged": SHARES_LAKH,
    "desi_mcap_cr": r2(lst["market_cap"] / 100), "ofs_mcap_threshold_cr": 1000,
}
assert ex_ofs["public_after_pct"] == 25.0 and ex_ofs["size_cr"] < 25
ofs = {"ipo_price": ipo_p, "ipo_compare": ofs_compare, "exchange_ofs": ex_ofs, "delist": delist}

# ======================================================== 8. surveillance (hypothetical trade)
# Capital a buyer must put up for a Rs 1 lakh purchase under each GSM stage.
# Stage rules: NSE GSM FAQ v1.1 (June 2026), Q4 — Stage I 100% margin, 5% band;
# Stage II trade-for-trade + Additional Surveillance Deposit (ASD) of 50% of trade
# value; Stage III ASD 100%, trading once a week; Stage IV as III, no upward move.
TRADE = 100000.0
GSM = [
    ("Stage I", 100, 0, "Every day", "5% or lower"),
    ("Stage II", 100, 50, "Every day, trade-for-trade", "5% or lower"),
    ("Stage III", 100, 100, "Once a week (Monday), trade-for-trade", "5% or lower"),
    ("Stage IV", 100, 100, "Once a week (Monday), trade-for-trade", "5% or lower, no upward movement"),
]
gsm = []
for st, marg, asd, when, band in GSM:
    gsm.append({"stage": st, "margin_pct": marg, "asd_pct": asd, "trading": when, "band": band,
                "margin_rs": r2(TRADE * marg / 100), "asd_rs": r2(TRADE * asd / 100),
                "total_locked_rs": r2(TRADE * (marg + asd) / 100)})
surv = {"trade_value": TRADE, "gsm": gsm, "max_daily_move_5pct_rs": r2(TRADE * 0.05),
        "desi_mcap_cr": r2(lst["market_cap"] / 100), "esm_mcap_limit_cr": 1000,
        "esm_launch_mcap_limit_cr": 500}
assert surv["desi_mcap_cr"] < surv["esm_mcap_limit_cr"]

out = {
    "_meta": {
        "generated_by": "scripts/derive_jargon_m7.py — do not edit by hand, re-run the script",
        "market_data_end": d(brit.index[-1]),
        "lag_note": "All series end March 2026 or earlier; first M7 post publishes 2026-10-14.",
    },
    "spread": spread_ask, "circuit": circuit, "settlement": settlement, "exdiv": exdiv, "exdiv_noise": exdiv_noise,
    "free_float": free_float, "rights": rights, "ofs": ofs, "surveillance": surv,
}


def _py(o):
    if isinstance(o, dict):
        return {k: _py(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_py(v) for v in o]
    if isinstance(o, (float, np.floating)):
        # whole numbers print without a trailing ".0" (no false precision in posts)
        return int(o) if float(o).is_integer() else float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


OUT.write_text(
    "# GENERATED by scripts/derive_jargon_m7.py — every figure used by the Jargon,\n"
    "# Decoded Module 7 (market mechanics) posts. Do not edit by hand; change the\n"
    "# script and re-run. Sources and the lag check are in the script header.\n"
    + yaml.safe_dump(_py(out), sort_keys=False, allow_unicode=True, width=120)
)
print(f"wrote {OUT.relative_to(ROOT)}")
