# A6.1 · Three fields

> A6 · Talent Active / Passive

1. **A6.1.1** — **Status** — the talent lifecycle field, 9 possible values: `Guest`, `Incomplete`, `PaymentRequired`, `InReview`, `Rejected`, `Active`, `Passive`, `ReviewPassive`, `Temp`. The status chip on a talent profile only lets you switch between **Active** and **Passive**; every other value is set by the system or by the review actions in [A6.x ↗](a6-x-edge-cases.md). The chip is **read-only** unless the current status is already Active or Passive.

2. **A6.1.2** — **Employment Status** — a different field, shown as a line of text on the profile: *Full-time Employee*, *Part-time Employee*, *Independent Consultant / Freelancer*, *Unemployed*, *Other*. This is what the legacy automatic rule reads. It is **not** the same as Status, and it is not evidence of who someone works for.

3. **A6.1.3** — **Company Background** — the filter chip formerly labelled *Classification*. It describes the **type of company a talent has worked at across their whole career**, inferred by AI from each employer, with a year count attached. It does not say where they work today. Someone who spent one year at a PE fund a decade ago still carries the *Private Equity / Venture Capital* label. Treat it as a way to **narrow the haystack**, never as the answer.
