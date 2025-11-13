#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'installation des dépendances
À exécuter une seule fois avant de lancer l'application
"""

import subprocess
import sys
from pathlib import Path


def install_requirements():
    """Installer toutes les dépendances"""
    requirements_file = Path(__file__).parent / "requirements.txt"

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
    install_requirements()
