# A6-B · Identify PASSIVE talent

> A6 · Talent Active / Passive — **DEFERRED · will run as a migration**

> ## Not worked by hand any more
> Existing Active records are **no longer re-reviewed one at a time**. This whole section is kept as the specification for a **migration** that will run later, and as the reference for the rule tables the live intake flow borrows from.
>
> The live flow is [A6-C · Review the In Review queue](a6-c-review-in-review-queue.md).
>
> **Two decisions landed after these pages were written**, and the migration must honour them:
> * The Full-time gate has **no escape hatch** — `totalApplications` and `totalAccepted` no longer keep anybody Active. Rule 2's two exits are withdrawn.
> * Titles are read from **`workExperiences[].position`**, the job title on each current row — **not** the profile headline. The two differ on **49%** of records with a current role.

Only the **Active → Passive** direction. Two lists to work, nothing else.

**Nothing here changes a status by itself.** Each list ends in a queue you read and decide on. Production is read-only — do the changes on **UAT**.

## In this flow

* [A6-B.0 · The rules](a6-b-0-the-rules.md) — read this once before you start
* [A6-B.1 · List 1 — Active + Full Time](a6-b-1-employment-gate.md)
* [A6-B.2 · List 2 — Active + PE/VC background](a6-b-2-title-and-background.md)
* [A6-B.3 · Sub-rule 2 — the employer check](a6-b-3-sub-rule-2.md)
* [A6-B.4 · Set the status Active → Passive](a6-b-4-set-status-on-uat.md) — **on UAT**

## The two lists

Both start from **Statuses = Active** and differ only in the second chip. Between them no record is looked at twice.

| List | Chips to set | On production | You end up with |
|---|---|---:|---|
| **[List 1](a6-b-1-employment-gate.md)** | Statuses = Active · Employment Status = **Full Time** | **29** | **13** to consider |
| **[List 2](a6-b-2-title-and-background.md)** | Statuses = Active · Employment Status = **the other two** · Company Background = **PE/VC** | **133** | **8** to Passive · **13** to read |

Nothing outside these two lists is in scope.

## The order to work in

```
1. Build the list          (2 or 3 chips on the Talents page)
2. Read each row           (List 1 = two numbers · List 2 = the title)
3. Check the employer      (List 2 only, and only for generic titles)
4. Open Activity Logs      (an admin decision is left alone)
5. Write the row down      (queue → Passive, or queue → needs a read)
6. Do the change on UAT    (A6-B.4 — one profile at a time, no bulk)
```

Steps 1–5 run on **production, read-only**. Step 6 runs on **UAT**.
