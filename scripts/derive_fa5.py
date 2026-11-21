#!/usr/bin/env python3
"""
Derive every figure used by module 5 of "Fundamental Analysis", "Reading the
statements closer" (_data/fa5.yml): consolidated vs standalone, segment
reporting, leases (Ind AS 116), diluted EPS, normalised earnings and sum of the
parts. Roadmap: _review/roadmaps/2026-11-02-fa-m5.md (posts dated 27 January to
1 February 2027).

    python3 scripts/derive_fa5.py        # rewrites _data/fa5.yml

INPUTS (read-only): _data/case_study.yml and _data/case_study_2.yml (Desi Bites
Foods, fictional). Everything here is FICTIONAL. The new facts this module adds
(listed under NEW FACTS) are invented for teaching and kept here so every post
agrees; they are chosen to reconcile exactly with the FY26 consolidated
accounts in case_study_2.yml, and the script asserts that they do.

NEW FACTS (fictional):
  * Chatpata Foods (acquired 1 October 2025) is a 100%-owned subsidiary,
    Chatpata Foods Pvt Ltd. In H2 FY26 it also sold goods to the parent for
    INTRAGROUP_SALES (cost INTRAGROUP_COST), all resold to customers by
    31 March 2026, so no unrealised profit remains in inventory.
  * Chatpata's tax rate CHATPATA_TAX_RATE; its PBT and the parent's follow.
  * The brand intangible (and its amortisation) and goodwill exist only in the
    consolidated accounts: the parent's own books carry "investment in
    subsidiary" at the price paid.
  * Segment assets for Chatpata at 31 March 2026: CHATPATA_SEGMENT_ASSETS.
  * IPO shares allotted ALLOTMENT_DATE (the Friday before the 16 June 2025
    listing); ESOP grants and the FY26 average share price as in ESOP below.
  * Desi Bites' FY26 accounts have no leases; the lease post adds a
    hypothetical five-year warehouse lease (L) on top. The two ESOP grants were
    made before the IPO and had vested by FY26 (illustrative). A hypothetical
    holding company (SOTP) — the latter is not Desi Bites.

SOURCES for the rules the posts describe (MCA's own pages refuse automated
requests; texts read 21 Nov 2026 from mirrors, VERIFY row in TODO.md):
  Ind AS 110 paras 4, 19-22, B86 and Ind AS 116 paras 5, 22, 26, 36-37, 49-50,
  Appendix A (ca2013.com, "valid as on 20/11/2026"); Ind AS 108 paras 5, 7,
  13, 15, 16 (ICAI's 2022-23 Ind AS volume, copy on caalley.com); Ind AS 33
  paras 19-21, 41-47A (ca2013.com PDF of the standard).

Needs pyyaml.
"""
import math
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "fa5.yml"
cs = yaml.safe_load(open(ROOT / "_data/case_study.yml", encoding="utf-8"))
cs2 = yaml.safe_load(open(ROOT / "_data/case_study_2.yml", encoding="utf-8"))
f26, acq, bs = cs2["fy26"], cs2["acquisition"], cs2["fy26"]["balance_sheet"]

INTRAGROUP_SALES, INTRAGROUP_COST = 30, 20
CHATPATA_TAX_RATE = 0.25
CHATPATA_SEGMENT_ASSETS = 690   # its own assets at 31 March 2026 plus the goodwill and brand allocated to it
ALLOTMENT_DATE = date(2025, 6, 13)
FY_START, FY_END = date(2025, 4, 1), date(2026, 3, 31)


def half_up(x, d=2):
    from decimal import Decimal, ROUND_HALF_UP
    return float(Decimal(str(x)).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP))


def r(x, d=1):
    v = round(float(x), d)
    return int(v) if v == int(v) else v


def close(a, b, tol=0.01):
    assert abs(a - b) < tol, (a, b)


# ---------------------------------------------------------------- 1. consolidated vs standalone
c = {k: f26[k] for k in ("revenue", "cogs", "gross_profit", "opex", "ebitda", "depreciation", "amortisation",
                         "ebit", "other_income", "exceptional_items", "interest", "pbt", "tax", "pat")}
sub = {
    "revenue": acq["h2_revenue"] + INTRAGROUP_SALES,
    "cogs": acq["h2_cogs"] + INTRAGROUP_COST,
    "opex": acq["h2_opex"],
    "depreciation": acq["h2_depreciation"],
    "amortisation": 0, "other_income": 0, "exceptional_items": 0, "interest": 0,
}
sub["gross_profit"] = sub["revenue"] - sub["cogs"]
sub["ebitda"] = sub["gross_profit"] - sub["opex"]
sub["ebit"] = sub["ebitda"] - sub["depreciation"]
sub["pbt"] = sub["ebit"]
sub["tax"] = sub["pbt"] * CHATPATA_TAX_RATE
sub["pat"] = sub["pbt"] - sub["tax"]
# consolidation-only items: brand amortisation; eliminations: intragroup sale
elim = {"revenue": -INTRAGROUP_SALES, "cogs": -INTRAGROUP_SALES}
par = {}
par["revenue"] = c["revenue"] - sub["revenue"] - elim["revenue"]
par["cogs"] = c["cogs"] - sub["cogs"] - elim["cogs"]
par["gross_profit"] = par["revenue"] - par["cogs"]
par["opex"] = c["opex"] - sub["opex"]
par["ebitda"] = par["gross_profit"] - par["opex"]
par["depreciation"] = c["depreciation"] - sub["depreciation"]
par["amortisation"] = 0
par["ebit"] = par["ebitda"] - par["depreciation"]
par["other_income"], par["exceptional_items"], par["interest"] = c["other_income"], c["exceptional_items"], c["interest"]
par["pbt"] = par["ebit"] + par["other_income"] + par["exceptional_items"] - par["interest"]
par["tax"] = c["tax"] - sub["tax"]
par["pat"] = par["pbt"] - par["tax"]
assert par["revenue"] == cs2["fy26"]["organic_revenue"] + 0, "parent revenue should equal FY26 organic revenue"
# the consolidated lines must rebuild from parent + subsidiary + adjustments
for k in ("revenue", "cogs"):
    close(par[k] + sub[k] + elim[k], c[k])
for k in ("opex", "depreciation", "tax"):
    close(par[k] + sub[k], c[k])
close(par["ebit"] + sub["ebit"] - c["amortisation"], c["ebit"])
close(par["pat"] + sub["pat"] - c["amortisation"], c["pat"])
# the investment line the consolidation replaces
close(acq["identifiable_net_assets"] + acq["goodwill"], acq["price"])
nci_pct = 20
nci_share = (sub["pat"] - c["amortisation"]) * nci_pct / 100   # Ind AS 110 B88/B94: on the subsidiary's profit in the group accounts (after the brand amortisation); deferred tax ignored
order = ["revenue", "cogs", "gross_profit", "opex", "ebitda", "depreciation", "amortisation", "ebit",
         "other_income", "exceptional_items", "interest", "pbt", "tax", "pat"]
labels = {"revenue": "Revenue", "cogs": "Cost of goods sold", "gross_profit": "Gross profit", "opex": "Operating expenses",
          "ebitda": "EBITDA", "depreciation": "Depreciation", "amortisation": "Brand amortisation", "ebit": "EBIT",
          "other_income": "Other income", "exceptional_items": "Exceptional items", "interest": "Interest",
          "pbt": "Profit before tax", "tax": "Tax", "pat": "Profit after tax"}
adj = {k: 0 for k in order}
adj.update({"revenue": -INTRAGROUP_SALES, "cogs": -INTRAGROUP_SALES, "amortisation": c["amortisation"],
            "ebit": -c["amortisation"], "pbt": -c["amortisation"], "pat": -c["amortisation"]})
rows = [{"line": labels[k], "parent": r(par[k]), "sub": r(sub[k]), "adj": r(adj[k]), "consolidated": r(c[k])} for k in order]
for row in rows:
    close(row["parent"] + row["sub"] + row["adj"], row["consolidated"], 0.06)
out = {"consolidation": {
    "sub_name": "Chatpata Foods Pvt Ltd", "acquired": acq["date"], "ownership_pct": 100,
    "intragroup_sales": INTRAGROUP_SALES, "intragroup_cost": INTRAGROUP_COST,
    "sub_tax_rate_pct": int(CHATPATA_TAX_RATE * 100),
    "rows": rows,
    "parent_ebitda_margin_pct": r(par["ebitda"] / par["revenue"] * 100),
    "sub_ebitda_margin_pct": r(sub["ebitda"] / sub["revenue"] * 100),
    "cons_ebitda_margin_pct": r(c["ebitda"] / c["revenue"] * 100),
    "parent_pat": r(par["pat"]), "cons_pat": r(c["pat"]),
    "investment": acq["price"], "net_assets": acq["identifiable_net_assets"], "goodwill": acq["goodwill"],
    "brand": acq["brand_intangible"], "brand_closing": bs["brand_intangible"],
    "fixed_assets": acq["fixed_assets"], "inventory": acq["inventory"], "receivables": acq["receivables"],
    "payables": acq["payables"],
    "nci_example_pct": nci_pct, "nci_example_share": r(nci_share), "nci_example_owners_pat": r(c["pat"] - nci_share),
}}

# ---------------------------------------------------------------- 2. segments
seg_rev_desi, seg_rev_chat = par["revenue"], sub["revenue"]
seg_ext_desi, seg_ext_chat = par["revenue"], acq["h2_revenue"]
seg_res_desi, seg_res_chat = par["ebit"], sub["ebit"]
assets_total = bs["total_assets"]
unalloc_assets = bs["cash"]               # IPO cash is held centrally, not in either segment
seg_assets_desi = assets_total - unalloc_assets - CHATPATA_SEGMENT_ASSETS
assert seg_assets_desi > 0
comb_rev = seg_rev_desi + seg_rev_chat
comb_res = seg_res_desi + seg_res_chat
comb_assets = seg_assets_desi + CHATPATA_SEGMENT_ASSETS
tests = {"revenue_pct": r(seg_rev_chat / comb_rev * 100), "result_pct": r(seg_res_chat / comb_res * 100),
         "assets_pct": r(CHATPATA_SEGMENT_ASSETS / comb_assets * 100)}
gw_brand = acq["goodwill"] + bs["brand_intangible"]
assets_ex_gw_pct = r((CHATPATA_SEGMENT_ASSETS - gw_brand) / (comb_assets - gw_brand) * 100)
assets_with_cash_pct = r(CHATPATA_SEGMENT_ASSETS / (comb_assets + unalloc_assets) * 100)
meets_any = any(v >= 10 for v in tests.values())
ext_cover = r(seg_ext_desi / c["revenue"] * 100)
# reconciliation of segment results to consolidated PBT
recon_pbt = comb_res - c["amortisation"] + c["other_income"] + c["exceptional_items"] - c["interest"]
close(recon_pbt, c["pbt"])
out["segments"] = {
    "names": ["Desi Bites brand", "Chatpata (regional namkeen)"],
    "desi": {"revenue": r(seg_rev_desi), "external": r(seg_ext_desi), "inter": 0, "result": r(seg_res_desi),
             "margin_pct": r(seg_res_desi / seg_rev_desi * 100), "assets": r(seg_assets_desi),
             "result_on_assets_pct": r(seg_res_desi / seg_assets_desi * 100)},
    "chat": {"revenue": r(seg_rev_chat), "external": r(seg_ext_chat), "inter": INTRAGROUP_SALES, "result": r(seg_res_chat),
             "margin_pct": r(seg_res_chat / seg_rev_chat * 100), "assets": CHATPATA_SEGMENT_ASSETS,
             "result_on_assets_pct": r(seg_res_chat / CHATPATA_SEGMENT_ASSETS * 100),
             "months": 6},
    "combined_revenue": r(comb_rev), "combined_result": r(comb_res), "combined_assets": r(comb_assets),
    "unallocated_assets": r(unalloc_assets), "total_assets": r(assets_total),
    "chat_tests": tests, "chat_meets_threshold": meets_any, "chat_assets_ex_goodwill_brand_pct": assets_ex_gw_pct,
    "chat_assets_if_cash_counted_pct": assets_with_cash_pct, "goodwill_and_brand": r(gw_brand),
    "group_ebit_margin_pct": r(c["ebit"] / c["revenue"] * 100), "combined_result_margin_pct": r(comb_res / comb_rev * 100), "desi_external_cover_pct": ext_cover,
    "recon": {"segment_results": r(comb_res), "brand_amortisation": r(-c["amortisation"]), "other_income": c["other_income"],
              "exceptional": c["exceptional_items"], "interest": -c["interest"], "pbt": r(c["pbt"])},
    "chat_annualised_revenue": r(acq["h2_revenue"] * 2),
}
assert tests["revenue_pct"] < 10 and tests["result_pct"] < 10 and tests["assets_pct"] >= 10, tests  # the post: fails two tests, passes on assets

# ---------------------------------------------------------------- 3. leases (hypothetical, on FY26 figures)
L = {"rent": 60, "years": 5, "rate_pct": 9}
i = L["rate_pct"] / 100
annuity = (1 - (1 + i) ** -L["years"]) / i
liab0 = L["rent"] * annuity
dep = liab0 / L["years"]
sched, bal = [], liab0
for y in range(1, L["years"] + 1):
    interest = bal * i
    principal = L["rent"] - interest
    close_bal = bal - principal
    sched.append({"year": y, "opening": r(bal), "interest": r(interest), "payment": L["rent"], "principal": r(principal),
                  "closing": r(close_bal), "depreciation": r(dep), "charge": r(dep + interest), "rent_charge": L["rent"]})
    bal = close_bal
close(bal, 0, 1e-6)
close(sum(s["charge"] for s in sched), L["rent"] * L["years"], 0.2)
y1 = sched[0]
net_debt = bs["term_loan"] - bs["cash"]
# both cases pay the year's Rs 60 lakh from cash; the lease case also carries the year-end (closing) liability
liab_close = sched[0]["closing"]
rent_case = {"ebitda": c["ebitda"] - L["rent"], "ebit": c["ebit"] - L["rent"], "interest": c["interest"],
             "net_debt": net_debt + L["rent"], "cfo": f26["cash_flow"]["cfo"] - L["rent"]}
lease_case = {"ebitda": c["ebitda"], "ebit": c["ebit"] - dep, "interest": c["interest"] + liab0 * i,
              "net_debt": net_debt + L["rent"] + liab_close, "cfo": f26["cash_flow"]["cfo"]}  # Ind AS 116 para 50: principal AND interest in financing
for case in (rent_case, lease_case):
    case["pbt"] = case["ebit"] + c["other_income"] + c["exceptional_items"] - case["interest"]
    case["ebitda_margin_pct"] = r(case["ebitda"] / c["revenue"] * 100)
    case["interest_cover"] = r(case["ebit"] / case["interest"])
    case["net_debt_ebitda"] = r(case["net_debt"] / case["ebitda"], 2)
    for k in ("ebitda", "ebit", "interest", "net_debt", "pbt", "cfo"):
        case[k] = r(case[k])
out["leases"] = {**L, "liability0": r(liab0), "rou0": r(liab0), "depreciation": r(dep), "schedule": sched,
                 "total_charge": L["rent"] * L["years"], "rent_case": rent_case, "lease_case": lease_case,
                 "y1_charge_minus_rent": r(y1["charge"] - L["rent"]), "net_debt_fy26": r(net_debt), "liability_close": liab_close}

# ---------------------------------------------------------------- 4. EPS: weighted shares and dilution
pre, fresh = cs["listing"]["pre_ipo_shares_lakh"], cs["listing"]["fresh_issue_shares_lakh"]
days_fy = (FY_END - FY_START).days + 1
days_out = (FY_END - ALLOTMENT_DATE).days + 1
wavg = pre + fresh * days_out / days_fy
ESOP = {"avg_price": 700, "grants": [
    {"name": "Grant A (vested)", "options_lakh": 0.5, "exercise": 400},
    {"name": "Grant B (vested)", "options_lakh": 0.2, "exercise": 760},
]}
pat = c["pat"]
basic = pat / wavg
grants = []
incremental = 0.0
for g in ESOP["grants"]:
    dilutive = g["exercise"] < ESOP["avg_price"]
    bought = g["options_lakh"] * g["exercise"] / ESOP["avg_price"]
    free = g["options_lakh"] - bought
    grants.append({**g, "dilutive": dilutive, "shares_at_market_lakh": r(bought, 4), "free_shares_lakh": r(free, 4)})
    if dilutive:
        incremental += free
diluted = pat / (wavg + incremental)
assert diluted <= basic
naive = pat / (wavg + sum(g["options_lakh"] for g in ESOP["grants"]))
out["eps"] = {
    "pat": pat, "pre_shares_lakh": pre, "fresh_shares_lakh": fresh, "year_end_shares_lakh": pre + fresh,
    "allotment_date": f"{ALLOTMENT_DATE.day} {ALLOTMENT_DATE.strftime('%B %Y')}",
    "listing_date": cs["listing"]["listing_date"], "days_fy": days_fy, "days_outstanding": days_out,
    "wavg_shares_lakh": r(wavg, 4), "basic": half_up(basic), "year_end_eps": r(pat / (pre + fresh), 2),
    "avg_price": ESOP["avg_price"], "grants": grants, "incremental_lakh": r(incremental, 4),
    "diluted_shares_lakh": r(wavg + incremental, 4), "diluted": r(diluted, 2),
    "dilution_pct": r((1 - diluted / basic) * 100, 2), "naive_all_options": r(naive, 2),
}

# ---------------------------------------------------------------- 5. normalised earnings
years = ["FY23", "FY24", "FY25"]
gm = {y: cs["income_statement"][y]["gross_profit"] / cs["income_statement"][y]["revenue"] * 100 for y in years}
gm["FY26"] = c["gross_profit"] / c["revenue"] * 100
gm = {y: round(v, 1) for y, v in gm.items()}   # the post shows one decimal and averages what it shows
OIL = {"oil_share_of_cogs_pct": 55, "spike_pct": 20}   # hypothetical: edible oil and flour ~55% of raw material cost (cs2 annual_report), up 20% in a year
avg_gm = sum(gm.values()) / len(gm)
# a "spike year": same FY26 revenue, but oil-and-flour costs 20% higher
cogs_spike = c["cogs"] * (1 + OIL["oil_share_of_cogs_pct"] / 100 * OIL["spike_pct"] / 100)
eff_tax = c["tax"] / c["pbt"]
cash = bs["cash"]


def pat_from(gross_profit, other_income, exceptional):
    ebit = gross_profit - c["opex"] - c["depreciation"] - c["amortisation"]
    pbt_ = ebit + other_income + exceptional - c["interest"]
    return ebit, pbt_, pbt_ * (1 - eff_tax)


rep_ebit, rep_pbt, rep_pat = pat_from(c["gross_profit"], c["other_income"], c["exceptional_items"])
close(rep_pbt, c["pbt"])
spike_gp = c["revenue"] - cogs_spike
sp_ebit, sp_pbt, sp_pat = pat_from(spike_gp, c["other_income"], c["exceptional_items"])
norm_gp = c["revenue"] * avg_gm / 100
n_ebit, n_pbt, n_pat = pat_from(norm_gp, c["other_income"], 0)
core_ebit, core_pbt, core_pat = pat_from(norm_gp, 0, 0)
shares = pre + fresh
price = cs["listing"]["ipo_price"]
mcap = price * shares               # price (Rs) x shares (lakh) = Rs lakh
out["normalised"] = {
    "gross_margins": [{"fy": y, "pct": f"{v:.1f}"} for y, v in gm.items()], "avg_gm_pct": f"{avg_gm:.2f}",
    "oil_share_pct": OIL["oil_share_of_cogs_pct"], "spike_pct": OIL["spike_pct"],
    "eff_tax_pct": r(eff_tax * 100), "price": price, "shares_lakh": shares, "mcap": r(mcap), "cash": cash,
    "reported": {"gm_pct": r(gm["FY26"]), "ebit": r(rep_ebit), "pbt": r(rep_pbt), "pat": r(rep_pat), "pe": r(mcap / rep_pat)},
    "spike": {"gm_pct": r(spike_gp / c["revenue"] * 100), "ebit": r(sp_ebit), "pbt": r(sp_pbt), "pat": r(sp_pat), "pe": r(mcap / sp_pat)},
    "normal": {"gm_pct": r(avg_gm), "ebit": r(n_ebit), "pbt": r(n_pbt), "pat": r(n_pat), "pe": r(mcap / n_pat)},
    "core": {"ebit": r(core_ebit), "pbt": r(core_pbt), "pat": r(core_pat), "pe_ex_cash": r((mcap - cash) / core_pat)},
    "exceptional": c["exceptional_items"], "other_income": c["other_income"],
}

# ---------------------------------------------------------------- 6. sum of the parts (generic company)
S = {"name": "Sample Holdings Ltd (fictional)", "shares_crore": 50, "net_debt": 2000,
     "parts": [
         {"name": "Packaged foods", "metric": "EBITDA", "value": 800, "multiple": 20},
         {"name": "Cement", "metric": "EBITDA", "value": 600, "multiple": 10},
         {"name": "Stake in a listed associate", "metric": "market value of stake", "value": 3000, "multiple": 1},
     ],
     "discount_on_stake_pct": 20, "holdco_discounts": [0, 10, 20, 30],
     "multiple_shift": 2}
parts = []
gross = 0.0
for p in S["parts"]:
    v = p["value"] * p["multiple"]
    if p["metric"] != "EBITDA":
        v = v * (1 - S["discount_on_stake_pct"] / 100)
    parts.append({**p, "ev": r(v)})
    gross += v
equity = gross - S["net_debt"]
per_share = [{"discount_pct": d, "equity": r(equity * (1 - d / 100)), "per_share": r(equity * (1 - d / 100) / S["shares_crore"])}
             for d in S["holdco_discounts"]]
# sensitivity: food multiple +/- 2
sens = []
for shift in (-S["multiple_shift"], 0, S["multiple_shift"]):
    g2 = gross + S["parts"][0]["value"] * shift
    sens.append({"food_multiple": S["parts"][0]["multiple"] + shift, "per_share": r((g2 - S["net_debt"]) / S["shares_crore"])})
out["sotp"] = {**{k: S[k] for k in ("name", "shares_crore", "net_debt", "discount_on_stake_pct", "multiple_shift")},
               "parts": parts, "gross": r(gross), "equity": r(equity), "per_share": per_share, "sensitivity": sens,
               "food_share_pct": r(parts[0]["ev"] / gross * 100)}
close(sum(p["ev"] for p in parts), gross, 0.5)

OUT.write_text("# Generated by scripts/derive_fa5.py. Do not edit by hand. Desi Bites and Sample Holdings are FICTIONAL.\n"
               + yaml.safe_dump(out, sort_keys=False, allow_unicode=True), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
