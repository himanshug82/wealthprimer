#!/usr/bin/env python3
"""
Reproduce the SIP examples in _data/tax.yml (example_sip, example_loss) from the
committed NAV CSV and assert they still match.

    python3 scripts/derive_tax.py

NAV DATE CONVENTION (the same one _data/mf.yml uses for the SIP/XIRR post, so the
two series agree): each instalment is dated the 1st of the month and buys at the
latest NAV on or before that date (when the 1st is a holiday, the previous
business day's NAV). A real SIP falling on a holiday is allotted at the NEXT
business day's NAV; on that rule the 5-year example gains Rs 88,165 instead of
Rs 88,376 (long-term 1,00,506, short-term -12,341). The posts say so. Lot split:
an instalment is long-term if held more than 12 months at redemption.
Regular plan, growth; redemption at the last NAV on or before 31 March 2026.
"""
from pathlib import Path
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parent.parent
nav = (pd.read_csv(ROOT / "assets/data/uti-nifty50-index-fund-nav.csv", parse_dates=["date"])
       .set_index("date")["nav_regular_growth"].dropna())
tax = yaml.safe_load((ROOT / "_data/tax.yml").read_text(encoding="utf-8"))


def sip(start, last, redeem, amount, rule="on_or_before"):
    red = pd.Timestamp(redeem)
    rnav = nav.loc[:red].iloc[-1]
    out = dict(lt=0.0, st=0.0, ltn=0, stn=0, units=0.0)
    for d in pd.date_range(start, last, freq="MS"):
        ad = nav.loc[:d].index[-1] if rule == "on_or_before" else nav.loc[d:].index[0]
        u = amount / nav[ad]
        out["units"] += u
        k = "lt" if ad < red - pd.DateOffset(months=12) else "st"
        out[k] += u * rnav - amount
        out[k + "n"] += 1
    n = out["ltn"] + out["stn"]
    value = round(out["units"] * rnav)
    return dict(redemption_nav=round(float(rnav), 4), value=value, gain=value - amount * n,
                lt=round(out["lt"]), st=round(out["st"]), ltn=out["ltn"], stn=out["stn"])


s = tax["example_sip"]
r = sip(s["start"], s["last_instalment"], s["redemption_date"], s["monthly_amount"])
assert (r["value"], r["gain"], r["lt"], r["st"], r["ltn"], r["stn"]) == (
    s["value"], s["total_gain"], s["long_term_gain"], s["short_term_gain"], s["long_term_lots"], s["short_term_lots"]), r
assert abs(r["redemption_nav"] - s["redemption_nav"]) < 1e-4
alt = sip(s["start"], s["last_instalment"], s["redemption_date"], s["monthly_amount"], rule="next")
assert s["next_business_day_gain"] == alt["gain"], alt

l = tax["example_loss"]
r = sip(l["start"], "2026-03-01", l["redemption_date"], l["monthly_amount"])
assert (r["value"], r["gain"], r["lt"], r["st"], r["ltn"], r["stn"]) == (
    l["value"], l["total_loss"], l["long_term_loss"], l["short_term_loss"], l["long_term_lots"], l["short_term_lots"]), r
alt = sip(l["start"], "2026-03-01", l["redemption_date"], l["monthly_amount"], rule="next")
assert l["next_business_day_loss_abs"] == -alt["gain"], alt
print("tax.yml SIP examples reproduce (on-or-before rule); next-business-day figures match")
