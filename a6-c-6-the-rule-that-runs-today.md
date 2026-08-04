# A6-C.6 · The rule that runs today

> A6 · Approve a new talent (decides Active or Passive) → A6-C · Review the In Review queue

**What this is:** the rule behind every recommendation, read off the engine's own output rather than guessed at. It never changes anybody's status. It feeds the warning icon in the queue, the icon beside the status chip on the list, and the **Recommend Status** filter.

## Five steps, in order, and it stops at the first answer

| # | What it reads | Outcome |
|---|---|---|
| **1** | **Employment Status, and nothing else.** **Full-time** or **Part-time** employee → **Passive**. **Never answered** → **Active**. Anything else (Freelancer, Other…) → carry on | **decided here in most cases** |
| **2** | Is any role marked **current**? No → there is nothing that could hold them | **Active**, stop |
| **3** | Does a **current job title or employer** contain a freelance keyword? | **Active**, stop |
| **4** | Is a **current role** at a company flagged **portfolio**, **sponsor** or **corporate**? | **Passive**, stop |
| **5** | Nothing matched | **Active**, the fallback |

Step 1 decides most records without opening the profileThree of the seven outcomes are settled on that one field, and the engine says so in its own words: *“Profile was not examined — employment status alone decides this”* for a Full-time or Part-time employee, and *“Profile was not examined — this path skips every profile check”* when the field was never answered. The second one is the uncomfortable case. **A blank field produces Active**, so a talent who never finished sign-up is treated as available, and no current role, no employer and no company flag is ever looked at.

## Every outcome the rule can produce

Seven, no more. The code is what tells you which step fired:

| Code | Recommends | The sentence you see | Step |
|---|---|---|---|
| `EmployedFullTime` | **Passive** | employed full-time | **1** |
| `EmployedPartTime` | **Passive** | employed part-time | **1** |
| `NoEmployeeStatus` | **Active** | employment status was never answered, so availability is assumed | **1** |
| `NoCurrentRole` | **Active** | no current role on the profile, so nothing marks them passive | **2** |
| `FreelanceKeywordMatched` | **Active** | the current role reads as freelance or independent | **3** |
| `ClientCompanyMatched` | **Passive** | currently works at a client company (portfolio, sponsor or corporate) | **4** |
| `NoPassiveSignal` | **Active** | self-directed, and nothing ties them to a client company | **5** |

Across 418 live records carrying a recommendation: **Active 75%, Passive 25%**. The largest single outcome is the fallback at step 5. A further **382 of the 800 sampled had no recommendation at all**, so an absent icon means *no opinion*, not *agrees with the status*.

## The freelance keywords at step 3

Matched against the **current job title** and the **current employer name**. These are the ones seen firing, taken from the engine's own record of what it matched:

`independent` `freelan` `self-employed` `self employed` `remote` `contractor`

🐛 The match is loose, and it produces wrong answers **It matches inside words and inside company names.** `freelan` is a stem, so it catches freelance, freelancer and freelancing. `independent` matches on its own rather than only in *independent consultant*, which is how a talent whose employer is **“Independent Record Label”** comes out **Active**. An independent record label is a company, not a way of working. **And two of the keywords have nothing to do with being self-employed.** `remote` describes where somebody sits, not who pays them; a full-time employee working from home matches it. `contractor` is closer but still catches people on long contracts to a single client.

The reasoning is recorded, but never shownBehind each recommendation the engine keeps an **evidence list**, three or four lines naming what it actually read: the employment status, how many current roles, whether any keyword matched, which company was checked and what flag it carries. **None of it reaches the screen.** The tooltip prints the one-line summary and stops, so a reviewer re-does by hand the work the engine already did and wrote down.

## How to read a company flag, and how not to

**The flag is `workExperiences[].linkedCompany.isSponsor` / `.isPortfolio` / `.isCorporate`, on a row with `ongoing = true`. Nothing else is a flag.** On screen: the **S / P / Corporate badge next to the company name in the Work Experience tab**. No badge means no flag.

These are NOT flags: do not read them as one **① *“CFO of VC-backed SaaS…”* in the role description**. That is text the talent typed about themselves. Syed Ishaque Hasib’s current employer reads exactly like a portfolio company and carries **no flag at all**. **② Company Background = `PE-Backed` / `Portfolio Company`**, an AI label inferred across the **whole career**, not a fact about today’s employer. Syed carries `PE-Backed (8 yrs)` from past roles. **③ the company’s own description**: only S6 reads a description, and S6 is still open. Getting this wrong is easy: on Syed’s record all three lookalikes say *portfolio company*, and the flag says nothing. **Check `linkedCompany` before concluding.**

**A shortcut that has held on 4 of 4 records checked:** the header line next to the status chip shows a green **Corporate** badge exactly when the current employer carries the flag. Arnaud and Athanasia have it; Syed and Mark do not, and neither of their current employers is flagged. Useful for a fast eye check, but confirm on the Work Experience row before acting on it.

## What counts as junior or back office

A judgement cue, not a step**The rule does not read seniority at all.** An Analyst at a flagged company is recommended Passive like anybody else. The list below is here because a reviewer can still weigh it by hand, and because it is the exception most often argued for. If it should be part of the rule, that is a decision to take, not a reading to assume.

**Read the POSITION on the current row. It is authoritative.**

`Analyst`, `Associate`, `Junior`, `Intern`, `Internship`, `Trainee`, `Apprentice`, `Werkstudent`, `Working Student`, `Student`, `MBA Candidate`, `Teaching Assistant`, `Investor Relations`, `Fundraising`, `Fund Finance`, `Capital Formation`, `Fund Accountant`, `Fund Controller`, `Taxation` and `Business Partner`

Match on **word boundaries**, not substring. Plain substring turns *“M&A International Manager”* into an intern.

`seniorityLevel` cannot veto the position: settled on Athanasia PanteliHer record carries `seniorityLevel: "Manager"` while the current row reads `Senior FP&A Analyst`. **The position wins: `Analyst` fires, she is ACTIVE.** The enum is a whole-person label (`Analyst`, `Associate`, `Manager` and `Senior`) and it is demonstrably out of step here, 12 years’ experience labelled `Manager`, actually working as an Analyst. **Untested:** whether `seniorityLevel` being `Analyst` or `Associate` should fire S5 on its own when the position text does *not* look junior. No record has produced that combination yet.

This is [A6-C.7 ↗](a6-c-7-the-rule-as-proposed.md) from our business rule, moved into the intake path, same list, but it now runs **at approval** and **before the company check**.
