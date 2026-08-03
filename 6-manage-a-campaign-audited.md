# 6† · Manage a campaign — audited

> SDR

A decision-maker’s view of [Flow 6 ↗](6-manage-a-campaign.md) — what breaks, how often, and what to fix first. The step-by-step instructions stay on the flow page.

Measured on UAT · Sections 1–5

Every campaign on UAT read through the API and through its own health snapshot, then compared against what the screen prints. Scope: the campaign list, the People and Preview tabs, Email Queue, and Data Health β.

Headline finding **The number that blocks the Start button is roughly double the truth.** Data Health counts a cross-campaign overlap once by contact id and again by email address, then adds the two together — so the same person is counted twice. On `Corp Dev outreach — DD capacity (DACH)` the issue reads **15** while its own evidence list holds **8** contact ids: 8 by id + 7 by email = 15. **9 of the 10 campaigns** that carry this issue match the formula exactly. The only one that does not is the campaign where the email count is zero — nothing to double. Every SDR with an overlap is being blocked on an inflated figure.
