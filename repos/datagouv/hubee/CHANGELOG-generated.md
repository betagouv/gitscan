## Changelog : hubee (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité, la modernisation de l'infrastructure et la préparation du portail V2. Des corrections de vulnérabilités ont été apportées, le format des logs a été mis à jour pour une meilleure analyse, et l'intégration de Sentry permettra un suivi plus efficace des erreurs.

### Évolutions fonctionnelles
- **Sécurité :** Activation d'une politique de sécurité de contenu (CSP) minimale et gestion de `force_ssl` côté application pour renforcer la sécurité des échanges. [#87](https://github.com/datagouv/hubee/issues/87)
- **Portail V2 :** Début de la construction de l'interface utilisateur du portail V2 en utilisant le Design System FR (DSFR). [#73](https://github.com/datagouv/hubee/issues/73)
- **Logs :** Les logs sont désormais au format `logfmt`, plus adapté aux outils d'analyse et de surveillance. [#90](https://github.com/datagouv/hubee/issues/90)

### Évolutions techniques
- **Infrastructure :** Mise à jour de l'image Ruby Docker vers la version 4.0.5-slim. [#79](https://github.com/datagouv/hubee/issues/79) et [#74](https://github.com/datagouv/hubee/issues/74)
- **CI/CD :** La CI est désormais déclenchée quotidiennement pour une analyse statique et de sécurité régulière. [#85](https://github.com/datagouv/hubee/issues/85)
- **Configuration :** Suppression du fichier `credentials.yml.enc` et récupération des informations de connexion PostgreSQL via des variables d'environnement en production. [#94](https://github.com/datagouv/hubee/issues/94)
- **Renovate :** Renovate est désormais le seul outil de mise à jour des dépendances. [#88](https://github.com/datagouv/hubee/issues/88)
- **Devcontainer :** Suppression du devcontainer, car il n'était plus utilisé. [#82](https://github.com/datagouv/hubee/issues/82)
- **Monitoring :** Intégration de Sentry pour le suivi et la notification des erreurs. [#81](https://github.com/datagouv/hubee/issues/81)
- **Dépendances :** Mise à jour de la gem `cucumber-rails` vers la version 4.1.0 et de `aasm` vers la version 6.0.0. [#84](https://github.com/datagouv/hubee/issues/84) et [#83](https://github.com/datagouv/hubee/issues/83)
- **Correction de vulnérabilités :** Correction d'une vulnérabilité CVE dans la gem `crass`. [#80](https://github.com/datagouv/hubee/issues/80) et correction de 4 advisories sur `loofah` et `rails-html-sanitizer`. [#95](https://github.com/datagouv/hubee/issues/95)
- **Tests :** La gem `strong_migrations` est maintenant chargée dans tous les environnements. [#91](https://github.com/datagouv/hubee/issues/91)

### Autres changements
- Ajout de la gem `hub-api-v1` (client API Hubee V1). [#93](https://github.com/datagouv/hubee/issues/93)
- Restriction de la CI GitHub à l'analyse statique et à la sécurité. [#92](https://github.com/datagouv/hubee/issues/92)
- Mise à jour de l'image PostgreSQL dans le devcontainer vers la version 18. [#78](https://github.com/datagouv/hubee/issues/78)
- Mise à jour de l'action `actions/checkout` vers la version v7. [#76](https://github.com/datagouv/hubee/issues/76)
