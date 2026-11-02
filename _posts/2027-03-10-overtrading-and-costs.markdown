---
layout: post
title: "Overtrading: what every extra trade costs, in arithmetic"
seo_title: "Overtrading and trading costs: the arithmetic"
description: "Overtrading is trading more than your edge can pay for. The cost arithmetic by trade count, and what SEBI's F&O studies say about costs and repeat losses."
image: /assets/og/overtrading-and-costs.png
date: 2027-03-10 09:00:00 +0530
series: risk
term: "Overtrading"
---

{% assign r4 = site.data.risk4 %}
{% assign o = r4.overtrading %}
{% assign sb = o.sebi %}
{% assign fno = site.data.fno %}

## What is overtrading?

**Overtrading** is trading more often than the expected gain from each trade can pay for. It isn't a fixed number of trades: it is the point where costs eat the edge. Every trade pays brokerage, exchange charges, taxes and the gap between the buying and selling price ([the bid-ask spread]({% post_url 2026-10-14-bid-ask-spread-and-liquidity %})). Those costs arrive whether the trade makes money or not, and they compound against you the way [fund costs]({% post_url 2026-09-28-expense-ratios-direct-vs-regular %}) do, only faster.

This post does the arithmetic and then looks at what SEBI's own studies of individual F&O (futures and options) traders say. It describes patterns; it is not advice about how often to trade. It is part of the [Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}) series and follows [what the F&O numbers actually say]({% post_url 2026-10-08-what-the-fo-numbers-actually-say %}).

## The formula

```
Cost of one round trip (buy and sell)  =  2 × cost per side
Net return after N round trips in a year  =  (1 + gross return) × (1 − round-trip cost)^N − 1
```

This treats each trade as a round trip using all the capital, and the cost as a fraction of it. It is a simplification (real trades often use part of the capital) but it shows the shape.

## Worked example: a hypothetical gross return of {{ o.gross_pct }}%

Suppose that before any trading costs, a strategy would earn {{ o.gross_pct }}% a year, and that every side costs {{ o.cost_per_side_pct }}% all-in. These are illustrative assumptions, the same 0.1% a side used in the [Technical Analysis backtests]({% post_url 2026-10-15-how-to-backtest-honestly %}), not a quote for any broker. The only variable is how many round trips it takes to earn that gross return:

| Round trips a year | Net return after costs | Costs took (percentage points) |
|---:|---:|---:|
{% for g in o.grid %}{% assign n1 = g.net_pct %}{% assign c1 = g.cost_drag_pp %}| {{ g.round_trips }} | {% include inr.html n=n1 %}% | {% include inr.html n=c1 %} |
{% endfor %}
With zero round trips, the gross return is untouched. At roughly one a month, costs take a few points. At roughly one a week, they take nearly all of it. At daily trading, the same gross return becomes a net loss. The point isn't that these particular numbers are real: it is that a cost that looks tiny per trade is a large annual number when multiplied by the trade count, and the gross return has to clear it every year.

## What SEBI's studies show

In our view, SEBI's (the Securities and Exchange Board of India's) studies of individual traders in the equity derivatives segment are the most useful public evidence on what active trading in that segment does. The figures below come from its [profitability]({{ fno.sources.fy25_fy26_study.pdf }}) and [trading behaviour]({{ fno.sources.fy25_fy26_behaviour_study.pdf }}) studies, both dated {{ fno.sources.fy25_fy26_study.date }}:

| Measure (FY26, financial year 2025-26, unless stated) | Figure |
|---|---:|
| Share of individual F&O traders who lost money | {{ sb.loss_pct_fy26 }}% |
| Individual traders' aggregate net loss (SEBI's top-15-broker sample) | ₹{% assign x = sb.aggregate_loss_cr %}{% include inr.html n=x %} crore |
| Transaction costs, about, per year (FY25 and FY26) | ₹{% assign x = sb.costs_cr_per_year %}{% include inr.html n=x %} crore |
| Costs as a share of the aggregate loss, about | {{ sb.costs_share_of_loss_pct }}% |
| Share of index-options turnover in contracts on their expiry day | {{ sb.zero_dte_share_pct }}% |

Costs were a sizeable fraction of the traders' aggregate loss, roughly {{ sb.costs_share_of_loss_pct }}% by this rough comparison (the studies give "about ₹25,000 crore" for costs, so the ratio is approximate, and we couldn't confirm the two figures share a base: the loss is a sample figure, and SEBI says the full population's would be about 1.11 times it). That doesn't mean cutting costs would have turned a loss into a profit: 82.1% of traders lost even before costs, against 87.7% after.

SEBI also reports that 90–92% of those who lost money in each of the two preceding years lost again. That figure needs its base rate beside it: {{ sb.loss_pct_fy26 }}% of *all* traders lost money in FY26. A repeat-loser rate of about {{ sb.repeat_loser_pct }}% against an overall rate of {{ sb.loss_pct_fy26 }}% is only a little worse than the average trader, so repetition by itself isn't the striking part. What is striking is how high the base rate is.

The studies don't establish that trading frequency *caused* the losses. They show the combination: a high loss rate, costs that run into tens of thousands of crores a year, and much activity concentrated on very short-dated contracts. The cost arithmetic above explains why high frequency makes the break-even harder.

## Common mistakes

- **Counting costs per trade instead of per year.** A cost that looks negligible per round trip, multiplied by a trade a day, is a large share of the year's capital.
- **Treating activity as effort.** More trades feel like more work, but in our view there is no reason for returns to rise with the count.
- **Ignoring the costs that aren't brokerage.** Taxes and the bid-ask gap are costs too; the [contract note post]({% post_url 2027-01-03-contract-note-charges %}) shows the first, and the second depends on how liquid the instrument is.
- **Taking a repeat-loser statistic at face value.** Compare it with the share of all traders who lost, as above.

## Doing it in Python

```python
gross, side_cost = 0.12, 0.001          # hypothetical gross return and cost per side

for trips in (0, 12, 52, 250):
    net = (1 + gross) * (1 - 2 * side_cost) ** trips - 1
    print(f"{trips:>3} round trips: net {net:6.1%}, costs took {(gross - net) * 100:5.1f} points")
```

**Takeaway:** A trading cost that looks tiny per trade becomes a large annual number once you multiply by the trade count, and the gross return has to clear it every year. SEBI's studies show a very high share of individual F&O traders losing money, with costs a sizeable part of the total loss.
