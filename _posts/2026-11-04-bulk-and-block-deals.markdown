---
layout: post
title: "Bulk and block deals, explained"
seo_title: "Bulk deal vs block deal: what each one means"
description: "A bulk deal is a day's trading above 0.5% of a company's shares; a block deal is one big trade in a special window. How they differ, on Desi Bites."
image: /assets/og/bulk-and-block-deals.png
date: 2026-11-04 09:00:00 +0530
series: jargon
term: "Bulk deal and block deal"
---

{% assign bb = site.data.jargon_m8.bulk_block %}
{% assign bk = bb.bulk %}
{% assign bl = bb.block %}
{% assign ds = bb.desi %}

## What bulk and block deals mean

News headlines say things like "a fund bought ₹X crore of a company in a bulk deal". The words *bulk* and *block* look like cousins. They are two different things, defined by two different rules from SEBI (the Securities and Exchange Board of India, the market regulator).

A **bulk deal** is a count of a day's trading. It covers every transaction in one stock on an exchange where the total quantity bought (or sold) is more than {{ bk.threshold_pct }}% of the company's listed equity shares. The total can be reached through one trade or many, in the normal market, during the day.

A **block deal** is a single large trade done in a separate trading window set aside for such trades, so that neither the buyer nor the seller is put at a disadvantage. In the circular's words, it is "execution of large trades through a single transaction".

Both are about size. The difference is that a bulk deal is *counted afterwards* from ordinary trading, while a block deal is *executed on purpose* in its own window.

This is a [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}) post. Rules below are as read from SEBI's texts on 1 November 2026; check the current text before relying on any limit.

## The rules side by side

| | Bulk deal | Block deal |
|---|---|---|
| What triggers it | Day's total in a stock is more than {{ bk.threshold_pct }}% of listed shares | A single trade placed in a block window |
| Where it trades | The normal market | A separate window: {{ bl.morning_window }} (morning) or {{ bl.afternoon_window }} (afternoon) |
| Size | Measured in shares, as a share of the company | Minimum order size ₹{{ bl.min_order_cr }} crore |
| Price | Whatever the market price was | Within {{ bl.band_pct }}% of a reference price (see below) |
| Delivery | Normal settlement | Every trade must result in delivery; it cannot be squared off or reversed |
| Disclosure | Brokers report the stock, client name, quantity and price immediately; the exchange publishes it the same day, after market hours | The exchange publishes the stock, client name, quantity and price the same day, after market hours |

Sources: the bulk-deal rule is paragraph 1.1 of Chapter 1 of SEBI's [Master Circular for Stock Exchanges and Clearing Corporations](https://www.sebi.gov.in/sebi_data/commondocs/dec-2024/RE_Chapter%201%20-%20Trading%20-%20NEW_p.pdf) (SEBI/HO/MRD-PoD2/CIR/P/2024/00181, 30 December 2024). The block-deal rules are in SEBI's circular [SEBI/HO/MRD/POD-III/CIR/P/2025/134, {{ bl.circular_date }}, "Review of Block Deal Framework"](https://www.sebi.gov.in/legal/circulars/oct-2025/review-of-block-deal-framework_97145.html), applicable from the 60th day after issue ({{ bl.applicable_from }} by our count). The October 2025 circular revised the earlier block-deal framework, so articles written before it may quote older limits.

## The tests

```
Bulk deal test:   shares bought (or sold) in a stock in one day
                  >  {{ bk.threshold_pct }}% × the company's listed equity shares

Block deal test:  one trade in a block window
                  order value  ≥  ₹{{ bl.min_order_cr }} crore
                  price        within {{ bl.band_pct }}% of the reference price

Reference price:  morning window    =  previous day's closing price
                  afternoon window  =  VWAP (volume-weighted average price) of cash-market trades between {{ bl.afternoon_vwap_window }}
```

VWAP counts each trade's price in proportion to its size (the [OBV and VWAP post]({% post_url 2026-10-21-obv-and-vwap %}) shows how it is built). The circular's text reads "+3%" in the copy I read; whether the range is one-sided or two-sided is worth confirming in the circular before you rely on it.

## Worked example: Desi Bites, hypothetical deals

Desi Bites is our [fictional case-study company]({{ '/case-study/' | relative_url }}). It has {% include inr.html n=ds.total_shares %} shares. For the block-deal part we assume its previous close was ₹{% include inr.html n=ds.ref_price %}, the price of its initial public offering (IPO) used as a stand-in. Every trade below is invented, for illustration only; no real market price or date is used.

**Bulk deal**

1. {{ bk.threshold_pct }}% of {% include inr.html n=ds.total_shares %} shares is {% include inr.html n=bk.threshold_shares %} shares. A day's trading above that is a bulk deal.
2. A fund buys {% include inr.html n=bk.day_trades[0] %}, then {% include inr.html n=bk.day_trades[1] %}, then {% include inr.html n=bk.day_trades[2] %} shares in three separate trades. The total is {% include inr.html n=bk.day_total %} shares, or {{ bk.day_total_pct }}% of the company. No single trade is large, but the day's total crosses the line, so it is reported as a bulk deal.
3. Had the fund bought exactly {% include inr.html n=bk.edge_total %} shares ({{ bk.edge_pct }}%), the total would *not* be "more than" {{ bk.threshold_pct }}%, and the rule would not apply.

**Block deal**

1. The minimum order is ₹{{ bl.min_order_cr }} crore. At ₹{% include inr.html n=ds.ref_price %} a share, that is {% include inr.html n=bl.min_shares_at_ref %} shares.
2. That is {{ bl.min_pct_of_company }}% of the whole company. Desi Bites' entire market value at that price is only ₹{% include inr.html n=ds.market_cap_cr %} crore. A block deal is plainly meant for much larger companies; a company this small could hardly use the window at all.
3. For a morning-window order, the price would have to sit within {{ bl.band_pct }}% of the reference price: from about ₹{% include inr.html n=bl.band_lo %} to ₹{% include inr.html n=bl.band_hi %}.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a school canteen that sells 100 samosas a day. If one kid buys a few samosas at 10 am, then a few more at 11, then a few more at lunch, and by the end of the day that one kid has bought a *lot* of the samosas, the canteen aunty writes the kid's name on a board. That is a **bulk deal**: nobody planned a big purchase, but the day's total got big.

A **block deal** is different. A teacher walks in and says, "I'll take 60 samosas for the whole class, in one go." The aunty serves that order at a special counter at a set time, at a price near the usual one, so nobody else's lunch gets messed up. Both mean "a lot of samosas". One is added up afterwards; the other is ordered in one lump on purpose.

</details>

## Common mistakes

- **Reading a deal as a signal.** The published data tells you who traded and how much, not *why*. Every deal has a buyer and a seller. A fund may be rebalancing, an index change may be forcing the trade, or a promoter may be selling to raise cash. "Smart money" is a story people tell afterwards, and the list is published after the market closes.
- **Treating "bulk" and "block" as synonyms.** One is a day's total measured against the company's share count; the other is a single trade in its own window at a controlled price. A bulk deal can be made of many small trades; a block deal cannot.
- **Forgetting the denominator.** "Bulk" is relative to the company's shares ({{ bk.threshold_pct }}% of them), not to a rupee amount. The same ₹{{ bl.min_order_cr }} crore can be a rounding error in a giant company and a third of a small one, as the Desi Bites numbers show.
- **Quoting old limits.** SEBI revised the block-deal framework in October 2025. A rule that an older article calls "the minimum" may no longer be the minimum.

**Takeaway:** A bulk deal is a day's trading above {{ bk.threshold_pct }}% of a company's shares, counted afterwards; a block deal is one large trade executed in its own window. Both are published after market hours, and neither tells you why the buyer or seller traded.
