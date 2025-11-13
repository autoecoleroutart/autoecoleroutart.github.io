#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚗 Rout'Art CMS - Application de Gestion du Site
Application desktop pour gérer le contenu du site Rout'Art
Permet: Pull Git, édition HTML, préview local et Push Git
"""

import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
from tkinter import ttk
import customtkinter as ctk
import threading
import json
import os
import sys
from pathlib import Path

# Imports locaux
from git_manager import GitManager
from html_manager import HTMLManager
from server_manager import ServerManager
from config_manager import ConfigManager
from logger import Logger

# Configuration du thème CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class RoutArtCMS:
    """Application principale du CMS Rout'Art"""

    def __init__(self, root):
        self.root = root
        self.root.title("🚗 Rout'Art - Gestionnaire de Contenu (CMS)")
        self.root.geometry("1400x800")
        self.root.minsize(1000, 600)

        # Gestionnaires
        self.config_manager = ConfigManager()
        self.logger = Logger()
        self.git_manager = GitManager(self.logger)
        self.html_manager = HTMLManager(self.logger)
        self.server_manager = ServerManager(self.logger)

        # État de l'application
        self.repo_path = tk.StringVar(
            value=self.config_manager.get_repo_path())
        self.current_file = None
        self.server_thread = None
        self.server_running = False

        # Charger la configuration sauvegardée
        self.config_manager.load_config()

        # Construire l'interface
        self._build_ui()

        # Vérifier si le repo existe au démarrage
        self._on_startup()

    def _build_ui(self):
        """Construire l'interface utilisateur"""

        # Frame principal avec tabs
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Créer les tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Onglets
        self._create_git_tab()
        self._create_editor_tab()
        self._create_preview_tab()
        self._create_settings_tab()
        self._create_logs_tab()

    def _create_git_tab(self):
        """Onglet pour les opérations Git"""
        git_frame = ttk.Frame(self.notebook)
        self.notebook.add(git_frame, text="🔗 Git & Synchronisation")

        # Section Repository
        repo_section = ctk.CTkFrame(git_frame)
        repo_section.pack(fill=tk.X, padx=15, pady=15)

        ctk.CTkLabel(repo_section, text="Chemin du Repository:",
                     font=("Arial", 12, "bold")).pack(anchor="w", pady=5)

        repo_frame = ctk.CTkFrame(repo_section)
        repo_frame.pack(fill=tk.X, pady=5)

        ctk.CTkEntry(repo_frame, textvariable=self.repo_path, height=35).pack(
            side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ctk.CTkButton(repo_frame, text="📁 Parcourir",
                      command=self._browse_repo, width=120).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(repo_frame, text="✓ Vérifier",
                      command=self._verify_repo, width=120).pack(side=tk.LEFT, padx=5)

        # Section Actions Git
        actions_section = ctk.CTkFrame(git_frame)
        actions_section.pack(fill=tk.X, padx=15, pady=15)

        ctk.CTkLabel(actions_section, text="Actions Git:", font=(
            "Arial", 12, "bold")).pack(anchor="w", pady=5)

        buttons_frame = ctk.CTkFrame(actions_section)
        buttons_frame.pack(fill=tk.X, pady=10)

        ctk.CTkButton(buttons_frame, text="⬇️  Pull (Récupérer les modifications)",
                      command=self._git_pull, width=200, height=40, font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(buttons_frame, text="⬆️  Push (Envoyer les modifications)",
                      command=self._git_push, width=200, height=40, font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(buttons_frame, text="📊 Statut",
                      command=self._git_status, width=100, height=40).pack(side=tk.LEFT, padx=5)

        # Message de commit
        ctk.CTkLabel(actions_section, text="Message de commit:",
                     font=("Arial", 11)).pack(anchor="w", pady=(15, 5))
        self.commit_message = ctk.CTkEntry(
            actions_section, placeholder_text="Exemple: Mise à jour des tarifs", height=35)
        self.commit_message.pack(fill=tk.X, pady=5)
        self.commit_message.insert(0, "Mise à jour du contenu")

        # Status panel
        status_section = ctk.CTkFrame(git_frame)
        status_section.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        ctk.CTkLabel(status_section, text="Statut du Repository:",
                     font=("Arial", 12, "bold")).pack(anchor="w", pady=5)

        self.git_status_display = ctk.CTkTextbox(
            status_section, height=200, state="disabled")
        self.git_status_display.pack(fill=tk.BOTH, expand=True, pady=5)

    def _create_editor_tab(self):
        """Onglet pour l'édition du contenu"""
        editor_frame = ttk.Frame(self.notebook)
        self.notebook.add(editor_frame, text="✏️  Éditeur de Contenu")

        # Sélection du fichier
        file_section = ctk.CTkFrame(editor_frame)
        file_section.pack(fill=tk.X, padx=15, pady=15)

        ctk.CTkLabel(file_section, text="Fichier à éditer:", font=(
            "Arial", 12, "bold")).pack(anchor="w", pady=5)

        file_frame = ctk.CTkFrame(file_section)
        file_frame.pack(fill=tk.X, pady=5)

        self.file_combo = ctk.CTkComboBox(file_frame,
                                          values=self._get_page_files(),
                                          command=self._on_file_selected,
                                          height=35)
        self.file_combo.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        ctk.CTkButton(file_frame, text="🔄 Actualiser",
                      command=self._refresh_files, width=120).pack(side=tk.LEFT, padx=5)

        # Contenu éditable
        content_section = ctk.CTkFrame(editor_frame)
        content_section.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        ctk.CTkLabel(content_section, text="Contenu HTML:", font=(
            "Arial", 12, "bold")).pack(anchor="w", pady=5)

        self.editor_text = scrolledtext.ScrolledText(content_section, height=20, wrap=tk.WORD,
                                                     bg="#2b2b2b", fg="#ffffff", font=("Courier", 10))
        self.editor_text.pack(fill=tk.BOTH, expand=True, pady=5)

        # Boutons d'action
        button_frame = ctk.CTkFrame(editor_frame)
        button_frame.pack(fill=tk.X, padx=15, pady=15)

        ctk.CTkButton(button_frame, text="💾 Sauvegarder", command=self._save_file,
                      width=150, height=35).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="↻ Recharger", command=self._reload_file,
                      width=150, height=35).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="🔍 Rechercher", command=self._show_find_dialog,
                      width=150, height=35).pack(side=tk.LEFT, padx=5)

    def _create_preview_tab(self):
        """Onglet pour la prévisualisation locale"""
        preview_frame = ttk.Frame(self.notebook)
        self.notebook.add(preview_frame, text="👁️  Prévisualisation")

        # Section serveur
        server_section = ctk.CTkFrame(preview_frame)
        server_section.pack(fill=tk.X, padx=15, pady=15)

        ctk.CTkLabel(server_section, text="Serveur Local HTTP:",
                     font=("Arial", 12, "bold")).pack(anchor="w", pady=5)

        server_frame = ctk.CTkFrame(server_section)
        server_frame.pack(fill=tk.X, pady=10)

        self.server_status_label = ctk.CTkLabel(
            server_frame, text="⚫ Arrêté", font=("Arial", 11), text_color="red")
        self.server_status_label.pack(side=tk.LEFT, padx=5)

        ctk.CTkLabel(server_frame, text="Port:", font=(
            "Arial", 11)).pack(side=tk.LEFT, padx=5)
        self.port_entry = ctk.CTkEntry(server_frame, width=100, height=35)
        self.port_entry.pack(side=tk.LEFT, padx=5)
        self.port_entry.insert(0, "8000")

        self.server_toggle_btn = ctk.CTkButton(server_frame, text="▶️  Démarrer Serveur",
                                               command=self._toggle_server, width=150, height=35)
        self.server_toggle_btn.pack(side=tk.LEFT, padx=5)

        # URL d'accès
        url_section = ctk.CTkFrame(preview_frame)
        url_section.pack(fill=tk.X, padx=15, pady=15)

        ctk.CTkLabel(url_section, text="URL de prévisualisation:",
                     font=("Arial", 11)).pack(anchor="w", pady=5)

        url_frame = ctk.CTkFrame(url_section)
        url_frame.pack(fill=tk.X, pady=5)

        self.url_label = ctk.CTkLabel(url_frame, text="http://localhost:8000",
                                      text_color="cyan", font=("Arial", 11, "underline"))
        self.url_label.pack(side=tk.LEFT, padx=5)

        ctk.CTkButton(url_frame, text="🌐 Ouvrir dans le navigateur",
                      command=self._open_preview, width=180).pack(side=tk.LEFT, padx=5)

        # Instructions
        info_section = ctk.CTkFrame(preview_frame)
        info_section.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        ctk.CTkLabel(info_section, text="Instructions:", font=(
            "Arial", 12, "bold")).pack(anchor="w", pady=5)

        instructions = """
1️⃣  Cliquez sur "Démarrer Serveur" pour lancer un serveur local
2️⃣  Le serveur servira les fichiers depuis votre repository
3️⃣  Cliquez sur "Ouvrir dans le navigateur" pour voir le site en direct
4️⃣  Les modifications sauvegardées s'affichent immédiatement
5️⃣  Cliquez sur "Arrêter Serveur" pour terminer la session
        """

        info_label = ctk.CTkLabel(
            info_section, text=instructions, justify="left", font=("Arial", 10))
        info_label.pack(anchor="nw", pady=10)

        # Logs du serveur
        logs_section = ctk.CTkFrame(preview_frame)
        logs_section.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        ctk.CTkLabel(logs_section, text="Logs du serveur:",
                     font=("Arial", 11)).pack(anchor="w", pady=5)

        self.server_logs = ctk.CTkTextbox(
            logs_section, height=100, state="disabled")
        self.server_logs.pack(fill=tk.BOTH, expand=True)

    def _create_settings_tab(self):
        """Onglet pour les paramètres"""
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="⚙️  Paramètres")

        # Section configuration
        config_section = ctk.CTkFrame(settings_frame)
        config_section.pack(fill=tk.X, padx=15, pady=15)

        ctk.CTkLabel(config_section, text="Configuration Générale:",
                     font=("Arial", 12, "bold")).pack(anchor="w", pady=5)

        # Repo par défaut
        ctk.CTkLabel(config_section, text="Chemin du repository par défaut:", font=(
            "Arial", 11)).pack(anchor="w", pady=(10, 5))
        self.default_repo = ctk.CTkEntry(config_section, height=35)
        self.default_repo.pack(fill=tk.X, pady=5)
        self.default_repo.insert(0, self.config_manager.get_repo_path())

        # Options
        self.auto_pull_var = tk.BooleanVar(
            value=self.config_manager.get_auto_pull())
        ctk.CTkCheckBox(config_section, text="Pull automatique au démarrage",
                        variable=self.auto_pull_var).pack(anchor="w", pady=5)

        self.auto_refresh_var = tk.BooleanVar(
            value=self.config_manager.get_auto_refresh())
        ctk.CTkCheckBox(config_section, text="Rafraîchir automatiquement l'éditeur",
                        variable=self.auto_refresh_var).pack(anchor="w", pady=5)

        # Boutons
        button_frame = ctk.CTkFrame(config_section)
        button_frame.pack(fill=tk.X, pady=20)

        ctk.CTkButton(button_frame, text="💾 Sauvegarder les paramètres",
                      command=self._save_settings, width=200, height=35).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="🔄 Réinitialiser",
                      command=self._reset_settings, width=150, height=35).pack(side=tk.LEFT, padx=5)

    def _create_logs_tab(self):
        """Onglet pour les logs"""
        logs_frame = ttk.Frame(self.notebook)
        self.notebook.add(logs_frame, text="📋 Logs")

        # Contrôles
        controls_frame = ctk.CTkFrame(logs_frame)
        controls_frame.pack(fill=tk.X, padx=15, pady=15)

        ctk.CTkButton(controls_frame, text="🗑️  Effacer les logs",
                      command=self._clear_logs, width=150).pack(side=tk.LEFT, padx=5)
        ctk.CTkButton(controls_frame, text="💾 Exporter les logs",
                      command=self._export_logs, width=150).pack(side=tk.LEFT, padx=5)

        # Logs display
        self.logs_display = ctk.CTkTextbox(logs_frame, state="disabled")
        self.logs_display.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Refresh logs periodically
        self._refresh_logs_display()

    # ======= Méthodes Git =======

    def _browse_repo(self):
        """Parcourir et sélectionner un dossier"""
        path = filedialog.askdirectory(
            title="Sélectionner le dossier du repository")
        if path:
            self.repo_path.set(path)
            self.config_manager.set_repo_path(path)

    def _verify_repo(self):
        """Vérifier que le repo existe et est valide"""
        path = self.repo_path.get()
        result = self.git_manager.verify_repo(path)
        if result["valid"]:
            messagebox.showinfo("✓ Repository Valide", result["message"])
            self._update_git_status()
        else:
            messagebox.showerror("✗ Erreur Repository", result["message"])

    def _git_pull(self):
        """Pull du repository"""
        path = self.repo_path.get()
        if not path:
            messagebox.showerror(
                "Erreur", "Veuillez spécifier le chemin du repository")
            return

        # Exécuter en thread pour ne pas bloquer l'UI
        thread = threading.Thread(target=self._git_pull_thread, args=(path,))
        thread.daemon = True
        thread.start()

    def _git_pull_thread(self, path):
        """Thread pour le pull"""
        try:
            result = self.git_manager.pull(path)
            self.root.after(0, lambda: messagebox.showinfo(
                "Pull Réussi", result["message"]))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "Erreur Pull", str(e)))
        finally:
            self.root.after(0, self._update_git_status)

    def _git_push(self):
        """Push du repository"""
        path = self.repo_path.get()
        message = self.commit_message.get()

        if not path:
            messagebox.showerror(
                "Erreur", "Veuillez spécifier le chemin du repository")
            return

        if not message:
            messagebox.showerror(
                "Erreur", "Veuillez entrer un message de commit")
            return

        thread = threading.Thread(
            target=self._git_push_thread, args=(path, message))
        thread.daemon = True
        thread.start()

    def _git_push_thread(self, path, message):
        """Thread pour le push"""
        try:
            result = self.git_manager.push(path, message)
            self.root.after(0, lambda: messagebox.showinfo(
                "Push Réussi", result["message"]))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "Erreur Push", str(e)))
        finally:
            self.root.after(0, self._update_git_status)

    def _git_status(self):
        """Afficher le statut du repository"""
        path = self.repo_path.get()
        thread = threading.Thread(target=self._git_status_thread, args=(path,))
        thread.daemon = True
        thread.start()

    def _git_status_thread(self, path):
        """Thread pour le statut"""
        try:
            result = self.git_manager.get_status(path)
            self.root.after(0, lambda: self._display_git_status(result))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "Erreur Statut", str(e)))

    def _display_git_status(self, status):
        """Afficher le statut dans le textbox"""
        self.git_status_display.configure(state="normal")
        self.git_status_display.delete("1.0", tk.END)
        self.git_status_display.insert("1.0", status["output"])
        self.git_status_display.configure(state="disabled")

    def _update_git_status(self):
        """Mettre à jour le statut Git"""
        self._git_status()

    # ======= Méthodes Éditeur =======

    def _get_page_files(self):
        """Récupérer la liste des fichiers HTML disponibles"""
        page_dir = Path(self.repo_path.get()) / "page"
        if page_dir.exists():
            files = sorted([f.name for f in page_dir.glob("*.html")])
            return files
        return []

    def _refresh_files(self):
        """Rafraîchir la liste des fichiers"""
        files = self._get_page_files()
        self.file_combo.configure(values=files)
        messagebox.showinfo("Succès", f"{len(files)} fichiers trouvés")

    def _on_file_selected(self, choice):
        """Charger le fichier sélectionné"""
        if not choice:
            return

        repo_path = self.repo_path.get()
        file_path = Path(repo_path) / "page" / choice

        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                self.editor_text.config(state=tk.NORMAL)
                self.editor_text.delete("1.0", tk.END)
                self.editor_text.insert("1.0", content)
                self.editor_text.config(state=tk.NORMAL)

                self.current_file = file_path
                self.logger.log(f"Fichier ouvert: {choice}")
            except Exception as e:
                messagebox.showerror(
                    "Erreur", f"Impossible de charger le fichier: {e}")
        else:
            messagebox.showerror("Erreur", f"Fichier introuvable: {file_path}")

    def _save_file(self):
        """Sauvegarder le fichier modifié"""
        if not self.current_file:
            messagebox.showerror("Erreur", "Aucun fichier sélectionné")
            return

        try:
            content = self.editor_text.get("1.0", tk.END)
            with open(self.current_file, 'w', encoding='utf-8') as f:
                f.write(content)

            messagebox.showinfo(
                "Succès", f"Fichier sauvegardé: {self.current_file.name}")
            self.logger.log(f"Fichier sauvegardé: {self.current_file.name}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de sauvegarder: {e}")

    def _reload_file(self):
        """Recharger le fichier"""
        if self.file_combo.get():
            self._on_file_selected(self.file_combo.get())
            messagebox.showinfo("Succès", "Fichier rechargé")

    def _show_find_dialog(self):
        """Afficher la boîte de dialogue de recherche"""
        find_window = tk.Toplevel(self.root)
        find_window.title("Rechercher")
        find_window.geometry("400x150")

        ctk.CTkLabel(find_window, text="Rechercher:",
                     font=("Arial", 11)).pack(pady=5)
        search_entry = ctk.CTkEntry(find_window, height=35)
        search_entry.pack(fill=tk.X, padx=10, pady=5)

        ctk.CTkLabel(find_window, text="Remplacer par:",
                     font=("Arial", 11)).pack(pady=5)
        replace_entry = ctk.CTkEntry(find_window, height=35)
        replace_entry.pack(fill=tk.X, padx=10, pady=5)

        def do_replace_all():
            search_text = search_entry.get()
            replace_text = replace_entry.get()
            if search_text:
                content = self.editor_text.get("1.0", tk.END)
                new_content = content.replace(search_text, replace_text)
                self.editor_text.config(state=tk.NORMAL)
                self.editor_text.delete("1.0", tk.END)
                self.editor_text.insert("1.0", new_content)
                messagebox.showinfo(
                    "Succès", f"Remplacé {content.count(search_text)} occurrence(s)")
                find_window.destroy()

        ctk.CTkButton(find_window, text="Remplacer tout",
                      command=do_replace_all).pack(pady=10)

    # ======= Méthodes Serveur =======

    def _toggle_server(self):
        """Démarrer/arrêter le serveur local"""
        if self.server_running:
            self._stop_server()
        else:
            self._start_server()

    def _start_server(self):
        """Démarrer le serveur local"""
        try:
            port = int(self.port_entry.get())
            repo_path = self.repo_path.get()

            if not Path(repo_path).exists():
                messagebox.showerror(
                    "Erreur", "Le chemin du repository n'existe pas")
                return

            # Démarrer le serveur en thread
            self.server_thread = threading.Thread(
                target=self.server_manager.start,
                args=(repo_path, port, self._on_server_log)
            )
            self.server_thread.daemon = False  # NOT daemon - on veut l'arrêter proprement
            self.server_thread.start()

            self.server_running = True
            self.server_toggle_btn.configure(text="⏹️  Arrêter Serveur")
            self.server_status_label.configure(
                text=f"🟢 Actif (Port {port})", text_color="green")
            self.url_label.configure(text=f"http://localhost:{port}")

            self.logger.log(f"Serveur démarré sur le port {port}")
            messagebox.showinfo(
                "Succès", f"Serveur local démarré sur http://localhost:{port}")

        except ValueError:
            messagebox.showerror("Erreur", "Le port doit être un nombre")
        except Exception as e:
            messagebox.showerror(
                "Erreur", f"Impossible de démarrer le serveur: {e}")

    def _stop_server(self):
        """Arrêter le serveur local"""
        try:
            self.server_manager.stop()
            self.server_running = False
            self.server_toggle_btn.configure(text="▶️  Démarrer Serveur")
            self.server_status_label.configure(
                text="⚫ Arrêté", text_color="red")
            self.logger.log("Serveur arrêté")
            messagebox.showinfo("Succès", "Serveur arrêté")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'arrêt: {e}")

    def _on_server_log(self, message):
        """Ajouter un log du serveur"""
        self.root.after(0, lambda: self._append_server_log(message))

    def _append_server_log(self, message):
        """Ajouter le message aux logs du serveur"""
        self.server_logs.configure(state="normal")
        self.server_logs.insert(tk.END, message + "\n")
        self.server_logs.see(tk.END)
        self.server_logs.configure(state="disabled")

    def _open_preview(self):
        """Ouvrir la prévisualisation dans le navigateur"""
        if not self.server_running:
            messagebox.showerror("Erreur", "Le serveur n'est pas actif")
            return

        import webbrowser
        port = self.port_entry.get()
        url = f"http://localhost:{port}"
        webbrowser.open(url)

    # ======= Méthodes Paramètres =======

    def _save_settings(self):
        """Sauvegarder les paramètres"""
        try:
            self.config_manager.set_repo_path(self.default_repo.get())
            self.config_manager.set_auto_pull(self.auto_pull_var.get())
            self.config_manager.set_auto_refresh(self.auto_refresh_var.get())
            self.config_manager.save_config()
            messagebox.showinfo("Succès", "Paramètres sauvegardés")
        except Exception as e:
            messagebox.showerror(
                "Erreur", f"Erreur lors de la sauvegarde: {e}")

    def _reset_settings(self):
        """Réinitialiser les paramètres"""
        self.default_repo.delete(0, tk.END)
        self.default_repo.insert(0, str(Path.home() / "Rout-Art"))
        self.auto_pull_var.set(False)
        self.auto_refresh_var.set(True)

    # ======= Méthodes Logs =======

    def _refresh_logs_display(self):
        """Rafraîchir l'affichage des logs"""
        logs = self.logger.get_logs()
        self.logs_display.configure(state="normal")
        self.logs_display.delete("1.0", tk.END)
        self.logs_display.insert("1.0", "\n".join(logs))
        self.logs_display.configure(state="disabled")

        # Refresh periodic
        self.root.after(1000, self._refresh_logs_display)

    def _clear_logs(self):
        """Effacer les logs"""
        self.logger.clear_logs()
        self._refresh_logs_display()
        messagebox.showinfo("Succès", "Logs effacés")

    def _export_logs(self):
        """Exporter les logs"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                logs = self.logger.get_logs()
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write("\n".join(logs))
                messagebox.showinfo("Succès", f"Logs exportés: {file_path}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'export: {e}")

    # ======= Startup =======

    def _on_startup(self):
        """Actions au démarrage"""
        if self.config_manager.get_auto_pull():
            self.logger.log("Pull automatique au démarrage...")
            self._git_pull()


def main():
    """Point d'entrée principal"""
    root = ctk.CTk()
    app = RoutArtCMS(root)
    root.mainloop()


if __name__ == "__main__":
    main()
