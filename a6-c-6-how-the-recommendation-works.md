# A6-C.6 · How the recommendation works

> A6 · Approve a new talent (decides Active or Passive) → A6-C · Review the In Review queue, LIVE

**What this is:** a rule that runs in the background on every talent and produces one recommended status plus one sentence saying why. It never changes anybody's status by itself. It appears in three places: the warning icon in the queue, the icon beside the status chip on the Talents list, and the **Recommend Status** filter.

## Five questions, in order, first Yes wins

The rule stops at the first question that answers Yes. Nothing after that point is read, which is why a profile can carry a flagged employer and a Full-time status and still be explained only by the first one.

| # | Question | Yes → | No → |
|---|---|---|---|
| **Q1** | Is any **current** role linked to a company in our database flagged as **Portfolio**, **Sponsor** or **Corporate**? | **PASSIVE**, stop | Q2 |
| **Q2** | Does a **current role title or company name** read as independent work? (keyword list below) | **ACTIVE**, stop | Q3 |
| **Q3** | Is **any** role on the profile marked as current? | Q4 | **ACTIVE**, stop |
| **Q4** | Is Employment Status **Freelancer**, **Unemployed** or **Other**? | **ACTIVE**, stop | Q5 |
| **Q5** | Is Employment Status **Full-time** or **Part-time** employee? | **PASSIVE**, stop | **ACTIVE** — the fallback |

Read the order, not just the answers**Q1 outranks everything.** A freelancer sitting in a current role at a sponsor is recommended Passive, because Q1 fires before the freelance wording at Q2 is ever read. And **Q3 is a gate, not a test**: no current role at all means nothing can mark the person passive, so the rule stops and says Active.

## The independent-work keywords at Q2

Matched against the **current role title** and the **company name**:

`freelance`, `freelancer`, `fractional`, `independent consultant`, `independent advisor`, `self-employed`, `interim`

## Every sentence the rule can print

Seven outcomes, no more. Each carries a code, and the code is what tells you which question fired:

| Code | Recommends | The sentence you see | Fired at |
|---|---|---|---|
| `ClientCompanyMatched` | **Passive** | currently works at a client company (portfolio, sponsor or corporate) | **Q1** Yes |
| `FreelanceKeywordMatched` | **Active** | the current role reads as freelance or independent | **Q2** Yes |
| `NoCurrentRole` | **Active** | no current role on the profile, so nothing marks them passive | **Q3** No |
| `NoEmployeeStatus` | **Active** | employment status was never answered, so availability is assumed | **Q4/Q5** blank |
| `EmployedFullTime` | **Passive** | employed full-time | **Q5** Yes |
| `EmployedPartTime` | **Passive** | employed part-time | **Q5** Yes |
| `NoPassiveSignal` | **Active** | self-directed, and nothing ties them to a client company | fallback, all five No |

🐛 The reasoning is recorded but never shownBehind each recommendation the system stores an **evidence list**, the actual facts it read, three or four lines long. A profile recommended Active carries lines like *“Employment status is Freelancer”*, *“1 current role on the profile”*, *“No freelance wording in any current job title or employer”*, *“No current role at a portfolio, sponsor or corporate company”*. **None of it reaches the screen.** The tooltip prints the one-line summary and stops, so the reviewer has to go and check by hand what the rule already checked. Worth asking for, since the work is already done.

Not every talent carries a recommendationSampled 800 records: **598 had no recommendation at all**, the field simply empty. Those are records the rule has not run against. An absent icon means *no opinion*, not *agrees with the current status*.
