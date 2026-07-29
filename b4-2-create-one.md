# B4.2 · Create one

> B4 · Publish a resource (Admin)

Click **Create New**, top right — a drawer opens over the list. Then work **down the form in order**, because the second field changes what the rest of it looks like.

![Create New button](res-03-create.png)

*B4.2 — Create New.*

## B4.2.1 · Title

**required**. This is what a talent reads on the card, so write it for them, not for the file.

## B4.2.2 · Resource Type

**Video** or **PDF**. **Set this before anything else.** It decides which fields exist below, and once the resource is saved you cannot change it ([B4.x.3 ↗](b4-x-3-type-is-locked-after-saving.md)).

| Type | What appears |
|---|---|
| **Video** | **Source** (required) + **Video URL** (required) |
| **PDF** | Source and Video URL **disappear**; **Upload PDF File** takes their place, required |

![Create Resource form, Video type](res-04-video.png)

*B4.2.2 — the two fields only Video has: ① Source · ② Video URL.*

![Create Resource form, PDF type](res-05-pdf.png)

*B4.2.2 — switch to PDF and Upload PDF File replaces them.*

## B4.2.3 · Source

(Video only) — where the video comes from. It changes what you have to supply:

| Source | What you do |
|---|---|
| **Youtube** | paste the video link into **Video URL**. |
| **Vimeo** | same — paste the link into **Video URL**. |
| **Internal** | **upload a video file from your own machine.** **Play it back in the drawer before you press Create** — that is the only moment you can catch the wrong file, and Resource Type is locked afterwards. |

## B4.2.4 · Status

what happens the instant you press **Create**. Default is **Draft**. Nothing here is one-way: all three statuses can be swapped later from the row menu ([B4.5 ↗](b4-5-edit-draft-archive.md)).

| Status | The moment you press Create |
|---|---|
| **Draft** | **Not on the talent portal.** Safe: keep editing, publish when you are happy. |
| **Published** | **Live immediately.** Talents can see it as soon as the drawer closes — so be sure it is right first. You can still edit it or change status afterwards. |
| **Archived** | **Not on the talent portal.** Goes to storage. Still editable, and you can move it back out. |

## B4.2.5 · Display Page

which talent screen also gets a block with this resource on it. Optional. **Leave it blank and nothing breaks:** the resource still shows up on the talent **Resources** tab like everything else — it just does not get an extra placement anywhere. Full breakdown of the three values in [B4.3 ↗](b4-3-decide-where-it-shows.md).

## B4.2.6 · Categories

how the resource is classified. Two values exist: **Profile Tips** and **Interview Prep**. You may leave it empty, pick one, or pick both. Worth filling in: **this is the only field a talent can filter on** in their Resources tab ([B5.2 ↗](b5-2-the-resources-page.md)). Empty means harder to find, not just untidy.

## B4.2.7 · Published At

the date on the card, and **the switch that decides whether a talent can see it at all**. **To schedule something, publish it and post-date it** — set **Status = Published** and **Published At** to the day you want it to appear. It stays out of sight until then and needs nothing further from you. Post-dating a Draft does nothing — the status never flips on its ownA future date on a **Draft** leaves it a Draft forever; there is no *Scheduled* status and nothing switches it over when the day comes. UAT has Drafts carrying dates well in the past, still sitting in Draft. **The date gates visibility; it does not publish.** So schedule with **Published + future date**, never with Draft + future date. Full consequences of the date, including the empty case, in [B4.x.1 ↗](b4-x-1-published-but-nobody-sees-it.md).

| You set… | What happens |
|---|---|
| **nothing** | publishing fills it in for you, whichever way you publish. Normal case. |
| **a past date** | visible immediately once the status is Published; the card just carries that date. |
| **a future date** | **held back until that day** — this is how you line a resource up in advance. |

## B4.2.8 · Description

a line or two under the title on the card. Optional; the card renders fine without it.

## B4.2.9 · Thumbnail

the picture on the card. Optional, and **what you get when you skip it is not the same everywhere**: A Youtube or Vimeo link does not bring its own pictureChecked on UAT with a published Youtube resource that has no thumbnail: neither the admin table nor the talent card pulls the video's cover image. The card is rendered as an empty placeholder — there is no `<img>` on it at all. **If you want a picture, upload one.**

| Left blank on… | Admin list | Talent card |
|---|---|---|
| **PDF** | a red **PDF icon** | plain grey **fintalent.com** placeholder |
| **Video** — any source | grey box with a **▶** | plain grey **fintalent.com** placeholder |

![PDF row with no thumbnail](res-22-thumb-pdf.png)

*B4.2.9 — PDF, no thumbnail: the admin table falls back to a PDF icon.*

![Video row with no thumbnail](res-21-thumb-video.png)

*B4.2.9 — Video (Youtube), no thumbnail: a grey box with a play symbol, not the Youtube cover.*

![Two talent cards with no thumbnail](res-23-thumb-talent.png)

*B4.2.9 — the same two on the talent side: ① the video · ② the PDF. Identical placeholder; only the badge tells them apart.*
