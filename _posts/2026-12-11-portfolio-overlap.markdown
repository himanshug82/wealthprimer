---
layout: post
title: "Portfolio overlap: why two funds can be one fund"
description: "Four large-cap funds feel diversified. The overlap formula — sum the smaller weight of every shared holding — shows how much of them is one portfolio."
image: /assets/og/portfolio-overlap.png
date: 2026-12-11 09:00:00 +0530
series: mutual-funds
term: "Portfolio overlap"
---

{% assign o = site.data.mf2.overlap %}

## The diversification you think you have

A common Indian portfolio: one large-cap fund, one flexi-cap fund, one
"bluechip" fund, and an index fund, from four different fund houses. Four
funds, four managers, four factsheets. It *feels* diversified.

Open the four factsheets side by side and the same ten company names appear
in every one, near the top, at similar weights. Because every large-cap fund
must hold [at least 80% of its assets in the top 100 companies]({% post_url 2026-12-10-sebi-fund-categories-decoded %}),
and the top 100 is dominated by the same handful of banks, IT firms and
conglomerates, there are only so many ways to build one.

**Portfolio overlap** puts a number on how much of two funds is the same
fund.

## The formula

For every stock held by both funds, take the *smaller* of the two weights.
Add them up.

```
Overlap (%)  =  Σ  min( weight in Fund A ,  weight in Fund B )
              over every stock held by both
```

The logic: if Fund A has 9% in a stock and Fund B has 8%, then 8% of each
portfolio is unarguably "the same position". The extra 1% in Fund A is
genuinely different exposure. Do that for every common holding and the total
is the share of the two portfolios that is interchangeable.

Overlap of 0% means no common holdings. Overlap of 100% means identical
portfolios — which is exactly what two index funds on the same index have.

## Worked example: two hypothetical large-cap funds

Both portfolios below are **invented** — the point is the arithmetic, and no
real fund's holdings are used. Each shows its top ten positions.

| Stock | Fund A weight | Fund B weight | Held by both? | Counts toward overlap |
|---|---:|---:|:---:|---:|{% for k in o.portfolio_a %}{% assign name = k[0] %}{% assign wa = k[1] %}{% assign wb = o.portfolio_b[name] %}
| {{ name }} | {{ wa }}% | {% if wb %}{{ wb }}%{% else %}— {% endif %} | {% if wb %}Yes{% else %}No{% endif %} | {% if wb %}{% if wa < wb %}{{ wa }}{% else %}{{ wb }}{% endif %}%{% else %}0%{% endif %} |{% endfor %}{% for k in o.portfolio_b %}{% assign name = k[0] %}{% unless o.portfolio_a[name] %}
| {{ name }} | — | {{ k[1] }}% | No | 0% |{% endunless %}{% endfor %}

The last four rows are stocks only Fund B holds. Summing the last column:

| Common holding | min(A, B) |
|---|---:|{% for r in o.common_holdings %}
| {{ r.stock }} | {{ r.min_weight }}% |{% endfor %}
| **Overlap** | **{{ o.overlap_pct }}%** |

So a little over a third of these two "different" funds is the same
portfolio — from their top tens alone. Extend the comparison to all forty or
fifty holdings and the figure for two real large-cap funds can easily exceed
half.

Notice also the top-ten concentration: {{ o.top10_weight_a }}% of Fund A and {{ o.top10_weight_b }}% of
Fund B sit in just ten names. Large-cap funds are concentrated by
construction, because the index they're measured against is — the Nifty 50's
ten largest constituents make up more than half of it (check the current
weights on NSE's index factsheet; they move).

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Two friends each pack a lunchbox with ten things. You compare them: both have
an apple, both have a sandwich, both have a juice, both have a biscuit. Only
the last few items differ.

If you ate from both boxes thinking "two lunches, lots of variety", you'd
mostly be eating the same lunch twice. Overlap is just counting how much of
the two boxes is the same food.

</details>

## Why overlap matters — and when it doesn't

**What high overlap costs you.** If two funds are 60% the same portfolio, the
second fund adds only 40% new exposure, but you pay its full expense ratio on
all of it. And when
the shared holdings fall, both funds fall together — the second fund adds
paperwork, not protection. The
[expense ratio post]({% post_url 2026-10-21-expense-ratios-direct-vs-regular %})
showed how much a fraction of a percent compounds to; paying it twice for the
same stocks is the easiest waste to eliminate.

**When overlap is fine.** Between an index fund and a large-cap fund, high
overlap is expected and harmless *if you meant it* — you may hold the active
fund for the 20% that is different. The problem isn't overlap; it's overlap
you didn't know about.

**What overlap doesn't measure.** Two funds can hold entirely different stocks
and still move together, because they hold the same *kind* of stock — two
small-cap funds with zero common holdings will both fall 40% in a small-cap
sell-off. Overlap catches duplicated positions, not duplicated *risk*. For
that you need correlation of returns, which is a different tool.

## Doing it in Python

Given two dictionaries of holdings and weights:

```python
fund_a = {"Stock A": 9.5, "Stock B": 8.0, "Stock C": 7.5, "Stock D": 6.0,
          "Stock E": 5.5, "Stock F": 5.0, "Stock G": 4.5, "Stock H": 4.0,
          "Stock I": 3.5, "Stock J": 3.0}
fund_b = {"Stock A": 8.0, "Stock B": 9.0, "Stock C": 4.0, "Stock D": 6.5,
          "Stock E": 3.0, "Stock K": 6.0, "Stock L": 5.0, "Stock F": 5.5,
          "Stock M": 4.5, "Stock N": 4.0}

common = set(fund_a) & set(fund_b)
overlap = sum(min(fund_a[s], fund_b[s]) for s in common)
print(f"{len(common)} common holdings, overlap {overlap:.1f}%")
```

AMCs publish full monthly portfolio disclosures (as a PDF or spreadsheet on the
fund house's site; factsheets usually show only the top holdings), so the same twelve lines work on real funds — type the weights
in, or paste them from the disclosure file.

## Common mistakes

- **Counting funds instead of holdings.** Four large-cap funds from four fund
  houses can be one portfolio held four times.
- **Diversifying across fund houses rather than across what the funds own.**
  The fund house's name has no bearing on which fifty stocks the mandate
  allows.
- **Treating low overlap as low correlation.** Two small-cap funds with no
  shared stocks still share the small-cap cycle.
- **Ignoring the index fund in the mix.** If you hold a Nifty 50 index fund,
  every large-cap fund you add is substantially the same exposure again.
- **Checking once.** Portfolios drift; overlap that was 40% at purchase can be
  65% two years later. Re-run it when factsheets refresh.

**Takeaway:** Portfolio overlap is the sum, over every shared holding, of the
smaller of the two funds' weights — and for two large-cap funds it can easily
exceed half, because the mandate leaves few ways to build one. Two funds with
60% overlap aren't diversification; they're one portfolio with two expense
ratios.
