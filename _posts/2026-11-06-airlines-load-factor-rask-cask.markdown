---
layout: post
title: "Airlines: load factor, RASK and CASK"
description: "An airline sells seats on a fixed schedule, so load factor, RASK and CASK decide the result. The three explained and rebuilt from IndiGo's FY26 results."
image: /assets/og/airlines-load-factor-rask-cask.png
date: 2026-11-06 09:00:00 +0530
series: fundamental-analysis
term: "RASK and CASK"
---

{% assign g = site.data.sectors2.indigo %}
{% assign d = g.derived %}

## What RASK and CASK mean

An airline sells a perishable product: once the plane leaves, an empty seat can never be sold. So airlines count everything per seat-kilometre flown.

- **ASK** (available seat kilometres) is seats on offer times kilometres flown — the capacity.
- **RPK** (revenue passenger kilometres) is paying passengers times kilometres flown — the capacity actually used.
- **Load factor** is RPK divided by ASK: the share of seats that carried a paying passenger.
- **RASK** (revenue per ASK) is revenue divided by ASK.
- **CASK** (cost per ASK) is cost divided by ASK.

RASK minus CASK is the profit or loss on every seat-kilometre the airline flew, full or empty. That's why the lens is useful: the schedule is committed in advance, so most costs are incurred whether or not the seats fill.

## The formulas

```
Load factor   =  RPK / ASK
Yield         =  passenger revenue / RPK         (what a flown passenger-km earns)
RASK          =  revenue / ASK
CASK          =  cost / ASK
CASK ex-fuel  =  (cost − fuel cost) / ASK        (fuel is the big cost the airline can't set)

RASK − CASK   =  result per seat-kilometre
```

Each airline defines RASK and CASK its own way. IndiGo's per-kilometre figures are net of finance income, so you cannot reproduce them by dividing total income by ASK.

## Worked example: IndiGo, year to March 2026

From InterGlobe Aviation's [press release]({{ g.source_url }}), [presentation]({{ g.presentation_url }}) and [audited results]({{ g.results_url }}), filed with the National Stock Exchange on {{ g.release_date }}. Consolidated. IndiGo prints RASK, CASK and CASK ex-fuel itself, so none is derived here. FY26 is the year ended 31 March 2026. Historical, for illustration only.

### Step 1: capacity and load

| | FY26 | FY25 |
|---|---:|---:|
| ASK (billion) | {{ g.ask_bn.FY26 }} | {{ g.ask_bn.FY25 }} |
| RPK (billion) | {{ g.rpk_bn.FY26 }} | {{ g.rpk_bn.FY25 }} |
| Load factor | {{ g.load_factor_pct.FY26 }}% | {{ g.load_factor_pct.FY25 }}% |
| Yield (₹ per km) | {{ g.yield_inr.FY26 }} | {{ g.yield_inr.FY25 }} |

1. Capacity (ASK) grew {{ d.ask_growth_pct }}% but traffic (RPK) grew {{ d.rpk_growth_pct }}%, so the load factor fell {{ d.load_factor_change_pts | abs }} percentage points. Capacity grew faster than the demand that filled it.
2. Yield fell {{ d.yield_change_pct | abs }}%. So each flown passenger-kilometre earned slightly less.

### Step 2: RASK against CASK

| ₹ per ASK | FY26 | FY25 |
|---|---:|---:|
| RASK | {{ g.rask_inr.FY26 }} | {{ g.rask_inr.FY25 }} |
| CASK | {{ g.cask_inr.FY26 }} | {{ g.cask_inr.FY25 }} |
| RASK − CASK | {{ d.rask_minus_cask_fy26 }} | {{ d.rask_minus_cask_fy25 }} |
| CASK ex-fuel | {{ g.cask_ex_fuel_inr.FY26 }} | {{ g.cask_ex_fuel_inr.FY25 }} |
| CASK ex-fuel, ex-forex | {{ g.cask_ex_fuel_ex_forex_inr.FY26 }} | {{ g.cask_ex_fuel_ex_forex_inr.FY25 }} |

3. The company prints RASK down {{ g.rask_change_printed_pct | abs }}% and CASK up {{ g.cask_change_printed_pct }}%. (Our own percentage from the rounded rupee figures differs by 0.1 point; the printed ones are the company's.) The gap between them swung from {{ d.rask_minus_cask_fy25 }} to {{ d.rask_minus_cask_fy26 }} rupees per ASK.
4. Fuel cost per ASK was ₹{{ g.fuel_cask_inr.FY26 }}, about {{ d.fuel_share_of_cask_pct }}% of CASK. Total fuel cost fell {{ d.fuel_cost_change_pct | abs }}% to ₹{% include inr.html n=d.fuel_cost_cr.FY26 %} crore while capacity rose, so fuel per seat-kilometre fell.
5. The ex-fuel figure rose from ₹{{ g.cask_ex_fuel_inr.FY25 }} to ₹{{ g.cask_ex_fuel_inr.FY26 }}. About ₹{{ d.forex_in_cask_ex_fuel_fy26 }} of FY26's figure is foreign-exchange effects: the release names rupee depreciation as a driver, and in our view that is because many airline costs, such as aircraft leases, are tied to the dollar. Strip that out and the figure is ₹{{ g.cask_ex_fuel_ex_forex_inr.FY26 }}, up {{ d.cask_ex_fuel_ex_forex_change_pct }}%.

The release states the reasons for the reported loss in its own words: sharp rupee depreciation, changes in labour laws and a challenging operating environment. It reports a net loss of ₹{% include inr.html n=d.pat_cr.FY26 %} crore, against a profit of ₹{% include inr.html n=d.pat_cr.FY25 %} crore a year earlier. It also prints a profit "excluding forex and exceptional items" of ₹{% include inr.html n=d.profit_ex_cr.FY26 %} crore. That second figure is a company-defined, non-audited measure; the audited number is the loss.

### Step 3: why leases matter here

6. EBITDAR (earnings before interest, tax, depreciation, amortisation and rentals) was ₹{% include inr.html n=d.ebitdar_cr.FY26 %} crore, {{ d.ebitdar_margin_pct.FY26 }}% of revenue from operations, against {{ d.ebitdar_margin_pct.FY25 }}% a year earlier. The "R" adds back aircraft rentals, because many aircraft are leased rather than owned.
7. The company's own debt measure including capitalised operating leases was ₹{% include inr.html n=d.total_debt_cr %} crore, of which ₹{% include inr.html n=d.cap_op_lease_cr %} crore ({{ d.cap_lease_share_of_debt_pct }}%) was the capitalised operating lease liability. The audited balance sheet's total lease liabilities were ₹{% include inr.html n=d.audited_lease_liab_cr.FY26 %} crore — a larger, differently scoped figure, because it also includes other lease obligations. The two measures aren't interchangeable; the release doesn't give a bridge.

Under the lease accounting standard (Ind AS 116 — Indian Accounting Standard 116), rentals move below EBITDA as depreciation and interest, as the [telecom post]({% post_url 2026-10-23-telecom-arpu-and-the-limits-of-sector-lenses %}) explains. Interest on lease liabilities was ₹{% include inr.html n=d.lease_interest_cr.FY26 %} crore in FY26. For leverage ratios, see [net debt/EBITDA]({% post_url 2026-09-18-net-debt-ebitda %}) and keep lease treatment consistent.

This is one lens from the [Fundamental Analysis]({{ '/series/fundamental-analysis/' | relative_url }}) series, and one year's release. It's not a view on IndiGo.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

A school bus leaves at 8 a.m. whether it carries 20 kids or 40. The fuel, the driver and the bus payment cost the same either way.

"Load factor" is how full the bus was. "RASK" is what you collect per seat per kilometre; "CASK" is what it costs you per seat per kilometre. If you collect less than you spend per seat, the bus loses money on that trip — no matter how busy the road looked.

</details>

## Common mistakes

- **Reading load factor alone.** A full plane at a low yield can earn less than a half-empty one at a higher yield. Look at load factor, yield and RASK together.
- **Comparing CASK with the fuel in or out inconsistently.** Fuel prices and currency swing the headline CASK. CASK ex-fuel is a cleaner view of costs the airline controls — but ex-forex versions are company-defined and need the definition.
- **Rebuilding RASK from total income.** The company's RASK is per ASK and net of finance income; total income divided by ASK gives a different number. Use the company's printed one or its stated method.
- **Mixing lease treatments.** Debt with capitalised leases against EBITDAR, or debt without them against EBITDA — never one of each.

## What this lens can't tell you

- **It describes one year.** Fuel prices, the rupee and regulation moved in FY26; nothing says they will repeat.
- **Most of the metrics are company-defined.** ASK, load factor and yield are standard; RASK, CASK and the "ex-forex" versions aren't.
- **It says nothing about price.** What any airline is worth is a separate question this post doesn't ask.

**Takeaway:** An airline's seats perish when the plane leaves, so what matters is revenue per seat-kilometre against cost per seat-kilometre, and how full the seats were. RASK and CASK are company-defined, so read the definition and watch what fuel and currency are doing to the headline.
