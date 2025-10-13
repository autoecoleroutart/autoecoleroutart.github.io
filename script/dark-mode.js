/* ==========================================================================
   DARK MODE FUNCTIONALITY - Gestion du thème clair/sombre
   ========================================================================== */

class DarkModeToggle {
    constructor() {
        this.init();
    }

    init() {
        // Créer le bouton de toggle
        this.createToggleButton();
        
        // Charger le thème sauvegardé ou détecter les préférences système
        this.loadSavedTheme();
        
        // Écouter les changements de préférences système
        this.listenToSystemChanges();
    }

    createToggleButton() {
        // Créer le bouton
        const toggleButton = document.createElement('button');
        toggleButton.className = 'theme-toggle';
        toggleButton.setAttribute('aria-label', 'Basculer entre thème clair et sombre');
        toggleButton.setAttribute('title', 'Changer le thème');

        // Créer les icônes SVG
        toggleButton.innerHTML = `
            <svg class="theme-toggle-icon sun" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10zM12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>
            </svg>
            <svg class="theme-toggle-icon moon" viewBox="0 0 24 24" aria-hidden="true">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
            </svg>
        `;

        // Ajouter l'événement de clic
        toggleButton.addEventListener('click', () => this.toggleTheme());

        // Ajouter le bouton au body
        document.body.appendChild(toggleButton);

        this.toggleButton = toggleButton;
    }

    toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        // Ajouter une classe pour l'animation
        this.toggleButton.classList.add('changing');
        
        setTimeout(() => {
            this.setTheme(newTheme);
            this.toggleButton.classList.remove('changing');
        }, 150);
    }

    setTheme(theme) {
        // Appliquer le thème
        if (theme === 'dark') {
            document.documentElement.setAttribute('data-theme', 'dark');
            this.updateToggleLabel('Passer au thème clair');
        } else {
            document.documentElement.removeAttribute('data-theme');
            this.updateToggleLabel('Passer au thème sombre');
        }

        // Mettre à jour les images selon le thème
        this.updateThemeImages(theme);

        // Sauvegarder le choix
        localStorage.setItem('preferred-theme', theme);
        
        // Déclencher un événement personnalisé
        document.dispatchEvent(new CustomEvent('themeChanged', {
            detail: { theme: theme }
        }));
    }

    updateToggleLabel(label) {
        if (this.toggleButton) {
            this.toggleButton.setAttribute('aria-label', label);
            this.toggleButton.setAttribute('title', label);
        }
    }

    updateThemeImages(theme) {
        // Définir les correspondances d'images pour le mode sombre
        const imageMapping = {
            'france-travail.png': 'france-travail-sombre.png'
            // Ajouter d'autres correspondances d'images ici si nécessaire
            // 'autre-image.png': 'autre-image-sombre.png'
        };

        // Trouver toutes les images dans la page
        const images = document.querySelectorAll('img');
        
        images.forEach(img => {
            let currentSrc = img.src;
            let filename = currentSrc.split('/').pop(); // Obtenir le nom du fichier
            
            if (theme === 'dark') {
                // Passer au mode sombre
                for (const [lightImage, darkImage] of Object.entries(imageMapping)) {
                    if (filename === lightImage) {
                        // Remplacer par la version sombre
                        img.src = currentSrc.replace(lightImage, darkImage);
                        // Optionnel: mettre à jour l'alt text
                        if (img.alt && img.alt.includes('France Travail')) {
                            img.alt = img.alt + ' (mode sombre)';
                        }
                        break;
                    }
                }
            } else {
                // Passer au mode clair
                for (const [lightImage, darkImage] of Object.entries(imageMapping)) {
                    if (filename === darkImage) {
                        // Remplacer par la version claire
                        img.src = currentSrc.replace(darkImage, lightImage);
                        // Restaurer l'alt text original
                        if (img.alt && img.alt.includes('(mode sombre)')) {
                            img.alt = img.alt.replace(' (mode sombre)', '');
                        }
                        break;
                    }
                }
            }
        });
    }

    loadSavedTheme() {
        // Vérifier le thème sauvegardé
        const savedTheme = localStorage.getItem('preferred-theme');
        
        if (savedTheme) {
            this.setTheme(savedTheme);
        } else {
            // Détecter les préférences système
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            this.setTheme(prefersDark ? 'dark' : 'light');
        }
    }

    listenToSystemChanges() {
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        mediaQuery.addEventListener('change', (e) => {
            // Ne changer automatiquement que si l'utilisateur n'a pas de préférence sauvegardée
            const savedTheme = localStorage.getItem('preferred-theme');
            if (!savedTheme) {
                this.setTheme(e.matches ? 'dark' : 'light');
            }
        });
    }

    // Méthode pour obtenir le thème actuel
    getCurrentTheme() {
        return document.documentElement.getAttribute('data-theme') || 'light';
    }

    // Méthode pour forcer un thème (utile pour debugging)
    forceTheme(theme) {
        this.setTheme(theme);
    }
}

// Initialiser le dark mode quand le DOM est chargé
document.addEventListener('DOMContentLoaded', () => {
    window.darkModeToggle = new DarkModeToggle();
    
    // Ajouter un raccourci clavier (Ctrl/Cmd + Shift + D)
    document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'D') {
            e.preventDefault();
            window.darkModeToggle.toggleTheme();
        }
    });
});

// Exporter pour utilisation globale
window.DarkModeToggle = DarkModeToggle;