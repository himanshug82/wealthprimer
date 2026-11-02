---
layout: post
title: "Value at Risk (VaR): the number that hides the worst days"
seo_title: "Value at Risk (VaR) explained, with its limits"
description: "VaR is the loss a holding should stay under on 99 days in 100. Tested on 18 years of Nifty data: how often it was breached and what it hides."
image: /assets/og/value-at-risk.png
date: 2027-02-18 09:00:00 +0530
series: risk
term: "Value at Risk (VaR)"
---

{% assign r4 = site.data.risk4 %}
{% assign ds = r4.dataset %}
{% assign v = r4.var %}
{% assign t = r4.tails %}

## What is Value at Risk?

**Value at Risk (VaR)** answers a specific question: *over a given period, what is the loss that will not be exceeded with a given confidence?* "One-day 99% VaR of ₹{% assign x = v.hist_99 %}{% include inr.html n=x %} on a ₹{% assign y = v.position %}{% include inr.html n=y %} holding" means: on 99 days out of 100, the loss should be smaller than that figure. It says nothing about the 100th day. That blind spot is the main thing to understand about VaR, and this post tests it on real data. It is part of the [Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}) series and builds on [fat tails]({% post_url 2027-02-08-fat-tails %}).

VaR is widely used in the finance industry as a reporting number. It is a description of a risk profile, and the post doesn't suggest using it as a decision rule.

## The formula

Two common ways to estimate it, for a holding of value V:

```
Historical VaR(c)  =  V × (−1) × the (1 − c) percentile of past daily returns
                      e.g. 99% VaR = V × the loss that was exceeded on only 1% of past days

Parametric VaR(c)  =  V × (z × SD − average return)
                      with z = 1.645 for 95% and 2.326 for 99% (normal curve)
```

The parametric version assumes a bell curve. The historical version assumes the future looks like the sample.

## Worked example: a hypothetical holding in the Nifty 50

Hypothetical holding of ₹{% assign x = v.position %}{% include inr.html n=x %} that tracks the Nifty 50 price index, {{ ds.index_start | date: "%-d %B %Y" }} to {{ ds.index_end | date: "%-d %B %Y" }}, from [Yahoo Finance]({{ ds.index_source_url }}). It is a price index, so dividends are left out. Historical data, for illustration only. The daily SD was {{ v.sd_daily_pct }}%.

| One-day VaR on the holding | 95% | 99% |
|---|---:|---:|
| Historical (the actual percentile) | ₹{% assign x = v.hist_95 %}{% include inr.html n=x %} | ₹{% assign x = v.hist_99 %}{% include inr.html n=x %} |
| Parametric (bell curve) | ₹{% assign x = v.par_95 %}{% include inr.html n=x %} | ₹{% assign x = v.par_99 %}{% include inr.html n=x %} |

At 99%, the parametric number (₹{% assign x = v.par_99 %}{% include inr.html n=x %}) is lower than the historical one (₹{% assign x = v.hist_99 %}{% include inr.html n=x %}): the bell curve understates the tail, which is what [fat tails]({% post_url 2027-02-08-fat-tails %}) predicted. At 95%, it is the other way round.

## Does the 99% VaR hold 99% of the time?

The proper test of a VaR number is out of sample: estimate it from the past, then count how often the next day's loss exceeded it. For each day we computed a 99% parametric VaR from the previous {{ v.window }} sessions and checked the next day's return. That left {{ v.days_tested }} days to test.

| | Days | Share |
|---|---:|---:|
| Expected breaches (1% of days) | {{ v.expected_days }} | {{ v.expected_share_pct }}% |
| Actual breaches | {{ v.breaches }} | {{ v.breach_share_pct }}% |

The 99% VaR was breached about {{ v.breach_share_pct }}% of the time, not 1%. The worst year for breaches was {{ v.worst_year }}, with {{ v.worst_year_breaches }} of them. Breaches tend to bunch, most likely because the number is estimated from the calm stretch before a storm: when volatility jumps, it is out of date. (The test needs {{ v.window }} sessions of history, so it starts about a year into the data.)

The worst single day in the data cost ₹{% assign x = v.worst_day_loss %}{% include inr.html n=x %} on the holding, about {{ v.worst_day_vs_hist99_x }} times the historical 99% VaR. VaR told you nothing about how much worse than the threshold the bad days could be.

## What VaR does and doesn't tell you

| It tells you | It doesn't tell you |
|---|---|
| A loss level exceeded on only a small share of days | How big the loss is on those days |
| A single number comparable across holdings | Whether the past volatility will repeat |
| A scale for ordinary bad days | Anything about crises |

A related measure, **expected shortfall** (the average loss on the days beyond the VaR line), addresses the first row and is why many risk teams look at both. We don't compute it here.

## Common mistakes

- **Reading "99% VaR" as the worst case.** It is the threshold for the best 99 of 100 days, and the 100th day isn't bounded.
- **Trusting a VaR taken from a calm window.** A number estimated from a quiet year says little about a volatile one. Breaches here bunched into the worst years.
- **Applying a one-day number to a longer holding without care.** Scaling by the square root of time assumes returns are independent from day to day; we didn't test that here.
- **Using VaR as a position-sizing rule.** It is a description of a risk profile. The [position sizing post]({% post_url 2026-10-10-position-sizing-and-the-one-percent-rule %}) shows one conventional approach, with its own limits.

## Doing it in Python

```python
import numpy as np
import pandas as pd

s = pd.read_csv("nifty50-price-index.csv", parse_dates=["date"]
                ).set_index("date").nifty50_pri_close
r = s.pct_change().dropna()
position = 10_00_000

print("historical 99%:", round(-np.percentile(r, 1) * position, -2))
print("parametric 99%:", round((2.3263 * r.std() - r.mean()) * position, -2))

# out-of-sample check: VaR from the previous 250 sessions, then count breaches
var = -(r.rolling(250).mean() - 2.3263 * r.rolling(250).std()).shift()
test = pd.DataFrame({"r": r, "var": var}).dropna()
print("breach share:", round((test.r < -test["var"]).mean(), 4))
```

**Takeaway:** Value at Risk gives the loss that should not be exceeded on 99 days out of 100, and says nothing about the 100th. On 18 years of Nifty data the 99% number was breached more often than 1% of the time, mostly in crisis years, so it describes ordinary bad days and not the worst ones.
