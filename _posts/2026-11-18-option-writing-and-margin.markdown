---
layout: post
title: "Writing options: capped gain, large loss, margin"
description: "An option writer keeps the premium but takes the other side of the buyer's payoff. A hypothetical index shows the capped gain, uncapped loss and margin."
image: /assets/og/option-writing-and-margin.png
date: 2026-11-18 09:00:00 +0530
series: risk
term: "Option writing"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign r = site.data.risk3 %}
{% assign c = r.contract %}
{% assign w = r.writing %}
{% assign s = r.sources %}
{% assign f = site.data.fno.fy26_unverified %}

## What writing an option means

**Option writing** (also called *selling* an option) means taking the other side of the buyer's
contract. The writer receives the premium on day one and, in exchange,
accepts an obligation: if the buyer uses the option, the writer must pay the
payoff. Where the
[call and put post]({{ '/2026/11/06/call-and-put-options/' | relative_url }})
looked at what a buyer pays and risks, this post is the mirror image, and
it is why the position needs **margin**: money the writer must keep deposited
with the broker because the possible loss is far larger than the premium
received.

This is a description of the arithmetic, not a suggestion to take either side.
It is part of the options module in
[Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}), on the
same hypothetical Sample Index at {{ c.level }}, with a lot of {{ c.lot }}
units and a contract value of ₹{% assign cv = c.value %}{% include inr.html n=cv %}.

## The formula

At expiry, with `S` the index level and `K` the strike. This is the buyer's
formula from the earlier post with the sign reversed:

```
Short call, profit or loss  =  ( premium  −  max(S − K, 0) )  ×  lot size
Short put,  profit or loss  =  ( premium  −  max(K − S, 0) )  ×  lot size

Most a writer can gain      =  premium × lot size
Short call: loss has no upper limit as S rises
Short put:  worst case is S = 0:   ( premium − K ) × lot size
```

## Worked example: one lot, strike {{ w.strike }}, premium {{ w.prem }} points

The writer receives {{ w.prem }} points × {{ c.lot }} = ₹{% assign mg = w.max_gain %}{% include inr.html n=mg %} and that is the most the
writer can ever keep. Breakevens are the buyer's breakevens: {{ w.call_breakeven }}
for the call, {{ w.put_breakeven }} for the put.

| Index at expiry | Move from {{ c.level }} | Short call: profit or loss (₹) | ...as % of assumed margin | Short put: profit or loss (₹) | ...as % of assumed margin |
|---:|---:|---:|---:|---:|---:|
{% for row in w.rows -%}
| {{ row.level }} | {{ row.move_pct }}% | {{ row.call_pl }} | {{ row.call_pl_margin_pct }}% | {{ row.put_pl }} | {{ row.put_pl_margin_pct }}% |
{% endfor %}

Look at each column. For the short call the gain stops at
₹{% include inr.html n=mg %}; on the other side the loss grows with every point
the index rises: at {{ w.example_level }} it is already ₹{% assign l22 = w.loss_at_22000_call %}{% include inr.html n=l22 %},
about {{ w.loss_at_22000_vs_gain_multiple }} times the best-case gain. The short put's loss is bounded by the
index reaching zero, at ₹{% assign pwc = w.put_worst_case %}{% include inr.html n=pwc %}, a bound that is of little comfort in
practice. In both cases the premium is the *whole* upside and a
small part of the downside.

### Margin: why the deposit exists

The Securities and Exchange Board of India (SEBI) circular {{ s.circular_2024.number }} of
{{ s.circular_2024.date }}, as restated in its {{ s.master_circular.name }}
({{ s.master_circular.date }}, read on {{ s.master_circular.read }}), says applicable upfront margins must be collected from the
client in advance of the trade (master circular paragraph {{ s.upfront_margin.para }}). For short options on the day of expiry it
adds an **additional extreme loss margin (ELM) of {{ w.elm_pct }}%** on short options due to expire
that day, whether open at the start of the day or initiated during it
(paragraph {{ s.expiry_extra_elm.para }}, effective {{ s.expiry_extra_elm.effective }}). It also removed the offset benefit of
calendar spreads on expiry day (paragraph {{ s.no_calendar_spread_on_expiry.para }}, effective {{ s.no_calendar_spread_on_expiry.effective }}). Rules change, so check the current rule.

Actual margin amounts are set by the exchange and the clearing corporation, and
change with the market and the position. For the table above, this post
*assumes* a round {{ w.margin_pct }}% of contract value: ₹{% assign am = w.assumed_margin %}{% include inr.html n=am %} per lot. That
number is for illustration only. On it, the premium received is
{{ w.gain_over_margin_pct }}% of margin, while an index move of {{ w.example_move_pct }}% against
a short call is a loss of about {{ w.example_loss_pct_margin }}% of it, and a larger move takes the loss
past the whole deposit. What happens to a shortfall is set by the broker's and the exchange's rules, so check
them before relying on a figure like this one. If the {{ w.elm_pct }}% expiry-day add-on were applied to the contract value (the
paragraph quoted above does not say which value it applies to, so this is an
assumption), it would be ₹{% assign ex = w.expiry_extra %}{% include inr.html n=ex %} more.

The number of option positions still outstanding at any time is called
[open interest]({% post_url 2026-11-12-open-interest %}); for every written
option there is a bought one, so open interest counts contracts, not
people on one side.

### What SEBI's studies show about this side

SEBI's August 2026 behaviour study found that, in FY 2025-26 (the financial year to March 2026), about
{{ f.options_sellers_pct }}% of the individual traders it classified by how they traded options were mainly option
sellers, against about {{ f.options_buyers_pct }}% who were mainly buyers (the study's page 17; check it for the exact group counted); its
profitability study found that options accounted for about
{{ site.data.fno.fy26.options_share_of_losses_pct }}% of the futures and options (F&O) segment's aggregate
losses that year. These are SEBI's figures from the studies discussed in the
[F&O numbers post]({% post_url 2026-10-08-what-the-fo-numbers-actually-say %}),
quoted here and not recomputed; they are research statistics, and they do not
say that either side does better. How income and losses from this activity are
taxed is a separate matter in the
[Tax series]({{ '/2026/11/26/fo-is-business-income/' | relative_url }}).

## Common mistakes

- **Reading the premium as the return.** It is the maximum gain, collected in
  advance. Against margin it can look modest, and the loss that sits on the
  other side of the table can be many times larger.
- **Calling a put's loss "limited" because it has a floor.** The floor is the
  index at zero. The practical question is how much margin and capital stand
  behind a position, and a bounded loss can still be larger than the account.
- **Treating margin as the most you can lose.** Margin is a deposit set by the
  exchange's risk model. The last row of the table shows a loss larger than
  the assumed margin.
- **Ignoring expiry-day rules.** The {{ w.elm_pct }}% add-on and the end of the
  calendar-spread offset (both above) apply on the day of expiry, when moves
  can be quickest. The [expiry post]({{ '/2026/11/24/option-expiry-and-settlement/' | relative_url }})
  covers the day itself.

**Takeaway:** An option writer's gain is capped at the premium received, while the loss on a short call has no cap and on a short put stops only when the index reaches zero. Margin is a deposit against that asymmetry, not a ceiling on the loss, as the table's last row shows.
