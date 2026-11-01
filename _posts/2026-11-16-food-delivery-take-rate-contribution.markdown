---
layout: post
title: "Food delivery: take rate and contribution"
description: "A delivery platform keeps a slice of each order and pays costs out of it. Take rate and contribution explained with Eternal's FY26 food delivery figures."
image: /assets/og/food-delivery-take-rate-contribution.png
date: 2026-11-16 09:00:00 +0530
series: fundamental-analysis
term: "Take rate"
---

{% assign e = site.data.sectors2.eternal %}
{% assign d = e.derived %}
{% assign nov_q4_25 = e.nov.FY25[3] %}
{% assign contrib_q4_25 = e.contribution.FY25[3] %}

## What a take rate means

A food delivery platform doesn't cook or ride. It collects the money from the customer, passes most of it on to restaurants and delivery partners, and keeps a slice. The **take rate** is that slice as a share of the value of the orders — the platform's revenue per rupee of order value.

The measure has a catch, and it's the main thing to learn here: the answer depends on which "order value" is in the denominator and which "revenue" is in the numerator. Both are company-defined.

## The formulas

```
GOV  (gross order value)  =  order value before restaurant and platform discounts (the company's
                             definition adds delivery and platform fees and taxes)
NOV  (net order value)    =  GOV  −  all discounts (restaurant-, platform-, bank-funded)

Take rate     =  adjusted revenue / order value      (which value? check)
Contribution  =  adjusted revenue − delivery, payment, support, refund and other
                 order-level costs − platform-funded discounts
Contribution margin  =  contribution / order value
```

Eternal's own definitions, from the glossary of its Q4 FY26 shareholder letter: NOV is "GOV (−) all discounts (funded by restaurant, platform, bank, others)"; adjusted revenue is statutory revenue plus customer delivery charges and platform fees that sit outside revenue from operations because of the accounting standard Ind AS 115 (Indian Accounting Standard 115, revenue from contracts with customers); contribution is adjusted revenue less last-mile delivery, payment gateway, customer support, refund and other order-level costs, and platform-funded discounts. The company began reporting NOV, "in addition to GOV", from its Q4 FY25 letter (May 2025). In its [Q2 FY26 letter]({{ e.q2_letter_url }}) it said GOV is "a misleading measure of growth" and asked investors not to treat it as a proxy for growth.

## Worked example: Eternal's food delivery, FY26

From Eternal's [Q4 FY26 shareholder letter]({{ e.source_url }}) (which includes audited results) and, for the older GOV basis, its [Q4 FY25 letter]({{ e.fy25_letter_url }}). Food delivery segment, ₹ crore. FY26 is the year ended 31 March 2026. The FY26 quarters and Q4 FY25 are printed in the Q4 FY26 letter and the earlier FY25 quarters in the Q4 FY25 letter; the annual totals below are **our sums of the four printed quarters**, not company-printed full-year figures. Historical, for illustration only.

| ₹ crore | FY26 | FY25 |
|---|---:|---:|
| NOV | {{ d.nov_fy26 }} | {{ d.nov_fy25 }} |
| Adjusted revenue | {{ d.adj_rev_fy26 }} | {{ d.adj_rev_fy25 }} |
| Contribution | {{ d.contribution_fy26 }} | {{ d.contribution_fy25 }} |
| Adjusted EBITDA (earnings before interest, tax, depreciation and amortisation, adjusted by the company) | {{ d.adj_ebitda_fy26 }} | {{ d.adj_ebitda_fy25 }} |

### Step 1: growth, and the share kept

1. NOV rose {{ d.nov_growth_pct }}% over the year; in the March 2026 quarter alone it was up {{ d.q4_nov_growth_pct }}% (the letter prints 18.8%).
2. Adjusted revenue rose {{ d.adj_rev_growth_pct }}%, faster than NOV. Dividing one by the other gives {{ d.take_fy26 }}% in FY26 against {{ d.take_fy25 }}% in FY25, a rise of {{ d.take_change_pts }} percentage points. The Q4 FY26 letter doesn't print a take rate, so this is our ratio on its printed inputs, and the two sides aren't on the same footing: adjusted revenue includes delivery charges paid by customers and is before discounts the platform funds, while NOV is after all discounts. Read it as adjusted revenue per ₹100 of NOV, before delivery and discount costs, not as the slice the platform keeps.
3. Contribution rose {{ d.contribution_growth_pct }}%. As a share of NOV that is {{ d.contrib_pct_nov_fy26 }}% against {{ d.contrib_pct_nov_fy25 }}%, up {{ d.contrib_change_pts }} points. Adjusted EBITDA was {{ d.adj_ebitda_pct_nov_fy26 }}% of NOV against {{ d.adj_ebitda_pct_nov_fy25 }}%.

### Step 2: the denominator trap

The company added NOV beside GOV in its Q4 FY25 letter and shifted its commentary towards it, so older and newer margins can sit on different bases. The Q4 FY25 letter prints contribution as {{ e.contribution_pct_gov_q4fy25 }}% of GOV for the March 2025 quarter, from GOV of ₹{% include inr.html n=e.gov_q4fy25 %} crore. The same contribution of ₹{{ contrib_q4_25 }} crore over that quarter's NOV of ₹{% include inr.html n=nov_q4_25 %} crore is {{ d.contrib_pct_nov_q4_fy25 }}%.

4. Same rupees of contribution, two percentages: {{ d.contrib_pct_gov_q4_fy25 }}% and {{ d.contrib_pct_nov_q4_fy25 }}%. The difference is only the denominator: discounts were ₹{% include inr.html n=d.discounts_q4_fy25 %} crore, {{ d.discounts_pct_gov_q4_fy25 }}% of GOV.
5. So a FY25 margin quoted on GOV and a FY26 margin quoted on NOV can't be compared. Put both years on the same base, as the table above does.

Two further cautions. Adjusted revenue is **not** a statutory line; it adds delivery and platform charges to revenue from operations. And the letter's food delivery tables do not print orders or order values per order for these quarters, so per-order economics can't be derived from them.

This is one lens from the [Fundamental Analysis]({{ '/series/fundamental-analysis/' | relative_url }}) series. See [gross margin]({% post_url 2026-08-26-gross-margin %}) for the statutory counterpart and [EBITDA margin]({% post_url 2026-08-28-ebitda-margin %}) for the plain version of the adjusted measure. None of this is a view on Eternal.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You run a pizza-delivery app. A family orders ₹500 of pizza and the app gives them ₹50 off, so they pay ₹450.

Do you say the "order value" was ₹500 or ₹450? Both are true, but they give different percentages when you say "the app kept ₹30". Neither is wrong — you just have to say which one you used, or someone will compare your 6% with another app's 6.7% and think you did worse.

</details>

## Common mistakes

- **Comparing take rates without the denominator.** GOV, NOV and restaurant bill value give three different percentages for the same business.
- **Treating adjusted revenue as reported revenue.** It adds charges that sit outside statutory revenue. Use it within a company's own history, with its definition.
- **Reading contribution as profit.** Contribution is before most overheads: technology, marketing, corporate costs. Adjusted EBITDA is closer, but company-defined too.
- **Comparing a margin on one basis with last year's on another.** The addition of NOV beside GOV is a live example.

## What this lens can't tell you

- **It's all company-defined.** None of GOV, NOV, adjusted revenue or contribution is an accounting standard term.
- **It's one segment.** The company has other businesses, and group figures are a different story.
- **It's backward-looking and silent on price.** One year of one segment tells you how the unit economics worked then, not what they'll be.

**Takeaway:** A take rate is the platform's slice of an order, and the percentage changes with whatever order value you divide by. Before comparing any margin across years or companies, check the denominator and the definition of revenue.
