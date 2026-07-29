# 6.10 · Label the replies

> 6 · Manage a campaign

## 6.10.1 · Two different labels, and only one of them stops anything

This trips people up constantly:

| Label | Sits on | Set by |
|---|---|---|
| **Category** (the chip on a reply) | a **single reply**, and on the recipient inside this campaign | the system reads the message and guesses; **you correct it by hand** |
| **Lifecycle Stage** | the **contact**, across everything | always you ([Flow 4 ↗](4-view-replies-and-answer-replies.md)) |

## 6.10.2 · The twelve categories — and the three that matter

Read straight off the API on UAT: a recipient can hold any of **12**, an individual reply any of **11** (the same list minus **Unknown**). **Where this comes from:** the twelve / eleven values are read straight off the API and are certain. **Which three stop the sending is taken from Fintalent's internal feature documentation, not from a send test of my own** — proving it would mean mailing a real contact. Treat the split as authoritative but worth one confirmation with the team before you rely on it in anger. The three look exactly like the other nineNothing in the interface marks them out — same chip, same colour, same list. So the label that quietly keeps mailing someone who asked you to stop is one row away from the one that stops it. **Before you label a negative reply, decide which of the two you mean:** “not now, try later” is **Not Now** and keeps them in rotation; “stop emailing me” is **Opted Out** or **Do Not Contact** and takes them out.

| Group | Categories | Effect on sending |
|---|---|---|
| **Stops the sending** | **Opted Out** · **Not Interested** · **Do Not Contact** | **No further mail goes to this person.** Three labels, that is the whole list. |
| **Reporting only** | Call Scheduled · Interested · Not Now · Out Of Office · Left The Company · Email Updated · No Categories · Not Responded · Unknown | **Sending continues.** They describe what happened; they do not hold anything back. |

## 6.10.3 · Out Of Office is not a rejection

It is the most common auto-reply and it is reporting-only, so the person stays in the run — which is right, they are just away. Do not upgrade it to Not Interested to clear it off your screen; that is a different meaning and it is permanent.

## 6.10.4 · Nothing reminds you

Categorising is entirely manual: no prompt, no badge, and **no count of how many replies are still unlabelled**. If you do not work the inbox deliberately, an opt-out can sit there unread while the next send goes out. **Practical habit:** after every send, open the Inbox and clear it to zero before you do anything else. Filter the category rail to **No Categories** to find what nobody has touched. There is also no bulk categorise — thirty auto-replies is thirty separate actions. Sort by the auto chip first so the identical ones are together.

## 6.10.5 · Where you do it

Open the **Inbox** tab of the campaign, pick the category rail on the left to filter, click a reply, set its category. The same reply also appears in your own Inbox (Flow 4) — labelling in either place is the same record.
