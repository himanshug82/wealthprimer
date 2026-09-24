#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every worked example for the Tax series module 3 (REITs and InvITs;
bonds, debentures and Sovereign Gold Bonds; advance tax; gifts and clubbing;
NRI basics) and write them to _data/tax3.yml.

    python3 scripts/derive_tax3.py          # rewrites _data/tax3.yml

Needs PyYAML only (standard library otherwise).

CONVENTIONS (same as derive_tax2.py)
- Slab: 30% used as the illustrative marginal slab, 4% health and education
  cess ON the tax. Surcharge is ignored because every example keeps total
  income below Rs 50 lakh; the posts say so, and say where surcharge would
  change the answer.
- Rules are Tax Year 2026-27 (FY 2026-27): Income-tax Act, 2025 (No. 30 of
  2025) as amended by the Finance Act, 2026 (No. 4 of 2026). Unlike the
  earlier tax modules, this one was checked against the PRIMARY TEXT: the
  Gazette copy of the 2025 Act (hosted by ICAI), the Gazette copy of the
  Finance Act, 2026, and the Budget memoranda on indiabudget.gov.in. Section
  numbers below are the 2025 Act's. See the `verification` block.
- Fictional examples use round numbers and say so. Two examples use REAL NAVs
  already in the repo (AMFI via mfapi.in, truncated 31 March 2026):
    assets/data/uti-nifty50-index-fund-nav.csv  (UTI Nifty 50 Index Fund, regular, growth)
    assets/data/uti-gilt-fund-nav.csv           (UTI Gilt Fund, regular, growth)
  The index-fund lump sum is the same one as _data/tax.yml example_lumpsum;
  the script recomputes it and asserts it matches.
- Rupee outputs are rounded to whole rupees.
"""
import csv
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_data" / "tax3.yml"
TAX = yaml.safe_load((ROOT / "_data" / "tax.yml").read_text(encoding="utf-8"))
RATES = TAX["rates"]

SLAB = 0.30
CESS = RATES["cess_pct"] / 100            # 4%
STCG_EQ = RATES["equity_stcg_pct"] / 100  # 20%, s.196
LTCG = RATES["equity_ltcg_pct"] / 100     # 12.5%, s.197 and s.198
LTCG_EXEMPT = RATES["ltcg_annual_exemption"]  # Rs 1,25,000, s.198
TDS_RESIDENT = 0.10                       # s.393(1) business-trust income, interest on listed debentures


def r(x):
    return int(round(x))


def cess(tax):
    """Tax plus 4% cess, rounded."""
    return r(tax * (1 + CESS))


def nav_on(fname, day, col="nav_regular_growth"):
    with open(ROOT / "assets" / "data" / fname, newline="") as f:
        for row in csv.DictReader(f):
            if row["date"] == day:
                return float(row[col])
    raise KeyError(f"{day} not in {fname}")


# --------------------------------------------------------------------------
# 1. REITs and InvITs — hypothetical listed REIT, round numbers
# --------------------------------------------------------------------------
reit_units = 1000
reit_issue_price = 300           # price at which the REIT originally issued units
reit_buy_price = 320             # our investor bought later, on the exchange
reit_interest_pu = 9             # per unit, in Tax Year 2026-27
reit_dividend_pu = 5             # SPV has NOT opted for the concessional regime (s.200)
reit_repay_pu = 10               # "repayment of debt / capital"
reit_cum_repay_pu = 60           # all non-income distributions on a unit since issue, incl. this year
reit_sale_price = 350

reit_interest = reit_interest_pu * reit_units
reit_dividend = reit_dividend_pu * reit_units
reit_repay = reit_repay_pu * reit_units
reit_total = reit_interest + reit_dividend + reit_repay

reit_interest_tax = cess(reit_interest * SLAB)
reit_interest_tds = r(reit_interest * TDS_RESIDENT)
reit_div_tax_if_opted = cess(reit_dividend * SLAB)
reit_div_tds_if_opted = r(reit_dividend * TDS_RESIDENT)

# s.92(2)(k): specified sum = A - B - C, floored at zero
reit_specified_pu = max(0, reit_cum_repay_pu - reit_issue_price - 0)
assert reit_specified_pu == 0
# s.72(4): the untaxed repayment reduces the cost of acquisition
reit_cost_before = reit_buy_price * reit_units
reit_cost_after = (reit_buy_price - reit_repay_pu) * reit_units
reit_sale_value = reit_sale_price * reit_units
reit_gain = reit_sale_value - reit_cost_after
reit_gain_if_cost_not_reduced = reit_sale_value - reit_cost_before
assert reit_gain - reit_gain_if_cost_not_reduced == reit_repay
reit_ltcg_tax_if_exemption_used = cess(reit_gain * LTCG)
reit_stcg_tax = cess(reit_gain * STCG_EQ)
reit_cash_tax_year = reit_interest_tax  # tax actually owed on the year's distributions
reit_effective_on_distribution_pct = round(100 * reit_interest_tax / reit_total, 1)
reit_tax_if_all_interest = cess(reit_total * SLAB)   # the "treat it all as interest" mistake

# Mature InvIT: cumulative capital repayments have passed the issue price
invit_issue_price = 100
invit_cum_repay_y1 = 104         # A in year 1 (includes what earlier holders received)
invit_cum_repay_y2 = 110         # A in year 2
invit_units = 1000
invit_spec_y1_pu = max(0, invit_cum_repay_y1 - invit_issue_price - 0)
invit_spec_y2_pu = max(0, invit_cum_repay_y2 - invit_issue_price - invit_spec_y1_pu)
assert (invit_spec_y1_pu, invit_spec_y2_pu) == (4, 6)
invit_spec_y1 = invit_spec_y1_pu * invit_units
invit_spec_y2 = invit_spec_y2_pu * invit_units
invit_tax_y1 = cess(invit_spec_y1 * SLAB)
invit_tax_y2 = cess(invit_spec_y2 * SLAB)

reit = {
    "note": "Hypothetical listed REIT, round numbers. Illustrative 30% slab + 4% cess, no surcharge.",
    "units": reit_units,
    "issue_price": reit_issue_price,
    "buy_price": reit_buy_price,
    "buy_date": "1 April 2025",
    "interest_pu": reit_interest_pu,
    "dividend_pu": reit_dividend_pu,
    "repay_pu": reit_repay_pu,
    "total_pu": reit_interest_pu + reit_dividend_pu + reit_repay_pu,
    "interest": reit_interest,
    "dividend": reit_dividend,
    "repay": reit_repay,
    "total": reit_total,
    "interest_tax_with_cess": reit_interest_tax,
    "interest_tds": reit_interest_tds,
    "interest_balance_due": reit_interest_tax - reit_interest_tds,
    "dividend_tax_if_spv_opted_with_cess": reit_div_tax_if_opted,
    "dividend_tds_if_spv_opted": reit_div_tds_if_opted,
    "cum_repay_pu": reit_cum_repay_pu,
    "specified_sum_pu": reit_specified_pu,
    "cost_before": reit_cost_before,
    "cost_after": reit_cost_after,
    "cost_after_pu": reit_buy_price - reit_repay_pu,
    "sale_price": reit_sale_price,
    "sale_date": "1 March 2027",
    "months_held": 23,
    "sale_value": reit_sale_value,
    "gain": reit_gain,
    "gain_if_cost_not_reduced": reit_gain_if_cost_not_reduced,
    "ltcg_tax_if_exemption_used_with_cess": reit_ltcg_tax_if_exemption_used,
    "stcg_tax_if_within_12m_with_cess": reit_stcg_tax,
    "effective_tax_on_distribution_pct": reit_effective_on_distribution_pct,
    "tax_if_all_treated_as_interest_with_cess": reit_tax_if_all_interest,
    "overpay_if_all_interest": reit_tax_if_all_interest - reit_interest_tax,
    "invit_issue_price": invit_issue_price,
    "invit_units": invit_units,
    "invit_cum_repay_y1": invit_cum_repay_y1,
    "invit_cum_repay_y2": invit_cum_repay_y2,
    "invit_specified_y1_pu": invit_spec_y1_pu,
    "invit_specified_y2_pu": invit_spec_y2_pu,
    "invit_specified_y1": invit_spec_y1,
    "invit_specified_y2": invit_spec_y2,
    "invit_tax_y1_with_cess": invit_tax_y1,
    "invit_tax_y2_with_cess": invit_tax_y2,
}

# --------------------------------------------------------------------------
# 2. Bonds, debentures, Sovereign Gold Bonds — round numbers
# --------------------------------------------------------------------------
ncd_invested = 2_00_000
ncd_coupon_pct = 9
ncd_interest = r(ncd_invested * ncd_coupon_pct / 100)
ncd_tds_threshold = 10_000
assert ncd_interest > ncd_tds_threshold
ncd_tds = r(ncd_interest * TDS_RESIDENT)
ncd_tax = cess(ncd_interest * SLAB)

same_gain = 60_000
gain_at_ltcg = cess(same_gain * LTCG)
gain_at_slab = cess(same_gain * SLAB)

sgb_grams = 20
sgb_issue_price = 5_000
sgb_coupon_pct = 2.5
sgb_years = 8
sgb_maturity_price = 9_000
sgb_exchange_price = 6_000
sgb_invested = sgb_grams * sgb_issue_price
sgb_interest_yr = r(sgb_invested * sgb_coupon_pct / 100)
sgb_interest_tax_yr = cess(sgb_interest_yr * SLAB)
sgb_interest_total = sgb_interest_yr * sgb_years
sgb_interest_tax_total = sgb_interest_tax_yr * sgb_years
sgb_maturity_value = sgb_grams * sgb_maturity_price
sgb_gain_issue = sgb_maturity_value - sgb_invested
sgb_exchange_cost = sgb_grams * sgb_exchange_price
sgb_gain_exchange = sgb_maturity_value - sgb_exchange_cost
assert sgb_gain_exchange == same_gain
sgb_tax_exchange = cess(sgb_gain_exchange * LTCG)

bonds = {
    "note": "Round, hypothetical numbers. Illustrative 30% slab + 4% cess, no surcharge.",
    "ncd_invested": ncd_invested,
    "ncd_coupon_pct": ncd_coupon_pct,
    "ncd_interest": ncd_interest,
    "ncd_tds_threshold": ncd_tds_threshold,
    "ncd_tds": ncd_tds,
    "ncd_tax_with_cess": ncd_tax,
    "ncd_balance_due": ncd_tax - ncd_tds,
    "same_gain": same_gain,
    "gain_tax_ltcg_with_cess": gain_at_ltcg,
    "gain_tax_slab_with_cess": gain_at_slab,
    "gain_tax_difference": gain_at_slab - gain_at_ltcg,
    "sgb_grams": sgb_grams,
    "sgb_issue_price": sgb_issue_price,
    "sgb_invested": sgb_invested,
    "sgb_coupon_pct": sgb_coupon_pct,
    "sgb_years": sgb_years,
    "sgb_interest_yr": sgb_interest_yr,
    "sgb_interest_tax_yr_with_cess": sgb_interest_tax_yr,
    "sgb_interest_total": sgb_interest_total,
    "sgb_interest_tax_total_with_cess": sgb_interest_tax_total,
    "sgb_maturity_price": sgb_maturity_price,
    "sgb_maturity_value": sgb_maturity_value,
    "sgb_gain_issue": sgb_gain_issue,
    "sgb_exchange_price": sgb_exchange_price,
    "sgb_exchange_cost": sgb_exchange_cost,
    "sgb_gain_exchange": sgb_gain_exchange,
    "sgb_tax_exchange_with_cess": sgb_tax_exchange,
}

# --------------------------------------------------------------------------
# 3. Advance tax — hypothetical salaried investor
# --------------------------------------------------------------------------
at_salary = 30_00_000            # employer's TDS assumed to cover the salary tax exactly
at_fd_interest = 3_00_000
at_fd_tds = r(at_fd_interest * TDS_RESIDENT)
at_ltcg = 5_25_000               # equity-fund gain realised 10 August 2026
at_threshold = 10_000            # s.404
total_income = at_salary + at_fd_interest + at_ltcg
assert total_income < 50_00_000  # no surcharge
assert at_salary + at_fd_interest > 24_00_000   # interest sits in the 30% slab (s.202)

at_interest_tax = cess(at_fd_interest * SLAB)
at_interest_net = at_interest_tax - at_fd_tds
at_ltcg_taxable = at_ltcg - LTCG_EXEMPT
at_ltcg_tax = cess(at_ltcg_taxable * LTCG)
at_total = at_interest_net + at_ltcg_tax
assert at_total >= at_threshold

PCTS = [15, 45, 75, 100]
DATES = ["15 June 2026", "15 September 2026", "15 December 2026", "15 March 2027"]
RATE_425 = [3, 3, 3, 1]          # s.425(1) Table, column E

# Scenario A: regular income on the schedule, the gain's tax added to the
# first instalment after it arose (15 September).
cum_regular = [r(at_interest_net * p / 100) for p in PCTS]
cum_paid_a = [cum_regular[0]] + [c + at_ltcg_tax for c in cum_regular[1:]]
inst_a = [cum_paid_a[0]] + [cum_paid_a[i] - cum_paid_a[i - 1] for i in range(1, 4)]
assert cum_paid_a[-1] == at_total

required = [r(at_total * p / 100) for p in PCTS]
# June is short only because of the capital gain; s.425(4) forgives it
# because the gain's tax was paid in the remaining instalments.
june_shortfall_a = required[0] - cum_paid_a[0]
assert june_shortfall_a > 0
assert all(cum_paid_a[i] >= required[i] for i in range(1, 4))

# Scenario B: nothing paid until filing on 31 July 2027.
b_425 = [required[i] * RATE_425[i] / 100 for i in range(4)]
b_425_total = r(sum(b_425))
months_424 = 4                   # April, May, June, July 2027
b_424 = r(at_total * months_424 / 100)
b_total = b_425_total + b_424

# Scenario C: regular income paid on schedule; the gain's tax only at filing.
cum_paid_c = cum_regular
assert cum_paid_c[-1] < 0.9 * at_total       # fails the 90% test in s.424
c_short = [max(0, required[i] - cum_paid_c[i]) for i in range(4)]
c_425 = [c_short[i] * RATE_425[i] / 100 for i in range(4)]
c_425_total = r(sum(c_425))
c_424_base = at_total - cum_paid_c[-1]
c_424 = r(c_424_base * months_424 / 100)
c_total = c_425_total + c_424

advance = {
    "note": "Hypothetical salaried investor, Tax Year 2026-27. Employer TDS assumed to cover salary tax. Illustrative 30% slab + 4% cess; total income under Rs 50 lakh, so no surcharge. Interest ignores the rules' rounding conventions.",
    "threshold": at_threshold,
    "salary": at_salary,
    "fd_interest": at_fd_interest,
    "fd_tds": at_fd_tds,
    "ltcg": at_ltcg,
    "ltcg_date": "10 August 2026",
    "ltcg_taxable": at_ltcg_taxable,
    "total_income": total_income,
    "interest_tax_with_cess": at_interest_tax,
    "interest_tax_net_of_tds": at_interest_net,
    "ltcg_tax_with_cess": at_ltcg_tax,
    "advance_tax_total": at_total,
    "schedule": [
        {
            "date": DATES[i],
            "pct": PCTS[i],
            "required_cum": required[i],
            "regular_cum": cum_regular[i],
            "paid_a_cum": cum_paid_a[i],
            "instalment_a": inst_a[i],
            "rate_425_pct": RATE_425[i],
            "b_interest": r(b_425[i]),
            "c_shortfall": c_short[i],
            "c_interest": r(c_425[i]),
        }
        for i in range(4)
    ],
    "june_shortfall_a": june_shortfall_a,
    "b_425_total": b_425_total,
    "months_424": months_424,
    "b_424": b_424,
    "b_total": b_total,
    "c_424_base": c_424_base,
    "c_425_total": c_425_total,
    "c_424": c_424,
    "c_total": c_total,
    "ninety_pct": r(0.9 * at_total),
    "safe_june_pct": 12,
    "safe_sept_pct": 36,
}

# --------------------------------------------------------------------------
# 4. Gifts and clubbing — hypothetical family, plus the real index-fund lump sum
# --------------------------------------------------------------------------
gift_limit = 50_000
gift_single = 60_000
gift_single_tax = cess(gift_single * SLAB)
gift_two = [30_000, 25_000]
gift_two_total = sum(gift_two)
assert gift_two_total > gift_limit and max(gift_two) <= gift_limit
gift_two_tax = cess(gift_two_total * SLAB)

spouse_gift = 10_00_000
spouse_fd_pct = 7
spouse_interest = r(spouse_gift * spouse_fd_pct / 100)
spouse_interest_tax = cess(spouse_interest * SLAB)

minor_interest = 20_000
minor_exclusion = 1_500          # Schedule III, Sl. No. 17
minor_clubbed = minor_interest - minor_exclusion
minor_tax = cess(minor_clubbed * SLAB)

# Real data: the same lump sum as _data/tax.yml example_lumpsum
ls = TAX["example_lumpsum"]
buy_nav = nav_on("uti-nifty50-index-fund-nav.csv", ls["buy_date"])
sell_nav = nav_on("uti-nifty50-index-fund-nav.csv", ls["sell_date"])
units = round(ls["invested"] / buy_nav, 4)
value = r(units * sell_nav)
gain = value - ls["invested"]
assert abs(buy_nav - ls["buy_nav"]) < 1e-9 and abs(sell_nav - ls["sell_nav"]) < 1e-9
assert (units, value, gain) == (ls["units"], ls["value"], ls["gain"]), (units, value, gain)
tax_with_own_exemption = cess((gain - LTCG_EXEMPT) * LTCG)
assert tax_with_own_exemption == ls["tax_with_cess"]
tax_exemption_used = cess(gain * LTCG)
clubbing_cost = tax_exemption_used - tax_with_own_exemption

gifts = {
    "note": "Hypothetical family; the share example uses the real UTI Nifty 50 Index Fund lump sum from _data/tax.yml. Illustrative 30% slab + 4% cess, no surcharge.",
    "limit": gift_limit,
    "single": gift_single,
    "single_tax_with_cess": gift_single_tax,
    "two_a": gift_two[0],
    "two_b": gift_two[1],
    "two_total": gift_two_total,
    "two_tax_with_cess": gift_two_tax,
    "spouse_gift": spouse_gift,
    "spouse_fd_pct": spouse_fd_pct,
    "spouse_interest": spouse_interest,
    "spouse_interest_tax_with_cess": spouse_interest_tax,
    "minor_interest": minor_interest,
    "minor_exclusion": minor_exclusion,
    "minor_clubbed": minor_clubbed,
    "minor_tax_with_cess": minor_tax,
    "ls_buy_date": "1 April 2020",
    "ls_sell_date": "31 March 2026",
    "ls_invested": ls["invested"],
    "ls_buy_nav": ls["buy_nav"],
    "ls_sell_nav": ls["sell_nav"],
    "ls_value": value,
    "ls_gain": gain,
    "ls_tax_own_exemption_with_cess": tax_with_own_exemption,
    "ls_tax_exemption_used_with_cess": tax_exemption_used,
    "ls_clubbing_cost": clubbing_cost,
}

# --------------------------------------------------------------------------
# 5. NRI basics — the same equity lump sum, a real gilt-fund holding, and
#    round-number NRO/NRE interest
# --------------------------------------------------------------------------
NRI_TDS_EQ_LTCG = 0.125          # Finance Act 2026, First Schedule Part II, (b)(i)(C)
NRI_TDS_EQ_STCG = 0.20           # (b)(i)(E)
NRI_TDS_OTHER = 0.30             # (b)(i)(O) "the whole of the other income"

nri_eq_tds = cess((gain - LTCG_EXEMPT) * NRI_TDS_EQ_LTCG)
assert nri_eq_tds == tax_with_own_exemption

gilt_invested = 5_00_000
gilt_buy_day, gilt_sell_day = "2023-04-03", "2026-03-31"
gilt_buy_nav = nav_on("uti-gilt-fund-nav.csv", gilt_buy_day)
gilt_sell_nav = nav_on("uti-gilt-fund-nav.csv", gilt_sell_day)
gilt_units = round(gilt_invested / gilt_buy_nav, 4)
gilt_value = r(gilt_units * gilt_sell_nav)
gilt_gain = gilt_value - gilt_invested
gilt_tds = cess(gilt_gain * NRI_TDS_OTHER)
gilt_resident_tax = cess(gilt_gain * SLAB)   # same number at a 30% slab, but paid at filing

nro_interest = 1_00_000
nro_tds = cess(nro_interest * NRI_TDS_OTHER)
nre_interest = 1_00_000

nri = {
    "note": "Equity example = the UTI Nifty 50 Index Fund lump sum from _data/tax.yml; gilt example = UTI Gilt Fund (regular, growth), AMFI NAVs via mfapi.in; NRO/NRE interest are round numbers. TDS rates per the Finance Act, 2026; payments below Rs 50 lakh, so no surcharge on the TDS.",
    "eq_gain": gain,
    "eq_value": value,
    "eq_taxable": gain - LTCG_EXEMPT,
    "eq_tds_with_cess": nri_eq_tds,
    "tds_eq_ltcg_pct": 12.5,
    "tds_eq_stcg_pct": 20,
    "tds_other_pct": 30,
    "tds_investment_income_pct": 20,
    "tds_mf_income_pct": 20,
    "gilt_invested": gilt_invested,
    "gilt_buy_date": "3 April 2023",
    "gilt_sell_date": "31 March 2026",
    "gilt_buy_nav": gilt_buy_nav,
    "gilt_sell_nav": gilt_sell_nav,
    "gilt_units": gilt_units,
    "gilt_value": gilt_value,
    "gilt_gain": gilt_gain,
    "gilt_tds_with_cess": gilt_tds,
    "gilt_resident_tax_with_cess": gilt_resident_tax,
    "nro_interest": nro_interest,
    "nro_tds_with_cess": nro_tds,
    "nre_interest": nre_interest,
    "nre_tax": 0,
    "surcharge_threshold": 50_00_000,
    "resident_days": 182,
    "short_stay_days": 60,
    "lookback_days": 365,
    "lookback_years": 4,
}

# --------------------------------------------------------------------------
# Rules, sources, verification
# --------------------------------------------------------------------------
ACT = "https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf"
FA26 = "https://egazette.gov.in/WriteReadData/2026/271439.pdf"
MEMO26 = "https://www.indiabudget.gov.in/doc/memo.pdf"
MEMO24 = "https://www.indiabudget.gov.in/budget2024-25/doc/memo.pdf"
MEMO23 = "https://www.indiabudget.gov.in/budget2023-24/doc/memo.pdf"
RBI_SGB = "https://www.rbi.org.in/commonman/English/Scripts/FAQs.aspx?Id=1658"

verification = {
    "financial_year": "Tax Year 2026-27 (FY 2026-27)",
    "verified_on": "September 2026",
    "how": "Checked against the primary text: the Income-tax Act, 2025 (No. 30 of 2025, Gazette of 21 August 2025, copy hosted by ICAI), the Finance Act, 2026 (No. 4 of 2026, assent 30 March 2026, Gazette copy), and the Memoranda to the Finance Bills of 2023, 2024 and 2026 on indiabudget.gov.in. incometaxindia.gov.in's consolidated 'as amended by Finance Act 2026' text returned 403, so the 2025 Act was read as enacted and every Finance Act 2026 amendment to the sections used here was checked separately (only consequential cross-reference changes to s.99, s.393, s.424 and s.425; a substantive change to s.70(1)(x), the SGB exemption).",
    "sources": {
        "income_tax_act_2025": ACT,
        "finance_act_2026": FA26,
        "memorandum_finance_bill_2026": MEMO26,
        "memorandum_finance_no2_bill_2024": MEMO24,
        "memorandum_finance_bill_2023": MEMO23,
        "rbi_sgb_faq": RBI_SGB,
    },
    "reit": {
        "rules": [
            "Business trust = REIT or InvIT registered under the SEBI regulations (s.2(21)).",
            "Distributions keep the character they had in the trust's hands (s.223(1)).",
            "Unit holder exemption (Schedule V, Sl. No. 5): distributed income is exempt EXCEPT the part that is (a) interest from an SPV, (b) dividend from an SPV that has opted for the concessional company rate under s.200, (c) a REIT's rent from real estate it owns directly. Those parts are taxed in the unit holder's hands (s.223(3)).",
            "Anything else (e.g. 'repayment of debt/capital'): taxable as income from other sources only to the extent of the 'specified sum' = A - B - C (s.92(2)(k)), where A = all such distributions on the unit since issue (including to earlier holders), B = the unit's ISSUE price, C = amounts already taxed under this clause. Origin: Finance Act 2023 (old s.56(2)(xii)).",
            "Distributions that are neither income nor taxed under s.92(2)(k) reduce the unit's cost of acquisition (s.72(4)).",
            "TDS, residents: 10% on the interest, dividend and rent components, no threshold (s.393(1) Table Sl. 4(ii)); no TDS on a dividend from an SPV that has NOT opted for s.200 (s.393 no-deduction table, Sl. 5). Non-residents: 5% on SPV interest, 10% on SPV dividend, rates in force on rent (s.393(2) Table Sl. 6-7).",
            "Listed units: short-term if held 12 months or less (s.2(101)(b)(i), 'security listed in a recognised stock exchange'). STCG 20% if STT-paid (s.196); LTCG 12.5% above Rs 1,25,000 a year, sharing the equity exemption (s.198). Before 23 July 2024 the holding period was 36 months and the rates 15%/10% (Memorandum, Finance (No. 2) Bill 2024).",
        ],
        "disagreements": "None found in the text. OPEN for a professional: how trusts' statements label 'other income' (e.g. interest on the trust's own deposits, taxed at the trust level and exempt in the holder's hands under Schedule V Sl. 5) varies by trust; the post tells readers to follow the statement the trust issues under s.223(5).",
    },
    "bonds": {
        "rules": [
            "Interest on bonds and debentures: income from other sources at slab. TDS on interest on securities to residents at 10% ('rates in force', Finance Act 2026 First Schedule Part II; listed debentures named explicitly) above Rs 10,000 a year (s.393(1) Table Sl. 5(i)). The old exemption from TDS for listed demat debentures was removed from 1 April 2023 (Memorandum, Finance Bill 2023).",
            "Listed bonds/debentures: long-term after 12 months (s.2(101)(b)(i)), LTCG 12.5% without indexation and without the Rs 1.25 lakh exemption (s.197; the exemption in s.198 covers only equity shares, equity-oriented fund units and business trust units). STCG at slab.",
            "Unlisted bonds/debentures transferred, redeemed or maturing on or after 23 July 2024, and market-linked debentures (any date, listed or not): always short-term, taxed at slab (s.76(2)).",
            "SGB interest: 2.5% a year (RBI FAQ), taxable at slab; no TDS (RBI FAQ; Central Government securities are in the s.393 no-deduction table, Sl. 6).",
            "SGB redemption: not a transfer (so no capital gain) only 'if held by an individual from the date of original issue till maturity' (s.70(1)(x) as substituted by Finance Act 2026, s.43, from 1 April 2026). Bought on the exchange: taxable at maturity. Sold on the exchange: normal capital gains, listed security (12 months; LTCG 12.5%, no Rs 1.25 lakh exemption).",
        ],
        "disagreements": "OPEN: premature redemption with the RBI (allowed after the fifth year on interest dates, per the RBI FAQ) is not 'maturity' on the amended wording, so it appears to fall outside the exemption from 1 April 2026. No official clarification found; the post flags it. Also not covered: accrued interest paid/received when a bond trades between coupon dates.",
    },
    "advance": {
        "rules": [
            "Liability if the year's tax, after TDS/TCS, is Rs 10,000 or more (s.404, s.405). Resident individuals aged 60+ with no business/professional income are exempt (s.403(3)).",
            "Instalments (s.408(1)): 15% by 15 June, 45% by 15 September, 75% by 15 December, 100% by 15 March (cumulative). Presumptive business filers: all by 15 March (s.408(2)). Anything paid by 31 March counts as advance tax (s.408(3)).",
            "Interest for deferment (s.425, old 234C): 3% on the shortfall at each of the first three dates, 1% at 15 March. No interest if at least 12% was paid by 15 June and 36% by 15 September (s.425(2)). No interest on a shortfall caused by capital gains, dividends, casual income or first-year business income, if the tax on it is paid in the remaining instalments or by 31 March (s.425(4)).",
            "Interest for default (s.424, old 234B): if advance tax paid is under 90% of the assessed tax, 1% a month or part-month from 1 April after the tax year on the shortfall, until the tax is paid or assessed.",
            "Finance Act 2026 made only consequential changes to s.424 and s.425 (MAT cross-references).",
        ],
        "disagreements": "The old Income-tax Rules rounded the amounts used for this interest (to the nearest hundred, down); the example ignores rounding and the post says so. Whether the new Rules keep that convention was not checked.",
    },
    "gifts": {
        "rules": [
            "Money, or property (shares and securities, jewellery, bullion, art, land/buildings, virtual digital assets) received without consideration from non-relatives: taxable as income from other sources if the aggregate in the tax year exceeds Rs 50,000 - the WHOLE amount, not the excess (s.92(2)(m); 'property' in s.92(5)(f)).",
            "Exempt whatever the amount: from a relative; on the occasion of the individual's marriage; under a will or inheritance; in contemplation of the donor's death; and other listed cases (s.92(3)). 'Relative' for an individual: spouse; brother/sister; brother/sister of the spouse; brother/sister of either parent; any lineal ascendant or descendant, and those of the spouse; and the spouses of all these (s.92(5)(g)).",
            "A gift by an individual is not a transfer for capital gains (s.70(1)(b)). The recipient takes the previous owner's cost (s.73(1) Table Sl. 1) and holding period (s.2(101)(c)(B)(I)). Property taxed under s.92(2)(m) takes that taxed value as its cost (s.73 Table Sl. 17).",
            "Clubbing (s.99): income arising to a spouse, or a son's wife, from assets transferred by the individual 'otherwise than for adequate consideration' is taxed in the individual's hands; all income of a minor child is clubbed with the parent whose income is higher (except income from the child's own work or skill, or a child with a specified disability), with Rs 1,500 per child excluded (Schedule III, Sl. No. 17). 'Income' includes loss (s.99(5)(d)).",
            "Adult children are not in s.99: income on a gift to an adult child is the child's.",
        ],
        "disagreements": "Not in the Act's text, and stated in the post as 'generally treated' / worth confirming: (1) income earned by reinvesting clubbed income ('income on income') is the spouse's own; (2) what counts as 'adequate consideration', and how a documented interest-bearing loan to a spouse is treated. Both rest on case law and practice, not the statute.",
    },
    "nri": {
        "rules": [
            "Residence (s.6): resident if in India 182 days or more in the tax year, or 60 days in the year plus 365 days in the previous four (60 becomes 120 for a visiting citizen/PIO with Indian income over Rs 15 lakh). Details beyond this are out of scope.",
            "TDS on payments to non-residents (s.393(2)): Sl. 17 covers any sum chargeable to tax (the old s.195) at 'rates in force'; mutual fund income (IDCW) at 20% or the treaty rate if lower (Sl. 10, Note 2).",
            "Rates in force for a non-resident Indian (Finance Act 2026, First Schedule, Part II, (b)(i)): LTCG on equity/equity-fund units above Rs 1,25,000 12.5%; other LTCG 12.5%; STCG on STT-paid equity 20%; 'investment income' from foreign exchange assets 20%; the whole of other income 30%. Surcharge applies on the TDS when the income paid crosses Rs 50 lakh (capped at 15% for dividends and s.196/197/198 gains), plus 4% cess on non-residents' TDS (Memorandum 2026, rates section).",
            "Treaty relief (s.159): the Act applies only where more beneficial than the treaty (s.159(4)); a non-resident claiming treaty relief needs a tax residency certificate from their country of residence plus prescribed documents (s.159(8)). Lower/nil TDS certificate: s.395(1).",
            "NRE interest: exempt for an individual who is a 'person resident outside India' under FEMA s.2(w) (Schedule IV, Sl. No. 1). NRO interest: taxable; TDS at 30% plus cess under the rates in force.",
            "The resident-only reliefs: basic-exemption shortfall adjustment against special-rate gains (s.196(2), s.197(2), s.198(3)) and the s.156 rebate apply to residents only.",
        ],
        "disagreements": "OPEN: the form number for the prescribed documents with a TRC (Form 10F under the old Rules) under the Income-tax Rules made for the 2025 Act was not checked; the post says 'the prescribed form'. Specific treaty rates are not quoted.",
    },
}

header = """# The Tax Side of Investing - module 3 worked examples (REITs/InvITs, bonds
# and SGBs, advance tax, gifts and clubbing, NRI basics).
#
# GENERATED by scripts/derive_tax3.py - do not edit by hand; edit the script
# and re-run it. Every rupee figure in the five posts renders from here.
#
# Rules are Tax Year 2026-27, checked in September 2026 against the PRIMARY
# text of the Income-tax Act, 2025 and the Finance Act, 2026 (links in the
# `verification` block). Items a professional should confirm are under
# `verification.*.disagreements`.
"""

data = {
    "verification": verification,
    "reit": reit,
    "bonds": bonds,
    "advance": advance,
    "gifts": gifts,
    "nri": nri,
}

OUT.write_text(header + "\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
for k in ("reit", "bonds", "advance", "gifts", "nri"):
    print(k, {kk: vv for kk, vv in data[k].items() if not isinstance(vv, (dict, list, str))})
