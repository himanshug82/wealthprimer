#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every worked example for the Tax series add-on module (TAX-10..13:
ESOPs/RSUs, buybacks, F&O as business income, foreign stocks and Schedule FA)
and write them to _data/tax2.yml.

    python3 scripts/derive_tax2.py          # rewrites _data/tax2.yml

WHY A SCRIPT: the posts render every rupee figure from _data/tax2.yml via
Liquid, never inline. Re-running this after a rate change (or a mistake)
updates every table in every post at once, and the arithmetic is auditable
here rather than scattered across prose.

CONVENTIONS
- All examples are FICTIONAL and illustrative: a Desi Bites Foods employee
  and shareholder (the blog's fictional case-study company, IPO at Rs 640 on
  15 June 2025 per _data/case_study.yml), a hypothetical F&O trader whose
  loss equals SEBI's reported FY26 average (from _data/fno.yml), and a
  hypothetical US-stock purchase at stated illustrative exchange rates.
- Slab rate: 30% used as the illustrative marginal slab throughout, with 4%
  health & education cess ON the tax. Surcharge is ignored (income below the
  surcharge threshold) and said so in the posts.
- Rates are FY 2026-27 unless the regime is date-specific (buybacks span
  three regimes). Sources and verification date are recorded in the YAML's
  `verification` block, not here.
- Rupee outputs are rounded to whole rupees. Only Python's standard library
  plus PyYAML is needed.
"""
import math
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_data" / "tax2.yml"

SLAB = 0.30
CESS = 0.04
STCG_EQ = 0.20
LTCG_EQ = 0.125
LTCG_EXEMPT = 125_000
DIV_TDS = 0.10


def r(x):
    return int(round(x))


def with_cess(tax):
    return r(tax * (1 + CESS))


# --------------------------------------------------------------------------
# TAX-10  ESOPs and RSUs — fictional Desi Bites Foods employee
# --------------------------------------------------------------------------
esop_shares = 1000
esop_exercise_price = 200
esop_fmv_at_exercise = 700
esop_sale_price = 850

perq_per_share = esop_fmv_at_exercise - esop_exercise_price
perquisite = perq_per_share * esop_shares
perq_tax = perquisite * SLAB
perq_tax_cess = with_cess(perq_tax)
cash_to_exercise = esop_exercise_price * esop_shares
cash_out_total = cash_to_exercise + perq_tax_cess

ltcg_gain = (esop_sale_price - esop_fmv_at_exercise) * esop_shares
ltcg_taxable = max(0, ltcg_gain - LTCG_EXEMPT)
ltcg_tax_cess = with_cess(ltcg_taxable * LTCG_EQ)
stcg_tax_cess = with_cess(ltcg_gain * STCG_EQ)   # same sale inside 12 months

economic_gain = (esop_sale_price - esop_exercise_price) * esop_shares
total_tax_lt = perq_tax_cess + ltcg_tax_cess
# the beginner's wrong answer: tax the whole gain as LTCG once
wrong_answer_tax = with_cess(max(0, economic_gain - LTCG_EXEMPT) * LTCG_EQ)

rsu_units = 500
rsu_perquisite = esop_fmv_at_exercise * rsu_units
rsu_tax_cess = with_cess(rsu_perquisite * SLAB)
rsu_sell_to_cover = math.ceil(rsu_tax_cess / esop_fmv_at_exercise)

esop = {
    "note": "Fictional employee of Desi Bites Foods Ltd (the case-study company). Illustrative 30% slab + 4% cess, no surcharge.",
    "shares": esop_shares,
    "exercise_price": esop_exercise_price,
    "fmv_at_exercise": esop_fmv_at_exercise,
    "exercise_date": "1 September 2025",
    "perquisite_per_share": perq_per_share,
    "perquisite": perquisite,
    "perquisite_tax_before_cess": r(perq_tax),
    "perquisite_tax_with_cess": perq_tax_cess,
    "cash_to_exercise": cash_to_exercise,
    "cash_out_total": cash_out_total,
    "sale_price": esop_sale_price,
    "sale_date_long": "1 November 2026",
    "months_held_long": 14,
    "capital_gain": ltcg_gain,
    "ltcg_exempt": LTCG_EXEMPT,
    "ltcg_taxable": ltcg_taxable,
    "ltcg_tax_with_cess": ltcg_tax_cess,
    "stcg_tax_with_cess_if_sold_within_12m": stcg_tax_cess,
    "economic_gain": economic_gain,
    "total_tax_long_route": total_tax_lt,
    "effective_rate_pct": round(100 * total_tax_lt / economic_gain, 1),
    "wrong_answer_tax": wrong_answer_tax,
    "rsu_units": rsu_units,
    "rsu_perquisite": rsu_perquisite,
    "rsu_tax_with_cess": rsu_tax_cess,
    "rsu_sell_to_cover_shares": rsu_sell_to_cover,
    "rsu_net_shares": rsu_units - rsu_sell_to_cover,
}

# --------------------------------------------------------------------------
# TAX-11  Buybacks — three regimes on the same 100 shares
# --------------------------------------------------------------------------
bb_shares = 100
bb_cost = 640            # IPO price, 15 June 2025
bb_price = 700
bb_consideration = bb_price * bb_shares
bb_cost_total = bb_cost * bb_shares
bb_gain = bb_consideration - bb_cost_total

# Regime A (to 30 Sep 2024): company paid 20% + 12% surcharge + 4% cess on
# distributed income (consideration minus what the company received on issue).
regA_rate = 0.20 * 1.12 * 1.04
regA_company_tax = r(bb_gain * regA_rate)

# Regime B (1 Oct 2024 – 31 Mar 2026): whole consideration = deemed dividend.
regB_tax = with_cess(bb_consideration * SLAB)
regB_tds = r(bb_consideration * DIV_TDS)
regB_capital_loss = bb_cost_total          # consideration deemed nil
# Cess applied to the loss value too, so it nets cleanly against the
# with-cess dividend tax. Shares bought June 2025 and bought back before
# 31 Mar 2026 were held <= 12 months, so the loss is SHORT-term.
regB_loss_value_vs_stcg = with_cess(bb_cost_total * STCG_EQ)
regB_loss_value_vs_ltcg = with_cess(bb_cost_total * LTCG_EQ)
regB_net_if_loss_used_stcg = regB_tax - regB_loss_value_vs_stcg

# Regime C (from 1 Apr 2026): capital gains, cost deductible.
regC_ltcg_tax = with_cess(max(0, bb_gain - LTCG_EXEMPT) * LTCG_EQ)
regC_stcg_tax = with_cess(bb_gain * STCG_EQ)
regC_promoter_effective_noncorp = 0.30
regC_promoter_tax_noncorp = r(bb_gain * regC_promoter_effective_noncorp)

buyback = {
    "note": "Fictional Desi Bites Foods shareholder: 100 shares bought in the IPO at Rs 640 (15 June 2025), tendered in a hypothetical buyback at Rs 700. Illustrative 30% slab + 4% cess.",
    "shares": bb_shares,
    "cost_per_share": bb_cost,
    "buyback_price": bb_price,
    "consideration": bb_consideration,
    "cost_total": bb_cost_total,
    "gain": bb_gain,
    "regime_a": {
        "period": "up to 30 September 2024",
        "company_tax_rate_pct": round(100 * regA_rate, 3),
        "company_tax": regA_company_tax,
        "shareholder_tax": 0,
    },
    "regime_b": {
        "period": "1 October 2024 to 31 March 2026",
        "deemed_dividend": bb_consideration,
        "tax_with_cess": regB_tax,
        "tds": regB_tds,
        "capital_loss": regB_capital_loss,
        "loss_worth_against_stcg": regB_loss_value_vs_stcg,
        "loss_worth_against_ltcg": regB_loss_value_vs_ltcg,
        "net_cost_if_loss_used_against_stcg": regB_net_if_loss_used_stcg,
    },
    "regime_c": {
        "period": "from 1 April 2026",
        "gain": bb_gain,
        "ltcg_tax_with_cess": regC_ltcg_tax,
        "stcg_tax_with_cess": regC_stcg_tax,
        "promoter_effective_rate_noncorp_pct": 30,
        "promoter_effective_rate_corp_pct": 22,
        "promoter_tax_noncorp": regC_promoter_tax_noncorp,
    },
}

# --------------------------------------------------------------------------
# TAX-12  F&O as business income — trader with SEBI's FY26 average loss
# --------------------------------------------------------------------------
fno_yml = yaml.safe_load((ROOT / "_data" / "fno.yml").read_text(encoding="utf-8"))
# SEBI's FY26 average individual loss. Read from fno.yml (its block may be
# renamed as the corroboration status changes); fall back to the same figure.
avg_loss = 117_000
for _block in ("fy26", "fy26_unverified", "fy26_corroborated"):
    if isinstance(fno_yml.get(_block), dict) and "avg_loss_per_trader" in fno_yml[_block]:
        avg_loss = int(fno_yml[_block]["avg_loss_per_trader"])
        break

trades = [60_000, -95_000, 32_000, -74_000, -40_000]
assert sum(trades) == -avg_loss, sum(trades)
turnover = sum(abs(t) for t in trades)
audit_threshold = 10_00_00_000
trades_to_audit = r(audit_threshold / turnover)

salary = 12_00_000
interest = 40_000
stcg = 30_000
setoff_interest = min(avg_loss, interest)
setoff_stcg = min(avg_loss - setoff_interest, stcg)
carried_forward = avg_loss - setoff_interest - setoff_stcg
tax_saved = with_cess(setoff_interest * SLAB + setoff_stcg * STCG_EQ)

presumptive_profit = r(turnover * 0.06)
presumptive_tax = with_cess(presumptive_profit * SLAB)

fno = {
    "note": "Hypothetical trader whose net F&O result equals SEBI's reported FY26 average individual loss (_data/fno.yml). Salary and other incomes are illustrative.",
    "avg_loss": avg_loss,
    "trades": trades,
    "turnover": turnover,
    "audit_threshold": audit_threshold,
    "trades_to_reach_audit_threshold": trades_to_audit,
    "salary": salary,
    "interest_income": interest,
    "stcg": stcg,
    "setoff_against_interest": setoff_interest,
    "setoff_against_stcg": setoff_stcg,
    "carried_forward": carried_forward,
    "carry_forward_years": 8,
    "tax_saved_by_setoff_with_cess": tax_saved,
    "presumptive_rate_pct": 6,
    "presumptive_turnover_limit": 3_00_00_000,
    "presumptive_deemed_profit": presumptive_profit,
    "presumptive_tax_with_cess": presumptive_tax,
}

# --------------------------------------------------------------------------
# TAX-13  Foreign stocks and Schedule FA — hypothetical US purchase
# --------------------------------------------------------------------------
usd_buy = 5_000
fx_buy = 83
usd_sell = 7_000
fx_sell = 86
months_held = 30
inr_cost = r(usd_buy * fx_buy)
inr_sale = r(usd_sell * fx_sell)
fx_gain_inr = inr_sale - inr_cost
fx_currency_component = r(usd_buy * (fx_sell - fx_buy))
fx_ltcg_tax = with_cess(fx_gain_inr * LTCG_EQ)              # no exemption
fx_same_gain_indian_tax = with_cess(max(0, fx_gain_inr - LTCG_EXEMPT) * LTCG_EQ)
fx_stcg_tax_if_within_24m = with_cess(fx_gain_inr * SLAB)

div_usd = 100
div_us_withheld_usd = div_usd * 0.25
div_inr_gross = r(div_usd * fx_sell)
div_us_withheld_inr = r(div_us_withheld_usd * fx_sell)
div_india_tax = with_cess(div_inr_gross * SLAB)
div_india_payable_after_credit = max(0, div_india_tax - div_us_withheld_inr)

lrs_threshold = 10_00_000
lrs_rate = 0.20
lrs_remit_big = 15_00_000
lrs_tcs_big = r((lrs_remit_big - lrs_threshold) * lrs_rate)

foreign = {
    "note": "Hypothetical purchase of US-listed shares; exchange rates are ILLUSTRATIVE stand-ins for the SBI TT buying rate the rules prescribe.",
    "usd_buy": usd_buy, "fx_buy": fx_buy, "inr_cost": inr_cost,
    "usd_sell": usd_sell, "fx_sell": fx_sell, "inr_sale": inr_sale, "fx_change": fx_sell - fx_buy,
    "months_held": months_held,
    "gain_inr": fx_gain_inr,
    "currency_component_inr": fx_currency_component,
    "ltcg_tax_with_cess": fx_ltcg_tax,
    "same_gain_indian_listed_tax_with_cess": fx_same_gain_indian_tax,
    "stcg_tax_with_cess_if_within_24m": fx_stcg_tax_if_within_24m,
    "dividend_usd": div_usd,
    "dividend_us_withheld_usd": r(div_us_withheld_usd),
    "dividend_inr_gross": div_inr_gross,
    "dividend_us_withheld_inr": div_us_withheld_inr,
    "dividend_india_tax_with_cess": div_india_tax,
    "dividend_india_payable_after_credit": div_india_payable_after_credit,
    "lrs_tcs_threshold": lrs_threshold,
    "lrs_tcs_rate_pct": 20,
    "lrs_remit_example": lrs_remit_big,
    "lrs_tcs_example": lrs_tcs_big,
    "bma_penalty": 10_00_000,
    "bma_penalty_exemption_threshold": 20_00_000,
}

# --------------------------------------------------------------------------
# Rules, sources, verification — the part a professional should re-check
# --------------------------------------------------------------------------
verification = {
    "financial_year": "Tax Year 2026-27 (FY 2026-27)",
    "verified_on": "September 2026",
    "how": "Each rule below was checked against at least two public secondary sources on the dates shown. The primary text (Income-tax Act, 2025 / Finance Act, 2026) could not be fetched from incometaxindia.gov.in by automated means, same as the rest of the tax series.",
    "esop": {
        "rules": [
            "Perquisite = FMV on exercise date minus exercise price, taxed as salary at slab in the year of exercise; employer deducts TDS (old s.192; renumbered under the 2025 Act).",
            "RSU: perquisite = full FMV on vesting/settlement (exercise price nil); sell-to-cover is common.",
            "Capital gain at sale = sale price minus the FMV used for the perquisite; holding period runs from exercise/allotment.",
            "Indian listed shares: STCG 20% (<=12 months), LTCG 12.5% above Rs 1.25 lakh. Unlisted or foreign shares: slab up to 24 months, 12.5% beyond, no Rs 1.25 lakh exemption.",
            "Deferral only for employees of DPIIT-recognised startups holding the Inter-Ministerial Board certificate (old s.80-IAC): tax/TDS due within 14 days of the earliest of: 60 months from the end of the relevant tax year (Income-tax Act, 2025, s.289(3) read with s.392(3); the 1961 Act's s.192(1C) said 48 months from the end of the relevant assessment year, i.e. the same point in time), sale of the shares, or leaving the employer. Tax is computed at the rates of the year of exercise; only payment moves.",
        ],
        "sources": [
            "https://cleartax.in/s/taxation-on-esop-rsu-stock-options",
            "https://www.finnovate.in/learn/blog/esop-vs-rsu-taxation-india",
            "https://www.patronaccounting.com/blog/esop-tax-deferral-startup-employees-dpiit-section-80-iac",
            "https://www.equitylist.co/blog-post/perquisite-tax-deferral-startups",
        ],
        "disagreements": "One source phrases the deferral as 'five years from the end of the assessment year'. The 1961 Act (s.192(1C)) said 48 months from the end of the relevant assessment year; the 2025 Act (s.289(3), checked on eztax.in and indiankanoon.org in September 2026) says 60 months from the end of the relevant tax year. The post uses the 2025 Act wording and notes the old one.",
    },
    "buyback": {
        "rules": [
            "Up to 30 Sep 2024: company paid buyback tax (20% + 12% surcharge + 4% cess = 23.296%) on distributed income; shareholder exempt.",
            "1 Oct 2024 to 31 Mar 2026: entire consideration deemed dividend in the shareholder's hands, taxed at slab, TDS 10%, no deduction of cost against it; the cost of the tendered shares becomes a capital loss (sale consideration deemed nil), usable against capital gains and carried forward 8 years.",
            "From 1 Apr 2026 (Finance Act, 2026): buyback consideration taxed as CAPITAL GAINS (consideration minus cost) at the normal equity rates; PLUS an additional tax on PROMOTER shareholders bringing their effective rate to 22% (promoter companies) / 30% (other promoters), with a 12% surcharge prescribed on the additional component.",
        ],
        "sources": [
            "https://taxguru.in/income-tax/budget-2026-buyback-taxation-capital-gains-treatment-shareholders-additional-tax-promoters.html",
            "https://taxguru.in/income-tax/buy-taxation-finance-act-2026-resettling-unsettledae.html",
            "https://www.scconline.com/blog/post/2026/07/16/finance-act-2026-share-buyback-taxation-analysis/",
            "https://vinodkothari.com/2026/02/from-bye-backs-to-buy-backs-how-new-taxation-rules-impact-equity-extraction/",
            "https://taxguru.in/income-tax/buyback-tax-shifted-shareholders-deemed-dividend-october-2024.html",
        ],
        "disagreements": "Whether the Rs 1.25 lakh LTCG exemption applies to buyback gains of listed shares from 1 Apr 2026: the sources describe the gain as taxed 'under the capital gains head at normal rates', which would include the exemption; none states it explicitly. The post says so and flags it for professional confirmation. Promoter definition for unlisted companies (Companies Act promoter or >10% holder) taken from one source.",
    },
    "fno": {
        "rules": [
            "F&O gains/losses are NON-SPECULATIVE business income (intraday equity is speculative, with much tighter set-off rules).",
            "Turnover = sum of absolute profits and losses on closed trades (ICAI Guidance Note, 8th edition, Aug 2022). Premium received on options written is NOT added separately.",
            "Tax audit if turnover exceeds Rs 10 crore where cash receipts and payments are each <=5% (always true for F&O); the Rs 1 crore limit applies otherwise.",
            "Presumptive scheme: declare 6% of digital turnover as profit, available up to Rs 3 crore turnover (95%+ digital). A loss cannot be declared under it. Opting out within 5 years of opting in bars re-entry for 5 years and triggers audit if total income exceeds the basic exemption. Never having opted in, a loss can be declared without audit if turnover is under the threshold.",
            "Same-year set-off against any head EXCEPT salary; carry-forward 8 years against business income only, and ONLY if the return is filed by the due date. Form ITR-3 (ITR-4 only under presumptive).",
            "Expenses deductible against F&O income: brokerage, exchange charges, STT, software, internet, advisory, depreciation on equipment.",
            "STT on futures/options sales rose from 1 April 2026 (futures 0.02% -> 0.05%; options premium 0.10% -> 0.15%; exercised options 0.125% -> 0.15%) announced in the Union Budget 2026-27 and effective 1 April 2026; confirmed across several sources (ICICI Direct, HDFC Securities, ClearTax) in September 2026.",
        ],
        "sources": [
            "https://fnotax.com/articles/fo-taxation-turnover-guide-ay-2026-27-audits-expenses-rules/",
            "https://taxsocial.pro/article/fno-intraday-trading-taxation-ay-2026-27-itr-3-audit-44ad",
            "https://www.balakrishnaandco.com/news-and-articles/56-tax-audit-requirement-for-f-o-trading-fy-2025-26-ay-2026-27",
        ],
        "disagreements": "None material between the two detailed sources. Books-of-account thresholds (income > Rs 1.2 lakh or turnover > Rs 10 lakh) are from one source.",
    },
    "foreign": {
        "rules": [
            "Foreign listed shares: long-term if held more than 24 months; LTCG 12.5% without indexation (sales from 23 July 2024); STCG at slab. The Rs 1.25 lakh exemption does NOT apply (it is for STT-paid Indian equity).",
            "US dividends: 25% withheld in the US under the India-US DTAA; the gross dividend is taxed in India at slab and the US tax is credited via Form 67 (being renumbered). Rule 128(9) as amended by CBDT Notification 100/2022 allows Form 67 up to the end of the assessment year if the return itself is filed in time; filing it with or before the return is the safe route. Credit flows through Schedule FSI and Schedule TR.",
            "Schedule FA (ITR-2/ITR-3) must be filed by every Resident and Ordinarily Resident who held ANY foreign asset at ANY time in the CALENDAR year (1 Jan - 31 Dec) preceding the assessment year: shares, brokerage and bank accounts, RSUs/ESOPs of a foreign employer. No minimum. Report cost, peak value, closing value and income, in INR at the SBI TT buying rate.",
            "Black Money Act: Rs 10 lakh penalty for non-disclosure, not levied where aggregate foreign assets (excluding immovable property) are under Rs 20 lakh (from 1 Oct 2024) — the disclosure duty remains.",
            "TCS on LRS remittances for investment: 20% on the amount above Rs 10 lakh per financial year (threshold unchanged by Budget 2026); recoverable against tax when filing.",
            "Exchange rate for computing gains: the common approach converts each leg at the SBI TT buying rate on the last day of the month preceding the month of purchase/sale. Practice differs (some apply Rule 115 to the gain computed in foreign currency instead) — flagged for professional review.",
        ],
        "sources": [
            "https://vested.blog/posts/schedule-fa-for-ay-2026-27-step-by-step",
            "https://zerodha.com/varsity/chapter/foreign-stocks-and-taxation/",
            "https://www.lakshmisri.com/insights/articles/non-disclosure-of-foreign-assets-in-the-itr-ownership-valuation-threshold-for-penalty-under-the-black-money-act/",
            "https://cleartax.in/s/tax-on-foreign-remittance",
            "https://www.indmoney.com/learn/us-stocks/tax-on-us-stocks",
        ],
        "disagreements": "Sources differ on the exchange-rate DATE for Schedule FA valuation (transaction/valuation date) versus capital-gains computation (last day of the preceding month); the post states both as they apply.",
    },
}

header = """# The Tax Side of Investing — add-on module (TAX-10..13) worked examples.
#
# GENERATED by scripts/derive_tax2.py — do not edit by hand; edit the script
# and re-run it. Every rupee figure in the four posts renders from here.
#
# Same accuracy rules as _data/tax.yml: rates are FY 2026-27, VERIFIED against
# public sources in September 2026 (URLs in the `verification` block), not
# written from memory. The Income-tax Act, 2025 renumbered sections from
# 1 April 2026, so the posts teach mechanics and avoid section numbers.
# Buybacks are the exception where DATES matter: three regimes are shown.
#
# STILL OPEN: have a professional confirm the `verification.*.disagreements`
# items before these posts go out (first publish date 2026-12-14).
"""

data = {
    "verification": verification,
    "esop": esop,
    "buyback": buyback,
    "fno": fno,
    "foreign": foreign,
}

OUT.write_text(header + "\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
for k in ("esop", "buyback", "fno", "foreign"):
    print(k, {kk: vv for kk, vv in data[k].items() if not isinstance(vv, (dict, list, str))})
