# Mutual funds, module 5 "Newer fund rules and wrappers" (proposed 6 Nov 2026)

Status: **[Proposed]**. 6 posts, 22 Jan to 27 Jan 2027, one a day (the last mutual-funds file is 21 Jan 2027). Educational only: no fund is recommended, any real fund appears as a format or data example with observables, no suitability language. Rule claims from primary text opened at drafting; `needs_review: regulation` where a SEBI rule is stated.

| # | Date | Working title | Slug | Owned term / intent | Primary keyword (reasoned, no SERP run) | Prerequisite posts | Cross-series link | Data or script | Real company? | Risk / review |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2027-01-22 | NAV cut-off time: which day's price you get | nav-cut-off-and-allotment | NAV cut-off / rules lookup | mutual fund cut-off time NAV | what-a-mutual-fund-is, stp-and-swp (10-17), liquid-and-overnight-funds (2027-01-13) | Market basics | worked example by script | No | `regulation`; SEBI MF Regulations 2026 or master circular |
| 2 | 2027-01-23 | Life cycle funds: what the new category constrains | life-cycle-funds | Life cycle fund / method | what is a life cycle fund | sebi-fund-categories-decoded (10-14), hybrid-funds (10-18), the-riskometer (10-22) | none | allocation glide path by script (generic) | No | `regulation`; open SEBI circular of 26 Feb 2026 first; no suitability view |
| 3 | 2027-01-24 | Gold and silver ETFs and fund of funds: tracking and cost | gold-silver-etfs-and-fofs | Gold ETF vs gold FoF / method | gold ETF vs gold fund | index-funds-vs-etfs (10-13), expense-ratios-direct-vs-regular (09-28), debt-funds-gold-and-the-rest (tax, 12-04) | Tax | existing price data; refresh-data check for 3-month lag | No | low; no view on gold's outlook |
| 4 | 2027-01-25 | Scheme mergers and wind-ups: what happens to your units | scheme-mergers-and-wind-ups | Scheme merger / rules lookup | what happens when a mutual fund merges | segregated-portfolios (10-24), manager-changes-and-style-drift (10-23) | Market basics | none | No | `regulation`; SEBI MF Regulations 2026 |
| 5 | 2027-01-26 | Reading a debt fund's portfolio: rating mix and maturity | reading-a-debt-fund-portfolio | Portfolio rating mix / method | how to read debt fund portfolio | debt-funds-explained (10-12), modified-duration (10-06), the-riskometer | Jargon | generic portfolio table by script | No | low; define ratings inline (credit-ratings-explained is 6 Feb), owed link |
| 6 | 2027-01-27 | Specialised investment funds: what the label means | specialised-investment-funds | SIF / definition | what is a specialised investment fund | sebi-fund-categories-decoded | none | none | No | `regulation`; open SEBI SIF circular; do not state thresholds from memory |

Prerequisites checked: every `post_url` target is dated on or before the linking post.

## `_data/series.yml` bump
`mutual-funds`: `planned: 30` to `planned: 36`; comment "module 5 (6)".

## Data and scripts needed
`scripts/derive_mf5.py` to `_data/mf5.yml` (generic examples; assert allocations sum to 100); gold price data via `refresh-data` if used (3-month lag, say price vs total return); OG cards; `build_related.py`.

## Primary sources opened
None for the module's rules in this run. SEBI listing page read; the 5 Nov 2026 net-settlement circular was opened but is not used by any post here. See `_review/research/2026-11-06.md`.

## Could not verify
SEBI circular of 26 Feb 2026 (life cycle funds; only secondary summaries seen, which disagree on details); SEBI MF Regulations 2026; SIF circular; cut-off rules.

## Questions for the owner
1. Is SIF (post 6) worth a slot, or swap in close-ended funds and FMPs (no existing post)?
2. Gold post: confirm the 3-month lag is satisfiable with the data the repo has.
