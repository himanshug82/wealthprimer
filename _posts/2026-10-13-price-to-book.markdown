---
layout: post
title: "P/B: how much the market pays over accounting net worth"
date: 2026-10-13 09:00:00 +0530
series: jargon
---

{% assign listing = site.data.case_study.listing %}
{% assign bi_market = site.data.real_company.market %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign bi_bvps = bi_bs25.total_equity_owners | divided_by: bi_market.shares_outstanding_cr %}
{% assign db_pb = listing.ipo_price | divided_by: listing.book_value_per_share | round: 2 %}
{% assign bi_pb = bi_market.price | divided_by: bi_bvps | round: 2 %}

## What P/B means

[Book Value per Share]({% post_url 2026-10-07-book-value-per-share %}) told us what a share is worth on the accounting
books. **P/B — Price-to-Book** — closes that gap: how many rupees is the
market paying for each rupee of that accounting net worth?

## The formula

```
P/B = Price per Share / Book Value per Share
```

## Worked example: Desi Bites Foods Ltd

| | |
|---|---:|
| IPO Price | ₹{{ listing.ipo_price }} |
| ÷ Book Value per Share | ₹{{ listing.book_value_per_share }} |
| **P/B** | **{{ db_pb }}x** |

## Worked example: Britannia Industries

Price is the same {{ bi_market.price_date }} NSE closing price used throughout this
module. For illustration only.

| | |
|---|---:|
| Price ({{ bi_market.price_date }}) | ₹{{ bi_market.price }} |
| ÷ Book Value per Share | ₹{{ bi_bvps | round: 2 }} |
| **P/B** | **{{ bi_pb }}x** |

{{ bi_pb }}x is a striking number — the market is paying over thirty times
Britannia's accounting net worth per share. That's not a mispricing; it
follows directly from something this series already established. Back in
the [ROE post]({% post_url 2026-09-01-roe %}), Britannia's return on equity was over 50% — the
company earns far more on its book equity every year than the book equity
itself is worth. A business that can do that is worth much more than its
accounting net worth, and a high P/B is simply the market's way of pricing
that in. High ROE and high P/B tend to travel together, and this is exactly
why.

## Common mistakes

- **Reading high P/B as automatically expensive, without checking ROE
  alongside it.** As above, a high P/B paired with a high ROE is a
  coherent, expected combination — not a red flag on its own.
- **Comparing P/B across asset-light and asset-heavy businesses.** A
  brand-driven FMCG company or a services business carries most of its real
  value off the balance sheet (brand, customer relationships, know-how) —
  book value mechanically understates it, inflating P/B for reasons that
  have nothing to do with overvaluation.
- **Treating low P/B as automatically a bargain.** A company with a low
  ROE and a low P/B can simply be a weak business priced accordingly — not
  a value opportunity.
- **Forgetting book value can be stale.** Assets carried at decades-old
  historical cost (a factory bought long ago, still on the books at its
  original price) can understate what a company's assets are actually
  worth today — distorting P/B in the opposite direction from the brand-value
  issue above.

**Takeaway:** P/B measures how much the market pays over a company's
accounting net worth — a high number, like Britannia's here, usually just
reflects a high return on that equity, so P/B is best read together with
ROE rather than as a standalone verdict on whether a stock is cheap or
expensive.
