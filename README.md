# 🚗 Auto-École Rout'Art

> **Votre Permis, Votre Liberté** - Site web moderne pour l'auto-école Rout'Art

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/docs/Web/JavaScript)
[![Responsive](https://img.shields.io/badge/Responsive-Design-green)](https://web.dev/responsive-web-design-basics/)

## 📋 Description

Site web vitrine moderne et responsive pour l'auto-école Rout'Art, offrant une expérience utilisateur optimale pour présenter les formations de conduite, tarifs, équipe et services.

## ✨ Fonctionnalités

### 🎨 Design & UX

- **Design moderne** avec effets glassmorphism
- **Interface responsive** adaptée à tous les appareils
- **Navigation intuitive** avec menu hamburger mobile
- **Animations fluides** et transitions optimisées
- **Bouton retour en haut** pour une meilleure navigation

### 📱 Pages & Contenu

- **Accueil** : Présentation de l'auto-école avec hero section
- **Formations** : Détail des permis (B, A1, A2, AM/BSR) avec tableaux interactifs
- **Tarifs** : Grilles tarifaires complètes et transparentes
- **Financement** : Options de paiement et aides disponibles
- **Code de la Route** : Informations sur l'apprentissage théorique
- **Équipe** : Présentation des moniteurs avec photos
- **Contact** : Formulaire de contact et informations pratiques

### 🔧 Fonctionnalités Techniques

- **Boutons "Voir plus"** avec expansion du contenu
- **Tables responsives** pour les tarifs et formations
- **Système de navigation** avec état actif
- **Optimisation des performances** CSS et JavaScript
- **Architecture CSS modulaire** avec variables centralisées

## 🏗️ Structure du Projet

```text
Rout-Art/
├── index.html                 # Page d'accueil
├── README.md                  # Documentation du projet
├── chrome_no_secu.sh         # Script de développement
├── page/                        # Pages HTML
│   ├── code_de_la_route.html    # code de la route
│   ├── contact.html             # Page de contact
│   ├── equipe.html              # Présentation de l'équipe
│   ├── financement.html         # Options de financement
│   ├── garantie_financiere.html # Garantie financière
│   ├── positionnement.html      # Positionnement
│   ├── reclamation.html         # Gestion des réclamations
│   ├── resultat.html            # Résultats du permis
│   ├── satisfaction.html        # Enquête de satisfaction
│   ├── tarifs.html              # Tarifs des formations
│   └── template.html            # Modèle de page
├── style/                     # Styles CSS
│   ├── main.css              # Importation des styles
│   ├── variables.css         # Variables CSS centralisées
│   ├── base.css              # Styles de base
│   ├── layout.css            # Mise en page
│   ├── components.css        # Composants réutilisables
│   ├── pages.css             # Styles spécifiques aux pages
│   ├── buttons.css           # Styles des boutons
│   ├── tables.css            # Styles des tableaux
│   └── responsive.css        # Styles responsive
├── script/                    # Scripts JavaScript
│   ├── script.js             # Script principal
│   ├── formations.js         # Fonctionnalités formations
│   ├── tarifs.js             # Fonctionnalités tarifs
│   └── financement.js        # Fonctionnalités financement
├── images/                    # Images du site
│   ├── logo_routart_modern.png
│   ├── hero-car-road.png
│   ├── avatar-*.png          # Photos de l'équipe
│   ├── icon-*.png            # Icônes diverses
│   ├── permis-*.png          # image permis
│   └── logo-*.png            # logos diverses
├── files/                     # Documents PDF
│   ├── programme_formation_*.pdf
│   ├── enjeux_formation_*.pdf
│   └── reglement_interieur.docx
├── fonts/                     # Polices personnalisées
└── icon/                      # Icônes et favicon
```

## 🎨 Système de Design

### Couleurs Principales

- **Primary** : `#1d3557` (Bleu marine)
- **Secondary** : `#22223b` (Gris foncé)
- **Accent** : `#457b9d` (Bleu clair)
- **Text** : `#22223b`
- **Background** : `#ffffff`

### Variables CSS

Le projet utilise un système complet de variables CSS avec :

- **Couleurs** avec variations d'opacité (`--primary-10`, `--primary-20`, etc.)
- **Espacements** cohérents (`--spacing-xs` à `--spacing-3xl`)
- **Border radius** standardisés
- **Ombres** et effets glassmorphism
- **Transitions** optimisées

## 📱 Responsive Design

Le site est entièrement responsive avec des breakpoints optimisés :

- **Mobile** : < 480px
- **Tablet** : 480px - 768px
- **Desktop** : > 768px

Fonctionnalités responsive :

- Menu hamburger sur mobile
- Grilles adaptatives
- Images optimisées
- Navigation tactile

## 🔧 Technologies Utilisées

### Frontend

- **HTML5** : Structure sémantique
- **CSS3** : Styles modernes avec Flexbox/Grid
- **JavaScript (Vanilla)** : Interactions et fonctionnalités
- **Google Fonts** : Typographie (Montserrat, Open Sans)

### Fonctionnalités CSS Avancées

- **CSS Variables** : Système de design cohérent
- **Flexbox & Grid** : Layouts modernes
- **Glassmorphism** : Effets visuels
- **Animations** : Transitions fluides
- **Media Queries** : Responsive design

### Performance

- **CSS modulaire** : Chargement optimisé
- **Images optimisées** : Formats et tailles adaptés
- **JavaScript léger** : Fonctionnalités essentielles

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. **Fork** le projet
2. **Créer** une branche pour votre fonctionnalité
3. **Commit** vos changements
4. **Push** vers la branche
5. **Ouvrir** une Pull Request

## 📞 Contact

**Auto-École Rout'Art**

- 📧 Email : [autoecoleroutart@hotmail.com](mailto:autoecoleroutart@hotmail.com)
- 📱 Téléphone Sécrétariat: [06 25 39 87 22](tel:+33625398722)
- 📱 Téléphone Cédric : [06 24 07 18 39](tel:+33624071839)
- 📍 Adresse : 79 Rue d'Alsace, 54300 Lunéville

## 📄 Licence

Ce projet est la propriété de l'Auto-École Rout'Art. Tous droits réservés.

---

*Développé avec ❤️ pour l'Auto-École Rout'Art*
