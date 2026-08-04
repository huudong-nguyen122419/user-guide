# 6.2.2 · Write the step (fields)

> 6 · Manage a campaign → 6.2 · Build the sequence

**Write the step.** Every field of the editor, and what goes in it:

| # | Field / control | What it does · how to write it |
|---|---|---|
| 1 | **Subject** | The email's subject line. Type it plainly, and you **can personalize it with variables** via the **{ }** icon (2). |
| 2 | **{ }** | Inserts a **variable** (merge field) into the **Subject**, e.g. `{{contact.companyName}}`. Details: [6.x.8 ↗](6-x-8-variables.md). |
| 3 | **CC** | Copy someone on every send of this step, click **CC**, an **Add cc** field opens. |
| 4 | **Language (EN / DE)** | The flags switch between the **English and German version** of this step, write one per language you send in. |
| 5 | **Select an email template** | **Yes, templates work here**, prefill the whole step from a saved template instead of writing from scratch. Details: [6.x.7 ↗](6-x-7-start-from-a-template.md). |
| 6 | **Formatting toolbar** | Rich text: H1/H2, font & size, **B**/*I*/U/S, quote, lists, indent, colour, link, clear-format. |
| 7 | **Body** | The message itself. **Variables** (9) and **Snippets** (10) both work in the body; write short, personal, one clear ask. |
| 8 | **Force Update** | Only matters when **editing** a step later, tick it to push your edit onto previews already generated. Details: [6.x.12 ↗](6-x-12-force-update.md). |
| 9 | **Variables** | **Yes**: insert merge fields (`{{contact.firstName}}`…) that fill in per contact. Details: [6.x.8 ↗](6-x-8-variables.md). |
| 10 | **Snippets** | **Yes**: drop in a saved reusable block (enables once your cursor is in the body). Details: [6.x.9 ↗](6-x-9-snippets.md). |
| 11 | **Create / Save** | **Create** saves a new step; re-open a step later and the button reads **Save**. |
| 12 | **Upload files** | Attach files to the email; each attachment shows with an **✕** to remove. Details: [6.x.10 ↗](6-x-10-attachments-signature.md). |
| 13 | **Signature** | Appends your email signature (set up in Flow 1.x.5). |

![Campaign step editor: every field numbered](sdrx-camp-17-editor-fields.png)

*6.2.2: the step editor with every field numbered 1–13 (same numbers as the table).*
