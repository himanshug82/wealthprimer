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
  STT: NSE circular NSE/FATAX/73524, 31 March 2026 (opened 1 Nov 2026)
        https://nsearchives.nseindia.com/content/circulars/FATAX73524.pdf
  Exchange transaction charges: NSE circular NSE/FA/64232, 27 September 2024 (in force from 1 October 2024)
        https://nsearchives.nseindia.com/content/circulars/FA64232.pdf
  SEBI turnover fee, stamp duty, GST on broker services, STT table: NSE investor page "SEBI Turnover Fees, STT and
        Other levies", updated 17/04/2026
        https://www.nseindia.com/static/invest/first-time-investor-sebi-turnover-fees-stt-other-levies
  IPO (ASBA/UPI, T+2 unblock, T+3 listing, delay compensation): SEBI master circular for the ICDR Regulations,
        HO/49/14/14(2)2026-CFD-POD2/I/4518/2026, last updated 9 February 2026 (Chapters 10, 11, Annexure XXIII)
        https://www.sebi.gov.in/sebi_data/attachdocs/feb-2026/1770636136785.pdf
  SCORES: SEBI SCORES 2.0 FAQ for investors (Oct 2024 file) https://www.sebi.gov.in/sebi_data/faqfiles/oct-2024/1730356475310.pdf
        SMART ODR: SEBI investor page https://investor.sebi.gov.in/smart_orr.html
  Schemes of arrangement: SEBI master circular SEBI/HO/CFD/POD-2/P/CIR/2023/93, 20 June 2023 (NSE-hosted copy)
        https://nsearchives.nseindia.com/s3fs-public/inline-files/Master%20Circular%20on%20Scheme%20of%20Arrangement_2.pdf
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
    market=dict(fills=mk_fills, cost=mk_cost, qty=mk_qty, avg=round(mk_cost / mk_qty, 2), avg_fmt="%.2f" % (mk_cost / mk_qty),
                best_ask=ASKS[0][0], slippage_rs=round(mk_cost / mk_qty - ASKS[0][0], 2),
                slippage_fmt="%.2f" % (mk_cost / mk_qty - ASKS[0][0])),
    limit=dict(limit=LIMIT_PX, fills=lm_fills, cost=lm_cost, qty=lm_qty,
               avg=round(lm_cost / lm_qty, 2), avg_fmt="%.2f" % (lm_cost / lm_qty), unfilled=BUY_QTY - lm_qty),
    stop_loss=SL,
    listing_price=LISTING_PRICE,
)

NSE = dict(
    timings_url="https://www.nseindia.com/market-data/market-timings",
    trading_url="https://www.nseindia.com/static/products-services/equity-market-trading-system",
    preopen_url="https://www.nseindia.com/static/products-services/equity-market-pre-open",
    trading_page_updated="28 February 2024", preopen_page_updated="4 September 2026",
    preopen_window="9:00 am to 9:15 am", normal_close="3:30 pm", normal_open="9:15 am",
)

# ---- Contract note: charges on a delivery trade (rules typed once, opened 1 Nov 2026) ----
CS = yaml.safe_load(open(os.path.join(ROOT, "_data", "case_study.yml"), encoding="utf-8"))["listing"]
CHARGES = dict(
    as_of="November 2026",
    stt_circular="NSE/FATAX/73524, 31 March 2026",
    stt_url="https://nsearchives.nseindia.com/content/circulars/FATAX73524.pdf",
    txn_circular="NSE/FA/64232, 27 September 2024 (effective 1 October 2024)",
    txn_url="https://nsearchives.nseindia.com/content/circulars/FA64232.pdf",
    levies_url="https://www.nseindia.com/static/invest/first-time-investor-sebi-turnover-fees-stt-other-levies",
    levies_updated="17 April 2026",
    sebi_circular_charges="SEBI/HO/MRD/TPD-1/P/CIR/2024/92, 1 July 2024",
    stt_delivery_pct=0.1,          # purchaser and seller, delivery-based equity share
    stt_non_delivery_sell_pct=0.025,
    txn_per_lakh=2.97,             # cash market, each side, per lakh of traded value
    sebi_fee_per_crore=10,         # Rs 10 per crore, securities other than debt
    stamp_delivery_pct=0.015,      # buyer, delivery basis
    gst_pct=18,
)
CH_QTY, CH_BUY_PX, CH_SELL_PX = 100, 642, 655      # HYPOTHETICAL trade
CH_BROKERAGE = 20                                   # HYPOTHETICAL flat Rs per executed order (broker-specific)


def side(value, buy):
    brokerage = CH_BROKERAGE
    txn = value / 1e5 * CHARGES["txn_per_lakh"]
    sebi = value / 1e7 * CHARGES["sebi_fee_per_crore"]
    stt = value * CHARGES["stt_delivery_pct"] / 100
    stamp = value * CHARGES["stamp_delivery_pct"] / 100 if buy else 0.0
    gst = brokerage * CHARGES["gst_pct"] / 100          # ASSUMPTION: GST on brokerage only
    r = lambda x: round(x, 2)
    parts = [r(brokerage), r(txn), r(sebi), r(stt), r(stamp), r(gst)]
    total = r(sum(parts))              # total of the rounded lines, so the table reproduces
    return dict(value=value, brokerage=parts[0], txn=parts[1], sebi=parts[2], stt=parts[3], stamp=parts[4],
                gst=parts[5], total=total)


buy_v, sell_v = CH_QTY * CH_BUY_PX, CH_QTY * CH_SELL_PX
BUY, SELL = side(buy_v, True), side(sell_v, False)
gross = sell_v - buy_v
total_ch = round(BUY["total"] + SELL["total"], 2)
CHARGES.update(
    qty=CH_QTY, buy_px=CH_BUY_PX, sell_px=CH_SELL_PX, brokerage_each=CH_BROKERAGE,
    buy=BUY, sell=SELL, gross_gain=gross, total_charges=total_ch,
    net_after_charges=round(gross - total_ch, 2),
    charges_pct_of_gross=round(total_ch / gross * 100, 1),
    stt_total=round(BUY["stt"] + SELL["stt"], 2),
)
assert gross == 1300

# ---- IPO application (ICDR master circular, 9 Feb 2026; read 1 Nov 2026) ----
LOT = CS["ipo_lot_size_shares"]
PRICE = CS["ipo_price"]
LOT_AMT = LOT * PRICE
RETAIL_CAP = 200000                    # master circular: "two lakh rupees for retail category" (net payment amount)
MAX_LOTS = RETAIL_CAP // LOT_AMT
IPO = dict(
    as_of="November 2026",
    master_circular="HO/49/14/14(2)2026-CFD-POD2/I/4518/2026 (last updated 9 February 2026)",
    master_url="https://www.sebi.gov.in/sebi_data/attachdocs/feb-2026/1770636136785.pdf",
    upi_limit_lakh=5, retail_cap_rs=RETAIL_CAP,
    upi_mandate_cutoff="5 pm on T", unblock_by="T+2", listing_on="T+3",
    unblock_sponsor="Sponsor Banks execute the online mandate revoke file for non-allottees and partial allottees on T+2",
    comp_per_day=100, comp_rate_pct=15, comp_basis_days=365,
    price=PRICE, lot=LOT, lot_amt=LOT_AMT, fresh_shares_lakh=CS["fresh_issue_shares_lakh"],
    fresh_proceeds_lakh=CS["ipo_proceeds"],
    max_lots=MAX_LOTS, max_amt=MAX_LOTS * LOT_AMT, over_cap_lots=MAX_LOTS + 1, over_cap_amt=(MAX_LOTS + 1) * LOT_AMT,
    two_lot_amt=2 * LOT_AMT,
    comp_rows=[dict(amount=a, pct_per_day=round(a * 0.15 / 365, 2), per_day=max(100, round(a * 0.15 / 365, 2)))
               for a in (LOT_AMT, MAX_LOTS * LOT_AMT, 500000)],
    delay_days=5,
)
assert LOT_AMT == 14720 and MAX_LOTS == 13
assert IPO["comp_rows"][0]["per_day"] == 100 and IPO["comp_rows"][2]["per_day"] > 100
IPO["comp_breakeven"] = round(100 / (0.15 / 365))

# ---- SCORES and SMART ODR (SEBI FAQ, Oct 2024 file; SEBI investor pages) ----
SCORES = dict(
    as_of="November 2026",
    faq_url="https://www.sebi.gov.in/sebi_data/faqfiles/oct-2024/1730356475310.pdf",
    investor_url="https://investor.sebi.gov.in/sebi_scores.html",
    odr_url="https://investor.sebi.gov.in/smart_orr.html",
    scores_circular="SEBI/HO/OIAE/IGRD/CIR/P/2023/156 (as cited in SEBI's own SCORES FAQ)",
    odr_circular="SEBI/HO/OIAE/OIAE_IAD-1/P/CIR/2023/145, 31 July 2023 (as cited in SEBI's own SCORES FAQ)",
    limitation_years=1, atr_days=21, review_request_days=15, designated_days=10, second_review_days=15,
    conciliation_ok_rs=4800, conciliation_fail_rs=3240,
    example_atr_day=21, example_review_last_day=21 + 15,
    example_complaint="your broker has not credited funds that should be back in your trading account",
)
assert SCORES["example_review_last_day"] == 36

# ---- Schemes of arrangement: illustrative companies, hypothetical numbers ----
MERGE = dict(a_name="Alpha Foods Ltd", b_name="Beta Snacks Ltd", ratio_new=3, ratio_old=7, holding=100)
whole, rem = divmod(MERGE["holding"] * MERGE["ratio_new"], MERGE["ratio_old"])
MERGE.update(entitled=round(MERGE["holding"] * MERGE["ratio_new"] / MERGE["ratio_old"], 3), whole=whole,
             fraction=round(rem / MERGE["ratio_old"], 3), fraction_num=rem)
DEMERGE = dict(parent="Alpha Foods Ltd", child="Gamma Beverages Ltd", per_old=4, holding=100, pre_px=800,
               post_parent_px=620, post_child_px=720)
DEMERGE["child_shares"] = DEMERGE["holding"] // DEMERGE["per_old"]
DEMERGE["value_before"] = DEMERGE["holding"] * DEMERGE["pre_px"]
DEMERGE["value_after"] = DEMERGE["holding"] * DEMERGE["post_parent_px"] + DEMERGE["child_shares"] * DEMERGE["post_child_px"]
DEMERGE["parent_drop"] = DEMERGE["pre_px"] - DEMERGE["post_parent_px"]
assert DEMERGE["value_before"] == DEMERGE["value_after"] == 80000 and DEMERGE["holding"] % DEMERGE["per_old"] == 0
assert (MERGE["whole"], MERGE["fraction_num"]) == (42, 6)
SCHEME = dict(
    as_of="November 2026",
    master_circular="SEBI/HO/CFD/POD-2/P/CIR/2023/93, 20 June 2023",
    master_url="https://nsearchives.nseindia.com/s3fs-public/inline-files/Master%20Circular%20on%20Scheme%20of%20Arrangement_2.pdf",
    fraction_trust_days=90, merge=MERGE, demerge=DEMERGE,
)

out = dict(bsda=dict(BSDA, examples=[bsda_status(v) for v in BSDA_EXAMPLES]),
           nomination=dict(NOM, example_units=NOM_EXAMPLE_UNITS, example_split=NOM_EXAMPLE_SPLIT,
                           pct_example=dict(NOM_PCT_EXAMPLE, shares=NOM_PCT_SHARES)),
           orders=ORDERS, nse=NSE, charges=CHARGES, ipo=IPO, scores=SCORES, scheme=SCHEME)

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("# GENERATED by scripts/derive_mb.py — do not edit by hand.\n")
    yaml.safe_dump(out, fh, sort_keys=False, allow_unicode=True, width=100)
print("wrote", OUT)
print(ORDERS["market"], ORDERS["limit"], NOM_EXAMPLE_SPLIT, NOM_PCT_SHARES, out["bsda"]["examples"])
