# 4b.x.1 · They ask to move it

> 4b · Schedule a call → 4b.x · Edge cases

**They ask to move it — the whole sequence.** This is the common one, and there is no reschedule button, so it goes:

- Their reply arrives asking to move or drop the call.

- **⋮ → Cancel meeting** on the old booking. The old link is dead from that moment.

- New time agreed? **Create meeting** again — and it mints a **completely new Zoom meeting**. Verified on UAT: cancelling meeting `…630530` and rebooking produced `…971737`, a different number **and** a different password.

- Reply in the same thread with the **new** link, and say plainly that the earlier invitation no longer works. Their calendar still holds the old one.

- No new time? Cancel and leave it. The contact keeps the **Call Scheduled** lifecycle until somebody changes it, so fix the stage by hand or the inbox filter will keep offering them to you.
