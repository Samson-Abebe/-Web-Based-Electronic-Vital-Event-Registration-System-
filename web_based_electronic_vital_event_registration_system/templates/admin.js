
const menuToggle = document.getElementById('menu-toggle');
const sidebar = document.getElementById('sidebar');
const navbar = document.getElementById('navbar');
const mainContent = document.getElementById('main-content');

menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
    navbar.classList.toggle('collapsed');
    mainContent.classList.toggle('collapsed');
});
