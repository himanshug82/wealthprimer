---
layout: post
title: "NIM and the spread: a bank's gross margin, measured in basis points"
description: "Net interest margin is a bank's gross margin: yield on what it lends minus what it pays for the money. How to compute it, and why the basis changes the answer."
image: /assets/og/nim-and-the-spread.png
date: 2026-10-11 09:00:00 +0530
series: fundamental-analysis
term: "NIM (net interest margin)"
---

{% assign b = site.data.real_bank %}
{% assign f25 = b.reported.FY25 %}
{% assign f24 = b.reported.FY24 %}
{% assign a = b.averages %}
{% assign d = b.derived_fy25 %}
{% assign q = b.nim_q4_fy25_reported %}
{% assign avg_assets_lakh_cr = a.avg_total_assets | divided_by: 100000 | round: 1 %}
{% assign nii_lakh_cr = f25.net_interest_income | divided_by: 100000 | round: 2 %}

## The margin, when the product is money

The [last post]({% post_url 2026-10-10-why-ratios-break-on-a-bank %}) set up
the bank's P&L: interest earned, minus interest expended, equals **net
interest income (NII)**. That is the rupee figure. The question every
analyst asks next is the same one asked of a manufacturer's
[gross margin]({% post_url 2026-08-26-gross-margin %}): *as a percentage of
what?*

For a manufacturer the denominator is revenue. For a bank, the natural base
is the pile of assets that earn the interest — the loans and the investment
book. NII as a percentage of that pile is the **net interest margin (NIM)**.

```
NIM  =  Net interest income  /  Average interest-earning assets

which decomposes into

Yield on assets   =  Interest earned    /  Average interest-earning assets
Cost of funds     =  Interest expended  /  Average (deposits + borrowings)
Spread            =  Yield on assets  −  Cost of funds
```

NIM and spread are close cousins but not identical: spread compares two
different bases (earning assets vs. funding), NIM puts the net figure over one
base. Banks quote NIM; analysts often back out the spread to see *which side*
moved.

Two words in the formula matter enormously: **average** and
**interest-earning**. The balance sheet is a snapshot at 31 March; the
interest was earned over twelve months on whatever balances existed each day.
Using year-end balances instead of averages, or total assets instead of the
assets that actually earn interest, gives a different — usually lower — number.
Which is exactly what happens below.

## Worked example: HDFC Bank, FY25

From HDFC Bank's [results for the year ended 31 March 2025]({{ b.company.source_url }})
(standalone, audited; released 21 April 2025). ₹ crore, historical, for
illustration only.

Step 1 — the averages. Only two year-ends are in the filing, so the average is
(opening + closing) / 2:

| | 31 Mar 2024 | 31 Mar 2025 | Average |
|---|---:|---:|---:|
| Advances | {% include inr.html n=f24.advances %} | {% include inr.html n=f25.advances %} | {% include inr.html n=a.avg_advances %} |
| Investments | {% include inr.html n=f24.investments %} | {% include inr.html n=f25.investments %} | {% include inr.html n=a.avg_investments %} |
| **Interest-earning assets (approx.)** | | | **{% include inr.html n=a.avg_interest_earning_assets %}** |
| Deposits | {% include inr.html n=f24.deposits %} | {% include inr.html n=f25.deposits %} | {% include inr.html n=a.avg_deposits %} |
| Borrowings | {% include inr.html n=f24.borrowings %} | {% include inr.html n=f25.borrowings %} | {% include inr.html n=a.avg_borrowings %} |
| **Funding** | | | **{% include inr.html n=a.avg_funding %}** |
| Total assets | {% include inr.html n=f24.total_assets %} | {% include inr.html n=f25.total_assets %} | {% include inr.html n=a.avg_total_assets %} |

Step 2 — the ratios:

| | Computation | Result |
|---|---|---:|
| Yield on interest-earning assets | {% include inr.html n=f25.interest_earned %} / {% include inr.html n=a.avg_interest_earning_assets %} | **{{ d.yield_on_interest_earning_assets_pct }}%** |
| Cost of funds | {% include inr.html n=f25.interest_expended %} / {% include inr.html n=a.avg_funding %} | **{{ d.cost_of_funds_pct }}%** |
| Spread | {{ d.yield_on_interest_earning_assets_pct }} − {{ d.cost_of_funds_pct }} | **{{ d.spread_pct }}%** |
| NIM on interest-earning assets | {% include inr.html n=f25.net_interest_income %} / {% include inr.html n=a.avg_interest_earning_assets %} | **{{ d.nim_on_avg_interest_earning_assets_pct }}%** |
| NIM on total assets | {% include inr.html n=f25.net_interest_income %} / {% include inr.html n=a.avg_total_assets %} | **{{ d.nim_on_avg_total_assets_pct }}%** |

So: the bank earned about {{ d.yield_on_interest_earning_assets_pct }}% on what
it lent and paid about {{ d.cost_of_funds_pct }}% for the money, keeping a
spread of roughly {{ d.spread_pct }} percentage points — three-and-a-bit
rupees out of every hundred lent, before running costs and bad loans.

## Why the bank's own number is different

HDFC Bank's release quotes, for the March 2025 quarter:

> "{{ q.on_total_assets }}% on total assets, and {{ q.on_interest_earning_assets }}% based on interest earning assets. Excluding ₹ {{ q.tax_refund_interest_bn }} bn of interest on income tax refund, core net interest margin was at {{ q.core_on_total_assets }}% on total assets, and {{ q.core_on_interest_earning_assets }}% based on interest earning assets."

Our full-year figure on total assets is {{ d.nim_on_avg_total_assets_pct }}%,
against the bank's {{ q.on_total_assets }}% for the quarter. The gap is not an
error on either side. It comes from three things worth knowing, because they
apply to *every* bank you'll ever read:

1. **Averaging basis.** The bank uses average *daily* balances; we used two
   year-end snapshots. When a balance sheet grows through the year, the
   two-point average can overstate the base and understate the margin.
2. **Period.** The bank's figure is for one quarter, annualised; ours is the
   whole year. Margins move within a year as rates change.
3. **Definition of the base.** Our "interest-earning assets" is advances plus
   investments; the bank's includes some balances with RBI and other banks
   that also earn interest, and excludes items that don't. Note too that
   "interest earned" includes interest on bank balances and on tax
   refunds, which our narrower base leaves out.

The lesson isn't that one number is right. It's that **NIM is only comparable
on a stated basis** — and a filing will usually tell you the basis if you read
the footnote. Comparing Bank A's "NIM on interest-earning assets" with Bank B's
"NIM on total assets" is comparing two different things.

## Why 3.5% is a lot

A margin of three-and-a-half percent sounds like a rounding error next to
Britannia's {{ site.data.real_company.ratios.FY25.gross_margin }}% gross
margin. The base makes the difference.

Average total assets of about ₹{{ avg_assets_lakh_cr }} lakh crore, at a NIM
of {{ d.nim_on_avg_total_assets_pct }}%, is ₹{{ nii_lakh_cr }} lakh crore of
net interest income — ₹{% include inr.html n=f25.net_interest_income %} crore.
Put another way: for every ₹1 lakh sitting on the balance sheet, the bank
earned about ₹{% include inr.html n=d.nii_per_lakh_of_avg_assets %} of
net interest in the year.

It also means small moves are big money. If NIM had been 10 basis points
(0.10 percentage points) lower for the year, NII would have been roughly
₹{% include inr.html n=d.nii_per_10bp_cr %} crore lower — about
{{ d.nii_per_10bp_as_pct_of_pat }}% of the year's profit after tax, from a change most people would not notice
in a headline. This is why bank results are reported, and read, in basis
points.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Suppose you run a stall that sells water bottles. You buy each bottle for
₹9.05 and sell it for... wait, no: you *borrow* each bottle for ₹5.64 a year
and *rent it out* for ₹9.05 a year. You keep about ₹3.41 per bottle.

₹3.41 is not much. But say each bottle is a ₹100 bottle, and you are renting
out **₹39 lakh crore worth** of them. Suddenly ₹3.41 on every one is an
enormous amount of money — and if the price of borrowing
bottles goes up by just 10 paise, you lose a fortune.

That's a bank. Tiny margin, unimaginable volume, and every paisa matters.

</details>

## What moves NIM

NIM is not a fixed property of a bank; it moves with the interest-rate cycle,
and the two sides of the spread move at different speeds.

- **Loans reprice faster than deposits when rates rise.** Since October
  2019 the RBI has required new floating-rate retail and MSME loans to be
  linked to an external benchmark (the repo rate, for example), and those
  reset within months. Fixed deposits stay at the old rate until
  they mature. So when rates go up, yield rises before cost of funds does and
  NIM widens — temporarily.
- **The reverse when rates fall.** Yields drop quickly; the bank is still
  paying last year's deposit rates. NIM compresses, again temporarily.
- **Funding mix.** A bank funded mostly by low-cost current and savings
  accounts has a structurally lower cost of funds than one funded by
  wholesale borrowings. That is the next post, on CASA.
- **Asset mix.** Unsecured retail loans yield more than home loans, which
  yield more than government bonds. A bank can raise its NIM by lending
  riskier — which is not the same as being a better bank, and the NPA post
  later in this module is about the bill for that.

None of this says where HDFC Bank's margin is going. It says what to watch
when it moves.

## Common mistakes

- **Comparing NIMs quoted on different bases.** Total assets vs.
  interest-earning assets, quarterly vs. annual, reported vs. "core." Read
  the footnote first.
- **Treating a rising NIM as pure good news.** It can mean cheaper funding
  (good), a rate cycle that will reverse (temporary), or a shift into riskier
  lending (the cost arrives later, in provisions).
- **Computing NIM from year-end balances and calling it "the" NIM.** As
  above: {{ d.nim_on_avg_total_assets_pct }}% vs. {{ q.on_total_assets }}%
  from the same company and the same year. State the basis.
- **Ignoring the base.** A bank with a lower NIM on a much larger, safer
  balance sheet can earn more, more reliably, than a bank with a higher NIM.
  Margin is one term of a product; the price-to-book post later in this
  module puts the terms together.

**Takeaway:** NIM is a bank's gross margin — what it earns on what it lends
minus what it pays for the money, on a base of lakhs of crores. The same
NII can come out as {{ d.nim_on_avg_total_assets_pct }}% or {{ q.on_total_assets }}% depending on the base and period,
so the first question about any NIM is "measured on what?"
