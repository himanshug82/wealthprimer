# SEO rules for Wealth Primer

Stack: Jekyll on GitHub Pages (safe mode, no custom plugins), `jekyll-seo-tag` (emits `<title>` as "page title | Wealth Primer", description, canonical from `page.url`, Open Graph, Twitter card, BlogPosting JSON-LD, `dateModified` from `last_modified_at`), `jekyll-sitemap`, `jekyll-feed`, `lang: en-IN`, permalink `/:year/:month/:day/:title/`. Money content is YMYL: Google scrutinises accuracy and trust. This blog's edge is correctness, sourcing and honest limits — not volume.

Google-behaviour statements below are working conventions, not guarantees. Never invent search volumes, difficulty scores, rankings or "people also ask" questions; if you can't check, say so.

## 1. Pick the query by intent — and by whether we're allowed to answer it

| Intent | Typical queries | Page shape |
|---|---|---|
| Definition | "ROCE meaning", "what is P/E ratio" | Definition sentence, formula, one example, mistakes |
| How to calculate | "how to calculate XIRR", "ROCE formula" | Formula block, numbered worked example, sheet/Python if natural |
| Method | "how to read a balance sheet", "how to evaluate a mutual fund" | Steps; no winners |
| Rules lookup | "LTCG on equity mutual funds India" | As-of date, primary source, labels, worked example |
| Comparison | "ETF vs index fund" | Table of differences stated as properties (cost, liquidity, tax treatment). Never map to reader types, ages or goals; never rank |

**Do not target** (advisory/transactional; route to the method version instead):
- best / top / ideal / good stocks, funds, SIPs, indicators or settings; "multibagger"; penny-stock picks; buy / sell / hold; target price; tips; intraday or F&O "strategy that works"
- any query naming a real security plus good / bad / worth / outlook / forecast / review / IPO / GMP / subscribe-or-avoid; "is X a good investment"; "should I invest in X"
- "X vs Y, which is better" for named funds, stocks, brokers or apps; broker / app / AMC rankings
- Nifty / Sensex prediction or levels; "will X go up"
- income-target queries ("how to make ₹1 crore", "retire by 40"); "how to save tax on…" (prescriptive — use "what the Act allows")

Safe retitles: "What is a good P/E?" → "P/E ratio ranges: why 'good' depends on the sector". "How to save tax on capital gains" → "Capital gains exemptions: what the Act allows".

## 2. One term, one owner

- The jargon post owns "<term> meaning / formula / example". Other series own method and context ("how to analyse X using ROCE"). Before drafting: `grep -il "<term>" _posts/*` and check `term:` front matter. A second post on a term must name a different intent in the SEO brief. Link from it to the owner with the term as anchor.
- Any post that defines a term (not just jargon) sets `term:` so it reaches `/glossary/`.
- Never rename or delete a published post (the date is in the URL and there is no redirect plugin). To consolidate, put the content in the stronger URL and leave a visible pointer on the old one. A redirect gem (`jekyll-redirect-from`) is an owner decision, not a skill action.

## 3. On-page checklist

**Title** (`title:` is also the visible H1 — never add `# ` in the body)
- seo-tag appends " | Wealth Primer" (~15 characters). Put the primary keyword in the first ~45 characters; **aim ≤ 50, never > 60.** Existing titles run to 95 (median 63; 144 of 161 exceed 50) — don't copy the long ones. No clever subtitle after a colon unless it adds a searchable phrase ("…: formula and example").
- Sentence case. No hype, no clickbait numbers.
- Patterns: `<Term> explained: formula and example` · `How to calculate <X>: formula and worked example` · `<Concept>: what it tells you and what it can't`.
- Year/Tax Year in a title only for rules that change yearly, and then add a refresh row to `TODO.md`.

**Description** (`description:`; feeds meta description, homepage, RSS): 140–160 characters, primary keyword once, a concrete promise ("with formula and a worked example"), no hype, no advice.

**Slug**: short, lowercase, hyphenated, keyword-led, no date. Locked once published.

**Opening / snippet format**
- First 100 words contain the primary keyword and a plain definition.
- Under the first H2, one standalone definition sentence (≈ 40–60 words is a convention, not a Google rule). **The direct answer defines the term; it never states a "good" threshold or verdict** ("a good ROCE is above 15%" is out).
- Formula in a code block, comparisons in a markdown table, worked example as numbered steps.

**Headings**: sentence-case H2s, several phrased as the reader's question; logical H2→H3. TOC appears automatically at ≥ 6 H2s.

**Internal links** (the main lever on a 160-post site)
- Link wherever a term first appears, plus one or two "next step" links; descriptive anchors, never "click here". Count isn't a ranking factor.
- Every post links to its series hub once in the body (`{{ '/series/<slug>/' | relative_url }}`), and at least one cross-series link where natural (tax → mutual funds, TA → risk).
- Only `{% post_url %}` to posts dated on or before the post — **including when you edit an older post.** If a useful target is later-dated, don't link; log it in `TODO.md` as an owed link.

**External links**: primary sources (sebi.gov.in, rbi.org.in, nseindia.com, incometaxindia.gov.in, company filings, AMFI), descriptive anchors, circular number/date in the text.

**Images**: charts from a `scripts/` file into `assets/charts/`; informative alt text ("Britannia closing price with 50- and 200-day moving averages, March 2025 to March 2026"). Every post sets its own `image: /assets/og/<slug>.png` — **if omitted, the site-wide logo silently ships as the social card.** Run `scripts/make_og_cards.py` and confirm the file exists.

**Structured data**: seo-tag already emits BlogPosting JSON-LD; don't hand-write any. Don't add FAQ markup (Google restricted FAQ rich results in 2023 — from memory, unchecked). Question-style H2s give the benefit.

**Front-matter facts**: canonical comes from `page.url` — never set `canonical_url`. `noindex: true` works via `head.html`; use only for drafts or thin pages. `author:` is a string matched to `_data/authors.yml`; no post sets it today.

**Freshness**: `last_modified_at` only for substantive changes (a rule, a number, a correction) — never for typo or SEO edits; fake freshness is a spam signal. Keep as-of dates visible. Re-check rule and tax posts after the Union Budget and when SEBI/CBDT circulars land.

**Language**: Indian English; en-IN only. Use search vocabulary Indians use: demat, lakh/crore, "in India", "for beginners", Nifty 50, SIP, ELSS, LTCG/STCG, NAV, TER, F&O. Hinglish/Hindi queries are real but out of scope — no Hinglish titles; a Hindi edition would be a separate project.

## 4. Tax and rules posts

Readers still search the old labels. Put both the Tax Year and FY label ("Tax Year 2026-27 (FY 2026-27)") in the opening paragraph and one H2. Where section numbers changed under the Income-tax Act, 2025, name old and new (e.g. "old section 112A") **only after opening the Act or a primary source**; never guess a new number from memory. Tax posts are never "ready": mark them "draft pending professional read" and log it in `TODO.md`.

## 5. Trust signals (YMYL) — without inventing any

- Every number has an as-of date and source; every rule a primary-source citation.
- Honest-limits sections are the differentiator.
- **Do not claim credentials, a team, a track record, "our analysts", or personal results** the repo doesn't document. `about.markdown` says what the author is; stay within it.
- No fabricated reader stories, testimonials, "I made ₹X".
- Disclaimer is rendered by the layout; don't add or reword one.
- No broker/app/AMC rankings, referral or sponsored links unless the owner has decided on a disclosure policy.
- If asked for authority copy ("our analysts…"): offer only what `about.markdown` documents (a solo author, not SEBI-registered, scripts and data committed in the repo) and flag the rest as an owner decision.
- Owner decisions (flag, don't do): adding `author:` and an author URL/`sameAs` in `authors.yml`; a named "reviewed by" credit (only if true); a redirect gem.

## 6. Don't waste effort on

Keyword stuffing; doorway variants of one keyword; padding to a word count; hand-written JSON-LD; "In today's fast-paced world" intros; promising results.

## 7. Measuring

GA4 only is configured; Search Console is the right tool. If the user shares exports: monthly, list queries at position 8–20 and refresh those posts (then `last_modified_at`); look for "Duplicate, Google chose different canonical" and "Crawled, not indexed" on thin glossary posts; submit `/sitemap.xml` once. Never report rankings or traffic you haven't seen.
