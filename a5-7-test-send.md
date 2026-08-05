# A5.7 · Test send

> A5 · Manage a marketing email (Admin)

A marketing email goes to everyone at once, and there is no recall. **Send it to yourself first** and read the copy that arrives, not the one in the editor. You are checking four things: that it leaves at all, that the whole email is there, that the attachment came with it, and that it is readable in a real mail client.

## A5.7.1 · Open the ME → Template tab

The button is **Test Send**, top right of the step. It only exists once the template has been written, so on a brand new ME you will not find it until there is a step to send.

![Test Send on the Template tab](admm-17-test-send-button.png)

*A5.7.1: ① the Template tab · ② Test Send, beside the 🗑 on the step · ③ the attachment, which is one of the things the test is for.*

## A5.7.2 · The drawer opens with the email already in it

Title **Send test email**, the subject underneath, the sending account at the top, and the full body with its attachment below. The only empty field is **To**, and **Send test email** stays greyed out until you fill it.

![The Send test email drawer before a recipient is added](admm-18-test-send-drawer.png)

*A5.7.2: ① To, empty, reading \*Add recipient…\* · ② the send button, greyed out until there is one.*

## A5.7.3 · Type an address you can actually open

Any address works: your own Gmail, your Outlook, a shared team mailbox. It does not have to be a Fintalent address and it does not have to exist in the system. Once the chip appears, the button turns solid. **You can add more than one**, and it is worth doing. Gmail, Outlook and a corporate mailbox do not render the same email the same way, and sending to all three at once shows you the differences side by side rather than one test at a time.

![The drawer with a recipient added](admm-19-test-send-filled.png)

*A5.7.3: ① the address as a chip, with an ✕ to take it off again · ② Send test email, now live.*

> **Do not test on a real contact**
>
> The field takes any address, including one belonging to a contact on the **People** tab, and **the email really is sent**. There is no test mode at the other end. A prospect would receive an unfinished email with the merge tags showing, from the campaign you were about to run properly. Use your own inbox.

## A5.7.4 · Now read the email that arrived, not the one on screen

This is the whole point of the step, so go through it deliberately: Anything genuinely wrong gets fixed on the **Template** tab and tested again. Only then move on to the run ([A5.8 ↗](a5-8-run-force-send.md)).

| Check | What you are looking for |
|---|---|
| It arrived | and in the inbox, not in spam. Spam on your own test is a warning about the domain, not about the copy. |
| The sender | **From** shows the account you meant to send as ([A5.x.4 ↗](a5-x-4-switch-sender-safely.md)). |
| The subject | complete, and not cut off in the list view. |
| The body | every paragraph present, spacing intact, no block silently dropped. |
| The attachment | there, and it opens. |
| The links | the booking link and any tracked link go where they should. |

![The test email as it arrives in Outlook](admm-20-test-send-received.png)

*A5.7.4: the same email in an Outlook inbox. ① the client has blocked part of the message, because the sender is not on its safe list · ② the picture, a grey placeholder · ③ the merge tags, arriving exactly as they are written in the template.*

> **The merge tags staying as text is the correct result**
>
> **A test send posts the template exactly as it is written.** It substitutes nothing, because there is no contact behind it to substitute from, so **{{contact.firstName}}** arrives as those characters. That is the difference between this and the **Preview** tab, which renders the email per person ([A5.8.2 ↗](a5-8-run-force-send.md)). Nothing to fix, and nothing to read into it.

> **The picture is worth one more click before you judge it**
>
> Outlook blocks remote content from senders it does not know and says so in the bar at the top, so a grey placeholder on the first look tells you nothing. **Click Show blocked content and look again.** In this test the bar went away and **the placeholder stayed empty**, so the image really had not come through. The block was not the reason. That is the whole value of the step: the template showed a file, the delivered email did not show a picture, and the only way to know was to receive one.

![The same email after Show blocked content](admm-21-test-send-unblocked.png)

*A5.7.4: after Show blocked content. ① the warning bar is gone · ② and the picture is still not there. Unblocking was not what was missing.*
