---
layout: post
title: "Reading a Balance Sheet, using a snacks company"
date: 2026-08-20 09:00:00 +0530
series: jargon
---

{% assign bs = site.data.case_study.balance_sheet.FY25 %}

## What a balance sheet is

A balance sheet is a photograph, not a video. It shows what a company owns
and owes **on one specific date** — not how it performed over the year, just
where it stood at the end of it. Everything else (the income statement, the
cash flow statement) tells you what happened *during* a period. The balance
sheet tells you where the company landed.

It's built on one equation that's true for every company, every time, with no
exceptions:

<div style="text-align:center; font-size:1.2em; margin: 1.5em 0;"><strong>Assets = Liabilities + Equity</strong></div>

What the company **owns** (assets) always equals what it **owes to others**
(liabilities) plus what it owes to its own shareholders (equity, sometimes
called "owners' funds" or "net worth"). If those two sides don't match, the
statement is wrong — there's no such thing as a balance sheet that doesn't
balance.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you buy a ₹50,000 scooter. ₹20,000 is your own savings, ₹30,000 is a
loan from your dad. The scooter (asset, ₹50,000) equals the loan you owe your
dad (liability, ₹30,000) plus your own money in it (equity, ₹20,000). Every
company's balance sheet is that same idea, just with more zeros.

</details>

## The three sections

**Assets** — what the company owns. Split into current assets (cash, or
things that'll turn into cash within a year, like inventory and money
customers owe you) and non-current assets (things that stick around longer,
like a factory).

**Liabilities** — what the company owes to outsiders. Same current/non-current
split: current liabilities are due within a year (like money owed to
suppliers), non-current liabilities aren't (like a multi-year loan).

**Equity** — what's left over for shareholders after you subtract liabilities
from assets. It's share capital (money shareholders originally put in) plus
reserves (profit the company has kept and reinvested instead of paying out).

## Worked example: Desi Bites Foods, FY25

Here's Desi Bites' balance sheet as of the end of FY25 (year ended 31 March).
Full three-year version, with FY22–FY24 for comparison, is on the
[case study page]({{ '/case-study/' | relative_url }}).

| | ₹ Lakh |
|---|---:|
| Net fixed assets (the plant) | {{ bs.net_fixed_assets }} |
| Inventory | {{ bs.inventory }} |
| Trade receivables (money distributors owe it) | {{ bs.receivables }} |
| Cash & bank | {{ bs.cash }} |
| **Total Assets** | **{{ bs.total_assets }}** |
| Equity (capital + reserves) | {{ bs.equity }} |
| Term loan | {{ bs.term_loan }} |
| Trade payables (money it owes suppliers) | {{ bs.payables }} |
| Other current liabilities | {{ bs.other_current_liabilities }} |
| **Total Liabilities + Equity** | **{{ bs.total_liab_eq }}** |

Read it left to right: Desi Bites owns ₹{{ bs.total_assets }}L worth of stuff.
₹{{ bs.equity }}L of that belongs to its own shareholders; the rest —
₹{{ bs.term_loan }}L in a term loan plus ₹{{ bs.payables | plus: bs.other_current_liabilities }}L
owed to suppliers and other short-term obligations — belongs to outsiders. Add
the shareholders' share and the outsiders' share together, and you get back
to total assets. That's the equation, working exactly as it should.

Notice the plant (net fixed assets) is by far the largest asset, and it's
funded by a mix of the term loan and shareholder money — which is a
completely normal way for a manufacturer to finance a factory. Compare that
to inventory and receivables, which are funded mostly by short-term supplier
credit (payables) — also normal, and the kind of relationship the
[Efficiency module]({{ '/' | relative_url }}) digs into later.

## Common mistakes

- **Treating assets as automatically good.** A company with more assets isn't
  automatically stronger — *how* those assets are financed matters just as
  much. Assets funded mostly by debt carry more risk than the same assets
  funded mostly by equity.
- **Confusing profit with cash.** The balance sheet's cash line is real cash.
  It is not the same thing as this year's profit — a company can be
  profitable on paper and still be short on cash (more on this when we get to
  the cash flow statement).
- **Ignoring the current vs non-current split.** A liability due next month
  is a very different risk from one due in seven years, even if the rupee
  amount is identical.
- **Not checking that it actually balances.** If you're ever building your
  own summary of a company's numbers from an annual report, this is the
  single best sanity check available — total assets must equal total
  liabilities plus equity, always.

**Takeaway:** a balance sheet is a snapshot of what a company owns versus what
it owes, on one specific day — and the two sides always match, by definition,
because equity is simply defined as whatever's left over.
