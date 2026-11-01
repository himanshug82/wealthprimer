#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure used by module 3 of "Risk, Leverage and Your Own Brain"
(_data/risk3.yml): options, mechanically.

    python3 scripts/derive_risk3.py        # rewrites _data/risk3.yml

Posts (2026-11-04 .. 2026-11-09): call and put options; option payoff and
breakeven; time value; implied volatility; option writing and margin;
expiry and settlement.

Everything here is a HYPOTHETICAL underlying ("the Sample Index"): no real
index level, no real option quote, no live implied volatility is used.

Model used for time value and implied volatility (an ASSUMPTION, stated in the
posts): Black-Scholes-Merton price for a European option, zero interest rate,
zero dividends, flat volatility. It is a teaching model, not a quote.

Reported facts typed by hand (each from a primary source opened on 1 Nov 2026)
live in the SOURCES dict:
  SEBI circular SEBI/HO/MRD/TPD-1/P/CIR/2024/132, 1 October 2024 (read in full):
    - contract value at introduction not less than Rs 15 lakh; lot size so that
      the contract value on the review day is within Rs 15 lakh to Rs 20 lakh
      (para 5.4.1; effective for new index contracts after 20 Nov 2024)
    - option premium collected upfront from buyers (para 5.1; from 1 Feb 2025)
    - additional extreme loss margin (ELM) of 2% for short options on the day
      of expiry (para 5.6; from 20 Nov 2024)
    - no calendar-spread margin benefit on expiry day (para 5.2; 1 Feb 2025)
    - each exchange: weekly expiry on only one benchmark index (para 5.5)
  SEBI circular HO/47/11/11(3)2025-MRD-POD2/I/23843/2026, 15 October 2026
  (read in full; effective 7 December 2026, para 4.8 on 8 February 2027).
  SEBI circular of 16 January 2026 on the Closing Auction Session (read;
  CAS framework to be implemented from 3 August 2026).
  SEBI Master Circular for Stock Exchanges and Clearing Corporations,
  30 December 2024, Chapter 5 (read): index options are premium-style; premium
  paid in cash on T+1 (2.2.2.5); physical settlement mandatory for all stock
  derivatives (3.1.10).
  NSE equity-derivatives contract-specification page, "Updated on: 11/08/2026":
  Tuesday expiry for the listed indices; Nifty 50 has four weekly and three
  monthly expiries.

Fund-of-facts about SEBI's F&O studies come from _data/fno.yml, not this file.
Invariants are asserted.
"""
import math
import os
import yaml

OUT = os.path.join(os.path.dirname(__file__), "..", "_data", "risk3.yml")

# ---------------------------------------------------------------- the contract
LEVEL = 20000          # Sample Index level, points
LOT = 75               # units per lot (hypothetical)
STRIKE = 20000         # at-the-money strike
SPECIFIED_MIN, SPECIFIED_MAX = 1500000, 2000000   # SEBI band, rupees

contract_value = LEVEL * LOT
assert SPECIFIED_MIN <= contract_value <= SPECIFIED_MAX


def inr(x):
    return int(round(x))


# ------------------------------------------------------- Black-Scholes helpers
def ncdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bs(kind, s, k, t_years, vol):
    """European option, r = q = 0."""
    intrinsic = max(s - k, 0) if kind == "call" else max(k - s, 0)
    if t_years <= 0:
        return float(intrinsic)
    sd = vol * math.sqrt(t_years)
    d1 = (math.log(s / k) + 0.5 * sd * sd) / sd
    d2 = d1 - sd
    if kind == "call":
        return s * ncdf(d1) - k * ncdf(d2)
    return k * ncdf(-d2) - s * ncdf(-d1)


def implied_vol(kind, price, s, k, t_years):
    lo, hi = 0.0001, 3.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if bs(kind, s, k, t_years, mid) < price:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


DAYS_IN_YEAR = 365.0

# Premiums used in posts 1, 2 and 5 come from the same model as post 3 and 4:
# 30 days to expiry, 15% annualised volatility, so the posts agree with each other.
BASE_VOL, BASE_DAYS = 0.15, 30
CALL_PREM = round(bs("call", LEVEL, STRIKE, BASE_DAYS / DAYS_IN_YEAR, BASE_VOL))
PUT_PREM = round(bs("put", LEVEL, STRIKE, BASE_DAYS / DAYS_IN_YEAR, BASE_VOL))

# --------------------------------------------------------------------- post 1/2
levels = list(range(19000, 21001, 250))


def call_pl(s):   # buyer, per lot, rupees
    return (max(s - STRIKE, 0) - CALL_PREM) * LOT


def put_pl(s):
    return (max(STRIKE - s, 0) - PUT_PREM) * LOT


buyer_table = []
for s in levels:
    buyer_table.append({
        "level": s,
        "move_pct": round((s / LEVEL - 1) * 100, 2),
        "call_payoff": inr(max(s - STRIKE, 0) * LOT),
        "call_pl": inr(call_pl(s)),
        "put_payoff": inr(max(STRIKE - s, 0) * LOT),
        "put_pl": inr(put_pl(s)),
    })

call_premium_rs = CALL_PREM * LOT
put_premium_rs = PUT_PREM * LOT
call_be = STRIKE + CALL_PREM
put_be = STRIKE - PUT_PREM
assert call_pl(call_be) == 0 and put_pl(put_be) == 0
assert min(call_pl(s) for s in levels) == -call_premium_rs
assert min(put_pl(s) for s in levels) == -put_premium_rs

# an out-of-the-money pair for the breakeven post
OTM_STRIKE_CALL, OTM_STRIKE_PUT = 20500, 19500
OTM_PREM_CALL = round(bs('call', LEVEL, OTM_STRIKE_CALL, BASE_DAYS / DAYS_IN_YEAR, BASE_VOL))
OTM_PREM_PUT = round(bs('put', LEVEL, OTM_STRIKE_PUT, BASE_DAYS / DAYS_IN_YEAR, BASE_VOL))
otm = {
    "call_strike": OTM_STRIKE_CALL, "call_prem": OTM_PREM_CALL,
    "call_prem_rs": OTM_PREM_CALL * LOT,
    "call_be": OTM_STRIKE_CALL + OTM_PREM_CALL,
    "call_be_move_pct": round(((OTM_STRIKE_CALL + OTM_PREM_CALL) / LEVEL - 1) * 100, 2),
    "put_strike": OTM_STRIKE_PUT, "put_prem": OTM_PREM_PUT,
    "put_prem_rs": OTM_PREM_PUT * LOT,
    "put_be": OTM_STRIKE_PUT - OTM_PREM_PUT,
    "put_be_move_pct": round(((OTM_STRIKE_PUT - OTM_PREM_PUT) / LEVEL - 1) * 100, 2),
}
atm = {
    "call_be": call_be, "put_be": put_be,
    "call_be_move_pct": round((call_be / LEVEL - 1) * 100, 2),
    "put_be_move_pct": round((put_be / LEVEL - 1) * 100, 2),
}
# prem as a share of contract value
prem_share_pct = round(call_premium_rs / contract_value * 100, 2)

# ----------------------------------------------------------------------- post 3
TV_VOL = BASE_VOL
tv_days = [30, 20, 10, 5, 2, 1, 0]
tv_rows = []
for d in tv_days:
    t = d / DAYS_IN_YEAR
    atm_c = bs("call", LEVEL, 20000, t, TV_VOL)
    itm_c = bs("call", LEVEL, 19500, t, TV_VOL)
    otm_c = bs("call", LEVEL, 20500, t, TV_VOL)
    tv_rows.append({
        "days": d,
        "atm_price": round(atm_c, 1),
        "atm_tv": round(atm_c - 0, 1),                      # intrinsic 0
        "itm_price": round(itm_c, 1),
        "itm_tv": round(itm_c - (LEVEL - 19500), 1),
        "otm_price": round(otm_c, 1),
        "otm_tv": round(otm_c, 1),
    })
for a, b in zip(tv_rows, tv_rows[1:]):
    assert b["atm_tv"] <= a["atm_tv"] + 1e-9, "ATM time value must fall as expiry nears"
    assert b["otm_tv"] <= a["otm_tv"] + 1e-9
assert tv_rows[-1]["atm_tv"] == 0 and tv_rows[-1]["otm_tv"] == 0
assert abs(tv_rows[-1]["itm_tv"]) < 1e-9
assert all(r["itm_tv"] >= -1e-9 for r in tv_rows)
# decay per day, ATM, in each leg
for i in range(len(tv_rows) - 1):
    a, b = tv_rows[i], tv_rows[i + 1]
    span = a["days"] - b["days"]
    a["atm_decay_per_day"] = round((a["atm_tv"] - b["atm_tv"]) / span, 1)
tv_rows[-1]["atm_decay_per_day"] = None
first_leg = (tv_rows[0]["atm_tv"] - tv_rows[1]["atm_tv"]) / 10
last_leg = tv_rows[-2]["atm_tv"] - tv_rows[-1]["atm_tv"]    # last day
assert last_leg > first_leg, "decay per day should be larger in the last day than in the first leg"
tv_note = {
    "vol_pct": int(TV_VOL * 100),
    "first_leg_per_day": round(first_leg, 1),
    "last_day": round(last_leg, 1),
    "tv_30_over_tv_5_ratio": round(tv_rows[0]["atm_tv"] / tv_rows[3]["atm_tv"], 2),
}

# ----------------------------------------------------------------------- post 4
iv_t = 30 / DAYS_IN_YEAR
vol_rows = []
for v in (10, 15, 20, 25, 30, 40):
    vol_rows.append({"vol_pct": v, "atm_call": round(bs("call", LEVEL, 20000, iv_t, v / 100), 1)})
for a, b in zip(vol_rows, vol_rows[1:]):
    assert b["atm_call"] > a["atm_call"]
# invert: quotes -> implied vol
quote_prices = [(20000, 150), (20000, 250), (20000, 350), (20500, 120), (19500, 560)]
iv_rows = []
for k, p in quote_prices:
    kind = "call"
    v = implied_vol(kind, p, LEVEL, k, iv_t)
    back = bs(kind, LEVEL, k, iv_t, v)
    assert abs(back - p) < 1e-6, (k, p, back)
    iv_rows.append({"strike": k, "price": p, "iv_pct": round(v * 100, 1)})
# the same option, same vol, 2 expiries: price scales with sqrt(time)
sqrt_demo = {
    "price_30d": round(bs("call", LEVEL, 20000, 30 / 365, 0.15), 1),
    "price_120d": round(bs("call", LEVEL, 20000, 120 / 365, 0.15), 1),
}
sqrt_demo["ratio"] = round(sqrt_demo["price_120d"] / sqrt_demo["price_30d"], 2)
assert 1.9 < sqrt_demo["ratio"] < 2.1      # 4x time -> about 2x price (sqrt law, ATM)
# a 1-vol-point sensitivity
vega_pts = round(bs("call", LEVEL, 20000, iv_t, 0.16) - bs("call", LEVEL, 20000, iv_t, 0.15), 1)
# same underlying level, vol rises 15 -> 20 with 30 days to go
vol_up = {
    "from_pct": 15, "to_pct": 20,
    "price_from": round(bs("call", LEVEL, 20000, iv_t, 0.15), 1),
    "price_to": round(bs("call", LEVEL, 20000, iv_t, 0.20), 1),
}
vol_up["gain_pts"] = round(vol_up["price_to"] - vol_up["price_from"], 1)

# ----------------------------------------------------------------------- post 5
W_STRIKE, W_PREM = STRIKE, CALL_PREM
w_levels = [18500, 19000, 19500, 19800, 20000, 20350, 20500, 21000, 21500, 22000, 23000]


def short_call_pl(s):
    return (W_PREM - max(s - W_STRIKE, 0)) * LOT


def short_put_pl(s):
    return (W_PREM - max(W_STRIKE - s, 0)) * LOT


# illustrative margin assumptions (NOT an exchange figure)
ASSUMED_MARGIN_PCT = 12
ELM_EXPIRY_PCT = 2          # SEBI circular 5.6: additional ELM of 2% on short options on expiry day
assumed_margin = contract_value * ASSUMED_MARGIN_PCT // 100
expiry_extra = contract_value * ELM_EXPIRY_PCT // 100
w_rows = []
for s in w_levels:
    w_rows.append({
        "level": s,
        "move_pct": round((s / LEVEL - 1) * 100, 2),
        "call_pl": inr(short_call_pl(s)),
        "call_pl_margin_pct": round(short_call_pl(s) / assumed_margin * 100, 1),
        "put_pl": inr(short_put_pl(s)),
        "put_pl_margin_pct": round(short_put_pl(s) / assumed_margin * 100, 1),
    })
max_gain = W_PREM * LOT
assert short_call_pl(25000) < short_call_pl(23000) < short_call_pl(22000)   # keeps falling, no floor
assert short_call_pl(10 ** 6) == (W_PREM - (10 ** 6 - W_STRIKE)) * LOT
assert max(short_call_pl(s) for s in w_levels) == max_gain
put_floor = short_put_pl(0)      # index cannot go below zero
assert put_floor == (W_PREM - W_STRIKE) * LOT
writing = {
    "strike": W_STRIKE, "prem": W_PREM, "max_gain": max_gain,
    "margin_pct": ASSUMED_MARGIN_PCT, "assumed_margin": assumed_margin,
    "elm_pct": ELM_EXPIRY_PCT, "expiry_extra": expiry_extra,
    "gain_over_margin_pct": round(max_gain / assumed_margin * 100, 1),
    "call_breakeven": W_STRIKE + W_PREM, "put_breakeven": W_STRIKE - W_PREM,
    "put_worst_case": inr(-put_floor),
    "example_level": 22000,
    "example_move_pct": int(round((22000 / LEVEL - 1) * 100)),
    "example_loss_pct_margin": abs(round(short_call_pl(22000) / assumed_margin * 100, 1)),
    "loss_at_22000_call": inr(-short_call_pl(22000)),
    "loss_at_22000_vs_gain_multiple": round(-short_call_pl(22000) / max_gain, 1),
    "rows": w_rows,
}
assert writing["loss_at_22000_call"] == (22000 - W_STRIKE - W_PREM) * LOT

# ----------------------------------------------------------------------- post 6
# six five-minute buckets of the last 30 minutes of the continuous session,
# one illustrative constituent (price, volume)
buckets = [
    ("2:55-3:00 pm", 20190, 40),
    ("3:00-3:05 pm", 20195, 55),
    ("3:05-3:10 pm", 20210, 90),
    ("3:10-3:15 pm", 20205, 60),
    ("3:15-3:20 pm", 20190, 120),
    ("3:20-3:25 pm", 20170, 150),
]
last_print = 20215          # final trade before the close, illustrative
vwap = sum(p * v for _, p, v in buckets) / sum(v for _, _, v in buckets)
assert min(p for _, p, _ in buckets) <= vwap <= max(p for _, p, _ in buckets)
S_K = 20200                 # call strike for the boundary illustration
settle_vwap = round(vwap, 2)
call_lot_pl_vwap = (max(settle_vwap - S_K, 0) - 0) * LOT   # payoff before premium
call_lot_pl_last = (max(last_print - S_K, 0)) * LOT
assert settle_vwap < S_K < last_print
expiry = {
    "buckets": [{"window": w, "price": p, "volume": v, "pv": p * v} for w, p, v in buckets],
    "total_volume": sum(v for _, _, v in buckets),
    "total_pv": sum(p * v for _, p, v in buckets),
    "vwap": settle_vwap,
    "last_print": last_print,
    "strike": S_K,
    "payoff_vwap": inr(call_lot_pl_vwap),
    "payoff_last": inr(call_lot_pl_last),
    "diff_pts": round(last_print - settle_vwap, 2),
    "sebi_oct2026": {
        "number": "HO/47/11/11(3)2025-MRD-POD2/I/23843/2026",
        "date": "15 October 2026",
        "effective": "7 December 2026",
        "cas_start": "3:30 p.m.", "cas_end": "3:40 p.m.",
        "index_expiry_stop": "3:30 p.m.",
        "derivs_stop": "3:45 p.m.",
        "window_min": 30,
        "iceberg_effective": "8 February 2027",
    },
    "sebi_jan2026": {
        "date": "16 January 2026",
        "cas_start": "3 August 2026",
    },
    "sebi_oct2024": {
        "number": "SEBI/HO/MRD/TPD-1/P/CIR/2024/132",
        "date": "1 October 2024",
    },
    "nse": {"page_date": "11 August 2026", "expiry_day": "Tuesday"},
}

doc = {
    "contract": {
        "level": LEVEL, "lot": LOT, "value": contract_value,
        "sebi_min": SPECIFIED_MIN, "sebi_max": SPECIFIED_MAX,
        "strike": STRIKE,
        "call_prem": CALL_PREM, "put_prem": PUT_PREM,
        "call_prem_rs": call_premium_rs, "put_prem_rs": put_premium_rs,
        "prem_share_pct": prem_share_pct,
    },
    "buyer": {"table": buyer_table},
    "breakeven": {"atm": atm, "otm": otm},
    "time_value": {"vol_pct": int(TV_VOL * 100), "rows": tv_rows, "note": tv_note},
    "implied_vol": {
        "days": 30, "vol_rows": vol_rows, "iv_rows": iv_rows,
        "sqrt": sqrt_demo, "one_vol_point_pts": vega_pts, "vol_up": vol_up,
    },
    "writing": writing,
    "expiry": expiry,
}

with open(OUT, "w", encoding="utf-8") as f:
    f.write("# GENERATED by scripts/derive_risk3.py — do not edit by hand.\n")
    f.write("# Hypothetical Sample Index; Black-Scholes-Merton with zero rate and dividends (teaching model).\n")
    yaml.safe_dump(doc, f, allow_unicode=True, sort_keys=False)
print("wrote", OUT)
