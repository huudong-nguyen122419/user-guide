# A6-C.5 · Fix the status by hand

> A6-C · Review the In Review queue — **step 5, the edge case**

Only when the status the system chose is wrong. Everything before this is one click; this is the
correction path.

> ## The chip is locked until approval finishes
> While the status is `In Review` the chip is read-only, so you **cannot** pre-set the outcome.
> Approve first, correct after. That is why this is always two separate acts.

> ## Do this on UAT, never on production
> Production is read-only for this work. Read the data on production, make the change on **UAT** and
> confirm the result there.

## A6-C.5.1 · Open the record again

The record leaves the queue on approval and the **Approve Talent / Reject Talent** buttons disappear
from the toolbar — that is your signal it went through. Reopen it from **User Management → Talents**.

## A6-C.5.2 · Find the status chip

Under the avatar on the left of the drawer. Hover it first — the tooltip tells you whether it is live:

| Tooltip on hover | Meaning |
|---|---|
| **"Click to update"** | clickable, go ahead |
| **"Passive since &lt;date&gt;"** plus a reason | already Passive — read the reason before changing anything |
| no tooltip, chip does not open | the status is not Active or Passive, so the chip is **read-only** ([A6.x.10 ↗](a6-x-10-send-a-talent-back-to-in-review.md)) |

![Talent status chip](a6-05-status-chip.png)

*A6-C.5.2 — ① the status chip, click to open · ② the only alternative offered · ③ Employment Status on the header line.*

## A6-C.5.3 · Click the chip

**The dropdown shows one option: the opposite status.** On an Active record only **Passive**; on a
Passive record only **Active**. Verified on UAT. Rejected, In Review, ReviewPassive and the rest are
set by the system or by the review actions, never here.

![Status chip dropdown](a6-11-chip-dropdown.png)

## A6-C.5.4 · Active → Passive: the dialog has a trap

A dialog opens, **Set Talent Status to Passive**, asking *"Do you want to set `Passive` for
&lt;name&gt; ?"* — with a radio group and a free-text box.

![Set Passive confirm dialog](a6-b-03-set-passive-modal.png)

| Radio option | |
|---|---|
| **Unable to verify freelance status** | **pre-selected when the dialog opens** |
| Evidence insufficient | |
| Reference unresponsive | |
| **Other** | |

**The first three belong to the freelance-verification review, not to this flow.** They all mean *"we
could not confirm this person is really freelancing"*. Overruling the rule concludes something else
entirely — that the current employer makes this person a client. **So pick `Other`.**

> **The trap:** the dialog opens with *Unable to verify freelance status* already selected. Click
> **Yes** without touching the radio and that becomes the stored reason — wrong, permanent, and on
> every record you process.

**The Reasons box is not enforced.** On UAT, picking `Other` and clicking **Yes** with the box empty
saved fine; the record then shows only the word *"Other"* and no explanation. Typing it is on you.
One line naming the step and the employer:

```
S7 — current role at <company>, flagged <sponsor|portfolio|corporate>. Client, not supply.
```

The employer matters. Six months from now the title alone will not explain the call.

## A6-C.5.5 · Passive → Active: no dialog to speak of

**Set Talent Status to Active**, *"Do you want to set `Active` for &lt;name&gt; ?"*, and just
**Exit / Yes**. No radio group, no reason field.

> **The asymmetry is worth knowing.** Going Passive asks for a reason; going Active does not. So a
> record you corrected *to* Active carries no record of why the rule was overruled. If it matters,
> write it in Notes.

## A6-C.5.6 · Verify, twice

1. **The chip reads the new status.** Hover it — on Passive the tooltip now reads **"Passive since
   &lt;date&gt; at &lt;time&gt;"** followed by the radio value. Verified on UAT: *"Passive since
   Jul 29, 2026 at 17:12 · Other"*.
2. **Open Timelines, then reload the page.** The tab count does **not** refresh on its own. After
   reloading, the entry reads *"&lt;you&gt; (Admin) changed talent status (Active → Passive) by
   &lt;you&gt;"* with a detail block `STATUS Active → Passive`.

**That second check is what makes the correction stick.** A future migration tells a hand-set status
from an automatic one by the **transition inside the entry, not by the name on it** — an automatic
Passive at approval reads `In Review → Passive` and carries the approving admin's name anyway. Your
correction reads `Active → Passive`, so it is unmistakably yours and a migration will leave the record
alone.

## Things that will slow you down

| | |
|---|---|
| **No bulk status change** | Bulk Actions offers export, add / remove from list, and Set Skip / Require Review — no status. One profile at a time ([A6.x.3 ↗](a6-x-3-status-can-t-be-changed-in-bulk.md)) |
| **The chip is locked outside Active / Passive** | it only switches between those two. Anything else has to come back to In Review first ([A6.x.10 ↗](a6-x-10-send-a-talent-back-to-in-review.md)) |
| **The reason is not a field on the record** | it surfaces in the chip tooltip and the activity log only ([A6.x.7 ↗](a6-x-7-where-the-passive-reason-is-saved.md)) |
| **Going Passive stops nothing already running** | contracts, timesheets and invoices are unaffected. It only removes them from project invitations ([A6.x.9 ↗](a6-x-9-what-passive-does-not-affect.md)) |
| **Correcting twice leaves two entries** | switch back and forth and the timeline keeps both. Not a problem, but read the latest one |
