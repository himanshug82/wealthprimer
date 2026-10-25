# Primary sources and reachability

Reachability was tested from the cloud sandbox (egress proxy). Re-test if something changes; sites sometimes reset TLS on the first try, and `fetch_source.py` retries.

| Source | Use for | Reachable? | Notes |
|---|---|---|---|
| sebi.gov.in (circulars, master circulars, regulations) | MF rules, TER, categorisation, disclosures, F&O studies | Yes, via `fetch_source.py get` (PDF) | Master Circular for Mutual Funds, 20 March 2026, number HO/24/13/11(1)2026-IMD-POD-1/I/7602/2026. Para 11.2.4(a) TER formula; 5.6.5; 6.7.3 |
| rbi.org.in | Liquid/money-market context, SGB, repo | Try; HTML often fine | |
| incometaxindia.gov.in / Income-tax Act, 2025 text | Rates, sections, Tax Year | Try; large PDFs | Section numbers were renumbered: open the text, never guess |
| amfiindia.com | AMFI categories, NAV, scheme data | Partly | Prefer fund-house factsheets for per-scheme facts |
| niftyindices.com | Index methodology, TRI series | POST endpoint works for data; methodology PDFs via `get` | ≤1 year per request for TRI |
| mfapi.in | Scheme NAV history | Yes | Not a regulator; use for data, not rules |
| nseindia.com | Market data, circulars | Often blocks scripted access | Use niftyindices for index data |

## Citation format

`<Issuer> <document title>, <number>, <date>, <para/section/page>` — e.g. *SEBI Master Circular for Mutual Funds, HO/24/13/11(1)2026-IMD-POD-1/I/7602/2026, 20 March 2026, para 11.2.4(a)*.

## When a source can't be reached

Soften the sentence, add "check the current rule", log a `VERIFY` row in `TODO.md` with the source you wanted and why it failed. Secondary summaries are allowed only if labelled as such in the post.
