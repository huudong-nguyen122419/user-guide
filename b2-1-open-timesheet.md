# B2.1 · Open Timesheet

> B2 · Talent · log & submit timesheet

1. **B2.1.1** — **Sign in to the talent portal** (`talent.fintalent.io`) with the talent account.

   ![Talent portal sign-in screen](sdrx-ts-10-talent-login.png)

   *B2.1.1 — the Independent Consultant Sign In screen of the talent portal.*

2. **B2.1.2** — Open the **☰** menu (top left) → group **Work** → **Timesheet**. (Timesheet lives in the ☰ menu — it is not on the bottom navigation bar.)

   ![Work menu with Timesheet](sdrx-ts-17-talent-work-menu.png)

   *B2.1.2 — ① the Work group · ② the Timesheet entry.*

3. **B2.1.3** — **Pick the project to log against.** With **only one Active contract** the system **selects it for you** — the name shows in the top bar with an **Ongoing** label, nothing to do. With **several Active contracts**, **click that bar** to open the list and switch project; each project has its **own** calendar, totals and submission queue. Details in [B2.x.5 ↗](b2-x-5-several-projects.md).

   ![Project selector bar](sdrx-ts-18-talent-project-bar.png)

   *B2.1.3 — the project bar with its Ongoing label; with a single Active contract the system picks it automatically.*

4. **B2.1.4** — **Read the totals panel** before doing anything — these three numbers measure the whole flow: **The submitted line is a button, not a label.** The **›** on the right is easy to miss — click the line and the full **submission history** opens, which is the only place the talent can see what was actually locked in, day by day: The dialog also states the rule in the product's own words: *“**Hour(s) to bill** — the hours you're charging for. **You can bill less than you worked, never more.**”* That is the same constraint the admin side reads in [B3.2 ↗](b3-2-view-timesheets.md).

   | Line | What it means |
   |---|---|
   | **… submitted** | Total **hours to bill** locked in — **the number the money follows**. |
   | **Worked: …** | Total hours actually **logged**. Can exceed the submitted figure when the talent has billed less than they worked. |
   | **… pending submission** | Hours logged but **not yet submitted**. At **0h** the Submit button is greyed out. |

   ![Timesheet totals panel](sdrx-ts-01-talent-summary.png)

   *B2.1.4 — ① submitted = hours to bill · ② Worked = hours logged · ③ the Submit button, enabled only when hours are pending.*

   | In the dialog | What it gives you |
   |---|---|
   | **Timesheet date** From → To | Narrows the list to a period; the two totals above **recalculate for that period**. This is how you check a single billing round rather than the whole engagement. |
   | **Hour(s) worked** · **Hour(s) to bill** | The pair, side by side, for the selected range. |
   | One row per day | *Date · Hour(s) worked · Hour(s) to bill* — where the two figures diverge is visible immediately. |
   | **Export to CSV** | Downloads the same list. Use it to reconcile against an invoice, or to keep a record before the period rolls over. |

   ![Submission history opened from the totals panel](b2-28-timesheet-history.png)

   *B2.1.4 — ① the submitted line, clicked · ② the date filter · ③ both totals, recalculated for the filter · ④ the rule, stated in the dialog · ⑤ one row per day, worked next to to bill · ⑥ Export to CSV.*
