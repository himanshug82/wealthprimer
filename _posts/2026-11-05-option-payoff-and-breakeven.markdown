---
layout: post
title: "Option payoff and breakeven, worked step by step"
description: "How to work out an option's breakeven and payoff at expiry for a call and a put, and why a lower-premium out-of-the-money option needs a bigger move."
image: /assets/og/option-payoff-and-breakeven.png
date: 2026-11-05 09:00:00 +0530
series: risk
term: "Breakeven (options)"
---

{% assign r = site.data.risk3 %}
{% assign c = r.contract %}
{% assign be = r.breakeven %}

## What breakeven means for an option

The **breakeven** of an option is the index level at expiry at which the
buyer's profit or loss is exactly zero, after the premium. Below it (for a
call) the buyer is behind, even if the option finishes with some payoff,
because the payoff has not yet repaid the premium. It is the first number to
compute for any option, because it turns "the index has to go up" into a
specific level.

This post uses the same hypothetical Sample Index as the
[call and put post]({{ '/2026/11/04/call-and-put-options/' | relative_url }}): a
level of {{ c.level }}, a lot of {{ c.lot }} units, and premiums priced from a
simple teaching model ({{ r.time_value.days }} days to expiry, {{ r.time_value.vol_pct }}% annual volatility; see the
[time value post]({{ '/2026/11/06/option-time-value/' | relative_url }})). Nothing
here is a market quote. It sits in
[Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}).

## The formula

```
Call:  breakeven  =  strike  +  premium
Put:   breakeven  =  strike  −  premium

Move needed (%)  =  ( breakeven / current level  −  1 )  ×  100

Profit or loss at expiry  =  ( payoff  −  premium )  ×  lot size
    payoff, call = max(S − K, 0)       payoff, put = max(K − S, 0)
```

## Worked example: an at-the-money pair and an out-of-the-money pair

An option whose strike equals the current level is **at the money**. A call
whose strike is *above* the current level, or a put whose strike is *below*
it, would have no payoff if expiry were today: it is **out of the money**.
Premiums are in index points and are rounded to whole points in this post
(the time value and implied volatility posts show one decimal, so a premium of
{{ c.call_prem }} here is {{ r.time_value.rows[0].atm_price }} there).

| Option | Strike | Premium (points) | Premium per lot (₹) | Breakeven | Move needed from {{ c.level }} |
|---|---:|---:|---:|---:|---:|
| Call, at the money | {{ c.strike }} | {{ c.call_prem }} | {{ c.call_prem_rs }} | {{ be.atm.call_be }} | {{ be.atm.call_be_move_pct }}% |
| Put, at the money | {{ c.strike }} | {{ c.put_prem }} | {{ c.put_prem_rs }} | {{ be.atm.put_be }} | {{ be.atm.put_be_move_pct }}% |
| Call, out of the money | {{ be.otm.call_strike }} | {{ be.otm.call_prem }} | {{ be.otm.call_prem_rs }} | {{ be.otm.call_be }} | {{ be.otm.call_be_move_pct }}% |
| Put, out of the money | {{ be.otm.put_strike }} | {{ be.otm.put_prem }} | {{ be.otm.put_prem_rs }} | {{ be.otm.put_be }} | {{ be.otm.put_be_move_pct }}% |

The steps for the at-the-money call:

1. **Breakeven.** {{ c.strike }} + {{ c.call_prem }} = {{ be.atm.call_be }} points.
2. **Move needed.** {{ be.atm.call_be }} ÷ {{ c.level }} − 1 = {{ be.atm.call_be_move_pct }}%.
3. **Check.** At an expiry level of {{ be.atm.call_be }} the payoff is
   {{ c.call_prem }} points, equal to the premium, so profit or loss is zero.

Two things stand out in the table. The out-of-the-money options cost less per
lot, but their breakevens are further away; "lower-priced" and "closer to
paying off" are different things. And the at-the-money call and put are
exactly symmetrical here (a {{ be.atm.call_be_move_pct }}% move either way) because the model has zero
interest and dividends, which makes their premiums equal. The out-of-the-money
pair is only nearly symmetrical ({{ be.otm.call_be_move_pct }}% and {{ be.otm.put_be_move_pct }}%): the model's prices are
not evenly spread around the current level, so the two premiums differ
({{ be.otm.call_prem }} and {{ be.otm.put_prem }} points). Real quotes differ again.

For each lot, the loss if the option expires with no payoff is the whole
premium: ₹{% assign p1 = c.call_prem_rs %}{% include inr.html n=p1 %} for the at-the-money call, ₹{% assign p2 = be.otm.call_prem_rs %}{% include inr.html n=p2 %} for the
out-of-the-money one.

## Common mistakes

- **Using the strike as the breakeven.** The strike is where the payoff
  starts; the breakeven is where the *profit* starts. They differ by exactly
  the premium.
- **Reading a lower premium as a lower risk.** The out-of-the-money option
  risks less money per lot, but needs a bigger move to break even, so a loss
  of the entire premium covers more of the possible index levels. The table
  is arithmetic, not a forecast, and gives no probabilities.
- **Computing breakeven on the premium alone.** Brokerage, exchange charges
  and tax are real costs and move the true breakeven further out. They are
  left out here to keep the arithmetic clean; check a contract note for the
  actual figures.

**Takeaway:** An option's breakeven is its strike plus the premium for a call, or its strike minus the premium for a put, and it is the level the index must pass before the buyer is ahead. A lower-premium out-of-the-money option has a lower premium but a more distant breakeven, so the amount at risk is smaller while the move needed is larger.
