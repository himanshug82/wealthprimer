#!/usr/bin/env python3
"""
Derive the figures for Jargon, Decoded module 10, "Ratios and lines readers look
up" (_data/jargon_m10.yml): ROIC, price-to-sales, EBIT and operating profit,
gross block / net block / CWIP, DSCR, and other comprehensive income. Posts
dated 8 to 13 February 2027. Roadmap: _review/roadmaps/2026-11-21-jargon-m10.md

    python3 scripts/derive_jargon_m10.py      # rewrites _data/jargon_m10.yml

INPUTS: _data/case_study.yml (FY22-FY25, listing) and _data/case_study_2.yml (FY26).
Desi Bites Foods is FICTIONAL.

NEW FICTIONAL FACTS (kept here so every post agrees; each reconciles to the
existing books, and the script asserts it):
  * Fixed assets: gross block at 31 March 2022 of GROSS_FY22, accumulated
    depreciation ACC_DEP_FY22 (net 630, as the books show). No disposals.
    FY23-FY25 capex (cash from investing) is all capitalised in the year. In
    FY26, CWIP_FY26 of the 245 capex is a packing line still being built at
    31 March 2026 (capital work-in-progress); Chatpata's 200 of fixed assets
    join gross block at fair value on acquisition.
  * Debt service: principal repaid is the fall in the term loan (FY25: 60;
    FY26: 60, as the FY26 cash flow shows).
  * OCI overlay for the OCI post only (hypothetical, not in the FY26 books the
    other posts use): a gratuity remeasurement loss with assumed tax.

RULE: Ind AS 1 para 7 (definition and components of OCI), para 82A (two
groups) and para 96 (remeasurements are not reclassified), read 21 Nov 2026 in a copy of the notified standard on
ca2013.com (MCA refuses automated requests).

Needs pyyaml.
"""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "jargon_m10.yml"
cs = yaml.safe_load(open(ROOT / "_data/case_study.yml", encoding="utf-8"))
cs2 = yaml.safe_load(open(ROOT / "_data/case_study_2.yml", encoding="utf-8"))
IS, BS, CF = cs["income_statement"], cs["balance_sheet"], cs["cash_flow"]
f26, b26 = cs2["fy26"], cs2["fy26"]["balance_sheet"]

GROSS_FY22, ACC_DEP_FY22 = 1050, 420
CWIP_FY26 = 70


def r(x, d=1):
    v = round(float(x), d)
    return int(v) if v == int(v) else v


def close(a, b, tol=0.05):
    assert abs(a - b) < tol, (a, b)


out = {}

# ---------------------------------------------------------------- 1. ROIC vs ROCE
def year(fy):
    if fy == "FY24":
        i, b = IS["FY24"], BS["FY24"]
        return {"ebit": i["ebit"], "tax": i["tax"], "pbt": i["pbt"], "equity": b["equity"], "debt": b["term_loan"],
                "cash": b["cash"], "revenue": i["revenue"]}
    if fy == "FY26":
        return {"ebit": f26["ebit"], "tax": f26["tax"], "pbt": f26["pbt"], "equity": b26["equity"],
                "debt": b26["term_loan"], "cash": b26["cash"], "revenue": f26["revenue"]}
    i, b = IS[fy], BS[fy]
    return {"ebit": i["ebit"], "tax": i["tax"], "pbt": i["pbt"], "equity": b["equity"], "debt": b["term_loan"],
            "cash": b["cash"], "revenue": i["revenue"]}


roic = {}
prev = {"FY25": "FY24", "FY26": "FY25"}
def ic_ce(fy):
    y = year(fy)
    return y["equity"] + y["debt"] - y["cash"], y["equity"] + y["debt"]
for fy in ("FY25", "FY26"):
    y = year(fy)
    t = y["tax"] / y["pbt"]
    nopat = y["ebit"] * (1 - t)
    ic, ce = ic_ce(fy)
    ic0, ce0 = ic_ce(prev[fy])
    ic_avg, ce_avg = (ic + ic0) / 2, (ce + ce0) / 2
    roic[fy] = {"ebit": r(y["ebit"]), "tax_rate_pct": r(t * 100), "nopat": r(nopat), "equity": r(y["equity"]),
                "debt": y["debt"], "cash": y["cash"], "invested_capital": r(ic), "invested_capital_open": r(ic0),
                "invested_capital_avg": r(ic_avg), "capital_employed_avg": r(ce_avg),
                "roic_pct": r(nopat / ic_avg * 100), "roce_pct": r(y["ebit"] / ce_avg * 100),
                "roce_post_tax_pct": r(nopat / ce_avg * 100), "roic_closing_pct": r(nopat / ic * 100)}
assert abs(roic["FY25"]["roce_pct"] - cs["ratios"]["FY25"]["roce"]) < 0.15, "must match the ROCE post"
for fy in ("FY25", "FY26"):
    x = roic[fy]
    x["gap_pts"] = r(x["roic_pct"] - x["roce_post_tax_pct"])
    cash_avg = (year(fy)["cash"] + year(prev[fy])["cash"]) / 2
    x["cash_share_pct"] = r(cash_avg / x["capital_employed_avg"] * 100)
roic["FY26"]["roce_incl_oi_pct"] = r((f26["ebit"] + f26["other_income"]) / roic["FY26"]["capital_employed_avg"] * 100)
roic["FY26"]["other_income"] = f26["other_income"]
roic["FY26"]["cash_rise"] = b26["cash"] - BS["FY25"]["cash"]
out["roic"] = roic

# ---------------------------------------------------------------- 2. price-to-sales
price, shares = cs["listing"]["ipo_price"], cs["listing"]["post_ipo_shares_lakh"]
mcap = price * shares
ps = {}
for fy, rev, pat in (("FY25", IS["FY25"]["revenue"], IS["FY25"]["pat"]), ("FY26", f26["revenue"], f26["pat"])):
    ps[fy] = {"revenue": rev, "pat": pat, "ps": r(mcap / rev, 2), "pe": r(mcap / pat, 1),
              "net_margin_pct": r(pat / rev * 100, 1)}
    close(ps[fy]["ps"], mcap / pat * pat / rev, 0.01)
ev = mcap + b26["term_loan"] - b26["cash"]
ps["FY26"]["ev"] = r(ev)
ps["FY26"]["pe_exact"] = r(mcap / f26["pat"], 2)
ps["FY26"]["margin_exact_pct"] = r(f26["pat"] / f26["revenue"] * 100, 2)
ps["FY26"]["debt"] = b26["term_loan"]
ps["FY26"]["cash"] = b26["cash"]
ps["FY26"]["listing_ev"] = cs["listing"]["ev"]
ps["FY26"]["ev_sales"] = r(ev / f26["revenue"], 2)
# two made-up companies with the same P/S and different margins
gen = [{"name": "Company A", "ps": 2.0, "margin_pct": 15}, {"name": "Company B", "ps": 2.0, "margin_pct": 4}]
for g in gen:
    g["pe"] = r(g["ps"] / (g["margin_pct"] / 100), 1)
out["ps"] = {"price": price, "shares_lakh": shares, "mcap": r(mcap), "years": ps, "generic": gen}

# ---------------------------------------------------------------- 3. EBIT versions (FY26)
e = {"revenue": f26["revenue"], "ebitda": f26["ebitda"], "dep": f26["depreciation"], "amort": f26["amortisation"],
     "operating_ebit": f26["ebit"], "other_income": f26["other_income"], "exceptional": f26["exceptional_items"],
     "interest": f26["interest"], "pbt": f26["pbt"]}
e["ebit_incl_oi"] = e["operating_ebit"] + e["other_income"]
e["ebit_incl_all"] = e["ebit_incl_oi"] + e["exceptional"]
close(e["ebit_incl_all"], e["pbt"] + e["interest"])
for k in ("operating_ebit", "ebit_incl_oi", "ebit_incl_all"):
    e[k + "_margin_pct"] = r(e[k] / e["revenue"] * 100)
    e[k + "_cover"] = r(e[k] / e["interest"], 1)
out["ebit"] = {k: r(v) if isinstance(v, float) else v for k, v in e.items()}

# ---------------------------------------------------------------- 4. gross block, net block, CWIP
rows = []
gross, acc = GROSS_FY22, ACC_DEP_FY22
assert gross - acc == BS["FY22"]["net_fixed_assets"]
rows.append({"fy": "FY22", "gross": gross, "additions": None, "dep": None, "acc_dep": acc, "net": gross - acc, "cwip": 0,
             "fixed_assets": gross - acc})
for fy in ("FY23", "FY24", "FY25"):
    capex = -CF[fy]["cfi"]
    gross += capex
    acc += IS[fy]["depreciation"]
    rows.append({"fy": fy, "gross": gross, "additions": capex, "dep": IS[fy]["depreciation"], "acc_dep": acc,
                 "net": gross - acc, "cwip": 0, "fixed_assets": gross - acc})
    assert gross - acc == BS[fy]["net_fixed_assets"], fy
cap26 = f26["cash_flow"]["capex"]
acq = cs2["acquisition"]["fixed_assets"]
add26 = cap26 - CWIP_FY26 + acq
gross += add26
acc += f26["depreciation"]
rows.append({"fy": "FY26", "gross": gross, "additions": add26, "dep": f26["depreciation"], "acc_dep": acc,
             "net": gross - acc, "cwip": CWIP_FY26, "fixed_assets": gross - acc + CWIP_FY26})
assert gross - acc + CWIP_FY26 == b26["net_fixed_assets"]
for row in rows:
    row["acc_share_pct"] = r(row["acc_dep"] / row["gross"] * 100)
out["blocks"] = {"rows": rows, "capex_fy26": cap26, "acquired": acq, "cwip": CWIP_FY26,
                 "acc_dep_share_pct": r(acc / gross * 100), "acc_dep_share_fy22_pct": r(ACC_DEP_FY22 / GROSS_FY22 * 100),
                 "fy26_net_block": gross - acc, "fy26_gross": gross}

# ---------------------------------------------------------------- 5. DSCR
d = {}
for fy, pat, dep, interest, ebitda, cfo, repaid in (
        ("FY25", IS["FY25"]["pat"], IS["FY25"]["depreciation"], IS["FY25"]["interest"], IS["FY25"]["ebitda"], CF["FY25"]["cfo"],
         BS["FY24"]["term_loan"] - BS["FY25"]["term_loan"]),
        ("FY26", f26["pat"], f26["depreciation"] + f26["amortisation"], f26["interest"], f26["ebitda"], f26["cash_flow"]["cfo"],
         f26["cash_flow"]["loan_repaid"])):
    service = interest + repaid
    d[fy] = {"pat": pat, "da": r(dep), "interest": interest, "repaid": repaid, "service": service, "ebitda": ebitda,
             "cfo": cfo,
             "dscr_lender": r((pat + dep + interest) / service, 2),
             "dscr_ebitda": r(ebitda / service, 2),
             "interest_cover": r(year(fy)["ebit"] / interest, 1)}
assert d["FY26"]["repaid"] == BS["FY25"]["term_loan"] - b26["term_loan"]
# what a heavier repayment year would look like: same FY26 earnings, Rs 340 lakh bullet repayment
d["FY26"]["dscr_lender_ex_oi"] = r((f26["pat"] + f26["depreciation"] + f26["amortisation"] + f26["interest"]
                                    - f26["other_income"] * (1 - f26["tax"] / f26["pbt"])) / (f26["interest"] + d["FY26"]["repaid"]), 2)
d["FY26"]["other_income"] = f26["other_income"]
d["FY26"]["exceptional"] = f26["exceptional_items"]
bullet = b26["term_loan"]
d["bullet"] = {"repaid": bullet, "service": f26["interest"] + bullet,
               "dscr_lender": f'{(f26["pat"] + f26["depreciation"] + f26["amortisation"] + f26["interest"]) / (f26["interest"] + bullet):.2f}'}
out["dscr"] = d

# ---------------------------------------------------------------- 6. OCI overlay (hypothetical)
oci = {"pat": f26["pat"], "gratuity_remeasurement": -8, "gratuity_tax": 2}
oci["not_reclassified"] = oci["gratuity_remeasurement"] + oci["gratuity_tax"]
oci["total_oci"] = oci["not_reclassified"]
oci["tci"] = oci["pat"] + oci["total_oci"]
out["oci"] = {k: r(v) for k, v in oci.items()}
out["oci"]["source_url"] = "https://ca2013.com/rule/indian-accounting-standard-ind-1/"

OUT.write_text("# Generated by scripts/derive_jargon_m10.py. Do not edit by hand. Desi Bites is FICTIONAL.\n"
               + yaml.safe_dump(out, sort_keys=False, allow_unicode=True), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
