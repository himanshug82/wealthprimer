---
layout: post
title: "Seasonality myths, part one: \"sell in May\" and the best month to invest"
description: "Month-by-month Nifty returns since 2007, with the spread that averages hide, a shuffle test, and what \"sell in May and go away\" would actually have done."
image: /assets/og/sell-in-may-and-month-of-year.png
date: 2026-10-18 09:00:00 +0530
series: technical-analysis
term: "Seasonality (calendar effects)"
---

{% assign t3 = site.data.ta3 %}
{% assign ds = t3.dataset %}
{% assign s = t3.seasonality %}
{% assign worst_mo = s.worst_avg_pct | abs %}
{% assign mo_worst = s.may_oct_worst.pct | abs %}

## The calendar as a trading signal

Every April or May someone repeats it: *"Sell in May and go away."* The idea,
borrowed from London's markets, is that stocks do badly from May to October
and well from November to April, so you should sit out the summer. Around it
sits a lot of other calendar talk about which months are "always" weak or
strong.

These claims are called **seasonality**, or calendar effects. They're
appealing because they're simple and need no chart at all. They're also
perfect material for the method from the
[backtesting post]({% post_url 2026-10-15-how-to-backtest-honestly %}): every
claim is a fixed-horizon claim (one month, six months), and the data is easy
to get.

The research behind the saying is real. Bouman and Jacobsen's 2002 paper in
the *American Economic Review* reported a "Halloween effect" — better
November–April returns — in most of the markets they studied. The question
here is narrower: what did the Nifty do?

## The formula

```
Monthly return (month m) = Close on the last trading day of m
                           / Close on the last trading day of m − 1   − 1

For each calendar month, across all years:
   average, median, share of years positive,
   standard deviation (how far a typical year strays from the average),
   worst and best year

Sell in May (year y):
   May–Oct return = Close end-Oct(y) / Close end-Apr(y) − 1
   Nov–Apr return = Close end-Apr(y) / Close end-Oct(y − 1) − 1
```

The data is the Nifty 50 price index, {{ ds.index_start | date: "%-d %B %Y" }} to
{{ ds.index_end | date: "%-d %B %Y" }}, from [Yahoo Finance]({{ ds.index_source_url }}).
That gives {{ s.months }} complete months, {{ s.first_month }} to {{ s.last_month }}
({{ s.last_month_note }}). It's a **price** index, so dividends are left out.
They add a little to every month and don't change which month looks best.

## Every month, with the spread

| Month | Years | Average | Median | Years positive | Std dev | Worst | Best |
|---|---:|---:|---:|---:|---:|---:|---:|
{% for m in s.by_month %}| {{ m.month_name }} | {{ m.n }} | {{ m.avg_pct }}% | {{ m.median_pct }}% | {{ m.share_positive_pct }}% | {{ m.stdev_pct }}% | {{ m.worst_pct }}% | {{ m.best_pct }}% |
{% endfor %}| **All months** | {{ s.months }} | {{ s.all_months.avg_pct }}% | {{ s.all_months.median_pct }}% | {{ s.all_months.share_positive_pct }}% | {{ s.all_months.stdev_pct }}% | | |

![Every monthly Nifty return by calendar month]({{ '/assets/charts/ta3-month-of-year.svg' | relative_url }})

Nifty 50 price index. Source: [Yahoo Finance]({{ ds.index_source_url }}).
Historical data, for illustration only.

Read the average column alone and you'd have a story: {{ s.best_avg_month }} is
the best month (+{{ s.best_avg_pct }}%), {{ s.worst_avg_month }} the worst
({% include inr.html n=s.worst_avg_pct %}%). Now read across to the standard deviation
column. A typical month strays from its own average by about 4 to 9
percentage points. The gap between the "best" and "worst" months,
{{ s.best_minus_worst_pp }} points, is smaller than that ordinary year-to-year
noise in most individual months.

The chart shows why. Each column of dots is one calendar month across roughly
19 years. The red averages sit inside clouds of dots that overlap almost
completely, and a single extreme year (the dot far below or above the rest)
can drag an average by a point or more.

## Is any of that more than chance?

Here's a simple way to find out. Take all {{ s.months }} monthly returns, shuffle
which calendar month each one belongs to, and recompute the twelve averages.
Do that {% include inr.html n=s.shuffle_runs %} times. If the calendar means
nothing, how often does the best-minus-worst spread come out at least
{{ s.best_minus_worst_pp }} points anyway?

**{{ s.shuffle_share_at_least_as_wide_pct }}% of the time.** Twelve random buckets of
this data usually produce a "best month" and a "worst month" at least that far
apart. The month-of-year averages look no more unusual than pure noise would.

One number does look odd. {{ s.fewest_positive_month }} was positive in only
{{ s.fewest_positive_count }} of {{ s.by_month[0].n }} years
({{ s.fewest_positive_pct }}%). In the same shuffle, the month with the fewest
up-years was that bad only {{ s.shuffle_share_worst_month_as_bad_pct }}% of the time.
But notice what just happened. We looked at the table, saw January, and *then*
chose a test for it. With twelve months and several ways to rank them
(average, median, share positive), something will always look unusual. That's
the parameter-picking problem from the backtesting post, in calendar form.
Call it a question worth re-asking on new data, not a finding.

## "Sell in May", year by year

Now the headline claim. For each year, compare the six months from the end of
April to the end of October with the six months before it.

| Year | Nov–Apr | May–Oct |
|---|---:|---:|
{% for h in s.halves %}| {{ h.year }} | {{ h.nov_apr_pct }}% | {{ h.may_oct_pct }}% |
{% endfor %}

*The first row is November 2007–April 2008 against May–October 2008. The
{{ s.incomplete_excluded }} window is left out, because the data ends
{{ ds.index_end | date: "%-d %B %Y" }}.*

Over these {{ s.halves_years }} years:

| | Nov–Apr | May–Oct |
|---|---:|---:|
| Average | {{ s.nov_apr_avg_pct }}% | **{{ s.may_oct_avg_pct }}%** |
| Median | {{ s.nov_apr_median_pct }}% | **{{ s.may_oct_median_pct }}%** |

On the Nifty, the "go away" months were the *better* half on average, and
May–October was positive in {{ s.may_oct_positive_years }} of {{ s.halves_years }} years.
It beat the November–April half in {{ s.may_oct_beat_nov_apr_years }} of them. Selling
every May would mostly have meant sitting out rising markets. And you'd also
have paid costs twice a year, and tax on any gains you realised.

That doesn't prove the opposite rule works either. The biggest single number
in the table, a May–October fall of {{ mo_worst }}% in {{ s.may_oct_worst.year }}, came
from the global financial crisis, not from the calendar. Eighteen six-month
windows are too few to say any half of the year is reliably better.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine rolling a dice twelve times and writing each roll under a month name.
One month will get the biggest number and one the smallest. That doesn't mean
the dice likes March.

Do it again next year and a different month wins. If you want to know whether
a month is *really* special, you check whether it keeps winning, year after
year, by more than the dice would give it anyway. For the Nifty, it mostly
doesn't.

</details>

## Doing it in Python

```python
import pandas as pd

s = pd.read_csv("nifty50-price-index.csv", parse_dates=["date"]
                ).set_index("date").nifty50_pri_close

m = s.resample("ME").last().pct_change().dropna() * 100
m = m["2007-10":]                       # first complete month
by = m.groupby(m.index.month)
print(pd.DataFrame({"avg": by.mean(), "median": by.median(),
                    "up%": by.apply(lambda x: (x > 0).mean() * 100),
                    "std": by.std(), "n": by.size()}).round(1))

# shuffle test: how often do random month labels give as wide a spread?
real = by.mean().max() - by.mean().min()
wider = sum((g := m.groupby(m.sample(frac=1, random_state=i).index.month).mean()
             ).max() - g.min() >= real for i in range(2000))
print(f"spread {real:.1f} pts; random labels as wide {wider / 2000:.0%} of the time")
```

The shuffle line works because `m.sample(frac=1)` reorders the values while
`.index.month` on the shuffled series still hands each value a random
month label. Your percentage will wobble a point or two from ours, because the
shuffles are random.

## Common mistakes

- **Reading averages without the spread.** An average of +3% with a standard
  deviation of 5% says "most Aprils were somewhere between −2% and +8%".
  That's not a forecast; it's a wide range.
- **Letting one year drive the story.** Monthly averages over 18–19 years
  shift noticeably when you add or drop a single crisis year. Check the
  median and the share of positive years too.
- **Finding a pattern, then testing the pattern you found.** The January
  result above is exactly this. A test chosen after looking at the data
  tends to pass more often than it should.
- **Ignoring the cost of acting on it.** A calendar rule trades on fixed
  dates regardless of anything else. Each switch costs brokerage, taxes and
  slippage, and those are certain, while the calendar edge is not.

**Takeaway:** On the Nifty since 2007, "sell in May" would mostly have meant missing rising markets: May–October was the better half on average. Month-by-month averages look like a pattern, but shuffling the month labels produces spreads that wide more often than not.
