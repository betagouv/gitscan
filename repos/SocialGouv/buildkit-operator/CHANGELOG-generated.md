## Changelog : buildkit-operator (30 derniers jours, au 27 juin 2026)

### Résumé
Ce mois-ci, l'opérateur buildkit a connu une évolution significative, axée sur la sécurité, la flexibilité et l'intégration avec divers outils de CI/CD comme GitHub Actions, GitLab et Forgejo. Des améliorations ont été apportées pour supporter des environnements plus complexes, notamment avec l'ajout de fonctionnalités pour les builds hors cluster et l'isolation des builds via Kata Containers. L'opérateur est désormais plus robuste et configurable pour répondre aux besoins d'une plus large gamme d'utilisateurs.

### Évolutions fonctionnelles
- Ajout du support pour l'utilisation de variables d'environnement et de labels avec GitHub Actions, GitLab et Forgejo via l'option `--build-arg` et `--label` [#1](https://github.com/SocialGouv/buildkit-operator/issues/1).
- Prise en charge de l'authentification OIDC (OpenID Connect) pour une sécurité accrue, avec une migration progressive et une compatibilité avec les méthodes d'authentification existantes.
- Possibilité d'utiliser un gateway unique pour plusieurs populations clientes (multi-domain).
- Support de builds hors cluster via un proxy d'égress, permettant d'utiliser l'opérateur dans des environnements réseau restreints.
- Intégration avec GitLab CI/CD via un composant réutilisable.
- Prise en charge de l'utilisation de certificats mTLS encodés en base64, compatible avec les variables masquées de GitLab.
- Amélioration de la gestion des builds en utilisant Kata Containers pour l'isolation et la sécurité.
- Ajout de la possibilité d'utiliser un cache froid S3 configurable par projet.

### Évolutions techniques
- Refactorisation de l'architecture pour une meilleure séparation des préoccupations et une plus grande maintenabilité.
- Passage à une topologie à trois namespaces (opérateur, builds, système) pour une meilleure organisation et sécurité.
- Mise à jour des dépendances vers les dernières versions stables (Go 1.26.4, BuildKit v0.31.1, Kubernetes v0.36.1, controller-runtime v0.24.1).
- Amélioration des tests unitaires et d'intégration, avec une couverture accrue et une intégration continue plus robuste.
- Utilisation de GitHub Actions pour la publication des charts Helm et des images OCI.
- Remplacement du Makefile par un Taskfile pour une meilleure gestion des tâches de build et de déploiement.
- Implémentation de leader election pour les pods buildd afin d'assurer la haute disponibilité.
- Amélioration de la gestion des erreurs et de la résilience du système.
- Ajout d'un système de snapshot pour la durabilité des builds.

### Autres changements
- Mise à jour de la documentation avec des guides d'installation, d'utilisation et de dépannage.
- Ajout d'un site de documentation généré avec MkDocs Material.
- Ajout d'un rapport de validation des fonctionnalités et des performances.
- Correction de plusieurs bugs et améliorations de la stabilité.
- Amélioration des messages de log et de la surveillance.
- Ajout d'un schéma d'architecture détaillé.
- Ajout d'un guide d'onboarding pour les nouveaux contributeurs.
- Correction de problèmes liés à la gestion des timeouts et des connexions.
- Amélioration de la gestion des ressources et de la scalabilité.
