# 7.9 · Label the replies

> 7 · Manage a Marketing Email

> **Mostly this runs without you**
>
> Labelling is **the system’s job first**: every reply that lands is read automatically and given a category, which is why the chips are already there when you open the Inbox. Nothing below asks you to label from scratch. Your part is narrower and more important: **check the ones the system got wrong**, and set the three that actually stop future sending. Read this straight after [7.7 ↗](7-7-verify-in-conversations.md): the chips you are reading there are what this section explains.

## 7.9.1 · Two different labels, and only one of them stops anything

This trips people up constantly:

| Label | Sits on | Set by |
|---|---|---|
| **Category** (the chip on a reply) | a **single reply**, and on the recipient inside this marketing email | the system reads the message and guesses; **you correct it by hand** |
| **Lifecycle Stage** | the **contact**, across everything | always you ([Flow 4 ↗](4-view-replies-and-answer-replies.md)) |

## 7.9.2 · The twelve categories, and the three that matter

Read straight off the API: a recipient can hold any of **12**, an individual reply any of **11** (the same list minus **Unknown**). **Where this comes from:** the twelve / eleven values are read straight off the API. The three that block are named in the code as a constant, `MarketingEmailRecipientBlocklistEnforcementOptions = [OptedOut, NotInterested, DoNotContact]`, and the same three appear in Fintalent's own feature documentation. Not proven by a send test of my own; proving it would mean mailing a real contact.

| Group | Categories | Effect on sending |
|---|---|---|
| **Stops the sending** | **Opted Out** · **Not Interested** · **Do Not Contact** | **No further mail goes to this person.** Three labels, that is the whole list. |
| **Reporting only** | Call Scheduled · Interested · Not Now · Out Of Office · Left The Company · Email Updated · No Categories · Not Responded · Unknown | **Sending continues.** They describe what happened; they do not hold anything back. |

> **The three look exactly like the other nine**
>
> Nothing in the interface marks them out, same chip, same colour, same list. So the label that quietly keeps mailing someone who asked you to stop is one row away from the one that stops it. **Before you label a negative reply, decide which of the two you mean:** “not now, try later” is **Not Now** and keeps them in rotation; “stop emailing me” is **Opted Out** or **Do Not Contact** and takes them out.

## 7.9.3 · Out Of Office is not a rejection

It is the most common auto-reply and it is reporting-only, so the person stays in the run. Which is right, they are just away. Do not upgrade it to Not Interested to clear it off your screen; that is a different meaning and it is permanent.

## 7.9.4 · Nothing reminds you

Categorising is entirely manual: no prompt, no badge, and **no count of how many replies are still unlabelled**. If you do not work the inbox deliberately, an opt-out can sit there unread while the next send goes out. **Practical habit:** after every send, open the Inbox and clear it to zero before you do anything else. Filter the category rail to **No Categories** to find what nobody has touched. There is also no bulk categorise: thirty auto-replies is thirty separate actions. Sort by the auto chip first so the identical ones are together.

## 7.9.5 · Where you do it

Open the **Inbox** tab of the marketing email, pick the category rail on the left to filter, click a reply, set its category. The same reply also appears in your own Inbox (Flow 4), labelling in either place is the same record.
