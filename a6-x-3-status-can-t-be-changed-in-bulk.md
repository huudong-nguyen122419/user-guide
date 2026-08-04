# A6.x.3 · Status can’t be changed in bulk

> A6 · Approve a new talent (decides Active or Passive) → A6.x · Edge cases

**You cannot change status for several people at once, but two bulk actions still affect the result.** **Bulk Actions** offers Export PDF Talents, Add to list, Remove from list, Export Talents (CSV), **Set Skip Review**, **Set Require Review**, and nothing else. Every status change is one profile at a time; for a long list, **Add to list** first and split it between people. **Set Skip Review does not change the Active / Passive outcome.** It flips the talent's internal status to *Skip Review*, but that field is **not** part of the [automatic rule ↗](a6-a-6-the-rule-that-runs-today.md), confirmed 30 Jul 2026 by a record with no Skip Review that the system still set Passive at approval. Whatever else the two review flags do, they do not decide the status. **Set Require Review** is the opposite action.
