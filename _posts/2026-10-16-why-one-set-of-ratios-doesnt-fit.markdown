---
layout: post
title: "Sector lenses: why one set of ratios doesn't fit every business"
description: "The same EBITDA margin or return on assets means different things in FMCG, cement, telecom and lending. Why each sector needs its own lens, from real filings."
image: /assets/og/why-one-set-of-ratios-doesnt-fit.png
date: 2026-10-16 09:00:00 +0530
series: fundamental-analysis
term: "Sector-specific metrics (sector KPIs)"
---

{% assign o = site.data.sectors.opener %}
{% assign rows = o.margin_capex_rows %}
{% assign brit = rows[0] %}
{% assign utcl = rows[1] %}
{% assign air = rows[3] %}
{% assign ebitda_ratio = air.ebitda_margin | divided_by: brit.ebitda_margin | round: 1 %}
{% assign ebit_ratio = air.ebit_margin | divided_by: brit.ebit_margin | round: 1 %}
{% assign roa_ratio = o.britannia_roa | divided_by: o.hdfc_bank_roa | round %}

## One toolkit, many businesses

This series built one toolkit — margins, returns, working-capital days,
leverage, valuation multiples — and tested it on one kind of business: a
packaged-food maker (the fictional Desi Bites and the real Britannia). The
banks module then showed that a lender breaks half of that toolkit.

Banks aren't the only exception. Every sector has a few numbers that explain
more about its economics than any generic ratio, because they measure the
thing the business actually sells. A **sector lens** is that short list of
metrics — often called sector KPIs (key performance indicators) — used
*alongside* the standard ratios, not instead of them.

The generic ratios still work everywhere; the lens tells you what they mean.
A 20% EBITDA margin in a software company, a cement company and a telecom
company describe three very different businesses.

## The formula behind every lens

Almost every sector lens is the same move: split revenue (or profit) into
*how many units* and *how much per unit*, using the unit the business really
sells.

```
Revenue  =  Units sold  ×  Revenue per unit

  IT services     billable people × utilisation × billing rate
  FMCG            volume (tonnes, packs) × price and mix
  Cement, metals  tonnes sold × realisation per tonne
  Telecom         subscribers × ARPU (average revenue per user)
  Lenders         loan book × spread (yield − cost of funds)
  Life insurers   new business (APE, annualised premium equivalent)
                  × margin on it (VNB margin, value of new business ÷ APE)
```

The generic ratios sit on top of that split. [EBITDA margin]({% post_url 2026-08-28-ebitda-margin %})
(earnings before interest, tax, depreciation and amortisation, as a share of
revenue) tells you what's left per rupee of sales. The sector lens tells you
*why* — more units, a better price, or a cost per unit that fell.

## Worked example: the same two ratios, four businesses

Figures from each company's own results release for the year to 31 March 2026
(FY26, released April–May 2026) and, for Britannia, the FY25 filing this
blog already uses. Sources: [Britannia]({{ site.data.real_company.company.source_url }}),
[UltraTech Cement]({{ site.data.sectors.ultratech.source_url }}),
[Dr. Reddy's]({{ site.data.sectors.drreddy.source_url }}),
[Bharti Airtel]({{ site.data.sectors.airtel.source_url }}). Historical, for
illustration only — and note the periods differ, which is fine for seeing
*structure* but not for ranking.

| Company (sector) | Period | EBITDA margin | EBIT margin | Capex as % of revenue |
|---|---|---:|---:|---:|
{% for row in rows %}| {{ row.company }} | {{ row.period }} | {% include inr.html n=row.ebitda_margin %}% | {% if row.ebit_margin %}{% include inr.html n=row.ebit_margin %}%{% else %}—{% endif %} | {% include inr.html n=row.capex_intensity %}% |
{% endfor %}

EBIT is earnings before interest and tax — EBITDA after depreciation and
amortisation. UltraTech's release gives PBIDT (profit before interest,
depreciation and tax, its name for EBITDA) but not depreciation, and
Dr. Reddy's release doesn't print an EBIT line, so those cells are left blank
rather than estimated. Airtel's capex figure is for the March 2026
quarter only, against that quarter's revenue.

Read the table one column at a time.

1. **EBITDA margin.** Airtel’s is about {% include inr.html n=ebitda_ratio %} times Britannia’s.
   On this number alone the telecom company looks like the far better
   business.
2. **EBIT margin.** After depreciation — the cost of the towers, fibre and
   spectrum already bought — the gap narrows to about {% include inr.html n=ebit_ratio %} times.
   A network business earns its EBITDA by spending heavily up front, and
   depreciation is where that spending comes back.
3. **Capex.** Airtel spent about {% include inr.html n=air.capex_intensity %}% of the quarter's revenue on new
   capital assets; UltraTech {% include inr.html n=utcl.capex_intensity %}% of the year's; Britannia
   {% include inr.html n=brit.capex_intensity %}% (see [capex intensity]({% post_url 2026-09-21-capex-intensity %})).
   A high EBITDA margin that has to fund a network every year is a different
   thing from a lower one that mostly turns into free cash.

None of this says which company is better. It says the same ratio is
measuring different things, so it can't be compared across the table.

### Returns: a bank and a biscuit maker

The same problem hits returns. Britannia's [ROA]({% post_url 2026-09-05-roa %})
(return on assets) for FY25 was {{ o.britannia_roa }}%. HDFC Bank's for the
same year was {{ o.hdfc_bank_roa }}% — Britannia's is about {{ roa_ratio }} times as high. That
isn't a verdict on either; it's what the [banks module]({% post_url 2026-10-10-why-ratios-break-on-a-bank %})
explained. A bank's assets are loans funded mostly with other people's money,
so it earns a thin return on a huge balance sheet and multiplies it with
leverage (about {% include inr.html n=o.hdfc_bank_leverage %}x assets to equity), landing at
[ROE]({% post_url 2026-09-01-roe %}) (return on equity) of {{ o.hdfc_bank_roe }}%.
A biscuit maker's assets are ovens and inventory it owns outright. ROA is
comparable within banks, or within manufacturers — not between them.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

In cricket, you don't judge a fast bowler by his batting average, or an
opening batter by how many wickets she takes. Both numbers are real. They're
just measuring the wrong job.

Companies are the same. A phone company's job is to build a network and fill
it with customers. A biscuit company's job is to sell lots of packets at a
decent price. A bank's job is to lend money that mostly isn't its own. You
need a different scorecard for each — and then you can still compare two
bowlers, or two banks, with each other.

</details>

## The lenses in this module

Each sector post that follows takes one real company's FY26 filing and
works through the metrics that sector lives by. The companies are there to
make the numbers concrete, not as views on the companies.

| Sector | What the business really sells | Metrics the lens adds | Anchor filing |
|---|---|---|---|
| IT services | People's time, billed in dollars | Constant-currency growth, utilisation, attrition, deal wins | Infosys, FY26 |
| FMCG (fast-moving consumer goods) | Packs on shelves | Volume growth vs price growth | Marico, FY26 |
| Cement | Tonnes from a fixed plant | EBITDA per tonne, capacity utilisation | UltraTech, FY26 |
| Pharma | Molecules, patents and approvals | R&D (research and development) intensity, US generics vs India mix, US FDA (Food and Drug Administration) inspections | Dr. Reddy's, FY26 |
| Life insurance | Long contracts priced today, paid out over decades | Embedded value, VNB margin, persistency | HDFC Life, FY26 |
| NBFCs (non-banking financial companies) | Credit, funded without current and savings accounts | Cost of borrowing, spread, asset-liability matching | Bajaj Finance, FY26 |
| Telecom | Network capacity, rented monthly | ARPU, EBITDA after leases, capex | Bharti Airtel, FY26 |

Two sectors already have a module: banks (above), and the packaged-food
business this series has used from the start.

## Common mistakes

- **Screening the whole market on one ratio.** A filter like "EBITDA margin
  above 30%" pulls in capital-heavy businesses such as telecoms, where much
  of that margin goes back into capex. A filter like "ROA above
  10%" won't show you a bank. Screen within a sector, or use a ratio
  that already accounts for capital, such as [ROCE]({% post_url 2026-09-03-roce %})
  (return on capital employed) — and even then, compare within the sector.
- **Comparing with "the market average" instead of the right peers.** A
  sector average hides very different business models. Two pharma companies
  can have opposite exposure to US generic pricing; two IT companies can
  earn in different currencies. The peer set is part of the analysis
  ([relative valuation]({% post_url 2026-09-26-relative-valuation-comparables %})
  made the same point about multiples).
- **Treating company-defined metrics as standard.** "PBIDT", "operating
  PBIDT per tonne", "underlying volume growth", "before one-time actions" —
  each company chooses its own definitions, and many of these numbers sit
  outside the audited statements. Before comparing two companies' versions,
  read the footnote that defines each one.
- **Letting the lens replace the basics.** A sector KPI explains a
  company's economics; it doesn't replace the balance sheet, the cash-flow
  statement or the red-flag checks from earlier in this series. A cement
  company with a great EBITDA per tonne can still be over-borrowed.

**Takeaway:** The same ratio measures different things in different
businesses, so it can only be compared within a sector. Each sector has a
few metrics — usually units sold and money made per unit — that explain
what the generic ratios can't; learn those, then read the standard ratios
through them.
