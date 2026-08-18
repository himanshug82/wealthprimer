# Wealth Primer — CLAUDE.md

Wealth Primer is a financial education blog for Indian retail investors. It **teaches concepts — it does not give stock tips, predictions, or personalized advice.** Every writing decision in this repo should protect that line, because it's both the legal position (no SEBI Research Analyst / Investment Adviser registration needed) and the brand ("credibility-first").

Read this before drafting, editing, or reviewing any post.

## Who we're writing for

Readers range from someone who has never opened a balance sheet to someone who already trades and wants sharper technique. A single post should not try to serve both extremes in its main body — that's what the optional "explain it like a kid" section (below) is for. Default to writing for an intelligent beginner, and layer complexity in as the post progresses.

## Voice

Friendly, plain-spoken, a little informal — like a sharp friend explaining this over coffee, not a textbook and not a finfluencer hyping a trade. Concretely:

- Short sentences. Contractions are fine ("you'll", "it's").
- Define every acronym on first use in a post, even ones that feel obvious (P/E, ROCE, RSI). If a **Jargon, Decoded** post (or any other existing post) already explains that acronym with an example, link to it right at first use instead of re-explaining from scratch — a short inline definition plus the link is fine, but the link is mandatory when a post exists. If no post explaining it exists yet, define it inline as usual and add a TODO/note that a glossary post for it is still owed.
- Use Indian context by default: ₹, NSE/BSE-listed companies, Indian mutual funds, Indian financial-year conventions.
- It's fine to have a point of view (e.g. "TA alone won't tell you if a company is a fraud") as long as it's framed as an opinion/limitation, not a trade call.
- Avoid hype words: "guaranteed," "sure-shot," "multibagger," "can't lose." These are also compliance red flags, not just bad writing.
- Humor is welcome if it doesn't undercut clarity.

## Compliance guardrails (non-negotiable)

The whole reason this blog doesn't need RA/IA registration is that it stays educational. Every post must:

1. **Never recommend a specific transaction.** No "buy X," "sell Y," "target price ₹Z," no implied calls. Naming real companies to *illustrate* a concept (e.g. "here's how to compute Infosys's ROCE from its FY24 balance sheet") is fine; framing that as a signal to act on is not.
2. **Use lagged data in worked examples.** Any price, chart, or figure used as a worked example must be at least 3 months old at time of publishing (SEBI's rule for educational content). State the as-of date explicitly, e.g. "prices as of March 2026, used for illustration only." This is not optional — check the date on every chart/table before publishing.
3. **Carry a disclaimer.** Every post ends with a short, consistent disclaimer: educational content only, not investment advice, author is not a SEBI-registered RA/IA, past performance ≠ future results. Keep the wording identical across posts (a shared Jekyll include is worth setting up once this repo has more than a couple of posts) so it reads as a standing policy, not a legal afterthought.
4. **Frame mistakes/limitations honestly.** Especially in the TA series — end it with an honest reckoning of what technical analysis can't do. Credibility comes from admitting limits, not from every post ending on "and that's why this indicator wins."

## The post template

Every post in the three learning series (jargon glossary is the exception — see below) follows this structure:

1. **Definition** — what is this concept, in one or two tight paragraphs.
2. **Formula** — the actual formula/calculation, shown clearly (use a code block or table, not prose, for the math itself).
3. **Worked example** — a real, numbered walkthrough using 3-month-lagged price/financial data, with the as-of date stated.
4. **Common mistakes** — 2–4 ways beginners misread or misapply this concept. This section is a big part of what makes the blog worth reading over a generic explainer, so don't skip it or phone it in.
5. **Takeaway** — a 2–3 sentence summary, written to be quotable/tweetable on its own (see Twitter section below).

Glossary-series posts (jargon/ratios) can be shorter — definition → formula → one small worked example → takeaway — since "common mistakes" often collapses into the definition for a single-ratio explainer. Use judgment; don't pad.

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

Within a series, order posts so each one can link back to earlier ones instead of re-deriving prerequisites (e.g. the ROCE jargon post should exist before the DCF post cites it).

## Calculators and code

Google Sheet calculators and Python/pandas snippets are woven in **where the topic naturally needs one** — not stapled onto every post. A jargon post on P/E doesn't need a notebook. A DCF or rolling-returns post does. When you add one:

- Link a Google Sheet (view-only, "make a copy to use") for anything a reader should be able to use without coding.
- Use a Python/pandas snippet or notebook when the point is showing *how* the calculation works, not just letting readers plug in numbers (e.g. the TA charting series).
- Keep code snippets short and copy-pasteable; a reader should be able to lift 10–20 lines and run them, not clone a repo.

## Twitter

Twitter is a distribution channel, not a second content stream. Don't write threads that duplicate a post's content — write a short hook (often the post's takeaway line) plus a link. This is also why the "takeaway" section of every post should be able to stand alone as a tweet.

## Style conventions

- Currency: ₹, with commas per Indian numbering (₹12,34,567, not ₹1,234,567).
- Dates in examples: explicit and unambiguous ("March 2026," not "3/4/26").
- Headers: sentence case, not title case.
- Prefer tables for ratio comparisons, formula reference sheets, and "X vs Y" breakdowns.
- Cite data sources (screener.in, NSE/BSE, AMFI, fund factsheets, etc.) inline where a figure is used.

## File conventions (Jekyll)

- Posts live in `_posts/`, named `YYYY-MM-DD-slug.markdown`.
- Front matter should include `title`, `date`, and a `series`/`category` field identifying which of the four tracks the post belongs to, so series can be listed/filtered later.
- Keep the disclaimer and any shared boilerplate in a Jekyll `_includes/` partial once there's more than one post using it, rather than pasting it manually each time.
