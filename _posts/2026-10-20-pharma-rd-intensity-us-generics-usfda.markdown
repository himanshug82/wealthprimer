---
layout: post
title: "Pharma: R&D intensity, the US generics mix and USFDA inspections"
description: "Why a pharma company's revenue can hold steady while its US business shrinks by a fifth, and what R&D intensity and US FDA inspections show. Dr. Reddy's FY26."
image: /assets/og/pharma-rd-intensity-us-generics-usfda.png
date: 2026-10-20 09:00:00 +0530
series: fundamental-analysis
term: "R&D intensity"
---

{% assign r = site.data.sectors.drreddy %}
{% assign d = r.derived %}
{% assign ot = r.other %}
{% assign c26 = r.reported_cr.FY26 %}
{% assign c25 = r.reported_cr.FY25 %}

## Two very different businesses under one label

"Indian pharma" covers businesses that behave almost nothing alike. The two
that matter most for this lens:

- **US generics.** Copies of drugs whose patents have expired, sold in the
  US at a fraction of the original price. The first few companies to launch
  a generic can earn a lot on it; as more competitors arrive, the price
  falls — often steeply — and keeps falling. So a US generics business has
  to keep launching new products just to stand still, and one or two
  products with little competition can be a large, temporary share of
  profit.
- **Branded generics in India and other emerging markets.** Off-patent
  medicines sold under the company's own brand names, largely through
  doctors' prescriptions. Growth comes from brands, field sales forces and
  new launches; prices are steadier than in US generics.

Both depend on research and development (R&D) to file new products, and on
plants that regulators approve. So the sector lens adds three things to the
usual ratios: **where the revenue comes from**, **how much goes into R&D**,
and **what the US Food and Drug Administration (USFDA) has found at the
plants**.

## The formulas

```
R&D intensity     =  R&D expense  /  revenue

Segment share     =  segment revenue  /  total revenue

Gross margin      =  (revenue − cost of revenue)  /  revenue
                     (moves with the MIX of what's sold, not just efficiency)
```

R&D intensity is simple arithmetic. The judgement is in what the R&D is
buying, which no ratio tells you.

## Worked example: Dr. Reddy's, FY26

From Dr. Reddy's [FY26 results press release]({{ r.source_url }})
(consolidated, IFRS — International Financial Reporting Standards), released
{{ r.release_date }} and filed with the US SEC (Securities and Exchange
Commission). The release reports in
₹ million; shown here in ₹ crore (₹10 million = ₹1 crore). Historical, for
illustration only.

### Step 1: where the revenue came from

| Segment | FY26, ₹ crore | FY25, ₹ crore | Share FY26 | Share FY25 | Growth |
|---|---:|---:|---:|---:|---:|
{% for s in r.segments %}| {{ s.label }} | {{ s.fy26_cr }} | {{ s.fy25_cr }} | {% include inr.html n=s.share26 %}% | {% include inr.html n=s.share25 %}% | {% include inr.html n=s.growth %}% |
{% endfor %}| **Total** | **{% include inr.html n=c26.revenue %}** | **{% include inr.html n=c25.revenue %}** | | | **{{ d.revenue_growth_pct }}%** |

(North America, Europe, India and emerging markets together form the
company's Global Generics segment. Shares may not add to exactly 100% because
of rounding.)

1. **The headline** was revenue up {{ d.revenue_growth_pct }}%.
2. **Underneath**, North America fell {{ d.na_decline_pct }}% — about
   ₹{% include inr.html n=d.na_lost_cr %} crore — and its share of revenue dropped from
   {{ d.na_share25 }}% to {{ d.na_share26 }}%. Everything else together grew
   by about ₹{% include inr.html n=d.non_na_gain_cr %} crore, more than making up the gap.
3. **Why**, in the company's words: the North America decline "was largely
   due to lower Lenalidomide sales and the one-time SSA". Lenalidomide is one
   generic product. The SSA — shelf-stock adjustment — is a credit a
   generics maker gives US wholesalers when a product's price falls, to cover
   the value lost on stock they already hold. It was
   ₹{% include inr.html n=d.ssa_q4_cr %} crore in the March quarter, when North America revenue was
   ₹{% include inr.html n=d.na_q4_cr26 %} crore against ₹{% include inr.html n=d.na_q4_cr25 %} crore a year earlier.
4. **Europe's** {{ r.segments[1].growth }}% includes a consumer-health
   business (nicotine replacement therapy, NRT) acquired during FY25;
   excluding it, the release puts Europe's growth at
   {{ ot.europe_growth_ex_nrt_pct }}%. Not like-for-like.

### Step 2: what the mix did to margins

| | FY26 | FY25 |
|---|---:|---:|
| [Gross margin]({% post_url 2026-08-26-gross-margin %}) | {{ d.gm26 }}% | {{ d.gm25 }}% |
| [EBITDA margin]({% post_url 2026-08-28-ebitda-margin %}) (earnings before interest, tax, depreciation and amortisation) | {{ d.ebitda_m26 }}% | {{ d.ebitda_m25 }}% |
| R&D, ₹ crore | {% include inr.html n=c26.rnd %} | {% include inr.html n=c25.rnd %} |
| **R&D intensity** | **{{ d.rnd_pct26 }}%** | **{{ d.rnd_pct25 }}%** |
| Profit attributable to shareholders, ₹ crore | {% include inr.html n=c26.pat_attrib %} | {% include inr.html n=c25.pat_attrib %} |

5. Revenue rose {{ d.revenue_growth_pct }}% but gross margin fell from
   {{ d.gm25 }}% to {{ d.gm26 }}% and profit fell {{ d.pat_decline_pct }}%.
   For the lower gross margin, the release names "reduced sales of
   Lenalidomide, price erosion in North America and Europe Generics and a
   one-time SSA impact". That's the mix effect in action: when high-margin
   sales shrink and revenue is made up elsewhere at lower margins, the top
   line holds while the margin drops.
6. **R&D intensity** fell from {{ d.rnd_pct25 }}% to {{ d.rnd_pct26 }}%, and
   R&D spending fell {{ d.rnd_decline_pct }}% in rupees. The release
   attributes this to lower spending on biosimilars (copies of biological
   drugs) after most of one programme's investment was completed. A falling
   ratio can mean discipline or under-investment; the ratio can't tell you
   which.
7. **The pipeline** is where R&D shows up. At 31 March 2026 the company had
   {{ ot.anda_pending }} ANDAs (abbreviated new drug applications — the US
   filing to sell a generic) pending with the USFDA, {{ ot.para_iv }} of them
   "Paragraph IV" filings that challenge an existing patent, and
   {{ ot.anda_filed_fy26 }} new ANDAs filed during FY26. A first filer on a
   patent challenge can win a period of US market exclusivity, which is why
   companies report how many filings "may have 'First to File' status"
   ({{ ot.first_to_file_possible }} here).

### Step 3: USFDA inspections — the mechanism

A plant that makes medicines for the US has to pass USFDA inspections. At
the end of an inspection, observations may be written up on a Form FDA 483.
The USFDA then gives the inspection a final classification, which it
publishes in its [inspections data dashboard](https://datadashboard.fda.gov/oii/cd/inspections.htm):

| Classification | What it broadly means |
|---|---|
| NAI — No Action Indicated | No objectionable conditions requiring action |
| VAI — Voluntary Action Indicated | Objectionable conditions found, but the company is left to correct them; no regulatory action recommended |
| OAI — Official Action Indicated | Regulatory action recommended |

Why investors watch this: an OAI outcome can lead to a warning letter, and
new product approvals that depend on that plant can be delayed until it's
resolved. For a company whose growth depends on US launches, one plant's
status can matter more than a quarter's profit.

8. Dr. Reddy's release for the year reports that a formulations plant at
   Srikakulam, Andhra Pradesh, received a **VAI** classification after a
   USFDA inspection (including a pre-approval inspection) in December 2025.
   Classifications apply per plant and per inspection; they're a snapshot,
   not a permanent grade.

None of this is a view on Dr. Reddy's. It's one year's release, read through
the sector's metrics.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you're the first kid in school to sell a copy of a popular
sticker, the day the original company stops being the only seller. For a
while you can charge almost what they did. Then ten other kids start
selling the same sticker, and the price drops to almost nothing.

So you keep looking for the *next* sticker to copy — that's R&D. And a
teacher checks everyone's sticker-making desk to make sure it's clean and
safe — that's the USFDA inspection. If your desk fails, you're not allowed
to sell new stickers until you fix it.

</details>

## Common mistakes

- **Treating one product's windfall as the base business.** In US generics,
  a product with little competition can be a big share of profit for a year
  or two and then fade. When one product drives a year's growth, ask what
  the business looks like without it — Dr. Reddy's own release shows a
  year where the rest of the business grew while North America shrank.
- **Reading R&D intensity as a quality score.** A higher ratio isn't
  automatically better, and a falling one isn't automatically worse. What
  matters is what it buys — filings, approvals, launches — and that shows up
  years later.
- **Ignoring price erosion.** US generic prices tend to fall year after
  year. Revenue growth that relies only on existing products is fighting
  that tide; new launches are what offsets it.
- **Treating an inspection result as permanent.** USFDA classifications
  apply to a plant and an inspection. A clean result can be followed by a
  bad one, and the reverse, so track the status plant by plant.

**Takeaway:** For a pharma company, look past total revenue to where it
comes from: US generics can shrink fast when competition arrives, even as
branded businesses elsewhere grow. Read R&D intensity as spending, not
quality, and track USFDA outcomes plant by plant.
