# A6-C.7 · The rule as proposed

> A6 · Approve a new talent (decides Active or Passive) → A6-C · Review the In Review queue

Not built. This is a proposalNothing in this section runs anywhere. The rule in use is [A6-C.6 ↗](a6-c-6-the-rule-that-runs-today.md). Read this as the change being asked for, and as the reasoning behind it.

## The proposed order

| # | Question | Yes → | No → |
|---|---|---|---|
| **Q1** | Is any **current** role at a company flagged **Portfolio**, **Sponsor** or **Corporate**? | **Passive** | Q2 |
| **Q2** | Does a current role title or employer name indicate **independent work**? | **Active** | Q3 |
| **Q3** | Is any role marked as **current**? | Q4 | **Active** |
| **Q4** | Is Employment Status **Freelancer**, **Unemployed** or **Other**? | **Active** | Q5 |
| **Q5** | Is Employment Status **Full-time** or **Part-time**? | **Passive** | **Active**, fallback |

**Proposed keyword list for Q2:** `freelance`, `freelancer`, `fractional`, `independent consultant`, `independent advisor`, `self-employed`, `interim`. Note what is *not* in it: `remote` and `contractor`, both of which fire today, and bare `independent`, which is the source of the record-label false positive.

## What actually changes

The questions are nearly the same. **The order is reversed**, and since the rule stops at the first answer, the order is the decision:

|  | Runs today | Proposed |
|---|---|---|
| **Asked first** | Employment Status | Company flag |
| **Asked last** | Company flag | Employment Status |
| **Blank status** | early exit → **Active**, profile never opened | falls to the fallback, after the flag and the keywords have been read |

## The profiles that come out differently

| Profile | Today | Proposed |
|---|---|---|
| **Full-time employee**, no flagged employer | **Passive** at step 1 | **Passive** at Q5 — same answer, more work |
| **Full-time employee** at a flagged company | **Passive** at step 1 | **Passive** at Q1 — same answer, better reason |
| **Freelance wording** in the title, current role at a sponsor | **Active** — the keyword fires before the flag is read | **Passive** — the flag fires first |
| **Employment status blank**, current role at a sponsor | **Active** — decided on one empty field | **Passive** — the flag is read first |

The argument for the change, in one line**Where somebody works outranks what they call themselves.** A current role inside a client's organisation is a conflict before it is a scheduling problem, and it is a fact we hold in our own company data. Employment Status is the weakest evidence in the profile: self-reported, often stale, and blank on a large share of records. Today the weakest field is asked first and the strongest last.

## Decide these before it is built

| # | Question | Why it matters |
|---|---|---|
| **1** | Is a junior at a flagged company really Passive? | Under the proposal, an **Analyst or Associate at a sponsor firm becomes Passive**, because nothing overrides Q1. Two records were once ruled Active by hand for exactly this reason. The rule and those rulings cannot both stand |
| **2** | Should an advisory or sell-side employer be an exception? | Somebody at a boutique advisory is arguably a peer rather than a client. It has never been written into either rule |
| **3** | Do the loose keywords get fixed at the same time? | `remote` and `contractor` firing today, and bare `independent` matching company names, are wrong regardless of which order wins. Worth fixing whether or not the reorder happens |
| **4** | Blank employment status | The proposal stops treating it as an early exit, which is an improvement. It still ends at *assume available* on a field nobody filled in |
| **5** | Company matching quality | The biggest risk either way. Roughly **63%** of talents have a current employer never matched to a company record, so the flag question cannot fire at all for them. Putting it first makes that gap matter more, not less. See [A6.x.5 ↗](a6-x-5-employer-missing-from-the-company-list.md) |
