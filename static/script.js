
const navbar = document.getElementById('navbar');
//for changing the active class of the navbar links

const links = navbar.querySelectorAll('a');

const currentPath = window.location.pathname;

links.forEach(link => {
    const href = link.getAttribute('href');


    if (href === '/' && currentPath === '/') {
        link.classList.add('active');
    }
    else if (href !== '/' && currentPath.startsWith(href)) {
        link.classList.add('active');
    } else {
        link.classList.remove('active');
    }
});
