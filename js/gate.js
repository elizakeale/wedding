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

  /* The field shows one bullet per real character, so an index into the
   * displayed value is the same index into realPw. Everything below works
   * on those indices rather than assuming the caret is at the end — which is
   * what stopped select-all, and every mid-word edit, from behaving. */
  function caret() {
    return { s: input.selectionStart || 0, e: input.selectionEnd || 0 };
  }

  function show(revealAt) {
    var n = realPw.length;
    input.value = revealAt > 0
      ? '•'.repeat(revealAt - 1) + realPw.charAt(revealAt - 1) +
        '•'.repeat(n - revealAt)
      : '•'.repeat(n);
    if (cursor) cursor.classList.toggle('hidden', n > 0);
  }

  /* Re-masking must not move the caret or drop a selection: the mask fires
   * half a second after the last keystroke, which is long enough to land in
   * the middle of someone pressing Cmd+A. */
  function mask() {
    var c = caret();
    show(0);
    try { input.setSelectionRange(c.s, c.e); } catch (err) {}
  }

  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { e.preventDefault(); check(); return; }
    // Cmd/Ctrl/Alt chords are the browser's: select all, copy, word-delete.
    if (e.metaKey || e.ctrlKey || e.altKey) return;

    if (e.key !== 'Backspace' && e.key !== 'Delete') return;
    e.preventDefault();

    var c = caret(), at = c.s;
    if (c.e > c.s) {                                  // a selection: drop it
      realPw = realPw.slice(0, c.s) + realPw.slice(c.e);
    } else if (e.key === 'Backspace' && c.s > 0) {
      realPw = realPw.slice(0, c.s - 1) + realPw.slice(c.s);
      at = c.s - 1;
    } else if (e.key === 'Delete' && c.s < realPw.length) {
      realPw = realPw.slice(0, c.s) + realPw.slice(c.s + 1);
    }

    clearTimeout(maskTimer);
    show(0);
    input.setSelectionRange(at, at);
  });

  input.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    e.preventDefault();
    var ch = e.key;
    if (ch.length !== 1) return;
    ch = ch.toLowerCase();          // codes and the password are all lower case

    var c = caret();
    realPw = realPw.slice(0, c.s) + ch + realPw.slice(c.e);
    var at = c.s + 1;
    show(at);                       // the character just typed shows briefly
    input.setSelectionRange(at, at);
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
