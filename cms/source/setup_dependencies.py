#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'installation des dépendances
À exécuter une seule fois avant de lancer l'application
"""

import subprocess
import sys
from pathlib import Path


def setup_git_safe_directory():
    """Ajouter le répertoire Git comme safe directory si .git existe"""
    # Chercher le répertoire racine du projet (où se trouve .git)
    current_dir = Path(__file__).parent.parent.parent

    git_dir = current_dir / ".git"

    if git_dir.exists():
        try:
            # Convertir le chemin au format absolu pour git
            dir_path = str(current_dir.resolve())

            # Ajouter le répertoire comme safe directory en global
            result = subprocess.run([
                "git",
                "config",
                "--global",
                "--add",
                "safe.directory",
                dir_path
            ], capture_output=True, text=True, cwd=str(current_dir))

            if result.returncode == 0:
                print("✅ Répertoire Git configuré comme safe directory (global)")
                return True
            else:
                # Essayer avec la configuration locale si global échoue
                result_local = subprocess.run([
                    "git",
                    "config",
                    "--local",
                    "safe.directory",
                    dir_path
                ], capture_output=True, text=True, cwd=str(current_dir))

                if result_local.returncode == 0:
                    print("✅ Répertoire Git configuré comme safe directory (local)")
                    return True
                else:
                    print(
                        f"⚠️  Erreur lors de la configuration Git: {result_local.stderr}")
                    return False
        except Exception as e:
            print(f"⚠️  Erreur lors de la configuration Git: {e}")
            return False
    else:
        print("⚠️  Dossier .git non trouvé")
        return False


def install_requirements():
    """Installer toutes les dépendances"""
    requirements_file = Path(__file__).parent.parent / "requirements.txt"

    if not requirements_file.exists():
        print("❌ Fichier requirements.txt non trouvé!")
        return False

    print("📦 Installation des dépendances...\n")

    try:
        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            str(requirements_file)
        ])
        print("\n✅ Dépendances installées avec succès!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erreur lors de l'installation: {e}")
        return False


if __name__ == "__main__":
    setup_git_safe_directory()
    install_requirements()
