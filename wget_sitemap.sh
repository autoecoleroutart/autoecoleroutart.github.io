#!/bin/zsh
# Script pour télécharger tous les liens du sitemap.xml

SITEMAP="sitemap.xml"

# Extraire les URLs du sitemap.xml
URLS=($(grep -oP '(?<=<loc>)[^<]+' "$SITEMAP"))

# Créer un dossier pour les téléchargements
DOWNLOAD_DIR="downloads"
mkdir -p "$DOWNLOAD_DIR"

# Télécharger chaque URL
for url in "$URLS[@]"; do
    echo "Téléchargement de $url ..."
    wget -P "$DOWNLOAD_DIR" "$url"
done

echo "Téléchargements terminés. Les fichiers sont dans le dossier $DOWNLOAD_DIR."