# 4b.x.10 · “Not found” on a real contact

> 4b · Schedule a call → 4b.x · Edge cases

**🐛 “No matching contact found” on someone who *is* a contact.** [4b.x.3 ↗](4b-x-3-the-address-must-be-a-contact.md) covers the honest version of this guard. The address genuinely belongs to nobody. This is the other version: the address **is** on a contact record and the form still refuses it. Worked example: `dong@cyberhq.net`, `tin@cyberhq.net` and `long@cyberhq.net` all sit on real contacts and all three came back *“No matching contact found for this email”* with the button locked. A contact created minutes earlier was matched instantly. **Cause not established**: it is with the backend. **What to do meanwhile:** stop fighting the Meetings route and **book from the contact instead** ([4b.2 ↗](4b-2-book-the-call.md)). The 📅 icon on their row carries the address across for you and never asks you to type it, so this guard never fires.
