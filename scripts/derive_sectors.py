#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build _data/sectors.yml — the real-company anchors for the Fundamental
Analysis module "Sector lenses" (SEC-1..8).

WHY A SCRIPT: same discipline as derive_bank.py. Every figure a post quotes is
either typed ONCE below, straight from the company's own results filing (with
the URL beside it), or computed here from those typed figures. Never edit the
YAML by hand; re-run:

    python3 scripts/derive_sectors.py

WHAT THESE ANCHORS ARE FOR: observables and mechanics only. No valuation, no
discount rate, no target, no verdict on any of these companies. Each anchor
illustrates how a sector's own metrics work; it is not a view on the company.

LAG: every filing below was released between 16 April and 13 May 2026 and
covers the year ended 31 March 2026 (FY26). The first post in the module is
dated 16 October 2026, so every figure is more than 5 months old at
publication — well past the house 3-month rule.

SOURCES (all primary — the company's own filing, exchange filing or SEC
exhibit; fetched September 2026):
  Infosys     — IFRS INR/USD press releases and Fact Sheet, Q4 and FY26,
                23 April 2026, furnished to the US SEC on Form 6-K (exhibits
                99.1, 99.2, 99.4).
  Marico      — "Information Update for Q4FY26", filed with the exchanges
                5 May 2026 (marico.com).
  UltraTech   — press release "Financial Results Q4FY26", 27 April 2026
                (ultratechcement.com).
  Dr. Reddy's — "Q4 & Full Year FY26 Financial Results" press release (IFRS),
                12 May 2026, furnished to the US SEC on Form 6-K (exhibit 99.2).
  HDFC Life   — "Press release – performance for twelve months ended March
                31, 2026", 16 April 2026 (hdfclife.com).
  Bajaj Fin.  — "Q4 FY26 Investor Presentation", 29 April 2026
                (bajajfinserv.in CDN).
  Airtel      — "Media Release May 13, 2026" (Q4 FY26), airtel.in.
Regulatory:
  RBI FAQ "All you wanted to know about NBFCs" (updated as on 15 September
  2026): NBFCs cannot accept demand deposits; public deposits 12–60 months;
  no DICGC insurance. https://www.rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=1167
"""
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml (use the project venv)")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "_data", "sectors.yml")


def r(x, d=1):
    v = round(float(x), d)
    return int(v) if d == 0 else v


def pct(a, b, d=1):
    """a as % of b"""
    return r(100.0 * a / b, d)


def growth(new, old, d=1):
    return r(100.0 * (new / old - 1.0), d)


def close(a, b, tol):
    return abs(a - b) <= tol


# =====================================================================
# 1. INFOSYS — IT services
# =====================================================================
INFY_URL = "https://www.sec.gov/Archives/edgar/data/1067491/000106749126000018/exv99w02.htm"
INFY_USD_URL = "https://www.sec.gov/Archives/edgar/data/1067491/000106749126000018/exv99w01.htm"
INFY_FACT_URL = "https://www.sec.gov/Archives/edgar/data/1067491/000106749126000018/exv99w04.htm"
INFY = dict(
    rev_usd_m=dict(FY26=20158, FY25=19277),
    rev_inr_cr=dict(FY26=178650, FY25=162990),
    cc_growth_fy26_pct=3.1,                   # as printed
    op_profit_cr=dict(FY26=36254, FY25=34424),
    op_margin_pct=dict(FY26=20.3, FY25=21.1),  # reported IFRS
    op_margin_adjusted_fy26_pct=21.0,          # excl. Labour Codes one-off (Rs 1,289 cr)
    labour_code_charge_cr=1289,
    large_deal_tcv_usd_bn=14.9, large_deal_net_new_pct=55,
    fcf_usd_m=3733,
    total_equity_cr=dict(FY26=93297, FY25=96203),
    guidance_fy27_cc="1.5%-3.5%",
    # Fact Sheet, quarter ended 31 Mar 2026 vs 31 Mar 2025 (same exhibit set)
    q4=dict(
        utilisation_incl_trainees=dict(Q4FY26=79.7, Q4FY25=81.9),
        utilisation_excl_trainees=dict(Q4FY26=83.0, Q4FY25=84.9),
        attrition_ltm=dict(Q4FY26=12.6, Q4FY25=14.1),
        employees=dict(Q4FY26=328594, Q4FY25=323578),
        onsite_effort=dict(Q4FY26=22.8, Q4FY25=23.6),
        top10_clients_pct=dict(Q4FY26=20.2, Q4FY25=20.7),
        dso_days=dict(Q4FY26=67, Q4FY25=69),
        clients_100m_plus=dict(Q4FY26=41, Q4FY25=39),
        active_clients=dict(Q4FY26=1965, Q4FY25=1869),
        yoy_reported_pct=6.6, yoy_cc_pct=4.1,
        geography=[  # share of Q4FY26 revenue, YoY reported, YoY CC
            dict(region="North America", share=55.7, reported=4.1, cc=4.1),
            dict(region="Europe", share=32.6, reported=11.4, cc=4.1),
            dict(region="Rest of the world", share=9.1, reported=9.3, cc=5.0),
            dict(region="India", share=2.6, reported=-5.2, cc=0.0),
        ],
    ),
)


def build_infosys():
    i = INFY
    d = {}
    d["usd_growth_pct"] = growth(i["rev_usd_m"]["FY26"], i["rev_usd_m"]["FY25"])
    d["inr_growth_pct"] = growth(i["rev_inr_cr"]["FY26"], i["rev_inr_cr"]["FY25"])
    assert d["usd_growth_pct"] == 4.6 and d["inr_growth_pct"] == 9.6, d   # both printed in the releases
    # implied average rupees per dollar: Rs crore * 1e7 / (USD m * 1e6)
    fx26 = i["rev_inr_cr"]["FY26"] * 10 / i["rev_usd_m"]["FY26"]
    fx25 = i["rev_inr_cr"]["FY25"] * 10 / i["rev_usd_m"]["FY25"]
    d["implied_inr_per_usd_fy26"] = r(fx26, 2)
    d["implied_inr_per_usd_fy25"] = r(fx25, 2)
    d["rupee_weakening_pct"] = growth(fx26, fx25)
    d["check_usd_factor"] = "%.3f" % (1 + d["usd_growth_pct"] / 100)
    d["check_fx_factor"] = "%.3f" % (1 + d["rupee_weakening_pct"] / 100)
    d["check_inr_factor"] = "%.3f" % (1 + d["inr_growth_pct"] / 100)
    d["check_product"] = "%.3f" % ((1 + d["usd_growth_pct"] / 100) * (1 + d["rupee_weakening_pct"] / 100))
    d["cross_currency_effect_pts"] = r(d["usd_growth_pct"] - i["cc_growth_fy26_pct"], 1)
    d["inr_vs_cc_gap_pts"] = r(d["inr_growth_pct"] - i["cc_growth_fy26_pct"], 1)
    # identity check: (1+usd)*(1+fx) ~= (1+inr)
    assert close((1 + d["usd_growth_pct"] / 100) * (1 + d["rupee_weakening_pct"] / 100),
                 1 + d["inr_growth_pct"] / 100, 0.002)
    q = i["q4"]
    avg_emp = (q["employees"]["Q4FY26"] + q["employees"]["Q4FY25"]) / 2
    d["avg_employees"] = r(avg_emp, 0)
    d["rev_per_employee_usd"] = r(i["rev_usd_m"]["FY26"] * 1e6 / avg_emp, -2)
    d["rev_per_employee_usd"] = int(d["rev_per_employee_usd"])
    d["rev_per_employee_inr_lakh"] = r(i["rev_inr_cr"]["FY26"] * 100 / avg_emp, 1)
    d["employee_change"] = q["employees"]["Q4FY26"] - q["employees"]["Q4FY25"]
    d["employee_growth_pct"] = growth(q["employees"]["Q4FY26"], q["employees"]["Q4FY25"])
    d["utilisation_change_pts"] = r(q["utilisation_excl_trainees"]["Q4FY26"] - q["utilisation_excl_trainees"]["Q4FY25"], 1)
    d["attrition_change_pts"] = r(q["attrition_ltm"]["Q4FY26"] - q["attrition_ltm"]["Q4FY25"], 1)
    d["tcv_to_revenue_x"] = r(i["large_deal_tcv_usd_bn"] * 1000 / i["rev_usd_m"]["FY26"], 2)
    d["op_profit_growth_pct"] = growth(i["op_profit_cr"]["FY26"], i["op_profit_cr"]["FY25"])
    avg_eq = (i["total_equity_cr"]["FY26"] + i["total_equity_cr"]["FY25"]) / 2
    # Infosys reports no borrowings on the extract (only lease liabilities), so
    # operating profit / average total equity is a ROCE-style, pre-tax return.
    d["op_profit_to_avg_equity_pct"] = pct(i["op_profit_cr"]["FY26"], avg_eq)
    d["op_margin_check_pct"] = pct(i["op_profit_cr"]["FY26"], i["rev_inr_cr"]["FY26"])
    assert d["op_margin_check_pct"] == i["op_margin_pct"]["FY26"]
    g = q["geography"]
    assert close(sum(x["share"] for x in g), 100.0, 0.05)
    for x in g:
        x["fx_effect_pts"] = r(x["reported"] - x["cc"], 1)
    return dict(
        name="Infosys Ltd", exchange="NSE: INFY, BSE: 500209, NYSE: INFY",
        basis="Consolidated, IFRS (audited condensed statements); operating metrics from the Fact Sheet",
        as_of="FY26 (year ended 31 March 2026), released 23 April 2026",
        release_date="23 April 2026",
        source_url=INFY_URL, source_usd_url=INFY_USD_URL, fact_sheet_url=INFY_FACT_URL,
        source_label="IFRS press releases and Fact Sheet, Q4 and FY26 (Form 6-K exhibits, 23 April 2026)",
        cc_definition=("CC growth compares current-period revenue in each local currency, converted to US$ "
                       "at the prior period's exchange rates, with prior-period reported revenue (company's note)."),
        reported=i, derived=d,
    )


# =====================================================================
# 2. MARICO — FMCG
# =====================================================================
MARICO_URL = "https://marico.com/investorspdf/Information_Update_Q4FY26.pdf"
MARICO = dict(
    fy26=dict(revenue_cr=13611, revenue_growth_pct=26, ebitda_cr=2328, ebitda_growth_pct=9,
              ebitda_margin_pct=17.1, ebitda_margin_change_bps=-265,
              pat_excl_oneoffs_cr=1762, pat_growth_pct=11,
              domestic_volume_growth_pct=8, international_ccg_pct=20),
    q4=dict(revenue_cr=3333, revenue_growth_pct=22, ebitda_cr=521, ebitda_margin_pct=15.6,
            ebitda_margin_change_bps=-114, domestic_volume_growth_pct=9, international_ccg_pct=19,
            india_revenue_cr=2505, india_revenue_growth_pct=21,
            gross_margin_change_yoy_bps_approx=-360, gross_margin_change_qoq_bps_approx=140,
            ad_promo_growth_pct=5,
            parachute_rigids=dict(reported_volume_growth_pct=-1, revenue_growth_pct=29),
            vaho_value_growth_pct=26, saffola_oils_revenue_growth_pct=8,
            copra_off_peak_pct_approx=35),
)


def build_marico():
    m = MARICO
    q = m["q4"]
    d = {}
    # Revenue growth = (1 + volume) x (1 + price/mix) - 1  -> implied price/mix
    d["q4_india_implied_price_mix_pct"] = r(100 * ((1 + q["india_revenue_growth_pct"] / 100)
                                                   / (1 + q["domestic_volume_growth_pct"] / 100) - 1), 1)
    pr = q["parachute_rigids"]
    d["parachute_implied_realisation_growth_pct"] = r(100 * ((1 + pr["revenue_growth_pct"] / 100)
                                                             / (1 + pr["reported_volume_growth_pct"] / 100) - 1), 1)
    d["q4_rev_factor"] = "%.2f" % (1 + q["india_revenue_growth_pct"] / 100)
    d["q4_vol_factor"] = "%.2f" % (1 + q["domestic_volume_growth_pct"] / 100)
    d["q4_india_gap_pts"] = q["india_revenue_growth_pct"] - q["domestic_volume_growth_pct"]
    # FY25 margin implied by the printed FY26 margin and bps change (both rounded, so "about")
    d["fy26_ebitda_margin_prev_pct"] = r(m["fy26"]["ebitda_margin_pct"] - m["fy26"]["ebitda_margin_change_bps"] / 100, 1)
    d["gross_margin_yoy_bps_abs"] = abs(q["gross_margin_change_yoy_bps_approx"])
    d["ebitda_margin_fy_bps_abs"] = abs(m["fy26"]["ebitda_margin_change_bps"])
    d["ebitda_margin_q4_bps_abs"] = abs(q["ebitda_margin_change_bps"])
    d["parachute_volume_decline_pct"] = abs(q["parachute_rigids"]["reported_volume_growth_pct"])
    d["india_share_of_q4_revenue_pct"] = pct(q["india_revenue_cr"], q["revenue_cr"], 0)
    assert d["q4_india_implied_price_mix_pct"] > 0 and d["parachute_implied_realisation_growth_pct"] > 25
    # sanity: EBITDA margin printed vs computed
    assert close(pct(m["fy26"]["ebitda_cr"], m["fy26"]["revenue_cr"]), m["fy26"]["ebitda_margin_pct"], 0.1)
    assert close(pct(q["ebitda_cr"], q["revenue_cr"]), q["ebitda_margin_pct"], 0.1)
    return dict(
        name="Marico Ltd", exchange="NSE: MARICO, BSE: 531642",
        basis="Consolidated; company's quarterly Information Update (filed with the exchanges)",
        as_of="FY26 and Q4 FY26 (year/quarter ended 31 March 2026), released 5 May 2026",
        release_date="5 May 2026",
        source_url=MARICO_URL,
        source_label="Information Update for Q4FY26, 5 May 2026",
        reported=m, derived=d,
    )


# =====================================================================
# 3. ULTRATECH CEMENT — cement
# =====================================================================
UTCL_URL = "https://www.ultratechcement.com/corporate/media/press-releases/financial-results-q4fy26"
UTCL = dict(
    net_sales_cr=dict(FY26=87384, FY25=74936, Q4FY26=25467, Q4FY25=22788),
    pbidt_cr=dict(FY26=17598, FY25=13302, Q4FY26=5688, Q4FY25=4721),
    pat_excl_exceptional_cr=dict(FY26=8305, FY25=6115),
    india_grey_volume_mt=dict(Q4FY26=42.41, FY26=145.0),
    india_grey_volume_growth_q4_pct=9.3,
    capacity_utilisation_q4_pct=89,
    operating_pbidt_per_tonne_q4=1253, operating_pbidt_per_tonne_q4_growth_pct=11,
    total_cost_per_tonne_change_q4_pct=-2, energy_cost_change_q4_pct=-3,
    imported_fuel_usd_per_tonne_q4=122,
    green_power_mix_q4_pct=43, green_power_mix_prev_pct=34.4,
    capacity_commissioned_fy26_mtpa=8, capacity_commissioned_apr2026_mtpa=8.7,
    domestic_capacity_after_apr2026_mtpa=200.1, international_capacity_mtpa=5.4,
    global_capacity_mtpa=205.5,
    capex_fy26_cr=9600, operating_cash_flow_fy26_cr=14398,
    net_debt_to_ebitda_x=0.94,
    capacity_target_mtpa="over 240", capex_commitment_cr="over 16,000 over the next three years",
)


def build_ultratech():
    u = UTCL
    d = {}
    d["net_sales_growth_pct"] = growth(u["net_sales_cr"]["FY26"], u["net_sales_cr"]["FY25"])
    d["pbidt_growth_pct"] = growth(u["pbidt_cr"]["FY26"], u["pbidt_cr"]["FY25"])
    d["pbidt_margin_fy26_pct"] = pct(u["pbidt_cr"]["FY26"], u["net_sales_cr"]["FY26"])
    d["pbidt_margin_fy25_pct"] = pct(u["pbidt_cr"]["FY25"], u["net_sales_cr"]["FY25"])
    d["pbidt_margin_q4fy26_pct"] = pct(u["pbidt_cr"]["Q4FY26"], u["net_sales_cr"]["Q4FY26"])
    # Rs crore -> Rs (x1e7); million tonnes -> tonnes (x1e6)
    d["homemade_pbidt_per_tonne_fy26"] = r(u["pbidt_cr"]["FY26"] * 1e7 / (u["india_grey_volume_mt"]["FY26"] * 1e6), 0)
    d["homemade_pbidt_per_tonne_q4"] = r(u["pbidt_cr"]["Q4FY26"] * 1e7 / (u["india_grey_volume_mt"]["Q4FY26"] * 1e6), 0)
    d["homemade_vs_reported_q4_gap"] = d["homemade_pbidt_per_tonne_q4"] - u["operating_pbidt_per_tonne_q4"]
    d["homemade_sales_per_tonne_fy26"] = r(u["net_sales_cr"]["FY26"] * 1e7 / (u["india_grey_volume_mt"]["FY26"] * 1e6), 0)
    d["q4fy25_volume_mt_implied"] = r(u["india_grey_volume_mt"]["Q4FY26"] / (1 + u["india_grey_volume_growth_q4_pct"] / 100), 2)
    d["capacity_end_fy26_mtpa"] = r(u["domestic_capacity_after_apr2026_mtpa"] - u["capacity_commissioned_apr2026_mtpa"], 1)
    d["q4_annualised_volume_mt"] = r(u["india_grey_volume_mt"]["Q4FY26"] * 4, 1)
    d["q4_utilisation_check_pct"] = pct(u["india_grey_volume_mt"]["Q4FY26"] * 4, d["capacity_end_fy26_mtpa"])
    # our rough reconstruction should land near the company's printed 89%
    assert close(d["q4_utilisation_check_pct"], u["capacity_utilisation_q4_pct"], 1.0), d["q4_utilisation_check_pct"]
    d["capex_intensity_fy26_pct"] = pct(u["capex_fy26_cr"], u["net_sales_cr"]["FY26"])
    d["pat_growth_pct"] = growth(u["pat_excl_exceptional_cr"]["FY26"], u["pat_excl_exceptional_cr"]["FY25"])
    return dict(
        name="UltraTech Cement Ltd", exchange="NSE: ULTRACEMCO, BSE: 532538",
        basis="Consolidated; company press release on audited results",
        as_of="FY26 and Q4 FY26 (year/quarter ended 31 March 2026), released 27 April 2026",
        release_date="27 April 2026",
        source_url=UTCL_URL, source_label="Press release 'Financial Results Q4FY26', 27 April 2026",
        reported=u, derived=d,
    )


# =====================================================================
# 4. DR. REDDY'S — pharma (Rs MILLION in the filing; converted to crore)
# =====================================================================
DRL_URL = "https://www.sec.gov/Archives/edgar/data/1135951/000157587226000301/rdy0894_ex99-2.htm"
DRL_MN = dict(
    FY26=dict(revenue=335933, north_america=113737, emerging_markets=67608, india=62186, europe=55501,
              global_generics=299033, psai=34774, others=2127,
              gross_profit=177264, sga=106763, rnd=24058, ebitda=76595, pbt=54817, pat_attrib=42850),
    FY25=dict(revenue=325535, north_america=145164, emerging_markets=54772, india=53734, europe=35882,
              global_generics=289552, psai=33846, others=2137,
              gross_profit=190428, sga=93870, rnd=27380, ebitda=92133, pbt=76784, pat_attrib=56544),
)
DRL_OTHER = dict(
    gross_margin_pct=dict(FY26=52.8, FY25=58.5), rnd_pct=dict(FY26=7.2, FY25=8.4),
    na_q4_mn=dict(Q4FY26=17562, Q4FY25=35586), na_q4_decline_pct=51,
    ssa_q4_mn=4530, na_decline_ex_ssa_fy26_pct=19,
    europe_growth_ex_nrt_pct=14, nrt_revenue_fy26_bn=28.2, nrt_revenue_fy25_bn=12.0,
    anda_filed_fy26=15, filings_pending=77, anda_pending=75, para_iv=43, first_to_file_possible=22,
    nda_pending=2, us_launches_fy26=25,
    capex_fy26_bn=23.0, roce_reported_pct=15.8, roce_ex_oneoffs_pct=17.5,
    usfda_note=("Received 'VAI' classification after a GMP inspection and a pre-approval inspection (PAI) by "
                "the USFDA in December 2025 at formulations facility FTO-SEZ PU01, Srikakulam (company release)."),
    ipm_rank_mat=10, ipm_rank_mqt=9,
)


def build_drreddy():
    for fy, v in DRL_MN.items():
        gg = v["north_america"] + v["emerging_markets"] + v["india"] + v["europe"]
        assert close(gg, v["global_generics"], 2), (fy, gg)
        assert close(v["global_generics"] + v["psai"] + v["others"], v["revenue"], 2), fy
    cr = {fy: {k: r(x / 10.0, 0) for k, x in v.items()} for fy, v in DRL_MN.items()}
    f26, f25 = DRL_MN["FY26"], DRL_MN["FY25"]
    segs = []
    for key, label in [("north_america", "North America"), ("europe", "Europe (incl. acquired NRT business)"),
                       ("india", "India"), ("emerging_markets", "Emerging markets"),
                       ("psai", "PSAI (active ingredients and services)"), ("others", "Others")]:
        segs.append(dict(key=key, label=label, fy26_cr=cr["FY26"][key], fy25_cr=cr["FY25"][key],
                         share26=pct(f26[key], f26["revenue"]), share25=pct(f25[key], f25["revenue"]),
                         growth=growth(f26[key], f25[key], 0)))
    d = dict(
        revenue_growth_pct=growth(f26["revenue"], f25["revenue"]),
        na_growth_pct=growth(f26["north_america"], f25["north_america"]),
        na_share26=pct(f26["north_america"], f26["revenue"]), na_share25=pct(f25["north_america"], f25["revenue"]),
        na_lost_cr=r((f25["north_america"] - f26["north_america"]) / 10, 0),
        non_na_gain_cr=r(((f26["revenue"] - f26["north_america"]) - (f25["revenue"] - f25["north_america"])) / 10, 0),
        rnd_pct26=pct(f26["rnd"], f26["revenue"]), rnd_pct25=pct(f25["rnd"], f25["revenue"]),
        rnd_growth_pct=growth(f26["rnd"], f25["rnd"]),
        gm26=pct(f26["gross_profit"], f26["revenue"]), gm25=pct(f25["gross_profit"], f25["revenue"]),
        ebitda_m26=pct(f26["ebitda"], f26["revenue"]), ebitda_m25=pct(f25["ebitda"], f25["revenue"]),
        pat_growth_pct=growth(f26["pat_attrib"], f25["pat_attrib"]),
        ebitda_growth_pct=growth(f26["ebitda"], f25["ebitda"]),
        rnd_to_pat_x26=r(f26["rnd"] / f26["pat_attrib"], 2),
        ssa_q4_cr=r(DRL_OTHER["ssa_q4_mn"] / 10, 0),
        na_q4_cr26=r(DRL_OTHER["na_q4_mn"]["Q4FY26"] / 10, 0), na_q4_cr25=r(DRL_OTHER["na_q4_mn"]["Q4FY25"] / 10, 0),
        capex_intensity_pct=pct(DRL_OTHER["capex_fy26_bn"] * 1000, f26["revenue"]),
    )
    assert d["rnd_pct26"] == DRL_OTHER["rnd_pct"]["FY26"] and d["rnd_pct25"] == DRL_OTHER["rnd_pct"]["FY25"]
    assert d["gm26"] == DRL_OTHER["gross_margin_pct"]["FY26"] and d["gm25"] == DRL_OTHER["gross_margin_pct"]["FY25"]
    assert d["na_lost_cr"] > d["non_na_gain_cr"] * 0 and d["na_growth_pct"] < 0
    d["na_decline_pct"] = abs(d["na_growth_pct"])
    d["pat_decline_pct"] = abs(d["pat_growth_pct"])
    d["ebitda_decline_pct"] = abs(d["ebitda_growth_pct"])
    d["rnd_decline_pct"] = abs(d["rnd_growth_pct"])
    return dict(
        name="Dr. Reddy's Laboratories Ltd", exchange="NSE: DRREDDY, BSE: 500124, NYSE: RDY",
        basis="Consolidated, IFRS; company press release on audited results (Rs million in the filing, shown here in Rs crore)",
        as_of="FY26 (year ended 31 March 2026), released 12 May 2026",
        release_date="12 May 2026",
        source_url=DRL_URL, source_label="Q4 & Full Year FY26 Financial Results press release (Form 6-K exhibit 99.2, 12 May 2026)",
        reported_mn=DRL_MN, reported_cr=cr, other=DRL_OTHER, segments=segs, derived=d,
    )


# =====================================================================
# 5. HDFC LIFE — life insurance
# =====================================================================
HDFCLIFE_URL = ("https://www.hdfclife.com/content/dam/hdfclifeinsurancecompany/about-us/pdf/investor-relations/"
                "financial-information/Quarterly-financial-results/HDFC-Life-12M-FY2026-Press-Release.pdf")
HL = dict(
    FY26=dict(indiv_ape=14635, total_ape=16641, nbp=36096, renewal_premium=43291, total_premium=79387,
              aum=375198, pat=1910, ev=62139, vnb=4034, vnb_margin_pct=24.2, op_roev_pct=15.0,
              expense_ratio_pct=21.2, solvency_pct=177, persistency_13m=85, persistency_61m=64),
    FY25=dict(indiv_ape=13619, total_ape=15479, nbp=33365, renewal_premium=37680, total_premium=71045,
              aum=336282, pat=1802, ev=55423, vnb=3962, vnb_margin_pct=25.6, op_roev_pct=16.7,
              expense_ratio_pct=19.8, solvency_pct=194, persistency_13m=87, persistency_61m=63),
)
HL_OTHER = dict(vnb_margin_ex_gst_surrender_pct=25.5, op_roev_normalised_pct=15.4,
                pat_growth_ex_oneoffs_pct=16, product_mix_fy26="44/18/5/7/25", product_mix_fy25="39/32/5/5/19",
                preferential_issue_cr=1000)


def build_hdfclife():
    f26, f25 = HL["FY26"], HL["FY25"]
    for fy, v in HL.items():
        assert close(pct(v["vnb"], v["total_ape"]), v["vnb_margin_pct"], 0.06), fy
        assert v["nbp"] + v["renewal_premium"] == v["total_premium"], fy
    d = dict(
        vnb_margin_check26=pct(f26["vnb"], f26["total_ape"]),
        vnb_margin_check25=pct(f25["vnb"], f25["total_ape"]),
        ape_growth_pct=growth(f26["total_ape"], f25["total_ape"]),
        vnb_growth_pct=growth(f26["vnb"], f25["vnb"]),
        ev_growth_pct=growth(f26["ev"], f25["ev"]),
        ev_change_cr=f26["ev"] - f25["ev"],
        pat_growth_pct=growth(f26["pat"], f25["pat"]),
        pat_to_ev_pct=pct(f26["pat"], f25["ev"]),                 # PAT over OPENING EV, same base as RoEV
        evop_approx_cr=r(f26["op_roev_pct"] / 100 * f25["ev"], 0),  # Op RoEV = EVOP / opening EV
        vnb_to_pat_x=r(f26["vnb"] / f26["pat"], 1),
        renewal_share_pct=pct(f26["renewal_premium"], f26["total_premium"]),
        renewal_growth_pct=growth(f26["renewal_premium"], f25["renewal_premium"]),
        persistency_13m_change=f26["persistency_13m"] - f25["persistency_13m"],
        lapsed_13m_per_100=100 - f26["persistency_13m"],
        lapsed_61m_per_100=100 - f26["persistency_61m"],
    )
    d["evop_to_pat_x"] = r(d["evop_approx_cr"] / f26["pat"], 1)
    return dict(
        name="HDFC Life Insurance Company Ltd", exchange="NSE: HDFCLIFE, BSE: 540777",
        basis="Standalone; company press release on audited results (EV and VNB are actuarial, not accounting, figures)",
        as_of="FY26 (year ended 31 March 2026), released 16 April 2026",
        release_date="16 April 2026",
        source_url=HDFCLIFE_URL, source_label="Press release – performance for twelve months ended March 31, 2026 (16 April 2026)",
        reported=HL, other=HL_OTHER, derived=d,
    )


# =====================================================================
# 6. BAJAJ FINANCE — NBFC (consolidated, AFTER one-time actions = reported)
# =====================================================================
BAF_URL = "https://cms-assets.bajajfinserv.in/is/content/bajajfinance/bajaj-finance-q4-fy26-investor-presentation?scl=1&fmt=pdf"
BAF = dict(
    FY26=dict(aum=509975, auf=498944, interest_income=72776, interest_expense=28666, nii=44110,
              non_interest_income=9214, nti=53324, opex=17776, ppop=35548, loan_losses=9482,
              associates=16, exceptional=265, pbt=25817, pat=19332,
              cost_of_funds_pct=7.54, roa_pct_before_oneoffs=4.6, roe_pct_before_oneoffs=19.2,
              roa_pct_after=4.3, roe_pct_after=18.1, gnpa_pct=1.01, nnpa_pct=0.41,
              loan_loss_to_avg_auf_pct=2.09),
    FY25=dict(aum=416661, auf=407844, interest_income=61164, interest_expense=24770, nii=36394,
              non_interest_income=7683, nti=44077, opex=14927, ppop=29150, loan_losses=7088,
              associates=18, exceptional=0, pbt=22080, pat=16779,
              cost_of_funds_pct=7.97, gnpa_pct=0.96, nnpa_pct=0.44, loan_loss_to_avg_auf_pct=1.93),
)
BAF_OTHER = dict(
    deposits_cr=68533, deposits_share_of_borrowings_pct=16,
    borrowing_mix=dict(money_markets=48, banks=31, deposits=16, ecb=5),
    lending_mix=dict(urban=30, rural=11, msme=14, commercial=13, mortgages=32),   # consolidated AUM mix
    car_pct=21.55, tier1_pct=20.67, lcr_q4_pct=228, lcr_requirement_pct=100,
    one_time_fy26=("Q3 FY26 accelerated ECL provision Rs 1,406 cr; Labour Codes charge Rs 265 cr; "
                   "Q4 FY26 management/macro overlay Rs 142 cr"),
)
# Behaviouralised ALM, Bajaj Finance STANDALONE, 31 March 2026 (Rs crore), as printed
ALM_BUCKETS = ["1-7 days", "8-14 days", "15-30 days", "1-2 months", "2-3 months", "3-6 months",
               "6 months-1 year", "1-3 years", "3-5 years", "over 5 years"]
ALM_INFLOWS = [30545, 2955, 22208, 21172, 18354, 46483, 87742, 142026, 38494, 46159]
ALM_OUTFLOWS = [24632, 6256, 10183, 15550, 17543, 22481, 57578, 114874, 43309, 143729]
ALM_BORROWINGS = [20198, 4704, 7488, 13522, 16894, 21532, 55714, 112118, 39536, 38201]
ALM_CUM_PCT_PRINTED = [24, 8, 36, 36, 28, 47, 49, 38, 31, 0]
ALM_CUM_GAP_PRINTED = [5912, 2611, 14636, 20258, 21069, 45071, 75235, 102386, 97571, 0]
ALM_TOTAL = 456137
ALM_PERMISSIBLE = ["−10%", "−10%", "−20%"]   # first three buckets, as printed in the presentation
RBI_NBFC_FAQ_URL = "https://www.rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=1167"


def build_bajaj():
    for fy, v in BAF.items():
        assert v["interest_income"] - v["interest_expense"] == v["nii"], fy
        assert v["nii"] + v["non_interest_income"] == v["nti"], fy
        assert v["nti"] - v["opex"] == v["ppop"], fy
        assert v["ppop"] - v["loan_losses"] + v["associates"] - v["exceptional"] == v["pbt"], fy
    # printed rows are individually rounded, so the columns re-add to within a few crore
    assert close(sum(ALM_INFLOWS), ALM_TOTAL, 5) and close(sum(ALM_OUTFLOWS), ALM_TOTAL, 5)
    rows, ci, co = [], 0, 0
    for b, i, o, bor, p, cg in zip(ALM_BUCKETS, ALM_INFLOWS, ALM_OUTFLOWS, ALM_BORROWINGS,
                                   ALM_CUM_PCT_PRINTED, ALM_CUM_GAP_PRINTED):
        ci += i
        co += o
        assert close(ci - co, cg, 5), (b, ci - co, cg)
        assert abs(r(100 * cg / co, 0) - p) <= 1, (b, p)
        # show the company's printed cumulative gap and % (our re-add agrees within rounding)
        rows.append(dict(bucket=b, inflows=i, outflows=o, borrowings_due=bor, gap=i - o, cumulative_gap=cg,
                         cumulative_gap_pct=p))
    f26, f25 = BAF["FY26"], BAF["FY25"]
    avg_auf = (f26["auf"] + f25["auf"]) / 2
    d = dict(
        avg_auf=r(avg_auf, 0),
        yield_on_avg_auf_pct=pct(f26["interest_income"], avg_auf, 2),
        interest_cost_on_avg_auf_pct=pct(f26["interest_expense"], avg_auf, 2),
        nii_on_avg_auf_pct=pct(f26["nii"], avg_auf, 2),
        opex_on_avg_auf_pct=pct(f26["opex"], avg_auf, 2),
        loan_losses_on_avg_auf_pct=pct(f26["loan_losses"], avg_auf, 2),
        pat_on_avg_auf_pct=pct(f26["pat"], avg_auf, 2),
        cost_to_income_pct=pct(f26["opex"], f26["nti"]),
        aum_growth_pct=growth(f26["aum"], f25["aum"]),
        nii_growth_pct=growth(f26["nii"], f25["nii"]),
        pat_growth_pct=growth(f26["pat"], f25["pat"]),
        cof_change_bps=r((f26["cost_of_funds_pct"] - f25["cost_of_funds_pct"]) * 100, 0),
        implied_leverage_x=r(f26["roe_pct_before_oneoffs"] / f26["roa_pct_before_oneoffs"], 1),
        non_deposit_borrowing_pct=100 - BAF_OTHER["deposits_share_of_borrowings_pct"],
        alm_borrowings_total=sum(ALM_BORROWINGS),
        alm_borrowings_due_1y=sum(ALM_BORROWINGS[:7]),
    )
    d["alm_borrowings_due_1y_pct"] = pct(d["alm_borrowings_due_1y"], d["alm_borrowings_total"], 0)
    d["cof_improvement_bps"] = abs(d["cof_change_bps"])
    assert d["cof_change_bps"] == -43   # printed: "improved by 43 bps"
    assert sum(BAF_OTHER["borrowing_mix"].values()) == 100 and sum(BAF_OTHER["lending_mix"].values()) == 100
    return dict(
        name="Bajaj Finance Ltd", exchange="NSE: BAJFINANCE, BSE: 500034",
        basis=("Consolidated (includes Bajaj Housing Finance), reported figures after one-time actions; "
               "ALM table is Bajaj Finance standalone"),
        as_of="FY26 (year ended 31 March 2026), investor presentation dated 29 April 2026",
        release_date="29 April 2026",
        source_url=BAF_URL, source_label="Q4 FY26 Investor Presentation, 29 April 2026",
        reported=BAF, other=BAF_OTHER, alm=rows, alm_permissible=ALM_PERMISSIBLE,
        rbi_faq_url=RBI_NBFC_FAQ_URL, rbi_faq_as_of="15 September 2026",
        derived=d,
    )


# =====================================================================
# 7. BHARTI AIRTEL — telecom
# =====================================================================
AIRTEL_URL = "https://assets.airtel.in/static-assets/cms/investor/docs/quarterly_results/2025-26/Q4/Press-Release.pdf"
AIRTEL = dict(
    Q4FY26=dict(revenue=55383, ebitda=32038, ebit=18156, pbt=13205, net_income=7245),
    Q4FY25=dict(revenue=47876, ebitda=27404, ebit=14950, pbt=9724, net_income=5223),
    FY26=dict(revenue=210973, ebitda=121268, ebit=68100, pbt=48590, net_income=26904),
    FY25=dict(revenue=172985, ebitda=94249, ebit=48427, pbt=31112, net_income=17573),
)
AIRTEL_OTHER = dict(
    arpu=dict(Q4FY26=257, Q4FY25=245), india_revenue_q4_cr=39566, india_revenue_growth_pct=7.7,
    india_mobile_revenue_growth_pct=8.3, ebitdaal_q4_cr=28647, ebitdaal_margin_q4_pct=51.7,
    india_ebitda_margin_q4_pct=60.6, india_ebitdaal_margin_q4_pct=56.0,
    capex_q4_cr=16066, india_capex_q4_cr=13488,
    net_debt_to_ebitda_x=1.29, net_debt_to_ebitda_prev_x=1.86, net_debt_ex_leases_to_ebitdaal_x=0.79,
    india_customers_k=dict(Mar26=482421, Mar25=424461), smartphone_share_pct=80,
    data_gb_per_customer_month=31.4, data_usage_growth_pct=32.8, postpaid_m=29.0,
)


def build_airtel():
    a, o = AIRTEL, AIRTEL_OTHER
    for k, v in a.items():
        assert v["ebitda"] > v["ebit"] > v["pbt"] > v["net_income"], k
    d = dict(
        arpu_growth_pct=growth(o["arpu"]["Q4FY26"], o["arpu"]["Q4FY25"]),
        arpu_change=o["arpu"]["Q4FY26"] - o["arpu"]["Q4FY25"],
        ebitda_margin_fy26=pct(a["FY26"]["ebitda"], a["FY26"]["revenue"]),
        ebit_margin_fy26=pct(a["FY26"]["ebit"], a["FY26"]["revenue"]),
        ebitda_minus_ebit_fy26=a["FY26"]["ebitda"] - a["FY26"]["ebit"],
        ebitda_margin_q4=pct(a["Q4FY26"]["ebitda"], a["Q4FY26"]["revenue"]),
        ebit_margin_q4=pct(a["Q4FY26"]["ebit"], a["Q4FY26"]["revenue"]),
        capex_to_revenue_q4_pct=pct(o["capex_q4_cr"], a["Q4FY26"]["revenue"]),
        capex_to_ebitda_q4_pct=pct(o["capex_q4_cr"], a["Q4FY26"]["ebitda"]),
        ebitda_less_capex_q4=a["Q4FY26"]["ebitda"] - o["capex_q4_cr"],
        lease_gap_q4=a["Q4FY26"]["ebitda"] - o["ebitdaal_q4_cr"],
        revenue_growth_fy26_pct=growth(a["FY26"]["revenue"], a["FY25"]["revenue"]),
        revenue_growth_q4_pct=growth(a["Q4FY26"]["revenue"], a["Q4FY25"]["revenue"]),
        india_customer_growth_pct=growth(o["india_customers_k"]["Mar26"], o["india_customers_k"]["Mar25"]),
    )
    # mobile revenue = customers x ARPU, so implied growth in average mobile customers (rough:
    # quarter lengths differ and ARPU is rounded to the rupee)
    d["implied_mobile_customer_growth_pct"] = r(100 * ((1 + o["india_mobile_revenue_growth_pct"] / 100)
                                                       / (1 + d["arpu_growth_pct"] / 100) - 1), 1)
    d["ebitda_minus_ebit_pct_rev"] = pct(d["ebitda_minus_ebit_fy26"], a["FY26"]["revenue"])
    d["lease_gap_q4_pct_rev"] = pct(d["lease_gap_q4"], a["Q4FY26"]["revenue"])
    assert d["ebitda_margin_q4"] == 57.8 and d["ebit_margin_q4"] == 32.8 and d["revenue_growth_q4_pct"] == 15.7
    assert close(pct(o["ebitdaal_q4_cr"], a["Q4FY26"]["revenue"]), o["ebitdaal_margin_q4_pct"], 0.05)
    return dict(
        name="Bharti Airtel Ltd", exchange="NSE: BHARTIARTL, BSE: 532454",
        basis="Consolidated, Ind AS; company media release on audited results",
        as_of="Q4 FY26 and FY26 (quarter/year ended 31 March 2026), released 13 May 2026",
        release_date="13 May 2026",
        source_url=AIRTEL_URL, source_label="Media release, 13 May 2026 (Q4 FY26)",
        reported=a, other=o, derived=d,
    )


# =====================================================================
# Opener: one table across sectors, built from this file + existing data
# =====================================================================
def build_opener(infy, utcl, drl, airtel, bank_path, company_path):
    with open(company_path, encoding="utf-8") as fh:
        brit = yaml.safe_load(fh)
    with open(bank_path, encoding="utf-8") as fh:
        bank = yaml.safe_load(fh)
    b_is = brit["income_statement"]["FY25"]
    rows = [
        dict(company="Britannia (FMCG)", period="FY25",
             ebitda_margin=brit["ratios"]["FY25"]["ebitda_margin"],
             ebit_margin=pct(b_is["ebit"], b_is["revenue"]),
             capex_intensity=brit["ratios"]["FY25"]["capex_intensity"], capex_basis="year"),
        dict(company="UltraTech (cement)", period="FY26",
             ebitda_margin=utcl["derived"]["pbidt_margin_fy26_pct"], ebit_margin=None,
             capex_intensity=utcl["derived"]["capex_intensity_fy26_pct"], capex_basis="year"),
        dict(company="Dr. Reddy's (pharma)", period="FY26",
             ebitda_margin=drl["derived"]["ebitda_m26"], ebit_margin=None,
             capex_intensity=drl["derived"]["capex_intensity_pct"], capex_basis="year"),
        dict(company="Bharti Airtel (telecom)", period="FY26 (capex: Q4 only)",
             ebitda_margin=airtel["derived"]["ebitda_margin_fy26"], ebit_margin=airtel["derived"]["ebit_margin_fy26"],
             capex_intensity=airtel["derived"]["capex_to_revenue_q4_pct"], capex_basis="Q4 FY26"),
    ]
    bd = bank["derived_fy25"]
    return dict(
        margin_capex_rows=rows,
        infosys_op_margin=infy["reported"]["op_margin_pct"]["FY26"],
        infosys_op_profit_to_avg_equity=infy["derived"]["op_profit_to_avg_equity_pct"],
        britannia_roce=brit["ratios"]["FY25"]["roce"],
        britannia_roa=brit["ratios"]["FY25"]["roa"],
        hdfc_bank_roa=bd["roa_pct"], hdfc_bank_leverage=bd["avg_leverage"], hdfc_bank_roe=bd["roe_pct"],
        drl_roce_reported=drl["other"]["roce_reported_pct"],
    )


def main():
    infy = build_infosys()
    mar = build_marico()
    utcl = build_ultratech()
    drl = build_drreddy()
    hl = build_hdfclife()
    baf = build_bajaj()
    air = build_airtel()
    opener = build_opener(infy, utcl, drl, air,
                          os.path.join(ROOT, "_data", "real_bank.yml"),
                          os.path.join(ROOT, "_data", "real_company.yml"))
    out = {
        "_comment": ("GENERATED by scripts/derive_sectors.py — edit the reported figures there, not here. "
                     "Real companies: observables and mechanics only (no valuation, target or verdict)."),
        "infosys": infy, "marico": mar, "ultratech": utcl, "drreddy": drl,
        "hdfclife": hl, "bajaj": baf, "airtel": air, "opener": opener,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("# GENERATED by scripts/derive_sectors.py — do not edit by hand.\n")
        fh.write("# Reported figures are typed once in that script, each with its source URL;\n")
        fh.write("# every ratio here is computed. Re-run the script after any change.\n")
        yaml.safe_dump(out, fh, sort_keys=False, allow_unicode=True, width=100)
    print("wrote", OUT)
    for name, blk in [("infosys", infy), ("marico", mar), ("ultratech", utcl), ("drreddy", drl),
                      ("hdfclife", hl), ("bajaj", baf), ("airtel", air)]:
        print(name, blk["derived"])
    print("opener", opener)


if __name__ == "__main__":
    main()
