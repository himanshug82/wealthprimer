---
layout: post
title: "Relative valuation: what a company is worth compared to whom"
description: "Valuing a company against its peers. How multiples-based valuation works in practice, how the peer set gets chosen, and the traps that make cheap look cheap."
image: /assets/og/relative-valuation-comparables.png
date: 2026-10-01 09:00:00 +0530
series: fundamental-analysis
---

{% assign listing = site.data.case_study.listing %}
{% assign m = site.data.real_company.multiples %}
{% assign bi_market = site.data.real_company.market %}
{% assign db_pe = listing.ipo_price | divided_by: listing.eps_diluted | round: 1 %}
{% assign db_pb = listing.ipo_price | divided_by: listing.book_value_per_share | round: 2 %}
{% assign db_evebitda = listing.ev | divided_by: 441.0 | round: 1 %}

## Two ways to answer "what is this worth"

There are broadly two families of valuation. The first works out what a
business is worth from its own future cash flows, in isolation — that's
**discounted cash flow (DCF)**, and it takes the next four posts to build
properly.
The second is quicker and much more widely used in practice: figure out what
the market is paying for *similar* businesses, and apply that to this one.

That's **relative valuation**, or valuation by comparables — "comps." It's
what people are doing whenever they say a stock looks expensive at 60 times
earnings. The logic is borrowed wholesale from property: nobody builds a
discounted cash flow model to price a two-bedroom flat in Powai. They look
at what the last three similar flats in the building sold for, adjust for
the floor and the view, and land on a number.

The whole method turns on one word in that sentence — *similar*. Get the
comparison set wrong and every number after it is decoration.

## The formula

There's no single formula, because relative valuation is a procedure rather
than a calculation:

```
1. Pick a peer set — companies genuinely comparable to the target
2. Pick a multiple  — P/E, P/B, EV/EBITDA, or a sector-specific one
3. Compute that multiple for every peer, on a consistent basis
4. Take the median (not the mean — one outlier ruins a mean)
5. Apply it to the target's own metric
6. Explain every gap between the target and that median
```

Step 6 is the actual work. Steps 1 to 5 are arithmetic.

## The multiples you already know

This blog has a post on each of the three workhorse multiples, so this is a
reference table rather than a re-explanation:

| Multiple | What it compares | Best for | Breaks down when |
|---|---|---|---|
| [P/E]({% post_url 2026-09-24-price-to-earnings %}) | Price to earnings per share | Profitable, stable companies | Earnings are negative, tiny, or distorted by one-offs |
| [P/B]({% post_url 2026-09-25-price-to-book %}) | Price to book value per share | Banks, financials, asset-heavy businesses | Most value is intangible (brands, software) |
| [EV/EBITDA]({% post_url 2026-09-26-ev-ebitda %}) | Enterprise value to operating profit | Comparing across different debt levels | Capex needs differ wildly between peers |

EV/EBITDA deserves a note here, because it's the one that most often belongs
in a comps table. P/E is computed on the equity value alone, so two identical
businesses with different borrowings will show different P/Es purely because
of how they're financed. [Enterprise value]({% post_url 2026-09-26-ev-ebitda %}) adds debt back and
strips cash out, which puts companies with different capital structures onto
a common footing. When your peer set has a mix of debt-laden and net-cash
companies, EV/EBITDA is usually the fairer comparison.

## Worked example: Desi Bites Foods Ltd at its IPO

Desi Bites listed at ₹{% include inr.html n=listing.ipo_price %} a share on {{ listing.listing_date }}. Here's the full
multiple set at that price, using the FY25 figures from the
[case study](/case-study/):

| Multiple | Calculation | Value |
|---|---|---:|
| P/E | ₹{% include inr.html n=listing.ipo_price %} / diluted EPS ₹{% include inr.html n=listing.eps_diluted %} | {{ db_pe }}x |
| P/B | ₹{% include inr.html n=listing.ipo_price %} / BVPS ₹{% include inr.html n=listing.book_value_per_share %} | {{ db_pb }}x |
| EV/EBITDA | EV ₹{% include inr.html n=listing.ev %} Lakh / EBITDA ₹441 Lakh | {{ db_evebitda }}x |

Notice how differently the same company looks depending on which lens you
pick. The P/E of {{ db_pe }}x reads as a fairly demanding growth valuation. The
EV/EBITDA of {{ db_evebitda }}x looks far more modest — because enterprise value
subtracts the ₹{% include inr.html n=listing.post_ipo_cash %} Lakh of cash sitting on the post-IPO balance sheet, most
of it the IPO proceeds themselves. Same company, same day, same price;
two defensible-looking answers.

That's not a flaw to be resolved. It's the method telling you something
real: a large chunk of what an investor pays at ₹{% include inr.html n=listing.ipo_price %} is cash, not
operating business, and any multiple that ignores the balance sheet will
miss that.

## Worked example: Britannia Industries

Same price and financials used across this blog's valuation posts — the NSE
close on {{ bi_market.price_date }}, against the
[audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf).
Historical, for illustration only.

| Multiple | Calculation | Value |
|---|---|---:|
| P/E | ₹{% include inr.html n=bi_market.price %} / EPS ₹90.45 | {{ m.pe }}x |
| P/B | ₹{% include inr.html n=bi_market.price %} / BVPS ₹{% include inr.html n=m.book_value_per_share %} | {{ m.pb }}x |
| EV/EBITDA | EV ₹{% include inr.html n=bi_market.ev_cr %} Cr / EBITDA ₹3,187.15 Cr | {{ m.ev_ebitda }}x |

## Why you cannot simply compare these two

Put the two tables side by side and the temptation is immediate:

| Multiple | Desi Bites | Britannia |
|---|---:|---:|
| P/E | {{ db_pe }}x | {{ m.pe }}x |
| P/B | {{ db_pb }}x | {{ m.pb }}x |
| EV/EBITDA | {{ db_evebitda }}x | {{ m.ev_ebitda }}x |

Britannia trades at nearly ten times the P/B and three times the EV/EBITDA.
The naive conclusion — one is cheap, one is expensive — is exactly the
mistake this post exists to prevent. Both companies make packaged food in
India. That is roughly where the similarity ends, and the gaps explain
almost the entire spread:

- **Return on equity.** From the [last post]({% post_url 2026-09-30-dupont-roe-decomposition %}),
  Britannia earns 52.5% on shareholders' equity against Desi Bites'
  34.0%. A business that compounds equity faster is *worth* a higher
  multiple of that equity. Much of the P/B gap is this and nothing more.
- **Scale and track record.** Britannia has a century of history, national
  distribution, and brands people ask for by name. Desi Bites is a
  fictional mid-sized manufacturer with three years of audited accounts.
- **The exchange and liquidity.** Desi Bites is listed on the SME
  (small and medium enterprise) platform,
  where shares trade thinly. Illiquidity means a buyer can't easily get out,
  and the market prices that in with a discount.
- **The cash distortion, again.** Desi Bites' EV/EBITDA is held down by IPO
  cash that hasn't yet been put to work. Britannia's balance sheet has no
  equivalent lump.

Every one of those is a reason the multiples *should* differ. Relative
valuation done properly isn't the act of noticing a gap — it's the work of
accounting for it, item by item, until you either understand the gap or
conclude that you can't.

## About the peer set

Two companies do not make a comps table. A real one needs four to six
genuine peers, each with their multiples computed on the same basis, from
their own filings — same fiscal year, same treatment of exceptional items,
same definition of EBITDA. That last point matters more than it sounds:
"EBITDA" is not a defined term under Indian accounting standards, and two
data providers will happily give you two different numbers for the same
company.

This post deliberately doesn't invent a peer table. Sourcing one properly
means opening five annual reports, and a fabricated table would teach the
method badly. If you're building one yourself, the peer test is worth
stating plainly: a genuine peer sells to similar customers, faces similar
input costs, needs a similar asset base, and grows at a broadly similar
rate. "Also listed under FMCG" — fast-moving consumer goods, a label broad
enough to cover both a biscuit maker and a shampoo maker — is not a peer test.

## Common mistakes

- **Comparing multiples across sectors.** A 60x P/E means something entirely
  different in fast-moving consumer goods than in cement. Sector norms exist
  for real reasons — growth rates, capital intensity, and the stability of
  earnings all differ.
- **Using the mean instead of the median.** One peer with a collapsed
  earnings figure and a 400x P/E will drag a mean somewhere useless. The
  median shrugs it off.
- **Mixing trailing and forward multiples in one table.** A trailing P/E on
  one company and a forward P/E on the next is not a comparison. Pick one
  basis and hold it across every row.
- **Forgetting that the whole sector can be mispriced.** Relative valuation
  tells you what a company is worth *relative to its peers*. If the entire
  sector is priced for perfection, the cheapest name in it is still priced
  against that same optimism. This is the structural limitation of the
  method, and it's precisely why the DCF posts that follow exist.
- **Treating a low multiple as a finding.** Companies usually trade cheaply
  for a reason — weaker growth, worse returns, governance concerns, or a
  business in structural decline. The cheap multiple is the beginning of the
  question, not the answer to it.

**Takeaway:** Relative valuation prices a company by asking what the market
pays for similar businesses — fast, intuitive, and only as good as the word
"similar." The number that comes out is never the finding; the explanation
for why your company differs from its peers is. And because the method
assumes the peers themselves are sensibly priced, it can never tell you
whether an entire sector has lost its mind.
