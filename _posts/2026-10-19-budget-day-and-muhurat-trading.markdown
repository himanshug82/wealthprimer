---
layout: post
title: "Seasonality myths, part two: Budget day and Muhurat trading"
description: "Two Indian market rituals, checked against 18 years of Nifty data with verified dates: is Budget day unusually volatile, and is the Diwali session a good omen?"
image: /assets/og/budget-day-and-muhurat-trading.png
date: 2026-10-19 09:00:00 +0530
series: technical-analysis
term: "Muhurat trading"
---

{% assign t3 = site.data.ta3 %}
{% assign ds = t3.dataset %}
{% assign ev = t3.events %}
{% assign all = ev.all_days %}
{% assign b = ev.budget %}
{% assign mu = ev.muhurat %}
{% assign bfall = b.biggest_fall.move_pct | abs %}

## Two dates the market talks about every year

The [first seasonality post]({% post_url 2026-10-18-sell-in-may-and-month-of-year %})
tested calendar months. This one tests two dates that are specifically Indian
and come with a lot of commentary:

- **Union Budget day.** Every year TV channels run "Budget-day market"
  specials, and there's a popular belief that the market usually falls on
  the day, or at least moves a lot.
- **Muhurat trading.** On Diwali evening, the exchanges hold a special
  session of about an hour, traditionally seen as an auspicious start to the
  new year. Some investors buy a token amount for luck, and a common line is that the market
  "usually closes green" in that session.

Both are claims about a specific date, so they need correct dates. That turns
out to be half the work.

## Getting the dates right

A test on the wrong dates is worse than no test. So every date here comes
from a primary source, checked in September 2026:

- **Budget dates** come from the date printed on each Budget speech on
  [indiabudget.gov.in](https://www.indiabudget.gov.in/) (for 2008, the
  Press Information Bureau's release of that day). That's
  {{ b.listed }} Budgets from {{ b.first_year }} to {{ b.last_year }}, including the
  interim Budgets in election years and the full Budgets that followed them.
- **Weekend Budgets** were presented on a Saturday or Sunday {{ b.weekend_count }}
  times. For each, NSE issued a circular announcing a live trading session
  that day: NSE/CMTR/28939 (for 28 February 2015), NSE/CMTR/43290 (1 February
  2020), NSE/CMTR/65729 (1 February 2025) and
  [NSE/CMTR/72349](https://nsearchives.nseindia.com/content/circulars/CMTR72349.pdf)
  (1 February 2026).
- **Muhurat sessions** come from NSE's equity-segment circulars, one per year,
  {{ mu.listed }} sessions from 2008 to 2025. They're listed in full further down.

Then we check what the price file actually contains. The Nifty data here is
the Nifty 50 price index from [Yahoo Finance]({{ ds.index_source_url }}),
{{ ds.index_start | date: "%-d %B %Y" }} to {{ ds.index_end | date: "%-d %B %Y" }}. It
has no row for {{ b.not_in_file_count }} of the Budget days, and none for
{{ mu.not_in_file_count }} of the {{ mu.listed }} Muhurat sessions. Many of these are
weekend sessions the feed skipped. Every missing date is listed below rather
than quietly dropped.

## The formula

```
Event-day move = Nifty close on the event day / previous close − 1

Compared with every trading day in the file:
   size:       average |move| on event days  vs  average |move| on all days
   direction:  rises and falls on event days  vs  share of all days that rose

Shuffle test: draw the same number of random trading days 10,000 times.
   How often is a random set at least as extreme as the event days?
```

## Budget day: bigger moves, not a reliable direction

Across **{% include inr.html n=all.n %} trading days**, the Nifty's average move (up or down) was
{{ all.avg_abs_pct }}%, and it rose on {{ all.share_positive_pct }}% of days. The
{{ b.n }} Budget days with a row in the file:

| | Budget days | All days |
|---|---:|---:|
| Days | {{ b.n }} | {{ all.n }} |
| Average size of the move, up or down | **{{ b.avg_abs_pct }}%** | {{ all.avg_abs_pct }}% |
| Median size of the move | {{ b.median_abs_pct }}% | {{ all.median_abs_pct }}% |
| Rose | {{ b.rises }} of {{ b.n }} ({{ b.share_positive_pct }}%) | {{ all.share_positive_pct }}% |
| Average move | {% include inr.html n=b.avg_pct %}% | {{ all.avg_pct }}% |

![Nifty's move on each Budget day]({{ '/assets/charts/ta3-budget-days.svg' | relative_url }})

Nifty 50 price index. Source: [Yahoo Finance]({{ ds.index_source_url }}).
Historical data, for illustration only.

**Size.** Budget days moved more than ordinary days. In the shuffle test,
only {{ b.shuffle_share_random_as_big_pct }}% of random sets of {{ b.n }} days had an
average move as large. That is the one result in this post that looks
reasonably solid. But there's a catch. Two of the biggest moves came in 2009,
when every day was volatile. So we also compared each Budget day with the
average move of the 20 sessions before it. Budget days were bigger than their
own recent average {{ b.vs_prior20_bigger_count }} times out of {{ b.n }}
({{ b.vs_prior20_share_bigger_pct }}%). For all days the figure is
{{ b.all_days_vs_prior20_share_bigger_pct }}%. So the effect survives the check, but
it's smaller than the raw averages suggest.

**Direction.** {{ b.falls }} falls and {{ b.rises }} rises. In the shuffle test,
{{ b.shuffle_share_random_as_many_falls_pct }}% of random sets of {{ b.n }} days had
at least as many falls. That's worth noticing, but it isn't much to go on.
It's {{ b.n }} days. The biggest fall
({{ b.biggest_fall.date | date: "%-d %B %Y" }}, down {{ bfall }}%) and the biggest
rise ({{ b.biggest_rise.date | date: "%-d %B %Y" }}, up {{ b.biggest_rise.move_pct }}%)
both sit in the table. And "Budget day tends to fall" would not have told you
which kind of year you were in.

| Date | Day | Budget | Nifty move | Bigger than this % of all days |
|---|---|---|---:|---:|
{% for r in b.rows %}| {{ r.date }} | {{ r.weekday }} | {{ r.type }} | {{ r.move_pct }}% | {{ r.abs_move_percentile }}% |
{% endfor %}

The last column ranks each Budget-day move, by size, among all {% include inr.html n=all.n %}
trading days. A value of 50% would be a perfectly ordinary day.

**Not in the file.** For these Budget days the file has no row. The move shown
runs from the last close before the Budget to the first close after it, so it
includes a second session. It's here for completeness and isn't in any of the
averages above.

| Budget date | Day | First close after | Move over both sessions |
|---|---|---|---:|
{% for r in b.not_in_file %}| {{ r.date }} | {{ r.weekday }} | {{ r.spans_to }} | {{ r.move_pct }}% |
{% endfor %}

Three of these were weekend sessions the feed skipped. The fourth,
17 February 2014, was a Monday; the file simply has no row for it. Leaving
these out makes the Budget-day numbers slightly less complete. Leaving them
in as one-day moves would have made them wrong.

## Muhurat trading: an hour, six data points

Here is every Muhurat session from 2008 to 2025, with NSE's circular, and the
Nifty's move where the file has a row for it:

| Session | Day | Window (IST) | NSE circular | Nifty move |
|---|---|---|---|---:|
{% for r in mu.all %}| {{ r.date }} | {{ r.weekday }} | {{ r.window }} | [{{ r.circular }}]({{ r.source }}) | {% if r.in_file %}{{ r.move_pct }}%{% else %}no row{% endif %} |
{% endfor %}

The file has rows for only **{{ mu.n }}** of the {{ mu.listed }} sessions, all on
weekdays from 2017 on. The weekend sessions and the earlier weekday ones aren't
in this feed. We haven't substituted the next day's close for them, because
that would measure a full trading day, not the Muhurat hour.

On those {{ mu.n }}, the Nifty rose {{ mu.rises }} times and averaged
+{{ mu.avg_pct }}%. That matches the folklore. But:

- **Six is a very small number.** In the shuffle test,
  {{ mu.shuffle_share_random_as_many_rises_pct }}% of random sets of six ordinary days had
  at least {{ mu.rises }} rises. That's far too common to call unusual.
- **The moves were small.** An average size of {{ mu.avg_abs_pct }}%, against
  {{ all.avg_abs_pct }}% on an ordinary day. That's what you'd expect from about an
  hour of thin, ceremonial trading.
- **It's one hour, then a new week.** Even a reliable green hour wouldn't be
  a reason to hold anything afterwards. The session is a tradition, and it's
  worth enjoying as one.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you notice your cricket team won the last five matches you watched
wearing your lucky cap. Five wins in a row feels like proof.

But your team wins a lot of matches anyway. If you counted *every* match —
cap or no cap — you might find they win just as often. And five matches is
not many; a coin can land heads five times out of six more often than you'd
think.

Budget day and Diwali trading are the market's lucky caps. The only way to
know if they matter is to count every one, and compare with all the ordinary
days.

</details>

## Doing it in Python

```python
import pandas as pd

s = pd.read_csv("nifty50-price-index.csv", parse_dates=["date"]
                ).set_index("date").nifty50_pri_close
ret = s.pct_change().dropna()

budget_days = pd.to_datetime(["2021-02-01", "2022-02-01", "2023-02-01",
                              "2024-02-01", "2024-07-23", "2025-02-01"])
missing = budget_days.difference(ret.index)       # check before you trust it
print("not in file:", list(missing.date))
ev = ret.reindex(budget_days.intersection(ret.index))

print(f"Budget days: avg |move| {ev.abs().mean():.2%}, "
      f"all days {ret.abs().mean():.2%}, rises {(ev > 0).sum()} of {len(ev)}")
bigger = sum(ret.sample(len(ev), random_state=i).abs().mean() >= ev.abs().mean()
             for i in range(5000))
print(f"random sets as big: {bigger / 5000:.1%}")
```

Replace the six dates with the full verified list from the table above. The
`missing` line is the important habit: a date that isn't in your file must be
dealt with openly, not skipped without a word.

## Common mistakes

- **Using dates from memory.** Budgets moved from late February to 1 February
  in 2017. Election years have two. Some fell on weekends. Muhurat dates move
  with the Hindu calendar. Get every date from a primary source.
- **Silently dropping days your data doesn't have.** A weekend session missing
  from a price feed can be one of the bigger moves (the 2020 Budget,
  a Saturday, is missing from this one). List what's missing, and say why.
- **Treating "bigger" as "predictable".** Budget days moved more than
  ordinary days. That tells you volatility is higher, not which way it goes.
  Higher volatility cuts both ways.
- **Calling six observations a tradition that works.** Five green sessions
  out of six sounds convincing. Random sets of six ordinary days did that
  {{ mu.shuffle_share_random_as_many_rises_pct }}% of the time.

**Takeaway:** On 18 years of Nifty data with verified dates, Budget days moved noticeably more than ordinary days, but not in a dependable direction. The "Muhurat closes green" belief rests on a handful of sessions, which random sets of days matched {{ mu.shuffle_share_random_as_many_rises_pct }}% of the time. Both dates say something about volatility, not about direction.
