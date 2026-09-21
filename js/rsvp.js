/* E & L Wedding — RSVP form
 * Backend: Google Apps Script web app (see rsvp-backend/README.md)
 * Set ENDPOINT to the /exec URL after deploying.
 */
(function () {
  'use strict';

  var ENDPOINT = ''; // e.g. 'https://script.google.com/macros/s/AKfyc.../exec'

  var form = document.getElementById('rsvp-form');
  if (!form) return;

  var codeInput = document.getElementById('party-code');
  var stepGuests = document.getElementById('step-guests');
  var stepDiet = document.getElementById('step-diet');
  var guestList = document.getElementById('guest-list');
  var dietList = document.getElementById('diet-list');
  var submitBtn = document.getElementById('rsvp-submit');
  var msg = document.getElementById('rsvp-msg');

  var party = null;
  var lookupTimer = null;
  var lastCode = '';

  function say(text, isError) {
    msg.textContent = text || '';
    msg.className = 'form-msg' + (isError ? ' form-msg--error' : '');
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function renderParty(data) {
    party = data;
    guestList.innerHTML = data.guests.map(function (g, i) {
      return '<label class="guest"><input type="checkbox" data-guest="' + i + '"' +
        (g.attending ? ' checked' : '') + ' /><span>' + esc(g.name) + '</span></label>';
    }).join('');

    dietList.innerHTML = data.guests.map(function (g, i) {
      return '<label class="diet"><span>' + esc(g.name) + '</span>' +
        '<input class="field" type="text" data-diet="' + i + '" value="' + esc(g.dietary || '') +
        '" placeholder="None" /></label>';
    }).join('');

    stepGuests.classList.remove('is-hidden');
    stepDiet.classList.remove('is-hidden');
    say(data.greeting || '');
  }

  function clearParty() {
    party = null;
    stepGuests.classList.add('is-hidden');
    stepDiet.classList.add('is-hidden');
    guestList.innerHTML = '';
    dietList.innerHTML = '';
  }

  function lookup(code) {
    if (!ENDPOINT) {
      say('RSVP is not open yet — the form goes live with the invitations.', true);
      return;
    }
    say('Looking up your party…');
    fetch(ENDPOINT + '?action=lookup&code=' + encodeURIComponent(code))
      .then(function (r) { return r.json(); })
      .then(function (data) {
        if (!data || !data.ok) {
          clearParty();
          say(data && data.error ? data.error : 'We couldn’t find that code. Check the email, or text us.', true);
          return;
        }
        renderParty(data.party);
      })
      .catch(function () {
        clearParty();
        say('Something went wrong looking that up. Please try again in a moment.', true);
      });
  }

  codeInput.addEventListener('input', function () {
    var code = codeInput.value.trim();
    clearTimeout(lookupTimer);
    if (code.length < 3) { clearParty(); say(''); lastCode = ''; return; }
    if (code === lastCode) return;
    lookupTimer = setTimeout(function () { lastCode = code; lookup(code); }, 450);
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!party) {
      say('Please enter your party code first.', true);
      codeInput.focus();
      return;
    }

    var guests = party.guests.map(function (g, i) {
      var box = guestList.querySelector('[data-guest="' + i + '"]');
      var diet = dietList.querySelector('[data-diet="' + i + '"]');
      return {
        id: g.id,
        name: g.name,
        attending: !!(box && box.checked),
        dietary: diet ? diet.value.trim() : ''
      };
    });

    submitBtn.disabled = true;
    say('Sending…');

    fetch(ENDPOINT, {
      method: 'POST',
      // text/plain keeps the request "simple" so Apps Script needs no CORS preflight
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify({ action: 'rsvp', code: party.code, guests: guests })
    })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        if (data && data.ok) {
          var yes = guests.filter(function (g) { return g.attending; }).length;
          say(yes ? 'Got it — thank you! You can come back and change this any time before March 1.'
                  : 'Got it — we’ll miss you. You can change this any time before March 1.');
        } else {
          submitBtn.disabled = false;
          say(data && data.error ? data.error : 'That didn’t save. Please try again.', true);
        }
      })
      .catch(function () {
        submitBtn.disabled = false;
        say('That didn’t save. Please try again, or text us and we’ll add you by hand.', true);
      });
  });
})();
