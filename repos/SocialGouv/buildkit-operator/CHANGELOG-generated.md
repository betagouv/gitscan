## Changelog : buildkit-operator (30 derniers jours, au 27 juin 2026)

### Résumé
Ce mois-ci, l'équipe a réalisé d'importantes améliorations de sécurité, de robustesse et de flexibilité pour l'opérateur buildkit. Les nouveautés incluent l'ajout d'une authentification OIDC, la prise en charge de builds hors cluster via un proxy, et une nouvelle architecture à trois namespaces pour une meilleure isolation et gestion des ressources. Des efforts importants ont également été consacrés à la documentation et à l'amélioration des tests.

### Évolutions fonctionnelles
- Ajout de la prise en charge de l'authentification OIDC avec fallback pour une migration sans interruption de service. [#2026-06-26T21:49:41+02:00]
- Possibilité d'utiliser un nom d'hôte pour le gateway, permettant une configuration indépendante de l'IP. [#2026-06-27T00:43:20+02:00]
- Prise en charge de plusieurs domaines pour un seul gateway, permettant de servir différentes populations de clients. [#2026-06-26T13:52:26+02:00]
- Possibilité de réaliser des builds hors cluster via un proxy et un gateway sur le port 443. [#2026-06-26T13:35:07+02:00]
- Prise en charge des certificats mTLS encodés en base64, compatible avec la convention des variables masquées GitLab. [#2026-06-26T13:55:44+02:00]
- Composant GitLab CI/CD réutilisable pour simplifier l'intégration des builds. [#2026-06-26T12:34:48+02:00]
- Amélioration de la robustesse des builds en cas de cold-start et de proxy. [#2026-06-26T18:62:49+02:00]

### Évolutions techniques
- Refonte de l'architecture avec une séparation en trois namespaces : opérateur, builds et système. [#2026-06-26T09:30:19+02:00]
- Amélioration de la sécurité avec des politiques réseau pour le daemon, des attestations de supply-chain et un renforcement général de la sécurité. [#2026-06-26T13:52:06+02:00]
- Mise à jour des dépendances vers les dernières versions stables (Go 1.26.4, BuildKit v0.31.1, Kubernetes v0.36.1, controller-runtime v0.24.1). [#2026-06-26T00:13:52+02:00]
- Remplacement du Makefile par un Taskfile pour une meilleure gestion des tâches. [#2026-06-26T09:58:17+02:00]
- Implémentation de tests end-to-end complets avec une suite live pour chaque fonctionnalité et une couverture de sécurité OIDC. [#2026-06-26T23:40:09+02:00]
- Amélioration de la couverture des tests unitaires et ajout d'une porte de couverture CI. [#2026-06-26T20:04:25+02:00]
- Ajout de leader election pour les pods buildd afin de permettre plusieurs réplicas. [#2026-06-24T18:48:24+02:00]

### Autres changements
- Amélioration de la documentation avec des guides d'onboarding, des diagrammes d'architecture, des notes sur l'utilisation de Kata et des exemples de configuration. [#2026-06-26T12:12:44+02:00, #2026-06-25T22:26:02+02:00, #2026-06-25T18:57:57+02:00]
- Publication d'un site MkDocs Material avec la documentation. [#2026-06-25T07:36:04+02:00]
- Ajout d'un rapport de validation et de performance. [#2026-06-26T18:47:21+02:00, #2026-06-26T17:08:49+02:00]
- Correction de bugs et améliorations de la robustesse générale.
- Publication des versions v0.5.0, v0.5.1, v0.5.2, v0.6.0, v0.7.0, v0.8.0, v0.8.1, v0.8.2 et v0.8.3.
