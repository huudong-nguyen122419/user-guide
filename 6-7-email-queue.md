# 6.7 · Email Queue

> 6 · Manage a campaign

**Running the campaign creates the tab. It does not fill it.** Once Admin has run it ([A4.6 ↗](a4-6-run-a-campaign.md)) an **Email Queues** tab appears on the campaign, and the first thing you notice is that it is empty. Nothing is wrong. A step only enters the queue when somebody pushes it there.

## 6.7.1 · Admin / Ops opens the Steps tab and presses Force Send on a step

Every step carries its own **Force Send** button, main steps and sidesteps alike, so this is a decision per step rather than for the campaign as a whole.

## 6.7.2 · Read the dialog

*Force Send Campaign Flow* repeats the **Subject** and the opening of the **Content**, then states the size of the send: *The step will be sent immediately to 12 Peoples*. **Exit** changes nothing, **Yes** queues it.

## 6.7.3 · Now the queue has rows

Four tabs across the top: Each row shows the **Subject**, the **Content**, the **Status**, **Attachments**, the **from** and **to** addresses, and three dates: **Created**, **Expected Run** and **Expected Delivery**.

| Tab | What is in it |
|---|---|
| **All** | everything, whatever happened to it. |
| **In Queue** | written, waiting, **not sent yet**. |
| **Delivered** | gone out. |
| **Cancel** | pulled back before sending, so nobody received it ([6.x.22 ↗](6-x-22-cancel-a-queued-email.md)). |

> **12 people does not mean 12 emails**
>
> The dialog counts everybody on the campaign. **The queue does not.** In a worked example the campaign held **12** people, Force Send announced **12 Peoples**, and the queue came out at **9**. To work out the real number, start from the People count and take away: people on the campaign 12 minus contacts not marked done minus contacts you skipped for THIS step --- emails actually queued 9 **The count in the dialog is a headcount, not a send count.** If the two differ and you cannot say why, the answer is on the Preview tab: the **Done** and **Skipped** filters ([6.5.3 ↗](6-5-3-skip-a-step.md)).

> **When do the queued emails actually go?**
>
> **At the start of the day, in the timezone the campaign was created with.** Not when you pressed Force Send. That is why the **Expected Run** column can read an earlier hour than **Created**: the send is scheduled against a different clock from the one you are looking at. **So the timezone you pick when creating a campaign decides what time of day your prospects are mailed** ([6.1.5 ↗](#s6-1-5)). Get it wrong and a DACH campaign lands overnight. Check it before the first Force Send, not after.

**In a hurry?** A single queued email can be pushed out without waiting for the daily release: [6.x.23 ↗](6-x-23-set-as-delivered.md).

**Heads-up:** as with Marketing Emails, the **Email Queues** list can be slow or show **0** or *Couldn't load* even when the campaign has already delivered. If it looks empty, refresh, or confirm from the [campaign Inbox (6.8)](6-8-verify-replies.md) and the contact's Conversations.
