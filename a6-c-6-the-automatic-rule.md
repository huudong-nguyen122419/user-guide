# A6-C.6 · The automatic rule, in full

> A6-C · Review the In Review queue

> ## Which rule is this page?
> **This page describes the system's rule — what the code does today, not what we think it should
> do.** It is the *current* rule, not a legacy one: verified against live production behaviour on
> three records on 30 Jul 2026, all three matched.
>
> **It is also known to be wrong**, and is being replaced. The rule that will take over is
> [A6-C.7 · The rule being rebuilt](a6-c-7-the-rule-being-rebuilt.md). Read this page as *is*,
> that one as *will be*.
>
> **Our business rule is a different document**: [A6-B.0](a6-b-0-the-rules.md) — hard-stop A
> (junior / back office), hard-stop B (advisory / sell-side), TIER 1 / TIER 2 titles, and the
> employer check that reads the company **description**. The system implements none of that.
>
> The two disagree, deliberately. *[Where it disagrees with our rule](#where-it-disagrees-with-our-rule)*
> below lists the four places, and the section after it measures the cost.

What the system decides for you the moment you click **Approve**. Five questions, walked top to
bottom, **first Yes ends the walk**. Fall off the bottom and you get the fallback.

Know this cold, because [A6-C.3](a6-c-review-in-review-queue.md) asks you to compare it against your own answer — and the tooltip on the Approve button only tells you the outcome, never which question produced it.

## The spine

```
Admin approves a talent out of review
│
├─ Q1  Employment status is Full-time or Part-time employee?
│        YES → PASSIVE            profile never examined
│  NO ↓
├─ Q2  Employment status is Freelancer, Unemployed or Other?
│        NO — blank → ACTIVE      fallback · profile never examined
│  YES ↓
├─ Q3  Any role on the profile marked current?
│        NONE → ACTIVE            fallback · nothing to test
│  AT LEAST ONE ↓
├─ Q4  Does a current role's POSITION or COMPANY NAME contain freelance wording?
│        YES → ACTIVE             exits before Q5
│  NO ↓
├─ Q5  Is a current role at a company linked in our database and
│      flagged portfolio / sponsor / corporate?
│        YES → PASSIVE            the only client-company route
│  NO ↓
└─ ACTIVE                         fallback · nothing proved them passive
```

**Only three inputs exist**: the employment status the talent picked at sign-up, the **position** and **company name** of their **current** work-experience rows, and whether those companies carry a portfolio / sponsor / corporate flag. Nothing else is read — not the profile headline, not the company description, not the contract history, not the applications.

## How many steps one talent actually walks

**Between one and five.** The cheapest paths cost a single field read; only the deepest path touches the company flags.

| Path | Steps walked | What it costs to evaluate |
|---|---:|---|
| Q1 → Passive | **1** | one field: employment status |
| Q2 → Active *(blank)* | **2** | one field |
| Q3 → Active *(no current role)* | **3** | employment status + count of current rows |
| Q4 → Active *(freelance wording)* | **4** | + read position & company of every current row |
| Q5 → Passive *(flagged company)* | **5** | + look up every current company's flags |
| Q6 → Active *(fallback)* | **5** | the full walk, nothing matched |

### Measured on the real queue

**286 In Review records on UAT** — the population this flow actually serves. Production carries only 2, so the shape cannot be confirmed there yet.

Employment status as picked at sign-up:

| Value | Count |
|---|---:|
| Freelancer | 170 |
| **(blank / never answered)** | **76** |
| Full-time Employee | 24 |
| Part-time Employee | 12 |
| Other | 3 |
| Unemployed | 1 |

Where the walk ended:

| Stopped at | Count | Share | Verdict |
|---|---:|---:|---|
| **Q1** full/part-time | 36 | 13% | Passive |
| **Q2** blank employment status | **76** | **27%** | Active |
| **Q3** no current role | 18 | 6% | Active |
| **Q4** freelance wording | 9 | 3% | Active |
| **Q5** flagged company | 35 | 12% | Passive |
| **Q6** fallback | 112 | 39% | Active |
| | | | **Passive 71 (25%) · Active 215 (75%)** |

**Three findings from that table:**

**① Q2 is not a corner case — it is the second-largest branch.** 76 records, **27% of the queue**, have no employment status at all and are waved straight to Active without the profile ever being opened. On the Active population on production the same field is never blank, so this is specific to intake: people reach the queue without finishing sign-up. On UAT many of these are obvious test rows, so treat 27% as the shape, not the exact production figure.

**② Q5 fires almost entirely on `corporate`.** Of the 35 records it sent to Passive: **33 corporate · 2 portfolio · 0 sponsor**. Not one sponsor was caught.

> **Ruled 30 Jul 2026: a `corporate` flag counts as flagged**, the same as sponsor and portfolio. An earlier version of this page called those 33 records errors, on the assumption that corporate was group D and out of scope. **That was wrong — they are correct verdicts.** What the split still tells you is that the check is, in practice, a *corporate* detector: the sponsor and portfolio branches almost never fire.

**③ Only 9 records reach Q4 at all**, and the words that fired were `independent` 6 · **`fractional` 2** · `freelance` 1 · `self-employed` 1. `remote` fired zero times. **`fractional` earning two hits on a 286-record queue is why it belongs in the list.**

## The three things worth knowing about each question

> **Different population.** The numbers below, and everything under *What it gets wrong*, come from the **276 existing Active PE/VC records on production** — the set the [migration](a6-b-identify-passive-talent.md) will cover, and the only set with hand verdicts to score against. The In Review queue measured above behaves differently: Q1 is smaller (13% vs 22%) and Q2-blank does not exist on production at all.

**Q1 is the whole ball game for employees.** It decides **60 of 276** records on production with a single field read, and the profile is never opened. There is no exception: applications, accepted invitations and completed contracts are all invisible here.

**Q3 is where a third of the audience escapes.** **90 of 276** records have no role marked current, so Q4 and Q5 find nothing and the walk falls through to Active. Nobody ever reads their title. *"M&A Professional"*, *"Investment Banking | Corporate Development"* — straight to Active.

**Q5 is the only route to Passive that involves a company**, and it is narrow twice over:

* An **unlinked** company can never answer yes. Roughly **63%** of talents have a current employer that was never matched to the company list ([A6.x.5 ↗](a6-x-5-employer-missing-from-the-company-list.md)).
* On the 276 PE/VC records, only **43** carry any flag on a current role — **15%**.

## What Q4 actually matches

The rule uses **substring matching on two fields of every current role**: that role's **position** and its **company name**.

> **Not the profile headline.** A talent has a profile-level `title` — the sentence they wrote about themselves — and each work-experience row has its own `position`. **Q4 reads the row, not the headline.** On the 172 production records with a current role, **85 (49%)** have a profile title that matches none of their positions: *"Investment Manager (Infrastructure Private Equity)"* on the headline, `Investment Leader` on the row; *"M&A and Corporate Finance Consultant | Interim Management"* on the headline, `Self-employed` on the row.
>
> Scored both ways, the rule lands on **exactly the same 169/276** — because Q4 is only an exit to Active, so moving a record between Q4 and the Q6 fallback changes nothing. **It does matter for our own rule**, which reads the title looking for buy-side signal: `Investment Manager` is TIER 1, `Investment Leader` is not.

> **The full word list is not published.** `remote` and `independent` are the two the flowchart names, as **examples**. Anything else in there is unknown to us, so treat Q4 as *"the system may exit to Active for a reason you cannot see"*. If a record you expected to reach Q5 came back Active, an unlisted Q4 word is the likeliest explanation.

The two named examples, checked against 1,087 production records:

| Keyword | Found | Verdict |
|---|---:|---|
| **`remote`** | **0 records** | matches nothing at all today. Harmless, but also doing no work |
| **`independent`** | 25 records | all 25 are genuinely self-employed — *Independent Consultant*, *Independent M&A Consultant*, *Independent Advisor at Trivona* |

**Substring versus whole-word makes no difference on today's data** — both settings match the same 35 records. So the substring choice is currently harmless.

> **`independent` matching board seats is no longer treated as a hole.** *Independent Director* and *Senior Independent Director* are board seats, and a substring match on `independent` exits them to Active at Q4 before the flag check runs. An earlier version of this page called that a latent bug. **Withdrawn 30 Jul 2026 on the Mark Cox ruling: a title never makes anybody Passive — only the company flag does** ([A6-C.7](a6-c-7-the-rule-being-rebuilt.md)). A board director whose employer carries no flag is **correctly** Active, whether Q4 exits early or the walk reaches the end. The substring behaviour is still worth knowing, because it changes *which step* fires, but not the verdict.

### What the list should contain

Mined from 1,087 production records — the counts are how often each appears in a title / in a current company name.

**Self-employment, the core of it**

| Term | title | company |
|---|---:|---:|
| `freelance` · `freelancer` · `freelancing` | 22 | 7 |
| `self-employed` · `self employed` · `selfemployed` | 4 | 6 |
| **`fractional`** | **11** | 0 |
| `contractor` | 2 | 0 |
| `interim manager` · `interim management` | 11 | 2 |
| `sole trader` · `sole proprietor` · `own business` | — | — |

**`fractional` is the find worth adding** — 11 titles use it (*Fractional CFO*) and it appears in no list anywhere in our own rules either.

**Two signals that are not words at all.** These are the ones a keyword list can never reach:

* **The company field is a placeholder, not a company.** 17 records. Match the *whole* string, case-insensitively: `Freelance` (6) · `Self-employed` (4) · `Freelancer` (3) · `Self-Employed` (2) · `Various` · `Independent` — plus `N/A`, `-`, `None`, `Me`, `Myself`, `Own`. People use the employer field to say "I work for myself".
* **The company name carries the person's own name.** 10 records. Compare tokens longer than two characters from `firstName + lastName` against the company name; any overlap means their own shop: *Martina Liggesmeier → `Martina Liggesmeier`* · *Simon Petit → `Petit & Co`* · *Bryan Yankton → `Yankton Partners LLC`* · *James Forsyth → `Forsyth Ventures Limited`* · *Dr. Marcus Niebudek → `DR. NIEBUDEK CONSULTING GmbH`*.

**Two guards to build in**

| Guard | Why |
|---|---|
| `independent` only when followed by *consultant / contractor / advisor / professional / expert / specialist*, or when it is the whole company string. **Reject** before *director* / *non-executive* | otherwise it swallows board seats — see the warning above |
| `interim manager` / `interim management` only — **never bare `interim`** | *Interim Manager* is supply; **Interim CFO** is group C C-suite and may well be a client |

Legal suffixes — `GmbH` (7/7), `LLC` (8/3), `Ltd` (2/2) — are **not** freelance signals on their own. A real fund is also a GmbH. They only mean something combined with the own-name rule.

### Widening Q4 buys precision, not coverage

Measured on the 276 records with hand verdicts:

| Q4 list | Wrongly Passive | Wrongly Active |
|---|---:|---:|
| self-employment only | 4 | **103** |
| \+ sells advice (`consultant`, `advisory`, `advisor`) | 3 | **103** |
| \+ sell-side (`investment banking`, `due diligence`, `sell-side`) | 2 | **103** |

Every widening step cuts wrongly-Passive and leaves wrongly-Active **completely unchanged**. That is structural: **Q4 is an exit to Active**, so widening it only reroutes people who were heading to Active anyway. Getting the list right is worth doing — just do not expect it to catch a single extra client.

## Where it disagrees with our rule

Four places, all deliberate on our side. This is what A6-C.5 exists to correct.

| | The system | [Our rule](a6-b-0-the-rules.md) |
|---|---|---|
| **Q1** | Full/Part-time → Passive, no exception | same starting position, and we now agree: **no escape hatch** |
| **Q4** | freelance wording only | our hard-stop B is much wider — `consultant` · `advisory` · `advisor` · `investment banking` · `due diligence` · `sell-side` · `transaction services` |
| **Q4** | no junior / back-office check at all | our hard-stop A drops `Analyst` · `Associate` · `Intern` · `Investor Relations` · `Fundraising` … |
| **Q5** | flag on **any** current role decides it | we read the **company named in the title** and we use the **description** as well as the flag. **On `corporate` we now agree** — it counts (ruled 30 Jul 2026) |

## What it gets wrong, measured

Scored against the hand verdicts on the 276 PE/VC production records:

| | |
|---|---:|
| Agrees with the hand verdict | **169 / 276 = 61%** |
| **Wrongly Passive** (blocked a freelancer) | **8** |
| **Wrongly Active** (let a client through) | **99** |

Where the walk ended: Q1 60 · **Q3 90** · Q4 33 · Q5 20 · Q6 fallback 73.

**All eight wrongly-Passive cases exit at Q5, and every one has a POSITION our own rule would have stopped first:**

| Talent | Position on the current role | Q5 said |
|---|---|---|
| Achraf Tamim | M&A **Analyst** | corporate |
| Aymeric Faure | Investment Banking **Analyst** | corporate |
| Loïc Gottwalles | Investment Banking **Analyst** | corporate |
| Yassine Zenagui | M&A **Analyst** · Senior M&A **Analyst** | corporate |
| Manaf Abdinov | Investment Banking **Associate** | sponsor |
| Pavlo Moshynskyy | **Associate** | sponsor |
| Laura Elkins | Operations **Advisor**: Marketing | sponsor |
| Sandrine Vergnory-Mion | Managing Partner | corporate |

Four `Analyst`, two `Associate`, one `Advisor`. Q4's list contains none of those words, so they all fall to Q5 and get flagged by their employer's tag.

**Adding hard-stop A and the advisory / investment-banking words to Q4 would fix seven of the eight.** Measured: widening Q4 that far cuts wrongly-Passive to 2, and dropping the `corporate` flag from Q5 as well cuts it to 1.

### Restricting Q5 to the company named in the title

Worth knowing, because the tag is often taken from a company the talent is not presented as working at — on the 276, **18 of 43 tag hits (42%)** came from a different company than the one in the title. Restricting Q5 to the title's company scores:

| Q5 scope | Wrongly Passive | Wrongly Active |
|---|---:|---:|
| any current role *(as built)* | 8 | **99** |
| only the company named in the title | **5** | **103** |

So it trades three fewer wrong blocks for four more clients let through. Roughly neutral on the total, but **more defensible** — a tag on a company nobody claims to work at is not evidence about them.

The 99 wrongly-Active cases are a different problem and no word list can fix them: **the rule never reads the title looking for buy-side signal.** Q4 reads the title only to find an exit. So a client whose employer is unlinked, or who has no current role, walks through untouched.

## Worked example — the two rules disagreeing, on a live record

**Iman Dakhlaoui** (`iman.dakhlaoui@gmail.com`), production, approved 29 Jul 2026, currently
**Passive**. 7 years' experience, Paris, rate filled in, available for more than 40 hours a week.

| | |
|---|---|
| `employeeStatus` | `Freelancer` |
| `internalStatus` | `null` — **no Skip Review** |
| current role | position `M&A and Project Finance Associate` at `FINERGREEN`, flagged **corporate** |

**The system's walk:** Q1 not full-time → Q2 is Freelancer → Q3 one current row → Q4 no
freelance wording → **Q5 corporate flag → PASSIVE.** Five steps. That is the status the record
carries today.

**Our rule says ACTIVE, for two independent reasons:**

1. **`Associate` is hard-stop A** — too junior to be a client. The system has no junior check.
2. **Finergreen is a boutique investment bank** — its own company description reads *"a boutique
   investment bank dedicated to the energy transition with in-depth expertise in M&A and complex
   financing"*. That is hard-stop B, sell-side. The system reads the **flag**, never the description.
~~3. The flag that fired is `corporate` — group D, out of scope.~~ **Withdrawn 30 Jul 2026: `corporate` counts as flagged.** Iman comes out Active on reasons 1 and 2 alone, and only because the seniority check runs **before** the flag check — see [A6-C.7](a6-c-7-the-rule-being-rebuilt.md).

**And a data fault underneath it.** Production carries **two** FINERGREEN company records: one typed
`Public Corporation` with **no flags** and the correct investment-bank description, and one typed
`Asset Management` with `isCorporate = true` and a vaguer *"consulting services"* description. The
work-experience row is linked to the second. **Had it linked to the first, Q5 would not have fired
and the system would have said Active** — so the outcome turned on which duplicate got matched,
not on any fact about the company. See [A6.x.8 ↗](a6-x-8-a-company-can-be-tagged-wrongly.md).

**The timeline reads like a human decision and is not one.** One entry:
*actorName* **Bernhard Thalhammer (SuperAdmin)**, but `prevValues.status = InReview` →
`nextValues.status = Passive`. The transition is `InReview → Passive`, so this is the automatic
rule, stamped with the approving admin's name. Read the name instead of the transition and you would
wrongly conclude somebody weighed this up. See [rule 1](a6-b-0-the-rules.md).

**This also settles Skip Review.** `internalStatus = null` and the system still went Passive, so the
Passive branch does **not** need Skip Review. The five questions are the whole rule.

## How to use it

1. Answer Q1–Q4 of [A6-C.2](a6-c-review-in-review-queue.md) yourself first, on your own rule.
2. Hover **Approve Talent** and read the predicted outcome.
3. If they differ, approve anyway — then fix the status straight after, per [A6-C.5](a6-c-review-in-review-queue.md).

The two disagreements you will hit most often: a **junior title at a flagged company** (system says Passive, we say Active) and a **client at an unlinked company** (system says Active, we say Passive).

**That correction is the only manual step left in this flow.** Everything before it is the system's five questions; the admin's job is to read the prediction, approve, and flip the chip when the prediction is wrong. No list to build, no batch to work.

