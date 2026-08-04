# A5.x.2 · Force Send scope

> A5 · Manage a marketing email (Admin) → A5.x · Edge cases

**Force Send only reaches reviewed contacts.** Same rule as [A5.7.3 ↗](a5-7-run-force-send.md): people the SDR never marked **Content Reviewed** stay behind. A queue smaller than the People count usually means review, not a bug, check **People** before you chase it. **At zero reviewed the queue is not built at all**, and nothing on screen says why. The tab simply reads “No email queues yet”. Before treating a force send as broken, check the **reviewed** count in the Run dialog (A5.7.3).
