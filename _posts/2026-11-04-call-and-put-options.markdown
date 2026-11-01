---
layout: post
title: "Call and put options: what a buyer pays and risks"
description: "A call is the right to buy, a put the right to sell, for a premium paid upfront. Hypothetical index: lot, premium, payoffs and the buyer's maximum loss."
image: /assets/og/call-and-put-options.png
date: 2026-11-04 09:00:00 +0530
series: risk
term: "Option (call and put)"
---

{% assign r = site.data.risk3 %}
{% assign c = r.contract %}

## What a call option and a put option are

An **option** is a contract that gives its buyer the *right, but not the
obligation*, to trade an **underlying** (here, an index) at a fixed price
called the **strike**, at or by a set date called the **expiry**. A **call**
is the right to *buy*; a **put** is the right to *sell*. The buyer pays a
price for that right, the **premium**, and pays it upfront. Whoever sells the
option takes the other side and receives the premium; a later post
in this module, on [writing options]({{ '/2026/11/08/option-writing-and-margin/' | relative_url }}),
covers that side.

This module is about mechanics, in the series
[Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}). It
does not suggest any position. Everything below uses a **hypothetical** index,
the "Sample Index", not a real one. The premium numbers come from a
simple teaching model (explained in the
[time value post]({{ '/2026/11/06/option-time-value/' | relative_url }})), not
from any exchange quote.

| Term | What it means here |
|---|---|
| Underlying | The Sample Index, at {{ c.level }} points |
| Strike | The fixed price in the contract: {{ c.strike }} points |
| Lot | Options trade in fixed bundles. One lot here is {{ c.lot }} units of the index |
| Premium | The price of the option, quoted in index points, paid per unit |
| Expiry | The date the contract ends. Past it, the option is worthless |

## The formula

At expiry, with `S` the index level on the day and `K` the strike:

```
Call buyer, profit or loss  =  ( max(S − K, 0)  −  premium )  ×  lot size
Put buyer,  profit or loss  =  ( max(K − S, 0)  −  premium )  ×  lot size

Most a buyer can lose       =  premium  ×  lot size
```

The `max(…, 0)` is the "right, not obligation": if using the right would be
worth less than nothing, the buyer simply lets the option lapse and the
payoff is zero. The premium, though, has already gone.

## Worked example: one lot of the Sample Index

One lot is {{ c.lot }} units. At {{ c.level }} points, one lot controls
{% assign cv = c.value %}₹{% include inr.html n=cv %} of the index (the *contract value*). Both
options below have the same strike, {{ c.strike }}, and a premium of
{{ c.call_prem }} points each.

1. **Premium in rupees.** {{ c.call_prem }} points × {{ c.lot }} units =
   {% assign pr = c.call_prem_rs %}₹{% include inr.html n=pr %} per lot, paid on the day the option is bought.
2. **Premium against what it controls.** ₹{% include inr.html n=pr %} is
   {{ c.prem_share_pct }}% of the ₹{% include inr.html n=cv %} contract value.
   That ratio is where options get their leverage, and the previous
   [leverage and margin post]({% post_url 2026-10-11-leverage-and-margin %})
   showed what multiplying a move does in both directions.
3. **The payoff at expiry** for each index level:

| Index at expiry | Move from {{ c.level }} | Call payoff | **Call buyer's profit or loss** | Put payoff | **Put buyer's profit or loss** |
|---:|---:|---:|---:|---:|---:|
{% for row in r.buyer.table -%}
| {{ row.level }} | {{ row.move_pct }}% | {{ row.call_payoff }} | **{{ row.call_pl }}** | {{ row.put_payoff }} | **{{ row.put_pl }}** |
{% endfor %}

All amounts are in rupees per lot, for a hypothetical option. Read the call
column from top to bottom: the loss stops at the premium
(₹{% include inr.html n=pr %}) no matter how far the index falls, while the
profit keeps growing as the index rises. The put column is the mirror
image. The index has to move past the strike by *more than the premium*
before the buyer is ahead; the
[next post]({{ '/2026/11/05/option-payoff-and-breakeven/' | relative_url }}) works out
that point.

### What the rules say about size and payment

Two rules from SEBI (the Securities and Exchange Board of India), both from its
circular SEBI/HO/MRD/TPD-1/P/CIR/2024/132 dated 1 October 2024, as read on
1 November 2026:

- **Contract size.** A new index derivative contract must have a value of at
  least ₹{% assign mn = c.sebi_min %}{% include inr.html n=mn %} when it is introduced, and its lot size is to be fixed so that the
  contract value on the review day falls between ₹{% include inr.html n=mn %}
  and ₹{% assign mx = c.sebi_max %}{% include inr.html n=mx %} (paragraph 5.4.1; effective for new contracts after 20 November
  2024). The hypothetical lot above is built to sit inside that band. The
  actual lot size of any real contract is set by the exchange, so check the
  exchange's current contract specification.
- **Upfront premium.** Trading members must collect the option premium
  upfront from the option buyer (paragraph 5.1; effective 1 February 2025).
  The circular's stated reason is that option prices move in a non-linear way
  and carry "very high implicit leverage".

## Common mistakes

- **Reading "the most I can lose is the premium" as "the loss is small".**
  The cap is real, but a loss of the *whole* premium is a 100% loss of the
  money put in. In the table above the call buyer loses all of it at every
  index level at or below the strike. A limited loss can still be a complete
  one.
- **Forgetting the lot.** A premium is quoted per unit, in points. The
  rupees come from multiplying by the lot size, which is why ₹{% include inr.html n=pr %}
  here is {{ c.lot }} times the quoted {{ c.call_prem }}.
- **Ignoring the premium when counting a "win".** An index that finishes just
  above the strike gives a positive payoff but still a loss to the call
  buyer, because the payoff is smaller than the premium paid. The table shows
  the payoff and the profit side by side for exactly this reason.
- **Treating the table as odds.** A payoff table shows what happens at each
  level, not how likely each level is. SEBI's studies of individual traders
  in this segment, covered in the
  [F&O numbers post]({% post_url 2026-10-08-what-the-fo-numbers-actually-say %}),
  are the evidence on how buyers actually fared.

**Takeaway:** An option buyer pays a premium upfront for the right to buy (call) or sell (put) at a fixed strike, and the most the buyer can lose is that premium (the quoted points times the lot size). The premium is spent on day one, whether or not the option ends up worth anything.

*Educational only: the Sample Index and its premiums are hypothetical, and
nothing here is a recommendation to buy or sell any option. How income and
losses from derivatives are taxed is in the
[Tax series]({{ '/2026/11/13/fo-is-business-income/' | relative_url }}).*
