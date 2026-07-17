## Changelog : hubee (30 derniers jours, au 2026-07-15)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité, la modernisation de l'infrastructure et la préparation du portail V2. Des améliorations ont également été apportées à la CI/CD et au monitoring pour une meilleure qualité et stabilité de la plateforme.

### Évolutions fonctionnelles
- Amélioration de la sécurité avec la gestion de `force_ssl` côté application et l'activation d'une Content Security Policy (CSP) minimale. [#87](https://github.com/datagouv/hubee/pull/87)
- Début de la construction du socle DSFR pour le portail V2, posant les bases de la nouvelle interface utilisateur. [#73](https://github.com/datagouv/hubee/pull/73)
- Ajout d'un client API Hubee V1 (gem `hub-api-v1`) pour faciliter l'intégration avec d'autres services. [#84](https://github.com/datagouv/hubee/pull/84)

### Évolutions techniques
- Refactorisation de l'architecture en namespaces (`::API`, `::Portail`, `::Hubee`) pour une meilleure organisation du code. [#69](https://github.com/datagouv/hubee/pull/69)
- Mise en place de Renovate comme seul robot de mise à jour des dépendances. [#88](https://github.com/datagouv/hubee/pull/88)
- Intégration de Sentry pour le suivi des erreurs et l'amélioration de la qualité du code. [#81](https://github.com/datagouv/hubee/pull/81)
- Migration de la configuration de la connexion PostgreSQL vers des variables d'environnement en production pour une meilleure sécurité. [#94](https://github.com/datagouv/hubee/pull/94)
- Passage des logs au format `logfmt` recommandé par le CSIRT pour une meilleure lisibilité et analyse. [#90](https://github.com/datagouv/hubee/pull/90)
- Mise à jour de l'image Docker Ruby vers la version 4.0.5-slim. [#79](https://github.com/datagouv/hubee/pull/79)
- Mise à jour de PostgreSQL dans l'environnement de développement vers la version 18. [#78](https://github.com/datagouv/hubee/pull/78)
- Ajout d'une CI GitHub Actions et d'un hook pre-commit pour automatiser les tests et la validation du code. [#70](https://github.com/datagouv/hubee/pull/70)
- Restriction de la CI GitHub à l'analyse statique et à la sécurité. [#92](https://github.com/datagouv/hubee/pull/92)

### Autres changements
- Suppression du devcontainer, jugé non utilisé sur le projet. [#82](https://github.com/datagouv/hubee/pull/82)
- Documentation : interdiction des références confidentielles dans le dépôt public. [#68](https://github.com/datagouv/hubee/pull/68)
- Correction d'une vulnérabilité CVE dans la gem `crass`. [#80](https://github.com/datagouv/hubee/pull/80)
- Mise à jour de l'action `actions/checkout` vers la version v7. [#76](https://github.com/datagouv/hubee/pull/76)
- Mise en place de Renovate sur le portail V2. [#72](https://github.com/datagouv/hubee/pull/72)
- Déclenchement de la CI chaque nuit à 5h UTC. [#85](https://github.com/datagouv/hubee/pull/85)
- Chargement de la gem `strong_migrations` dans tous les environnements. [#91](https://github.com/datagouv/hubee/pull/91)
- Ajout de la gem cucumber-rails en version 4.1.0 [#84](https://github.com/datagouv/hubee/pull/84)
- Mise à jour de la gem aasm en version 6.0.0 [#83](https://github.com/datagouv/hubee/pull/83)
