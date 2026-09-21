# RSVP backend — your existing guest-list sheet + Apps Script

Twenty minutes of setup, no cost, and no second copy of the guest list.

## The important bit first

**The guest list never goes into this repo.** The repo is public — it's what
GitHub Pages serves — so 135 names and email addresses in a file here would be
readable by anyone who found the URL. The script below reads your spreadsheet
server-side; the website only ever sends a code and gets back the one party
that matches it.

`.gitignore` blocks the obvious filenames as a backstop, but the rule is
simple: guest data lives in the sheet, not in the repo.

## 1. Attach the script to your sheet

1. Open your guest-list spreadsheet.
2. **Extensions ▸ Apps Script**.
3. Delete the starter `myFunction` and paste all of `Code.gs`.
4. **Save** (⌘S).

It finds your guest tab automatically by looking for the **Group ID** header,
and matches the other columns by name — `Main`, `Email`, `Child?`. You can
move columns around without touching the code.

## 2. Check it reads your list correctly

In the Apps Script editor: **Run ▸ checkGuestList**, then open the execution
log. You should see:

```
135 people in 72 parties
Leaders with no email (17): SABRINA, SHERRY, SAM, SABS, CONNOR, REED, MIKE, …
```

If the party count looks wrong, it's the Group ID column. A **blank** Group ID
means "same party as the row above", which is how your sheet is already filled
in — BAILEY repeats down four rows, whereas Cass's group leaves the cell empty
for Alessia and Carsten. Both work out to the same thing.

Those 17 leaders with no email are the ones you can't send a code to yet.

## 3. Deploy

1. **Deploy ▸ New deployment** ▸ gear ▸ **Web app**.
2. Description `RSVP v1`. Execute as **Me**. Who has access **Anyone**.
3. **Deploy**, and authorize when prompted — you'll get an "unverified app"
   screen, which is expected for your own script: **Advanced ▸ Go to project
   ▸ Allow**.
4. Copy the **Web app URL** (it ends in `/exec`).

## 4. Point the site at it

In `js/rsvp.js`, line 17:

```js
var ENDPOINT = 'https://script.google.com/macros/s/PASTE_YOURS_HERE/exec';
```

Until that's filled in, the form tells guests RSVP isn't open yet.

## 5. Test before any invitation goes out

1. Add a fake row to the guest tab: Main `Test Person`, Group ID `TESTME`.
2. Open the site, enter `TESTME`, tick the guest, add a dietary note, submit.
3. Check the three new tabs appeared: **RSVP Responses**, **RSVP Latest**,
   **RSVP Parties**.
4. Enter `TESTME` again — it should refuse, because the code is now used.
5. In **RSVP Parties**, clear the `locked` cell for TESTME. Try again — it
   should let you in.
6. Delete the fake row when you're done.

## What the three tabs are for

| Tab | What it is |
|---|---|
| **RSVP Responses** | Append-only log, one row per guest per submission. Never edited, never deleted — the full history, including anything submitted before you reopened a party. |
| **RSVP Latest** | One row per guest, current answer. **Read this for headcounts.** |
| **RSVP Parties** | One row per code: locked, when, how many attending. |

## Reopening a party

Someone will email saying they ticked the wrong box. In **RSVP Parties**, find
their code and clear the `locked` cell. They can now RSVP again, and their new
answer replaces the old one in **RSVP Latest** while both remain in
**RSVP Responses**.

## What this protects against, and what it doesn't

- **One RSVP per code** is enforced on the server, re-checked inside a script
  lock, so two people submitting the same code at the same moment can't both
  get through.
- **Party codes are the only gate.** Anyone with a code sees that party's
  names — the same exposure as the shared site password. Fine for a wedding,
  not a secret.
- **The endpoint is public by necessity** — a static site has no server to
  hide it behind. Someone who found the URL could submit noise against a code
  they knew. `RSVP Responses` keeps the history, so nothing is lost.
- Codes drawn from names (`BAILEY`, `DODGE`) are guessable by other guests. If
  that bothers you, add a couple of digits (`BAILEY-4417`) before sending them
  out — the script doesn't care what they look like.

## Two things in the sheet worth a look

- `edunkle14@gmail.con` — almost certainly meant to be `.com`.
- `PS100` as Allison's code, where every other code is a name. Works fine,
  just looks like a leftover.
