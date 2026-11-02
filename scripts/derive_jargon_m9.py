#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by Jargon, Decoded Module 9 ("Finance building blocks":
yield curve and the repo rate, credit ratings, depreciation and amortisation,
effective tax rate, futures basis, authorised/issued/paid-up capital) into
_data/jargon_m9.yml.

    python3 scripts/derive_jargon_m9.py

INPUTS (read-only): _data/case_study.yml (Desi Bites, fictional).

HYPOTHETICAL: the yield curves, the rating-to-spread-to-loss grid, the futures
inputs and Desi Bites' authorised capital (a NEW Desi Bites fact introduced here:
authorised capital of Rs 150 lakh, i.e. 15 lakh shares of face value Rs 10 --
chosen so the 12.5 lakh post-IPO shares fit inside it). Nothing is a market quote.

RULES: no current policy rate, no statutory tax rate for a real company, no
exchange rule is stated; the posts say "check the current rule".

Invariants are asserted.
"""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "jargon_m9.yml"
cs = yaml.safe_load((ROOT / "_data" / "case_study.yml").read_text())
IS, BS = cs["income_statement"], cs["balance_sheet"]
LST, SH = cs["listing"], cs["share_data"]


class _NoAlias(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def r(x, nd=2):
    v = round(float(x), nd)
    return int(v) if v == int(v) else v


out = {}

# ================================================================ 1. yield curve (hypothetical)
curves = {
    "normal": {"1": 5.8, "2": 6.0, "3": 6.2, "5": 6.5, "10": 6.9},
    "flat": {"1": 6.3, "2": 6.3, "3": 6.3, "5": 6.3, "10": 6.3},
    "inverted": {"1": 7.0, "2": 6.9, "3": 6.7, "5": 6.5, "10": 6.2},
}
rows = []
for name, c in curves.items():
    rows.append({"shape": name, "y1": c["1"], "y2": c["2"], "y3": c["3"], "y5": c["5"], "y10": c["10"],
                 "term_spread_10y_1y_pp": r(c["10"] - c["1"], 1)})
assert rows[0]["term_spread_10y_1y_pp"] > 0 > rows[2]["term_spread_10y_1y_pp"] and rows[1]["term_spread_10y_1y_pp"] == 0
# price of a Rs 1,000 zero-coupon bond at each maturity on the normal curve
zc = [{"years": int(n), "yield_pct": y, "price": r(1000 / (1 + y / 100) ** int(n), 2)} for n, y in curves["normal"].items()]
# a parallel shift of +1 point: price change by maturity
shift = [{"years": z["years"],
          "pct_change": r((1 / (1 + (z["yield_pct"] + 1) / 100) ** z["years"]) / (1 / (1 + z["yield_pct"] / 100) ** z["years"]) * 100 - 100, 1)}
         for z in zc]
out["curve"] = {"curves": rows, "zero_prices": zc, "plus_1pt": shift,
                "five_year_vs_one_year_gap_pp": r(curves["normal"]["5"] - curves["normal"]["1"], 1)}

# ================================================================ 2. credit ratings (hypothetical grid)
# expected loss ~ probability of default x (1 - recovery); spread must at least cover it
grid = []
for grade, pd_, spread in [("Highest-rated", 0.1, 0.4), ("Strong", 0.5, 1.0), ("Adequate", 2.0, 2.5), ("Speculative", 8.0, 7.0)]:
    rec = 40
    el = pd_ * (1 - rec / 100)
    grid.append({"bucket": grade, "annual_default_prob_pct": pd_, "recovery_pct": rec, "expected_loss_pct": r(el, 2),
                 "spread_pct": spread, "spread_minus_loss_pp": r(spread - el, 2)})
base_yield = 6.5
price_gov = r(sum(70 / (1 + base_yield / 100) ** t for t in range(1, 6)) + 1000 / (1 + base_yield / 100) ** 5, 2)
issuer_y = base_yield + 2.5
price_issuer = r(sum(70 / (1 + issuer_y / 100) ** t for t in range(1, 6)) + 1000 / (1 + issuer_y / 100) ** 5, 2)
out["rating"] = {"grid": grid, "base_yield_pct": base_yield, "issuer_spread_pp": 2.5, "issuer_yield_pct": issuer_y,
                 "coupon_pct": 7, "years": 5, "price_at_base": price_gov, "price_at_issuer": price_issuer,
                 "price_gap": r(price_gov - price_issuer, 2),
                 "price_gap_pct": r((price_gov - price_issuer) / price_gov * 100, 1)}

# ================================================================ 3. depreciation and amortisation
COST, LIFE, SALVAGE, WDV_RATE = 100.0, 10, 0.0, 20.0           # Rs lakh, years, Rs lakh, % per year
slm = COST / LIFE
sched = []
wdv_open = COST
for y in range(1, 6):
    wdv_dep = wdv_open * WDV_RATE / 100
    sched.append({"year": y, "slm_dep": r(slm, 2), "slm_book_end": r(COST - slm * y, 2),
                  "wdv_dep": r(wdv_dep, 2), "wdv_book_end": r(wdv_open - wdv_dep, 2)})
    wdv_open -= wdv_dep
fy = "FY25"
dep_share_ebitda = IS[fy]["depreciation"] / IS[fy]["ebitda"] * 100
assert IS[fy]["ebitda"] - IS[fy]["depreciation"] == IS[fy]["ebit"]
dep_pct_open_nfa = IS[fy]["depreciation"] / BS["FY24"]["net_fixed_assets"] * 100
out["depreciation"] = {
    "cost": COST, "life": LIFE, "wdv_rate_pct": WDV_RATE, "schedule": sched,
    "ten_year_wdv_total": r(COST * (1 - (1 - WDV_RATE / 100) ** LIFE), 2), "ten_year_wdv_left": r(COST * (1 - WDV_RATE / 100) ** LIFE, 2),
    "ten_year_slm_total": r(slm * LIFE, 1),
    "five_year_slm_total": r(slm * 5, 1), "five_year_wdv_total": r(sum(s["wdv_dep"] for s in sched), 2),
    "db": {"fy": fy, "ebitda": IS[fy]["ebitda"], "depreciation": IS[fy]["depreciation"], "ebit": IS[fy]["ebit"],
           "dep_share_of_ebitda_pct": r(dep_share_ebitda, 1), "dep_pct_of_opening_nfa": r(dep_pct_open_nfa, 1),
           "pat": IS[fy]["pat"], "interest": IS[fy]["interest"], "pbt": IS[fy]["pbt"], "tax": IS[fy]["tax"]},
    # a small intangible example: software bought for Rs 30 lakh, amortised straight-line over 5 years
    "intangible": {"cost": 30, "life": 5, "per_year": r(30 / 5, 1)},
}

# ================================================================ 4. effective tax rate
rows = []
for y in ("FY23", "FY24", "FY25"):
    rows.append({"fy": y, "pbt": IS[y]["pbt"], "tax": IS[y]["tax"], "etr_pct": r(IS[y]["tax"] / IS[y]["pbt"] * 100, 1)})
STAT = cs["dcf"]["assumptions"]["tax_rate"]
STAT = STAT * 100 if STAT < 1 else STAT
# deferred tax illustration: asset of Rs 100 lakh; book SLM over 10 years (10 a year); tax depreciation faster (15 in year 1)
BOOK_DEP, TAX_DEP, RATE = 10.0, 15.0, 25.0
timing = TAX_DEP - BOOK_DEP
out["etr"] = {"rows": rows, "statutory_rate_pct": STAT,
              "deferred": {"book_dep": BOOK_DEP, "tax_dep": TAX_DEP, "rate_pct": RATE, "timing_difference": timing,
                           "dtl_created": r(timing * RATE / 100, 2),
                           "pbt": 200.0, "current_tax": r((200.0 + BOOK_DEP - TAX_DEP) * RATE / 100, 2),
                           "deferred_tax_charge": r(timing * RATE / 100, 2),
                           "total_tax": r(200.0 * RATE / 100, 2)}}
# a permanent difference moves the rate; surcharge and cess also lift it above the headline
EXEMPT, DISALLOWED = 20.0, 10.0
out["etr"]["permanent"] = {"pbt": 200.0, "rate_pct": RATE, "exempt_income": EXEMPT, "disallowed": DISALLOWED,
                           "tax_with_exempt": r((200.0 - EXEMPT) * RATE / 100, 2),
                           "etr_with_exempt_pct": r((200.0 - EXEMPT) * RATE / 200.0, 2),
                           "tax_with_disallowed": r((200.0 + DISALLOWED) * RATE / 100, 2),
                           "etr_with_disallowed_pct": r((200.0 + DISALLOWED) * RATE / 200.0, 2)}
# Finance Act 2026: 25% up to Rs 400 crore turnover, 7% surcharge in the Rs 1-10 crore income band, 4% cess
out["etr"]["surcharge_cess"] = {"headline_pct": 25.0, "surcharge_pct": 7.0, "cess_pct": 4.0,
                                "all_in_pct": r(25.0 * 1.07 * 1.04, 2)}
d_ = out["etr"]["deferred"]
assert d_["current_tax"] + d_["dtl_created"] == d_["total_tax"]       # total tax charge = rate x accounting profit

# ================================================================ 5. futures basis and cost of carry (hypothetical)
SPOT, RATE_PA, DIV = 1000.0, 6.0, 0.0
rows = []
for days in (30, 20, 10, 0):
    fair = SPOT * (1 + RATE_PA / 100 * days / 365)
    rows.append({"days_left": days, "fair_futures": r(fair, 2), "basis": r(fair - SPOT, 2),
                 "basis_pct": r((fair - SPOT) / SPOT * 100, 2)})
# the same with a dividend of Rs 8 due before expiry
DIVAMT = 8.0
fair_div = SPOT * (1 + RATE_PA / 100 * 30 / 365) - DIVAMT
out["futures"] = {"spot": SPOT, "rate_pct": RATE_PA, "rows": rows, "dividend": DIVAMT,
                  "fair_with_dividend": r(fair_div, 2), "basis_with_dividend": r(fair_div - SPOT, 2),
                  # an inverted (backwardation) example: futures below spot
                  "back_example": {"spot": 1000, "futures": 996, "basis": -4}}
assert rows[-1]["basis"] == 0

# ================================================================ 6. authorised, issued, paid-up
FACE = SH["face_value"]
AUTH_SHARES_LAKH = 15.0                                   # NEW Desi Bites fact (see docstring)
pre, fresh, post = SH["shares_outstanding_lakh"], LST["fresh_issue_shares_lakh"], LST["post_ipo_shares_lakh"]
assert pre + fresh == post and post <= AUTH_SHARES_LAKH
premium_per_share = LST["ipo_price"] - FACE
premium_total = fresh * premium_per_share                 # Rs lakh (shares in lakh x Rs)
cap_add = fresh * FACE
assert abs(cap_add + premium_total - LST["ipo_proceeds"]) < 1e-9
out["capital"] = {
    "face": FACE, "authorised_shares_lakh": AUTH_SHARES_LAKH, "authorised_capital_lakh": AUTH_SHARES_LAKH * FACE,
    "pre_ipo_shares_lakh": pre, "pre_ipo_paid_up_lakh": pre * FACE, "pre_ipo_headroom_lakh": r(AUTH_SHARES_LAKH - pre, 1),
    "fresh_shares_lakh": fresh, "post_ipo_shares_lakh": post, "post_ipo_paid_up_lakh": r(post * FACE, 1),
    "post_headroom_shares_lakh": r(AUTH_SHARES_LAKH - post, 1),
    "ipo_price": LST["ipo_price"], "premium_per_share": premium_per_share,
    "capital_added_lakh": r(cap_add, 1), "premium_lakh": r(premium_total, 1), "proceeds_lakh": LST["ipo_proceeds"],
    "partly_paid_example": {"shares_lakh": 1.0, "called_per_share": 6, "uncalled_per_share": FACE - 6,
                            "paid_up_lakh": 6.0, "issued_lakh": 10.0},
}

header = """# Jargon, Decoded — Module 9 ("Finance building blocks"): every figure quoted in the
# yield curve, credit rating, depreciation, effective tax rate, futures basis and
# share capital posts.
#
# GENERATED by scripts/derive_jargon_m9.py — do not edit by hand; re-run the script.
# Hypothetical: the curves, the rating grid, the futures inputs, Desi Bites'
# authorised capital (a new fictional fact). Desi Bites' accounts come from
# _data/case_study.yml.

"""
OUT.write_text(header + yaml.dump(out, Dumper=_NoAlias, sort_keys=False, allow_unicode=True, default_flow_style=False), encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))
