---
layout: post
title: "Segregated portfolios: side pockets, and the 2020 Franklin Templeton wind-up"
description: "How a side pocket ring-fences a defaulted bond so no one can dump the loss on others, and a sourced timeline of the 2020 Franklin Templeton wind-up."
image: /assets/og/segregated-portfolios.png
date: 2026-10-24 09:00:00 +0530
series: mutual-funds
term: "Segregated portfolio (side pocket)"
---

{% assign m = site.data.mf3 %}
{% assign g = m.segregation %}
{% assign sg = m.reg.segregation %}
{% assign r = m.reg %}
{% assign ft = m.franklin %}
{% assign so = ft.sebi_order %}
{% assign ev = ft.evoting %}

## The problem a side pocket solves

A debt fund holds dozens of bonds. One day a rating agency downgrades one of
them below investment grade — the borrower may not pay. What's that bond
worth now? Nobody knows. It might recover most of its value in a
restructuring, or almost none.

The fund still has to publish a [NAV]({% post_url 2026-09-25-what-a-mutual-fund-is %})
(net asset value) every day, so it marks the bond down to a guess. And that
guess creates a race:

- If the markdown is **too small**, investors who redeem now get paid out at
  a NAV that still counts the bad bond at too much, and the eventual loss
  falls on whoever stays.
- If it's **too large** and the borrower later pays more, new investors who
  bought at the depressed NAV collect a windfall that belonged to the people
  who were holding when the bond went bad.

Either way, the investors most alert to the news get the better deal, at the
expense of the rest. The [debt funds post]({% post_url 2026-10-12-debt-funds-explained %})
covered credit risk; this is what happens *after* it bites.

## Definition: what a segregated portfolio is

A **segregated portfolio** — informally a **side pocket** — splits the scheme
in two on the day of the credit event. The bad paper goes into the
segregated portfolio; everything else stays in the **main portfolio**. SEBI (the
Securities and Exchange Board of India) introduced the option in circular {{ sg.circular }}, extended it to unrated
paper on actual default in {{ sg.unrated_circular }}, and it now sits in
paragraph {{ sg.mc_para }} of the [Master Circular for Mutual Funds]({{ r.mc26.url }})
({{ r.mc26.date | date: "%-d %B %Y" }}). The key rules:

| Rule | What it says |
|---|---|
| Trigger | A downgrade to below investment grade (or further downgrades from there) by a SEBI-registered rating agency; for unrated paper, an actual default |
| Optional | At the fund house's discretion, only if the scheme's documents allow it; trustees must approve, within {{ sg.trustee_days }} business day, with subscriptions and redemptions suspended until they do |
| Who gets units | "All existing investors in the scheme as on the day of the credit event shall be allotted equal number of units in the segregated portfolio as held in the main portfolio" |
| New money | New investors get units in the main portfolio only |
| Redemptions | Redeeming investors are paid the main portfolio's NAV and *keep* their segregated units |
| Exit from the side pocket | No redemptions; units listed on a stock exchange within {{ sg.listing_business_days }} business days so they can be sold |
| Recovery | Any money recovered, even after a write-off, is "immediately distributed to the investors in proportion to their holding in the segregated portfolio" |
| Fees | No investment management fee on the segregated portfolio; its costs can never be charged to the main portfolio |
| Manager incentives | Trustees must be able to cut or claw back the fund managers' performance pay over the segregated paper |

## The formula

```
On the credit event day:

  Main NAV        = (Total assets − bad bond) ÷ units
  Segregated NAV  = (Bad bond at its marked-down value) ÷ units      (same number of units)

  Your holding    = your units × Main NAV  +  your units × Segregated NAV

Later, on recovery:
  Payout per segregated unit = amount recovered ÷ units
```

The total value on the day is the same as without segregation. What changes
is **who owns the bad bond from here on**: exactly the people who held the
fund when it went bad, in proportion to their units.

## Worked example: a hypothetical debt fund

A **hypothetical** debt scheme with ₹{% include inr.html n=g.aum_cr %} crore of assets and
{{ g.units_cr }} crore units: NAV ₹{{ g.nav_before }}. One bond, ₹{% include inr.html n=g.bond_cr %} crore
({{ g.bond_share_pct }}% of the fund), is downgraded to below investment grade. The
valuation agencies mark it down {{ g.valuation_haircut_pct }}%, to ₹{{ g.marked_cr }} crore. You hold
{% include inr.html n=g.investor_units %} units.

1. **Before the event**, your holding is worth ₹{% include inr.html n=g.investor_before %}.
2. **Without a side pocket**, the NAV drops to ₹{{ g.no_seg_nav }} and you hold
   ₹{% include inr.html n=g.investor_no_seg %}.
3. **With a side pocket**, the main NAV is ₹{{ g.main_nav }} — the fund without the
   bond — and you get {% include inr.html n=g.investor_units %} segregated units at ₹{{ g.seg_nav }}.
   Your holding: ₹{% include inr.html n=g.investor_main %} + ₹{% include inr.html n=g.investor_seg_marked %} = ₹{% include inr.html n=g.investor_no_seg %} — the same total, split in two.
4. **Two years later the fund recovers {{ g.recovery_pct }}% of the bond's face value**, ₹{{ g.recovered_cr }}
   crore. That's ₹{{ g.per_unit_recovery }} per segregated unit, so ₹{% include inr.html n=g.investor_recovery %} is paid to you —
   because you held the fund on the day it went bad.

Now see what the side pocket prevented. Without it, the recovery is
₹{{ g.excess_recovery_cr }} crore more than the ₹{{ g.marked_cr }} crore the bond was marked at, and it
flows into the NAV of whoever holds the fund *on the recovery day*: about
₹{{ g.excess_per_unit }} a unit, or {{ g.no_seg_gain_pct }}% on the NAV of ₹{{ g.no_seg_nav }}.
Someone who bought the day after the downgrade would share in it; you, if
you'd redeemed in between, wouldn't. With the side pocket, new money never
touches the bad bond, redeeming investors keep their claim on it, and the
race has no prize.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Ten friends share a big box of mangoes. One mango looks rotten — maybe it's
fine inside, maybe not.

Without a side pocket, anyone can leave the group right now and take their
share of mangoes, counting the maybe-rotten one as worth something. Anyone
new can join and get a share of whatever it turns out to be.

With a side pocket, the doubtful mango goes into a little separate bag with
the ten friends' names on it. The good mangoes stay in the big box, where
people can come and go. Whatever the doubtful mango turns out to be worth, it
belongs to the ten friends who were there when it went bad — nobody else.

</details>

## Case study: Franklin Templeton's six debt schemes, 2020

A side pocket handles *one bad bond*. What happened in April 2020 was a
different problem, and it's the episode most Indian debt-fund investors
remember. What follows is only what court orders, SEBI's order and the fund
house's own disclosures record.

On {{ ft.wind_up_date | date: "%-d %B %Y" }}, the trustees of Franklin
Templeton Mutual Fund decided to wind up six debt schemes:
{% for x in ft.schemes %}{{ x }}{% if forloop.last %}.{% elsif forloop.rindex == 2 %} and {% else %}, {% endif %}{% endfor %}
The reason given, as reproduced in the Supreme Court's order of
{{ ft.sc_feb2021.date | date: "%-d %B %Y" }}: "it is no longer possible for
certain schemes of Franklin Templeton to generate adequate liquidity to fund
daily redemptions", in light of "the severe market dislocation" and
illiquidity caused by the Covid-19 pandemic. Winding up meant redemptions
stopped, and the portfolios would be sold down and the proceeds paid out
over time.

| Date | What happened | Source |
|---|---|---|
| {{ ft.wind_up_date | date: "%-d %b %Y" }} | Trustees decide to wind up the six schemes | [SEBI order]({{ so.url }}) |
| {{ ft.hc_date | date: "%-d %b %Y" }} | Karnataka High Court holds that winding up needs unitholders' consent | As described in the [Supreme Court's order]({{ ft.sc_feb2021.url }}) |
| {{ ev.dates }} | Unitholders vote by e-voting; in each scheme {{ ev.for_by_holders_min }}%–{{ ev.for_by_holders_max }}% of those voting (by number) vote for winding up | [Supreme Court order]({{ ft.sc_feb2021.url }}) |
| {{ ft.sc_feb2021.date | date: "%-d %b %Y" }} | Supreme Court appoints SBI Funds Management (State Bank of India's fund house) to carry out the winding up, including selling the assets and paying unitholders | [Supreme Court order]({{ ft.sc_feb2021.url }}) |
| {{ so.date | date: "%-d %b %Y" }} | SEBI order against the fund house (below) | [SEBI order]({{ so.url }}) |
| June–July 2021 | The Securities Appellate Tribunal (SAT) stays SEBI's order, subject to a ₹{{ ft.sat_escrow_cr }} crore escrow deposit | [Franklin Templeton disclosure]({{ ft.ft_disclosure_url }}) |
| {{ ft.sc_jul2021.date | date: "%-d %b %Y" }} | Supreme Court rules that unitholder consent is to be sought after the wind-up notice, not before it | [Supreme Court judgment]({{ ft.sc_jul2021.url }}) |
| {{ ft.distributed_as_of | date: "%-d %b %Y" }} | ₹{% include inr.html n=ft.distributed_cr %} crore distributed across the six schemes — {{ ft.distributed_pct_of_aum }}% of their assets under management on 23 April 2020 | [Franklin Templeton]({{ ft.ft_page_url }}) |
| {{ ft.sat_pending_as_of | date: "%-d %b %Y" }} | Appeals at SAT still pending, per the fund house's disclosure | [Franklin Templeton disclosure]({{ ft.ft_disclosure_url }}) |

SEBI's order of {{ so.date | date: "%-d %B %Y" }} ({{ so.number }}) directed the
asset management company not to launch any new debt scheme for
{{ so.debt_scheme_bar_years }} years, to refund the investment management and advisory fees it had
collected on the six schemes from 4 June 2018 to 23 April 2020 with
{{ so.interest_pct }}% simple interest — ₹{{ so.refund_cr }} crore in all — and to pay a penalty of
₹{{ so.penalty_cr }} crore. The findings behind those directions are set out in the order
itself; the fund house appealed, and we've found no final SAT ruling as of
this post's writing.

What the case teaches about **mechanisms**, which is all this post claims:

1. **Side pockets are for credit events, not liquidity.** The segregation
   rules trigger on a downgrade or default of a specific instrument. The
   trustees' stated problem was being unable to raise enough cash for
   redemptions across the portfolios — a different problem that a side
   pocket isn't built to solve.
2. **Illiquid paper and daily redemptions are a mismatch.** An open-ended
   fund promises daily exits. If what it holds can't be sold quickly without
   a large price cut, that promise depends on markets staying calm.
3. **Winding up locks everyone in together.** Like a side pocket, it stops
   early leavers from exiting at others' expense — but for the whole fund,
   for as long as the sell-down takes. Unitholders in these schemes were
   paid in tranches over several years.

## Common mistakes

- **Reading a side pocket as a loss.** It's a *separation*, not a
  writedown. The markdown happens either way; the side pocket decides who
  owns the outcome.
- **Selling the segregated units in a panic.** They're listed so you *can*
  exit, but a thin market for units of a defaulted bond can pay far less than
  the eventual recovery — or more. Know that you're making a bet either way.
- **Ignoring the footnote.** A scheme's performance figures must show the fall
  in NAV from segregation and any recoveries, for at least
  {{ sg.disclosure_years }} years after the paper is fully recovered or written off. A fund
  with a side pocket in its history is telling you something about the credit
  risk it took.
- **Assuming "debt fund" means your money is always a day away.** The rules
  allow redemptions to be suspended in some circumstances, and 2020 showed a
  whole scheme can be wound up. Liquidity is a property of what the fund
  holds, not of its label.

**Takeaway:** A side pocket splits a defaulted bond away from the rest of a
debt fund, so only the people who held the fund when it went bad bear the
loss or share the recovery. It stops a run on one bad bond; it can't create
liquidity a whole portfolio doesn't have, as the 2020 Franklin Templeton
wind-up showed.
