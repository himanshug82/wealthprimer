---
layout: page
title: Privacy & Disclaimer
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

{% assign has_analytics = false %}{% if site.goatcounter and site.goatcounter != '' %}{% assign has_analytics = true %}{% endif %}
{% assign has_list = false %}{% if site.newsletter.action and site.newsletter.action != '' %}{% assign has_list = true %}{% endif %}
{% if has_analytics %}
- **Analytics**: this site uses [GoatCounter](https://www.goatcounter.com/),
  a privacy-focused analytics tool. It records the page visited, the referring
  site, and rough browser and country information. It sets **no cookies**, does
  not track you across other websites, and does not collect or store data that
  identifies you personally. GoatCounter's own
  [privacy policy](https://www.goatcounter.com/help/privacy) has the detail.
- **Cookies**: none. Neither Wealth Primer nor its analytics sets any cookie.
- **Third-party content**: the analytics script above is loaded from
  GoatCounter. Apart from that, pages load no external fonts, scripts,
  trackers, embeds or ad tags.
{% else %}
- **Analytics**: none. No analytics or measurement tool runs on this site, so
  no visit-level data is collected by Wealth Primer.
- **Cookies**: none. Wealth Primer sets no cookies of its own.
- **Third-party content**: none. Pages load no external fonts, scripts,
  trackers, embeds or ad tags — everything a page needs is served from this
  domain.
{% endif %}
- **Links out**: links to source documents (company filings, AMFI, exchange
  data) are ordinary links; following one takes you to that site under its own
  policy.
- **Advertising**: none. There are no ads on this site.
- **Comments**: none. There is no comment system, so nothing is collected
  through one.
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
MAINTENANCE: the analytics, cookie, third-party and email bullets above are
CONDITIONAL on the same _config.yml keys that switch the features on
(`goatcounter:` and `newsletter.action`). Turn a feature on and its disclosure
turns on with it — the two cannot silently disagree, which is the failure mode
this page most needs to avoid.

Anything NOT driven by a config key is still asserted as plain fact: no ads, no
comments, no other third-party resources. If you add an ad network, a comment
system, an embedded font or a CDN script, edit this list in the SAME commit.
-->

## Contact

Questions about this policy? Reach out at himanshu.direct@gmail.com.
