#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build _data/case_study_2.yml — the Desi Bites Foods FY26 narrative for
Fundamental Analysis Module 2 ("Reading between the lines").

WHY A SCRIPT: the FY23-FY25 model in _data/case_study.yml is a reconciled
three-statement model, and the seven posts in this module add a fourth year
(FY26, the company's first as a listed entity) plus an ALTERNATE, deliberately
dressed-up FY26 for the forensic post. Every table in those posts is rendered
from the YAML this script emits, and this script ASSERTS that:

  * the FY26 balance sheet balances,
  * FY26 cash flow ties to the balance sheet cash figure,
  * the dressed FY26 also balances and ties (a cooked set of books still has
    to add up — that is exactly why the frauds it imitates are hard to spot),
  * the four FY25 quarters sum to the FY25 year already in case_study.yml,
  * purchase price = identifiable net assets + goodwill.

Change an assumption here, re-run, and every post updates together.

    <venv>/bin/python scripts/build_case_study_2.py

Reads:  _data/case_study.yml   (opening FY25 balances, listing terms, DCF FY26 forecast)
Writes: _data/case_study_2.yml

Everything in here is FICTIONAL, invented for teaching. In particular the
"dressed" FY26 describes techniques, not any real company.
"""
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_data", "case_study.yml")
OUT = os.path.join(ROOT, "_data", "case_study_2.yml")

cs = yaml.safe_load(open(SRC, encoding="utf-8"))
fy25_is = cs["income_statement"]["FY25"]
fy25_bs = cs["balance_sheet"]["FY25"]
listing = cs["listing"]
dcf26 = cs["dcf"]["forecast"][0]
wacc = cs["dcf"]["wacc"]["wacc"]
TAX = cs["dcf"]["assumptions"]["tax_rate"] / 100.0


def r(x, d=0):
    return round(float(x), d) if d else int(round(float(x)))


def pct(a, b, d=1):
    return round(100.0 * a / b, d)


# ----------------------------------------------------------------- the deal
# Desi Bites buys "Chatpata Foods", a smaller regional namkeen brand, on
# 1 October 2025 (start of H2 FY26), for cash, out of the IPO proceeds.
acq = dict(
    target="Chatpata Foods (fictional regional namkeen brand)",
    date="1 October 2025",
    price=600,                       # cash consideration, Rs Lakh
    fixed_assets=200,                # fair value of plant & equipment acquired
    inventory=65,
    receivables=70,
    brand_intangible=70,             # identifiable intangible: the brand, 10-year life
    payables=50,
    h2_revenue=240,                  # six months of acquired sales (annualised ~480)
    h2_cogs=163,                     # 32% gross margin, weaker than Desi Bites' 38.5%
    h2_opex=53,                      # -> H2 EBITDA 24, a 10% margin
    h2_depreciation=12,
    h2_brand_amortisation=7,         # 70 / 10 years
    integration_costs=35,            # one-off: stamp duty, advisers, rebranding -> exceptional item
)
acq["identifiable_net_assets"] = (acq["fixed_assets"] + acq["inventory"] + acq["receivables"]
                                  + acq["brand_intangible"] - acq["payables"])
acq["goodwill"] = acq["price"] - acq["identifiable_net_assets"]
acq["h2_ebitda"] = acq["h2_revenue"] - acq["h2_cogs"] - acq["h2_opex"]
acq["h2_ebit"] = acq["h2_ebitda"] - acq["h2_depreciation"] - acq["h2_brand_amortisation"]
acq["goodwill_pct_of_price"] = pct(acq["goodwill"], acq["price"])
acq["ebitda_margin_h2"] = pct(acq["h2_ebitda"], acq["h2_revenue"])
# first-year return on the money spent: annualised H2 EBIT after tax / price
acq["year1_roic_pct"] = round(100.0 * acq["h2_ebit"] * 2 * (1 - TAX) / acq["price"], 1)
acq["price_to_h2_revenue_annualised"] = round(acq["price"] / (acq["h2_revenue"] * 2), 2)

# ------------------------------------------------------- FY26, honest version
# Organic business tracks the DCF's FY26 forecast (18% growth, ~17% EBITDA
# margin, capex Rs 245 Lakh) — that forecast was made for the organic business
# and the acquisition sits on top of it.
org_revenue = r(dcf26["revenue"])                     # 3059
org_gm_pct = 38.5
org_cogs = r(org_revenue * (1 - org_gm_pct / 100))    # 1881
org_opex = 655
org_ebitda = org_revenue - org_cogs - org_opex        # 523 (17.1%)
org_dep = r(dcf26["depreciation"])                    # 138
org_capex = r(dcf26["capex"])                         # 245

ipo_cash = listing["ipo_proceeds"]                    # 1600
other_income = 85                                     # interest on IPO cash parked in FDs: ~1600 x 6.5% x 6/12 + ~1000 x 6.5% x 6/12
interest = 42                                         # term loan 400 -> 340 during the year
loan_repaid = 60
dividend_per_share = 9.0
shares = listing["post_ipo_shares_lakh"]              # 12.5
dividend = r(dividend_per_share * shares)             # 112 (Rs Lakh, 12.5 lakh shares x Rs 9)

revenue = org_revenue + acq["h2_revenue"]
cogs = org_cogs + acq["h2_cogs"]
gross_profit = revenue - cogs
opex = org_opex + acq["h2_opex"]
ebitda = gross_profit - opex
depreciation = org_dep + acq["h2_depreciation"]
amortisation = acq["h2_brand_amortisation"]
ebit = ebitda - depreciation - amortisation
exceptional = -acq["integration_costs"]
pbt = ebit + other_income + exceptional - interest
tax = r(pbt * TAX)
pat = pbt - tax

# closing balance sheet (FY26 honest)
inv_days, rec_days, pay_days = 48, 28, 42
inventory = r(org_cogs * inv_days / 365.0) + acq["inventory"]
receivables = r(org_revenue * rec_days / 365.0) + r(acq["h2_revenue"] * 2 * rec_days / 365.0)
payables = r(org_cogs * pay_days / 365.0) + r(acq["h2_cogs"] * 2 * pay_days / 365.0)
ocl = 95
nfa = fy25_bs["net_fixed_assets"] + org_capex + acq["fixed_assets"] - depreciation
intangible = acq["brand_intangible"] - amortisation
goodwill = acq["goodwill"]
term_loan = fy25_bs["term_loan"] - loan_repaid
equity = fy25_bs["equity"] + ipo_cash + pat - dividend

# cash flow (indirect). Working-capital changes EXCLUDE the balances that
# arrived with the acquisition — those are part of the purchase price in CFI.
d_inventory = inventory - fy25_bs["inventory"] - acq["inventory"]
d_receivables = receivables - fy25_bs["receivables"] - acq["receivables"]
d_payables = payables - fy25_bs["payables"] - acq["payables"]
d_ocl = ocl - fy25_bs["other_current_liabilities"]
cfo = pat + depreciation + amortisation - d_inventory - d_receivables + d_payables + d_ocl
cfi = -org_capex - acq["price"]
cff = ipo_cash - loan_repaid - dividend
net_change = cfo + cfi + cff
cash = fy25_bs["cash"] + net_change

total_assets = nfa + intangible + goodwill + inventory + receivables + cash
total_liab_eq = equity + term_loan + payables + ocl
assert total_assets == total_liab_eq, (total_assets, total_liab_eq)

honest = dict(
    revenue=revenue, organic_revenue=org_revenue, acquired_revenue=acq["h2_revenue"],
    cogs=cogs, gross_profit=gross_profit, opex=opex, ebitda=ebitda,
    depreciation=depreciation, amortisation=amortisation, ebit=ebit,
    other_income=other_income, exceptional_items=exceptional, interest=interest,
    pbt=pbt, tax=tax, pat=pat, dividend=dividend, dividend_per_share=dividend_per_share,
    eps=round(pat / shares, 2),
    balance_sheet=dict(net_fixed_assets=nfa, brand_intangible=intangible, goodwill=goodwill,
                       inventory=inventory, receivables=receivables, cash=cash,
                       total_assets=total_assets, equity=equity, term_loan=term_loan,
                       payables=payables, other_current_liabilities=ocl,
                       total_liab_eq=total_liab_eq),
    cash_flow=dict(cfo=cfo, cfi=cfi, cff=cff, net_change=net_change,
                   opening_cash=fy25_bs["cash"], closing_cash=cash,
                   capex=org_capex, acquisition=acq["price"], ipo_proceeds=ipo_cash,
                   loan_repaid=loan_repaid, dividend_paid=dividend),
    ratios=dict(
        revenue_growth=pct(revenue - fy25_is["revenue"], fy25_is["revenue"]),
        organic_revenue_growth=pct(org_revenue - fy25_is["revenue"], fy25_is["revenue"]),
        gross_margin=pct(gross_profit, revenue), organic_gross_margin=org_gm_pct,
        ebitda_margin=pct(ebitda, revenue), organic_ebitda_margin=pct(org_ebitda, org_revenue),
        net_margin=pct(pat, revenue),
        pat_growth=pct(pat - fy25_is["pat"], fy25_is["pat"]),
        ocf_pat=round(cfo / pat, 2),
        receivable_days=r(receivables / revenue * 365.0),
        inventory_days=r(inventory / cogs * 365.0),
        capex_intensity=pct(org_capex, revenue),
        other_income_pct_pbt=pct(other_income, pbt),
        other_income_pct_pat=pct(other_income * (1 - TAX), pat),
        goodwill_pct_equity=pct(goodwill, equity),
        goodwill_pct_total_assets=pct(goodwill, total_assets),
        roe_on_closing_equity=pct(pat, equity),
        roe_fy25_closing=pct(fy25_is["pat"], fy25_bs["equity"]),
        pat_ex_other_income_and_exceptional=r(pat - other_income * (1 - TAX) - exceptional * (1 - TAX)),
    ),
)

# ------------------------------------------------------ FY26, dressed version
# Same real business, four cosmetic decisions by management. Invented.
dress = dict(
    channel_stuffing_revenue=150,   # March "sales" to distributors who did not order; COGS at 62%
    capitalised_opex=60,            # marketing + repairs booked as fixed assets instead of expenses
    capitalised_extra_dep=3,        # depreciation on the newly "capitalised" spend
    rp_asset_sale_price=55,         # old machinery sold to a promoter-owned entity...
    rp_asset_book_value=20,         # ...at nearly 3x book. Gain sits in "other income".
    provision_reversal=20,          # accrued expenses written back through opex
)
cs_cogs = r(dress["channel_stuffing_revenue"] * 0.62)
d_revenue = revenue + dress["channel_stuffing_revenue"]
d_cogs = cogs + cs_cogs
d_gp = d_revenue - d_cogs
d_opex = opex - dress["capitalised_opex"] - dress["provision_reversal"]
d_ebitda = d_gp - d_opex
d_dep = depreciation + dress["capitalised_extra_dep"]
d_ebit = d_ebitda - d_dep - amortisation
rp_gain = dress["rp_asset_sale_price"] - dress["rp_asset_book_value"]
d_other = other_income + rp_gain
d_pbt = d_ebit + d_other + exceptional - interest
d_tax = r(d_pbt * TAX)
d_pat = d_pbt - d_tax

d_inventory = inventory - cs_cogs
d_receivables_bal = receivables + dress["channel_stuffing_revenue"]
d_nfa = nfa + dress["capitalised_opex"] - dress["capitalised_extra_dep"] - dress["rp_asset_book_value"]
d_ocl = ocl - dress["provision_reversal"]
d_equity = fy25_bs["equity"] + ipo_cash + d_pat - dividend
# cash: the same cash was spent either way, except the related-party sale
# brought in 55, and the extra tax on the dressed profit went out.
d_cash = cash + dress["rp_asset_sale_price"] - (d_tax - tax)
d_total_assets = d_nfa + intangible + goodwill + d_inventory + d_receivables_bal + d_cash
d_total_liab_eq = d_equity + term_loan + payables + d_ocl
assert d_total_assets == d_total_liab_eq, (d_total_assets, d_total_liab_eq)

dd_inventory = d_inventory - fy25_bs["inventory"] - acq["inventory"]
dd_receivables = d_receivables_bal - fy25_bs["receivables"] - acq["receivables"]
dd_ocl = d_ocl - fy25_bs["other_current_liabilities"]
d_cfo = (d_pat + d_dep + amortisation - rp_gain
         - dd_inventory - dd_receivables + d_payables + dd_ocl)
d_cfi = -(org_capex + dress["capitalised_opex"]) - acq["price"] + dress["rp_asset_sale_price"]
d_cff = cff
d_net_change = d_cfo + d_cfi + d_cff
assert fy25_bs["cash"] + d_net_change == d_cash, (fy25_bs["cash"] + d_net_change, d_cash)

dressed = dict(
    techniques=dress,
    revenue=d_revenue, cogs=d_cogs, gross_profit=d_gp, opex=d_opex, ebitda=d_ebitda,
    depreciation=d_dep, amortisation=amortisation, ebit=d_ebit, other_income=d_other,
    related_party_gain=rp_gain, exceptional_items=exceptional, interest=interest,
    pbt=d_pbt, tax=d_tax, pat=d_pat, eps=round(d_pat / shares, 2),
    balance_sheet=dict(net_fixed_assets=d_nfa, brand_intangible=intangible, goodwill=goodwill,
                       inventory=d_inventory, receivables=d_receivables_bal, cash=d_cash,
                       total_assets=d_total_assets, equity=d_equity, term_loan=term_loan,
                       payables=payables, other_current_liabilities=d_ocl,
                       total_liab_eq=d_total_liab_eq),
    cash_flow=dict(cfo=d_cfo, cfi=d_cfi, cff=d_cff, net_change=d_net_change,
                   closing_cash=d_cash, capex_reported=org_capex + dress["capitalised_opex"]),
    ratios=dict(
        revenue_growth=pct(d_revenue - fy25_is["revenue"], fy25_is["revenue"]),
        gross_margin=pct(d_gp, d_revenue),
        ebitda_margin=pct(d_ebitda, d_revenue),
        net_margin=pct(d_pat, d_revenue),
        pat_growth=pct(d_pat - fy25_is["pat"], fy25_is["pat"]),
        pat_uplift_vs_honest=pct(d_pat - pat, pat),
        ocf_pat=round(d_cfo / d_pat, 2),
        receivable_days=r(d_receivables_bal / d_revenue * 365.0),
        inventory_days=r(d_inventory / d_cogs * 365.0),
        capex_intensity=pct(org_capex + dress["capitalised_opex"], d_revenue),
        other_income_pct_pbt=pct(d_other, d_pbt),
        cfo_uplift_vs_honest=pct(d_cfo - cfo, cfo),
    ),
)

# ------------------------------------------------------------- quarterlies
# Seasonality of a snacks business: the festive Q3 (Oct-Dec) is the big one.
shares_q = dict(Q1=0.22, Q2=0.24, Q3=0.30, Q4=0.24)
margin_q25 = dict(Q1=15.5, Q2=16.5, Q3=19.0, Q4=16.5)
fy25_q = {}
for q, s in shares_q.items():
    rev = round(fy25_is["revenue"] * s, 1)
    fy25_q[q] = dict(revenue=rev, ebitda=round(rev * margin_q25[q] / 100, 1), ebitda_margin=margin_q25[q])
assert abs(sum(v["revenue"] for v in fy25_q.values()) - fy25_is["revenue"]) < 0.5
assert abs(sum(v["ebitda"] for v in fy25_q.values()) - fy25_is["ebitda"]) < 1.0

fy26_q = {}
margin_q26 = dict(Q1=15.7, Q2=16.7)
acq_q = dict(Q3=130, Q4=110)
for q in ("Q1", "Q2"):
    rev = round(org_revenue * shares_q[q], 1)
    e = round(rev * margin_q26[q] / 100, 1)
    fy26_q[q] = dict(revenue=rev, ebitda=e, ebitda_margin=margin_q26[q],
                     yoy_revenue_growth=pct(rev - fy25_q[q]["revenue"], fy25_q[q]["revenue"]),
                     yoy_ebitda_growth=pct(e - fy25_q[q]["ebitda"], fy25_q[q]["ebitda"]))
fy26_q["Q1"]["qoq_revenue_growth"] = pct(fy26_q["Q1"]["revenue"] - fy25_q["Q4"]["revenue"], fy25_q["Q4"]["revenue"])
fy26_q["Q2"]["qoq_revenue_growth"] = pct(fy26_q["Q2"]["revenue"] - fy26_q["Q1"]["revenue"], fy26_q["Q1"]["revenue"])
# the trap: Q3 FY25 vs Q1 FY26 (festive quarter vs lean quarter)
q3_vs_q1 = pct(fy26_q["Q1"]["revenue"] - fy25_q["Q3"]["revenue"], fy25_q["Q3"]["revenue"])
ttm_after_q2 = round(fy25_q["Q3"]["revenue"] + fy25_q["Q4"]["revenue"] + fy26_q["Q1"]["revenue"] + fy26_q["Q2"]["revenue"], 1)
ttm_ebitda_after_q2 = round(fy25_q["Q3"]["ebitda"] + fy25_q["Q4"]["ebitda"] + fy26_q["Q1"]["ebitda"] + fy26_q["Q2"]["ebitda"], 1)
quarterly = dict(
    seasonality_shares_pct={q: int(s * 100) for q, s in shares_q.items()},
    FY25=fy25_q, FY26=fy26_q,
    festive_quarter="Q3 (October to December: Diwali, the wedding season, winter snacking)",
    q1fy26_vs_q3fy25_pct=q3_vs_q1,
    ttm_after_q2_fy26=dict(revenue=ttm_after_q2, ebitda=ttm_ebitda_after_q2,
                           revenue_growth_vs_fy25=pct(ttm_after_q2 - fy25_is["revenue"], fy25_is["revenue"])),
    acquired_revenue_by_quarter=acq_q,
)

# -------------------------------------------------- shareholding + contingents
promoter_shares = listing["pre_ipo_shares_lakh"]
pledged = 1.5
sh = dict(
    as_of="31 December 2025 (quarterly shareholding pattern filed with the exchange)",
    total_shares_lakh=shares,
    promoter_shares_lakh=promoter_shares,
    promoter_pct=pct(promoter_shares, shares),
    public_shares_lakh=shares - promoter_shares,
    public_pct=pct(shares - promoter_shares, shares),
    pledged_shares_lakh=pledged,
    pledge_date="12 December 2025",
    pledged_pct_of_promoter_holding=pct(pledged, promoter_shares),
    pledged_pct_of_total=pct(pledged, shares),
    pledged_value_at_ipo_price=r(pledged * listing["ipo_price"]),   # Rs Lakh
    pledge_purpose="Loan to a promoter-group entity for an unrelated real-estate venture (per the disclosure)",
    loan_against_pledge=600,   # Rs Lakh, ~62% loan-to-value at the IPO price
    ltv_at_ipo_price=pct(600, pledged * listing["ipo_price"]),
    price_fall_to_breach_ltv_75_pct=round(100 * (1 - 600 / (0.75 * pledged * listing["ipo_price"])), 1),
    promoter_lockin="Minimum promoter contribution locked in for three years from listing; the rest for one year",
)
contingent = dict(
    gst_demand=120,          # Rs Lakh, classification dispute FY23-FY24, under appeal, not provided
    gst_description="GST demand for FY23-FY24 on classification of a product line at 18% instead of 12%; under appeal, not provided for",
    bank_guarantees=25,      # performance guarantees to a modern-trade customer
    total=145,
    pct_of_equity=pct(145, equity),
    pct_of_fy26_pat=pct(145, pat),
    pct_of_cash=pct(145, cash),
)

# ------------------------------------------------------- capital allocation
uses = [
    dict(option="Hold as cash / fixed deposits", amount=None,
         expected_return_pct=round(6.5 * (1 - TAX), 1), basis="FD rate 6.5% pre-tax, ~4.9% post-tax"),
    dict(option="Repay the term loan", amount=term_loan,
         expected_return_pct=round(cs["dcf"]["wacc"]["cost_of_debt_after_tax"], 1), basis="saves after-tax interest"),
    dict(option="Organic capex (new line)", amount=org_capex,
         expected_return_pct=cs["ratios"]["FY25"]["roce"], basis="if it earns the existing business's ROCE"),
    dict(option="Acquisition (Chatpata Foods)", amount=acq["price"],
         expected_return_pct=acq["year1_roic_pct"], basis="year-one, on H2 numbers annualised"),
    dict(option="Dividend", amount=dividend,
         expected_return_pct=None, basis="returns capital; the shareholder decides"),
    dict(option="Buyback", amount=None,
         expected_return_pct=None, basis="returns capital; earnings yield at the price paid"),
]
capital_allocation = dict(
    hurdle_wacc=wacc,
    ipo_proceeds=ipo_cash,
    deployed_fy26=dict(acquisition=acq["price"], capex_from_proceeds=org_capex,
                       still_in_cash=r(cash - fy25_bs["cash"])),
    cash_pile_fy26=cash,
    cash_pct_of_total_assets=pct(cash, total_assets),
    idle_cash_drag_pct_points=round(wacc - 6.5 * (1 - TAX), 1),
    earnings_yield_at_ipo_price=pct(honest["eps"], listing["ipo_price"], 2),
    acquisition_case=dict(
        year1_roic=acq["year1_roic_pct"],
        management_case_revenue=480 * 1.15,
        management_case_ebit_margin=13.5,
        management_case_roic=round(100 * 480 * 1.15 * 0.135 * (1 - TAX) / acq["price"], 1),
    ),
    options=uses,
)

# ------------------------------------------------------------------ DRHP
issue = listing["ipo_proceeds"]
drhp = dict(
    filed="Draft red herring prospectus filed with the exchange in March 2025 (fictional)",
    issue_type="100% fresh issue; no offer for sale",
    fresh_issue_shares_lakh=listing["fresh_issue_shares_lakh"],
    ofs_shares_lakh=0,
    price=listing["ipo_price"],
    issue_size=issue,
    objects=[
        dict(object="Capital expenditure: second production line", amount=700, pct=pct(700, issue)),
        dict(object="Inorganic growth / acquisitions", amount=500, pct=pct(500, issue)),
        dict(object="Working capital", amount=250, pct=pct(250, issue)),
        dict(object="General corporate purposes", amount=150, pct=pct(150, issue)),
    ],
    gcp_cap_note="SEBI's ICDR regulations cap 'general corporate purposes' at 25% of the amount raised",
    actual_use_by_fy26_end=dict(capex=org_capex, acquisitions=acq["price"], working_capital=0,
                                unspent=r(ipo_cash - org_capex - acq["price"])),
    deviation_note="Acquisitions ran Rs 100 Lakh over the stated object; capex ran Rs 455 Lakh under. Listed companies must report such deviations to the exchange every quarter until the money is spent.",
    valuation_at_issue=dict(
        pe_diluted=round(listing["ipo_price"] / listing["eps_diluted"], 1),
        pe_undiluted=round(listing["ipo_price"] / listing["eps_undiluted"], 1),
        pb=round(listing["ipo_price"] / listing["book_value_per_share"], 2),
        ev_ebitda=round(listing["ev"] / fy25_is["ebitda"], 1),
        market_cap=listing["market_cap"],
    ),
    related_party=dict(
        entity="Sharma Distributors (owned by the promoter's brother)",
        share_of_fy25_revenue_pct=9.0,
        fy25_revenue_via_rp=r(fy25_is["revenue"] * 0.09),
        credit_terms="45 days vs 30 for other distributors",
    ),
    risk_factors=[
        "Dependence on a single manufacturing unit in one state",
        "Edible oil and flour make up roughly 55% of raw material cost; no hedging",
        "Nine per cent of revenue flows through a promoter-group distributor",
        "The brand is registered but a similar mark is under dispute in one state",
        "No prior experience as a listed company; the CFO joined eight months before filing",
        "GST classification dispute for FY23-FY24 (see contingent liabilities)",
    ],
    promoter=dict(holding_pre_ipo_pct=100, holding_post_ipo_pct=pct(promoter_shares, shares),
                  background="Founder and spouse; founder ran the family's wholesale namkeen trade before setting up the plant in 2015"),
)

# ------------------------------------------------------------- annual report
annual_report = dict(
    fy="FY26 (year ended 31 March 2026), the first annual report as a listed company",
    approx_pages=140,
    sections=[
        dict(name="Chairman's letter", pages="2", who_writes="Management", read_order=5,
             what_it_is="Tone and priorities. Written to reassure. Read it last, and compare with what the numbers said."),
        dict(name="Management discussion & analysis (MD&A)", pages="12", who_writes="Management", read_order=3,
             what_it_is="Management's own explanation of the year: volumes, prices, costs, segments. The only place the 'why' is written down."),
        dict(name="Directors' report", pages="18", who_writes="Board", read_order=6,
             what_it_is="Statutory disclosures: dividend recommended, directors' changes, CSR, energy. Mostly boilerplate; the related-party (AOC-2) annexure is the exception."),
        dict(name="Corporate governance report", pages="15", who_writes="Board", read_order=7,
             what_it_is="Board composition, committee meetings, remuneration. Skim for independent-director resignations and attendance."),
        dict(name="Independent auditor's report", pages="6", who_writes="Auditor", read_order=1,
             what_it_is="Opinion (unmodified / qualified / adverse / disclaimer), Key Audit Matters, emphasis-of-matter paragraphs. Six pages that can change everything."),
        dict(name="Financial statements", pages="5", who_writes="Management (audited)", read_order=2,
             what_it_is="Balance sheet, P&L, cash flow, statement of changes in equity. The five pages this blog spent thirty posts on."),
        dict(name="Notes to accounts", pages="70", who_writes="Management (audited)", read_order=4,
             what_it_is="Half the report. Accounting policies, related parties, contingent liabilities, borrowings, revenue by segment, tax reconciliation. Where the bodies are buried."),
        dict(name="Shareholding pattern & other information", pages="12", who_writes="Company secretary", read_order=8,
             what_it_is="Who owns what, pledges, top-ten holders, distribution of holdings."),
    ],
    notes_to_read_first=[
        dict(note="Significant accounting policies", why="Revenue recognition and capitalisation policy set the rules for every number that follows."),
        dict(note="Related party transactions (Ind AS 24)", why="Every rupee that crossed between the company and people who control it."),
        dict(note="Contingent liabilities and commitments (Ind AS 37)", why="Claims not yet on the balance sheet."),
        dict(note="Borrowings", why="Maturity, security, covenants, and any default."),
        dict(note="Trade receivables ageing", why="Whether the debtor-days number is one big slow customer or many small ones."),
        dict(note="Business combinations (Ind AS 103)", why="What was bought, what was paid, and how much of it is goodwill."),
        dict(note="Exceptional items and other income", why="The two lines that most often flatter a bad year or hide a good one."),
    ],
    kam_example="Revenue recognition around the year-end (cut-off) — a standard Key Audit Matter for a distributor-led business",
)

out = dict(
    _note="Fictional. Generated by scripts/build_case_study_2.py from _data/case_study.yml; do not edit by hand.",
    company=dict(name="Desi Bites Foods Ltd", fy="FY26 (year ended 31 March 2026)",
                 currency_note="All figures in Rs Lakh unless noted", shares_lakh=shares,
                 opening_balances="FY25 closing balances from _data/case_study.yml"),
    acquisition=acq,
    fy26=honest,
    fy26_dressed=dressed,
    quarterly=quarterly,
    shareholding=sh,
    contingent_liabilities=contingent,
    capital_allocation=capital_allocation,
    drhp=drhp,
    annual_report=annual_report,
)

HEADER = """# Desi Bites Foods Ltd — FY26, the first year as a listed company.
# GENERATED by scripts/build_case_study_2.py from _data/case_study.yml. Do not
# edit by hand: change the script, re-run, and every post in Fundamental
# Analysis Module 2 ("Reading between the lines") updates together.
#
# Everything here is FICTIONAL, invented for teaching. `fy26` is the honest set
# of accounts; `fy26_dressed` is the SAME business with four cosmetic
# decisions layered on, for the forensic post. Both balance and both tie —
# the script asserts it. The acquisition, pledge, GST dispute and DRHP are
# narrative beats for this module, not derived from any real company.
"""
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HEADER)
    yaml.safe_dump(out, f, sort_keys=False, allow_unicode=True, width=100)

print("FY26 honest : revenue %d ebitda %d (%.1f%%) pat %d cfo %d cash %d  assets %d = %d" % (
    revenue, ebitda, honest["ratios"]["ebitda_margin"], pat, cfo, cash, total_assets, total_liab_eq))
print("FY26 dressed: revenue %d ebitda %d (%.1f%%) pat %d cfo %d cash %d  assets %d = %d" % (
    d_revenue, d_ebitda, dressed["ratios"]["ebitda_margin"], d_pat, d_cfo, d_cash, d_total_assets, d_total_liab_eq))
print("goodwill %d  ocf/pat honest %.2f dressed %.2f  debtor days %d vs %d" % (
    goodwill, honest["ratios"]["ocf_pat"], dressed["ratios"]["ocf_pat"],
    honest["ratios"]["receivable_days"], dressed["ratios"]["receivable_days"]))
print("wrote", OUT)
