# B4.4 · Publish it

> B4 · Publish a resource (Admin)

## B4.4.1 · Status defaults to Draft

, so a resource you just created is invisible to talents until you say otherwise. You can publish from inside the drawer (set **Status** → **Published**) or later from the row menu.

> **Status on its own does not make it visible**
>
> A resource shows on the talent **Resources** page only when it is **Published** and **Published At** is today or earlier. Publish something whose date is empty and it stays invisible ([B4.2.7 ↗](b4-2-create-one.md)).

## B4.4.2

From the list: row **⋮** → **Set Publish**. The menu always offers the **two statuses the resource is not currently in**, so what you see depends on the row:

| Row is | Menu offers |
|---|---|
| Draft | Edit/View Details · Copy Resource Link · **Set Publish** · **Set Archive** |
| Published | Edit/View Details · Copy Resource Link · **Set Draft** · **Set Archive** |
| Archived | Edit/View Details · Copy Resource Link · **Set Draft** · **Set Publish** |

![Row menu on a Published resource](res-08-rowmenu.png)

*B4.4.2: the row menu on a Published row: the two moves offered are Set Draft and Set Archive.*

## B4.4.3 · Confirm

The dialog names the resource, shows the status change as chips, and tells you what publishing means, *“It will be visible to users on the selected display page.”* If you left Display Page empty, read that as the Resources page.

![Publish Resource confirmation](res-09-publish.png)

*B4.4.3: ① what publishing does · ② Confirm.*

## B4.4.4 · You can also publish on the way in, and you do not have to

Leaving **Status** on its default **Draft** is perfectly normal: write the resource now, publish it later from the row menu above whenever it is ready. Nothing is lost by waiting. If you already know it should be live, set **Status** to **Published** on the create form ([B4.2.4 ↗](b4-2-create-one.md)) and skip the row menu entirely. Either way **Published At still needs a date**, or the resource is published and invisible ([B4.x.1 ↗](b4-x-1-published-but-nobody-sees-it.md)).
