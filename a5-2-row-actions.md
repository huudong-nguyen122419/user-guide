# A5.2 · Row actions

> A5 · Manage a marketing email (Admin)

## A5.2.1 · The ⋮ menu changes with status

It is short either way, but the difference matters: So the window to delete closes the moment the ME starts sending. After that it is a record and it stays — there is no Archive to move it to either, and no Clone and no Move, unlike a campaign ([A4.2 ↗](a4-2-row-actions.md)). **Delete asks first** — *“Do you want to delete this Marketing Email”*, with **Exit** and **Delete**. It is a real delete: the list count drops by one (measured: 92 → 91), not an archive.

| ME status | ⋮ offers |
|---|---|
| **Draft** · **Paused** | Edit/View Details · **Delete** · Manage assignee |
| **Running** | Edit/View Details · Manage assignee — **Delete is gone** |

![Row menu on a Draft marketing email](admm-02-row-menu.png)

*A5.2.1 — a Draft: Delete is there. On a Running ME the same menu has two items.*

## A5.2.2 · Bulk does one thing only

Tick rows → **“N marketing email(s) selected”** → **Assign assignee**. There is no bulk delete and no bulk status change — reassigning owners is the whole feature.

![Bulk bar and Assignee column](me-48-list-bulk.png)

*A5.2.2 — ① the selection bar with its single action · ② the Assignee column, with the role chip above each name.*
