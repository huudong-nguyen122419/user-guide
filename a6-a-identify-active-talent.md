# A6-A · Identify ACTIVE talent

> A6 · Talent Active / Passive — **ON HOLD**

**This direction is not being worked.** Nothing here is a live procedure. It is recorded so the scope is explicit and so nobody assumes the Passive pool has been reviewed.

## What it would cover

Passive records that are really supply — freelancers and consultants shut out of every project invitation for no good reason.

## Why it is parked

The audit trail cannot tell us how those records became Passive.

Measured on production, 29 Jul 2026, over the 811 Passive records that are Freelancer / Unemployed / Other with a non-PE/VC company background:

| | Count |
|---|---:|
| Have a `TalentStatus` log entry | **22** |
| Have **no** log entry at all | **789** |

A sample of 105 of those 789, spread across signup years 2020 → 2026, was pulled with the type filter removed — the full history, every entry type:

| | Result |
|---|---|
| Talents with **zero** history of any type | **102 / 105** |
| Total entries found | 3, all `Login` |
| Earliest entry anywhere | **2026-04-26** |
| Entries before 2026-04-06 | **0** |

**The talent audit log only starts around April 2026.** For a record that went Passive before then, there is no way to tell whether an admin decided it or the automatic rule at approval did it.

So for the great majority of the Passive pool, "no log" means **unknown** — not "automatic", and not "safe to flip".

## What must be settled before starting

1. How to treat a Passive record with no log. Flipping it discards a human decision we cannot see; leaving it keeps supply locked out. Neither is free.
2. Whether the [automatic rule at approval](a6-x-1-new-sign-ups-to-approve.md) is a good enough proxy for "nobody reviewed this" once the log gap is accepted.

Until those are answered, **leave the Passive pool alone.**
