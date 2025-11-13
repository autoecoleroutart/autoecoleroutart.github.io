#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Outil de Déploiement - Crée une version distribuable de l'application
"""

import shutil
import subprocess
import sys
from pathlib import Path
from datetime import datetime


def create_deployment_package():
    """Créer un package de déploiement complet"""

    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║                    🚀 DÉPLOIEMENT ROUT'ART CMS                    ║")
    print("╚════════════════════════════════════════════════════════════════════╝\n")

    # Créer le répertoire de déploiement
    deploy_dir = Path("deploy")
    if deploy_dir.exists():
        shutil.rmtree(deploy_dir)

    deploy_dir.mkdir(parents=True)
    print(f"📁 Répertoire de déploiement créé: {deploy_dir}")

    # Créer les sous-répertoires
    (deploy_dir / "source").mkdir()
    (deploy_dir / "executable").mkdir()
    (deploy_dir / "docs").mkdir()

    # Copier les fichiers Python source
    print("\n📋 Copie des fichiers source...")
    source_dir = deploy_dir / "source"

    shutil.copy("rout_art_cms.py", source_dir)
    shutil.copy("requirements.txt", source_dir)
    shutil.copy("setup_dependencies.py", source_dir)
    shutil.copy("run.bat", source_dir)
    shutil.copy("launcher.py", source_dir)

    # Copier le module CMS
    shutil.copytree("cms", source_dir / "cms")
    print("   ✅ Fichiers source copiés")

    # Copier la documentation
    print("\n📚 Copie de la documentation...")
    docs_dir = deploy_dir / "docs"

    docs_to_copy = [
        "CMS_README.md",
        "GUIDE_INSTALLATION.py",
        "test_configuration.py",
        "rout_art_cms.spec",
    ]

    for doc in docs_to_copy:
        if Path(doc).exists():
            shutil.copy(doc, docs_dir)

    # Créer un README de déploiement
    readme = docs_dir / "README.md"
    with open(readme, "w", encoding="utf-8") as f:
        f.write("""# 📦 Package de Déploiement - Rout'Art CMS

## 📂 Contenu du Package

```
deploy/
├── source/                    # Code source Python
│   ├── rout_art_cms.py       # Application principale
│   ├── cms/                  # Module CMS
│   ├── requirements.txt      # Dépendances
│   ├── setup_dependencies.py # Installation auto
│   ├── launcher.py           # Lanceur interactif
│   └── run.bat               # Script de lancement Windows
│
├── executable/               # Exécutables compilés
│   └── (À remplir après compilation)
│
└── docs/                     # Documentation
    ├── README.md             # Ce fichier
    ├── CMS_README.md         # Documentation du CMS
    ├── GUIDE_INSTALLATION.py # Guide complet
    └── test_configuration.py # Script de test
```

## 🚀 Installation pour les Utilisateurs

### Option 1: Avec l'exécutable (.exe)
1. Extraire `executable/Rout'Art CMS.exe`
2. Double-cliquer pour lancer
3. ✓ Aucune installation supplémentaire nécessaire

### Option 2: Avec Python
1. Avoir Python 3.9+ d'installé
2. Aller dans le dossier `source/`
3. Double-cliquer sur `run.bat`
4. L'application se lance et installe les dépendances automatiquement

## 🔧 Compilation (Pour développeurs)

1. Aller dans `source/`
2. Exécuter: `python build_exe.py`
3. L'exécutable se trouve dans: `dist/Rout'Art CMS/`
4. Copier le répertoire `dist/Rout'Art CMS/` vers `executable/`

## 📋 Système Requis

- **Windows 11** ou ultérieur
- **RAM:** 2 GB minimum (4 GB recommandé)
- **Espace disque:** 500 MB
- **Python 3.9+** (si utilisation du code source)

## ✅ Vérification de l'Installation

```bash
python test_configuration.py
```

## 💡 Conseils de Distribution

1. **Archive ZIP**
   ```bash
   # Créer une archive pour distribution
   7z a Rout_Art_CMS_v1.0_Windows.7z deploy/
   ```

2. **GitHub Releases**
   - Upload l'archive sur les Releases
   - Ajouter des notes de version

3. **Documentation pour l'Utilisateur**
   - Inclure le fichier CMS_README.md
   - Fournir des screenshots
   - Créer un guide vidéo si possible

## 🔗 Liens Utiles

- Repository: https://github.com/gossotjeanbaptiste/Rout-Art
- Issues: https://github.com/gossotjeanbaptiste/Rout-Art/issues
- Discussions: https://github.com/gossotjeanbaptiste/Rout-Art/discussions

## 📞 Support

Pour toute question ou problème:
- Ouvrir une issue sur GitHub
- Consulter la documentation
- Vérifier les logs dans l'application

---

**Package Date:** {date}
**Version:** 1.0.0
""".format(date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    print("   ✅ Documentation copiée")

    # Créer un manifest
    print("\n📄 Création du manifest...")
    manifest = {
        "name": "Rout'Art CMS",
        "version": "1.0.0",
        "created": datetime.now().isoformat(),
        "author": "Rout'Art Team",
        "files": {
            "source": "Code source Python complet",
            "executable": "Exécutables Windows compilés",
            "docs": "Documentation complète"
        },
        "requirements": {
            "windows_version": "11+",
            "python_version": "3.9+",
            "ram": "2GB minimum",
            "disk": "500MB"
        }
    }

    import json
    with open(deploy_dir / "MANIFEST.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print("   ✅ Manifest créé")

    # Résumé final
    print("\n" + "="*70)
    print("✅ PACKAGE DE DÉPLOIEMENT CRÉÉ AVEC SUCCÈS!".center(70))
    print("="*70)

    print(f"\n📦 Localisation: {deploy_dir.absolute()}")
    print(f"\n📂 Structure créée:")
    print(f"   • {deploy_dir / 'source'} - Code source")
    print(f"   • {deploy_dir / 'executable'} - Exécutables (à remplir)")
    print(f"   • {deploy_dir / 'docs'} - Documentation")

    print("\n🔨 Prochaines étapes:")
    print("   1. cd source/")
    print("   2. python build_exe.py")
    print("   3. Copier dist/Rout'Art CMS/ vers ../executable/")
    print("   4. Créer l'archive: 7z a Rout_Art_CMS_v1.0.7z deploy/")

    print("\n💾 Documentation:")
    print(f"   Voir: {docs_dir / 'README.md'}")


if __name__ == "__main__":
    try:
        create_deployment_package()
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        sys.exit(1)
