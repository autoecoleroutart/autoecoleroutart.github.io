# 🚗 ROUT'ART CMS - Documentation Complète

> Application de gestion de contenu pour le site Rout'Art  
> Édition HTML • Git Sync • Prévisualisation • Interface GUI  
> ✨ Compilable en .exe pour Windows 11

---

## 📚 Table des Matières

1. [🚀 Démarrage Rapide](#démarrage-rapide)
2. [📁 Structure du Projet](#structure-du-projet)
3. [🎮 Guide d'Utilisation](#guide-dutilisation)
4. [⚙️ Installation Complète](#installation-complète)
5. [🔨 Compilation en .exe](#compilation-en-exe)
6. [🏗️ Architecture Technique](#architecture-technique)
7. [🐛 Dépannage](#dépannage)

---

## 🚀 Démarrage Rapide

### Option 1: Exécutable Windows (Recommandé)
```bash
Double-cliquez: rout_art_cms.exe
```

### Option 2: Python directement
```bash
python setup_dependencies.py
python rout_art_cms.py
```

### Option 3: Menu interactif
```bash
python launcher.py
```

### Option 4: Batch file Windows
```bash
Double-cliquez: run.bat
```

---

## 📁 Structure du Projet

```
Rout-Art/
├── 🎯 rout_art_cms.py              ← Application principale
│
├── 🔧 cms/                         ← Modules fonctionnels
│   ├── git_manager.py              (Git: pull/push/status)
│   ├── html_manager.py             (HTML: lecture/édition)
│   ├── server_manager.py           (Serveur HTTP local)
│   ├── config_manager.py           (Configuration persistante)
│   └── logger.py                   (Journalisation)
│
├── 🛠️ Scripts d'installation
│   ├── setup_dependencies.py       (Installation dépendances)
│   ├── test_configuration.py       (Tests de configuration)
│   ├── launcher.py                 (Menu interactif)
│   └── run.bat                     (Lanceur Windows)
│
├── 🔨 Compilation & Distribution
│   ├── build_exe.py                (Compilation PyInstaller)
│   ├── rout_art_cms.spec           (Configuration compilation)
│   └── create_deployment.py        (Package de distribution)
│
├── 📦 requirements.txt             (Dépendances Python)
│
└── 📚 Documentation
    └── DOCUMENTATION.md             (Vous êtes ici!)
```

---

## 🎮 Guide d'Utilisation

### Écran Initial

L'application se lance avec une interface à **5 onglets**:

#### 1️⃣ Onglet "Git & Synchronisation"
- **Pull**: Récupérez les modifications du repository
- **Push**: Publiez vos changements
- **Statut**: Vérifiez l'état du repository
- **Message commit**: Rédigez un message pour le push

#### 2️⃣ Onglet "Éditeur Contenu"
- **Sélectionner fichier**: Choisissez un fichier HTML à éditer
- **Prévisualisation**: Voyez le contenu actuel
- **Recherche/Remplace**: Trouvez et modifiez du texte
- **Sauvegarder**: Enregistrez vos modifications

#### 3️⃣ Onglet "Prévisualisation"
- **Démarrer serveur**: Lance un serveur HTTP local
- **Port**: Personnalisez le port (défaut: 8000)
- **Ouvrir navigateur**: Lance la prévisualisation
- **Logs**: Consultez les logs du serveur

#### 4️⃣ Onglet "Paramètres"
- **Chemin repository**: Configurez le dossier Git
- **Auto pull au démarrage**: Synchronisation automatique
- **Auto refresh**: Actualisation automatique
- **Réinitialiser**: Restaure les paramètres par défaut

#### 5️⃣ Onglet "Logs"
- **Historique complet**: Tous les événements
- **Filtrage**: Par niveau ou type
- **Export**: Téléchargez les logs
- **Temps réel**: Mise à jour instantanée

### Flux Typique d'Utilisation

```
1. ⚙️ CONFIGURATION (1ère fois)
   └─ Aller à "Paramètres"
   └─ Entrer le chemin du repository
   └─ Cliquer "Sauvegarder"

2. 🔄 TRAVAIL QUOTIDIEN
   └─ Git: Pull
   └─ Éditeur: Ouvrir et modifier fichier
   └─ Prévisualisation: Vérifier le résultat
   └─ Git: Push avec message
   └─ Logs: Vérifier succès

3. 💾 AVANT DE QUITTER
   └─ Tous les fichiers sont auto-sauvegardés
   └─ Les logs sont archivés
```

---

## ⚙️ Installation Complète

### Prérequis
- Python 3.9+ (ou exécutable .exe fourni)
- Windows 7+ ou WSL
- 200 MB d'espace disque

### Étape 1: Installation des Dépendances

```bash
python setup_dependencies.py
```

Cela installe automatiquement:
- `customtkinter` (GUI moderne)
- `beautifulsoup4` (Édition HTML)
- `gitpython` (Gestion Git)

### Étape 2: Vérifier la Configuration

```bash
python test_configuration.py
```

Ce script vérifie:
- ✓ Python version
- ✓ Modules disponibles
- ✓ Permissions fichiers
- ✓ Accès Git

### Étape 3: Lancer l'Application

```bash
python rout_art_cms.py
```

Ou utilisez le menu:
```bash
python launcher.py
```

---

## 🔨 Compilation en .exe

### Prérequis de Compilation
```bash
pip install pyinstaller
```

### Compiler

```bash
python build_exe.py
```

**Résultat:**
- Exécutable créé dans `dist/Rout'Art CMS/`
- Nom: `Rout'Art CMS.exe`
- Taille: ~200 MB (inclut Python)
- Aucune dépendance requise

### Tester l'Exécutable

```bash
# Navigez dans le dossier de sortie
cd dist/Rout'Art CMS/

# Lancez l'exe
Rout'Art CMS.exe
```

### Distribuer

Pour partager l'application:

```bash
python create_deployment.py
```

Cela crée un package complet à distribuer.

---

## 🏗️ Architecture Technique

### Modules Principaux

#### `git_manager.py`
Gère toutes les opérations Git:
```python
pull()          # Récupère les modifications
push(message)   # Publie les changements
get_status()    # Affiche l'état du repo
get_history()   # Historique des commits
```

#### `html_manager.py`
Édition et manipulation HTML:
```python
read_file(path)              # Lit un fichier HTML
write_file(path, content)    # Sauvegarde
find_element(selector)       # Localise un élément
replace_element(old, new)    # Remplace du contenu
```

#### `server_manager.py`
Serveur HTTP local pour prévisualisation:
```python
start(port, path)   # Démarre le serveur
stop()              # Arrête le serveur
is_running()        # État du serveur
```

#### `config_manager.py`
Stockage et récupération de configuration:
```python
load_config()       # Charge depuis ~/.rout_art_cms/
save_config()       # Sauvegarde persistante
get_repo_path()     # Chemin du repository
set_repo_path()     # Configure le repository
```

#### `logger.py`
Centralisation des logs:
```python
log(msg)            # Info
log_error(err)      # Erreur
log_success(msg)    # Succès
get_logs()          # Récupère l'historique
```

### Flux de Données

```
Utilisateur
    ↓
[Interface GUI - CustomTkinter]
    ↓
[Managers - Métier]
    ├─ git_manager (GitPython)
    ├─ html_manager (BeautifulSoup4)
    ├─ server_manager (http.server)
    ├─ config_manager (JSON)
    └─ logger (File + Memory)
    ↓
[Système de fichiers + Git + HTTP]
```

### Threading

Les opérations longues tournent en thread séparé:
- Git pull/push
- Démarrage serveur
- Lecture de fichiers volumineux

Cela garde l'interface responsive.

---

## 🐛 Dépannage

### "Module not found"

```bash
# Solution:
python setup_dependencies.py
```

### "Repository not found"

1. Vérifiez le chemin dans ⚙️ Paramètres
2. Assurez-vous que c'est un dossier Git valide
3. Cliquez "Sauvegarder"

### "Erreur de compilation"

```bash
# Vérifiez d'abord:
python test_configuration.py

# Puis réessayez:
python build_exe.py
```

### Serveur HTTP n'apparaît pas

1. Vérifiez que le port n'est pas utilisé
2. Essayez avec un autre port (ex: 8001)
3. Consultez les logs pour plus de détails

### Les changements Git ne fonctionnent pas

1. Vérifiez la configuration Git: `git config --list`
2. Testez la connexion au repository
3. Vérifiez les permissions fichiers

---

## 📋 Checklist de Déploiement

Avant de distribuer l'application:

- [ ] Compiler l'exe: `python build_exe.py`
- [ ] Tester l'exe sur une machine sans Python
- [ ] Vérifier tous les onglets fonctionnent
- [ ] Tester Git pull/push
- [ ] Tester édition HTML
- [ ] Tester prévisualisation
- [ ] Vérifier logs complets
- [ ] Créer package: `python create_deployment.py`

---

## 📞 Aide & Support

### Fichiers de Logs
- **Localisation**: `~/.rout_art_cms/app.log`
- **Consultez les logs** pour diagnostiquer les problèmes
- **Export**: Utilisez le bouton "Export" dans l'onglet Logs

### Script de Test
```bash
python test_configuration.py
```
Teste complètement votre installation.

### Informations de Configuration
- **Stockage**: `~/.rout_art_cms/config.json`
- **Réinitialiser**: Cliquez "Réinitialiser" dans Paramètres

---

## ℹ️ Informations Techniques

| Aspect | Détail |
|--------|--------|
| **Langage** | Python 3.9+ |
| **GUI** | CustomTkinter 5.0+ |
| **HTML** | BeautifulSoup4 4.11+ |
| **Git** | GitPython 3.1+ |
| **Serveur** | http.server (stdlib) |
| **Compilation** | PyInstaller 5.0+ |
| **Taille .exe** | ~200 MB |
| **Mémoire** | 50-150 MB |
| **Compatibilité** | Windows 7+ |
| **Python** | 3.9, 3.10, 3.11, 3.12 |

---

## 🎯 Raccourcis Utiles

- **Onglet Git**: Git & Synchronisation → Pull/Push
- **Onglet Éditeur**: Modification de contenu HTML
- **Onglet Serveur**: Prévisualisation en temps réel
- **Onglet Paramètres**: Configuration de l'app
- **Onglet Logs**: Suivi des opérations

---

## ✨ Version

**Rout'Art CMS v1.0.0**
- Status: Production Ready ✅
- Dernière mise à jour: 13 novembre 2025
- Auteur: Rout'Art Team
- License: MIT

---

**Besoin d'aide?** Consultez les logs ou relancez `python test_configuration.py`

**À bientôt!** 🚀
