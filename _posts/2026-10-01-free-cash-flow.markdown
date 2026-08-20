---
layout: post
title: "Free Cash Flow: what's actually left over to spend, save, or return to shareholders"
date: 2026-10-01 09:00:00 +0530
series: jargon
---

{% assign db_cf25 = site.data.case_study.cash_flow.FY25 %}
{% assign bi_cf25 = site.data.real_company.cash_flow.FY25 %}
{% assign bi_cf24 = site.data.real_company.cash_flow.FY24 %}
{% assign bi_fcf24 = bi_cf24.cfo | minus: bi_cf24.capex %}

## What free cash flow means

We closed the Leverage module by seeing that no single ratio told the whole
story on its own — it took several together. **Free Cash Flow (FCF)** opens
this module with a single number that does try to answer one very direct
question by itself: after running the business and paying for the capex
needed to keep it running (or growing), how much actual cash is left over —
free to pay dividends, pay down debt, buy back shares, or reinvest further?

It starts from [Cash from Operations (CFO)]({% post_url 2026-08-24-reading-a-cash-flow-statement %}), the cash the core
business actually generated, and subtracts capex — the cash spent
maintaining or expanding the company's plant and equipment.

## The formula

```
Free Cash Flow = CFO − Capex
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Cash from Operations | {{ db_cf25.cfo }} |
| − Capex | {{ db_cf25.cfi | abs }} |
| **Free Cash Flow** | **{{ site.data.case_study.ratios.FY25.fcf }}** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025), consolidated statement of cash
flows. For illustration only.

| | ₹ Crore |
|---|---:|
| Cash from Operations | {{ bi_cf25.cfo }} |
| − Capex | {{ bi_cf25.capex }} |
| **Free Cash Flow** | **{{ site.data.real_company.ratios.FY25.fcf }}** |

For context, FY24's FCF (same filing) was ₹{{ bi_fcf24 }} crore — so FCF actually
*rose* year on year, even though operating cash flow itself fell slightly
(₹{{ bi_cf24.cfo }} crore in FY24 versus ₹{{ bi_cf25.cfo }} crore in FY25). The reason is on the other
side of the formula — capex — which is exactly what the last post in this
module, Capex Intensity, digs into.

## Common mistakes

- **Confusing FCF with profit.** A company can report a healthy PAT and
  still generate weak or negative FCF, if profit is tied up in receivables
  and inventory, or if it's spending heavily on capex. FCF and PAT answer
  different questions.
- **Not distinguishing maintenance capex from growth capex.** A company
  cutting capex to flatter FCF in the short term, at the cost of an ageing
  plant or missed capacity expansion, can look temporarily stronger on this
  one number while quietly storing up a problem — this is the same warning
  from the [cash flow statement post]({% post_url 2026-08-24-reading-a-cash-flow-statement %}), worth repeating here.
- **Comparing FCF across companies of very different sizes without
  normalizing.** ₹2,000 crore of FCF means something very different for a
  company with ₹18,000 crore of revenue than for one with ₹1,800 crore —
  compare FCF as a share of revenue, or read it alongside the company's own
  history.
- **Reading a single year's FCF as the trend.** Capex is often lumpy — a
  big plant expansion completes one year and eases off the next — so one
  year's FCF swing doesn't necessarily mean anything structural has
  changed.

**Takeaway:** free cash flow is the cash genuinely left over after running
and maintaining the business — the closest thing to "money the company
could actually hand out" — but it needs at least one more year of context
to tell whether a swing came from the business improving or from capex
simply timing differently.
