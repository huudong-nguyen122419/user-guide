# A6.x.1 · New sign-ups to approve

> A6 · Approve a new talent → A6.x · Edge cases

**The *In Review* queue — new sign-ups waiting for approval.** The **N In Review** button at the top right of the talents list opens the queue one profile at a time. **Approving does not simply mean “Active”.** The confirmation dialog repeats the name, email and title; on **Approve** the system applies an automatic rule and picks the resulting status itself.

**The rule is the five-question spine in [A6-C.6 ↗](a6-c-6-the-automatic-rule.md)** — employment status first, then the **position** and **company** of each **current** work-experience row, then the Mergermarket flag on those companies. It stamps `passiveDate` but records **no reason**, so the profile gives no explanation afterwards.

**Ruled 28 Jul 2026: this is intended behaviour, not a defect.** The system deciding a status at approval is by design. **Two gaps remain**, and both are what [A6-C.7 ↗](a6-c-7-the-rule-being-rebuilt.md) sets out to close:

* it has **no seniority check** — an `Analyst` or `Associate` at a flagged company comes out Passive, where our rule makes them Active. On the UAT queue **33 of the 35** records Q5 sent to Passive were flagged `corporate` and **not one** was a sponsor, so in practice the check is a corporate detector. *(A `corporate` flag does count — ruled 30 Jul 2026 — so those verdicts are correct; the missing seniority check is the defect.)*
* it never looks for **buy-side signal in the position** — it reads the position only to find an exit to Active. A client at a company that was never matched to the Mergermarket list walks straight through.

Neither gap is logged as a bug.

![In Review profile toolbar](a6-07-in-review.png)

*A6.x.1 — ① status chip reads In Review and is not editable · ② Reject Talent → status becomes \*Rejected\*; Approve Talent → confirmation dialog, then the talent enters the normal pool · ③ pager — step through the whole queue without going back to the list · ④ Employment Status, visible on the header.*

> **Skip Review is not part of it — settled 30 Jul 2026.** An earlier note here said the Passive branch needed **Skip Review** set, based on six approvals watched on production. That was a coincidence in the sample. **Iman Dakhlaoui** (`iman.dakhlaoui@gmail.com`) has `internalStatus = null` — no Skip Review — and the system still set **Passive** at approval, transition `InReview → Passive`, on a `corporate` flag. **The five questions are the whole rule; Skip Review does not gate them.**

The chip is **locked while the status is In Review**, so a client has to be approved first and set Passive afterwards ([A6-C.5 ↗](a6-c-review-in-review-queue.md)).

- After each decision the drawer **advances to the next profile** and the counter drops, so the whole queue can be worked without returning to the list.

- The queue drawer **does not put the talent id in the URL**, so a profile being reviewed cannot be linked to. Opening the same person from the list does add `?id=…` — and the Approve / Reject buttons are there too, so use that route when you need to share or come back.
