#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire de Configuration - Stockage et récupération des paramètres
"""

import json
from pathlib import Path
import os


class ConfigManager:
    """Gère la configuration persistante de l'application"""

    def __init__(self):
        self.config_dir = Path.home() / ".rout_art_cms"
        self.config_file = self.config_dir / "config.json"
        self.default_config = {
            "repo_path": str(Path.home() / "Rout-Art"),
            "auto_pull": False,
            "auto_refresh": True,
            "default_port": 8000,
            "theme": "dark",
            "window_width": 1400,
            "window_height": 800
        }

        # Créer le répertoire de config s'il n'existe pas
        self.config_dir.mkdir(parents=True, exist_ok=True)

        # Charger ou créer la config
        self.config = self.default_config.copy()
        self.load_config()

    def load_config(self):
        """Charger la configuration depuis le fichier"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                    self.config.update(loaded_config)
            else:
                self.save_config()
        except Exception as e:
            print(f"Erreur lors du chargement de la config: {e}")
            self.config = self.default_config.copy()

    def save_config(self):
        """Sauvegarder la configuration"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de la config: {e}")

    def get_repo_path(self):
        """Récupérer le chemin du repository"""
        return self.config.get("repo_path", self.default_config["repo_path"])

    def set_repo_path(self, path):
        """Définir le chemin du repository"""
        self.config["repo_path"] = str(path)
        self.save_config()

    def get_auto_pull(self):
        """Récupérer le paramètre de pull automatique"""
        return self.config.get("auto_pull", self.default_config["auto_pull"])

    def set_auto_pull(self, value):
        """Définir le pull automatique"""
        self.config["auto_pull"] = bool(value)
        self.save_config()

    def get_auto_refresh(self):
        """Récupérer le paramètre de rafraîchissement automatique"""
        return self.config.get("auto_refresh", self.default_config["auto_refresh"])

    def set_auto_refresh(self, value):
        """Définir le rafraîchissement automatique"""
        self.config["auto_refresh"] = bool(value)
        self.save_config()

    def get_default_port(self):
        """Récupérer le port par défaut"""
        return self.config.get("default_port", self.default_config["default_port"])

    def set_default_port(self, port):
        """Définir le port par défaut"""
        self.config["default_port"] = int(port)
        self.save_config()

    def get_all_config(self):
        """Récupérer toute la configuration"""
        return self.config.copy()

    def reset_to_defaults(self):
        """Réinitialiser aux paramètres par défaut"""
        self.config = self.default_config.copy()
        self.save_config()
