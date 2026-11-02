---
layout: post
title: "Supertrend explained: an ATR line that flips with the trend"
seo_title: "Supertrend indicator explained: formula and test"
description: "Supertrend is a trailing line set a multiple of ATR from the price. How it is built, and how its settings changed the result on two years of Britannia."
image: /assets/og/supertrend-indicator.png
date: 2027-02-16 09:00:00 +0530
series: technical-analysis
term: "Supertrend"
---

{% assign t4 = site.data.ta4 %}
{% assign ds = t4.dataset %}
{% assign st = t4.supertrend %}
{% assign ch = st.chosen %}

## What is Supertrend?

**Supertrend** is a line plotted on the price chart that sits below the price while the trend is up and above it while the trend is down. It is built from the ATR ([average true range]({% post_url 2026-10-12-bollinger-bands-and-atr %})), so it keeps a distance from the price that widens when the stock is jumpy and narrows when it is calm. When the price closes on the wrong side of the line, the line flips to the other side and the "trend" is relabelled. It is widely available on charting platforms because it gives a clear yes/no picture. This post shows how it is built, and what the settings do to that picture.

It is a close relative of the stop-loss ideas in the [stop-loss placement post]({% post_url 2026-10-22-stop-loss-placement %}): the lower line in an uptrend is a trailing stop that only ever moves up. It is part of the [Technical Analysis]({{ '/series/technical-analysis/' | relative_url }}) series.

## The formula

```
Mid        = (High + Low) / 2
Upper band = Mid + multiplier × ATR(period)
Lower band = Mid − multiplier × ATR(period)

In an uptrend:   the line is the Lower band, and it never moves down
                 (it only rises, or stays) while the close stays above it.
In a downtrend:  the line is the Upper band, and it never moves up.

Flip to down:  the close finishes below the uptrend line.
Flip to up:    the close finishes above the downtrend line.
```

Two settings: the ATR **period** and the **multiplier**. A period of 10 and a multiplier of 3 is a frequently used pair, and we use it as the starting point here. These are conventions, not recommended settings; the test below shows why they matter.

## Worked example: Britannia, two years

Britannia Industries (NSE: BRITANNIA), daily bars from {{ st.dates.start | date: "%-d %B %Y" }} to {{ st.dates.end | date: "%-d %B %Y" }}, {{ st.bars_used }} bars once the first ATR is available, from [Yahoo Finance]({{ ds.stock_source_url }}). It is one stock over two years, so this is a demonstration of the mechanics, not evidence about Supertrend in general. Historical data, for illustration only.

With a period of {{ ch.period }} and a multiplier of {{ ch.multiplier }}, the line flipped {{ ch.flips }} times. The first six flips:

| Date | Flipped to | Close (₹) | Line (₹) |
|---|---|---:|---:|
{% for f in st.first_flips %}| {{ f.date }} | {{ f.to }} | {{ f.close }} | {{ f.line }} |
{% endfor %}
The "line" column is the level the close crossed. {% assign f2 = st.first_flips[2] %}{% assign f3 = st.first_flips[3] %}On {{ f2.date }} the close (₹{{ f2.close }}) fell below the line (₹{{ f2.line }}) and the line flipped to down. By the next flip, on {{ f3.date }}, the close was ₹{{ f3.close }}. The flip to down came only after the close was already under the line, and the flip back to up came only after the close was already above it. That lag is the price of not flipping on every wobble.

## What do the settings change?

Every row below is the same stock and the same two years. The "long" columns follow a simple rule: be long the stock while the line is below the price (uptrend), hold cash otherwise (assumed to earn nothing), trade at the next session's close, and pay 0.1% a side.

| Period, multiplier | Flips | Median run (sessions) | Runs under 10 sessions | Share of time long | Return, long-only rule | Return, buy and hold | Deepest fall, rule | Deepest fall, buy and hold |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
{% for g in st.grid %}{% assign dr = g.strategy_max_drawdown_pct %}{% assign db = g.buy_hold_max_drawdown_pct %}| {{ g.period }}, {{ g.multiplier }} | {{ g.flips }} | {{ g.median_run_sessions }} | {{ g.runs_under_10_pct }}% | {{ g.share_time_long_pct }}% | {{ g.strategy_return_pct }}% | {{ g.buy_hold_return_pct }}% | {% include inr.html n=dr %}% | {% include inr.html n=db %}% |
{% endfor %}
Read the table down the columns:

- **A smaller multiplier flips more often.** At a multiplier of 1.5 the line flipped {{ st.grid[3].flips }} times against {{ ch.flips }} at 3, and {{ st.grid[3].runs_under_10_pct }}% of its runs lasted under 10 sessions. Those are the whipsaws.
- **The returns jump around with the settings.** The long-only rule returned anywhere from {{ st.grid[4].strategy_return_pct }}% to {{ st.grid[3].strategy_return_pct }}% across five settings, against {{ ch.buy_hold_return_pct }}% for buy and hold. With one stock and a stretch of only {{ st.bars_used }} bars, which setting "won" is a feature of this particular two years. Picking the best row after seeing it would be exactly the mistake the [backtesting post]({% post_url 2026-10-15-how-to-backtest-honestly %}) warns about.
- **The deepest fall was smaller for the rule in every row**, because a rule that sits in cash when the line is above the price avoids some of the fall. That is the one consistent pattern, and it is a property of any trend-following exit, not evidence that this one is better.

## Common mistakes

- **Treating the flip as a signal to act.** A flip is a rule's way of labelling what has already happened. Whether anything useful follows depends on the stock and the period, and one stock over two years can't tell you.
- **Tuning the settings to the chart.** Every setting looks good on some stretch. Fix the parameters first, then look.
- **Forgetting the whipsaws.** The tighter the line, the more flips, and each flip in a sideways market costs money in this test and in real trading.
- **Confusing it with a stop order.** Supertrend is a line on a chart. A stop is an order with a price, and a gap can fill it well beyond the line.

## Doing it in Python

```python
import numpy as np
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")
period, mult = 10, 3
prev = df.close.shift()
tr = pd.concat([df.high - df.low, (df.high - prev).abs(),
                (df.low - prev).abs()], axis=1).max(axis=1)
atr = tr.ewm(alpha=1 / period, adjust=False).mean()
mid = (df.high + df.low) / 2
ub, lb = (mid + mult * atr).to_numpy(), (mid - mult * atr).to_numpy()
c = df.close.to_numpy()

up = np.ones(len(c), dtype=bool)
fub, flb = ub.copy(), lb.copy()
for i in range(1, len(c)):
    fub[i] = ub[i] if ub[i] < fub[i - 1] or c[i - 1] > fub[i - 1] else fub[i - 1]
    flb[i] = lb[i] if lb[i] > flb[i - 1] or c[i - 1] < flb[i - 1] else flb[i - 1]
    up[i] = (c[i] >= flb[i]) if up[i - 1] else (c[i] > fub[i])

df["supertrend"] = np.where(up, flb, fub)
flips = pd.Series(up).ne(pd.Series(up).shift())
print(flips.iloc[period:].sum(), "flips")      # skip the first bars, as the post's table does
```

**Takeaway:** Supertrend is an ATR-based trailing line that flips when the close crosses it, so it labels a trend after the fact. Changing its two settings changed the number of flips and the result several-fold on the same stock, which is a good reason to distrust any single "best setting".
