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

## B4.4.4 · You do not have to come through here at all

If you already know the resource should be live, set **Status** to **Published** and **Published At** to **today** while you are creating it ([B4.2.4 ↗](b4-2-create-one.md)), and it is live the moment you press **Create**. **Both fields**, a status with no date publishes nothing anyone can see. The route above is for anything that was saved as a **Draft**.
