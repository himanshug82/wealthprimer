---
layout: post
title: "Advance tax for investors: pay as you earn, gains included"
description: "If TDS doesn't cover your tax, you pay it in four instalments during the year. Capital gains get a special rule — and missing it costs interest. Worked example."
image: /assets/og/advance-tax-for-investors.png
date: 2026-11-11 09:00:00 +0530
series: tax
term: "Advance tax"
---

{% assign t3 = site.data.tax3 %}
{% assign v = t3.verification %}
{% assign x = t3.advance %}
{% assign r = site.data.tax.rates %}

*Rules described here apply to **{{ v.financial_year }}**, checked against the
text of the Income-tax Act, 2025 and the Finance Act, 2026 in {{ v.verified_on }}.
Educational content, not tax advice.*

## Tax is due during the year, not when you file

Most salaried people never think about this, because their employer deducts
tax from every pay slip. But the law's default is that you pay tax **during**
the year in which you earn the income, not months later when you file. For
tax nobody deducts for you — on capital gains, and the part of the tax on
dividends and interest that a 10% TDS doesn't cover — that means paying it
yourself, in instalments.
That's **advance tax**.

Investors are the classic case. A salaried person who redeems a large fund
holding in August has a capital gain with no TDS on it at all (for a resident,
[funds don't deduct tax on redemptions]({% post_url 2026-10-27-how-investment-income-is-taxed %})).
The tax on that gain was due during the year. Pay it only at filing and you
pay interest on top.

## Who has to pay

Under the Income-tax Act, 2025:

- **Anyone whose tax for the year, after TDS and TCS, is ₹{% include inr.html n=x.threshold %} or more**
  (sections 404 and 405). The TDS your employer, bank or broker deducts is
  subtracted first; what's left is what advance tax is about.
- **Except** resident individuals aged **60 or more** with no business or
  professional income (section 403(3)). They can pay it all when they file.
- F&O traders count as having business income, as the
  [F&O post]({% post_url 2026-11-07-fo-is-business-income %}) explained, so the senior-citizen
  exemption doesn't help them.

## The four instalments

| Pay by | Cumulative share of the year's advance tax |
|---|---:|
{% for s in x.schedule %}| {{ s.date | split: " " | slice: 0, 2 | join: " " }} | {% if s.pct < 100 %}at least {% endif %}{{ s.pct }}% |
{% endfor %}

That's section 408. Two extra details: anything paid by 31 March still counts
as advance tax for that year, and taxpayers on the presumptive business
scheme pay the whole amount by 15 March in one go.

## What it costs to be late

Two separate interest charges, both simple interest. The old Act called them
234C and 234B; in the 2025 Act they are sections 425 and 424.

```
Section 425 (deferment — "missed an instalment"):
  At 15 June, 15 Sept, 15 Dec:  3% × shortfall against 15% / 45% / 75%
  At 15 March:                  1% × shortfall against 100%
  No interest if you paid ≥ 12% by 15 June and ≥ 36% by 15 Sept.

Section 424 (default — "paid too little overall"):
  If advance tax paid < 90% of the tax finally assessed:
  1% per month (or part of a month) on the shortfall,
  from 1 April after the year, until you pay.
```

The 3% at each of the first three dates is three months of 1%, covering the
gap until the next instalment. Both charges are computed on the tax **after**
TDS.

## Why capital gains get special treatment

The instalment schedule assumes income arrives evenly. A capital gain doesn't:
you can't pay 15% of the tax on an August sale by 15 June. So section 425(4)
carves it out:

> No interest for a shortfall caused by **capital gains**, **dividends**,
> lottery-type winnings, or the first year's business income — **provided**
> the tax on that income is paid in full in the remaining instalments, or by
> 31 March.

That proviso is the whole game. Pay the gain's tax in the next instalment
after the sale and the earlier shortfall is forgiven. Don't, and the
exception doesn't apply at all: the shortfall is measured against the
full-year tax, including the gain, right back to 15 June.

The carve-out is from section 425 only. Section 424's 90% test looks at the
year as a whole, so the gain's tax still has to be paid by 31 March to avoid
it.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your parents let you pay for the school trip in four parts: a little in June,
more in September, more in December, and the rest in March. If you're late
with a part, you pay a small late fee.

Then in August your grandmother gives you a big gift of pocket money, and
the trip rule says a share of *that* must go toward the trip too. It wouldn't
be fair to charge you a late fee for June — you didn't have the money in
June. So the rule is: put it in with your next payment, and there's no late
fee for the earlier months. Forget until the trip itself, and you pay late
fees for all of them.

</details>

## Worked example: one gain, three ways to pay

A hypothetical salaried investor, {{ v.financial_year }}:

| | |
|---|---:|
| Salary (employer's TDS covers its tax exactly) | ₹{% include inr.html n=x.salary %} |
| Fixed deposit interest (bank deducts 10%: ₹{% include inr.html n=x.fd_tds %}) | ₹{% include inr.html n=x.fd_interest %} |
| Long-term gain on an equity fund, sold on {{ x.ltcg_date }} | ₹{% include inr.html n=x.ltcg %} |

Total income is ₹{% include inr.html n=x.total_income %}, under ₹50 lakh, so no surcharge; the salary
alone puts the interest in the 30% slab. Tax beyond the TDS already deducted:

| | Tax with {{ r.cess_pct }}% cess |
|---|---:|
| Interest: 30% on ₹{% include inr.html n=x.fd_interest %} | ₹{% include inr.html n=x.interest_tax_with_cess %} |
| − TDS already deducted | −₹{% include inr.html n=x.fd_tds %} |
| Gain: {{ r.equity_ltcg_pct }}% on ₹{% include inr.html n=x.ltcg_taxable %} (after the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption) | ₹{% include inr.html n=x.ltcg_tax_with_cess %} |
| **Advance tax for the year** | **₹{% include inr.html n=x.advance_tax_total %}** |

Well above ₹{% include inr.html n=x.threshold %}, so advance tax applies.

### A: pays on schedule, gain added after it arises

The interest is regular income, so its tax (₹{% include inr.html n=x.interest_tax_net_of_tds %}) goes on the
15/45/75/100% schedule. The gain's tax goes into the first instalment after
the sale, 15 September.

| Date | Required (cumulative, whole year) | Paid (cumulative) | This instalment |
|---|---:|---:|---:|
{% for s in x.schedule %}| {{ s.date }} | ₹{% include inr.html n=s.required_cum %} | ₹{% include inr.html n=s.paid_a_cum %} | ₹{% include inr.html n=s.instalment_a %} |
{% endfor %}

On 15 June the investor is ₹{% include inr.html n=x.june_shortfall_a %} short of 15% of the year's tax. That
shortfall is entirely due to a gain that didn't exist yet, and its tax was
paid in the next instalment, so section 425(4) forgives it. **Interest: ₹0.**

### B: pays nothing until filing on 31 July 2027

| Date | Shortfall | Rate | Interest (section 425) |
|---|---:|---:|---:|
{% for s in x.schedule %}| {{ s.date }} | ₹{% include inr.html n=s.required_cum %} | {{ s.rate_425_pct }}% | ₹{% include inr.html n=s.b_interest %} |
{% endfor %}| **Total** | | | **₹{% include inr.html n=x.b_425_total %}** |

Plus section 424: nothing was paid, so interest runs on the whole
₹{% include inr.html n=x.advance_tax_total %} at 1% a month for {{ x.months_424 }} months (April to July 2027):
₹{% include inr.html n=x.b_424 %}. **Total interest: ₹{% include inr.html n=x.b_total %}.**

### C: pays the interest's tax on schedule, forgets the gain

This is the pattern that loses the capital-gains relief. The regular schedule is met, but the
₹{% include inr.html n=x.ltcg_tax_with_cess %} on the gain waits until filing. Because the gain's tax wasn't
paid by 31 March, the capital-gains exception falls away, and every date is
measured against the full-year figure:

| Date | Required | Paid | Shortfall | Interest (section 425) |
|---|---:|---:|---:|---:|
{% for s in x.schedule %}| {{ s.date }} | ₹{% include inr.html n=s.required_cum %} | ₹{% include inr.html n=s.regular_cum %} | ₹{% include inr.html n=s.c_shortfall %} | ₹{% include inr.html n=s.c_interest %} |
{% endfor %}| **Total** | | | | **₹{% include inr.html n=x.c_425_total %}** |

Paid by 31 March: ₹{% include inr.html n=x.interest_tax_net_of_tds %}, below 90% of the year's tax
(₹{% include inr.html n=x.ninety_pct %}). So section 424 also applies, on the unpaid
₹{% include inr.html n=x.c_424_base %} for {{ x.months_424 }} months: ₹{% include inr.html n=x.c_424 %}. **Total interest:
₹{% include inr.html n=x.c_total %}** — for forgetting one payment.

These figures ignore the rounding the rules apply to the amounts before
computing interest, so the portal's numbers can differ by a few rupees.

## Common mistakes

- **Assuming TDS means you're done.** TDS on interest and dividends is 10%.
  In a higher slab the rest is due during the year, through advance tax.
- **Waiting until filing to pay tax on a big redemption.** Residents get no
  TDS on fund redemptions. The tax on a gain belongs in the first instalment
  after the sale.
- **Reading the capital-gains relief as "gains are exempt from advance tax".**
  They aren't. The relief only forgives the *earlier* instalments, and only
  if you pay in the ones that remain, or by 31 March.
- **Forgetting that 31 March counts.** A gain realised after 15 March still
  avoids interest if its tax is paid by 31 March.
- **Senior citizens with a small trading habit assuming the 60+ exemption.**
  It's lost if there's any business income, and F&O trading is business
  income.

**Takeaway:** Tax on investment income is due during the year, in four
instalments by 15 June, September, December and March. A capital gain's tax
only has to join the instalments left after the sale — but skip that and
interest runs as if you'd known about the gain in June.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax3.yml)
lists the sections of the Income-tax Act, 2025 behind every rule here, and
the points a professional should confirm before you rely on them.*
