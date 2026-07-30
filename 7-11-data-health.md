# 7.11 · Data Health — check before you send

> 7 · Manage a Marketing Email

A Marketing Email carries the same **Data Health β** tab as a campaign, and it works identically: open the tab, press **↻ Recompute live**, read the blocker banner, then work the Issues & Actions.

**Full description of every card and panel: [6.12 ↗](6-12-data-health.md).** Everything there applies here.

## The two things worth checking on an ME specifically

**Unbound merge tags.** An ME goes to the whole audience in one blast — there is no drip to catch a mistake on. The **EMAIL HEALTH → Unbound merge tags** row is the one that tells you a `{{variable}}` will not resolve. Anything other than `0` means somebody receives a broken sentence, and you find out after it has gone.

**Recently contacted · 7 days.** An ME is the easiest way to over-contact somebody who is already in a campaign sequence. This panel names the actual addresses.

## Read TOTAL CONTACTS here, not the People tab

Same caution as the campaign side. On one ME the **People** tab read **69** while **Email Queues** read **70**, with 70 distinct recipients and no duplicates — one person sat in the send queue without appearing in People.

The Data Health **TOTAL CONTACTS** card and the **People** column on the ME list are the numbers to trust. See [6.x.15 ↗](6-x-15-people-tab-undercounts.md).
