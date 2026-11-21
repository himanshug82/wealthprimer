---
layout: post
title: "Glide path: shifting the mix as a goal gets close"
description: "A glide path moves money from equity to bonds as a goal nears. Tested on 97 ten-year windows of Indian data against a fixed mix with the same average."
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
Money for a goal ten years away has time to recover from a fall. The same
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

**Fair comparison first.** A glide that averages 50% equity should be
compared with a fixed 50/50 mix, not with a mix holding more or less equity
on average. We also show a fixed 80/20 mix, the glide's starting point.

**Data.** Equity is the Nifty 50 TRI (Total Returns Index, dividends
reinvested, from NSE Indices, part of the National Stock Exchange). Bonds are
the UTI Gilt Fund, regular plan, NAV (net asset value) from AMFI, the
Association of Mutual Funds in India; sources are in the
[asset classes post]({% post_url 2027-01-21-asset-classes %}).

**Windows.** One window starts on the first trading day of each month from
{{ gp.first_start }} to {{ gp.last_start }} and runs {{ gp.years }} years:
{{ gp.windows }} windows. Later starts are dropped because their 10 years end
after {{ ds.end }}. Each puts in ₹10,00,000 at the start. No tax, no costs.
Past data, for illustration only.

| {{ gp.windows }} ten-year windows | Fixed 50/50 | Glide 80 → 20 | Fixed 80/20 |
|---|---:|---:|---:|
| Median ending value (₹) | {{ s50.median_final }} | {{ gl.median_final }} | {{ s80.median_final }} |
| Median CAGR | {{ s50.median_cagr_pct }}% | {{ gl.median_cagr_pct }}% | {{ s80.median_cagr_pct }}% |
| Worst ending value (₹) | {{ s50.worst_final }} | {{ gl.worst_final }} | {{ s80.worst_final }} |
| Best ending value (₹) | {{ s50.best_final }} | {{ gl.best_final }} | {{ s80.best_final }} |
| Worst fall within the last 2 years | {{ s50.worst_last2_dd_pct }}% | {{ gl.worst_last2_dd_pct }}% | {{ s80.worst_last2_dd_pct }}% |
| Median fall within the last 2 years | {{ s50.median_last2_dd_pct }}% | {{ gl.median_last2_dd_pct }}% | {{ s80.median_last2_dd_pct }}% |
| Windows with a fall over 10% in the last 2 years | {{ s50.last2_dd_over_10_pct }}% | {{ gl.last2_dd_over_10_pct }}% | {{ s80.last2_dd_over_10_pct }}% |

CAGR is the compound annual growth rate. "Fall within the last 2 years" is
the largest drop from a high to a later low in a window's final two years,
the [drawdown]({% post_url 2026-09-29-drawdown %}) measured over that stretch
only.

### What the table shows

1. **The glide did what it's for.** Its worst fall in the final two years
   was {{ gl.worst_last2_dd_pct }}%, against {{ s50.worst_last2_dd_pct }}%
   for the fixed 50/50 mix with the same average equity, and
   {{ s80.worst_last2_dd_pct }}% for 80/20. Falls of more than 10% near the
   end happened in {{ gl.last2_dd_over_10_pct }}% of glide windows, against
   {{ s50.last2_dd_over_10_pct }}% for 50/50.
2. **It wasn't free.** The glide's median ending value was lower than
   50/50's: ₹{% include inr.html n=gl.median_final %} against
   ₹{% include inr.html n=s50.median_final %}. The glide holds less equity
   late in each window, so whatever equity earned then counted for less.
3. **The worst outcomes were close.** The worst ending values of the glide
   and 50/50 were within a few percent of each other; the glide's was
   slightly higher. Fixed 80/20 had the highest median and the lowest worst
   case, the widest range of the three.

So the trade, in this data, was a little median return for a calmer last
stretch, when a fall would be hardest to recover from.

## Common mistakes

1. **Comparing a glide with the wrong fixed mix.** Against an all-equity
   portfolio, any glide looks safer and poorer. Against a fixed mix with the
   same average equity, the real trade-off shows up.
2. **Reading {{ gp.windows }} windows as {{ gp.windows }} experiences.**
   The windows overlap heavily: all start within eight years of each other
   and run ten, so every pair shares at least two years. This is one stretch
   of history seen from many angles.
3. **Treating the schedule as standard.** Starting at {{ gp.glide_from }}% and
   ending at {{ gp.glide_to }}% in a straight line is one illustrative choice.
   Products that build in a glide path set their own schedules; read the
   product's own documents for what it actually does.
4. **Forgetting the goal can move.** A glide path is tied to a date. If the
   date shifts, the schedule needs to shift with it, or the money ends up too
   cautious too early, or too exposed too late.

**Takeaway:** A glide path trades some return for a calmer finish, cutting
equity as the goal gets close so a late fall does less damage. Judge one
against a fixed mix with the same average equity, not against all-equity, or
the trade-off disappears from view.
