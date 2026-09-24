---
layout: post
title: "Tracking error vs tracking difference: two numbers that sound alike and aren't"
description: "Tracking difference is how far an index fund ended from its index; tracking error is how much the gap wobbled. Only one costs money; a plus sign is a warning."
image: /assets/og/tracking-error-and-tracking-difference.png
date: 2026-10-04 09:00:00 +0530
series: jargon
term: "Tracking error and tracking difference"
---

{% assign t = site.data.jargon_m6.tracking %}

## What the two terms mean

An index fund has one job: deliver the index's return. Two numbers measure how
well it does that, and they answer different questions.

**Tracking difference** is the gap between the fund's return and the index's
return over a period. It answers: *how much did I actually give up (or gain)
by holding the fund instead of the index?* This is the number that costs you
money.

**Tracking error** is the *variability* of that gap — the standard deviation
of the fund's return minus the index's return, measured at daily or monthly
frequency and annualised. It answers: *how tightly does the fund hug the index
day to day?* A fund can have a large tracking difference with tiny tracking
error (it lags the index by exactly its expense ratio, like clockwork), or a
small difference with large error (it wobbles around the index and happens to
end up close).

Both numbers are now published. SEBI's
[passive funds circular of 23 May 2022](https://www.sebi.gov.in/legal/circulars/may-2022/circular-on-development-of-passive-funds_59098.html)
(SEBI/HO/IMD/DOF2/P/CIR/2022/69) caps tracking error for equity index funds
and ETFs (exchange-traded funds) at 2% (measured on one year of daily data), requires it to be
disclosed daily, and requires tracking difference to be disclosed monthly
over 1, 3, 5 and 10 years. Tracking error is still the one that tends to get
quoted, because it's almost always a small, reassuring number. Tracking
difference is the one to look at first.

## The formula

```
Tracking difference  =  R_fund − R_index               (over a stated period)

Tracking error       =  σ( r_fund,t − r_index,t ) × √N

  where r_t are period returns (daily: N = 252; monthly: N = 12)
```

## Worked example: UTI Nifty 50 Index Fund against the Nifty 50

Fund NAV from AMFI via mfapi.in (regular and direct plans); index from Yahoo
Finance, price index. Data to 31 March 2026, so the most recent full calendar
year is 2025. Historical data, for illustration only.

**Tracking error, regular plan, {{ t.window_3y }}:**

| Measured on | Tracking error (annualised) |
|---|---:|
| Daily return differences | {{ t.tracking_error_daily_annualised_pct }}% |
| Monthly return differences | {{ t.tracking_error_monthly_annualised_pct }}% |

Small, as it should be for a fifty-stock index fund — a fraction of one
percent. The fund hugs the index closely.

**Tracking difference, regular plan, same three years:** fund {{ t.fund_cagr_3y_pct }}% a year, index
{{ t.index_pri_cagr_3y_pct }}% a year, difference **+{{ t.tracking_difference_3y_pp }} pp a year**.

And by calendar year, both plans:

| Year | Index (price) | Regular plan | Difference | Direct plan | Difference |
|---|---:|---:|---:|---:|---:|{% for r in t.regular_years %}{% assign d = t.direct_years[forloop.index0] %}
| {{ r.year }} | {{ r.index_pri_pct }}% | {{ r.fund_pct }}% | +{{ r.tracking_difference_pp }} | {{ d.fund_pct }}% | +{{ d.tracking_difference_pp }} |{% endfor %}
| **Mean** | | | **+{{ t.regular_mean_td_pp }}** | | **+{{ t.direct_mean_td_pp }}** |

## Reading the plus sign correctly

An index fund that *beats* its index by a point a year, every year, for ten
years is not a good index fund. It's a fund being measured against the wrong
index.

{{ t.pri_caveat }}

The [alpha post]({% post_url 2026-10-03-alpha %}) made the same point from the other direction.
Against the **total return index (TRI)** — which is what SEBI has required funds to
benchmark against since February 2018 — both columns would flip to small
*negative* numbers: roughly minus the expense ratio, minus a little friction
from cash held for redemptions and the timing of dividend reinvestment. That
negative number is the true cost of indexing, and it's what you should be
comparing across index funds.

To be clear about this post's own numbers: tracking difference should be
measured against the TRI, and every figure above is against the price index,
because a TRI series isn't in this post's data. The table shows the method
and the size of the dividend distortion — not the fund's true cost of
indexing. For that, use the TRI-based tracking difference the fund house
publishes each month.

One thing the table does show correctly, because the benchmark error is the
same for both plans: the **direct plan's difference is {{ t.direct_minus_regular_pp }} pp a year
better than the regular plan's**. That gap is the distributor commission, and
it is the entire subject of the
[expense ratio post]({% post_url 2026-09-28-expense-ratios-direct-vs-regular %}).

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You're trying to walk exactly in your older brother's footsteps in the sand.

Tracking *error* is how wobbly your line is compared to his — do you weave
left and right, or stay right on top of his prints?

Tracking *difference* is where you end up: if he walks 100 steps and you've
only managed 98 by the time he stops, your difference is 2 steps, however
straight your line was.

</details>

## Common mistakes

- **Judging an index fund by tracking error alone.** It measures wobble, not
  cost. Two funds with identical tracking error can differ by half a point a
  year in tracking difference, and that half point compounds.
- **Reading a positive tracking difference as skill.** For an index fund
  against a price index, it's dividends. Check whether the benchmark is the
  PRI (price return index, no dividends) or the TRI (total return index,
  dividends reinvested) before reading any sign.
- **Comparing tracking errors computed on different frequencies.** Daily and
  monthly figures differ ({{ t.tracking_error_daily_annualised_pct }}% vs {{ t.tracking_error_monthly_annualised_pct }}% here) and
  neither is "wrong" — but they aren't interchangeable.
- **Expecting zero.** Even a perfect index fund can't return the index: it has
  costs, holds a little cash, and receives dividends a few days after the
  index books them. A small, steady negative difference against the TRI is
  what good looks like.

**Takeaway:** tracking error is how much an index fund wobbles around its
index; tracking difference is how far it ends up from it — and only the second
one costs you money. When the difference is *positive* year after year, as it
is here against the price index, the fund isn't winning; the benchmark is
missing its dividends.
