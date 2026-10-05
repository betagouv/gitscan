## Changelog : ci (30 derniers jours, au 01/10/2026)

### Résumé
Lancement de la version initiale du dépôt. Ce projet centralise désormais des workflows GitHub Actions réutilisables pour standardiser et automatiser les processus de CI/CD (Docker, Helm, Python, Sécurité) au sein de l'écosystème La Suite.

### Évolutions fonctionnelles
- **Nouveaux workflows réutilisables** : Mise à disposition de workflows pour la publication Docker, la gestion des charts Helm (lint et release), le linting Python, et la synchronisation des traductions via Crowdin.
- **Qualité et Sécurité** : Ajout de workflows pour la génération automatique de changelogs, l'évaluation de la qualité des projets et des scans de sécurité via Zizmor.
- **Utilitaires** : Nouvelle action pour la construction de templates d'emails.

### Évolutions techniques
- **Docker** : Introduction de builds multi-plateformes et de scans de sécurité Trivy optionnels (avec possibilité de ne pas bloquer le workflow en cas d'alerte).
- **Sécurité & Scan** : Migration des actions Trivy, correction d'un conflit de variable d'environnement (`DOCKER_CONTEXT`) et mise à jour du cache Trivy.
- **ArgoCD** : Migration de l'action de notification webhook et amélioration de la gestion des paramètres via l'environnement.
- **Optimisation CI** : Ajout d'une action de nettoyage de l'espace disque sur les runners et optimisation de la gestion de la concurrence pour les workflows de qualité.
- **Renovate** : Migration du preset partagé.

### Autres changements
- **Documentation** : Ajout d'un fichier README détaillant l'organisation et l'utilisation du dépôt.
