---
layout: post
title: "The pre-open session and how the closing price is set"
seo_title: "Pre-open session and closing auction: how prices are set"
description: "The day opens and, for many stocks, closes with a call auction that sets one price. How the pre-open session and closing auction work, on an order book."
image: /assets/og/pre-open-session-closing-price.png
date: 2027-05-14 09:00:00 +0530
series: market-basics
term: "Pre-open session and closing auction"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign a = site.data.market_basics_m2.auction %}

## What a call auction is

Most of the trading day is a **continuous session**: each order is matched
as soon as an opposite order at a compatible price arrives. At the open, and
for stocks with derivatives at the close too, the Indian stock exchanges do
something different, a **call auction**. Orders are
collected for a few minutes without trading, and then one price is worked
out at which the most shares can change hands. Everyone who trades in the
auction trades at that single price.

The morning auction is the **pre-open session**. Since 3 August 2026, under a
circular of 16 January 2026 from SEBI (the Securities and Exchange Board of
India), stocks that have derivatives also close with one: the **closing
auction session**, whose price becomes the stock's closing price. This post sets out both
as they stand once every announced change has taken effect (the last on
8 February 2027), as read in November 2026. It's
part of [Your first year in the market]({{ '/series/market-basics/' | relative_url }}),
after [order types]({% post_url 2026-12-12-order-types-explained %}).

## The rules

**Pre-open session**, {{ a.preopen }} (from {{ a.preopen_from }}):

| Starts | What happens | Minutes |
|---|---|---:|
{% for s in a.preopen_sessions -%}
| {{ s.start }} | {{ s.what }} | {{ s.mins }} |
{% endfor %}

**Closing auction**, for stocks on which derivatives trade, {{ a.cas_window }}
(from {{ a.cas_from }}, under SEBI's circular of 15 October 2026):

- A **reference price** is set from the
  [volume-weighted average price (VWAP)]({% post_url 2026-10-21-obv-and-vwap %})
  of trades in the last {{ a.cas_ref_minutes }} minutes of the continuous
  session. If there were none, the day's last traded price is used.
- Orders can be placed within ±{{ a.band_pct }}% of the reference price.
  Limit and market orders are allowed; stop-loss orders aren't, and new
  iceberg orders must show their full quantity.
- Limit orders still unfilled at the end of the continuous session are
  carried into the auction, unless they are stop-loss orders or priced
  outside the band. From 8 February 2027 unfilled iceberg orders are carried
  in too, as fully shown limit orders, unless you opted out when placing them.
- Order entry closes at a random moment in the last two minutes.
- The closing price is the auction's equilibrium price. If none is found, the
  reference price becomes the closing price.
- Trades in the post-close session, {{ a.post_close }}, happen at that
  closing price.

**Stocks without derivatives** keep the older method: the closing price is the
VWAP of trades in the last {{ a.vwap_minutes_non_cas }} minutes of the
continuous session.

**How the closing auction price is found:**

```
1. Take the price at which the most shares can be matched.
2. If several prices tie, take the one with the smallest unmatched quantity.
3. If they still tie, take the one closest to the reference price.
4. If the reference price is exactly midway between the two, it is the closing price.
Market orders are matched first, then limit orders by price and time.
```

The pre-open session also sets one price by a call auction; its detailed
rules are in SEBI's master circular for stock exchanges and aren't covered
here.

## Worked example: one closing auction, one price

A hypothetical stock in the closing auction, with a reference price of ₹{{ a.reference }}, so
orders are allowed between ₹{{ a.band_low }} and ₹{{ a.band_high }}. At the
end of order entry the book holds:

| Buy orders | Shares | Sell orders | Shares |
|---|---:|---|---:|
{% for b in a.buys -%}{% assign s = a.sells[forloop.index0] -%}
| {% if b.price == "Market" %}Market{% else %}₹{{ b.price }} or less{% endif %} | {{ b.qty }} | {% if s.price == "Market" %}Market{% else %}₹{{ s.price }} or more{% endif %} | {{ s.qty }} |
{% endfor %}

A buyer at ₹503 will also buy at any lower price; a seller at ₹499 will also
sell at any higher one. So at each candidate price:

| Price | Shares wanted at this price or better | Shares offered at this price or better | Shares that can trade | Left unmatched |
|---:|---:|---:|---:|---:|
{% for r in a.rows -%}
| ₹{{ r.price }} | {{ r.buy }} | {{ r.sell }} | {% if r.price == a.eq_price %}**{{ r.matched }}**{% else %}{{ r.matched }}{% endif %} | {{ r.unmatched }} |
{% endfor %}

The most shares, {{ a.eq_volume }}, trade at **₹{{ a.eq_price }}**, so that is
the auction price and the day's closing price.
Every matched buyer pays ₹{{ a.eq_price }}, including those who were willing
to pay more; every matched seller gets ₹{{ a.eq_price }}, including those who
would have taken less. {{ a.eq_unmatched }} shares on the buy side are left
over.

## Common mistakes

1. **Expecting a stop-loss to work in the closing auction.** Stop-loss
   orders aren't allowed in it, and pending ones aren't carried in.
2. **Forgetting an unfilled limit order.** A day's limit order still open at
   the end of the continuous session can trade in the closing auction, at
   the auction price.
3. **Reading the "last traded price" as the closing price.** For stocks with
   derivatives, the closing price comes from the auction, after the
   continuous session ends.
4. **Assuming your limit price is your trade price.** In an auction everyone
   trades at the single equilibrium price, which may be better than your
   limit.
5. **Missing the random close.** Order entry ends at an unannounced moment in
   the last two minutes, so an order sent at the very end may miss the
   auction.

**Takeaway:** The trading day opens with a call auction and, for stocks with
derivatives, since August 2026 closes with one: orders are collected, then one price is set
where the most shares trade. Everyone matched in the auction trades at that
price, and the closing auction's price becomes the closing price.

## Sources

- SEBI circular HO/47/11/11(3)2025-MRD-POD2/I/2765/2026, [16 January 2026]({{ a.jan_url }}): closing auction introduced; pre-open session revised (paras 4 and 5, implemented from 3 August and 7 September 2026).
- SEBI circular HO/47/11/11(3)2025-MRD-POD2/I/23843/2026, [15 October 2026]({{ a.oct_url }}): closing auction moved to 3:30–3:40 pm and reference price to the last 15 minutes, from 7 December 2026; carrying unexecuted iceberg orders into the auction from 8 February 2027.
- Both read on 21 November 2026. Exchanges issue their own operating procedures under these circulars; check them for any later change.
