# 6.x.1 · A/B variants

> 6 · Manage a campaign → 6.x · Edge cases

**A/B variants.** Under any step, **+ Add variant** creates an alternative email (**A**, **B**, …) for that step, so you can test subject or copy. Each contact receives **one** of them (on the Preview the step reads *“A random option will be sent”*), so you can test subject / copy. **The split is a weighting, not a coin toss.** Each variant carries a **percentage weight**, and the weights on a step always add up to **100**, checked across **every step, 118 records, all summing to exactly 100**. One variant is `100`; two variants are `50` / `50`. So “random” means *drawn against the weights*, not *even by accident*. **Variants live inside a branch.** A sidestep gets its own **+ Add variant** per step, independent of the main sequence ([6.x.2 ↗](6-x-2-sidestep-conditional.md)). **Which address it sends from.** Every variant stores its own **From** address and **signature**, but the editor never shows either. Across **36 campaigns every campaign uses exactly one sender**, the owner’s address, so a variant does not change who the email comes from. **The risk sits on the owner:** reassign the campaign and the sender changes with it, silently, because nothing on screen names the address in use.

![A/B variants on a step](sdrx-camp-09-variants.png)

*6.x.1: Step 1 with two variants A and B.*

> **No control for the weight was found in the editor**
>
> The number exists on the record and is always an even split in the data, so whether it can be changed, and where, is **unverified**. Do not promise a client a 70/30 test until that is answered.
