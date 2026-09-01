/* =============================================
   E & L WEDDING — PASSWORD GATE LOGIC
   ============================================= */

(function () {
  'use strict';

  const CORRECT_PASSWORD = 'rockpiles';
  const SESSION_KEY = 'el_wedding_auth';

  const pagePassword = document.getElementById('page-password');
  const pageSaveDate = document.getElementById('page-save-the-date');
  const passwordInput = document.getElementById('password-input');
  const errorMsg = document.getElementById('password-error');
  const inputWrap = document.getElementById('password-input-wrap');

  // Init
  if (sessionStorage.getItem(SESSION_KEY) === 'true') {
    showSaveTheDate();
  } else {
    showPassword();
  }

  // Keyboard
  passwordInput.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
      e.preventDefault();
      checkPassword();
    }
  });

  passwordInput.addEventListener('input', function () {
    errorMsg.classList.remove('visible');
  });

  window.submitPassword = checkPassword;

  function checkPassword() {
    var entered = (passwordInput.value || '').trim().toLowerCase().replace(/\s+/g, '');
    var correct = CORRECT_PASSWORD.toLowerCase().trim();
    if (entered === correct) {
      sessionStorage.setItem(SESSION_KEY, 'true');
      showSaveTheDate();
    } else {
      triggerError();
    }
  }

  function triggerError() {
    errorMsg.classList.add('visible');
    inputWrap.classList.remove('shake');
    void inputWrap.offsetWidth;
    inputWrap.classList.add('shake');
    passwordInput.value = '';
    setTimeout(function () { passwordInput.focus(); }, 50);
    inputWrap.addEventListener('animationend', function onEnd() {
      inputWrap.classList.remove('shake');
      inputWrap.removeEventListener('animationend', onEnd);
    });
  }

  function showPassword() {
    pagePassword.style.display = 'flex';
    pageSaveDate.style.display = 'none';
    document.body.style.overflow = 'hidden';
    window.scrollTo(0, 0);
    setTimeout(function () { passwordInput.focus(); }, 100);
  }

  function showSaveTheDate() {
    // Force scroll to top first
    window.scrollTo(0, 0);
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
    // Swap pages
    pagePassword.style.display = 'none';
    pageSaveDate.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

})();
