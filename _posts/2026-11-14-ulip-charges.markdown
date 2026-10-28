---
layout: post
title: "ULIP charges: what comes out before it grows"
description: "A ULIP deducts several charges before your money grows. How each works, what IRDAI's circular requires, and a worked 10-year example on made-up charges."
image: /assets/og/ulip-charges.png
date: 2026-11-14 09:00:00 +0530
series: money-before-markets
term: "ULIP (unit linked insurance plan)"
---

{% assign m = site.data.mbm %}
{% assign u = m.ulip %}
{% assign c = u.circular %}
{% assign inp = u.inputs %}
{% assign hi = u.high %}
{% assign lo = u.low %}

## What a ULIP is

A **unit linked insurance plan (ULIP)** is a life insurance policy where part of each premium buys life cover and part is invested in funds you choose. The policy's **fund value** is the number of units you hold times the unit price, like a mutual fund's [NAV]({% post_url 2026-09-25-what-a-mutual-fund-is %}) (net asset value, the price per unit).

IRDAI, the Insurance Regulatory and Development Authority of India, draws the line this way in its [Master Circular on Life Insurance Products]({{ c.url }}) (reference {{ c.ref }}, dated {{ c.date | date: "%-d %B %Y" }}), paragraph 34: if every fund in a linked product tracks a publicly available index, it is an index-linked product; otherwise it is a ULIP. The circular is as of {{ c.date | date: "%-d %B %Y" }} and is reviewed every year, so check for a later version. This post is part of [Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}). It is about the cost mechanics, not about whether to hold one. The earlier post on [insurance as risk transfer]({% post_url 2026-10-23-insurance-as-risk-transfer %}) covers why term cover is a different thing from a bundled plan.

## The charges, named

The circular refers to these deductions, each reducing what reaches the fund or what the fund earns:

- **Premium allocation charge:** a share of each premium kept before the rest is invested.
- **Policy administration charge:** a fixed or percentage fee for running the policy.
- **Mortality charge:** the price of the life cover, deducted from the fund.
- **Fund management charge (FMC):** a yearly percentage of the fund value.
- **Switching charge** for moving between funds, and a **guarantee charge** where a plan carries a guarantee.
- **Discontinuance charge** if you stop paying or surrender during the lock-in.

The circular points to Schedule I of the IRDAI (Insurance Products) Regulations, 2024 for the cap on discontinuance charges and for the 4% minimum guaranteed rate. This post doesn't cover any other limit, because Schedule I was not read for it. The same circular (paragraph 3) requires a life insurer to give a customised benefit illustration at the point of sale; that is where a plan's actual charges appear.

## Rules in the circular that matter for cost

| Rule | What the circular says |
|---|---|
| Lock-in | {{ c.lock_in_years }} years for linked products; proceeds are not payable to the policyholder during it except on death or other covered contingencies |
| Stopping early | On discontinuance during the lock-in, the fund value after discontinuance charges moves to a discontinued policy fund. The minimum guaranteed interest on that fund is {{ c.discontinued_fund_min_pct }}% a year. The proceeds are paid at the end of the lock-in, or on surrender if that is later; where the policyholder opts to revive but doesn't, at the end of a three-year revival period if that is later still. Single-premium policies are treated separately (paragraph 40) |
| Illustration floor | For individual ULIPs, the illustrated fund value at maturity must be at least {{ c.illus_floor_pct }}% of total premium paid, at a gross yield of {{ c.illus_floor_gross_pct }}% on the fund, after all deductions (paragraph 7.15.1) |

## The formula

```
Fund at the end of a year  =  (fund at start + premium × (1 − allocation %) − administration charge)
                              × (1 + gross yield) × (1 − FMC %)

Reduction in yield  =  gross yield on the fund  −  yield you earn on the premiums you paid
```

The yield on premiums paid is an internal rate of return, the same idea as the [XIRR (extended internal rate of return)]({% post_url 2026-10-01-sips-xirr-and-timing-myths %}) used for SIPs (systematic investment plans). The second line is the number that sums up all charges: how far the yield you earned falls short of the fund's own return. Mortality charges are left out below, so the example shows the cost of the investment part only.

## Worked example: a made-up plan

**These charges are invented to show the arithmetic.** They are not any insurer's charges and not IRDAI's caps. A real plan will differ.

- Premium: ₹{% include inr.html n=inp.premium %} a year for {{ inp.years }} years (₹{% include inr.html n=inp.total_premium %} in all).
- Allocation charge: {% for a in inp.alloc %}{% assign x = a.pct %}{% include inr.html n=x %}% in year {{ a.year }}{% unless forloop.last %}, {% endunless %}{% endfor %}, then nothing.
- Administration charge: ₹{% include inr.html n=inp.admin %} a year.
- Fund management charge: {% assign x = inp.fmc_pct %}{% include inr.html n=x %}% of the fund each year.

At a gross yield of {% assign x = hi.gross_pct %}{% include inr.html n=x %}% a year on the fund:

| Year | Premium (₹) | Allocation charge (₹) | Administration (₹) | FMC (₹) | Fund at year end (₹) |
|---|---:|---:|---:|---:|---:|
{% for r in hi.rows -%}
| {{ r.year }} | {{ r.premium }} | {{ r.allocation_charge }} | {{ r.admin_charge }} | {{ r.fmc }} | {{ r.fund_end }} |
{% endfor %}
The result at the end of year {{ inp.years }}, and the same plan at a lower gross yield:

| | Gross yield on the fund | Fund value (₹) | Fund value as % of premiums paid | Yield on premiums paid | Reduction in yield |
|---|---:|---:|---:|---:|---:|
| Higher case | {% assign x = hi.gross_pct %}{% include inr.html n=x %}% | {{ hi.fund_value }} | {% assign x = hi.pct_of_premiums %}{% include inr.html n=x %}% | {% assign x = hi.net_yield_pct %}{% include inr.html n=x %}% | {% assign x = hi.reduction_pts %}{% include inr.html n=x %} points |
| Lower case | {% assign x = lo.gross_pct %}{% include inr.html n=x %}% | {{ lo.fund_value }} | {% assign x = lo.pct_of_premiums %}{% include inr.html n=x %}% | {% assign x = lo.net_yield_pct %}{% include inr.html n=x %}% | {% assign x = lo.reduction_pts %}{% include inr.html n=x %} points |

The yield on premiums paid treats each year's premium as paid at the start of the year and the fund as received at the end of year {{ inp.years }}. The lower case mirrors the circular's test of {{ c.illus_floor_gross_pct }}% gross. But the circular counts all deductions, including mortality charges, and this model leaves those out. Without them, the made-up plan's fund value is {% assign x = lo.pct_of_premiums %}{% include inr.html n=x %}% of premiums paid, above the {{ c.illus_floor_pct }}% floor of ₹{% include inr.html n=u.floor_amount %}. With a mortality charge it would be lower, so this doesn't show that the plan would pass.

What the table shows: the allocation charge falls only in the first five years, while the fund management charge and the administration charge recur every year, so the gap between the fund's return and your return is not one number but a fee that applies all through the term. What it doesn't show: the mortality charge, any guarantee, or what the same premiums would have earned elsewhere.

## Common mistakes

- **Comparing the fund's return with a policy's return.** The fund's return is before charges. What you earned on premiums paid is lower, by the reduction in yield.
- **Ignoring the lock-in.** Proceeds are not paid out during the first {{ c.lock_in_years }} years even if you stop paying. The fund value moves to a discontinued policy fund, after discontinuance charges, and is paid out later, on the terms in the table above.
- **Reading an illustrated return as a forecast.** An illustration at any gross yield is an assumption about the fund, not a promise, and the [real return]({% post_url 2026-10-20-inflation-and-real-returns %}) after inflation is lower again.
- **Taking a made-up example as typical.** The charges above were chosen for the arithmetic. The plan in front of you states its own.

**Takeaway:** A ULIP's charges are taken before and during growth, so the return you earn on premiums paid is lower than the fund's own return by the combined effect of every charge. The plan's own benefit illustration is where to read that reduction in yield, and it is worth checking which charges fall in the early years.
