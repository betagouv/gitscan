## Changelog : hubee (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de Hubee se concentrent sur l'amélioration de la sécurité, la modernisation de l'infrastructure et la préparation du portail V2. Des corrections de vulnérabilités ont été apportées, la configuration de Renovate a été revue et l'intégration de Sentry permet un meilleur suivi des erreurs en production.

### Évolutions fonctionnelles
- **Sécurité:** Activation du `force_ssl` au niveau de l'application et ajout d'une politique de sécurité du contenu (CSP) minimale pour renforcer la sécurité. [#87](https://github.com/datagouv/hubee/pulls/87)
- **Portail V2:** Début de l'implémentation de la base du portail V2 en utilisant le Design System FR (DSFR). [#73](https://github.com/datagouv/hubee/pulls/73)
- **Monitoring:** Intégration de Sentry pour le suivi et la notification des erreurs en production. [#81](https://github.com/datagouv/hubee/pulls/81)

### Évolutions techniques
- **Configuration:** Suppression du fichier `credentials.yml.enc` et récupération des informations de connexion PostgreSQL via 4 variables d'environnement en production. [#94](https://github.com/datagouv/hubee/pulls/94)
- **Logs:** Passage des logs au format `logfmt` recommandé par le CSIRT. [#90](https://github.com/datagouv/hubee/pulls/90)
- **Renovate:** Configuration de Renovate pour être le seul robot de mise à jour et regroupement de la version Ruby sur `depName`. [#88](https://github.com/datagouv/hubee/pulls/88), [#92](https://github.com/datagouv/hubee/pulls/92), [#62](https://github.com/datagouv/hubee/pulls/62)
- **CI/CD:** Restriction de la CI GitHub à l'analyse statique et à la sécurité. [#85](https://github.com/datagouv/hubee/pulls/85)
- **Docker:** Ajout d'un argument de construction pour la gem `bundler` dans le Dockerfile. [#93](https://github.com/datagouv/hubee/pulls/93)
- **Dépendances:** Mise à jour de plusieurs dépendances : `solid_cable` vers v4.0.2 [#100](https://github.com/datagouv/hubee/pulls/100), `rails_semantic_logger` vers v5.1.0, `simplecov` vers v1, `cucumber-rails` vers 4.1.0 [#84](https://github.com/datagouv/hubee/pulls/84), `aasm` vers 6.0.0 [#83](https://github.com/datagouv/hubee/pulls/83).
- **Correction de vulnérabilités:** Correction de 4 vulnérabilités identifiées dans `loofah` et `rails-html-sanitizer`. [#95](https://github.com/datagouv/hubee/pulls/95)
- **Correction de CVE:** Correction de la CVE dans `crass`. [#80](https://github.com/datagouv/hubee/pulls/80)

### Autres changements
- Suppression des patchs Ruby de la documentation.
- Ajout de la gem `hub-api-v1` (client API Hubee V1).
- Suppression du devcontainer, car non utilisé. [#82](https://github.com/datagouv/hubee/pulls/82)
- Mise à jour de la version de PostgreSQL dans le devcontainer vers 18. [#78](https://github.com/datagouv/hubee/pulls/78)
- Migration de la configuration SimpleCov vers l'API 1.x.
- Chargement de `strong_migrations` dans tous les environnements. [#91](https://github.com/datagouv/hubee/pulls/91)
- La CI est déclenchée chaque nuit à 5h UTC.
