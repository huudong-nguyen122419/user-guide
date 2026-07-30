# 7.x.15 · The row-actions button can be unreachable

> 7 · Manage a Marketing Email → 7.x · Edge cases

The two row actions themselves — **Set as Delivered** and **Cancel Email Queue** — are covered in
[7.6.5 ↗](7-6-email-queue-3-tabs.md). This page is only about not being able to reach them.

**The queue table scrolls sideways, and the sticky column can sit on top of the actions column.** On
UAT, 30 Jul 2026, the **⋮** at the end of the row could not be clicked at all — the pointer landed on
the cell covering it.

**Workaround:** widen the browser window, or scroll the table fully to one side, until the actions
column clears the sticky cell.

Logged as **ME-02** in `docs/bug-checking-log.md`, with a second point still open: when the menu was
forced open and *Set as Delivered* chosen, nothing happened and no confirmation appeared — while 7.6.5
says both actions ask first. Whether that is the overlay or the action itself is **not established**;
confirm by hand before relying on it.
