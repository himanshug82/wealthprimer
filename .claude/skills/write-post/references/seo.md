# SEO rules for Wealth Primer

Context: Jekyll on GitHub Pages, `jekyll-seo-tag` (emits title, description, canonical, Open Graph, Twitter card and BlogPosting JSON-LD), `jekyll-sitemap`, `jekyll-feed`, `lang: en-IN`, permalink `/:year/:month/:day/:title/`. YMYL (money) niche: Google weighs experience, expertise, authoritativeness and trust heavily. This blog's edge is accuracy, sourcing and honest limits.

## Search intent first

| Intent | Typical queries | Page shape |
|---|---|---|
| Definition / glossary | "ROCE meaning", "what is P/E ratio" | Direct answer first, formula, one example, mistakes |
| How-to-calculate | "how to calculate XIRR", "ROCE formula" | Formula block, numbered worked example, optional sheet/Python |
| Method | "how to read a balance sheet", "how to evaluate a mutual fund" | Step-by-step; no recommendations |
| Rules lookup | "LTCG on equity mutual funds India" | As-of date, primary source, Tax Year label, worked example |
| Comparison | "ETF vs index fund" | Table of differences, who each suits *structurally*, no "winner" for the reader |

Queries to **avoid targeting** (transactional/advisory, compliance conflict): best/top stocks or funds, multibagger, penny stock picks, buy/sell/hold, target price, tips, "will X go up", "is X overvalued", guaranteed or "safe high return". If the topic is wanted anyway, target the method version ("how to screen stocks — and what screens miss").

## Keyword patterns per series

- **Jargon**: `<term> meaning`, `<term> formula`, `how to calculate <term>`, `<term> example`, `<term> vs <term>`. Avoid "good/ideal <term>" as a verdict; if answering, say ranges depend on industry and give no pass/fail for a named company.
- **Fundamental analysis**: `how to read <statement>`, `<ratio> analysis`, `DCF explained`, `how to analyse <sector> companies`.
- **Technical analysis**: `how to read <indicator>`, `<indicator> formula`, `<indicator> in Python`, `<indicator> settings explained` (describe conventions; don't recommend settings).
- **Mutual funds**: `how to read a factsheet`, `expense ratio explained`, `what is rolling return`, `SIP vs lump sum`, `XIRR vs CAGR`.
- **Tax**: `how is <asset> taxed in India`, `<asset> capital gains tax Tax Year 2026-27` — rule posts only with primary sources.
- **Risk / behaviour**: `position sizing explained`, `why F&O traders lose money (SEBI study)`, `what is leverage in trading`.

## On-page checklist

**Title** (front matter `title`; layout renders it as the H1 — never add `# ` in the body)
- ≤ 60 characters so it isn't truncated in results; primary keyword at or near the front; one idea; sentence case (some older posts are title case — don't copy them).
- Patterns that fit: `<Term> explained: formula and example` · `How to calculate <X>: formula and worked example` · `<Concept>: what it tells you and what it can't`.
- No hype words, no clickbait numbers, no year unless the rule changes yearly (tax/regulatory) — then use "Tax Year 2026-27" and refresh the post each year.

**Description** (front matter; feeds meta description, homepage, RSS)
- 140–160 characters. Primary keyword once, a concrete promise ("with formula and a worked example"), no hype, no advice.

**Slug**: short, lowercase, hyphenated, keyword-led, no stop-word padding, no date (the permalink already carries one). Locked once published.

**Opening**: the first 100 words contain the primary keyword and a plain definition. Put a 40–60-word direct answer immediately under the "What is X" heading — this is the snippet candidate.

**Headings**: sentence-case H2s; phrase several as the questions readers type ("What does ROCE tell you?", "How is XIRR different from CAGR?"). One H1 only (the title). Logical H2 → H3 nesting. The TOC appears automatically at ≥ 6 H2s (`toc: false` to suppress).

**Internal links** (the main SEO lever on a 160-post site)
- 3–6 contextual links in the body with descriptive anchors ("price-to-book ratio"), never "click here" or "this post".
- Mandatory jargon links at first use (see `CLAUDE.md`). Link prerequisites forward-safely with `{% post_url %}` — earlier-dated posts only.
- If a link would be useful but the target is dated later, don't link; log it in `TODO.md` as an owed link.
- Don't force links; every link must help the reader's next question.

**External links**: primary sources (sebi.gov.in, rbi.org.in, nseindia.com, incometaxindia.gov.in, company filings, AMFI) with descriptive anchors; cite the circular number/date in the text. Primary sources are an E-E-A-T signal; use them for every rule, rate and statistic.

**Images and charts**: SVG/PNG in `assets/charts/` from a script in `scripts/`; markdown alt text that says what the chart shows ("Britannia closing price with 50- and 200-day moving averages, March 2025 to March 2026"), not "chart". Never hotlink. Every post needs an OG card: run `python3 scripts/make_og_cards.py` and set `image: /assets/og/<slug>.png`.

**Structured data**: `jekyll-seo-tag` already emits BlogPosting JSON-LD. Don't hand-write JSON-LD. Don't build FAQ markup for rich results — Google restricted FAQ rich results in 2023; question-style H2s capture the benefit.

**Length**: as long as the intent needs and no longer. Existing posts run roughly 500–2,100 words. Compare with the SERP; beat competitors on correctness, worked examples and "common mistakes", not on word count.

**Freshness**: add `last_modified_at` when a post is materially updated. Keep as-of dates visible in the body. Rule/tax posts: recheck after the Union Budget and when SEBI/CBDT circulars land.

**Language**: Indian English (en-IN): "utilisation", lakh/crore, ₹, FY25 / Tax Year 2026-27. Use the terms Indian readers search: demat, Nifty 50, SIP, ELSS, LTCG/STCG, NAV, TER, F&O.

## Trust signals for a YMYL site

- Every number has an as-of date and a source; every rule has a primary-source citation.
- Honest limits sections ("what this can't tell you") — they are the differentiator.
- No fabricated experience: no "I made ₹X", no invented reader stories, no testimonials.
- The disclaimer is rendered by the layout — don't add or reword one.
- Link to `/methodology/` where the data approach matters.

## What not to do

Keyword stuffing; doorway posts for variants of the same keyword (consolidate and update instead); AI-boilerplate intros ("In today's fast-paced world…"); padding to hit a word count; clickbait titles; comparing yourself to named competitors; promising results ("learn to beat the market").

## Measuring (honest)

The repo has GA4 only. Search Console is the right tool for query/impression data; if the user shares it, use it to pick titles and find posts that rank on page 2 for a refresh. Don't claim rankings or traffic you haven't seen.
