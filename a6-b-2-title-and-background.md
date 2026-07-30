# A6-B.2 · List 2 — Active + PE/VC background

> A6-B · Identify PASSIVE talent

Finds clients hiding in the talent pool — people who sit on the buy side today. The rule behind it: [A6-B.0 rule 3](a6-b-0-the-rules.md).

## A6-B.2.1 · Open the Talents page and set three chips

**User Management → Talents.**

| Chip | Set it to |
|---|---|
| **Statuses** | `Active` |
| **Employee Statuses** | the **two options that are not Full-Time Employed** — `Independent Consultant / Freelancer` and `Business Owner / Partner / Boutique Owner` |
| **Company Background** | see the next step |

The chip is called **Employee Statuses** and is **not on the bar by default** — pin it with **+ Add filter**, see [A6-B.1.2](a6-b-1-employment-gate.md).

`Independent Consultant / Freelancer` also pulls Unemployed. Together with [List 1](a6-b-1-employment-gate.md) that covers everybody exactly once.

## A6-B.2.2 · Tick the Company Background boxes — parent AND children

Open the **Company Background** chip. The list starts with two catch-alls — *Has company background* / *No company background* — then the branches, each showing its child count in brackets.

Find **Private Equity / Venture Capital (5)** and **tick the parent box and all five children**. Then scroll to **Corporate / Industry (4)** and tick **PE-Backed / Portfolio Company** as well.

| Box | People on production |
|---|---:|
| **Private Equity / Venture Capital** *(the parent)* | 129 |
| Mega-Cap PE | 5 |
| Upper Mid-Market PE | 12 |
| Mid-Market PE | 115 |
| Venture Capital | 0 |
| Growth Equity | 2 |
| **PE-Backed / Portfolio Company** | **0** |
| **all six ticked together** | **133** |

**Ticking the parent alone gives you 129 and quietly loses four people** — they carry a leaf label without the parent. If your count comes out around 129–130 instead of 133, this is why: go back and tick every child box.

*PE-Backed / Portfolio Company* returns nobody. Tick it anyway — it is the right box for portfolio-company bosses and the day the data is fixed it will start returning people. It does not change today's total ([A6.x.6 ↗](a6-x-6-no-filter-finds-portfolio-company-bosses.md)).

Read the count above the table: **133**.

## A6-B.2.3 · Read the title — the part before "at"

Work down the list. For each row, look at the **title column** and mentally cut it at the first `at` / `@` / `chez` / `bei` / `en`. **Only the part before the cut counts.**

> *"Manager at Fide **Partners**"* → you judge `Manager`, not `Partners`. Fund names contain the word *Partners* constantly; reading the whole string turns half the list into false hits.

Ask four questions, in this order, and **stop at the first Yes**.

### Question 1 — is it junior, or back office?

`Associate` · `Analyst` · `Junior` · `Intern` · `Trainee` · `Student` · `MBA Candidate` · `Investor Relations` · `Fundraising` · `Fund Accountant` · `Taxation` · `Business Partner` *(full list in [A6-B.0](a6-b-0-the-rules.md))*

**Yes → not a client.** Skip the row.

### Question 2 — does the title say they sell advice, or sit sell-side?

`consultant` · `consulting` · `advisory` · `advisor` · `adviser` · **`investment banking`** · **`investment bank`** · `transaction services` · `due diligence` · `sell-side` · `interim manager`

**Yes → not a client.** Skip the row. These people are exactly what Fintalent sells.

> *"Vice President Technology & Services **Investment Banking**"* → skip. *"Vice President, M&A **Advisory**"* → skip. *"Principal **Consultant** at ADC Innovations"* → skip.

This question removes the largest slice of the list — 46 of 133. That is expected.

### Question 3 — is it a title that only exists inside a fund?

*Operating Partner* · *Operating Director* · *Portfolio Operations* · *Value Creation* · *Head of Talent* · *Talent Partner* · *General Partner* · *Venture Partner* · *Investment Partner* · *Investment Director* · *Investment Manager* · *Investment Professional* · *Deal Lead* *(full list in [A6-B.0](a6-b-0-the-rules.md))*

**Yes → client.** Write the row into the Passive queue. No further checking needed.

### Question 4 — is it a senior title that could be anywhere?

*Partner* · *Principal* · *Managing Partner* · *Managing Director* · *Vice President* · *VP* · *Director* · *CEO* · *CFO* · *Chair* · *President* · *Founder* · *Head of M&A* · *Corporate Development* *(full list in [A6-B.0](a6-b-0-the-rules.md))*

**Yes → you cannot decide from the title.** Go to [A6-B.2.4](#a6-b-2-4-check-the-employer-sub-rule-2).

**All four No → not a client.** Skip the row.

## A6-B.2.4 · Check the employer (sub-rule 2)

Only for rows that stopped at question 4. Open the talent, go to the work-experience list, and find the company **named in the title** — among the roles that are **currently ongoing**.

Full procedure and word lists: [A6-B.3 · Sub-rule 2](a6-b-3-sub-rule-2.md). In short:

| What you find | Verdict |
|---|---|
| The company name itself contains *Advisory* / *Consulting* / *Advisors* | **not a client** |
| Its description says it **is** an advisory / consulting firm | **not a client** |
| Its description says private equity, buyout, LBO, family office, asset manager | **client** → Passive queue |
| No company in the title · not among the current roles · no description · unclear | **needs a human read** — do not decide |

## A6-B.2.5 · Check the Timelines tab before you decide

Same as [A6-B.1.5](a6-b-1-employment-gate.md). Read the **transition in the parentheses**, not the name — every entry carries an admin name, including the automatic one. `(In Review → Passive)` alone means the system did it, so the row stays in the queue. Nothing in the log at all → also stays in the queue.

## A6-B.2.6 · Make the change on UAT

Full click path, dialog and traps: **[A6-B.4 · Set the status Active → Passive ↗](a6-b-4-set-status-on-uat.md)**.

The reason to type for this list — **name the employer**, the title alone will not explain the call six months from now:

```
Buy side — <title> at <company>. Client, not supply.
```

Pick **Other** in the radio group — the three preset reasons are about freelance verification and none of them fits.

---

## What this produced on production

| Question | | Count |
|---|---|---:|
| Three chips set | | **133** |
| Q1 · junior / back office | skipped | 18 |
| Q2 · advisory / investment banking | skipped | 46 |
| all four No | skipped | 39 |
| Q3 · fund-only title | **client** | **5** |
| Q4 · generic senior title | → employer check | 25 |
| &nbsp;&nbsp;· employer is a service provider | skipped | 9 |
| &nbsp;&nbsp;· employer confirmed buy-side | **client** | **3** |
| &nbsp;&nbsp;· evidence missing | **needs a read** | **13** |
| Timeline showed a hand-set change | | 0 |

**8 rows to the Passive queue · 13 to read by hand.**

## Queue → Passive (8)

| Talent | Title | Why |
|---|---|---|
| Florian · florian.pierre7@gmail.com | Private Equity Investment Manager | Q3 |
| François · francoisfrigara@gmail.com | Investment Manager \| ex-J.P. Morgan | Q3 |
| Gleb · golubtsovgs@gmail.com | Investment Manager / VP | Q3 |
| Luisa · luisawalz@icloud.com | Value Creation / Private investor support / VC&PE | Q3 |
| Mohamed · mohamedelgazzane@gmail.com | Investment Professional \| PE / M&A / Strategy | Q3 |
| Andrew · amueller@contourpointcap.com | Managing Partner at Contour Point Capital | employer: `private equity`, `buyout`, `sponsor` |
| Julius · juliusm1@gmail.com | CFO & Principal at Spring St. Group | employer: `family office`, `portfolio companies` |
| Jesús · jesus.dealvaro@alumni.ie.edu | Vice President at Arcano Partners | employer: `alternative asset`, `asset manager` |

## Needs a human read (13)

| Why you could not decide | Who |
|---|---|
| The title names no company | William · Alpay · Teddy · Pablo · Dana · Simon Petit |
| The company is only on a **past** role | Yassir *(Torch Partners)* · Valerian *(Cooltra)* |
| The company is not in the work experience at all | Simon Fedi *(Scandola)* |
| The company has no description | Mathias *(Sparring)* · Hawken *(Edgewater Strategy Group)* |
| The description reads either way | Peder *(Global PMI Partners)* · Renate *(Sapphire Partners)* |
