---
layout: post
title: "Option expiry and settlement: the last day"
description: "How index and stock options end: cash or delivery, which price settles an index option, and what is unconfirmed, as read on 1 November 2026."
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
{% assign s = r.sources %}

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
have changed more than once recently, so this post separates what could be
confirmed from the text of a rule from what could not, as of
**1 November 2026**. Where the post says "check the current rule", that is a
prompt to open the exchange's current circular, not filler. It sits in
[Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}).

## Two different payments

It helps to keep two payments apart.

- **The premium.** Index options are *premium-style* contracts (master circular
  paragraph {{ s.index_options_style.para }}). The premium is paid in by the buyer and paid out to the
  seller in cash on T+1, the next trading day after the trade (paragraph
  {{ s.premium_settlement.para }}; the [T+1 post]({% post_url 2026-10-16-t-plus-1-settlement %})
  explains that term). Separately, the buyer's broker must collect the premium
  from the client upfront, as the earlier posts noted. Both belong to the day
  the option is bought, not to expiry.
- **The expiry payoff.** What an option pays at expiry comes from the payoff
  formula and the settlement price below. The exchange's final-settlement
  procedure for that payoff is set out in its own circulars, which this post
  does not quote: check the current rule.

## Who settles in what

The source for this section is the {{ s.master_circular.name }}
({{ s.master_circular.date }}), read on {{ s.master_circular.read }}.

- **Index contracts are settled in rupees.** The chapter says index futures
  "shall be settled in Indian Rupees" (paragraph 1.1.8), and index options
  follow the same settlement mechanism (paragraph {{ s.index_options_style.para }}). No shares change hands.
- **Stock derivatives are settled by delivery.** The same chapter says
  "{{ s.stock_derivs.text }}" (paragraph {{ s.stock_derivs.para }}). A stock option still open at
  expiry can therefore end as an obligation to deliver or take delivery of
  shares. Which positions go to delivery, and the margin on them, are exchange
  rules: check the current rule.

## Which price settles an index option

For a cash-settled index option, the amount paid at expiry is the payoff
formula from the earlier posts, with `S` taken as the **settlement price**:

```
Call payoff = max( settlement price − strike, 0 ) × lot size
Put payoff  = max( strike − settlement price, 0 ) × lot size
```

So the rule that fixes the settlement price decides whether an option near
its strike finishes with a payoff or with nothing. What the master circular
text says (paragraphs {{ s.settlement_price.para }}):

> The settlement price shall be the {{ s.settlement_price.rule }}.

VWAP, the volume-weighted average price, is explained in the
[on-balance volume (OBV) and VWAP post]({% post_url 2026-10-21-obv-and-vwap %}).

**What is not confirmed.** SEBI's site lists a circular of
{{ s.closing_auction_2026.circular_jan_2026 }} and one of
{{ s.closing_auction_2026.circular_oct_2026 }} on the Closing Auction Session (CAS, a
separate closing session in the cash market), market timings and the settlement
methodology for derivatives contracts; the later one is titled
"{{ s.closing_auction_2026.oct_2026_title }}". Their
operative terms, effective dates and timings could not be opened for this
post, and a SEBI publication of August 2026 describes a closing auction
session with timings that differ from those some sources give. So this post
does **not** say which settlement-price rule applies on a given expiry date after the
master circular's rule above, whether the closing auction session has started,
or what the trading hours are on expiry day. That is a question for the
exchange's current circular, and the rule in the master circular may no longer
be the one in force when you read this.

## Other expiry-day rules in the same chapter

Several other rules from the {{ s.circular_2024.date }} circular
({{ s.circular_2024.number }}), as restated in the master circular, apply
around expiry:

- an additional extreme loss margin of {{ s.expiry_extra_elm.pct }}% on short options due to expire that
  day (paragraph {{ s.expiry_extra_elm.para }}, effective {{ s.expiry_extra_elm.effective }}), and no
  calendar-spread offset on expiry day (paragraph {{ s.no_calendar_spread_on_expiry.para }}, effective
  {{ s.no_calendar_spread_on_expiry.effective }}), as the [writing post]({{ '/2026/11/08/option-writing-and-margin/' | relative_url }})
  described;
- weekly contracts on indices available on only one benchmark index for each
  exchange (paragraph {{ s.one_weekly_benchmark.para }}, effective {{ s.one_weekly_benchmark.effective }}).

The National Stock Exchange (NSE) contract-specification page, updated
{{ s.nse_expiry.page_date }}, lists {{ s.nse_expiry.expiry_day }} as the expiry day for its listed index contracts; that page
was not re-opened for this post, and the expiry calendar changes, so check the
current one.

## Worked example: how an averaging rule can matter

The example uses the averaging rule quoted above, the last half hour VWAP, on a
simplification: treat the index as a single constituent, so that its settlement
value is that stock's VWAP over 3:00 to 3:30 pm. In five-minute blocks, with
illustrative prices and volumes:

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

For contrast, suppose a single late trade inside the 3:25 to 3:30 block went through at
{{ e.last_print }}, above that block's average. This is not a rule quoted in this
post: it only shows what a "last trade" method would do differently. Take a call
with a strike of {{ e.strike }}, one lot of {{ c.lot }} units:

| Settlement price used | Value | Call payoff per lot (₹) |
|---|---:|---:|
| Last-half-hour VWAP | {{ e.vwap }} | {{ e.payoff_vwap }} |
| One late trade (for contrast only) | {{ e.last_print }} | {{ e.payoff_last }} |

The two prices are {{ e.diff_pts }} points apart. That is a small gap, and
it separates an option that finishes with nothing from one that finishes with a payoff
of ₹{% assign pl = e.payoff_last %}{% include inr.html n=pl %} per lot. The averaging window dampens the effect of a single late
trade on the settlement, which is what an averaging rule is for; it does not
remove the sharp edge at the strike. The numbers here are made up and the
one-stock index is a simplification.

## Common mistakes

- **Assuming the settlement price is the last price on the screen.** For
  index options it is a rule-defined value, and the rule has been under review
  within the last year. Check the current rule before assuming how a position
  near the strike will settle.
- **Forgetting that stock options can end in delivery.** Index options
  settle in rupees; stock derivatives are physically settled under the
  master circular, so a position held into expiry can create a share
  obligation that a cash-settled position never does.
- **Treating the master circular as today's rule.** It is the text that could
  be confirmed for this post, dated {{ s.master_circular.date }}. Later SEBI
  circulars on the closing auction session and derivatives settlement exist
  and are not confirmed here.
- **Reading a rules summary as a trading note.** The facts here are as of
  1 November 2026 and come from the documents named. Exchanges publish the
  operational detail and the dates it applies from.

**Takeaway:** Index options settle in rupees against a settlement price fixed by rule, and stock derivatives settle by delivery. As read on 1 November 2026, the confirmed rule uses the last half hour VWAP, and later SEBI changes to the closing session and settlement method are not confirmed here, so check the exchange's current circular.
