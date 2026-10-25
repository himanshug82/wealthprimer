# PageSpeed / Lighthouse review — 25 October 2026

Method: Lighthouse (the engine behind PageSpeed Insights), mobile profile (emulated phone, slow 4G,
4× CPU slowdown) and desktop profile, run from the build environment. The shared PageSpeed API
quota was exhausted and the report page needs JavaScript, so the runs are our own; the Search
Console link shows **no field data (CrUX) yet** — the site is too new — so Google ranks on lab
data for now. Pages tested: homepage, a chart post, a table-heavy post (Step-up SIPs), the
glossary (4,900 words), factsheet, case study, methodology, About, Series, Privacy.

## Before

| | Mobile perf | Desktop perf | Accessibility | Best practices | SEO |
|---|---|---|---|---|---|
| Homepage | 81 (one noisy run; 92–95 on rerun) | 100 | 96 | 100 | 100 |
| Posts (table-heavy / charts) | 84 / 99 | 100 | 92 | 100 | 100 |
| Glossary | 95 | 100 | 95 | 100 | 100 |

Core Web Vitals in the lab were already good: CLS 0.000 everywhere, FCP ≈ 1.1 s and LCP ≈ 1.1 s
on mobile for most pages, desktop 0.3 s.

## What was wrong, and the fix

| Finding | Fix |
|---|---|
| **Accessibility 92–96** on every page: `aria-label` on the menu `<label>` (not allowed on a label) | Real visually-hidden "Menu" text instead |
| Contrast failures: the "Explain it like I'm 10" hint (4.07:1, from an `opacity: 0.8`), code strings (4.3:1), numbers (3.0:1) and comments (2.5:1) | Opacity 0.92; darker token colours (5.8, 5.3 and 4.8:1); all pass WCAG AA 4.5:1 |
| Data tables with an empty corner header cell (`td-has-header`) | The layouts give that cell hidden text "Item", so every column has a header (posts and the generic page layout) |
| Glossary jumped from `<h1>` to `<h3>` (heading-order) | Letter headings are `<h2>`, restyled to the same look |
| CSS shipped expanded (43 KB, 8.5 KB gzipped) | `sass: style: compressed` → 35 KB, 7.7 KB gzipped |

## After (same Lighthouse, local copy of the production build, gzip on)

Accessibility **100**, best practices **100**, SEO **100** on all 11 pages tested, on mobile and
desktop. Desktop performance 100 everywhere. Mobile performance 92–98 (glossary 92 and case study
93 are the heaviest pages; both are long, table-heavy documents).

## Looked at and deliberately not changed

- **Google Analytics (`gtag.js`) is the largest remaining cost** (≈180 KB, 300–600 ms of script on a
  throttled phone; it is also the whole "unused JavaScript" and "network dependency" finding).
  I tried loading it after the page is idle: the lab scores did not move (97→96, 94→93, 97→98,
  within run-to-run noise), so I did **not** ship it — it adds risk to analytics for no
  measured gain. If you want a bigger step, the option is to load GA on first interaction only;
  that would drop the lab TBT but undercount visitors who read without scrolling or tapping.
- **Render-blocking CSS (≈190 ms simulated)**: one 7.7 KB gzipped file; inlining it into every page
  would cost more than it saves for repeat views.
- **Cache lifetime of 10 minutes** on CSS/icons: GitHub Pages fixes `Cache-Control: max-age=600`
  and doesn't let a site change it. Putting the site behind a CDN (e.g. Cloudflare's free plan)
  would allow long cache headers; not needed at this size.
- **The earlier "LCP 3.9 s" on posts** is an artefact of the build environment's egress proxy
  (real headline render delay 1.16 s live versus 0.14 s on a local copy of identical code); the
  homepage's first-run 81 was a one-off. Judge the real numbers from your own PageSpeed run,
  or from Search Console's Core Web Vitals report once field data appears.
