## Changelog : hubee (30 derniers jours, au 9 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la modernisation de l'infrastructure et la préparation du portail V2. Cela inclut l'intégration d'outils de surveillance des erreurs (Sentry), la mise à jour des dépendances et l'amélioration de la structure du code pour une meilleure modularité. Des corrections de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Début du développement du socle DSFR pour le portail V2 [#73](https://github.com/datagouv/hubee/issues/73).
- Intégration de Sentry pour le suivi des erreurs, permettant une meilleure réactivité en cas de problèmes [#81](https://github.com/datagouv/hubee/issues/81).

### Évolutions techniques
- Refactoring de l'architecture pour une meilleure modularité, avec l'introduction de namespaces ::API, ::Portail et ::Hubee [#69](https://github.com/datagouv/hubee/issues/69).
- Mise à jour de PostgreSQL vers la version 18 [#78](https://github.com/datagouv/hubee/issues/78).
- Mise à jour de Ruby vers la version 4.0.5 [#79](https://github.com/datagouv/hubee/issues/79) et [#74](https://github.com/datagouv/hubee/issues/74).
- Adoption de Renovate comme unique robot de mise à jour des dépendances [#88](https://github.com/datagouv/hubee/issues/88).
- Mise en place d'une CI avec GitHub Actions et d'un hook pre-commit [#70](https://github.com/datagouv/hubee/issues/70).
- Mise à jour de l'action `actions/checkout` vers la version v7 [#76](https://github.com/datagouv/hubee/issues/76).
- Correction d'une vulnérabilité CVE dans la librairie Crass [#80](https://github.com/datagouv/hubee/issues/80).
- Gel de l'API V2, de PostgreSQL 18 et de Ruby 4.0.5 [#65](https://github.com/datagouv/hubee/issues/65).

### Autres changements
- Documentation : interdiction des références confidentielles dans le dépôt public [#68](https://github.com/datagouv/hubee/issues/68).
- Adoption de `hubee-claude-plugin` comme source de vérité pour l'IA [#67](https://github.com/datagouv/hubee/issues/67).
- Mise à jour des gems et suppression des contraintes de version [#66](https://github.com/datagouv/hubee/issues/66).
- Suppression du devcontainer, jugé inutile sur le projet [#82](https://github.com/datagouv/hubee/issues/82).
- Ajout d'un déclenchement de CI nocturne [#85](https://github.com/datagouv/hubee/issues/85).
