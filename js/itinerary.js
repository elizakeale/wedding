/* E & L Wedding — the itinerary, fetched per party.
 *
 * This page ships empty on purpose. The events come from the Apps Script,
 * already filtered to the party whose code was used at the gate, so an event
 * someone isn't invited to never reaches their browser — it isn't hidden with
 * CSS, it simply isn't sent. Reading the page source shows nothing.
 *
 * That's the whole reason this page is dynamic while the rest of the site is
 * static: hiding the Welcome BBQ client-side would have left its details in
 * the HTML for anyone who looked, which is worse than not hiding it at all.
 *
 * Someone who came in on the shared password sees everything.
 */
(function () {
  'use strict';

  var mount = document.getElementById('itinerary');
  if (!mount) return;

  var CFG = window.ELW || {};
  var session = CFG.session ? CFG.session() : null;

  function note(text) {
    mount.innerHTML = '';
    var p = document.createElement('p');
    p.className = 'row__text itinerary__note';
    p.textContent = text;
    mount.appendChild(p);
  }

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text) n.textContent = text;
    return n;
  }

  function render(events) {
    mount.innerHTML = '';
    if (!events.length) {
      note('The week’s plans are still coming together — check back soon.');
      return;
    }

    var day = null;
    events.forEach(function (ev) {
      if (ev.day && ev.day !== day) {
        day = ev.day;
        mount.appendChild(el('h3', 'day', day));
      }

      var wrap = el('div', 'event');
      wrap.appendChild(el('p', 'event__time', ev.time || ''));
      wrap.appendChild(el('div', 'event__rule'));

      var body = el('div', 'event__body');
      var name = el('h3', 'event__name');
      if (ev.optional) name.appendChild(el('span', 'opt', 'Optional:'));
      name.appendChild(document.createTextNode((ev.optional ? ' ' : '') + ev.name));
      body.appendChild(name);

      if (ev.body) body.appendChild(el('p', 'event__text', ev.body));

      /* Location, parking and the rest print as one labelled block, in a
       * fixed order so every event reads the same way — and only the lines
       * that have something to say appear. */
      var DETAILS = [
        ['Location:', ev.location],
        ['Parking:', ev.parking],
        ['Transportation:', ev.transportation],
        ['Directions:', ev.directions],
        ['Attire:', ev.attire]
      ].filter(function (d) { return d[1]; });

      if (DETAILS.length) {
        var p = el('p', 'event__text');
        DETAILS.forEach(function (d, i) {
          if (i) p.appendChild(document.createElement('br'));
          p.appendChild(el('span', 'k', d[0]));
          p.appendChild(document.createTextNode(' ' + d[1]));
        });
        body.appendChild(p);
      }

      wrap.appendChild(body);
      mount.appendChild(wrap);
    });
  }

  if (!CFG.request || !CFG.ENDPOINT) {
    note('The itinerary isn’t published yet — check back soon.');
    return;
  }

  note('Loading…');

  CFG.request('itinerary', { code: (session && session.code) || '' })
    .then(function (data) {
      if (!data || !data.ok) {
        note('We couldn’t load the itinerary. Please try again in a moment.');
        return;
      }
      render(data.events || []);
    })
    .catch(function () {
      note('We couldn’t reach the server. Please try again in a moment.');
    });
})();
