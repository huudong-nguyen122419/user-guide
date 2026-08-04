# 4b.x.9 · Create switches on with no time

> 4b · Schedule a call → 4b.x · Edge cases

**🐛 The Create button can switch on while the start time is still empty.** Reproduced every time. Open the form, fill the participant, then **touch the Date & time box without finishing it**, type the date but not the time, or click in and back out. **Create meeting** goes from greyed to clickable while the field is still blank, and the red *“Required — the meeting cannot be created without a start time”* line is **still on screen underneath it**. Click it and the request goes out with nothing in the time field. What comes back is not a friendly message. It is the raw server error: `BAD_USER_INPUT: Variable “$input” got invalid value null at “input.startTime”; Expected non-nullable type “FintalentDate!” not to be null.` **Nothing is booked**: the meeting count does not move. **Read the date box, not the button.** If the field looks empty, it is empty, whatever the button is doing.
