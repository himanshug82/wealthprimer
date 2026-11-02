---
layout: post
title: "Futures basis and cost of carry: why futures usually trade above spot"
seo_title: "Futures basis and cost of carry explained"
description: "The basis is the futures price minus spot. How cost of carry sets it, why it shrinks to zero at expiry, and what a dividend does, on an invented example."
image: /assets/og/futures-basis-and-cost-of-carry.png
date: 2027-02-26 09:00:00 +0530
series: jargon
term: "Futures basis (cost of carry)"
---

{% assign f = site.data.jargon_m9.futures %}

## What is the basis?

A **futures contract** is an agreement to buy or sell something at a set price on a set future date. The **spot price** is today's price for immediate delivery. The **basis** is the futures price minus the spot price. Futures usually trade a little *above* spot, and that gap is explained by the **cost of carry**: what it costs to hold the underlying until the futures date (mainly the interest on the money tied up), less anything the holder earns meanwhile (such as a dividend).

This post uses an **invented** example, not a live quote, and it describes how pricing works rather than suggesting any trade. It builds on [open interest]({% post_url 2026-11-12-open-interest %}), [short selling]({% post_url 2027-01-17-short-selling-mechanics %}) and [leverage and margin]({% post_url 2026-10-11-leverage-and-margin %}), and is part of the [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}) series.

## The formula

```
Theoretical futures price  =  Spot × (1 + r × days / 365)  −  dividends due before expiry

Basis               =  Futures price − Spot price
```

`r` is the annual interest rate for the period (a simple, non-compounded rate keeps the arithmetic visible). The logic is **arbitrage**, buying one thing and selling a linked thing to lock in a gain: if the futures price were much higher than this theoretical value, someone could buy the underlying now, sell the futures, and hold to the date for a gain beyond their financing cost. If it were much lower, the reverse, which is harder because holding a short beyond the day needs borrowed shares. Such trades push the futures price toward the fair value. Real prices differ from this by costs, margins and constraints that the formula leaves out.

## Worked example: an invented underlying

Spot ₹{% assign sp = f.spot | round %}{% include inr.html n=sp %}, interest rate {{ f.rate_pct | round }}% a year, no dividends. How the theoretical futures price and the basis change with days left:

| Days to expiry | Theoretical futures price (₹) | Basis (₹) | Basis as % of spot |
|---:|---:|---:|---:|
{% for r in f.rows %}| {{ r.days_left }} | {{ r.fair_futures }} | {{ r.basis }} | {{ r.basis_pct }}% |
{% endfor %}
Two things to notice:

1. **The basis shrinks to zero at expiry.** At expiry, the futures contract is an agreement to deal today, so its price equals spot. This is called **convergence**. It doesn't by itself say anything about price direction, since spot could rise to meet futures. What ties a premium to carry is the arbitrage above, which is why a futures price above spot needn't signal any view.
2. **In this formula the basis is a financing charge.** With {{ f.rate_pct }}% a year, a month of carry is about {{ f.rows[0].basis_pct }}% of spot, which is the {{ f.rate_pct }}% rate scaled to the period. Real gaps also reflect the frictions listed under common mistakes.

Now add a dividend of ₹{{ f.dividend | round }} due before the 30-day expiry. The holder of the underlying would receive it, the futures holder would not, so the theoretical price falls by that amount: ₹{{ f.fair_with_dividend }}, a basis of {% assign bd = f.basis_with_dividend %}−₹{{ bd | abs }}. The basis can be **negative**, with futures below spot, when the expected dividends exceed the financing cost. Such a negative basis is also called backwardation.

## Common mistakes

- **Reading a futures premium as a forecast.** Arbitrage ties a positive basis to carrying cost, so it needn't signal a view on price.
- **Comparing futures prices of different expiries without adjusting.** The near-month basis is smaller than the far-month basis by the extra days of carry, before dividends.
- **Forgetting dividends.** Around dividend dates, the basis moves for reasons that have nothing to do with market direction.
- **Treating the formula as a price you can trade at.** Real futures prices also reflect margin requirements, costs and demand for leverage, so they sit around the theoretical value and not exactly on it.

**Takeaway:** The futures basis is the futures price minus the spot price, and in theory it is the cost of carrying the underlying (interest less dividends). Arbitrage ties the premium to that cost, so it needn't signal any view on price.
