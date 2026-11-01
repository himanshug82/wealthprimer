---
layout: post
title: "IPO applications: ASBA, UPI and unblocking"
description: "In an IPO your money is blocked, not paid, until allotment. How ASBA and UPI work, the T to T+3 timeline and delay compensation, on the Desi Bites IPO."
image: /assets/og/ipo-application-asba-upi.png
date: 2026-12-05 09:00:00 +0530
series: market-basics
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign i = site.data.market_basics.ipo %}

## What ASBA means

When you apply for shares in an IPO (initial public offering), you do not send the money to the company. Your bank **blocks** the amount in your own account. The money stays yours until the shares are allotted; only then does the bank debit the part that was allotted and release the rest. This is called **ASBA**, short for Application Supported by Block Amount.

For small investors, the blocking now usually happens through **UPI** (Unified Payments Interface), the same payment system you use for everyday transfers. You enter a UPI ID, and you approve a "mandate" on your UPI app that blocks the amount. SEBI (the Securities and Exchange Board of India) describes the setup in Chapter 10 of its master circular for the ICDR (Issue of Capital and Disclosure Requirements) Regulations, {{ i.master_circular }} ([source]({{ i.master_url }})), as at {{ i.as_of }}.

This post explains the mechanics only. It does not say whether any IPO is worth applying for. To read what an offer document says, see [reading a DRHP (draft red herring prospectus)]({% post_url 2026-10-09-reading-a-drhp %}); after listing, trading follows the same [rules as any other share]({% post_url 2026-12-03-order-types-explained %}). It is part of [Your first year in the market]({{ '/series/market-basics/' | relative_url }}).

## What the master circular says

| Question | As printed in the master circular |
|---|---|
| Who handles your application | An "intermediary": a syndicate member, registered stock broker, registrar and transfer agent or depository participant (DP); or you apply through your own bank (an SCSB, a "self-certified syndicate bank") |
| Paying by UPI | A retail individual investor may use a UPI ID to block funds; an individual in the non-institutional category may do so "upto the limit for which blocking through UPI is permitted (Presently it 5 lakhs)" |
| Whose account | Only your own bank account or your own bank-linked UPI ID. Applications using a third party's account or UPI ID "are liable for rejection" |
| The "retail" line | The master circular segregates investor categories at "two lakh rupees for retail category", based on the net payment amount |
| When the UPI mandate must be accepted | Annexure XXIII gives "T day – 5 pm" ("T" is the issue closing date) |
| When unblocking is due | By the closing hours of the bank day on T+2 for applicants who get no shares or only some |
| When shares list | Trading starts on T+3 |

SEBI's wording of the ₹5 lakh UPI figure is "presently", which tells you it is a number SEBI revises. **Check the current rule** and the offer document for any issue you look at.

## The timeline in days

"T" is the day the issue closes. The master circular's Annexure XXIII ("Indicative timeline of activities for listing of shares through Public Issues on T+3 day") spreads the work like this:

| Day | What happens (as printed) |
|---|---|
| T | Applications accepted; UPI mandates accepted up to 5 pm; issue closes at 5 pm for the retail category |
| T+1 | Third-party checks on UPI applications completed before 9:30 am; rejections finalised before 6 pm; basis of allotment approved by the exchange before 9 pm |
| T+2 | Debit and unblock instructions issued from 9:30 am; fund transfers complete before 2 pm and unblocking before 4 pm; shares are credited to demat accounts before 6 pm (see [how a demat account works]({% post_url 2026-12-01-demat-trading-bank-accounts %})) |
| T+3 | Trading starts |

(Times are those in the annexure as at {{ i.as_of }}. "Indicative" is SEBI's word.)

## Worked example: a Desi Bites application

Desi Bites Foods is the blog's fictional company. Its invented IPO is a fresh issue of {{ i.fresh_shares_lakh }} lakh shares at ₹{{ i.price }}, raising ₹{% include inr.html n=i.fresh_proceeds_lakh %} lakh. The offer document would set the **lot**: the smallest number of shares you can bid for. We assume a lot of {{ i.lot }} shares, so one lot costs {{ i.lot }} × ₹{{ i.price }} = ₹{% include inr.html n=i.lot_amt %}. Real lot sizes are set per issue.

Three hypothetical applicants:

| Applicant | Bid | Amount blocked | Outcome | What happens to the money |
|---|---|---|---|---|
| A | 1 lot | ₹{% include inr.html n=i.lot_amt %} | Not allotted | Whole amount unblocked by T+2 |
| B | 1 lot | ₹{% include inr.html n=i.lot_amt %} | Allotted 1 lot | ₹{% include inr.html n=i.lot_amt %} debited; {{ i.lot }} shares credited on T+2; trading on T+3 |
| C | 2 lots | ₹{% include inr.html n=i.two_lot_amt %} | Allotted 1 lot | ₹{% include inr.html n=i.lot_amt %} debited, the other ₹{% include inr.html n=i.lot_amt %} unblocked by T+2 |

How many lots a retail bidder can take: at ₹{% include inr.html n=i.lot_amt %} a lot, {{ i.max_lots }} lots come to ₹{% include inr.html n=i.max_amt %}, under the ₹{% include inr.html n=i.retail_cap_rs %} retail line. A {{ i.over_cap_lots }}th lot would make ₹{% include inr.html n=i.over_cap_amt %}, which crosses it, and the application would be counted in a different investor category with different rules. How shares are shared out when an issue is oversubscribed is in the offer document and is not covered here.

## Delay compensation

If the bank is late unblocking money, the master circular sets a compensation. For each day of delay, it is "Rs.100/- per day or 15% per annum of the application amount, whichever is higher", payable by the bank; the circular adds a similar amount payable by the post-issue lead manager for delay in resolving a complaint. SEBI's text says the compensation for delay in unblocking is computed from T+3.

If the 15% a year is spread evenly over {{ i.comp_basis_days }} days (an assumption: the circular says "per annum"), which side is higher depends on the amount:

| Application amount (₹) | 15% a year, per day (₹) | Higher of that and ₹{{ i.comp_per_day }} (₹) |
|---:|---:|---:|
{% for r in i.comp_rows -%}
| {{ r.amount }} | {{ r.pct_per_day }} | {{ r.per_day }} |
{% endfor %}

The two are equal at about ₹{% include inr.html n=i.comp_breakeven %}. Below that the flat ₹{{ i.comp_per_day }} a day is the higher figure, which covers most retail applications. If your money is late, the route to claiming is a complaint to the intermediary or bank; SEBI's complaint system, SCORES (SEBI Complaints Redress System), is the usual next step, and a later post in this series covers it.

## Common mistakes

- **Treating blocked money as spent.** Blocking is not payment. In the example, applicants A and C get money back; only the allotted part is debited.
- **Missing the UPI mandate window.** The annexure puts UPI mandate acceptance at 5 pm on T. An application whose mandate is never approved cannot be funded.
- **Using someone else's account or UPI ID.** Applications from a third party's account or UPI ID are liable for rejection under the circular.
- **Expecting money and shares on the same day as listing.** Unblocking is due by T+2 and trading starts on T+3; the credit of shares is on T+2.

**Takeaway:** In an IPO your bank blocks the money and releases it by T+2 if you are not allotted; shares arrive on T+2 and trading starts on T+3. Use only your own account, approve the UPI mandate in time, and check the current rule, as SEBI's figures such as the ₹5 lakh UPI limit are revised.
