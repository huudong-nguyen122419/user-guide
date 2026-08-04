# A6-B · Re-check an existing status

> A6 · Approve a new talent (decides Active or Passive)

**When to run this:** when you want to know whether the statuses already on the platform are still right. It applies to **Active** and **Passive** records, not to the queue. Nothing here is automatic: the system points, you decide.

## A6-B.1 · Read what the system thinks

## A6-B.1 · The icon beside the status chip tells you whether the two agree

It is on the **Talents list** and on the profile drawer, in both places, in the same shape: Hover either icon for the same two lines as in the queue: the recommended status, then the reason.

| Icon | Meaning | What to do |
|---|---|---|
| **⚠ warning** | the current status **does not match** what the rule would pick | worth opening; it may be right anyway |
| **ⓘ info** | status and recommendation **agree** | nothing to do |
| no icon | the rule has no opinion on this record | judge it by hand or leave it |

![Warning and info icons on the talents list](a6q-04-list-icons.png)

*A6-B.1: ① warning, status and recommendation disagree · ② info, they agree.*

## A6-B.2 · Active → Passive

## A6-B.2a · Build the list of candidates

On **Talents**, set **Statuses = Active**. Then **+ Add filter** → under **Availability & Engagement** tick **Recommend Status**, which pins it to the filter bar. Open it and pick **Passive**. The dropdown offers only **Active** and **Passive**. What comes back is every Active talent the rule would have made Passive. **737 of them** when this was walked, so treat it as a working queue rather than a list to clear in one sitting.

![Statuses Active plus Recommend Status Passive](a6q-05-recommend-filter.png)

*A6-B.2a: ① Statuses = Active · ② Recommend Status = Passive · ③ what falls out.*

## A6-B.2b · Open one and read it before you touch the chip

Same three fields as [A6-A.4 ↗](a6-a-review-the-in-review-queue.md): Employment Status, the current title and company, and whether that company is flagged. **Leaving it alone is a valid outcome**, the rule is often pointing at a record that a human already judged correctly.

## A6-B.2c · Change it from the status chip

The chip on the profile carries a caret. Click it and you get exactly one alternative, **Passive**. Picking it opens **Set Talent Status to Passive**, which asks for a reason: Then **Yes**. The chip flips to Passive and the icon beside it changes from warning to info, because status and recommendation now agree.

| Reason | Needs typing? |
|---|---|
| **Unable to verify freelance status** (pre-selected) | no |
| **Evidence insufficient** | no |
| **Reference unresponsive** | no |
| **Other** | yes, in the **Reasons** box |

> **Two things to watch in this dialog**
>
> **The first reason is already selected when it opens.** Press Yes without reading and you have filed “Unable to verify freelance status” on a record where that may be untrue. **🐛 And *Other* does not actually enforce anything.** Picking Other and leaving the Reasons box empty saves without complaint, no error, no disabled button. The reason is meant to be required and is not.

![Set Talent Status to Passive](a6q-06-passive-modal.png)

*A6-B.2c: ① pre-selected reason · ② Other · ③ the Reasons box, on screen whichever reason is picked.*

## A6-B.3 · Passive → Active

## A6-B.3 · The same walk, with the filters the other way round and no reason to give

Set **Statuses = Passive** and **Recommend Status = Active**, open a record, read it, then click the chip and pick **Active**. **Set Talent Status to Active** asks one question, *“Do you want to set Active for <name>?”*, and offers **Exit** and **Yes**. No reason list, no free text.

> **Only one direction is asked to explain itself**
>
> Making somebody Passive takes them out of the invitation flow, so the system asks why. Putting them back does not, which means a record can go Active with nothing on file about who decided or why. If you want that written down, put it in **Notes** yourself.

![Set Talent Status to Active](a6q-07-active-modal.png)

*A6-B.3: the whole dialog. Nothing to fill in.*

## A6-B.4 · Review Passive: the talent asks to be looked at again

The two flows above are you deciding to revisit somebody. **This one starts with the talent.** A person you have already filed as **Passive** can send in a request to be reassessed, and when they do, their status changes on its own to **Review Passive** and they turn up in your queue.

## A6-B.4a · They arrive in the same queue as everyone else

The button at the top right of **Talents** is labelled **N In Review**, but the number covers **both** statuses. So a resubmission is not sitting somewhere separate waiting to be noticed. It is in the queue, mixed in with the new sign-ups. **To see only the resubmissions**, filter the talents list on **Statuses = Review Passive** instead of opening the queue.

| Filter the list by | Count |
|---|---|
| Statuses = **In Review** | 278 |
| Statuses = **Review Passive** | 2 |
| the queue button says | **280** |

## A6-B.4b · Open the profile and read what they sent

A **Review Passive** profile carries the orange **Review Passive** chip, and the Summary tab opens with a block the other statuses do not have: **Talent Resubmit since <date>**, holding the evidence they supplied. **Read it against the rule the same way you would any other profile** ([A6-A.4 ↗](a6-a-4-check-it-against-the-profile.md)). The question is whether the employment situation that made them Passive has actually changed, and whether the reference backs it up.

| Field | What it is |
|---|---|
| **Reference Email** | somebody who can vouch for them. Often a different address from the one they signed up with. |
| **Reference Linkedin** | that person’s profile. A dash means they left it out. |
| **Additional Context of Request** | anything they wanted to say. Frequently empty. |

![A Review Passive profile](a6q-11-review-passive.png)

*A6-B.4b: ① the Review Passive chip · ② what the talent submitted · ③ three buttons instead of the usual two.*

## A6-B.4c · Decide, using the three buttons at the top right

They are not the same buttons a new sign-up gets, and each one says where it lands if you hover it.

| Button | Status afterwards | When |
|---|---|---|
| **Approve Review Passive** | **Active** | the change is real and the evidence holds. Confirms with *Set Talent Status to Active*. |
| **Reject Review Passive** | **Passive** | the request does not stand up. They go back where they were, not out. |
| **Reject** | **Rejected** | they should not be on the platform at all. A different decision from the one above, and much heavier. |

> **Reject and Reject Review Passive sit next to each other**
>
> One puts them back to **Passive**, which is where they already were. The other files them as **Rejected**. The labels differ by two words and the buttons are both red. **Hover before you click**, the tooltip names the status you are about to set.

## A6-B.4d · Rejecting a resubmission asks you why

**Reject Review Passive** opens *Reject Status Update Request*. Pick one of four reasons, add a note if it helps, then **Confirm Rejection**, which stays greyed out until a reason is chosen. The four are **Unable to verify freelance status**, **Evidence insufficient**, **Reference unresponsive** and **Other**. Three of them are about the reference they gave you, which is the point of collecting it: **the reason is a record of what you checked**, not a formality. **Approving asks nothing beyond a yes.** Only the rejection wants a reason, so the case for turning somebody down is written down and the case for letting them through is not.

![Reject Status Update Request dialog](a6q-12-reject-resubmit.png)

*A6-B.4d: ① the four reasons · ② the free-text box · ③ Confirm Rejection, greyed out until you pick one.*

## In this step

* [A6-B.1 · Read what the system thinks](a6-b-1-read-what-the-system-thinks.md)
* [A6-B.2 · Active → Passive](a6-b-2-active-passive.md)
* [A6-B.3 · Passive → Active](a6-b-3-passive-active.md)
* [A6-B.4 · Review Passive (they ask)](a6-b-4-review-passive-they-ask.md)
