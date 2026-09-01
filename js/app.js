/* =============================================
   E & L WEDDING — PASSWORD GATE LOGIC
   ============================================= */

(function () {
  'use strict';

  // ── CONFIG ──────────────────────────────────
  // Change this to your real password (case-insensitive check below)
  const CORRECT_PASSWORD = 'rockpiles';
  const SESSION_KEY = 'el_wedding_auth';

  // ── DOM refs ─────────────────────────────────
  const pagePassword   = document.getElementById('page-password');
  const pageSaveDate   = document.getElementById('page-save-the-date');
  const passwordInput  = document.getElementById('password-input');
  const errorMsg       = document.getElementById('password-error');
  const inputWrap      = document.getElementById('password-input-wrap');

  // ── Init ─────────────────────────────────────
  // If already authenticated in this session, skip to save-the-date
  if (sessionStorage.getItem(SESSION_KEY) === 'true') {
    showSaveTheDate();
  } else {
    showPassword();
  }

  // ── Keyboard submit ───────────────────────────
  passwordInput.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
      checkPassword();
    }
  });

  // Clear error as soon as they type again
  passwordInput.addEventListener('input', function () {
    errorMsg.classList.remove('visible');
  });

  // ── Expose submit for onclick in HTML ─────────
  window.submitPassword = checkPassword;

  // ── Core functions ────────────────────────────

  function checkPassword() {
    const entered = passwordInput.value.trim().toLowerCase();
    const correct = CORRECT_PASSWORD.toLowerCase();

    if (entered === correct) {
      sessionStorage.setItem(SESSION_KEY, 'true');
      showSaveTheDate();
    } else {
      triggerError();
    }
  }

  function triggerError() {
    // Show message
    errorMsg.classList.add('visible');

    // Shake the card
    inputWrap.classList.remove('shake');
    // Force reflow so animation re-triggers if already shaking
    void inputWrap.offsetWidth;
    inputWrap.classList.add('shake');

    // Clear input & refocus
    passwordInput.value = '';
    setTimeout(function () { passwordInput.focus(); }, 50);

    // Remove shake class after animation ends
    inputWrap.addEventListener('animationend', function onEnd() {
      inputWrap.classList.remove('shake');
      inputWrap.removeEventListener('animationend', onEnd);
    });
  }

  function showPassword() {
    pagePassword.classList.add('active');
    pageSaveDate.classList.remove('active');
    setTimeout(function () { passwordInput.focus(); }, 100);
  }

  function showSaveTheDate() {
    pageSaveDate.classList.add('active');
    pagePassword.classList.remove('active');
  }

})();
