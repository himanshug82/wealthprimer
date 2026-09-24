---
layout: post
title: "Bid-ask spread and liquidity: why the price on the screen isn't the price you get"
description: "The gap between the best buyer and the best seller, and what happens when your order is bigger than it. Impact cost worked on a thin, hypothetical order book."
image: /assets/og/bid-ask-spread-and-liquidity.png
date: 2026-10-14 09:00:00 +0530
series: jargon
term: "Bid-ask spread (and impact cost)"
---

{% assign s = site.data.jargon_m7.spread %}
{% assign bs = s.buy_small %}
{% assign bb = s.buy_big %}
{% assign sb = s.sell_big %}
{% assign br = s.britannia %}
{% assign bb_lakh = bb.value | divided_by: 100000.0 | round: 1 %}

## What the bid-ask spread is

Every listed share has two prices at any moment, not one. The **bid** is the
highest price someone is currently willing to *pay*. The **ask** (or offer)
is the lowest price someone is currently willing to *sell* at. The gap
between them is the **bid-ask spread**.

The "price" you see quoted on an app is usually the last traded price — what
the most recent buyer and seller agreed on. It's history. If you place a
market order now, you'll buy at the ask or sell at the bid, and the spread is
the toll for trading immediately instead of waiting.

**Liquidity** is how much you can trade without moving that price much. A
liquid stock has many orders stacked close to the best bid and ask; a thin
("illiquid") one has a handful, spread far apart. The spread tells you what a
*small* order costs. For a bigger order you need a second number,
**impact cost**, because your order eats through several price levels.

## The formula

```
Spread (Rs)            = Best ask − Best bid
Mid price ("ideal")    = (Best ask + Best bid) / 2
Spread (%)             = Spread / Mid price × 100

Impact cost (%)        = (Your average fill price − Mid price) / Mid price × 100    for a buy
                       = (Mid price − Your average fill price) / Mid price × 100    for a sell
```

That impact-cost definition — the mark-up over the mid-point of the best bid
and ask for an order of a given size — is the one NSE uses (NSE, [impact cost](https://www.nseindia.com/static/products-services/indices-impact-cost)).
Notice it depends on *order size*: a stock doesn't have "an impact cost", it
has one for ₹1 lakh, another for ₹10 lakh, and so on.

## Worked example: a thin order book for Desi Bites

Desi Bites Foods is our [fictional](/case-study/) small listed company. Here
is a *hypothetical* snapshot of its order book: the best five bids and asks,
the view any trading app shows under "market depth".

| Bid (buyers) | Shares | | Ask (sellers) | Shares |
|---:|---:|---|---:|---:|{% for i in (0..4) %}{% assign b = s.book.bids[i] %}{% assign a = s.book.asks[i] %}
| ₹{{ b.price }} | {{ b.shares }} | | ₹{{ a.price }} | {{ a.shares }} |{% endfor %}

**Step 1 — the spread.** Best bid ₹{{ s.best_bid }}, best ask ₹{{ s.best_ask }}, so the spread is
₹{{ s.spread }}. The mid price is ₹{{ s.mid }}, and the spread is {{ s.spread_pct_of_mid }}% of it.

**Step 2 — a small buy.** Buy {{ bs.shares }} shares at market and all of them fill at
₹{{ bs.avg_price }}. Impact cost = {{ bs.impact_cost_pct }}% — exactly half the spread, the least a
market buy can cost.

**Step 3 — a bigger buy.** Buy {{ bb.shares }} shares at market (about
₹{% include inr.html n=bb.value %}). The order clears the first ask level and keeps going:

| Filled at | Shares | Value (₹) |
|---:|---:|---:|{% for f in bb.fills %}
| ₹{{ f.price }} | {{ f.shares }} | {{ f.value }} |{% endfor %}
| **Average ₹{{ bb.avg_price }}** | **{{ bb.shares }}** | **{{ bb.value }}** |

Impact cost = ({{ bb.avg_price }} − {{ s.mid }}) ÷ {{ s.mid }} = **{{ bb.impact_cost_pct }}%**, or
₹{% include inr.html n=bb.cost_vs_mid_rupees %} more than the same shares would cost at the mid price.

**Step 4 — sell them straight back.** The order walks down the bids to an
average of ₹{{ sb.avg_price }}: impact cost {{ sb.impact_cost_pct }}%. The round trip loses
₹{% include inr.html n=s.round_trip_loss %} ({{ s.round_trip_loss_pct }}% of the purchase) before brokerage,
tax or charges, and without the price having "moved" at all.

The screen said ₹{{ s.mid }}-ish the whole time. The order paid ₹{{ bb.avg_price }} and got
₹{{ sb.avg_price }} back.

### For contrast: how much trades in Britannia

We don't have Britannia's historical order book, so here's the observable
that stands in for depth: how much changes hands each day. Across
{{ br.sessions }} NSE sessions in FY26 (close × volume from Yahoo Finance,
{{ br.window }}; one zero-volume data row dropped), Britannia's median day
saw about ₹{{ br.median_daily_value_cr }} crore traded on the NSE alone; a quiet day (10th
percentile) about ₹{{ br.p10_daily_value_cr }} crore. Our hypothetical Desi Bites book shows
{{ s.visible_ask_shares }} shares on offer across five levels, worth about ₹{{ s.visible_ask_value_lakh }} lakh
in all. A ₹{{ bb_lakh }} lakh order is a rounding error in the first and takes
{{ s.big_order_pct_of_visible_asks }}% of the shares visibly on offer in the second. For illustration only.

Turnover isn't the same as spread, but they travel together: heavily traded
stocks tend to have tight spreads and deep books, because many participants
keep quoting on both sides. This is also why the
[volume post]({% post_url 2026-10-07-volume %}) treats volume as
information about how many people are behind a move.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

A shop buys old cricket bats for ₹400 and sells them for ₹450. If you sell
your bat and buy it straight back, you're ₹50 poorer and still have the same
bat. That ₹50 is the spread.

Now imagine the shop only has one bat at ₹450, and the next one it can find
costs ₹500, and the one after that ₹560. If you want three bats, you don't
pay ₹450 each. That's impact cost.

</details>

## Common mistakes

- **Treating the last traded price as the price you'll get.** On a thin
  stock the last trade may be minutes or hours old. The ask is what you'll
  pay; the bid is what you'll get.
- **Using market orders in illiquid stocks.** A market order says "fill me at
  whatever the book offers". A limit order caps the price, at the cost of
  maybe not filling. Neither is right or wrong in general; not knowing which
  one you placed is the mistake.
- **Judging liquidity from the spread alone.** A ₹0.05 spread with 10 shares
  on each side is not liquid for a 5,000-share order. Look at the depth
  behind the best prices, or the impact cost for *your* size.
- **Backtesting on closing prices.** A strategy that trades a small, thin
  stock at the close every day ignores the spread and impact it would
  actually pay. On liquid large caps that cost is small; on thin stocks it
  can be larger than the edge being tested.

**Takeaway:** the price on the screen is where the last trade happened; the
price you get is the other side of the order book, and for a big order in a
thin stock it gets worse the more you trade. Check the spread and the depth
before you check the price.
