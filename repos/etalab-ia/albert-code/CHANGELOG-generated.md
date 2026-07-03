## Changelog : albert-code (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de la sécurité de l'environnement d'exécution d'Albert Code, notamment via des correctifs importants liés à l'installation et à la gestion des environnements virtuels. Des améliorations significatives ont également été apportées à la documentation et à l'expérience utilisateur, en particulier pour les développeurs.

### Évolutions fonctionnelles
- Amélioration de l'onboarding et de la validation de l'environnement virtuel (VM) avec un hint dynamique et une validation S15.
- Ajout d'un mode `--dry-run` et d'un sandbox de test pour une meilleure expérimentation et un développement plus sûr.
- Mise en place d'un bundle initial contenant la configuration, le runtime, les profils, l'installation, les templates et la documentation.
- Résolution immédiate de l'agent VM lors de l'installation.
- Correction d'un problème où la clé Albert était absente dans la VM (TUI), entraînant une erreur 401 [#ada1997](https://github.com/etalab-ia/albert-code/commit/ada1997).
- Correction du prompt choice cassé en command substitution, redirigeant tout affichage humain vers la sortie d'erreur standard.
- Correction d'un problème de synchronisation des skills (profondeur et collision) grâce à un cache et des symlinks.

### Évolutions techniques
- Renforcement de la sécurité avec un garde-fou CI anti-fuite et une doctrine VM-only.
- Migration des anciens formats de marqueurs legacy.
- Nettoyage des chemins d'installation et enregistrement des retours d'installation.
- Correction de plusieurs problèmes liés à l'installation et à la suppression de l'environnement (T-FIX-1 à T-FIX-4).
- Mise en place d'un marqueur unique pour l'installation.
- Application de permissions 600 sur les fichiers sensibles.
- Ajout d'une clé dédiée pour l'environnement.
- Implémentation d'une deny-list pour renforcer la sécurité.
- Fallback vers un TTY si nécessaire.

### Autres changements
- Mise à jour de la documentation README pour cibler un public de développeurs et supprimer les informations non pertinentes pour les utilisateurs finaux.
- Correction d'un banner corrompu dans le script `install.sh` en utilisant celui du README.
- Ajout d'une section "Dépannage" et de garde-fous dans le README, en lien avec les findings AC-R011/R012.
