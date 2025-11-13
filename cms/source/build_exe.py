#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour compiler l'application en .exe avec PyInstaller
À exécuter après avoir installé PyInstaller: pip install pyinstaller
"""

import subprocess
import sys
from pathlib import Path
import shutil


def check_pyinstaller():
    """Vérifier que PyInstaller est installé"""
    try:
        import PyInstaller
        print(f"✅ PyInstaller trouvé: {PyInstaller.__version__}")
        return True
    except ImportError:
        print("❌ PyInstaller n'est pas installé!")
        print("Installez-le avec: pip install pyinstaller")
        return False


def compile_to_exe():
    """Compiler l'application en .exe"""

    if not check_pyinstaller():
        return False

    print("\n🔨 Compilation en cours...\n")

    spec_file = Path(__file__).parent / "rout_art_cms.spec"

    try:
        # Nettoyer les anciens builds
        build_dir = Path(__file__).parent / "build"
        dist_dir = Path(__file__).parent / "dist"

        if build_dir.exists():
            shutil.rmtree(build_dir)
            print("🗑️  Dossier build supprimé")

        # Compiler
        subprocess.check_call([
            sys.executable,
            "-m",
            "PyInstaller",
            str(spec_file),
            "--noconfirm"
        ])

        print("\n✅ Compilation réussie!")
        print(
            f"\n📦 L'exécutable se trouve dans: {dist_dir / 'Rout\'Art CMS.exe'}")
        print("\n🎉 Vous pouvez maintenant distribuer ce fichier .exe!")

        return True

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erreur lors de la compilation: {e}")
        return False


if __name__ == "__main__":
    success = compile_to_exe()
    sys.exit(0 if success else 1)
