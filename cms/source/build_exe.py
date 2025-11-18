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
import os
import signal


def kill_exe_process():
    """Tuer les processus de l'exécutable CMS s'il est en cours d'exécution"""
    try:
        # Windows: utiliser taskkill
        subprocess.run(
            ['taskkill', '/IM', "Rout'Art CMS.exe", '/F'],
            capture_output=True,
            timeout=5
        )
        print("🛑 Processus de l'application fermé")
    except Exception:
        pass  # L'application n'est pas en cours d'exécution


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


def prepare_icon():
    """Préparer l'icône pour PyInstaller"""
    try:
        from convert_icon import convert_png_to_ico
        return convert_png_to_ico()
    except Exception as e:
        print(f"⚠️  Impossible de convertir l'icône: {e}")
        return False


def compile_to_exe():
    """Compiler l'application en .exe"""

    if not check_pyinstaller():
        return False

    # Fermer l'exécutable s'il est en cours d'exécution
    print("\n🛑 Vérification de l'application en cours d'exécution...\n")
    kill_exe_process()

    # Préparer l'icône
    print("\n🎨 Préparation de l'icône...\n")
    prepare_icon()

    print("\n🔨 Compilation en cours...\n")

    spec_file = Path(__file__).parent / "rout_art_cms.spec"

    try:
        # Nettoyer les anciens builds et dist
        build_dir = Path(__file__).parent / "build"
        dist_dir = Path(__file__).parent / "dist"

        if build_dir.exists():
            shutil.rmtree(build_dir)
            print("🗑️  Dossier build supprimé")

        # Nettoyer le dossier dist pour éviter les conflits
        if dist_dir.exists():
            try:
                shutil.rmtree(dist_dir)
                print("🗑️  Dossier dist supprimé")
            except Exception as e:
                print(f"⚠️  Impossible de supprimer dist: {e}")

        # Compiler
        subprocess.check_call([
            sys.executable,
            "-m",
            "PyInstaller",
            str(spec_file),
            "--noconfirm"
        ])

        # Nettoyer les dossiers intermédiaires après la compilation
        if build_dir.exists():
            shutil.rmtree(build_dir)
            print("🧹 Dossier build intermédiaire supprimé")

        # Nettoyer les fichiers .spec générés
        spec_temp = build_dir / "rout_art_cms"
        if spec_temp.exists():
            shutil.rmtree(spec_temp)

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
