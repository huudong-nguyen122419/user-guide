# 7.5 · Force send

> 7 · Manage a Marketing Email

No Force Send on the SDR view**Force Send is an Admin / Ops action** — on the SDR login there is **no Force Send button** (the ME's ⋮ menu only offers **Edit / View Details**). Your Admin both flips the ME **Draft → Active** and clicks **Force Send** — the Admin side is [Flow A3.1 ↗](a3-1-run-a-marketing-email.md).

## What your Admin sees — two dialogs, very different

**Draft → Active** is the status switch at the top right of the ME. It opens a careful confirm:

> **Run marketing email** — *"Sending starts as soon as you confirm. This cannot be undone."*
> `3 recipients · 1 email step · 0 reviewed`
> ⚠ *"3 of 3 recipients have not been reviewed. They will receive the default template as-is."*
> ☐ **I understand 3 unreviewed emails will be sent** — the Run button stays disabled until this is ticked
> **Review them now** — closes the dialog and opens Preview

**Force Send** is the opposite. Its dialog shows the Subject and Content and nothing else — **no
recipient count, no mention of attachments**, and the merge tags are still raw (`{{contact.firstName}}`).
It is also titled *"Force Send Campaign Flow"* on a Marketing Email. Read the Run dialog's numbers
before you get here, because Force Send will not repeat them.

Once your Admin has force-sent, your job is to **check the queue**:

## 7.5.1

Open the **marketing email detail**.

## 7.5.2

Go to the **Email Queue** tab.

## 7.5.3 · Check the count

the number of queued emails should match the **number of contacts you marked as reviewed** (7.4.5). If it doesn't, something's off; flag it — don't just carry on.
