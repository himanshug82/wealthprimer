---
layout: post
title: "Enterprise value: what it would cost to buy the whole business, debt and all"
description: "Enterprise value is market cap plus debt minus cash: the price of the business, not just its shares. Desi Bites' Rs 8,000 lakh market cap is a Rs 6,520 lakh EV."
image: /assets/og/enterprise-value.png
date: 2026-12-07 09:00:00 +0530
series: jargon
term: "Enterprise value (EV)"
---

{% assign e = site.data.jargon_m6.ev %}
{% assign d = e.desi_bites %}
{% assign b = e.britannia %}

## What enterprise value means

[Market cap]({% post_url 2026-09-27-market-cap %}) is what all the *shares*
are worth. **Enterprise value (EV)** is what the whole *business* is worth to
someone buying it outright — because a buyer doesn't just get the shares.
They inherit the debt, which they'll have to repay, and they get the cash in
the bank, which they can pocket. So:

```
Enterprise value  =  Market cap  +  Debt  −  Cash and equivalents
```

Think of buying a house with a mortgage. The price you agree with the seller
is the "market cap" of their equity. But you're also taking over the loan, so
the true cost of the *house* is price plus outstanding mortgage. If the seller
leaves ₹2 lakh in a drawer as part of the deal, subtract that. EV is the price
of the house; market cap is the price of the seller's stake in it.

The [EV/EBITDA post]({% post_url 2026-09-26-ev-ebitda %}) used this without
dwelling on it. It deserves its own entry because the adjustment can be large,
can go either direction, and is the thing that makes EV-based multiples
comparable across companies with different amounts of debt.

## The formula, and why each term is there

| Term | Why it's included |
|---|---|
| **+ Market cap** | The equity — what shareholders would be paid |
| **+ Debt** (borrowings, short and long term) | The buyer assumes it; a lender has a claim on the business ahead of shareholders |
| **− Cash and liquid investments** | The buyer receives it; it isn't part of the operating business |

Stricter versions also add preference shares and minority interests and
subtract non-operating investments. For most listed Indian companies the
three-term version gets you almost all the way.

Because EV represents the claims of *both* lenders and shareholders, it should
be compared with profit measures that belong to both — EBIT (earnings before
interest and tax), EBITDA (the same, before depreciation and amortisation too),
revenue — and never with PAT (profit after tax), which belongs to shareholders
alone. That is the logic
behind pairing EV with EBITDA and market cap with earnings.

## Worked example: Desi Bites Foods Ltd, at listing

From the [case study](/case-study/)'s listing block. The IPO raised
₹1,600 lakh of fresh cash that sits on the balance sheet, which is what makes
this example instructive:

| ₹ lakh | |
|---|---:|
| Market cap ({{ site.data.case_study.listing.post_ipo_shares_lakh }} lakh shares × ₹640) | {% include inr.html n=d.market_cap_lakh %} |
| + Term loan | {{ d.debt_lakh }} |
| − Cash (post-IPO) | {% include inr.html n=d.cash_lakh %} |
| **= Enterprise value** | **{% include inr.html n=d.ev_lakh %}** |
| FY25 EBITDA | {{ d.ebitda_lakh }} |
| Market cap / EBITDA | {{ d.mcap_ebitda }}x |
| **EV / EBITDA** | **{{ d.ev_ebitda }}x** |

The market values Desi Bites' shares at ₹{% include inr.html n=d.market_cap_lakh %} lakh, but nearly a
quarter of that is cash the company is holding, not a snacks business. Strip
it out and a buyer is paying ₹{% include inr.html n=d.ev_lakh %} lakh for the operations — {{ d.ev_ebitda }}x
EBITDA rather than the {{ d.mcap_ebitda }}x the market cap alone suggests. Same
company, and a multiple that's a fifth lower once you count the cash.

## Worked example: Britannia Industries

Price ₹5,851 (NSE close, 30 June 2025; source: Yahoo Finance) against the
FY25 balance sheet from the
[audited results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025). For illustration only.

| ₹ crore | |
|---|---:|
| Market cap | {% include inr.html n=b.market_cap_cr %} |
| + Total borrowings | {% include inr.html n=b.borrowings_cr %} |
| − Cash and bank balances | {{ b.cash_and_bank_cr }} |
| − Current (liquid) investments | {% include inr.html n=b.current_investments_cr %} |
| **= Enterprise value** | **{% include inr.html n=b.ev_cr %}** |
| EV − market cap | {{ b.ev_minus_mcap_cr }} |
| **EV / EBITDA** | **{{ b.ev_ebitda }}x** |

Britannia's EV is *smaller* than its market cap, by ₹{{ b.ev_minus_mcap_cr | abs }} crore. That is
the [net debt/EBITDA post]({% post_url 2026-09-18-net-debt-ebitda %})'s
finding restated: the company holds slightly more cash and liquid investments
than it owes, so a buyer would be paid a little to take the balance sheet. At
Britannia's scale the adjustment is tiny — 0.1% of market cap — and EV/EBITDA
rounds to the same {{ b.ev_ebitda }}x either way. For Desi Bites it was a fifth. The
adjustment's *size* is company-specific; the *principle* isn't.

## Same market cap, three different prices

Three made-up companies, each with a market cap of 1,000:

| | Market cap | Debt | Cash | **EV** |
|---|---:|---:|---:|---:|{% for c in e.illustration %}
| {{ c.company }} | {% include inr.html n=c.market_cap %} | {{ c.debt }} | {{ c.cash }} | **{% include inr.html n=c.ev %}** |{% endfor %}

If all three earned the same EBITDA, a market-cap multiple would call them
equally priced. An EV multiple says C costs more than twice what A does. C's
shareholders own a thin slice of a heavily borrowed business; A's own a
business plus a pile of cash. Those aren't the same purchase, and only EV says
so.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your friend sells you her bicycle shop for ₹1,000. But the shop owes the bank
₹600, and you'll have to pay that. And there's ₹100 in the till, which is now
yours. What did the shop really cost you? ₹1,000 + ₹600 − ₹100 = ₹1,500.

That's enterprise value. The ₹1,000 is just what your friend's *share* of the
shop was worth.

</details>

## Common mistakes

- **Comparing EV with PAT, or market cap with EBITDA.** Match the numerator's
  claim-holders to the denominator's: EV ↔ EBIT/EBITDA/revenue; market cap ↔
  PAT/book value.
- **Forgetting to subtract cash.** For a cash-rich company this overstates
  the price of the business — by a fifth in Desi Bites' case.
- **Treating all cash as excess.** Some cash is needed to run the business
  (working capital). Analysts sometimes subtract only "surplus" cash; the
  simple version subtracts all of it. Know which you're using.
- **Ignoring debt-like items.** Lease liabilities, preference capital, and
  pension deficits behave like debt. For leasing-heavy businesses (retail,
  airlines) leaving them out understates EV materially.

**Takeaway:** Enterprise value is market cap plus debt minus cash — the cost
of the whole business rather than of its shares. Desi Bites' ₹8,000 lakh of
shares is a ₹6,520 lakh business once its IPO cash is netted off, which is why
EV, not market cap, is the right numerator whenever the denominator belongs to
lenders as well as shareholders.
