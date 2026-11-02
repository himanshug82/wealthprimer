---
layout: post
title: "Breakouts and false breakouts: how often the break holds"
seo_title: "Breakouts and false breakouts, tested on the Nifty"
description: "A breakout is a close above a recent high. We tested 20, 50 and 100-day breakouts on 18 years of Nifty closes: how often they fell back, and what followed."
image: /assets/og/breakouts-and-false-breakouts.png
date: 2027-02-20 09:00:00 +0530
series: technical-analysis
term: "Breakout"
---

{% assign t4 = site.data.ta4 %}
{% assign ds = t4.dataset %}
{% assign bo = t4.breakouts %}
{% assign base = t4.base_rate %}

## What is a breakout, and what is a false one?

A **breakout** is a price closing above a level it has failed to close above recently, usually the highest close of the last several weeks or months. The idea comes straight from [support and resistance]({% post_url 2026-10-04-support-and-resistance %}): a ceiling the price keeps bumping into, and then a close above it. A **false breakout** (also called a fakeout or failed breakout) is one where the price drops back below that level soon after.

Chart-pattern articles describe breakouts as meaningful, especially when [volume]({% post_url 2026-10-07-volume %}) is high. This post defines the rule in advance, tests it on the Nifty at three lookbacks, and reports how often the break held. It is part of the [Technical Analysis]({{ '/series/technical-analysis/' | relative_url }}) series.

## The formula

```
Level(N)       = highest close of the previous N sessions
Breakout day   = close above Level(N), with no breakout counted in the
                 previous {{ bo.cooldown }} sessions (so a run of new highs counts once)
False breakout = within the next 5 sessions, some close falls back below
                 the Level(N) that was broken
Outcome        = Close(t + 63 sessions) / Close(t) − 1
```

The rule needs only closing prices, so it runs on the Nifty 50 price index, {{ ds.index_start | date: "%-d %B %Y" }} to {{ ds.index_end | date: "%-d %B %Y" }}, from [Yahoo Finance]({{ ds.index_source_url }}). Price index, so dividends are left out. The lookbacks 20, 50 and 100 were chosen in advance and all three are reported. The 5-session window for "false" and the {{ bo.cooldown }}-session gap between events are also conventions, not laws, so the second table shows other gaps.

## What happened after the breakouts

| Lookback | Breakouts | With a 63-session window | Fell back within 5 sessions | Average next-63-session change | Median | Share higher | Separate episodes |
|---|---:|---:|---:|---:|---:|---:|---:|
{% for b in bo.grid %}| {{ b.lookback }} sessions | {{ b.events_total }} | {{ b.n }} | {{ b.false_share_pct }}% | {{ b.avg_pct }}% | {{ b.median_pct }}% | {{ b.share_positive_pct }}% | {{ b.episodes }} |
{% endfor %}| **Every day (base rate)** | | {{ base.n }} | | {{ base.avg_pct }}% | {{ base.median_pct }}% | {{ base.share_positive_pct }}% | |

Breakouts with no full 63-session window before the data ends were dropped ({{ bo.grid[0].dropped_no_window }}, {{ bo.grid[1].dropped_no_window }} and {{ bo.grid[2].dropped_no_window }} at the three lookbacks). "Fell back" is counted only for breakouts with five sessions of data after them. "Separate episodes" counts breakouts at least 63 sessions apart: it is a better guide to how much independent evidence there is than the raw count.

The count depends on how a run of new highs is treated, which is easy to miss:

| Lookback | Sessions required between breakouts | Breakouts | Fell back within 5 sessions |
|---|---:|---:|---:|
{% for b in bo.grid %}| {{ b.lookback }} | none | {{ b.k0_events }} | {{ b.k0_false_share_pct }}% |
| {{ b.lookback }} | 5 | {{ b.k5_events }} | {{ b.k5_false_share_pct }}% |
| {{ b.lookback }} | 20 | {{ b.k20_events }} | {{ b.k20_false_share_pct }}% |
{% endfor %}
Two plain readings:

1. **About half of breakouts fell back below the broken level within a week, and that's roughly what noise gives.** The "false" share stayed near {{ bo.grid[0].false_share_pct }}%. The median breakout closed only about {{ bo.grid[0].median_gap_pct }}% above the level. Give any day the same gaps, and a close fell under that level within five sessions {{ bo.grid[0].false_base_pct }}% to {{ bo.grid[2].false_base_pct }}% of the time. So breakouts fell back no more often than ordinary days would, and a little less.
2. **What followed was close to the base rate.** The average change after a breakout was {{ bo.grid[0].avg_pct }}% to {{ bo.grid[1].avg_pct }}%, against {{ base.avg_pct }}% from any day, and the share ending higher was {{ bo.grid[2].share_positive_pct }}% to {{ bo.grid[1].share_positive_pct }}% against {{ base.share_positive_pct }}%. A rising index makes new highs often, so "a breakout" is a description of an index that was already rising, and the extra information in it is small.

## Why "false" is so common

On a rising market a close above the highest of the last 20 closes is not rare, and it usually clears the level by very little, so ordinary day-to-day moves can take it back under, as the base rate above shows. A close that dips just under the old high on day three counts as "false" under this rule, even if the price recovers a week later. Stricter definitions (a buffer of 1% above the level, or two closes above it) would give fewer signals and, we'd expect, a lower false share (we did not test them), and every such choice is another setting that can be tuned to a chart. We stuck with one definition.

## Common mistakes

- **Using volume as a magic filter without testing it.** "Only buy breakouts on high volume" is a rule you can test the same way. We haven't tested it here, because this index file has no volume.
- **Counting every new high as a new breakout.** In a rising stretch, new highs come days apart and are really one move. Counting each more than quadruples the events in the table above, which inflates the apparent evidence.
- **Ignoring the base rate in a rising market.** If most 63-session windows end higher anyway, a breakout that is followed by a gain has told you little.
- **Treating the broken level as a safe floor.** Close to half of the breakouts in this test closed back under it within five sessions.

## Doing it in Python

The data is [this CSV]({{ ds.index_csv_path | relative_url }}). Historical data, for illustration only.

```python
import pandas as pd

s = pd.read_csv("nifty50-price-index.csv", parse_dates=["date"]
                ).set_index("date").nifty50_pri_close
lookback = 20
level = s.shift().rolling(lookback).max()          # highest close of the previous N
days, last = [], -99
for i in (s > level).to_numpy().nonzero()[0]:      # keep one per 10 sessions
    if i - last > 10:
        days.append(i)
        last = i

fell = [(s.iloc[i + 1:i + 6] < level.iloc[i]).any()
        for i in days if i + 5 < len(s)]
fwd = s.shift(-63) / s - 1                         # NaN where the window is incomplete
print("breakouts:", len(days), "false share:", round(sum(fell) / len(fell), 2))
print(fwd.iloc[days].dropna().describe().round(3))
print("base rate:", round(fwd.dropna().mean(), 3))
```

**Takeaway:** A breakout is a close above a recent high, and on {{ ds.index_years }} years of Nifty closes close to half fell back below that level within five sessions, a little less often than any day with the same small gap would. What followed was close to the average from any day, so "it broke out" describes what the price just did.
