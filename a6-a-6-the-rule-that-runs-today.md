# A6-A.6 · The rule that runs today

> A6 · Approve a new talent (decides Active or Passive) → A6-A · Review the In Review queue

**What this is:** the rule behind every recommendation, read off the engine's own output rather than guessed at. It never changes anybody's status. It feeds the warning icon in the queue, the icon beside the status chip on the list, and the **Recommend Status** filter.

## Five steps, in order, and it stops at the first answer

| # | What it reads | Outcome |
|---|---|---|
| **1** | **Employment Status, and nothing else.** **Full-time** or **Part-time** employee → **Passive**. **Never answered** → **Active**. Anything else (Freelancer, Other…) → carry on | **decided here in most cases** |
| **2** | Is any role marked **current**? No → there is nothing that could hold them | **Active**, stop |
| **3** | Does a **current job title or employer** contain a freelance keyword? | **Active**, stop |
| **4** | Is a **current role** at a company flagged **portfolio**, **sponsor** or **corporate**? | **Passive**, stop |
| **5** | Nothing matched | **Active**, the fallback |

> **Step 1 decides most records without opening the profile**
>
> Three of the seven outcomes are settled on that one field, and the engine says so in its own words: *“Profile was not examined — employment status alone decides this”* for a Full-time or Part-time employee, and *“Profile was not examined — this path skips every profile check”* when the field was never answered. The second one is the uncomfortable case. **A blank field produces Active**, so a talent who never finished sign-up is treated as available, and no current role, no employer and no company flag is ever looked at.

## Every sentence the rule can print

Seven, no more. Whichever one you see on the tooltip, this is the step behind it:

| The sentence you see | It recommends | Decided at step |
|---|---|---|
| employed full-time | **Passive** | **1** |
| employed part-time | **Passive** | **1** |
| employment status was never answered, so availability is assumed | **Active** | **1** |
| no current role on the profile, so nothing marks them passive | **Active** | **2** |
| the current role reads as freelance or independent | **Active** | **3** |
| currently works at a client company (portfolio, sponsor or corporate) | **Passive** | **4** |
| self-directed, and nothing ties them to a client company | **Active** | **5** |

Not every talent carries a recommendation. Where the icon is missing the rule has no opinion on that record, which is **not** the same as agreeing with the status it already has.

## The freelance keywords at step 3

Matched against the **current job title** and the **current employer name**. These are the ones seen firing, taken from the engine's own record of what it matched:

`independent` `freelan` `self-employed` `self employed` `remote` `contractor`

> **🐛 The match is loose, and it produces wrong answers**
>
> **It matches inside words and inside company names.** `freelan` is a stem, so it catches freelance, freelancer and freelancing. `independent` matches on its own rather than only in *independent consultant*, which is how a talent whose employer is **“Independent Record Label”** comes out **Active**. An independent record label is a company, not a way of working. **And two of the keywords have nothing to do with being self-employed.** `remote` describes where somebody sits, not who pays them; a full-time employee working from home matches it. `contractor` is closer but still catches people on long contracts to a single client.

> **The reasoning is recorded, but never shown**
>
> Behind each recommendation the engine keeps an **evidence list**, three or four lines naming what it actually read: the employment status, how many current roles, whether any keyword matched, which company was checked and what flag it carries. **None of it reaches the screen.** The tooltip prints the one-line summary and stops, so a reviewer re-does by hand the work the engine already did and wrote down.

## How to read a company flag, and how not to

**The flag is the S / P / Corporate badge sitting next to the company name**, on a role with no end date. You see it on the talents list and in the **Work Experience** tab. **No badge means no flag**, and nothing else on the profile counts as one.

> **These are NOT flags: do not read them as one**
>
> **① *“CFO of VC-backed SaaS…”* in the role description**. That is text the talent typed about themselves. Syed Ishaque Hasib’s current employer reads exactly like a portfolio company and carries **no flag at all**. **② Company Background = `PE-Backed` / `Portfolio Company`**, an AI label inferred across the **whole career**, not a fact about today’s employer. Syed carries `PE-Backed (8 yrs)` from past roles. **③ the company’s own description**: only S6 reads a description, and S6 is still open. Getting this wrong is easy: on Syed’s record all three lookalikes say *portfolio company*, and the flag says nothing. **Check the linked company before concluding.**

**A shortcut that has held on 4 of 4 records checked:** the header line next to the status chip shows a green **Corporate** badge exactly when the current employer carries the flag. Arnaud and Athanasia have it; Syed and Mark do not, and neither of their current employers is flagged. Useful for a fast eye check, but confirm on the Work Experience row before acting on it.

## What counts as junior or back office

> **A judgement cue, not a step**
>
> **The rule does not read seniority at all.** An Analyst at a flagged company is recommended Passive like anybody else. The list below is here because a reviewer can still weigh it by hand, and because it is the exception most often argued for. If it should be part of the rule, that is a decision to take, not a reading to assume.

**Read the POSITION on the current row. It is authoritative.**

`Analyst`, `Associate`, `Junior`, `Intern`, `Internship`, `Trainee`, `Apprentice`, `Werkstudent`, `Working Student`, `Student`, `MBA Candidate`, `Teaching Assistant`, `Investor Relations`, `Fundraising`, `Fund Finance`, `Capital Formation`, `Fund Accountant`, `Fund Controller`, `Taxation` and `Business Partner`

Match **whole words**. Matching on part of a word turns *“M&A International Manager”* into an intern.

This is [A6-A.7 ↗](a6-a-7-the-rule-as-proposed.md) from our business rule, moved into the intake path, same list, but it now runs **at approval** and **before the company check**.
