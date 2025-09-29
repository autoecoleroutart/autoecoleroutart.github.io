#!/bin/zsh
# Script pour télécharger toutes les images des pages listées dans le sitemap.xml

SITEMAP="sitemap.xml"
PAGE_DIR="pages"
IMG_DIR="images"

mkdir -p "$PAGE_DIR"
mkdir -p "$IMG_DIR"

# Extraire les URLs des pages du sitemap.xml
PAGES=($(grep -oP '(?<=<loc>)[^<]+' "$SITEMAP"))

# Télécharger chaque page HTML
for page_url in "$PAGES[@]"; do
    echo "Téléchargement de la page $page_url ..."
    page_file="$PAGE_DIR/$(basename $page_url)"
    wget -O "$page_file" "$page_url"

    # Extraire les URLs d'images de la page téléchargée
    IMG_URLS=($(grep -oP '<img[^>]+src=["'\'']\K([^"'\'']+)' "$page_file"))

    # Télécharger chaque image
    for img_url in "$IMG_URLS[@]"; do
        # Gérer les URLs relatives
        if [[ "$img_url" != http* ]]; then
            # Préfixer avec le domaine de la page
            domain=$(echo "$page_url" | grep -oP '^https?://[^/]+')
            img_url="$domain/$img_url"
        fi
        echo "  Téléchargement de l'image $img_url ..."
        wget -P "$IMG_DIR" "$img_url"
    done

done

echo "Téléchargement des images terminé. Les fichiers sont dans le dossier $IMG_DIR."