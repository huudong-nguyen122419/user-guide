# 6.2.3 · Step 1 appears

> 6 · Manage a campaign → 6.2 · Build the sequence

The step lists as **Step 1 - Day 1** with its **timing** ("Right away") and variant **A**.

![Step 1 in the sequence](sdrx-camp-06-sequence.png)

*6.2.3 — Step 1 · Day 1 · Right away · variant A.*

**The header carries a running day count, not just the delay.** *Right away* is Day 1; a step set to
*Wait for 10 days* after a Day 2 step reads **Step 3 - Day 12**. Read the last step's day to see how
long the whole sequence runs.

> **The Steps badge counts every step in every branch.** Once the campaign has sidesteps the badge
> exceeds the main sequence — a campaign with 2 main steps and 4 branches reads **Steps 8**. That is
> correct, not a miscount ([6.x.2 ↗](6-x-2-sidestep-conditional.md)).
