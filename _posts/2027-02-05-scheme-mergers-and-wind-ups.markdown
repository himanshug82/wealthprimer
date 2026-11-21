---
layout: post
title: "Scheme mergers and wind-ups: what happens to your units"
description: "When a mutual fund scheme merges or winds up, SEBI's rules set your options: the exit window, how units convert at NAV, and how a wind-up pays out."
image: /assets/og/scheme-mergers-and-wind-ups.png
date: 2027-02-05 09:00:00 +0530
series: mutual-funds
term: "Scheme merger and wind-up"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign m = site.data.mf5.merger %}
{% assign c = site.data.mf5.cutoff %}

## What a merger and a wind-up are

Fund houses sometimes **merge** two schemes into one. The master circular of
SEBI (the Securities and Exchange Board of India)
allows a fund house only one scheme per category, with exceptions such as
index funds tracking different indices (paragraph 2.8.1), so two look-alike
schemes in one category can't both carry on. Occasionally a scheme is **wound up**: closed, its holdings
sold and the money paid out to unitholders. Both change what you own, and
both come with rules about what you must be told and what you can do.

This post sets out those rules as read in November 2026 in the SEBI (Mutual
Funds) Regulations, 2026 and SEBI's master circular, with a worked example.
It's part of [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}).
An AMC is the asset management company that runs the fund.

## The rules

**A merger is a change in fundamental attributes.** The master circular
(paragraph 2.2.1) treats any consolidation or merger of schemes as a change
in the "fundamental attributes" of the schemes involved. Under the
regulations ([regulation 22(9)(c), "Changes to scheme attribute"]({{ m.regs_url }})),
such a change can't be made unless:

- each unitholder is sent a written communication (email or SMS counts),
- the details are displayed on the AMC's website, and
- unitholders are given an option to exit at the prevailing NAV (net asset
  value) **without any exit load**.

Wherever an exit option has to be given, the master circular (paragraph
17.10.1) sets at least {{ m.exit_days }} calendar days to use it. The merger
letter goes to the unitholders of all the schemes involved (paragraph
2.2.2.2). The scheme being merged away always has to offer its unitholders
the exit. The surviving scheme's unitholders get it too, unless all three
conditions in paragraph 2.2.2.5 hold: its fundamental attributes don't
change, the fund house can show the circumstances merit the merger, and its
unitholders' interests aren't adversely affected.

**A wind-up has its own steps** (regulations 36 to 38). A scheme is wound up
if the trustees think an event requires it, if {{ m.wind_up_majority_pct }}% of
its unitholders pass a resolution, or if SEBI directs it. Then:

1. The trustees give notice within {{ m.notice_days }} day, to SEBI and in
   newspapers.
2. Where the trustees started it, unitholders vote by simple majority, one
   vote per unit, with results published within {{ m.vote_days }} days. If
   the vote fails, the scheme reopens.
3. From the notice, the scheme stops issuing and redeeming units, and its
   units are listed on a stock exchange.
4. Its assets are sold, liabilities paid, winding-up expenses provided for,
   and the rest paid to unitholders in proportion to their holdings on the
   date of the decision.

## Worked example: a merger, unit by unit

A hypothetical case. You hold {{ m.fmt.units_a }} units of Scheme A, NAV
₹{{ m.fmt.nav_a }}. Scheme A is being merged into Scheme B, NAV ₹{{ m.fmt.nav_b }}.

```
Value of your holding   =  {{ m.fmt.units_a }} × ₹{{ m.fmt.nav_a }}  =  ₹{{ m.fmt.value }}
Units of B you receive  =  ₹{{ m.fmt.value }} ÷ ₹{{ m.fmt.nav_b }}  =  {{ m.fmt.units_b }} units
```

Your unit count changes by the ratio of the two NAVs, here from
{{ m.fmt.units_a }} to {{ m.fmt.units_b }}, and the value doesn't change. A merger
converts at NAV: nothing is gained or lost in the swap itself. What changes is
the scheme you now hold: B's portfolio, B's fund manager, B's expense ratio.

**Your options in the exit window:**

| Option | What happens |
|---|---|
| Do nothing | Your units convert into B's at NAV on the merger date |
| Exit during the window | Redeemed at the prevailing NAV, with no exit load |
| Exit after the window | Redeemed as normal; whatever exit load terms then apply are set out in the merger letter and the surviving scheme's documents |

The NAV for an exit follows the usual cut-off rules, which the
[NAV cut-off post]({% post_url 2027-02-02-nav-cut-off-and-allotment %})
explains.

## Common mistakes

1. **Reading a merger as a loss or a gain.** Conversion happens at NAV, so
   the number of units changes and the value doesn't. Comparing unit counts
   before and after misleads.
2. **Missing the exit window.** The load-free exit lasts a set period after
   the notice. After it, normal exit load terms apply; the merger letter says
   which.
3. **Assuming the old scheme's record carries over.** The master circular
   sets rules for which scheme's past performance is shown after a merger.
   The record you see afterwards may be the surviving scheme's, not the one
   you held. The [manager changes and style drift post]({% post_url 2026-10-23-manager-changes-and-style-drift %})
   covers reading a track record across changes.
4. **Treating a wound-up scheme like a redemption.** Once the notice is out,
   the scheme stops redeeming; the money comes when the assets are sold, in
   proportion to holdings on the decision date. How long that takes depends
   on what the scheme holds; the
   [segregated portfolios post]({% post_url 2026-10-24-segregated-portfolios %})
   shows a case where some holdings couldn't be sold quickly.

This post doesn't cover tax. The master circular requires the merger letter
to state the tax impact on unitholders (paragraph 2.2.2.2); the rules
themselves are in the Income-tax Act, so check the current rule.

**Takeaway:** When a mutual fund scheme merges, your units convert at NAV and
you get a load-free window to leave. When it winds up, it stops redemptions and
pays out what selling its holdings realises, after liabilities and winding-up
costs.

## Sources

- [SEBI (Mutual Funds) Regulations, 2026, as amended to 10 October 2026]({{ m.regs_url }}), regulation 22(9)(c) ("Changes to scheme attribute") and regulations 36 to 38, read on 21 November 2026.
- [{{ c.master_circular }}]({{ c.master_circular_url }}), paragraphs 2.2, 2.8.1, 13.4 and 17.10.1.
