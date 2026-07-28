# A6.x.1 · New sign-ups to approve

> A6 · Talent Active / Passive → A6.x · Edge cases

**The *In Review* queue — new sign-ups waiting for approval.** The **N In Review** button at the top right of the talents list opens the queue one profile at a time. **Approving does not simply mean “Active”.** The confirmation dialog repeats the name, email and title; on **Approve** the system then applies an automatic rule and picks the resulting status itself: Verified on six approvals: *Skip Review + ongoing role at a flagged company* produced Passive twice; the same talent with the flag missing, with no ongoing role at all, or without Skip Review produced Active four times. The trigger is the flag on the linked company — an ongoing role at a company that was never matched to the Mergermarket list does **not** fire it. This is where most wrongly-Passive talents come fromFreelancers get set Passive **at approval time** purely because they hold a current job, whatever that job is — a corporate role counts, and group D is supposed to be out of scope. Nobody clicked anything, and because the rule writes no reason, the profile gives no explanation afterwards. If you are auditing Passive talents, start here. **Ruled 28 Jul 2026: this is intended behaviour, not a defect — but it is narrower than the business rule.** The system deciding a status at approval is by design. Two gaps remain, and both are for a human to close: it fires on a plain **corporate** flag, which is group D and out of scope; and it never reads **Employment Status**, so it cannot enforce the gate in [A6.3.1 ↗](a6-3-how-to-decide.md). Neither gap is logged as a bug — they are the reason A6.4 and A6.5 exist. **Two things worth knowing about the queue itself:** The chip is locked while the status is In Review, so a client has to be approved first and set Passive afterwards per [A6.5 ↗](a6-5-active-who-should-be-passive.md).

![In Review profile toolbar](a6-07-in-review.png)

*A6.x.1 — ① status chip reads In Review and is not editable · ② Reject Talent → status becomes \*Rejected\*; Approve Talent → confirmation dialog, then the talent enters the normal pool · ③ pager — step through the whole queue without going back to the list · ④ Employment Status, visible on the header.*

| Condition at the moment of approval | Resulting status |
|---|---|
| **internal status = Skip Review** and an **ongoing** role at a company flagged **sponsor / portfolio / corporate** | **Passive** — `passiveDate` stamped, **no reason recorded** |
| anything else | **Active** |

- After each decision the drawer **advances to the next profile** and the counter drops, so the whole queue can be worked without returning to the list.

- The queue drawer **does not put the talent id in the URL**, so a profile being reviewed cannot be linked to. Opening the same person from the list does add `?id=…` — and the Approve / Reject buttons are there too, so use that route when you need to share or come back.
