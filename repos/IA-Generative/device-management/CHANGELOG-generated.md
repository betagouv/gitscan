## Changelog : device-management (30 derniers jours, au 7 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité, la documentation et l'amélioration de la gestion des secrets et des déploiements. Des corrections de vulnérabilités ont été implémentées, la documentation a été restructurée pour une meilleure clarté et des améliorations ont été apportées à la gestion des configurations et des déploiements Kubernetes. Des fonctionnalités ont également été ajoutées pour améliorer la gestion des extensions et des mises à jour.

### Évolutions fonctionnelles
- Amélioration de l'exposition de l'ID des plugins dans l'API `/catalog/api/plugins` pour remplacer l'utilisation du slug. [#9](https://github.com/IA-Generative/device-management/pull/9)
- Ajout de la prise en charge de la génération de fichiers XML pour les mises à jour (gupdate) et JSON pour Mozilla, permettant une distribution multi-cible des extensions. [#20](https://github.com/IA-Generative/device-management/pull/20)
- Possibilité de configurer le template avec un token de service pour l'upload de plugins. [#20](https://github.com/IA-Generative/device-management/pull/20)
- Ajout d'une section "Comment fonctionnent les mises à jour" dans la documentation. [#31](https://github.com/IA-Generative/device-management/pull/31)

### Évolutions techniques
- **Sécurité :** Correction de plusieurs vulnérabilités de sécurité identifiées lors d'un audit, incluant des correctifs pour des problèmes liés à l'authentification, à la révocation d'accès et à des dépendances vulnérables (FastAPI, Starlette, Pytest). [#5](https://github.com/IA-Generative/device-management/pull/5), [#6](https://github.com/IA-Generative/device-management/pull/6), [#7](https://github.com/IA-Generative/device-management/pull/7)
- **Déploiement :** Mise à jour de l'image Docker vers la version 0.6.0 et configuration des variables d'environnement Kubernetes. [#9](https://github.com/IA-Generative/device-management/pull/9)
- **Gestion des secrets :** Normalisation de la gestion des secrets Kubernetes, en supprimant les secrets du code source et en utilisant des overlays spécifiques à l'environnement. [#7](https://github.com/IA-Generative/device-management/pull/7), [#20](https://github.com/IA-Generative/device-management/pull/20)
- **Infrastructure :** Suppression d'Adminer et de Filebrowser pour des raisons de sécurité et de maintenance (versions obsolètes).
- **Refactoring :** Suppression du relais `/llm` devenu inutile.
- Amélioration de la gestion des timeouts pour la récupération des JWKS (JSON Web Key Set) de Keycloak. [#4](https://github.com/IA-Generative/device-management/pull/4)
- Augmentation de la taille du buffer proxy pour gérer les gros cookies renvoyés lors du callback d'authentification.

### Autres changements
- Restructuration de la documentation par audience et séparation des artefacts internes. [#30](https://github.com/IA-Generative/device-management/pull/30)
- Ajout d'un plan de mise à jour de la documentation. [#30](https://github.com/IA-Generative/device-management/pull/30)
- Nettoyage du code. [#28](https://github.com/IA-Generative/device-management/pull/28)
- Ajout d'un fichier `.dockerignore` pour exclure les fichiers sensibles et inutiles du contexte de construction Docker.
- Mise à jour des versions minimales de Python.
- Suppression des clés secrètes du commit de base et ajout d'un fichier `.example` pour les configurations.
- Ajout de notes de sécurité pour le dépôt public.
- Suppression des versions historiques purgées du rapport d'audit anonymisé.
- Caviardage du HEAD avant publication en public.
