---
layout: post
title: "SIPs and FIFO: one redemption, sixty tax lots"
description: "One redemption, sixty tax lots. Why each SIP instalment is a separate purchase with its own holding-period clock, and how FIFO picks which units go first."
image: /assets/og/sips-and-fifo.png
date: 2026-11-08 09:00:00 +0530
series: tax
term: "FIFO (tax lots)"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}
{% assign s = t.example_sip %}

*Tax Year 2026-27 (FY 2026-27) is the label for the rules below. The worked example redeems on 31 March 2026, which falls in FY 2025-26, so it illustrates the mechanics rather than a Tax Year 2026-27 return; the rates and exemption it uses are the ones shown in the table.*

## A SIP is not one investment

A [SIP]({% post_url 2026-10-01-sips-xirr-and-timing-myths %}) — systematic investment plan, a fixed sum
invested every month — feels like one. One instruction, one fund, one folio,
one line on your statement. For tax, it is nothing of the sort.

**Every instalment is a separate acquisition**, with its own date, its own
cost, and its own holding-period clock. A five-year monthly SIP isn't one
investment held five years — it's sixty investments, the oldest held five
years and the newest held a month.

That single fact drives everything else in this post.

## FIFO: which units leave first

When you redeem part of a holding, which units did you sell? You didn't
specify, and it matters enormously, because different lots have different
costs and different holding periods.

The answer in practice is **FIFO — first in, first out**. The units you
bought earliest are treated as the units sold first. For shares and units held
in demat (electronic) form, FIFO is written into the Income-tax Act, 2025 itself
(the provision on determining the cost and holding period of securities held in
a depository). For mutual fund units held in a folio statement
rather than demat, the registrars apply FIFO as standard practice — and it's
what your capital gains statement will use. Check the current rule if your
holding is in an unusual form.

```
Redeem  ->  oldest units go first
        ->  their cost and their purchase date determine the gain
```

FIFO tends to put the oldest units first, and the oldest units are the ones most
likely to have crossed the twelve-month line and qualify for the long-term
rate. Whether that helps depends on the market path: if the oldest units sit on a
loss, the first units out carry that loss. FIFO also means your remaining holding is
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

A ₹{% include inr.html n=s.monthly_amount %} monthly SIP into the fund used throughout this blog — UTI
Nifty 50 Index Fund (regular plan, growth), [NAVs]({% post_url 2026-09-25-what-a-mutual-fund-is %}) (net asset values, the
per-unit prices) from AMFI (the Association of Mutual Funds in India), as of
31 March 2026, used for illustration only — running from
{{ s.start | date: "%-d %B %Y" }} to {{ s.last_instalment | date: "%-d %B %Y" }}, redeemed in full on {{ s.redemption_date | date: "%-d %B %Y" }}:

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
short-term *loss* simultaneously. That can happen whenever the recent
instalments are priced above the redemption NAV; the table above shows it in this
example.

## And the tax comes to nothing

Work it through:

- The short-term result is a loss of ₹{% include inr.html n=s.short_term_loss_abs %}, so there's no short-term tax.
- That loss can't wait for a better year. Under the
  [set-off rules]({% post_url 2026-11-07-losses-set-off-and-harvesting %}), a short-term loss is first set
  off against the same year's gains — short-term, then long-term — and only
  what's left over carries forward. There are no short-term gains here, so it
  comes off the long-term gain: ₹{% include inr.html n=s.long_term_gain %} − ₹{% include inr.html n=s.short_term_loss_abs %} = ₹{% include inr.html n=s.total_gain %}.
- That ₹{% include inr.html n=s.total_gain %} is below the ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption, so no tax
  is due on it.

**Total tax on a ₹{% include inr.html n=s.total_gain %} gain: zero.** But notice what happened to the
loss: it's used up, and nothing carries forward. The long-term gain was
already under the exemption, so absorbing the loss saved no tax at all. A short-term
loss in a year with no gains to absorb it would instead carry forward, so the same
lots can be taxed differently depending on what else lands in the same year.

The zero is real, and it’s worth being careful about what it does and
doesn't show. It isn't clever planning — nobody arranged it. It's the
arithmetic of a moderate gain meeting a generous annual exemption. A larger
SIP, or a stronger final year, and there would have been tax to pay. The
lesson isn't "SIPs are tax-free"; it's that you cannot know your tax from the
headline gain without splitting it by lot.

## What follows practically

**The exemption is per financial year.** The ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption applies to the long-term gains
of one financial year; it does not carry over to the next.

**Stopping a SIP doesn't start any clock.** Holding periods run from each
instalment's own purchase date, regardless of whether you're still investing.

**Switching between funds is a redemption.** A switch — even within the same
fund house — is generally treated as a sale of one scheme and a purchase of another, and so as a
taxable event; no rule text for this was opened for this post, so check the current rule. The same generally applies to moving from regular to direct plans of the same fund
(see the [expense ratio post]({% post_url 2026-09-28-expense-ratios-direct-vs-regular %})): the switch itself may be a taxable event, separate from the ongoing cost difference.

**Dividend reinvestment creates new lots.** Each reinvested payout is a fresh
purchase with a fresh date and its own clock.

## Common mistakes

- **Treating a SIP as one investment with one holding period.** Each
  instalment stands alone.
- **Assuming a long-running SIP is all long-term.** The most recent twelve
  months of instalments never are.
- **Expecting to choose which units you sell.** FIFO decides, not you.
- **Estimating tax from the total gain.** The split between long and short
  lots is what determines it, and the two can point in opposite directions.
  A switch is also a sale, including a regular-to-direct switch of the same fund.

## Sources

- [Income-tax Act, 2025 (a copy hosted by ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself.
- [Finance Act, 2026, Gazette of India](https://egazette.gov.in/WriteReadData/2026/271439.pdf): the Finance Act that made the 2026 changes.
- [Memorandum explaining the provisions of the Finance Bill, 2026](https://www.indiabudget.gov.in/doc/memo.pdf): the government's explanation of those changes.

**Takeaway:** A SIP is as many separate investments as it has instalments,
each with its own purchase date, and redemptions consume the oldest units
first under FIFO. That's why one redemption can produce a long-term gain and
a short-term loss at once — and why the total gain tells you almost nothing
about the tax until you've split it by lot.
