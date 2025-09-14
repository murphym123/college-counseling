// toggle mobile menu
const btn = document.getElementById('nav-toggle');
const menu = document.getElementById('menu');
if (btn && menu) {
  btn.addEventListener('click', () => {
    const open = menu.style.display === 'flex';
    menu.style.display = open ? 'none' : 'flex';
    btn.setAttribute('aria-expanded', String(!open));
  });
}
// footer year
const y = document.getElementById('year');
if (y) y.textContent = new Date().getFullYear();