#!/usr/bin/env python3
"""
Derive every figure used by module 2 of "Money Before Markets", "Putting a
portfolio together" (_data/mbm2.yml): compounding, asset classes, investment
horizon, asset allocation, goal-based investing, glide path, and the limits
of model portfolios. Roadmap: _review/roadmaps/2026-11-21-money-before-markets-m2.md

    python3 scripts/derive_mbm2.py        # rewrites _data/mbm2.yml

INPUTS (read-only)
  assets/data/nifty50-tri.csv           niftyindices.com Nifty 50 Total Returns Index (TRI)
  assets/data/uti-gilt-fund-nav.csv     AMFI via mfapi.in, UTI Gilt Fund, regular plan growth
  assets/data/uti-liquid-fund-nav.csv   AMFI via mfapi.in, UTI Liquid Fund, regular plan growth
  assets/data/uti-gold-etf-nav.csv      AMFI via mfapi.in (scheme code 105463), UTI Gold ETF.
                                        The NAV falls by a factor of about 100 between 26 and
                                        30 March 2021, consistent with a unit split; NAVs before
                                        30 March 2021 are divided by SPLIT_FACTOR here. Verify the
                                        split ratio against UTI's notice (TODO.md VERIFY row).
  assets/data/cpi-all-india-combined.csv MoSPI CPI (Combined); FY inflation chained as in
                                        derive_risk2.py: base 2012 to March 2025, base 2024 for FY26.

HYPOTHETICAL (assumptions, not forecasts): the rates in the compounding tables, the
goal-based example (cost, years, inflation and return scenarios), the 10% step-up.
REAL, backward-looking: the four series above, 31 March 2008 to 30/31 March 2026.

LAG: first post 20 January 2027 (cut-off 20 October 2026); all series end March 2026.

Needs pandas, numpy, pyyaml.
"""
import math
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_data" / "mbm2.yml"
FIRST_POST = pd.Timestamp("2027-01-20")
CUTOFF = FIRST_POST - pd.DateOffset(months=3)
START = pd.Timestamp("2008-03-31")   # first FY end after the gold ETF's first full year
SPLIT_DATE = pd.Timestamp("2021-03-30")
SPLIT_FACTOR = 100
ASSETS = ["equity", "gilt", "liquid", "gold"]
LABEL = {"equity": "Equity (Nifty 50 TRI)", "gilt": "Government bonds (UTI Gilt Fund)",
         "liquid": "Cash-like (UTI Liquid Fund)", "gold": "Gold (UTI Gold ETF)"}


def r2(x):
    return float(round(float(x), 2))


def c2(x):
    """A correlation, always shown to two decimals."""
    return f"{float(x):.2f}"


def r1(x):
    return float(round(float(x), 1))


def pct(x, nd=1):
    return float(round(float(x) * 100, nd))


def rupees(x):
    return int(round(float(x)))


# ---------------------------------------------------------------- data
def load(name, col):
    s = pd.read_csv(ROOT / "assets/data" / name, parse_dates=["date"]).set_index("date")[col]
    return s.dropna().sort_index()


eq = load("nifty50-tri.csv", "nifty50_tri_close")
gilt = load("uti-gilt-fund-nav.csv", "nav_regular_growth")
liq = load("uti-liquid-fund-nav.csv", "nav_regular_growth")
gold = load("uti-gold-etf-nav.csv", "nav")

# the unit split: assert the jump is there and about 100x, then adjust
before = gold[gold.index < SPLIT_DATE].iloc[-1]
after = gold[gold.index >= SPLIT_DATE].iloc[0]
assert 95 < before / after < 105, before / after
gold = gold.where(gold.index >= SPLIT_DATE, gold / SPLIT_FACTOR)
assert (gold.pct_change().abs().dropna() < 0.15).all(), "unexplained jump in gold NAV"

for s in (eq, gilt, liq, gold):
    assert s.index.max() <= CUTOFF, "data newer than the lag allows"

# daily panel on the index's trading days, funds forward-filled to those days
px = pd.DataFrame({"equity": eq})
for k, s in (("gilt", gilt), ("liquid", liq), ("gold", gold)):
    px[k] = s.reindex(px.index.union(s.index)).ffill().reindex(px.index)
px = px[px.index >= START].dropna()
assert px.index[0] == START
END = px.index[-1]
rets = px.pct_change().dropna()


def on_or_before(s, d):
    return s[s.index <= d].iloc[-1]


def fy_end(y):
    return pd.Timestamp(f"{y}-03-31")


FYS = list(range(2009, 2027))          # FY09 .. FY26
fy_px = pd.DataFrame({a: [on_or_before(px[a], fy_end(y)) for y in [2008] + FYS] for a in ASSETS},
                     index=[2008] + FYS)
fy_ret = fy_px.pct_change().dropna()

# CPI, FY inflation (March to March), chained across the base change
cpi = pd.read_csv(ROOT / "assets/data/cpi-all-india-combined.csv")
cpi = cpi.set_index("month")
infl = {}
for y in range(2014, 2027):
    if y <= 2025:
        infl[y] = cpi.loc[f"{y}-03", "cpi_base2012"] / cpi.loc[f"{y-1}-03", "cpi_base2012"] - 1
    else:
        infl[y] = cpi.loc[f"{y}-03", "cpi_base2024"] / cpi.loc[f"{y-1}-03", "cpi_base2024"] - 1
infl = pd.Series(infl)


def cagr(v0, v1, years):
    return (v1 / v0) ** (1 / years) - 1


def years_between(a, b):
    return (b - a).days / 365.25


def max_drawdown(series):
    peak = series.cummax()
    dd = series / peak - 1
    trough = dd.idxmin()
    pk = series[:trough].idxmax()
    rec = series[trough:][series[trough:] >= series[pk]]
    return dd.min(), pk, trough, (rec.index[0] if len(rec) else None)


def fmt_date(d):
    return f"{d.day} {d.strftime('%B %Y')}" if d is not None else None


def fmt_month(d):
    return d.strftime("%B %Y")


out = {
    "dataset": {
        "start": fmt_date(START), "end": fmt_date(END), "end_month": fmt_month(END),
        "fy_first": "FY09", "fy_last": "FY26", "fy_count": len(FYS),
        "labels": LABEL,
        "gold_scheme_code": 105463,
        "gold_split_date": fmt_date(SPLIT_DATE), "gold_split_factor": SPLIT_FACTOR,
        "gold_source_url": "https://api.mfapi.in/mf/105463",
        "gilt_source_url": "https://api.mfapi.in/mf/102510",
        "liquid_source_url": "https://api.mfapi.in/mf/102012",
        "tri_source_url": "https://www.niftyindices.com/reports/historical-data",
        "cpi_source_url": "https://www.mospi.gov.in/",
        "csv": {"equity": "/assets/data/nifty50-tri.csv", "gilt": "/assets/data/uti-gilt-fund-nav.csv",
                "liquid": "/assets/data/uti-liquid-fund-nav.csv", "gold": "/assets/data/uti-gold-etf-nav.csv",
                "cpi": "/assets/data/cpi-all-india-combined.csv"},
    }
}

# ---------------------------------------------------------------- 1. compounding
rates = [4, 6, 8, 10, 12]
horizons = [5, 10, 20, 30]
grid = []
for r in rates:
    grid.append({"rate_pct": r, "values": [rupees(100000 * (1 + r / 100) ** n) for n in horizons]})
rule72 = []
for r in [3, 6, 8, 9, 12, 18, 24]:
    exact = math.log(2) / math.log(1 + r / 100)
    rule72.append({"rate_pct": r, "rule72": r1(72 / r), "exact": r1(exact), "gap": r1(abs(72 / r - exact)) * (1 if 72 / r >= exact else -1) + 0.0})
# where the gain arrives: Rs 1 lakh at 10% for 30 years, gain per decade
v = [100000 * 1.1 ** n for n in (0, 10, 20, 30)]
decades = [{"years": f"{i*10+1}–{i*10+10}", "start": rupees(v[i]), "end": rupees(v[i+1]),
            "gain": rupees(v[i+1] - v[i]), "share_pct": pct((v[i+1] - v[i]) / (v[3] - v[0]))}
           for i in range(3)]
assert sum(d["gain"] for d in decades) in range(rupees(v[3] - v[0]) - 2, rupees(v[3] - v[0]) + 3)


def sip_fv(monthly, annual_rate, years, step_up=0.0):
    """Instalment at the start of each month; amount rises by step_up once a year."""
    m = (1 + annual_rate) ** (1 / 12) - 1
    total, paid = 0.0, 0.0
    for k in range(years * 12):
        amt = monthly * (1 + step_up) ** (k // 12)
        total = (total + amt) * (1 + m)
        paid += amt
    return total, paid


a_fv, a_paid = sip_fv(5000, 0.10, 30)
b_fv, b_paid = sip_fv(10000, 0.10, 15)
c_fv, c_paid = sip_fv(10000, 0.10, 30)
assert abs(a_paid - b_paid) < 1
comp_real_v = px["equity"].iloc[-1] / px["equity"].iloc[0] * 100000
out["compounding"] = {
    "horizons": horizons, "grid": grid, "rule72": rule72, "decades": decades,
    "decade_rate_pct": 10, "decade_final": rupees(v[3]),
    "sip": {
        "rate_pct": 10,
        "a": {"monthly": 5000, "years": 30, "paid": rupees(a_paid), "fv": rupees(a_fv)},
        "b": {"monthly": 10000, "years": 15, "paid": rupees(b_paid), "fv": rupees(b_fv)},
        "c": {"monthly": 10000, "years": 30, "paid": rupees(c_paid), "fv": rupees(c_fv)},
        "a_over_b": r1(a_fv / b_fv),
    },
    "real": {
        "years": r1(years_between(START, END)),
        "lakh_became": rupees(comp_real_v),
        "cagr_pct": pct(cagr(100000, comp_real_v, years_between(START, END))),
        "negative_fys": int((fy_ret["equity"] < 0).sum()),
        "worst_fy": f"FY{str(fy_ret['equity'].idxmin())[2:]}",
        "worst_fy_pct": pct(fy_ret["equity"].min()),
        "best_fy": f"FY{str(fy_ret['equity'].idxmax())[2:]}",
        "best_fy_pct": pct(fy_ret["equity"].max()),
    },
}

# ---------------------------------------------------------------- 2. asset classes
yrs = years_between(START, END)
summary = {}
for a in ASSETS:
    mdd, pk, tr, rec = max_drawdown(px[a])
    summary[a] = {
        "label": LABEL[a],
        "cagr_pct": pct(cagr(px[a].iloc[0], px[a].iloc[-1], yrs)),
        "lakh_became": rupees(px[a].iloc[-1] / px[a].iloc[0] * 100000),
        "vol_pct": pct(rets[a].std() * math.sqrt(252)),
        "worst_fy_pct": pct(fy_ret[a].min()), "worst_fy": f"FY{str(fy_ret[a].idxmin())[2:]}",
        "best_fy_pct": pct(fy_ret[a].max()), "best_fy": f"FY{str(fy_ret[a].idxmax())[2:]}",
        "negative_fys": int((fy_ret[a] < 0).sum()),
        "max_dd_pct": pct(-mdd), "dd_peak": fmt_date(pk), "dd_trough": fmt_date(tr),
        "dd_recovered": fmt_date(rec),
    }
# like-with-like real returns over FY14..FY26 (the CPI series starts 2013)
cpi_cum = float((1 + infl).prod())
real = {}
for a in ASSETS:
    nom = fy_px.loc[2026, a] / fy_px.loc[2013, a]
    real[a] = {"nominal_cagr_pct": pct(nom ** (1 / 13) - 1), "real_cagr_pct": pct((nom / cpi_cum) ** (1 / 13) - 1)}
fy_rows = []
for y in FYS:
    row = {"fy": f"FY{str(y)[2:]}"}
    for a in ASSETS:
        row[a] = pct(fy_ret.loc[y, a])
    row["best"] = max(ASSETS, key=lambda a: fy_ret.loc[y, a])
    fy_rows.append(row)
best_counts = {a: sum(1 for r in fy_rows if r["best"] == a) for a in ASSETS}
assert sum(best_counts.values()) == len(FYS)
corr = fy_ret.corr()
dcorr = rets.corr()
out["asset_classes"] = {
    "summary": summary, "fy_rows": fy_rows, "best_counts": best_counts,
    "real": real, "real_first_fy": "FY14", "real_last_fy": "FY26",
    "cpi_cagr_pct": pct(cpi_cum ** (1 / 13) - 1),
    "corr_fy": {"equity_gilt": c2(corr.loc["equity", "gilt"]), "equity_gold": c2(corr.loc["equity", "gold"]),
                "gilt_gold": c2(corr.loc["gilt", "gold"])},
    "corr_daily": {"equity_gilt": c2(dcorr.loc["equity", "gilt"]), "equity_gold": c2(dcorr.loc["equity", "gold"]),
                   "gilt_gold": c2(dcorr.loc["gilt", "gold"])},
}

# ---------------------------------------------------------------- 3. horizon (rolling windows)
hz = {}
idx = px.index
for n in [1, 3, 5, 10]:
    starts, ends = [], []
    for s in idx:
        target = s + pd.DateOffset(years=n)
        if target > END:
            break
        e = idx[idx <= target][-1]
        starts.append(s)
        ends.append(e)
    starts, ends = pd.DatetimeIndex(starts), pd.DatetimeIndex(ends)
    res = {"windows": len(starts), "first_start": fmt_date(starts[0]), "last_start": fmt_date(starts[-1]),
           "dropped_note": "start dates after " + fmt_date(starts[-1]) + " have no complete window"}
    cg = {}
    for a in ASSETS:
        tot = px[a].reindex(ends).values / px[a].reindex(starts).values
        c = tot ** (1 / n) - 1
        cg[a] = c
        res[a] = {"neg_pct": pct((c < 0).mean()), "worst_pct": pct(c.min()), "median_pct": pct(np.median(c)),
                  "best_pct": pct(c.max())}
    res["equity_below_liquid_pct"] = pct((cg["equity"] < cg["liquid"]).mean())
    res["gold_below_liquid_pct"] = pct((cg["gold"] < cg["liquid"]).mean())
    hz[f"y{n}"] = res
out["horizon"] = hz

# ---------------------------------------------------------------- 4. allocation (annual rebalancing)
def run_mix(weights, start=None, end=None, glide=None):
    """Daily value of Rs 1 with target weights reset on the first trading day of each FY
    (and on the start day). `glide` is a function year_index -> weights."""
    p = px if start is None else px[(px.index >= start) & (px.index <= end)]
    vals = []
    value = 1.0
    units = None
    year_i = -1
    last_reset_fy = None
    for d in p.index:
        fy = d.year + (1 if d.month >= 4 else 0)
        reset = units is None or (glide is None and fy != last_reset_fy)
        if glide is not None and units is not None:
            # glide: reset on each anniversary of the start
            yi = int(years_between(p.index[0], d) + 1e-9)
            reset = yi != year_i
        if reset:
            if units is not None:
                value = sum(units[a] * p.at[d, a] for a in units)
            if glide is not None:
                year_i = int(years_between(p.index[0], d) + 1e-9)
                w = glide(year_i)
            else:
                w = weights
            assert abs(sum(w.values()) - 1) < 1e-9
            units = {a: value * w[a] / p.at[d, a] for a in w}
            last_reset_fy = fy
        vals.append(sum(units[a] * p.at[d, a] for a in units))
    return pd.Series(vals, index=p.index)


mixes = [(100, 0, 0), (80, 20, 0), (60, 40, 0), (40, 60, 0), (20, 80, 0), (0, 100, 0), (60, 30, 10)]
mix_rows = {}
mix_series = {}
for e, g, au in mixes:
    w = {"equity": e / 100, "gilt": g / 100, "gold": au / 100}
    w = {k: v for k, v in w.items() if v > 0}
    s = run_mix(w)
    mix_series[(e, g, au)] = s
    fyv = pd.Series([on_or_before(s, fy_end(y)) for y in [2008] + FYS], index=[2008] + FYS).pct_change().dropna()
    mdd, pk, tr, rec = max_drawdown(s)
    key = f"m{e}_{g}" + (f"_{au}" if au else "")
    mix_rows[key] = {
        "equity": e, "gilt": g, "gold": au,
        "cagr_pct": pct(cagr(s.iloc[0], s.iloc[-1], yrs)),
        "ten_lakh_became": rupees(s.iloc[-1] / s.iloc[0] * 1000000),
        "vol_pct": pct(s.pct_change().dropna().std() * math.sqrt(252)),
        "max_dd_pct": pct(-mdd), "dd_trough": fmt_date(tr), "dd_peak": fmt_date(pk),
        "worst_fy_pct": pct(fyv.min()), "worst_fy": f"FY{str(fyv.idxmin())[2:]}",
        "negative_fys": int((fyv < 0).sum()),
        "peak_value": rupees(s[pk] / s.iloc[0] * 1000000),
        "trough_value": rupees(s[tr] / s.iloc[0] * 1000000),
        "peak_to_trough": rupees((s[pk] - s[tr]) / s.iloc[0] * 1000000),
    }
# invariants: a 100% sleeve equals the asset itself
assert abs(mix_rows["m100_0"]["cagr_pct"] - summary["equity"]["cagr_pct"]) < 0.05
assert abs(mix_rows["m0_100"]["cagr_pct"] - summary["gilt"]["cagr_pct"]) < 0.05
out["allocation"] = {"rows": mix_rows, "order": [f"m{e}_{g}" + (f"_{au}" if au else "") for e, g, au in mixes]}

# ---------------------------------------------------------------- 5. goal arithmetic (hypothetical)
G = {"cost_today": 1000000, "years": 12, "inflation_pct": 6, "returns_pct": [6, 8, 10, 12],
     "inflations_pct": [5, 6, 7], "step_up_pct": 10, "base_return_pct": 10, "shortfall_return_pct": 8}


def fv_cost(cost, infl_pct, years):
    return cost * (1 + infl_pct / 100) ** years


def sip_needed(target, r_pct, years, step_up=0.0):
    fv1, _ = sip_fv(1.0, r_pct / 100, years, step_up)
    return target / fv1


future = fv_cost(G["cost_today"], G["inflation_pct"], G["years"])
by_return = []
for r in G["returns_pct"]:
    by_return.append({"return_pct": r,
                      "lump_today": rupees(future / (1 + r / 100) ** G["years"]),
                      "monthly": rupees(sip_needed(future, r, G["years"])),
                      "monthly_stepup": rupees(sip_needed(future, r, G["years"], G["step_up_pct"] / 100))})
sens = []
for i in G["inflations_pct"]:
    t = fv_cost(G["cost_today"], i, G["years"])
    sens.append({"inflation_pct": i, "future_cost": rupees(t),
                 "monthly": [rupees(sip_needed(t, r, G["years"])) for r in G["returns_pct"]]})
base_sip = sip_needed(future, G["base_return_pct"], G["years"])
got, paid = sip_fv(base_sip, G["shortfall_return_pct"] / 100, G["years"])
got_ok, _ = sip_fv(base_sip, G["base_return_pct"] / 100, G["years"])
assert abs(got_ok - future) < 1
step_first = sip_needed(future, G["base_return_pct"], G["years"], G["step_up_pct"] / 100)
step_last = step_first * (1 + G["step_up_pct"] / 100) ** (G["years"] - 1)
_, step_paid = sip_fv(step_first, G["base_return_pct"] / 100, G["years"], G["step_up_pct"] / 100)
_, flat_paid = sip_fv(base_sip, G["base_return_pct"] / 100, G["years"])
out["goal"] = {
    **G, "future_cost": rupees(future), "by_return": by_return, "sensitivity": sens,
    "base_monthly": rupees(base_sip), "flat_paid": rupees(flat_paid),
    "shortfall_corpus": rupees(got), "shortfall_gap": rupees(future - got),
    "shortfall_share_pct": pct(got / future),
    "step_first": rupees(step_first), "step_last": rupees(step_last), "step_paid": rupees(step_paid),
}

# ---------------------------------------------------------------- 6. glide path (rolling 10-year windows)
N = 10
month_starts = px.groupby([px.index.year, px.index.month]).head(1).index
starts = [s for s in month_starts if s + pd.DateOffset(years=N) <= END]


def glide_fn(yi):
    e = 0.80 - 0.60 * min(yi, N - 1) / (N - 1)
    return {"equity": e, "gilt": 1 - e}


strategies = {
    "static_50": lambda yi: {"equity": 0.5, "gilt": 0.5},
    "glide": glide_fn,
    "static_80": lambda yi: {"equity": 0.8, "gilt": 0.2},
}
avg_equity = np.mean([glide_fn(i)["equity"] for i in range(N)])
assert abs(avg_equity - 0.5) < 1e-9
gl = {k: {"final": [], "last2_dd": [], "last2_change": [], "eq_w": []} for k in strategies}
for s in starts:
    target = s + pd.DateOffset(years=N)
    e = px.index[px.index <= target][-1]
    for k, f in strategies.items():
        v = run_mix(None, s, e, glide=f)
        # value-weighted equity share: each year's target share weighted by the money held that year
        yr = np.array([int(years_between(s, d) + 1e-9) for d in v.index])
        gl[k]["eq_w"].append(float((np.array([f(min(y, N - 1))["equity"] for y in yr]) * v.values).sum() / v.values.sum()))
        v = v / v.iloc[0] * 1000000
        gl[k]["final"].append(v.iloc[-1])
        two = v[v.index >= (e - pd.DateOffset(years=2))]
        gl[k]["last2_dd"].append(-max_drawdown(two)[0])
        gl[k]["last2_change"].append(two.iloc[-1] / two.iloc[0] - 1)
glide_out = {"windows": len(starts), "first_start": fmt_date(starts[0]), "last_start": fmt_date(starts[-1]),
             "years": N, "glide_from": 80, "glide_to": 20}
for k in strategies:
    f = np.array(gl[k]["final"])
    dd = np.array(gl[k]["last2_dd"])
    ch = np.array(gl[k]["last2_change"])
    glide_out[k] = {
        "median_final": rupees(np.median(f)), "worst_final": rupees(f.min()), "best_final": rupees(f.max()),
        "median_cagr_pct": pct(np.median(f / 1000000) ** (1 / N) - 1),
        "worst_last2_dd_pct": pct(dd.max()), "median_last2_dd_pct": pct(np.median(dd)),
        "last2_dd_over_10_pct": pct((dd > 0.10).mean()),
        "last2_loss_windows_pct": pct((ch < 0).mean()),
        "median_money_weighted_equity_pct": pct(np.median(gl[k]["eq_w"])),
    }
out["glide"] = glide_out

# ---------------------------------------------------------------- 7. limits: the period decides
halves = {"first": (2008, 2017), "second": (2017, 2026)}
lim = {}
for h, (a0, a1) in halves.items():
    row = {"label": f"FY{str(a0 + 1)[2:]}–FY{str(a1)[2:]}"}
    for a in ASSETS:
        row[a] = pct((fy_px.loc[a1, a] / fy_px.loc[a0, a]) ** (1 / (a1 - a0)) - 1)
    row["rank"] = [LABEL[a].split(" (")[0] for a in sorted(ASSETS, key=lambda a: -row[a])]
    s60 = mix_series[(60, 40, 0)]
    row["mix60"] = pct((on_or_before(s60, fy_end(a1)) / on_or_before(s60, fy_end(a0))) ** (1 / (a1 - a0)) - 1)
    sub = fy_ret.loc[a0 + 1:a1]
    row["corr_equity_gilt"] = c2(sub["equity"].corr(sub["gilt"]))
    row["corr_equity_gold"] = c2(sub["equity"].corr(sub["gold"]))
    row["years"] = a1 - a0
    lim[h] = row
out["limits"] = lim
out["limits"]["start_peak"] = summary["equity"]["dd_peak"]
out["limits"]["start_trough"] = summary["equity"]["dd_trough"]
out["limits"]["start_dd_pct"] = summary["equity"]["max_dd_pct"]
out["limits"]["gold_last_fy_pct"] = fy_rows[-1]["gold"]
out["limits"]["gold_cagr_to_fy25_pct"] = pct((fy_px.loc[2025, "gold"] / fy_px.loc[2008, "gold"]) ** (1 / 17) - 1)
out["limits"]["gold_cagr_pct"] = summary["gold"]["cagr_pct"]

def tidy(x, key=""):
    if isinstance(x, dict):
        return {k: tidy(v, k) for k, v in x.items()}
    if isinstance(x, list):
        return [tidy(v, key) for v in x]
    if isinstance(x, float) and x == int(x):
        return int(x)
    return x


out = tidy(out)
OUT.write_text("# Generated by scripts/derive_mbm2.py. Do not edit by hand.\n"
               + yaml.safe_dump(out, sort_keys=False, allow_unicode=True), encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)}")
