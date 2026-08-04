# A6-C.7 · The rule, rebuilt

> A6 · Approve a new talent (decides Active or Passive) → A6-C · Review the In Review queue, LIVE

⚠ Written against the previous engineThis section was worked out when the recommendation ran on a different set of questions. The engine now in place is the five in [A6-C.6 ↗](a6-c-6-how-the-recommendation-works.md). The business thinking below still stands, but **the seven validated records and the step numbers were checked against the old rule** and need re-running before anything here is built.

**Validated against 7 live records, all 7 agree.** This is the rule for the intake decision. The section above stays as the record of what the code does *today*: read that as *is*, this as *will be*.

## The shape of it: only two things make somebody Passive

This is the single most useful thing to hold in your head.

| **S1: employment status** is Full-time or Part-time | → **PASSIVE** |
|---|---|
| **S7. The current company carries a Mergermarket flag** | → **PASSIVE** |
| **everything else** | → **ACTIVE**, either as an exit or as the fallback |

**A job title never makes anybody Passive.** Titles only ever push *towards* Active (S4, S5) or pass through. A board seat, a C-suite title, `Head of`, `Managing Partner`, none of them decide anything on their own. **The flag decides.**

Ruled 30 Jul 2026, on Mark Cox`Director Board of Directors at Dollar Bank`, a board seat, 31 years’ experience, ex-investment-banking, group C on paper. Every title signal says client. **Dollar Bank carries no flag, so the answer is ACTIVE, and that is correct.** No board-member step was added. The title getting you all the way to S7 and then failing there is **the rule working as intended, not a hole**.

## Put precisely: the flag is necessary, not sufficient

After S1, a Passive verdict **requires** a flag, but a flag does not **produce** one. S4, S5 and S6 can each veto it. **A title can only ever veto; it can never trigger.**

| Title on the current row | Company flag | Result | Live case |
|---|---|---|---|
| freelance wording *(S4)* | **flagged** | **ACTIVE** | , |
| junior / back office *(S5)* | **flagged** | **ACTIVE** | Iman Dakhlaoui · Athanasia Panteli |
| advisory / sell-side *(S6)* | **flagged** | **ACTIVE** | *(never yet fired)* |
| nothing to veto with | **flagged** | **PASSIVE** | Arnaud Leblanc |
| nothing to veto with | no flag | **ACTIVE** | Syed Ishaque Hasib · Mark Cox |
| junior / back office | no flag | ACTIVE | , |

**So: had Dollar Bank carried a flag, Mark Cox would be PASSIVE.** His walk hits no veto: a board title is not freelance wording, not junior, and a retail bank is not advisory, so S7 is the only thing left deciding. **Iman is the mirror image: flagged employer, still Active**, because `Associate` vetoed at S5 before S7 ran. That single pair is the reason the step order is what it is.

## The walk

**S5 before S7 is the whole point of the rebuild.** Iman Dakhlaoui’s employer *is* flagged; test the flag first and a junior comes out Passive. **Order is load-bearing, not cosmetic.**

## The seven records it was validated on

| # | Talent | Stops at | Result | What the case proves |
|---|---|---|---|---|
| 1 | Thomas Tawse | **S3** | ACTIVE | no row marked current → nothing to test *(tooltip confirmed)* |
| 2 | Yakob Sarakhman | **S4** | ACTIVE | `independent` in the row’s **company** field *(tooltip confirmed)* |
| 3 | Iman Dakhlaoui | **S5** | ACTIVE | `Associate` exits **before** a flagged employer is read |
| 4 | Athanasia Panteli | **S5** | ACTIVE | `Analyst` in the position wins over `seniorityLevel: Manager` |
| 5 | Arnaud Leblanc | **S7** | **PASSIVE** | a `corporate` flag counts, same as sponsor |
| 6 | Syed Ishaque Hasib | **S7** | ACTIVE | company **not linked** → no flag → Active |
| 7 | Mark Cox | **S7** | ACTIVE | board seat + no flag → **Active is correct** |

Records 1–2 were checked against the system’s own Approve tooltip. Records 3–7 were decided by ruling.

**Four of the seven turn on S7**, and two of those four turn on the company simply not being linked. That makes S7 the most consequential step and **company matching quality the biggest risk in the whole rule**.

## How to read the flag at S7, and how not to

**The flag is `workExperiences[].linkedCompany.isSponsor` / `.isPortfolio` / `.isCorporate`, on a row with `ongoing = true`. Nothing else is a flag.** On screen: the **S / P / Corporate badge next to the company name in the Work Experience tab**. No badge means no flag.

These are NOT flags: do not read them as one **① *“CFO of VC-backed SaaS…”* in the role description**. That is text the talent typed about themselves. Syed Ishaque Hasib’s current employer reads exactly like a portfolio company and carries **no flag at all**. **② Company Background = `PE-Backed` / `Portfolio Company`**, an AI label inferred across the **whole career**, not a fact about today’s employer. Syed carries `PE-Backed (8 yrs)` from past roles. **③ the company’s own description**: only S6 reads a description, and S6 is still open. Getting this wrong is easy: on Syed’s record all three lookalikes say *portfolio company*, and the flag says nothing. **Check `linkedCompany` before concluding.**

**A shortcut that has held on 4 of 4 records checked:** the header line next to the status chip shows a green **Corporate** badge exactly when the current employer carries the flag. Arnaud and Athanasia have it; Syed and Mark do not, and neither of their current employers is flagged. Useful for a fast eye check, but confirm on the Work Experience row before acting on it.

## What counts as junior or back office at S5

**Read the POSITION on the current row. It is authoritative.**

`Analyst`, `Associate`, `Junior`, `Intern`, `Internship`, `Trainee`, `Apprentice`, `Werkstudent`, `Working Student`, `Student`, `MBA Candidate`, `Teaching Assistant`, `Investor Relations`, `Fundraising`, `Fund Finance`, `Capital Formation`, `Fund Accountant`, `Fund Controller`, `Taxation` and `Business Partner`

Match on **word boundaries**, not substring. Plain substring turns *“M&A International Manager”* into an intern.

`seniorityLevel` cannot veto the position: settled on Athanasia PanteliHer record carries `seniorityLevel: "Manager"` while the current row reads `Senior FP&A Analyst`. **The position wins: `Analyst` fires, she is ACTIVE.** The enum is a whole-person label (`Analyst`, `Associate`, `Manager` and `Senior`) and it is demonstrably out of step here, 12 years’ experience labelled `Manager`, actually working as an Analyst. **Untested:** whether `seniorityLevel` being `Analyst` or `Associate` should fire S5 on its own when the position text does *not* look junior. No record has produced that combination yet.

This is [A6-C.7 ↗](a6-c-7-the-rule-rebuilt.md) from our business rule, moved into the intake path, same list, but it now runs **at approval** and **before the company check**.

## Still open: do not build these until they are decided

| # | Question | Why it is open |
|---|---|---|
| **1** | **S2, blank employment status.** Active, or hold for a human? | **27%** of the In Review queue has this field empty. Today they are waved to Active on the strength of one unread field, the largest branch after the fallback. |
| **2** | **S6: advisory / sell-side employer.** Keep it, and on what evidence? | It is in the flow but **has never fired** in 7 records. Iman is the case it exists for, Finergreen is a boutique investment bank, but S5 got there first. A **senior** person at a sell-side boutique still needs S6. Sub-question: does S6 read the company *name*, its *description*, or a NAICS code? |
| **3** | **Company matching quality**: the biggest risk in the rule | Three faults in seven records, all at S7, the step that decides most often: Finergreen has **two records with different flags** and the row links to the wrong one; `Fin Edge` links to **nothing**; `Criteo` links to **HookLogic**, a subsidiary acquired in 2016. S7 is only as good as this. |
| **4** | **`ongoing = true` with a `to` date already in the past** | Mark Cox’s current row reads `from 1-1-2025, to 1-3-2026, ongoing = true`, four months past its end date. The UI trusts `ongoing` and shows *Until Now*. **Should S3 trust `ongoing` or `to`?** No verdict changed here, but it will elsewhere. |
| **5** | **The S4 word list** | Still not published by dev. `remote` and `independent` are the two named examples; `fractional` was found in the data (11 titles) and is in no list we hold. |
| **6** | `corporate`: drop it from S7? | **Decided 30 Jul 2026: it counts**, same as sponsor and portfolio. S7 asks only *is the company flagged at all*. |
| **7** | Board-seat step? | **Decided 30 Jul 2026 on Mark Cox: no.** A title never makes anybody Passive. The flag decides. |

**Not in scope here:** existing Active and Passive records are not re-reviewed by hand. That runs as a **the retired existing-records branch** later. This is the intake decision only.
