---
layout: post
title: "REITs: structure, 90% payout and what's inside"
description: "A REIT is a trust that owns rent-earning property and must pay out most of its cash. The roles, the 80% and 90% rules in SEBI's text, and a payout example."
image: /assets/og/reit-structure.png
date: 2026-11-15 09:00:00 +0530
series: money-before-markets
term: "REIT (real estate investment trust)"
---

{% assign m = site.data.mbm %}
{% assign r = m.reit %}
{% assign rg = r.regs %}
{% assign a = r.assets %}
{% assign po = r.payout %}

## What a REIT is

A **real estate investment trust (REIT)**, as SEBI (the Securities and Exchange Board of India) now defines it, pools ₹{{ rg.pool_min_cr }} crore or more by issuing units to at least {{ rg.min_investors }} investors, to buy and manage real estate whose income goes to those investors without giving them day-to-day control. It owns income-producing property, such as leased offices, and sells **units** (defined as "beneficial interest of the REIT") to investors. Those units are listed on a stock exchange, so you can buy and sell a share of the trust without buying a building.

The rules are in SEBI's [Real Estate Investment Trusts Regulations, 2014]({{ rg.url }}), notified {{ rg.notified | date: "%-d %B %Y" }}. This post reads SEBI's consolidated text as last amended on {{ rg.last_amended | date: "%-d %B %Y" }} (read {{ rg.read | date: "%-d %B %Y" }}). SEBI's REIT master circular, which adds detail on disclosures and procedures, was not read, and SEBI amends these rules often, so check the current text before relying on any limit below. It sits in [Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}) because a REIT is another place money can go, with its own rules. InvITs (infrastructure investment trusts, the infrastructure counterpart) and how REIT payouts are taxed are not covered here.

## Who does what

The regulations define these roles:

- **Sponsor:** the person or group that sets up the REIT.
- **Trustee:** holds the REIT's assets "in trust for the benefit of the unit holders".
- **Manager:** a company, LLP (limited liability partnership) or other body corporate incorporated in India that "manages assets and investments of the REIT and undertakes operational activities".
- **SPV (special purpose vehicle):** a company or LLP in which the REIT or its holding company holds at least {{ rg.spv_min_holding_pct }}% of the equity or interest, which holds at least 80% of its assets directly in properties and doesn't invest in other SPVs, and which does nothing other than hold and develop property (and what is incidental to that). The regulations also describe a **holdco**, a holding company through which the REIT can own several SPVs.

The property sits in the SPVs or holdco, the REIT owns them, and you own units of the REIT.

## The two rules that shape a REIT

1. **Where the money sits.** At least {{ rg.assets_min_pct }}% of the value of the REIT's assets must be in completed properties that generate rent or other income (regulation 18(4)).
2. **What must be paid out.** At least {{ rg.dist_pct }}% of an SPV's *net distributable cash flows* must go to the REIT, and at least {{ rg.dist_pct }}% of the REIT's own net distributable cash flows must go to unit holders. Payouts must be declared at least once every {{ rg.dist_months }} months in each financial year. Since {{ rg.dist_rule_from | date: "%-d %B %Y" }} the record date is {{ rg.record_working_days_after_declaration }} working days after the declaration, and the payout must be made within {{ rg.dist_working_days_after_record }} working days of the record date (regulation 18(16)). Where a holdco sits in between, it must pass on all the cash it receives from SPVs and at least {{ rg.dist_pct }}% of cash it generates itself.

If a property is sold and the REIT proposes to reinvest the proceeds in another property, it is not required to distribute them. If it proposes not to reinvest them within one year, at least 90% of the proceeds must be distributed. The payout rule is about cash flows, not about profit or unit price. For why a payout isn't the same as a return, see [free cash flow]({% post_url 2026-09-19-free-cash-flow %}).

## The formulas

```
Minimum payout to the REIT       =  90% × SPV net distributable cash flows
Minimum payout to unit holders   =  90% × REIT net distributable cash flows
Minimum in income-generating property  =  80% × value of REIT assets
```

Net distributable cash flows (NDCF) are defined in the regulations; this post doesn't reproduce the definition, so the example below treats them as given.

## Worked example: a made-up REIT

Every number here is invented to show the arithmetic. It isn't any REIT.

**The asset rule.** If the REIT's assets are worth ₹{% include inr.html n=a.total_cr %} crore, at least ₹{% include inr.html n=a.rent_generating_min_cr %} crore must be in completed property that generates rent or other income, which leaves at most ₹{% include inr.html n=a.other_max_cr %} crore for everything else the regulations permit.

**The payout rule.** One SPV earns net distributable cash flows of ₹{% include inr.html n=po.spv_ndcf %} crore, and the REIT owns 100% of it directly, with no holdco. The REIT has no other cash flows.

1. The SPV must pay at least {{ rg.dist_pct }}% to the REIT: ₹{% include inr.html n=po.to_reit_min %} crore.
2. The REIT's NDCF is therefore ₹{% include inr.html n=po.reit_ndcf %} crore, and it must pay at least {{ rg.dist_pct }}% of that to unit holders: ₹{% include inr.html n=po.to_holders_min %} crore.
3. With {% include inr.html n=po.units_cr %} crore units, that is at least ₹{% include inr.html n=po.per_unit %} a unit.

At the legal minimum at each step, unit holders receive {{ po.floor_share_pct }}% of the SPV's cash flows, not 90%, because the 90% rule applies twice. These are floors. The regulations set no ceiling, and what a real REIT pays depends on its cash flows and decisions.

## Common mistakes

- **Treating "90%" as a yield.** The rule is a share of cash flows, not a return on the unit price or on the money you invested. A [dividend yield]({% post_url 2026-09-28-dividend-yield %}) is a different calculation.
- **Reading the payout as profit.** It is a share of distributable cash, so a payout can differ from accounting profit. How each part of a payout is taxed is a separate question, covered in the Tax series.
- **Ignoring the layers.** The 90% rule applies at the SPV and again at the REIT, so a chain of SPVs and holdcos changes what reaches you.
- **Assuming a unit's price follows the property's value.** The regulations define a REIT's **net asset value (NAV)** as the value of its assets reduced by external debt, divided by units outstanding. The listed price is set by trading and can differ from that figure, much as an exchange-traded fund's (ETF's) price can differ from its NAV, as the [index funds vs ETFs post]({% post_url 2026-10-13-index-funds-vs-etfs %}) explained.

**Takeaway:** A REIT is a listed trust whose rules require most of its assets to be in completed, income-generating property and most of its distributable cash to be paid out. Those are floors on structure and payout, not a promise of any return on the unit, and SEBI amends them often.
