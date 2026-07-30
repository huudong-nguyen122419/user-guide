# A6 · audit — The approval decision, audited

> A6 · Talent Active / Passive — **the decision-maker's view**

The same rule as the rest of A6, written for whoever decides what gets fixed. **The full page with
every section lives in the guide** — open `v4.html` and pick *A6† · The approval decision, audited*
from the sidebar.

**This page carries only what is not already written elsewhere:** the scored defect register and the
quick-win shortlist. For the rule itself, go to the source pages instead of repeating them here:

| | |
|---|---|
| The five questions the code asks **today**, and how many of them each talent walks | [A6-C.6](a6-c-6-the-automatic-rule.md) |
| The seven-step rule that **replaces** it, validated on 7 live records | [A6-C.7](a6-c-7-the-rule-being-rebuilt.md) |
| What an admin clicks, start to finish | [A6-C](a6-c-review-in-review-queue.md) |
| Correcting a verdict by hand | [A6-C.5](a6-c-5-fix-the-status-by-hand.md) |

## The one-line finding

**A job title never makes anybody Passive.** After the employment-status gate, only a Mergermarket flag
on the current employer can produce Passive — and a junior title vetoes even that. **The flag is
necessary, not sufficient.**

Which puts the whole decision on one lookup that fails quietly: **roughly 63% of talents have a current
employer that was never matched to a company record**, and an unmatched company can never raise a flag.

## Defect register

Priority = Impact − Effort. A quick win is Impact ≥ 4 with Effort ≤ 2. Sorted by priority descending,
quick wins first.

| ID | Symptom | Consequence | I | E | P | |
|---|---|---|---:|---:|---:|---|
| **PP-01** | No seniority test anywhere in the walk. A junior title reaches the flag step and is filed as a client. | A 7-year M&A associate at a boutique investment bank is excluded from every project invitation from day one. | 5 | 1 | **4** | **quick win** |
| **PP-03** | An automatic Passive stamps `passiveDate` and writes no reason. | The profile cannot explain itself later; a batch cannot be audited; every disagreement is re-derived by hand. | 4 | 1 | **3** | **quick win** |
| **PP-02** | A blank employment status is read as "not full-time" and waved to Active. | **27% of the queue** decided on a field nobody filled in, without the profile being opened. | 4 | 2 | **2** | **quick win** |
| **PP-04** | One company holds two records with different flags; the role links to the wrong one. | The verdict turns on which duplicate got matched. Finergreen: the correct record is unflagged, the linked one is flagged Corporate. | 5 | 3 | 2 | |
| **PP-07** | An automatic status change is stamped with the approving admin's name. | An auditor reading the name instead of the transition drops exactly the records the audit exists to find. | 3 | 1 | 2 | |
| **PP-08** | `ongoing = true` on a row whose `to` date has already passed. | A finished job counts as current. One record's end date is four months in the past and the UI still prints *Until Now*. | 3 | 1 | 2 | |
| **PP-11** | The freelance word list is unpublished and incomplete. | A record can exit to Active for a reason nobody outside the code can see. `remote` matches nothing; `fractional` appears in 11 titles and is in no list we hold. | 3 | 1 | 2 | |
| **PP-05** | An unmatched current employer silences the deciding step. | About **63%** of current employers are unmatched, so for most records the flag step cannot fire whatever the company actually is. | 5 | 4 | 1 | |
| **PP-10** | `seniorityLevel` describes the person, not the current role. | A 12-year record labelled `Manager` is working as an Analyst. Trusting the label files her as a client. | 3 | 2 | 1 | |
| **PP-09** | The tooltip names the outcome but never which test produced it. | A correct verdict cannot be told from a coincidence, so a wrong reason survives as long as the right answer comes out. | 2 | 1 | 1 | |
| **PP-06** | A work-experience row links to a subsidiary instead of the parent. | `Criteo` resolved to *HookLogic, acquired by Criteo in 2016*. Both are flagged Corporate, so the verdict held — by luck. | 3 | 3 | 0 | |
| **PP-12** | The status chip is read-only while the status is In Review. | A known client must be approved first and corrected second. The wrong status exists, briefly, on every corrected record. | 2 | 2 | 0 | |

## Quick-win shortlist

### PP-01 · Check seniority before checking the employer  · I5 · E1 · P4

**Product** — A junior analyst is the product, not the customer. Right now holding a job at a
recognised company is enough to file one as a client, and nothing on the profile says why. Largest
class of wrong verdicts, cheapest to close.

**Engineering** — Add S5 between the freelance-wording test and the flag lookup, matching hard-stop A
on word boundaries against `workExperiences[].position` for rows with `ongoing = true`. **S5 must
short-circuit before the flag is read** — order is the whole point.

### PP-03 · Record why the rule decided what it decided  · I4 · E1 · P3

**Product** — A status with no reason cannot be reviewed, appealed or trusted. Every argument about a
verdict currently starts by rebuilding the reasoning from scratch.

**Engineering** — Persist the step that fired alongside `passiveDate`, reusing the shape the manual
reason already writes, and render it next to the status chip.

### PP-02 · Stop treating a missing answer as an answer  · I4 · E2 · P2

**Product** — More than a quarter of the queue is filed without anyone reading the profile, because an
empty field passed a test it should not have been eligible for.

**Engineering** — Separate *blank* from *not full-time* at S2. Then either continue the walk on the
position alone, or route the record to a hold state. The code is small; **the decision is the work**.

## What the register does not cover

Effort scores assume the fix stays inside the rule and needs no company-data work — **except PP-04,
PP-05 and PP-06**, which are scored as data work, and that is exactly why none of the three is a quick
win despite two of them carrying the highest impact on the list.

Open questions and unverified claims are kept with the rule, in
[A6-C.7 → Still open](a6-c-7-the-rule-being-rebuilt.md).
