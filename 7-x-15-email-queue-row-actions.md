# 7.x.15 · Email Queue row actions

> 7 · Manage a Marketing Email → 7.x · Edge cases

Each row in **Email Queues** carries its own action menu at the far right of the table, with two items:

| Action | What it does |
|---|---|
| **Set as Delivered** | marks that one queued email delivered without waiting for the sender |
| **Cancel Email Queue** | drops that one email from the queue — see [A5.x.3 ↗](a5-x-3-cancelled-failed.md), cancelled is not failed |

Neither asks for confirmation.

> ## The button is hard to reach
> The queue table scrolls sideways, and the sticky column sits **on top of** the actions column. On
> UAT, 30 Jul 2026, the row-actions button could not be clicked with a mouse at all — the pointer
> lands on the cell covering it.
>
> **Workaround:** widen the browser window, or scroll the table fully to one side, until the actions
> column clears the sticky cell.
>
> Logged as **ME-02** in `docs/bug-checking-log.md`, together with a second unknown: when the menu was
> forced open and *Set as Delivered* chosen, **nothing happened and no message appeared**. Whether that
> is the overlay or the action itself is **not yet established** — confirm by hand before relying on it.
