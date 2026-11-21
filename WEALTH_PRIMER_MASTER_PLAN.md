# Wealth Primer 2.0 — master plan

The single, permanent reference for the Wealth Primer 2.0 transformation: what we are building, the rules it must respect, where it stands, and what has been decided. Keep it current. When a sprint ends or a decision is made, update the **Status** and **Decision log** sections here and link the evidence.

- **Started:** 21 November 2026
- **Last updated:** 21 November 2026 (Sprint 1 done; first Sprint 2 hygiene fixes shipped)
- **House rules for writing:** `CLAUDE.md` (they take precedence over anything here)
- **How the site builds and publishes:** `_docs/how-it-works.md`
- **Open editorial tasks:** `TODO.md`
- **Sprint evidence:** `_review/sprint-<n>/`

---

## 1. Vision

Turn Wealth Primer from a concept-by-concept finance blog into **an independent investor education and decision-support platform for India**.

> **Understand your money. Evaluate your investments. Make informed decisions.**

**Audience:** Indian self-directed investors who want to make better decisions by understanding investments, evaluating risk and managing portfolios. Default reader: an intelligent beginner; depth layered in.

**What "decision support" means here.** Frameworks, checklists, worked examples and calculators that run on the reader's own generic inputs and show the mechanics. It never means ranking, screening or scoring real securities, reviewing a reader's holdings, or telling anyone what to do. (Proposed scope rule, pending decision D3.)

## 2. Business objectives, in order

1. Increase organic search traffic.
2. Improve content quality and differentiation.
3. Improve engagement and returning readership.
4. Build a newsletter audience.
5. Establish a credible financial education brand.
6. Generate AdSense revenue.
7. Later: premium educational resources and investor tools.

Objectives 1–5 come before 6 and 7. A finance site earns ads and paid products only after it has earned trust and traffic.

## 3. Non-negotiables

1. **Education, not advice.** No buy/sell calls, targets, verdicts on a real company's valuation or management, or fair values for listed companies. The legal position is no SEBI RA/IA registration; the brand is credibility-first. Full rules in `CLAUDE.md` → Compliance guardrails.
2. **Lagged, dated data.** Worked-example prices and figures are at least 3 months old, with the as-of date stated.
3. **Rules from primary sources.** Tax and regulation posts carry `needs_review` and `rules_as_of`; no rule from memory.
4. **URL continuity.** No permalink changes, deletions or redirects without explicit owner approval.
5. **No unnecessary rebuild.** Stay on Jekyll, GitHub Pages, Markdown/YAML and the existing calculators. No React, Next.js, CMS, database or paid infrastructure without a demonstrated need.
6. **No bulk AI rewriting** of existing posts. Improve one post or cluster at a time, through the existing skills and the `post-auditor`.
7. **Evidence before decisions.** Use real analytics; separate verified findings from hypotheses; document major decisions here.
8. **Small, reviewable changes.** One concern per pull request; production changes only with owner approval.

## 4. Where we started (baseline, 21 Nov 2026)

Details and sources: `_review/sprint-1/`.

| Area | Baseline |
|---|---|
| Content | 216 posts written: 157 published (18 Aug – 20 Nov 2026), 59 scheduled to 18 Mar 2027 (one every two days; moved to one a day, to 19 Jan 2027, on 21 Nov). 8 series. 101 posts published in October 2026 alone |
| Tools | 8 calculators: 3 Google Sheets (rolling returns, SIP/XIRR, DCF), 5 on-page JavaScript. 103 calculator figures match their posts |
| Technical SEO | Strong: titles, descriptions, canonicals, one H1, JSON-LD (BlogPosting, BreadcrumbList), custom sitemap, Lighthouse 100 on mobile and desktop |
| Indexing | 53 pages indexed, of which 49 posts (of 157). 101 "crawled – currently not indexed", 20 "discovered – not indexed" |
| Search | 30 Sep – 19 Nov 2026: 2 clicks, 692 impressions, average position 24.1, 91 queries |
| GA4 | 1 Aug – 20 Nov 2026: 217 sessions, 190 users, 0 returning; mostly bot traffic; 21 organic sessions |
| Sitemap | Last read by Google 25 Oct 2026 |

**Diagnosis.** The binding constraint is **indexing and trust**, not templates or page speed. Structure is organised by how the site was written (series of concepts), not by what a reader comes to do. The strongest assets — generated numbers, the Desi Bites case study, methodology, calculators — are under-exposed.

## 5. Product architecture

### Reader journeys

| Journey | Scope | Main sources today |
|---|---|---|
| **Learn** | Concepts, jargon, market mechanics | Jargon, Decoded; Market basics |
| **Analyse** | Stocks, funds, ETFs, bonds, valuation | Fundamental analysis; Technical analysis; Mutual funds |
| **Portfolio** | Allocation, diversification, rebalancing, cash and safe money | Money Before Markets; portfolio posts from Risk and MF — thinnest journey |
| **Risk & Tax** | Drawdowns, leverage, behaviour, taxation | Risk; Tax |
| **Tools** | Calculators, worksheets, checklists | `/tools/` |

Series stay as they are (they drive Part N of M and prev/next). Journeys are a second, reader-facing layer of hub pages that curate existing posts. A post can appear in more than one journey.

### Navigation (decided 21 Nov 2026, D2)

**Learn · Analyse · Portfolio · Risk & Tax · Tools · About**, plus a site search box. Six items, which is the most the header fits on one line. "Insights" is dropped: it implies market commentary, at odds with the lag and no-calls rules. Series, Glossary, Case study and Methodology leave the top bar: the glossary sits under Learn, the case study under Analyse, Methodology under About and in the footer. The series pages stay (they drive Part N of M and prev/next) and are linked from the journey pages.

### Flagship guides

Each is a hub page in one shared template, **guide option A with question cards** (decided 21 Nov 2026; [wireframes](https://claude.ai/artifact/HxbMJTyDtRPqJsMAVf2VQV#artboard-HubA)): a block of reader questions near the top, each answered by one explainer (from option B), then an ordered path in stages with a line on why to read each, calculator buttons beside the posts that have one, a sidebar with progress (optional, browser-only), the guide's tools, a note on the worked-example data and its key terms, and one clear next step. A post not yet published shows its date, not a link. New writing is connective only.

| # | Guide | Built from | Status |
|---|---|---|---|
| 1 | The Indian Investor's Guide to Mutual Funds | Mutual funds series (27 published), rolling-returns and SIP tools | **Built 21 Nov 2026** at `/guides/mutual-funds/`: 8 questions, 17 posts in 6 stages, 4 calculators |
| 2 | How to Analyse Stocks | The three statement posts (now in Jargon), FA series, case study, DCF sheet | Not started |
| 3 | Building Your Investment Portfolio | Money Before Markets, diversification, rebalancing, overlap | Not started; content gap |
| 4 | Understanding Investment Risk | Risk series, drawdown, volatility, behaviour | Not started |
| 5 | Indian Investor's Taxation Handbook | Tax series (18 written) | Not started; re-check after Union Budget 2027 |

### Homepage (decided 21 Nov 2026: option A, problem-first; [wireframes](https://claude.ai/artifact/HxbMJTyDtRPqJsMAVf2VQV#artboard-Main))

1. Problem-first hero that leaves entry points visible on a phone.
2. "What are you trying to do?" — journey cards.
3. Featured guides.
4. Calculators.
5. The Desi Bites case study and real-world examples.
6. How we work: lagged data, scripted numbers, no tips, no paid promotions (links Methodology).
7. Latest posts (short list).
8. Newsletter.

Option B (tools-first) was not chosen: its hero needs an on-page rolling-returns calculator, three of the eight tools are Google Sheets, and it promises more than the tools deliver today. Until a guide exists, its goal card links to the matching series page.

## 6. Content strategy

- **Publish daily, improve in parallel.** The owner set one post a day (D1, 21 Nov 2026): the written backlog runs out on 19 Jan 2027, after which the site needs seven new posts a week. Improving and interlinking existing posts (hubs, refreshes) runs alongside, and the indexed share of published posts is the check on whether the pace is hurting.
- **Every published post has a proposed action** in `_review/sprint-1/content-inventory.csv`: KEEP 58 · IMPROVE 62 · CONSOLIDATE 37 · REDIRECT 0 · RETIRE 0 (59 scheduled posts not yet labelled). Proposals only, pending D5.
- **CONSOLIDATE** means connect overlapping posts under a hub and choose which one owns the head term. It does not mean merge or redirect.
- **Priority clusters** (from Search Console): rolling returns (14 query variants, the only calculator demand); exit load / expense ratio / NAV; ex-date vs record date; trend lines; banking ratios.
- **Tax content** stays mechanics-only with primary sources, and is re-checked after each Union Budget.

## 7. Technical strategy

Keep the stack. Improve, in this order:

1. ~~Build production with the Gemfile.~~ **Done 21 Nov 2026** (PR #36; Pages source switched from "Deploy from a branch" to "GitHub Actions"). Live site now reports Jekyll 4.4.1.
2. ~~Check plain links to future-dated posts in `check_posts.py`.~~ **Done 21 Nov 2026** (PR #35).
3. ~~Add `jekyll-redirect-from`, with no redirects configured.~~ **Done 21 Nov 2026** (v0.17; `redirect_from:` in front matter; still owner approval for any URL change).
4. Design tokens extracted from `assets/main.scss`, then the hub/guide layout and homepage.
5. Client-side search over a generated JSON index.
6. An on-page rolling-returns calculator (and possibly SIP/XIRR), keeping the Sheets as "make a copy" downloads.
7. GA4 events: calculator use, Sheet opens, newsletter sign-ups, outbound source clicks.
8. Editorial standards and corrections page; author page.

Not planned: generator migration, permalink changes, CMS, database, AMP.

## 8. Roadmap (12 weeks from 21 Nov 2026)

| Phase | Weeks | Focus | Status |
|---|---|---|---|
| 1 | 1–2 | Repository assessment, analytics baseline, content inventory, SEO audit | **Done** (21 Nov 2026, PR #34) |
| 2 | 3–4 | Owner decisions D1–D5; hygiene fixes (done: A1–A3); information architecture; homepage and hub wireframes (done; options chosen); design tokens | **In progress** |
| 3 | 5–6 | Build, in order: (1) navigation and site search (**done**, PR #43); (2) the guide template and (3) the mutual funds guide (**done**, one PR); (4) the new homepage, last, so its goal cards link to real guides | **In progress** |
| 4 | 7–8 | Content consolidation, internal linking, first flagship guides | Not started |
| 5 | 9–10 | Calculator experience, newsletter offer, analytics events | Not started |
| 6 | 11–12 | SEO validation, distribution process, monitoring, next-quarter backlog | Not started |

Sprint 2 backlog: `_review/sprint-1/sprint-2-recommendations.md`.

## 9. Measures

Leading indicators until the baseline is large enough to set honest targets. Refresh monthly into `_review/sprint-<n>/analytics-baseline-<date>.md`.

| Measure | 21 Nov 2026 | Direction |
|---|---|---|
| Published posts indexed | 49 / 157 | Up, as a share |
| Search impressions (28 days) | To read at Sprint 2 start | Up |
| Organic sessions | 21 since 1 Aug (all countries) | Up |
| Returning users | 0 | Above 0, then up |
| Newsletter subscribers | Unknown (owner to supply) | Up |

## 10. Top risks

Full register: `_review/sprint-1/technical-risk-register.md`.

| Risk | Mitigation |
|---|---|
| Google judges the site low-value (fast volume, new YMYL domain) | Daily pace chosen (D1); offset with improving and interlinking, hubs, visible editorial standards; monthly indexed-share check |
| "Decision support" drifts into advice | Scope rule D3 in `CLAUDE.md` before building evaluation tools |
| ~~Production and CI build differently~~ | **Resolved 21 Nov 2026**: workflow builds with the Gemfile; Pages source is GitHub Actions |
| Rule/tax accuracy without professional review | Existing `needs_review` safeguards; post-Budget re-check |
| Analytics not decision-grade | Internal-traffic filter, bot awareness, event design |
| Ads conflict with "no paid promotions" | Defer ads; block trading/crypto/betting categories when enabled |

## 11. Decision log

| ID | Decision | Status | Date | Notes |
|---|---|---|---|---|
| — | Keep Jekyll, GitHub Pages, Markdown/YAML and existing calculators | **Decided** (brief) | 21 Nov 2026 | Revisit only with demonstrated need |
| — | Production builds only through the Actions workflow with the Gemfile; Pages source set to "GitHub Actions" | **Decided** (owner) | 21 Nov 2026 | PR #36 and settings change; ends the race with GitHub's Jekyll 3.10 builder |
| — | No URL changes, deletions or redirects without approval | **Decided** (brief) | 21 Nov 2026 | |
| — | No professional tax review; process safeguards instead | **Decided** (owner) | 26 Oct 2026 | See `CLAUDE.md` → Professional review |
| D1 | Publishing pace for the 59 scheduled posts | **Decided** (owner): one post a day | 21 Nov 2026 | 22 Nov 2026 – 19 Jan 2027, same order (`_review/schedule-2026-11-21.md`). Sprint 1 had recommended slowing down; watch the indexed share monthly and revisit if it falls |
| D2 | Navigation labels | **Decided** (owner): Learn · Analyse · Portfolio · Risk & Tax · Tools · About, plus search | 21 Nov 2026 | Series, Glossary, Case study, Methodology leave the top bar (see §5) |
| — | Homepage direction | **Decided** (owner): option A, problem-first | 21 Nov 2026 | [Wireframes](https://claude.ai/artifact/HxbMJTyDtRPqJsMAVf2VQV); option B (tools-first) set aside |
| — | Guide page template | **Decided** (owner): option A (ordered path) with option B's question cards | 21 Nov 2026 | First built for the mutual funds guide |
| D3 | Scope rule for decision-support tools | **Pending** | — | Generic inputs, mechanics only, no ranking/scoring of securities or holdings review |
| D4 | AdSense timing | **Pending** | — | Recommended: defer until organic traffic is meaningful |
| D5 | Inventory actions | **Pending** | — | Approve or amend `content-inventory.csv` proposals |

Add each new decision as a row; never delete a row — mark it superseded.

## 12. Owner actions outstanding

- Resubmit `sitemap.xml` in Search Console.
- Add a GA4 internal-traffic filter; list the current key events.
- Supply the Buttondown subscriber count and the AdSense application status.
- Decide D3–D5 (D1 and D2 decided 21 Nov 2026).

## 13. Sprint record

| Sprint | Dates | Output | Evidence |
|---|---|---|---|
| 1 | 21 Nov 2026 | Assessment: repository, inventory, SEO, UX, risks, Sprint 2 recommendations, analytics baseline | `_review/sprint-1/`, PR #34 |
| 2 (in progress) | from 21 Nov 2026 | D1 decided: one post a day to 19 Jan 2027. D2 decided; homepage option A and guide option A (with question cards) chosen from the wireframes. Hygiene: plain links to unpublished posts now checked (6 fixed, 6 RELINK markers swept); production builds with the Gemfile and Pages source is GitHub Actions; `jekyll-redirect-from` added | PRs #35, #36 |
