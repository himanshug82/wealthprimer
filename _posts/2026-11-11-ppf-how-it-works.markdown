---
layout: post
title: "PPF: how the rate, lock-in and limits work"
description: "The Public Provident Fund runs on a government-set rate, a 15-year term and a yearly deposit cap. How interest is counted, with a worked 15-year example."
image: /assets/og/ppf-how-it-works.png
date: 2026-11-11 09:00:00 +0530
series: money-before-markets
term: "PPF (Public Provident Fund)"
---

{% assign m = site.data.mbm %}
{% assign p = m.ppf %}
{% assign sc = p.scheme %}
{% assign ex = p.example %}
{% assign lw = ex.loan_wd %}

## What the PPF is

The **Public Provident Fund (PPF)** is a government savings scheme. You open an account, deposit up to a yearly limit, and the government pays interest at a rate it sets. The account matures 15 years after the end of the financial year in which it was opened.

The rules come from the [Public Provident Fund Scheme, 2019]({{ sc.url }}) ({{ sc.gsr }}, notified {{ sc.date | date: "%-d %B %Y" }}). **Rule text:** the notification as of {{ sc.date | date: "%-d %B %Y" }}, when it was published. Amendments since then were not checked, so confirm the current text before relying on a detail. **Rate:** NSI's table, read on 25 October 2026, plus the Ministry of Finance memorandum for the October to December quarter. This post is part of [Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}). Tax treatment isn't covered here.

## What the scheme text says

| Item | Rule in the notification |
|---|---|
| Deposit per year | At least ₹{% include inr.html n=sc.min_deposit %} and at most ₹{% include inr.html n=sc.max_deposit %}, in multiples of ₹{{ sc.multiple }} (paragraph 4). The cap covers your own account plus any account you hold for a minor |
| Interest | On the lowest balance between the close of the fifth day and the end of each month; credited at the end of the year (paragraph 7) |
| Maturity | After the expiry of {{ sc.maturity_years }} years from the end of the financial year of opening (paragraph 11); can be extended in blocks of {{ sc.extension_block_years }} years (paragraph 12). The option to extend with deposits must be exercised within one year of maturity; the account can also simply continue without further deposits and keep earning the prevailing rate (paragraph 11) |
| Loan | After one year from the end of the year of the first deposit and before five years from it; up to {{ sc.loan_pct_of_balance }}% of the balance at the end of the second preceding year (paragraph 8) |
| Loan interest | {{ sc.loan_rate_in_time_pct }}% a year if repaid within {{ sc.loan_repay_months }} months, {{ sc.loan_rate_late_pct }}% if not (paragraph 9) |
| Withdrawal | After five years from the end of the year of opening, once a year, up to {{ sc.withdraw_pct }}% of the lower of two balances (paragraph 10; see below) |
| Premature closure | Allowed only on listed grounds, such as treatment of a life-threatening illness or higher education, and not before five years from the end of the year of opening (paragraph 13) |

## The rate is not in the rule

Paragraph 7 of the notification prints {% include inr.html n=sc.rate_printed_in_scheme_pct %}% a year. That was the rate when it was notified. The rate has changed since, because the government sets it for each period.

The National Savings Institute (NSI) publishes a [table of PPF rates since inception]({{ p.nsi.url }}). Read on {{ p.nsi.read | date: "%-d %B %Y" }}, it shows:

| Period | Rate (% a year) |
|---|---:|
{% for r in p.rate_history -%}
| {{ r.period }} | {% assign x = r.rate_pct %}{% include inr.html n=x %} |
{% endfor %}
Some periods are left out of this extract; the full table is on NSI's page. The last row is the current one, {% include inr.html n=p.rate_pct %}% since 1 April 2020. The Ministry of Finance's [most recent office memorandum]({{ p.dea_om.url }}), for the third quarter of the financial year 2026-27, says the rate stays unchanged from the previous quarter. Rates are set quarter by quarter, so it can be reset again. That makes it different from a bond's yield, which moves with the market, as the [G-secs and T-bills post]({% post_url 2026-11-10-g-secs-and-t-bills %}) showed.

## The formula

```
Year-end balance  =  (previous year-end balance + deposit made that year) × (1 + r)
                     where the deposit is in place for all twelve months
```

Interest is calculated monthly but credited once a year, so within a year it doesn't compound. The compounding happens from one year to the next.

## Worked example: ₹1,50,000 every year for 15 years

This is arithmetic, not a forecast. It assumes ₹{% include inr.html n=sc.max_deposit %} is deposited every April on or before the 5th, and that the rate stays at {% include inr.html n=p.rate_pct %}% for all 15 years, which the table above shows is not how rates have behaved.

| Year | Deposited so far (₹) | Interest that year (₹) | Balance at year end (₹) |
|---|---:|---:|---:|
{% for r in ex.rows -%}
| {{ r.year }} | {{ r.deposited }} | {{ r.interest_year }} | {{ r.balance }} |
{% endfor %}
After {{ ex.rows | size }} years of deposits, ₹{% include inr.html n=ex.total_deposited %} has gone in and the balance is ₹{% include inr.html n=ex.balance_after_deposits %}, of which ₹{% include inr.html n=ex.interest_total %} is interest. The scheme counts maturity from the end of the year of opening, so the maturity date falls a financial year after the last row; the example stops at {{ ex.rows | size }} deposits and does not model that extra year.

**Two timing effects follow from paragraph 7.**

1. A deposit made after the 5th of a month earns nothing for that month, because interest is on the lowest balance between the 5th and month-end. A ₹{% include inr.html n=sc.max_deposit %} deposit on 6 April instead of 5 April earns ₹{{ ex.miss_april_text }} less over the year at {% include inr.html n=p.rate_pct %}%.
2. When in the year you deposit changes the interest. ₹{% include inr.html n=sc.max_deposit %} deposited in one lump in April earns ₹{% include inr.html n=ex.lump_interest %} that year. The same amount as ₹{% include inr.html n=ex.monthly_deposit %} on the 1st of each month earns ₹{{ ex.monthly_interest }}, because most of it sits in the account for fewer months.

**Loan and withdrawal, on the same example.** Count year 1 as the financial year of the first deposit.

- *Loan.* The first loan year is year {{ lw.loan_year }}. The limit is {{ sc.loan_pct_of_balance }}% of the balance at the end of year {{ lw.loan_year | minus: 2 }}, ₹{% include inr.html n=lw.loan_base %}, so ₹{% include inr.html n=lw.loan_max %}.
- *Withdrawal.* The first withdrawal year is year {{ lw.wd_year }}. The limit is {{ sc.withdraw_pct }}% of the lower of the year {{ lw.wd_fourth_preceding_year }} balance (₹{% include inr.html n=lw.wd_fourth_preceding_balance %}) and the year {{ lw.wd_preceding_year }} balance (₹{% include inr.html n=lw.wd_preceding_balance %}). The lower is ₹{% include inr.html n=lw.wd_base %}, so the limit is ₹{% include inr.html n=lw.wd_max %}.

## Common mistakes

- **Treating the current rate as fixed for 15 years.** It is set for each period, and whether it beats prices is a separate question, covered in [inflation and real returns]({% post_url 2026-10-20-inflation-and-real-returns %}). The table shows rates of 12% and 7.1% in the same scheme's history.
- **Depositing after the 5th and expecting that month's interest.** The scheme counts the lowest balance between the 5th and month-end.
- **Assuming the money is freely available.** That matters if you were thinking of it as part of an [emergency fund]({% post_url 2026-11-08-emergency-fund-sizing %}). The scheme allows a loan only in a window and a withdrawal only after five years, and caps both.
- **Forgetting to ask for the extension.** The option to continue with deposits must be exercised within one year of maturity; deposits made after that are refunded without interest.

**Takeaway:** PPF interest is set by the government for each period, counted on the lowest monthly balance after the 5th, and credited once a year, so the account is a 15-year arrangement with capped deposits and capped access. The rate that applies today is not in the scheme's rule text, so read the current rate from the official table.
