---
layout: post
title: "Contingent liabilities, pledged shares and promoter holding: the page after the balance sheet"
description: "Three disclosures outside the statements that can outweigh them: a tax demand not yet booked, promoter shares pledged for a loan, and who owns the company."
image: /assets/og/contingent-liabilities-pledges-and-promoter-holding.png
date: 2026-11-16 09:00:00 +0530
series: fundamental-analysis
term: "Promoter pledge"
---

{% assign c2 = site.data.case_study_2 %}
{% assign sh = c2.shareholding %}
{% assign cl = c2.contingent_liabilities %}
{% assign f = c2.fy26 %}

## What the balance sheet leaves out

A [balance sheet]({% post_url 2026-08-20-reading-a-balance-sheet %}) records
what a company owns and owes *as of a date, as far as the accounting rules
allow it to be recorded*. That last clause hides three things a minority
shareholder needs to know and won't find in the statements:

1. Obligations that *might* become real — **contingent liabilities**.
2. Whether the people running the company have borrowed against their own
   shares — **promoter pledges**.
3. Who owns the company, and how that's changing — the **shareholding
   pattern**.

All three live in disclosures around the statements: a note, a quarterly
filing to the exchange, a table at the back of the annual report. This post
walks through each on Desi Bites Foods (fictional, as always), as of
{{ sh.as_of }}.

## 1. Contingent liabilities: the claim that isn't a liability yet

Under Ind AS 37, a company records a liability when an outflow is
*probable* and can be estimated. When it's only *possible* — a tax demand
under appeal, a lawsuit, a guarantee that may never be called — nothing
goes on the balance sheet. It goes in a note instead:

| Contingent liabilities, 31 March 2026 | ₹ lakh |
|---|---:|
| GST demand under appeal | {{ cl.gst_demand }} |
| Bank guarantees issued | {{ cl.bank_guarantees }} |
| **Total** | **{{ cl.total }}** |

The GST line reads, in the note: *{{ cl.gst_description }}*. Management's
view is that the appeal will succeed, so no provision has been made. That
may well be right. But the shareholder's arithmetic is different from
management's:

| If the demand crystallises… | |
|---|---:|
| …as a share of FY26 equity | {{ cl.pct_of_equity }}% |
| …as a share of FY26 PAT | **{{ cl.pct_of_fy26_pat }}%** |
| …as a share of cash on hand | {{ cl.pct_of_cash }}% |

A ₹{{ cl.gst_demand }} lakh demand is {{ cl.pct_of_equity }}% of equity — survivable — and half a year's
profit. For a company with Desi Bites' cash pile it's an annoyance. For a
company with thin margins and a stretched balance sheet, the same
disclosure would be the most important sentence in the report.

The reading rule: **scale contingent liabilities against PAT and against
cash, not against total assets.** Total assets makes everything look
small. What matters is whether the company could pay if it lost, and how
many years of profit that would cost.

Two more things to look for in the note. *Growth* — a contingent liability
that was ₹40 lakh three years ago and ₹120 lakh now is a dispute getting
worse, not staying still. And *nature* — a tax classification dispute is
ordinary corporate life; a guarantee given for a promoter-group company's
borrowings is a different animal, and leads directly to the next section.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Suppose you have ₹500 saved. Your friend says you owe him ₹100 from a bet.
You say you don't. You're arguing about it.

If you write down how much money you have, you'd still write ₹500 — you
haven't paid him, and you think you won't have to. But it'd be honest to
add a note: "there's an argument about ₹100."

That note is a contingent liability. It's not a debt yet. It might become
one. And anyone lending you money would want to know about it.

</details>

## 2. Promoter pledges: borrowing against the company

The **promoter** is the person or group that controls the company — in
Desi Bites' case the founder and spouse, who held {{ c2.drhp.promoter.holding_pre_ipo_pct }}% before the IPO
and hold {{ sh.promoter_pct }}% after it. Their shares are an asset, and like any asset they
can be used as collateral. When a promoter borrows against shares, the
lender takes a **pledge** over them, and the company must disclose it in
the quarterly shareholding pattern.

From Desi Bites' filing:

| Shareholding pattern, {{ sh.as_of | split: " (" | first }} | Shares (lakh) | % of total |
|---|---:|---:|
| Promoter & promoter group | {{ sh.promoter_shares_lakh }} | {{ sh.promoter_pct }}% |
| Public | {{ sh.public_shares_lakh }} | {{ sh.public_pct }}% |
| **Total** | **{{ sh.total_shares_lakh }}** | 100% |
| *of which pledged (promoter)* | *{{ sh.pledged_shares_lakh }}* | *{{ sh.pledged_pct_of_total }}%* |

So {{ sh.pledged_pct_of_promoter_holding }}% of the promoter's holding — {{ sh.pledged_pct_of_total }}% of the company — was pledged
on {{ sh.pledge_date }}. The stated purpose: *{{ sh.pledge_purpose }}*.

Why this matters to a shareholder who didn't borrow anything:

**It's a leverage you can't see on the company's balance sheet.** Desi
Bites has a modest term loan and a lot of cash. Its promoter, personally,
now has ₹{% include inr.html n=sh.loan_against_pledge %} lakh of debt secured on the company's stock. The
[debt-to-equity]({% post_url 2026-09-15-debt-to-equity %}) ratio is silent about it.

**It creates a forced seller at the worst moment.** Lenders lend a fraction
of the shares' value — here ₹{% include inr.html n=sh.loan_against_pledge %} lakh against shares worth
₹{% include inr.html n=sh.pledged_value_at_ipo_price %} lakh at the IPO price, a loan-to-value of {{ sh.ltv_at_ipo_price }}%. If the price
falls, the ratio rises. If it crosses the lender's limit (say 75%), the
promoter must top up cash or shares — or the lender sells the pledged stock
into a falling market. For Desi Bites that limit is a {{ sh.price_fall_to_breach_ltv_75_pct }}% fall from the
issue price. Pledged shares turn a price decline into a supply of shares,
which is the mechanism behind some of the ugliest falls in Indian small
caps.

**It tells you something about the promoter's own finances.** People with
spare cash don't borrow against their company. A pledge for the company's
own expansion is one thing; a pledge to fund an unrelated venture — the
case here — says the promoter's attention and money are somewhere else.

The reading rule is a ladder. *Any* pledge: read the purpose. *More than a
quarter* of the promoter holding: understand the lender's terms. *Rising
quarter after quarter*: treat it as the most important fact about the
company until it stops.

## 3. The shareholding pattern itself

Beyond pledges, the quarterly shareholding pattern answers three questions
that no ratio can:

**Is the promoter buying or selling?** A promoter stake that drifts down a
percent a quarter, with no stated reason, is the people who know most
about the company reducing their exposure. The reverse — promoters buying
in the open market — is a signal in the other direction, though smaller,
since it may be about control rather than value.

**Who else is on the register?** Institutional holders (mutual funds,
insurers, foreign investors) bring scrutiny and liquidity. Their arrival
or exit over several quarters is worth noting. For an SME-platform listing
like Desi Bites, the public {{ sh.public_pct }}% is mostly individual investors — no
institutional check on management yet.

**Is the promoter's stake locked in?** Post-IPO, {{ sh.promoter_lockin | downcase }}. A
lock-in expiry date is a date on which supply can appear. It's in the
prospectus; the [last post in this module]({{ '/series/fundamental-analysis/' | relative_url }}) covers
where.

## Where these live in a real filing

For a real company, all three are public and free. Contingent liabilities:
the notes to the annual accounts, usually titled "Contingent liabilities
and commitments." Pledges and holdings: the shareholding pattern every
listed company files with the exchange within 21 days of each quarter-end
— on the NSE or BSE site under the company's corporate filings, and on the
company's own investor page. The annual report also carries the
shareholding tables. Britannia's, for instance, is in the same
[FY25 filings]({{ site.data.real_company.company.source_url }}) this blog has used
throughout; none of the figures here are Britannia's, and this post makes
no claim about its disclosures beyond where to find them.

## Common mistakes

- **Treating "contingent" as "unlikely."** It means "not yet recorded."
  Management decides the probability, and management is not neutral.
  Scale the amount against PAT and cash yourself.
- **Reading pledge % of total shares instead of % of promoter holding.**
  {{ sh.pledged_pct_of_total }}% of the company sounds small; {{ sh.pledged_pct_of_promoter_holding }}% of the promoter's stake is the
  number that governs a forced sale.
- **Ignoring the stated purpose.** A pledge to fund the company's own
  plant and a pledge to fund a promoter's unrelated venture carry
  different messages, and the disclosure says which.
- **Assuming a high promoter stake is always good.** {{ sh.promoter_pct }}% means aligned
  incentives *and* the ability to do anything at a shareholder meeting.
  Related-party transactions matter more, not less, when one family holds
  the votes.
- **Checking once.** Shareholding patterns are quarterly. The trend over
  eight quarters is the information; a single snapshot is a fact.
- **Forgetting guarantees.** Bank and corporate guarantees, especially
  for group companies, are contingent liabilities that become very real
  very quickly when the group company can't pay.

**Takeaway:** The statements stop at the edge of what the rules let them
record. Three disclosures just past that edge — a ₹{{ cl.gst_demand }} lakh tax demand not
yet booked, {{ sh.pledged_pct_of_promoter_holding }}% of the promoter's shares pledged for an unrelated loan, and a
register showing who's buying and selling — can matter more to a minority
shareholder than anything in the five audited pages. Read them every
quarter; read the trend, not the snapshot.
