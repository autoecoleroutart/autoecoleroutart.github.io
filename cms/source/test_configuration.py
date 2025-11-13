#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test - Vérifier que toutes les dépendances fonctionnent
À exécuter avant la compilation en .exe
"""

import sys
from pathlib import Path


def test_imports():
    """Tester l'import de toutes les dépendances"""
    print("🧪 Test des dépendances...\n")

    dependencies = {
        "tkinter": "Interface graphique (inclus avec Python)",
        "customtkinter": "Interface graphique moderne",
        "git": "Gestion Git (GitPython)",
        "bs4": "Parsing HTML (BeautifulSoup4)",
        "http.server": "Serveur HTTP (stdlib)",
        "socketserver": "Serveur HTTP (stdlib)",
    }

    failed = []

    for module, description in dependencies.items():
        try:
            __import__(module)
            print(f"✅ {module:20} | {description}")
        except ImportError as e:
            print(f"❌ {module:20} | {description}")
            print(f"   Erreur: {e}")
            failed.append(module)

    print()
    return len(failed) == 0, failed


def test_local_modules():
    """Tester les modules locaux du CMS"""
    print("🧪 Test des modules locaux...\n")

    modules = [
        "cms.git_manager",
        "cms.html_manager",
        "cms.server_manager",
        "cms.config_manager",
        "cms.logger",
    ]

    failed = []

    for module in modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}")
            print(f"   Erreur: {e}")
            failed.append(module)

    print()
    return len(failed) == 0, failed


def test_main_app():
    """Tester le module principal"""
    print("🧪 Test du module principal...\n")

    try:
        import rout_art_cms
        print("✅ rout_art_cms")
        return True
    except ImportError as e:
        print(f"❌ rout_art_cms")
        print(f"   Erreur: {e}")
        return False


def test_file_structure():
    """Vérifier la structure des fichiers"""
    print("🧪 Test de la structure des fichiers...\n")

    required_files = [
        "rout_art_cms.py",
        "requirements.txt",
        "cms/__init__.py",
        "cms/git_manager.py",
        "cms/html_manager.py",
        "cms/server_manager.py",
        "cms/config_manager.py",
        "cms/logger.py",
    ]

    failed = []

    for file_path in required_files:
        path = Path(file_path)
        if path.exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} (MANQUANT)")
            failed.append(file_path)

    print()
    return len(failed) == 0, failed


def main():
    """Exécuter tous les tests"""
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║              🚗 TEST DE CONFIGURATION - ROUT'ART CMS              ║")
    print("╚════════════════════════════════════════════════════════════════════╝")
    print()

    all_passed = True

    # Test 1: Structure des fichiers
    passed, failed = test_file_structure()
    if not passed:
        all_passed = False
        print(f"⚠️  {len(failed)} fichier(s) manquant(s)\n")

    # Test 2: Imports des dépendances
    passed, failed = test_imports()
    if not passed:
        all_passed = False
        print(f"⚠️  {len(failed)} dépendance(s) manquante(s)")
        print("💡 Exécutez: pip install -r requirements.txt\n")

    # Test 3: Modules locaux
    passed, failed = test_local_modules()
    if not passed:
        all_passed = False
        print(f"⚠️  {len(failed)} module(s) local(aux) manquant(s)\n")

    # Test 4: Module principal
    if not test_main_app():
        all_passed = False
        print()

    # Résumé
    print("╔════════════════════════════════════════════════════════════════════╗")
    if all_passed:
        print("║                    ✅ TOUS LES TESTS RÉUSSIS                      ║")
        print("║                                                                    ║")
        print("║  Vous pouvez maintenant:                                          ║")
        print("║  • Lancer l'application: python rout_art_cms.py                  ║")
        print("║  • Compiler en .exe: python build_exe.py                         ║")
    else:
        print("║                    ❌ CERTAINS TESTS ONT ÉCHOUÉ                   ║")
        print("║                                                                    ║")
        print("║  Veuillez corriger les erreurs ci-dessus puis réessayer          ║")
    print("╚════════════════════════════════════════════════════════════════════╝")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
