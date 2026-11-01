---
layout: post
title: "Contract note charges: what each line costs"
description: "A contract note lists brokerage, exchange fees, SEBI fee, STT, stamp duty and GST. What each charge is, who pays it, and a worked buy-and-sell example."
image: /assets/og/contract-note-charges.png
date: 2026-12-04 09:00:00 +0530
series: market-basics
needs_review: tax
rules_as_of: "November 2026"
rules_for: "Tax Year 2026-27 (FY 2026-27)"
---

{% assign c = site.data.market_basics.charges %}
{% assign b = c.buy %}
{% assign s = c.sell %}
{% assign ipo = site.data.market_basics.ipo %}

## What a contract note is

A **contract note** is the document your stockbroker sends after you trade. It lists each trade and, under it, the charges taken out. Buying ₹{% include inr.html n=b.value %} of shares does not cost ₹{% include inr.html n=b.value %}: some lines are the broker's own fee, some are the exchange's, and some are taxes the broker collects for the government.

This post covers a normal delivery trade in shares on the NSE (National Stock Exchange of India), as at {{ c.as_of }}, for {{ page.rules_for }}. The rates below are as described in NSE's circulars and investor page, linked in the table; the circular PDFs could not be re-opened when this post was last checked, so treat every rate as "as described on NSE's page" and **check the current rule**. Your broker's price list can also differ on its own lines, so read your own contract note. It is part of [Your first year in the market]({{ '/series/market-basics/' | relative_url }}), after [how accounts work]({% post_url 2026-12-01-demat-trading-bank-accounts %}) and [what order types do]({% post_url 2026-12-03-order-types-explained %}).

## The lines on a contract note

| Charge | What it is | Rate for a delivery trade in shares | Who pays |
|---|---|---|---|
| **Brokerage** | The broker's fee | Set by your broker (this post uses a made-up flat ₹{{ c.brokerage_each }} an order) | You |
| **Exchange transaction charge** | The exchange's fee for matching the trade | ₹{{ c.txn_per_lakh }} per lakh of traded value, each side ([NSE circular {{ c.txn_circular }}]({{ c.txn_url }})) | You, through the broker |
| **SEBI turnover fee** | The fee charged on turnover for the securities regulator (SEBI, the Securities and Exchange Board of India) | ₹{{ c.sebi_fee_per_crore }} per crore of traded value ([NSE page]({{ c.levies_url }}), updated {{ c.levies_updated }}) | You, through the broker |
| **STT** (securities transaction tax) | A tax on the trade | {{ c.stt_delivery_pct }}% on the buy and {{ c.stt_delivery_pct }}% on the sell ([NSE circular {{ c.stt_circular }}]({{ c.stt_url }})) | Buyer on the buy; seller on the sell |
| **Stamp duty** | A duty on the transfer of securities | {{ c.stamp_delivery_pct }}% of the value, on the buy only ([NSE page]({{ c.levies_url }})) | Buyer |
| **GST** (Goods and Services Tax) | Tax on the broker's services | {{ c.gst_pct }}% on stockbroker services ([NSE page]({{ c.levies_url }})) | You, through the broker |

Three things to read carefully:

- **The exchange fee is a flat rate since {{ c.txn_flat_since }}.** NSE's circular describes a SEBI direction to charge one uniform rate rather than slabs that depended on a broker's volume, and to make brokers recover from you only what they pay the exchange ("true to label"). We did not open SEBI's own circular, so check the current rule.
- **STT is not the same for every kind of trade.** The same NSE circular gives {{ c.stt_non_delivery_sell_pct }}% on the sell side when an equity share trade is settled without delivery (for example, squared off within the day), and separate rates on futures and options, which are described as raised from {{ c.stt_fno_raised_from }}. This post does not work those through; the tax treatment of the profit is a different question, covered in the Tax series.
- **GST: an assumption in this post.** NSE's page gives the {{ c.gst_pct }}% rate for stockbroker services but does not say which of the lines above it is charged on. The worked example below **assumes GST on brokerage only**; if your broker also charges it on the exchange and SEBI fees, real charges would be slightly higher. Your contract note shows what your broker actually did.

Depository charges (what your depository participant (DP) bills you for a sale) are separate and are not on this list. Your DP's price list has them.

How a trade settles is in [T+1 settlement]({% post_url 2026-10-16-t-plus-1-settlement %}). A thin order book can also move your average price before any charge applies, as the [bid-ask spread]({% post_url 2026-10-14-bid-ask-spread-and-liquidity %}) post shows.

## The arithmetic, line by line

```
Exchange transaction charge = traded value / 1,00,000 x {{ c.txn_per_lakh }}
SEBI turnover fee           = traded value / 1,00,00,000 x {{ c.sebi_fee_per_crore }}
STT                         = traded value x {{ c.stt_delivery_pct }}%
Stamp duty (buy only)       = traded value x {{ c.stamp_delivery_pct }}%
GST                         = {{ c.gst_pct }}% of the lines it applies to (assumed: brokerage only)
```

## Worked example: buy 100, sell 100

A hypothetical round trip in Desi Bites Foods, whose fictional IPO (initial public offering) price was ₹{{ ipo.price }}. The prices are **made up for illustration**, not market data, and the ₹{{ c.brokerage_each }} brokerage is invented too.

You buy {{ c.qty }} shares at ₹{{ c.buy_px }} (₹{% include inr.html n=b.value %}), then sell {{ c.qty }} shares at ₹{{ c.sell_px }} (₹{% include inr.html n=s.value %}). The price difference is ₹{% include inr.html n=c.gross_gain %}.

| Line | Buy side (₹) | Sell side (₹) |
|---|---:|---:|
| Traded value | {{ b.value }} | {{ s.value }} |
| Brokerage | {{ b.fmt.brokerage }} | {{ s.fmt.brokerage }} |
| Exchange transaction charge | {{ b.fmt.txn }} | {{ s.fmt.txn }} |
| SEBI turnover fee | {{ b.fmt.sebi }} | {{ s.fmt.sebi }} |
| STT | {{ b.fmt.stt }} | {{ s.fmt.stt }} |
| Stamp duty | {{ b.fmt.stamp }} | {{ s.fmt.stamp }} |
| GST on brokerage (assumed base) | {{ b.fmt.gst }} | {{ s.fmt.gst }} |
| **Total charges** | **{{ b.fmt.total }}** | **{{ s.fmt.total }}** |

Add the two sides: ₹{{ c.total_fmt }} of charges against a ₹{% include inr.html n=c.gross_gain %} price difference. That leaves ₹{{ c.net_fmt }} before depository charges and before any income tax on the gain, and the charges took {{ c.charges_pct_of_gross }}% of the price difference. STT alone was ₹{{ c.stt_total_fmt }}, more than half of the total.

The rounding is per line, to the paisa, and the totals add the rounded lines, so you can recompute every cell. Real contract notes may round differently.

## Common mistakes

- **Reading only the brokerage.** A "zero brokerage" plan removes one line. The taxes and the exchange and SEBI fees remain, and the example shows STT is the biggest of them on a delivery trade.
- **Comparing the price difference with the cost, not the net.** A move of ₹{{ c.sell_px | minus: c.buy_px }} a share can look comfortable until all lines are added. The effect is largest when the price barely moves.
- **Assuming every trade has the same STT.** The rate depends on the type of trade, as NSE's circular lists. A rate for delivery trades does not carry over to intraday or derivatives trades.
- **Treating one broker's contract note as the rule.** Brokerage and the base used for GST are the broker's own; the exchange and government lines come from circulars. Read the note and the broker's price list together.

*Rates are as described in NSE circulars {{ c.stt_circular }} and {{ c.txn_circular }}, and NSE's investor page "SEBI Turnover Fees, STT and Other levies" (updated {{ c.levies_updated }}). The circulars' PDFs could not be re-opened at the last check; verify before relying on any rate. Prices and brokerage in the example are illustrative.*

**Takeaway:** A contract note is brokerage plus exchange and SEBI fees plus taxes, and on a delivery trade the taxes can be the largest lines. Add every line, both sides, before judging a trade's result; the rates are in the circulars and can change, so check the current rule.
