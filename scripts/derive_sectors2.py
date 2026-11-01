#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build _data/sectors2.yml — real-company anchors for the Fundamental Analysis
module "More sector lenses" (hospitals, airlines, retail, food delivery).

Same discipline as derive_sectors.py: every reported figure is typed ONCE
below, from the company's own filing (URL beside it); every ratio is computed
here. Re-run, never hand-edit the YAML:

    python3 scripts/derive_sectors2.py

Observables and mechanics only: no valuation, target or verdict on any company.

LAG: all filings cover the year ended 31 March 2026 (FY26) and were released
2 May - 29 May 2026; the earliest post in this file is dated 4 November 2026,
so every figure is more than 5 months old at publication.

SOURCES (primary; opened 1 November 2026):
  Max Healthcare — press release + investor presentation, filed on NSE 21 May 2026
    https://nsearchives.nseindia.com/corporate/MAXHEALTH_21052026163050_SE_Intimation_Final.pdf
  InterGlobe (IndiGo) — press release, presentation and audited results, 29 May 2026
    https://nsearchives.nseindia.com/corporate/Indigo1_29052026161907_Press_Release.pdf
    https://nsearchives.nseindia.com/corporate/Indigo1_29052026161729_Presentation.pdf
    https://nsearchives.nseindia.com/corporate/Indigo1_29052026162550_Outcome_of_BM_29052027.pdf
  Avenue Supermarts (DMart) — press release and investor presentation, 2 May 2026
    https://nsearchives.nseindia.com/corporate/DMART_02052026173007_ASLPressRelease02052026.pdf
  Eternal — Q4 FY26 shareholder letter (includes audited FY26 results)
    https://b.zmtcdn.com/investor-relations/Eternal_Limited_Shareholders_Letter_Q4FY26_Results.pdf
    https://b.zmtcdn.com/investor-relations/d9c290cd23764a09789769c39682276a_1746094084.pdf  (Q4 FY25 letter)
"""
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_data", "sectors2.yml")


def r(x, d=1):
    return round(float(x), d)


def pct(a, b, d=1):
    return r(100.0 * a / b, d)


def growth(new, old, d=1):
    return r(100.0 * (new / old - 1.0), d)


# ---------------------------------------------------------------- Max Healthcare
MAX = dict(
    name="Max Healthcare Institute Ltd",
    source_url="https://nsearchives.nseindia.com/corporate/MAXHEALTH_21052026163050_SE_Intimation_Final.pdf",
    release_date="21 May 2026",
    basis="Network (Max's own 'overall' basis: the company, subsidiaries, managed hospitals and partner facilities); not the statutory consolidated figures",
    gross_revenue_cr=dict(FY26=10538, FY25=9065),
    net_revenue_cr=dict(FY26=10065, FY25=8667),
    ebitda_cr=dict(FY26=2638, FY25=2319),
    pat_cr=dict(FY26=1631, FY25=1336),
    arpob_k=dict(FY26=77.8, FY25=73.9, Q4FY26=77.9, Q4FY25=77.1),
    occupancy_pct=dict(FY26=76, FY25=74, Q4FY26=75, Q4FY25=75),
    alos_days=dict(FY26=4.1, FY25=4.0),
    beds=dict(FY26=4966, FY25=4654),
    beds_added_gross=412, beds_divested=100,
    obd_growth_pct=10,            # printed: "increase in OBDs (+10% YoY)" for FY26
    international_rev_cr=897, international_share_pct=9,
    arpob_growth_printed_pct=5,
    revenue_growth_printed_pct=16,
)


def build_max():
    m = MAX
    d = {}
    d["gross_rev_growth_pct"] = growth(m["gross_revenue_cr"]["FY26"], m["gross_revenue_cr"]["FY25"])
    d["arpob_growth_pct"] = growth(m["arpob_k"]["FY26"], m["arpob_k"]["FY25"])
    assert round(d["arpob_growth_pct"]) == m["arpob_growth_printed_pct"]
    assert round(d["gross_rev_growth_pct"]) == m["revenue_growth_printed_pct"]
    d["net_beds_added"] = m["beds"]["FY26"] - m["beds"]["FY25"]
    assert d["net_beds_added"] == m["beds_added_gross"] - m["beds_divested"]
    d["bed_growth_pct"] = growth(m["beds"]["FY26"], m["beds"]["FY25"])
    d["occupancy_change_pts"] = m["occupancy_pct"]["FY26"] - m["occupancy_pct"]["FY25"]
    # revenue ~ OBD x ARPOB  =>  (1+OBD growth) x (1+ARPOB growth) - 1
    d["obd_times_arpob_pct"] = r(100 * ((1 + m["obd_growth_pct"] / 100) * (1 + d["arpob_growth_pct"] / 100) - 1))
    # OBD = beds x days x occupancy  =>  implied average-bed growth
    d["implied_avg_bed_growth_pct"] = r(100 * ((1 + m["obd_growth_pct"] / 100)
                                               / (m["occupancy_pct"]["FY26"] / m["occupancy_pct"]["FY25"]) - 1))
    d["ebitda_margin_net_fy26"] = pct(m["ebitda_cr"]["FY26"], m["net_revenue_cr"]["FY26"])
    d["ebitda_margin_net_fy25"] = pct(m["ebitda_cr"]["FY25"], m["net_revenue_cr"]["FY25"])
    assert d["ebitda_margin_net_fy26"] == 26.2 and d["ebitda_margin_net_fy25"] == 26.8   # printed
    d["pat_growth_pct"] = growth(m["pat_cr"]["FY26"], m["pat_cr"]["FY25"])
    d["revenue_per_bed_lakh_fy26"] = r(m["gross_revenue_cr"]["FY26"] * 100 / m["beds"]["FY26"], 1)
    m["derived"] = d
    return m


# ---------------------------------------------------------------- InterGlobe
# Rs million as printed; converted to Rs crore (/10) where shown.
IGO = dict(
    name="InterGlobe Aviation Ltd (IndiGo)",
    source_url="https://nsearchives.nseindia.com/corporate/Indigo1_29052026161907_Press_Release.pdf",
    presentation_url="https://nsearchives.nseindia.com/corporate/Indigo1_29052026161729_Presentation.pdf",
    results_url="https://nsearchives.nseindia.com/corporate/Indigo1_29052026162550_Outcome_of_BM_29052027.pdf",
    release_date="29 May 2026",
    basis="Consolidated (press release; audited consolidated results for balance-sheet items)",
    ask_bn=dict(FY26=172.4, FY25=157.5),
    rpk_bn=dict(FY26=145.5, FY25=135.4),
    load_factor_pct=dict(FY26=84.4, FY25=86.0),
    yield_inr=dict(FY26=5.06, FY25=5.15),
    rask_inr=dict(FY26=4.99, FY25=5.14),
    cask_inr=dict(FY26=5.00, FY25=4.66),
    cask_ex_fuel_inr=dict(FY26=3.52, FY25=3.00),
    cask_ex_fuel_ex_forex_inr=dict(FY26=3.00, FY25=2.89),
    fuel_cask_inr=dict(FY26=1.47),
    fuel_cost_mn=dict(FY26=253892, FY25=261973),
    total_income_mn=dict(FY26=895134, FY25=840982),
    revenue_ops_mn=dict(FY26=849619, FY25=808029),
    rask_change_printed_pct=-3.0, cask_change_printed_pct=7.2,
    ebitdar_mn=dict(FY26=150892, FY25=212520),
    ebitdar_ex_forex_mn=dict(FY26=231889, FY25=228612),
    pat_mn=dict(FY26=-23936, FY25=72584),
    profit_ex_forex_exceptional_mn=dict(FY26=75025, FY25=88676),
    passengers_mn=dict(FY26=123.4, FY25=118.6),
    finance_income_mn=dict(FY26=35304, FY25=31119),
    cap_op_lease_mn=dict(FY26=534608),
    total_debt_incl_lease_mn=dict(FY26=777492),
    lease_liab_audited_mn=dict(FY26=759429, FY25=650098),   # non-current + current, audited consolidated balance sheet
    lease_interest_pl_mn=dict(FY26=48059, FY25=41084),
    total_cash_mn=dict(FY26=516506),
    fleet=dict(FY26=441),
)


def build_igo():
    g = IGO
    d = {}
    cr = lambda x: int(round(x / 10.0))
    d["ask_growth_pct"] = growth(g["ask_bn"]["FY26"], g["ask_bn"]["FY25"])
    d["rpk_growth_pct"] = growth(g["rpk_bn"]["FY26"], g["rpk_bn"]["FY25"])
    assert abs(g["rpk_bn"]["FY26"] / g["ask_bn"]["FY26"] * 100 - g["load_factor_pct"]["FY26"]) < 0.2   # LF = RPK/ASK
    assert abs(g["rpk_bn"]["FY25"] / g["ask_bn"]["FY25"] * 100 - g["load_factor_pct"]["FY25"]) < 0.2
    d["load_factor_change_pts"] = r(g["load_factor_pct"]["FY26"] - g["load_factor_pct"]["FY25"])
    d["rask_change_pct"] = growth(g["rask_inr"]["FY26"], g["rask_inr"]["FY25"])
    d["cask_change_pct"] = growth(g["cask_inr"]["FY26"], g["cask_inr"]["FY25"])
    d["yield_change_pct"] = growth(g["yield_inr"]["FY26"], g["yield_inr"]["FY25"])
    d["rask_minus_cask_fy26"] = r(g["rask_inr"]["FY26"] - g["cask_inr"]["FY26"], 2)
    d["rask_minus_cask_fy25"] = r(g["rask_inr"]["FY25"] - g["cask_inr"]["FY25"], 2)
    d["yield_x_lf_fy26"] = r(g["yield_inr"]["FY26"] * g["load_factor_pct"]["FY26"] / 100, 2)
    d["yield_x_lf_fy25"] = r(g["yield_inr"]["FY25"] * g["load_factor_pct"]["FY25"] / 100, 2)
    d["rask_gap_over_yield_lf_fy26"] = r(g["rask_inr"]["FY26"] - d["yield_x_lf_fy26"], 2)
    # components: CASK ex fuel + fuel CASK ~ CASK (rounding)
    assert abs(g["cask_ex_fuel_inr"]["FY26"] + g["fuel_cask_inr"]["FY26"] - g["cask_inr"]["FY26"]) <= 0.02
    d["forex_in_cask_ex_fuel_fy26"] = r(g["cask_ex_fuel_inr"]["FY26"] - g["cask_ex_fuel_ex_forex_inr"]["FY26"], 2)
    d["cask_ex_fuel_ex_forex_change_pct"] = growth(g["cask_ex_fuel_ex_forex_inr"]["FY26"], g["cask_ex_fuel_ex_forex_inr"]["FY25"])
    d["fuel_share_of_cask_pct"] = pct(g["fuel_cask_inr"]["FY26"], g["cask_inr"]["FY26"])
    d["seat_growth_vs_passenger_growth"] = (d["ask_growth_pct"], growth(g["passengers_mn"]["FY26"], g["passengers_mn"]["FY25"]))
    d["passenger_growth_pct"] = d["seat_growth_vs_passenger_growth"][1]
    d["seat_growth_vs_passenger_growth"] = None
    d["total_income_cr"] = cr(g["total_income_mn"]["FY26"])
    d["ebitdar_cr"] = dict(FY26=cr(g["ebitdar_mn"]["FY26"]), FY25=cr(g["ebitdar_mn"]["FY25"]))
    d["ebitdar_ex_forex_cr"] = dict(FY26=cr(g["ebitdar_ex_forex_mn"]["FY26"]), FY25=cr(g["ebitdar_ex_forex_mn"]["FY25"]))
    # printed EBITDAR margins (17.8%, 26.3%) are on revenue from operations
    d["ebitdar_margin_pct"] = dict(FY26=pct(g["ebitdar_mn"]["FY26"], g["revenue_ops_mn"]["FY26"]),
                                   FY25=pct(g["ebitdar_mn"]["FY25"], g["revenue_ops_mn"]["FY25"]))
    assert d["ebitdar_margin_pct"] == dict(FY26=17.8, FY25=26.3), d["ebitdar_margin_pct"]
    d["revenue_ops_cr"] = dict(FY26=cr(g["revenue_ops_mn"]["FY26"]), FY25=cr(g["revenue_ops_mn"]["FY25"]))
    d["pat_cr"] = dict(FY26=cr(g["pat_mn"]["FY26"]), FY25=cr(g["pat_mn"]["FY25"]))
    d["profit_ex_cr"] = dict(FY26=cr(g["profit_ex_forex_exceptional_mn"]["FY26"]), FY25=cr(g["profit_ex_forex_exceptional_mn"]["FY25"]))
    d["fuel_cost_cr"] = dict(FY26=cr(g["fuel_cost_mn"]["FY26"]), FY25=cr(g["fuel_cost_mn"]["FY25"]))
    d["fuel_cost_change_pct"] = growth(g["fuel_cost_mn"]["FY26"], g["fuel_cost_mn"]["FY25"])
    d["cap_op_lease_cr"] = cr(g["cap_op_lease_mn"]["FY26"])
    d["total_debt_cr"] = cr(g["total_debt_incl_lease_mn"]["FY26"])
    d["cap_lease_share_of_debt_pct"] = pct(g["cap_op_lease_mn"]["FY26"], g["total_debt_incl_lease_mn"]["FY26"])
    d["audited_lease_liab_cr"] = dict(FY26=cr(g["lease_liab_audited_mn"]["FY26"]), FY25=cr(g["lease_liab_audited_mn"]["FY25"]))
    d["lease_interest_cr"] = dict(FY26=cr(g["lease_interest_pl_mn"]["FY26"]), FY25=cr(g["lease_interest_pl_mn"]["FY25"]))
    d["total_cash_cr"] = cr(g["total_cash_mn"]["FY26"])
    g["derived"] = d
    return g


# ---------------------------------------------------------------- DMart (standalone)
DM = dict(
    name="Avenue Supermarts Ltd (DMart)",
    source_url="https://nsearchives.nseindia.com/corporate/DMART_02052026173007_ASLPressRelease02052026.pdf",
    release_date="2 May 2026",
    basis="Standalone, as in the company's headline figures and investor presentation",
    revenue_cr=dict(FY26=66968, FY25=57790),
    ebitda_cr=dict(FY26=5255, FY25=4543),
    pat_cr=dict(FY26=3224, FY25=2927),
    stores=dict(FY26=500, FY25=415),
    stores_added=dict(FY26=85, FY25=50),
    area_mn_sqft=dict(FY26=20.6, FY25=17.2),
    sales_per_sqft=dict(FY26=33422, FY25=33896),
    lfl_pct=dict(FY26=8.1, FY25=8.4),
    bills_cr=dict(FY26=39.8, FY25=35.3),
    revenue_growth_printed_pct=15.9,
)


def build_dm():
    m = DM
    d = {}
    d["revenue_growth_pct"] = growth(m["revenue_cr"]["FY26"], m["revenue_cr"]["FY25"])
    assert d["revenue_growth_pct"] == m["revenue_growth_printed_pct"]
    d["ebitda_margin_fy26"] = pct(m["ebitda_cr"]["FY26"], m["revenue_cr"]["FY26"])
    d["ebitda_margin_fy25"] = pct(m["ebitda_cr"]["FY25"], m["revenue_cr"]["FY25"])
    assert d["ebitda_margin_fy26"] == 7.8 and d["ebitda_margin_fy25"] == 7.9   # printed
    d["area_growth_pct"] = growth(m["area_mn_sqft"]["FY26"], m["area_mn_sqft"]["FY25"])
    d["store_growth_pct"] = growth(m["stores"]["FY26"], m["stores"]["FY25"])
    assert m["stores"]["FY26"] - m["stores"]["FY25"] == m["stores_added"]["FY26"]
    d["sales_per_sqft_change_pct"] = growth(m["sales_per_sqft"]["FY26"], m["sales_per_sqft"]["FY25"])
    d["avg_store_size_sqft"] = int(round(m["area_mn_sqft"]["FY26"] * 1e6 / m["stores"]["FY26"], -2))
    d["bills_growth_pct"] = growth(m["bills_cr"]["FY26"], m["bills_cr"]["FY25"])
    d["revenue_per_bill"] = int(round(m["revenue_cr"]["FY26"] / m["bills_cr"]["FY26"], 0))
    d["revenue_per_bill_fy25"] = int(round(m["revenue_cr"]["FY25"] / m["bills_cr"]["FY25"], 0))
    # Illustration of the denominator effect (generic, not a DMart estimate):
    # same sales, area counted at year end vs the average of opening and closing
    avg_area = (m["area_mn_sqft"]["FY26"] + m["area_mn_sqft"]["FY25"]) / 2
    d["avg_area_mn_sqft"] = r(avg_area, 1)
    d["area_growth_vs_revenue_gap_pts"] = r(d["area_growth_pct"] - d["revenue_growth_pct"])
    m["derived"] = d
    return m


# ---------------------------------------------------------------- Eternal food delivery (Rs crore, printed by quarter)
ET = dict(
    name="Eternal Ltd — food delivery segment",
    source_url="https://b.zmtcdn.com/investor-relations/Eternal_Limited_Shareholders_Letter_Q4FY26_Results.pdf",
    fy25_letter_url="https://b.zmtcdn.com/investor-relations/d9c290cd23764a09789769c39682276a_1746094084.pdf",
    release_date="Q4 FY26 shareholder letter (filed May 2026)",
    nov=dict(FY26=[8967, 9423, 9846, 9757], FY25=[7928, 8281, 8443, 8210]),
    adj_rev=dict(FY26=[2657, 2863, 3053, 3125], FY25=[2256, 2340, 2413, 2409]),
    contribution=dict(FY26=[885, 976, 1023, 998], FY25=[673, 735, 843, 842]),
    adj_ebitda=dict(FY26=[451, 503, 531, 532], FY25=[313, 341, 423, 428]),
    # Q4 FY25 letter, on the older GOV basis
    gov_q4fy25=9778, contribution_pct_gov_q4fy25=8.6,
    contribution_pct_nov_q4fy25_printed=10.3,
    q4_nov_growth_printed_pct=18.8,
)


def build_et():
    e = ET
    d = {}
    s = lambda k, y: sum(e[k][y])
    for k in ("nov", "adj_rev", "contribution", "adj_ebitda"):
        d[k + "_fy26"] = s(k, "FY26")
        d[k + "_fy25"] = s(k, "FY25")
    d["nov_growth_pct"] = growth(d["nov_fy26"], d["nov_fy25"])
    d["q4_nov_growth_pct"] = growth(e["nov"]["FY26"][3], e["nov"]["FY25"][3])
    assert d["q4_nov_growth_pct"] == e["q4_nov_growth_printed_pct"]
    d["take_fy26"] = pct(d["adj_rev_fy26"], d["nov_fy26"])
    d["take_fy25"] = pct(d["adj_rev_fy25"], d["nov_fy25"])
    d["take_q4_fy26"] = pct(e["adj_rev"]["FY26"][3], e["nov"]["FY26"][3])
    d["take_q4_fy25"] = pct(e["adj_rev"]["FY25"][3], e["nov"]["FY25"][3])
    d["contrib_pct_nov_fy26"] = pct(d["contribution_fy26"], d["nov_fy26"])
    d["contrib_pct_nov_fy25"] = pct(d["contribution_fy25"], d["nov_fy25"])
    d["contrib_pct_nov_q4_fy25"] = pct(e["contribution"]["FY25"][3], e["nov"]["FY25"][3])
    assert d["contrib_pct_nov_q4_fy25"] == e["contribution_pct_nov_q4fy25_printed"]
    d["contrib_pct_gov_q4_fy25"] = pct(e["contribution"]["FY25"][3], e["gov_q4fy25"])
    assert d["contrib_pct_gov_q4_fy25"] == e["contribution_pct_gov_q4fy25"]
    d["discounts_q4_fy25"] = e["gov_q4fy25"] - e["nov"]["FY25"][3]
    d["discounts_pct_gov_q4_fy25"] = pct(d["discounts_q4_fy25"], e["gov_q4fy25"])
    d["adj_ebitda_pct_nov_fy26"] = pct(d["adj_ebitda_fy26"], d["nov_fy26"])
    d["adj_ebitda_pct_nov_fy25"] = pct(d["adj_ebitda_fy25"], d["nov_fy25"])
    d["adj_rev_growth_pct"] = growth(d["adj_rev_fy26"], d["adj_rev_fy25"])
    d["contribution_growth_pct"] = growth(d["contribution_fy26"], d["contribution_fy25"])
    d["take_change_pts"] = r(d["take_fy26"] - d["take_fy25"])
    d["contrib_change_pts"] = r(d["contrib_pct_nov_fy26"] - d["contrib_pct_nov_fy25"])
    e["derived"] = d
    return e


def main():
    out = {"_comment": "GENERATED by scripts/derive_sectors2.py — edit figures there, not here. "
                       "Real companies: observables and mechanics only.",
           "max": build_max(), "indigo": build_igo(), "dmart": build_dm(), "eternal": build_et()}
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("# GENERATED by scripts/derive_sectors2.py — do not edit by hand.\n")
        yaml.safe_dump(out, fh, sort_keys=False, allow_unicode=True, width=100)
    print("wrote", OUT)
    for k in ("max", "indigo", "dmart", "eternal"):
        print(k, out[k]["derived"])


if __name__ == "__main__":
    main()
