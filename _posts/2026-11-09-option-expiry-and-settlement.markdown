---
layout: post
title: "Option expiry and settlement: the last day"
description: "How index and stock options end: cash or delivery, which price settles an index option, and the VWAP rule from December 2026, as read on 1 Nov 2026."
image: /assets/og/option-expiry-and-settlement.png
date: 2026-11-09 09:00:00 +0530
series: risk
term: "Expiry and settlement"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign r = site.data.risk3 %}
{% assign c = r.contract %}
{% assign e = r.expiry %}

## What expiry and settlement mean

**Expiry** is the last day an option exists. **Settlement** is what happens to
a position that is still open at the end of it: who pays whom, and in what.
For an option buyer, expiry either leaves a payoff (the option finished in the
money) or leaves nothing. For a writer, it settles the obligation the earlier
posts described: the
[buyer's payoff]({{ '/2026/11/04/call-and-put-options/' | relative_url }}) is the
[writer's payment]({{ '/2026/11/08/option-writing-and-margin/' | relative_url }}).

The rules for how it settles, and which price is used, are set by SEBI (the
Securities and Exchange Board of India) and implemented by the exchanges. They
have changed more than once recently, so this post gives each rule with the
document and date it was read from, as of **1 November 2026**. Where the post
says "check the current rule", that is a prompt to open the exchange's current
circular, not filler. It sits in
[Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}).

## Who settles in what

- **Index options are settled in rupees.** SEBI's Master Circular for Stock
  Exchanges and Clearing Corporations (30 December 2024, Chapter 5) says index
  futures are "settled in Indian Rupees" and that index options follow the
  same settlement mechanism, as *premium-style* contracts. The premium is paid
  in cash by the buyer and paid out in cash to the seller on the next
  working day (T+1; the [T+1 post]({% post_url 2026-10-16-t-plus-1-settlement %})
  explains that term). No shares change hands.
- **Stock derivatives are settled by delivery.** The same chapter says
  "physical settlement is mandatory for all stock derivatives" (para 3.1.10).
  A stock option still open at expiry can therefore end as an obligation to
  deliver or take delivery of shares. Which positions go to delivery, and the
  margin on them, are exchange rules: check the current rule.

## Which price settles an index option

For a cash-settled index option, the amount paid at expiry is the payoff
formula from the earlier posts, with `S` taken as the **settlement price**:

```
Call payoff = max( settlement price − strike, 0 ) × lot size
Put payoff  = max( strike − settlement price, 0 ) × lot size
```

So the rule that fixes the settlement price decides whether an option near
its strike finishes with a payoff or with nothing. The documents read for this
post say, in order:

| Document (date) | Rule for the settlement price of an expiring index contract |
|---|---|
| Master Circular, Chapter 5 (30 Dec 2024) | The closing value of the index, based on the **last half hour VWAP** of the constituents |
| SEBI circular on the Closing Auction Session, CAS (16 Jan 2026) | The closing value of the index, based on the **closing prices** of the constituents, with the CAS to be implemented from {{ e.sebi_jan2026.cas_start }} |
| SEBI circular {{ e.sebi_oct2026.number }} ({{ e.sebi_oct2026.date }}) | From **{{ e.sebi_oct2026.effective }}**: the index value calculated using the **VWAP of the constituents during the last {{ e.sebi_oct2026.window_min }} minutes** of the continuous trading session (CTS) |

VWAP is the volume-weighted average price, as in the
[OBV and VWAP post]({% post_url 2026-10-21-obv-and-vwap %}). Stock derivatives
expiring on that day follow the matching rule: from {{ e.sebi_oct2026.effective }},
their settlement price is the VWAP of the underlying over the last
{{ e.sebi_oct2026.window_min }} minutes of the CTS, taken across all exchanges.
Which of these rows the exchanges are applying on a given date, and how the CAS
has been implemented, are things to check in the exchange's current circular;
the rule in the last row is not in force on the date of this post.

## The same day under the December 2026 rule

The October 2026 circular also set the following timings for the day, effective
{{ e.sebi_oct2026.effective }} (exchanges' own circulars give the detail):

- the Closing Auction Session runs from {{ e.sebi_oct2026.cas_start }} to
  {{ e.sebi_oct2026.cas_end }};
- trading in *expiring* index derivative contracts stops at
  **{{ e.sebi_oct2026.index_expiry_stop }}** on expiry days, while on other days index
  derivatives trade until {{ e.sebi_oct2026.derivs_stop }};
- stock derivatives trade until {{ e.sebi_oct2026.derivs_stop }} on all days,
  including expiry days.

On expiry day SEBI's circular of 1 October 2024 (SEBI/HO/MRD/TPD-1/P/CIR/2024/132)
also removed the calendar-spread margin offset and added 2% extra margin for
short options, as the [writing post]({{ '/2026/11/08/option-writing-and-margin/' | relative_url }})
described, and limited each exchange to one benchmark index with weekly
expiries. NSE's contract-specification page, updated {{ e.nse.page_date }}, lists
{{ e.nse.expiry_day }} as the expiry day for its listed index contracts; the expiry
calendar changes, so check the current one.

## Worked example: how the averaging rule can matter

A simplification: treat the index as a single constituent, so that its
settlement value is that stock's VWAP over the last 30 minutes. In
five-minute blocks, with illustrative prices and volumes:

| Window | Average price | Volume | Price × volume |
|---|---:|---:|---:|
{% for b in e.buckets -%}
| {{ b.window }} | {{ b.price }} | {{ b.volume }} | {{ b.pv }} |
{% endfor %}
| **Total** | | **{{ e.total_volume }}** | **{{ e.total_pv }}** |

```
VWAP = total (price × volume) ÷ total volume
     = {{ e.total_pv }} ÷ {{ e.total_volume }} = {{ e.vwap }}
```

Suppose the last trade before the close was at {{ e.last_print }}. Now take a
call with a strike of {{ e.strike }}, one lot of {{ c.lot }} units:

| Settlement price used | Value | Call payoff per lot (₹) |
|---|---:|---:|
| Last-30-minute VWAP | {{ e.vwap }} | {{ e.payoff_vwap }} |
| Final trade before the close | {{ e.last_print }} | {{ e.payoff_last }} |

The two prices are {{ e.diff_pts }} points apart. That is a small gap, and
it separates an option that finishes with nothing from one that finishes with a payoff
of ₹{% assign pl = e.payoff_last %}{% include inr.html n=pl %} per lot. The averaging window dampens the effect of a single late
trade on the settlement, which is what an averaging rule is for; it does not
remove the sharp edge at the strike. The numbers here are made up and the
one-stock index is a simplification.

## Common mistakes

- **Assuming the settlement price is the last price on the screen.** For
  index options it is a rule-defined value, and the rule has changed within a
  year. Check the current rule before assuming how a position near the strike
  will settle.
- **Forgetting that stock options can end in delivery.** Index options
  settle in rupees; stock derivatives are physically settled under the
  Master Circular, so a position held into expiry can create a share
  obligation that a cash-settled position never does.
- **Treating the first rows of the table as today's rule.** The December 2024
  and January 2026 rules were superseded, in part, by the October 2026
  circular, effective {{ e.sebi_oct2026.effective }}. Part of that circular (the
  treatment of unexecuted iceberg orders) applies later, from
  {{ e.sebi_oct2026.iceberg_effective }}.
- **Reading a rules summary as a trading note.** The facts here are as of
  1 November 2026 and come from the circulars named. Exchanges publish the
  operational detail and the dates it applies from.

**Takeaway:** Index options settle in rupees against a settlement price fixed by rule, stock derivatives settle by delivery, and the rule for the index settlement price has changed, with an averaging rule set from 7 December 2026. For any option near its strike, the rule that fixes the settlement price decides whether it pays anything.
