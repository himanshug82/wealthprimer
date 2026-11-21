---
layout: post
title: "NAV cut-off time: which day's price you get"
description: "Mutual fund units are bought and sold at a NAV set by a cut-off time. SEBI's 3 pm and 1.30 pm rules, why the money's arrival matters, and worked cases."
image: /assets/og/nav-cut-off-and-allotment.png
date: 2027-04-12 09:00:00 +0530
series: mutual-funds
term: "NAV cut-off time"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign c = site.data.mf5.cutoff %}

## What a cut-off time is

A mutual fund doesn't trade all day like a share. Units are bought and sold
once a day, at that day's **NAV** (net asset value: the value of the fund's
holdings per unit, worked out after the market closes). The **cut-off time**
decides which day's NAV your purchase or redemption gets. Miss it, and your
transaction moves to the next business day's NAV.

The rules are SEBI's (the Securities and Exchange Board of India's), in its
[master circular for mutual funds]({{ c.master_circular_url }}). They matter most
on days when markets move a lot, and on large or time-sensitive amounts. This
post sets out the rules as read in November 2026, with worked cases. It's part
of [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}).
The [NAV post]({% post_url 2026-09-25-what-a-mutual-fund-is %}) explains what
the NAV is.

## The rules

From paragraphs 8.4.5 to 8.4.7 of the {{ c.master_circular }}, with paragraph
8.4.5.4 as modified by the {{ c.amendment }}. The rules cover all schemes
except international schemes and units bought or sold on a stock exchange
(paragraph 8.4.3.1):

| Transaction | Scheme | Cut-off | NAV you get |
|---|---|---|---|
| Purchase | All schemes except liquid and overnight | Money must reach the scheme and be usable | Closing NAV of the day the money is available for use, whatever time the application came in |
| Purchase | Debt schemes other than liquid and overnight | Application and money in by {{ c.other_cutoff }} | That day's closing NAV |
| Purchase | Liquid and overnight funds | Application and money in by {{ c.liquid_purchase }} | Closing NAV of the day *before* the day of receipt |
| Purchase | Liquid and overnight funds | After {{ c.liquid_purchase }}, money available the same day | Closing NAV of the day before the next business day |
| Purchase | Liquid and overnight funds | Money not available before the cut-off | Closing NAV of the day before the day the money becomes available |
| Redemption | Most schemes | Application by {{ c.other_cutoff }} | That day's closing NAV |
| Redemption | Most schemes | After {{ c.other_cutoff }} | Next business day's closing NAV |
| Redemption | Liquid and overnight funds | Application by {{ c.other_cutoff }} | Closing NAV of the day before the next business day |
| Redemption | Liquid and overnight funds | After {{ c.other_cutoff }} | Next business day's closing NAV |
| Redemption | Overnight funds, online applications | {{ c.overnight_online_redemption }} (from {{ c.overnight_online_from }}) | As above |

Three details sit under the table:

1. **For purchases, the money decides, not the form.** The circular ties the
   NAV to when the funds are "available for utilization" by the scheme,
   without any credit facility. For an equity or debt fund, a purchase
   submitted at 10 am whose money reaches the fund's bank account the next
   day gets the next day's NAV.
2. **Switches follow the same rules** (paragraph 8.4.7). A switch-out is
   treated as a redemption from the first scheme and a switch-in as a purchase
   into the second.
3. **Time is stamped where the application is received.** Cut-offs apply at
   the fund's official points of acceptance (paragraph 8.4.8), which is why a
   platform may ask for orders earlier than the fund's own cut-off.

For liquid and overnight funds, the "business day" excludes days when money
markets are closed, and these funds calculate a NAV for every calendar day
(paragraph 8.4.5.5).

## Worked cases

All of these are hypothetical, and each assumes a normal business day
followed by another.

1. **An equity fund purchase, form in on Monday morning, money arrives
   Tuesday.** The NAV is Tuesday's: the day the money became available, not
   the day the form came in.
2. **An equity fund redemption at 2.55 pm on Monday.** Monday's closing NAV.
   The same request at 3.05 pm gets Tuesday's.
3. **A liquid fund purchase, application and money in by 1 pm on Monday.**
   The NAV is Sunday's closing NAV: the day immediately before the day of
   receipt. Liquid funds publish a NAV for every calendar day, so the
   investment starts earning from Monday.
4. **A liquid fund purchase at 2 pm on Monday, money in the same day.** The
   NAV is Monday's: the day immediately before the next business day,
   Tuesday.
5. **A switch from an equity fund into a liquid fund, requested at 2 pm.**
   The switch-out is a redemption before {{ c.other_cutoff }}, at that day's
   NAV; the switch-in is a purchase, and the liquid-fund rules apply to when
   the money actually moves.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

A school canteen prices its samosas once a day, at closing time, based on
what the ingredients cost that day. If you hand in your order and money
before the bell, you pay today's price. Hand it in after the bell, and you
pay tomorrow's price, whatever it turns out to be.

And if you hand in the order but forget the money until tomorrow, the
canteen waits for the money. The price is the one for the day your money
arrived.

</details>

## Common mistakes

1. **Assuming the time you click "invest" is what counts.** For purchases the
   rule follows the money. A payment that takes a day to reach the fund's
   account shifts the NAV by a day.
2. **Treating a platform's cut-off as the fund's.** A broker or app may close
   orders earlier than the fund's own cut-off so it can pass them on in time.
3. **Thinking you can "catch" a known move.** For schemes other than liquid
   and overnight funds, the rules allow only a prospective NAV (paragraph
   8.4.6.1): one set after the cut-off, so nobody gets an old price on news
   that's already out. Liquid and overnight funds are the deliberate
   exception, using the previous day's NAV, and their holdings barely move
   from one day to the next.
4. **Forgetting the exit load clock.** A redemption's date also decides
   whether an [exit load]({% post_url 2026-10-07-exit-load %}) applies, and
   that date moves with the cut-off.

**Takeaway:** A mutual fund trade gets one NAV, set after a daily cut-off: 3 pm
for most redemptions, and for purchases, the day the money is available to the
fund. Get the form and the money in before the cut-off, and you know which
day's price you'll get.

## Sources

- {{ c.master_circular }}, paragraphs 8.4.3.1 and 8.4.5 to 8.4.8 ([SEBI]({{ c.master_circular_url }})), read on 21 November 2026.
- {{ c.amendment }}, modifying paragraph 8.4.5.4 ([SEBI]({{ c.amendment_url }})).
