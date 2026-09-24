#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build _data/real_bank.yml — the real-bank anchor for the Fundamental Analysis
"banks and NBFCs" module (BANK-1..6).

WHY A SCRIPT: every ratio a post quotes about HDFC Bank must be re-derivable
from the reported figures below, the same discipline as _data/real_company.yml
(Britannia) and _data/ta.yml. Reported figures are typed ONCE here, straight
from the filing; every ratio is computed, never typed. Re-run after any edit:

    python3 scripts/derive_bank.py

SOURCE (primary): HDFC Bank Ltd, results for the quarter and year ended
31 March 2025 — STANDALONE, audited (Price Waterhouse LLP; Batliboi & Purohit),
board-approved 19 April 2025, released 21 April 2025, filed as an exhibit to
the bank's Form 6-K with the US SEC:
  https://www.sec.gov/Archives/edgar/data/1144967/000119312525087787/d930582dex99.htm
All figures ₹ crore unless noted. FY24 columns are the filing's own comparatives.

MARKET DATA: NSE close on 30 June 2025 from Yahoo Finance (HDFCBANK.NS chart
API). Yahoo serves prices ADJUSTED for the 1:1 bonus (record date 27 Aug 2025):
it shows ₹1,000.75; the price actually traded that day was twice that,
₹2,001.50. FY25 EPS (₹88.29) and book value per share are PRE-bonus, so the
pre-bonus price is the consistent one to pair with them. Same lag logic as
Britannia's 30 June 2025 price: > 3 months before the first BANK post
(2026-11-20).

REGULATORY MINIMUM: the filing itself says "regulatory requirement of 11.7%":
RBI Basel III minimum CRAR 9% + capital conservation buffer 2.5% + D-SIB
(domestic systemically important bank) surcharge 0.2% for HDFC Bank's bucket.
"""
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml (use the project venv)")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_data", "real_bank.yml")

SRC_URL = "https://www.sec.gov/Archives/edgar/data/1144967/000119312525087787/d930582dex99.htm"

# ---- reported, typed once, from the filing --------------------------------
R = {
    "FY25": dict(
        interest_earned=300517.04, interest_expended=177846.95,
        other_income=45632.28, operating_expenses=68174.89,
        provisions_and_contingencies=11649.42, provision_for_npa=12715.31,
        floating_provision=0.0, pat=67347.36,
        capital=765.22, reserves_and_surplus=496854.21, net_worth_reported=488899.89,
        deposits=2714714.90, borrowings=547930.90, other_liabilities=146128.52,
        total_assets=3910198.94, cash_with_rbi=144355.03, investments=836359.68,
        advances=2619608.61, fixed_assets=13655.40, other_assets=201004.57,
        savings_deposits=630500.0, current_deposits=314100.0,  # ₹6,305 bn and ₹3,141 bn as printed
        gross_npa=35222.64, gross_npa_pct_reported=1.33, net_npa=11320.43, net_npa_pct_reported=0.43,
        car_pct=19.55, tier1_pct=17.7, cet1_pct=17.2, rwa=2660000.0,  # RWA ₹26,600 bn as printed
        eps_basic=88.29, eps_diluted=87.90, branches=9455,
    ),
    "FY24": dict(
        interest_earned=258340.56, interest_expended=149808.10,
        other_income=49240.99, operating_expenses=63386.01,
        provisions_and_contingencies=23492.14, floating_provision=10900.0, pat=60812.27,
        capital=759.69, reserves_and_surplus=436833.39, net_worth_reported=427634.18,
        deposits=2379786.28, borrowings=662153.07, other_liabilities=135437.91,
        total_assets=3617623.06, cash_with_rbi=178683.22, investments=702414.96,
        advances=2484861.52, fixed_assets=11398.97, other_assets=199800.20,
        gross_npa=31173.32, gross_npa_pct_reported=1.24, net_npa=8091.74, net_npa_pct_reported=0.33,
        car_pct=18.80, roa_pct_reported=1.98,
        eps_basic=85.83, eps_diluted=85.44, branches=8738,
    ),
}
# Q4 FY25 NIM sentences, verbatim from the filing (quarter, not year).
NIM_Q4 = dict(on_total_assets=3.54, on_interest_earning_assets=3.73,
              core_on_total_assets=3.46, core_on_interest_earning_assets=3.65,
              tax_refund_interest_bn=7)
CASA_FY25_PCT_REPORTED = 34.8
REG_MIN = dict(crar=9.0, ccb=2.5, dsib_surcharge=0.2, total=11.7, cet1_min=5.5, tier1_min=7.0)
MARKET = dict(price_date="30 June 2025", price_adjusted_yahoo=1000.75, bonus_ratio="1:1",
              bonus_record_date="27 August 2025", price=2001.50,
              dividend_per_share_fy25=22.0,
              source_url="https://finance.yahoo.com/quote/HDFCBANK.NS/history/")

# Segment revenue FY25, as printed (₹ crore) — for BANK-1's "what a bank sells".
SEGMENTS_FY25 = dict(treasury=62227.48, retail_banking=283434.79,
                     wholesale_banking=191964.51, other_banking_operations=35449.05,
                     total=573075.83)


def r(x, d=2):
    return round(float(x), d)


def avg(a, b):
    return (a + b) / 2.0


def main():
    f25, f24 = R["FY25"], R["FY24"]
    for fy in R.values():
        fy["net_interest_income"] = r(fy["interest_earned"] - fy["interest_expended"])
        fy["total_income"] = r(fy["interest_earned"] + fy["other_income"])
        fy["operating_income"] = r(fy["net_interest_income"] + fy["other_income"])   # "net revenue"
        fy["pre_provision_operating_profit"] = r(fy["operating_income"] - fy["operating_expenses"])
        fy["profit_before_tax"] = r(fy["pre_provision_operating_profit"] - fy["provisions_and_contingencies"])
        fy["tax"] = r(fy["profit_before_tax"] - fy["pat"])
        fy["shareholders_equity"] = r(fy["capital"] + fy["reserves_and_surplus"])
        fy["shares_cr"] = r(fy["capital"] / 1.0, 2)   # face value ₹1 → ₹ crore of capital = crore shares
        fy["book_value_per_share"] = r(fy["shareholders_equity"] / fy["shares_cr"], 2)
        fy["leverage_assets_to_equity"] = r(fy["total_assets"] / fy["shareholders_equity"], 1)
        fy["equity_to_assets_pct"] = r(100 * fy["shareholders_equity"] / fy["total_assets"], 2)
        fy["credit_deposit_ratio_pct"] = r(100 * fy["advances"] / fy["deposits"], 1)
        fy["cost_to_income_pct"] = r(100 * fy["operating_expenses"] / fy["operating_income"], 1)
        fy["other_income_share_pct"] = r(100 * fy["other_income"] / fy["operating_income"], 1)
        fy["gross_npa_pct"] = r(100 * fy["gross_npa"] / fy["advances"], 2)   # on reported (net) advances — see note
        fy["net_npa_pct"] = r(100 * fy["net_npa"] / (fy["advances"] - (fy["gross_npa"] - fy["net_npa"])), 2)
        fy["npa_provisions_held"] = r(fy["gross_npa"] - fy["net_npa"])
        fy["provision_coverage_pct"] = r(100 * (fy["gross_npa"] - fy["net_npa"]) / fy["gross_npa"], 1)
        fy["deposits_share_of_funding_pct"] = r(100 * fy["deposits"] / (fy["deposits"] + fy["borrowings"]), 1)
        fy["borrowings_share_of_funding_pct"] = r(100 * fy["borrowings"] / (fy["deposits"] + fy["borrowings"]), 1)

    f25["casa_deposits"] = r(f25["savings_deposits"] + f25["current_deposits"])
    f25["casa_ratio_pct"] = r(100 * f25["casa_deposits"] / f25["deposits"], 1)
    f25["term_deposits"] = r(f25["deposits"] - f25["casa_deposits"])
    f25["casa_ratio_pct_reported"] = CASA_FY25_PCT_REPORTED
    # FY24 CASA ratio: the filing prints FY25 CASA in ₹ bn only; FY24 ratio is widely reported ~38.2%
    # and is NOT in this document — recorded as external context, flagged.
    f24["casa_ratio_pct_reported_external"] = 38.2

    # ---- averages-based ratios (FY25 only; need both year-ends) ----------
    A = dict(
        avg_total_assets=r(avg(f25["total_assets"], f24["total_assets"])),
        avg_advances=r(avg(f25["advances"], f24["advances"])),
        avg_deposits=r(avg(f25["deposits"], f24["deposits"])),
        avg_borrowings=r(avg(f25["borrowings"], f24["borrowings"])),
        avg_equity=r(avg(f25["shareholders_equity"], f24["shareholders_equity"])),
        avg_investments=r(avg(f25["investments"], f24["investments"])),
    )
    A["avg_interest_earning_assets"] = r(A["avg_advances"] + A["avg_investments"])   # approximation: excludes call money, RBI balances
    A["avg_funding"] = r(A["avg_deposits"] + A["avg_borrowings"])
    D = dict(
        nim_on_avg_total_assets_pct=r(100 * f25["net_interest_income"] / A["avg_total_assets"], 2),
        nim_on_avg_interest_earning_assets_pct=r(100 * f25["net_interest_income"] / A["avg_interest_earning_assets"], 2),
        yield_on_interest_earning_assets_pct=r(100 * f25["interest_earned"] / A["avg_interest_earning_assets"], 2),
        cost_of_funds_pct=r(100 * f25["interest_expended"] / A["avg_funding"], 2),
        spread_pct=None,
        credit_cost_pct=r(100 * f25["provision_for_npa"] / A["avg_advances"], 2),
        roa_pct=r(100 * f25["pat"] / A["avg_total_assets"], 2),
        roe_pct=r(100 * f25["pat"] / A["avg_equity"], 1),
        avg_leverage=r(A["avg_total_assets"] / A["avg_equity"], 1),
        nii_growth_pct=r(100 * (f25["net_interest_income"] / f24["net_interest_income"] - 1), 1),
        pat_growth_pct=r(100 * (f25["pat"] / f24["pat"] - 1), 1),
        deposit_growth_pct=r(100 * (f25["deposits"] / f24["deposits"] - 1), 1),
        advances_growth_pct=r(100 * (f25["advances"] / f24["advances"] - 1), 1),
        borrowings_change_pct=r(100 * (f25["borrowings"] / f24["borrowings"] - 1), 1),
        provisions_change_pct=r(100 * (f25["provisions_and_contingencies"] / f24["provisions_and_contingencies"] - 1), 1),
        ppop_growth_pct=r(100 * (f25["pre_provision_operating_profit"] / f24["pre_provision_operating_profit"] - 1), 1),
    )
    D["spread_pct"] = r(D["yield_on_interest_earning_assets_pct"] - D["cost_of_funds_pct"], 2)
    # ROE identity check: ROA × leverage
    D["roa_x_leverage_pct"] = r(D["roa_pct"] * D["avg_leverage"], 1)

    # ---- "why 3.5% is a lot": NIM in rupees per ₹1 lakh of assets ---------
    D["nii_per_lakh_of_avg_assets"] = r(1e5 * f25["net_interest_income"] / A["avg_total_assets"], 0)
    # sensitivity: 10 basis points of NIM on the average balance sheet, in ₹ crore and as % of PAT
    D["nii_per_10bp_cr"] = r(A["avg_total_assets"] * 0.001, 0)
    D["nii_per_10bp_as_pct_of_pat"] = r(100 * A["avg_total_assets"] * 0.001 / f25["pat"], 1)

    # ---- capital: rupees of buffer, and the 11.7% line ---------------------
    C = dict(
        rwa=f25["rwa"],
        rwa_to_total_assets_pct=r(100 * f25["rwa"] / f25["total_assets"], 1),
        capital_at_car=r(f25["car_pct"] / 100 * f25["rwa"]),         # ≈ total regulatory capital
        capital_at_reg_min=r(REG_MIN["total"] / 100 * f25["rwa"]),
        headroom_pct_points=r(f25["car_pct"] - REG_MIN["total"], 2),
        headroom_rupees=r((f25["car_pct"] - REG_MIN["total"]) / 100 * f25["rwa"]),
        cet1_rupees=r(f25["cet1_pct"] / 100 * f25["rwa"]),
        # loss the CET1 layer could absorb before breaching the 11.7% total floor is not a clean
        # single number (different tiers); the post uses headroom_rupees as the illustrative buffer.
        gross_npa_as_pct_of_cet1=r(100 * f25["gross_npa"] / (f25["cet1_pct"] / 100 * f25["rwa"]), 1),
    )

    # ---- valuation at 30 June 2025 (pre-bonus basis) ---------------------
    V = dict(
        as_of="Price NSE close 30 June 2025 (pre-bonus basis); financials FY25 (year ended 31 March 2025)",
        price=MARKET["price"],
        book_value_per_share=f25["book_value_per_share"],
        pb=r(MARKET["price"] / f25["book_value_per_share"], 2),
        pe=r(MARKET["price"] / f25["eps_basic"], 1),
        market_cap_cr=r(MARKET["price"] * f25["shares_cr"]),
        dividend_yield_pct=r(100 * MARKET["dividend_per_share_fy25"] / MARKET["price"], 2),
        earnings_yield_pct=r(100 * f25["eps_basic"] / MARKET["price"], 2),
        # P/B = P/E × ROE identity (using closing-equity ROE for consistency with BVPS)
        roe_on_closing_equity_pct=r(100 * f25["pat"] / f25["shareholders_equity"], 1),
    )
    V["pe_x_roe_check"] = r(V["pe"] * V["roe_on_closing_equity_pct"] / 100, 2)
    # illustrative justified P/B = (ROE − g) / (Ke − g), stated as illustration with round inputs
    # The point of the table is how VIOLENTLY the output moves with two guessed inputs —
    # not which scenario is "right". BANK-6 draws no conclusion from it.
    roe = D["roe_pct"]
    V["justified_pb_scenarios"] = [
        dict(label="A", cost_of_equity_pct=14.0, growth_pct=9.0, pb=r((roe - 9.0) / (14.0 - 9.0), 2)),
        dict(label="B", cost_of_equity_pct=13.0, growth_pct=10.0, pb=r((roe - 10.0) / (13.0 - 10.0), 2)),
        dict(label="C", cost_of_equity_pct=12.0, growth_pct=11.0, pb=r((roe - 11.0) / (12.0 - 11.0), 2)),
    ]

    out = {
        "_comment": ("GENERATED by scripts/derive_bank.py — edit the reported figures there, not here. "
                     "Every ratio is computed from the reported lines. Source: " + SRC_URL),
        "company": dict(
            name="HDFC Bank Ltd", type="Listed private-sector bank (India's largest by assets)",
            exchange="NSE: HDFCBANK, BSE: 500180", basis="Standalone, audited",
            currency_note="All figures in Rs crore unless noted",
            source_url=SRC_URL,
            source_label="Results for the quarter and year ended 31 March 2025 (Form 6-K exhibit, 21 April 2025)",
            as_of="FY25 (year ended 31 March 2025), released 21 April 2025",
            auditors="Price Waterhouse LLP; Batliboi & Purohit",
            merger_note=("HDFC Ltd (the housing-finance parent) merged into HDFC Bank effective 1 July 2023, "
                         "so FY24 was the first full year of the combined balance sheet and FY24 comparatives "
                         "already include it. Widely reported context, not analysis."),
        ),
        "reported": R,
        "nim_q4_fy25_reported": NIM_Q4,
        "averages": A,
        "derived_fy25": D,
        "capital": C,
        "regulatory_minimum": REG_MIN,
        "segments_fy25": SEGMENTS_FY25,
        "market": MARKET,
        "valuation": V,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("# GENERATED by scripts/derive_bank.py — do not edit by hand.\n")
        fh.write("# Reported figures are typed once in that script, from the filing named below;\n")
        fh.write("# every ratio here is computed. Re-run the script after any change.\n")
        yaml.safe_dump(out, fh, sort_keys=False, allow_unicode=True, width=100)
    print("wrote", OUT)
    for k, v in D.items():
        print(f"  {k}: {v}")
    print("  casa_ratio_pct:", f25["casa_ratio_pct"], "| cd ratio:", f25["credit_deposit_ratio_pct"],
          "| PCR:", f25["provision_coverage_pct"], "| BVPS:", f25["book_value_per_share"],
          "| P/B:", V["pb"], "| P/E:", V["pe"], "| headroom cr:", C["headroom_rupees"])


if __name__ == "__main__":
    main()
