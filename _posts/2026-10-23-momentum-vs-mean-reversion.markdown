---
layout: post
title: "Momentum vs mean reversion: does the trend continue, or snap back?"
description: "Two opposite beliefs, both popular: winners keep winning, or what falls must bounce. We test 12-1 momentum and one-month reversal on 18 years of Nifty data."
image: /assets/og/momentum-vs-mean-reversion.png
date: 2026-10-23 09:00:00 +0530
series: technical-analysis
term: "Momentum and mean reversion"
---

{% assign t3 = site.data.ta3 %}
{% assign ds = t3.dataset %}
{% assign m = t3.momentum %}
{% assign ex = m.ex_2008_09 %}
{% assign pct_neg = 100 | minus: m.pct_months_positive_mom %}

## Two beliefs that can't both be right

Listen to market commentary for a week and you'll hear both of these, often
from the same person:

- **Momentum**: "The trend is your friend." What has been rising tends to keep
  rising.
- **Mean reversion**: "What goes up must come down." A big move tends to be
  followed by a move back.

They predict opposite things from the same chart. On any horizon, at most one
of them can describe the data, and quite possibly neither does. That makes
them a good last test for this run of posts, which have all used the method
from the [backtesting post]({% post_url 2026-10-15-how-to-backtest-honestly %}):
fixed horizons, base rates, and every result reported.

## The definitions

**12-1 momentum.** The return over the past twelve months, *skipping* the
most recent month. The skip is standard in the research literature, because
the latest month tends to behave differently (it's where short-term reversal
is usually found). A positive number means the market has been in an uptrend
over the past year.

**Short-term reversal.** Just last month's return. The mean-reversion idea is
that a bad month tends to be followed by a better one, and a great month by a
weaker one.

**Autocorrelation.** A single number for "does today's return tell you
anything about the next one?" It runs from −1 to +1. Positive means moves tend
to continue, negative means they tend to reverse, and zero means no
relationship at all.

## The formula

```
At each month-end t:

12-1 momentum(t)    = Close(end of month t − 1) / Close(end of month t − 12) − 1
Last month(t)       = Close(end of month t)     / Close(end of month t − 1)  − 1
Next month(t)       = Close(end of month t + 1) / Close(end of month t)      − 1

Test: average Next month, split by the sign of 12-1 momentum
      (and by last month's return), against the average over all months.

Lag-1 autocorrelation = correlation(return(t), return(t − 1))
Rough noise band      = ± 2 / √(number of returns)
```

The data is the Nifty 50 price index, {{ ds.index_start | date: "%-d %B %Y" }} to
{{ ds.index_end | date: "%-d %B %Y" }}, from [Yahoo Finance]({{ ds.index_source_url }}).
The first month-end with a full twelve months behind it is
{{ m.first_signal }}, and the last with a month after it is {{ m.last_signal }}:
**{{ m.months }} month-ends**. It's a price index, so dividends are left out.

## Momentum: the trend didn't help

| At month-end, 12-1 momentum was… | Months | Next month, average | Median | Share positive |
|---|---:|---:|---:|---:|
| Positive (past year up) | {{ m.mom_positive.n }} | {{ m.mom_positive.avg_next_pct }}% | {{ m.mom_positive.median_next_pct }}% | {{ m.mom_positive.share_next_positive_pct }}% |
| Negative (past year down) | {{ m.mom_negative.n }} | **{{ m.mom_negative.avg_next_pct }}%** | {{ m.mom_negative.median_next_pct }}% | {{ m.mom_negative.share_next_positive_pct }}% |
| **All months (base rate)** | {{ m.base.n }} | {{ m.base.avg_next_pct }}% | {{ m.base.median_next_pct }}% | {{ m.base.share_next_positive_pct }}% |

On this index, over this period, momentum pointed the *wrong way*. Months
after a down year did better on average than months after an up year. The
correlation between 12-1 momentum and the next month's return was
{% include inr.html n=m.corr_mom_next %}: slightly negative, and weak.

Is that just the 2009 rebound? We checked by dropping every signal from
September 2008 to December 2009 ({{ ex.dropped_months }} months). The pattern held:
{{ ex.mom_negative.avg_next_pct }}% after negative momentum ({{ ex.mom_negative.n }} months)
against {{ ex.mom_positive.avg_next_pct }}% after positive ({{ ex.mom_positive.n }}).

Before turning that into "buy after bad years", notice how thin it is. The
past year was down at only {{ pct_neg }}% of month-ends, {{ m.mom_negative.n }} months
in all, and they cluster in a few episodes, mostly 2008–09, 2011–12, 2015–16 and 2020.
That's a handful of independent market episodes, not {{ m.mom_negative.n }}
independent observations. And the spread after negative momentum was much
wider: a standard deviation of {{ m.mom_negative.stdev_next_pct }}% a month, against
{{ m.mom_positive.stdev_next_pct }}% after positive momentum.

![Nifty 12-1 momentum against the next month's return]({{ '/assets/charts/ta3-momentum.svg' | relative_url }})

Nifty 50 price index. Source: [Yahoo Finance]({{ ds.index_source_url }}).
Historical data, for illustration only.

The chart makes the "weak" part visible: a cloud with no clear slope. And the
labelled points are the months people remember:

| Month | 12-1 momentum at the previous month-end | Signal | What the month did |
|---|---:|---|---:|
{% for c in m.crash_months %}| {{ c.month }} | {{ c.momentum_pct }}% | {{ c.signal_at_prev_month_end }} | {{ c.month_return_pct }}% |
{% endfor %}

The signal was on the right side of the October 2008 crash. It was on the
wrong side of the May 2009 surge, the March 2020 crash and the April 2020
rebound. Trend rules usually get caught out when a trend turns sharply, and
these are exactly those months.

## Mean reversion: nothing to find

| Last month was… | Months | Next month, average | Median | Share positive |
|---|---:|---:|---:|---:|
| Up | {{ m.last_month_up.n }} | {{ m.last_month_up.avg_next_pct }}% | {{ m.last_month_up.median_next_pct }}% | {{ m.last_month_up.share_next_positive_pct }}% |
| Down | {{ m.last_month_down.n }} | {{ m.last_month_down.avg_next_pct }}% | {{ m.last_month_down.median_next_pct }}% | {{ m.last_month_down.share_next_positive_pct }}% |
| Worst fifth (≤ {% include inr.html n=m.last_month_worst_fifth.cutoff_pct %}%) | {{ m.last_month_worst_fifth.n }} | {{ m.last_month_worst_fifth.avg_next_pct }}% | {{ m.last_month_worst_fifth.median_next_pct }}% | {{ m.last_month_worst_fifth.share_next_positive_pct }}% |
| Best fifth (≥ {{ m.last_month_best_fifth.cutoff_pct }}%) | {{ m.last_month_best_fifth.n }} | {{ m.last_month_best_fifth.avg_next_pct }}% | {{ m.last_month_best_fifth.median_next_pct }}% | {{ m.last_month_best_fifth.share_next_positive_pct }}% |
| **All months (base rate)** | {{ m.base.n }} | {{ m.base.avg_next_pct }}% | {{ m.base.median_next_pct }}% | {{ m.base.share_next_positive_pct }}% |

Up months and down months were followed by almost identical averages. The
extreme fifths disagree with each other depending on whether you read the
average or the median, which is what small groups with a few big months in
them do. The correlation between one month and the next was
{{ m.corr_last1_next }}: effectively zero.

The autocorrelations say the same thing more compactly:

| Returns | Pairs | Lag-1 autocorrelation | Rough noise band |
|---|---:|---:|---:|
| Daily | {{ m.autocorr_daily.n }} | {{ m.autocorr_daily.autocorr }} | ±{{ m.autocorr_daily.noise_band }} |
| Weekly | {{ m.autocorr_weekly.n }} | {{ m.autocorr_weekly.autocorr }} | ±{{ m.autocorr_weekly.noise_band }} |
| Monthly | {{ m.autocorr_monthly.n }} | {{ m.autocorr_monthly.autocorr }} | ±{{ m.autocorr_monthly.noise_band }} |

Weekly and monthly are well inside the noise band. Daily sits just outside
it, slightly *positive* (a very faint tendency for one day's direction to
carry into the next). Even so, a correlation of {{ m.autocorr_daily.autocorr }} means
yesterday's return explains well under 1% of the variation in today's. That's
far too little to trade against a 0.1%-per-side cost.

## What this does and doesn't say about momentum

This test is narrow, and it's worth being exact about how narrow.

- **It's time-series momentum on one index.** The best-known momentum
  research is about something else: *cross-sectional* momentum, comparing
  stocks with each other and holding the recent winners against the recent
  losers (Jegadeesh and Titman, *Journal of Finance*, 1993). One index can't
  test that at all.
- **Time-series momentum has been studied across many markets at once.**
  Moskowitz, Ooi and Pedersen (*Journal of Financial Economics*, 2012) looked
  at dozens of futures markets together. A single index over 18 years is one
  small slice of that kind of evidence. It doesn't overturn it, and it
  doesn't confirm it.
- **So the honest conclusion is local.** On the Nifty, from 2008 to 2026, a
  simple trend signal on the index itself didn't point the right way, and
  last month's move said nothing about next month's.

## Doing it in Python

```python
import pandas as pd

s = pd.read_csv("nifty50-price-index.csv", parse_dates=["date"]
                ).set_index("date").nifty50_pri_close
me = s.resample("ME").last()

df = pd.DataFrame({
    "mom":  me.shift(1) / me.shift(12) - 1,        # 12-1: skip the latest month
    "last": me / me.shift(1) - 1,
    "next": me.shift(-1) / me - 1,                 # the outcome, one month ahead
}).dropna()                                        # drops incomplete windows

print(df.groupby(df.mom > 0).next.agg(["count", "mean", "median"]).round(4))
print(df.groupby(df["last"] > 0).next.agg(["count", "mean", "median"]).round(4))
for name, r in [("daily", s.pct_change()), ("monthly", me.pct_change())]:
    r = r.dropna()
    print(name, round(r.autocorr(), 3), "noise ±", round(2 / len(r) ** 0.5, 3))
```

## Common mistakes

- **Picking whichever belief fits the chart in front of you.** "The trend is
  your friend" after a rise, "what goes up must come down" after a fall. Two
  opposite rules used after the fact will always explain everything.
- **Reading an index result as a stock-picking result.** Momentum across
  stocks and momentum in one index are different questions with different
  evidence.
- **Counting months as if each were independent.** Negative-momentum months
  come in clumps around a few crises. {{ m.mom_negative.n }} months from a handful of episodes is much
  less evidence than it sounds.
- **Mistaking a tiny correlation for a usable one.** A daily autocorrelation
  of a few hundredths can be "statistically detectable" on 4,500 days and
  still be worth nothing after costs.

## Where this leaves us

Put the tests from this run side by side and a consistent picture emerges. Gaps filled about as often as
nearby prices get revisited anyway. Fibonacci levels caught no more pullbacks
than lines nobody draws. The calendar looked like a pattern until the month
labels were shuffled. Budget days were volatile but not directional.
Oscillators and OBV divergences often came before the opposite of what their
names say. Stops capped the worst loss but didn't improve the average. And the
trend on the index pointed the wrong way.

None of that proves these ideas never work anywhere. It does mean that, on
the data in front of us, each one needed a base rate to be understood, and
none of them survived one in the confident form it usually comes in. That's
exactly the argument of
[what technical analysis cannot do]({% post_url 2026-10-11-what-technical-analysis-cannot-do %}),
now with the tests to back it: treat charts as a description of what happened,
and be most sceptical of the idea that sounds most certain.

**Takeaway:** On 18 years of Nifty data, neither "the trend is your friend" nor "what goes up must come down" held up: months after a down year did better, and last month said nothing about next month. Momentum is a real research finding across many stocks and markets, but one index's chart isn't where you'll see it.
