# 7.2a · Reading the numbers

> 7 · Manage a Marketing Email → 7.2 · View your MEs

**Reading the numbers on a row.** Every row carries the ME's whole health check: **The three rates stay blank on a Draft.** Nothing has been sent, so there is nothing to measure — blank is not zero.

| Column | What it actually counts |
|---|---|
| **Name** | the name, the **From** address it sends as, and the status chip. |
| **People** | who is in it **right now**. An old ME can read 0 if people were removed after it ran. |
| **Delivered** | **emails**, not people — one contact can receive several over time, so *1 person / 12 delivered* is normal. |
| **Open Rate** | raw count in brackets, but the **% is out of People, not out of Delivered** — see the warning below. |
| **Reply Rate** | total replies in brackets, same denominator problem. **The bracket count is the number that matters; ignore the %.** |
| **Bounce/Dropped Rate** | % that failed. **Anything above 0 is a to-do** — those people never got it; reach them via [Flow 3 ↗](3-send-a-1-1-email.md). |
| **Progress** | empty grey bar + 0% while Draft; full purple bar + green ✓ once everything has gone. |
| **Last run** | when it last actually sent (— if never). |

![Marketing email metrics](sdrx-me-06-metrics.png)

*7.2.3 — the per-row metrics.*

> ## The percentages are misleading until an ME has finished
>
> **Open Rate and Reply Rate divide by People, not by Delivered.** Verified on UAT against the raw numbers.
>
> One ME read **69 People · 1 Delivered · Open Rate 1% (1) · Reply Rate 3% (2)**. The single person who actually received it opened it and replied — a real open rate of 100%. The screen said 1%, because it computed 1 ÷ 69.
>
> **So while an ME is paused, part-sent, or still running, the percentages understate everything.** Read the **bracket counts** instead, and compare them against **Delivered** yourself. The percentages only mean what you expect once Progress hits 100%.
>
> Two more things the same row can show you, both worth a second look:
>
> * **Reply count higher than Delivered** — e.g. *Delivered 1, Reply Rate (2)*. The bracket counts **messages**, so one person replying twice reads as 2. The **Inbox** tab counts **conversations**, so the same ME shows *"Showing 1 of 1"* there. Neither is wrong on its own; they answer different questions.
> * **People and Email Queues disagreeing** — one ME showed **People 69** but **Email Queues 70**, with 70 distinct recipients and no duplicates. Somebody sits in the send queue without appearing in People. If you see this, check the queue before restarting the ME.
