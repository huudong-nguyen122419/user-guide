# 6† · Manage a campaign — audited

> Flow 6 · Manage a campaign — **the decision-maker's view**

Measured on **UAT, 30 Jul 2026**: all **49 campaigns** read through the API and through their own
health snapshot, then compared against what the screen prints. **The full page lives in the guide** —
open `v4.html` and pick *6† · Manage a campaign — audited*.

This page carries the register and the shortlist. The step-by-step instructions stay on
[Flow 6](6-manage-a-campaign.md).

## The one-line finding

**The number that blocks the Start button is roughly double the truth.** Data Health counts a
cross-campaign overlap once by contact id and again by email address, then adds the two together — so
the same person is counted twice.

```
Corp Dev outreach — DD capacity (DACH)
  duplicatedByContactId = 8
  duplicatedByEmail     = 7
  issue count           = 15   ← 8 + 7
  evidence contactIds   = [ 8 ids ]
```

**9 of the 10** campaigns carrying this issue match the formula exactly. The only exception is the one
whose email count is zero — nothing to double.

## Defect register

Priority = Impact − Effort. A quick win is Impact ≥ 4 with Effort ≤ 2.

| ID | Symptom | Consequence | I | E | P | |
|---|---|---|---:|---:|---:|---|
| **CMP-01** | The cross-campaign issue count adds by-id and by-email matches together. | The blocker gating **Start** reads roughly double. SDRs stopped on campaigns not really in conflict. **9 of 10** affected. | 5 | 1 | **4** | **quick win** |
| **CMP-02** | `NaN%` when the email queue is empty. | **24 of 49 campaigns (48%)**, including two with 585 and 511 people. The Cancelled row loses its count as well as its percentage. | 4 | 1 | **3** | **quick win** |
| **CMP-03** | The People tab drops contacts with no health tier: 21 → 18 → 17. | An SDR works a shorter list than the campaign will send to, and nobody is told. | 4 | 2 | **2** | **quick win** |
| **CMP-04** | `/email-queues` returns 403 for an SDR; the UI draws an empty queue. | A permission problem is indistinguishable from an empty result. | 5 | 3 | 2 | |
| **CMP-05** | Contacts hidden from the SDR menu but fully reachable from inside a campaign, Export CSV included. | The product answers both ways depending on the route taken. | 3 | 2 | 1 | |
| **CMP-06** | Manage assignee drawer lists 38 accounts and their roles to an SDR. | Staff directory exposed to a role with no need for it. | 3 | 2 | 1 | |
| **CMP-07** | The folder rail shows other owners' folders with live counts. | An SDR learns how much work everyone else has. Opening a folder correctly shows nothing — only the count leaks. | 2 | 1 | 1 | |
| **CMP-08** | Four campaigns have no health snapshot; tier counts fail to sum on two others. | A blank Data Health tab reads as *healthy* rather than *never computed*. | 2 | 2 | 0 | |

**Also seen, not scored:** the status tab prints `Finished` while the API returns `Completed`; Steps
writes *"Side Step"* and Preview writes *"Sidestep"*; and `O` removes a contact with no confirmation,
sitting next to `E` on most keyboards.

## Quick wins

### CMP-01 · Stop adding the two overlap counts together · I5 · E1 · P4

**Product** — This is the only defect on the list that stops work outright. An SDR cannot start a
campaign until the blocker clears, and the blocker is inflated on nearly every campaign that has any
overlap at all.

**Engineering** — Report `metadata.contactIds.length`, which the issue already carries, and keep
`duplicatedByContactId` / `duplicatedByEmail` for diagnostics only.

### CMP-02 · Never print a percentage without checking the denominator · I4 · E1 · P3

**Product** — Half the campaigns show `NaN%` where a number should be. It reads as broken because it
is.

**Engineering** — Render `—` when the denominator is zero, and keep the raw count visible.

### CMP-03 · Make the People tab agree with itself · I4 · E2 · P2

**Product** — Three numbers for one campaign — 21, 18, 17 — none of them labelled.

**Engineering** — Left-join the health table instead of inner-joining it, and show untiered contacts
as `Unknown`, which is already a tier the snapshot uses.

## Open questions

1. Should the overlap check dedupe across the two match methods, or report them separately? A shared
   address across two contact records is itself a data problem, so they may not be the same signal.
2. Are SDRs meant to reach Contacts and Email Queue at all? The product answers *no* via the menu,
   *yes* via the campaign, and *403* via the API.
3. Why an SDR sees 17 where an admin sees 18. The untiered-contact theory accounts for 21 → 18 and
   nothing else.
4. Whether the four campaigns without a snapshot were never computed or failed.
5. The permission findings (CMP-04 … 07) came from an earlier pass under an SDR login and were **not**
   re-checked in this sweep, which ran as an admin.

Full sweep data: `plans/reports/audit-260730-1441-campaign-me-sweep-root-causes.md`
