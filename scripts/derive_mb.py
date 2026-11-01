#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build _data/market_basics.yml — figures for the "Your first year in the market"
series. Rules are typed ONCE here with the primary source beside them (opened
1 November 2026); worked examples are computed here from generic/illustrative
inputs. Re-run, never hand-edit the YAML:

    python3 scripts/derive_mb.py

Illustrative order-book prices are HYPOTHETICAL (not market data). They sit
around Desi Bites' fictional Rs 640 IPO price (_data/case_study.yml).

PRIMARY SOURCES
  BSDA: SEBI circular SEBI/HO/MIRSD/MIRSD-PoD1/P/CIR/2024/91, 28 June 2024
        https://www.sebi.gov.in/legal/circulars/jun-2024/facility-for-basic-services-demat-account-bsda-for-financial-inclusion-and-ease-of-investing_84470.html
        as amended by SEBI circular HO/38/11/11(3)2025-MIRSD-POD/I/1101/2025, 24 December 2025
        https://www.sebi.gov.in/legal/circulars/dec-2025/ease-of-investments-and-ease-of-doing-business-measures-enhancing-the-facility-for-basic-services-demat-account-bsda-_98667.html
  Nomination: SEBI circular SEBI/HO/OIAE/OIAE_IAD-3/P/CIR/2026/12676, 29 May 2026
        https://www.sebi.gov.in/legal/circulars/may-2026/ease-of-doing-investments-modified-norms-for-nomination-in-demat-accounts-and-mutual-fund-folios_101703.html
  Order types: NSE, equity market trading system page (updated 28/02/2024)
        https://www.nseindia.com/static/products-services/equity-market-trading-system
  Pre-open: NSE page (updated 04/09/2026)
        https://www.nseindia.com/static/products-services/equity-market-pre-open
  Depositories: SEBI investor site https://investor.sebi.gov.in/depositories.html ;
        CDSL FAQ https://www.cdslindia.com/downloads/Investors/FAQs/01%20Demat%20CDSL%20Way%20-%20I%20-%20General%20%20-%202024.pdf
"""
import os

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_data", "market_basics.yml")

# ---- BSDA (rules as printed) ----
BSDA = dict(
    as_of="November 2026",
    circular_2024="SEBI/HO/MIRSD/MIRSD-PoD1/P/CIR/2024/91, 28 June 2024 (effective 1 September 2024)",
    circular_2025="HO/38/11/11(3)2025-MIRSD-POD/I/1101/2025, 24 December 2025 (effective 31 March 2026)",
    url_2024="https://www.sebi.gov.in/legal/circulars/jun-2024/facility-for-basic-services-demat-account-bsda-for-financial-inclusion-and-ease-of-investing_84470.html",
    url_2025="https://www.sebi.gov.in/legal/circulars/dec-2025/ease-of-investments-and-ease-of-doing-business-measures-enhancing-the-facility-for-basic-services-demat-account-bsda-_98667.html",
    limit_lakh=10,           # value of securities must not exceed Rs 10 lakh at any point
    free_up_to_lakh=4,       # AMC nil up to Rs 4 lakh
    max_amc_rs=100,          # max annual maintenance charge, more than 4 lakh up to 10 lakh
    statement_fee_max_rs=25, # physical statement
)
# illustrative holdings (hypothetical)
BSDA_EXAMPLES = [3, 7, 12]    # Rs lakh


def bsda_status(v):
    if v <= BSDA["free_up_to_lakh"]:
        return dict(holding_lakh=v, status="BSDA eligible", max_amc="Nil")
    if v <= BSDA["limit_lakh"]:
        return dict(holding_lakh=v, status="BSDA eligible", max_amc="Up to ₹%d a year" % BSDA["max_amc_rs"])
    return dict(holding_lakh=v, status="Above the BSDA limit", max_amc="Regular AMC may be charged")


# ---- Nomination ----
NOM = dict(
    as_of="November 2026",
    circular="SEBI/HO/OIAE/OIAE_IAD-3/P/CIR/2026/12676, 29 May 2026",
    url="https://www.sebi.gov.in/legal/circulars/may-2026/ease-of-doing-investments-modified-norms-for-nomination-in-demat-accounts-and-mutual-fund-folios_101703.html",
    effective="1 September 2026",
    max_nominees=3,
)


def split_equal(units, n):
    base, rem = divmod(units, n)
    shares = [base] * n
    shares[0] += rem          # circular: odd lot goes to the first nominee named
    assert sum(shares) == units
    return shares


NOM_EXAMPLE_UNITS = 100
NOM_EXAMPLE_SPLIT = split_equal(NOM_EXAMPLE_UNITS, NOM["max_nominees"])
NOM_PCT_EXAMPLE = dict(units=200, pcts=[50, 30, 20])
NOM_PCT_SHARES = [NOM_PCT_EXAMPLE["units"] * p // 100 for p in NOM_PCT_EXAMPLE["pcts"]]
assert sum(NOM_PCT_SHARES) == NOM_PCT_EXAMPLE["units"] and sum(NOM_PCT_EXAMPLE["pcts"]) == 100

# ---- Order types: hypothetical sell-side queue (price, quantity) ----
LISTING_PRICE = 640     # case_study.yml listing.ipo_price (fictional)
ASKS = [(641, 100), (642, 200), (645, 300), (650, 400)]
BUY_QTY = 400


def fill_market(qty, asks):
    left, cost, fills = qty, 0, []
    for p, q in asks:
        t = min(left, q)
        if t:
            fills.append(dict(price=p, qty=t))
            cost += p * t
            left -= t
    return fills, cost, qty - left


def fill_limit(qty, limit, asks):
    return fill_market(qty, [(p, q) for p, q in asks if p <= limit])


mk_fills, mk_cost, mk_qty = fill_market(BUY_QTY, ASKS)
assert mk_qty == BUY_QTY
LIMIT_PX = 642
lm_fills, lm_cost, lm_qty = fill_limit(BUY_QTY, LIMIT_PX, ASKS)
SL = dict(trigger=650, limit=652, ltp_before=641)

ORDERS = dict(
    note="HYPOTHETICAL order book around Desi Bites' fictional listing price; not market data.",
    asks=[dict(price=p, qty=q) for p, q in ASKS],
    buy_qty=BUY_QTY,
    market=dict(fills=mk_fills, cost=mk_cost, qty=mk_qty, avg=round(mk_cost / mk_qty, 2),
                best_ask=ASKS[0][0], slippage_rs=round(mk_cost / mk_qty - ASKS[0][0], 2)),
    limit=dict(limit=LIMIT_PX, fills=lm_fills, cost=lm_cost, qty=lm_qty,
               avg=round(lm_cost / lm_qty, 2), unfilled=BUY_QTY - lm_qty),
    stop_loss=SL,
    listing_price=LISTING_PRICE,
)

NSE = dict(
    trading_url="https://www.nseindia.com/static/products-services/equity-market-trading-system",
    preopen_url="https://www.nseindia.com/static/products-services/equity-market-pre-open",
    trading_page_updated="28 February 2024", preopen_page_updated="4 September 2026",
    preopen_window="9:00 am to 9:15 am", normal_close="3:30 pm", normal_open="9:15 am",
)

out = dict(bsda=dict(BSDA, examples=[bsda_status(v) for v in BSDA_EXAMPLES]),
           nomination=dict(NOM, example_units=NOM_EXAMPLE_UNITS, example_split=NOM_EXAMPLE_SPLIT,
                           pct_example=dict(NOM_PCT_EXAMPLE, shares=NOM_PCT_SHARES)),
           orders=ORDERS, nse=NSE)

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("# GENERATED by scripts/derive_mb.py — do not edit by hand.\n")
    yaml.safe_dump(out, fh, sort_keys=False, allow_unicode=True, width=100)
print("wrote", OUT)
print(ORDERS["market"], ORDERS["limit"], NOM_EXAMPLE_SPLIT, NOM_PCT_SHARES, out["bsda"]["examples"])
