# Source PDFs for blocked posts

Drop the filing PDFs here (keep the original file names). The cloud session cannot fetch them:
NSE's archive refuses plain requests, company sites return 403/404, and getting past NSE's bot check
with a spoofed browser header is not allowed. Once a file is here, the post can be drafted with every
figure going into `scripts/derive_sectors*.py` → `_data/`.

| Post (date) | Files needed |
|---|---|
| `hotels-arr-occupancy-revpar` (slot to be chosen; 2 Nov is now Tax) | IHCL FY26 results filing of 11 May 2026 (NSE INDHOTEL / BSE 500850): press release + investor presentation |
| `real-estate-presales-vs-revenue` (8 Dec) | Godrej Properties FY26 (Q4) press release + investor presentation; Ind AS 115 text (MCA) for the revenue-recognition point |
| `capital-goods-order-book-book-to-bill` (9 Dec) | Larsen & Toubro Q4 FY26 press release + investor presentation |
| `general-insurers-combined-ratio-solvency` (10 Dec) | ICICI Lombard 15 Apr 2026 filing `ICICIGI_15042026193418_IP.pdf` (NSE); IRDAI regulation that sets the minimum solvency ratio (Assets, Liabilities and Solvency Margin regulations, current text) |
| `epf-how-it-works` (MBM, 12 Nov slot) | EPF Scheme, 1952 (contributions, para 60 interest, withdrawals); EPFO circular notifying the FY 2025-26 rate; EPFO table of declared rates |

PDFs here are working sources, not site content: `_review/` starts with an underscore, so Jekyll does not publish it.
