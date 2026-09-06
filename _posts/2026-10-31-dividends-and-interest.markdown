---
layout: post
title: "Dividends and interest: taxed at your slab, with TDS on top"
description: "Both are simply added to your income and taxed at your slab rate. What changed when the dividend distribution tax went, and how TDS arrives before you file."
image: /assets/og/dividends-and-interest.png
date: 2026-10-31 09:00:00 +0530
series: tax
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

*Rules described here apply to **{{ r.financial_year }}**. Educational content, not tax
advice.*

## The simple bucket, with one sharp edge

After four posts on capital gains, dividends and interest come as a relief:
both are simply **added to your total income and taxed at whatever slab rate
you fall into**. No holding periods, no special rates, no annual exemption.

The sharp edge is that this used to be very different, and a lot of what
people believe about dividends dates from before it changed.

## Dividends are no longer tax-free in your hands

Until 2020, companies paid a Dividend Distribution Tax and dividends arrived
tax-free for the investor. That system was abolished: **dividends are now
taxed in the recipient's hands at their slab rate.**

The practical effect depends entirely on your slab, and it's large:

| Your slab | Tax on ₹1,00,000 of dividend |
|---|---:|
| 5% | ₹5,000 |
| 20% | ₹20,000 |
| 30% | ₹30,000 |

Compare that with long-term capital gains on equity at {{ r.equity_ltcg_pct }}% with a
₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption, and something important follows: for an investor
in the highest slab, **dividend income is taxed more heavily than long-term
capital gains on the same shares**.

This is the reasoning behind a point made back in the
[opening mutual funds post]({% post_url 2026-10-18-what-a-mutual-fund-is %}): choosing the IDCW option over
growth doesn't create extra income. It converts what would have been a
capital gain — taxed at {{ r.equity_ltcg_pct }}% with an exemption, and only when you choose to
sell — into income taxed at your slab rate, now, whether you wanted it or
not.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine two ways of getting pocket money.

**Way one:** your savings jar just grows, and you only count it when you
decide to spend some. You're taxed a little, on the bit you take, when you
take it.

**Way two:** every month someone takes coins out of your jar and hands them
to you — and you're taxed on those coins straight away, at a higher rate,
even if you put them right back.

Your jar has the same money in both cases. The second way just costs more and
gives you less say about when.

</details>

## TDS: tax deducted before it reaches you

Unlike capital gains, dividends and interest usually arrive with tax already
withheld. **TDS — Tax Deducted at Source** — means the payer deducts a slice
and deposits it against your PAN before paying you the rest.

| Income | Typically deducted at |
|---|---|
| Dividends from shares and mutual funds | 10%, above a threshold per payer per year |
| Bank fixed deposit interest | 10%, above a threshold |
| Interest on most bonds | 10% |

Two things matter more than the exact thresholds, which move with each
Budget.

**TDS is not your final tax.** It's an advance. If you're in the 30% slab,
10% withheld leaves you owing the balance when you file. If you're below the
taxable limit, you claim it back as a refund. Either way, the deduction is
not the end of the story — and treating it as though it were is how people
end up with unexpected demands.

**No PAN means a much higher rate.** Where PAN isn't provided, deduction runs
at a considerably higher rate. Worth checking on old accounts and inherited
holdings.

## Interest

Same treatment, added to income at your slab rate. Some specifics worth
knowing:

- **Savings account interest** attracts a modest deduction for individuals,
  which the interest on most ordinary balances falls within.
- **Fixed deposit interest is taxable as it accrues each year**, not when the
  deposit matures. People with multi-year cumulative deposits routinely miss
  this and then face several years' tax at once.
- **Public Provident Fund interest is exempt.** So is interest on some other
  specified small-savings instruments.
- **Employees' Provident Fund** is exempt within limits, with interest on
  contributions above a specified annual threshold becoming taxable.

That fixed-deposit accrual point is the one that catches most people. The
bank may not deduct anything until maturity, but the tax was due year by
year.

## Form 26AS and the AIS

Everything deducted against your PAN shows up in two places: **Form 26AS**
(the tax credit statement) and the **Annual Information Statement (AIS)**,
which is broader and includes reported dividends, interest and securities
transactions.

Checking these before filing is the single most useful habit in this entire
series, for a blunt reason: the tax department already has this data. A
mismatch between what you report and what's in your AIS is what generates
notices. The last post in this series covers reading them properly.

## Common mistakes

- **Believing dividends are still tax-free.** They've been taxed in the
  recipient's hands since 2020.
- **Choosing IDCW for "income".** It converts a lightly-taxed, deferrable
  capital gain into slab-rate income received now.
- **Treating TDS as the final tax.** It's an advance against a liability that
  may be larger or smaller.
- **Missing accrued fixed-deposit interest.** Taxable each year, even on a
  cumulative deposit that pays nothing until maturity.
- **Not checking the AIS before filing.** The department already has the
  data; mismatches are what get flagged.
- **Assuming small dividends escape tax.** Below the TDS threshold means
  nothing was *deducted*, not that nothing is *taxable*.

**Takeaway:** Dividends and interest are simply added to your income and
taxed at your slab rate — which, for anyone in the top slab, is a heavier
charge than long-term capital gains on the same shares. TDS deducted along
the way is an advance, not a settlement, and the AIS already shows the tax
department what you received.
