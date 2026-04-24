## Changelog : apistration (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des accès et des quotas, l'ajout de nouvelles fonctionnalités pour les API scolaires et la correction de plusieurs problèmes de tests et de configuration. Des améliorations de la documentation et de la sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la gestion du régime de pensionnat dans l'API Scolarités (V5) [#13](https://github.com/datagouv/apistration/pull/13).
- Implémentation d'une limitation de débit (rate limiting) pour l'API GIP-MDS, avec affichage des informations de limitation sur les pages d'endpoint [#48](https://github.com/datagouv/apistration/pull/48).
- Ajout d'une bannière d'annonce pour afficher des informations temporaires sur le site [#33](https://github.com/datagouv/apistration/pull/33).
- Ajout de la prise en charge du paramètre `nomUsage` pour la civilité dans l'API QF [#45](https://github.com/datagouv/apistration/pull/45).
- Ajout de traductions pour les scopes d'autorisation [#42](https://github.com/datagouv/apistration/pull/42).
- Mise à jour des mocks pour l'année scolaire 2026 [#52](https://github.com/datagouv/apistration/pull/52) et pour les cas de test avec un seul prénom pour l'EAJE [#51](https://github.com/datagouv/apistration/pull/51).

### Évolutions techniques
- Refactorisation de la gestion des utilisateurs et de l'authentification pour une meilleure centralisation et simplification [#50](https://github.com/datagouv/apistration/pull/50).
- Simplification de la lecture des informations de limitation de débit à partir de l'environnement de requête.
- Amélioration de la gestion des erreurs de quota pour l'API GIP-MDS, avec suivi via Sentry.
- Mise en place d'un système de cache pour les réponses de l'API GIP-MDS afin d'améliorer les performances.
- Mise à jour de la configuration des dépendances et des workflows CI/CD.
- Utilisation de fichiers YAML pour la gestion des identifiants, améliorant la sécurité et la flexibilité.
- Suppression de la collecte de déchets différée (DeferredGarbageCollection) pour améliorer la vitesse de la suite de tests.
- Stub de DataEncryptor dans les tests pour éviter les opérations GPG réelles.
- Amélioration de la gestion des fichiers de configuration et des secrets.
- Ajout de tests pour les mocks et correction de tests flaky.

### Autres changements
- Ajout d'une adresse e-mail pour la divulgation de vulnérabilités de sécurité dans le fichier CONTRIBUTING.md.
- Ajout d'un fichier README plus complet.
- Mise à jour de la documentation pour refléter les changements apportés.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de commentaires et de documentation pour faciliter la maintenance et la compréhension du code.
- Import des données de staging de siade.
- Mise à jour des références à etalab/siade_staging_data vers datagouv/apistration.
- Ajout de la possibilité de ping DataSubvention pour le monitoring [#43](https://github.com/datagouv/apistration/pull/43).
- Mise à jour des mocks pour l'API CNAV.
- Ajout de tests pour les mocks.
- Correction de problèmes liés aux identifiants de test en staging [#6](https://github.com/datagouv/apistration/pull/6).
- Ajout de nouveaux endpoints manquants [#242](https://github.com/datagouv/apistration/pull/242).
- Mise à jour des scopes manquants [#241](https://github.com/datagouv/apistration/pull/241).
- Correction d'un bug lié à l'affichage des anciens endpoints MEN.
- Mise à jour des dépendances et des outils de développement.
- Ajout d'un cooldown de 7 jours pour les mises à jour de dépendances.
