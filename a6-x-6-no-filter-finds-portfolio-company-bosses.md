# A6.x.6 · No filter finds portfolio-company bosses

> A6 · Talent Active / Passive → A6.x · Edge cases

**No filter finds bosses of companies a fund owns.** These are the people in **group C** — the CEO or CFO of a business a PE fund has bought. The box that ought to find them, *Corporate / Industry → PE-Backed / Portfolio Company*, is **attached to nobody at all**: zero people on production and on UAT.

Re-checked 29 Jul 2026 — still zero, and the problem is wider than one box. The whole *Corporate / Industry* branch is essentially unpopulated:

| Box | People, all statuses |
|---|---:|
| PE-Backed / Portfolio Company | **0** |
| Large Cap (>$10B) | **0** |
| Mid Cap ($1B–$10B) | **0** |
| Small Cap / SME | 2 |

So group C **and** group D are both invisible on the chip.

**Group C is therefore out of reach from the chip, and out of scope for now.** [List 2](a6-b-2-title-and-background.md) still tells you to tick the *PE-Backed / Portfolio Company* box — it is the right box, it just returns nobody yet, and it will start working the day the data is fixed.

There is a possible way round it — the **Work Experience** filter with *company type = Portfolio* and *Currently* — but it is **not part of the flow**. A trial run showed the flag is too noisy to act on ([A6.x.8](a6-x-8-a-company-can-be-tagged-wrongly.md)): it currently tags *FTI Consulting*, *Accenture*, *Valcon* and even the literal strings *Self-Employed* and *Independent Consultant* as portfolio companies. Notes in `plans/reports/`.
