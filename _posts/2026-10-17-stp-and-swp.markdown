---
layout: post
title: "STP and SWP: pacing money in, and pacing it out"
description: "An STP paces a lump sum into equity; an SWP draws a corpus down monthly. What each did to a real ₹12 lakh and ₹1 crore starting in 2008, 2010 and 2020."
image: /assets/og/stp-and-swp.png
date: 2026-10-17 09:00:00 +0530
series: mutual-funds
term: "STP and SWP"
---

{% assign m = site.data.mf2 %}
{% assign stp = m.stp %}
{% assign swp = m.swp %}
{% assign s08 = stp.scenarios[0] %}
{% assign s15 = stp.scenarios[1] %}
{% assign s20 = stp.scenarios[2] %}
{% assign w08 = swp.scenarios[0] %}
{% assign w10 = swp.scenarios[1] %}
{% assign w20 = swp.scenarios[2] %}

## Two plumbing tools

The [SIP post]({% post_url 2026-10-01-sips-xirr-and-timing-myths %}) covered
money arriving monthly from a salary. Two other situations come up constantly
and have their own plumbing:

- You have a **lump sum** now — a bonus, a maturity, a property sale — and
  the idea of putting all of it into equity on one day makes you nervous. An
  **STP — systematic transfer plan** — parks the money in a low-volatility
  fund (usually a liquid or overnight fund) and moves a fixed amount into an
  equity fund every month, automatically.
- You have a **corpus** and need **income** from it — retirement, a
  sabbatical, school fees. An **SWP — systematic withdrawal plan** — redeems a
  fixed rupee amount from a fund every month and pays it to your bank account.

Both are just standing instructions to the fund house. Neither is a strategy
in itself. What they *do* to your money depends entirely on what the market
does during the months they're running — which is the part worth seeing on
real numbers.

## STP: the same ₹12 lakh, three ways in

Take ₹{% include inr.html n=stp.amount %}, and three ways to invest it in the Nifty 50 index fund
this series has used throughout:

1. **Lump sum**: all of it into the index fund on day one.
2. **STP**: park it in a low-volatility debt fund; move ₹1,00,000 into the
   index fund on the first of each month for {{ stp.months }} months. The
   unmoved balance keeps earning the parking fund's returns.
3. **Do nothing**: leave it in the parking fund.

Regular plans; source {{ m.sources.label }}. Historical data, for illustration
only — the funds are the same ones used all series, chosen for their history,
not their merits.

One caveat about that parking fund. It's UTI's scheme that **became** its
overnight fund on 3 May 2018, under SEBI's recategorisation. Before that date
it ran a different portfolio that wasn't an overnight fund, which is why the
[debt funds post]({% post_url 2026-10-12-debt-funds-explained %}) doesn't use
that older history. So wherever the numbers below start before May 2018 (the
2008 and 2015 STP rows, and the 2008 and 2010 SWP rows), read the parking
fund as "a low-volatility debt fund of its day", not as what a modern
overnight fund would have done.

![Value of ₹12 lakh from January 2008 as a lump sum, as a 12-month STP, and left in the parking fund]({{ '/assets/charts/mf2-stp.svg' | relative_url }})

| Start | Lump sum after 3 years | STP after 3 years | Parking fund only, after 3 years |
|---|---:|---:|---:|
| {{ s08.label }} | ₹{% include inr.html n=s08.lump_sum_3y %} | **₹{% include inr.html n=s08.stp_12m_3y %}** | ₹{% include inr.html n=s08.overnight_only_3y %} |
| {{ s15.label }} | ₹{% include inr.html n=s15.lump_sum_3y %} | ₹{% include inr.html n=s15.stp_12m_3y %} | ₹{% include inr.html n=s15.overnight_only_3y %} |
| {{ s20.label }} | **₹{% include inr.html n=s20.lump_sum_3y %}** | ₹{% include inr.html n=s20.stp_12m_3y %} | ₹{% include inr.html n=s20.overnight_only_3y %} |

Three rows, two different winners — and the "safe" option of leaving it all
in the parking fund won none of them. The pattern is not subtle.

**Starting at the January 2008 top**, the lump sum was still *below* ₹12 lakh
three years later. The STP, which bought most of its units during the 2008
collapse at far lower NAVs, was worth ₹{% include inr.html n=s08.stp_12m_3y %} — about
₹{{ s08.stp_12m_3y | minus: s08.lump_sum_3y | divided_by: 100000.0 | round: 2 }} lakh more. By March 2026 the gap had compounded: the lump sum
was worth ₹{% include inr.html n=s08.lump_sum_to_2026 %}, the STP ₹{% include inr.html n=s08.stp_12m_to_2026 %}.

**Starting at the April 2020 low**, the opposite. The market rose almost
every month the STP was running, so each transfer bought at a higher NAV than
the last. The lump sum finished three years at ₹{% include inr.html n=s20.lump_sum_3y %};
the STP at ₹{% include inr.html n=s20.stp_12m_3y %} — some ₹{{ s20.lump_sum_3y | minus: s20.stp_12m_3y | divided_by: 100000.0 | round: 1 }} lakh behind.

**Starting in January 2015**, an ordinary year, the two were within a
few percent of each other.

So: an STP is **insurance against investing everything just before a fall**.
Like all insurance it has a premium, and the premium is the return you give up
when the market rises while you're still half in cash. Most twelve-month
windows go up — {{ site.data.mf.rolling_returns.years_1.pct_positive | round }}% of all one-year windows in this index fund's
history ended higher, which is the whole reason to own equity — so the
premium is paid more often than the insurance pays out. When it does pay out,
as in 2008, it pays out a great deal.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You've got ₹120 to spend on a toy that changes price every month. You can buy
it all today, or buy a bit each month for a year.

If the price is about to drop, spreading it out is brilliant — you get more
toy for the same money. If the price is about to climb, spreading it out means
you keep paying more each month and wish you'd bought it all at the start.

You don't know which will happen. Spreading it out is choosing to be a bit
wrong either way rather than very wrong one way.

</details>

## SWP: the same ₹1 crore, drawn down from three dates

Now the other direction. ₹{% include inr.html n=swp.corpus %} in the index fund, withdrawing
₹{% include inr.html n=swp.monthly %} on the first of every month — ₹6 lakh a year, a 6% initial
withdrawal rate — starting on three different dates, and running to
{{ swp.end | date: "%-d %B %Y" }}.

![Corpus remaining after each monthly withdrawal, for SWPs starting January 2008, January 2010 and April 2020, and a parking-fund SWP from 2008]({{ '/assets/charts/mf2-swp.svg' | relative_url }})

| Start | Withdrawals made | Total withdrawn | Corpus left, index fund | Corpus left if it had sat in the parking fund |
|---|---:|---:|---:|---:|
| {{ w08.label }} | {{ w08.withdrawals }} | ₹{% include inr.html n=w08.withdrawn_total %} | ₹{% include inr.html n=w08.corpus_at_end_equity %} | ₹{% include inr.html n=w08.corpus_at_end_overnight %} |
| {{ w10.label }} | {{ w10.withdrawals }} | ₹{% include inr.html n=w10.withdrawn_total %} | ₹{% include inr.html n=w10.corpus_at_end_equity %} | ₹{% include inr.html n=w10.corpus_at_end_overnight %} |
| {{ w20.label }} | {{ w20.withdrawals }} | ₹{% include inr.html n=w20.withdrawn_total %} | ₹{% include inr.html n=w20.corpus_at_end_equity %} | ₹{% include inr.html n=w20.corpus_at_end_overnight %} |

Start in **January 2010** and the story is the one SWP marketing tells: you
withdraw ₹{{ w10.withdrawn_total | divided_by: 100000 }} lakh over sixteen years and the corpus more than doubles anyway.

Start **two years earlier**, in January 2008, with the identical fund and the
identical withdrawal, and the corpus falls to
**₹{% include inr.html n=swp.jan2008_low.value %}** by {{ swp.jan2008_low.date | date: "%-d %B %Y" }} — you've taken out
₹7 lakh and lost another ₹55 lakh to the crash. It never gets back above the
original ₹1 crore. Eighteen years on it stands at ₹{% include inr.html n=w08.corpus_at_end_equity %},
having paid out ₹{{ w08.withdrawn_total | divided_by: 100000 }} lakh — not a disaster, but a completely different
retirement from the 2010 one, and the difference is *which two years you were
unlucky enough to start in*.

That is **[sequence-of-returns risk]({% post_url 2026-10-13-sequence-of-returns-risk %})**: when you are withdrawing, the order of
returns matters, not just their average. A crash in year one of an SWP
forces you to sell units cheaply to fund the withdrawal, and those units are
gone when the recovery comes. The same crash in year fifteen barely matters.
The risk series' post (linked above) covers it in full; the table above is
the short version.

One more column to notice: from the 2008 start, the parking fund ended with
*more* corpus than the equity fund. (Before May 2018 it wasn't yet an
overnight fund and did have down days — plenty of them — but its swings were
tiny next to equity's.) Across the other two starts, equity won by a wide
margin. Low volatility during withdrawals is worth more than it looks.

## Tax, briefly

Both tools create taxable events every month:

- An **STP** is a redemption from the parking fund each month (debt-fund
  gains, taxed at slab rate) and a purchase into the equity fund — so it
  creates a fresh **tax lot** with its own holding period every month.
- An **SWP** is a monthly redemption; each one is matched to your oldest
  units first under FIFO — first in, first out (the
  FIFO post in the Tax series<!-- RELINK 2026-11-02-sips-and-fifo --> walks through it). So
  in a fund you've held for years, or built up through a SIP, the oldest (and usually
  cheapest) units go first, so the withdrawals are gain-heavy from the very
  first month. The opposite pattern — mostly your own capital back early on,
  more gain later — only applies to a lump sum invested just before the SWP
  starts, because those units haven't had time to grow.

The tax series<!-- RELINK 2026-10-27-how-investment-income-is-taxed --> has
the rates; the mechanics are the same as any redemption, just twelve times a
year.

Tax isn't the only deduction. An SWP from an equity fund that starts within
the fund's [exit load]({% post_url 2026-10-07-exit-load %}) window — commonly
1% on units held less than a year — pays that load on every early withdrawal. An STP out of a
liquid fund can attract SEBI's small graded exit load on units redeemed in
their first week; overnight funds generally carry none. Check the scheme's
exit-load terms before you set either one up.

## Doing it in Python

An SWP is a loop that sells units at each month's NAV:

```python
import pandas as pd

nav = pd.read_csv("uti-nifty50-index-fund-nav.csv",
                  parse_dates=["date"]).set_index("date").nav_regular_growth

def swp(start, corpus=1e7, monthly=5e4, end="2026-03-31"):
    units = corpus / nav.loc[start:].iloc[0]
    for dt in pd.date_range(start, end, freq="MS")[1:]:
        px = nav.loc[dt:].iloc[0]
        if units * px < monthly:
            return f"ran out on {dt.date()}"
        units -= monthly / px
    return round(units * nav.loc[:end].iloc[-1])

for s in ["2008-01-01", "2010-01-01", "2020-04-01"]:
    print(s, swp(s))
```

Swap the withdrawal for a transfer between two NAV series and the same loop
is an STP.

## Common mistakes

- **Treating an STP as a return-enhancer.** It lowers the *variance* of your
  entry price. On average, over most windows, it costs return. That is a
  reasonable trade for someone who would otherwise not invest at all — it is
  not free money.
- **Running an STP for years.** Twelve months of transfers reduces
  bad-timing risk meaningfully; a five-year STP mostly means holding cash for
  five years.
- **Setting an SWP rate off a good decade.** 6% looked comfortable from 2010.
  From 2008 it cut the corpus by more than half within 14 months, and the
  corpus never recovered to ₹1 crore. Withdrawal rates need to survive the
  bad start, not the average one.
- **Drawing an SWP from a 100% equity fund.** The 2008 row is what that
  looks like. A withdrawal portfolio usually wants a low-volatility bucket to
  draw from while equity recovers.
- **Forgetting both create monthly tax lots.** Twelve redemptions a year is
  twelve entries in your capital gains statement.
- **Starting an SWP inside the exit-load window.** Withdrawals from units
  bought less than a year ago can each lose the exit load (often 1%), on top of
  tax.

**Takeaway:** An STP paces a lump sum into equity and an SWP paces a corpus
out; neither changes what the market does, only *how many months of it you're
exposed to*. On real data, a 12-month STP from the January 2008 top beat the
lump sum by ₹5.7 lakh in three years and lost to it by ₹6.8 lakh from the 2020
low, while an SWP begun in 2010 doubled its corpus and the identical plan begun
in 2008 never recovered its starting value. The tool is neutral; the start
date isn't.
