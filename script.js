document.getElementById('year').textContent = new Date().getFullYear();
const toggle = document.getElementById('nav-toggle');
const menu = document.getElementById('menu');
toggle?.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') === 'true';
  toggle.setAttribute('aria-expanded', String(!open));
  menu.style.display = open ? 'none' : 'flex';
});
