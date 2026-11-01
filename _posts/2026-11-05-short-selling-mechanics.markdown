---
layout: post
title: "Short selling: how you sell what you don't own"
seo_title: "What is short selling? How it works in India"
description: "Short selling means selling shares you don't own yet and buying them back later. The mechanics, SEBI's framework and why losses can outrun the sale."
image: /assets/og/short-selling-mechanics.png
date: 2026-11-05 09:00:00 +0530
series: jargon
term: "Short selling"
---

{% assign ss = site.data.jargon_m8.short_selling %}

## What short selling means

Most people buy first and sell later. **Short selling** flips the order: you sell a stock first and buy it back afterwards. SEBI (the Securities and Exchange Board of India, the market regulator) defines it as "selling a stock which the seller does not own at the time of trade".

The idea is simple. If you sell at one price and later buy back at a lower price, the difference is your gain. If the price goes the other way, it is your loss. A short seller is exposed to the opposite risk of a buyer: the seller is hurt when the price *rises*.

Short selling is legal in India, within a framework. This post covers how it works mechanically. It does not suggest that anyone should do it, or that any stock is a candidate. It is part of [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}).

## What SEBI's framework says

SEBI's circular [SEBI/HO/MRD/MRD-PoD-3/P/CIR/2024/1, {{ ss.sebi_date }}, "Framework for Short Selling"](https://www.sebi.gov.in/legal/circulars/jan-2024/framework-for-short-selling_80448.html) sets out the broad rules (Annexure 3 of Chapter 1 of the exchanges' master circular, as restated). In summary:

| Point | What the framework says |
|---|---|
| Who may short | All classes of investors, retail and institutional |
| Naked short selling | Not permitted. Every investor must deliver the shares at settlement |
| Institutions | May not square off intraday; their trades are settled on a gross basis at the custodian |
| Eligible shares | Securities traded in the F&O (futures and options) segment; SEBI may review the list |
| Securities lending and borrowing (SLB) | A scheme to be in place to give "the necessary impetus to short sell" |
| Disclosure | Institutions must say upfront that an order is a short sale; retail investors may say so by the end of that trading day |
| Reporting | Brokers collect scrip-wise short positions and send them to the exchange before the next day's trading; exchanges publish them weekly |
| Failure to deliver | Exchanges must frame deterrent provisions against brokers |

The rows above are the framework as restated in the 5 January 2024 circular. It says SEBI may review the framework and the list of eligible stocks from time to time, so check the current text.

## How the trade works

Because the framework bans naked shorting, a short seller has two ways to meet the delivery obligation:

- **Buy back before the day ends.** The sale and the purchase cancel out, and nothing is left to deliver. This is the simplest route.
- **Borrow the shares.** To stay short beyond the day, the seller needs shares to deliver at settlement. The SLB scheme exists to let investors borrow shares from holders who lend them. Check the current terms, fees and eligibility with your broker or the exchange.

Either way the settlement cycle matters: shares sold today are due for delivery on the next trading day under [T+1 settlement]({% post_url 2026-10-16-t-plus-1-settlement %}).

## The arithmetic

```
Gain or loss on a short  =  (sale price − buy-back price) × shares
Gain or loss on a buy    =  (sale price − buy price) × shares      (mirror image)

Most a short can gain    =  sale proceeds   (the price cannot fall below zero)
Most a buyer can lose    =  the amount paid (the price cannot fall below zero)
Most a short can lose    =  no upper limit  (a price has no ceiling)
```

## Worked example: Desi Bites, hypothetical trade

Desi Bites is our [fictional case-study company]({{ '/case-study/' | relative_url }}). Suppose someone sells {{ ss.qty }} shares short at ₹{% include inr.html n=ss.sell_price %}. That brings in ₹{% include inr.html n=ss.proceeds %}. The price later moves, and they buy back to close. Brokerage, taxes and any cost of borrowing are left out. All numbers are invented, for illustration only.

| Price change before buy-back | Buy-back price | Short seller's gain (+) or loss (−) | A buyer at the same entry |
|---|---:|---:|---:|
{% for r in ss.rows -%}
{% assign sp = r.short_pl -%}{% assign lp = r.long_pl -%}
| {% if r.move_pct > 0 %}+{% else %}−{% endif %}{% if r.move_pct < 0 %}{% assign mv = r.move_pct | times: -1 %}{{ mv }}{% else %}{{ r.move_pct }}{% endif %}% | ₹{% include inr.html n=r.cover_price %} | {% if sp < 0 %}−₹{% assign v = sp | times: -1 %}{% include inr.html n=v %}{% else %}₹{% include inr.html n=sp %}{% endif %} | {% if lp < 0 %}−₹{% assign v = lp | times: -1 %}{% include inr.html n=v %}{% else %}₹{% include inr.html n=lp %}{% endif %} |
{% endfor %}
Read the last row against the first. The short seller's gain can never exceed the sale proceeds (the price can't go below zero), while a doubling of the price already wipes out the whole sale value (₹{% include inr.html n=ss.doubling_loss %}), and nothing stops the price going higher. A buyer's worst case is losing what they paid; the short seller's worst case has no ceiling. The two columns are mirror images at each price, but the *shape* of the risk is not.

The risk is also tied to [leverage and margin]({% post_url 2026-10-11-leverage-and-margin %}): a short position is normally taken with margin, so a loss can exceed the money you put up. A stock can also be halted at its [circuit limit]({% post_url 2026-10-15-circuit-limits-and-price-bands %}), which can make buying back harder just when you most want to.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Say your friend has a rare cricket card and you promise to give them one back next week. You *sell* your friend's card to a classmate today for ₹100. Next week you must find a card to hand back. If the card has dropped in price, you buy one for ₹60 and keep ₹40. If everyone suddenly wants that card and it costs ₹300 now, you still have to hand one back, and you are ₹200 poorer. And there's no rule that says the price can't go to ₹1,000. That is why "you must deliver" matters, and why the rules ban selling a card you have no way to hand back.

</details>

## Common mistakes

- **Thinking the loss is capped like a buyer's.** A buyer can lose at most 100% of what they paid. A short seller's loss grows as the price rises, with no ceiling.
- **Ignoring the delivery obligation.** Naked short selling is not permitted. Selling first without a plan to buy back or borrow the shares means a failure to deliver, and the framework requires exchanges to have deterrent provisions against brokers for exactly that.
- **Forgetting the costs on the other side.** The example above leaves out brokerage, taxes and borrowing costs. These reduce a short seller's result, and a position held for a long time carries them for longer.
- **Treating "short interest" or short-sale data as a verdict.** The weekly data the exchanges publish counts positions. It does not say whether the shorts are right.

**Takeaway:** Short selling means selling first and buying back later, and SEBI's framework permits it for all investors but bans naked shorting: the shares must be delivered. A buyer can lose at most what was paid; a short seller has no such limit.
