// Menu hamburger functionality
document.addEventListener('DOMContentLoaded', function () {
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const mainNav = document.querySelector('.main-nav');
    const body = document.body;

    if (hamburgerMenu && mainNav) {
        hamburgerMenu.addEventListener('click', function () {
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
            button.addEventListener('click', function (event) {
                mainNav.classList.remove('active');
                hamburgerMenu.classList.remove('active');
                body.classList.remove('menu-open');
                hamburgerMenu.setAttribute('aria-label', 'Ouvrir le menu');
                hamburgerMenu.setAttribute('aria-expanded', 'false');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function (event) {
            if (!hamburgerMenu.contains(event.target) && !mainNav.contains(event.target)) {
                mainNav.classList.remove('active');
                hamburgerMenu.classList.remove('active');
                body.classList.remove('menu-open');
                hamburgerMenu.setAttribute('aria-label', 'Ouvrir le menu');
                hamburgerMenu.setAttribute('aria-expanded', 'false');
            }
        });

        // Close menu on escape key
        document.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && mainNav.classList.contains('active')) {
                mainNav.classList.remove('active');
                hamburgerMenu.classList.remove('active');
                body.classList.remove('menu-open');
                hamburgerMenu.setAttribute('aria-label', 'Ouvrir le menu');
                hamburgerMenu.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // Fonctionnalité bouton retour en haut
    function createBackToTopButton() {
        // Créer le bouton
        const backToTopBtn = document.createElement('button');
        backToTopBtn.innerHTML = '↑';
        backToTopBtn.className = 'back-to-top';
        backToTopBtn.setAttribute('aria-label', 'Retour en haut de la page');
        backToTopBtn.style.display = 'none';

        // Ajouter le bouton au body
        document.body.appendChild(backToTopBtn);

        // Fonction pour afficher/masquer le bouton selon le scroll
        function toggleBackToTopButton() {
            if (window.scrollY > 300) {
                backToTopBtn.style.display = 'flex';
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
                setTimeout(() => {
                    if (!backToTopBtn.classList.contains('show')) {
                        backToTopBtn.style.display = 'none';
                    }
                }, 300); // Délai correspondant à la transition CSS
            }
        }

        // Fonction pour remonter en haut avec animation fluide
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }

        // Event listeners
        window.addEventListener('scroll', toggleBackToTopButton);
        backToTopBtn.addEventListener('click', scrollToTop);

        // Vérifier la position initiale
        toggleBackToTopButton();
    }

    // Initialiser le bouton retour en haut
    createBackToTopButton();

    // ===== SMOOTH SCROLL POUR LA MOLETTE DE LA SOURIS =====
    // N'appliquer que sur desktop pour de meilleures performances
    if (window.innerWidth > 768) {
        // Variables pour le smooth scroll de la page
        let isSmoothing = false;
        let targetY = window.scrollY;
        let currentY = window.scrollY;

        // Variables pour le smooth scroll du menu
        let isMenuSmoothing = false;
        let menuTargetY = 0;
        let menuCurrentY = 0;

        window.addEventListener('wheel', (e) => {
            // Vérifier si on est dans le menu de navigation
            const navList = document.querySelector('.main-nav .nav-list');
            if (navList && navList.contains(e.target)) {
                // Appliquer le smooth scroll pour le menu
                e.preventDefault();

                menuTargetY += e.deltaY;

                // Limiter entre 0 et la hauteur scrollable du menu
                const maxScroll = navList.scrollHeight - navList.clientHeight;
                menuTargetY = Math.max(0, Math.min(menuTargetY, maxScroll));

                if (!isMenuSmoothing) {
                    isMenuSmoothing = true;
                    menuCurrentY = navList.scrollTop;
                    smoothScrollMenu();
                }
                return;
            }

            // Smooth scroll pour la page principale
            e.preventDefault();

            // Ajouter le delta à la position cible
            targetY += e.deltaY;

            // Limiter entre 0 et la hauteur maximale
            targetY = Math.max(0, Math.min(targetY, document.documentElement.scrollHeight - window.innerHeight));

            // Démarrer l'animation si elle n'est pas déjà en cours
            if (!isSmoothing) {
                isSmoothing = true;
                smoothScrollAnimation();
            }
        }, { passive: false });

        // Fonction d'animation smooth pour la page
        function smoothScrollAnimation() {
            // Interpolation pour un mouvement fluide (0.15 = vitesse de transition)
            currentY += (targetY - currentY) * 0.15;

            // Arrondir pour éviter les micro-mouvements
            if (Math.abs(targetY - currentY) < 0.5) {
                currentY = targetY;
                isSmoothing = false;
            }

            window.scrollTo(0, currentY);

            // Continuer l'animation si nécessaire
            if (isSmoothing) {
                requestAnimationFrame(smoothScrollAnimation);
            }
        }

        // Fonction d'animation smooth pour le menu
        function smoothScrollMenu() {
            const navList = document.querySelector('.main-nav .nav-list');
            if (!navList) {
                isMenuSmoothing = false;
                return;
            }

            // Interpolation pour un mouvement fluide
            menuCurrentY += (menuTargetY - menuCurrentY) * 0.15;

            // Arrondir pour éviter les micro-mouvements
            if (Math.abs(menuTargetY - menuCurrentY) < 0.5) {
                menuCurrentY = menuTargetY;
                isMenuSmoothing = false;
            }

            navList.scrollTop = menuCurrentY;

            // Continuer l'animation si nécessaire
            if (isMenuSmoothing) {
                requestAnimationFrame(smoothScrollMenu);
            }
        }

        // Synchroniser lors de scroll direct du menu
        const navList = document.querySelector('.main-nav .nav-list');
        if (navList) {
            navList.addEventListener('scroll', function () {
                if (!isMenuSmoothing) {
                    menuTargetY = navList.scrollTop;
                    menuCurrentY = navList.scrollTop;
                }
            });
        }

        // Synchroniser lors de scroll direct de la page (touches clavier, barre de défilement, etc.)
        let scrollTimeout;
        window.addEventListener('scroll', function () {
            clearTimeout(scrollTimeout);
            scrollTimeout = setTimeout(() => {
                if (!isSmoothing) {
                    targetY = window.scrollY;
                    currentY = window.scrollY;
                }
            }, 50);
        });
    }
});

/**
 * Liens dynamiques (data-link)
 * Génère l'attribut href des liens à partir de leur texte, afin qu'une
 * modification faite via le CMS (qui ne change que le texte) mette aussi
 * à jour la destination du lien.
 * Usage : <a data-link="mail">contact@exemple.fr</a>
 *         <a data-link="tel">06 12 34 56 78</a>
 *         <a data-link="url">https://exemple.fr</a>
 */
function buildLinkHref(type, text) {
    const value = text.trim();
    if (!value) return null;

    switch (type) {
        case 'mail': {
            const email = value.match(/[^\s@:]+@[^\s@]+\.[^\s@]+/);
            return email ? 'mailto:' + email[0] : null;
        }
        case 'tel': {
            // Garde uniquement les chiffres et le "+", format international pour les numéros français
            const phone = value.match(/\+?\d[\d\s.()-]{5,}\d/);
            if (!phone) return null;
            let number = phone[0].replace(/[^\d+]/g, '');
            if (/^0\d{9}$/.test(number)) {
                number = '+33' + number.slice(1);
            }
            return 'tel:' + number;
        }
        case 'url':
            return /^https?:\/\//i.test(value) ? value : 'https://' + value;
        default:
            return null;
    }
}

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('a[data-link]').forEach(function (link) {
        const href = buildLinkHref(link.dataset.link, link.textContent);
        if (href) {
            link.href = href;
        }
    });
});
