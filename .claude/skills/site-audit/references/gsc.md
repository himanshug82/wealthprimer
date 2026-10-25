# Search Console reports: what they mean here

Only the owner can open Search Console; ask for the screenshot/export. Never report rankings, impressions or index counts you haven't seen.

| Report / status | Usually means | Action |
|---|---|---|
| **Page with redirect** | Old URL variants (http, www, trailing slash) that 301 to the canonical | Normal. Check the list holds only variants, not live pages |
| **Alternate page with proper canonical tag** | Google found a duplicate and respects our canonical | Normal |
| **Duplicate, Google chose different canonical** | Two URLs near-identical; Google picked its own | Make pages distinct or point the weaker at the stronger. Seen on /series/ |
| **Excluded by noindex** | Intentional (/404.html; a series hub with no published post) | Verify intent; a hub flips by itself when its first post is live |
| **Crawled – currently not indexed** | Google read it and chose not to index (thin, similar, or low site authority/new site) | Not an error. Improve internal links and uniqueness; request indexing for key pages; wait |
| **Discovered – currently not indexed** | Known URL, not yet crawled (crawl budget on a young site) | Sitemap + internal links; patience |
| **Soft 404 / Not found (404)** | Real problem | Fix or remove the link |
| **Breadcrumbs (Enhancements)** | Valid items should ≈ number of posts | Errors = JSON-LD issue in `_layouts/post.html` |
| **Core Web Vitals** | Field data from real users; needs traffic | Compare with local Lighthouse, not the sandbox's live run |
| **Performance → Queries** | Position 8–20 queries = refresh candidates | Use `refresh-post`; `last_modified_at` only for substantive changes |

Domain property (DNS TXT) is preferred over URL-prefix. Sitemap: `https://wealthprimer.in/sitemap.xml`.
