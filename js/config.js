/* E & L Wedding — one place for the backend URL.
 *
 * Paste the Apps Script /exec URL here ONCE. The gate, the RSVP form and the
 * itinerary all read it from here, so there is no second copy to forget.
 *
 * Leave it empty and the site falls back to its offline behaviour: the gate
 * accepts the shared password on its own, and RSVP says it isn't open yet.
 * That fallback is deliberate — it means the live site keeps working exactly
 * as it does today until the script is actually deployed.
 */
window.ELW = window.ELW || {};

window.ELW.ENDPOINT = 'https://script.google.com/macros/s/AKfycbzV_Pz9_JUaxIG6OHyeQba0Oa99Be2kJihEg1-qkdWIr8E3PqYVZrrpZ1KTJZ44_EDK4g/exec';

/* The shared password. Still works alongside party codes, so you can send the
 * link to a plus-one, a vendor, or someone not on the sheet yet — and so the
 * parties whose leader has no email address can still be let in.
 *
 * Only used for the no-ENDPOINT fallback; once the script is deployed the
 * server holds the real copy of this and this value is never checked. */
window.ELW.FALLBACK_PASSWORD = 'rockpiles';

/* Where the gate sends people once they're in. */
window.ELW.ENTRY_PAGE = 'home.html';

/* Who the browser thinks you are. sessionStorage, not localStorage: it clears
 * when the tab closes, which is the right lifetime for a shared family laptop.
 *
 * This is convenience, not security. Anyone can set it by hand — which is
 * fine, because it doesn't gate anything on its own. The itinerary's contents
 * come from the server keyed by code, so a forged session shows you nothing
 * you couldn't already see. */
window.ELW.session = function () {
  try {
    var raw = sessionStorage.getItem('elw.session');
    return raw ? JSON.parse(raw) : null;
  } catch (e) { return null; }
};

window.ELW.setSession = function (data) {
  try { sessionStorage.setItem('elw.session', JSON.stringify(data)); }
  catch (e) { /* private mode — the session just won't persist */ }
};

/* Every backend call goes through here so the demo can stand in for it. */
window.ELW.request = function (kind, payload) {
  var url = window.ELW.ENDPOINT;
  if (!url) {
    if (window.RSVP_DEMO) return window.RSVP_DEMO(kind, payload);
    return Promise.resolve({ ok: false, notOpen: true });
  }
  if (kind === 'rsvp') {
    return fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },  // avoids CORS preflight
      body: JSON.stringify(payload)
    }).then(function (r) { return r.json(); });
  }
  var q = '?action=' + encodeURIComponent(kind);
  if (payload && payload.code) q += '&code=' + encodeURIComponent(payload.code);
  return fetch(url + q).then(function (r) { return r.json(); });
};
