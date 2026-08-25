---
layout: post
title: "Expense ratios: what the same fund costs in two different plans"
date: 2026-12-04 09:00:00 +0530
series: mutual-funds
---

{% assign mf = site.data.mf %}
{% assign f = mf.index_fund %}
{% assign e = mf.expense_ratio %}
{% assign ei = e.index_fund %}
{% assign ea = e.active_fund %}

## A fee you never see

The **expense ratio** is what a fund charges annually to run itself —
management fees, administration, distributor commissions, marketing. It's
quoted as a percentage of assets: a 1.5% expense ratio on ₹1,00,000 costs
₹1,500 a year.

You will never see this charged. No debit appears, no statement line itemises
it — as the [opening post]({% post_url 2026-11-28-what-a-mutual-fund-is %}) noted, every
NAV you have ever seen is already net of it. It's deducted from the fund's assets daily, before NAV is published. Every
return you have ever seen quoted for a fund is already net of it.

That invisibility is exactly why it deserves a post. A cost you never
consciously pay is a cost you never think about.

## The natural experiment

Ordinarily, working out what fees cost you means comparing different funds —
and then you can't separate the fee from everything else that differs.

Indian mutual funds hand us a perfect controlled experiment. Since January
2013, every scheme has been available in two plans:

| Plan | What it is |
|---|---|
| **Regular** | Bought through a distributor, whose trail commission is built into the expense ratio |
| **Direct** | Bought straight from the AMC — same fund, no commission |

Same portfolio. Same fund manager. Same securities, bought and sold on the
same days, in the same proportions. The **only** difference is the commission
inside the expense ratio.

So any divergence between the two NAVs over time *is* the fee. Nothing else.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine two identical piggy banks, filled the same way, on the same days, for
thirteen years.

The only difference: one has a tiny hole in the bottom. Every day, a few
paise fall out.

You'd never notice a few paise. But leave it thirteen years and open both, and
one has noticeably less in it. Nothing was stolen dramatically — it leaked, so
slowly you couldn't see it happening.

The expense ratio is the hole. This post is about measuring it by weighing
both piggy banks.

</details>

## The formula

```
Value after N years = Initial × (1 + r − fee)^N

where r   = the portfolio's gross return
      fee = the expense ratio
```

The fee subtracts from the return *every year*, and the loss compounds — you
lose the fee, and also all the growth that fee would have produced.

## Two real comparisons

![Direct vs regular plans of the same funds]({{ '/assets/charts/mf-direct-vs-regular.svg' | relative_url }})

Source: [AMFI via mfapi.in]({{ f.source_url }}). Historical data, for illustration only.

**The index fund**, from {{ ei.start }} to {{ ei.end }} ({{ ei.years }} years):

| | Regular | Direct |
|---|---:|---:|
| CAGR | {{ ei.regular_cagr }}% | {{ ei.direct_cagr }}% |
| ₹1,00,000 grew to | ₹{{ ei.lumpsum_1lakh_regular }} | ₹{{ ei.lumpsum_1lakh_direct }} |

A gap of **{{ ei.gap_pp }} percentage points a year**, worth ₹{{ ei.lumpsum_difference }} — about {{ ei.difference_pct }}% more money
for doing nothing except buying the same fund a different way.

That's a modest number, and it's modest for a good reason: index funds are
already cheap, so there isn't much commission to remove. Which makes the
second comparison the instructive one.

**An actively managed fund** with a more typical expense ratio, from
{{ ea.start }} to {{ ea.end }} ({{ ea.years }} years):

| | Regular | Direct |
|---|---:|---:|
| CAGR | {{ ea.regular_cagr }}% | {{ ea.direct_cagr }}% |
| ₹1,00,000 grew to | ₹{{ ea.lumpsum_1lakh_regular }} | ₹{{ ea.lumpsum_1lakh_direct }} |

Here the gap is **{{ ea.gap_pp }} percentage points a year** — and on ₹1,00,000 over thirteen
years that comes to **₹{{ ea.lumpsum_difference }}**, or {{ ea.difference_pct }}% more money.

To be explicit about what this comparison is and isn't: the fund on both
sides of that table is the *same fund*. This post takes no view on whether it
is a good fund, and nothing here should be read as suggesting anyone buy or
avoid it. It appears because it has a normal actively-managed expense ratio
and thirteen years of both plans, which is what the arithmetic needed.

## Why 0.83% becomes 9.5%

The leap from "under one percent a year" to "₹74,000" is the part worth
sitting with, and it's just compounding running against you.

Each year you keep {{ ea.gap_pp }}% less. The following year, that missing amount isn't
there to grow either. Over thirteen years the shortfall compounds into
roughly a tenth of the final corpus — and over a thirty-year investing life
it would be far larger still.

A useful rough guide: over long periods, **each 1% of annual fee costs
roughly 20–25% of your final corpus over 30 years.** Not 1%. That's the
number worth carrying around.

## What you actually get for it

None of this makes fees illegitimate. Running a fund costs money, and active
management costs more than tracking an index. SEBI caps total expense ratios
on a sliding scale by fund size and type, and the caps are meaningful.

The honest questions are narrower:

- **For the regular-plan premium specifically**: are you receiving advice
  worth {{ ea.gap_pp }}% a year? If a distributor is genuinely planning, rebalancing and
  stopping you from panic-selling in a crash, that can be worth well more
  than the fee. If they sold you a fund once and haven't called since, it
  isn't.
- **For active management generally**: is the manager beating a comparable
  index by more than the extra fee, consistently? That's the subject of the
  benchmarks post later in this series.

Fees are only "high" or "low" relative to what they buy.

## Doing it in Python

```python
import pandas as pd

nav = pd.read_csv("uti-nifty50-index-fund-nav.csv",
                  parse_dates=["date"]).set_index("date")
start, end = pd.Timestamp("2013-01-02"), pd.Timestamp("2026-03-31")
years = (end - start).days / 365.25

for plan in ["nav_regular_growth", "nav_direct_growth"]:
    s = nav[plan].dropna()
    cagr = ((s.asof(end) / s.asof(start)) ** (1/years) - 1) * 100
    print(f"{plan:20s} CAGR {cagr:.3f}%  "
          f"Rs 1,00,000 -> Rs {100000 * s.asof(end)/s.asof(start):,.0f}")
```

## Common mistakes

- **Thinking the expense ratio is charged separately.** It's already inside
  every NAV, which is what makes it so easy to ignore.
- **Dismissing a 1% fee as small.** Over thirty years it's a fifth to a
  quarter of the final corpus.
- **Holding regular plans by inertia.** Many people bought regular plans
  before direct existed, or without knowing the choice existed. Switching
  has tax consequences worth checking, but the ongoing cost is worth knowing.
- **Assuming direct is automatically right.** Direct means no advice. If
  advice is what stops you selling at the bottom of a 60% drawdown, it may
  be the best money you spend — just pay for it knowingly.
- **Comparing expense ratios across categories.** Index funds, active equity
  and debt funds have structurally different cost bases and different caps.
- **Ignoring exit loads and taxes when switching.** Moving from regular to
  direct is a redemption and a fresh purchase, with the tax that implies.

**Takeaway:** The expense ratio is deducted from NAV daily, so you never see
it — but comparing a fund's direct and regular plans isolates it exactly,
since everything else about them is identical. On an actively managed fund
that gap was {{ ea.gap_pp }}% a year, which over thirteen years came to {{ ea.difference_pct }}% of the
final corpus. Small annual percentages are not small.
