---
layout: post
title: "Value at Risk (VaR): the number that hides the worst days"
seo_title: "Value at Risk (VaR) explained, with its limits"
description: "VaR is the loss a holding should stay under on 99 days in 100. Tested on 18 years of Nifty data: how often it was breached and what it hides."
image: /assets/og/value-at-risk.png
date: 2027-02-18 09:00:00 +0530
series: risk
term: "Value at Risk (VaR)"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign r4 = site.data.risk4 %}
{% assign ds = r4.dataset %}
{% assign v = r4.var %}
{% assign t = r4.tails %}

## What is Value at Risk?

**Value at Risk (VaR)** answers a specific question: *over a given period, what is the loss that will not be exceeded with a given confidence?* "One-day 99% VaR of ₹{% assign x = v.hist_99 %}{% include inr.html n=x %} on a ₹{% assign y = v.position %}{% include inr.html n=y %} holding" means: on 99 days out of 100, the loss should be smaller than that figure. It says nothing about the 100th day. That blind spot is the main thing to understand about VaR, and this post tests it on real data. It is part of the [Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}) series and builds on [fat tails]({% post_url 2027-02-08-fat-tails %}).

VaR also sits behind margins: SEBI's (the Securities and Exchange Board of India's) master circular SEBI/HO/MRD-PoD2/CIR/P/2024/00181 of 30 December 2024 bases the initial margin in derivatives on a 99% one-day VaR (Chapter 5, para 1.2.5.1). SEBI announced a review of that circular in June 2026, so check the current text. In this post it is a description of a risk profile, and the post doesn't suggest using it as a decision rule.

## The formula

Two common ways to estimate it, for a holding of value V:

```
Historical VaR(c)  =  V × (−1) × the (1 − c) percentile of past daily returns
                      e.g. 99% VaR = V × the loss that was exceeded on only 1% of past days

Parametric VaR(c)  =  V × (z × SD − average return)      (SD is standard deviation)
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

The proper test of a VaR number is out of sample: estimate it from the past, then count how often the next day's loss exceeded it. For each day we computed a 99% bell-curve VaR from the previous {{ v.window }} sessions and checked the next day's return. That left {% assign x = v.days_tested %}{% include inr.html n=x %} days, from {{ v.test_start | date: "%-d %B %Y" }} to {{ v.test_end | date: "%-d %B %Y" }}, so the test misses the first {{ v.fall_before_test_pct | abs }}% of the 2008 fall but includes October 2008.

| | Days | Share |
|---|---:|---:|
| Expected breaches (1% of days) | {{ v.expected_days }} | {{ v.expected_share_pct }}% |
| Actual breaches | {{ v.breaches }} | {{ v.breach_share_pct }}% |

That rolling bell-curve VaR was breached about {{ v.breach_share_pct }}% of the time, not 1%, and not just in crises:

| | Breaches | Share of those days |
|---|---:|---:|
| 2008, 2009 and 2020 | {{ v.breaches_crisis_years }} | {{ v.breach_share_crisis_pct }}% |
| All other years | {{ v.breaches_other_years }} | {{ v.breach_share_other_pct }}% |

The highest count was {{ v.worst_year_breaches }} in {{ v.worst_year }}, but 2009 had none. Breaches came in short runs, though: the {{ v.breaches }} of them fell in {{ v.months_with_breach }} of {{ v.months_tested }} months, in ordinary years as well as crisis years. Two causes plausibly contribute, and this test doesn't separate them: the number goes stale when volatility jumps, and the bell curve understates tails. A rolling historical VaR, with no bell curve, was breached {{ v.breach_share_rolling_historical_pct }}% of the time; a bell-curve line fixed on the whole sample, which can't go stale but uses hindsight, {{ v.breach_share_full_sample_normal_pct }}%.

The worst single day in the data cost ₹{% assign x = v.worst_day_loss %}{% include inr.html n=x %} on the holding, about {{ v.worst_day_vs_hist99_x }} times the historical 99% VaR. VaR told you nothing about how much worse than the threshold the bad days could be.

## What VaR does and doesn't tell you

| It tells you | It doesn't tell you |
|---|---|
| A loss level exceeded on only a small share of days | How big the loss is on those days |
| A single number comparable across holdings | Whether the past volatility will repeat |
| A scale for ordinary bad days | Anything about crises |

A related measure, **expected shortfall** (the average loss on the days beyond the VaR line), addresses the first row. We don't compute it here.

## Common mistakes

- **Reading "99% VaR" as the worst case.** It is the threshold for the best 99 of 100 days, and the 100th day isn't bounded.
- **Trusting a VaR taken from a calm window.** A number estimated from a quiet year says little about a volatile one. Breaches here came in short runs, and in ordinary years too.
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

**Takeaway:** Value at Risk gives the loss that should not be exceeded on 99 days out of 100, and says nothing about the 100th. On Nifty data since 2008, a 99% bell-curve VaR re-estimated daily was breached more than 1% of the time, in crisis years and, less often, in ordinary ones, so it is an estimate and says nothing about the worst days.
