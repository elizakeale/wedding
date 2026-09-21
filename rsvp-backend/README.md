# RSVP backend — Google Sheet + Apps Script

Twenty minutes of setup, zero cost, and the guest list stays a spreadsheet you can sort and filter.

## 1. Make the sheet

1. Go to <https://sheets.new> and name it **E&L Wedding RSVPs**.
2. Rename the first tab to **Guests** and give it this header row (row 1, exact spelling):

   | code | party_name | guest_id | guest_name | invited_events |
   |------|------------|----------|------------|----------------|
   | raza | The Raza Family | raza-1 | Sara Raza | all |
   | raza | The Raza Family | raza-2 | Hasnain Raza | all |
   | raza | The Raza Family | raza-3 | Child | all |

   One row per person. Everyone in a party shares the `code`; `guest_id` must be unique.
   Codes are matched case-insensitively — `RAZA` and `raza` both work.

The **Responses** and **Latest** tabs create themselves on the first submission:
`Responses` keeps every submission (an audit trail), `Latest` keeps one row per guest
with their current answer. Read `Latest` for headcounts.

## 2. Add the script

1. In the sheet: **Extensions ▸ Apps Script**.
2. Delete the starter `myFunction` and paste all of `Code.gs`.
3. **Save** (⌘S), then **Deploy ▸ New deployment**.
4. Gear icon ▸ **Web app**. Description: `RSVP v1`. Execute as: **Me**.
   Who has access: **Anyone**. ▸ **Deploy**.
5. Authorize when prompted (you'll get an "unverified app" screen — **Advanced ▸
   Go to project ▸ Allow**; it's your own script).
6. Copy the **Web app URL** — it ends in `/exec`.

## 3. Point the site at it

In `js/rsvp.js`, line 6:

```js
var ENDPOINT = 'https://script.google.com/macros/s/PASTE_YOURS_HERE/exec';
```

Commit and push. Until that line is filled in, the form tells guests RSVP isn't open yet.

## 4. Test before invites go out

1. Add a fake party to **Guests** (`code: test`, two guests).
2. Open the site, type `test`, check one guest, add a dietary note, submit.
3. Confirm a row landed in both **Responses** and **Latest**.
4. Re-enter `test` — the form should come back pre-filled with what you saved.
   That's what lets guests change their minds without emailing you.

## Re-deploying after an edit

Editing `Code.gs` does **not** update the live web app. After any change:
**Deploy ▸ Manage deployments ▸ pencil icon ▸ Version: New version ▸ Deploy.**
The `/exec` URL stays the same.

## What this does and doesn't protect

- Party codes are the only gate. Anyone with a code can see that party's names —
  the same exposure as the shared site password. Fine for a wedding, not a secret.
- The endpoint is public by necessity (a static site has no server to hide it behind).
  Someone who found the URL could submit noise; `Responses` keeps the history so
  nothing is lost if that ever happened.
- Use codes that aren't guessable from a name (`raza-4417`, not `raza`) if you want
  a little more friction.

## Making the codes

Once the guest list is final, ask Claude to generate the `Guests` tab from it —
one row per person, a shared code per party, short and easy to read aloud over the
phone. Paste the result straight into the sheet.
