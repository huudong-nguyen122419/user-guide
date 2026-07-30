# A6-B.3 · Sub-rule 2 — the employer check

> A6-B · Identify PASSIVE talent

A TIER 2 title cannot settle anything on its own. A *Vice President* at a fund is a client; a *Vice President* at an investment bank is supply. **The employer decides.**

Only [A6-B.2](a6-b-2-title-and-background.md) TIER 2 rows reach this page. TIER 1 skips it by design.

## The order

Each gate ends the check. The description is only read at step 4 — and on production only **8 of 133** people ever get that far.

```
1. Does the title carry a company name?
     NO  → needs a human read                        [6 people]
2. Find that company among the ONGOING work experience rows
     NOT FOUND → needs a human read                  [3 people]
     (this includes "found, but only on a closed row")
3. Does the company NAME contain a service word?
     (advisory · consulting · advisor · law …)
     YES → service provider, not a client            [6 people]
4. ►► READ THE DESCRIPTION ◄◄  (mainActivities of that ongoing row)
     a. self-describes as a service provider → not a client
     b. buy-side words                       → CLIENT
     c. any other service word               → not a client
5. No description → check linkedCompany tags → otherwise a human read   [2 people]
```

## Step 2 — ongoing rows only

A closed row describes a **past** employer and cannot settle who somebody works for today.

> **Yassir — "Managing Director at Torch Partners".** The Torch Partners row is `ongoing = false`. His current role is *Y Advisory — self-employed corporate finance advisor*. Reading the closed row would have made him a client; reading the ongoing one does not.

## Step 3 — the company name is evidence

Cheaper and more reliable than the description, and it works when there is no description at all. *Victoria Advisory*, *N-Squared Advisory*, *Borromeo Mondino Advisory GmbH*, *Array Capital \| Software M&A Advisory* are all settled by their names.

## Step 4 — service identity is read BEFORE the buy-side words

This ordering is the whole point of the step, and it is counter-intuitive.

**"Private equity" in a description usually names the company's CLIENTS, not the company itself.** An advisory firm's description is full of buy-side vocabulary precisely because it serves buy-side firms.

| Company | Description says | Correct reading |
|---|---|---|
| N-Squared Advisory | *"Co-founded a **boutique advisory firm**, focusing on **investment banking mandates** … leverage deep investor relationships (from large-cap **Private Equity** to seed-stage **Venture Capital**)"* | PE/VC are relationships. The firm is an advisory boutique → **not a client** |
| Borromeo Mondino Advisory | *"**Independent senior advisor** … working with Asset Owners, **Asset Managers** … as well as with **their** portfolio companies"* | "their" names the clients → **not a client** |
| CAPX | *"an algorithmic corporate financing **platform that connects** borrowers and **private equity sponsors** with institutional capital providers"* | a fintech marketplace; PE sponsors are users → **not a client** |

With the buy-side words read first, all three came out as clients. Reading service identity first drops all three correctly.

### Word lists

**Service identity** — what the company *is*:
`advisory firm` · `boutique advisory` · `advisory boutique` · `advisor` · `adviser` · `advising` · `advises` · `consultancy` · `consulting firm` · `consultant` · `investment banking mandates` · `corporate finance advisor` · `self-employed` · `freelance` · `platform that connects` · `our clients` · `for clients` · `client engagements` · `mandates` · `interim management` · `law firm` · `recruitment` · `executive search`

**Buy-side**:
`private equity` · `venture capital` · `buyout` · `buy-out` · `LBO` · `sponsor` · `investment firm` · `alternative asset` · `asset manager` · `family office` · `growth equity` · `investment fund` · `fund manager` · `portfolio companies` · `principal investing`

> **`financial services` is deliberately absent.** A PE fund *is* a financial services firm — keeping that term in the service list would release exactly the people the branch exists to catch.

## Step 5 — missing evidence is never confirmation

A title with no company, an employer that is not in the ongoing work experience, an empty description, a description that reads either way — all go to **needs a human read**. None of them is treated as a match.

This matters more than it looks: roughly **63%** of talents have a current employer that was never matched to the company list ([A6.x.5](a6-x-5-employer-missing-from-the-company-list.md)), so the no-data path is the common one, not the exception.

The `linkedCompany.isSponsor` / `isPortfolio` tags are used only as a last resort, and flagged as low confidence when they are — the tags come from an outside source and are wrong often enough to matter ([A6.x.8](a6-x-8-a-company-can-be-tagged-wrongly.md)).

## What it produced on production

25 TIER 2 rows in, and the description was actually read for 8 of them.

| Outcome | Count |
|---|---:|
| Not a client — employer is a service provider | 9 |
| **Client — employer confirmed buy-side** | **3** |
| Needs a human read | 13 |

| Where the check stopped | Count |
|---|---:|
| Description read, verdict reached | 6 |
| Description read, inconclusive | 2 |
| Row matched but description empty | 2 |
| Company name settled it, description never read | 6 |
| Title had no company name | 6 |
| Company not on an ongoing row | 3 |
