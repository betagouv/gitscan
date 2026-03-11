## Changelog : roadmaps-faciles (30 derniers jours)

### Résumé
Le projet a connu une période d'évolution rapide et significative au cours des 30 derniers jours. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, l'ajout de nouvelles fonctionnalités clés comme la synchronisation Notion, l'intégration de l'authentification avancée et la mise en place d'un système de gestion des tenants plus robuste. Des améliorations techniques importantes ont également été apportées, notamment en matière de CI/CD, de tests et de sécurité.

### Évolutions fonctionnelles
- Ajout d'un système de feature flags pour les super-admins [#97](https://github.com/incubateur-ademe/roadmaps-faciles/issues/97).
- Amélioration de l'expérience utilisateur du wizard d'intégration [#103](https://github.com/incubateur-ademe/roadmaps-faciles/issues/103).
- Refonte de la page des tenants avec une interface de type GitHub et un formulaire simplifié [#60](https://github.com/incubateur-ademe/roadmaps-faciles/issues/60).
- Ajout d'un mode iframe embarquable pour les boards et la roadmap [#64](https://github.com/incubateur-ademe/roadmaps-faciles/issues/64).
- Nouvelle vue liste compacte des posts [#55](https://github.com/incubateur-ademe/roadmaps-faciles/issues/55).
- Ajout de la possibilité de créer des posts anonymes avec modération et suppression [#32](https://github.com/incubateur-ademe/roadmaps-faciles/issues/32).
- Implémentation de l'internationalisation (français et anglais) [#21](https://github.com/incubateur-ademe/roadmaps-faciles/issues/21).
- Ajout d'un site de documentation utilisateur avec Fumadocs [#57](https://github.com/incubateur-ademe/roadmaps-faciles/issues/57).
- Ajout d'un système d'authentification avancé avec 2FA (passkey/OTP/email) et SSO OAuth pour les tenants [#61](https://github.com/incubateur-ademe/roadmaps-faciles/issues/61).
- Refonte des emails avec DSFR Mail et react-email [#58](https://github.com/incubateur-ademe/roadmaps-faciles/issues/58).
- Nouveau thème visuel avec une palette "French Blue" et refonte de la page d'accueil [#104](https://github.com/incubateur-ademe/roadmaps-faciles/issues/104).

### Évolutions techniques
- Mise en place d'un pipeline CI/CD basé sur GitHub Actions et Scalingo [#90](https://github.com/incubateur-ademe/roadmaps-faciles/issues/90).
- Ajout d'une suite de tests complète avec Vitest et Playwright E2E [#63](https://github.com/incubateur-ademe/roadmaps-faciles/issues/63).
- Intégration d'un connecteur Notion pour la synchronisation bidirectionnelle [#94](https://github.com/incubateur-ademe/roadmaps-faciles/issues/94).
- Implémentation d'un éditeur Markdown enrichi avec upload d'images sur S3 [#93](https://github.com/incubateur-ademe/roadmaps-faciles/issues/93).
- Ajout de Sentry pour le hardening et PostHog pour le tracking [#98](https://github.com/incubateur-ademe/roadmaps-faciles/issues/98).
- Refonte de l'architecture de l'authentification et ajout d'un pont SSO [#20](https://github.com/incubateur-ademe/roadmaps-faciles/issues/20).
- Mise en place d'un audit log et d'outils d'observabilité [#23](https://github.com/incubateur-ademe/roadmaps-faciles/issues/23).
- Correction de vulnérabilités de dépendances (hono, lodash) [#79](https://github.com/incubateur-ademe/roadmaps-faciles/issues/79).
- Amélioration du script de build pour plus de sécurité et suppression de variables d'environnement sensibles [#81](https://github.com/incubateur-ademe/roadmaps-faciles/issues/81).
- Mise en place d'un système de release-please pour la gestion des releases [#86](https://github.com/incubateur-ademe/roadmaps-faciles/issues/86).

### Autres changements
- Synchronisation de la documentation CLAUDE.md et README avec la documentation complète.
- Refonte des screenshots pour les thèmes et audit de la documentation.
- Ajout de règles de création d'issues GitHub.
- Mise à jour du template GitHub.
- Mise à jour du fichier TODO.md.
- Correction de problèmes de déploiement liés à Prisma migrate et à l'authentification SSH [#1234](https://github.com/incubateur-ademe/roadmaps-faciles/issues/1234).
- Correction de problèmes de linting et mise à jour de Storybook.
- Ajout d'un canonical redirect via PLATFORM_DOMAIN [#92](https://github.com/incubateur-ademe/roadmaps-faciles/issues/92).
- Correction de problèmes liés au CSP pour les domaines PostHog [#5d99311](https://github.com/incubateur-ademe/roadmaps-faciles/commit/5d99311).
- Filtrage des jobs CI par fichiers modifiés [#73](https://github.com/incubateur-ademe/roadmaps-faciles/issues/73).
- Suppression de NODE_ENV des fichiers .env.
- Correction du filtrage des tests CI pour éviter les déclenchements inutiles [#80](https://github.com/incubateur-ademe/roadmaps-faciles/issues/80).
