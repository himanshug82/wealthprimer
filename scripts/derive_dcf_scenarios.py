#!/usr/bin/env python3
"""Derive the reverse-DCF scenarios in _data/case_study.yml (dcf.reverse).

The terminal value post (30 Sep 2026) shows a base case, a "market case" and
an "aggressive" case. The base case is the forecast in dcf.forecast; the two
scenarios used to be typed by hand. This script recomputes them, plus the
implied terminal growth, the cash-flow multiple and the sensitivity grid,
from the same model as the post's Python calculator, and writes the scenario
values back in place (the rest of case_study.yml is hand-maintained with
comments, so it is edited line by line rather than re-dumped).

Scenario assumptions (all fictional, for teaching):
  market case  revenue growth 25% a year for five years, EBITDA margin 20%
               from FY26, base-case capex path (8% of revenue easing to 5%)
  aggressive   revenue growth 30% a year for five years, EBITDA margin 22%
               from FY26, base-case capex path
Everything else (tax, depreciation, working capital, WACC, terminal growth,
net debt, shares) is the base case's.

    python3 scripts/derive_dcf_scenarios.py          # check and write
    python3 scripts/derive_dcf_scenarios.py --check  # check only; exit 1 on drift
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "case_study.yml"

SCENARIOS = {
    "scenario_market_case": {"growth": [0.25] * 5, "margin": [0.20] * 5},
    "scenario_aggressive": {"growth": [0.30] * 5, "margin": [0.22] * 5},
}


def model(cs):
    d = cs["dcf"]
    a, r = d["assumptions"], d["result"]
    fc = d["forecast"]
    return {
        "revenue0": float(cs["income_statement"]["FY25"]["revenue"]),
        "tax": a["tax_rate"] / 100,
        "dep": a["depreciation_pct_revenue"] / 100,
        "nwc": a["nwc_pct_revenue"] / 100,
        "wacc": d["wacc"]["wacc_unrounded"] / 100,
        "g": a["terminal_growth"] / 100,
        "net_debt": float(r["net_debt"]),
        "shares": float(r["shares_lakh"]),
        "growth": [y["revenue_growth"] / 100 for y in fc],
        "margin": [y["ebitda_margin"] / 100 for y in fc],
        "capex": [y["capex_pct_revenue"] / 100 for y in fc],
    }


def flows(m, growth, margin, capex):
    out, rev = [], m["revenue0"]
    for g, mg, cx in zip(growth, margin, capex):
        prev, rev = rev, rev * (1 + g)
        dep = rev * m["dep"]
        ebit = rev * mg - dep
        out.append(ebit * (1 - m["tax"]) + dep - rev * cx - (rev - prev) * m["nwc"])
    return out


def per_share(m, cf, wacc=None, g=None, mult=1.0):
    wacc = m["wacc"] if wacc is None else wacc
    g = m["g"] if g is None else g
    cf = [c * mult for c in cf]
    pv = sum(c / (1 + wacc) ** n for n, c in enumerate(cf, start=1))
    tv = cf[-1] * (1 + g) / (wacc - g)
    ev = pv + tv / (1 + wacc) ** len(cf)
    return (ev - m["net_debt"]) / m["shares"]


def solve(f, target, lo, hi):
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    check_only = "--check" in sys.argv
    text = DATA.read_text()
    cs = yaml.safe_load(text)
    m = model(cs)
    d = cs["dcf"]
    base = flows(m, m["growth"], m["margin"], m["capex"])

    # Invariants: the base case must reproduce the stored result.
    vps = per_share(m, base)
    assert abs(vps - d["result"]["value_per_share"]) < 0.01, vps
    ipo = d["result"]["ipo_price"]
    g_impl = solve(lambda g: per_share(m, base, g=g), ipo, 0.0, m["wacc"] - 1e-4)
    assert abs(g_impl * 100 - d["reverse"]["implied_terminal_growth"]) < 0.005, g_impl
    mult = solve(lambda k: per_share(m, base, mult=k), ipo, 1.0, 5.0)
    assert abs(mult - d["reverse"]["cash_flow_multiple_required"]) < 0.005, mult
    for row in d["sensitivity"]["rows"]:
        for g, v in zip(d["sensitivity"]["terminal_growth_cols"], row["values"]):
            got = per_share(m, base, wacc=m["wacc"] + (row["wacc"] - 13.91) / 100, g=g / 100)
            assert abs(got - v) <= 0.5 + 1e-9, (row["wacc"], g, got, v)

    drift = False
    for key, sc in SCENARIOS.items():
        value = round(per_share(m, flows(m, sc["growth"], sc["margin"], m["capex"])))
        stored = d["reverse"][key]
        print(f"{key:22s} {value:5d}  (stored {stored})")
        if value != stored:
            drift = True
            text, n = re.subn(rf"^(\s*{key}:\s*)\d+", rf"\g<1>{value}", text, count=1, flags=re.M)
            assert n == 1, key
    if drift and check_only:
        sys.exit(1)
    if drift:
        DATA.write_text(text)
        print(f"wrote {DATA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
