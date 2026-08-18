Still needs your input

- Domain: CNAME and _config.yml both say dummynotes.com — is that your real, registered domain, or a placeholder that needs replacing? Everything (sitemap, canonical URLs, OG tags, future ads.txt) derives from this.
- Twitter/X handle and author name — for the _config.yml TODOs (social meta tags, byline).
- Contact email — for the privacy page.

Lower-priority, not done (say the word if you want these next)

- Favicon (currently none).
- Series index pages — I added _data/series.yml (the four series, titles, slugs) as a source of truth, but there's no /series/fundamental-analysis/ listing page yet.
- Analytics (GA4/Plausible/GoatCounter) — not added, your call which one.
- Formula rendering (MathJax/KaTeX) if you want real math notation rather than code-block formulas.
- Minor: minima's bundled SCSS throws harmless Dart-Sass deprecation warnings during build (lighten() is deprecated) — cosmetic build noise, not a bug, will resolve itself on minima's next release.