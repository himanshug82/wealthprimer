---
layout: post
title: "Sum of the parts: valuing a company piece by piece"
seo_title: "Sum of the parts (SOTP) valuation explained with an example"
description: "Sum of the parts values each business of a group separately, then adds them up. The method, the holding-company discount, worked on a fictional group."
image: /assets/og/sum-of-the-parts.png
date: 2027-02-01 09:00:00 +0530
series: fundamental-analysis
term: "Sum of the parts (SOTP)"
---

{% assign s = site.data.fa5.sotp %}
{% assign p0 = s.parts[0] %}
{% assign p1 = s.parts[1] %}
{% assign p2 = s.parts[2] %}

## What sum of the parts means

**Sum of the parts** (SOTP) values a company that runs several different
businesses by valuing each one on its own terms and adding them up. A group
with a foods business, a cement plant and a stake in another listed company
doesn't fit one multiple: foods, cement and a shareholding are priced very
differently. SOTP gives each part its own method, then subtracts the group's
net debt to reach a value for the shareholders.

It builds on two earlier ideas: [relative valuation]({% post_url 2026-09-26-relative-valuation-comparables %}),
which prices a business against peers, and
[segment reporting]({% post_url 2027-01-28-segment-reporting %}), which
supplies each part's own figures. It's part of
[Fundamental Analysis]({{ '/series/fundamental-analysis/' | relative_url }}).

## The formula

EBITDA is earnings before interest, tax, depreciation and amortisation. A
DCF (discounted cash flow) values a business from its forecast cash flows;
see [terminal value and the full DCF]({% post_url 2026-09-30-terminal-value-and-the-full-dcf %}).

```
Value of each operating business  =  its EBITDA × a multiple chosen for that kind of business
                                     (or a DCF of that business on its own)

Value of each investment  =  market value of the stake  ×  (1 − any discount applied)

Gross value of the parts  =  Σ operating businesses  +  Σ investments
Equity value              =  gross value  −  net debt
Per share                 =  equity value ÷ shares   (then any holding-company discount)
```

The operating businesses' values are enterprise values; the listed stake is
an investment added alongside them, not part of any business's enterprise
value. [EV/EBITDA]({% post_url 2026-09-26-ev-ebitda %}) (enterprise value to
EBITDA) and [enterprise value]({% post_url 2026-10-13-enterprise-value %})
explain why debt is subtracted after the parts are added.

## Worked example: a fictional group

{{ s.name }} is invented. So is every input below: the EBITDA of each
business, the multiples, the stake's value and the discounts are assumptions
chosen to show the method, not estimates for any real company. Figures in
₹ crore; {{ s.shares_crore }} crore shares; net debt ₹{% include inr.html n=s.net_debt %}
crore.

**Step 1: value each part.**

| Part | Basis | Input (₹ crore) | Multiple or adjustment | Value (₹ crore) |
|---|---|---:|---|---:|
| {{ p0.name }} | EBITDA | {{ p0.value }} | {{ p0.multiple }}× | {{ p0.ev }} |
| {{ p1.name }} | EBITDA | {{ p1.value }} | {{ p1.multiple }}× | {{ p1.ev }} |
| {{ p2.name }} | Market value of stake | {{ p2.value }} | less {{ s.discount_on_stake_pct }}% | {{ p2.ev }} |
| **Sum of the parts** | | | | **{{ s.gross }}** |
| Less net debt | | | | {{ s.net_debt }} |
| **Equity value** | | | | **{{ s.equity }}** |

The {{ s.discount_on_stake_pct }}% taken off the listed stake in Step 1 is an
assumption for what selling it would cost: tax on the gain and the price
impact of selling a large block. The foods business is {{ s.food_share_pct }}%
of the total, so its multiple drives most of the answer.

**Step 2: the holding-company discount.** Some analysts take a further
discount off the whole group's value, on the view that a group with several
businesses is worth less to an outside shareholder than its parts would be
separately: capital may be moved between businesses in ways the shareholder
can't control. It comes on top of Step 1's discount on the stake, and both
can end up pricing the same worry, so a reader should check that each has a
separate reason. The size is a judgement, not a rule:

| Holding-company discount | Equity value (₹ crore) | Per share (₹) |
|---:|---:|---:|
{% for r in s.per_share -%}
| {{ r.discount_pct }}% | {{ r.equity }} | {{ r.per_share }} |
{% endfor %}

**Step 3: how much one multiple matters.** Move only the foods multiple by
{{ s.multiple_shift }} either way, with no holding-company discount:

| Foods multiple | Per share (₹) |
|---:|---:|
{% for r in s.sensitivity -%}
| {{ r.food_multiple }}× | {{ r.per_share }} |
{% endfor %}

A two-point change in one multiple moves the per-share answer about as much
as a several-point change in the holding-company discount. SOTP looks
precise because it has many lines, but each line carries an assumption.

## Common mistakes

1. **Valuing the parts at peak multiples.** Each part's multiple is
   usually borrowed from listed peers, and peers' multiples move with
   markets. Taking the highest multiple for every part inflates the sum.
2. **Counting a stake twice.** If a group consolidates a subsidiary, the
   subsidiary's EBITDA is already in the group's figures. Valuing the
   subsidiary separately and also applying a multiple to group EBITDA counts
   it twice. Use the [segment]({% post_url 2027-01-28-segment-reporting %})
   figures, and check what each one includes.
3. **Forgetting the debt sits at different levels.** Net debt can belong to
   the parent or to a particular subsidiary. Subtracting it once at the top
   is a simplification; a part with its own debt may need it subtracted
   there.
4. **Treating the SOTP value as what the market "should" pay.** The gap
   between a SOTP figure and a share price is a result of the assumptions
   chosen, not a sign that either is wrong. Whether a gap ever closes isn't
   something the method can tell you.

**Takeaway:** Sum of the parts values a multi-business company one business
at a time and adds them up, which fits groups no single multiple can
describe. Every part brings its own assumption, so the total is only as
reliable as the shakiest of them.
