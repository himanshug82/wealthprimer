---
layout: post
title: "Benchmarks: how a passive fund 'beat its index' by doing nothing"
description: "A benchmark decides what a return means. Price return versus total return indices, and how funds could once beat an index by doing nothing at all."
image: /assets/og/benchmarks-and-comparing-like-with-like.png
date: 2026-10-25 09:00:00 +0530
series: mutual-funds
term: "Benchmark (TRI vs PRI)"
---

{% assign mf = site.data.mf %}
{% assign f = mf.index_fund %}
{% assign b = mf.benchmark %}

## Compared to what?

Every return needs a comparison before it means anything. A fund returning
14% in a year when its market returned 22% did badly. The same 14% in a year
the market returned 4% was excellent.

A **benchmark** is that reference point — an index representing what the fund
is trying to do. And the choice of benchmark quietly decides a great deal.

This post is mostly about one benchmark choice that used to flatter every
equity fund in India, and how you can see it in the data.

## The finding

Take the index fund this series has been using — a purely passive vehicle
that holds the Nifty 50 and does nothing clever at all. Compare it to the
Nifty 50 price index over the {{ b.years }} years both exist:

| | CAGR |
|---|---:|
| {{ b.index_name }} | {{ b.index_pri_cagr }}% |
| {{ f.name }}, regular plan | **{{ b.fund_regular_cagr }}%** |
| **Fund minus index** | **{{ b.fund_minus_pri_pp }} pp a year** |

Period {{ b.common_start }} to {{ b.common_end }}. Fund NAV: [AMFI via mfapi.in]({{ f.source_url }}).
Index: [{{ b.source_label }}]({{ b.source_url }}). Historical data, for illustration only.

The fund beat its own benchmark by {{ b.fund_minus_pri_pp }} percentage points a year, while charging
a fee, for {{ b.years }} years.

That should look impossible. A fund tracking an index, after costs, ought to
land slightly *below* it. Beating it consistently by a passive strategy isn't
skill — so what is it?

## PRI versus TRI

The answer is dividends.

- A **price index (PRI)** measures only price movement of its constituents.
  When a company pays a dividend, its share price typically drops by roughly
  the dividend, and the price index falls with it. The dividend itself is
  never counted.
- A **total return index (TRI)** counts price movement *and* assumes
  dividends are reinvested.

A fund holding those fifty companies actually *receives* the dividends. They
land in the fund and raise its NAV. So a fund measured against a price index
gets credited with the entire
[dividend yield]({% post_url 2026-09-28-dividend-yield %}) of the market as apparent
outperformance — for doing nothing at all.

Roughly:

```
Fund return ≈ Index price return
            + dividend yield          ← the fund receives these
            − expense ratio           ← the fund pays this
            − other costs & cash drag ← part of the tracking difference
```

The {{ b.fund_minus_pri_pp }} pp gap above is the Nifty's dividend yield, net of this fund's
costs. It is an artefact of the comparison, not a result.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine judging apple farmers by how tall their trees grow.

One farmer's trees grow the same as everyone else's — but she also sells the
apples. At the end of the year she has more money than the "tree height"
scoreboard suggests she should.

She hasn't outsmarted anyone. The scoreboard was just measuring the wrong
thing — it forgot the apples existed.

Dividends are the apples. A price index only measures the tree.

</details>

## Why this mattered enormously

Until 2018, Indian mutual funds were generally permitted to benchmark against
price indices. Which meant every actively managed equity fund got a free head
start of roughly the market's dividend yield — a percentage point or more a
year — before any manager did anything.

Fund A claims it beat its benchmark by 1.5% a year. If most of that came from
dividends the benchmark structurally ignored, the manager's actual
contribution was a fraction of the claim.

SEBI required benchmarking against **total return indices from
{{ b.tri_mandated_from }}**. It's an unglamorous rule change and one of the more consequential
ones for retail investors, because it removed a systematic bias from every
performance claim in the industry.

**The practical check**: when you see "the fund beat its benchmark," find out
whether the benchmark was TRI. For older track records spanning pre-2018,
some of the claimed outperformance may simply be missing dividends.

## Choosing a benchmark honestly

Three rules.

**It must match what the fund actually does.** A small-cap fund measured
against the Nifty 50 is being measured against the wrong market. A fund that
holds 30% debt shouldn't be compared to a pure equity index.

**It must be total return, and stated.** Per above.

**It must be fixed in advance.** A benchmark chosen after the fact, from
several candidates, is an argument rather than a measurement.

## Category comparison, and its trap

The other common comparison is against the fund's category — "top quartile
among flexi-cap funds." Useful, with one serious caveat.

**Survivorship bias.** Funds that perform badly get merged or wound up, and
disappear from the category. Compare today's surviving funds and you're
comparing against a group with the failures deleted. The surviving average is
flattered by exactly the funds that no longer exist.

This applies to almost every "average category return" you'll see, and it
biases in one direction — always upward.

Two smaller cautions: category definitions changed materially with SEBI's
2017–18 scheme rationalisation, so pre- and post-2018 category comparisons
aren't like-for-like. And within a category, funds can run very different
risk levels — beating your category with far more volatility isn't obviously
winning, which is what [Sharpe]({% post_url 2026-10-23-volatility-and-sharpe %}) was for.

## Doing it in Python

```python
import pandas as pd

nav = pd.read_csv("uti-nifty50-index-fund-nav.csv",
                  parse_dates=["date"]).set_index("date")
idx = pd.read_csv("nifty50-price-index.csv",
                  parse_dates=["date"]).set_index("date").nifty50_pri_close
fund = nav.nav_regular_growth.dropna()

start = max(idx.index[0], fund.index[0])
end = pd.Timestamp("2026-03-31")
years = (end - start).days / 365.25

def cagr(s):
    return ((s.asof(end) / s.asof(start)) ** (1/years) - 1) * 100

print(f"index (PRI) {cagr(idx):.2f}%   fund {cagr(fund):.2f}%   "
      f"gap {cagr(fund) - cagr(idx):+.2f} pp")
```

Note both series must be compared over the *same* window — hence taking the
later of the two start dates. Comparing a fund's 20-year record to an index's
18-year record is a common and entirely avoidable error.

## Common mistakes

- **Not checking whether the benchmark is TRI.** As shown, a price index
  hands every fund the dividend yield as free outperformance.
- **Accepting a benchmark that doesn't match the mandate.** Small-cap funds
  compared to large-cap indices, hybrid funds to pure equity.
- **Forgetting survivorship bias in category averages.** The failures were
  removed from the comparison set.
- **Comparing over different periods.** Same window, always.
- **Treating benchmark outperformance as skill without checking risk.** More
  return from more risk isn't the same achievement.
- **Assuming a benchmark-beating record persists.** Past outperformance is a
  weak predictor of future outperformance — much weaker than most fund
  marketing implies.

**Takeaway:** A benchmark decides what a return means, and the choice does
more work than it appears to — a purely passive index fund out-returned the
Nifty 50 price index by {{ b.fund_minus_pri_pp }} percentage points a year for {{ b.years }} years purely
because the price index ignores dividends the fund actually collects. Check
that any benchmark is total-return, matches the mandate, and was fixed in
advance, before reading anything into beating it.
