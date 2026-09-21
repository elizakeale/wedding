/* E & L Wedding — RSVP form.
 *
 * Three steps, revealed in order: party code, who's attending, dietary needs.
 * The last two stay hidden until a code comes back from the server, which is
 * both what the design asks for and what stops the page showing a form nobody
 * can meaningfully fill in yet.
 *
 * The guest list itself never ships with the site — this file only ever sends
 * a code and receives back the one party that matches. The site is a public
 * repo; the names live in the spreadsheet.
 *
 * One RSVP per code. The server is what enforces that (it re-checks inside a
 * script lock, so two people submitting the same code at once can't both get
 * through). Everything here is just the polite version of the same message.
 */
(function () {
  'use strict';

  // Paste the Apps Script /exec URL here. See rsvp-backend/README.md.
  var ENDPOINT = '';

  var form     = document.getElementById('rsvp-form');
  if (!form) return;

  var codeField = document.getElementById('party-code');
  var stepGuest = document.getElementById('step-guests');
  var stepDiet  = document.getElementById('step-diet');
  var guestList = document.getElementById('guest-list');
  var dietList  = document.getElementById('diet-list');
  var submitBtn = document.getElementById('rsvp-submit');
  var msg       = document.getElementById('rsvp-msg');
  var intro     = document.getElementById('rsvp-intro');

  var party = null;
  var busy  = false;

  function say(text, kind) {
    msg.textContent = text || '';
    msg.className = 'form-msg' + (kind ? ' form-msg--' + kind : '');
  }

  function reveal(on) {
    stepGuest.classList.toggle('is-hidden', !on);
    stepDiet.classList.toggle('is-hidden', !on);
    submitBtn.classList.toggle('is-hidden', !on);
  }

  reveal(false);

  /* ----------------------------------------------------------- rendering */

  function renderParty() {
    guestList.innerHTML = '';
    dietList.innerHTML = '';

    party.guests.forEach(function (g) {
      var id = 'g-' + g.id.replace(/[^a-z0-9]+/gi, '-');

      var row = document.createElement('label');
      row.className = 'guest';
      row.setAttribute('for', id);

      var box = document.createElement('input');
      box.type = 'checkbox';
      box.className = 'guest__box';
      box.id = id;
      box.checked = !!g.attending;
      box.addEventListener('change', function () {
        g.attending = box.checked;
        syncDiet();
      });

      var nm = document.createElement('span');
      nm.className = 'guest__name';
      nm.textContent = g.name;

      row.appendChild(box);
      row.appendChild(nm);
      guestList.appendChild(row);
      g._box = box;
    });

    syncDiet();
  }

  /* Dietary rows follow the checkboxes: you're only asked about people who
     are actually coming. */
  function syncDiet() {
    dietList.innerHTML = '';
    var coming = party.guests.filter(function (g) { return g.attending; });

    if (!coming.length) {
      var note = document.createElement('p');
      note.className = 'row__text diet__empty';
      note.textContent = 'Tick who’s coming above and we’ll ask about their dietary needs here.';
      dietList.appendChild(note);
      return;
    }

    coming.forEach(function (g) {
      var id = 'd-' + g.id.replace(/[^a-z0-9]+/gi, '-');
      var row = document.createElement('div');
      row.className = 'diet';

      var lab = document.createElement('label');
      lab.className = 'diet__name';
      lab.setAttribute('for', id);
      lab.textContent = g.name;

      var input = document.createElement('input');
      input.type = 'text';
      input.className = 'field diet__field';
      input.id = id;
      input.value = g.dietary || '';
      input.setAttribute('aria-label', 'Dietary restrictions for ' + g.name);
      input.addEventListener('input', function () { g.dietary = input.value; });

      row.appendChild(lab);
      row.appendChild(input);
      dietList.appendChild(row);
    });
  }

  /* ------------------------------------------------------------- lookup */

  function lookup() {
    var code = (codeField.value || '').trim();
    if (!code || busy) return;

    if (!ENDPOINT) {
      say('RSVP isn’t open yet — please check back soon.', 'error');
      return;
    }

    busy = true;
    say('Looking for you…');

    fetch(ENDPOINT + '?action=lookup&code=' + encodeURIComponent(code))
      .then(function (r) { return r.json(); })
      .then(function (data) {
        busy = false;
        if (!data.ok) {
          reveal(false);
          party = null;
          say(data.error || 'Something went wrong.', 'error');
          return;
        }
        party = data.party;
        renderParty();
        reveal(true);
        say(party.greeting || '');
        if (intro) intro.classList.add('is-hidden');
        stepGuest.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      })
      .catch(function () {
        busy = false;
        say('We couldn’t reach the server. Please try again in a moment.', 'error');
      });
  }

  // Enter in the code field looks the party up rather than submitting.
  codeField.addEventListener('keydown', function (ev) {
    if (ev.key === 'Enter') { ev.preventDefault(); lookup(); }
  });
  codeField.addEventListener('blur', function () { if (!party) lookup(); });

  /* ------------------------------------------------------------- submit */

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    if (busy) return;

    if (!party) { lookup(); return; }

    busy = true;
    submitBtn.disabled = true;
    say('Sending…');

    fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },  // avoids CORS preflight
      body: JSON.stringify({
        code: party.code,
        guests: party.guests.map(function (g) {
          return { id: g.id, attending: !!g.attending, dietary: g.dietary || '' };
        })
      })
    })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        busy = false;
        if (!data.ok) {
          submitBtn.disabled = false;
          say(data.error || 'Something went wrong.', 'error');
          return;
        }
        reveal(false);
        codeField.disabled = true;
        say(data.attending
              ? 'Thank you — we’ve got you down. See you in Kane’ohe.'
              : 'Thank you for letting us know — we’ll miss you.',
            'done');
      })
      .catch(function () {
        busy = false;
        submitBtn.disabled = false;
        say('We couldn’t reach the server. Please try again in a moment.', 'error');
      });
  });
})();
