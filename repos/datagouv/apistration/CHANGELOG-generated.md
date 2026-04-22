## Changelog : apistration (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la surveillance de l'API, notamment en ajoutant des mécanismes de limitation de débit et de suivi des erreurs. Des corrections ont été apportées pour améliorer la gestion des jetons d'authentification et des mocks pour les tests. L'infrastructure CI/CD a également été revue pour faciliter les déploiements et la gestion des dépendances.

### Évolutions fonctionnelles
- Ajout d'une limitation de débit (rate limiting) pour l'API GIP-MDS, avec affichage d'informations sur les limites de débit pour chaque endpoint. [#48](https://github.com/datagouv/apistration/pull/48)
- Amélioration de la gestion des quotas GIP-MDS avec le suivi des erreurs 429 dans Sentry. [#44](https://github.com/datagouv/apistration/pull/44)
- Ajout d'une nouvelle fonctionnalité permettant de pinguer DataSubvention pour vérifier sa disponibilité. [#43](https://github.com/datagouv/apistration/pull/43)
- Ajout de la prise en charge du régime de pensionnat dans l'API des scolarités (MEN V5). [#13](https://github.com/datagouv/apistration/pull/13)
- Ajout de mocks pour les tests de l'année scolaire 2026 et pour les cas de test avec un seul prénom pour les EAJE. [#51](https://github.com/datagouv/apistration/pull/51), [#52](https://github.com/datagouv/apistration/pull/52)
- Correction de l'affichage des jetons sur la page `/compte/demandes`. [#32](https://github.com/datagouv/apistration/pull/32)
- Correction de l'affichage des informations sur les bénéficiaires sans participation né à l'étranger. [#34](https://github.com/datagouv/apistration/pull/34)
- Ajout d'une bannière d'annonce pour informer les utilisateurs de la maintenance de ProConnect. [#33](https://github.com/datagouv/apistration/pull/33)
- Ajout de traductions pour les scopes d'autorisation. [#42](https://github.com/datagouv/apistration/pull/42)

### Évolutions techniques
- Refactorisation de la configuration du rate limiting pour utiliser les `operation_id` au lieu des couples controller/action. [#48](https://github.com/datagouv/apistration/pull/48)
- Mise à jour de la dépendance `jwt` pour corriger un problème lié à la base64 dans Ruby 4.0. [#43](https://github.com/datagouv/apistration/pull/43)
- Mise en place d'un système de gestion des credentials centralisé et plus robuste. [#4](https://github.com/datagouv/apistration/pull/4), [#6](https://github.com/datagouv/apistration/pull/6)
- Amélioration de la gestion des fichiers temporaires pour éviter les erreurs `EBADF` sur les workers Puma. [#27](https://github.com/datagouv/apistration/pull/27)
- Mise en place d'un système de tests plus complet et fiable, incluant des tests pour les mocks. [#17](https://github.com/datagouv/apistration/pull/17), [#29](https://github.com/datagouv/apistration/pull/29)
- Refactorisation de l'infrastructure CI/CD pour une meilleure organisation et une gestion plus facile des déploiements. [#26](https://github.com/datagouv/apistration/pull/26), [#35](https://github.com/datagouv/apistration/pull/35)
- Utilisation de fichiers YAML pour la configuration des credentials au lieu des credentials chiffrés Rails. [#4](https://github.com/datagouv/apistration/pull/4)
- Mise à jour des dépendances (Rubocop, Rack, Activestorage, etc.).

### Autres changements
- Ajout d'un fichier `CONTRIBUTING.md` pour encourager les contributions et protéger les mainteneurs. [#35](https://github.com/datagouv/apistration/pull/35)
- Mise à jour de la documentation README. [#9](https://github.com/datagouv/apistration/pull/9), [#20](https://github.com/datagouv/apistration/pull/20)
- Ajout d'un cooldown de 7 jours pour les mises à jour de dépendances. [#29](https://github.com/datagouv/apistration/pull/29)
- Import des données de staging de siade. [#14](https://github.com/datagouv/apistration/pull/14)
- Correction de bugs mineurs et améliorations de la qualité du code.
- Suppression des anciens endpoints MEN (v3/v4). [#27](https://github.com/datagouv/apistration/pull/27)
- Ajout de mocks pour les tests.
