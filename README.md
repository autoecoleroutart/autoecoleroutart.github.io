# 🚗 Auto-École Rout'Art

> **Votre Permis, Votre Liberté** - Site web moderne et professionnel pour l'auto-école Rout'Art

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/docs/Web/JavaScript)
[![Responsive](https://img.shields.io/badge/Responsive-Design-04AA6D?style=for-the-badge)](https://web.dev/responsive-web-design-basics/)

## 📋 Aperçu du Projet

Site web vitrine moderne et entièrement responsive pour l'auto-école Rout'Art, située à Lunéville (54300). Ce projet offre une expérience utilisateur optimale pour présenter l'ensemble des services de l'auto-école : formations de conduite, tarifs transparents, équipe professionnelle et informations pratiques.

### 🎯 Objectifs

- Présenter l'offre de formation de l'auto-école
- Faciliter la prise de contact et les inscriptions
- Offrir une expérience utilisateur moderne et intuitive
- Assurer une accessibilité optimale sur tous les appareils

## ✨ Fonctionnalités Principales

### 🎨 Design & Expérience Utilisateur

- **Interface moderne** avec système de design glassmorphism
- **Architecture CSS modulaire** avec variables centralisées
- **Navigation responsive** avec menu hamburger adaptatif
- **Animations fluides** et transitions optimisées pour l'engagement
- **Optimisation UX** avec bouton retour en haut et navigation intuitive

### 📱 Pages & Contenu Complet

| Page | Description | Fonctionnalités |
|------|-------------|-----------------|
| **🏠 Accueil** | Présentation générale avec hero section | Cartes interactives, informations de contact |
| **🎓 Formations** | Détail des permis (B, A1, A2, AM/BSR) | Tableaux comparatifs, documents téléchargeables |
| **💰 Tarifs** | Grilles tarifaires transparentes | Tables responsives, options de financement |
| **💳 Financement** | Solutions de paiement | CPF, aides disponibles, simulateurs |
| **📚 Code de la Route** | Apprentissage théorique | Méthodes pédagogiques, outils numériques |
| **👥 Équipe** | Présentation des moniteurs | Photos, spécialités, expériences |
| **📞 Contact** | Informations pratiques | Formulaire, géolocalisation, horaires |

### 🔧 Fonctionnalités Techniques Avancées

- **Système de grilles adaptatives** pour tous les contenus
- **Boutons "Voir plus" dynamiques** avec expansion progressive
- **Tables responsives intelligentes** avec transformation mobile
- **Navigation avec états actifs** et indicateurs visuels
- **Architecture CSS optimisée** avec import modulaire
- **JavaScript vanilla optimisé** pour les performances

## 🏗️ Architecture du Projet

```text
Rout-Art/
├── 📄 index.html                     # Page d'accueil principale
├── 📖 README.md                      # Documentation complète
├── 🔧 chrome_no_secu.sh             # Script de développement local
│
├── 📁 page/                          # Pages HTML organisées
│   ├── 📚 code_de_la_route.html         # Formation théorique
│   ├── 📞 contact.html                  # Contact et localisation
│   ├── 👥 equipe.html                   # Présentation de l'équipe
│   ├── 💳 financement.html              # Solutions de paiement
│   ├── 🎓 formations.html               # Détails des formations
│   ├── 🏦 garantie_financiere.html      # Garanties légales
│   ├── 📋 positionnement.html           # Évaluation initiale
│   ├── 📝 reclamation.html              # Gestion des réclamations
│   ├── 📊 resultat.html                 # Consultation des résultats
│   ├── 😊 satisfaction.html             # Enquêtes qualité
│   ├── 💰 tarifs.html                   # Grilles tarifaires
│   ├── 🌑 test-dark-mode.html           # Test du dark-mode
│   └── 📄 template.html                 # Modèle de développement
│
├── 📁 style/                         # Architecture CSS modulaire
│   ├── 🎨 variables.css                 # Variables de design système
│   ├── 🏗️ general.css                   # Styles de base globaux
│   ├── � README.md                     # Documentation CSS
│   ├── 🏠 index.css                     # Styles page d'accueil
│   ├── 🎓 formations.css                # Styles page formations
│   ├── 💰 tarifs.css                    # Styles page tarifs
│   ├── 📞 contact.css                   # Styles page contact
│   ├── 👥 equipe.css                    # Styles page équipe
│   ├── 💳 financement.css               # Styles page financement
│   ├── 📚 code_de_la_route.css          # Styles page code
│   ├── 🏦 garantie_financiere.css       # Styles page garantie
│   ├── 📋 positionnement.css            # Styles page positionnement
│   ├── 📝 reclamation.css               # Styles page réclamation
│   ├── 📊 resultat.css                  # Styles page résultat
│   ├── 😊 satisfaction.css              # Styles page satisfaction
│   └── 📜 reglement.css                 # Styles page règlement
│
├── 📁 script/                        # Scripts JavaScript
│   ├── ⚙️ script.js                     # Fonctionnalités principales
│   ├── 🎓 formations.js                 # Logique page formations
│   ├── 💰 tarifs.js                     # Logique page tarifs
│   └── 💳 financement.js                # Logique page financement
│
├── 📁 images/                        # Ressources visuelles
│   ├── 🎨 logo_routart_modern.png       # Logo principal
│   ├── 🌅 hero-car-road.png            # Image hero section
│   ├── 👤 avatar-*.png                  # Photos équipe
│   ├── 🎯 icon-*.png                    # Icônes fonctionnelles
│   ├── 🎓 permis-*.png                  # Visuels formations
│   └── 🏢 logo-groupama.png             # Logos pour la garantie financière
│
├── 📁 files/                         # Documents officiels
│   ├── 📋 programme_formation_*.pdf     # Programmes détaillés
│   ├── ⚖️ enjeux_formation_*.pdf        # Documents légaux
│   └── 📜 reglement_interieur.docx      # Règlement interne
│
└── 📁 icon/                          # Favicon et icônes
    └── 🎯 logo_routart_modern.png
```

## 🎨 Système de Design

### 🎨 Palette de Couleurs

```css
/* Couleurs Principales */
--primary-color: #1d3557;     /* Bleu marine professionnel */
--secondary-color: #22223b;    /* Gris anthracite */
--accent-color: #457b9d;       /* Bleu clair dynamique */
--white-color: #ffffff;        /* Blanc pur */
--light-gray: #f8f9fa;        /* Gris clair fond */
--text-color: #22223b;         /* Texte principal */
--success-color: #28a745;      /* Vert validation */
--warning-color: #ffc107;      /* Orange attention */
--error-color: #dc3545;        /* Rouge erreur */
```

### 📏 Système d'Espacement

```css
/* Espacements Cohérents */
--spacing-xs: 0.25rem;    /* 4px */
--spacing-sm: 0.5rem;     /* 8px */
--spacing-md: 1rem;       /* 16px */
--spacing-lg: 1.5rem;     /* 24px */
--spacing-xl: 2rem;       /* 32px */
--spacing-2xl: 3rem;      /* 48px */
--spacing-3xl: 4rem;      /* 64px */
```

### 🎭 Effets Visuels

- **Glassmorphism** : `backdrop-filter: blur(10px)`
- **Ombres progressives** : 4 niveaux d'intensité
- **Border radius** : Système unifié (4px, 8px, 12px)
- **Transitions** : Durées optimisées (0.3s, 0.5s)

## 📱 Responsive Design Avancé

### 📐 Breakpoints Stratégiques

| Appareil | Largeur | Optimisations |
|----------|---------|---------------|
| 📱 **Mobile** | < 480px | Menu hamburger, navigation tactile |
| 📱 **Large Mobile** | 480px - 768px | Grilles 1-2 colonnes |
| 💻 **Tablette** | 768px - 992px | Grilles 2-3 colonnes |
| 🖥️ **Desktop** | > 992px | Grilles complètes, hover effects |

### 🔄 Transformations Adaptatives

- **Tables → Cartes empilées** sur mobile
- **Grilles multi-colonnes → Colonne unique** responsive
- **Navigation horizontale → Menu hamburger** tactile
- **Images → Format adaptatif** selon l'écran

## � Technologies & Performance

### 💻 Stack Technique

- **HTML5** : Structure sémantique moderne
- **CSS3** : Flexbox, Grid, Variables, Media Queries
- **JavaScript ES6+** : Modules, Arrow Functions, DOM moderne
- **Google Fonts** : Montserrat (Display), Open Sans (Body)

### ⚡ Optimisations Performance

- **CSS modulaire** : Chargement ciblé par page
- **Images optimisées** : Formats WebP/PNG selon usage
- **JavaScript léger** : < 15KB total, fonctionnalités essentielles
- **Architecture scalable** : Variables CSS, composants réutilisables

### 🔧 Fonctionnalités JavaScript

```javascript
// Navigation responsive
toggleMobileMenu()

// Expansion de contenu
expandContent(trigger, content)

// Tables adaptatives
transformTable(breakpoint)

// Navigation fluide
smoothScroll(target)

// Bouton retour haut
showScrollToTop()
```

## 🛠️ Installation & Développement

### 📋 Prérequis

- Navigateur moderne (Chrome, Firefox, Safari, Edge)
- Serveur HTTP local (Live Server, XAMPP, WAMP)
- Éditeur de code (VS Code recommandé)

### 🚀 Démarrage Rapide

```bash
# Cloner le projet
git clone https://github.com/gossotjeanbaptiste/Rout-Art.git

# Naviguer dans le dossier
cd Rout-Art

# Ouvrir avec un serveur local
# Avec Live Server (VS Code)
# Ou via Python
python -m http.server 8000

# Accéder au site
http://localhost:8000
```

### 🔧 Script de Développement

```bash
# Pour Chrome sans sécurité (développement)
./chrome_no_secu.sh
```

## 📊 Structure des Données

### 👥 Équipe

```javascript
const team = [
  {
    name: "Cédric",
    role: "Exploitant & Formateur",
    specialties: ["Permis B", "A1", "A2", "AM"],
    experience: "Depuis 2002"
  },
  // ...autres membres
];
```

### 🎓 Formations

```javascript
const formations = {
  "permis-b": {
    title: "Permis B",
    age: "Dès 17 ans",
    duration: "Variable selon profil",
    price: "À partir de 1200€"
  }
  // ...autres formations
};
```

## 🔐 Sécurité & Bonnes Pratiques

- **Validation côté client** pour les formulaires
- **Sanitisation des entrées** utilisateur
- **Accessibilité WCAG** niveau AA
- **SEO optimisé** avec meta tags appropriés
- **Structure sémantique** HTML5

## 📞 Contact & Support

### 🏢 Auto-École Rout'Art

- **📧 Email** : [autoecoleroutart@hotmail.com](mailto:autoecoleroutart@hotmail.com)
- **📱 Sécrétariat** : [06 25 39 87 22](tel:+33625398722)
- **📱 Cédric (Gérant)** : [06 24 07 18 39](tel:+33624071839)
- **📍 Adresse** : 79 Rue d'Alsace, 54300 Lunéville
- **🌐 Réseaux sociaux** : Facebook, Instagram

### 🗓️ Horaires d'Ouverture

- **Lundi - Vendredi** : 10h00 - 19h00
- **Samedi** : 9h00 - 17h00
- **Dimanche** : Fermé

## 📈 Roadmap & Évolutions

### 🎯 Version Actuelle (v2.0)

- ✅ Design responsive complet
- ✅ Architecture CSS modulaire
- ✅ Pages optimisées mobile
- ✅ Système de navigation avancé

### 🚀 Prochaines Améliorations

- 🔄 Système de réservation en ligne
- 📱 Application mobile PWA
- 🤖 Chatbot d'assistance
- 📊 Dashboard élève personnalisé

## 📄 Licence & Droits

Ce projet est la propriété exclusive de **l'Auto-École Rout'Art**. Tous droits réservés © 2025.

**Développement** : Réalisé avec ❤️ pour offrir la meilleure expérience aux futurs conducteurs de Lunéville et ses environs.

---

> *"Apprendre à conduire, c'est gagner en liberté"* - Auto-École Rout'Art
