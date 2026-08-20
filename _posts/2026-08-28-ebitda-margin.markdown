---
layout: post
title: "EBITDA Margin: how the core business performs, before financing and accounting choices"
date: 2026-08-28 09:00:00 +0530
series: jargon
---

{% assign db25 = site.data.case_study.income_statement.FY25 %}
{% assign bi25 = site.data.real_company.income_statement.FY25 %}
{% assign bi24 = site.data.real_company.income_statement.FY24 %}

## What EBITDA margin means

**EBITDA** — Earnings Before Interest, Tax, Depreciation & Amortisation — is
a checkpoint one step further down the waterfall than gross profit: revenue,
minus the direct cost of what was sold ([COGS]({% post_url 2026-08-22-reading-an-income-statement %})), minus the day-to-day cost
of running the business (salaries, distribution, admin), but before the
company's financing decisions (interest), tax, or the accounting effect of
its assets ageing (depreciation) enter the picture. We defined the full
waterfall in [Reading an Income Statement]({% post_url 2026-08-22-reading-an-income-statement %}) — EBITDA margin is just
that EBITDA line expressed as a percentage of revenue.

The point of stopping *here* specifically: it's the cleanest read on how the
core operating business is doing, stripped of two things that have nothing
to do with how good the business itself is — how it's financed (debt vs
equity) and how its accountants choose to depreciate its assets.

## The formula

```
EBITDA Margin (%) = EBITDA / Revenue × 100
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Revenue | {{ db25.revenue }} |
| EBITDA | {{ db25.ebitda }} |
| **EBITDA Margin** | **{{ db25.ebitda | times: 100.0 | divided_by: db25.revenue | round: 1 }}%** |

## Worked example: Britannia Industries, FY25

Same source as always for the real-company half of this series: Britannia
Industries' [audited consolidated results for FY25](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only, not a
signal to act on.

| | ₹ Crore |
|---|---:|
| Revenue from operations | {{ bi25.revenue }} |
| EBITDA (revenue − COGS − operating opex) | {{ bi25.ebitda }} |
| **EBITDA Margin** | **{{ site.data.real_company.ratios.FY25.ebitda_margin }}%** |

FY24's EBITDA margin, from the same filing, was {{ bi24.ebitda | times: 100.0 | divided_by: bi24.revenue | round: 1 }}% —
again a touch richer than FY25. That tracks the same story as [Gross Margin]({% post_url 2026-08-26-gross-margin %}):
the compression starts at the raw-material line and mostly carries through,
since operating expenses (the other thing between gross profit and EBITDA)
moved by less.

## Common mistakes

- **Treating EBITDA margin as a cash margin.** EBITDA excludes depreciation
  because it's a non-cash accounting entry — but that doesn't mean EBITDA
  *is* cash. Working capital changes (unpaid customer invoices, growing
  inventory) can still mean healthy EBITDA and weak actual cash — that's
  what the [cash flow statement]({% post_url 2026-08-24-reading-a-cash-flow-statement %}) is for.
- **Using it to compare companies with very different asset intensity.** A
  company that leases most of its equipment and a company that owns a heavy
  factory outright can show similar EBITDA margins while having very
  different real economics — depreciation (which EBITDA ignores) is exactly
  where that difference would show up.
- **Ignoring debt entirely because EBITDA excludes interest.** EBITDA margin
  tells you nothing about whether a company can actually service its debt —
  a highly leveraged company can have a great EBITDA margin and still be in
  financial trouble once interest and debt repayment are due.
- **Reading a single year as the whole story.** As with gross margin, one
  year's EBITDA margin can move on input costs alone — worth checking
  against at least one prior year, as above, before drawing a conclusion.

**Takeaway:** EBITDA margin isolates how the core operating business is
doing, before financing and depreciation choices — useful for comparing
operating performance, but it is not a cash number and says nothing about a
company's ability to service its debt.
