# B4.x.1 · Published but nobody sees it

> B4 · Publish a resource (Admin) → B4.x · Edge cases

**Published, and still nobody can see it. The date is a gate, not a label.** The talent Resources page shows a resource only when its **Published At is today or earlier**. Status alone is not enough, and the comparison is what matters: **Proved rather than assumed.** 27 Published, talent saw **19**. Took one visible resource, changed nothing but its Published At to **1 December**, and the talent count dropped to **18** with that resource gone from the list. Put the date back and it returned. The other 8 of the 27 have an **empty** date and are invisible for the same reason. The quickest way to see what a talent seesOn the admin list, pin the **Published Date** quick filter ([B4.1.3 ↗](b4-1-open-resources.md)) and set its **To** to **today**. What comes back is exactly the set on the talent Resources page, in the example above, that is the 19. Anything in the Published tab but not in that filtered list is published and unreachable. **But the placed blocks do not check the date at all.** A resource with a future or empty date still shows in its **Home** / **Project** / **Project Details** block ([B5.4 ↗](b5-4-where-the-blocks-appear.md)). Counted in one example: Home block **17**, of which only **12** are on the Resources page. So a talent can watch a video on their Home page and then fail to find it by searching. **What to do:** a future date is a legitimate way to line something up in advance, publish it and post-date it. An **empty** date is never deliberate: spot those in the **Published** tab as a row with a status chip and **no date under it**, and fix with **Edit**.

| Published At | Talent sees it? |
|---|---|
| **today or earlier** | **Yes.** |
| **a future date** | **No**: hidden until that day arrives. This is the scheduling behaviour, and it does work. |
| **empty** | **No.** Nothing to compare against, so it never passes the gate. |
