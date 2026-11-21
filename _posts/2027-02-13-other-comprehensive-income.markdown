---
layout: post
title: "Other comprehensive income: profit that skips the P&L"
seo_title: "Other comprehensive income (OCI): meaning and example"
description: "Other comprehensive income holds gains and losses kept out of profit, like gratuity remeasurements. What goes in it under Ind AS 1, worked on Desi Bites."
image: /assets/og/other-comprehensive-income.png
date: 2027-02-13 09:00:00 +0530
series: jargon
term: "Other comprehensive income (OCI)"
---

{% assign o = site.data.jargon_m10.oci %}

## What OCI means

Under Ind AS (Indian Accounting Standards), the income statement has two
parts. The first ends in **profit or loss**, the figure behind
[EPS]({% post_url 2026-09-23-eps %}) (earnings per share) and the
[P/E ratio]({% post_url 2026-09-24-price-to-earnings %}) (price-to-earnings). The second, **other comprehensive income
(OCI)**, holds gains and losses that the standards keep *out* of profit.
Add the two and you get **total comprehensive income**: the change in
shareholders' equity in the year from everything except dealings with the
shareholders themselves.

Ind AS 1 (paragraph 7) defines OCI as items of income and expense "not
recognised in profit or loss as required or permitted by other Ind ASs",
and lists what it includes. This post goes through the common ones, with a
worked example. It's part of [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}),
and builds on the [income statement post]({% post_url 2026-08-22-reading-an-income-statement %}).

## What goes into OCI

From Ind AS 1, paragraph 7 (the list is longer; these are the ones most
often seen):

| Item | Typical cause |
|---|---|
| Remeasurements of defined benefit plans | Changes in the actuarial estimate of gratuity or pension owed to staff |
| Gains and losses on equity investments designated at fair value through OCI | A long-term stake whose value changes |
| Changes in revaluation surplus | Property or intangibles carried at revalued amounts |
| Translation differences | Converting a foreign subsidiary's accounts into rupees |
| The effective part of cash flow hedges | Gains and losses on hedges of future cash flows |

Paragraph 82A requires OCI to be shown in two groups: items that **will not
be reclassified** to profit or loss later, and items that **will be
reclassified** to profit or loss when specific conditions are met. The first
group never reaches profit; the second can arrive in profit in a later year.

```
Total comprehensive income  =  profit after tax  +  other comprehensive income (after tax)
```

## Worked example: Desi Bites, with a gratuity remeasurement added

[Desi Bites Foods]({{ '/case-study/' | relative_url }}) is fictional, and the
FY26 books the other posts use have no OCI. For this post only, suppose its
actuary's year-end valuation of the staff gratuity plan came in higher than
expected: a remeasurement loss. Gratuity is a lump sum many Indian employers owe
long-serving staff when they leave. The amount and the tax on it are
assumptions. Figures in ₹ lakh.

| ₹ lakh, FY26 | |
|---|---:|
| **Profit after tax** | **{{ o.pat }}** |
| *Items that will not be reclassified to profit or loss:* | |
| Remeasurement of the gratuity plan | {{ o.gratuity_remeasurement | replace: "-", "−" }} |
| Tax on it | {{ o.gratuity_tax }} |
| **Other comprehensive income** | **{{ o.total_oci | replace: "-", "−" }}** |
| **Total comprehensive income** | **{{ o.tci }}** |

EPS and the P/E are based on profit after tax, ₹{{ o.pat }} lakh, not on
total comprehensive income. The OCI items still change equity on the balance
sheet; they just don't pass through profit.

## Common mistakes

1. **Ignoring OCI because it's small.** For most companies it is, but a
   large actuarial loss, a foreign subsidiary or a big strategic stake can
   make it material. Check the second half of the income statement.
2. **Expecting every OCI item to show up in profit later.** Items in the
   "will not be reclassified" group, such as remeasurements of defined benefit
   plans like gratuity (Ind AS 1, paragraph 96), never reach profit or loss.
   The company's statement shows which items sit in which group.
3. **Comparing total comprehensive income with another company's profit.**
   They're different measures. Compare profit with profit, and OCI
   separately.

**Takeaway:** Other comprehensive income holds gains and losses that Ind AS
keeps out of profit, such as gratuity remeasurements and fair-value changes on
some equity stakes. It changes shareholders' equity without touching profit,
EPS or the P/E.

## Sources

- Ind AS 1, *Presentation of Financial Statements*, paragraphs 7, 82A and 96, read on 21 November 2026 in [a copy of the notified standard]({{ o.source_url }}) on the Companies Act Integrated Ready Reckoner, a third-party site, because the Ministry of Corporate Affairs' (MCA's) [Ind AS page](https://www.mca.gov.in/content/mca/global/en/acts-rules/ebooks/accounting-standards.html) refuses automated requests. Check against MCA's current text.
