# A6-C.7 · The business rule behind it

> A6 · Approve a new talent (decides Active or Passive) → A6-C · Review the In Review queue, LIVE

**What this is:** the same five questions as [A6-C.6 ↗](a6-c-6-how-the-recommendation-works.md), written as business reasoning rather than as a list of field reads. Use A6-C.6 to know *what the system will say*; use this to know *why the answer is the right one* when you are deciding a record by hand.

## The shape of it: somebody is Passive when their week already belongs to someone else

Everything reduces to one question. **Is there already a claim on this person's working time?** Two things count as a claim, and they are read in this order:

| The claim | Read at | Why it counts |
|---|---|---|
| **A current role at a company we work with** (Portfolio, Sponsor or Corporate) | **first** | the strongest claim there is. They are inside a client's organisation right now, so putting them on a project is a conflict before it is a scheduling problem |
| **An employment contract** (Full-time or Part-time) | **last** | somebody else buys their week. Nothing about the work is wrong, there is simply no time to sell |

Everything else is a reason to say **Active**: independent wording on the current role, no current role at all, a self-directed employment status, or nothing to go on.

The company flag decides, and nothing overrides itThis is the rule as it now stands, and it is a reversal. An earlier version of this section held that the flag was *necessary but not sufficient*, with junior titles and advisory employers able to veto it. **They no longer can.** A current role at a flagged company produces **Passive**, whatever the title says and whatever the person calls themselves. Read the consequence plainly: an **Analyst or Associate at a sponsor firm is now Passive**. Two records that were ruled Active by hand, *Iman Dakhlaoui* (Associate at a flagged employer) and *Athanasia Panteli* (Analyst), come out the other way under this rule. If that is wrong for the business, the fix is to change the rule, not to re-decide the records one at a time.

## The walk, in business terms

| # | What you are really asking | Answer |
|---|---|---|
| **1** | Are they sitting inside a client's organisation today? | Yes → **Passive**. Stop; nothing else matters |
| **2** | Does the current role describe itself as independent work? | Yes → **Active**. They sell their own time |
| **3** | Is there any current role at all? | No → **Active**. Nothing can hold a claim on them |
| **4** | Do they describe themselves as freelance, between roles, or something else? | Yes → **Active** |
| **5** | Are they employed full-time or part-time? | Yes → **Passive**. Otherwise **Active** |

Why the order is the whole designThe rule stops at the first Yes, so the order *is* the business decision. Putting the company flag first says: **where they work outranks what they call themselves**. Putting employment status last says: it is the weakest evidence, a self-reported field that is often stale or never filled in.

## The two vetoes that were dropped

The earlier design carried two exceptions that let a flagged employer be overruled. Neither is in the rule any more. They are still worth knowing, because **a reviewer deciding by hand can still apply them** and the recommendation will simply disagree:

| Dropped veto | What it used to say | Where it stands now |
|---|---|---|
| **Junior / back office** | an Analyst, Associate or intern at a flagged company is not a client contact, so keep them Active | no longer read. The flag wins. Definitions kept below as a judgement cue |
| **Advisory / sell-side employer** | somebody at a boutique advisory or investment bank is a peer, not a client | no longer read. It never fired in the seven validated records either |

The seven validated records need re-scoringThe table of seven live records that used to sit here was scored against the previous rule, and its step numbers no longer exist. **It has been taken out rather than left to mislead.** Two of the seven are known to flip to Passive under the current rule, *Iman Dakhlaoui* and *Athanasia Panteli*. The rest need re-running before anybody quotes them. **Re-running them is not a five-minute job:** the live system answers a different shape of this field from the one described in [A6-C.6 ↗](a6-c-6-how-the-recommendation-works.md), which means it is on a different build of the engine. The re-score has to be done where the business actually runs.

## How to read a company flag, and how not to

**The flag is `workExperiences[].linkedCompany.isSponsor` / `.isPortfolio` / `.isCorporate`, on a row with `ongoing = true`. Nothing else is a flag.** On screen: the **S / P / Corporate badge next to the company name in the Work Experience tab**. No badge means no flag.

These are NOT flags: do not read them as one **① *“CFO of VC-backed SaaS…”* in the role description**. That is text the talent typed about themselves. Syed Ishaque Hasib’s current employer reads exactly like a portfolio company and carries **no flag at all**. **② Company Background = `PE-Backed` / `Portfolio Company`**, an AI label inferred across the **whole career**, not a fact about today’s employer. Syed carries `PE-Backed (8 yrs)` from past roles. **③ the company’s own description**: only S6 reads a description, and S6 is still open. Getting this wrong is easy: on Syed’s record all three lookalikes say *portfolio company*, and the flag says nothing. **Check `linkedCompany` before concluding.**

**A shortcut that has held on 4 of 4 records checked:** the header line next to the status chip shows a green **Corporate** badge exactly when the current employer carries the flag. Arnaud and Athanasia have it; Syed and Mark do not, and neither of their current employers is flagged. Useful for a fast eye check, but confirm on the Work Experience row before acting on it.

## What counts as junior or back office

**Read the POSITION on the current row. It is authoritative.**

`Analyst`, `Associate`, `Junior`, `Intern`, `Internship`, `Trainee`, `Apprentice`, `Werkstudent`, `Working Student`, `Student`, `MBA Candidate`, `Teaching Assistant`, `Investor Relations`, `Fundraising`, `Fund Finance`, `Capital Formation`, `Fund Accountant`, `Fund Controller`, `Taxation` and `Business Partner`

Match on **word boundaries**, not substring. Plain substring turns *“M&A International Manager”* into an intern.

`seniorityLevel` cannot veto the position: settled on Athanasia PanteliHer record carries `seniorityLevel: "Manager"` while the current row reads `Senior FP&A Analyst`. **The position wins: `Analyst` fires, she is ACTIVE.** The enum is a whole-person label (`Analyst`, `Associate`, `Manager` and `Senior`) and it is demonstrably out of step here, 12 years’ experience labelled `Manager`, actually working as an Analyst. **Untested:** whether `seniorityLevel` being `Analyst` or `Associate` should fire S5 on its own when the position text does *not* look junior. No record has produced that combination yet.

This is [A6-C.7 ↗](a6-c-7-the-business-rule-behind-it.md) from our business rule, moved into the intake path, same list, but it now runs **at approval** and **before the company check**.

## Still open

| # | Question | Why it is open |
|---|---|---|
| **1** | Is a junior at a flagged company really Passive? | The rule now says yes. Two hand rulings said no. Somebody has to pick one, because the two cannot both stand |
| **2** | Should an advisory or sell-side employer still be an exception? | It was in the old design and never fired. Either write it into the rule or drop the idea |
| **3** | Company matching quality | Still the biggest risk. Roughly **63%** of talents have a current employer that was never matched to a company record, so question 1 cannot fire at all and they fall through to the weakest evidence. See [A6.x.5 ↗](a6-x-5-employer-missing-from-the-company-list.md) |
| **4** | Which build is the truth? | The five questions were read off one build. The live system answers a different shape of the same field, so the rule running against live records has not been confirmed to be this one |
| **5** | Blank employment status | No longer an early exit, it now falls to the Active fallback after the flag and the keywords have been read. Better than before, but it still means *assume available* on a field nobody filled in |
