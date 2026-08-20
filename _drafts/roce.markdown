---
layout: post
title: "ROCE (Return on Capital Employed): return on ALL the money in the business, not just shareholders'"
series: jargon
---

{% assign db_bs24 = site.data.case_study.balance_sheet.FY24 %}
{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
{% assign bi_bs24 = site.data.real_company.balance_sheet.FY24 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}
{% assign db_ce24 = db_bs24.equity | plus: db_bs24.term_loan %}
{% assign db_ce25 = db_bs25.equity | plus: db_bs25.term_loan %}
{% assign bi_ce24 = bi_bs24.total_equity | plus: bi_bs24.total_borrowings %}
{% assign bi_ce25 = bi_bs25.total_equity | plus: bi_bs25.total_borrowings %}

## What ROCE means

[ROE]({% post_url 2026-09-01-roe %}) only looks at shareholders' own money. But most companies run partly
on borrowed money too — a term loan, working capital debt. **ROCE — Return
on Capital Employed** — asks the bigger question: how much profit did the
business generate on *all* the capital invested in it, whether that capital
came from shareholders or lenders?

**Capital Employed** = Equity + Borrowings — everyone who's put long-term
money into the business, not just its owners. And because that capital
belongs to lenders too (who get paid via interest, before shareholders see
anything), ROCE uses **EBIT** — profit before interest and tax — instead of
PAT, so the return isn't already net of what's owed to one of the two groups
who supplied the capital.

## The formula

```
ROCE (%) = EBIT / Average Capital Employed × 100
Capital Employed = Total Equity + Total Borrowings
```

As with ROE, we average the opening and closing capital employed rather than
using the closing figure alone.

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| EBIT (FY25) | {{ db_is25.ebit }} |
| Capital employed, start of year (FY24) | {{ db_ce24 }} |
| Capital employed, end of year (FY25) | {{ db_ce25 }} |
| Average capital employed | {{ db_ce24 | plus: db_ce25 | divided_by: 2.0 }} |
| **ROCE** | **{{ site.data.case_study.ratios.FY25.roce }}%** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). Total equity here includes
non-controlling interests, since capital employed is a whole-business
measure, not an owners-only one. For illustration only.

| | ₹ Crore |
|---|---:|
| EBIT (FY25) | {{ bi_is25.ebit }} |
| Capital employed, start of year (FY24) | {{ bi_ce24 }} |
| Capital employed, end of year (FY25) | {{ bi_ce25 }} |
| Average capital employed | {{ bi_ce24 | plus: bi_ce25 | divided_by: 2.0 }} |
| **ROCE** | **{{ site.data.real_company.ratios.FY25.roce }}%** |

Notice Britannia's ROCE ({{ site.data.real_company.ratios.FY25.roce }}%) is close to, but a little below, its
[ROE]({% post_url 2026-09-01-roe %}) ({{ site.data.real_company.ratios.FY25.roe }}%) from the previous post. That's actually a
reassuring pattern, not a red flag — it means the strong ROE isn't being
artificially pumped up by heavy borrowing; the company earns a genuinely
high return on capital regardless of who supplied it.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine two friends open identical lemonade stands. Friend A used ₹1,000 of
her own savings. Friend B used ₹500 of his own savings and ₹500 borrowed
from his dad. If both stands make the exact same ₹300 profit before paying
dad back any interest, judging them only on "return on my own money" makes
Friend B look like the better businessman — his ₹500 "earned" 60%, versus
Friend A's ₹1,000 earning 30%. But that's not because Friend B ran a better
stand — it's because he used less of his own money. ROCE looks at the
₹1,000 total in *both* stands, so it judges the lemonade-selling skill
itself, not who financed it.

</details>

## Common mistakes

- **Comparing ROCE across companies with very different debt levels without
  also checking ROE.** If ROCE is healthy but ROE is dramatically higher,
  leverage is doing a lot of the work — worth understanding before assuming
  the business itself is that efficient.
- **Using EBITDA instead of EBIT in the numerator.** EBITDA still includes
  the benefit of assets that are ageing and losing value — EBIT accounts for
  that, which is why ROCE specifically uses EBIT.
- **Using closing capital employed instead of average**, especially in a
  year with a large mid-year capital raise or debt repayment — this can
  distort the ratio significantly in either direction.
- **Treating a high ROCE as a reason to buy at any price.** ROCE measures
  business quality, not value for money — a genuinely excellent business can
  still be a poor investment if bought at too high a price. That's a
  separate question, covered in the Valuation module.

**Takeaway:** ROCE measures the return a business generates on *all* the
capital invested in it — equity and debt alike — making it a fairer way to
judge operating quality than ROE alone, which can be flattered by leverage.
