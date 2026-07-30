# 6.x.15 · The People tab undercounts — trust the list column

> 6 · Manage a campaign → 6.x · Edge cases

**The People tab shows fewer people than the campaign actually targets, and the number changes depending on who is looking.**

Measured on one campaign on UAT, all four readings taken within minutes of each other:

| Where | Count |
|---|---:|
| **People** column on the campaigns list | **21** |
| **TOTAL CONTACTS** on the [Data Health tab](6-12-data-health.md) | **21** |
| `campaignTargets` in the API — *all active, none inactive* | **21** |
| **People** tab, opened by an **admin** | **18** |
| **People** tab, opened by the **SDR** who owns it | **17** |

The list column and the Data Health card agree with the database. Only the People tab disagrees — and it disagrees by a different amount for each role.

## Why it probably happens

Data Health on the same campaign breaks the audience down as **Healthy 0 · Degraded 14 · Critical 4**, and the Critical card adds **"+ 3 unknown"**.

`14 + 4 = 18` — exactly what the admin's People tab showed. The **3 contacts with no health tier are missing from the tab**. The SDR loses one more on top of that.

## What it means for you

**The campaign still sends to all 21.** The tab is the only thing that shrinks — the send does not.

So when you are reviewing *"who is going to get this"*:

* Read the count from the **list column** or the **Data Health** card, never from the tab header.
* If the tab count is lower than either, **some people in the campaign are invisible to you** — you cannot review, personalise, or skip them from this screen.
* Two people comparing notes on the same campaign will see different numbers. That is the tool, not a mistake either of you made.

Same shape of problem on Marketing Emails, where **People** read 69 while **Email Queues** read 70 with 70 distinct recipients.
