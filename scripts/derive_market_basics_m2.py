#!/usr/bin/env python3
"""
Derive the worked examples for module 2 of "Your first year in the market",
"Inside your demat account" (_data/market_basics_m2.yml): the consolidated
account statement, KYC and CKYC, the pre-open session and closing price,
delivery vs intraday, margin pledge, and corporate actions in demat. Posts dated
14 to 19 February 2027. Roadmap: _review/roadmaps/2026-11-21-market-basics-m2.md

    python3 scripts/derive_market_basics_m2.py

RULES (read 21 Nov 2026; every post carries needs_review: regulation or tax):
  * CAS: SEBI Master Circular for Depositories, 3 Dec 2024, para 1.24 (NSDL's copy,
    circular 2024-0176); SEBI circulars SEBI/HO/MRD-PoD2/CIR/P/2024/93 (1 Jul 2024)
    and SEBI/HO/MRD/PoD1/CIR/P/2025/16 (14 Feb 2025, effective 14 May 2025).
  * KYC: SEBI KYC Master Circular SEBI/HO/MIRSD/SECFATF/P/CIR/2023/169, 12 Oct 2023,
    paras 82-101 (KRA) and 113-117 (CKYCR).
  * Pre-open and closing auction: SEBI circular of 16 Jan 2026 (CAS introduced;
    pre-open revised from 7 Sep 2026) and of 15 Oct 2026 (CAS moved to 3:30-3:40 pm
    from 7 Dec 2026; para 4.8 from 8 Feb 2027).
  * Margins: SEBI Master Circular for Stock Exchanges and Clearing Corporations,
    Chapter 4 (2023 edition, as consolidated): VaR margin minimum 9% for Group I
    stocks, ELM 3.5%, collected upfront.
  * STT: NSE circular NSE/FATAX/73524 (31 Mar 2026). Stamp duty: NSE investor page
    on levies (delivery 0.015%, non-delivery 0.003%, buyer pays).
  * Margin pledge: SEBI circulars of 25 Feb 2020 and 3 Jun 2025.
  * Bonus credit: SEBI circular CIR/CFD/PoD/2024/122, 16 Sep 2024 (NSE's copy).

HYPOTHETICAL: every order book, holding, haircut and trade below.
Needs pyyaml.
"""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "market_basics_m2.yml"
mb = yaml.safe_load(open(ROOT / "_data/market_basics.yml", encoding="utf-8"))
ch = mb["charges"]


def r(x, d=2):
    v = round(float(x), d)
    return int(v) if v == int(v) else v


out = {}

# ---------------------------------------------------------------- 1. CAS
out["cas"] = {
    "data_days": 5, "ecas_days": 12, "physical_days": 15,
    "half_yearly_data": "8 April and 8 October", "half_yearly_ecas": "18 April and 18 October",
    "half_yearly_physical": "21 April and 21 October", "effective": "14 May 2025",
    "email_default_from": "1 August 2024",
    "example_month": "January 2027", "example_ecas_by": "12 February 2027", "example_physical_by": "15 February 2027",
    "mc_url": "https://nsdl.com/nsdl/circulars/2024-0176-Policy-SEBI_Master_Circular_for_Depositories.pdf",
    "c2024_url": "https://www.sebi.gov.in/legal/circulars/jul-2024/dispatch-of-consolidated-account-statement-cas-for-all-securities-assets_84514.html",
    "c2025_url": "https://www.sebi.gov.in/legal/circulars/feb-2025/revised-timelines-for-issuance-of-consolidated-account-statement-cas-by-depositories_91927.html",
}

# ---------------------------------------------------------------- 2. KYC
out["kyc"] = {
    "upload_kra_days": 3, "kra_letter_days": 2, "ckyc_days": 10,
    "url": "https://www.sebi.gov.in/legal/master-circulars/oct-2023/master-circular-on-know-your-client-kyc-norms-for-the-securities-market_77945.html",
    "consultation": "January 2026",
    "nov26_url": "https://www.sebi.gov.in/sebi_data/attachdocs/nov-2026/1793791897866.pdf",
}

# ---------------------------------------------------------------- 3. pre-open / closing auction: equilibrium price
ref = 500.0
# hypothetical order book at the end of order entry: (price, buy qty at or above, sell qty at or below) built from orders
buys = [(None, 300), (505, 200), (503, 400), (501, 500), (499, 300)]     # None = market order
sells = [(None, 250), (497, 300), (499, 400), (501, 350), (503, 500)]
prices = sorted({p for p, _ in buys + sells if p is not None})
rows = []
for p in prices:
    dem = sum(q for bp, q in buys if bp is None or bp >= p)
    sup = sum(q for sp, q in sells if sp is None or sp <= p)
    rows.append({"price": p, "buy": dem, "sell": sup, "matched": min(dem, sup), "unmatched": abs(dem - sup)})
best = max(rows, key=lambda x: (x["matched"], -x["unmatched"], -abs(x["price"] - ref)))
ties = [x for x in rows if x["matched"] == best["matched"]]
out["auction"] = {
    "reference": r(ref), "band_pct": 3, "band_low": r(ref * 0.97), "band_high": r(ref * 1.03),
    "buys": [{"price": ("Market" if p is None else p), "qty": q} for p, q in buys],
    "sells": [{"price": ("Market" if p is None else p), "qty": q} for p, q in sells],
    "rows": rows, "eq_price": best["price"], "eq_volume": best["matched"], "eq_unmatched": best["unmatched"],
    "tie_count": len(ties),
    "preopen": "9:00 to 9:15 am", "preopen_from": "7 September 2026",
    "preopen_sessions": [
        {"start": "9:00 am", "what": "Order entry, limit and market orders", "mins": 5},
        {"start": "9:05 am", "what": "Order entry for limit orders only; market orders can't be modified or cancelled; random close in the last 2 minutes", "mins": 5},
        {"start": "9:10 am", "what": "Order matching", "mins": 2},
        {"start": "9:12 am", "what": "Transition to the continuous session", "mins": 3},
    ],
    "cas_window": "3:30 to 3:40 pm", "cas_from": "7 December 2026", "cas_ref_minutes": 15,
    "vwap_minutes_non_cas": 30, "post_close": "3:50 to 4:00 pm",
    "jan_url": "https://www.sebi.gov.in/sebi_data/attachdocs/jan-2026/1768576287344.pdf",
    "oct_url": "https://www.sebi.gov.in/sebi_data/attachdocs/oct-2026/1792079571420.pdf",
}
assert best["matched"] > 0

# ---------------------------------------------------------------- 4. delivery vs intraday (same trade as the contract note post)
qty, bp, sp = ch["qty"], ch["buy_px"], ch["sell_px"]
bv, sv = qty * bp, qty * sp
txn, sebi_fee, gst = ch["txn_per_lakh"] / 100000, ch["sebi_fee_per_crore"] / 1e7, ch["gst_pct"] / 100
brk = ch["brokerage_each"]
STAMP_NON_DELIVERY = 0.003


def legs(delivery):
    """Each line rounded to the paisa per leg, then added, as the contract note post does."""
    stt_rate_s = ch["stt_delivery_pct"] if delivery else ch["stt_non_delivery_sell_pct"]
    buy = {"brokerage": brk, "txn": round(bv * txn, 2), "sebi": round(bv * sebi_fee, 2),
           "stt": round(bv * ch["stt_delivery_pct"] / 100, 2) if delivery else 0.0,
           "stamp": round(bv * (ch["stamp_delivery_pct"] if delivery else STAMP_NON_DELIVERY) / 100, 2),
           "gst": round(brk * gst, 2)}
    sell = {"brokerage": brk, "txn": round(sv * txn, 2), "sebi": round(sv * sebi_fee, 2),
            "stt": round(sv * stt_rate_s / 100, 2), "stamp": 0.0, "gst": round(brk * gst, 2)}
    t = {k: buy[k] + sell[k] for k in buy}
    t["total"] = sum(t.values())
    return {k: r(v) for k, v in t.items()}


dl, it = legs(True), legs(False)
assert abs(dl["total"] - ch["total_charges"]) < 0.005, (dl["total"], ch["total_charges"])
VAR_MIN, ELM = 9, 3.5
out["delivery"] = {
    "qty": qty, "buy_px": bp, "sell_px": sp, "buy_value": bv, "sell_value": sv, "gross": sv - bv,
    "delivery": dl, "intraday": it, "net_delivery": r(sv - bv - dl["total"]), "net_intraday": r(sv - bv - it["total"]),
    # two-decimal display strings for the charge table, as the contract note post shows them
    "fmt": {"delivery": {k: f"{v:.2f}" for k, v in dl.items()},
            "intraday": {k: f"{v:.2f}" for k, v in it.items()},
            "net_delivery": f"{sv - bv - dl['total']:.2f}", "net_intraday": f"{sv - bv - it['total']:.2f}"},
    "stt_delivery_pct": ch["stt_delivery_pct"], "stt_intraday_sell_pct": ch["stt_non_delivery_sell_pct"],
    "stamp_delivery_pct": ch["stamp_delivery_pct"], "stamp_intraday_pct": STAMP_NON_DELIVERY,
    "var_min_pct": VAR_MIN, "elm_pct": ELM, "margin_pct": VAR_MIN + ELM,
    "margin_rupees": r(bv * (VAR_MIN + ELM) / 100), "stt_url": ch["stt_url"], "levies_url": ch["levies_url"],
    "ch4_url": "https://www.sebi.gov.in/sebi_data/commondocs/oct-2023/Chapter-4-Comprehensive_Risk_Management_for_Cash_p.pdf",
}

# ---------------------------------------------------------------- 5. margin pledge (illustrative haircut)
hold = 200000
haircut = 12.5
fall = 20
credit = hold * (1 - haircut / 100)
after = hold * (1 - fall / 100)
credit_after = after * (1 - haircut / 100)
out["pledge"] = {"holding": hold, "haircut_pct": haircut, "credit": r(credit), "fall_pct": fall, "holding_after": r(after),
                 "credit_after": r(credit_after), "credit_drop": r(credit - credit_after),
                 "url2020": "https://www.sebi.gov.in/legal/circulars/feb-2020/margin-obligations-to-be-given-by-way-of-pledge-re-pledge-in-the-depository-system_46082.html",
                 "url2025": "https://www.sebi.gov.in/legal/circulars/jun-2025/margin-obligations-to-be-given-by-way-of-pledge-re-pledge-in-the-depository-system_94363.html"}

# ---------------------------------------------------------------- 6. corporate actions (illustrative holding)
shares, price = 50, 1200.0
out["corp"] = {
    "shares": shares, "price": r(price), "value": r(shares * price),
    "bonus_ratio": "1:1", "bonus_shares_after": shares * 2, "bonus_price": r(price / 2),
    "split_from": 10, "split_to": 2, "split_shares_after": shares * 5, "split_price": r(price / 5),
    "dividend_per_share": 12, "dividend_total": shares * 12,
    "bonus_url": "https://nsearchives.nseindia.com/web/sites/default/files/inline-files/SEBI_Circular_16092024_0.pdf",
    "bonus_from": "1 October 2024",
}

OUT.write_text("# Generated by scripts/derive_market_basics_m2.py. Do not edit by hand. Examples are HYPOTHETICAL.\n"
               + yaml.safe_dump(out, sort_keys=False, allow_unicode=True), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
