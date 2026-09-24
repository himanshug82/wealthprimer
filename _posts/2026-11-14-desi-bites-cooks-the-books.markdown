---
layout: post
title: "Desi Bites cooks the books: four tricks and the ratios that catch them"
description: "A fictional dressed-up FY26 beside the honest one: channel stuffing, capitalised expenses, a related-party gain, a write-back — and the ratios that expose each."
image: /assets/og/desi-bites-cooks-the-books.png
date: 2026-11-14 09:00:00 +0530
series: fundamental-analysis
term: "Red flags (forensic checks)"
---

{% assign c2 = site.data.case_study_2 %}
{% assign h = c2.fy26 %}
{% assign d = c2.fy26_dressed %}
{% assign t = d.techniques %}
{% assign hr = h.ratios %}
{% assign dr = d.ratios %}

## Two sets of accounts for the same year

Everything in this post is invented. Desi Bites Foods is fictional, and the
"dressed" FY26 below never happened even in the fiction — it's the same
business, the same cash, the same customers, with four cosmetic decisions
layered on by an imaginary management that wanted its first year as a
listed company to look better than it was. No real company is being
described, and the point is not that companies routinely do this. The point
is that each trick is *legal or nearly legal*, each one makes the statements
look better, and each one leaves a fingerprint that a reader with the ratios
from this blog's first thirty posts can find.

The honest FY26 is the one the [previous post]({% post_url 2026-11-13-reading-an-annual-report %})
introduced. Here is what management could have done instead.

## The four tricks

| Trick | What was done | Which line it flatters |
|---|---|---|
| **1. Channel stuffing** | Shipped ₹{% include inr.html n=t.channel_stuffing_revenue %} lakh of stock to distributors in the last week of March that nobody ordered, booked as sales | Revenue, gross profit, PAT |
| **2. Capitalising expenses** | Booked ₹{% include inr.html n=t.capitalised_opex %} lakh of marketing and repairs as "plant and equipment" instead of expensing it | Opex down, EBITDA up, capex up |
| **3. Related-party asset sale** | Sold old machinery with a book value of ₹{% include inr.html n=t.rp_asset_book_value %} lakh to a promoter-owned firm for ₹{% include inr.html n=t.rp_asset_sale_price %} lakh; the gain sits in "other income" | Other income, PBT |
| **4. Provision write-back** | Reversed ₹{% include inr.html n=t.provision_reversal %} lakh of accrued expenses through the P&L | Opex down, EBITDA up |

None of these involves a fake invoice or a missing rupee. Trick 1 is a
timing decision the auditor may or may not catch (this is exactly why
*revenue cut-off* is a standard Key Audit Matter). Trick 2 is a
classification judgement. Trick 3 is a real transaction at a generous
price. Trick 4 is an estimate being revised. That's what makes them worth
learning: the frauds that make headlines are usually these, done bigger and
for longer.

## Side by side

₹ lakh, FY26:

| | Honest | Dressed | Change |
|---|---:|---:|---:|
| Revenue | {{ h.revenue }} | {{ d.revenue }} | +{{ t.channel_stuffing_revenue }} |
| Operating expenses | {{ h.opex }} | {{ d.opex }} | −{{ t.capitalised_opex | plus: t.provision_reversal }} |
| **EBITDA** | **{{ h.ebitda }}** | **{{ d.ebitda }}** | +{{ d.ebitda | minus: h.ebitda }} |
| EBITDA margin | {{ hr.ebitda_margin }}% | {{ dr.ebitda_margin }}% | |
| Other income | {{ h.other_income }} | {{ d.other_income }} | +{{ d.related_party_gain }} |
| **PAT** | **{{ h.pat }}** | **{{ d.pat }}** | **+{{ dr.pat_uplift_vs_honest }}%** |
| EPS (₹) | {{ h.eps }} | {{ d.eps }} | |
| PAT growth on FY25 | {{ hr.pat_growth }}% | {{ dr.pat_growth }}% | |

![Honest vs dressed FY26]({{ '/assets/charts/fa2-honest-vs-dressed.svg' | relative_url }})

The honest year was already good: PAT up {{ hr.pat_growth }}%. The dressed year
reports PAT more than doubling. Every rupee of the difference is
presentation. The plant made the same namkeen and the same customers paid
for it.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Say you run a lemonade stand and your parents pay you based on your profit
for the summer.

You could sell more lemonade. Or, on the last day, you could pour fifty cups
and leave them with your friends, saying "pay me whenever" — and count all
fifty as sold. Your "sales" jump. The money doesn't arrive.

You could also decide that the money you spent on posters wasn't really a
cost — it was an "investment in the brand" — and leave it out of your
expenses. Profit goes up. The money is still gone.

Your parents, if they're sharp, will ask one question: *how much cash is
actually in the jar?* That question is what the rest of this post is about.

</details>

## The fingerprints

Each trick moves a P&L line. But the balance sheet and cash flow statement
have to keep balancing — the model behind this post asserts that both
versions do — and *that* is what leaves the marks. The
[cash flow post]({% post_url 2026-08-24-reading-a-cash-flow-statement %}) called
cash the statement that's hardest to fake; here is what that means in practice.

| Check | Honest | Dressed | What it catches |
|---|---:|---:|---|
| [OCF/PAT]({% post_url 2026-09-20-ocf-pat %}) | {{ hr.ocf_pat }}x | {{ dr.ocf_pat }}x | Profit rose {{ dr.pat_uplift_vs_honest }}%; operating cash rose {{ dr.cfo_uplift_vs_honest }}%. Tricks 1, 2 and 3 all inflate profit without producing cash |
| [Debtor days]({% post_url 2026-09-08-debtor-days %}) | {{ hr.receivable_days }} | {{ dr.receivable_days }} | Trick 1. Stuffed channels don't pay; receivables balloon against a 30-day credit policy |
| [Inventory days]({% post_url 2026-09-07-inventory-days %}) | {{ hr.inventory_days }} | {{ dr.inventory_days }} | Trick 1's mirror image. Stock "sold" in March leaves the warehouse, so inventory looks lean — a *fall* that's too good |
| [Capex intensity]({% post_url 2026-09-21-capex-intensity %}) | {{ hr.capex_intensity }}% | {{ dr.capex_intensity }}% | Trick 2. Capex jumps while the MD&A mentions no new capacity; the "asset" is last year's advertising |
| Other income ÷ PBT | {{ hr.other_income_pct_pbt }}% | {{ dr.other_income_pct_pbt }}% | Trick 3 hides here — same share, different *nature*. The notes reveal a gain on sale to a related party |
| Gross margin | {{ hr.gross_margin }}% | {{ dr.gross_margin }}% | Unchanged — stuffing adds revenue *and* cost. Not every ratio catches every trick |

Read the first row twice. **OCF/PAT is the single most useful forensic
ratio** because almost every way of flattering profit fails to flatter cash.
Channel stuffing books revenue nobody has paid for. Capitalising an expense
moves the cash outflow from operating to investing — the cash still leaves,
just under a different heading. A gain on selling an asset is non-cash from
the operating statement's point of view (the proceeds sit in investing). So
profit goes up and operating cash barely moves, and the ratio collapses from
{{ hr.ocf_pat }}x to {{ dr.ocf_pat }}x.

One year of OCF/PAT near 1 is unremarkable — working capital swings do that.
A *fall* in OCF/PAT in the same year profit *jumps* is the pattern.

## The one that doesn't show in a ratio

Trick 3 — the related-party sale — has the same "other income as a share of
PBT" in both versions, because the honest year also has a big other-income
line (interest on the IPO cash). The ratio doesn't catch it. **The note
does.** Ind AS 24 requires every transaction with a related party to be
listed: counterparty, relationship, amount. A line reading *sale of plant
and equipment to an entity controlled by the promoter, ₹55 lakh, carrying
value ₹20 lakh* is the whole story in one row.

That's the general lesson of this module. Ratios are the smoke detector.
The notes are where you find the fire. A related-party note that is long,
or that grew this year, or that involves the promoter's relatives'
businesses buying and selling things at odd prices, deserves more of your
time than any single ratio.

## Why this works on people

Because every number in the dressed accounts is *defensible*. The
distributors did receive the stock. Marketing does build a long-lived
brand. The machine was sold. The provision was an estimate. An analyst who
asks will get a plausible answer to each question separately. The pattern
only appears when you look at the four together, alongside the cash flow
statement, and notice that a company reporting its best-ever profit
generated roughly the same cash as it would have on a normal year.

There is also a tell in the timing. Trick 1 happens in the last week of the
year; trick 4 happens at year-end when estimates are revisited. A quarterly
pattern where Q4 is always the strongest quarter, and Q1 is always weak
because the channel is full, is worth a look — the
[next post]({{ '/series/fundamental-analysis/' | relative_url }}) is about reading
quarters.

## Common mistakes

- **Checking P&L ratios only.** Margins and growth are the *targets* of
  window-dressing. The evidence is on the balance sheet (receivables,
  fixed assets) and in the cash flow statement.
- **Treating one soft OCF/PAT year as a red flag.** Working capital is
  lumpy. The signal is a fall in cash conversion *coinciding* with a jump in
  profit, not a single reading.
- **Assuming the auditor would have caught it.** Each of these four is a
  judgement call inside the rules. Auditors test cut-off; they don't
  second-guess a capitalisation policy or the price a promoter's brother
  paid for a machine.
- **Being reassured by an improving ratio.** Inventory days *fell* in the
  dressed version. Too-good-to-be-true works in both directions.
- **Ignoring "other income."** For a snacks company, interest and gains on
  asset sales aren't the business. Strip them out before judging the year:
  Desi Bites' honest PAT excluding other income and the one-off charge is
  ₹{% include inr.html n=hr.pat_ex_other_income_and_exceptional %} lakh, not ₹{% include inr.html n=h.pat %} lakh.
- **Thinking this only happens at small companies.** Size changes the
  zeroes, not the techniques.

**Takeaway:** Four legal-looking tricks turned a good year into a
spectacular one on paper — revenue up, margins up, PAT more than doubled —
while operating cash flow barely moved. That gap is the tell. OCF/PAT
collapsing from {{ hr.ocf_pat }}x to {{ dr.ocf_pat }}x, debtor days jumping from {{ hr.receivable_days }} to {{ dr.receivable_days }}, and
a related-party line in the notes catch what the P&L was built to hide.
Profit is an opinion; cash is closer to a fact.
