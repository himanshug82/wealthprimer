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
Breakout day   = first close above Level(N) in a run (a streak of closes
                 above the level counts once, on its first day)
False breakout = within the next 5 sessions, some close falls back below
                 the Level(N) that was broken
Outcome        = Close(t + 63 sessions) / Close(t) − 1
```

The rule needs only closing prices, so it runs on the Nifty 50 price index, {{ ds.index_start | date: "%-d %B %Y" }} to {{ ds.index_end | date: "%-d %B %Y" }}, from [Yahoo Finance]({{ ds.index_source_url }}). Price index, so dividends are left out. The lookbacks 20, 50 and 100 were chosen in advance and all three are reported. The 5-session window for "false" is also a convention, not a law.

## What happened after the breakouts

| Lookback | Breakouts | With a 63-session window | Fell back within 5 sessions | Average next-63-session change | Median | Share higher | Separate episodes |
|---|---:|---:|---:|---:|---:|---:|---:|
{% for b in bo.grid %}| {{ b.lookback }} sessions | {{ b.events_total }} | {{ b.n }} | {{ b.false_share_pct }}% | {{ b.avg_pct }}% | {{ b.median_pct }}% | {{ b.share_positive_pct }}% | {{ b.episodes }} |
{% endfor %}| **Every day (base rate)** | | {{ base.n }} | | {{ base.avg_pct }}% | {{ base.median_pct }}% | {{ base.share_positive_pct }}% | |

Breakouts with no full 63-session window before the data ends were dropped ({{ bo.grid[0].dropped_no_window }}, {{ bo.grid[1].dropped_no_window }} and {{ bo.grid[2].dropped_no_window }} at the three lookbacks). "Fell back" is counted only for breakouts with five sessions of data after them. "Separate episodes" counts breakouts at least 63 sessions apart: it is a better guide to how much independent evidence there is than the raw count.

Two plain readings:

1. **About half of breakouts fell back below the broken level within a week.** Whatever the lookback, the "false" share stayed near {{ bo.grid[0].false_share_pct }}%. By the rule's own definition, breaking a level is easier than holding it.
2. **What followed was close to the base rate.** The average change after a breakout was {{ bo.grid[0].avg_pct }}% to {{ bo.grid[1].avg_pct }}%, against {{ base.avg_pct }}% from any day, and the share ending higher was {{ bo.grid[0].share_positive_pct }}% against {{ base.share_positive_pct }}%. A rising index makes new highs often, so "a breakout" is a description of an index that was already rising, and the extra information in it is small.

## Why "false" is so common

On a rising market a close above the highest of the last 20 closes is not rare, and the next few closes tend to jitter around that level. A close that dips just under the old high on day three counts as "false" under this rule, even if the price recovers a week later. Stricter definitions (a buffer of 1% above the level, or two closes above it) would give fewer signals and, we'd expect, a lower false share (we did not test them), and every such choice is another setting that can be tuned to a chart. We stuck with one definition.

## Common mistakes

- **Using volume as a magic filter without testing it.** "Only buy breakouts on high volume" is a rule you can test the same way. Until someone does, it is a story.
- **Counting every close above the level as a new breakout.** A streak of ten closes above the old high is one event, not ten. Counting each inflates the apparent evidence.
- **Ignoring the base rate in a rising market.** If most 63-session windows end higher anyway, a breakout that is followed by a gain has told you little.
- **Treating the broken level as a safe floor.** Roughly half of the breakouts in this test closed back under it within five sessions.

## Doing it in Python

```python
import pandas as pd

s = pd.read_csv("nifty50-price-index.csv", parse_dates=["date"]
                ).set_index("date").nifty50_pri_close
lookback = 20
level = s.shift().rolling(lookback).max()          # highest close of the previous N
above = s > level
breakout = above & ~above.shift(fill_value=False)  # first day of each streak

fwd = s.shift(-63) / s - 1                         # NaN where the window is incomplete
print("breakouts:", breakout.sum())
print(fwd[breakout].dropna().describe().round(3))
print("base rate:", round(fwd.dropna().mean(), 3))
```

**Takeaway:** A breakout is a close above a recent high, and on 18 years of Nifty closes roughly half of them closed back below that level within five sessions. What followed was close to the average from any day, so "it broke out" is a description of what the price just did.
