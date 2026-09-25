/* E & L Wedding — header behaviour.
 *
 * The header is one fixed element holding the nav and the wordmark. On a tall
 * hero the wordmark starts big and low — its hero position — and as you scroll
 * it rides up and shrinks until it settles beside the nav, at which point the
 * header IS the compact bar. Same element throughout, so there is no crossfade
 * and nothing to keep in sync.
 *
 * WHERE the morph happens matters as much as that it happens. Run linearly
 * against the wordmark's own travel it was finished less than halfway down
 * the hero, leaving a half-formed bar over a photo that was still mostly on
 * screen — the hero appeared to split in two. So the timeline is the whole
 * hero, not the wordmark's travel, and the fraction is CUBED: the first half
 * of the hero spends about an eighth of the morph, and the rest arrives over
 * the last stretch, landing exactly as the hero's bottom meets the bar. The
 * hero holds; the bar gathers itself as the photo leaves.
 *
 * This file publishes just two numbers and lets CSS derive everything else:
 *
 *   --hdr-p    0 = full hero, 1 = settled. Drives position, size and tracking.
 *   --hdr-bg   opacity of the orchid slice behind the bar, 0..1.
 *
 * Keeping the two states described in CSS (rather than computing pixel values
 * here) means the Figma numbers live in one place, and they keep scaling with
 * the viewport-relative root font size for free.
 *
 * Scroll reads are batched into a rAF so scrolling never forces a synchronous
 * layout. With JS off the header renders in its hero state, which is still a
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
  var EASE = 3;   // how hard the morph is pushed to the end of the hero

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

    // Fraction of the way down the hero, then cubed — see the note up top.
    var t = settleAt > 0 ? Math.min(1, Math.max(0, y / settleAt)) : 1;
    var p = Math.pow(t, EASE);

    // The bar's own photo strip waits until the hero has gone. While the hero
    // is still behind the bar, the hero's photo IS the bar's background —
    // turning this on any earlier paints a second, differently-cropped slice
    // over the first, and the edge of it is the seam that made the hero look
    // like it was splitting. It fades up as the hero slides out from behind.
    var bg = Math.min(1, Math.max(0, (y - settleAt) / 70));

    root.style.setProperty('--hdr-p', p.toFixed(4));
    root.style.setProperty('--hdr-bg', bg.toFixed(3));

    // The wordmark is only a link once it has arrived in the bar. Above the
    // fold it is the page's title and shouldn't behave like navigation.
    header.classList.toggle('is-bar', p > 0.995);
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
