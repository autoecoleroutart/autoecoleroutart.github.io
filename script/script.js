// Menu hamburger functionality
document.addEventListener('DOMContentLoaded', function() {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const mainNav = document.querySelector('.main-nav');
    const body = document.body;

    // Fonction pour jouer le son de changement de page au chargement
    function playPageLoadSound() {
        // Attendre un petit délai pour s'assurer que la page est bien chargée
        setTimeout(() => {
            try {
                // Déterminer le chemin correct selon la page actuelle
                const isIndexPage = window.location.pathname.includes('index.html') || 
                                   window.location.pathname.endsWith('/') || 
                                   window.location.pathname === '/';
                
                const soundPath = isIndexPage ? 'sounds/change_page.mp3' : '../sounds/change_page.mp3';
                
                const audio = new Audio(soundPath);
                audio.volume = 0.4; // Volume modéré
                audio.preload = 'auto';
                
                // Jouer le son après un court délai
                audio.addEventListener('canplaythrough', () => {
                    audio.play().catch(error => {
                        // Son bloqué par le navigateur (normal pour la première visite)
                    });
                });
                
                // Forcer la lecture si l'événement ne se déclenche pas
                setTimeout(() => {
                    if (audio.readyState >= 2) { // HAVE_CURRENT_DATA
                        audio.play().catch(error => {
                            // Son bloqué (autoplay policy)
                        });
                    }
                }, 100);
                
            } catch (error) {
                // Erreur avec le son de chargement
            }
        }, 200); // Délai de 200ms après le chargement du DOM
    }

    // Jouer le son au chargement de la page
    playPageLoadSound();

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
            button.addEventListener('click', function(event) {
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