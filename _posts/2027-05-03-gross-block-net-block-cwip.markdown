---
layout: post
title: "Gross block, net block and CWIP: reading fixed assets"
seo_title: "Gross block, net block and CWIP: meaning and example"
description: "Gross block is what fixed assets cost, net block is that cost less depreciation, and CWIP is what's still being built. All three, on Desi Bites' books."
image: /assets/og/gross-block-net-block-cwip.png
date: 2027-05-03 09:00:00 +0530
series: jargon
term: "Gross block, net block and CWIP"
---

{% assign k = site.data.jargon_m10.blocks %}
{% assign last = k.rows[4] %}
{% assign first_gross = k.rows[0].gross %}

## What the three terms mean

A company's fixed assets (factories, machines, buildings) are reported in
three pieces:

- **Gross block**: what the assets in use cost when they were bought or built.
- **Net block**: gross block minus all the depreciation charged on them so
  far (accumulated depreciation). It's what's left on the books.
- **CWIP, capital work-in-progress**: money spent on assets that aren't
  ready for use yet, such as a production line still being installed. It
  usually isn't depreciated until the asset starts working, and on a real
  balance sheet it's normally shown as a separate line.

Together they show how much a company has put into its plant, how old that
plant is, and what's on the way. This post builds all three for Desi Bites.
It's part of [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}), and
builds on the [balance sheet post]({% post_url 2026-08-20-reading-a-balance-sheet %}).

## The formula

```
Gross block (end)      =  gross block (start) + assets that came into use − assets sold or scrapped
Accumulated dep (end)  =  accumulated dep (start) + depreciation for the year − depreciation on assets sold
Net block              =  gross block − accumulated depreciation
Fixed assets (in this post's tables)  =  net block + CWIP

Accumulated dep ÷ gross block  →  a rough gauge of how much of the plant's cost has been written off
```

[Depreciation and amortisation]({% post_url 2027-02-01-depreciation-and-amortisation %})
explains the yearly charge;
[capex intensity]({% post_url 2026-09-21-capex-intensity %}) explains
spending on new assets.

## Worked example: Desi Bites, FY22 to FY26

[Desi Bites Foods]({{ '/case-study/' | relative_url }}) is fictional. Its
balance sheet shows only net fixed assets, so this post adds three facts: a
gross block of ₹{% include inr.html n=first_gross %} lakh at 31 March 2022,
no assets sold since, and a packing line of ₹{{ k.cwip }} lakh still being
built at 31 March 2026. Each year's capex (capital expenditure) comes from the
cash flow statement;
FY26 also adds the ₹{{ k.acquired }} lakh of fixed assets that came with the
Chatpata acquisition. Figures in ₹ lakh.

| Year | Gross block | Added in the year | Depreciation | Accumulated depreciation | Written off | Net block | CWIP | Fixed assets |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
{% for r in k.rows -%}
| {{ r.fy }} | {{ r.gross }} | {% if r.additions %}{{ r.additions }}{% else %}—{% endif %} | {% if r.dep %}{{ r.dep }}{% else %}—{% endif %} | {{ r.acc_dep }} | {{ r.acc_share_pct }}% | {{ r.net }} | {{ r.cwip }} | {{ r.fixed_assets }} |
{% endfor %}

The last column matches the net fixed assets on Desi Bites' balance sheet
every year. The FY26 depreciation here is ₹{{ last.dep }} lakh; the ₹{{ site.data.case_study_2.fy26.amortisation }} lakh of amortisation
elsewhere in the FY26 accounts is on the Chatpata brand, an intangible
outside the block.

What it shows:

1. **The written-off share rose, then fell.** Accumulated depreciation was
   {{ k.rows[0].acc_share_pct }}% of gross block in FY22 and
   {{ k.rows[3].acc_share_pct }}% by FY25: each year's depreciation added to
   it faster, in proportion, than the year's additions grew the gross block.
   In FY26 it fell to {{ k.rows[4].acc_share_pct }}%, because the Chatpata
   assets and new capex joined the gross block with little depreciation behind
   them yet.
2. **Just over half of FY26's additions weren't organic.** Of the ₹{{ last.additions }}
   lakh added to gross block, ₹{{ k.acquired }} lakh came with Chatpata; the
   rest is capex that came into use. Another ₹{{ k.cwip }} lakh of that year's
   ₹{{ k.capex_fy26 }} lakh capex sits in CWIP.
3. **CWIP is future depreciation.** When the packing line starts working, it
   moves into gross block and starts being depreciated.

## Common mistakes

1. **Reading a low net block as a lean, capital-light business.** It may be
   an old plant, mostly written off and due for replacement. Look at the accumulated depreciation
   share, not just the net figure.
2. **Ignoring CWIP that doesn't move.** CWIP that sits on the balance sheet
   year after year can mean a project is stalled or delayed. It earns nothing
   until it's finished.
3. **Comparing net blocks across companies.** Different depreciation methods
   and asset lives change the net figure for the same physical plant. Gross
   block is closer to how much was invested, though it too depends on when
   the assets were bought and how (acquired assets come in at their value on
   acquisition, as Chatpata's did).

**Takeaway:** Gross block is what a company's fixed assets cost, net block is
that cost after depreciation, and CWIP is spending on assets not yet in use.
Read together, they show how much was invested, how old it is and what's still
coming.
