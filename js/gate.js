/* E & L Wedding — the front door.
 *
 * Accepts either a party code or the shared password, and remembers which,
 * so the RSVP form doesn't have to ask again and the itinerary can show only
 * the events that party is actually invited to.
 *
 * TWO MODES, on purpose:
 *
 *   ENDPOINT set    — the typed value is checked by the Apps Script, which is
 *                     the only thing that knows the 72 codes. They are never
 *                     shipped to the browser; this repo is public.
 *
 *   ENDPOINT empty  — falls back to checking the shared password here, in the
 *                     browser, exactly as the site does today. This matters:
 *                     without it, pointing the gate at a script that isn't
 *                     deployed yet would lock everyone out of a live site.
 *
 * The masking behaviour (bullets, the brief reveal of the last character) is
 * kept from the original gate, including the paste/autofill path — mobile
 * keyboards don't fire usable keypress events, so the typed value is tracked
 * separately rather than read back out of the field.
 */
(function () {
  'use strict';

  var input  = document.getElementById('input');
  var error  = document.getElementById('error');
  var wrap   = document.getElementById('wrap');
  /* The placeholder and its caret are one element, so the caret sits at the
   * end of the words at any font size. Falls back to the bare caret for the
   * phase-2 gate page, which still has the older markup. */
  var cursor = document.getElementById('ph') || document.getElementById('cursor');
  if (!input) return;

  var CFG = window.ELW || {};
  var realPw = '';
  var maskTimer = null;
  var busy = false;

  input.type = 'text';

  if (CFG.session && CFG.session() && document.getElementById('site')) {
    document.documentElement.className = 'unlocked';
    return;                                  // still inside; no door needed
  }

  setTimeout(function () { input.focus(); }, 100);

  function mask() {
    input.value = '•'.repeat(realPw.length);
    input.setSelectionRange(input.value.length, input.value.length);
  }

  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { e.preventDefault(); check(); return; }
    if (e.key === 'Backspace') {
      e.preventDefault();
      if (realPw.length > 0) {
        realPw = realPw.slice(0, -1);
        clearTimeout(maskTimer);
        mask();
      }
      if (realPw.length === 0 && cursor) cursor.classList.remove('hidden');
    }
  });

  input.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') return;
    e.preventDefault();
    var ch = e.key;
    if (ch.length !== 1) return;
    ch = ch.toLowerCase();          // codes and the password are all lower case
    realPw += ch;
    input.value = '•'.repeat(realPw.length - 1) + ch;   // reveal the last one briefly
    input.setSelectionRange(input.value.length, input.value.length);
    if (cursor) cursor.classList.add('hidden');
    clearTimeout(maskTimer);
    maskTimer = setTimeout(mask, 500);
  });

  input.addEventListener('input', function () {
    if (error) error.classList.remove('show');
    var v = input.value || '';
    if (v && v.indexOf('•') === -1) {       // paste, autofill, mobile IME
      realPw = v.toLowerCase();
      input.value = realPw;
      clearTimeout(maskTimer);
      maskTimer = setTimeout(mask, 500);
    }
    if (cursor) cursor.classList.toggle('hidden', realPw.length > 0);
  });

  /* The arrow does what Enter does. mousedown is swallowed so the field keeps
   * focus and the caret doesn't jump out from under someone mid-correction. */
  var go = document.getElementById('go');
  if (go) {
    go.addEventListener('mousedown', function (e) { e.preventDefault(); });
    go.addEventListener('click', function (e) { e.preventDefault(); check(); });
  }

  function typed() {
    var v = realPw || input.value || '';
    return v.replace(/•/g, '').trim().toLowerCase();
  }

  function reject() {
    busy = false;
    if (error) error.classList.add('show');
    if (wrap) {
      wrap.classList.remove('shake');
      void wrap.offsetWidth;                      // restart the animation
      wrap.classList.add('shake');
      wrap.addEventListener('animationend', function f () {
        wrap.classList.remove('shake');
        wrap.removeEventListener('animationend', f);
      });
    }
    input.value = '';
    realPw = '';
    clearTimeout(maskTimer);
    if (cursor) cursor.classList.remove('hidden');   // the prompt comes back
  }

  /* Two shapes of door. In phase 1 the gate is an overlay on the page it
   * protects, so getting in is a class change and the URL never moves —
   * there is no second address to walk around it. In phase 2 the root is a
   * door of its own and this navigates, as before. */
  function enter(session) {
    if (CFG.setSession) CFG.setSession(session);
    if (document.getElementById('site')) {
      document.documentElement.className = 'unlocked';
      window.scrollTo(0, 0);
      return;
    }
    window.location.href = (CFG.ENTRY_PAGE || 'home.html');
  }

  function check() {
    var value = typed();
    if (!value || busy) return;

    // No backend yet: behave exactly as the site does today.
    if (!CFG.ENDPOINT) {
      if (value.toLowerCase() === String(CFG.FALLBACK_PASSWORD || '').toLowerCase()) {
        enter({ kind: 'master', code: '' });
      } else {
        reject();
      }
      return;
    }

    busy = true;
    CFG.request('auth', { code: value })
      .then(function (data) {
        busy = false;
        if (data && data.ok) {
          enter({ kind: data.kind || 'party', code: data.code || '' });
        } else {
          reject();
        }
      })
      .catch(function () {
        // Network trouble shouldn't strand someone at the door when they may
        // well have typed the shared password.
        if (value.toLowerCase() === String(CFG.FALLBACK_PASSWORD || '').toLowerCase()) {
          enter({ kind: 'master', code: '' });
        } else {
          reject();
        }
      });
  }
})();
