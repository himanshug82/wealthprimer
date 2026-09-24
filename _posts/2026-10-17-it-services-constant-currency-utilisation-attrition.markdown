---
layout: post
title: "IT services: constant currency, utilisation, attrition and deal wins"
description: "Why an Indian IT company's rupee revenue growth can be triple its real growth, and how utilisation, attrition and deal wins explain the rest. Infosys FY26."
image: /assets/og/it-services-constant-currency-utilisation-attrition.png
date: 2026-10-17 09:00:00 +0530
series: fundamental-analysis
term: "Constant currency (CC) growth"
---

{% assign i = site.data.sectors.infosys %}
{% assign rp = i.reported %}
{% assign d = i.derived %}
{% assign q = rp.q4 %}
{% assign emp26 = q.employees.Q4FY26 %}
{% assign emp25 = q.employees.Q4FY25 %}
{% assign utl_drop = d.utilisation_change_pts | abs %}
{% assign att_drop = d.attrition_change_pts | abs %}

## What you're really analysing

An Indian IT services company sells its people's time and skills — writing,
testing and running software, and increasingly running whole processes — to
clients who are mostly abroad. That one sentence explains the sector lens:

- **It earns in dollars, euros and pounds, but reports in rupees**, so a
  weaker rupee lifts reported growth without a single extra hour of work.
- **Its capacity is people**, so how many of them are billed (utilisation),
  how many leave (attrition) and how many it hires drive both revenue and
  margin.
- **Its future revenue is signed in advance**, in multi-year contracts, so
  deal wins are the closest thing to an order book.

The generic ratios still apply — Infosys's
[operating margin]({% post_url 2026-08-28-ebitda-margin %}) and
[debtor days]({% post_url 2026-09-08-debtor-days %}) mean what they always
meant. The lens is about reading the top line correctly.

## The formulas

```
Growth in rupees   ≈  (1 + growth in US$) × (1 + change in ₹ per US$) − 1

Growth in US$       =  Constant-currency growth  +  cross-currency effect

Constant-currency (CC) growth
   = this year's revenue in each billing currency, converted at LAST year's
     exchange rates, compared with last year's reported revenue

Utilisation            =  effort billed to clients / total available effort
Attrition (LTM)        =  employees who left in the last twelve months / average headcount
Revenue per employee   =  revenue / average headcount
TCV (total contract value) = everything a signed contract is expected to bill,
                             over its whole life
```

Constant currency is the company's number for "how much more work did we
sell", with exchange rates held still. Utilisation and attrition definitions
vary a little between companies (with or without trainees; voluntary or all
exits), so always read the footnote.

## Worked example: Infosys, FY26

All figures from Infosys's own [IFRS press release]({{ i.source_url }}),
[US-dollar release]({{ i.source_usd_url }}) and [Fact Sheet]({{ i.fact_sheet_url }})
for the year ended 31 March 2026, released {{ i.release_date }} and filed
with the US SEC (Securities and Exchange Commission). IFRS is International
Financial Reporting Standards, the basis Infosys uses for these releases.
Historical, for illustration only.

### Step 1: one year, three growth rates

| | FY26 | FY25 | Growth |
|---|---:|---:|---:|
| Revenue, US$ million | {{ rp.rev_usd_m.FY26 }} | {{ rp.rev_usd_m.FY25 }} | {{ d.usd_growth_pct }}% |
| Revenue, ₹ crore | {{ rp.rev_inr_cr.FY26 }} | {{ rp.rev_inr_cr.FY25 }} | {{ d.inr_growth_pct }}% |
| Implied ₹ per US$ (₹ revenue ÷ US$ revenue) | {{ d.implied_inr_per_usd_fy26 }} | {{ d.implied_inr_per_usd_fy25 }} | {{ d.rupee_weakening_pct }}% |
| **Constant-currency growth** (as reported) | | | **{{ rp.cc_growth_fy26_pct }}%** |

The same year's business grew {{ rp.cc_growth_fy26_pct }}%,
{{ d.usd_growth_pct }}% or {{ d.inr_growth_pct }}%, depending on which
number you read.

1. **Rupees vs dollars.** Each dollar of revenue was worth about
   {{ d.rupee_weakening_pct }}% more rupees in FY26 than in FY25 (an implied
   average of ₹{{ d.implied_inr_per_usd_fy26 }} against
   ₹{{ d.implied_inr_per_usd_fy25 }}). The check: {{ d.check_usd_factor }}
   × {{ d.check_fx_factor }} = {{ d.check_product }}, against rupee growth of
   {{ d.check_inr_factor }}.
2. **Dollars vs constant currency.** The remaining
   {{ d.cross_currency_effect_pts }} percentage points came from revenue
   billed in other currencies being worth more dollars. The Fact Sheet shows
   where: in the March 2026 quarter, Europe grew {% for g in q.geography %}{% if g.region == "Europe" %}{{ g.reported }}% reported but {{ g.cc }}% in constant currency{% endif %}{% endfor %}.
3. **What's left.** About {{ rp.cc_growth_fy26_pct }}% is the growth that
   came from selling more work (or better-priced work). That is the number
   the company itself leads with, and guides on.

So of the {{ d.inr_growth_pct }}% rupee growth, roughly
{{ d.inr_vs_cc_gap_pts }} points was currency. That flows into rupee profit
too — which is why an IT company's rupee EPS (earnings per share, see the
[EPS post]({% post_url 2026-09-23-eps %})) can look strong in a year of
modest real growth.

### Step 2: the people engine

From the Fact Sheet, quarter ended 31 March, IT services:

| | Mar 2026 | Mar 2025 |
|---|---:|---:|
| Total employees | {{ emp26 }} | {{ emp25 }} |
| Utilisation, excluding trainees | {% include inr.html n=q.utilisation_excl_trainees.Q4FY26 %}% | {{ q.utilisation_excl_trainees.Q4FY25 }}% |
| Utilisation, including trainees | {{ q.utilisation_incl_trainees.Q4FY26 }}% | {{ q.utilisation_incl_trainees.Q4FY25 }}% |
| Voluntary attrition (last twelve months) | {{ q.attrition_ltm.Q4FY26 }}% | {{ q.attrition_ltm.Q4FY25 }}% |
| Effort delivered onsite (at client locations) | {{ q.onsite_effort.Q4FY26 }}% | {{ q.onsite_effort.Q4FY25 }}% |

1. **Headcount** rose by {% include inr.html n=d.employee_change %}
   ({{ d.employee_growth_pct }}%), less than constant-currency revenue's
   {{ rp.cc_growth_fy26_pct }}%. Yet utilisation fell (next point), so the
   extra revenue per person didn't come from billing more of each person's
   hours — it came from pricing, mix or getting more done per hour on
   fixed-price work. The filing doesn't split those.
2. **Utilisation** fell {{ utl_drop }} points (excluding trainees). Fewer of
   the available hours were billed. That can mean softer demand, or capacity
   built ahead of expected work; the number alone doesn't say which.
3. **Attrition** fell {{ att_drop }} points. Fewer people leaving means lower
   hiring and training costs and less wage pressure — and, in a slow market,
   it can also simply mean fewer outside offers.
4. **Revenue per employee**: US${% include inr.html n=rp.rev_usd_m.FY26 %} million over an
   average of about {% include inr.html n=d.avg_employees %} people is roughly
   US${% include inr.html n=d.rev_per_employee_usd %} each (about
   ₹{{ d.rev_per_employee_inr_lakh }} lakh). It's crude, but tracked over
   time it shows whether each person is producing more.

### Step 3: the order book

1. **Large deal wins** had a TCV of US${{ rp.large_deal_tcv_usd_bn }} billion
   in FY26, {{ rp.large_deal_net_new_pct }}% of it "net new" (the rest being
   renewals of existing work). That's about {{ d.tcv_to_revenue_x }} times
   the year's revenue — but it will be billed over several years, and part of
   it replaces revenue that was already there.
2. **Concentration and collection.** The top ten clients were
   {{ q.top10_clients_pct.Q4FY26 }}% of revenue; days sales outstanding (DSO)
   was {{ q.dso_days.Q4FY26 }} days, against {{ q.dso_days.Q4FY25 }} a year
   earlier.
3. **Margin.** Reported operating margin was {{ rp.op_margin_pct.FY26 }}%
    against {{ rp.op_margin_pct.FY25 }}% in FY25. The company also shows
    {% include inr.html n=rp.op_margin_adjusted_fy26_pct %}% "adjusted", excluding a one-off
    ₹{% include inr.html n=rp.labour_code_charge_cr %} crore charge from India's new
    Labour Codes — the kind of adjustment the
    [exceptional items post]({% post_url 2026-10-07-goodwill-exceptional-items-and-other-income %})
    says to read, not just accept.

None of this is an opinion on Infosys. It's one year's filing, read through
the sector's own metrics.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You sell lemonade to a friend in America for $1 a cup. Last summer $1 got
you ₹84 at home. This summer it gets you ₹88.

You sold exactly the same number of cups — but you "made" more rupees. Did
your lemonade stand get better? No. The dollar just bought more rupees.

Constant currency is asking: "If the dollar were still worth ₹84, how much
more did I really sell?" That's the part you actually earned by making more
lemonade.

</details>

## Common mistakes

- **Reading rupee growth as business growth.** In FY26 about
  {{ d.inr_vs_cc_gap_pts }} of Infosys's {{ d.inr_growth_pct }} points of
  rupee growth came from currency. When the rupee strengthens, the same
  effect runs in reverse. Start from constant currency.
- **Treating deal wins as next year's revenue.** TCV is spread over the
  contract's life, may include renewals, and can be cut if the client's
  plans change. Compare it with revenue over several years, and pay attention
  to the net-new share.
- **Reading utilisation and attrition as "higher is better" or "lower is
  better".** Very high utilisation leaves no spare people for new projects;
  low attrition can reflect a weak job market rather than happy staff. Both
  are signals to explain, not scores.
- **Comparing metrics with different definitions.** Utilisation with and
  without trainees differs by several points; some companies report
  voluntary attrition, others total; some annualise a quarter, others use
  the last twelve months. Line up the definitions before lining up the
  numbers.

**Takeaway:** For an IT services company, start with constant-currency
growth — rupee growth mixes the business with the exchange rate. Then read
utilisation, attrition and deal wins as signals about demand and capacity,
not as scores, and check each company's definitions before comparing.
