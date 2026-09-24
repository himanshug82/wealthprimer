---
layout: post
title: "Losses: set-off, carry-forward, and the ₹1.25 lakh you can use each year"
description: "A capital loss is an asset for tax purposes. Which losses offset which gains, the carry-forward window, and how harvesting works against the annual exemption."
image: /assets/og/losses-set-off-and-harvesting.png
date: 2026-11-01 09:00:00 +0530
series: tax
term: "Set-off, carry-forward and tax-loss harvesting"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}
{% assign l = t.example_loss %}

*Rules described here apply to **{{ r.financial_year }}**. Educational content, not tax
advice.*

## Losses are worth something, if you claim them

A capital loss isn't only a bad outcome — it's an asset for tax purposes. It
can reduce gains you'd otherwise pay tax on, this year or for years
afterwards. But only if you claim it properly, and there are rules about what
can offset what.

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

There is one condition, and it is absolute:

> **You must file your return by the due date.** File late, and the
> carry-forward is lost permanently.

This deserves emphasis because it's the most avoidable expensive mistake in
this series. Someone with a large loss and no gains this year might reasonably
think there's nothing to report. But filing on time is precisely what
preserves the loss for the eight years in which it might be worth a great
deal. A return filed late doesn't just delay the benefit — it destroys it.

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

The fund NAV (net asset value, the per-unit price) history used throughout
this blog — UTI Nifty 50 Index Fund (regular plan, growth), NAVs from AMFI
(the Association of Mutual Funds in India), as of 31 March 2026, used for
illustration only — contains an actual loss. A ₹{% include inr.html n=l.monthly_amount %} monthly
[SIP]({% post_url 2026-10-24-sips-xirr-and-timing-myths %}) (systematic investment plan) started {{ l.start }} and redeemed on {{ l.redemption_date }} — {{ l.instalments }}
instalments through the Q1 2026 decline:

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

- The **short-term loss of ₹12,529** can be set against any capital gain —
  short-term or long-term — in this year or the next {{ r.carry_forward_years }}.
- The **long-term loss of ₹5,763** can only be set against long-term gains.

If this investor had, say, a ₹2,00,000 long-term gain elsewhere in the same
year, both losses could be applied against it, reducing the taxable long-term
gain to ₹1,81,708 before the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption — which would then take it
down to ₹56,708.

## Tax-loss harvesting, and its more useful sibling

**Harvesting losses** means deliberately realising a loss on something that's
down, to offset gains realised elsewhere, and then reinvesting. The loss
becomes usable; the exposure continues.

Two cautions. There's no benefit unless you have gains for it to offset,
either now or plausibly within eight years. And selling and immediately
rebuying incurs real transaction costs, plus a day or two out of the market —
so the tax saving needs to exceed the friction.

**Harvesting gains is the more interesting idea**, and it's specific to
Indian equity taxation. Recall from the
[equity post]({% post_url 2026-10-29-equity-and-equity-funds %}) that the first
₹{% include inr.html n=r.ltcg_annual_exemption %} of long-term gains each financial year is exempt, and that the
allowance does not carry forward. Unused, it expires on 31 March.

So an investor with a large unrealised long-term gain can realise roughly
₹{% include inr.html n=r.ltcg_annual_exemption %} of it each year, pay nothing, and immediately reinvest — which resets
the cost base upward. Do that annually and a gain that would eventually be
taxed in one large lump is instead drawn down in exempt slices.

The arithmetic is genuinely favourable. It's also genuinely fiddly: you need
gains of the right size and vintage, you pay transaction costs each time, and
you're out of the market briefly. Whether it's worth the annual effort depends
on the sums involved, and on many portfolios it simply isn't.

## Common mistakes

- **Not filing on time when you have a loss.** The most expensive avoidable
  error here. Late filing destroys the carry-forward entirely.
- **Trying to save a loss for a better year.** Same-year set-off isn't
  optional. If you have gains this year, a loss is set against them first,
  before the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption is applied, even where the exemption
  would have covered those gains anyway. Only what's left carries forward.
- **Expecting a long-term loss to offset a short-term gain.** It can't. The
  restriction runs one way only.
- **Trying to offset salary income with capital losses.** Not permitted.
- **Harvesting losses with no gains to use them against.** You've paid costs
  for a benefit that may never arrive.
- **Letting the annual exemption lapse without noticing.** ₹{% include inr.html n=r.ltcg_annual_exemption %} of
  tax-free long-term gain, expiring every 31 March.
- **Forgetting the carried-forward loss when you finally have gains.** It
  needs to be tracked across years and reported each year to stay alive.

**Takeaway:** A capital loss is worth real money — short-term losses offset
any capital gain, long-term losses only offset long-term gains, and whatever
is unused carries forward eight years *provided you file on time*. On the
other side, the ₹{% include inr.html n=r.ltcg_annual_exemption %} annual long-term exemption expires unused each 31
March, which is the one genuinely free thing in Indian equity taxation.
