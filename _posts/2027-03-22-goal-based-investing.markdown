---
layout: post
title: "Goal-based investing: the arithmetic of a future cost"
description: "Goal-based investing works back from a future cost to a monthly sum. Inflating the cost, the SIP formula, a sensitivity grid, and what a lower return does."
image: /assets/og/goal-based-investing.png
date: 2027-03-22 09:00:00 +0530
series: money-before-markets
term: "Goal-based investing"
---

{% assign g = site.data.mbm2.goal %}
{% assign b6 = g.by_return[0] %}
{% assign b8 = g.by_return[1] %}
{% assign b10 = g.by_return[2] %}
{% assign b12 = g.by_return[3] %}

## What goal-based investing means

**Goal-based investing** starts from what the money is for. Instead of "how
much can I put away?", it asks: this cost, this many years away, what monthly
amount gets there under stated assumptions? Each goal then gets its own
sum, its own [investment horizon]({% post_url 2027-03-17-investment-horizon %})
and, often, its own [asset allocation]({% post_url 2027-03-19-asset-allocation %}).

The arithmetic is simple. What makes it useful is seeing how much the answer
moves when the assumptions move, which is most of this post. It's part of
[Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}).

## The formula

Three steps, each one a [compounding]({% post_url 2027-03-12-compounding-and-time %}) calculation:

```
1. Future cost       =  cost today × (1 + inflation) ^ years

2. Lump sum today    =  future cost / (1 + return) ^ years

3. Monthly amount    =  future cost / FV of ₹1 a month
   where FV of ₹1 a month  =  Σ (1 + m) ^ k  for k = 1 … months,
   m = (1 + yearly return) ^ (1/12) − 1, each instalment paid at the start of the month
```

FV is future value. The monthly amount is a SIP (systematic investment plan): a fixed sum
invested every month. The return is the steady rate you assume the money
earns; inflation is how fast the cost itself rises.

## Worked example: a ₹{% include inr.html n=g.cost_today %} cost, {{ g.years }} years away

Every number here is an assumption, chosen to show the method. None is a
forecast, and the returns are not what any investment will earn.

**Step 1, the future cost.** A cost of
₹{% include inr.html n=g.cost_today %} today, rising {{ g.inflation_pct | replace: "-", "−" }}%
a year for {{ g.years }} years, becomes
₹{% include inr.html n=g.future_cost %}.

**Steps 2 and 3, at four assumed returns:**

| Assumed return a year | Lump sum needed today (₹) | Monthly amount (₹) | Monthly amount in year 1, rising {{ g.step_up_pct | replace: "-", "−" }}% a year (₹) |
|---:|---:|---:|---:|
{% for r in g.by_return -%}
| {{ r.return_pct | replace: "-", "−" }}% | {{ r.lump_today }} | {{ r.monthly }} | {{ r.monthly_stepup }} |
{% endfor %}

The first row is a useful check: when the assumed return equals inflation
({{ g.inflation_pct | replace: "-", "−" }}%), the lump sum needed today is exactly today's cost.
The money only keeps pace.

The last column is a step-up SIP, which the
[step-up SIP post]({% post_url 2026-10-25-step-up-sips %}) explains. At
{{ g.base_return_pct | replace: "-", "−" }}%, it starts at
₹{% include inr.html n=g.step_first %} a month and ends at
₹{% include inr.html n=g.step_last %} in year {{ g.years }}. In total it
puts in ₹{% include inr.html n=g.step_paid %}, against
₹{% include inr.html n=g.flat_paid %} for the flat
₹{% include inr.html n=g.base_monthly %} a month: a smaller start, a bigger
total.

### How the answer moves with the assumptions

Monthly amount needed (₹), for each pair of assumptions:

| Inflation ↓ / return → | Future cost (₹) | {{ g.returns_pct[0] }}% | {{ g.returns_pct[1] }}% | {{ g.returns_pct[2] }}% | {{ g.returns_pct[3] }}% |
|---|---:|---:|---:|---:|---:|
{% for s in g.sensitivity -%}
| {{ s.inflation_pct | replace: "-", "−" }}% | {{ s.future_cost }} | {{ s.monthly[0] }} | {{ s.monthly[1] }} | {{ s.monthly[2] }} | {{ s.monthly[3] }} |
{% endfor %}

One point of inflation moved the answer by nearly as much as two points of
return did in the other direction. Assumptions that look small are not small
over {{ g.years }} years.

{% include tool.html id="goal" embed=true note="It starts from the example above; change any assumption to see how far the answer moves." %}

### What if the return comes in lower?

Say the plan assumed {{ g.base_return_pct | replace: "-", "−" }}% and set
₹{% include inr.html n=g.base_monthly %} a month. If the money actually earns
{{ g.shortfall_return_pct | replace: "-", "−" }}% a year, it reaches
₹{% include inr.html n=g.shortfall_corpus %}: {{ g.shortfall_share_pct | replace: "-", "−" }}%
of the goal, short by ₹{% include inr.html n=g.shortfall_gap %}. Real
returns aren't steady either, so the actual shortfall, or surplus, depends on
the order of the years too; the
[sequence-of-returns post]({% post_url 2026-10-13-sequence-of-returns-risk %})
shows how much order matters.

## Common mistakes

1. **Planning for today's price.** Leaving out inflation understates the
   target. Here the cost roughly doubles in {{ g.years }} years at
   {{ g.inflation_pct | replace: "-", "−" }}%.
2. **Using one return as if it were known.** The table gives four answers
   because the return is unknown. A plan built on the highest one has the
   least room for a bad decade.
3. **Using an equity-like return for a short goal.** The return it's
   reasonable to assume depends on what the money is held in. The
   [investment horizon post]({% post_url 2027-03-17-investment-horizon %})
   shows how often each asset lost money over short windows.
4. **Setting it once.** Costs, income and markets change. Re-running the
   three steps every year or so, with the money already saved as a lump sum,
   shows whether the plan is on track.

**Takeaway:** Goal-based investing turns a future cost into a monthly
number in three steps: inflate the cost, then work back at an assumed return.
The answer is only as good as those two assumptions, so the useful output is
the range, not the single figure.
