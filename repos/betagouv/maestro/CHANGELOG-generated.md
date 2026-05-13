## Changelog : maestro (30 derniers jours, au 12 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de la stabilité et de la fonctionnalité de Maestro. Les efforts se sont concentrés sur l'amélioration de l'intégration avec les systèmes externes (Brevo, S3, OIDC), la correction de bugs et l'optimisation des performances, notamment au niveau des tests et de l'export de données. De nouvelles fonctionnalités ont été ajoutées pour faciliter la gestion des prélèvements, des analyses et des utilisateurs.

### Évolutions fonctionnelles
- Amélioration de la synchronisation des utilisateurs entre Maestro et Brevo [#840](https://github.com/betagouv/maestro/issues/840).
- Ajout de la possibilité de dupliquer les prélèvements en environnement de test [#842](https://github.com/betagouv/maestro/issues/842).
- Ajout d'un filtre sur les prélèvements avec plusieurs exemplaires [#850](https://github.com/betagouv/maestro/issues/850) et [#2fc8968](https://github.com/betagouv/maestro/commit/2fc8968).
- Ajout d'une interface pour consulter les DAI (Demandes d'Analyses Individualisées) [#798](https://github.com/betagouv/maestro/issues/798).
- Ajout d'une nouvelle interface pour l'envoi des DAI via SFTP [#698](https://github.com/betagouv/maestro/issues/698).
- Amélioration de la gestion des abattoirs et des utilisateurs associés [#836](https://github.com/betagouv/maestro/issues/836).
- Possibilité de valider la programmation si la région a approuvé celle-ci [#738](https://github.com/betagouv/maestro/issues/738).
- Possibilité de saisir le résultat des résidus complexes [#739](https://github.com/betagouv/maestro/issues/739).
- Ajout d'un service OIDC local pour l'authentification [#841](https://github.com/betagouv/maestro/issues/841).
- Ajout d'une table pour stocker toutes les RAI (Requêtes d'Analyse Individualisées) reçues [#870](https://github.com/betagouv/maestro/issues/870).
- Ajout d'une interface au S3 local [#889](https://github.com/betagouv/maestro/issues/889).

### Évolutions techniques
- Refactor de la gestion des dates et des types pour plus de cohérence.
- Amélioration de la gestion des erreurs et ajout de logs pour faciliter le débogage (notamment pour l'API Brevo [#886](https://github.com/betagouv/maestro/issues/886)).
- Mise à jour de nombreuses dépendances (React, TypeScript, Node.js, PostgreSQL, Express, etc.).
- Optimisation des tests et correction d'alertes obsolètes [#867](https://github.com/betagouv/maestro/issues/867).
- Ajout de sourcemaps pour Sentry afin d'améliorer le suivi des erreurs [#768](https://github.com/betagouv/maestro/issues/768).
- Amélioration du CI/CD avec ajout de cache pour Playwright [#814](https://github.com/betagouv/maestro/issues/814).
- Suppression de `exceljs` et ajout d'un test de non régression [#863](https://github.com/betagouv/maestro/issues/863).

### Autres changements
- Mise à jour de la documentation.
- Correction de divers bugs mineurs et améliorations de l'expérience utilisateur.
- Correction de l'affichage des prélèvements pour les administrateurs [#897](https://github.com/betagouv/maestro/issues/897).
- Correction d'un problème d'affichage des identifiants de listes Brevo [#901](https://github.com/betagouv/maestro/issues/901).
- Ajout d'un message d'alerte pour la vérification des informations avant l'envoi d'un prélèvement (temporairement revert puis réappliqué) [#902](https://github.com/betagouv/maestro/issues/902).
- Correction de l'affichage du SIRET de l'établissement [#885](https://github.com/betagouv/maestro/issues/885).
- Correction d'un problème empêchant de passer à l'étape 3 du prélèvement si l'étape 2 n'était pas complète [#869](https://github.com/betagouv/maestro/issues/869).
