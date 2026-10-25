#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by the Money Before Markets posts and write them to _data/mbm.yml.

    python3 scripts/derive_mbm.py          # rewrites _data/mbm.yml

Every number a post renders comes from _data/mbm.yml. Market figures are READ from the generated
data the other series already publish (_data/mf4.yml for the liquid and gilt funds, _data/risk2.yml
for CPI and the SBI one-year deposit rate); rules and auction results are TYPED ONCE below, each
next to the primary document it was read from. Illustrative households and balances are labelled
as such in the output.

The first post publishes 8 November 2026, so the 3-month cutoff is 8 August 2026. Every market
series here ends on or before 31 March 2026; the RBI auction result is dated 19 June 2026.

Posts covered: emergency fund, fixed deposit vs debt fund, G-secs and T-bills, PPF, NPS, ULIP, REIT (EPF has no data yet:
its primary sources were unreachable).
"""
import os
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_data", "mbm.yml")


def load(name):
    with open(os.path.join(ROOT, "_data", name), encoding="utf-8") as f:
        return yaml.safe_load(f)


mf4 = load("mf4.yml")
risk2 = load("risk2.yml")
lo = mf4["liquid_overnight"]
liq = lo["funds"]["liquid"]
gilt = lo["funds"]["gilt"]
ovn = lo["funds"]["overnight"]
fy_labels = lo["fy_labels"]
infl_rows = {r["fy"]: r for r in risk2["inflation"]["rows"]}

assert fy_labels == ["FY22", "FY23", "FY24", "FY25", "FY26"], fy_labels
assert mf4["sources"]["end"] == "2026-03-31"

# ---------------------------------------------------------------- 1. emergency fund
# An illustrative household. Nothing here is a recommendation; the inputs only show the arithmetic.
essentials = [
    ("Rent", 22000),
    ("Groceries and household", 12000),
    ("Loan EMIs", 10000),
    ("School fees", 6000),
    ("Transport", 5000),
    ("Utilities and phone", 4000),
    ("Insurance premiums", 3000),
]
other = [("Eating out, travel, subscriptions", 9000)]
ess_total = sum(v for _, v in essentials)
all_total = ess_total + sum(v for _, v in other)
assert ess_total == 62000 and all_total == 71000

months = [3, 6, 12]  # shown only to make the target scale; not a recommended setting
targets = [{"months": m, "essentials": m * ess_total, "everything": m * all_total} for m in months]

buffer_amt = 6 * ess_total  # the six-month row of the table above
fy26 = fy_labels.index("FY26")
liq_fy26 = liq["fy_returns_pct"][fy26]
cpi_fy26 = infl_rows["FY26"]["cpi_pct"]
assert abs(cpi_fy26 - 3.4) < 1e-9
liq_end = round(buffer_amt * (1 + liq_fy26 / 100))
real_liq_pct = round(((1 + liq_fy26 / 100) / (1 + cpi_fy26 / 100) - 1) * 100, 2)
cash_power = round(buffer_amt / (1 + cpi_fy26 / 100))  # what buffer_amt of idle cash buys a year on

emergency = {
    "essentials": [{"item": k, "monthly": v} for k, v in essentials],
    "other": [{"item": k, "monthly": v} for k, v in other],
    "essentials_total": ess_total,
    "all_total": all_total,
    "targets": targets,
    "buffer": buffer_amt,
    "buffer_months": 6,
    "fy26": {
        "liquid_return_pct": liq_fy26,
        "liquid_end": liq_end,
        "cpi_pct": cpi_fy26,
        "liquid_real_pct": real_liq_pct,
        "cash_purchasing_power": cash_power,
        "cash_loss": buffer_amt - cash_power,
    },
    "liquid": {
        "name": mf4["sources"]["funds"]["liquid"]["name"],
        "down_days": liq["down_days"],
        "days": liq["days"],
        "down_days_share_pct": liq["down_days_share_pct"],
        "worst_day_pct": liq["worst_day_pct"],
        "worst_day_date": liq["worst_day_date"],
        "max_drawdown_pct": liq["max_drawdown"]["pct"],
        "cagr_5y_pct": liq["cagr_5y_pct"],
    },
    "overnight": {
        "name": mf4["sources"]["funds"]["overnight"]["name"],
        "down_days": ovn["down_days"],
        "days": ovn["days"],
    },
    "gilt": {
        "name": mf4["sources"]["funds"]["gilt"]["name"],
        "max_drawdown_pct": gilt["max_drawdown"]["pct"],
        "peak_date": gilt["max_drawdown"]["peak_date"],
        "trough_date": gilt["max_drawdown"]["trough_date"],
        "recovered_date": gilt["max_drawdown"]["recovered_date"],
    },
    "window": lo["window"],
}

# ---------------------------------------------------------------- 2. fixed deposit vs debt fund
fd_rows = []
v_fd = v_liq = v_gilt = 100000.0
for i, lab in enumerate(fy_labels):
    r = infl_rows[lab]
    fd = float(r["fd_nominal_pct"])
    lq = liq["fy_returns_pct"][i]
    gl = gilt["fy_returns_pct"][i]
    v_fd *= 1 + fd / 100
    v_liq *= 1 + lq / 100
    v_gilt *= 1 + gl / 100
    fd_rows.append({
        "fy": lab,
        "sbi_1y_rate_pct": r["fd_rate_pct"],
        "fd_pct": fd,
        "liquid_pct": lq,
        "gilt_pct": gl,
        "cpi_pct": r["cpi_pct"],
        "fd_value": round(v_fd),
        "liquid_value": round(v_liq),
        "gilt_value": round(v_gilt),
    })
assert fd_rows[-1]["gilt_pct"] == 2.67
gilt_above = [r["fy"] for r in fd_rows if r["gilt_pct"] > r["fd_pct"]]
gilt_below = [r["fy"] for r in fd_rows if r["gilt_pct"] < r["fd_pct"]]
assert len(gilt_above) + len(gilt_below) == len(fd_rows)  # no ties
liq_vals = [r["liquid_pct"] for r in fd_rows]
assert min(liq_vals) > 0  # no negative year, asserted before the prose says so
# the deposit-rate path a renewing depositor faced, each 1 April (SBI one-year rate)
rate_path = [{"fy": r["fy"], "rate_pct": r["fd_rate_pct"]}
             for r in risk2["inflation"]["rows"] if r["fy"] in ("FY21", "FY22", "FY23", "FY24", "FY25", "FY26")]
assert rate_path[0]["rate_pct"] > rate_path[1]["rate_pct"]  # the rate you could lock fell between FY21 and FY22

dicgc_limit = 500000
dicgc_balance = 620000  # illustrative total at ONE bank across savings + FD
dicgc = {
    "limit": dicgc_limit,
    "illustrative_balance": dicgc_balance,
    "insured": min(dicgc_limit, dicgc_balance),
    "uninsured": max(0, dicgc_balance - dicgc_limit),
    "split_banks_each": dicgc_balance // 2,
    "split_banks_each_insured": min(dicgc_limit, dicgc_balance // 2),
    "source": {
        "name": "DICGC, A Guide to Deposit Insurance",
        "url": "https://www.dicgc.org.in/guide-to-deposit-insurance",
        "read": "2026-10-25",
        "wording": "Each depositor in a bank is insured upto a maximum of Rs 5,00,000 (Rupees Five Lakhs).",
        "read_lines": [
            "The guide's 'What's Not covered?' list includes: Mutual funds; Stocks and bonds; Exchange Traded Funds (ETFs); Cryptocurrencies; deposits mobilized by NBFCs and Land Development Banks.",
            "FAQ: The deposits kept in different branches of a bank are aggregated for the purpose of insurance cover.",
            "FAQ: The DICGC insures principal and interest upto a maximum amount of Rs 5 lakh.",
            "FAQ: If you have deposits with more than one bank, deposit insurance coverage limit is applied separately to the deposits in each bank.",
        ],
        "note": "The guide page gives no effective date for the limit.",
    },
}
assert dicgc["uninsured"] == 120000

fd_vs_debt = {
    "rows": fd_rows,
    "start_value": 100000,
    "rate_path": rate_path,
    "gilt_above_fd": gilt_above,
    "gilt_below_fd": gilt_below,
    "liquid_min_pct": min(liq_vals),
    "liquid_max_pct": max(liq_vals),
    "gilt_drawdown": emergency["gilt"],
    "fd_source": {
        "name": "SBI retail term deposit rates (historical)",
        "url": risk2["dataset"]["sbi_page_url"],
    },
    "dicgc": dicgc,
}

# ---------------------------------------------------------------- 3. G-secs and T-bills
# RBI press release "Government Stock - Auction Results: Cut-off", 19 June 2026
# https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62972  (read 25 Oct 2026)
auction = [
    # name, coupon %, maturity year, cut-off price, implicit yield at cut-off %, notified cr, accepted cr
    ("6.03% GS 2029", 6.03, 2029, 99.52, 6.2300, 11000, 11000),
    ("6.68% GS 2033", 6.68, 2033, 99.69, 6.7373, 11000, 11000),
    ("7.24% GS 2055", 7.24, 2055, 97.10, 7.4847, 5000, 5000),
    ("7.50% GOI SGrB 2056", 7.50, 2056, 100.52, 7.4551, 5000, 5000),
]
rows = []
for name, c, y, p, yld, n, a in auction:
    # a bond priced below 100 yields more than its coupon; above 100, less (checked, not assumed)
    assert (p < 100) == (yld > c), name
    rows.append({
        "name": name, "coupon_pct": c, "maturity_year": y, "price": p, "yield_pct": yld,
        "notified_cr": n, "accepted_cr": a,
        "gap_pts": round(yld - c, 4),
        "price_text": f"{p:.2f}", "yield_text": f"{yld:.4f}",
        "annual_coupon_per_10k": round(10000 * c / 100, 2),
        "half_yearly_per_10k": round(10000 * c / 100 / 2, 2),
        "half_yearly_text": f"{10000 * c / 100 / 2:.2f}",
        "cost_of_10k_face": round(10000 * p / 100, 2),
    })
short_yield, long_yield = rows[0]["yield_pct"], rows[2]["yield_pct"]
assert short_yield < rows[1]["yield_pct"] < long_yield  # yields rose with maturity at this auction

# RBI's own illustrative T-bill (FAQ "Government Securities Market in India - A Primer", dated 01/04/2020):
# a 91-day bill of Rs 100 face issued at Rs 98.20. An illustration, not an auction result.
tb_face, tb_price, tb_days = 100.0, 98.20, 91
tb_discount = round(tb_face - tb_price, 2)
tb_simple_yield = round((tb_face - tb_price) / tb_price * 365 / tb_days * 100, 2)
assert tb_discount == 1.8 and abs(tb_simple_yield - 7.35) < 0.01

gsec = {
    "auction": {
        "date": "2026-06-19",
        "title": "Government Stock - Auction Results: Cut-off",
        "url": "https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62972",
        "read": "2026-10-25",
        "rows": rows,
        "devolvement": "Devolvement on primary dealers was NIL for all four securities.",
        "n_below_par": sum(1 for r in rows if r["price"] < 100),
    },
    "tbill": {
        "face": tb_face, "price": tb_price, "days": tb_days, "discount": tb_discount,
        "price_text": f"{tb_price:.2f}", "discount_text": f"{tb_discount:.2f}",
        "simple_yield_pct": tb_simple_yield,
        "source": {
            "name": "RBI, Government Securities Market in India - A Primer (FAQ)",
            "url": "https://www.rbi.org.in/commonperson/English/Scripts/FAQs.aspx?Id=711",
            "page_date": "2020-04-01", "read": "2026-10-25",
        },
    },
    "retail_direct": {
        "min_bid_face": 10000, "as_on": "2021-11-12",
        "url": "https://www.rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=3337",
        "read": "2026-10-25",
    },
}


# ---------------------------------------------------------------- 4. PPF
# Public Provident Fund Scheme, 2019, G.S.R. 915(E), 12 December 2019 (India Post PDF, read 25 Oct 2026):
#   para 4  deposit Rs 500 to Rs 1,50,000 a year, multiples of Rs 50; para 7 interest on the lowest balance between the close
#   of the fifth day and the end of each month, credited at the end of the year; para 8 loan after one year and before five
#   years from the end of the year of first deposit, up to 25% of the balance at the end of the second preceding year;
#   para 9 loan interest 1% a year if repaid in 36 months, 6% if not; para 10 withdrawal after five years, up to 50% of the
#   lower of the balance at the end of the fourth preceding year or the preceding year, once a year; maturity 15 years,
#   extension in blocks of five years (para 12). The rate printed in para 7 (7.9%) is the rate at notification; the rate
#   is set by the Ministry of Finance and published by NSI.
# NSI "Public Provident Fund Account Interest Rate Since Inception" (nsiindia.gov.in, Id_Pk=178, read 25 Oct 2026):
ppf_rate_history = [
    ("1986-87 to 1998-99", 12.0), ("1 Mar 2001 to 28 Feb 2002", 9.5), ("1 Mar 2002 to 28 Feb 2003", 9.0),
    ("1 Mar 2003 to 30 Nov 2011", 8.0), ("1 Apr 2012 to 31 Mar 2013", 8.8), ("1 Apr 2013 to 31 Mar 2016", 8.7),
    ("1 Oct 2016 to 31 Mar 2017", 8.0), ("1 Jul 2017 to 31 Dec 2017", 7.8), ("1 Jan 2018 to 30 Sep 2018", 7.6),
    ("1 Oct 2018 to 30 Jun 2019", 8.0), ("1 Jul 2019 to 31 Mar 2020", 7.9), ("1 Apr 2020 onward", 7.1),
]
ppf_rate = 7.1
ppf_limit = 150000
ppf_years = 15
bal = 0.0
ppf_rows = []
for y in range(1, ppf_years + 1):
    start = bal + ppf_limit            # deposit in April, on or before the 5th: earns all twelve months
    interest = start * ppf_rate / 100  # interest is credited only at year end, so no intra-year compounding
    bal = start + interest
    ppf_rows.append({"year": y, "deposited": ppf_limit * y, "interest_year": round(interest), "balance": round(bal)})
ppf_total_in = ppf_limit * ppf_years
ppf_maturity = round(bal)
# the fifth-of-the-month rule: a Rs 1,50,000 deposit made after 5 April earns nothing for April
ppf_miss_april = round(ppf_limit * ppf_rate / 100 / 12, 2)
# the same Rs 1,50,000 as one April deposit vs Rs 12,500 on the 1st of each month (all before the 5th)
ppf_lump_interest = round(ppf_limit * ppf_rate / 100, 2)
ppf_monthly_dep = ppf_limit // 12
ppf_monthly_interest = round(sum(ppf_monthly_dep * k for k in range(1, 13)) * ppf_rate / 100 / 12, 2)
assert ppf_limit % 12 == 0 and ppf_monthly_dep % 50 == 0
assert abs(ppf_lump_interest - 10650.0) < 1e-6 and abs(ppf_monthly_interest - 5768.75) < 1e-6
assert abs(ppf_miss_april - 887.5) < 1e-6
# Illustrations of paras 8 and 10 on the worked example above (constant 7.1%, Rs 1,50,000 each April)
bal_by_year = {r["year"]: r["balance"] for r in ppf_rows}
loan_yr = 3        # first financial year a loan can be applied for when the first deposit is made in year 1
loan_base = bal_by_year[loan_yr - 2]           # balance at the end of the second preceding year
loan_max = round(loan_base * 0.25)
wd_yr = 7          # first financial year a withdrawal can be made (after five years from the end of the year of opening)
wd_candidates = {"fourth_preceding": bal_by_year[wd_yr - 4], "preceding": bal_by_year[wd_yr - 1]}
wd_base = min(wd_candidates.values())
wd_max = round(wd_base * 0.5)
assert loan_yr - 2 == 1 and wd_yr - 4 == 3 and wd_yr - 1 == 6
ppf_loan_wd = {"loan_year": loan_yr, "loan_base": loan_base, "loan_max": loan_max, "wd_year": wd_yr,
               "wd_fourth_preceding_year": wd_yr - 4, "wd_fourth_preceding_balance": wd_candidates["fourth_preceding"],
               "wd_preceding_year": wd_yr - 1, "wd_preceding_balance": wd_candidates["preceding"], "wd_base": wd_base, "wd_max": wd_max}
ppf = {
    "rate_pct": ppf_rate, "rate_history": [{"period": a, "rate_pct": b} for a, b in ppf_rate_history],
    "scheme": {
        "title": "Public Provident Fund Scheme, 2019", "gsr": "G.S.R. 915(E)", "date": "2019-12-12",
        "url": "https://www.indiapost.gov.in/documents/offerings/schemesandservices/posb/PublicProvidentFundScheme2019English.pdf",
        "min_deposit": 500, "max_deposit": ppf_limit, "multiple": 50, "maturity_years": ppf_years, "extension_block_years": 5,
        "rate_printed_in_scheme_pct": 7.9, "loan_pct_of_balance": 25, "loan_rate_in_time_pct": 1, "loan_rate_late_pct": 6,
        "loan_repay_months": 36, "withdraw_pct": 50, "read": "2026-10-25",
    },
    "nsi": {"url": "https://www.nsiindia.gov.in/InternalPage.aspx?Id_Pk=178", "read": "2026-10-25",
            "table_end": "2026-09-30"},
    "dea_om": {"q3_date": "2026-09-30", "q3_period": "1 October 2026 to 31 December 2026",
               "url": "https://dea.gov.in/index.php/budget-division/revision-interest-rates-small-savings-schemes-q3-2026-27"},
    "example": {"rows": ppf_rows, "total_deposited": ppf_total_in, "maturity": ppf_maturity,
                "interest_total": ppf_maturity - ppf_total_in, "balance_after_deposits": ppf_maturity, "miss_april": ppf_miss_april, "miss_april_text": f"{ppf_miss_april:.2f}",
                "loan_wd": ppf_loan_wd, "lump_interest": ppf_lump_interest, "monthly_deposit": ppf_monthly_dep, "monthly_interest": ppf_monthly_interest},
}

# ---------------------------------------------------------------- 5. NPS
# PFRDA (Exits and Withdrawals under the NPS) (Amendment) Regulations, 2025 (Gazette notification 12 Dec 2025, published
# 16 Dec 2025): reg 4(1)(a) non-government subscriber, normal exit: at least 20% of the accumulated pension wealth (APW) to buy an
# annuity; up to Rs 8 lakh may be withdrawn in full; above Rs 8 lakh up to Rs 12 lakh, lump sum up to Rs 6 lakh with the rest by
# systematic unit redemption (SUR) for at least six years or annuity; defer to age 85. reg 4(1)(b) exit before eligibility:
# at least 80% to an annuity; Rs 5 lakh or less may be withdrawn in full. Government sector, reg 3(1)(a): at least 40% to an annuity.
# The 20 July 2026 amendment (notified 13 July 2026) concerns schemes for a specific purpose; it does not change these exits.
# PFRDA FAQ "Exits and Withdrawals from NPS for All Citizen Model" (updated March 2026) qn 18-20 and 54-66.
def nps_normal_exit(apw):
    """Options at normal exit for a non-government subscriber, in rupees, from reg 4(1)(a)."""
    out = {"apw": apw}
    out["annuity_min"] = round(apw * 0.20)
    out["lump_max_option_a"] = apw - out["annuity_min"]            # the 80/20 option, any corpus
    if apw <= 800000:
        out["full_withdrawal"] = True
    elif apw <= 1200000:
        out["lump_max_slab"] = 600000
        out["balance_after_slab_lump"] = apw - 600000              # SUR for at least six years, or annuity
    return out


nps_examples = [nps_normal_exit(a) for a in (600000, 900000, 1300000)]
# reproduce PFRDA's own FAQ illustration (qn 20): A Rs 6 lakh, B Rs 9 lakh, C Rs 13 lakh
assert nps_examples[0]["lump_max_option_a"] == 480000 and nps_examples[0]["annuity_min"] == 120000
assert nps_examples[1]["lump_max_slab"] == 600000 and nps_examples[1]["balance_after_slab_lump"] == 300000
assert nps_examples[1]["lump_max_option_a"] == 720000 and nps_examples[1]["annuity_min"] == 180000
assert nps_examples[2]["lump_max_option_a"] == 1040000 and nps_examples[2]["annuity_min"] == 260000
prem_apw = 1000000
nps_premature = {"apw": prem_apw, "annuity_min": round(prem_apw * 0.80), "lump_max": prem_apw - round(prem_apw * 0.80),
                 "full_withdrawal_up_to": 500000}
own_contrib = 400000
nps_partial = {"own_contributions": own_contrib, "first_max": round(own_contrib * 0.25), "min_years": 3,
               "max_times_before_60": 4, "gap_years_before_60": 4, "pct": 25}
assert nps_partial["first_max"] == 100000
nps = {
    "regs": {
        "title": "PFRDA (Exits and Withdrawals under the National Pension System) (Amendment) Regulations, 2025",
        "notified": "2025-12-12", "published": "2025-12-16",
        "url": "https://www.pfrda.org.in/w/regulatory-framework/regulations/pension-fund-regulatory-and-development-authority-exits-and-withdrawals-under-the-national-pension-system-amendment-regulations-2025",
        "pdf": "https://www.pfrda.org.in/documents/33652/184762/Gazette+PFRDA+Exit+and+Withdrawals+under+the+NPS+Amendment+Regulations+2025.pdf",
        "read": "2026-10-25",
        "amend_2026": {"notified": "2026-07-13", "listed": "2026-07-20",
                       "url": "https://www.pfrda.org.in/w/pension-fund-regulatory-and-development-authority-exits-and-withdrawals-under-the-national-pension-system-amendment-regulations-2026",
                       "subject": "inserts sub-regulations (2) to (4) in regulation 4A on specific-purpose schemes"},
    },
    "faq": {"title": "FAQs - Exits & Withdrawals from NPS for All Citizen Model (updated March 2026)",
            "url": "https://pfrda.org.in/documents/33652/676426/Exits+and+Withdrawals+under+NPS+for+All+Citizen+Model.pdf",
            "read": "2026-10-25"},
    "annuity_min_pct": 20, "annuity_min_govt_pct": 40, "annuity_min_premature_pct": 80,
    "slab_full": 800000, "slab_mid_top": 1200000, "slab_mid_lump_max": 600000, "premature_full": 500000, "defer_age": 85,
    "vesting_years": 15, "vesting_age": 60,
    "examples": nps_examples, "premature": nps_premature, "partial": nps_partial,
}

# ---------------------------------------------------------------- 6. ULIP
# IRDAI Master Circular on Life Insurance Products, Ref IRDAI/ACTL/MSTCIR/MISC/89/6/2024 dated 12 June 2024 (read 25 Oct 2026;
# the circular is reviewed yearly, so check for a later version): lock-in of five years for linked products (summary para);
# para 34 a linked product whose funds are all linked to a publicly available index is index-linked, otherwise a ULIP;
# para 7.15.1 illustrated fund value at maturity at least 90% of total premium paid at 4% gross yield after all deductions;
# para 40 discontinuance during lock-in goes to a discontinued policy fund, minimum guaranteed interest 4% a year (40.1.5).
# The charge CAPS sit in Schedule I of the IRDAI (Insurance Products) Regulations, 2024, which has NOT been read for this post.
ULIP_PREMIUM = 100000
ULIP_YEARS = 10
# ILLUSTRATIVE charges, made up for the arithmetic. They are not any plan's charges and not IRDAI caps.
ALLOC = {1: 0.05, 2: 0.03, 3: 0.03, 4: 0.03, 5: 0.03}   # premium allocation charge by policy year, 0 afterwards
ADMIN_PA = 1200                                         # policy administration charge, Rs a year
FMC = 0.0135                                            # fund management charge, a year, on the fund
# Mortality charge (the cost of the life cover) is left out on purpose, so the rows show the cost of the investment part.


def ulip_fund(gross):
    fund = 0.0
    rows = []
    for y in range(1, ULIP_YEARS + 1):
        alloc = ALLOC.get(y, 0.0)
        invested = ULIP_PREMIUM * (1 - alloc)
        fund_start = fund + invested - ADMIN_PA
        growth = fund_start * gross
        fmc = (fund_start + growth) * FMC
        fund = fund_start + growth - fmc
        rows.append({"year": y, "premium": ULIP_PREMIUM, "allocation_charge": round(ULIP_PREMIUM * alloc),
                     "admin_charge": ADMIN_PA, "fmc": round(fmc), "fund_end": round(fund)})
    return fund, rows


def irr(flows):
    """flows: list of (t_years, amount). Annual IRR by bisection."""
    lo_r, hi_r = -0.5, 1.0
    f = lambda r: sum(a / (1 + r) ** t for t, a in flows)
    for _ in range(200):
        mid = (lo_r + hi_r) / 2
        if f(mid) > 0:
            lo_r = mid
        else:
            hi_r = mid
    return (lo_r + hi_r) / 2


total_prem = ULIP_PREMIUM * ULIP_YEARS
scen = {}
for label, g in (("gross_8", 0.08), ("gross_4", 0.04)):
    fv, rows = ulip_fund(g)
    flows = [(t, -ULIP_PREMIUM) for t in range(ULIP_YEARS)] + [(ULIP_YEARS, fv)]
    net = irr(flows) * 100
    scen[label] = {"gross_pct": g * 100, "fund_value": round(fv), "net_yield_pct": round(net, 2),
                   "reduction_pts": round(g * 100 - net, 2), "pct_of_premiums": round(fv / total_prem * 100, 1), "rows": rows}
# IRDAI para 7.15.1: at 4% gross the illustrated fund value must be at least 90% of premiums paid. The made-up charges must pass.
assert scen["gross_4"]["fund_value"] >= 0.9 * total_prem, scen["gross_4"]
assert scen["gross_8"]["fund_value"] > scen["gross_4"]["fund_value"] > 0
ulip = {
    "circular": {"ref": "IRDAI/ACTL/MSTCIR/MISC/89/6/2024", "date": "2024-06-12", "title": "Master Circular on Life Insurance Products",
                 "url": "https://irdai.gov.in/documents/37343/365525/Master+Circular+on+Life+Insurance+Products.pdf/d7ca89f3-b894-8c93-3e53-d8caf67a8ba6?version=1.1&t=1718190178836",
                 "read": "2026-10-25", "lock_in_years": 5, "illus_floor_pct": 90, "illus_floor_gross_pct": 4, "discontinued_fund_min_pct": 4},
    "inputs": {"premium": ULIP_PREMIUM, "years": ULIP_YEARS, "total_premium": total_prem, "admin": ADMIN_PA, "fmc_pct": FMC * 100,
               "alloc": [{"year": k, "pct": v * 100} for k, v in ALLOC.items()]},
    "low": scen["gross_4"], "high": scen["gross_8"],
    "floor_amount": round(0.9 * total_prem),
}

# ---------------------------------------------------------------- 7. REIT
# SEBI (Real Estate Investment Trusts) Regulations, 2014, notified 26 September 2014: the SEBI-published text read here carries
# footnoted amendments up to 30 November 2016 only; later amendments and the SEBI master circular exist and were NOT read.
# reg 2(1)(zm) REIT = a trust registered under the regulations; (zx) unit = beneficial interest of the REIT; reg 18(4) at least 80% of
# the value of REIT assets in completed and rent-generating properties; reg 18(16) (a) at least 90% of an SPV's net distributable cash
# flows to the REIT, (b) at least 90% of the REIT's net distributable cash flows to unit holders, (c) declared at least once every six
# months and paid within fifteen days of declaration; (aa) a holdco passes on 100% of cash received from SPVs and at least 90% of its own.
reit_assets = 10000   # Rs crore, illustrative
reit_rg_min = reit_assets * 80 // 100
spv_ndcf = 100.0
to_reit = spv_ndcf * 0.90
reit_ndcf = to_reit            # assumes the REIT has no other cash flows; illustrative
to_holders = reit_ndcf * 0.90
units_cr = 9.0                 # crore units, illustrative
per_unit = to_holders / units_cr
assert abs(to_reit - 90.0) < 1e-9 and abs(to_holders - 81.0) < 1e-9 and abs(per_unit - 9.0) < 1e-9
reit = {
    "regs": {"title": "SEBI (Real Estate Investment Trusts) Regulations, 2014", "notified": "2014-09-26",
             "url": "https://www.sebi.gov.in/sebi_data/attachdocs/1411722678653.pdf", "read": "2026-10-25",
             "amendments_in_text_to": "2016-11-30", "assets_min_pct": 80, "dist_pct": 90, "dist_months": 6, "dist_days": 15},
    "assets": {"total_cr": reit_assets, "rent_generating_min_cr": reit_rg_min, "other_max_cr": reit_assets - reit_rg_min},
    "payout": {"spv_ndcf": spv_ndcf, "to_reit_min": to_reit, "reit_ndcf": reit_ndcf, "to_holders_min": to_holders,
               "floor_share_pct": 81, "units_cr": units_cr, "per_unit": per_unit},
}

doc = {
    "_note": "GENERATED by scripts/derive_mbm.py from _data/mf4.yml, _data/risk2.yml and the sourced facts typed in the script. Do not edit by hand.",
    "cutoff": {"first_post": "2026-11-08", "three_month_cutoff": "2026-08-08", "market_data_end": "2026-03-31"},
    "emergency": emergency,
    "fd_vs_debt": fd_vs_debt,
    "gsec": gsec,
    "ppf": ppf,
    "nps": nps,
    "ulip": ulip,
    "reit": reit,
}

with open(OUT, "w", encoding="utf-8") as f:
    f.write("# GENERATED by scripts/derive_mbm.py — do not edit by hand; re-run the script.\n")
    f.write("# Money Before Markets — Module 1 (emergency fund, FD vs debt fund, G-secs and T-bills; PPF, EPF, NPS, ULIP, REIT to follow).\n")
    yaml.safe_dump(doc, f, sort_keys=False, allow_unicode=True, width=120)
print("wrote", OUT)
