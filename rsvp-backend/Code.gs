/**
 * E & L Wedding — RSVP backend (Google Apps Script)
 * ---------------------------------------------------------------------------
 * Bind this to YOUR EXISTING guest-list spreadsheet (Extensions ▸ Apps Script
 * from inside that sheet). It reads the guest tab in place — there is no
 * second copy of the guest list to keep in sync, and nothing about your
 * guests ever goes into the website repo, which is public.
 *
 * WHAT IT READS
 *   Your guest tab, found automatically by looking for a header row with a
 *   "Group ID" cell. Columns are matched by header name, so you can move them
 *   around. Expected headers: Main, Group ID, Email, Child?, Drinker?,
 *   Welcome BBQ?, Host, Group.
 *
 *   A blank Group ID means "same party as the row above" — which is how your
 *   sheet is already filled in. 135 people resolve to 72 parties that way.
 *   The first person in each party is its leader.
 *
 * WHAT IT WRITES (new tabs, in this same spreadsheet — your columns untouched)
 *   RSVP Responses  append-only log, one row per guest per submission.
 *                   Nothing here is ever edited or deleted, so you can always
 *                   see what was said and when, even after a party is reopened.
 *   RSVP Latest     one row per guest, the current answer. Read this for
 *                   headcounts.
 *   RSVP Parties    one row per code: locked, when it was submitted, count.
 *                   To let a party RSVP again, clear the LOCKED cell.
 *
 * DEPLOY
 *   Deploy ▸ New deployment ▸ Web app ▸ Execute as: Me ▸
 *   Who has access: Anyone ▸ copy the /exec URL into js/rsvp.js (ENDPOINT).
 *   After editing this file: Deploy ▸ Manage deployments ▸ pencil ▸
 *   Version: New version ▸ Deploy. The URL stays the same.
 */

var RESPONSES_TAB = 'RSVP Responses';
var LATEST_TAB    = 'RSVP Latest';
var PARTIES_TAB   = 'RSVP Parties';

// Header cell that identifies your guest tab. Change only if you rename it.
var CODE_HEADER = 'group id';


/* ---------------------------------------------------------------- helpers */

function ss_() { return SpreadsheetApp.getActiveSpreadsheet(); }

function norm_(v) { return String(v == null ? '' : v).trim(); }
function key_(v)  { return norm_(v).toLowerCase(); }

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function sheet_(name, headers) {
  var s = ss_().getSheetByName(name);
  if (!s) {
    s = ss_().insertSheet(name);
    s.appendRow(headers);
    s.setFrozenRows(1);
    s.getRange(1, 1, 1, headers.length).setFontWeight('bold');
  }
  return s;
}

/** Find the guest tab: the first sheet with a "Group ID" header cell. */
function guestSheet_() {
  var sheets = ss_().getSheets();
  for (var i = 0; i < sheets.length; i++) {
    var rows = sheets[i].getRange(1, 1, Math.min(10, sheets[i].getLastRow() || 1),
                                  sheets[i].getLastColumn() || 1).getValues();
    for (var r = 0; r < rows.length; r++) {
      for (var c = 0; c < rows[r].length; c++) {
        if (key_(rows[r][c]) === CODE_HEADER) {
          return { sheet: sheets[i], headerRow: r + 1 };
        }
      }
    }
  }
  throw new Error('No guest tab found — no sheet has a "Group ID" header.');
}

/**
 * Read the guest list into parties.
 * Blank Group ID continues the party above; first person in a party leads it.
 */
function loadParties_() {
  var found = guestSheet_();
  var values = found.sheet.getDataRange().getValues();
  var head = values[found.headerRow - 1].map(key_);

  function col(name) { return head.indexOf(name); }
  var cName  = col('main');
  var cCode  = col(CODE_HEADER);
  var cEmail = col('email');
  var cChild = col('child?');
  if (cName < 0 || cCode < 0) throw new Error('Guest tab needs "Main" and "Group ID" headers.');

  var parties = {};   // code(lower) -> { code, leader, guests: [...] }
  var current = '';

  for (var r = found.headerRow; r < values.length; r++) {
    var name = norm_(values[r][cName]);
    if (!name) continue;                       // skip spacer rows

    var code = norm_(values[r][cCode]);
    if (code) current = code;                  // a code starts a new party
    if (!current) continue;                    // nothing above it yet

    var k = key_(current);
    if (!parties[k]) parties[k] = { code: current, leader: name, guests: [] };
    parties[k].guests.push({
      id:    k + '|' + key_(name),             // stable across row reordering
      name:  name,
      child: cChild >= 0 ? norm_(values[r][cChild]) : '',
      email: cEmail >= 0 ? norm_(values[r][cEmail]) : ''
    });
  }
  return parties;
}

/** code(lower) -> { locked: bool, row: n } */
function partyState_() {
  var s = sheet_(PARTIES_TAB, ['code', 'locked', 'submitted', 'attending', 'party size', 'note']);
  var v = s.getDataRange().getValues();
  var out = {};
  for (var i = 1; i < v.length; i++) {
    var c = key_(v[i][0]);
    if (c) out[c] = { locked: key_(v[i][1]) === 'yes', row: i + 1 };
  }
  return out;
}


/* -------------------------------------------------------------------- GET */

/** GET ?action=lookup&code=XXXX */
function doGet(e) {
  try {
    var action = (e && e.parameter && e.parameter.action) || 'lookup';
    if (action !== 'lookup') return json_({ ok: false, error: 'Unknown action.' });

    var code = norm_(e.parameter.code);
    if (!code) return json_({ ok: false, error: 'Please enter your party code.' });

    var party = loadParties_()[key_(code)];
    if (!party) {
      return json_({ ok: false, error: 'We couldn’t find that code. Check your invitation, or text us.' });
    }

    var state = partyState_()[key_(code)];
    if (state && state.locked) {
      return json_({
        ok: false,
        locked: true,
        error: 'This code has already been used to RSVP. If you need to change your answer, email ' +
               'elizakeale@gmail.com and we’ll reopen it for you.'
      });
    }

    return json_({
      ok: true,
      party: {
        code: party.code,
        leader: party.leader,
        greeting: 'Found you — ' + party.leader + '’s party.',
        guests: party.guests.map(function (g) {
          return { id: g.id, name: g.name, child: g.child, attending: false, dietary: '' };
        })
      }
    });
  } catch (err) {
    return json_({ ok: false, error: 'Server error: ' + err });
  }
}


/* ------------------------------------------------------------------- POST */

/** POST { code, guests: [ { id, attending, dietary } ] } */
function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(25000);

    var body = JSON.parse(e.postData.contents);
    var code = norm_(body.code);
    if (!code || !body.guests || !body.guests.length) {
      return json_({ ok: false, error: 'Nothing to save.' });
    }

    var party = loadParties_()[key_(code)];
    if (!party) return json_({ ok: false, error: 'We couldn’t find that code.' });

    // Re-check the lock INSIDE the lock: two people submitting the same code
    // at once must not both get through.
    var states = partyState_();
    var state = states[key_(code)];
    if (state && state.locked) {
      return json_({
        ok: false, locked: true,
        error: 'This code has already been used to RSVP.'
      });
    }

    var valid = {};
    party.guests.forEach(function (g) { valid[g.id] = g.name; });

    var now = new Date();
    var responses = sheet_(RESPONSES_TAB,
      ['timestamp', 'code', 'leader', 'guest', 'attending', 'dietary']);
    var latest = sheet_(LATEST_TAB,
      ['code', 'leader', 'guest', 'attending', 'dietary', 'updated']);

    var latestValues = latest.getDataRange().getValues();
    var index = {};
    for (var i = 1; i < latestValues.length; i++) {
      index[key_(latestValues[i][0]) + '|' + key_(latestValues[i][2])] = i + 1;
    }

    var attending = 0;
    body.guests.forEach(function (g) {
      var id = norm_(g.id);
      if (!valid.hasOwnProperty(id)) return;          // ignore anything not on the list
      var name = valid[id];
      var yes = g.attending ? 'Yes' : 'No';
      if (g.attending) attending++;
      var diet = norm_(g.dietary).slice(0, 500);

      responses.appendRow([now, party.code, party.leader, name, yes, diet]);

      var k = key_(party.code) + '|' + key_(name);
      if (index[k]) {
        latest.getRange(index[k], 1, 1, 6)
              .setValues([[party.code, party.leader, name, yes, diet, now]]);
      } else {
        latest.appendRow([party.code, party.leader, name, yes, diet, now]);
        index[k] = latest.getLastRow();
      }
    });

    // Lock the party. Clearing the LOCKED cell in RSVP Parties reopens it.
    var parties = sheet_(PARTIES_TAB,
      ['code', 'locked', 'submitted', 'attending', 'party size', 'note']);
    var row = [party.code, 'YES', now, attending, party.guests.length, ''];
    if (state) {
      parties.getRange(state.row, 1, 1, row.length).setValues([row]);
    } else {
      parties.appendRow(row);
    }

    return json_({ ok: true, attending: attending });
  } catch (err) {
    return json_({ ok: false, error: 'Server error: ' + err });
  } finally {
    try { lock.releaseLock(); } catch (ignored) {}
  }
}


/* ------------------------------------------------------------------ check */

/**
 * Run this once from the editor (Run ▸ checkGuestList) before you go live.
 * It reads the guest tab and logs what the site will actually see, plus the
 * things worth fixing: parties whose leader has no email can't be sent a code.
 */
function checkGuestList() {
  var parties = loadParties_();
  var codes = Object.keys(parties);
  var people = 0, noEmail = [];
  codes.forEach(function (k) {
    people += parties[k].guests.length;
    if (!parties[k].guests[0].email) noEmail.push(parties[k].code);
  });
  Logger.log('%s people in %s parties', people, codes.length);
  Logger.log('Leaders with no email (%s): %s', noEmail.length, noEmail.join(', '));
  var locked = partyState_();
  Logger.log('Parties already locked: %s',
             Object.keys(locked).filter(function (k) { return locked[k].locked; }).length);
}
