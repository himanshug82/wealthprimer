---
layout: post
title: "Stochastic oscillator: RSI's cousin, tested the same way"
description: "Where the close sits in its recent range, on a 0–100 scale. The stochastic's formula, how closely it tracks RSI, and what 80/20 readings were followed by."
image: /assets/og/stochastic-oscillator.png
date: 2026-10-20 09:00:00 +0530
series: technical-analysis
term: "Stochastic oscillator"
---

{% assign t3 = site.data.ta3 %}
{% assign ds = t3.dataset %}
{% assign st = t3.stochastic %}
{% assign w = st.worked %}
{% assign bs = st.britannia.stochastic %}
{% assign br = st.britannia.rsi %}
{% assign ns = st.nifty_closes.stochastic %}
{% assign nr = st.nifty_closes.rsi %}
{% assign bs_ob_low = 100 | minus: bs.overbought.random_sets_at_least_as_high_pct %}
{% assign br_ob_low = 100 | minus: br.overbought.random_sets_at_least_as_high_pct %}
{% assign ns_ob_low = 100 | minus: ns.overbought.random_sets_at_least_as_high_pct %}
{% assign nr_ob_low = 100 | minus: nr.overbought.random_sets_at_least_as_high_pct %}

## A second oscillator, and why it looks familiar

The [RSI post]({% post_url 2026-10-08-rsi %}) introduced the **RSI (Relative
Strength Index)**: a 0–100 score for how one-sided the last fourteen sessions
were. The **stochastic oscillator**, usually credited to George Lane, asks a
closely related question in a different way:

> Where did today's close land inside the range of the last fourteen
> sessions?

A close at the very top of the recent range scores 100. A close at the very
bottom scores 0. Readings above 80 get called "overbought" and below 20
"oversold". Those are the same words RSI uses, with the same problem: they
describe where price has been, not where it's going.

## The formula

```
Fast %K = 100 × (Close − Lowest low of last 14 sessions)
              / (Highest high of last 14 sessions − Lowest low of last 14)

Slow %K = 3-session simple average of Fast %K       ← the line most charts show
%D      = 3-session simple average of Slow %K       ← the "signal" line

Conventional labels:  Slow %K > 80 "overbought",  < 20 "oversold"
```

This is the common "slow stochastic (14, 3, 3)" setting. Fast %K jumps around
too much for most people, so charting platforms usually show the smoothed
version by default. Check which one yours uses before comparing numbers.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Think of the last fourteen days as a staircase. The lowest step is the
cheapest price and the top step is the most expensive.

The stochastic tells you which step today's price is standing on. Top step: 100.
Bottom step: 0. Halfway: 50.

Standing on the top step doesn't mean you're about to fall down the stairs.
Sometimes a new, higher step gets built tomorrow and you climb onto that.

</details>

## A worked example

Britannia (NSE: BRITANNIA) on {{ w.date | date: "%-d %B %Y" }}, the last day in
this blog's dataset. Historical, for illustration only.

| Step | Value |
|---|---:|
| Close | ₹{% include inr.html n=w.close %} |
| Lowest low, last 14 sessions | ₹{% include inr.html n=w.lowest_low_14 %} |
| Highest high, last 14 sessions | ₹{% include inr.html n=w.highest_high_14 %} |
| Fast %K = 100 × (close − low) ÷ (high − low) | **{{ w.fast_k }}** |
| Fast %K on the two sessions before | {{ w.fast_k_prev1 }}, {{ w.fast_k_prev2 }} |
| Slow %K = average of the three | **{{ w.slow_k }}** |
| %D = average of the last three slow %K values | {{ w.slow_d }} |

The close was near the bottom of its two-week range, so fast %K was low. The
slow line, averaging three days, was still just above 20. Same stock, same
day, and whether it counts as "oversold" depends on which line you read.

## How close a cousin is it?

Both indicators are built from the same few weeks of prices, and they
mostly agree. Over the {{ st.britannia.corr_days }} scored sessions of Britannia,
the correlation between slow %K and RSI(14) was **{{ st.britannia.corr_with_rsi }}**.
On the Nifty it was **{{ st.nifty_closes.corr_with_rsi }}**. A correlation of 1 would
mean they always move together. At above 0.8, they're mostly two views of the
same thing.

The real difference is how often they hit their thresholds. Over the same
sessions, slow %K spent {{ st.britannia.pct_days_below_20 }}% of days below 20 and
{{ st.britannia.pct_days_above_80 }}% above 80. RSI spent
{{ st.britannia.pct_days_rsi_below_30 }}% below 30 and {{ st.britannia.pct_days_rsi_above_70 }}%
above 70. The stochastic is at an "extreme" far more often. A signal that fires
several times as often isn't several times as informative. Mostly, it's
noisier.

![Britannia with slow stochastic and RSI]({{ '/assets/charts/ta3-stochastic.svg' | relative_url }})

Britannia (NSE: BRITANNIA), {{ ds.stock_as_of }}. Source:
[Yahoo Finance]({{ ds.stock_source_url }}). Historical data, for illustration only.

## The test

The same test as the [backtesting post]({% post_url 2026-10-15-how-to-backtest-honestly %})
recommends, applied the same way to both indicators:

- **Event**: the first day slow %K crosses below 20 (or above 80), and for
  RSI the first day it crosses below 30 (or above 70). Staying below 20 for a
  week counts once, not five times.
- **Outcome**: the return over the next **{{ st.horizon_sessions }} sessions**,
  fixed. Events without 20 sessions of data after them are dropped.
- **Base rate**: the same 20-session return, on every scored day.
- **Shuffle check**: draw random sets of ordinary days, the same size as the
  events, and see how often they do at least as well as the folklore says the
  events should.

Both indicators are scored from the 100th session on, so RSI's warm-up period
doesn't distort anything and both share one base rate.

**Britannia**, {{ st.britannia.days_scored }} scored sessions:

| After… | Events | Average 20-session return | Median | Share positive |
|---|---:|---:|---:|---:|
| Stochastic crosses below 20 | {{ bs.oversold.n }} | {{ bs.oversold.avg_pct }}% | {{ bs.oversold.median_pct }}% | {{ bs.oversold.share_positive_pct }}% |
| Stochastic crosses above 80 | {{ bs.overbought.n }} | {{ bs.overbought.avg_pct }}% | {{ bs.overbought.median_pct }}% | {{ bs.overbought.share_positive_pct }}% |
| RSI crosses below 30 | {{ br.oversold.n }} | {{ br.oversold.avg_pct }}% | {{ br.oversold.median_pct }}% | {{ br.oversold.share_positive_pct }}% |
| RSI crosses above 70 | {{ br.overbought.n }} | {{ br.overbought.avg_pct }}% | {{ br.overbought.median_pct }}% | {{ br.overbought.share_positive_pct }}% |
| **Any day (base rate)** | {{ bs.base.n }} | {{ bs.base.avg_pct }}% | {{ bs.base.median_pct }}% | {{ bs.base.share_positive_pct }}% |

On Britannia, "oversold" readings were *not* followed by bounces: the
average after the stochastic's oversold readings was about the same as any
day, and after RSI's it was lower. "Overbought" readings were followed by
weaker returns, most of all for RSI, where {{ br.overbought.n }} events had an
average of {% include inr.html n=br.overbought.avg_pct %}%. In the shuffle,
{{ br_ob_low }}% of random sets of {{ br.overbought.n }} days did as badly. Suggestive,
on eight events. And on this same stock, the RSI post showed one overbought
reading followed by a rise and another followed by a fall.

Two years of one stock can't settle this, so here's more data.

**Nifty 50**, {{ ds.index_years }} years. The Nifty file has only closing prices,
so the "highest high" and "lowest low" here are the highest and lowest *close*
of the last 14 sessions. The mechanics are identical; the readings are a little
more extreme than a high/low version would give.

| After… | Events | Average 20-session return | Median | Share positive | Random sets doing at least as well for the folklore |
|---|---:|---:|---:|---:|---:|
| Stochastic crosses below 20 | {{ ns.oversold.n }} | **{{ ns.oversold.avg_pct }}%** | {{ ns.oversold.median_pct }}% | {{ ns.oversold.share_positive_pct }}% | {{ ns.oversold.random_sets_at_least_as_high_pct }}% |
| Stochastic crosses above 80 | {{ ns.overbought.n }} | {{ ns.overbought.avg_pct }}% | {{ ns.overbought.median_pct }}% | {{ ns.overbought.share_positive_pct }}% | {{ ns_ob_low }}% |
| RSI crosses below 30 | {{ nr.oversold.n }} | {{ nr.oversold.avg_pct }}% | {{ nr.oversold.median_pct }}% | {{ nr.oversold.share_positive_pct }}% | {{ nr.oversold.random_sets_at_least_as_high_pct }}% |
| RSI crosses above 70 | {{ nr.overbought.n }} | **{{ nr.overbought.avg_pct }}%** | {{ nr.overbought.median_pct }}% | {{ nr.overbought.share_positive_pct }}% | {{ nr_ob_low }}% |
| **Any day (base rate)** | {{ ns.base.n }} | {{ ns.base.avg_pct }}% | {{ ns.base.median_pct }}% | {{ ns.base.share_positive_pct }}% | |

*"Doing at least as well for the folklore" means a higher return for oversold
readings and a lower one for overbought. Events without 20 sessions after them
are dropped: {{ ns.oversold.dropped_no_forward_data }} for the stochastic,
{{ nr.oversold.dropped_no_forward_data }} for RSI, all of them oversold readings.*

On the index, the results partly contradict the Britannia table, which is
exactly why one chart shouldn't be trusted:

- **Stochastic "oversold"** was followed by a somewhat higher average than an
  ordinary day. Only {{ ns.oversold.random_sets_at_least_as_high_pct }}% of random sets
  did as well. That's the closest thing to support for the folklore in this
  post. The difference is about half a percentage point over a month, before
  costs, on events that often overlap.
- **Stochastic "overbought"** was followed by about the same as any day.
  No warning at all.
- **RSI "overbought"** on the Nifty was followed by *higher* than average
  returns. The "sell" reading, if anything, came before gains, as it does
  when a trend is strong.

## Doing it in Python

```python
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")

low14, high14 = df.low.rolling(14).min(), df.high.rolling(14).max()
fast_k = 100 * (df.close - low14) / (high14 - low14)
slow_k = fast_k.rolling(3).mean()
slow_d = slow_k.rolling(3).mean()

k = slow_k.iloc[100:]                              # same scored window as the post
fwd = (df.close.shift(-20) / df.close - 1).iloc[100:]
cross_dn = (k < 20) & (k.shift() >= 20)            # first day only
print("after crossing below 20:", fwd[cross_dn].dropna().describe().round(3))
print("any day:", fwd.dropna().describe().round(3))
```

## Common mistakes

- **Treating stochastic and RSI as two confirmations.** With a correlation
  above 0.8, one agreeing with the other isn't independent evidence. It's
  mostly the same measurement twice.
- **Counting every day below 20 as a separate signal.** A week spent below 20
  is one event. Counting it five times makes the sample look bigger and more
  certain than it is.
- **Mixing up fast and slow.** On the worked day above, fast %K said "deeply
  oversold" and slow %K said "just above 20". Know which line you're
  reading.
- **Trusting the result from one stock.** Britannia's overbought readings
  preceded weaker returns; the Nifty's preceded ordinary or stronger ones.
  Neither sample alone would have told you that.

**Takeaway:** The stochastic measures where today's close sits in the recent range, and it tracks RSI closely enough to be mostly the same signal. Its 80/20 readings fire far more often, and in these tests they didn't reliably come before the reversals their labels promise.
