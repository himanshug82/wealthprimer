---
layout: post
title: "Life insurers: embedded value, VNB margin and persistency"
description: "Why a life insurer's yearly profit understates what it earns, and how embedded value, VNB margin and persistency fill the gap, using HDFC Life's FY26 data."
image: /assets/og/life-insurers-embedded-value-vnb-margin.png
date: 2026-10-21 09:00:00 +0530
series: fundamental-analysis
term: "Embedded value (EV) and VNB margin"
---

{% assign h = site.data.sectors.hdfclife %}
{% assign f26 = h.reported.FY26 %}
{% assign f25 = h.reported.FY25 %}
{% assign d = h.derived %}
{% assign ot = h.other %}

## Why this year's profit is the wrong number

A life insurer sells contracts that last 10, 20, 40 years. The costs of
selling one — commission to the agent or bank, underwriting, setting up the
policy, and the reserves the insurer must set aside up front — land mostly
in the year it's sold. The profit on it arrives slowly, over the whole life
of the policy.

So the accounting profit for a year mixes two things: profit released from
old policies, and the up-front cost of new ones (often called *new business
strain*). An insurer that sells *more* this year can report *less* profit
this year. That's why profit after tax (PAT), and so the
[P/E]({% post_url 2026-09-24-price-to-earnings %}) (price-to-earnings)
ratio built on it, says little about a growing life insurer.

The sector's answer is to value the future profits directly:

- **Embedded value (EV)** — what the business already on the books is worth
  to shareholders: the shareholders' adjusted net worth, plus the present
  value of future profits from policies already in force.
- **Value of new business (VNB)** — the present value of future profits from
  the policies sold *this year*.
- **VNB margin** — VNB per unit of new business sold, measured in APE
  (annualised premium equivalent).
- **Persistency** — how many customers keep paying. Every future profit in EV
  and VNB assumes a certain share will.

## The formulas

```
Embedded value (EV)  =  adjusted net worth
                        + present value of future profits on policies in force

VNB margin           =  VNB  /  APE

APE                  =  annualised first-year regular premiums
                        + 10% of single premiums

Operating return on EV (RoEV)  =  EV operating profit (EVOP)  /  EV at start of year

13-month persistency =  share of policies (by number or premium) still paying
                        in their 13th month; 61-month likewise
```

"Present value" is the discounting from the
[time value of money post]({% post_url 2026-09-27-discounting-time-value-of-money %}):
future profits are shrunk back to today's rupees at an assumed rate. EV and
VNB are calculated by the insurer's actuaries using their own assumptions
about lapses, mortality, costs and investment returns — they are not
accounting line items.

## Worked example: HDFC Life, FY26

From HDFC Life's [press release on its FY26 results]({{ h.source_url }})
(standalone), dated {{ h.release_date }}. ₹ crore. Historical, for
illustration only.

| | FY26 | FY25 |
|---|---:|---:|
| Total APE | {{ f26.total_ape }} | {{ f25.total_ape }} |
| Value of new business (VNB) | {{ f26.vnb }} | {{ f25.vnb }} |
| **VNB margin** | **{{ f26.vnb_margin_pct }}%** | **{{ f25.vnb_margin_pct }}%** |
| Embedded value (EV), end of year | {{ f26.ev }} | {{ f25.ev }} |
| Operating return on EV | {% include inr.html n=f26.op_roev_pct %}% | {{ f25.op_roev_pct }}% |
| Profit after tax | {{ f26.pat }} | {{ f25.pat }} |
| 13-month / 61-month persistency | {{ f26.persistency_13m }}% / {{ f26.persistency_61m }}% | {{ f25.persistency_13m }}% / {{ f25.persistency_61m }}% |
| Renewal premium | {{ f26.renewal_premium }} | {{ f25.renewal_premium }} |
| Total premium | {{ f26.total_premium }} | {{ f25.total_premium }} |

### Step 1: VNB margin

1. {% include inr.html n=f26.vnb %} ÷ {% include inr.html n=f26.total_ape %} = {{ d.vnb_margin_check26 }}%.
   For each ₹100 of annualised new premium sold in FY26, the insurer
   expects about ₹{{ d.vnb_margin_check26 }} of profit over the policies'
   lives, in today's money.
2. APE grew {{ d.ape_growth_pct }}% but VNB only {{ d.vnb_growth_pct }}%, so
   the margin slipped from {{ f25.vnb_margin_pct }}% to
   {{ f26.vnb_margin_pct }}%. The company says that excluding the effect of
   GST (goods and services tax) changes and new surrender regulations, the
   margin would have been {{ ot.vnb_margin_ex_gst_surrender_pct }}%.
   Product mix moves this number too: the release shows unit-linked plans
   rising from 39% to 44% of individual APE, and non-participating savings
   plans falling from 32% to 18%.

### Step 2: profit vs value

3. PAT was ₹{% include inr.html n=f26.pat %} crore. VNB — the value added by
   *one year's* sales alone — was ₹{% include inr.html n=f26.vnb %} crore, about
   {{ d.vnb_to_pat_x }} times PAT.
4. Operating RoEV is EV operating profit over opening EV, so EV operating
   profit was roughly {% include inr.html n=f26.op_roev_pct %}% ×
   ₹{% include inr.html n=f25.ev %} crore ≈ ₹{% include inr.html n=d.evop_approx_cr %} crore —
   about {{ d.evop_to_pat_x }} times PAT. (Approximate, because the printed
   RoEV is rounded.) PAT, by contrast, was {{ d.pat_to_ev_pct }}% of opening EV.
5. So a P/E built on ₹{% include inr.html n=f26.pat %} crore measures a small
   slice of what the business added in EV terms. That's why, in our
   experience, life insurers are more often discussed against EV than
   against earnings. This post
   doesn't compute that multiple for HDFC Life; the point is which
   denominator makes sense.

### Step 3: persistency

6. A 13-month persistency of {{ f26.persistency_13m }}% means roughly
   {{ d.lapsed_13m_per_100 }} in every 100 policies (or premium rupees) had
   stopped paying by their 13th month. By month 61, about
   {{ d.lapsed_61m_per_100 }} in 100 had. The 13-month figure slipped
   {{ d.persistency_13m_change | abs }} points; the company says the trends
   "reflect the underlying product and tier mix".
7. Persistency is what turns EV into cash. Renewal premiums were
   {{ d.renewal_share_pct }}% of FY26's total premium and grew
   {{ d.renewal_growth_pct }}%. If fewer customers keep paying than the
   actuaries assumed, future profits already counted in EV and VNB don't
   arrive.

The release also reports a solvency ratio (available capital against the
regulatory requirement) of {{ f26.solvency_pct }}%, down from
{{ f25.solvency_pct }}% — the insurer's version of a bank's
[capital adequacy]({% post_url 2026-10-14-capital-adequacy %}) — and board
approval to raise up to ₹{% include inr.html n=ot.preferential_issue_cr %} crore from its parent to add to it.

None of this is a view on HDFC Life. It's one year's release, read through
the sector's metrics.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You start a newspaper-delivery round. To sign up each new house you spend
₹50 on a flyer and a free first week. Each house then pays you ₹20 a month
for years.

In the month you sign up lots of houses, you *lose* money — all those
flyers. But you're actually much richer, because all those houses will pay
you for years.

Embedded value is adding up all the future payments from the houses you
already have. VNB is the future payments from the houses you signed up this
year. Persistency is how many houses keep paying instead of cancelling.

</details>

## Common mistakes

- **Using P/E on a growing life insurer.** New business strain pushes
  current profit down when sales go up. PAT understates a growing insurer
  and can overstate a shrinking one that's just releasing profit from old
  policies.
- **Treating EV as a hard number.** EV is a present value built on the
  insurer's own assumptions. Change the discount rate or the lapse
  assumption and EV changes. Operating RoEV, which (by HDFC Life's
  definition) excludes changes in economic variables and capital flows to
  and from shareholders, is the steadier gauge of what the business earned.
- **Comparing VNB margins across different product mixes.** Pure life
  cover, unit-linked savings, annuities and guaranteed plans carry different
  margins, so a company's margin can move because of *what* it sold, with
  no change in efficiency. Read the mix alongside the margin.
- **Ignoring persistency.** A high VNB margin on policies customers abandon
  after a year is profit that never arrives. Watch the 13-month and 61-month
  figures over time.

**Takeaway:** A life insurer's yearly profit mostly reflects old policies
and the up-front cost of new ones, so P/E misreads it. Read embedded value
for what's on the books, VNB margin for what this year's sales are worth,
and persistency for whether customers stay long enough to make either real.
