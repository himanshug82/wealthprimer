---
layout: post
title: "EBIT and operating profit: the same line, two names?"
seo_title: "EBIT meaning: earnings before interest and tax, explained"
description: "EBIT is earnings before interest and tax, but sources build it differently. Three versions on Desi Bites' FY26, and how the choice moves margins and cover."
image: /assets/og/ebit-operating-profit.png
date: 2027-04-30 09:00:00 +0530
series: jargon
term: "EBIT (earnings before interest and tax)"
---

{% assign e = site.data.jargon_m10.ebit %}

## What EBIT means

**EBIT, earnings before interest and tax,** is a company's profit before it
pays its lenders and the government: what the business earned for everyone
who funded it. It sits one step below
[EBITDA]({% post_url 2026-08-28-ebitda-margin %}) (EBIT plus depreciation and
amortisation) on the [income statement]({% post_url 2026-08-22-reading-an-income-statement %}),
and it's the numerator of [ROCE]({% post_url 2026-09-03-roce %}) (return on
capital employed) and of
[interest coverage]({% post_url 2026-09-17-interest-coverage %}). This blog's
ROCE and interest-coverage posts use the operating version below.

"Operating profit" is often used for the same thing, and that's where the
trouble starts. Companies and data sources build EBIT differently,
especially in whether they include **other income** (interest on cash,
dividends, gains on investments) and **exceptional items** (one-offs). This
post shows three versions on one set of books. It's part of
[Jargon, Decoded]({{ '/series/jargon/' | relative_url }}).

## The formula

```
Operating EBIT       =  revenue − operating costs − depreciation − amortisation
EBIT incl. other income      =  operating EBIT + other income
EBIT incl. everything        =  operating EBIT + other income + exceptional items
                             =  profit before tax + interest
```

The last line is the quick way to back out EBIT from a published income
statement: add the interest (finance cost) back to profit before tax. It
gives the all-in version: the widest in what it includes, not necessarily the
biggest number.

## Worked example: Desi Bites, FY26

[Desi Bites Foods]({{ '/case-study/' | relative_url }}) is fictional. FY26
figures in ₹ lakh. Its other income is mostly interest on the IPO (initial
public offering) cash, and its exceptional item is the cost of integrating
an acquisition.

| ₹ lakh, FY26 | |
|---|---:|
| Revenue | {{ e.revenue }} |
| EBITDA | {{ e.ebitda }} |
| Less depreciation | {{ e.dep }} |
| Less amortisation | {{ e.amort }} |
| **Operating EBIT** | **{{ e.operating_ebit }}** |
| Add other income | {{ e.other_income }} |
| **EBIT incl. other income** | **{{ e.ebit_incl_oi }}** |
| Exceptional items | {{ e.exceptional | replace: "-", "−" }} |
| **EBIT incl. everything** | **{{ e.ebit_incl_all }}** |
| Check: profit before tax + interest | {{ e.pbt }} + {{ e.interest }} |

Same company, same year, three EBITs:

| Version | EBIT margin | Interest cover (EBIT ÷ interest) |
|---|---:|---:|
| Operating EBIT | {{ e.operating_ebit_margin_pct }}% | {{ e.operating_ebit_cover }}× |
| Incl. other income | {{ e.ebit_incl_oi_margin_pct }}% | {{ e.ebit_incl_oi_cover }}× |
| Incl. everything | {{ e.ebit_incl_all_margin_pct }}% | {{ e.ebit_incl_all_cover }}× |

The operating version says what the snacks business earned. Adding other
income lifts the margin because the IPO cash earns interest, which has
nothing to do with selling snacks. The
[goodwill and other income post]({% post_url 2026-10-07-goodwill-exceptional-items-and-other-income %})
looks at why other income can flatter profit.

## Common mistakes

1. **Comparing EBIT from two sources without checking the build.** A data
   site's EBIT and a company's "operating profit" may differ by other income
   or exceptional items. Rebuild it from the income statement if the
   comparison matters.
2. **Using the widest EBIT for interest cover.** Other income can disappear
   (cash gets spent) and exceptional items aren't expected to recur. For whether operations
   cover the interest, the operating version is the stricter test.
3. **Mixing EBIT and EBITDA.** Depreciation and amortisation sit between
   them. A capital-heavy business looks much better on EBITDA than on EBIT.

**Takeaway:** EBIT is profit before interest and tax, but it can be built
with or without other income and one-offs, and the choice moves both the
margin and interest cover. Say which version you're using, and rebuild it
from the income statement when comparing sources.
