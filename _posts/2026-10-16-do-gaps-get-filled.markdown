---
layout: post
title: "Gaps: the hole in the chart, and whether it really gets filled"
description: "\"Gaps get filled\" is one of the oldest lines in charting. We test it on two years of Britannia, against a base rate most gap tutorials never show you."
image: /assets/og/do-gaps-get-filled.png
date: 2026-10-16 09:00:00 +0530
series: technical-analysis
term: "Gap (gap up, gap down)"
---

{% assign t3 = site.data.ta3 %}
{% assign ds = t3.dataset %}
{% assign g = t3.gaps %}
{% assign gu = g.up %}
{% assign gd = g.down %}
{% assign bg = g.biggest %}
{% assign bg_size = bg.size_pct | abs %}
{% assign up1_extra = gu.windows.h1.fill_pct | minus: gu.windows.h1.base_pct %}
{% assign dn1_extra = gd.windows.h1.fill_pct | minus: gd.windows.h1.base_pct %}
{% assign up20_extra = gu.windows.h20.fill_pct | minus: gu.windows.h20.base_pct %}
{% assign dn20_extra = gd.windows.h20.fill_pct | minus: gd.windows.h20.base_pct %}
{% assign gu_o2c_fall = gu.open_to_close_avg_pct | abs %}

## A new kind of post

The [backtesting post]({% post_url 2026-10-15-how-to-backtest-honestly %})
ended with a set of rules: fix the horizon before you look, pay your costs,
and always compare against a base rate. This post, and the ones after it, take
popular chart ideas and put them through exactly that. Each one explains the
idea first, then tests it on data already on this blog, and reports what came
out — including the parts that don't flatter the idea.

We start with one of the oldest lines in charting: **gaps get filled.**

## What a gap is

Stocks don't trade overnight. News does. When something happens between one
day's close and the next day's open — results, a policy change, a global
sell-off — the first trade of the new day can happen well away from where the
last one did. On a [candlestick chart]({% post_url 2026-10-03-reading-a-candlestick-chart %})
that shows up as a visible hole between two bars. That hole is a **gap**.

- **Gap up**: today's open is above yesterday's *high*. Nothing traded in
  between.
- **Gap down**: today's open is below yesterday's *low*.

Some people count any open above the previous close as a gap. We use the
stricter, chart-visible version: an open beyond the previous high or low. We
chose it before running anything, because it's the gap you can actually see.

A gap is **filled** when price later trades back to where it was before the
gap — the previous day's close. The folklore says this nearly always happens.

## The formula

```
Gap up:    Open(today) > High(yesterday)
Gap down:  Open(today) < Low(yesterday)

Gap size   = Open(today) / Close(yesterday) − 1

Filled within N sessions (gap up):
           the lowest Low from today to N−1 sessions later ≤ Close(yesterday)
Filled within N sessions (gap down):
           the highest High over the same sessions ≥ Close(yesterday)
```

"Within 1 session" means filled on the gap day itself.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a ball bouncing along a pavement. Most of the time each bounce lands
close to the last one. Once in a while a gust of wind carries it a bit further
and there's a gap between bounces.

"Gaps get filled" is like saying the ball will bounce back over that spot
later. It usually does. But a ball that bounces around a lot passes over
nearly *every* nearby spot sooner or later. So the real question isn't "does it
come back?" It's "does it come back more often than it would to any spot that
far away?"

</details>

## The test, and the base rate nobody shows you

Here's the trap. Most gaps are small. And a stock that moves around a lot
revisits prices close to where it is all the time. So "the gap got filled"
could be true almost every time without meaning anything about gaps.

The honest comparison is a **base rate**: take *every* session, not just gap
days, and ask how often price came back the same distance from its open
within the same window. If a gap up opened 0.6% above yesterday's close, the
base rate asks: on an ordinary day, how often does price trade 0.6% below
where it opened, within the same number of sessions? If gaps fill more often
than that, there's something about gaps. If not, the folklore is just
describing how prices wander.

The data is Britannia (NSE: BRITANNIA), {{ ds.stock_as_of }}, from
[Yahoo Finance]({{ ds.stock_source_url }}), which the whole series has used. It
ends {{ ds.stock_end | date: "%-d %B %Y" }}, more than six months before this
post. The Nifty file on this blog only has closing prices, so it can't show
gaps at all. That's why this test runs on one stock rather than the index,
which is a real limitation.

In {{ g.sessions_scanned }} sessions there were **{{ gu.count }} gap ups** and
**{{ gd.count }} gap downs**. They were mostly small: the median gap up was
{{ gu.median_size_pct }}% and the median gap down {{ gd.median_size_pct }}%.

| | Gap ups filled | Base rate | Gap downs filled | Base rate |
|---|---:|---:|---:|---:|
| Same day | **{{ gu.windows.h1.fill_pct }}%** | {{ gu.windows.h1.base_pct }}% | **{{ gd.windows.h1.fill_pct }}%** | {{ gd.windows.h1.base_pct }}% |
| Within 5 sessions | **{{ gu.windows.h5.fill_pct }}%** | {{ gu.windows.h5.base_pct }}% | **{{ gd.windows.h5.fill_pct }}%** | {{ gd.windows.h5.base_pct }}% |
| Within 20 sessions | **{{ gu.windows.h20.fill_pct }}%** | {{ gu.windows.h20.base_pct }}% | **{{ gd.windows.h20.fill_pct }}%** | {{ gd.windows.h20.base_pct }}% |
| Events scored (5 / 20 sessions) | {{ gu.windows.h5.n }} / {{ gu.windows.h20.n }} | | {{ gd.windows.h5.n }} / {{ gd.windows.h20.n }} | |

*Gap downs too close to the end of the data to have a full window are dropped:
{{ gd.windows.h5.dropped_no_forward_data }} from the 5-session test and
{{ gd.windows.h20.dropped_no_forward_data }} from the 20-session test. No gap ups
needed dropping.*

![Gap fill rates against the base rate]({{ '/assets/charts/ta3-gaps.svg' | relative_url }})

Britannia (NSE: BRITANNIA), {{ ds.stock_as_of }}. Source:
[Yahoo Finance]({{ ds.stock_source_url }}). Historical data, for illustration only.

## What the numbers say

Two things are true at once.

**Most of "gaps get filled" is just the base rate.** Over 20 sessions an
ordinary open got revisited by the same distance {{ gu.windows.h20.base_pct }}% of
the time (matched to the gap ups) and {{ gd.windows.h20.base_pct }}% (matched to the
gap downs). Gaps filled {{ gu.windows.h20.fill_pct }}% and
{{ gd.windows.h20.fill_pct }}% of the time — {{ up20_extra }} and {{ dn20_extra }}
points more. When a tutorial says "over 90% of gaps fill", most of that 90% would
have happened to any price that close by.

**On the gap day itself, there was something extra.** Same-day fills beat the
base rate by {{ up1_extra }} points for gap ups and {{ dn1_extra }} for gap downs.
You can see the same thing another way. From open to close, the stock fell an
average of {{ gu_o2c_fall }}% on gap-up days (it closed above its open on only
{{ gu.open_to_close_share_up_pct }}% of them) and rose {{ gd.open_to_close_avg_pct }}% on
gap-down days. Across all sessions, the average open-to-close move was
{% include inr.html n=g.all_open_to_close_avg_pct %}%. In this sample, part of the
overnight jump tended to come back during the day.

Before reading that as an edge, count what it rests on:

- **{{ gu.count }} and {{ gd.count }} events, on one stock, over two years.** A few
  unusual days can move an average like that a long way.
- **The effect is small next to the costs.** A round trip at this blog's
  illustrative {{ ds.cost_per_side_pct }}% per side costs {{ g.round_trip_cost_pct }}%,
  before slippage at the open, which is exactly when prices move fastest.
- **Opening prices are noisy.** The open is one print at the start of the
  day. In our view, part of any "reversal from the open" is just that print
  being an outlier, which then looks like a move back.
- **The unfilled ones are where the damage is.** {{ gu.windows.h1.not_filled }}
  gap ups and {{ gd.windows.h1.not_filled }} gap downs didn't fill the same day, and
  {{ gu.windows.h20.not_filled }} gap ups were still unfilled 20 sessions later.
  Anyone betting on a fill has to survive those, and the tutorials never show
  them.

## The biggest gap in the data

The largest gap was on {{ bg.date | date: "%-d %B %Y" }}: a gap {{ bg.direction }} of
{{ bg_size }}%, from a previous close of ₹{% include inr.html n=bg.prev_close %} to an
open of ₹{% include inr.html n=bg.open %}. It filled the same day. That day is also a
good warning. It doesn't show that big gaps are safe to bet against. It shows
that on a violent day the open can be far from where the stock settles, in
either direction. One example proves nothing either way, which is why the table
above counts all of them.

## Doing it in Python

```python
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")

prev_close, prev_high = df.close.shift(), df.high.shift()
gap_up = df.open > prev_high                          # a visible hole in the chart

N = 5                                                  # fixed window, chosen first
low_ahead = df.low[::-1].rolling(N, min_periods=N).min()[::-1]  # min low, today..today+N-1
filled = (low_ahead <= prev_close)[gap_up & low_ahead.notna()]  # drop incomplete windows
print(f"gap ups: {gap_up.sum()}  filled within {N}: {filled.mean():.0%}")

# the base rate: for each gap's size, how often does ANY day's price come
# back that far below its own open within the same window?
ok = low_ahead.notna()
base = [(low_ahead <= df.open / (1 + d))[ok].mean()
        for d in (df.open / prev_close - 1)[gap_up]]
print(f"base rate, matched to each gap's size: {sum(base) / len(base):.0%}")
```

Change `N` to 1 or 20 for the other rows of the table.

## Common mistakes

- **Quoting the fill rate without the base rate.** "90% of gaps fill" sounds
  like an edge. Here, an ordinary open got revisited by the same distance in
  well over three-quarters of the 20-session windows. The claim has to beat
  that, not zero.
- **Leaving the window open-ended.** "Gaps *eventually* fill" can't lose,
  because a wandering price eventually revisits almost everything nearby. A
  claim with no time limit can't be tested. Fix the window first.
- **Confusing "filled" with "profitable".** A gap can fill after price has
  first run a long way against you. And every unfilled gap is a loss the fill
  statistic quietly leaves out.
- **Changing the definition after looking.** Open above yesterday's close,
  open above yesterday's high, gaps above 1% only, gaps on high volume only:
  each gives a different count. Try enough of them and one will look
  impressive by chance.

**Takeaway:** "Gaps get filled" is mostly true for a dull reason: most gaps are small, and prices revisit nearby levels all the time anyway. On two years of Britannia, gaps filled only somewhat more often than that base rate, mostly on the gap day itself. The effect was small next to costs and rested on a few dozen events, so treat it as a description, not an edge.
