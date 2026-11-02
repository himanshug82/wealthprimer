---
layout: post
title: "Pivot points and round numbers: do prices respect them?"
seo_title: "Pivot points and round numbers, tested vs placebo"
description: "Pivot points turn yesterday's high, low and close into levels for today. We tested how often Britannia touched them, against random placebo levels."
image: /assets/og/pivot-points-and-round-numbers.png
date: 2027-02-28 09:00:00 +0530
series: technical-analysis
term: "Pivot points"
---

{% assign t4 = site.data.ta4 %}
{% assign ds = t4.dataset %}
{% assign pv = t4.pivots %}
{% assign ex = pv.example %}
{% assign rn = pv.round_numbers %}

## What are pivot points?

**Pivot points** are a set of price levels calculated from the previous session's high, low and close. Day traders mark them on the chart as possible support and resistance for the coming session: a central **pivot (P)**, resistance levels **R1** and **R2** above it, and support levels **S1** and **S2** below. The idea is a cousin of [support and resistance]({% post_url 2026-10-04-support-and-resistance %}), with the levels worked out by formula instead of drawn by eye.

Since the formula is mechanical, it can be tested mechanically. The question this post asks is narrow: **does price react at pivot levels any more than at levels that mean nothing?** It is part of the [Technical Analysis]({{ '/series/technical-analysis/' | relative_url }}) series.

## The formula

The classic version, from the previous day's high (H), low (L) and close (C):

```
P  = (H + L + C) / 3
R1 = 2 × P − L          S1 = 2 × P − H
R2 = P + (H − L)        S2 = P − (H − L)
```

## Worked example: one day of Britannia

Britannia Industries (NSE: BRITANNIA), from [Yahoo Finance]({{ ds.stock_source_url }}), {{ ds.stock_bars }} daily bars from {{ ds.stock_start | date: "%-d %B %Y" }} to {{ ds.stock_end | date: "%-d %B %Y" }}. Historical data, for illustration only. Take the session of {{ ex.date | date: "%-d %B %Y" }}: high ₹{{ ex.high }}, low ₹{{ ex.low }}, close ₹{{ ex.close }}.

| Level | Working | ₹ |
|---|---|---:|
| P | (high + low + close) / 3 | {{ ex.pivot }} |
| R1 | 2 × P − low | {{ ex.r1 }} |
| S1 | 2 × P − high | {{ ex.s1 }} |
| R2 | P + (high − low) | {{ ex.r2 }} |
| S2 | P − (high − low) | {{ ex.s2 }} |

These would be the day-traders' levels for the *next* session. Figures are computed from unrounded prices, so a hand calculation from the rounded values can be a paisa off.

## The test: touch and reject, against placebo levels

For each of the {{ pv.sessions }} sessions with a next day, we computed R1, R2, S1 and S2 and asked two questions about the next session:

- **Touched:** did the next day's high reach the resistance level (or its low reach the support level)?
- **Rejected:** having touched it, did the day then *close* on the near side of it (below a resistance level, above a support level)?

A level that matters should be rejected more often than a level that doesn't. To get a fair comparison we built a **placebo**: the same distances from the close, but reshuffled across days, so each day got another day's distance. That keeps the typical size of the distances and removes any link to that day's actual high and low. The table averages {{ pv.placebo_reps }} reshuffles.

| Level | Touched | Touch rate | Placebo touch rate | Rejected after touch | Placebo rejected |
|---|---:|---:|---:|---:|---:|
{% for p in pv.rows %}| {{ p.level }} | {{ p.touched }} | {{ p.touch_share_pct }}% | {{ p.placebo_touch_share_pct }}% | {{ p.reject_share_pct }}% | {{ p.placebo_reject_share_pct }}% |
{% endfor %}
The pivot levels and the placebo levels look the same. The touch rates are within a couple of percentage points of each other. The rejection rates are within about five points, with the support levels a little higher, and sit a little above half for both real and placebo levels: after touching a level, closing back on the near side is slightly more likely than not, most likely because a day's close lands between its high and low. On this stock over these two years, the formula's levels did nothing the random ones didn't.

That is one stock and {{ pv.sessions }} days. It does not show that pivots never work, and it doesn't show they do. It shows the measuring stick: a claim about levels needs a placebo.

## Round numbers

The same idea applies to round numbers such as Nifty 22,000. Traders say index levels cluster near them. A quick check on the Nifty 50 price index, {{ t4.dataset.index_start | date: "%-d %B %Y" }} to {{ t4.dataset.index_end | date: "%-d %B %Y" }}: the share of daily closes within ±{{ rn.tolerance_pct }}% of a multiple of {{ rn.step }} points was {{ rn.round_grid_share_pct }}%. The share within the same distance of a grid shifted by half a step (250, 750, 1,250…) was {{ rn.shifted_grid_share_pct }}%.

If round numbers attracted the index, the first number would be clearly bigger than the second. It isn't; it is slightly smaller. The Nifty's closes did not pile up around multiples of 500. Round numbers may still matter psychologically for individual orders, but in the daily closes there is no visible clustering.

## Common mistakes

- **Reading a touch as a reaction.** Even the random placebo levels at R1's distances were touched {{ pv.rows[0].placebo_touch_share_pct }}% of the time. A reaction means more than a touch.
- **Looking only at the times it worked.** Every chart has a famous pivot reversal. Without a count of the times price ignored the level, it tells you nothing.
- **Skipping the placebo.** Any level, drawn anywhere, will seem to work some of the time. The only fair question is whether the real levels beat arbitrary ones.
- **Mixing up pivot points with the pivot in a swing high or low.** Same word, different thing: here "pivot" is a formula output.

## Doing it in Python

```python
import numpy as np
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")
P = (df.high + df.low + df.close) / 3
R1, S1 = 2 * P - df.low, 2 * P - df.high

nh, nc = df.high.shift(-1), df.close.shift(-1)
ok = nh.notna()
touched = (nh >= R1) & ok
rejected = touched & (nc < R1)
print("R1 touch rate:", round(touched.sum() / ok.sum(), 3),
      "| rejected after touch:", round(rejected.sum() / touched.sum(), 3))

# placebo: reshuffle the distances from the close across days
rng = np.random.default_rng(1)
dist = (R1 - df.close)[ok].to_numpy()
lvl = df.close[ok].to_numpy() + rng.permutation(dist)
print("placebo touch rate:", round((nh[ok].to_numpy() >= lvl).mean(), 3))
```

**Takeaway:** Pivot points are levels computed from yesterday's high, low and close, and on two years of Britannia they were touched and rejected about as often as random placebo levels. A claim that price respects a level needs the same test against levels that mean nothing.
