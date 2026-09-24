---
layout: post
title: "Reading a factsheet: what's in it, and what isn't"
description: "Section by section through a real mutual fund factsheet: holdings, costs, risk numbers, portfolio turnover, and what the document deliberately leaves out."
image: /assets/og/reading-a-factsheet.png
date: 2026-10-26 09:00:00 +0530
series: mutual-funds
term: "Factsheet"
---

{% assign mf = site.data.mf %}
{% assign f = mf.index_fund %}
{% assign rr = mf.rolling_returns %}
{% assign v = mf.volatility_and_sharpe %}

## The document nobody reads

Every mutual fund publishes a monthly **factsheet** — a two-or-three-page
summary of what the fund holds, what it costs, and how it has done. It's free,
it's on every AMC's (asset management company's) website, and it is the single most useful document about
a fund that almost nobody opens.

This post walks through it section by section, using everything the previous
eight posts built. It closes the first half of the series, so it also says
plainly what a factsheet cannot tell you.

## Section by section

### Scheme details

| Field | What to actually check |
|---|---|
| Category | SEBI-defined. Decides what the fund is *allowed* to hold and which benchmark applies |
| Inception date | How much history exists. A fund launched after 2013 has never seen a 2008 |
| Benchmark | Is it a **TRI** (total return index)? [The last post]({% post_url 2026-10-25-benchmarks-and-comparing-like-with-like %}) explains why this matters more than it looks |
| Fund manager & tenure | A ten-year record under a manager who left last year is not this fund's record |
| AUM (assets under management — the fund's size in ₹) | Very large AUM can constrain a small-cap strategy; very small AUM raises viability questions |

Manager tenure is the field most often skipped. Performance history belongs
to whoever produced it.

### Expense ratio

Two numbers, direct and regular. From [the expense post]({% post_url 2026-10-21-expense-ratios-direct-vs-regular %}):
the gap between them is pure distribution commission, and on an actively
managed fund it was {{ mf.expense_ratio.active_fund.gap_pp }} percentage points a year — about {{ mf.expense_ratio.active_fund.difference_pct }}% of the final
corpus over thirteen years.

Check which plan you actually hold. Many people assume direct and own regular.

### Portfolio

- **Top holdings and concentration.** Top-10 weight tells you how concentrated
  it is. A fund with 45% in ten names behaves very differently from one with
  20%.
- **Sector allocation.** Two funds in the same category can hold entirely
  different sectors.
- **Number of holdings.** Fifty-plus stocks starts to resemble an index at a
  considerably higher fee.
- **Portfolio turnover.** How much was traded. High turnover means trading
  costs that sit *outside* the expense ratio and are never itemised anywhere.

**The overlap check** is worth doing once: if you own four large-cap funds,
compare their top-10 lists. Owning the same twelve companies four times over
is not diversification, and it's the most common portfolio error among
Indian retail investors who own many funds.

### Performance

Point-to-point returns for 1, 3, 5 years and since inception, alongside the
benchmark. As [MF-2]({% post_url 2026-10-19-point-to-point-returns %}) showed, these all
end on the same date — so they share the same endpoint bias. The same fund
showed 2.56% and 23.92% over five-year windows depending on the start month.

If the AMC publishes rolling returns or a SIP-return table, that's more
informative. If it doesn't, you can compute them yourself — that's what the
Python in [MF-3]({% post_url 2026-10-20-rolling-returns %}) is for.

### Risk measures

Usually standard deviation, beta (how much the fund tends to move when its
benchmark moves 1%), Sharpe, sometimes maximum drawdown. From
[MF-6]({% post_url 2026-10-23-volatility-and-sharpe %}): always check the period and the
risk-free rate, and never compare a Sharpe across categories.

And note what's usually missing: **drawdown recovery time**. A factsheet may
tell you the fund fell 59.7%. It rarely tells you the last such fall took
[almost six years]({% post_url 2026-10-22-drawdown %}) to recover. That's the number that
decides whether you'd still have been holding.

## A worked read

The fund used throughout this series, read as if off a factsheet:

| Field | Value |
|---|---|
| Fund | {{ f.name }} |
| Category | {{ f.category }} |
| History available | {{ f.regular_start }} to {{ f.regular_end }} ({{ f.years_of_history }} years) |
| Return over the available history | {{ v.annualised_return_pct }}% a year |
| Volatility | {{ v.annualised_volatility_pct }}% |
| Sharpe (rf {{ v.risk_free_pct }}%) | {{ v.sharpe }} |
| Maximum drawdown | {{ mf.drawdowns.worst_pct }}% ({{ mf.drawdowns.worst_date }}) |

All figures computed from [AMFI NAV history via mfapi.in]({{ f.source_url }}),
{{ f.regular_start }} to {{ f.regular_end }}. Historical data, for illustration only.
The free AMFI history starts in April 2006, so the return row covers that
window — a real factsheet's "since inception" figure runs from the fund's
launch date and can differ.

And the things a factsheet would not have told you, which this series
computed:

| | |
|---|---|
| 5-year rolling returns | {{ rr.years_5.min }}% to {{ rr.years_5.max }}%, median {{ rr.years_5.median }}% |
| 10-year windows below 8% a year | {{ rr.years_10.pct_below_8 }}% |
| Recovery from the 2008 fall | 2,162 days (5.9 years) |
| 5-year SIP from Jan 2007 | XIRR of −0.02% |
| Cost of the regular plan | {{ mf.expense_ratio.index_fund.gap_pp }} pp a year on this fund |

Same fund. The second table is the one that describes what owning it was
actually like.

## What a factsheet cannot tell you

The honest close, in the spirit of [what technical analysis cannot
do]({% post_url 2026-10-17-what-technical-analysis-cannot-do %}).

**Whether past returns will continue.** The strongest, most consistent finding
in fund research is that past performance predicts future performance weakly
at best. Every factsheet carries the required warning, and it is not
boilerplate — it's the finding.

**Whether the manager's record was skill or luck.** Distinguishing the two
needs far more data than any individual track record contains. A five-year
record is a small sample, and thousands of funds competing guarantees some
excellent records arise by chance alone.

**What the portfolio holds today.** Factsheets show month-end holdings,
published with a lag. An actively traded fund may look quite different now.

**What it costs beyond the expense ratio.** Trading costs from portfolio
turnover aren't in the TER (total expense ratio — the expense ratio's
official name). Neither is the tax you'll pay on redemption.

**Whether it suits you.** Nothing in the document knows your horizon, your
other holdings, or whether you'd sell in a 60% drawdown. Suitability is not a
property of the fund.

## How to actually evaluate a fund

Condensed from the whole series:

1. **Check the category and benchmark first.** Decide what it's *meant* to
   do, and whether the benchmark is TRI.
2. **Check the expense ratio, and which plan you hold.**
3. **Ignore the headline point-to-point returns.** They're one window,
   ending today.
4. **Compute rolling returns yourself.** The distribution, not one number.
5. **Look up the worst drawdown and how long recovery took.** Ask honestly
   whether you'd have held.
6. **Check overlap with what you already own.** Four funds holding the same
   companies is one bet.
7. **Check manager tenure against the track record's period.**
8. **Match the horizon to the asset.** Three-year money does not belong
   somewhere that has taken six years to recover.
9. **Write down what would make you sell** — before you buy. If the answer is
   "a fall," you've planned to sell at the bottom.

## Common mistakes

- **Reading only the returns table.** It's the least informative section and
  the most prominently placed.
- **Ignoring manager tenure.** The record may belong to someone who left.
- **Owning many funds and calling it diversification.** Check the overlap.
- **Assuming the benchmark is fairly chosen.** Check it's TRI and that it
  matches the mandate.
- **Comparing risk measures across categories.** Different denominators,
  different meanings.
- **Treating the risk warning as legal boilerplate.** It's the most
  evidence-backed sentence in the document.

**Takeaway:** A factsheet tells you what a fund holds, what it costs, and how
it has done over windows ending today — genuinely useful, and roughly half of
what you need. The rest you compute yourself: the distribution of rolling
returns, how deep the falls went and how long they lasted, and what the fee
compounds to. What no factsheet can supply is whether any of it will happen
again, or whether the fund suits you — and those are the two questions that
actually decide the outcome.
