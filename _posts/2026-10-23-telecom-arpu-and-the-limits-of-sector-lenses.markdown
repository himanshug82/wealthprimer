---
layout: post
title: "Telecom: ARPU, EBITDA after leases, and the limits of sector lenses"
description: "A telecom firm's revenue is customers times ARPU, and its big EBITDA margin must pay for the network. Bharti Airtel's FY26 data, then what sector lenses miss."
image: /assets/og/telecom-arpu-and-the-limits-of-sector-lenses.png
date: 2026-10-23 09:00:00 +0530
series: fundamental-analysis
term: "ARPU (average revenue per user)"
---

{% assign a = site.data.sectors.airtel %}
{% assign rp = a.reported %}
{% assign ot = a.other %}
{% assign d = a.derived %}
{% assign q26 = rp.Q4FY26 %}
{% assign q25 = rp.Q4FY25 %}
{% assign y26 = rp.FY26 %}

## Building a network, renting it by the month

A mobile operator spends enormous sums up front — spectrum licences,
towers, fibre, radio equipment — and then rents access to that network,
month by month, to hundreds of millions of customers. Most of its costs are
fixed; most of its revenue is small and recurring.

That shapes the lens:

- **Revenue is customers × ARPU** (average revenue per user). Growth comes
  from more customers, or from each paying more — through tariff increases
  or by moving to richer plans (postpaid, more data).
- **EBITDA margins look huge**, because the biggest cost — the network —
  sits mostly in depreciation, amortisation and interest, below EBITDA
  (earnings before interest, tax, depreciation and amortisation).
- **Capex never stops.** Networks have to be upgraded (4G to 5G) and
  expanded, so a large share of EBITDA goes straight back into the network.

## The formulas

```
Mobile revenue    =  average mobile customers  ×  ARPU  ×  months in the period
ARPU              =  mobile revenue  /  average customers  /  months

Growth split      ≈  (1 + customer growth) × (1 + ARPU growth) − 1

EBITDAaL          =  EBITDA after leases
                     (EBITDA minus the depreciation and interest on leased
                      assets such as tower sites)

Capex intensity   =  capex  /  revenue
```

Why "after leases"? Under the lease accounting standard (Ind AS 116 —
Indian Accounting Standard 116),
rentals on leased assets — for an operator, largely tower and site rentals —
are no longer shown as operating expenses. They reappear as depreciation of
a "right-of-use" asset plus interest on a lease liability, both *below*
EBITDA. So reported EBITDA excludes a real, recurring cash cost. EBITDAaL
puts it back, which makes it closer to the old, pre-standard EBITDA.

## Worked example: Bharti Airtel, quarter and year to March 2026

From Airtel's [media release]({{ a.source_url }}) of {{ a.release_date }}
(consolidated, Ind AS). ₹ crore unless noted. Historical, for illustration
only.

### Step 1: ARPU and customers

1. Mobile ARPU in India was ₹{{ ot.arpu.Q4FY26 }} a month in the March 2026
   quarter, against ₹{{ ot.arpu.Q4FY25 }} a year earlier — up
   {{ d.arpu_growth_pct }}%.
2. India mobile revenue grew {{ ot.india_mobile_revenue_growth_pct }}% over
   the same period. Using the growth split, that implies average mobile
   customers grew roughly {{ d.implied_mobile_customer_growth_pct }}%. So
   more than half of the mobile revenue growth came from each customer
   paying more, and the rest from more customers. (Rough: ARPU is rounded to
   the rupee and quarters differ in length.)
3. ARPU rises for more than one reason. The release credits "portfolio
   premiumization" — {{ ot.smartphone_share_pct }}% of mobile customers now
   use smartphone data, and postpaid customers reached
   {% include inr.html n=ot.postpaid_m %} million — as well as higher realisations. Mix and
   price both push ARPU.

### Step 2: EBITDA, EBITDAaL, EBIT

| | Q4 FY26 | Share of revenue |
|---|---:|---:|
| Revenue | {{ q26.revenue }} | 100% |
| EBITDA | {{ q26.ebitda }} | {{ d.ebitda_margin_q4 }}% |
| EBITDAaL (after leases) | {{ ot.ebitdaal_q4_cr }} | {{ ot.ebitdaal_margin_q4_pct }}% |
| EBIT (earnings before interest and tax) | {{ q26.ebit }} | {{ d.ebit_margin_q4 }}% |
| Capex | {{ ot.capex_q4_cr }} | {% include inr.html n=d.capex_to_revenue_q4_pct %}% |

4. Lease costs alone — the gap between EBITDA and EBITDAaL — were
   ₹{% include inr.html n=d.lease_gap_q4 %} crore, about {{ d.lease_gap_q4_pct_rev }}% of the
   quarter's revenue.
5. For the full year, EBITDA was ₹{% include inr.html n=y26.ebitda %} crore and EBIT
   ₹{% include inr.html n=y26.ebit %} crore. The difference — mostly depreciation and
   amortisation of the network and spectrum — was about
   ₹{% include inr.html n=d.ebitda_minus_ebit_fy26 %} crore, or {{ d.ebitda_minus_ebit_pct_rev }}% of revenue.
   An EBITDA margin of {{ d.ebitda_margin_fy26 }}% became an EBIT margin of
   {{ d.ebit_margin_fy26 }}%.
6. Capex in the quarter was ₹{% include inr.html n=ot.capex_q4_cr %} crore — about
   {% include inr.html n=d.capex_to_revenue_q4_pct %}% of revenue and {{ d.capex_to_ebitda_q4_pct }}% of EBITDA.
   Roughly half of every rupee of EBITDA went back into the network that
   quarter, before interest, tax, lease payments or spectrum dues.

The release gives two leverage figures: net debt to EBITDA of
{{ ot.net_debt_to_ebitda_x }} times (from {{ ot.net_debt_to_ebitda_prev_x }}
a year earlier), and net debt *excluding leases* to EBITDAaL of
{{ ot.net_debt_ex_leases_to_ebitdaal_x }} times. By implication the first
keeps lease liabilities in the debt and lease costs out of EBITDA, and the
second takes them out of both — each pair consistent, which is the point: see
[net debt/EBITDA]({% post_url 2026-09-18-net-debt-ebitda %}) and never mix
the two.

None of this is a view on Airtel. It's one year's release, read through the
sector's metrics.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You build a giant water slide for ₹10 lakh. Each kid pays ₹100 a month to
use it as often as they like.

Your "average revenue per user" is ₹100. You earn more if more kids sign up,
or if you get kids to pay ₹150 for the fast lane.

The monthly money looks like almost pure profit — the slide is already
built. But slides wear out, and next year everyone wants a taller one. If
you forget that, you'll think you're rich right up until the slide needs
replacing.

</details>

## Common mistakes

- **Reading EBITDA margin without capex and leases.** A
  {{ d.ebitda_margin_fy26 }}% EBITDA margin isn't three times as good as
  Britannia's {{ site.data.real_company.ratios.FY25.ebitda_margin }}% (FY25). Subtract leases, depreciation and ongoing capex
  first.
- **Treating every ARPU increase as a price increase.** Customers moving to
  postpaid or richer data plans lift ARPU with no tariff change. Read the
  company's explanation of mix before assuming pricing power.
- **Comparing ARPU across companies without checking the definition.**
  Operators can count customers differently (for example, all SIMs versus
  active ones), which changes ARPU without changing revenue. Compare each
  company's ARPU with its own history first.
- **Mixing lease treatments in leverage ratios.** Net debt with leases
  against EBITDA, or net debt without leases against EBITDAaL — never one of
  each.

## What sector lenses can't do

This module has used one real filing per sector to show that the same ratio means
different things in different businesses. It's worth being just as clear
about what a sector lens *can't* tell you.

- **Most sector metrics are the company's own.** Utilisation, underlying
  volume growth, cement profit per tonne, value of new business, ARPU —
  each is defined and
  calculated by the company, and many sit outside the audited financial
  statements. They're useful, but they deserve the same scepticism as any
  adjusted number. The
  [red-flags post]({% post_url 2026-10-04-desi-bites-cooks-the-books %})
  still applies.
- **They describe one past year.** Every example here is backward-looking.
  A strong ARPU year says nothing certain about next year's tariffs,
  competition or regulation.
- **They say nothing about price.** This module deliberately never asked
  whether any of these companies is cheap or expensive. A lens explains the
  business; it doesn't value it.
- **Businesses don't stay in one sector.** A telecom company adding data
  centres and a lending arm, an FMCG company building foods and digital
  brands, a pharma company buying a consumer-health business — each needs
  more than one lens, applied segment by segment.
- **The metric that matters can change.** A new regulation, a technology
  shift or a price war can make last decade's key number less relevant. The
  lens is a starting checklist, not a permanent one.

**Takeaway:** In telecom, revenue is customers times ARPU, and a big EBITDA
margin has to pay for leases, depreciation and a network that's never
finished. Across every sector, the lens explains how a business makes money
— it doesn't audit the numbers, predict next year, or tell you what the
company is worth.
