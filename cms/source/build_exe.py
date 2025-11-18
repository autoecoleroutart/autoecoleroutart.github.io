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


def compile_to_exe():
    """Compiler l'application en .exe"""

    if not check_pyinstaller():
        return False

    # Fermer l'exécutable s'il est en cours d'exécution
    print("\n🛑 Vérification de l'application en cours d'exécution...\n")
    kill_exe_process()

    print("\n🔨 Compilation en cours...\n")

    # Le répertoire parent du script est cms/source, on doit remonter à la racine du projet
    source_dir = Path(__file__).parent
    project_root = source_dir.parent.parent
    spec_file = source_dir / "rout_art_cms.spec"

    try:
        # Nettoyer les anciens builds et dist à la racine du projet
        build_dir = project_root / "build"
        dist_dir = project_root / "dist"

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

        # Changer le répertoire de travail à la racine du projet pour la compilation
        original_cwd = os.getcwd()
        os.chdir(project_root)

        try:
            # Compiler
            subprocess.check_call([
                sys.executable,
                "-m",
                "PyInstaller",
                str(spec_file),
                "--noconfirm"
            ])
        finally:
            os.chdir(original_cwd)

        # Nettoyer les dossiers intermédiaires après la compilation
        if build_dir.exists():
            shutil.rmtree(build_dir)
            print("🧹 Dossier build supprimé")

        exe_path = dist_dir / "Rout'Art CMS.exe"
        print("\n✅ Compilation réussie!")
        print(f"\n📦 L'exécutable se trouve dans: {exe_path}")
        print("\n🎉 Vous pouvez maintenant distribuer ce fichier .exe!")

        return True

    except subprocess.CalledProcessError as e:
        print(f"\n❌ Erreur lors de la compilation: {e}")
        return False


if __name__ == "__main__":
    success = compile_to_exe()
    sys.exit(0 if success else 1)
