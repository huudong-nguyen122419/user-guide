# 7.x.15 · Row-actions button unreachable

> 7 · Manage a Marketing Email → 7.x · Edge cases

**The row-actions button can be unreachable.** The two actions themselves — **Set as Delivered** and **Cancel Email Queue** — are covered in [7.6.5](7-6-email-queue-3-tabs.md). This is only about not being able to reach them: the queue table scrolls sideways and the sticky column can sit *on top of* the actions column. On UAT 30 Jul 2026 the **⋮** at the end of the row could not be clicked at all — the pointer landed on the cell covering it. **Widen the window, or scroll the table fully to one side**, until the actions column clears the sticky cell. Still openLogged as **ME-02**. When the menu was forced open and *Set as Delivered* chosen, nothing happened and no confirmation appeared — while 7.6.5 says both actions ask first. Whether that is the overlay or the action itself is **not established**; confirm by hand before relying on it.
