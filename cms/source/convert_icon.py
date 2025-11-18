#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour convertir l'icône PNG en ICO pour PyInstaller
"""

from PIL import Image
from pathlib import Path


def convert_png_to_ico():
    """Convertir logo_routart_modern.png en .ico"""

    # Chemins
    png_file = Path(__file__).parent.parent / \
        "icon" / "logo_routart_modern.png"
    ico_file = Path(__file__).parent.parent / "icon" / "logo_routart.ico"

    if not png_file.exists():
        print(f"❌ Fichier PNG non trouvé: {png_file}")
        return False

    try:
        print(f"🎨 Conversion de {png_file.name} en .ico...")

        # Ouvrir l'image PNG
        img = Image.open(png_file)

        # S'assurer que c'est en RGBA
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # Redimensionner à 256x256 (taille standard pour les icônes Windows)
        img = img.resize((256, 256), Image.Resampling.LANCZOS)

        # Sauvegarder en ICO
        img.save(ico_file, format='ICO')

        print(f"✅ Icône convertie avec succès: {ico_file}")
        print(f"📦 Fichier: {ico_file.name}")

        return True

    except ImportError:
        print("❌ Pillow n'est pas installé!")
        print("Installez-le avec: pip install pillow")
        return False
    except Exception as e:
        print(f"❌ Erreur lors de la conversion: {e}")
        return False


if __name__ == "__main__":
    success = convert_png_to_ico()
    exit(0 if success else 1)
