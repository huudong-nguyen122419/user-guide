# 7† · Manage a Marketing Email — audited

> SDR

A decision-maker’s view of [Flow 7 ↗](7-manage-a-marketing-email.md) — what breaks, how often, and what to fix first. The step-by-step instructions stay on the flow page.

Measured on UAT · Sections 1–5

All 93 marketing emails on UAT read through the API and compared against what the list and the detail header print. Scope: the ME list, People, Preview, Inbox and Email Queues.

Headline finding **The rates on this page divide one unit by another.** The numerator counts *opens* — one person opening three times counts three — and the denominator counts *people*. So the Open Rate can exceed 100%, and does: **173.5%** on one live email, **132.1%** on another. Underneath it, **“delivered” has two counters that do not agree on 13 of the 20 emails that have an event log** — one reads 2,172 where the other reads 0; another reads 0 where the log reads 602. Nothing on the screen says which one you are looking at.
