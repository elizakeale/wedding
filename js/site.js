/* E & L Wedding — phase 2 behaviour.
 *
 * Pins the nav bar to the top once the banner has scrolled out of the way.
 *
 * Driven by an IntersectionObserver on a zero-height sentinel placed at the
 * bottom of the banner rather than by a scroll handler: the browser reports
 * the crossing itself, so there is no listener running on every scroll frame
 * and no layout read (getBoundingClientRect) to force a reflow mid-scroll.
 */
(function () {
  'use strict';

  var bar = document.getElementById('topbar');
  var banner = document.querySelector('.banner');
  if (!bar || !banner) return;

  function pin(on) {
    bar.classList.toggle('is-pinned', on);
  }

  if (!('IntersectionObserver' in window)) {
    // Old browser: leave the bar hidden rather than pinning it permanently.
    return;
  }

  // Sentinel sits at the very bottom edge of the banner. When it leaves the
  // top of the viewport, the banner is gone and the bar should take over.
  var sentinel = document.createElement('span');
  sentinel.setAttribute('aria-hidden', 'true');
  sentinel.style.cssText = 'position:absolute;bottom:0;left:0;width:1px;height:1px;pointer-events:none;';
  if (getComputedStyle(banner).position === 'static') banner.style.position = 'relative';
  banner.appendChild(sentinel);

  new IntersectionObserver(function (entries) {
    pin(!entries[0].isIntersecting);
  }, { rootMargin: '0px 0px 0px 0px', threshold: 0 }).observe(sentinel);
})();
