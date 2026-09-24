---
layout: post
title: "What the F&O numbers actually say"
description: "SEBI has counted, five years running: most individual derivatives traders lose money. What the data shows, and the arithmetic behind why it keeps happening."
image: /assets/og/what-the-fo-numbers-actually-say.png
date: 2026-11-05 09:00:00 +0530
series: risk
---

{% assign f = site.data.fno %}
{% assign s = f.sources %}
{% assign u = f.fy26_unverified %}

## The one statistic worth knowing before you start

**F&O — Futures and Options** — is the derivatives segment of the Indian
market: contracts whose value is derived from something else, usually a stock
or an index, rather than being ownership of a business the way a share is.

It is also the most thoroughly measured corner of Indian retail investing,
because SEBI — the Securities and Exchange Board of India, the market
regulator — has gone and counted. Not surveyed. Counted, using actual
client-level trading data from brokers.

Here is what five years of counting found:

| Period | Individual traders who lost money |
|---|---:|
| FY22 ([{{ s.fy22_study.date }} study]({{ s.fy22_study.url }})) | {{ f.fy22.loss_pct }}% |
| FY22–FY24 ([{{ s.fy22_fy24_study.date }} study]({{ s.fy22_fy24_study.url }})) | {{ f.fy22_fy24.loss_pct }}% |
| FY26 ([{{ s.fy25_fy26_study.date }} study]({{ s.fy25_fy26_study.url }})) | {{ f.fy26.loss_pct }}% |

Over FY22–FY24, aggregate losses for individual traders exceeded
**₹{% include inr.html n=f.fy22_fy24.aggregate_loss_cr %} crore**. In FY26
alone the figure was **₹{% include inr.html n=f.fy26.aggregate_loss_cr %}
crore**, of which about {{ f.fy26.options_share_of_losses_pct }}% came from
options rather than futures.

Read the first column again. This is not a bad year being reported. It is
every year that has been measured, through a bull market and a correction,
before and after a round of regulatory tightening designed to cool the
segment down. The number moves by a few points. It does not move by twenty.

## Why this post exists

This blog has spent sixty-odd posts on how to value a business, read a chart,
compare a fund, and calculate a tax. All of it assumes the thing you're doing
is *investing*: putting money into an asset and being paid by what that asset
produces.

F&O is a different activity wearing similar clothes. Most of the money
individuals lose in the Indian market is lost here, and it is lost by people
who arrived through the same apps, the same feeds, and often the same
vocabulary as everyone else. A blog that taught RSI and never mentioned this
would have been withholding the single most useful number in Indian retail
finance.

## The arithmetic underneath

The loss rate isn't a mystery, and it isn't mainly about people being stupid.
Three structural facts do most of the work.

**1. It is a zero-sum transfer before costs, and negative-sum after.**

A share can make everyone who owns it richer, because the company underneath
generates profit and pays it out or reinvests it. There's a real economic
engine producing returns.

A derivatives contract has no engine. Every rupee gained by one side is lost
by the other, exactly:

```
Sum of all gains  +  Sum of all losses  =  0        (before costs)
Sum of all gains  +  Sum of all losses  = −(costs)  (after costs)
```

So the segment as a whole cannot make money. It can only move money between
participants, minus what leaks out in brokerage, exchange fees, STT (Securities
Transaction Tax), stamp duty and GST. SEBI puts the individual segment's
transaction costs at roughly
₹{% include inr.html n=u.transaction_costs_cr_fy22_fy26 %} crore over FY22–FY26
{% comment %}Two independent secondary sources agree on this figure; the primary SEBI PDF is still unread — see _data/fno.yml{% endcomment %}. That is
the house's cut, and it is paid whether you win or lose.

**2. The people on the other side are not like you.**

The counterparty to a retail options trade is usually a proprietary desk or a
foreign institutional investor running algorithms — SEBI's earlier study found
the overwhelming majority of those participants' profits came from algorithmic
trading. Faster execution, better pricing models, lower costs per trade, and
no emotional stake in any single position.

**3. Leverage compresses the time you have to be right.**

This is the part that gets least appreciated, so it gets a worked example.

## Worked example: what leverage actually does

Illustrative round numbers, not a real contract or a real price — the point is
the structure, not the instrument.

Suppose an index sits at 24,000 and one lot is 75 units. Buying the underlying
outright would cost:

```
24,000 × 75  =  ₹18,00,000
```

A futures contract on it might need roughly 12% of that as margin:

```
Margin  =  ₹18,00,000 × 12%  =  ₹2,16,000
```

Now move the index by 1%, which is an ordinary Tuesday:

| | Bought the underlying | Bought one futures lot |
|---|---:|---:|
| Capital committed | ₹18,00,000 | ₹2,16,000 |
| Index moves +1% | +₹18,000 | +₹18,000 |
| Return on capital committed | **+1.0%** | **+8.3%** |
| Index moves −1% | −₹18,000 | −₹18,000 |
| Return on capital committed | **−1.0%** | **−8.3%** |

The rupee move is identical. The percentage return on *your* money is roughly
eight times larger in both directions. That multiplier is the entire appeal,
and it is also the entire problem: a 12% adverse move — which an index can
deliver over a few weeks and a single stock over a single session — takes the
margin to zero.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine two ways to bet on a cricket match.

The first: you buy a share of the team. If the team does well for years —
wins matches, sells tickets, sells jerseys — you slowly get richer. Everybody
who owns a piece of a good team can do well at the same time, because the
team is actually *making* money.

The second: you and a friend bet ₹100 on today's match. At the end of the day,
one of you has ₹200 and the other has nothing. Nothing was made. The money
just moved.

Now add two details. A bookie takes ₹5 from every bet, win or lose. And the
person betting against you does this professionally, all day, with a computer
that has watched a million matches.

You can still win a bet. You will find it very hard to keep winning bets.

</details>

## What the data does *not* say

Being fair to the numbers matters more than being dramatic with them.

- **It does not say derivatives are useless.** Futures and options exist for
  hedging, and they do that job well. A fund manager protecting a portfolio
  and an individual buying weekly options are doing unrelated things with the
  same instrument.
- **It does not say nobody makes money.** Roughly one in eight individual
  traders was profitable in FY26. Some of them are genuinely skilled.
- **It does not tell you what to do.** It tells you the base rate. What you do
  with a base rate is your business, and this blog is not registered to advise
  you on it.

What the data does say is that the honest prior, before any personal
confidence enters the picture, is that this is an activity in which the large
majority of participants lose, repeatedly, and that the minority who don't are
mostly not individuals.

## Common mistakes

- **Reading the loss rate as "unlucky people."** Roughly nine in ten of those
  who lost in two consecutive years lost again
  {% comment %}Two independent secondary sources agree; primary PDF still unread — see _data/fno.yml{% endcomment %}. If the outcome were
  luck, it would not persist that reliably at the individual level.
- **Confusing a win rate with a profit.** Options buyers can be right most of
  the time and still lose overall, because the losses on the wrong days are
  bigger than the gains on the right ones. Count rupees, not trades.
- **Ignoring costs because each one is small.** A ₹20 brokerage on a position
  held for two hours is a rounding error per trade and a very large number per
  year. Costs are the one part of the outcome that is certain in advance.
- **Assuming a small position is a small risk.** Leverage means the position
  size and the money at risk are different numbers. That is the whole point of
  the table above.
- **Treating "I understand the strategy" as an edge.** Understanding a
  strategy is table stakes. An edge means having something the counterparty
  doesn't, and the counterparty is usually a machine.
- **Forgetting F&O is taxed differently.** F&O gains and losses are generally
  treated as **business income**, not capital gains — so the
  [holding-period rules]({% post_url 2026-10-28-short-term-vs-long-term %})
  and the
  [₹1.25 lakh exemption]({% post_url 2026-10-29-equity-and-equity-funds %})
  that this blog's tax series covers do not apply to them. Different return
  form, different rules, often an audit requirement. Worth its own post.

## If you're going to do it anyway

Not advice — just the things the data suggests you'd want to have settled
before, rather than after:

1. **Decide the maximum you can lose entirely** and treat it as spent, not
   invested. The base rate says that is the likely outcome.
2. **Write down the edge you think you have**, in one sentence, before you
   start. If it comes out as "I think it'll go up," that isn't an edge.
3. **Track rupees, not trades**, including every cost. Most people's memory of
   their own performance is a great deal kinder than their contract notes.
4. **Set a review date** at which you compare the two honestly.

**Takeaway:** SEBI has counted, five years running, and the answer barely
moves — around nine in ten individual F&O traders lose money, and the losses
run to tens of thousands of crores a year. That isn't a run of bad luck; it's
what a zero-sum market minus costs does to the participants who are slowest,
smallest and paying the most to be there. You can still choose to trade. You
just can't claim nobody told you the base rate.
