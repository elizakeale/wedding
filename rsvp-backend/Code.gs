/**
 * E & L Wedding — RSVP backend (Google Apps Script)
 *
 * Sheet tabs expected in the bound spreadsheet:
 *
 *   Guests    | code | party_name          | guest_id | guest_name    | invited_events
 *             | raza | The Raza Family     | raza-1   | Sara Raza     | all
 *             | raza | The Raza Family     | raza-2   | Hasnain Raza  | all
 *             | raza | The Raza Family     | raza-3   | Child         | all
 *
 *   Responses | timestamp | code | guest_id | guest_name | attending | dietary
 *             (written by this script; one row per guest per submission)
 *
 *   Latest    | code | guest_id | guest_name | attending | dietary | updated
 *             (kept in sync — one row per guest, always the current answer)
 *
 * Deploy: Extensions ▸ Apps Script ▸ paste this ▸ Deploy ▸ New deployment ▸
 * Web app ▸ Execute as: Me ▸ Who has access: Anyone ▸ copy the /exec URL
 * into js/rsvp.js (ENDPOINT).
 */

var GUESTS_TAB = 'Guests';
var RESPONSES_TAB = 'Responses';
var LATEST_TAB = 'Latest';

function ss_() {
  return SpreadsheetApp.getActiveSpreadsheet();
}

function sheet_(name, headers) {
  var s = ss_().getSheetByName(name);
  if (!s) {
    s = ss_().insertSheet(name);
    s.appendRow(headers);
    s.setFrozenRows(1);
  }
  return s;
}

function rows_(name) {
  var s = ss_().getSheetByName(name);
  if (!s) return [];
  var values = s.getDataRange().getValues();
  if (values.length < 2) return [];
  var head = values[0].map(function (h) { return String(h).trim().toLowerCase(); });
  return values.slice(1).map(function (r) {
    var o = {};
    head.forEach(function (h, i) { o[h] = r[i]; });
    return o;
  });
}

function json_(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function normCode_(code) {
  return String(code || '').trim().toLowerCase();
}

/** GET ?action=lookup&code=xxxx — returns the party and any answers already saved. */
function doGet(e) {
  try {
    var action = (e.parameter.action || 'lookup');
    if (action !== 'lookup') return json_({ ok: false, error: 'Unknown action.' });

    var code = normCode_(e.parameter.code);
    if (!code) return json_({ ok: false, error: 'Please enter your party code.' });

    var guests = rows_(GUESTS_TAB).filter(function (r) {
      return normCode_(r.code) === code;
    });
    if (!guests.length) {
      return json_({ ok: false, error: 'We couldn’t find that code. Check the email, or text us.' });
    }

    var latest = {};
    rows_(LATEST_TAB).forEach(function (r) {
      if (normCode_(r.code) === code) latest[String(r.guest_id)] = r;
    });

    var partyName = String(guests[0].party_name || '').trim();

    return json_({
      ok: true,
      party: {
        code: code,
        name: partyName,
        greeting: partyName ? 'Found you — ' + partyName + '.' : 'Found you.',
        guests: guests.map(function (g) {
          var prev = latest[String(g.guest_id)];
          return {
            id: String(g.guest_id),
            name: String(g.guest_name),
            attending: prev ? String(prev.attending).toLowerCase() === 'yes' : false,
            dietary: prev ? String(prev.dietary || '') : ''
          };
        })
      }
    });
  } catch (err) {
    return json_({ ok: false, error: 'Server error: ' + err });
  }
}

/** POST {action:'rsvp', code, guests:[{id,name,attending,dietary}]} */
function doPost(e) {
  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(20000);

    var body = JSON.parse(e.postData.contents);
    var code = normCode_(body.code);
    if (!code || !body.guests || !body.guests.length) {
      return json_({ ok: false, error: 'Nothing to save.' });
    }

    var valid = {};
    rows_(GUESTS_TAB).forEach(function (r) {
      if (normCode_(r.code) === code) valid[String(r.guest_id)] = String(r.guest_name);
    });
    if (!Object.keys(valid).length) {
      return json_({ ok: false, error: 'We couldn’t find that code.' });
    }

    var now = new Date();
    var responses = sheet_(RESPONSES_TAB,
      ['timestamp', 'code', 'guest_id', 'guest_name', 'attending', 'dietary']);
    var latest = sheet_(LATEST_TAB,
      ['code', 'guest_id', 'guest_name', 'attending', 'dietary', 'updated']);

    var latestValues = latest.getDataRange().getValues();
    var index = {};
    for (var i = 1; i < latestValues.length; i++) {
      index[normCode_(latestValues[i][0]) + '|' + String(latestValues[i][1])] = i + 1;
    }

    body.guests.forEach(function (g) {
      var id = String(g.id);
      if (!valid.hasOwnProperty(id)) return; // ignore anything not on the list
      var name = valid[id];
      var attending = g.attending ? 'Yes' : 'No';
      var dietary = String(g.dietary || '').slice(0, 500);

      responses.appendRow([now, code, id, name, attending, dietary]);

      var key = code + '|' + id;
      var row = index[key];
      if (row) {
        latest.getRange(row, 1, 1, 6).setValues([[code, id, name, attending, dietary, now]]);
      } else {
        latest.appendRow([code, id, name, attending, dietary, now]);
        index[key] = latest.getLastRow();
      }
    });

    return json_({ ok: true });
  } catch (err) {
    return json_({ ok: false, error: 'Server error: ' + err });
  } finally {
    try { lock.releaseLock(); } catch (ignored) {}
  }
}
