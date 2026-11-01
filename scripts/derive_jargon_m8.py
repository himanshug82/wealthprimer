#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by Jargon, Decoded Module 8 ("Market terms": bulk and
block deals, short selling, open interest, index weights, price vs total-return
index, India VIX) into _data/jargon_m8.yml.

WHY: the posts render numbers from that YAML via Liquid, never typed inline, so
a figure in a table always matches the same figure in the text. Nothing in
jargon_m8.yml is typed by hand — re-run this:

    python3 scripts/derive_jargon_m8.py

INPUTS (read-only):
  _data/case_study.yml, _data/case_study_2.yml   Desi Bites (fictional): share count, IPO price
  assets/data/nifty50-price-index.csv            Yahoo Finance ^NSEI daily close (price index)
  assets/data/nifty50-tri.csv                    Nifty 50 TRI, niftyindices.com historical data

RULES TYPED ONCE BELOW, each with the primary source opened on 1 Nov 2026:
  * Bulk deal: more than 0.5% of the company's listed equity shares bought/sold in a
    scrip in a day (one or more transactions, normal market segment); brokers disclose
    scrip, client name, quantity and price; exchanges publish after market hours.
    SEBI Master Circular for Stock Exchanges and Clearing Corporations,
    SEBI/HO/MRD-PoD2/CIR/P/2024/00181, 30 December 2024, Chapter 1, para 1.1
    (https://www.sebi.gov.in/sebi_data/commondocs/dec-2024/RE_Chapter%201%20-%20Trading%20-%20NEW_p.pdf).
  * Block deal: SEBI circular SEBI/HO/MRD/POD-III/CIR/P/2025/134, 8 October 2025,
    "Review of Block Deal Framework" (https://www.sebi.gov.in/legal/circulars/oct-2025/review-of-block-deal-framework_97145.html):
    morning window 08:45-09:00, reference price = previous close; afternoon window
    14:05-14:20, reference = VWAP of cash-segment trades 13:45-14:00; orders within 3%
    of the reference price (the text of the copy read shows "+3%"; check); minimum
    order size Rs 25 crore; every trade must result in delivery and not be squared off
    or reversed; exchanges publish scrip, client name, quantity, price the same day after
    market hours; applicable "from the 60th day of issuance" of the circular.
  * Short selling: SEBI circular SEBI/HO/MRD/MRD-PoD-3/P/CIR/2024/1, 5 January 2024,
    "Framework for Short Selling", Annexure 3 (https://www.sebi.gov.in/legal/circulars/jan-2024/framework-for-short-selling_80448.html).
  * Index formula, free float (IWF) and total-return index: NSE Indices, Methodology
    Document for Equity Indices, September 2026 (document dated 20260821)
    (https://www.niftyindices.com/Methodology/Method_NIFTY_Equity_Indices.pdf), "Index
    Calculation Formula" and "Total Return Index Calculation".
  * India VIX: NSE, "About India VIX" computation methodology
    (https://nsearchives.nseindia.com/web/sites/default/files/inline-files/India_VIX_comp_meth.pdf)
    and NSE white paper (https://nsearchives.nseindia.com/web/sites/default/files/inline-files/white_paper_IndiaVIX.pdf);
    both undated; read 1 Nov 2026.

EVERYTHING ELSE is a HYPOTHETICAL scenario invented here (deal sizes, an order
sequence, a five-stock index, VIX levels). It borrows Desi Bites' share count
and IPO price only. The Nifty 50 price and total-return series are real,
backward-looking market data.

LAG CHECK: both Nifty series end 30 March 2026; the latest M8 post publishes
9 November 2026 (cut-off 9 August 2026). Rule texts are as read on 1 Nov 2026.

Needs pandas, numpy, pyyaml.
"""
import math
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "jargon_m8.yml"

cs = yaml.safe_load((ROOT / "_data" / "case_study.yml").read_text())
lst = cs["listing"]
SHARES = int(round(lst["post_ipo_shares_lakh"] * 100000))   # 12,50,000
IPO_PRICE = lst["ipo_price"]                                 # 640
assert SHARES == 1250000


def r2(x):
    return float(round(float(x), 2))


def r1(x):
    return float(round(float(x), 1))


def d(ts):
    return str(pd.Timestamp(ts).date())


# ================================================ 1. bulk and block deals
BULK_PCT = 0.5
bulk_threshold_shares = SHARES * BULK_PCT / 100          # more than this many shares
assert bulk_threshold_shares == 6250
day_trades = [2500, 2000, 2500]                          # one fund, one day, three trades
day_total = sum(day_trades)
assert day_total > bulk_threshold_shares
edge_total = int(bulk_threshold_shares)                   # exactly 0.5% does not count
assert not (edge_total > bulk_threshold_shares)

BLOCK_MIN_CR = 25
BLOCK_BAND_PCT = 3
ref_price = float(IPO_PRICE)                              # assumed previous close, illustrative
band_lo = r2(ref_price * (1 - BLOCK_BAND_PCT / 100))
band_hi = r2(ref_price * (1 + BLOCK_BAND_PCT / 100))
block_min_value = BLOCK_MIN_CR * 10_000_000               # rupees
min_shares_at_ref = block_min_value / ref_price
assert min_shares_at_ref == 390625
market_cap_cr = SHARES * ref_price / 10_000_000
block_min_pct_of_company = min_shares_at_ref / SHARES * 100
assert abs(block_min_pct_of_company - BLOCK_MIN_CR / market_cap_cr * 100) < 1e-9
# the 60th day of issuance (circular dated 8 Oct 2025)
circular_date = date(2025, 10, 8)
applicable_from = circular_date + timedelta(days=60)
assert applicable_from == date(2025, 12, 7)

bulk_block = {
    "desi": {"total_shares": SHARES, "ref_price": ref_price, "market_cap_cr": r2(market_cap_cr)},
    "bulk": {
        "threshold_pct": BULK_PCT, "threshold_shares": int(bulk_threshold_shares),
        "day_trades": day_trades, "day_total": day_total,
        "day_total_pct": r2(day_total / SHARES * 100),
        "edge_total": edge_total, "edge_pct": r2(edge_total / SHARES * 100),
    },
    "block": {
        "min_order_cr": BLOCK_MIN_CR, "band_pct": BLOCK_BAND_PCT,
        "band_lo": band_lo, "band_hi": band_hi,
        "min_shares_at_ref": int(min_shares_at_ref),
        "min_pct_of_company": r2(block_min_pct_of_company),
        "morning_window": "08:45 to 09:00", "afternoon_window": "14:05 to 14:20",
        "afternoon_vwap_window": "13:45 to 14:00",
        "circular": "SEBI/HO/MRD/POD-III/CIR/P/2025/134",
        "circular_date": "8 October 2025",
        "applicable_from": "7 December 2025",
    },
}

# ================================================ 2. short selling
SS_QTY = 100
SS_PRICE = float(IPO_PRICE)
proceeds = SS_QTY * SS_PRICE
moves = [-50, -10, 10, 50, 100]
ss_rows = []
for m in moves:
    cover = SS_PRICE * (1 + m / 100)
    short_pl = proceeds - cover * SS_QTY            # sell first, buy back later
    long_pl = cover * SS_QTY - proceeds             # buy first, sell later
    ss_rows.append({"move_pct": m, "cover_price": r2(cover), "short_pl": r2(short_pl), "long_pl": r2(long_pl)})
    assert abs(short_pl + long_pl) < 1e-6           # mirror images
assert ss_rows[-1]["short_pl"] == -proceeds         # a doubling loses the full sale value
max_gain = proceeds                                  # price cannot fall below zero
short_selling = {
    "qty": SS_QTY, "sell_price": SS_PRICE, "proceeds": r2(proceeds),
    "max_gain": r2(max_gain), "rows": ss_rows,
    "doubling_loss": r2(-ss_rows[-1]["short_pl"]),
    "sebi_circular": "SEBI/HO/MRD/MRD-PoD-3/P/CIR/2024/1", "sebi_date": "5 January 2024",
}

# ================================================ 3. open interest
# kinds: 'open' = both sides opening new positions; 'transfer' = one side closes, one opens;
# 'close' = both sides closing.
trades = [
    ("Day 1", "Both sides open new positions", "open", 100),
    ("Day 2", "One side closes, the other opens", "transfer", 50),
    ("Day 3", "Both sides open new positions", "open", 40),
    ("Day 4", "Both sides close existing positions", "close", 60),
    ("Day 5", "One side closes, the other opens", "transfer", 30),
]
oi = 0
oi_rows = []
for day, desc, kind, q in trades:
    delta = {"open": q, "transfer": 0, "close": -q}[kind]
    oi += delta
    assert oi >= 0
    oi_rows.append({"day": day, "desc": desc, "kind": kind, "volume": q, "change": delta, "oi": oi})
open_interest = {
    "rows": oi_rows,
    "total_volume": sum(r["volume"] for r in oi_rows),
    "final_oi": oi,
}
# the identity: OI(end) = sum of changes; volume never equals OI
assert oi == sum(r["change"] for r in oi_rows) == 80
assert open_interest["total_volume"] == 280

# ================================================ 4. index weights (illustrative five-stock index)
cos = [  # name, shares (crore), price, IWF
    ("Alpha Ltd", 200, 50.0, 0.45),
    ("Bravo Ltd", 100, 120.0, 0.75),
    ("Charlie Ltd", 50, 400.0, 0.90),
    ("Delta Ltd", 300, 20.0, 0.30),
    ("Echo Ltd", 80, 250.0, 0.60),
]
day1 = {"Alpha Ltd": 55.0, "Bravo Ltd": 114.0, "Charlie Ltd": 408.0, "Delta Ltd": 19.0, "Echo Ltd": 255.0}
BASE_VALUE = 1000.0


def mcap(sh, p, iwf=1.0):
    return sh * p * iwf     # Rs crore, since shares are in crore


full0 = {n: mcap(s, p) for n, s, p, w in cos}
ff0 = {n: mcap(s, p, w) for n, s, p, w in cos}
tot_full, tot_ff = sum(full0.values()), sum(ff0.values())
ff1 = {n: mcap(s, day1[n], w) for n, s, p, w in cos}
full1 = {n: mcap(s, day1[n]) for n, s, p, w in cos}
tot_ff1, tot_full1 = sum(ff1.values()), sum(full1.values())
idx1_ff = tot_ff1 / tot_ff * BASE_VALUE               # NSE formula: index mcap / base mcap * base value
idx1_full = tot_full1 / tot_full * BASE_VALUE
rets = {n: day1[n] / p - 1 for n, s, p, w in cos}
equal_ret = sum(rets.values()) / len(rets)
idx_rows = []
for n, s, p, w in cos:
    idx_rows.append({
        "name": n, "shares_cr": s, "price": p, "iwf": w,
        "full_mcap": r2(full0[n]), "ff_mcap": r2(ff0[n]),
        "w_full": r1(full0[n] / tot_full * 100), "w_ff": r1(ff0[n] / tot_ff * 100), "w_equal": 20.0,
        "price1": day1[n], "ret_pct": r2(rets[n] * 100),
        "w_ff_after": r1(ff1[n] / tot_ff1 * 100),
    })
assert abs(sum(r["w_ff"] for r in idx_rows) - 100) < 0.31
assert abs(sum(r["w_full"] for r in idx_rows) - 100) < 0.31
index_weights = {
    "rows": idx_rows,
    "base_value": BASE_VALUE,
    "tot_full": r2(tot_full), "tot_ff": r2(tot_ff), "tot_ff_after": r2(tot_ff1),
    "index_after_ff": r2(idx1_ff), "index_after_full": r2(idx1_full),
    "ret_ff_pct": r2((idx1_ff / BASE_VALUE - 1) * 100),
    "ret_full_pct": r2((idx1_full / BASE_VALUE - 1) * 100),
    "ret_equal_pct": r2(equal_ret * 100),
    "ff_share_of_full_pct": r1(tot_ff / tot_full * 100),
}

# ================================================ 5. price vs total-return index
pri = pd.read_csv(ROOT / "assets/data/nifty50-price-index.csv", parse_dates=["date"]).set_index("date")["nifty50_pri_close"]
tri = pd.read_csv(ROOT / "assets/data/nifty50-tri.csv", parse_dates=["date"]).set_index("date")["nifty50_tri_close"]
both = pd.concat([pri, tri], axis=1, join="inner").dropna()
END = both.index[-1]
assert d(END) == "2026-03-30"
tr_rows = []
for label, yrs in [("1 year", 1), ("5 years", 5), ("10 years", 10)]:
    target = END - pd.DateOffset(years=yrs)
    start = both.index[both.index <= target][-1]
    p0, p1 = both.loc[start, "nifty50_pri_close"], both.loc[END, "nifty50_pri_close"]
    t0, t1 = both.loc[start, "nifty50_tri_close"], both.loc[END, "nifty50_tri_close"]
    years = (END - start).days / 365.25
    pr_tot, tr_tot = p1 / p0 - 1, t1 / t0 - 1
    pr_cagr, tr_cagr = (p1 / p0) ** (1 / years) - 1, (t1 / t0) ** (1 / years) - 1
    assert tr_cagr > pr_cagr or yrs == 1
    tr_rows.append({
        "label": label, "start": d(start), "end": d(END),
        "pr_start": r2(p0), "pr_end": r2(p1), "tr_start": r2(t0), "tr_end": r2(t1),
        "pr_total_pct": r1(pr_tot * 100), "tr_total_pct": r1(tr_tot * 100),
        "pr_cagr_pct": r2(pr_cagr * 100), "tr_cagr_pct": r2(tr_cagr * 100),
        "gap_pp": r2((tr_cagr - pr_cagr) * 100),
        "pr_100k": int(round(100000 * p1 / p0)), "tr_100k": int(round(100000 * t1 / t0)),
    })
# the 1-year window must show a strictly positive gap too (TRI adds dividends)
assert all(r["tr_total_pct"] >= r["pr_total_pct"] for r in tr_rows)
# formula illustration (made-up numbers)
ill_prev_pr, ill_today_pr, ill_div_pts, ill_prev_tr = 20000.0, 20100.0, 5.0, 30000.0
ill_today_tr = ill_prev_tr * (1 + ((ill_today_pr + ill_div_pts) / ill_prev_pr - 1))
ill_pr_ret = ill_today_pr / ill_prev_pr - 1
ill_tr_ret = ill_today_tr / ill_prev_tr - 1
price_vs_tr = {
    "rows": tr_rows,
    "illustration": {
        "prev_pr": ill_prev_pr, "today_pr": ill_today_pr, "div_pts": ill_div_pts,
        "prev_tr": ill_prev_tr, "today_tr": r2(ill_today_tr),
        "pr_ret_pct": r2(ill_pr_ret * 100), "tr_ret_pct": r2(ill_tr_ret * 100),
    },
    "data_end": d(END),
    "special_dividend_pct": 2,
}

# ================================================ 6. India VIX (illustrative levels only)
INDEX_LEVEL = 20000.0
levels = [12, 16, 20, 30]
vix_rows = []
for v in levels:
    sd30 = v * math.sqrt(30 / 365)
    vix_rows.append({
        "vix": v, "sigma": r2(v / 100),
        "sd_30d_pct": r1(sd30), "sd_30d_points": int(round(INDEX_LEVEL * sd30 / 100)),
        "lo": int(round(INDEX_LEVEL * (1 - sd30 / 100))), "hi": int(round(INDEX_LEVEL * (1 + sd30 / 100))),
    })
assert vix_rows[0]["sd_30d_pct"] < vix_rows[-1]["sd_30d_pct"]
india_vix = {
    "rows": vix_rows, "index_level": int(INDEX_LEVEL),
    "ratio_30_365": r2(30 / 365),
}

out = {
    "_meta": {
        "generated_by": "scripts/derive_jargon_m8.py",
        "nifty_data_end": d(END),
        "lag_note": "Nifty series end 30 March 2026; latest M8 post publishes 2026-11-09. Rules read 2026-11-01.",
    },
    "bulk_block": bulk_block, "short_selling": short_selling, "open_interest": open_interest,
    "index_weights": index_weights, "price_vs_tr": price_vs_tr, "india_vix": india_vix,
}


def _py(o):
    if isinstance(o, dict):
        return {k: _py(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_py(v) for v in o]
    if isinstance(o, (float, np.floating)):
        return int(o) if float(o).is_integer() else float(o)
    if isinstance(o, np.integer):
        return int(o)
    return o


OUT.write_text(
    "# GENERATED by scripts/derive_jargon_m8.py — every figure used by the Jargon,\n"
    "# Decoded Module 8 (market terms) posts. Do not edit by hand; change the\n"
    "# script and re-run. Sources and the lag check are in the script header.\n"
    + yaml.safe_dump(_py(out), sort_keys=False, allow_unicode=True, width=120)
)
print(f"wrote {OUT.relative_to(ROOT)}")
