## Changelog : apistration (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la maintenabilité du projet. Des corrections ont été apportées pour gérer les erreurs de fichiers et les problèmes liés aux jetons d'authentification. L'ajout d'une bannière d'annonce permet de communiquer des maintenances planifiées. Des efforts importants ont été faits pour harmoniser la configuration et les dépendances, ainsi que pour améliorer la documentation et la gestion des secrets.

### Évolutions fonctionnelles

*   Ajout d'une bannière d'annonce pour informer les utilisateurs des maintenances planifiées ([#33](https://github.com/datagouv/apistration/pull/33)).
*   Amélioration de l'affichage des jetons sur la page de gestion des demandes ([#32](https://github.com/datagouv/apistration/pull/32)).
*   Correction d'un bug d'affichage lié aux bénéficiaires sans participation à l'étranger ([#28](https://github.com/datagouv/apistration/pull/28)).
*   Ajout du régime de pensionnat dans l'API d'inscription des élèves (V5) ([#13](https://github.com/datagouv/apistration/pull/13)).
*   Mise à jour des mocks pour l'année paramétrique CNAV de 2023 à 2026.
*   Ajout de tous les endpoints manquants pour l'API Claude ([#242](https://github.com/datagouv/apistration/pull/242)).

### Évolutions techniques

*   Refactorisation de l'extraction d'un helper `AppConfig` pour la mémorisation par processus.
*   Correction d'un problème de `EBADF` sur les workers Puma en mémorisant les lectures de fichiers par requête ([#27](https://github.com/datagouv/apistration/pull/27)).
*   Mise en place d'un cooldown de 7 jours pour tous les groupes de mises à jour Dependabot ([#29](https://github.com/datagouv/apistration/pull/29)).
*   Migration des fichiers de credentials Rails vers des fichiers YAML en clair.
*   Amélioration de la gestion des credentials en staging ([#6](https://github.com/datagouv/apistration/pull/6), [#3](https://github.com/datagouv/apistration/pull/3)).
*   Import du code de `admin_api_entreprise` dans le dépôt ([#8](https://github.com/datagouv/apistration/pull/8)).
*   Refonte de la configuration CI/CD pour un monorepo.
*   Mise à jour des dépendances (Rubocop, RSpec, Faraday, etc.).
*   Ajout de tests pour les mocks et intégration dans le workflow CI.
*   Utilisation locale des fichiers OpenAPI.
*   Simplification de la gestion des tests avec l'introduction de `bin/test`.

### Autres changements

*   Ajout d'une adresse email pour la divulgation de vulnérabilités dans le fichier `CONTRIBUTING.md`.
*   Création d'un fichier `CONTRIBUTING.md` pour protéger les mainteneurs des PR hors scope.
*   Amélioration de la documentation README.
*   Suppression des anciens endpoints MEN (v3/v4).
*   Mise à jour des références `etalab/siade_staging_data` vers `datagouv/apistration`.
*   Correction de tests flaky.
*   Mise à jour des workflows GitHub pour le déploiement sur l'infrastructure.
*   Ajout de mocks pour les nouveaux endpoints.
*   Mise à jour des dépendances et configuration de Dependabot.
*   Amélioration de la configuration des tests et de la CI.
*   Correction de problèmes de Brakeman et de simplecov.
*   Ajout de la possibilité de lancer la CI sur push.
*   Correction d'un dump de contexte dans la CI.
*   Mise à jour de la documentation pour la nouvelle gestion des credentials.
