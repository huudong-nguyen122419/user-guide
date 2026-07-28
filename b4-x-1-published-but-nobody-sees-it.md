# B4.x.1 · Published but nobody sees it

> B4 · Publish a resource (Admin) → B4.x · Edge cases

**Published, and still nobody can find it.** The talent **Resources** page only lists resources that have a **Published At** date. Status alone is not enough. On UAT this is not hypothetical: **26** resources are Published, the talent page shows **18**, and the missing **8** are exactly the ones whose date is empty. They are not entirely gone — if they carry a **Display Page** they still show in that block, because the blocks do not check the date. So the resource lives on the Home page but cannot be found by searching. Counted on UAT: Home block **17**, Resources page **12** of those same 17. **What to do:** publishing today stamps the date automatically, so this is legacy or imported data rather than something you will create by accident. Spot them in the **Published** tab — a row with a status chip and **no date under it**. Fix by opening **Edit** and setting **Published At**.
