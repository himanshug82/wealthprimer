---
layout: post
title: "Order types: market, limit, stop-loss, IOC and day"
description: "Market, limit, stop-loss, IOC and day orders decide your price and whether you get filled. Each explained with a worked example on an illustrative book."
image: /assets/og/order-types-explained.png
date: 2026-12-03 09:00:00 +0530
series: market-basics
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign o = site.data.market_basics.orders %}
{% assign x = site.data.market_basics.nse %}

## What an order type is

An order type tells the exchange two things: **at what price** you'll trade, and **for how long** the order should live. Most orders you place through a broker are one of a small set of main types.

This post uses NSE's (National Stock Exchange of India's) own definitions, from its [equity trading system page]({{ x.trading_url }}) (page last updated {{ x.trading_page_updated }}) and [pre-open page]({{ x.preopen_url }}) (updated {{ x.preopen_page_updated }}), as at November 2026.

| Type | What NSE says it is |
|---|---|
| **Market** | An order to buy or sell at the best price obtainable at the time of entering the order |
| **Limit** | An order where you specify the price when entering it |
| **Stop-loss (SL)** | An order that is activated only when the market price reaches or crosses a threshold (trigger) price; until then it does not enter the market |
| **Day** | Valid for the day it's entered; cancelled automatically at the end of the day if unmatched |
| **IOC** (immediate or cancel) | Trades as soon as it's released, and any unmatched part is cancelled immediately; a partial match is possible |

NSE's page says that good-till-cancelled and good-till-date orders are not available on its system under SEBI (Securities and Exchange Board of India) directives. Your broker's app may offer features that look like these; they work differently from exchange orders, so read the broker's description.

For a stop-loss order, NSE says a sell order in the stop-loss book is triggered when the last traded price reaches or falls below the trigger price, and a buy order when it reaches or rises above it. A stop-loss order has a trigger and a limit price: once triggered, it becomes a limit order. Whether your broker's "SL-M" stop-loss-market option exists for equities isn't covered on the NSE page we read, so check with your broker.

## Hours

NSE's pre-open page gives a pre-open session of {{ x.preopen_window }}, with market orders and limit orders in the first part, and says stop-loss and IOC orders are not allowed in pre-open. NSE's [market-timings page]({{ x.timings_url }}) shows the normal market opening at {{ x.normal_open }} and closing at {{ x.normal_close }}. **Check the current timings**: NSE's pages and SEBI circulars on timings change.

## The flow

```
Buy order  -->  matched against the lowest sell prices first (price priority)
               at the same price, the earlier order first (time priority)
```

## Worked example: one buy order, three ways

A hypothetical order book for a stock trading around Desi Bites' fictional ₹{{ o.listing_price }} IPO price. This is **made up for illustration**, not market data. Sellers are offering:

| Ask price (₹) | Quantity |
|---:|---:|
{% for a in o.asks -%}
| {{ a.price }} | {{ a.qty }} |
{% endfor %}

You want to buy {{ o.buy_qty }} shares.

**Market order.** It takes the best prices available in order: {% for f in o.market.fills %}{{ f.qty }} at ₹{{ f.price }}{% unless forloop.last %}, {% endunless %}{% endfor %}. You get all {{ o.market.qty }} shares, for ₹{% include inr.html n=o.market.cost %}, an average of ₹{{ o.market.avg_fmt }}. That's ₹{{ o.market.slippage_fmt }} a share above the best ask you saw. You put execution ahead of price. That worked here because the book had enough shares on offer; on a thinner book the order could be filled only in part or at much worse prices.

**Limit order at ₹{{ o.limit.limit }}.** It trades only at ₹{{ o.limit.limit }} or better: {% for f in o.limit.fills %}{{ f.qty }} at ₹{{ f.price }}{% unless forloop.last %}, {% endunless %}{% endfor %}. That fills {{ o.limit.qty }} shares at an average of ₹{{ o.limit.avg_fmt }}. The other {{ o.limit.unfilled }} shares stay unfilled: as a day order they wait on the book until the end of the day, as an IOC order they are cancelled immediately. You bought price control and gave up certainty of a fill.

**Stop-loss buy.** Say the last traded price is ₹{{ o.stop_loss.ltp_before }}, and you place a stop-loss buy with a trigger of ₹{{ o.stop_loss.trigger }} and a limit of ₹{{ o.stop_loss.limit }}. Nothing happens while the price stays below ₹{{ o.stop_loss.trigger }}. Once the last traded price reaches or exceeds ₹{{ o.stop_loss.trigger }}, it enters the market as a limit order at ₹{{ o.stop_loss.limit }}. If the price jumps past ₹{{ o.stop_loss.limit }} before it can match, it may not fill. For where stops are placed, see [stop-loss placement]({% post_url 2026-10-22-stop-loss-placement %}); this post only covers what the order does.

How wide the gaps between prices are, and why a market order costs more on a thinly traded stock, is the [bid-ask spread]({% post_url 2026-10-14-bid-ask-spread-and-liquidity %}). Daily limits on how far a price can move are in [circuit limits]({% post_url 2026-10-15-circuit-limits-and-price-bands %}).

## Common mistakes

- **Using a market order on a stock that trades thinly.** The example shows the average price drifting above the best ask as the order eats deeper into the book. The thinner the book, the bigger the drift.
- **Thinking a limit order guarantees a trade.** It guarantees a price, not a fill.
- **Confusing the trigger and the limit in a stop-loss.** The trigger switches the order on; the limit price then sets the worst price you'll accept. If the market gaps through your limit, you can be left unfilled.
- **Assuming every order type works in every session.** NSE says stop-loss and IOC orders are not allowed in pre-open.

**Takeaway:** A market order puts getting traded ahead of the price, and a thin book can move that price a lot; a limit order puts the price first, at the risk of no fill. Stop-loss, day and IOC orders add a trigger or a time limit — know which one you're sending before you press the button.
