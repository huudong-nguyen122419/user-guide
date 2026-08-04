# A6† · Approve a new talent · audit

> ADMIN

A decision-maker’s view of the same rule documented in [A6 ↗](a6-approve-a-new-talent-decides-active-or-passive.md). What it costs when it is wrong, what to fix first, and what is still undecided. The operator’s view, with the click path, stays on the A6 page.

Validated on live records · Sections 1–7

Reverse-engineered from live behaviour, not from source. Scope: the admin app, `In Review` queue → **Approve Talent**, the moment the system chooses a status on its own, with no picker and no reason recorded.

Headline finding **A job title never makes anybody Passive.** After the employment-status gate, only a *Mergermarket flag on the current employer* can produce Passive, and a junior title vetoes even that. **The flag is necessary, not sufficient.** Which means the decision rests almost entirely on one lookup that fails quietly: **roughly 63% of talents have a current employer that was never matched to a company record**, and an unmatched company can never raise a flag. Every journey below treats that lookup as the load-bearing step.
