---
layout: post
title: "Tracking error vs tracking difference: two numbers that sound alike and aren't"
seo_title: "Tracking error vs tracking difference, explained"
description: "Tracking difference is how far an index fund ended from its index; tracking error is how much the gap wobbled. Only one costs money; a plus is a warning."
image: /assets/og/tracking-error-and-tracking-difference.png
date: 2026-10-04 09:00:00 +0530
series: jargon
term: "Tracking error and tracking difference"
last_modified_at: 2026-10-25
---

{% assign t = site.data.jargon_m6.tracking %}
{% assign src = site.data.mf4.sources.tri %}

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

Fund NAV from AMFI via mfapi.in (regular and direct plans). Index: the Nifty 50
**total return index (TRI)** from [{{ src.source }}]({{ src.url }}), which is the
benchmark SEBI requires, and for contrast the price index from Yahoo Finance.
Data to 31 March 2026, so the most recent full calendar year is 2025.
Historical data, for illustration only.

**Tracking error, regular plan, {{ t.window_3y_tri }}:**

| Measured on | Against the TRI | Against the price index |
|---|---:|---:|
| Daily return differences | **{{ t.tracking_error_daily_vs_tri_pct }}%** | {{ t.tracking_error_daily_annualised_pct }}% |
| Monthly return differences | **{{ t.tracking_error_monthly_vs_tri_pct }}%** | {{ t.tracking_error_monthly_annualised_pct }}% |

Against the right index the wobble is tiny: a few hundredths of a percent a
year. Against the price index it looks several times bigger, because every
time a Nifty company goes ex-dividend the price index drops and the fund
doesn't. The wrong benchmark inflates the error as well as the difference.

**Tracking difference, regular plan, same three years:** fund {{ t.fund_cagr_3y_tri_window_pct }}% a year, TRI
{{ t.index_tri_cagr_3y_pct }}% a year, difference **{{ t.tracking_difference_3y_vs_tri_pp | replace: "-", "−" }} pp a year**. Against the price
index ({{ t.index_pri_cagr_3y_pct }}% a year) the same fund would show +{{ t.tracking_difference_3y_pp }} pp.

And by calendar year, both plans, against the TRI:

| Year | Index (TRI) | Regular plan | Difference | Direct plan | Difference |
|---|---:|---:|---:|---:|---:|{% for r in t.regular_years %}{% assign d = t.direct_years[forloop.index0] %}
| {{ r.year }} | {{ r.index_tri_pct }}% | {{ r.fund_pct }}% | {{ r.td_vs_tri_pp | replace: "-", "−" }} | {{ d.fund_pct }}% | {{ d.td_vs_tri_pp | replace: "-", "−" }} |{% endfor %}
| **Mean** | | | **{{ t.regular_mean_td_vs_tri_pp | replace: "-", "−" }}** | | **{{ t.direct_mean_td_vs_tri_pp | replace: "-", "−" }}** |

## Reading the sign correctly

All {{ t.years_negative_vs_tri }} differences in that table are negative, and they're small and steady.
That is what a working index fund looks like: it returns the index minus its
costs. Those costs are the expense ratio, a little cash held for redemptions,
and dividends that reach the fund a few days after the index books them.
That negative number is the true cost of indexing, and it's what you should
be comparing across index funds.

Now measure the same fund against the price index and the signs flip. The
regular plan's mean difference becomes **+{{ t.regular_mean_td_pp }} pp a year** (direct plan
+{{ t.direct_mean_td_pp }}). An index fund that *beats* its index by about a point a year,
every year, for ten years is not a good index fund. It's a fund being
measured against the wrong index. The plus sign is mostly dividends (the TRI ran
{{ site.data.jargon_m6.alpha.tri_minus_pri_mean_pp }} pp a year ahead of the price index over these ten years) minus the
fund's costs. It is not outperformance.

The [alpha post]({% post_url 2026-10-03-alpha %}) made the same point from the other direction.
SEBI has required funds to benchmark against the TRI since February 2018; for
any other index fund, use the TRI-based tracking difference the fund house
publishes.

One more thing the table shows: the **direct plan trails the index by {{ t.direct_minus_regular_vs_tri_pp }} pp a
year less than the regular plan**. That gap is the distributor commission, and
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
- **Comparing tracking errors computed on different frequencies or
  benchmarks.** Daily and monthly figures can differ, and neither is "wrong",
  but they aren't interchangeable. Against the price index they differed here
  ({{ t.tracking_error_daily_annualised_pct }}% vs {{ t.tracking_error_monthly_annualised_pct }}%), and both were several times the TRI figures.
- **Expecting zero.** Even a perfect index fund can't return the index: it has
  costs, holds a little cash, and receives dividends a few days after the
  index books them. A small, steady negative difference against the TRI is
  what good looks like.

**Takeaway:** tracking error is how much an index fund wobbles around its
index; tracking difference is how far it ends up from it — and only the second
one costs you money. Measured against the total return index, a good index fund
shows a small, steady negative difference; a positive one year after year
means the benchmark is missing its dividends.
