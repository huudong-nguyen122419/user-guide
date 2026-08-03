# A3.0 · Add contacts

> A3 · Run a ME / campaign

Do this before anything in A3.1A marketing email with no recipients cannot be run, and the People count is one of the two numbers the run check looks at ([A3.1.2 ↗](a3-1-run-a-marketing-email.md)). Verified end to end on UAT, 3 August.

## A3.0.1 · Start from the marketing email, not from Contacts

Open the ME → **People** tab. An empty one says so plainly, and tells you the only way in: *“No people yet — Contacts added to this marketing email via the Contacts V2 bulk flow will appear here.”*

![Empty People tab with the Add contacts button](me-50-people-empty.png)

*A3.0.1 — ① + Add contacts, top right of the tab · ② the empty state naming the bulk flow.*

## A3.0.2 · + Add contacts does not open a picker — it takes you to Contacts

You land on the full **Contacts** list with a filter already applied: a chip reading **Marketing Email : 1 excluded**. That chip is doing real work — it hides everyone already in this ME, so whatever you tick next is genuinely new. You have left the marketing emailThis is a normal Contacts page now. The full filter bar is yours — Lifecycles, Has signal, Countries, Work Experience, keyword search. Narrow the list here rather than ticking your way down 15,000 rows.

![Contacts pre-filtered to exclude this ME](me-51-prefiltered.png)

*A3.0.2 — ① the Marketing Email : 1 excluded chip · ② the row count you are working against.*

## A3.0.3 · Tick the contacts you want

A selection bar appears with the count, **Select all N matching** for the whole filtered set, and **Clear**. Of the actions on the right, the one you want is **Add to marketing email** — the neighbours add to a list or a campaign instead, and **Delete contacts** sits two buttons away.

![Selection bar with Add to marketing email](me-52-bulkbar.png)

*A3.0.3 — ① the count and Select all N matching · ② Add to marketing email.*

## A3.0.4 · The drawer is two panes, and both matter

It opens titled **Add N contacts to marketing email**. **Read the legend above the table** — *“☑ Tick to add · ◉ Email to send”*. Two different controls: the checkbox decides **whether** the contact goes in, the radio beside each address decides **which address** gets used. **What each bucket actually means — and when to tick it:** **When a contact has more than one address, the system has already chosen one.** It picks by priority — a **valid** address first, then one belonging to a **sponsor company**, and so on down. The chosen address carries the filled radio; any others sit under **Additional Emails**. **You can overrule it right here.** Click the radio next to a different address and that is where the email goes. Worth a look whenever someone has a work address and a personal one — the automatic pick is a sensible default, not a decision about which inbox this particular message belongs in.

| Pane | What it does |
|---|---|
| **Left — Select marketing email** | every ME you can reach, searchable and sortable. Each row shows **name · owner · status chip · N recipients**, so you can tell a Draft from something already sending before you pick it. |
| **Right — the contacts** | split into three buckets: **Valid** · **Missing + Invalid** · **Platform Signup**, each with its own count. **They are not a quality ranking** — which ones you tick depends on what the email is for. See below. |

| Bucket | What is in it | Tick it? |
|---|---|---|
| **Valid** | The safe ground. The address is confirmed working, so a send has a high chance of landing rather than being dropped. | **Yes** — pre-ticked for you. |
| **Missing + Invalid** | **Needs a human look.** The contact has an address, but nothing has ever been sent to it, so its reliability is unknown — unverified rather than proven bad. | **Your call.** Tick individually if you are willing to risk a bounce on that name; leave it if you would rather not spend the sender reputation. |
| **Platform Signup** | People who **already have a Fintalent account** — talent or client. Nothing to do with whether the address works. | **Depends entirely on the campaign.** See the rule below. |

| The email is aimed at… | Platform Signup | Why |
|---|---|---|
| **Talents** | **Tick all of them** | These are your talents. Leaving them out means mailing everyone except the audience. |
| **Prospective clients** | **Judgement call** | Having an account already suggests they may be a client. Whether that makes them a target or means you should leave them alone depends on the campaign — decide deliberately, do not let the default decide for you. |

![The add-to-marketing-email drawer](me-53-drawer.png)

*A3.0.4 — ① pick the ME (status and recipient count on every row) · ② the three buckets · ③ tick-to-add vs email-to-send · ④ the confirm button and the line above it.*

## A3.0.5 · ⚠ Read the button before you click it — it will not add everyone you ticked

Confirm reads **Add 2 of 6 contacts**, and directly above it: **Not ticked by default: 4 Missing + Invalid**. Only the **Valid** bucket is pre-ticked. Contacts with a missing or unusable address are carried into the drawer but left **unticked on purpose**, so selecting six people and adding two is the expected outcome, not a fault. Measured on UAT: six selected → `Valid 2 · Missing + Invalid 4 · Platform Signup 0` → button `Add 2 of 6 contacts`. **If you want the excluded ones anyway**, open the **Missing + Invalid** tab and tick them yourself — but fix the address first, or they will bounce ([7.7a ↗](7-7-verify-in-conversations.md)).

## A3.0.6 · Confirm, and read the toast

It names both the number and the email: **“Added to marketing email — 2 contacts added to M&A Executive Briefing - Berlin, October 2026.”** That is your receipt — the one moment the system tells you what actually went in.

![Success toast naming the count and the marketing email](me-54-toast.png)

*A3.0.6 — the toast, bottom left. It clears quickly, so read it as it appears.*

## A3.0.7 · Check the People tab

Go back to the ME — the **People** tab badge should carry the new total. If it does not match what the toast said, something was dropped; re-run the add rather than assuming it landed.
