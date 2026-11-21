# Money Before Markets, module 2 "Putting a portfolio together" (approved 21 Nov 2026)

Status: **[Approved]** by the owner on 21 Nov 2026 and **drafted** the same day (7 posts, 20–26 Jan 2027; #7 gold dropped because the 8 Dec Tax post already owns SGB structure; #5 has the on-page goal calculator the owner asked for), as module 2 of Money Before Markets (not a new series). 8 posts, one a day from the first free day after the written backlog (20 Jan 2027). The dates are provisional: other series need slots from 20 Jan too, so set the final dates when the posts are scheduled. Written to complete the flagship guide "Building Your Investment Portfolio" (`WEALTH_PRIMER_MASTER_PLAN.md` §5, guide 3). No post owned these terms on 21 Nov 2026 (checked against every `term:`).

| # | Date | Working title | Slug | Owned term / intent | Primary keyword (reasoned, no SERP run) | Prerequisite posts | Cross-series link | Data or script | Real company? | Risk / review |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2027-01-20 | Compounding: why time does most of the work | compounding-and-time | Compounding (and rule of 72) / definition | power of compounding | inflation-and-real-returns (10-20), point-to-point-returns (09-26) | MF, Risk | `scripts/derive_mbm2.py` → `_data/mbm2.yml`; Nifty 50 TRI illustration | No | — |
| 2 | 2027-01-21 | Asset classes: what equity, debt, gold and cash each do | asset-classes | Asset class / definition | asset classes in India | debt-funds-explained (10-12), fixed-deposit-vs-debt-fund (12-25), drawdown (09-29) | MF | Nifty 50 TRI, UTI gilt, UTI liquid, CPI (held); **new: a gold ETF NAV series from AMFI to March 2026** (`refresh-data`) | No | — |
| 3 | 2027-01-22 | Investment horizon: how often each asset lost money over 1, 3, 5 and 10 years | investment-horizon | Investment horizon / method | investment horizon meaning | rolling-returns (09-27), asset-classes | MF | rolling windows on held data; fixed horizons, incomplete windows dropped and counted | No | — |
| 4 | 2027-01-23 | Asset allocation: the mix decides most of the ride | asset-allocation | Asset allocation / definition + method | asset allocation | diversification-is-a-correlation-problem (10-12), volatility-and-sharpe (09-30), investment-horizon | Risk | mixes 100/0 to 40/60 of Nifty 50 TRI and the UTI gilt fund: return, volatility, worst drawdown | No | Brinson, Hood and Beebower (1986) cited only after reading the paper; never "93% of returns" |
| 5 | 2027-01-24 | Goal-based investing: the arithmetic of a future cost | goal-based-investing | Goal-based investing / how to calculate | goal based investing | compounding-and-time, step-up-sips (10-25), inflation-and-real-returns | MF | script: inflate the goal's cost, required monthly amount, sensitivity table | No | On-page calculator only if decision D3 allows; avoid income-target framing ("₹1 crore") |
| 6 | 2027-01-25 | Glide path: shifting the mix as a goal gets close | glide-path | Glide path / definition | glide path investing | sequence-of-returns-risk (10-13), asset-allocation, stp-and-swp (10-17) | Risk | script on held data; NPS lifecycle choices from PFRDA's own text | No | `needs_review: regulation`, `rules_as_of` |
| 7 | 2027-01-26 | Gold ETFs, gold funds and SGBs: how each is built | gold-etf-fund-sgb | Gold ETF (and SGB structure) / comparison as properties | gold ETF vs SGB | asset-classes; Tax `debt-funds-gold-and-the-rest` (11-28) for tax, linked not restated | Tax | gold ETF NAV (shared with #2); SGB terms from RBI notifications | No | `needs_review: regulation`; SGB issuance and redemption rules from RBI primary text only. Kept in at approval; drop if the RBI text can't be confirmed |
| 8 | 2027-01-27 | What a model portfolio can't tell you | limits-of-model-portfolios | Honest-limits post | asset allocation limitations | posts 2–6 | Risk | reuses #3–#4 outputs | No | — |

Checks: no duplicate owned term; every prerequisite dated earlier; no do-not-target title (`write-post/references/seo.md` §1); nothing needs a verdict on a real security; rule-stating posts flagged.

## `_data/series.yml`
`money-before-markets`: description and `about` widened to cover portfolio construction (done at approval). `planned: 7` → `planned: 15` once drafted (16 with EPF).

## Data and scripts needed
`scripts/derive_mbm2.py` writing `_data/mbm2.yml`, asserting invariants (allocation weights sum to 100%, every rolling window complete, displayed rounding reproduces). One new dataset: a gold ETF's NAV from AMFI, ending March 2026 (3-month lag holds for January 2027). OG cards via `scripts/make_og_cards.py`; `build_related.py`.

## Dropped
Safe withdrawal rate / "4% rule" (US research needing careful sourcing, close to retirement-income advice); "how to review your portfolio" (XIRR is owned, the topic leans prescriptive).

## After drafting
Add the new posts, with the existing ones (emergency fund, FD vs debt fund, diversification, concentration, overlap, rebalancing, step-up SIPs, STP/SWP, sequence risk, real returns), to `_guides/portfolio.md` and point the homepage "Build and look after a portfolio" card at it.
