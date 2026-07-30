# 7† · Manage a Marketing Email — audited

> Flow 7 · Manage a Marketing Email — **the decision-maker's view**

Measured on **UAT, 30 Jul 2026**: all **93 marketing emails** read through the API and compared
against what the list and the detail header print. **The full page lives in the guide** — open
`v4.html` and pick *7† · Manage a Marketing Email — audited*.

This page carries the register and the shortlist. The step-by-step instructions stay on
[Flow 7](7-manage-a-marketing-email.md).

## The one-line finding

**The rates on this page divide one unit by another.** The numerator counts *opens* — one person
opening three times counts three — and the denominator counts *people*. So the Open Rate can exceed
100%, and does:

| Marketing email | opens | people | printed |
|---|---:|---:|---:|
| [Prod] US-based Thanksgiving | 1669 | 962 | **173.5%** |
| [Prod] M&A Workshop & Networking | 185 | 140 | **132.1%** |

Underneath it, **"delivered" has two counters that disagree on 13 of the 20** emails that have an
event log — one reads 2,172 where the other reads 0; another reads 0 where the log reads 602.

## Where each number comes from

| On screen | Source | Counts | Notes |
|---|---|---|---|
| **Open Rate** | `statusCount.open` ÷ `totalTargets` | events ÷ people | **Mixed units.** Prints above 100% on two live emails |
| **Reply Rate** | `totalReplied` ÷ `totalTargets` | messages ÷ people | Same problem. Inbox counts conversations instead |
| **Delivered (header)** | `totalDelivered` | — | **Disagrees** with the event log on 13 of 20 |
| Delivered (event log) | `statusCount.delivered` | events | Not shown anywhere on screen |
| People tab | `totalTargets` | people | Lower than the queue on 5 emails |
| Email Queues tab | `emailQueueStatusStatistic` | queue rows | Holds addresses in no other tab |
| Inbox count | reply threads | conversations | Same *Interested* label as Reply Rate, different number |

Worked example, `[Prod] US-based Thanksgiving`: `totalTargets 962` · `totalDelivered 0` ·
`statusCount = {delivered 602, open 1669, bounce 209, dropped 17}` · `totalReplied 33`. The header
says nothing was delivered; the log says 602 were; the Open Rate prints **173.5%**.

## Defect register

Priority = Impact − Effort. A quick win is Impact ≥ 4 with Effort ≤ 2.

| ID | Symptom | Consequence | I | E | P | |
|---|---|---|---:|---:|---:|---|
| **ME-01** | Rates divide an event count by a headcount. | Open Rate prints **173.5%** and **132.1%** on live emails, and **1%** where the truth is 100%. Every percentage on the page is affected. | 5 | 2 | **3** | **quick win** |
| **ME-02** | Two counters for "delivered" disagree on **13 of 20** emails with an event log. | Header says 2,172 where the log says 0; says 0 where the log says 602. Nothing indicates which is shown. | 4 | 2 | **2** | **quick win** |
| **ME-03** | `totalReplied` exceeds `totalDelivered` on 5 emails. | One reads **34 replies against 0 delivered**. Any funnel built on these two fields is unusable. | 4 | 2 | 2 | |
| **ME-04** | The send queue holds people in neither People nor Preview. | 5 emails, gaps of **+472**, **+253**, **+253**, +2, +1. Those people are sent to while being invisible. | 5 | 4 | 1 | |
| **ME-05** | Inbox counts conversations, Reply Rate counts messages, both labelled *Interested*. | The reader sees 1 in one place and 2 in another, unexplained. | 3 | 2 | 1 | |
| **ME-06** | Pausing marks the outstanding queue `Cancel` in bulk — 69 of 70 rows. | Correct in itself, but undocumented; with ME-01 it makes a paused email look like a failed one. | 2 | 1 | 1 | |

## Quick wins

### ME-01 · Count opens per person before dividing · I5 · E2 · P3

**Product** — A rate above 100% destroys trust in every other number on the page. And the opposite
error is worse: the Berlin invite delivered one email, that person opened it *and* replied, and the
screen says **1%**.

**Engineering** — Count distinct openers, divide by people actually delivered to, and clamp nothing —
if it still exceeds 100% the inputs are wrong and should say so. **Fixing the denominator alone is not
enough**: events ÷ people can still exceed 100%.

### ME-02 · Reconcile the two delivered counters · I4 · E2 · P2

**Product** — Two numbers for the same word, and the one driving every rate is the one that is
sometimes zero when hundreds of emails went out.

**Engineering** — Pick one source. If `totalDelivered` stays, backfill it from the event log and
reconcile on write. **ME-03 falls out of this** — the replies are real, the delivered counter is not.

## Open questions

1. Should Reply Rate count people or messages? Both are defensible; the page shows one of each and
   calls them the same thing.
2. Where is `totalDelivered` written, and why do two production-imported emails carry 0 against
   hundreds of delivery events? Suspicion: it only increments on the newer send path.
3. Whether moving campaign targets leaves queue rows behind. Three of the five affected emails are
   named `test move …` — suggestive, not evidence.
4. Whether the same faults appear on production. Everything here was measured on **UAT**, where a
   large share of the records are test data.
5. The `Inbox V1` and `People V1` tabs sit beside the current ones and were not audited. If they are
   being retired they should come out of the guide.

Full sweep data: `plans/reports/audit-260730-1441-campaign-me-sweep-root-causes.md`
