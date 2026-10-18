## Changelog : st-ansible (30 derniers jours, au 14 octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes avec l'ajout de nouveaux services de communication (Conversations) et de gestion de fichiers (Transfers et File-scanner). La sécurité du traitement des emails a été renforcée et l'outil de ligne de commande (CLI) a été optimisé pour rendre les mises à jour et la gestion du système plus robustes et fluides.

### Évolutions fonctionnelles
- **Nouveaux services** : Introduction des modules **Conversations**, **Transfers** et **File-scanner**, incluant l'intégration automatique de l'antivirus pour le scan de fichiers.

### Évolutions techniques
- **Messagerie et Sécurité** :
    - Amélioration du filtrage des messages via Rspamd (support d'Exav en remplacement de ClamAV et configuration du classificateur Bayes pour l'apprentissage automatique).
    - Transition vers le composant `pymta` et dépréciation de `mta-in`.
- **Outil CLI (st-cli)** :
    - Amélioration du processus de mise à jour avec l'ajout de la commande `rebootstrap` et une meilleure gestion des groupes d'hôtes hérités.
    - Refonte de la qualité du code (suppression du code mort, doublons et application des règles Ruff).
    - Découplage des tests de réparation du proxy SOCKS des drapeaux de mise à jour.
- **Infrastructure et Réseau** :
    - **Gestion des accès** : Mise en place de listes blanches d'adresses IP (allowlist) pour l'administration Django sur les services Docs, Drive et Meet.
    - **Architecture réseau** : Migration de l'accès "edge" de l'application Drive vers Caddy et intégration de Caddy devant l'image Keycloak pour les messages.
    - **Conteneurisation** : Optimisation de Podman avec l'installation de `podman-compose` et amélioration des tests de santé (healthchecks) des workers.

### Autres changements
- **Documentation** : Mise à jour de la documentation pour inclure les nouveaux rôles (Conversations), les procédures de bootstrap et les configurations de sécurité.
- **CI/CD** : Maintenance des workflows GitHub Actions (mise à jour des digests).
