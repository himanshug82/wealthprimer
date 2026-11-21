---
layout: post
title: "Delivery vs intraday: charges, margin and settlement"
seo_title: "Delivery vs intraday trades: charges, margin and settlement"
description: "A delivery trade puts the shares in your demat account; an intraday trade is squared off the same day. How STT, stamp duty, margin and settlement differ."
image: /assets/og/delivery-vs-intraday.png
date: 2027-02-17 09:00:00 +0530
series: market-basics
term: "Delivery vs intraday trade"
needs_review: tax
rules_as_of: "November 2026"
rules_for: "Tax Year 2026-27 (FY 2026-27)"
---

{% assign d = site.data.market_basics_m2.delivery %}
{% assign dl = d.fmt.delivery %}
{% assign it = d.fmt.intraday %}

## What the two kinds of trade are

A **delivery trade** is one where the shares change hands: you buy, pay in
full, and the shares arrive in your demat account, where you can hold them
for as long as you like. An **intraday trade** is bought and sold (or sold
and bought back) within the same trading day, so no shares are delivered;
only the difference in price is settled.

The two are treated differently by the tax on the trade, the stamp duty, the
margin a broker must collect and the settlement. This post sets the
differences out side by side, as read in November 2026. It's part of
[Your first year in the market]({{ '/series/market-basics/' | relative_url }}),
after [contract note charges]({% post_url 2026-12-13-contract-note-charges %})
and [T+1 settlement]({% post_url 2026-10-16-t-plus-1-settlement %}).

## The rules

| | Delivery | Intraday (non-delivery) |
|---|---|---|
| STT (securities transaction tax) | {{ d.stt_delivery_pct }}% on the buy and {{ d.stt_delivery_pct }}% on the sell | {{ d.stt_intraday_sell_pct }}% on the sell only |
| Stamp duty | {{ d.stamp_delivery_pct }}% of the buy value, paid by the buyer | {{ d.stamp_intraday_pct }}% of the buy value, paid by the buyer |
| Exchange transaction and SEBI (Securities and Exchange Board of India) fees | Same rates | Same rates |
| Brokerage | Set by your broker | Set by your broker; often a different rate |
| Margin | Upfront margin at the time of trade, then the full price by pay-in on T+1 | Only the upfront margin; the position is closed the same day |
| Settlement | Shares and money change hands on T+1 | Only the net gain or loss is settled, on T+1 |

STT rates are from the circular of 31 March 2026 from NSE (the National Stock
Exchange of India), applying the Finance Act, 2026 to trades from 1 April
2026; stamp duty rates are from NSE's page on levies.

**The margin.** SEBI's risk management rules for the cash market require a
[VaR (value at risk)]({% post_url 2027-01-05-value-at-risk %}) margin and an
extreme loss margin (ELM), collected up front at the time of trade, on
delivery and intraday positions alike. For the most liquid stocks, the VaR margin is at
least {{ d.var_min_pct }}% and the ELM {{ d.elm_pct }}%; less liquid stocks
carry far higher margins. Brokers may collect more than the minimum.

## Worked example: the same trade, both ways

The trade from the [contract note post]({% post_url 2026-12-13-contract-note-charges %}):
{{ d.qty }} shares bought at ₹{{ d.buy_px }} and sold at ₹{{ d.sell_px }},
a gross gain of ₹{% include inr.html n=d.gross %}. Hypothetical; brokerage of
₹{{ site.data.market_basics.charges.brokerage_each }} an order assumed on both, and GST (goods and services tax) charged on
brokerage only, as that post assumed. Figures in ₹.

| Charge | Delivery | Intraday |
|---|---:|---:|
| Brokerage | {{ dl.brokerage }} | {{ it.brokerage }} |
| Exchange transaction charges | {{ dl.txn }} | {{ it.txn }} |
| SEBI fee | {{ dl.sebi }} | {{ it.sebi }} |
| STT | {{ dl.stt }} | {{ it.stt }} |
| Stamp duty | {{ dl.stamp }} | {{ it.stamp }} |
| GST | {{ dl.gst }} | {{ it.gst }} |
| **Total charges** | **{{ dl.total }}** | **{{ it.total }}** |
| Gain after charges | {{ d.fmt.net_delivery }} | {{ d.fmt.net_intraday }} |

STT is most of the gap: the delivery trade pays it on both legs at
{{ d.stt_delivery_pct }}%, the intraday trade on the sell leg only at
{{ d.stt_intraday_sell_pct }}%.

**The margin side.** In a stock at the minimum margins, both trades need at
least {{ d.margin_pct }}% of the value, ₹{% include inr.html n=d.margin_rupees %},
up front. The delivery trade then needs the full
₹{% include inr.html n=d.buy_value %} by pay-in; the intraday trade, closed
the same day, never does. A position of
the same size needs far less cash, which is also why a loss on it is a far
larger share of the cash put up.

This post doesn't cover how the gain is taxed, which can depend on the kind
of trade; the [Tax series]({{ '/series/tax/' | relative_url }}) covers it.

## Common mistakes

1. **Comparing only the charges.** Intraday charges are lower here, but the
   smaller cash outlay means each rupee of price move is a bigger share of
   the money at risk. The [leverage and margin post]({% post_url 2026-10-11-leverage-and-margin %})
   works through that.
2. **Assuming an intraday position can be held overnight.** If it isn't closed
   by the broker's cut-off, the broker may square it off, or it may turn into
   a delivery trade that needs full payment. Each broker sets its own rule.
3. **Expecting identical charges everywhere.** STT and stamp duty are set by
   law; brokerage and some charges are the broker's own. Read your contract
   note.
4. **Mixing up the tax on the trade and the tax on the gain.** STT is charged
   on the trade itself; income tax on the profit is separate.

**Takeaway:** A delivery trade takes the shares and pays STT on both sides; an
intraday trade is squared off the same day and pays a lower STT on the sell
only. Its charges are lower, mainly because of STT, and because it needs only
a margin up front, the risk per rupee of cash is higher.

## Sources

- NSE circular NSE/FATAX/73524, [31 March 2026]({{ d.stt_url }}): STT rates under the Finance Act, 2026.
- NSE, [SEBI turnover fees, STT and other levies]({{ d.levies_url }}): stamp duty rates, read on 21 November 2026.
- SEBI Master Circular for Stock Exchanges and Clearing Corporations, [Chapter 4, risk management for the cash market]({{ d.ch4_url }}) (2023 edition), paras 1.1.8 to 1.1.10: VaR margin and ELM. Check the current master circular for any later change.
