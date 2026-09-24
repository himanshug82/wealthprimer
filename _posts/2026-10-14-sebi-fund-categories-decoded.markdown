---
layout: post
title: "SEBI fund categories decoded: what the label on the tin actually constrains"
description: "SEBI's 2017 rules define every fund category by a hard portfolio constraint. What large cap, flexi cap and credit risk actually bind, and why it matters."
image: /assets/og/sebi-fund-categories-decoded.png
date: 2026-10-14 09:00:00 +0530
series: mutual-funds
term: "Fund categories (SEBI)"
---

{% assign c = site.data.mf2.categories %}

## Why there are labels at all

Until 2017 an Indian fund house could run three "large cap" funds with three
different definitions of large, and a scheme called *Opportunities* could hold
anything. Comparing funds meant first working out what each one actually was.

SEBI's categorisation circular of October 2017 fixed that with two rules. Each
fund house may run **only one scheme per category** (with a few exceptions such
as index funds), and every category is defined by a **hard portfolio
constraint** — a minimum the scheme must hold, checked continuously, not a
description of intent.

That second rule is the useful part. A category name is a promise about the
portfolio that the manager cannot break without SEBI noticing. Knowing exactly
what each promise is — and, just as important, what it *leaves open* — is what
lets you compare like with like, which the
[benchmarks post]({% post_url 2026-10-02-benchmarks-and-comparing-like-with-like %})
argued is most of the work in evaluating a fund.

Definitions below start from that circular ({{ c.circular }} in 2020), later
consolidated in SEBI's {{ c.master_circular }}. SEBI then replaced
that clause with a revised categorisation circular ({{ c.revision_2026 }}):
value, contra, dividend yield and focused funds now need at least 80% in
equity rather than 65%, a fund house may run both a value and a contra fund
as long as their portfolios overlap by no more than 50%, sectoral and thematic
funds face a similar overlap cap, and the "solution-oriented" category was
discontinued. Existing schemes got six months to comply (three years for the
sectoral/thematic overlap cap). The thresholds below reflect the 2026 revision
as reported when this post was written — check the current text before
relying on one, since these do get tweaked.

## Market cap bands: who counts as large, mid and small

Every equity category starts from one list. Twice a year AMFI (the Association
of Mutual Funds in India) ranks all listed companies by average
[market capitalisation]({% post_url 2026-09-27-market-cap %}) and publishes the
cut-offs:

```
Large cap  =  ranks   1 to 100
Mid cap    =  ranks 101 to 250
Small cap  =  ranks 251 onwards
```

Two consequences people miss. The bands are defined by **rank, not by a
rupee size**, so the 100th company today is a far bigger business than the
100th company in 2017 — "large cap" has quietly inflated. And because the
list is republished every six months, a stock can move from mid to large (or
back) without anything happening to the company. A mid-cap fund holding it
then has one month to rebalance to the updated list.

## Equity categories

| Category | The hard rule | Core band |
|---|---|---|{% for k in c.equity %}
| **{{ k.category }}** | {{ k.rule }} | {{ k.universe }} |{% endfor %}

That's the equity group only. SEBI also defines debt categories (below),
hybrid categories, life-cycle funds, and an "other schemes" group that holds
index funds, ETFs and funds of funds — hybrids and the
rest are out of scope here.

Read the rules for what they *don't* say.

**Large cap** must keep 80% in the top 100 — but the other 20% is free, and a
"large cap" fund's excess return over the Nifty can come from that 20%,
which is not large-cap exposure at all.

**Flexi cap** has no band minimums whatsoever. Two flexi-cap funds can be
80% large cap and 60% small cap respectively and both be perfectly compliant.
Comparing them to each other, or to one benchmark, tells you very little until
you look at where the money actually sits.

**Multi cap** is the opposite: it *forces* at least a quarter each into large,
mid and small, so it is structurally more mid-and-small-heavy than most
"flexi" funds. The two names sound interchangeable. The portfolios are not.
(The flexi-cap category was created in November 2020 precisely because the
multi-cap rule was tightened in September 2020, and many funds that had
called themselves multi cap moved over rather than be forced into small caps.)

**Index fund / ETF** is the one category where the constraint is total: at
least 95% in the index's securities. That's what makes the arithmetic in this
series clean — there's no discretionary residue to explain.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Think of a school sports day with age groups. "Under-10" means every runner
must be under 10 — the rule is checked, so you know a race is fair.

But imagine one race called "Open" where anyone can run, and another called
"Mixed" where the organiser *must* pick a third of the team from each age
group. Both sound like "everyone welcome". They're completely different races.
If you compared an Open team full of 15-year-olds against a Mixed team, the
Open team would win, and it would mean nothing.

Flexi cap is the Open race. Multi cap is the Mixed one.

</details>

## Debt categories: duration by name, credit by rule

Debt categories are sliced two ways at once, and the
[debt funds post]({% post_url 2026-10-12-debt-funds-explained %}) explained why both
matter: **duration** decides how much the NAV moves when rates move; **credit
quality** decides whether a borrower might not pay.

Most debt categories are defined by **Macaulay duration** — the
weighted-average time to the portfolio's cash flows, a close cousin of the
[modified duration]({% post_url 2026-10-06-modified-duration %}) used to
estimate price sensitivity. A few are defined by *what* they hold instead.

| Category | The hard rule | What it implies |
|---|---|---|{% for k in c.debt %}
| **{{ k.category }}** | {{ k.rule }} | {{ k.risk }} |{% endfor %}

The row to stare at is **credit risk**: the category is *defined* as holding
at least 65% in bonds rated AA and below. That is not a warning label someone
forgot to remove — it is the mandate. The higher yield is the market's price
for exactly that.

Two more things the debt table reveals. **Dynamic bond** funds have no
duration constraint at all, which means their rate risk is whatever the
manager currently believes; two dynamic bond funds can be as different as an
overnight fund and a gilt fund. And **liquid** funds are constrained by
*maturity* (91 days) rather than duration, which is why their NAVs look like
straight lines.

## Why the label matters for comparison

Every performance comparison — returns, [rolling returns]({% post_url 2026-09-27-rolling-returns %}),
[drawdowns]({% post_url 2026-09-29-drawdown %}), [Sharpe ratios]({% post_url 2026-09-30-volatility-and-sharpe %}),
rankings, star ratings — is only meaningful *within* a category, because the
category constraint is what makes the funds comparable. A small-cap fund
beating a large-cap fund over five years is not information about either
manager; it is information about small caps over those five years.

That is also why category boundaries are where the mischief happens. A fund at
the loose end of its category (a flexi cap that is really a small-cap fund; a
"large cap" leaning hard on its free 20%) will top its category's table in
the years its tilt works, and look like a genius against peers who took the
label literally.

## Common mistakes

- **Treating flexi cap and multi cap as synonyms.** One has no band minimums;
  the other forces 25% into each band. They are structurally different
  products.
- **Assuming "large cap" means 100% large cap.** It means 80%. Check the
  factsheet for where the other 20% sits — the
  [factsheet post]({% post_url 2026-10-11-reading-a-factsheet %}) shows where.
- **Comparing across categories.** A fund winning against a different
  category's funds has told you about the category, not the fund.
- **Reading "dynamic" as "safe".** It means unconstrained duration, which is
  the opposite of a promise.
- **Not noticing a category change.** Funds do get reclassified; a scheme's
  five-year record may belong to a different mandate.

**Takeaway:** SEBI's categories are hard portfolio constraints, not marketing
adjectives — large cap means 80% in the top 100 companies, credit risk means
65% in bonds rated AA or below, flexi cap means no band minimums at all. Know
the constraint and you know what a fund's record is actually a record *of*,
which is the only basis on which comparing two funds means anything.
