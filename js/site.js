/* E & L Wedding — phase 2 header behaviour.
 *
 * The header is one fixed element holding the nav and the wordmark. On a tall
 * hero the wordmark starts big and low — its hero position — and as you scroll
 * it rides up and shrinks until it settles beside the nav, at which point the
 * header IS the compact bar. Same element throughout, so there is no crossfade
 * and nothing to keep in sync.
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
 * layout. With JS off the header renders settled, which is still a correct and
 * readable page.
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
  var FADE_OVER = 80;   // px of scroll the bar background fades in across

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

    // The banner sits behind the header until its bottom reaches the bar's
    // bottom. Until then the bar background stays off, so the banner's own
    // photo shows through and the two never show a seam.
    settleAt = Math.max(0, banner.offsetHeight - header.offsetHeight);
  }

  var ticking = false;

  function apply() {
    ticking = false;
    var y = window.pageYOffset || root.scrollTop || 0;

    // 1:1 with the scroll, so it reads as the words coming to rest rather
    // than an animation playing at some unrelated rate.
    var p = travel > 0 ? Math.min(1, Math.max(0, y / travel)) : 1;
    var bg = Math.min(1, Math.max(0, (y - settleAt) / FADE_OVER));

    root.style.setProperty('--hdr-p', p.toFixed(4));
    root.style.setProperty('--hdr-bg', bg.toFixed(3));
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
