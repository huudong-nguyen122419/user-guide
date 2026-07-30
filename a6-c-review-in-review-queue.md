# A6-C · Review the In Review queue

> A6 · Talent Active / Passive — **the only live flow**

A new sign-up sits at `In Review`. An admin opens it, clicks **Approve**, and **the system sets Active or Passive by itself** using the five-question rule in [A6-C.6](a6-c-6-the-automatic-rule.md). Your job is to know what it will pick *before* you click, and to flip it afterwards if it picked wrong.

**Five steps, and that is the whole flow:**

| # | Step | Where |
|---:|---|---|
| 1 | Open the queue | A6-C.1 |
| 2 | Read the profile and decide for yourself | A6-C.2 |
| 3 | Hover **Approve Talent** — the tooltip names the status the system *will* set | A6-C.3 |
| 4 | Click **Approve** — the rule runs | A6-C.4 |
| 5 | *Edge case only:* the status is wrong → flip the chip by hand | A6-C.5 |

**Step 5 fires more often than it should.** The rule the system runs today is [A6-C.6](a6-c-6-the-automatic-rule.md), and it is known to get this wrong — it has **no seniority check**, so a junior at a flagged company comes out Passive. The replacement is [A6-C.7 · The rule being rebuilt](a6-c-7-the-rule-being-rebuilt.md).

**The default is Active.** A record only becomes Passive if a rule fires.

**Existing records are out of scope.** Nobody re-reviews the Active or Passive population by hand any more — a [migration](a6-b-identify-passive-talent.md) will do that. This page is the intake path only.

Production today: **2 records** sitting at In Review. UAT has **286**, which is where this page was walked end to end and where the rule was measured.

> Read on production, click on **UAT**.

## A6-C.1 · Open the queue

**User Management → Talents.** Top right of the list, the **N In Review** button. It opens the first profile straight into the drawer, with a pager **1 / N** and ‹ › arrows at the top right — that is how you step through the queue without going back to the list.

![Talents list controls](a6-01-filter-bar.png)

*A6-C.1 — ④ is the **N In Review** button.*

> **To work a specific slice instead**, filter the list normally: **Statuses = In Review** plus whatever else. On UAT, `In Review` + `Full-Time Employed` returns 36 of the 286 — and every one of those is a Q1 = Yes, so that slice is the fastest place to start.

## A6-C.2 · Decide, before you touch any button

You are reading **one profile**, not filtering a list — so there is no Company Background chip narrowing things for you. Read the profile directly and ask four questions in order. **Stop at the first Yes.**

> **Read the work-experience row, not the headline.** Every title question below is asked of the **position** on a role marked **current** — the job title on the row — and of that row's **company**. The sentence at the top of the profile is a self-description, and it matches none of the positions on **49%** of records. **No current role at all → ACTIVE**, immediately: there is nothing to test.

This is your yardstick for step 5. It is not a separate approval path — the system decides regardless of what you conclude here.

### Q1 · Employment Status says Full-time or Part-time?

It is on the header line of the profile, under the name and location: **`Employment Status: Full-Time Employed`**. The three values you will see are *Independent Consultant / Freelancer*, *Full-Time Employed* and *Business Owner / Partner / Boutique Owner*.

**Yes → PASSIVE.** Stop. Somebody else already pays for their week, so they cannot take a project whatever the title says.

> **The line is often not there at all.** On the UAT queue **76 of 286 (27%)** have no employment status — they reached In Review without finishing sign-up. The system reads that as "not Full-time" and waves them to **Active** without opening anything else, so **this is the one branch where the rule decides most often on the least evidence.** If the header line is missing, the position questions below are the only thing you have.

### Q2 · Does a current role's **position** say junior, back office, advisory or sell-side?

Read the **position** field on each row marked current. No cutting needed — the position is already just the role, and the company sits in its own field beside it.

* junior / back office — `Associate` · `Analyst` · `Junior` · `Intern` · `Trainee` · `Student` · `MBA Candidate` · `Investor Relations` · `Fundraising` · `Fund Accountant` · `Taxation` · `Business Partner`
* sells advice / sell-side — `consultant` · `consulting` · `advisory` · `advisor` · `adviser` · `investment banking` · `investment bank` · `transaction services` · `due diligence` · `sell-side` · `interim manager`

**Yes → ACTIVE.** Stop. These people are the supply Fintalent sells.

### Q3 · Is it a **position** that only exists inside a fund?

*Operating Partner* · *Operating Director* · *Portfolio Operations* · *Value Creation* · *Head of Talent* · *Talent Partner* · *General Partner* · *Venture Partner* · *Investment Partner* · *Investment Director* · *Investment Manager* · *Investment Professional* · *Deal Lead*

**Yes → PASSIVE.** Stop.

### Q4 · Is it a senior **position** that could be anywhere?

*Partner* · *Principal* · *Managing Partner* · *Managing Director* · *Vice President* · *VP* · *Director* · *CEO* · *CFO* · *Chair* · *President* · *Founder* · *Head of M&A* · *Corporate Development*

**Yes → the position cannot settle it. Do the [employer check](a6-b-3-sub-rule-2.md).** Stay on the same row — you already have its company — and read that company's name and description:

| | |
|---|---|
| Name or description says advisory / consulting / investment bank | **ACTIVE** |
| Description says private equity, buyout, LBO, family office, asset manager | **PASSIVE** |
| The row carries no company · no description · reads either way | **ACTIVE**, and note it — see below |

### All four No → ACTIVE.

> **Why missing evidence means Active here, and "needs a read" in [A6-B](a6-b-2-title-and-background.md).** In A6-B you are re-examining an existing record and can safely park it. Here the record cannot stay In Review — it has to leave the queue. Active is the safe default: a wrongly-Active new sign-up is one record to fix later, a wrongly-Passive one is a freelancer silently shut out from day one. Write these down so somebody can look again.

Full term lists: [A6-B.0](a6-b-0-the-rules.md). Note that [rule 1](a6-b-0-the-rules.md) does **not** apply here — a brand-new record has no admin decision behind it yet.

## A6-C.3 · Hover Approve Talent before clicking it

**The button tells you in advance what the system is about to do.** Hover **Approve Talent** and read the tooltip.

| Tooltip | The system will set |
|---|---|
| *"Talent status will change to Passive because this talent is a full-time employee"* | **Passive** — seen live on UAT |
| *"Talent status will be updated to Passive because the employee status is Freelancer and the talent is currently working at a &lt;sponsor / portfolio / corporate&gt; company"* | **Passive** |
| *"Talent status will be updated to Active"* | **Active** — seen live on UAT |
| *"This talent has been deleted"* | nothing — the record is deleted |

**Approving does not simply mean "Active".** There is no status picker in the dialog; the system decides and the tooltip is your only warning.

![The Approve Talent tooltip](a6-c-01-approve-tooltip.png)

*A6-C.3 — the tooltip on a Full-Time Employed record. Note the status badge still reads **In Review** and the header line reads **Employment Status: Full-Time Employed**.*

### Compare the tooltip against your own answer from A6-C.2

| | What to do |
|---|---|
| **They agree** | click Approve. Done |
| **They disagree** | click Approve anyway, then fix the status straight after — see A6-C.5 |

Two ways they routinely disagree, both worth knowing:

* **The system has no seniority check.** A `Analyst` or `Associate` holding a current role at a flagged company comes out **Passive**, where Q2 would leave them Active. This is the single biggest source of disagreement, and the reason the rule is being rebuilt ([A6-C.7](a6-c-7-the-rule-being-rebuilt.md)).
* **The system only looks at `Freelancer`.** Somebody whose Employment Status is *Unemployed* or *Other*, holding a current role at a fund, gets *"will be updated to Active"* — while Q3 says Passive.

> **The tooltip is a prediction, not a record of what happened.** It is computed in the browser from what is on screen, so verify with A6-C.5. It has been right on every record checked so far — three walked end to end on production on 30 Jul 2026, all three matched. What it never tells you is **which question fired**. The full five-question spine behind it is written out in [A6-C.6 ↗](a6-c-6-the-automatic-rule.md).

## A6-C.4 · Click Approve

The dialog is titled **"Do you want to approve this Talent?"** and repeats the name, **Email:** and **Title:** so you can check you are on the right record. The buttons are **Exit** (cancel) and **Approve**. There is no status choice in it.

![The approve confirm dialog](a6-c-02-approve-dialog.png)

To reject instead, use **Reject Talent** — the tooltip warns *"Talent status will be updated to Rejected"*. Rejected is a different outcome from Passive and is not part of this flow.

## A6-C.5 · Check what the system actually set, and fix it if needed

After approving, the record leaves the queue and the **Approve Talent / Reject Talent** buttons disappear from the toolbar — that is your signal it went through. The status chip becomes editable at the same moment.

Open the record again from the Talents list.

> **Walked end to end on UAT.** A record whose Employment Status was *Full-Time Employed*, tooltip *"will change to Passive because this talent is a full-time employee"* → clicked Approve → the chip came back **Passive**. The tooltip was right that time. Check anyway: it is computed in the browser, and it is the only warning you get.

1. **Read the status chip.** It now says Active or Passive.
2. **If it does not match your A6-C.2 answer, change it.** The chip is unlocked now — it was read-only while the status was In Review, which is exactly why this is a two-step job.
3. **Passive is needed but the system set Active** → follow [A6-B.4](a6-b-4-set-status-on-uat.md): click the chip, pick **Passive**, choose **Other** in the radio group, and type the reason.
4. **Active is needed but the system set Passive** → click the chip and pick **Active**.

Whichever way you correct it, the change is written to the timeline. From then on [rule 1](a6-b-0-the-rules.md) treats the record as **hand-set**, and later passes over the A6-B lists will leave it alone. That is the intended outcome — your decision is the one that sticks.

> **What the approval itself leaves behind.** It writes a timeline entry too, and it carries **your** name: *"&lt;you&gt; (Admin) changed talent status (In Review → Passive) by &lt;you&gt;"*, with `PASSIVE DATE`, `REFERRAL CODE` and `REFERRAL STATUS` in the detail block. Do not let that fool you later — the name does not mean a human chose the status. Only the transition does. See [rule 1](a6-b-0-the-rules.md).

> The **Timelines** tab count does not refresh on its own. Reload the page before reading it.

## Two other things that happen in this queue

| | |
|---|---|
| **A Passive talent resubmitting** | that is `ReviewPassive`, not `InReview`, and it has its own toolbar with three buttons — *Approve Review Passive*, *Reject Review Passive*, *Reject Talent*. See [A6.x.2 ↗](a6-x-2-a-passive-talent-resubmits.md) |
| **The status chip is locked while In Review** | you cannot pre-set the outcome. Approve first, correct after ([A6.x.10 ↗](a6-x-10-send-a-talent-back-to-in-review.md) covers the reverse direction) |
