# A5.x.3 · Cancelled ≠ failed

> A5 · Manage a marketing email (Admin) → A5.x · Edge cases

**Cancelled ≠ failed.** In the example the queue reads **Delivered 1 and Cancelled 2** of 3 people. Cancelled rows were pulled before sending (unreviewed, suppressed, or lifecycle-excluded), they never hit the provider, so they don't count against the domain.
