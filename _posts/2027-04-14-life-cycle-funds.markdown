---
layout: post
title: "Life cycle funds: what the new category constrains"
description: "SEBI's life cycle funds carry a maturity year in the name and a glide path set by rule: the tenures, the allocation bands by years left, and exit loads."
image: /assets/og/life-cycle-funds.png
date: 2027-04-14 09:00:00 +0530
series: mutual-funds
term: "Life cycle fund"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign l = site.data.mf5.life_cycle %}

## What a life cycle fund is

A **life cycle fund** is a mutual fund category SEBI (the Securities and
Exchange Board of India) created in its circular of 26 February 2026. It is
an open-ended fund with a target maturity year in its name, say
"{{ l.example_name }}", that invests across equity, debt, gold and silver
ETFs (exchange-traded funds) and InvITs (infrastructure investment trusts),
and moves from equity towards debt as that year approaches.

That's a [glide path]({% post_url 2027-03-24-glide-path %}) with the schedule
written into the rules rather than chosen by each fund. This post sets out
what the rules require, as read in November 2026, and what they leave to the
fund. It's part of [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}),
and builds on the [SEBI fund categories post]({% post_url 2026-10-14-sebi-fund-categories-decoded %}).

## The rules

From Annexure B of the [{{ l.circular }}]({{ l.circular_url }}):

- **Tenure:** from {{ l.min_tenure }} to {{ l.max_tenure }} years, in steps
  of {{ l.step }} years. A fund house can have at most {{ l.max_active }}
  open for subscription at a time.
- **Name:** the maturity year must be in the name, as in the circular's own
  example, "Life Cycle Fund 2045".
- **Allocation:** set by how many years are left to maturity, in bands. The
  same bands apply to every tenure; a shorter fund simply starts further down
  the table.
- **Exit load:** the circular's words are "an exit load of 3% would be
  chargeable on any exit by an investor within one year of investment; an
  exit load of 2% within first two years of investment and 1% in the first
  three years of investment", "to inculcate financial discipline". We read
  that as graded: {% for e in l.exit_load %}{{ e.pct }}% in year {{ forloop.index }}{% if forloop.last %}{% else %}, {% endif %}{% endfor %}, and nothing after year 3.
- **Benchmark:** the framework prescribed for multi asset allocation funds.
- **Near maturity:** once a fund has less than a year left, it may be merged
  into the nearest-maturity life cycle fund, with unitholders' positive
  consent.

The allocation bands, in percent of the fund. ETCDs are exchange-traded
commodity derivatives; the circular allows only gold or silver ones here.

| Years to maturity | Equity | Debt | Gold or silver ETFs, ETCDs, InvITs |
|---|---:|---:|---:|
{% for b in l.bands -%}
| {{ b.ytm }} | {{ b.equity }} | {{ b.debt }} | {{ b.other }} |
{% endfor %}

In the last two bands, debt must be rated AA or
above and mature before the fund's own target date. With under
{{ l.arbitrage_note_years }} years left, a fund may also take equity
arbitrage positions of up to {{ l.arbitrage_extra_pct }}% on top of the
equity band, as long as total equity and equity-related exposure stays
within {{ l.equity_total_band }}%.

## Worked example: {{ l.example_name }} over time

A hypothetical {{ l.example_tenure }}-year fund launched in {{ l.example_launch }},
maturing in 2046 (tenures must be multiples of {{ l.step }} years). The bands
it has to sit in at different points in its life, where "years left" is 2046
minus the year. The
circular's bands share their end points (10 years appears in two rows), so
these years avoid the boundaries; in its final year the fund moves to the
under-1-year band.

| Year | Years left | Equity band | Debt band |
|---:|---:|---:|---:|
{% for e in l.example -%}
| {{ e.year }} | {{ e.years_left }} | {{ e.equity }}% | {{ e.debt }}% |
{% endfor %}

Read down the equity column and the glide path appears: wide and high at
first, then narrowing as the target year comes. The bands are ranges, not
points. Two {{ l.example_name }}s from different fund houses could both
comply while one holds, say, 90% equity and the other 66% in the same year.
The rules fix the corridor; the fund chooses where in it to sit.

## Common mistakes

1. **Assuming two funds with the same year behave alike.** The bands allow
   a wide spread, especially early on. Compare the actual allocation each
   fund reports, not just the year in the name.
2. **Reading the target year as a promise.** The year sets the glide path.
   It isn't a promised value, and the fund still holds equity in its final
   year.
3. **Overlooking the exit load.** Leaving within the first three years costs
   up to {{ l.exit_load[0].pct }}% of the amount, which is high by mutual fund
   standards. The [exit load post]({% post_url 2026-10-07-exit-load %})
   explains how instalments of a SIP (systematic investment plan) each carry
   their own clock.
4. **Treating the bands as a recommendation for anyone's own mix.** They are
   SEBI's limits for this category of fund. Whether a glide path, or this one,
   suits a particular goal isn't something the circular, or this post,
   decides.

**Takeaway:** A life cycle fund is a mutual fund with its maturity year in the
name and a glide path set by SEBI's rules, moving from up to 95% equity into
lower equity bands as the year approaches. The rules fix the bands and exit loads;
where in each band a fund sits is its own choice.

## Sources

- [{{ l.circular }}]({{ l.circular_url }}), "Categorization and Rationalization of Mutual Fund Schemes", Annexure B, read on 21 November 2026.
