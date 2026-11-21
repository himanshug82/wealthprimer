# UX assessment — Sprint 1

21 November 2026. Local build viewed at 375 × 812 (phone) and desktop width; behaviour cross-checked with GA4 (1 Aug – 20 Nov 2026). **[V]** verified, **[H]** hypothesis. No design changes made.

## Verdict

The pages themselves are clean, fast and readable: good typography, generous spacing, accessible (Lighthouse accessibility 100), tables that scroll on phones, a table of contents, a takeaway card, prev/next and related reading on every post. The weakness is **navigation between pages**: the site is organised by how it was written (series of concepts), not by what a visitor came to do. The brief's "reference library" diagnosis holds for the structure, not the page design.

## What a first-time visitor sees

### Homepage [V]

Order: hero → "Start here" (8 series cards) → latest 8 posts → newsletter.

- On a phone the hero fills the whole first screen; the first content link is below the fold. The hero says *what kind* of site this is ("Financial concepts, one at a time") but not *what problem it solves*.
- The two calls to action are "Start with the basics" (→ Jargon series) and "Browse the glossary". Nothing points to the calculators, the Desi Bites case study or the methodology, which are the strongest differentiators.
- The series cards' "start with" line reads the first post of each series by date. For *Fundamental Analysis — Beginner to Expert* it says **"start with 'DuPont'"**, because the true beginner posts (reading a balance sheet, income statement, cash flow statement) are filed under *Jargon, Decoded*. A beginner following the series as labelled starts at an intermediate post.
- "Latest posts" makes the homepage a feed; with one post every two days, the content below the series cards changes constantly while the top stays the same.

### Navigation [V]

Series · Glossary · Tools · Case study · Methodology · About. CSS-only menu on phones (works without JavaScript; checked). There is **no site search**. With 157 published posts (216 written) and many readers arriving with a term in mind, search or an A–Z entry point matters; the Glossary page partly fills this.

### Post page [V]

Series line ("Fundamental Analysis — Beginner to Expert · Part 17 of 43") → H1 → date and read time → on-this-page list → body → takeaway card → prev/next in series → three related-reading cards → newsletter box → disclaimer → comments.

- Strong: the reading experience. Body serif at a comfortable size, tables wrapped for horizontal scroll, Indian number formatting, takeaway styled as a card.
- On phones the series pill and "· Part 17 of 43" wrap onto two lines and the pill pushes the part number to the right edge; minor.
- "Part 17 of 43" is honest but signals a long commitment to someone who arrived from search for one term. A reader from Google rarely wants part 17 [H].
- The end of the post offers three kinds of next step (series next, related reading, newsletter) before the disclaimer. Clear, but every next step is "read another article"; none is "use the tool for this" unless the post includes a tool callout.

### Tool pages [V]

`/tools/sip-xirr/`: eyebrow, H1, one-line description, a callout "Open the Google Sheet" with "make a copy" instructions and the prefill source. Three of the eight tools (rolling returns, SIP/XIRR, DCF) are Google Sheets, so the visitor leaves the site to use them; the five on-page calculators work in place. The Sheet-based tools are exactly the ones with search demand (see technical SEO audit, §5).

## Behaviour data (GA4) [V, small sample]

- 297 page views, 190 users, **0 returning users** recorded, 1 Aug – 20 Nov 2026.
- `/` takes 51% of views. Next: `/2026/10/25/step-up-sips/` (26 views, 2 s average engagement — likely a bot or a single shared link [H]), `/glossary/` 15, `/case-study/` 12.
- Most users are "(not set)" or United States with 0–1 s engagement: automated traffic [H]. The 11 users from India averaged 5 min 58 s with 78% engagement; organic-search sessions averaged 2 min 19 s.
- Device split in GA4 was not read; Search Console shows desktop 449 vs mobile 239 impressions.

The sample is too small to judge journeys; treat this section as a baseline, not evidence.

## Accessibility [V]

Lighthouse accessibility 100 on the three page types. Landmarks and `aria-label` on navigation, `aria-current` on the active nav item, visually hidden labels on empty table headers, alt text on every image, no layout shift. Not tested: keyboard-only walk-through of the on-page calculators, screen reader reading of large tables, colour contrast in the chart SVGs.

## Problems, ranked

| # | Problem | Evidence | Impact |
|---|---|---|---|
| U1 | Structure by series, not by reader goal | Nav and homepage are series-first; beginner FA path lives in Jargon | High |
| U2 | Differentiators are hidden | Case study, methodology, calculators get no homepage placement; tools hub is one nav item | High |
| U3 | Highest-demand calculators are off-site Sheets | Rolling returns, SIP/XIRR, DCF | Medium–high |
| U4 | No search | 216 posts, term-driven visitors | Medium |
| U5 | Homepage hero uses the whole phone screen with no content visible | 375 × 812 screenshot | Medium |
| U6 | Posts reached from search present themselves as "Part N of M" | Post header | Low–medium |
| U7 | Newsletter offer is generic ("One email a week") | Same box on every post | Medium for list growth |

## Direction for Sprint 2 wireframes (not designs yet)

1. **Homepage** — problem-first hero sized to leave the first entry points visible on a phone; "What are you trying to do?" with 4–5 journey cards; calculators row; "How we work" (lagged data, scripts, no tips) linking methodology and the case study; newsletter; latest posts demoted to a short list.
2. **Journey/guide hub template** — ordered path through existing posts with one-line "why read this", tools for the journey, the related Desi Bites chapter, and a single "next step" — the template for the five flagship guides.
3. **Post template** — keep everything; make the series line secondary for search arrivals, add "Part of the <guide>" link, and surface the relevant tool near the top when one exists.
4. **Search** — client-side search over a generated JSON index (titles, descriptions, terms); no server or paid service.

Each needs at least two wireframe alternatives before implementation, as the brief asks.
