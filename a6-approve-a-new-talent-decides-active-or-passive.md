---
description: "keep clients out of the talent supply. A client is someone who sits on the buy side today — holding a role at a PE fund, or running a company a fund owns. Clients must be Passive so they never enter the project-invitation flow. Everyone else is talent and stays Active."
---

# A6 · Approve a new talent (decides Active or Passive)

> ADMIN · decides Active or Passive

Production is read-only for this workRun the filters and read the data on production, but **never change a status there**. Do every status change on **UAT** first and confirm the result before touching live records.

Looking for the summary, not the procedure?[Approve a new talent · audit ↗](a6-approve-a-new-talent-audit.md) is the same rule written for whoever decides what gets fixed: ten findings, a register of **12 defects** scored by impact and effort, three quick wins, and the questions still open. This page is the operator’s view — what to click, and what the system will do.

## One flow, and what it deliberately leaves out

This section covers **the intake decision only** — the moment an admin approves a new sign-up and the system picks a status. The existing population is a different problem with different evidence, and it is **not worked by hand**.

| Flow | The question it answers | Cost of getting it wrong | Status |
|---|---|---|---|
| [A6-C ↗](a6-c-review-the-in-review-queue-live.md) Review the **In Review** queue | New sign-up — Passive or Active? | the same client, but caught a year later | **the whole flow** |
| **Existing Active and Passive records** | Which of them are wrong today? | a project invitation landing in a client’s inbox | **OUT OF SCOPE** — not re-reviewed by hand. A migration may run the same rule over them later; it may not |

Passive is not a punishment and not a quality judgement. It is a routing decision: Passive records are excluded from project invitations, nothing more.

## Where the talents are today

Production, 30 Jul 2026 — **8,878 talent records**. Active **2,680** · Passive **2,820** · Rejected 1,790 · Incomplete 1,533 · Guest 27 · PaymentRequired 25 · **InReview 2** · ReviewPassive 0 · Temp 0.

The queue the live flow serves is normally tiny. **UAT carries 286** In Review records — that is where the rule was measured.

The 2,680 Active records split by Employment Status: Freelancer 2,343 · Unemployed 206 · Other 102 · Full-time 28 · Part-time 1.

## In this flow

* [A6-C · Review the In Review queue — LIVE](a6-c-review-the-in-review-queue-live.md)
* [A6.1 · Three fields people mix up](a6-1-three-fields-people-mix-up.md)
* [A6.x · Edge cases](a6-x-edge-cases.md)
