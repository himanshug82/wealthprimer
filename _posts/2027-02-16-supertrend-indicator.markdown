---
layout: post
title: "Supertrend explained: an ATR line that flips with the trend"
seo_title: "Supertrend indicator explained: formula and settings"
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

Britannia Industries (NSE, the National Stock Exchange: BRITANNIA), daily bars from {{ st.dates.start | date: "%-d %B %Y" }} to {{ st.dates.end | date: "%-d %B %Y" }}, {{ st.bars_used }} bars after dropping the first {{ st.warmup_dropped }} while the ATR settles, from [Yahoo Finance]({{ ds.stock_source_url }}). It is one stock over two years, so this is a demonstration of the mechanics, not evidence about Supertrend in general. Historical data, for illustration only.

With a period of {{ ch.period }} and a multiplier of {{ ch.multiplier }}, the line flipped {{ ch.flips }} times. The first six flips:

| Date | Flipped to | Close (₹) | Level crossed (₹) | New line after the flip (₹) |
|---|---|---:|---:|---:|
{% for f in st.first_flips %}| {{ f.date }} | {{ f.to }} | {{ f.close }} | {{ f.level_crossed }} | {{ f.line }} |
{% endfor %}
{% assign f2 = st.example_down %}{% assign f3 = st.example_next %}On {{ f2.date | date: "%-d %B %Y" }} the close (₹{% include inr.html n=f2.close %}) fell below the line then in force (₹{% include inr.html n=f2.level_crossed %}), so the line jumped above the price, to ₹{% include inr.html n=f2.line %}. By the next flip, on {{ f3.date | date: "%-d %B %Y" }}, the close was ₹{% include inr.html n=f3.close %}. The flip to down came only after the close was already under the old line, and the flip back to up came only after the close was already above the upper one. That lag is the price of not flipping on every wobble.

## What do the settings change?

Every row below is the same stock over the same dates, {{ st.dates.start | date: "%-d %B %Y" }} to {{ st.dates.end | date: "%-d %B %Y" }}. These are price returns, so dividends are left out. The "long" columns follow a simple rule: be long the stock while the line is below the price (uptrend), hold cash otherwise (assumed to earn nothing), trade at the next session's close, and pay an illustrative {{ ds.cost_per_side_pct }}% a side. "Runs" leaves out the cut-off first and last runs.

| Period, multiplier | Flips | Median run (sessions) | Runs under 10 sessions | Share of time long | Return, long-only rule | Return, buy and hold | Deepest fall, rule | Deepest fall, buy and hold |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
{% for g in st.grid %}{% assign dr = g.strategy_max_drawdown_pct %}{% assign db = g.buy_hold_max_drawdown_pct %}| {{ g.period }}, {{ g.multiplier }} | {{ g.flips }} | {{ g.median_run_sessions }} | {{ g.runs_under_10_pct }}% | {{ g.share_time_long_pct }}% | {{ g.strategy_return_pct }}% | {{ g.buy_hold_return_pct }}% | {% include inr.html n=dr %}% | {% include inr.html n=db %}% |
{% endfor %}
Read the table down the columns:

- **A smaller multiplier flips more often.** At a multiplier of 1.5 the line flipped {{ st.grid[3].flips }} times against {{ ch.flips }} at 3, and {{ st.grid[3].runs_under_10_pct }}% of its runs lasted under 10 sessions. Those short runs are the whipsaws. Whipsaws didn't sink the result here, though: the two settings with the most flips had the two highest returns. That is one stock, so it doesn't show flipping more helps.
- **The returns jump around with the settings.** The long-only rule returned anywhere from {{ st.return_min_pct }}% to {{ st.return_max_pct }}% across five settings, against {% assign bh = ch.buy_hold_return_pct %}{% include inr.html n=bh %}% for buy and hold. With one stock and a stretch of only {{ st.bars_used }} bars, which setting "won" is a feature of these particular dates. Picking the best row after seeing it would be exactly the mistake the [backtesting post]({% post_url 2026-10-15-how-to-backtest-honestly %}) warns about.
- **The deepest fall was smaller for the rule in every row**, and the rule was in cash for roughly a third to a half of the time, so a smaller fall is close to mechanical here. It doesn't show the exit itself helped.

## Common mistakes

- **Treating the flip as a signal to act.** A flip is a rule's way of labelling what has already happened. Whether anything useful follows depends on the stock and the period, and one stock over two years can't tell you.
- **Tuning the settings to the chart.** Every setting looks good on some stretch. Fix the parameters first, then look.
- **Forgetting the whipsaws.** The tighter the line, the more flips, and each flip pays costs in this test and in real trading, whatever the table above happened to show on one stock.
- **Confusing it with a stop order.** Supertrend is a line on a chart. A stop is an order with a price, and a gap can fill it well beyond the line.

## Doing it in Python

The data is [this CSV]({{ ds.stock_csv_path | relative_url }}). 

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
print(flips.iloc[60:].sum(), "flips")      # skip the first 60 bars, as the post's table does
```

**Takeaway:** Supertrend is an ATR-based trailing line that flips when the close crosses it, so it labels a trend after the fact. Changing its two settings moved the flips from {{ st.flips_min }} to {{ st.flips_max }} and the return from {{ st.return_min_pct }}% to {{ st.return_max_pct }}% on the same stock, which is a good reason to distrust any single "best setting".
