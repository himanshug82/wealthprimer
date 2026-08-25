---
layout: post
title: "Capstone: reading one real company with the whole toolkit"
date: 2026-11-06 09:00:00 +0530
series: fundamental-analysis
---

{% assign bi = site.data.real_company %}
{% assign r = bi.ratios.FY25 %}
{% assign d = bi.dupont.FY25 %}
{% assign m = bi.multiples %}
{% assign mk = bi.market %}
{% assign db = site.data.case_study.ratios.FY25 %}

## Putting it together

Forty-odd posts in, this blog has covered how to read three financial
statements, roughly twenty ratios, and the machinery of valuation. Each one
arrived in isolation. That's the wrong way to actually use them — nobody
computes a debtor-days figure and stops.

So this post does one pass over one real company, in the order you'd
sensibly do it, showing how the pieces build on each other. The company is
Britannia Industries, the anchor used throughout this blog, and every figure
comes from its
[audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed with NSE/BSE on 8 May 2025), with the share
price being the NSE close on {{ mk.price_date }}. All of it historical, and used here purely
to illustrate the method.

One thing this post does **not** do is arrive at a verdict on the stock.
There's a section at the end on why that's a deliberate stopping point rather
than a cop-out.

## Step 1: what does the business actually do?

Before a single ratio. Britannia makes biscuits, bread, cakes, rusk and
dairy products, sells them through a distribution network reaching millions
of Indian retail outlets, and owns brands — Good Day, Marie Gold, NutriChoice,
Milk Bikis — that people ask for by name.

That paragraph already tells you what to expect from the numbers: modest
gross margins (food inputs are commodities), heavy advertising spend, fast
inventory turns (biscuits have shelf lives), and pricing power that shows up
in the margin line rather than in volumes. If the ratios contradicted that
picture, the interesting question would be why.

Skipping this step is how people end up computing a current ratio for a bank
and concluding something silly.

## Step 2: profitability

| Ratio | Britannia FY25 | Desi Bites FY25 |
|---|---:|---:|
| [Gross margin]({% post_url 2026-08-26-gross-margin %}) | {{ r.gross_margin }}% | {{ db.gross_margin }}% |
| [EBITDA margin]({% post_url 2026-08-28-ebitda-margin %}) | {{ r.ebitda_margin }}% | {{ db.ebitda_margin }}% |
| [Net margin]({% post_url 2026-08-30-net-margin %}) | {{ r.net_margin }}% | {{ db.net_margin }}% |
| [ROE]({% post_url 2026-09-01-roe %}) | {{ r.roe }}% | {{ db.roe }}% |
| [ROCE]({% post_url 2026-09-03-roce %}) | {{ r.roce }}% | {{ db.roce }}% |
| [ROA]({% post_url 2026-09-05-roa %}) | {{ r.roa }}% | {{ db.roa }}% |

A {{ r.gross_margin }}% gross margin narrowing to a {{ r.net_margin }}% net margin is the shape of a
consumer-brands business: the gap is advertising, distribution and staff.
Returns are high — a {{ r.roce }}% ROCE means the business earns roughly half its
capital employed back every year in operating profit.

Note the FY25 detail that a single year's table hides. Revenue grew about 7%
while EBITDA was almost flat, because input costs rose faster than prices —
gross margin compressed year on year. Good years and bad years both need
reading; this was a margin-pressure year for a business that usually doesn't
have them.

## Step 3: why the returns are what they are

The [DuPont decomposition]({% post_url 2026-10-23-dupont-roe-decomposition %}) turns the
ROE from a score into an explanation:

| Component | Britannia | Desi Bites |
|---|---:|---:|
| Net margin | {{ d.net_margin }}% | {{ site.data.case_study.dupont.FY25.net_margin }}% |
| Asset turnover | {{ d.asset_turnover }}x | {{ site.data.case_study.dupont.FY25.asset_turnover }}x |
| Equity multiplier (avg basis) | {{ d.equity_multiplier_avg }}x | {{ site.data.case_study.dupont.FY25.equity_multiplier_avg }}x |
| **ROE** | **{{ d.roe_reconciled }}%** | **{{ site.data.case_study.dupont.FY25.roe_reconciled }}%** |

Turnover and leverage are near-identical across the two companies. The entire
ROE gap is margin — which is to say, brand. That's a specific, checkable
claim about where the value in this business sits, and it points you at the
right things to monitor: pricing power and input costs, not asset
utilisation.

## Step 4: efficiency and working capital

| Ratio | Britannia FY25 |
|---|---:|
| [Inventory days]({% post_url 2026-09-07-inventory-days %}) | {{ r.inventory_days }} |
| [Debtor days]({% post_url 2026-09-09-debtor-days %}) | {{ r.receivable_days }} |
| [Creditor days]({% post_url 2026-09-11-creditor-days %}) | {{ r.payable_days }} |
| [Cash conversion cycle]({% post_url 2026-09-13-cash-conversion-cycle %}) | **{{ r.ccc }}** |
| [Asset turnover]({% post_url 2026-09-15-asset-turnover %}) | {{ r.asset_turnover }}x |

That negative cash conversion cycle is the most interesting number in this
entire post. Britannia collects from its customers in about {{ r.receivable_days }} days while
taking around {{ r.payable_days }} days to pay its own suppliers. Its suppliers are, in
effect, financing its working capital.

That's not an accounting trick — it's what distribution power looks like in
the accounts. Retailers pay quickly because they need the stock; suppliers
accept long terms because the volume is worth having. Growth funds itself
rather than consuming cash, which is why this business can grow without
constantly raising money.

## Step 5: is the balance sheet safe?

| Ratio | Britannia FY25 | Reads as |
|---|---:|---|
| [Current ratio]({% post_url 2026-09-19-current-ratio %}) | {{ r.current_ratio }} | Thin on its face |
| [Quick ratio]({% post_url 2026-09-21-quick-ratio %}) | {{ r.quick_ratio }} | Below 1 |
| [Debt-to-equity]({% post_url 2026-09-23-debt-to-equity %}) | {{ r.debt_equity }} | Low |
| [Interest coverage]({% post_url 2026-09-27-interest-coverage %}) | {{ r.interest_coverage }}x | Very comfortable |
| [Net debt/EBITDA]({% post_url 2026-09-29-net-debt-ebitda %}) | {{ r.net_debt_ebitda }}x | Net cash |

Here's where reading ratios in isolation would mislead you badly. A current
ratio of {{ r.current_ratio }} and a quick ratio of {{ r.quick_ratio }} look, by textbook rules of thumb,
like a liquidity problem.

They aren't, and the other rows explain why. Interest is covered {{ r.interest_coverage }} times
over. Net debt is *negative* — the company holds more cash and liquid
investments than total borrowings. And the negative cash conversion cycle
from the previous step means large trade payables are a structural feature of
how this business runs, not a sign of trouble paying bills. Those payables
inflate current liabilities, which is exactly what drags the current ratio
down.

The lesson generalises: a ratio that looks alarming in isolation often has
its explanation two ratios away. Rules of thumb are a prompt to investigate,
not a finding.

## Step 6: is the profit real?

| Ratio | Britannia FY25 |
|---|---:|
| [Free cash flow]({% post_url 2026-10-01-free-cash-flow %}) | ₹{% include inr.html n=r.fcf %} Cr |
| [OCF/PAT]({% post_url 2026-10-03-ocf-pat %}) | {{ r.ocf_pat }}x |
| [Capex intensity]({% post_url 2026-10-05-capex-intensity %}) | {{ r.capex_intensity }}% |

An OCF/PAT ratio above 1 means reported profit is converting into actual
cash — the single most useful check against accounting that flatters the
income statement. Britannia's {{ r.ocf_pat }}x is healthy.

But apply the scepticism the [FCF post]({% post_url 2026-10-01-free-cash-flow %}) built in. Free cash flow
rose from FY24 to FY25 mainly because capex fell from 3.3% to {{ r.capex_intensity }}% of
revenue — operating cash flow actually *declined* slightly. A rising FCF
driven by a capex pause is a different fact from a rising FCF driven by
better operations, and only one of them is repeatable.

## Step 7: what is the market paying?

At the {{ mk.price_date }} closing price of ₹{% include inr.html n=mk.price %}:

| Multiple | Britannia |
|---|---:|
| [P/E]({% post_url 2026-10-11-price-to-earnings %}) | {{ m.pe }}x |
| [P/B]({% post_url 2026-10-13-price-to-book %}) | {{ m.pb }}x |
| [EV/EBITDA]({% post_url 2026-10-15-ev-ebitda %}) | {{ m.ev_ebitda }}x |
| [Dividend yield]({% post_url 2026-10-19-dividend-yield %}) | {{ m.dividend_yield }}% |
| [PEG]({% post_url 2026-10-21-peg-ratio %}) | ~35.9 (on 1.8% FY25 PAT growth) |

Every one of these needs the context the earlier posts supplied. The P/B of
{{ m.pb }}x is extreme in the abstract, and less so once you know the business earns
{{ r.roe }}% on that book value — most of what makes Britannia valuable (brands,
distribution relationships, shelf position) was built through the P&L over
decades and appears nowhere on the balance sheet. Book value simply isn't
measuring the asset that matters.

The PEG of ~35.9 is the one to be most careful with, and the
[PEG post]({% post_url 2026-10-21-peg-ratio %}) covered why: it divides a high P/E by a single weak
year's growth. It's a statement about FY25 being a soft year, not about the
business's long-run trajectory.

## Step 8: what this exercise cannot tell you

The natural next step would be a
[discounted cash flow model]({% post_url 2026-11-02-terminal-value-and-the-full-dcf %}),
a value per share, and a comparison against the ₹{% include inr.html n=mk.price %} price. This blog stops here, on
purpose, and it's worth being straight about why.

**The compliance reason.** Wealth Primer is educational. Publishing an
intrinsic value for a specific listed stock is functionally a price target,
and price targets are the work of SEBI-registered Research Analysts. That
registration exists for good reasons and this blog doesn't hold it. So the
DCF machinery in this series was built on a fictional company, where the
method can be shown in full without the output being mistaken for a call.

**The intellectual reason, which matters more.** Everything above is
*backward-looking*. FY25 is history. The ratios describe a year that has
already happened, and a valuation depends almost entirely on what happens
next — which of these numbers persist, which mean-revert, which are about to
be disrupted by something not in the accounts at all.

Financial statement analysis is superb at telling you what kind of business
you're looking at and which questions to ask next. It is close to silent on
whether the price is right. The things it can't see are exactly the things
that usually decide the outcome:

- Management quality, capital allocation instincts, and integrity
- Competitive dynamics and whether the moat is widening or eroding
- Regulatory and input-cost shifts still ahead
- What the market has already priced in

The toolkit gets you to an informed question. It doesn't get you to an
answer, and any framework claiming otherwise is selling something.

## How to actually run this on a company

Condensed to a checklist:

1. **Understand the business first.** What it sells, to whom, and why they
   buy it. Then predict roughly what the ratios should look like.
2. **Read three years, not one.** Trends carry more information than levels,
   and one year is mostly noise.
3. **Profitability, then efficiency, then leverage, then cash.** In that
   order — each layer explains the previous one.
4. **Run DuPont on the ROE.** It converts a score into a reason.
5. **Check profit converts to cash.** OCF/PAT above 1, sustained.
6. **Never read a ratio alone.** Britannia's current ratio of {{ r.current_ratio }} would
   have misled you completely without the four numbers around it.
7. **Compare against peers and against its own history**, not against
   textbook thresholds.
8. **Write down what would change your mind.** If nothing in the accounts
   could, you weren't analysing — you were justifying.

**Takeaway:** No single ratio tells you anything; the toolkit works because
each number explains the last one, and a figure that looks alarming alone
usually has its answer two ratios away. Used well, financial statement
analysis tells you precisely what kind of business you're looking at and
which questions to ask next — and it stops well short of telling you whether
the price is right, which is a limit worth respecting rather than papering
over.
