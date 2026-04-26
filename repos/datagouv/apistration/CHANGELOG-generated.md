## Changelog : apistration (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des données d'API, la refactorisation de l'architecture pour une meilleure maintenabilité et performance, ainsi que sur l'ajout de nouvelles fonctionnalités de surveillance et d'annonces pour les utilisateurs. Des corrections de bugs et des améliorations de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la gestion des quotas pour l'API GIP-MDS, incluant le suivi des erreurs 429 dans Sentry [#44](https://github.com/datagouv/apistration/pull/44).
- Implémentation d'une bannière d'annonce pour communiquer des maintenances planifiées (ProConnect) [#33](https://github.com/datagouv/apistration/pull/33).
- Ajout de la prise en charge du régime de pensionnat dans l'API Scolarités (MEN V5) [#13](https://github.com/datagouv/apistration/pull/13).
- Amélioration de la gestion des paramètres de civilité pour le QF, notamment avec le paramètre `nomUsage` [#45](https://github.com/datagouv/apistration/pull/45).
- Ajout de la possibilité d'afficher les informations de limitation de débit (rate limiting) sur chaque page d'endpoint de l'API [#48](https://github.com/datagouv/apistration/pull/48).
- Ajout de traductions pour les scopes d'autorisation [#42](https://github.com/datagouv/apistration/pull/42).

### Évolutions techniques
- Refactorisation majeure de la structure des définitions d'endpoints, avec déplacement des fichiers vers `commons/endpoints/` et intégration des données Swagger [#55](https://github.com/datagouv/apistration/pull/55).
- Simplification de la résolution des utilisateurs et de la gestion des tokens, avec l'introduction de `UserResolutionMiddleware` et la lecture des informations depuis `request.env` [#48](https://github.com/datagouv/apistration/pull/48).
- Amélioration de la gestion des fichiers de configuration, avec l'utilisation de fichiers YAML en clair au lieu des credentials chiffrés de Rails [#4](https://github.com/datagouv/apistration/pull/4).
- Mise en place d'un système de tests plus robuste, incluant des mocks et des tests d'intégration [#57](https://github.com/datagouv/apistration/pull/57), [#52](https://github.com/datagouv/apistration/pull/52).
- Mise à jour de l'infrastructure CI/CD pour une meilleure gestion des workflows et des dépendances [#61](https://github.com/datagouv/apistration/pull/61).
- Mise en place d'un système de cooldown pour les mises à jour de dépendances via Dependabot [#29](https://github.com/datagouv/apistration/pull/29).
- Ajout d'une sonde de monitoring pour DataSubvention [#43](https://github.com/datagouv/apistration/pull/43).
- Mise en place d'un système de gestion des bases de données isolées par worktree via dotenv [#60](https://github.com/datagouv/apistration/pull/60).
- Suppression de `DeferredGarbageCollection` pour améliorer la performance des tests.

### Autres changements
- Ajout d'une adresse email pour la divulgation de vulnérabilités de sécurité dans le fichier `CONTRIBUTING.md` [#35](https://github.com/datagouv/apistration/pull/35).
- Ajout d'un fichier `CONTRIBUTING.md` pour guider les contributeurs et protéger les mainteneurs [#35](https://github.com/datagouv/apistration/pull/35).
- Mise à jour de la documentation et des exemples pour refléter les changements apportés.
- Corrections mineures et améliorations de la lisibilité du code.
- Mises à jour de dépendances (Rubocop, Rack, ActionText-Trix, MCP) [#2177](https://github.com/datagouv/apistration/pull/2177), [#2176](https://github.com/datagouv/apistration/pull/2176), [#2175](https://github.com/datagouv/apistration/pull/2175), [#2174](https://github.com/datagouv/apistration/pull/2174).
