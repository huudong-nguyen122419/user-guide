# A6.0 · The rulebook

> A6 · Talent Active / Passive

**Read this once before you touch the queues.** Everything below is the rule as it was settled by manual review of the **276 PE/VC-labelled talents on production** on 27 Jul 2026. The steps in A6.3 are this rulebook turned into a click-by-click procedure; when the two ever disagree, this section wins.

#### The question the rule answers

Every talent record is either **supply** or **demand**. Someone who sits on the **buy side today** — they hold a role at a PE fund, or they run a company a fund owns — is a potential **client**, and Fintalent must never invite them into a project as a freelancer. They go **Passive**. Everybody else is **talent** and goes **Active**.

Passive is not a punishment and not a quality judgement. It is a routing decision: Passive records are excluded from project invitations, nothing more. Being wrong in either direction costs money — a wrongly-Passive freelancer is supply you cannot sell, a wrongly-Active fund Partner is an invitation landing in a client's inbox.

#### Rule 1 — the evidence, in strict order

Always work the four sources **in this order** and stop at the first one that answers. Later sources never overturn earlier ones. **Employment Status sits at the top, not the bottom** — it is a gate, not a tie-breaker.

| # | Source | Why it sits here |
|---|---|---|
| **1** | **Employment Status** | The **closing gate**. Full-time or Part-time means someone else already pays for their week, so they cannot take a project — **Passive**, and nothing in the title reopens it. Decides **22%** of the 276 production records. |
| **2** | **The job title** — the headline the talent wrote about themselves | Only reached once the gate is passed. It is what the talent says they do *now*, in their own words. Decides **78%** of records. |
| **3** | **Work experience** — description of the company named in the title | Only when the title is genuinely ambiguous. Read the company that appears in the title, not every job on the profile. |
| **4** | **One override** — a status an admin set by hand | Beats all three above. It is the **only** bypass. |

Company Background is not evidenceThe *PE / VC* label is a career-history label produced by AI, not a statement about today. Of the 262 people carrying it on production, only **16 (6%)** currently hold a role at a company flagged as a sponsor. Use the chip to **build the list** and never as the answer for an individual.

#### Rule 2 — read the role part only

Split the title at the first `at` / `@` / `chez` / `bei` / `en`. Everything **before** the split is the role; everything after is the employer. **Only the role part is matched**, for both the include and the exclude lists.

| Title | Role part matched | Why it matters |
|---|---|---|
| Manager at Fide **Partners** | `Manager` | Whole-string matching would score "Partners" from the fund name and wrongly make this a group B hit. |
| Managing Director and Founder at DZ **Consulting** | `Managing Director and Founder` | The advisory keyword sits in the **company name**, so it does not rescue them. This is a group B match → **Passive**. |
| **Independent Consultant** at Various | `Independent Consultant` | Here the advisory keyword is in the **role** → **Active**. |

#### Rule 3 — exclusions are a hard stop, and they run first

If the role part contains an exclusion term, the verdict is **Active** and the rule **ends there**. It does not fall through to the group tables. It is a hard stop *within the title*, so it never overturns the gate that already ran ahead of it.

Two buckets, one reason each: **too junior to hold a budget**, and **back office — never a buyer**.

**But the gate still comes first.** An Investment Banking Senior Analyst is not a client — and if they are **Full-time**, they are still **Passive**, because they are not available either. The exclusion list settles *are they a buyer*; the gate settles *can they take work at all*. Both must pass before someone is Active.

Match on **word boundaries**. Plain substring matching turns "M&A **Intern**ational Manager" into an intern and "Head of **Intern**ational Capital Partnerships" into a trainee.

#### Rule 4 — selling advice beats matching a group

An M&A advisory practice is exactly the supply Fintalent sells. When the role part contains `consultant`, `consulting`, `consultancy`, `advisory`, `advisor` or `adviser`, the verdict is **Active** even when the same title also matches a group. A "Principal **Consultant**" is a consultant, not a fund Principal; a "Private Equity **Consultant**" advises funds, they do not run one.

The mirror imageThe absence of an advisory word is just as decisive. "Partner and co-founder at EKEM Partners" and "Founding Partner at Scandola | Buy-side M&A" carry no advisory keyword, so the group B match stands and both are **Passive** — even though a human might argue they run advisory shops. If you disagree with a specific record, escalate it; do not bend the rule.

#### Rule 5 — buy-side vocabulary counts as a title match

This is the part that grew the most during manual review. Inside a list already narrowed to PE/VC backgrounds, a talent who describes themselves with **investing or deal vocabulary** is claiming the buy side, even without a formal job title. All of these were ruled **Passive** by hand:

| Title as written | Keyword that fires |
|---|---|
| *Investor* | `Investor` |
| *Private Equity chez IK Investment Partners* | `Private Equity` |
| *Wharton MBA, technology, private equity* | `Private Equity` |
| *|| Venture Capital || Product || Strategy* | `Venture Capital` |
| *Venture Investing & M&A* | `Investing` |
| *M&A / Investments / Buy&build* | `Investments` |
| *Strategic partnerships, JV, Business Development, M&A* | `M&A` |
| *Entrepreneur* · *Founder at InstaVal* | `Entrepreneur` · `Founder` |
| *Corporate Development & Strategy at Booz Allen Hamilton* | `Corporate Development` |
| *M&A International Manager at Swile* | `M&A` |

This net is deliberately wide, and it is **only safe inside the PE/VC-filtered list**. Applied to the whole talent base it would sweep up every banker and every corporate finance manager. Never run this keyword set without the Company Background chip in place.

#### Rule 6 — Employment Status is the closing gate, and it runs first

**Full-time Employee** and **Part-time Employee** both mean **Passive**, full stop. Somebody else already pays for their week, so they are not available for a Fintalent project — whatever their title says. Freelancer, Unemployed, Other and blank all pass the gate and go on to the title.

| Employment Status | Gate |
|---|---|
| **Full-time Employee** · **Part-time Employee** | **Passive** — stop here, do not read the title |
| Independent Consultant / Freelancer · Unemployed · Other · blank | pass — go on to the title |

Full-time and Active together is always wrongThe two fields contradict each other, so the record is broken by definition — you do not need to read the title to know it. On production there are exactly **two**: *Mehdi Benjelloun* (Investment Banking Senior Analyst) and *Sahib Maker* (Vice President at Apis Partners). Fix these before anything else in the queues.

**Do not confuse this gate with the automatic rule at approval.** They are different mechanisms that happen to agree most of the time. The gate above is the business rule you apply. The automatic rule — [A6.x.1 ↗](a6-x-1-in-review-queue.md) — fires on *Skip Review + an ongoing role at a flagged company* and does not read Employment Status at all; the one-line verdict printed on the profile does read it, but that line is only a display. Treating Full/Part-time as Passive is **settled business policy**, not something the system currently enforces on its own.

#### Rule 7 — one override, and only one

**A status an admin set by hand stays put.** Open *Activity Logs* before overturning anything: an entry with a named admin is a decision, and a decision outranks the rule. An entry with no actor, or no entry at all, is a default — the rule applies.

A completed contract is not an overrideIt used to be treated as proof that someone is talent. It is not: a full-time employee who delivered one project last year is still unavailable today. Contract history is **context for the reviewer**, never a reason to skip the gate.

#### The rule as one flowchart

| # | Test, in order | If it fires |
|---|---|---|
| **0** | An admin set the status **by hand** (Activity Logs) | **stop** — leave as is |
| **1** | **Employment Status is Full-time or Part-time** | **Passive**, stop |
| **2** | Role part contains an **exclusion** term | **Active**, stop |
| **3** | Role part contains an **advisory** term | **Active**, stop |
| **4** | Role part matches **group A, B or C** | **Passive**, stop |
| **5** | Title ambiguous → company named in the title is an advisory firm | **Active**, stop |
| **6** | Nothing matched | **Active** |

#### What the rule says about production today

Run over the 276 PE/VC-labelled records that currently sit at Active or Passive:

| Outcome | Count | Meaning |
|---|---|---|
| Status already correct | **178** | — |
| Active, should be Passive | **60** | clients able to receive project invitations — [Queue 2 ↗](a6-5-queue-2-active-passive.md) |
| Passive, should be Active | **33** | supply locked out of every invitation — [Queue 1 ↗](a6-4-queue-1-passive-active.md) |
| Exempt under rule 7 | **5** | a named admin set the status by hand |

The rule was validated against the **23 records classified by hand** on 27 Jul plus the gate ruling of 28 Jul, and reproduces all of them. That is the evidence it rests on — it is not proof it is right on the other 253, which is why every change still goes through a human read in A6.4 / A6.5.
