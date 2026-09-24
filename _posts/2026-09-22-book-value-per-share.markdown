---
layout: post
title: "Book Value per Share: what each share is worth on paper"
description: "What each share is worth on the books. Desi Bites lists on the exchange, and book value per share becomes the first ratio with a share price attached to it."
image: /assets/og/book-value-per-share.png
date: 2026-09-22 09:00:00 +0530
series: jargon
term: "Book value per share"
---

{% assign listing = site.data.case_study.listing %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign bi_market = site.data.real_company.market %}

## Desi Bites goes public

Every post so far has used Desi Bites Foods Pvt Ltd — a *private* company,
with no share price at all. That changes here. Shortly after FY25 closed,
Desi Bites converted to a public limited company and listed on the main board
of the NSE and BSE on {{ listing.listing_date }}, as **{{ listing.company_name_post_listing }}**. It raised fresh growth
capital through an IPO (initial public offering — the first time a company
sells shares to the public), issuing {{ listing.fresh_issue_shares_lakh }} lakh new shares at an IPO price of
₹{% include inr.html n=listing.ipo_price %}, on top of the {{ listing.pre_ipo_shares_lakh }} lakh shares that already existed. That's a
fictional event, invented for this series — but it's what makes the next
eight posts (Valuation & Market) possible, since valuation ratios need a
share price to work with.

## What book value per share means

**Book value per share (BVPS)** is the simplest of the valuation-adjacent
ratios, because it doesn't need a share price at all — just the [balance
sheet]({% post_url 2026-08-20-reading-a-balance-sheet %}) and the share count. It answers: if the company sold every
asset at its accounting value and paid off every liability, how much would
be left over for each share?

## The formula

```
Book Value per Share = Total Equity / Shares Outstanding
```

## Worked example: Desi Bites Foods Ltd, post-IPO

| | |
|---|---:|
| Post-IPO Equity (₹ Lakh) | {{ listing.post_ipo_equity }} |
| Post-IPO Shares Outstanding (Lakh) | {{ listing.post_ipo_shares_lakh }} |
| **Book Value per Share** | **₹{% include inr.html n=listing.book_value_per_share %}** |

Post-IPO equity is the FY25 closing equity (₹678 Lakh) plus the
₹{% include inr.html n=listing.ipo_proceeds %} Lakh raised in the fresh issue — the company's own accounting net
worth grew the moment it took in fresh shareholder capital.

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). Shares outstanding here (24.09
crore) is derived from reported EPS and PAT, and matches the reported
equity share capital at a face value of ₹1 — a consistency check, not a
separate estimate. For illustration only.

| | |
|---|---:|
| Total Equity, owners (₹ Crore) | {{ bi_bs25.total_equity_owners }} |
| Shares Outstanding (Crore) | {{ bi_market.shares_outstanding_cr }} |
| **Book Value per Share** | **₹{{ bi_bs25.total_equity_owners | divided_by: bi_market.shares_outstanding_cr | round: 2 }}** |

Genuinely a coincidence, not a designed one — Desi Bites' and Britannia's
book values per share land in a similar range (₹{% include inr.html n=listing.book_value_per_share %} and
₹{{ bi_bs25.total_equity_owners | divided_by: bi_market.shares_outstanding_cr | round: 2 }}) despite the two companies being wildly
different in scale. Book value per share depends entirely on how many
shares exist, which has nothing to do with how big or valuable a company
actually is — a reminder for the very first common mistake below.

## Common mistakes

- **Confusing book value with market value.** BVPS is an accounting number,
  not what the market thinks the company is worth. The gap between the two
  is exactly what P/B (the price-to-book ratio), a few posts from now,
  measures.
- **Not adjusting for share count changes.** A stock split doubles the share
  count and halves BVPS overnight, without changing anything real about the
  business — BVPS is only comparable across time if the share count is
  stable, or you adjust for splits.
- **Ignoring what isn't on the balance sheet.** A strong consumer brand,
  distribution reach, or customer loyalty — the things that actually make a
  company like Britannia valuable — mostly don't show up in book value at
  all. BVPS undersells genuinely brand-driven businesses by design.
- **Assuming rising BVPS is automatically bullish.** It usually just means
  retained profit is piling up — whether that profit is being reinvested
  well is a completely separate question BVPS can't answer on its own.

**Takeaway:** book value per share is what each share is worth on the
accounting books alone — a useful starting reference point, but on its own
it says nothing about what the market is actually willing to pay, which is
where the rest of this module goes next.
