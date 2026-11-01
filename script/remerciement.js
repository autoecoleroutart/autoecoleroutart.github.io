/**
 * Script pour gérer le changement des images selon le thème
 * Toute image ayant un attribut data-dark-src utilise cette image en mode sombre
 * et revient à son src d'origine en mode clair.
 * Usage : <img src="logo.svg" data-dark-src="logo_dark.svg" alt="...">
 */

// Fonction pour mettre à jour les images selon le thème
function updateImagesForTheme() {
    const isDarkMode = document.documentElement.getAttribute('data-theme') === 'dark';

    document.querySelectorAll('img[data-dark-src]').forEach((img) => {
        // Mémorise l'image du mode clair au premier passage
        if (!img.dataset.lightSrc) {
            img.dataset.lightSrc = img.getAttribute('src');
        }
        img.src = isDarkMode ? img.dataset.darkSrc : img.dataset.lightSrc;
    });
}

// Mettre à jour les images au chargement de la page
document.addEventListener('DOMContentLoaded', updateImagesForTheme);

// Observer pour les changements de thème
const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.attributeName === 'data-theme') {
            updateImagesForTheme();
        }
    });
});

// Configurer l'observateur pour surveiller les changements d'attribut
observer.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ['data-theme']
});
