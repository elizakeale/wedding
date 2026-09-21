/* E & L Wedding — phase 2 header behaviour.
 *
 * The header is one fixed element holding the nav and the wordmark. On a tall
 * hero the wordmark starts pushed down to its hero position and rides up with
 * the scroll until it rests beside the nav — at which point the header IS the
 * compact bar. Nothing slides in and nothing crossfades; it is the same words
 * the whole way.
 *
 * Two values are handed to CSS, which does all the painting:
 *   --hdr-drop  how far the wordmark is still pushed down, in px
 *   --hdr-bg    opacity of the orchid slice behind the bar, 0..1
 *
 * Reads are batched into a rAF so a scroll never triggers a synchronous
 * layout, and both properties drive compositor-friendly work (transform and
 * opacity), so this does not repaint the page on every frame.
 *
 * With JS off the header stays in its resting state — nav and wordmark in the
 * compact bar — which is still a correct, readable page.
 */
(function () {
  'use strict';

  var header = document.getElementById('pageheader');
  var banner = document.querySelector('.banner');
  if (!header || !banner) return;

  var isTall = header.classList.contains('pageheader--tall');

  // How far the wordmark drops on a hero, and how tall the resting bar is.
  // Read from CSS so the two stay in one place and keep scaling with the
  // viewport-relative root font size.
  function readPx(name, el) {
    var v = getComputedStyle(el || header).getPropertyValue(name).trim();
    if (v.slice(-2) === 'px') return parseFloat(v);
    if (v.slice(-3) === 'rem') {
      return parseFloat(v) * parseFloat(getComputedStyle(document.documentElement).fontSize);
    }
    return parseFloat(v) || 0;
  }

  var travel = 0, settleAt = 0, fadeOver = 80;

  function measure() {
    travel = isTall ? readPx('--hdr-travel') : 0;
    // The banner sits behind the header until its bottom reaches the bar's
    // bottom. Until then the bar background stays off, so the banner's own
    // photo shows through and there is no seam between the two.
    settleAt = Math.max(0, banner.offsetHeight - header.offsetHeight);
  }

  var ticking = false;

  function apply() {
    ticking = false;
    var y = window.pageYOffset || document.documentElement.scrollTop || 0;

    // Wordmark rides up 1:1 with the scroll, then stops. Moving with the page
    // rather than at some other rate is what makes it read as the same object
    // coming to rest rather than an animation playing.
    var drop = Math.max(0, travel - y);

    var bg = settleAt <= 0
      ? Math.min(1, y / fadeOver)
      : Math.min(1, Math.max(0, (y - settleAt) / fadeOver));

    header.style.setProperty('--hdr-drop', drop.toFixed(1) + 'px');
    header.style.setProperty('--hdr-bg', bg.toFixed(3));
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
