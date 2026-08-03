# A6-C.6 · The rule as built today

> A6 · Approve a new talent (decides Active or Passive) → A6-C · Review the In Review queue — LIVE

What the code does **right now** — five questions, and how many of them each talent actually walks. This is the behaviour to predict before clicking Approve. The rule that replaces it is [A6-C.7 ↗](a6-c-7-the-rule-rebuilt.md).

Which rule is this?**This is the system's rule — what the code does today, not what we think it should do.** It is the *current* rule, not a legacy one: verified against live production behaviour on three records on 30 Jul 2026, all three matched. **It is also known to be wrong, and is being replaced** by [A6-C.7 ↗](a6-c-7-the-rule-rebuilt.md), which has been validated on 7 live records. Read this section as *is*, that one as *will be*. **Our business rule is a different thing** — [A6-C.7 ↗](a6-c-7-the-rule-rebuilt.md): hard-stop A (junior / back office), hard-stop B (advisory / sell-side), TIER 1 / TIER 2 titles, and the employer check that reads the company **description**. **The system implements none of that.** The two disagree deliberately — the worked example below is one live record where they split.

**Five questions, walked top to bottom, first Yes ends the walk.** Fall off the bottom and you get the fallback. Only three inputs exist: the **employment status** picked at sign-up, the **position** and **company name** of the **current** work-experience rows, and whether those companies carry a **Mergermarket flag**. It never reads the profile headline, the company description, the contract history or the applications.

**One talent walks between one and five steps.** The cheapest paths cost a single field read; only the deepest touches the company flags.

| Stops at | Steps | What was read | Verdict | UAT queue 286 records |
|---|---|---|---|---|
| **Q1** Full/Part-time | **1** | one field | **PASSIVE** | 36 · 13% |
| **Q2** blank employment status | **2** | one field | ACTIVE | **76 · 27%** |
| **Q3** no current role | **3** | + count of current rows | ACTIVE | 18 · 6% |
| **Q4** freelance wording | **4** | + position & company of every current row | ACTIVE | 9 · 3% |
| **Q5** flagged company | **5** | + flag lookup on those companies | **PASSIVE** | 35 · 12% |
| **Q6** fallback | **5** | the full walk, nothing matched | ACTIVE | 112 · 39% |
| **Outcome** | **Passive 71 (25%) Active 215 (75%)** |  |  |  |

**46% of the queue never gets past step 2** — the employment-status field decides it alone.

Three things that need a decision**① 27% of the queue has no employment status.** 76 records waved to Active at step 2 without the profile ever being read. That field is never blank on the existing Active population, so this is specific to intake: people arrive before sign-up is finished. **② Q5 is in practice a corporate detector.** Of the 35 records it sent to Passive: **33 corporate · 2 portfolio · 0 sponsor** — **not one sponsor was caught**. **Ruled 30 Jul 2026: a `corporate` flag counts as flagged**, same as sponsor and portfolio, so those 33 verdicts are **correct** — an earlier version of this page called them errors, which was wrong. The sponsor and portfolio branches simply almost never fire. **③ Q4 fired only 9 times** — `independent` 6 · **`fractional` 2** · `freelance` 1 · `self-employed` 1. `remote`: zero. Two hits for `fractional` on 286 records is why it belongs in the list.

**Can it be automated without a review step?** Q1 and Q3 yes — clean field reads. **Q5 is the one that will generate overrides**, and the fix is dropping `corporate` from it, not adding a review gate. Widening Q4 is worth doing but buys precision only, never coverage: Q4 is an *exit to Active*, so a wider list only reroutes people already heading to Active.

**The full Q4 word list is not published.** `remote` and `independent` are the two the flowchart names, as examples. Treat Q4 as “the system may exit to Active for a reason you cannot see”.

## Worked example — the two rules disagreeing, on a live record

**Iman Dakhlaoui** (`iman.dakhlaoui@gmail.com`), production, approved 29 Jul 2026, currently **Passive**. 7 years’ experience, Paris, rate filled in, available for more than 40 hours a week. `employeeStatus = Freelancer` · `internalStatus = null` (no Skip Review) · one current role: position `M&A and Project Finance Associate` at `FINERGREEN`, flagged **corporate**.

**The system’s walk:** Q1 not full-time → Q2 is Freelancer → Q3 one current row → Q4 no freelance wording → **Q5 corporate flag → PASSIVE**. Five steps. That is the status the record carries today.

**Our rule says ACTIVE, for two independent reasons:**

| # | Reason | Why the system misses it |
|---|---|---|
| **1** | `Associate` is **hard-stop A** — too junior to be a client | the system has no junior check at all |
| **2** | **Finergreen is a boutique investment bank** — its own company description reads *“a boutique investment bank dedicated to the energy transition with in-depth expertise in M&A and complex financing”*. Hard-stop B, sell-side. | the system reads the **flag**, never the description |

A data fault underneath itProduction carries **two** FINERGREEN company records: one typed `Public Corporation` with **no flags** and the correct investment-bank description, and one typed `Asset Management` with `isCorporate = true` and a vaguer *“consulting services”* description. The work-experience row is linked to the second. **Had it linked to the first, Q5 would not have fired and the system would have said Active** — so the outcome turned on which duplicate got matched, not on any fact about the company. See [A6.x.8 ↗](a6-x-8-a-company-can-be-tagged-wrongly.md).

The timeline reads like a human decision and is not oneOne entry: *actorName* **Bernhard Thalhammer (SuperAdmin)**, but `prevValues.status = InReview` → `nextValues.status = Passive`. The transition is `InReview → Passive`, so this is the **automatic rule**, stamped with the approving admin’s name. Read the name instead of the transition and you would wrongly conclude somebody weighed this up.
