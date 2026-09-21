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
    // How far the wordmark has to travel, in px at the current root size.
    // Zero on a short-banner page: it is already settled.
    if (isTall) {
      var rem = parseFloat(getComputedStyle(root).fontSize) || 16;
      var declared = getComputedStyle(header).getPropertyValue('--hdr-travel').trim();
      travel = declared.slice(-3) === 'rem' ? parseFloat(declared) * rem : parseFloat(declared);
      if (!travel || travel < 1) travel = 388;
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
