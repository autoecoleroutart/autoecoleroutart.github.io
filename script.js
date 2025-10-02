// Menu hamburger functionality
document.addEventListener('DOMContentLoaded', function() {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const mainNav = document.querySelector('.main-nav');
    const body = document.body;

    if (hamburgerMenu && mainNav) {
        hamburgerMenu.addEventListener('click', function() {
            // Toggle navigation visibility
            mainNav.classList.toggle('active');
            hamburgerMenu.classList.toggle('active');
            
            // Toggle body scroll
            body.classList.toggle('menu-open');
            
            // Update aria-label for accessibility
            const isOpen = mainNav.classList.contains('active');
            hamburgerMenu.setAttribute('aria-label', isOpen ? 'Fermer le menu' : 'Ouvrir le menu');
            hamburgerMenu.setAttribute('aria-expanded', isOpen);
        });

        // Close menu when clicking on a navigation link
        const navButtons = mainNav.querySelectorAll('.nav-btn');
        navButtons.forEach(button => {
            button.addEventListener('click', function() {
                mainNav.classList.remove('active');
                hamburgerMenu.classList.remove('active');
                body.classList.remove('menu-open');
                hamburgerMenu.setAttribute('aria-label', 'Ouvrir le menu');
                hamburgerMenu.setAttribute('aria-expanded', 'false');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!hamburgerMenu.contains(event.target) && !mainNav.contains(event.target)) {
                mainNav.classList.remove('active');
                hamburgerMenu.classList.remove('active');
                body.classList.remove('menu-open');
                hamburgerMenu.setAttribute('aria-label', 'Ouvrir le menu');
                hamburgerMenu.setAttribute('aria-expanded', 'false');
            }
        });

        // Close menu on escape key
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape' && mainNav.classList.contains('active')) {
                mainNav.classList.remove('active');
                hamburgerMenu.classList.remove('active');
                body.classList.remove('menu-open');
                hamburgerMenu.setAttribute('aria-label', 'Ouvrir le menu');
                hamburgerMenu.setAttribute('aria-expanded', 'false');
            }
        });
    }
});