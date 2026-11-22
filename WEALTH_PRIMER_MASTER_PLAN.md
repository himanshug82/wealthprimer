# Wealth Primer 2.0 — master plan

The single, permanent reference for the Wealth Primer 2.0 transformation: what we are building, the rules it must respect, where it stands, and what has been decided. Keep it current. When a sprint ends or a decision is made, update the **Status** and **Decision log** sections here and link the evidence.

- **Started:** 21 November 2026
- **Last updated:** 21 November 2026 (Phases 1–3 done; Phase 4 in progress: four of five guides built, two modules drafted, D1–D5 decided, IMPROVE queue started; brief v2 merged, D6–D11 decided, D8 deferred)
- **House rules for writing:** `CLAUDE.md` (they take precedence over anything here)
- **How the site builds and publishes:** `_docs/how-it-works.md`
- **Open editorial tasks:** `TODO.md`
- **Sprint evidence:** `_review/sprint-<n>/`
- **Brief v2 (21 Nov 2026):** a revised owner brief was merged into this plan rather than starting over; what it changes, and the decisions it led to (D6–D11), are in §1 → *Brief v2* and §11

---

## 1. Vision

Turn Wealth Primer from a concept-by-concept finance blog into **an independent investor education and decision-support platform for India**.

> **Understand your money. Evaluate your investments. Make informed decisions.**

**Audience:** Indian self-directed investors who want to make better decisions by understanding investments, evaluating risk and managing portfolios. Default reader: an intelligent beginner; depth layered in.

**What "decision support" means here.** Frameworks, checklists, worked examples and calculators that run on the reader's own generic inputs and show the mechanics. It never means ranking, screening or scoring real securities, reviewing a reader's holdings, or telling anyone what to do. (Scope rule decided 21 Nov 2026, D3; written into `CLAUDE.md` under Calculators and code.)

### Brief v2 (21 Nov 2026)

The owner issued a revised transformation brief on 21 Nov 2026. It restates most of what this plan already covers (stay on Jekyll and GitHub Pages, preserve URLs, education not advice, evidence before decisions, small reviewable changes, a 12-week programme), so it is folded in here instead of restarting the programme. Its "Sprint 1, assessment only" step was already done (§13, sprint 1); the work continues from Phase 4.

**Positioning statement (brief v2).** *An independent financial education and decision-support platform that helps Indian investors learn financial concepts, understand the underlying mathematics, analyse investments and make more informed financial decisions.* Core philosophy: **Learn → Analyse → Decide → Manage Risk.** It is not to become a stock-tips site, a news aggregator, an affiliate site, a generic AI-written blog, or a source of return promises. This matches §1 and the D3 scope rule; "Decide" means the reader decides with frameworks and their own inputs, never that the site decides for them.

**What brief v2 adds or changes**

| Area | Brief v2 | Where it lands in this plan |
|---|---|---|
| Content volume | "Not pursuing article volume as a growth strategy"; new articles must pass a justification gate | **D6 decided:** 2–3 posts a week (supersedes D1); the gate is in §6 |
| Distribution | Organic search, newsletter, LinkedIn, repurposing; no paid ads | **D7 decided:** RSS plus LinkedIn; no newsletter for now |
| Monetisation | Premium programmes, advanced tools, downloads, courses, membership | §2 has AdSense (objective 6) gated by D4. **D8 deferred** until traffic nears the D4 bar |
| Navigation | Learn · Analyse · Manage Wealth · Risk & Tax · Tools | **D9 decided:** keep "Portfolio" (D2, live) |
| Inventory labels | Keep · Improve · Consolidate · Redirect · Retire · **Monitor** | **D10 decided:** MONITOR added to the D5 labels (§6) |
| Credibility | Editorial principles, correction and update policy, last-reviewed information, author credibility | §7 item 8, now expanded |
| Analytics | Events for calculator starts and completions, learning-pathway progression, internal navigation, subscriptions | §7 item 7, now expanded; §9 |
| Documentation | Twelve documents in `/docs` | One master plan plus `_review/` evidence; **D11 decided**; mapping in §11 |
| Article audit criteria | Accuracy, originality, intent, performance, authority, depth, linking, freshness, duplication, relevance, pathway fit | Most are columns in `content-inventory.csv` already; originality, freshness and pathway fit to be added when the IMPROVE queue reaches each post |

## 2. Business objectives, in order

1. Increase organic search traffic.
2. Improve content quality and differentiation.
3. Improve engagement and returning readership.
4. ~~Build a newsletter audience.~~ Dropped 21 Nov 2026 (owner): the email newsletter was removed; readers follow by RSS.
5. Establish a credible financial education brand.
6. Generate AdSense revenue. *(Brief v2 lists premium learning, tools, downloads, courses and membership instead and does not mention ads; which model leads is open as D8.)*
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
| 2 | How to Analyse Stocks | The three statement posts (now in Jargon), FA series, case study, DCF sheet | **Built 21 Nov 2026** at `/guides/stocks/`: 8 questions, 24 posts in 7 stages, the DCF sheet; homepage "Read a company's financial statements" card now points here |
| 3 | Building Your Investment Portfolio | Money Before Markets, diversification, rebalancing, overlap | **Built 21 Nov 2026** at `/guides/portfolio/`: 8 questions, 20 posts in 6 stages (11 scheduled, shown by date until they publish; 4 of the 8 question cards show now, the rest as their posts go live), 2 calculators (real return, goal). The content gap was filled by Money Before Markets module 2 (PR #49); homepage "Build and look after a portfolio" card now points here |
| 4 | Understanding Investment Risk | Risk series, drawdown, volatility, behaviour | **Built 21 Nov 2026** at `/guides/risk/`: 8 questions, 18 posts in 5 stages (4 scheduled, shown by date), 2 calculators. Diversification, rebalancing and sequence risk left for the portfolio guide |
| 5 | Indian Investor's Taxation Handbook | Tax series (18 written) | Not started; re-check after Union Budget 2027 |

### Homepage (decided 21 Nov 2026: option A, problem-first; [wireframes](https://claude.ai/artifact/HxbMJTyDtRPqJsMAVf2VQV#artboard-Main))

1. Problem-first hero that leaves entry points visible on a phone.
2. "What are you trying to do?" — journey cards.
3. Featured guides.
4. Calculators.
5. The Desi Bites case study and real-world examples.
6. How we work: lagged data, scripted numbers, no tips, no paid promotions (links Methodology).
7. Latest posts (short list).
8. Follow box (RSS).

Option B (tools-first) was not chosen: its hero needs an on-page rolling-returns calculator, three of the eight tools are Google Sheets, and it promises more than the tools deliver today. Until a guide exists, its goal card links to the matching series page.

## 6. Content strategy

- **Fewer posts, improve in parallel.** D6 (21 Nov 2026) sets 2–3 posts a week, superseding D1's one a day. Time-sensitive posts and tax posts keep their dates; the other 68 were re-dated to Mon/Wed/Fri, 16 Dec 2026 – 21 May 2027 (PR #64). Under D1 the written backlog ran to 1 Feb 2027 (Money Before Markets M2 and FA M5 drafted 21 Nov). Four modules approved 21 Nov 2026 cover 2–25 Feb 2027 (MF M5, Jargon M10, Market basics M2, Tax M4 after the Budget); at the slower pace that backlog lasts well into 2027, so no new module is planned until the indexed share rises, and any that is must pass the gate below. Improving and interlinking existing posts (hubs, refreshes) runs alongside, and the indexed share of published posts is the check on whether the pace is hurting.
- **Every published post has a proposed action** in `_review/sprint-1/content-inventory.csv`: KEEP 58 · IMPROVE 62 · CONSOLIDATE 37 · REDIRECT 0 · RETIRE 0 (59 scheduled posts not yet labelled). Labels approved 21 Nov 2026 (D5): IMPROVE posts are worked first, in Search Console order (pages with impressions first), one small PR at a time. CONSOLIDATE is largely served by the four flagship guides; the remaining work is choosing one owner per head term.
- **CONSOLIDATE** means connect overlapping posts under a hub and choose which one owns the head term. It does not mean merge or redirect.
- **Priority clusters** (from Search Console): rolling returns (14 query variants, the only calculator demand); exit load / expense ratio / NAV; ex-date vs record date; trend lines; banking ratios.
- **Tax content** stays mechanics-only with primary sources, and is re-checked after each Union Budget.
- **MONITOR label (D10).** Added to the D5 labels for posts under about 90 days old, or with too little Search Console data to judge. They are re-labelled at the monthly review. Applied 22 Nov 2026: the 90 posts scheduled or published since Sprint 1 carry MONITOR in `content-inventory.csv` (31 of them added as rows then).
- **New-article gate (brief v2).** A new article is proposed only if it does at least one of: build credibility and topical authority; capture meaningful, relevant search demand; fill an important knowledge gap; strengthen an existing learning pathway; give a distinctive, evidence-based explanation the site lacks. The proposal states the reader problem, audience, search intent, primary and secondary keywords, the evidence of demand (or the authority rationale), overlapping Wealth Primer posts and why they can't serve the need, the unique value, the primary sources needed, and the expected contribution. No two articles chase the same intent. `plan-module` roadmaps should carry these fields from the next module on; modules already approved (2–25 Feb 2027) are not re-gated unless D6 says so.

## 7. Technical strategy

Keep the stack. Improve, in this order:

1. ~~Build production with the Gemfile.~~ **Done 21 Nov 2026** (PR #36; Pages source switched from "Deploy from a branch" to "GitHub Actions"). Live site now reports Jekyll 4.4.1.
2. ~~Check plain links to future-dated posts in `check_posts.py`.~~ **Done 21 Nov 2026** (PR #35).
3. ~~Add `jekyll-redirect-from`, with no redirects configured.~~ **Done 21 Nov 2026** (v0.17; `redirect_from:` in front matter; still owner approval for any URL change).
4. Design tokens extracted from `assets/main.scss`, then the hub/guide layout and homepage.
5. Client-side search over a generated JSON index.
6. An on-page rolling-returns calculator (and possibly SIP/XIRR), keeping the Sheets as "make a copy" downloads.
7. GA4 events: calculator starts and completions, Sheet opens, outbound source clicks, guide (learning-pathway) progression, internal post-to-post and post-to-tool navigation, follow/RSS clicks (and subscriptions if D7 brings a newsletter back). Needs the owner's internal-traffic filter first.
8. Editorial standards page (principles, how numbers are produced, sourcing), a corrections and update policy with a visible "last reviewed" date on posts, and a stronger author page.

Not planned: generator migration, permalink changes, CMS, database, AMP.

## 8. Roadmap (12 weeks from 21 Nov 2026)

| Phase | Weeks | Focus | Status |
|---|---|---|---|
| 1 | 1–2 | Repository assessment, analytics baseline, content inventory, SEO audit | **Done** (21 Nov 2026, PR #34) |
| 2 | 3–4 | Owner decisions D1–D5 (**all decided** 21 Nov 2026); hygiene fixes (done: A1–A3); information architecture; homepage and hub wireframes (done; options chosen); design tokens (done: named in `assets/main.scss`, reference `_docs/design-tokens.md`) | **Done** 21 Nov 2026 |
| 3 | 5–6 | Build, in order: (1) navigation and site search (**done**, PR #43); (2) the guide template and (3) the mutual funds guide (**done**, PR #44); (4) the new homepage (**done**; goal cards and featured calculators edited in `index.markdown`) | **Done** 21 Nov 2026 |
| 4 | 7–8 | Content consolidation, internal linking, first flagship guides. **Done:** guides 1–4 (mutual funds PR #44, stocks #46, risk #47, portfolio #50); Money Before Markets module 2 written to fill the portfolio gap (#48, #49); FA module 5 drafted (#51); IMPROVE queue begun: GNPA answer (#53), direct answers on four not-indexed posts (#54), six indexing requests (#55). **Left:** guide 5, the Taxation Handbook (after the 1 Feb 2027 Budget re-check); choosing one owner post per head term (CONSOLIDATE); the rest of the IMPROVE queue (57 posts) | **In progress** |
| 5 | 9–10 | Calculator experience and analytics events (the newsletter offer was dropped with the newsletter, 21 Nov 2026). Ahead of schedule: the on-page goal-based investing calculator (#49), built under the D3 scope rule (#52). Analytics events wait on the owner's GA4 internal-traffic filter | Not started (one calculator built early) |
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

## 10. Top risks

Full register: `_review/sprint-1/technical-risk-register.md`.

| Risk | Mitigation |
|---|---|
| Google judges the site low-value (fast volume, new YMYL domain) | Pace cut to three posts a week from 16 Dec 2026 (D6); offset with improving and interlinking, hubs, visible editorial standards; monthly indexed-share check |
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
| D1 | Publishing pace for the 59 scheduled posts | **Decided** (owner): one post a day | 21 Nov 2026 | 22 Nov 2026 – 19 Jan 2027, same order (`_review/schedule-2026-11-21.md`). Sprint 1 had recommended slowing down; watch the indexed share monthly and revisit if it falls. **Superseded by D6** (21 Nov 2026) |
| D2 | Navigation labels | **Decided** (owner): Learn · Analyse · Portfolio · Risk & Tax · Tools · About, plus search | 21 Nov 2026 | Series, Glossary, Case study, Methodology leave the top bar (see §5) |
| — | Homepage direction | **Decided** (owner): option A, problem-first | 21 Nov 2026 | [Wireframes](https://claude.ai/artifact/HxbMJTyDtRPqJsMAVf2VQV); option B (tools-first) set aside |
| — | Guide page template | **Decided** (owner): option A (ordered path) with option B's question cards | 21 Nov 2026 | First built for the mutual funds guide |
| D3 | Scope rule for decision-support tools | **Decided** (owner): generic inputs only | 21 Nov 2026 | Tools run on the reader's own assumptions and show the mechanics. They never rank, screen or score real securities or funds, review a reader's holdings, or say what to do; tools don't load real-fund data. Written into `CLAUDE.md`. First case: the goal-based investing calculator (PR #49) |
| D4 | AdSense timing | **Decided** (owner): defer to a traffic bar | 21 Nov 2026 | Revisit when organic search brings 5,000+ sessions a month for two months running (GA4, internal and bot traffic filtered). Before any ad goes live: `ads.txt`, a consent tool, a privacy page update and category blocking (trading, crypto, betting), so ads can't contradict the no-paid-promotions promise |
| D5 | Inventory actions | **Decided** (owner): approve, IMPROVE first | 21 Nov 2026 | Labels in `content-inventory.csv` approved as proposed (KEEP 58, IMPROVE 62, CONSOLIDATE 37; no redirects or deletions). IMPROVE posts are refreshed in Search Console order, pages with impressions first, one small PR each (`refresh-post`). CONSOLIDATE = link under the guides and pick one owner per head term, never merge |
| — | Newsletter | **Decided** (owner): removed | 21 Nov 2026 | Email signup (Buttondown) removed from posts, guides and the homepage; the box at the end now offers the RSS feed only. Privacy page and the finfluencer post's disclosure updated to say there is no email list |

| D6 | Publishing pace under brief v2 ("not volume") | **Decided** (owner): 2–3 posts a week, new-article gate on unapproved modules | 21 Nov 2026 | Supersedes D1. Time-sensitive and tax posts keep their dates; the rest move to 2–3 a week until the indexed share of published posts rises, then revisit. The §6 new-article gate applies to every module not yet approved. Reversible. **Applied 21 Nov 2026** (PR #64): the 22 posts of 22 Nov – 13 Dec 2026 keep their dates; the other 68 publish Mon/Wed/Fri, 16 Dec 2026 – 21 May 2027 (`_review/schedule-2026-11-21-d6.md`) |
| D7 | Distribution channels | **Decided** (owner): RSS plus LinkedIn, no newsletter for now | 21 Nov 2026 | Brief v2 names newsletter and LinkedIn; the newsletter was removed the same day. Chosen: RSS plus LinkedIn, until there are returning readers worth emailing. LinkedIn posts follow the Twitter rule (hook plus link, no duplicate threads) |
| D8 | Monetisation model | **Deferred** (owner): decide before the D4 traffic bar is near | 21 Nov 2026 | AdSense (objective 6, D4) or brief v2's premium resources, courses and membership, or both. Either waits for the D4 traffic bar; decide before that bar is near |
| D9 | Third navigation label | **Decided** (owner): keep "Portfolio" | 21 Nov 2026 | "Portfolio" (D2, live) or brief v2's "Manage Wealth". Kept: "Portfolio" is shorter, already live, and matches the guide title |
| D10 | Add a MONITOR inventory label | **Decided** (owner): yes | 21 Nov 2026 | For posts under about 90 days old or with too little Search Console data to judge; they are re-labelled at the monthly review |
| D11 | Project documentation structure | **Decided** (owner): one master plan, no `/docs` set | 21 Nov 2026 | Brief v2 asks for twelve documents in `/docs` but also says to avoid redundancy. Kept: this plan is the one living document and split a section out only when it outgrows it. Mapping: charter, strategy and positioning → §1–3; current-state audit → §4 and `_review/sprint-1/`; information architecture → §5; SEO strategy → §6–7 and `_review/sprint-1/technical-seo-audit.md`; content audit → `_review/sprint-1/content-inventory.csv`; editorial guidelines → `CLAUDE.md`; technical blueprint → §7 and `_docs/how-it-works.md`; analytics plan → §7 item 7 and §9; backlog → §8 and `TODO.md`; decision log → §11; changelog → §13 and git history |

Add each new decision as a row; never delete a row — mark it superseded.

## 12. Owner actions outstanding

- ~~Resubmit `sitemap.xml` in Search Console.~~ Done: resubmitted and read on 21 Nov 2026, status Success, 179 pages discovered.
- Add a GA4 internal-traffic filter; list the current key events.
- Supply the AdSense application status.
- ~~Close or pause the Buttondown account (`wealthprimer`).~~ Done by the owner (confirmed 22 Nov 2026).
- Check organic sessions monthly against the D4 bar (5,000+ a month, two months running).
- D6–D11 decided 21 Nov 2026 (D8 deferred). Revisit D8 before the D4 traffic bar is near.
- Set up a LinkedIn page or profile for Wealth Primer distribution (D7), if one doesn't exist.

## 13. Sprint record

| Sprint | Dates | Output | Evidence |
|---|---|---|---|
| 1 | 21 Nov 2026 | Assessment: repository, inventory, SEO, UX, risks, Sprint 2 recommendations, analytics baseline | `_review/sprint-1/`, PR #34 |
| 2 | 21 Nov 2026 | D1 decided: one post a day (backlog now to 1 Feb 2027). D2 decided; D3–D5 decided in sprint 4 (#52); homepage option A and guide option A (with question cards) chosen from the wireframes. Hygiene: plain links to unpublished posts now checked (6 fixed, 6 RELINK markers swept); production builds with the Gemfile and Pages source is GitHub Actions; `jekyll-redirect-from` added; `scripts/` no longer published. Design tokens named with no visual change, plus a dark-mode button contrast fix | PRs #35–#42 and the design tokens PR |
| 3 (Phase 3 build) | 21 Nov 2026 | New navigation (Learn · Analyse · Portfolio · Risk & Tax · Tools · About), four journey pages and client-side search; guide template and the mutual funds guide; homepage option A | PRs #43, #44, #45 |
| 4 (Phase 4, guides and content) | 21 Nov 2026 | Guides: *How to Analyse Stocks* (24 posts, 7 stages), *Understanding Investment Risk* (18 posts, 5 stages), *Building Your Investment Portfolio* (20 posts, 6 stages); homepage goal cards repointed. Content: Money Before Markets module 2 (7 posts, 20–26 Jan 2027, with `derive_mbm2.py` and a UTI Gold ETF series) and the on-page goal calculator; FA module 5 (6 posts, 27 Jan – 1 Feb 2027, with `derive_fa5.py`); both reviewed by `post-auditor` and every P0 fixed before merge. Decisions D3 (tool scope rule, in `CLAUDE.md`), D4 (AdSense deferred to 5,000+ organic sessions a month), D5 (inventory labels approved, IMPROVE first). IMPROVE queue: GNPA direct answer and description; "In short" openings on trend lines, Fibonacci, Bollinger/ATR and CASA; indexing requested for those six pages; sitemap confirmed read (Success, 179 pages). Finding: links aren't the bottleneck (5–12 inbound each); Search Console hides most queries | PRs #46–#55 |
