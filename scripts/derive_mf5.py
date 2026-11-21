#!/usr/bin/env python3
"""
Derive the figures used by module 5 of "Mutual Funds, Minus the Marketing",
"Newer fund rules and wrappers" (_data/mf5.yml): NAV cut-off times, life cycle
funds, gold ETFs and fund of funds, scheme mergers and wind-ups, reading a debt
fund's portfolio, and specialised investment funds. Posts dated 2 to 7 February
2027. Roadmap: _review/roadmaps/2026-11-06-mutual-funds.md

    python3 scripts/derive_mf5.py        # rewrites _data/mf5.yml

RULES (read 21 Nov 2026 from SEBI's own documents; posts carry needs_review: regulation):
  * Cut-off times: SEBI Master Circular for Mutual Funds, 27 June 2024
    (SEBI/HO/IMD/IMD-PoD-1/P/CIR/2024/90), paras 8.4.5 to 8.4.7, with para 8.4.5.4
    as modified by circular SEBI/HO/IMD/PoD2/P/CIR/2025/56 of 22 April 2025
    (7 pm online cut-off for overnight-fund redemptions, from 1 June 2025).
  * Life cycle funds: SEBI circular HO/24/13/15(2)2026-IMD-RAC4/I/5764/2026 of
    26 February 2026, Annexure B (tenures, glide-path bands, exit load, naming).
  * Scheme mergers and wind-ups: SEBI (Mutual Funds) Regulations, 2026 (amended to
    10 October 2026), regulation 22 ("Changes to scheme attribute") and
    regulations 36 to 38; Master Circular paras 2.1.1.4 and 2.2.
  * SIF: the same Regulations, regulation 49; SEBI's SIF FAQs of 22 September 2026.

DATA (worked examples, real and lagged): UTI Gold ETF NAV (assets/data/uti-gold-etf-nav.csv,
unit-split adjusted as in derive_mbm2.py) and UTI Gold ETF Fund of Fund NAVs, regular and
direct (assets/data/uti-gold-etf-fof-nav.csv, AMFI via mfapi.in, schemes 150715/150714),
both to 31 March 2026. HYPOTHETICAL: the merger units example and the debt fund portfolio.

LAG: first post 2 February 2027 (cut-off 2 November 2026); data ends March 2026.

Needs pandas, pyyaml.
"""
import math
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "mf5.yml"
CUTOFF = pd.Timestamp("2026-11-02")


def r(x, d=1):
    v = round(float(x), d)
    return int(v) if v == int(v) else v


out = {}

# ---------------------------------------------------------------- 1. cut-off rules (as read)
out["cutoff"] = {
    "liquid_purchase": "1.30 pm",
    "other_cutoff": "3.00 pm",
    "overnight_online_redemption": "7 pm",
    "overnight_online_from": "1 June 2025",
    "master_circular": "SEBI Master Circular for Mutual Funds, 27 June 2024",
    "master_circular_url": "https://www.sebi.gov.in/legal/master-circulars/jun-2024/master-circular-for-mutual-funds_84441.html",
    "amendment": "SEBI circular SEBI/HO/IMD/PoD2/P/CIR/2025/56, 22 April 2025",
    "amendment_url": "https://www.sebi.gov.in/legal/circulars/apr-2025/change-in-cut-off-timings-to-determine-applicable-nav-with-respect-to-repurchase-redemption-of-units-in-overnight-schemes-of-mutual-funds_93541.html",
}

# ---------------------------------------------------------------- 2. life cycle funds (Annexure B)
bands = [  # years to maturity, equity, debt, gold/silver ETFs/ETCDs/InvITs (percent ranges)
    {"ytm": "15–30 years", "equity": "65–95", "debt": "5–25", "other": "0–10"},
    {"ytm": "10–15 years", "equity": "65–80", "debt": "5–25", "other": "0–10"},
    {"ytm": "5–10 years", "equity": "50–65", "debt": "5–25", "other": "0–10"},
    {"ytm": "3–5 years", "equity": "35–50", "debt": "25–50", "other": "0–10"},
    {"ytm": "1–3 years", "equity": "20–35", "debt": "25–65", "other": "0–10"},
    {"ytm": "Under 1 year", "equity": "5–20", "debt": "25–65", "other": "0–10"},
]
out["life_cycle"] = {
    "circular": "SEBI circular HO/24/13/15(2)2026-IMD-RAC4/I/5764/2026, 26 February 2026",
    "circular_url": "https://www.sebi.gov.in/legal/circulars/feb-2026/categorization-and-rationalization-of-mutual-fund-schemes_99983.html",
    "min_tenure": 5, "max_tenure": 30, "step": 5, "max_active": 6,
    "bands": bands,
    "exit_load": [{"within": "1 year", "pct": 3}, {"within": "2 years", "pct": 2}, {"within": "3 years", "pct": 1}],
    "arbitrage_note_years": 5, "arbitrage_extra_pct": 50, "equity_total_band": "65–75",
    "compliance_months": 6,
}
# illustration: the equity band a "Life Cycle Fund 2045" must sit in, year by year
ex_year = 2046   # a 20-year fund launched in 2026: tenures must be multiples of 5 (Annexure B para 1)
# years chosen to avoid band boundaries (the circular's bands share end points, e.g. 10)
ill = []
for fy, b in [(2027, bands[0]), (2033, bands[1]), (2038, bands[2]), (2042, bands[3]), (2044, bands[4])]:
    ytm = ex_year - fy
    lo, hi = [int(x.split()[0]) for x in b["ytm"].replace("years", "").split("–")]
    assert lo < ytm < hi, (fy, ytm, b)
    ill.append({"year": fy, "years_left": ytm, "equity": b["equity"], "debt": b["debt"]})
out["life_cycle"]["example_name"] = f"Life Cycle Fund {ex_year}"
out["life_cycle"]["example_launch"] = 2026
out["life_cycle"]["example_tenure"] = ex_year - 2026
out["life_cycle"]["example"] = ill

# ---------------------------------------------------------------- 3. gold ETF vs fund of funds
etf = pd.read_csv(ROOT / "assets/data/uti-gold-etf-nav.csv", parse_dates=["date"]).set_index("date")["nav"]
etf = etf.where(etf.index >= pd.Timestamp("2021-03-30"), etf / 100)   # unit split, as derive_mbm2.py
fof = pd.read_csv(ROOT / "assets/data/uti-gold-etf-fof-nav.csv", parse_dates=["date"]).set_index("date")
for s in (etf, fof):
    assert s.index.max() <= CUTOFF
start = pd.Timestamp("2022-11-30")    # a month after the FoF's first NAV, past its NFO period
end = min(etf.index.max(), fof.index.max())
def at(s, d):
    return float(s[s.index <= d].iloc[-1])
yrs = (end - start).days / 365.25
g = {}
for name, s in [("etf", etf), ("fof_regular", fof["nav_regular_growth"].dropna()), ("fof_direct", fof["nav_direct_growth"].dropna())]:
    tot = at(s, end) / at(s, start)
    g[name] = {"cagr_pct": r((tot ** (1 / yrs) - 1) * 100, 2), "lakh_became": r(tot * 100000, 0)}
sens = []
for e in ["2026-03-13", "2026-03-20", "2026-03-25", "2026-03-27", "2026-03-31"]:
    e = pd.Timestamp(e)
    y = (e - start).days / 365.25
    ce = (at(etf, e) / at(etf, start)) ** (1 / y) - 1
    cd = (at(fof["nav_direct_growth"].dropna(), e) / at(fof["nav_direct_growth"].dropna(), start)) ** (1 / y) - 1
    sens.append({"end": f"{e.day} {e.strftime('%B %Y')}", "gap_pp": r((ce - cd) * 100, 2)})
g["sensitivity"] = sens
g["gap_regular_pp"] = r(g["etf"]["cagr_pct"] - g["fof_regular"]["cagr_pct"], 2)
g["gap_direct_pp"] = r(g["etf"]["cagr_pct"] - g["fof_direct"]["cagr_pct"], 2)
assert g["gap_regular_pp"] > g["gap_direct_pp"] > -0.5, g
out["gold"] = {**g, "start": f"{start.day} {start.strftime('%B %Y')}", "end": f"{end.day} {end.strftime('%B %Y')}",
               "years": r(yrs, 1), "etf_code": 105463, "fof_codes": "150715 (regular), 150714 (direct)",
               "etf_url": "https://api.mfapi.in/mf/105463", "fof_url": "https://api.mfapi.in/mf/150715",
               "csv_etf": "/assets/data/uti-gold-etf-nav.csv", "csv_fof": "/assets/data/uti-gold-etf-fof-nav.csv"}

# ---------------------------------------------------------------- 4. scheme merger example (hypothetical)
m = {"units_a": 1000, "nav_a": 25.40, "nav_b": 63.50}
m["value"] = r(m["units_a"] * m["nav_a"], 2)
m["units_b"] = r(m["value"] / m["nav_b"], 3)
m["fmt"] = {"units_a": f"{m['units_a']:,}", "nav_a": f"{m['nav_a']:.2f}", "nav_b": f"{m['nav_b']:.2f}",
            "value": f"{m['value']:,.0f}" if m['value'] == int(m['value']) else f"{m['value']:,.2f}",
            "units_b": f"{m['units_b']:,.0f}" if m['units_b'] == int(m['units_b']) else f"{m['units_b']:,.3f}"}
m["unit_change_pct"] = r((m["units_b"] / m["units_a"] - 1) * 100, 1)
assert abs(m["units_b"] * m["nav_b"] - m["value"]) < 0.1
out["merger"] = {**m, "exit_days": 30, "regs_url": "https://www.sebi.gov.in/legal/regulations/oct-2026/securities-and-exchange-board-of-india-mutual-funds-regulations-2026-last-amended-on-october-10-2026-_105356.html",
                 "wind_up_majority_pct": 75, "notice_days": 1, "vote_days": 45}

# ---------------------------------------------------------------- 5. a debt fund's portfolio (hypothetical)
hold = [  # name, rating, weight %, residual maturity (years), YTM %, modified duration
    ("Government of India bond", "Sovereign", 22, 6.5, 6.55, 5.1),
    ("State development loan", "Sovereign", 10, 9.0, 6.95, 6.6),
    ("PSU bank bond", "AAA", 18, 3.0, 7.05, 2.7),
    ("Housing finance company NCD", "AAA", 14, 2.5, 7.30, 2.2),
    ("Private bank certificate of deposit", "A1+", 8, 0.4, 6.90, 0.4),
    ("NBFC non-convertible debenture", "AA+", 10, 2.0, 7.80, 1.8),
    ("Manufacturing company bond", "AA", 8, 1.5, 8.30, 1.4),
    ("Treasury bills, cash and repo", "Sovereign/cash", 10, 0.1, 6.20, 0.1),
]
assert sum(h[2] for h in hold) == 100
rows = [{"name": n, "rating": rt, "weight": w, "maturity": (int(mt) if mt == int(mt) else mt), "ytm": y, "mod_dur": md} for n, rt, w, mt, y, md in hold]
wavg = lambda k: sum(h["weight"] * h[k] for h in rows) / 100
mix = {}
for h in rows:
    key = "Sovereign and cash" if h["rating"].startswith("Sovereign") else ("AAA and A1+" if h["rating"] in ("AAA", "A1+") else "Below AAA")
    mix[key] = mix.get(key, 0) + h["weight"]
out["debt_portfolio"] = {
    "rows": rows, "avg_maturity": r(wavg("maturity"), 2), "ytm": r(wavg("ytm"), 2), "mod_dur": r(wavg("mod_dur"), 2),
    "mix": [{"bucket": k, "pct": v} for k, v in mix.items()],
    "rate_move_bp": 100, "price_change_pct": r(-wavg("mod_dur"), 2),
    "below_aaa_pct": mix.get("Below AAA", 0),
}

# ---------------------------------------------------------------- 6. SIF
out["sif"] = {"min_lakh": 10, "faq_date": "22 September 2026",
              "faq_url": "https://www.sebi.gov.in/sebi_data/faqfiles/sep-2026/1790074512985.pdf",
              "restore_days": 30, "regulation": 49}

text = yaml.safe_dump(out, sort_keys=False, allow_unicode=True)
# Ruby's YAML (Jekyll) reads an unquoted 1,000 as the integer 1000: quote the display strings
import re
text = re.sub(r"^(    (?:units_a|nav_a|nav_b|value|units_b)): ([0-9][0-9,.]*)$", r"\1: '\2'", text, flags=re.M)
OUT.write_text("# Generated by scripts/derive_mf5.py. Do not edit by hand.\n" + text, encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
