/* E & L Wedding — header behaviour.
 *
 * Two states, one element, one threshold. On a tall hero the header is part
 * of the hero and scrolls away with it at full size; when the hero's bottom
 * reaches the top of the window this adds .is-bar and CSS brings the same
 * element back as the compact bar.
 *
 * It used to interpolate continuously — the wordmark shrinking and riding up
 * from the first pixel of scroll — which left a half-formed bar sitting over
 * a hero that was still mostly on screen. A single class change at the hero's
 * bottom is both what the design asks for and a great deal less work per
 * frame: no custom properties written on every scroll event, so no style
 * recalculation until the one moment it matters.
 *
 * This publishes two numbers, both only on load and resize:
 *
 *   --hdr-travel  how far down the hero the wordmark sits, in px.
 *   settleAt      the scroll position where the bar takes over.
 *
 * Scroll reads are batched into a rAF so scrolling never forces a synchronous
 * layout. With JS off a tall hero simply never forms its bar, which leaves a
 * correct and readable page.
 */
(function () {
  'use strict';

  var header = document.getElementById('pageheader');
  var banner = document.querySelector('.banner');
  if (!header || !banner) return;

  // Short-banner pages open settled (CSS pins --hdr-p to 1 for them) but they
  // still need the bar background, or content scrolls through the header.
  var isTall = header.classList.contains('pageheader--tall');

  var root = document.documentElement;
  var travel = 0, settleAt = 0;
  var HYST = 6;   // px of slack, so resting on the line doesn't flicker

  // Short-banner pages are the bar from the start — there is no hero for
  // them to come out of, and the wordmark is a link immediately.
  if (!isTall) header.classList.add('is-bar');

  function measure() {
    // How far the wordmark has to travel. Measured against the hero's real
    // height, not a rem constant: rem tracks viewport WIDTH, but the hero is
    // clamped to the window HEIGHT, so on a wide short window a rem-based
    // drop keeps growing after the hero has stopped and the wordmark lands
    // on top of the scroll cue.
    //
    // 0.46077 = 464/1007, where the hero wordmark sits in the frame.
    // 5rem is the wordmark's own flow offset inside the header at p=0, so
    // subtracting it makes the rendered top land on that fraction exactly.
    // Mirrors the --hdr-travel calc in the stylesheet (the no-JS path).
    if (isTall) {
      // Where the wordmark sits in the frame, as a fraction of the hero.
      // Phase 2 is 464/1007; the save-the-date frame is higher up, and the
      // mobile frame higher still, so the number is a CSS variable that the
      // media query can change rather than a constant in here.
      var frac = parseFloat(
        getComputedStyle(header).getPropertyValue('--hero-frac')) || 0.46077;

      // The wordmark's own offset inside the header. Measured rather than
      // assumed, because phase 2 has the nav above it and the save-the-date
      // header does not. offsetTop ignores the transform, which is what we
      // want: this is the flow position, not the travelled one.
      var word = header.querySelector('.pageheader__wordmark');
      var flow = word ? word.offsetTop : 0;

      travel = banner.offsetHeight * frac - flow;
      if (!(travel > 1)) travel = 388;
      root.style.setProperty('--hdr-travel', travel.toFixed(1) + 'px');
    } else {
      travel = 0;
    }

    // Where the bar takes over: the hero's bottom arriving at the bar's own
    // bottom edge. Read from the stylesheet rather than the element, because
    // in its hero state the header has no fixed height to measure.
    var rootStyle = getComputedStyle(root);
    var rem  = parseFloat(rootStyle.fontSize) || 16;
    var barH = parseFloat(rootStyle.getPropertyValue('--hdr-h')) * rem;
    if (!(barH > 0)) barH = 9.75 * rem;
    settleAt = Math.max(0, banner.offsetHeight - barH);
  }

  var ticking = false;

  function apply() {
    ticking = false;
    if (!isTall) return;

    var y = window.pageYOffset || root.scrollTop || 0;
    var on = header.classList.contains('is-bar');

    // The bar takes over exactly when the hero's bottom arrives at the top of
    // the window. The wordmark is a link only in that state: in the hero it
    // is the page's title and shouldn't behave like navigation.
    if (!on && y > settleAt) header.classList.add('is-bar');
    else if (on && y < settleAt - HYST) header.classList.remove('is-bar');
  }

  function onScroll() {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(apply);
    }
  }

  measure();
  apply();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', function () { measure(); onScroll(); });
})();
