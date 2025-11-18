#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire Git - Opérations de synchronisation avec GitHub
"""

from git import Repo, GitCommandError
from pathlib import Path
import datetime
import os
import subprocess


class GitManager:
    """Gère les opérations Git (pull, push, statut)"""

    def __init__(self, logger):
        self.logger = logger
        self._setup_git_safe_directory()

    def _setup_git_safe_directory(self):
        """Configurer le répertoire comme safe directory pour éviter les erreurs de propriété"""
        try:
            repo_path = Path(__file__).parent.parent.parent
            result = subprocess.run(
                ["git", "config", "--global", "--add",
                    "safe.directory", str(repo_path.resolve())],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                self.logger.log("Git safe directory configuré")
        except Exception as e:
            self.logger.log(
                f"Attention: impossible de configurer git safe directory: {e}")


class GitManager:
    """Gère les opérations Git (pull, push, statut)"""

    def __init__(self, logger):
        self.logger = logger

    def verify_repo(self, repo_path):
        """Vérifier si le chemin est un repository Git valide"""
        try:
            repo = Repo(repo_path)
            self._ensure_git_config(repo_path)
            return {
                "valid": True,
                "message": f"✓ Repository valide\nBranche: {repo.active_branch.name}\nURL: {repo.remotes.origin.url}"
            }
        except Exception as e:
            return {
                "valid": False,
                "message": f"✗ Erreur: {str(e)}"
            }

    def _ensure_git_config(self, repo_path):
        """S'assurer que le répertoire est configuré comme safe"""
        try:
            subprocess.run(
                ["git", "config", "--global", "--add",
                    "safe.directory", str(Path(repo_path).resolve())],
                capture_output=True,
                cwd=repo_path
            )
        except:
            pass

    def pull(self, repo_path):
        """Pull les dernières modifications"""
        try:
            self._ensure_git_config(repo_path)
            repo = Repo(repo_path)

            # Fetch
            origin = repo.remotes.origin
            origin.fetch()

            # Pull
            current_branch = repo.active_branch
            origin.pull(current_branch.name)

            message = f"✓ Pull réussi\nBranche: {current_branch.name}\nTimestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            self.logger.log(f"Git pull réussi depuis {current_branch.name}")

            return {"success": True, "message": message}
        except GitCommandError as e:
            error_msg = f"✗ Erreur Git: {str(e)}"
            self.logger.log(f"Erreur Git: {error_msg}")
            return {"success": False, "message": error_msg}
        except Exception as e:
            error_msg = f"✗ Erreur: {str(e)}"
            self.logger.log(f"Erreur: {error_msg}")
            return {"success": False, "message": error_msg}

    def push(self, repo_path, commit_message):
        """Push les modifications vers le repository distant"""
        try:
            self._ensure_git_config(repo_path)
            repo = Repo(repo_path)

            # Ajouter tous les fichiers modifiés
            if repo.is_dirty(untracked_files=True):
                repo.git.add(A=True)

                # Commit
                repo.index.commit(commit_message)

                # Push
                origin = repo.remotes.origin
                current_branch = repo.active_branch
                origin.push(current_branch.name)

                message = f"✓ Push réussi\nMessage: {commit_message}\nBranche: {current_branch.name}\nTimestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                self.logger.log(f"Git push réussi: {commit_message}")

                return {"success": True, "message": message}
            else:
                message = "ℹ️  Aucune modification à pousser"
                self.logger.log(message)
                return {"success": True, "message": message}

        except GitCommandError as e:
            error_msg = f"✗ Erreur Git: {str(e)}"
            self.logger.log(f"Erreur Git: {error_msg}")
            return {"success": False, "message": error_msg}
        except Exception as e:
            error_msg = f"✗ Erreur: {str(e)}"
            self.logger.log(f"Erreur: {error_msg}")
            return {"success": False, "message": error_msg}

    def get_status(self, repo_path):
        """Récupérer le statut du repository"""
        try:
            repo = Repo(repo_path)

            # Info de base
            status = f"📊 STATUT DU REPOSITORY\n"
            status += f"{'='*60}\n\n"

            # Branche actuelle
            status += f"🌳 Branche actuelle: {repo.active_branch.name}\n"

            # Fichiers staged (à commiter) avec leur type
            staged_diffs = repo.index.diff("HEAD")
            if staged_diffs:
                status += f"\n✅ Changements suivi ({len(staged_diffs)}):\n"
                for item in staged_diffs:
                    file_path = item.a_path
                    change_type = item.change_type

                    # Déterminer l'icône selon le type de changement
                    if change_type == 'A':  # Added
                        icon = "[AJOUTER]"
                    elif change_type == 'D':  # Deleted
                        icon = "[SUPPRIMER]"
                    elif change_type == 'R':  # Renamed
                        icon = "[RENOMMER]"
                    else:  # Modified
                        icon = "[MODIFIER]"

                    status += f"   {icon} {file_path}\n"
            else:
                status += f"\n✓ Aucun changement suivi\n"

            # Fichiers modifiés non staged avec leur type
            unstaged_diffs = repo.index.diff(None)
            if unstaged_diffs:
                status += f"\n❌ Changements non suivi ({len(unstaged_diffs)}):\n"
                for item in unstaged_diffs:
                    file_path = item.a_path
                    change_type = item.change_type

                    # Déterminer l'icône selon le type de changement
                    if change_type == 'A':  # Added
                        icon = "[AJOUTER]"
                    elif change_type == 'D':  # Deleted
                        icon = "[SUPPRIMER]"
                    elif change_type == 'R':  # Renamed
                        icon = "[RENOMMER]"
                    else:  # Modified
                        icon = "[MODIFIER]"

                    status += f"   {icon} {file_path}\n"
            else:
                status += f"\n✓ Aucun fichier modifié non suivi\n"

            # Fichiers non suivis
            untracked = repo.untracked_files
            if untracked:
                status += f"\n📄 Fichiers non suivis ({len(untracked)}):\n"
                for file in untracked:
                    status += f"   [EN AJOUT] {file}\n"
            else:
                status += f"\n✓ Aucun fichier non suivi\n"

            # Dernier commit
            if repo.head.is_valid():
                latest_commit = repo.head.commit
                status += f"\n📝 Dernier commit:\n"
                status += f"   Auteur: {latest_commit.author.name}\n"
                status += f"   Message: {latest_commit.message.strip()}\n"
                status += f"   Date: {datetime.datetime.fromtimestamp(latest_commit.committed_date).strftime('%Y-%m-%d %H:%M:%S')}\n"

            # Branche de suivi
            if repo.active_branch.tracking_branch():
                status += f"\n🔗 Suivi: {repo.active_branch.tracking_branch().name}\n"

            # Historique récent
            status += f"\n📜 Historique récent:\n"
            for i, commit in enumerate(repo.iter_commits(max_count=5)):
                status += f"   {i+1}. {commit.message.strip()[:60]}\n"

            return {"success": True, "output": status}

        except Exception as e:
            error_msg = f"✗ Erreur lors du statut: {str(e)}"
            return {"success": False, "output": error_msg}
