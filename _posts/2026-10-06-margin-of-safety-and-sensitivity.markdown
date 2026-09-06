---
layout: post
title: "Margin of safety: what to do with a valuation you don't fully trust"
description: "A DCF gives a number to two decimals and supports a range. Sensitivity tables, margin of safety, and what to do with a valuation you don't fully trust."
image: /assets/og/margin-of-safety-and-sensitivity.png
date: 2026-10-06 09:00:00 +0530
series: fundamental-analysis
---

{% assign dcf = site.data.case_study.dcf %}
{% assign r = dcf.result %}
{% assign s = dcf.sensitivity %}

## A false sense of precision

The [last post]({% post_url 2026-10-05-terminal-value-and-the-full-dcf %}) ended with a
value of ₹{% include inr.html n=r.value_per_share %} a share for Desi Bites. Two decimal places. It looks like a
measurement.

It isn't. It's the output of a chain of estimates — a growth rate that fades
on a schedule someone chose, a
[margin path]({% post_url 2026-10-04-forecasting-free-cash-flow %}) someone assumed, a beta borrowed
from a sector, an equity risk premium that reasonable people put anywhere in
a two-point range, and a perpetual growth rate for a company that will
outlive everyone reading this. Every one of those is arguable. The
spreadsheet reports ₹{% include inr.html n=r.value_per_share %} because spreadsheets always report something.

This post is about the two habits that keep a discounted cash flow (DCF)
model honest: showing how much
the answer moves when the inputs move, and refusing to act on the answer
unless there's room to be wrong.

## Sensitivity: show the range, not the point

A sensitivity table re-runs the model across a grid of assumptions and prints
every answer. The two inputs worth gridding are almost always WACC and
terminal growth, because those two do the most damage.

Value per share (₹) for Desi Bites, at varying discount rates and perpetual
growth rates:

| WACC ↓ / g → |{% for c in s.terminal_growth_cols %} {{ c }}% |{% endfor %}
|---|{% for c in s.terminal_growth_cols %}---:|{% endfor %}{% for row in s.rows %}
| {{ row.wacc }}% |{% for v in row.values %} {{ v }} |{% endfor %}{% endfor %}

The base case sits in the middle at ₹{% include inr.html n=r.value_per_share %}. But move one percentage point
in each direction on both inputs — a range no analyst would call
unreasonable — and the answer runs from about **₹334 to ₹525**. The high end
is 57% above the low end.

That's the honest output of this model. Not ₹{% include inr.html n=r.value_per_share %}, but "somewhere in the
high 300s to low 400s if my central assumptions hold, and plausibly ₹330 to
₹525 across assumptions I can't rule out."

A range is less satisfying than a number. It's also true, which is the better
property for something you're about to risk money on.

## Which assumptions actually matter

Not every input deserves equal worry. Rough sense of what moves the Desi
Bites valuation, in order:

| Assumption | Impact | Why |
|---|---|---|
| Terminal growth rate | Very high | Sits in the denominator of {{ r.terminal_pct_of_ev }}% of the value |
| WACC | Very high | Compounds through every year, and hits terminal value twice |
| Revenue growth path | High | Drives every downstream line in the forecast |
| [EBITDA]({% post_url 2026-08-28-ebitda-margin %}) margin path | High | A point of margin on ₹5,000 Lakh of revenue is real money |
| Capex intensity | Medium | Large in the forecast years, fades in importance by the terminal year |
| Working capital % | Low | Only the *change* matters, and it's small relative to everything else |
| Tax rate | Low | Fairly well known, doesn't move much |

The pattern is worth noticing: the assumptions with the most influence are
also the hardest to defend. Tax rates are knowable. Perpetual growth rates
are not. Precision and importance run in opposite directions here, which is
the fundamental awkwardness of the whole exercise.

## Margin of safety

If a valuation is a range rather than a number, acting only when the price
sits at the *bottom* of the plausible range gives you room to be wrong. That
buffer is the **margin of safety** — an idea from Benjamin Graham, and
probably the single most durable concept in fundamental analysis.

```
Margin of Safety (%) = (Intrinsic Value − Price) / Intrinsic Value × 100
```

The logic is defensive rather than clever. Your model *will* be wrong; the
question is only by how much and in which direction. A price well below your
estimated value means you can be substantially mistaken and still not lose
money. A price at or above it means every one of your assumptions has to come
good just to break even.

How large a buffer? There's no formula, and anyone offering one is
overselling. The sensible principle is that the buffer should scale with your
uncertainty:

| Situation | Buffer typically wanted |
|---|---|
| Stable, predictable business; long track record | Smaller |
| Cyclical, or a short operating history | Larger |
| Model leans heavily on terminal value | Larger |
| Sensitivity table shows a wide range | Larger |

Desi Bites hits three of those four. It's a small-cap with three years of
audited accounts, {{ r.terminal_pct_of_ev }}% of its value sits in the terminal value, and the
sensitivity range spans ₹334 to ₹525. That combination argues for a wide
buffer, whatever number you'd normally use.

## Where margin of safety gets misused

Two failure modes, both common.

The first is **treating the buffer as a substitute for understanding the
business**. A 50% discount to a valuation built on assumptions you can't
defend isn't safety, it's a bigger bet on a worse model. Graham's buffer was
meant to absorb ordinary estimation error, not to compensate for not knowing
what a company does.

The second is **assuming a gap between price and value must be an
opportunity**. Sometimes the market knows something the model doesn't — a
customer concentration risk, a promoter dispute, a regulatory change working
its way through. When the market disagrees with your model, "I'm right and
they're wrong" is one explanation, and it's rarely the first one to reach
for. The reverse DCF from the last post is the better instinct: work out what
the price is assuming, then go and check whether that assumption is
defensible.

## Common mistakes

- **Reporting a DCF as a single number.** If you've built the model you've
  already got the sensitivity grid — it's the same code in a loop. Publishing
  a point estimate while sitting on a range is a choice to look more certain
  than you are.
- **Tuning assumptions until the model agrees with the price.** The most
  seductive error in valuation, because the result feels like confirmation.
  It's the opposite: you've fitted the answer to the data. If you catch
  yourself nudging terminal growth to close a gap, stop.
- **Using a wide margin of safety to justify a business you don't
  understand.** The buffer covers estimation error, not ignorance.
- **Applying the same buffer to every company.** A predictable business with
  twenty years of stable cash flows and a loss-making three-year-old startup
  do not warrant the same discount.
- **Forgetting the model can be wrong in the good direction.** Sensitivity
  cuts both ways, and a business that outperforms your fade assumption is
  worth more than your model says. Margin of safety is about surviving errors,
  not about assuming the worst case is the true case.
- **Believing precision equals accuracy.** ₹{% include inr.html n=r.value_per_share %} is precise. Whether it's
  accurate depends entirely on assumptions no spreadsheet can check.

**Takeaway:** A DCF produces a number, but what it actually supports is a
range — so run the sensitivity grid and quote the range, because that's the
honest output. Then insist on a gap between price and value big enough to
absorb the fact that you'll be wrong about something. The margin of safety
isn't a way of being cleverer than the market; it's an admission that you
won't be.
