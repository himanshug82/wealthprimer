---
layout: post
title: "NBFCs vs banks: cost of borrowing, no CASA, and asset-liability matching"
description: "An NBFC lends like a bank but can't take current or savings deposits. How that changes its spread, returns and liquidity risk, with Bajaj Finance's FY26 data."
image: /assets/og/nbfcs-vs-banks-spread-borrowing-alm.png
date: 2026-10-22 09:00:00 +0530
series: fundamental-analysis
term: "ALM (asset-liability management)"
---

{% assign bj = site.data.sectors.bajaj %}
{% assign f26 = bj.reported.FY26 %}
{% assign f25 = bj.reported.FY25 %}
{% assign d = bj.derived %}
{% assign ot = bj.other %}
{% assign mix = ot.borrowing_mix %}
{% assign hb = site.data.real_bank %}
{% assign hd = hb.derived_fy25 %}
{% assign hf = hb.reported.FY25 %}

## A lender without a deposit franchise

An NBFC (non-banking financial company) makes loans much as a bank does —
to buy a phone, a car, a house, to run a small business. The difference is
on the other side of the balance sheet. The Reserve Bank of India's
[FAQ on NBFCs]({{ bj.rbi_faq_url }}) (updated as on {{ bj.rbi_faq_as_of }})
lists the differences from banks plainly: NBFCs **cannot accept demand
deposits**, they aren't part of the payment and settlement system (no
cheques drawn on themselves), and deposits with the NBFCs specifically
licensed to take them are **not insured** by the DICGC (Deposit Insurance and Credit
Guarantee Corporation). Those that may take public deposits can only take
ones repayable after 12 months and within 60 months.

"No demand deposits" means no current and savings accounts — no
[CASA]({% post_url 2026-10-12-casa-and-the-deposit-franchise %}), the cheap,
sticky funding that the banks module showed is a bank's biggest advantage.
An NBFC borrows instead: from banks, by issuing bonds and commercial paper
in the money market, from abroad, and (if licensed) through fixed deposits.
Three things follow:

1. **Its money costs more**, so it has to lend at higher rates to earn a
   spread — which usually means lending to riskier or more specialised
   borrowers.
2. **It runs with less leverage** than a bank, so its return on assets has
   to be higher to reach a similar return on equity.
3. **It has to keep refinancing.** Borrowed money comes due on a schedule,
   whether or not markets are willing to lend again that week. Matching
   when money comes in against when it goes out — **asset-liability
   management (ALM)** — is a survival skill, not a technicality.

## The formulas

```
Spread                   ≈  yield on loans  −  cost of funds
NII margin               =  net interest income  /  average loan assets
                            (the NBFC version of NIM, net interest margin)
ROE (return on equity)   =  ROA (return on assets)  ×  (average assets / average equity)

ALM cumulative gap       =  cumulative inflows − cumulative outflows,
                            bucket by bucket, from 1 day out to 5+ years
Cumulative gap %         =  cumulative gap / cumulative outflows
```

A positive gap in a bucket means more money is due *in* than *out* by then.
A negative gap in the short buckets means the lender needs to borrow again
(or sell assets) just to pay what it owes.

## Worked example: Bajaj Finance, FY26, next to HDFC Bank

Bajaj Finance figures from its [Q4 FY26 investor presentation]({{ bj.source_url }})
({{ bj.release_date }}), consolidated, as reported (after the one-time
provisions it separately discloses). HDFC Bank figures are the FY25 numbers
from the [banks module]({% post_url 2026-10-11-nim-and-the-spread %}), some
reported and some computed by this blog. Different years and slightly
different denominators — read this as a comparison of *structure*, not a
precise ranking. Historical, for illustration only.

| | HDFC Bank (FY25) | Bajaj Finance (FY26) |
|---|---:|---:|
| Cheap current and savings deposits (CASA) | {{ hf.casa_ratio_pct }}% of deposits | None — not permitted |
| Deposits as a share of borrowed funds | {{ hf.deposits_share_of_funding_pct }}% | {{ ot.deposits_share_of_borrowings_pct }}% (fixed deposits only) |
| Cost of funds | {{ hd.cost_of_funds_pct }}% | {{ f26.cost_of_funds_pct }}% |
| Yield (interest income ÷ average earning assets / loans) | {{ hd.yield_on_interest_earning_assets_pct }}% | {{ d.yield_on_avg_auf_pct }}% |
| Net interest income ÷ same base | {{ hd.nim_on_avg_interest_earning_assets_pct }}% | {{ d.nii_on_avg_auf_pct }}% |
| Credit cost (loan losses ÷ average loans) | {{ hd.credit_cost_pct }}% | {{ f26.loan_loss_to_avg_auf_pct }}% |
| ROA (profit after tax ÷ average assets or loans) | {{ hd.roa_pct }}% | {{ d.pat_on_avg_auf_pct }}% |
| Leverage (assets ÷ equity) | {% include inr.html n=hd.avg_leverage %}x | about {{ d.implied_leverage_x }}x |

Bajaj Finance's "average loans" here is average assets under finance (AUF) —
the loans on its books — at ₹{% include inr.html n=d.avg_auf %} crore. Its ROA
in the table is reported PAT over that base; the company's own figure before
one-time provisions is {{ f26.roa_pct_before_oneoffs }}%. The leverage figure
is the company's pre-one-off ROE divided by its ROA
({{ f26.roe_pct_before_oneoffs }}% ÷ {{ f26.roa_pct_before_oneoffs }}%), an
approximation. On the bank side, "earning assets" include its large bond
portfolio, which yields less than loans — one reason its yield looks so much
lower.

### Step 1: funding costs more

1. Bajaj Finance's borrowing mix at 31 March 2026 was
   {{ mix.money_markets }}% money markets, {{ mix.banks }}% bank loans,
   {{ mix.deposits }}% deposits and {{ mix.ecb }}% external commercial
   borrowings (loans from abroad). None of it is CASA.
2. Its cost of funds was {{ f26.cost_of_funds_pct }}% against
   {{ hd.cost_of_funds_pct }}% for HDFC Bank a year earlier. The company
   reports it fell {{ d.cof_improvement_bps }} basis points from FY25's
   {{ f25.cost_of_funds_pct }}%. Because it borrows at market rates, an
   NBFC's cost of funds moves with those markets, in both directions.

### Step 2: so it lends differently

3. Its yield on loans was about {{ d.yield_on_avg_auf_pct }}% —
   far above the bank's. That's what a lender without cheap deposits has to
   do: lend where rates are higher. The presentation splits its loans
   (by AUM, assets under management) as {{ ot.lending_mix.urban }}% urban,
   {{ ot.lending_mix.rural }}% rural, {{ ot.lending_mix.msme }}% MSME
   (micro, small and medium enterprises), {{ ot.lending_mix.commercial }}%
   commercial and {{ ot.lending_mix.mortgages }}% mortgages.
4. Higher-yield lending costs more to run and loses more to defaults. Its
   operating costs were about {{ d.opex_on_avg_auf_pct }}% of average loans
   and loan losses {{ f26.loan_loss_to_avg_auf_pct }}%, against a
   {{ hd.credit_cost_pct }}% credit cost at the bank. The wide spread is
   *paying for* those costs; it isn't pure profit.

### Step 3: higher ROA, lower leverage

5. What's left is a much higher return on assets —
   {{ d.pat_on_avg_auf_pct }}% on reported profit — but on far less
   leverage. The company's ROE before one-time items was
   {{ f26.roe_pct_before_oneoffs }}%
   ({{ f26.roe_pct_after }}% after them), against HDFC Bank's
   {{ hd.roe_pct }}% in FY25. Same identity as in the
   [price-to-book post]({% post_url 2026-10-15-valuing-a-bank-price-to-book %}):
   ROE = ROA × leverage. The two lenders get there by opposite routes.

### Step 4: the ALM table

The presentation includes Bajaj Finance's (standalone) *behavioural* ALM
statement at 31 March 2026 — "behavioural" meaning cash flows are bucketed
by when the company expects them (allowing for early repayments, for
example), not only by contract dates. ₹ crore:

| Time bucket | Inflows | Outflows | Cumulative gap | Cumulative gap % |
|---|---:|---:|---:|---:|
{% for row in bj.alm %}| {{ row.bucket }} | {{ row.inflows }} | {{ row.outflows }} | {{ row.cumulative_gap }} | {{ row.cumulative_gap_pct }}% |
{% endfor %}

6. In every bucket up to five years, more money was due in than out
   cumulatively. The company shows the limits it's held to for the first
   three buckets as permissible *negative* gaps of
   {{ bj.alm_permissible[0] }}, {{ bj.alm_permissible[1] }} and
   {{ bj.alm_permissible[2] }}; its gaps there were positive.
7. The last bucket closes the table: shareholders' capital sits in "over 5
   years" as an outflow that never actually comes due, so the cumulative gap
   ends at zero by construction.
8. Refinancing never stops. Of about
   ₹{% include inr.html n=d.alm_borrowings_total %} crore of borrowings in the table,
   ₹{% include inr.html n=d.alm_borrowings_due_1y %} crore — {{ d.alm_borrowings_due_1y_pct }}% — falls due within
   a year. The presentation also reports a daily average liquidity coverage
   ratio (LCR — liquid assets held against 30 days of stressed outflows) of
   {{ ot.lcr_q4_pct }}% in the March quarter, against a
   {{ ot.lcr_requirement_pct }}% requirement.

None of this is a view on Bajaj Finance. It's one year's disclosures, read
through the lens that separates an NBFC from a bank.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Two friends lend pocket money to classmates.

The first friend's class keeps its spare money with her for free — she's
the class piggy bank. She lends it out at a little interest and keeps the
difference.

The second friend has no free piggy-bank money. She has to borrow from an
older cousin who charges her interest. To make anything, she lends to
classmates who pay *more* interest — often the ones the first friend
wouldn't lend to. She earns more on each loan, but more of her borrowers
forget to pay back.

And every few weeks, the cousin wants his money back. If he ever says "no
more loans this month", she'd better have enough coming in to pay him.
That's ALM.

</details>

## Common mistakes

- **Comparing an NBFC's margin with a bank's and calling the NBFC more
  profitable.** A higher yield usually comes with higher operating costs and
  credit losses. Compare what's left after both — ROA — and then remember
  the leverage difference.
- **Ignoring where the money comes from.** Two NBFCs with the same margin
  can have very different risks if one borrows long-term and the other
  leans on short-term market paper. Read the borrowing mix and the ALM
  table, not just the P&L (profit and loss statement).
- **Treating NBFC fixed deposits like bank deposits.** Per the RBI, they are
  term deposits (12 to 60 months), not repayable on demand, and not covered
  by DICGC insurance.
- **Taking "before one-time items" as the headline.** Bajaj Finance
  discloses both: ROA of {{ f26.roa_pct_before_oneoffs }}% before its
  one-time provisions and {{ f26.roa_pct_after }}% after. Those provisions
  were real costs; use the adjusted figure to understand trend, not to
  replace the reported one.

**Takeaway:** An NBFC lends like a bank but can't take current or savings
deposits, so it pays more for money, lends at higher rates to riskier
borrowers, and runs on less leverage. Judge it on what's left after credit
losses, and read its funding mix and ALM table, because it must keep
refinancing.
