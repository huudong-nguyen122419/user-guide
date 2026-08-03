# 7.3.8 · Remove & Undo

> 7 · Manage a Marketing Email → 7.3 · Add people to the ME

**Taking someone back out.** Same tab: tick them, then **Remove contacts** in the selection bar. You get told twice, in two different places, and they do not say the same thing: **Undo really does restore them** — verified on UAT: removed one of two, People went 2 → 1, clicked **Undo**, People went back to **2** with the contact returned. The banner stays until you dismiss it, so you have a moment to change your mind rather than a two-second toast. 🐛 After Undo the table lies until you reloadThe **People** badge corrects itself, but the list underneath keeps the post-removal total — it read **People 2** and *Showing 1 of 1* at the same time. Refresh before you trust the table, and count off the badge, not the footer.

| Where | What it says |
|---|---|
| **Banner**, above the table | *Removed 1 contact* — with an **Undo** beside it. |
| **Toast**, bottom left | *Removed 1 contact from M&A Executive Briefing - Berlin, October 2026* — the only one that names the email. |

![Remove banner with Undo, and the toast naming the email](me-55-remove-undo.png)

*7.3.8 — ① the banner and its Undo · ② the toast, the only place the email is named.*
