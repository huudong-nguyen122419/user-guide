# 7.x.14 · Personalizing drops the attachment

> 7 · Manage a Marketing Email → 7.x · Edge cases

**If you personalize a contact's email, that contact stops receiving the file.** Everyone you did not
personalize still gets it.

Walked end to end on UAT, 30 Jul 2026. One ME, one step, one attachment (`1-1-log-in.md`), three
recipients. **Only Tin was personalized.**

| to: | Content | Attachments in the queue |
|---|---|---|
| dong@cyberhq.net | *"Hi Dong, …"* — template | **`1-1-log-in.md`** |
| long@cyberhq.net | *"Hi Long, …"* — template | **`1-1-log-in.md`** |
| **tin@cyberhq.net** | *"Hi Tin, **PERSONALISED FOR TIN** …"* | **empty** |

Same subject, same step, same created time. The only difference is the personalization.

![The queue row for the personalized contact has no attachment](sdrx-me-29-attachment-dropped.png)

*7.x.14 — two rows carry the file, the personalized row does not.*

## Why you will not notice

**Preview keeps showing the attachment** for the personalized contact, because Preview renders the
file list from the **template**, not from that contact's own copy. Everything looks right on screen.
The only place it shows is the **Attachments** column in Email Queues — after the queue is built.

## What to do

* **Check the Attachments column in Email Queues before the send goes out**, every time you have
  personalized anyone on an ME that carries a file.
* If a row is empty and you did not remove the file yourself, that contact will receive the email
  **without the attachment**.
* Removing a file deliberately is different — that is the **✕** next to the filename in Preview, and it
  only affects the contact you are looking at.

Logged as **ME-01** in `docs/bug-checking-log.md`.

> **Not yet tested:** whether the same happens on a **campaign**, and whether *Bulk Actions → Mark all
> as Not Personalized* brings the file back.
