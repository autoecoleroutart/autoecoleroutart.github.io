#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lanceur Quick Start - Instructions de démarrage pour l'application Rout'Art CMS
"""

import subprocess
import sys
from pathlib import Path


def show_menu():
    """Afficher le menu principal"""
    print("\n" + "="*70)
    print("🚗 ROUT'ART CMS - MENU PRINCIPAL".center(70))
    print("="*70 + "\n")

    print("Que voulez-vous faire?\n")
    print("1️⃣  Lancer l'application")
    print("2️⃣  Installer/Vérifier les dépendances")
    print("3️⃣  Afficher le guide d'installation")
    print("4️⃣  Exécuter les tests de configuration")
    print("5️⃣  Compiler en .exe (PyInstaller requis)")
    print("6️⃣  Afficher les informations système")
    print("0️⃣  Quitter\n")

    return input("Choisissez une option (0-6): ").strip()


def run_app():
    """Lancer l'application"""
    print("\n🚀 Lancement de l'application...\n")
    try:
        subprocess.run([sys.executable, "rout_art_cms.py"])
    except Exception as e:
        print(f"❌ Erreur: {e}")


def install_dependencies():
    """Installer les dépendances"""
    print("\n📦 Installation des dépendances...\n")
    try:
        subprocess.run([sys.executable, "setup_dependencies.py"])
    except Exception as e:
        print(f"❌ Erreur: {e}")


def show_guide():
    """Afficher le guide d'installation"""
    print("\n📚 Affichage du guide d'installation...\n")
    try:
        subprocess.run([sys.executable, "GUIDE_INSTALLATION.py"])
    except Exception as e:
        print(f"❌ Erreur: {e}")


def run_tests():
    """Exécuter les tests"""
    print("\n🧪 Exécution des tests...\n")
    try:
        subprocess.run([sys.executable, "test_configuration.py"])
    except Exception as e:
        print(f"❌ Erreur: {e}")


def compile_exe():
    """Compiler en .exe"""
    print("\n🔨 Compilation en .exe...\n")
    try:
        subprocess.run([sys.executable, "build_exe.py"])
    except Exception as e:
        print(f"❌ Erreur: {e}")


def show_system_info():
    """Afficher les informations système"""
    print("\n📊 Informations Système\n")
    print(f"Python: {sys.version}")
    print(f"Plateforme: {sys.platform}")
    print(f"Répertoire actuel: {Path.cwd()}")
    print(f"Utilisateur: {Path.home()}")

    # Vérifier les dépendances
    print("\n📦 Dépendances:\n")

    deps = ["customtkinter", "beautifulsoup4", "gitpython"]
    for dep in deps:
        try:
            __import__(dep)
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ❌ {dep} (non installé)")


def main():
    """Fonction principale"""
    while True:
        choice = show_menu()

        if choice == "1":
            run_app()
        elif choice == "2":
            install_dependencies()
        elif choice == "3":
            show_guide()
        elif choice == "4":
            run_tests()
        elif choice == "5":
            compile_exe()
        elif choice == "6":
            show_system_info()
        elif choice == "0":
            print("\n👋 Au revoir!\n")
            break
        else:
            print("\n❌ Option invalide. Veuillez réessayer.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interruption de l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
