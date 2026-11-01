---
layout: post
title: "Hospitals: ARPOB, occupancy and bed count"
description: "A hospital earns beds × occupancy × revenue per occupied bed. ARPOB explained and rebuilt from Max Healthcare's FY26 results, plus what the lens misses."
image: /assets/og/hospitals-arpob-occupancy.png
date: 2026-11-04 09:00:00 +0530
series: fundamental-analysis
term: "ARPOB (average revenue per occupied bed)"
---

{% assign m = site.data.sectors2.max %}
{% assign d = m.derived %}

## What ARPOB means

ARPOB stands for average revenue per occupied bed — the revenue a hospital earns for each bed that has a patient in it, per day. It's the hospital world's version of a price. A bed that's empty earns nothing, so hospitals count revenue against *occupied* bed days, not against every bed they own.

A hospital's growth then comes from three levers, and each one needs a different explanation:

- **Beds:** building or buying capacity.
- **Occupancy:** how much of that capacity is in use.
- **ARPOB:** what each occupied bed earns — which moves with treatment mix, case complexity and price.

A company can grow revenue on any of the three. They don't have the same causes or the same limits, so a lens that splits them is more useful than total revenue growth alone.

## The formulas

```
Occupied bed days (OBD)  =  operational beds  ×  days in the period  ×  occupancy

ARPOB                    =  gross revenue  /  occupied bed days

Revenue                  =  OBD  ×  ARPOB
Revenue growth           ≈  (1 + OBD growth)  ×  (1 + ARPOB growth)  −  1

ALOS (average length of stay)  =  days patients spend in hospital per admission
```

Max Healthcare's own definition, from the definitions page of its investor presentation: ARPOB is gross revenue divided by occupied bed days, excluding revenue from its diagnostics-lab operations. Gross revenue is the amount billed at contracted or rack rates.

## Worked example: Max Healthcare, year to March 2026

From Max Healthcare's [press release and presentation]({{ m.source_url }}) filed on the National Stock Exchange (NSE) on {{ m.release_date }}. One basis matters before any number: these are the company's **network** figures — the company, its subsidiaries, managed hospitals and partner facilities. They are not the statutory consolidated figures, which are lower, so don't mix the two in one calculation. Historical, for illustration only. FY26 means the year ended 31 March 2026.

### Step 1: the three levers

| | FY26 | FY25 |
|---|---:|---:|
| Operational beds at year end | {{ m.beds.FY26 }} | {{ m.beds.FY25 }} |
| Occupancy | {{ m.occupancy_pct.FY26 }}% | {{ m.occupancy_pct.FY25 }}% |
| ARPOB (₹ thousand per day) | {{ m.arpob_k.FY26 }} | {{ m.arpob_k.FY25 }} |
| Average length of stay (days) | {{ m.alos_days.FY26 }} | {{ m.alos_days.FY25 }} |
| Gross revenue (₹ crore) | {{ m.gross_revenue_cr.FY26 }} | {{ m.gross_revenue_cr.FY25 }} |

1. Year-end beds rose by {{ d.net_beds_added }}, or {{ d.bed_growth_pct }}%. The release counts {{ m.beds_added_gross }} beds added in the year, less a {{ m.beds_divested }}-bed hospital divested — the difference is our arithmetic, not a printed line.
2. Occupancy moved up {{ d.occupancy_change_pts }} percentage points. The release prints occupancy in whole percentages only, so small moves can't be seen.
3. ARPOB rose {{ d.arpob_growth_pct }}% (the release prints 5%).

### Step 2: put the levers together

4. The release says occupied bed days grew {{ m.obd_growth_pct }}%. Combining that with ARPOB growth of {{ d.arpob_growth_pct }}% gives roughly {{ d.obd_times_arpob_pct }}% revenue growth. The reported gross revenue growth was {{ d.gross_rev_growth_pct }}%. They agree to within rounding, which is the point: the revenue line is two numbers multiplied.
5. Run the other formula backwards. Occupied bed days equal beds times days times occupancy, so {{ m.obd_growth_pct }}% growth in bed days, with occupancy up from {{ m.occupancy_pct.FY25 }}% to {{ m.occupancy_pct.FY26 }}%, implies average operational beds grew about {{ d.implied_avg_bed_growth_pct }}%. Year-end beds grew {{ d.bed_growth_pct }}%. These are different measures (average versus year end, and rounded occupancy), so treat the match as a sanity check, not a result.
6. Network EBITDA — earnings before interest, tax, depreciation and amortisation — was ₹{% include inr.html n=m.ebitda_cr.FY26 %} crore, which is {{ d.ebitda_margin_net_fy26 }}% of net revenue against {{ d.ebitda_margin_net_fy25 }}% a year earlier. How fixed costs make margins move with occupancy is covered in [operating leverage]({% post_url 2026-10-09-operating-leverage %}); see also [EBITDA margin]({% post_url 2026-08-28-ebitda-margin %}) for how to read that.

Max also reports that international patients brought in ₹{{ m.international_rev_cr }} crore, about {{ m.international_share_pct }}% of hospital revenue. That's a mix fact: it is one reason ARPOB can move without a price change.

This is one lens from the [Fundamental Analysis]({{ '/series/fundamental-analysis/' | relative_url }}) series. None of this is a view on Max Healthcare. It is one year's release read through the sector's metrics.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a hotel for sick people. Each bed is a room. The hotel can only earn from rooms that have a guest tonight.

If it has 100 rooms and 75 guests, it's "75% occupied". ARPOB is how much each *occupied* room brings in for the night. A guest who needs a big operation pays far more than a guest who needs a day of rest.

So the hotel can earn more by building more rooms, by filling more of them, or by treating guests who need more care. Those are three different stories, which is why we keep them apart.

</details>

## Common mistakes

- **Dividing revenue by all beds.** Revenue per bed hides occupancy. Two hospitals with the same revenue per bed can be very different: one full at a lower ARPOB, one half-empty at a higher one.
- **Reading a higher ARPOB as a price rise.** Case mix, a bigger share of complex procedures or of international patients all lift ARPOB with no tariff change. Check the company's explanation of mix.
- **Mixing network and statutory numbers, or year-end beds with a full year of days.** Network figures include managed and partner hospitals. Network revenue divided by statutory profit gives a ratio that belongs to no one. And beds added in March count at year end but add almost no occupied days.
- **Comparing ARPOB across companies without the definition.** Whether revenue is gross (billed) or net, whether diagnostics are in, and whether beds are operational or licensed all change the number. Compare a company with its own history first.

## What this lens can't tell you

- **ARPOB and occupancy are company-defined.** They sit outside the audited statements. The release gives a definition for ARPOB but no formula for occupancy, and whether it is measured on operational or licensed beds isn't stated in the pages we read.
- **New hospitals dilute everything.** A new hospital fills slowly, so occupancy and margin can fall while the business is doing what it planned. The release doesn't split new hospitals out.
- **The lens says nothing about price or quality of care.** It explains how the revenue is made; it doesn't say whether that revenue is good value for patients or for investors.
- **One year, backward-looking.** It describes FY26 only.

**Takeaway:** A hospital's revenue is occupied bed days times revenue per occupied bed, so growth can come from more beds, fuller beds or richer treatment — three different stories. ARPOB is a company-defined number; read its definition and compare a company with its own history first.
