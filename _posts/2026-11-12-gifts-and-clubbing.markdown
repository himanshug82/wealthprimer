---
layout: post
title: "Gifts and clubbing: why moving money to family rarely moves the tax"
description: "Gifts from relatives are tax-free, others above Rs 50,000 aren't. But income on money gifted to a spouse or minor child is still taxed in your hands."
image: /assets/og/gifts-and-clubbing.png
date: 2026-11-12 09:00:00 +0530
series: tax
term: "Clubbing of income"
---

{% assign t3 = site.data.tax3 %}
{% assign v = t3.verification %}
{% assign x = t3.gifts %}
{% assign r = site.data.tax.rates %}

*Rules described here apply to **{{ v.financial_year }}**, checked against the
text of the Income-tax Act, 2025 and the Finance Act, 2026 in {{ v.verified_on }}.
Educational content, not tax advice.*

## Two questions, two sets of rules

When money or investments move within a family, two separate tax questions
come up, and people tend to blur them:

1. **Is the gift itself taxed in the hands of the person receiving it?**
   Usually not, if it's from a relative.
2. **Once it's invested, whose income is the return?** Often not the
   recipient's. For a spouse or a minor child, the law **clubs** the income
   back into the giver's return.

The first question is about the gift. The second is about everything the
gift earns afterwards, and it's the one that decides whether spreading money
around the family changes anyone's tax.

## Gifts: tax-free from relatives, taxable above ₹{% include inr.html n=x.limit %} from others

Under section 92(2)(m) of the 2025 Act, if you receive money, or certain
property, **without paying for it**, and the total from non-relatives in the
tax year exceeds ₹{% include inr.html n=x.limit %}, the **whole amount** is taxed as your income at your
slab rate. "Property" here means shares and securities, jewellery, bullion,
land and buildings, art, and virtual digital assets, among others. Receive
them for well below their value and the shortfall is taxed on similar
terms.

The rule doesn't apply — whatever the amount — to gifts:

- **from a relative**;
- on the occasion of **your marriage**;
- under a **will or inheritance**, or in contemplation of the giver's death;
- and a few institutional cases (local authorities, registered charities).

"Relative" has a precise, closed list (section 92(5)(g)):

| Relative of an individual | Examples |
|---|---|
| Spouse | Husband, wife |
| Brother or sister | Your siblings |
| Brother or sister of your spouse | Brother-in-law, sister-in-law (spouse's side) |
| Brother or sister of either parent | Uncles and aunts |
| Any lineal ascendant or descendant — yours or your spouse's | Parents, grandparents, children, grandchildren, parents-in-law |
| The spouse of anyone above | Sister's husband, uncle's wife, son's wife |

Friends, cousins, and a nephew or niece giving to you are **not** on it.

**Worked example.** At a 30% slab plus {{ r.cess_pct }}% cess:

| Gift received in the year | Taxable | Tax with cess |
|---|---:|---:|
| ₹{% include inr.html n=x.limit %} from a friend | ₹0 | ₹0 |
| ₹{% include inr.html n=x.single %} from a friend | ₹{% include inr.html n=x.single %} — the whole amount | ₹{% include inr.html n=x.single_tax_with_cess %} |
| ₹{% include inr.html n=x.two_a %} + ₹{% include inr.html n=x.two_b %} from two friends | ₹{% include inr.html n=x.two_total %} — the total crosses ₹{% include inr.html n=x.limit %} | ₹{% include inr.html n=x.two_tax_with_cess %} |
| Any amount from a parent or sibling | ₹0 | ₹0 |

The ₹{% include inr.html n=x.limit %} is a cliff, not an allowance: one rupee over and the entire
sum is taxed. And it is counted across all non-relatives for the year, not
per giver.

**What the recipient inherits along with the gift.** Giving shares or fund
units away isn't a sale, so the giver owes no capital gains tax
(section 70(1)(b)). The recipient takes over the **giver's cost** and the
**giver's holding period** (sections 73 and 2(101)). When they eventually
sell, the gain is measured from what the giver originally paid.

## Clubbing: whose income is it?

Here's the rule that stops the obvious trick. Section 99 says your income
includes income that arises to:

- **your spouse**, from assets you transferred to them "otherwise than for
  adequate consideration" — that is, without being paid a fair price for
  them;
- **your son's wife**, from assets you transferred to her on the same terms;
- **your minor child** — *all* of the child's income, not only from what you
  gave, except income from the child's own work or skill, or where the child
  has a specified disability.

A gift to your spouse is tax-free when it's made. But the interest, dividends
and capital gains it earns come back into **your** return, at **your** slab.
A loss is clubbed too.

A minor child's income is added to the income of whichever parent earns more,
after excluding ₹{% include inr.html n=x.minor_exclusion %} per child a year (Schedule III of the 2025 Act).

**Not clubbed**: income on gifts to an **adult child**, to your parents, or to
siblings. They aren't in section 99. Gifts to them are tax-free when made
(they're relatives), and what the gift earns afterwards is theirs.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your mum's piggy bank is in the "big savings" jar, where the tax collector
takes a bigger slice of any interest. Your dad's is in the "small savings" jar, where
the slice is smaller. So mum thinks: I'll just move my coins into dad's jar.

The rule says: fine, you can move them — but any interest those coins earn
still counts as yours, and gets your slice taken. Same if mum moves coins
into *your* jar while you're a kid.

The trick only works once you're grown up. Then your jar really is your own.

</details>

## Worked example: three ways money moves in one family

At a 30% slab plus {{ r.cess_pct }}% cess, no surcharge.

**A spouse's fixed deposit.** Rahul gifts ₹{% include inr.html n=x.spouse_gift %} to his wife Priya.
She puts it in a {{ x.spouse_fd_pct }}% fixed deposit. The gift is tax-free (spouse is a
relative). The ₹{% include inr.html n=x.spouse_interest %} of interest is clubbed into Rahul's income:
₹{% include inr.html n=x.spouse_interest_tax_with_cess %} of tax, at his slab — exactly what it would have cost had he kept
the deposit himself.

**A minor child's deposit.** Interest of ₹{% include inr.html n=x.minor_interest %} on a deposit in a minor
child's name:

| | |
|---|---:|
| Child's interest | ₹{% include inr.html n=x.minor_interest %} |
| − Exclusion per child | ₹{% include inr.html n=x.minor_exclusion %} |
| Clubbed into the higher-earning parent's income | ₹{% include inr.html n=x.minor_clubbed %} |
| Tax at 30% + cess | ₹{% include inr.html n=x.minor_tax_with_cess %} |

**Fund units given to a spouse — real prices.** Rahul bought ₹{% include inr.html n=x.ls_invested %} of
UTI Nifty 50 Index Fund (regular plan, growth) on {{ x.ls_buy_date }} at a NAV of
₹{{ x.ls_buy_nav }}, and later gave the units to Priya. She redeems them on
{{ x.ls_sell_date }} at ₹{{ x.ls_sell_nav }} (NAVs from AMFI, as of 31 March 2026,
used for illustration only; we apply the rules for {{ v.financial_year }}). This is the
same holding as the
[equity post's lump sum]({% post_url 2026-10-29-equity-and-equity-funds %}).

- Cost and holding period are Rahul's: ₹{% include inr.html n=x.ls_invested %}, held since 2020 — so
  the gain of ₹{% include inr.html n=x.ls_gain %} is long-term.
- The gain arises from an asset Rahul transferred to his spouse for nothing,
  so it's **clubbed into Rahul's income**.

| Whose exemption absorbs the first ₹{% include inr.html n=r.ltcg_annual_exemption %}? | Tax with cess |
|---|---:|
| Rahul's, if still unused this year | ₹{% include inr.html n=x.ls_tax_own_exemption_with_cess %} |
| None — Rahul already used his on other gains | ₹{% include inr.html n=x.ls_tax_exemption_used_with_cess %} |

The gift didn't give the household a second ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption. Had Priya
bought the units with her own money, her exemption would have been available;
because the money was Rahul's, clubbing puts the gain back with him. If his
exemption was already used, that costs ₹{% include inr.html n=x.ls_clubbing_cost %}.

## What "adequate consideration" means, and the grey areas

The Act doesn't define **adequate consideration**. In ordinary reading it
means the spouse paid something close to what the asset was worth. A gift
fails that test by definition; so does a sale at a token price.

Two points are widely followed in practice but rest on court rulings, not on
the Act's text, so treat them as things to confirm:

- **Income on clubbed income.** If Priya reinvests the interest from Rahul's
  gift, the income *on that reinvested interest* is generally treated as her
  own.
- **Loans versus gifts.** A genuine, documented loan to a spouse at a fair
  interest rate is treated differently from a gift. How differently, and
  what counts as genuine, is a question for someone who files professionally.

## Common mistakes

- **Treating the ₹{% include inr.html n=x.limit %} as a free allowance.** Cross it and the *whole*
  amount from non-relatives is taxable, not just the excess.
- **Assuming cousins, friends or a nephew count as relatives.** They don't.
  The list is closed.
- **Investing in a spouse's or minor child's name to use their lower slab.**
  The income is clubbed back to you. It moves paperwork, not tax.
- **Forgetting to report clubbed income in your own return.** The AIS may
  show it against the spouse's or child's PAN (permanent account number);
  your return still has to include it.
- **Resetting the holding period on a gifted asset.** The recipient inherits
  the giver's purchase date and cost. That usually helps: it can turn a sale
  into a long-term one.

**Takeaway:** A gift from a relative isn't taxed; from anyone else, the
whole amount is taxed once the year's total passes ₹{% include inr.html n=x.limit %}. But whatever a
gift to your spouse or minor child earns is clubbed back into your return,
so moving money to them changes the paperwork, not the tax.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax3.yml)
lists the sections of the Income-tax Act, 2025 behind every rule here, and
the points a professional should confirm before you rely on them.*
