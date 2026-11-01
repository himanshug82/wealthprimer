---
layout: post
title: "Losses: set-off, carry-forward and how the annual exemption interacts"
seo_title: "Capital losses: set-off, carry-forward, harvesting"
description: "Which capital losses can be set off against which gains, the eight-year carry-forward window, and what harvesting losses and gains does and does not do."
image: /assets/og/losses-set-off-and-harvesting.png
date: 2026-11-07 09:00:00 +0530
series: tax
term: "Set-off, carry-forward and tax-loss harvesting"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "August 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}
{% assign l = t.example_loss %}

## What a loss does for tax

This post covers **Tax Year 2026-27 (FY 2026-27)**; FY is *financial year*. A capital loss can be set off against capital gains, in the
same year or in later years, and there are rules about what can offset what.

## The set-off rules

Two rules, and the asymmetry between them is the whole thing:

```
Short-term capital LOSS  ->  can be set off against
                             short-term gains AND long-term gains

Long-term capital LOSS   ->  can be set off against
                             long-term gains ONLY
```

Short-term losses are more flexible. Long-term losses are restricted to
long-term gains.

There's also a broader rule worth knowing: capital losses can only be set off
against capital gains. You cannot use a loss on shares to reduce your salary
or business income.

## Carry-forward, and the deadline that decides it

Whatever you can't use this year carries forward for **{{ r.carry_forward_years }} years**, retaining
its character — a long-term loss stays a long-term loss and remains
restricted to long-term gains.

There is one condition, and it is near-absolute:

> **You must file your return by the due date.** File late, and the
> carry-forward is lost permanently.

The Income-tax Act, 2025 ties carry-forward of losses to a return filed within
the due-date provision, so a return filed late can lose the carry-forward. Someone with a
loss and no gains this year might think there's nothing to report; the rule
is why the loss would still be reported. (The Central Board of Direct Taxes (CBDT) has a power, in section 239(3)(b) of the
Income-tax Act, 2025, to authorise a tax authority to admit a claim for relief after
its time limit to avoid genuine hardship. It is discretionary, and the text doesn't say
it covers a late loss return.) Check the current rule for your case.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you get a voucher every time something goes wrong, which you can use
against future bills.

There are two kinds. The blue voucher works on any bill. The red one only
works on one specific type of bill.

They're valid for eight years — but only if you **register them before the
deadline**. Forget to register and the voucher is just a piece of paper, no
matter how much it was worth.

Registering is filing your return on time. It takes an afternoon and it's the
only thing keeping the voucher alive.

</details>

## Worked example: a real loss

The fund [NAV]({% post_url 2026-09-25-what-a-mutual-fund-is %}) (net asset value, the per-unit price) history used throughout
this blog — UTI Nifty 50 Index Fund (regular plan, growth), NAVs from AMFI
(the Association of Mutual Funds in India), as of 31 March 2026, used for
illustration only — contains an actual loss. A ₹{% include inr.html n=l.monthly_amount %} monthly
[SIP]({% post_url 2026-10-01-sips-xirr-and-timing-myths %}) (systematic investment plan) started {{ l.start | date: "%-d %B %Y" }} and redeemed on {{ l.redemption_date | date: "%-d %B %Y" }} — {{ l.instalments }}
instalments, with the redemption date chosen as the last date in the data, for illustration:

| | |
|---|---:|
| Invested | ₹{% include inr.html n=l.invested %} |
| Value at redemption | ₹{% include inr.html n=l.value %} |
| **Total loss** | **₹{% include inr.html n=l.total_loss_abs %}** |
| of which long-term ({{ l.long_term_lots }} lots) | ₹{% include inr.html n=l.long_term_loss_abs %} |
| of which short-term ({{ l.short_term_lots }} lots) | ₹{% include inr.html n=l.short_term_loss_abs %} |

Note that one redemption produced *both* kinds of loss, because the earlier
instalments had crossed the twelve-month line and the later ones hadn't.
That's the FIFO point arriving early.

Now what can be done with each:

- The **short-term loss of ₹{% include inr.html n=l.short_term_loss_abs %}** can be set against any capital gain —
  short-term or long-term — in this year or the next {{ r.carry_forward_years }}.
- The **long-term loss of ₹{% include inr.html n=l.long_term_loss_abs %}** can only be set against long-term gains.

If this investor had, say, a ₹2,00,000 long-term gain elsewhere in the same
year, both losses could be applied against it, reducing the taxable long-term
gain to ₹{% assign lt_left = 200000 | minus: l.total_loss_abs %}{% include inr.html n=lt_left %} before the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption — which would then take it
down to ₹{% assign lt_tax = lt_left | minus: r.ltcg_annual_exemption %}{% include inr.html n=lt_tax %}.

## Harvesting, described

**Harvesting losses** means realising a loss on something that's
down, so it can be set off against gains, and then holding a similar exposure
again. A loss can only be set off if there are gains for it to offset, now or
within eight years, and selling and rebuying involves transaction costs and a
period out of the market.

India's rules have no wash-sale provision that this post found. The general
anti-avoidance rule (GAAR) exists in Chapter XI of the Income-tax Act, 2025,
covering arrangements whose main purpose is a tax benefit. Whether and when it
could apply to a sale and repurchase is not covered here; check the current rule.

**Harvesting gains** is the mirror image. Recall from the
[equity post]({% post_url 2026-11-04-equity-and-equity-funds %}) that the first
₹{% include inr.html n=r.ltcg_annual_exemption %} of long-term gains each financial year is exempt, and that the
allowance does not carry forward: unused, it expires on 31 March. Selling and
repurchasing a holding realises the gain, so that year's exempt amount applies
to it, and the repurchase gives the new units a new acquisition date and a
higher cost. The new units' holding period starts again, so a later sale within
twelve months would be short-term. The sale and the repurchase also carry transaction
costs. This is a description of the mechanics; whether it suits a particular
portfolio is outside this blog's scope.

## Common mistakes

- **Not filing on time when you have a loss.** The carry-forward is tied to a return filed by the due date; a late return can lose it.
- **Expecting to hold a loss back for a later year.** Set-off in the same year
  generally comes first, before the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption is applied; check the current rule.
- **Expecting a long-term loss to offset a short-term gain.** It can't. The
  restriction runs one way only.
- **Trying to offset salary income with capital losses.** Not permitted.

## Sources

- [Income-tax Act, 2025 (a copy hosted by ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself.
- [Finance Act, 2026, Gazette of India](https://egazette.gov.in/WriteReadData/2026/271439.pdf): the Finance Act that made the 2026 changes.
- [Memorandum explaining the provisions of the Finance Bill, 2026](https://www.indiabudget.gov.in/doc/memo.pdf): the government's explanation of those changes.

**Takeaway:** Short-term capital losses can be set off against any capital gain, long-term losses only against long-term gains, and what is unused carries forward {{ r.carry_forward_years }} years if the return is filed on time. The ₹{% include inr.html n=r.ltcg_annual_exemption %} annual long-term exemption expires each 31 March.
