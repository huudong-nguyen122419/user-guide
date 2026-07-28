# A6.x.7 · Where the reason lives

> A6 · Talent Active / Passive → A6.x · Edge cases

**Where the Passive reason actually lives, and what the audit trail shows.** The reason you type is written to the **activity log**, not to a field on the talent record — the record's own `passiveReason` field stays empty. It surfaces in the tooltip on the status chip and in the *Passive since* panel. The **Activity Logs** tab is the audit trail. Each entry reads *“Admin <name> changed talent status to <status>”* with a timestamp. Two limits to know:

- A status set by the **automatic rule at approval** carries **no reason** — the entry only says the status changed.

- The entry for an approval reads *“approved talent review **(moved from Review Passive)**”* even when the talent was in **In Review**, not Review Passive. The wording is fixed, so do not read the previous status from it.
