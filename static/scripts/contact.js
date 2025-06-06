document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  const overlay = document.getElementById('sending-overlay');

  form.addEventListener('submit', function () {
    overlay.classList.remove('d-none');
  });
});