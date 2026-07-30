---
description: "when an admin approves a talent out of In Review, the system decides Active or Passive by itself. This flow is how you read that decision before you click, and how to override it when it is wrong."
---

# A6 · Approve a new talent (xác định talent là active hay passive)

> ADMIN · In Review queue → approve → the system sets the status

## Scope

**One live flow: the In Review queue.** A new sign-up sits at `In Review`; an admin opens it, clicks **Approve**, and the system decides **Active** or **Passive** on its own using a fixed rule. Your job is to know what it will decide *before* you click, and to correct it afterwards if the rule got it wrong.

| | |
|---|---|
| ✅ **In scope** | [A6-C · Review the In Review queue](a6-c-review-in-review-queue.md) — the intake decision, and the only thing this flow covers |
| ❌ **Out of scope** | **Existing Active and Passive records.** Nobody re-reviews them by hand. A migration may run over them later using the same rule; it may not. Either way it is not this flow, and the pages that used to describe it have been removed. |

## The flow, end to end

```
In Review queue
      │
      ▼
Admin opens the profile and reads it
      │
      ▼
Hover  Approve Talent   →  tooltip shows the status the system WILL set
      │
      ▼
Click  Approve          →  the rule runs, status becomes Active or Passive
      │
      ▼
                          done
      │
      └── edge case: the status is wrong
                 │
                 ▼
          Admin flips it by hand on the status chip
```

Five things happen and that is all of them. There is no queue to build, no list to work, no batch.

## What the decision rests on

The rule reads **three things and nothing else**:

1. the **employment status** the talent picked at sign-up
2. the **position** and **company name** of their **current** work-experience rows
3. whether those companies carry a **Mergermarket flag** — portfolio / sponsor / corporate

It never reads the profile headline, the company description, the contract history, or the applications.

**How many steps a single talent walks through: between one and five.** Most stop early. The full analysis, with how many records stop at each step, is in [A6-C.6 · The automatic rule, in full](a6-c-6-the-automatic-rule.md).

## Where the talents are today

Production, 30 Jul 2026 — **8,878 talent records**. Active **2,680** · Passive **2,820** · Rejected 1,790 · Incomplete 1,533 · **In Review 2** · Guest 27 · PaymentRequired 25.

The queue this flow serves is normally tiny. UAT carries **286** In Review records, which is where the rule was measured.

## Reference

* [A6-C.6 · The automatic rule, in full](a6-c-6-the-automatic-rule.md) — every step, what it decides, what it gets wrong
* [A6.1 · Three fields people mix up](a6-1-three-fields-people-mix-up.md) — Status vs Employment Status vs Company Background
* [A6.x · Edge cases](a6-x-edge-cases.md) — 10 behaviours that bite during the work
