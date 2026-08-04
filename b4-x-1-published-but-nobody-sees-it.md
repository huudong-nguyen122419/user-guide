# B4.x.1 · Published but nobody sees it

> B4 · Publish a resource (Admin) → B4.x · Edge cases

**Published, but the talent still cannot see it? Check Published At.** A resource only reaches the talent **Resources** page once **Published At is today or earlier**. Setting the status to **Published** by hand does not get around that. So nothing is broken and there is nothing to chase. Open the resource, look at **Published At**, and either bring the future date back to today or fill in the empty one. **The placed blocks ignore the date.** A resource with a future or empty date still shows in its **Home** / **Project** / **Project Details** block ([B5.4 ↗](b5-4-where-the-blocks-appear.md)), which is how a talent can watch a video on their Home page and then fail to find it by searching.

| Published At | Talent sees it? |
|---|---|
| **today or earlier** | **Yes.** |
| **a future date** | **No.** It waits until that day, however you published it. |
| **empty** | **No.** There is nothing to compare against, so it never appears at all. |
