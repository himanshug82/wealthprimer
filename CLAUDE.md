# Wealth Primer — CLAUDE.md

Wealth Primer is a financial education blog for Indian retail investors. It **teaches concepts — it does not give stock tips, predictions, or personalized advice.** Every writing decision in this repo should protect that line, because it's both the legal position (no SEBI Research Analyst / Investment Adviser registration needed) and the brand ("credibility-first").

Read this before drafting, editing, or reviewing any post.

## Who we're writing for

Readers range from someone who has never opened a balance sheet to someone who already trades and wants sharper technique. A single post should not try to serve both extremes in its main body — that's what the optional "explain it like a kid" section (below) is for. Default to writing for an intelligent beginner, and layer complexity in as the post progresses.

## Voice

Friendly, plain-spoken, a little informal — like a sharp friend explaining this over coffee, not a textbook and not a finfluencer hyping a trade. Concretely:

- Short sentences. Contractions are fine ("you'll", "it's").
- Define every acronym on first use **in every post**, even ones that feel obvious and even if an earlier post defined it (P/E, ROCE, RSI, PAT, SIP, NAV, AMC, TER, YTM, EBIT, CAGR…). If a **Jargon, Decoded** post (or any other post) already explains that term and is **dated on or before** the post you're writing, link to it right at first use — a short inline definition plus the link is fine, but the link is mandatory. If the explaining post is dated *later*, define inline and don't link (a `{% post_url %}` to a future post breaks the build — see File conventions); note the owed link in TODO.md, never as TODO text in the post.
- Use Indian context by default: ₹, NSE/BSE-listed companies, Indian mutual funds, Indian financial-year conventions.
- It's fine to have a point of view (e.g. "TA alone won't tell you if a company is a fraud") as long as it's framed as an opinion/limitation, not a trade call.
- Avoid hype words: "guaranteed," "sure-shot," "multibagger," "can't lose." These are also compliance red flags, not just bad writing.
- Humor is welcome if it doesn't undercut clarity.

## Compliance guardrails (non-negotiable)

The whole reason this blog doesn't need RA/IA registration is that it stays educational. Every post must:

1. **Never recommend a specific transaction.** No "buy X," "sell Y," "target price ₹Z," no implied calls. Naming real companies to *illustrate* a concept (e.g. "here's how to compute Infosys's ROCE from its FY24 balance sheet") is fine; framing that as a signal to act on is not.
   - **No verdicts on a real company's valuation or management, even soft ones.** The review caught lines like "rich, but not an irrational one", "that's not a mispricing", "not being valued cheaply relative to peers", "which is honest of them". Describe mechanics ("P/B = P/E × ROE, so a high ROE mechanically produces a high P/B") and say plainly that whether the multiple is justified isn't assessed.
   - **No discount rate, justified multiple or fair-value range for a real listed company** — that's a short step from a valuation call. DCFs, WACCs and justified-P/B scenarios run on Desi Bites or a generic/illustrative company; real companies get observables only.
   - Watch the cumulative effect: praise repeated across a module ("structural strength", "genuine operating strength") reads like a quality case. Frame real-company figures as one-year, backward-looking facts.
2. **Use lagged data in worked examples.** Any market price, chart, or figure used as a worked example must be at least **3 months** old at time of publishing. This is our **house rule**, deliberately stricter than SEBI's: SEBI's condition for education content was 3 months (circular of 29 January 2025) and was shortened to 30 days from 1 July 2026 (circular of 8 May 2026) — don't describe 3 months as "SEBI's rule". State the as-of date explicitly, e.g. "prices as of March 2026, used for illustration only." This is not optional — check the date on every chart/table before publishing. (Research statistics such as a newly published SEBI study are not worked-example prices and may be quoted when released — say so if a post implies otherwise.)
3. **Carry a disclaimer.** Every post ends with the shared disclaimer in `_includes/disclaimer.html`, rendered automatically by the post layout. Don't paste or reword it per post; change the include if the policy changes.
4. **Frame mistakes/limitations honestly.** Especially in the TA series — end it with an honest reckoning of what technical analysis can't do. Credibility comes from admitting limits, not from every post ending on "and that's why this indicator wins."

## The post template

Every post in the learning series (jargon glossary is the exception — see below) follows this structure:

1. **Definition** — what is this concept, in one or two tight paragraphs.
2. **Formula** — the actual formula/calculation, shown clearly (use a code block or table, not prose, for the math itself).
3. **Worked example** — a real, numbered walkthrough using 3-month-lagged price/financial data, with the as-of date stated.
4. **Common mistakes** — 2–4 ways beginners misread or misapply this concept. This section is a big part of what makes the blog worth reading over a generic explainer, so don't skip it or phone it in.
5. **Takeaway** — a 2–3 sentence summary, written to be quotable/tweetable on its own (see Twitter section below). Start the paragraph with `**Takeaway:**` exactly — the post layout styles it as a card. The **first sentence must stand alone at ≤280 characters**; most takeaways in the Sept 2026 review ran 60–90 words and weren't tweetable. Don't pack it with figures.

Glossary-series posts (jargon/ratios) can be shorter — definition → formula → one small worked example → takeaway — since "common mistakes" often collapses into the definition for a single-ratio explainer. Use judgment; don't pad.

Posts where the concept has no formula (behavioural biases, how finfluencers make money, reading a DRHP) may replace Formula/Worked example with a real, sourced illustration — but keep Common mistakes and Takeaway.

### Optional: "Explain it like you're 10"

An optional, clearly-marked, skippable section that breaks the concept down the way you'd explain it to a genuinely curious kid — analogies, no jargon, short. Rules:

- Mark it clearly so advanced readers can skip it without feeling talked down to. Suggested format:

  ```markdown
  <details markdown="1">
  <summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

  [plain-analogy explanation here]

  </details>
  ```

- Use it for genuinely non-obvious concepts (e.g. why P/E multiples differ across industries), not for things that are already simple.
- Never make this section required reading to understand the rest of the post — it's a supplement, not a dependency.
- Tone here can be more playful than the rest of the post (real-world analogies: pizza slices, lemonade stands, cricket, whatever fits), but stay accurate — simplifying is fine, being wrong is not.

## Series

Working titles below — these are strong defaults, not locked in; swap freely if a better one comes to mind while writing.

- **Jargon, Decoded** *(alt: "The Ratio Files")* — one financial term or ratio per post: P/E, P/B, ROE, ROCE, debt-to-equity, EV/EBITDA, etc. Short, glossary-style, heavily cross-linked from the other series (e.g. the Fundamental Analysis DCF post links out to the jargon post on WACC instead of re-explaining it).
- **Fundamental Analysis — Beginner to Expert** — reading financial statements (balance sheet, income statement, cash flow) → key ratios → valuation basics (DCF, comparables). Includes a Google Sheet DCF calculator.
- **Technical Analysis — Zero to Hero** — candlesticks, support/resistance, trend lines, moving averages, RSI, MACD, volume, chart patterns → closes with an honest post on TA's limitations. Includes a Python/pandas charting notebook.
- **Mutual Funds, Minus the Marketing** *(alt: "Evaluating Mutual Funds")* — rolling returns, expense ratios, relative strength vs. category, drawdown/volatility, SIP timing myths, Sharpe ratio, reading a factsheet. Includes rolling-returns and SIP/XIRR calculators.
- **The Tax Side of Investing** — how capital gains, dividends, losses, ESOPs, buybacks, F&O and foreign assets are taxed in India. Mechanics first, worked examples on real fund data. Highest-stakes series for accuracy — see "Rules, regulations and tax" below.
- **Risk, Leverage and Your Own Brain** — what SEBI's F&O studies show, the arithmetic of losses, position sizing, leverage, diversification, sequence risk, behavioural biases. Descriptive, never prescriptive: sizing rules are "conventions from the trading literature", not recommended settings.

The canonical list, with slugs and planned post counts, is `_data/series.yml`; a post's `series:` front matter must match a slug there.

Within a series, order posts so each one can link back to earlier ones instead of re-deriving prerequisites (e.g. the ROCE jargon post should exist before the DCF post cites it).

**Don't hard-code series structure in prose.** Series grow: the review found "the next nine posts", "the final post in this series", "it closes the series", "seven of the nine posts" and "Fifty-nine posts on this blog" all gone stale. Say "the limitations post" or "later in this series", not a count or "final".

### The Desi Bites case study

Desi Bites Foods is **fictional**, used so every ratio can be shown on one consistent set of books. Its facts live in `_data/case_study.yml` and `_data/case_study_2.yml` (generated by `scripts/build_case_study_2.py`) — never restate them from memory. Fixed points: listed on the **NSE and BSE main board** (illustrative — its size is below real main-board thresholds, which is fine for teaching); DRHP filed December 2024, RHP June 2025 carrying FY25 accounts, listed 15 June 2025; main-board rules apply (quarterly results, ICDR lock-ins and issue-object caps). If a new post needs a new Desi Bites fact, add it to the data/script so every post agrees.

## Calculators and code

Google Sheet calculators and Python/pandas snippets are woven in **where the topic naturally needs one** — not stapled onto every post. A jargon post on P/E doesn't need a notebook. A DCF or rolling-returns post does. When you add one:

- Link a Google Sheet (view-only, "make a copy to use") for anything a reader should be able to use without coding.
- Use a Python/pandas snippet or notebook when the point is showing *how* the calculation works, not just letting readers plug in numbers (e.g. the TA charting series).
- Keep code snippets short and copy-pasteable; a reader should be able to lift 10–20 lines and run them, not clone a repo.

## Twitter

Twitter is a distribution channel, not a second content stream. Don't write threads that duplicate a post's content — write a short hook (often the post's takeaway line) plus a link. This is also why the "takeaway" section of every post should be able to stand alone as a tweet.

## Accuracy rules (learned the hard way)

A full review of all 116 posts in September 2026 (`_review/REVIEW-2026-09-24.md`) found the arithmetic almost always right and the **interpretation** often wrong. Most errors were a sentence saying more than its own table showed. Before publishing, check every interpretive sentence against the numbers beside it.

- **Compare like with like.** Pre-tax vs post-tax (ROCE is pre-tax; ROE and WACC are post-tax — compare ROCE × (1 − t)). Same book (P/B = P/E × ROE only on the same equity; post-IPO book is mostly IPO cash). Same period and plan. Price index vs total-return index (say which; price-only returns understate).
- **No hindsight endpoints.** Measure "what happened next" over a fixed horizon (e.g. 63 sessions), never "to the later peak/trough". Don't count an event whose forward window is incomplete, and say how many were dropped and why.
- **Claims must survive the base rate.** "90% of repeat losers lost again" proves nothing if 88% of everyone lost.
- **Describe the whole table.** If the heading says "every fall of more than 15%", the table must contain every one — including one still unrecovered at the data's end.
- **Directions and signs.** Check that "rose/fell", "above/below", "same/opposite direction" and "who wins" match the data. Reversed claims were the most common P0.
- **Use terms in their exact accounting/market sense.** "Diluted EPS" means Ind AS 33 potential shares, not "after the IPO" (we say pre-issue / post-issue EPS). Tracking *error* is a standard deviation; tracking *difference* is the drag. Macaulay ≠ modified duration. Volatility clustering means quiet follows quiet.
- **Rounding shown must reproduce.** If a formula displays 13.91%, the table beside it must compute from 13.91% (or display the unrounded rate). A reader recomputing your example should get your answer.
- **Numbers come from `_data/`, never typed into prose.** Every figure in a post should be a Liquid value from a data file, generated by a script in `scripts/` where one exists (re-run the script, don't hand-edit its output). Hard-coded prose numbers ("projected ₹5,289", "20-day-faster", "nearly eight months") went stale in several posts. When a script derives a table, assert its invariants (a balance sheet's two sides sum; shares are computed on non-missing data).
- **Unsourced claims about the world** ("one of the most robust findings", "flows reliably peak at highs", "the ratio agencies reach for first") need a citation you're sure exists, or an honest "in our view". Never invent a citation.

## Rules, regulations and tax

- **State the as-of date and cite the primary source** for every rule, rate, threshold or limit: circular/notification number and date (sebi.gov.in, rbi.org.in, incometaxindia.gov.in, the Finance Act text). Secondary summaries (news, broker blogs, law-firm notes) are acceptable only when labelled and when a primary source genuinely can't be reached — record it in TODO.md as VERIFY.
- **Never state a rule from memory.** Rules changed a lot in 2024–26 (debt-fund indexation gone for sales from 23 July 2024; "specified mutual fund" redefined as >65% debt from FY 2025-26; STT raised from 1 April 2026; SGB exemption narrowed; the Income-tax Act, 2025 renumbered sections and replaced PY/AY with "Tax Year"; SEBI MF Regulations 2026; SEBI category revisions Feb 2026). If you can't confirm the current position, soften to what is certain and say "check the current rule".
- Tax posts use "Tax Year 2026-27 (FY 2026-27)" style, apply 4% cess consistently (or say it's excluded), mention surcharge where it could change the answer, and name the example fund and data source. Every tax post needs a read by someone who files professionally before it goes out (tracked in TODO.md).

## Style conventions

- Currency: ₹, with commas per Indian numbering (₹12,34,567, not ₹1,234,567). Table cells that are pure numbers get Indian grouping automatically (`_includes/inr-tables.html`); for numbers in prose use `{% include inr.html n=… %}`. Don't show false precision — no trailing ".0" on whole rupees or percentages.
- Negative numbers: use "−" (U+2212) in prose, and avoid double negatives — "fell 59.7%", not "fell -59.7%"; show losses as "−₹6,000", not "₹-6,000".
- Dates: explicit and unambiguous. In prose write "3 October 2024" or "March 2026"; ISO dates (2024-10-03) are fine in tables and code, not in sentences.
- Headers: sentence case, not title case — and running text too ("capex intensity", not "Capex Intensity").
- Prefer tables for ratio comparisons, formula reference sheets, and "X vs Y" breakdowns.
- Cite data sources (screener.in, NSE/BSE, AMFI, fund factsheets, company filings) inline where a figure is used. For index data prefer NSE Indices/niftyindices.com over Yahoo Finance where available.

## File conventions (Jekyll)

- Posts live in `_posts/`, named `YYYY-MM-DD-slug.markdown`. Posts publish on their date via a daily rebuild (`future: false`).
- Front matter: `title`, `date`, `series` (a slug from `_data/series.yml`), `description` (140–160 characters — it feeds the homepage, meta description and RSS), `image` (an OG card in `assets/og/`, made with `scripts/make_og_cards.py`), and `term` for glossary posts.
- **`{% post_url %}` may only point to a post dated on or before the linking post.** A link to a future post fails the whole build on the day the linking post publishes.
- **Never start a line with a number or a Liquid value followed by ". "** in the middle of a paragraph (`48. That's…`, `2030. It carries…`) — kramdown turns it into a list item and the sentence breaks. Reflow the line.
- The disclaimer, table-of-contents, series navigation and number formatting are shared includes in `_includes/`; don't paste boilerplate into posts.
- Before scheduling a post: run `python3 scripts/check_posts.py` (must report 0 errors) and build with future posts included (`bundle exec jekyll build --future`) to catch Liquid and link errors, then read the rendered page.
