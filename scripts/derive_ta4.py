#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Derive every figure quoted in the Technical Analysis Module 4 posts ("Trend
tools, tested": ADX, golden and death crosses, Supertrend, breakouts, pivot
points and round numbers, indicator confluence) and write them to _data/ta4.yml.

    python3 scripts/derive_ta4.py            # rewrites _data/ta4.yml

DATA (both committed, both end 30 March 2026)
  assets/data/nifty50-price-index.csv                  Yahoo Finance ^NSEI, closes only (price index)
  assets/data/britannia-ohlcv-2024-04-to-2026-03.csv   Yahoo Finance BRITANNIA.NS (OHLCV)
ADX, Supertrend and pivot points need highs and lows, which the Nifty file lacks,
so they are worked on Britannia's 495 bars (one stock, two years: a mechanics
demonstration, not evidence). Golden cross, breakouts and confluence use the
Nifty closes (18.5 years).

HOUSE RULES (same as scripts/derive_ta3.py): fixed horizons, never "to the later
peak"; an event whose forward window runs past the data is dropped and counted;
every conditional result sits beside its base rate and n; parameters fixed
before looking; where a threshold is arbitrary the whole grid is reported.

LAG: the first Module 4 post publishes 10 November 2026; cut-off 10 August 2026.

Needs pandas, numpy, pyyaml.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import yaml


class _NoAlias(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


ROOT = Path(__file__).resolve().parents[1]
PX_CSV = ROOT / "assets/data/britannia-ohlcv-2024-04-to-2026-03.csv"
NIFTY_CSV = ROOT / "assets/data/nifty50-price-index.csv"
OUT = ROOT / "_data/ta4.yml"
FIRST_POST = pd.Timestamp("2026-11-10")
COST = 0.001            # per side, illustrative all-in (same as ta2/ta3)
H63 = 63                # forward horizon, sessions
RNG = np.random.default_rng(20261110)


def r(x, nd=1):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return None
    v = round(float(x), nd)
    return int(v) if v == int(v) else v


def pct(x, nd=1):
    return r(x * 100, nd)


def d(ts):
    return pd.Timestamp(ts).strftime("%Y-%m-%d")


px = pd.read_csv(PX_CSV, parse_dates=["date"]).set_index("date").sort_index()
nifty = pd.read_csv(NIFTY_CSV, parse_dates=["date"]).set_index("date").sort_index()["nifty50_pri_close"]
assert px.index.is_unique and nifty.index.is_unique
assert px.index[-1] <= FIRST_POST - pd.DateOffset(months=3), "lag rule"
assert nifty.index[-1] <= FIRST_POST - pd.DateOffset(months=3), "lag rule"

out: dict = {"dataset": {
    "index_sessions": int(len(nifty)), "index_start": d(nifty.index[0]), "index_end": d(nifty.index[-1]),
    "index_years": r((nifty.index[-1] - nifty.index[0]).days / 365.25, 1),
    "index_csv_path": "/assets/data/nifty50-price-index.csv",
    "index_source_url": "https://finance.yahoo.com/quote/%5ENSEI/history/",
    "stock_bars": int(len(px)), "stock_start": d(px.index[0]), "stock_end": d(px.index[-1]),
    "stock_csv_path": "/assets/data/britannia-ohlcv-2024-04-to-2026-03.csv",
    "stock_source_url": "https://finance.yahoo.com/quote/BRITANNIA.NS/history/",
    "horizon_sessions": H63, "cost_per_side_pct": COST * 100,
}}

# ------------------------------------------------------------------ helpers
close = nifty.copy()
N = len(close)
fwd63 = close.shift(-H63) / close - 1            # NaN where the window runs past the data


def fwd_block(mask: pd.Series) -> dict:
    """Forward-63-session return for the days in mask; events without a full window are dropped and counted."""
    idx = mask[mask].index
    f = fwd63.loc[idx]
    kept = f.dropna()
    return {"events": int(len(idx)), "dropped_no_window": int(len(idx) - len(kept)), "n": int(len(kept)),
            "avg_pct": pct(kept.mean(), 1) if len(kept) else None,
            "median_pct": pct(kept.median(), 1) if len(kept) else None,
            "share_positive_pct": pct((kept > 0).mean(), 0) if len(kept) else None,
            "episodes": episodes(kept.index)}


def episodes(idx) -> int:
    """Events at least 63 sessions apart count as separate episodes."""
    pos = [close.index.get_loc(t) for t in idx]
    n, last = 0, -10**9
    for p in sorted(pos):
        if p - last >= H63:
            n += 1
            last = p
    return n


base_f = fwd63.dropna()
out["base_rate"] = {"n": int(len(base_f)), "avg_pct": pct(base_f.mean(), 1), "median_pct": pct(base_f.median(), 1),
                    "share_positive_pct": pct((base_f > 0).mean(), 0)}


def wilder(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(alpha=1 / n, adjust=False).mean()


# ================================================================ 1. ADX (Britannia)
H, L, C = px.high, px.low, px.close
up, dn = H.diff(), -L.diff()
plus_dm = np.where((up > dn) & (up > 0), up, 0.0)
minus_dm = np.where((dn > up) & (dn > 0), dn, 0.0)
prev = C.shift()
tr = pd.concat([H - L, (H - prev).abs(), (L - prev).abs()], axis=1).max(axis=1)
atr = wilder(tr, 14)
pdi = 100 * wilder(pd.Series(plus_dm, index=px.index), 14) / atr
mdi = 100 * wilder(pd.Series(minus_dm, index=px.index), 14) / atr
dx = 100 * (pdi - mdi).abs() / (pdi + mdi)
adx = wilder(dx, 14)
WARM = 60                                                   # ADX needs ~2x its period to settle
a = pd.DataFrame({"close": C, "pdi": pdi, "mdi": mdi, "adx": adx}).iloc[WARM:]
F20 = 20
a["fwd20"] = C.shift(-F20).reindex(a.index) / a["close"] - 1
a["abs_fwd20"] = a["fwd20"].abs()
a["dir_up"] = a["pdi"] > a["mdi"]


def adx_row(mask, label):
    s = a[mask].dropna(subset=["fwd20"])
    return {"band": label, "days": int(mask.sum()), "n": int(len(s)),
            "avg_abs_move_pct": pct(s["abs_fwd20"].mean(), 1),
            "share_up_pct": pct((s["fwd20"] > 0).mean(), 0)}


allm = a["fwd20"].notna()
adx_bands = [adx_row(a["adx"] < 20, "below 20"), adx_row((a["adx"] >= 20) & (a["adx"] < 25), "20 to 25"),
             adx_row(a["adx"] >= 25, "25 and above")]
bands_all = {"n": int(allm.sum()), "avg_abs_move_pct": pct(a.loc[allm, "abs_fwd20"].mean(), 1),
             "share_up_pct": pct((a.loc[allm, "fwd20"] > 0).mean(), 0)}
di_up = a[allm & a["dir_up"]]
di_dn = a[allm & ~a["dir_up"]]
# worked rows: lowest, middle, highest ADX day
pick = {"lowest": a["adx"].idxmin(), "highest": a["adx"].idxmax(),
        "middle": (a["adx"] - a["adx"].median()).abs().idxmin()}
worked = []
for k, t in pick.items():
    row = a.loc[t]
    worked.append({"which": k, "date": d(t), "close": r(row["close"], 1), "plus_di": r(row["pdi"], 1),
                   "minus_di": r(row["mdi"], 1), "adx": r(row["adx"], 1)})
out["adx"] = {"period": 14, "warmup_dropped": WARM, "horizon_sessions": F20, "bars_used": int(len(a)),
              "bands": adx_bands, "all": bands_all,
              "di_up": {"n": int(len(di_up)), "share_up_pct": pct((di_up["fwd20"] > 0).mean(), 0),
                        "avg_pct": pct(di_up["fwd20"].mean(), 1)},
              "di_down": {"n": int(len(di_dn)), "share_up_pct": pct((di_dn["fwd20"] > 0).mean(), 0),
                          "avg_pct": pct(di_dn["fwd20"].mean(), 1)},
              "share_days_adx_25_plus_pct": pct((a["adx"] >= 25).mean(), 0),
              "adx_min": r(a["adx"].min(), 1), "adx_max": r(a["adx"].max(), 1),
              "worked": worked,
              "windows_dropped_no_forward": int((~allm).sum())}

# ================================================================ 2. Golden and death cross (Nifty)
s50, s200 = close.rolling(50).mean(), close.rolling(200).mean()
above = (s50 > s200)
valid = s200.notna()
cross_up = valid & above & ~above.shift(fill_value=False) & valid.shift(fill_value=False)
cross_dn = valid & ~above & above.shift(fill_value=False) & valid.shift(fill_value=False)
golden, death = fwd_block(cross_up), fwd_block(cross_dn)
# whipsaw: opposite cross within 63 sessions
cu_pos = [close.index.get_loc(t) for t in cross_up[cross_up].index]
cd_pos = [close.index.get_loc(t) for t in cross_dn[cross_dn].index]
allc = sorted([(p, "g") for p in cu_pos] + [(p, "d") for p in cd_pos])
whip = sum(1 for (p1, _), (p2, _) in zip(allc, allc[1:]) if p2 - p1 <= H63)
# strategy: hold index while 50 > 200, cash otherwise, vs buy and hold, from first valid day
ret = close.pct_change().fillna(0)
pos = above.where(valid, False).astype(int).shift().fillna(0)      # trade next session
trades = int((pos.diff().abs() > 0).sum())
strat = (1 + ret * pos - (pos.diff().abs().fillna(0) * COST)).cumprod()
first = valid.idxmax()
bh = (1 + ret.loc[first:]).cumprod()
st = strat.loc[first:] / strat.loc[first]
yrs = (close.index[-1] - first).days / 365.25
dd = lambda s: float((s / s.cummax() - 1).min())
out["golden_cross"] = {
    "fast": 50, "slow": 200, "first_valid_day": d(first),
    "golden": golden, "death": death,
    "all_crosses": len(allc), "reversed_within_63": whip,
    "reversed_share_pct": pct(whip / max(len(allc) - 1, 1), 0),
    "strategy": {"years": r(yrs, 1), "trades": trades,
                 "strategy_cagr_pct": pct(st.iloc[-1] ** (1 / yrs) - 1, 1),
                 "buy_hold_cagr_pct": pct(bh.iloc[-1] ** (1 / yrs) - 1, 1),
                 "strategy_max_drawdown_pct": pct(dd(st), 0), "buy_hold_max_drawdown_pct": pct(dd(bh), 0),
                 "share_time_invested_pct": pct(pos.loc[first:].mean(), 0)},
    "first_golden": d(cross_up[cross_up].index[0]), "last_golden": d(cross_up[cross_up].index[-1]),
    "last_death": d(cross_dn[cross_dn].index[-1]),
}

# ================================================================ 3. Supertrend (Britannia)
def supertrend(df, period, mult):
    h, l, c = df.high.to_numpy(), df.low.to_numpy(), df.close.to_numpy()
    pc = np.r_[np.nan, c[:-1]]
    trr = np.maximum.reduce([h - l, np.abs(h - pc), np.abs(l - pc)])
    trr[0] = h[0] - l[0]
    at = wilder(pd.Series(trr), period).to_numpy()
    hl2 = (h + l) / 2
    ub, lb = hl2 + mult * at, hl2 - mult * at
    fub, flb = ub.copy(), lb.copy()
    st = np.full(len(c), np.nan)
    trend = np.ones(len(c), dtype=int)
    for i in range(1, len(c)):
        fub[i] = ub[i] if (ub[i] < fub[i - 1] or c[i - 1] > fub[i - 1]) else fub[i - 1]
        flb[i] = lb[i] if (lb[i] > flb[i - 1] or c[i - 1] < flb[i - 1]) else flb[i - 1]
        if trend[i - 1] == 1:
            trend[i] = -1 if c[i] < flb[i] else 1
        else:
            trend[i] = 1 if c[i] > fub[i] else -1
        st[i] = flb[i] if trend[i] == 1 else fub[i]
    return pd.Series(st, index=df.index), pd.Series(trend, index=df.index)


def st_stats(period, mult):
    line, tr_ = supertrend(px, period, mult)
    tr_ = tr_.iloc[period:]
    flips = tr_.ne(tr_.shift()) & tr_.shift().notna()
    fl = tr_[flips].index
    runs = []
    pos_ = [tr_.index.get_loc(t) for t in fl]
    bounds = [0] + pos_ + [len(tr_)]
    for b0, b1 in zip(bounds, bounds[1:]):
        runs.append(b1 - b0)
    inner = runs[1:-1] if len(runs) > 2 else runs     # exclude the truncated first and last runs
    rets = px.close.pct_change().loc[tr_.index].fillna(0)
    held = (tr_ == 1).astype(int).shift().fillna(0)
    cost = held.diff().abs().fillna(0) * COST
    eq = (1 + rets * held - cost).cumprod()
    bh_ = (1 + rets).cumprod()
    return {"period": period, "multiplier": mult, "flips": int(flips.sum()),
            "complete_runs": len(inner),
            "median_run_sessions": r(float(np.median(inner)), 0) if inner else None,
            "runs_under_10_pct": pct(np.mean([x < 10 for x in inner]), 0) if inner else None,
            "share_time_long_pct": pct(held.mean(), 0),
            "strategy_return_pct": pct(eq.iloc[-1] - 1, 0), "buy_hold_return_pct": pct(bh_.iloc[-1] - 1, 0),
            "strategy_max_drawdown_pct": pct(dd(eq), 0), "buy_hold_max_drawdown_pct": pct(dd(bh_), 0)}


grid = [st_stats(p, m) for p, m in [(7, 2), (10, 3), (14, 3), (10, 1.5), (20, 3)]]
line10, tr10 = supertrend(px, 10, 3)
last_flip_rows = []
t10 = tr10.iloc[10:]
flipdays = t10[t10.ne(t10.shift()) & t10.shift().notna()].index
for t in flipdays[:6]:
    last_flip_rows.append({"date": d(t), "to": "up" if t10.loc[t] == 1 else "down", "close": r(px.close.loc[t], 1),
                           "line": r(line10.loc[t], 1)})
out["supertrend"] = {"chosen": grid[1], "grid": grid, "first_flips": last_flip_rows,
                     "bars_used": int(len(t10)), "dates": {"start": d(t10.index[0]), "end": d(t10.index[-1])},
                     "stock_return_pct": pct(px.close.iloc[-1] / px.close.iloc[0] - 1, 0)}

# ================================================================ 4. Breakouts (Nifty closes)
bo = {}
for lb in (20, 50, 100):
    hi = close.shift().rolling(lb).max()
    ev = (close > hi)
    # count only the first close above in a streak (a new breakout), not every day above
    new = ev & ~ev.shift(fill_value=False)
    fwd = fwd_block(new)
    # false breakout: within 5 sessions the close falls back below the old high (the level broken)
    lvl = hi
    pos_list = [close.index.get_loc(t) for t in new[new].index]
    fb = 0
    for p in pos_list:
        if p + 5 < N and (close.iloc[p + 1:p + 6] < lvl.iloc[p]).any():
            fb += 1
    full = [p for p in pos_list if p + 5 < N]
    out_ = {"lookback": lb, **fwd, "events_total": len(pos_list), "false_within_5": fb,
            "false_share_pct": pct(fb / len(full), 0) if full else None}
    bo[lb] = out_
out["breakouts"] = {"definition": "first close above the highest close of the previous N sessions", "grid": list(bo.values())}

# ================================================================ 5. Pivot points and round numbers
Hh, Ll, Cc = px.high, px.low, px.close
P = (Hh + Ll + Cc) / 3
R1, S1 = 2 * P - Ll, 2 * P - Hh
R2, S2 = P + (Hh - Ll), P - (Hh - Ll)
nxt_h, nxt_l, nxt_c = Hh.shift(-1), Ll.shift(-1), Cc.shift(-1)
ok = nxt_h.notna()


def touch_reject(level, side):
    """side 'up': next-day high >= level; rejected if that day then closes below level."""
    if side == "up":
        t = (nxt_h >= level) & ok
        rej = t & (nxt_c < level)
    else:
        t = (nxt_l <= level) & ok
        rej = t & (nxt_c > level)
    return int(t.sum()), int(rej.sum())


def pv_row(name, level, side):
    t, rj = touch_reject(level, side)
    return {"level": name, "touched": t, "rejected": rj, "touch_share_pct": pct(t / ok.sum(), 0),
            "reject_share_pct": pct(rj / t, 0) if t else None}


# placebo: same distances from the close, but each day's distance is taken from a different, randomly chosen day
def placebo(dist_series, side, reps=200):
    dist = dist_series[ok].to_numpy()
    c = Cc[ok].to_numpy()
    nh, nl, nc = nxt_h[ok].to_numpy(), nxt_l[ok].to_numpy(), nxt_c[ok].to_numpy()
    ts, rs = [], []
    for _ in range(reps):
        dd_ = RNG.permutation(dist)
        lvl = c + dd_ if side == "up" else c - dd_
        t = (nh >= lvl) if side == "up" else (nl <= lvl)
        rj = t & ((nc < lvl) if side == "up" else (nc > lvl))
        ts.append(t.mean())
        rs.append(rj.sum() / max(t.sum(), 1))
    return {"touch_share_pct": pct(np.mean(ts), 0), "reject_share_pct": pct(np.mean(rs), 0)}


pivots = [pv_row("R1", R1, "up"), pv_row("R2", R2, "up"), pv_row("S1", S1, "down"), pv_row("S2", S2, "down")]
plc = {"R1": placebo(R1 - Cc, "up"), "R2": placebo(R2 - Cc, "up"), "S1": placebo(Cc - S1, "down"), "S2": placebo(Cc - S2, "down")}
for row in pivots:
    row["placebo_touch_share_pct"] = plc[row["level"]]["touch_share_pct"]
    row["placebo_reject_share_pct"] = plc[row["level"]]["reject_share_pct"]
ex_t = px.index[len(px) // 2]
ex = {"date": d(ex_t), "high": r(Hh.loc[ex_t], 1), "low": r(Ll.loc[ex_t], 1), "close": r(Cc.loc[ex_t], 1),
      "pivot": r(P.loc[ex_t], 1), "r1": r(R1.loc[ex_t], 1), "s1": r(S1.loc[ex_t], 1),
      "r2": r(R2.loc[ex_t], 1), "s2": r(S2.loc[ex_t], 1)}

# round numbers on the Nifty: share of closes within +/-0.25% of a multiple of 500, against a grid shifted by 250
def near_grid(step, offset, tol=0.0025):
    k = np.round((close.to_numpy() - offset) / step)
    lvl = k * step + offset
    return float((np.abs(close.to_numpy() / lvl - 1) <= tol).mean())


rn = {"step": 500, "tolerance_pct": 0.25,
      "round_grid_share_pct": pct(near_grid(500, 0), 1), "shifted_grid_share_pct": pct(near_grid(500, 250), 1)}
out["pivots"] = {"sessions": int(ok.sum()), "rows": pivots, "example": ex, "round_numbers": rn,
                 "placebo_reps": 200}

# ================================================================ 6. Confluence (Nifty closes)
delta = close.diff()
rsi = 100 - 100 / (1 + wilder(delta.clip(lower=0), 14) / wilder((-delta.clip(upper=0)), 14))
ema12, ema26 = close.ewm(span=12, adjust=False).mean(), close.ewm(span=26, adjust=False).mean()
macd = ema12 - ema26
macd_hist = macd - macd.ewm(span=9, adjust=False).mean()
ma20, sd20 = close.rolling(20).mean(), close.rolling(20).std()
pb = (close - (ma20 - 2 * sd20)) / (4 * sd20)           # %B: 0 = lower band, 1 = upper band
roc20 = close.pct_change(20)
W = 60
frame = pd.DataFrame({"rsi": rsi, "macd_hist": macd_hist, "pctb": pb, "roc20": roc20}).iloc[W:]
corr = frame.corr()
# oversold-type conditions (parameters fixed in advance)
c1 = frame["rsi"] < 30
c2 = frame["pctb"] < 0
c3 = frame["roc20"] < frame["roc20"].quantile(0.10)       # worst tenth of 20-session returns
cnt = c1.astype(int) + c2.astype(int) + c3.astype(int)
cf = {}
for name, m in [("rsi_below_30", c1), ("below_lower_band", c2), ("worst_tenth_20d", c3),
                ("at_least_2", cnt >= 2), ("all_3", cnt == 3)]:
    full = pd.Series(False, index=close.index)
    full.loc[m.index] = m
    cf[name] = fwd_block(full)
overlap = {"rsi_days": int(c1.sum()), "rsi_and_band_pct": pct((c1 & c2).sum() / max(c1.sum(), 1), 0),
           "band_days": int(c2.sum()), "band_and_rsi_pct": pct((c1 & c2).sum() / max(c2.sum(), 1), 0)}
# MACD and RSI correlation matters: report the pairwise correlations
out["confluence"] = {
    "warmup_dropped": W, "days": int(len(frame)),
    "corr_rsi_macdhist": r(corr.loc["rsi", "macd_hist"], 2), "corr_rsi_pctb": r(corr.loc["rsi", "pctb"], 2),
    "corr_pctb_macdhist": r(corr.loc["pctb", "macd_hist"], 2), "corr_rsi_roc20": r(corr.loc["rsi", "roc20"], 2),
    "corr_pctb_roc20": r(corr.loc["pctb", "roc20"], 2),
    "worst_tenth_cutoff_pct": pct(frame["roc20"].quantile(0.10), 1),
    "overlap": overlap, "tests": cf,
    "share_days_two_or_more_pct": pct((cnt >= 2).mean(), 1),
}

header = """# Technical Analysis — Module 4 ("Trend tools, tested"): every figure quoted in the
# ADX, golden cross, Supertrend, breakouts, pivot points and confluence posts.
#
# GENERATED by scripts/derive_ta4.py from the committed Nifty and Britannia CSVs
# (both end 2026-03-30; first Module 4 post 2026-11-10) — do not edit by hand.
# Every conditional figure sits beside its base rate and n; horizons are fixed;
# events without a full forward window are dropped and counted.

"""
OUT.write_text(header + yaml.dump(out, Dumper=_NoAlias, sort_keys=False, allow_unicode=True, default_flow_style=False), encoding="utf-8")
print("wrote", OUT.relative_to(ROOT))
