---
layout: post
title: "Segment reporting: the businesses inside the total"
description: "Segment reporting splits a company's revenue, profit and assets by business line. How Ind AS 108 picks the segments, worked on Desi Bites' two businesses."
image: /assets/og/segment-reporting.png
date: 2027-03-31 09:00:00 +0530
series: fundamental-analysis
term: "Segment reporting"
---

{% assign s = site.data.fa5.segments %}
{% assign d = s.desi %}
{% assign c = s.chat %}
{% assign t = s.chat_tests %}
{% assign rc = s.recon %}

## What segment reporting is

**Segment reporting** is the note in a company's annual report that splits
its revenue, profit and assets by business line or region. A group that
sells snacks and runs a cement plant reports one total revenue on the
income statement; the segment note shows how much of it, and how much of the
profit, came from each.

It matters because a total can hide very different businesses. One segment
can be growing and profitable while another shrinks or loses money, and the
consolidated figure, which the
[consolidated vs standalone post]({% post_url 2027-03-29-consolidated-vs-standalone %})
explains, blends them. It's part of
[Fundamental Analysis]({{ '/series/fundamental-analysis/' | relative_url }}).

## How the segments are chosen

Ind AS 108 (the Indian Accounting Standard on operating segments) starts
from how management runs the business, not from a fixed list:

```
Operating segment  =  a part of the business that earns revenue and incurs costs,
                      whose results the "chief operating decision maker" reviews
                      regularly to allocate resources, and with its own
                      financial information                          (para 5)

Reportable if ANY of these is 10% or more of all operating segments combined:
  (a) revenue, external plus inter-segment
  (b) profit or loss (in absolute terms, against the larger of total profits
      and total losses)
  (c) assets                                                         (para 13)

And: reportable segments together must cover at least 75% of the
company's external revenue, adding segments until they do           (para 15)
```

The "chief operating decision maker" is a function, not a job title
(paragraph 7): often the managing director or a management committee. Other
segments can be reported anyway if management thinks the information is
useful, and the rest go into an "all other segments" line (paragraphs 13
and 16).

## Worked example: Desi Bites' two businesses, FY26

Desi Bites Foods is fictional. Since it bought Chatpata Foods on 1 October
2025, suppose its board reviews two businesses separately: the original
Desi Bites brand, and Chatpata's regional namkeen. Segment result here is
EBIT (earnings before interest and tax) before group-level items. Chatpata's
assets include the goodwill and brand allocated to it; the IPO cash is held
centrally and belongs to neither. Figures in ₹ lakh, FY26, from the same
books as the [consolidated vs standalone post]({% post_url 2027-03-29-consolidated-vs-standalone %}).

| ₹ lakh, FY26 | {{ s.names[0] }} | {{ s.names[1] }} | All segments |
|---|---:|---:|---:|
| External revenue | {{ d.external }} | {{ c.external }} | |
| Inter-segment revenue | {{ d.inter }} | {{ c.inter }} | |
| Segment revenue | {{ d.revenue }} | {{ c.revenue }} | {{ s.combined_revenue }} |
| Segment result (EBIT) | {{ d.result }} | {{ c.result }} | {{ s.combined_result }} |
| Result margin | {{ d.margin_pct }}% | {{ c.margin_pct }}% | |
| Segment assets | {{ d.assets }} | {{ c.assets }} | {{ s.combined_assets }} |
| Result on segment assets | {{ d.result_on_assets_pct }}% | {{ c.result_on_assets_pct }}% | |

Chatpata's column covers six months, so its revenue and result are half a
year's worth while its assets are a full year-end balance. That's why its
result on assets looks so low.

**Step 1: is Chatpata a reportable segment?**

| Test (para 13) | Chatpata's share | 10% or more? |
|---|---:|:---:|
| Revenue | {{ t.revenue_pct }}% | No |
| Result | {{ t.result_pct }}% | No |
| Assets | {{ t.assets_pct }}% | **Yes** |

It fails on revenue and profit and passes on assets. Goodwill and the brand
(₹{{ s.goodwill_and_brand }} lakh) add to its share, but even without them
Chatpata would hold {{ s.chat_assets_ex_goodwill_brand_pct }}% of segment
assets. A bigger reason is that the IPO (initial public offering) cash sits
outside both segments; counted in the total, Chatpata's share would still be
{{ s.chat_assets_if_cash_counted_pct }}%. Passing any one test is enough, so
Chatpata is reportable.

**Step 2: the 75% check.** The Desi Bites brand segment alone covers
{{ s.desi_external_cover_pct }}% of the group's external revenue, so no extra
segment needs adding.

**Step 3: reconcile to the income statement.** The segment results must be
reconciled to the company's profit, with the group-level items shown
(paragraph 28):

| ₹ lakh | |
|---|---:|
| Total of segment results | {{ rc.segment_results }} |
| Brand amortisation (group level) | {{ rc.brand_amortisation | replace: "-", "−" }} |
| Other income | {{ rc.other_income }} |
| Exceptional items | {{ rc.exceptional | replace: "-", "−" }} |
| Interest | {{ rc.interest | replace: "-", "−" }} |
| **Profit before tax** | **{{ rc.pbt }}** |

**What the note tells you that the total didn't.** The group's EBIT margin
blends a {{ d.margin_pct }}% business with an {{ c.margin_pct }}% one. And
the acquired business ties up ₹{% include inr.html n=c.assets %} lakh of the
₹{% include inr.html n=s.combined_assets %} lakh of segment assets while
producing ₹{{ c.result }} lakh of the ₹{{ s.combined_result }} lakh of
segment result. Its segment assets include the brand, while the brand's
amortisation sits in the group-level line, so its result on assets pairs a
result without the brand's cost with assets that include the brand. Whether that improves over a
full year, and with integration, is what later segment notes would show;
one half-year can't.

## Common mistakes

1. **Treating segments as standard across companies.** Segments follow how
   each management runs its own business, so two companies in the same
   industry can split themselves differently. Compare a company's segments
   with its own history first.
2. **Ignoring "unallocated" lines.** Head-office costs, central cash and
   group-level items often sit outside every segment, so the combined
   segment result can look better than the company's. Here they nearly net
   out: {{ s.combined_result_margin_pct }}% across the segments against
   {{ s.group_ebit_margin_pct }}% for the group.
3. **Comparing a part-year segment with a full-year one.** A segment that
   arrived by acquisition mid-year, as Chatpata did, shows part-year revenue
   against year-end assets. Annualising roughly (Chatpata's external revenue would be
   about ₹{{ s.chat_annualised_revenue }} lakh for a year at the same pace)
   helps, but seasonality can make that wrong too.
4. **Missing a resegmentation.** When a company redraws its segments, past
   years are usually restated, but a reader comparing old annual reports
   with new ones can mix the two definitions.

**Takeaway:** Segment reporting splits a company's total into the businesses
inside it, using the lines management itself uses to run them. It's often
the only place to see which business earns the profit and which one ties up
the capital.

## Sources

- Ind AS 108, *Operating Segments*, paragraphs 5, 7, 13, 15, 16 and 28, read on
  21 November 2026 in [the Institute of Chartered Accountants of India's (ICAI's) compiled Ind AS text (2022-23)](https://www.caalley.com/as/indAs/600asb-cias-2022-23-vol1-8.pdf),
  a copy hosted on a third-party site because the Ministry of Corporate Affairs' (MCA's)
  [Ind AS page](https://www.mca.gov.in/content/mca/global/en/acts-rules/ebooks/accounting-standards.html)
  refuses automated requests. Check against MCA's current text.
