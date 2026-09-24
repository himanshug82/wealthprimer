---
layout: post
title: "SIPs and FIFO: one redemption, sixty tax lots"
description: "One redemption, sixty tax lots. Why each SIP instalment is a separate acquisition with its own holding-period clock, and how FIFO decides which units go first."
image: /assets/og/sips-and-fifo.png
date: 2026-11-02 09:00:00 +0530
series: tax
term: "FIFO (tax lots)"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}
{% assign s = t.example_sip %}

*Rules described here apply to **{{ r.financial_year }}**. Educational content, not tax
advice.*

## A SIP is not one investment

It feels like one. One instruction, one fund, one folio, one line on your
statement. For tax, it is nothing of the sort.

**Every instalment is a separate acquisition**, with its own date, its own
cost, and its own holding-period clock. A five-year monthly SIP isn't one
investment held five years — it's sixty investments, the oldest held five
years and the newest held a month.

That single fact drives everything else in this post.

## FIFO: which units leave first

When you redeem part of a holding, which units did you sell? You didn't
specify, and it matters enormously, because different lots have different
costs and different holding periods.

Indian tax law answers with **FIFO — First In, First Out**. The units you
bought earliest are treated as the units sold first.

```
Redeem  ->  oldest units go first
        ->  their cost and their purchase date determine the gain
```

FIFO is generally favourable for a long-running SIP, because the oldest units
are the ones most likely to have crossed the twelve-month line and qualify
for the long-term rate. But it also means your remaining holding is
progressively made up of *newer*, shorter-held units — so a second redemption
soon after is more likely to be short-term.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a tall glass jar where you drop in a coin every month, and it can
only be emptied from the bottom.

The coins at the bottom are the oldest ones. When you take money out, those
come out first — that's FIFO.

Now suppose coins become "special" once they've been in the jar a year, and
special coins are cheaper to spend. The bottom coins are usually special. But
if you empty a lot at once, you start reaching the newer coins near the top,
and those aren't special yet.

That's the whole rule. Oldest out first, and how long each coin sat there
decides what it costs you to spend it.

</details>

## Worked example: sixty instalments, one redemption

A ₹{% include inr.html n=s.monthly_amount %} monthly SIP into the fund used throughout this blog, running from
{{ s.start }} to {{ s.last_instalment }}, redeemed in full on {{ s.redemption_date }}:

| | |
|---|---:|
| Instalments | {{ s.instalments_total }} |
| Total invested | ₹{% include inr.html n=s.invested %} |
| Value at redemption | ₹{% include inr.html n=s.value %} |
| **Total gain** | **₹{% include inr.html n=s.total_gain %}** |

Now the part a single "total gain" number hides. Of those {{ s.instalments_total }} instalments,
**{{ s.long_term_lots }} had been held more than twelve months and {{ s.short_term_lots }} had not**:

| | Lots | Result |
|---|---:|---:|
| Long-term (held > {{ r.equity_holding_months }} months) | {{ s.long_term_lots }} | ₹{% include inr.html n=s.long_term_gain %} |
| Short-term (held ≤ {{ r.equity_holding_months }} months) | {{ s.short_term_lots }} | a **loss** of ₹{% include inr.html n=s.short_term_loss_abs %} |

One redemption, on one day, from one fund — producing a long-term gain and a
short-term *loss* simultaneously. That isn't unusual; it's what a SIP
redemption normally looks like when the recent market has been weak, as it
was in early 2026.

## And the tax comes to nothing

Work it through:

- The long-term gain of ₹{% include inr.html n=s.long_term_gain %} is below the ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption, so no tax
  is due on it.
- The short-term result is a loss, so there's no short-term tax either — and
  that loss can be [set off or carried forward]({% post_url 2026-11-01-losses-set-off-and-harvesting %}).

**Total tax on a ₹{% include inr.html n=s.total_gain %} gain: zero.**

That outcome is real, and it's worth being careful about what it does and
doesn't show. It isn't clever planning — nobody arranged it. It's the
arithmetic of a moderate gain meeting a generous annual exemption. A larger
SIP, or a stronger final year, and there would have been tax to pay. The
lesson isn't "SIPs are tax-free"; it's that you cannot know your tax from the
headline gain without splitting it by lot.

## What follows practically

**Redeeming the whole thing in one financial year concentrates the gain.**
Everything lands in one year, against one ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption. Splitting a large
redemption across two financial years gets two exemptions — the difference is
worth up to about ₹16,250 in tax, for nothing more than waiting until April.

**Stopping a SIP doesn't start any clock.** Holding periods run from each
instalment's own purchase date, regardless of whether you're still investing.

**Switching between funds is a redemption.** A switch — even within the same
fund house — is a sale of one scheme and a purchase of another. It's a
taxable event. So is moving from regular to direct plans of the same fund,
which is worth knowing before acting on the
[expense ratio post]({% post_url 2026-10-21-expense-ratios-direct-vs-regular %}): the ongoing saving is real, but
the switch itself may trigger tax now.

**Dividend reinvestment creates new lots.** Each reinvested payout is a fresh
purchase with a fresh date and its own clock.

## Common mistakes

- **Treating a SIP as one investment with one holding period.** Each
  instalment stands alone.
- **Assuming a long-running SIP is all long-term.** The most recent twelve
  months of instalments never are.
- **Expecting to choose which units you sell.** FIFO decides, not you.
- **Redeeming everything in one financial year without thinking.** One
  exemption instead of two.
- **Forgetting a switch is a sale.** Including regular-to-direct switches of
  the same fund.
- **Estimating tax from the total gain.** The split between long and short
  lots is what determines it, and the two can point in opposite directions.

**Takeaway:** A SIP is as many separate investments as it has instalments,
each with its own purchase date, and redemptions consume the oldest units
first under FIFO. That's why one redemption can produce a long-term gain and
a short-term loss at once — and why the total gain tells you almost nothing
about the tax until you've split it by lot.
