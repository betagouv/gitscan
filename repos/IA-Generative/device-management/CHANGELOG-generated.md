## Changelog : device-management (30 derniers jours, au 7 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité, la documentation et l'amélioration de la gestion des secrets. Des corrections importantes ont été apportées pour répondre aux vulnérabilités identifiées lors d'audits de sécurité, et la documentation a été restructurée pour une meilleure clarté.  Des améliorations ont également été apportées à la gestion des déploiements et à la configuration des extensions.

### Évolutions fonctionnelles
- Amélioration de l'exposition de l'ID des plugins dans l'API `/catalog/api/plugins` (au lieu du slug), facilitant l'intégration avec d'autres systèmes. [#9](https://github.com/IA-Generative/device-management/pull/9)
- Ajout de la prise en charge de la génération de fichiers XML et JSON pour les mises à jour, permettant une distribution multi-cible des extensions. [#20](https://github.com/IA-Generative/device-management/pull/20)
- Possibilité de configurer l'API via des variables d'environnement (API_BASE, RELAY_ASSISTANT_BASE_URL, etc.). [#25](https://github.com/IA-Generative/device-management/pull/25)
- Ajout d'une section "Comment fonctionnent les mises à jour" à la documentation. [#31](https://github.com/IA-Generative/device-management/pull/31)
- Amélioration de la gestion des redirects OIDC pour l'interface d'administration. [#36](https://github.com/IA-Generative/device-management/pull/36)

### Évolutions techniques
- Renforcement significatif de la sécurité suite à un audit, incluant la correction de plusieurs vulnérabilités (CT-1, CT-7, CT-9, CT-12, IMM-1..8). [#30](https://github.com/IA-Generative/device-management/pull/30)
- Mise à jour de Nginx en version 1.29-alpine pour corriger une vulnérabilité OpenSSL. [#41](https://github.com/IA-Generative/device-management/pull/41)
- Mise à jour des dépendances FastAPI et Starlette pour corriger des CVE. [#37](https://github.com/IA-Generative/device-management/pull/37)
- Suppression de composants obsolètes et potentiellement dangereux (Adminer, ingress Filebrowser). [#38](https://github.com/IA-Generative/device-management/pull/38) et [#39](https://github.com/IA-Generative/device-management/pull/39)
- Amélioration de la gestion des secrets dans Kubernetes, avec une normalisation de la configuration et suppression des secrets du dépôt. [#40](https://github.com/IA-Generative/device-management/pull/40) et [#42](https://github.com/IA-Generative/device-management/pull/42)
- Refonte de la structure de la documentation pour une meilleure organisation par audience. [#32](https://github.com/IA-Generative/device-management/pull/32)
- Ajout d'un fichier `.dockerignore` pour exclure les fichiers sensibles et inutiles du contexte de build Docker. [#43](https://github.com/IA-Generative/device-management/pull/43)

### Autres changements
- Suppression du relais `/llm` devenu inutile. [#44](https://github.com/IA-Generative/device-management/pull/44)
- Nettoyage du code et suppression de code mort. [#45](https://github.com/IA-Generative/device-management/pull/45)
- Mise à jour des variables d'environnement pour le déploiement Scaleway. [#46](https://github.com/IA-Generative/device-management/pull/46)
- Ajout d'un runbook de déploiement consolidé pour Scaleway et DGX. [#47](https://github.com/IA-Generative/device-management/pull/47)
- Ajout d'une note de sécurité pour le dépôt public. [#48](https://github.com/IA-Generative/device-management/pull/48)
- Publication d'un rapport d'audit de sécurité anonymisé. [#49](https://github.com/IA-Generative/device-management/pull/49)
- Caviardage de l'historique du dépôt avant sa publication. [#50](https://github.com/IA-Generative/device-management/pull/50)
