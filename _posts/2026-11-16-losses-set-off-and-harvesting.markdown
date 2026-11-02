---
layout: post
title: "Losses: set-off, carry-forward and how the annual exemption interacts"
seo_title: "Capital losses: set-off, carry-forward, harvesting"
description: "Which capital losses can be set off against which gains, the eight-year carry-forward window, and what harvesting losses and gains does and does not do."
image: /assets/og/losses-set-off-and-harvesting.png
date: 2026-11-16 09:00:00 +0530
series: tax
term: "Set-off, carry-forward and tax-loss harvesting"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}
{% assign l = t.example_loss %}

## What a loss does for tax, Tax Year 2026-27

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

There is one condition that matters:

> **The return has to be filed by the due date.** A late return can lose the
> carry-forward.

Section 121 of the Income-tax Act, 2025 ties carry-forward of a capital loss to a return filed under section 263(1), so a return filed late can lose it. A loss with no gains this year would still need to be reported in time to be carried forward. (Section 121 doesn't list house-property losses, so this is about capital and business losses.) Whether the Central Board of Direct Taxes (CBDT) can admit a late claim to avoid genuine hardship is not covered here, so check the current rule for your case.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you get a voucher every time something goes wrong, which you can use
against future bills.

There are two kinds. The blue voucher works on any bill. The red one only
works on one specific type of bill.

They're valid for eight years — but only if you **register them before the
deadline**. Forget to register and the voucher may stop counting.

Registering is filing your return on time. That's what keeps the voucher valid.

</details>

## Worked example: a real loss

The fund [NAV]({% post_url 2026-09-25-what-a-mutual-fund-is %}) (net asset value, the per-unit price) history used throughout
this blog — UTI Nifty 50 Index Fund (regular plan, growth), NAVs from AMFI
(the Association of Mutual Funds in India), as of 31 March 2026, used for
illustration only — contains an actual loss. A ₹{% include inr.html n=l.monthly_amount %} monthly
[SIP]({% post_url 2026-10-01-sips-xirr-and-timing-myths %}) (systematic investment plan) started {{ l.start | date: "%-d %B %Y" }} and redeemed on {{ l.redemption_date | date: "%-d %B %Y" }} — {{ l.instalments }}
instalments, with the redemption date chosen as the last date in the data, for illustration. Each instalment
buys at {{ t.example_sip.nav_rule }}. A real SIP that falls on a holiday is typically allotted at the next
business day's NAV, which would make the loss ₹{% include inr.html n=l.next_business_day_loss_abs %}. The figures below use the first rule:

| | |
|---|---:|
| Invested | ₹{% include inr.html n=l.invested %} |
| Value at redemption | ₹{% include inr.html n=l.value %} |
| **Total loss** | **₹{% include inr.html n=l.total_loss_abs %}** |
| of which long-term ({{ l.long_term_lots }} lots) | ₹{% include inr.html n=l.long_term_loss_abs %} |
| of which short-term ({{ l.short_term_lots }} lots) | ₹{% include inr.html n=l.short_term_loss_abs %} |

Note that one redemption produced *both* kinds of loss, because the earlier
instalments had crossed the twelve-month line and the later ones hadn't.
That's the FIFO (first in, first out) point arriving early.

Now what can be done with each:

- The **short-term loss of ₹{% include inr.html n=l.short_term_loss_abs %}** can be set against any capital gain —
  short-term or long-term — in this year or, as we read the rule, the next {{ r.carry_forward_years }}.
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

India's rules have no wash-sale provision that this post found. A general
anti-avoidance rule (GAAR, Chapter XI of the Act) also exists, covering arrangements whose main purpose is a tax benefit. Whether and when it
could apply to a sale and repurchase is a question of facts, and this post doesn't answer it. This section describes the mechanism and is not a suggestion to do either.

**Harvesting gains** is the mirror image: selling and repurchasing realises the gain, gives the new units a new acquisition date and cost (which restarts the holding period), and carries transaction costs on both legs, while the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption from the [equity post]({% post_url 2026-11-08-equity-and-equity-funds %}) does not carry forward.

## Common mistakes

- **Not filing on time when you have a loss.** As described above, the carry-forward is tied to a return filed by the due date, and a late return can lose it.
- **Expecting to choose when a loss is used.** Section 108 says a loss "shall be set off" against the same year's gains, so it isn't optional, and it comes before the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption is applied.
- **Expecting a long-term loss to offset a short-term gain.** It can't. The
  restriction runs one way only.
- **Trying to offset salary income with capital losses.** Section 109(2) doesn't allow a capital loss to be set off against any other head of income.

## Sources

- [Income-tax Act, 2025 (a copy hosted by the Institute of Chartered Accountants of India, ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself, as read in that copy. Points not found there are marked "check the current rule".
- [Finance Act, 2026 (No. 4 of 2026)](https://egazette.gov.in/WriteReadData/2026/271439.pdf), Gazette of India, 30 March 2026: opened 2 November 2026 for the amendments and the rates for Tax Year 2026-27.

**Takeaway:** Short-term capital losses can be set off against any capital gain, long-term losses only against long-term gains, and what is unused carries forward {{ r.carry_forward_years }} years, generally only if the return is filed on time (check the current rule). The ₹{% include inr.html n=r.ltcg_annual_exemption %} annual long-term exemption expires each 31 March.
