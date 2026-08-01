## Changelog : hubee (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de hubee se concentrent sur l'amélioration de la sécurité, la modernisation de l'infrastructure et la simplification de la configuration. Des corrections de vulnérabilités ont été appliquées, le format des logs a été mis à jour pour une meilleure intégration avec les outils de surveillance, et la configuration de l'environnement de production a été simplifiée.

### Évolutions fonctionnelles
- Acceptation des Conditions Générales d'Utilisation (CGU) du DSFR requises par la dernière version de dsfr-assets [#100](https://github.com/datagouv/hubee/issues/100).
- Intégration de Sentry pour le suivi des erreurs, permettant une meilleure réactivité face aux incidents [#81](https://github.com/datagouv/hubee/issues/81).
- Activation d'une Content Security Policy (CSP) minimale et gestion de `force_ssl` côté application pour renforcer la sécurité [#87](https://github.com/datagouv/hubee/issues/87).

### Évolutions techniques
- Mise à jour de la configuration Renovate pour une gestion centralisée des dépendances [#92](https://github.com/datagouv/hubee/issues/92).
- Migration des logs au format `logfmt` pour une meilleure compatibilité avec les outils de surveillance et d'analyse [#90](https://github.com/datagouv/hubee/issues/90).
- Suppression des patchs Ruby de la documentation pour simplifier la maintenance et la compréhension du code [#93](https://github.com/datagouv/hubee/issues/93).
- Simplification de la configuration de l'environnement de production en dérivation des informations de connexion PostgreSQL à partir de variables d'environnement [#94](https://github.com/datagouv/hubee/issues/94).
- Ajout d'une gem client API Hubee V1 (`hub-api-v1`) [#84](https://github.com/datagouv/hubee/issues/84).
- Correction de vulnérabilités identifiées dans les dépendances Loofah et Rails HTML Sanitizer [#95](https://github.com/datagouv/hubee/issues/95) et Active Storage [#100](https://github.com/datagouv/hubee/issues/100).
- Mise à jour de plusieurs dépendances : `solid_queue` (v1.5.0), `solid_cable` (v4.0.2), `standard` (v1.56.0), `rails_semantic_logger` (v5.1.0), `simplecov` (v1), `ruby` (v4.0.6), `cucumber-rails` (v4.1.0), `aasm` (v6.0.0).

### Autres changements
- Restriction de la CI GitHub à l'analyse statique et à la sécurité pour optimiser les ressources [#85](https://github.com/datagouv/hubee/issues/85).
- Suppression du devcontainer, jugé inutile pour le projet [#82](https://github.com/datagouv/hubee/issues/82).
- Ajout d'une tâche planifiée pour déclencher la CI chaque nuit à 5h UTC [#85](https://github.com/datagouv/hubee/issues/85).
- Migration de la configuration SimpleCov vers l'API 1.x [#91](https://github.com/datagouv/hubee/issues/91).
- Chargement de `strong_migrations` dans tous les environnements [#91](https://github.com/datagouv/hubee/issues/91).
