---
layout: post
title: "Emergency fund: how it's sized and where it sits"
description: "An emergency fund is cash set aside for essential bills if income stops. The months-of-expenses arithmetic, and how five places it can sit differ."
image: /assets/og/emergency-fund-sizing.png
date: 2026-11-08 09:00:00 +0530
series: money-before-markets
term: "Emergency fund"
---

{% assign m = site.data.mbm %}
{% assign e = m.emergency %}
{% assign f = e.fy26 %}
{% assign lq = e.liquid %}
{% assign gl = e.gilt %}

## What an emergency fund is

An **emergency fund** is money kept aside for one job: paying essential bills when your income stops or a large unplanned cost lands. It isn't an investment and isn't meant to earn the most. Its test is whether the full amount is there, in rupees, on the day you need it.

That test is why an emergency fund comes before market investing in [Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}). Market investing assumes you can leave money alone for years. An emergency fund is what lets you.

## The arithmetic

The size of the fund comes from one number: what you must keep paying every month if income stops, including loan EMIs (equated monthly instalments).

```
Essential monthly outflow  =  rent + groceries + loan EMIs + fees + transport + utilities + insurance premiums

Fund target  =  essential monthly outflow  ×  number of months you want to cover
```

Loan EMIs stay on the list because the lender doesn't pause when your income does. How many months to cover is a personal choice with no correct answer. The table below uses 3, 6 and 12 only to show how the target scales; they aren't recommended settings.

## Worked example: an illustrative household

This household is made up. Its monthly figures are made-up inputs, not data about anyone.

| Essential item | Per month (₹) |
|---|---:|
{% for x in e.essentials -%}
| {{ x.item }} | {{ x.monthly }} |
{% endfor -%}
| **Essential outflow** | **{{ e.essentials_total }}** |

The household also spends on things that could be paused: {% assign o = e.other[0] %}{{ o.item | downcase }}, ₹{% include inr.html n=o.monthly %} a month. Counting those too, the total is ₹{% include inr.html n=e.all_total %}. Which list you size against matters:

| Months covered | On essentials only (₹) | On everything (₹) |
|---|---:|---:|
{% for t in e.targets -%}
| {{ t.months }} | {{ t.essentials }} | {{ t.everything }} |
{% endfor %}
To carry the example through, the rest of this post uses the {{ e.buffer_months }}-month row on essentials, ₹{% include inr.html n=e.buffer %}, as the buffer. That is a choice made for the example, not a suggested setting.

## Where the money can sit

Five places come up most often. The table compares properties, not merits.

| Place | Can the rupee amount fall? | How fast can you reach it? | What can go wrong |
|---|---|---|---|
| Savings account | No | Immediately | Interest can trail inflation; deposit insurance covers a limited amount per bank |
| Fixed deposit (FD) | Not if held to maturity | Banks set their own early-withdrawal terms | A penalty or reduced rate on early exit |
| Overnight fund | No down day in the sample below, but nothing guarantees that | Fund's redemption process | Not insured; rules can change |
| Liquid fund | Tiny moves; see below | Fund's redemption process | An [exit load]({% post_url 2026-10-07-exit-load %}) on exits within 7 days |
| Gilt fund | Yes, and by more | Fund's redemption process | Its price can fall when interest rates rise |

The last three are mutual funds, which hold securities and publish a daily **NAV** (net asset value, the price per unit; explained in [what a mutual fund is]({% post_url 2026-09-25-what-a-mutual-fund-is %})). The [liquid and overnight funds post]({% post_url 2026-11-03-liquid-and-overnight-funds %}) covers what SEBI (the Securities and Exchange Board of India) lets them hold.

Here is what the NAVs did over the five years to 31 March 2026. The data is from AMFI (the Association of Mutual Funds in India) via mfapi.in, ends on 31 March 2026, and is shown for illustration only.

- **{{ e.overnight.name }}** had {{ e.overnight.down_days }} down days in {% include inr.html n=e.overnight.days %} days with a published NAV (weekends included for these two funds).
- **{{ lq.name }}** had {{ lq.down_days }} down days in {% include inr.html n=lq.days %} ({{ lq.down_days_share_pct }}%). Its worst day was {% include inr.html n=lq.worst_day_pct %}% on {{ lq.worst_day_date | date: "%-d %B %Y" }}.
- **{{ gl.name }}** fell {{ gl.max_drawdown_pct | abs }}% from its peak on {{ gl.peak_date | date: "%-d %B %Y" }} to its low on {{ gl.trough_date | date: "%-d %B %Y" }}, and didn't regain the peak until {{ gl.recovered_date | date: "%-d %B %Y" }}. A [drawdown]({% post_url 2026-09-29-drawdown %}) of that kind comes from interest rates moving, as the [debt funds post]({% post_url 2026-10-12-debt-funds-explained %}) explained.

Past NAV behaviour doesn't promise future behaviour, and one fund each is a small sample.

## What idle cash costs

Take the ₹{% include inr.html n=e.buffer %} buffer. In FY26 (April 2025 to March 2026), inflation in the consumer price index (CPI) was {{ f.cpi_pct }}%, measured March to March on the all-India combined index. That is this site's calculation from MoSPI's (the Ministry of Statistics and Programme Implementation) old and new index series, set out in [inflation and real returns]({% post_url 2026-10-20-inflation-and-real-returns %}). Held as cash, the buffer buys what ₹{% include inr.html n=f.cash_purchasing_power %} bought a year earlier, a loss of ₹{% include inr.html n=f.cash_loss %} in purchasing power.

The liquid fund's FY26 return was {{ f.liquid_return_pct }}% before tax, which would have grown the buffer to about ₹{% include inr.html n=f.liquid_end %}, or {{ f.liquid_real_pct }}% in real terms. That is one fund over one backward-looking year. It shows why real return, covered in [inflation and real returns]({% post_url 2026-10-20-inflation-and-real-returns %}), applies to a buffer too. It doesn't say where yours belongs.

## Common mistakes

- **Sizing against income, not outflow.** What matters is what you must pay while income is zero. A fund sized on salary can end up far larger or smaller than the bills it has to cover.
- **Treating it as an investment.** Judging the buffer by its return invites moving it into something whose price can fall when you need it, such as the gilt fund above.
- **Forgetting the lag.** If you have to wait days or pay an exit charge to reach the money, the fund isn't doing its job. Check the terms of wherever it sits.
- **Counting money that is already committed.** An emergency fund that also has to cover next quarter's tax or a planned purchase is smaller than it looks.

**Takeaway:** An emergency fund is sized from what you must keep paying if income stops, multiplied by the months you want covered, and judged by whether the full rupee amount is there when you need it. Where it sits changes how fast you can reach it and whether its price can fall, so compare those properties first and the return after.
