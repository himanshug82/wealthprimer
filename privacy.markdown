---
layout: page
title: Privacy & Disclaimer
nav_title: "Privacy"   # short label for the header nav; `title` stays the page H1
permalink: /privacy/
---

## Disclaimer

Wealth Primer is an educational blog. Every post teaches a concept, ratio, or
technique — none of it is a recommendation to buy, sell, or hold any specific
stock, fund, or security, and none of it is personalized advice. The author
is not a SEBI-registered Research Analyst or Investment Adviser. Where posts
use real companies or funds as worked examples, prices and figures are
historical (at least three months old, per SEBI's guidance for educational
content) and used only to illustrate a calculation. Past performance does not
guarantee future results. Please do your own research, or consult a
SEBI-registered adviser, before making investment decisions.

## Privacy

This site does not require you to create an account or submit personal
information to read it.

{% assign has_ga = false %}{% if site.google_analytics and site.google_analytics != '' %}{% assign has_ga = true %}{% endif %}
{% assign has_gc = false %}{% if site.goatcounter and site.goatcounter != '' %}{% assign has_gc = true %}{% endif %}
{% assign has_comments = false %}{% if site.giscus.repo_id != '' and site.giscus.category_id != '' %}{% assign has_comments = true %}{% endif %}
{% assign has_list = false %}{% if site.newsletter.action and site.newsletter.action != '' %}{% assign has_list = true %}{% endif %}
{% if has_ga %}
- **Analytics**: this site uses [Google Analytics 4](https://marketingplatform.google.com/about/analytics/)
  to count visits and see which posts are read. It records the page visited,
  the referring site, rough location (IP addresses are anonymised by Google
  before storage), device and browser type, and time on page. Google Signals
  and ads personalisation are switched **off**, so visits here are not used to
  build advertising profiles. Google's
  [privacy policy](https://policies.google.com/privacy) and its page on
  [how Google uses data from sites that use its services](https://policies.google.com/technologies/partner-sites)
  have the detail. You can block it with any content blocker or with Google's
  [opt-out browser add-on](https://tools.google.com/dlpage/gaoptout).
{% endif %}{% if has_gc %}
- **Pageview counter**: this site also uses [GoatCounter](https://www.goatcounter.com/),
  a privacy-focused counter. It records the page visited, the referring site,
  and rough browser and country information. It sets **no cookies**, does not
  track you across other websites, and does not store data that identifies
  you personally. GoatCounter's own
  [privacy policy](https://www.goatcounter.com/help/privacy) has the detail.
{% endif %}{% if has_ga == false and has_gc == false %}
- **Analytics**: none. No analytics or measurement tool runs on this site, so
  no visit-level data is collected by Wealth Primer.
{% endif %}{% if has_ga %}
- **Cookies**: Google Analytics sets first-party cookies (named `_ga` and
  `_ga_…`) that hold a random identifier so repeat visits from the same
  browser can be counted as one visitor. They contain no personal
  information. Wealth Primer itself sets no other cookies. Clear or block
  cookies in your browser and the site works exactly the same.
{% else %}
- **Cookies**: none. Wealth Primer sets no cookies of its own.
{% endif %}
{% assign third_parties = "" | split: "" %}
{% if has_ga %}{% assign third_parties = third_parties | push: "the Google Analytics script (from googletagmanager.com)" %}{% endif %}
{% if has_gc %}{% assign third_parties = third_parties | push: "the GoatCounter script (from gc.zgo.at)" %}{% endif %}
{% if has_comments %}{% assign third_parties = third_parties | push: "the comments widget on post pages (from giscus.app)" %}{% endif %}
{% if third_parties.size > 0 %}
- **Third-party content**: the only resources loaded from outside this
  domain are {{ third_parties | join: "; " }}. Apart from those, pages load no
  external fonts, scripts, trackers, embeds or ad tags.
{% else %}
- **Third-party content**: none. Pages load no external fonts, scripts,
  trackers, embeds or ad tags — everything a page needs is served from this
  domain.
{% endif %}
- **Links out**: links to source documents (company filings, AMFI, exchange
  data) are ordinary links; following one takes you to that site under its own
  policy.
- **Advertising**: none. There are no ads on this site.
{% if has_comments %}
- **Comments**: post pages carry a comment box powered by
  [giscus](https://giscus.app), which stores comments as
  [GitHub Discussions](https://docs.github.com/en/discussions) on this
  site's public code repository. To comment you sign in with a GitHub
  account; giscus then acts on your behalf under
  [GitHub's Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
  and [giscus's own policy](https://github.com/giscus/giscus/blob/main/PRIVACY-POLICY.md).
  Comments are public, attached to your GitHub username, and can be deleted
  by you at any time from GitHub. Reading a post without commenting sends
  nothing to giscus beyond loading the widget. Comments that ask for or offer
  stock tips, price targets or "should I buy X" are removed — this is an
  educational site.
{% else %}
- **Comments**: none. There is no comment system, so nothing is collected
  through one.
{% endif %}
{% if has_list %}
- **Email list**: if you subscribe, the address you enter is stored by
  {% if site.newsletter.provider == 'buttondown' %}[Buttondown](https://buttondown.com/legal/privacy){% else %}[Mailchimp](https://www.intuit.com/privacy/statement/){% endif %},
  which runs the list, and is used only to send new posts. It is never sold or
  shared, and every email carries a one-click unsubscribe link that removes you
  immediately. The signup form posts directly to the provider — no signup
  script or tracking pixel runs on this site.
{% else %}
- **Email**: there is no mailing list. If you write to the address below, your
  message sits in an ordinary mailbox and isn't added to any list.
{% endif %}
- **Server logs**: this site is hosted on GitHub Pages, which — like any web
  host — receives and may log standard request data such as your IP address
  and browser user-agent in the course of serving the page. That processing
  is GitHub's, under
  [GitHub's Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement).

<!--
MAINTENANCE: the analytics, cookie, third-party, comments and email bullets
above are CONDITIONAL on the same _config.yml keys that switch the features on
(`google_analytics:`, `goatcounter:`, `giscus.repo_id`/`category_id`, and
`newsletter.action`). Turn a feature on and its disclosure turns on with it —
the two cannot silently disagree, which is the failure mode this page most
needs to avoid.

Anything NOT driven by a config key is still asserted as plain fact: no ads, no
other third-party resources. If you add an ad network, an embedded font or a
CDN script, edit this list in the SAME commit. The GA4 bullet also asserts that
Google Signals / ads personalisation are OFF — that is set in
_includes/analytics.html; if you ever turn them on, change this page too.
-->

## Contact

Questions about this policy? Reach out at himanshu.direct@gmail.com.
