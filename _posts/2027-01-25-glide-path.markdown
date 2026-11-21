---
layout: post
title: "Glide path: shifting the mix as a goal gets close"
description: "A glide path moves money from equity to bonds as a goal nears. Tested on 97 ten-year windows of Indian data against a fixed 50/50 mix and an 80/20 mix."
image: /assets/og/glide-path.png
date: 2027-01-25 09:00:00 +0530
series: money-before-markets
term: "Glide path"
---

{% assign m = site.data.mbm2 %}
{% assign ds = m.dataset %}
{% assign gp = m.glide %}
{% assign s50 = gp.static_50 %}
{% assign gl = gp.glide %}
{% assign s80 = gp.static_80 %}

## What a glide path is

A **glide path** is a plan to change a portfolio's
[asset allocation]({% post_url 2027-01-23-asset-allocation %}) on a
schedule as a goal gets closer: more equity while the goal is far away, more
bonds or cash as it nears. "Target-date" and "lifecycle" funds use the same
idea, with the schedule built in.

The reason is the [investment horizon]({% post_url 2027-01-22-investment-horizon %}).
Money for a goal ten years away has more time to recover from a fall. The same
money a year before the goal doesn't. A large fall in the last year or two
can leave a goal short with no time to make it up; the
[sequence-of-returns post]({% post_url 2026-10-13-sequence-of-returns-risk %})
shows why late losses hurt most. It's part of
[Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}).

## The formula

A straight-line glide over n years, from a starting equity share to an
ending one:

```
Equity share in year k  =  start − (start − end) × k / (n − 1)        k = 0, 1, … n − 1
Bond share              =  1 − equity share
```

Here n = {{ gp.years }}, start = {{ gp.glide_from }}% and end =
{{ gp.glide_to }}%, so equity steps down by the same amount each year and the
average equity share across the ten years is 50%. The portfolio is reset to
that year's target on each anniversary of the start.

## Worked example: every 10-year window from {{ gp.first_start }}

**Fair comparison first.** A glide that averages 50% equity over its years
is compared with a fixed 50/50 mix, not with a mix holding more or less
equity on average. It's not a perfect match: later years hold more money, so
weighted by rupees the glide held less equity than 50/50 (a median of
{{ gl.median_money_weighted_equity_pct }}% across the windows, against
{{ s50.median_money_weighted_equity_pct }}%). That is part of why its median
return comes out lower. We also show a fixed 80/20 mix, the glide's starting
point. All three reset to target on each anniversary of the start, not on 1
April as in the [asset allocation post]({% post_url 2027-01-23-asset-allocation %}),
so this 80/20 isn't quite that post's.

**Data.** Equity is the Nifty 50 TRI (Total Returns Index, dividends
reinvested, from NSE Indices, part of the National Stock Exchange). Bonds are
the UTI Gilt Fund (from UTI Mutual Fund), regular plan, NAV (net asset value) from AMFI, the
Association of Mutual Funds in India; sources are in the
[asset classes post]({% post_url 2027-01-21-asset-classes %}).

**Windows.** One window starts on {{ gp.first_start }}, the data's first
day, then one on the first trading day of each month to {{ gp.last_start }}, and runs {{ gp.years }} years:
{{ gp.windows }} windows. Later starts are dropped because their 10 years end
after {{ ds.end }}. Each puts in ₹10,00,000 at the start. No tax or trading
costs; the gilt fund's own costs (a regular plan's) are in its NAV, and the
index has none.
Past data, for illustration only.

| {{ gp.windows }} ten-year windows | Fixed 50/50 | Glide 80 → 20 | Fixed 80/20 |
|---|---:|---:|---:|
| Median ending value (₹) | {{ s50.median_final }} | {{ gl.median_final }} | {{ s80.median_final }} |
| Median CAGR | {{ s50.median_cagr_pct | replace: "-", "−" }}% | {{ gl.median_cagr_pct | replace: "-", "−" }}% | {{ s80.median_cagr_pct | replace: "-", "−" }}% |
| Worst ending value (₹) | {{ s50.worst_final }} | {{ gl.worst_final }} | {{ s80.worst_final }} |
| Best ending value (₹) | {{ s50.best_final }} | {{ gl.best_final }} | {{ s80.best_final }} |
| Worst fall within the last 2 years | {{ s50.worst_last2_dd_pct | replace: "-", "−" }}% | {{ gl.worst_last2_dd_pct | replace: "-", "−" }}% | {{ s80.worst_last2_dd_pct | replace: "-", "−" }}% |
| Median fall within the last 2 years | {{ s50.median_last2_dd_pct | replace: "-", "−" }}% | {{ gl.median_last2_dd_pct | replace: "-", "−" }}% | {{ s80.median_last2_dd_pct | replace: "-", "−" }}% |
| Windows with a fall over 10% in the last 2 years | {{ s50.last2_dd_over_10_pct | replace: "-", "−" }}% | {{ gl.last2_dd_over_10_pct | replace: "-", "−" }}% | {{ s80.last2_dd_over_10_pct | replace: "-", "−" }}% |

CAGR is the compound annual growth rate. "Fall within the last 2 years" is
the largest drop from a high to a later low in a window's final two years,
the [drawdown]({% post_url 2026-09-29-drawdown %}) measured over that stretch
only.

### What the table shows

1. **The glide did what it's for.** Its worst fall in the final two years
   was {{ gl.worst_last2_dd_pct | replace: "-", "−" }}%, against {{ s50.worst_last2_dd_pct | replace: "-", "−" }}%
   for the fixed 50/50 mix with the same time-average equity, and
   {{ s80.worst_last2_dd_pct | replace: "-", "−" }}% for 80/20. Falls of more than 10% near the
   end happened in {{ gl.last2_dd_over_10_pct | replace: "-", "−" }}% of glide windows, against
   {{ s50.last2_dd_over_10_pct | replace: "-", "−" }}% for 50/50.
2. **It wasn't free.** The glide's median ending value was lower than
   50/50's: ₹{% include inr.html n=gl.median_final %} against
   ₹{% include inr.html n=s50.median_final %}. The glide holds less equity
   late in each window, when there is most money, so whatever equity earned
   then counted for less. Its best ending value, though, was higher than
   50/50's: ₹{% include inr.html n=gl.best_final %} against
   ₹{% include inr.html n=s50.best_final %}.
3. **The worst outcomes were close.** The worst ending values of the glide
   and 50/50 were within a few percent of each other; the glide's was
   slightly higher. Fixed 80/20 had the highest median and the lowest worst
   case, the widest range of the three.

So the trade, in this data, was a little median return for a calmer last
stretch, when a fall would be hardest to recover from.

## Common mistakes

1. **Comparing a glide with the wrong fixed mix.** Against an all-equity
   portfolio, any glide looks safer and poorer. Against a fixed mix with the
   same time-average equity, the trade-off shows up more clearly, though the
   rupee-weighted difference above still tilts it.
2. **Reading {{ gp.windows }} windows as {{ gp.windows }} experiences.**
   The windows overlap heavily: all start within eight years of each other
   and run ten, so every pair shares at least two years. This is one stretch
   of history seen from many angles.
3. **Treating the schedule as standard.** Starting at {{ gp.glide_from }}% and
   ending at {{ gp.glide_to }}% in a straight line is one illustrative choice.
   Products that build in a glide path set their own schedules; read the
   product's own documents for what it actually does.
4. **Forgetting the goal can move.** A glide path is tied to a date. If the
   date shifts and the schedule doesn't, the money ends up too cautious too
   early, or too exposed too late.

**Takeaway:** A glide path cuts equity as a goal gets close, so a late fall
does less damage. In this data it gave up a little median return for a much
calmer finish; judged against all-equity instead of a comparable fixed mix,
that trade-off disappears from view.
