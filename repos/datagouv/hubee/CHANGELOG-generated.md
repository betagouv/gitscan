## Changelog : hubee (30 derniers jours, au 06 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la modernisation de l'infrastructure et la préparation du portail V2. Cela inclut l'intégration d'outils de monitoring (Sentry), la mise à jour des dépendances et l'amélioration de la structure du code pour une meilleure modularité. Des corrections de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Début du développement du socle DSFR pour le portail V2, posant les bases de la nouvelle interface utilisateur. [#73](https://github.com/datagouv/hubee/pull/73)

### Évolutions techniques
- **Monitoring :** Intégration de Sentry pour le suivi et la résolution des erreurs en production. [#81](https://github.com/datagouv/hubee/pull/81)
- **CI/CD :** Mise en place de GitHub Actions pour l'intégration continue et l'ajout d'un hook pre-commit pour garantir la qualité du code. [#70](https://github.com/datagouv/hubee/pull/70)
- **Refactoring :** Refactorisation de l'architecture en namespaces (`::API`, `::Portail`, `::Hubee`) pour une meilleure organisation et modularité du code. [#69](https://github.com/datagouv/hubee/pull/69)
- **Dépendances :**
    - Mise à jour de Ruby en version 4.0.5. [#79](https://github.com/datagouv/hubee/pull/79) et [#78](https://github.com/datagouv/hubee/pull/78)
    - Mise à jour de PostgreSQL en version 18. [#78](https://github.com/datagouv/hubee/pull/78)
    - Mise à jour de Cucumber-Rails en version 4.1.0. [#84](https://github.com/datagouv/hubee/pull/84)
    - Mise à jour de AASM en version 6.0.0. [#83](https://github.com/datagouv/hubee/pull/83)
    - Mise à jour de l'action `actions/checkout` en version 7. [#76](https://github.com/datagouv/hubee/pull/76)
- **Automatisation :** Mise en place de Renovate pour la gestion automatisée des dépendances sur le portail V2. [#72](https://github.com/datagouv/hubee/pull/72)

### Autres changements
- **Sécurité :** Correction d'une vulnérabilité CVE dans la gem `crass`. [#80](https://github.com/datagouv/hubee/pull/80)
- **Documentation :** Interdiction des références confidentielles dans le dépôt public. [#68](https://github.com/datagouv/hubee/pull/68)
- **IA :** Adoption de `hubee-claude-plugin` comme source de vérité pour les aspects liés à l'intelligence artificielle. [#67](https://github.com/datagouv/hubee/pull/67)
- **Configuration :** Gel de l'API V2, de PostgreSQL 18 et de Ruby 4.0.5 pour stabiliser l'environnement de développement. [#65](https://github.com/datagouv/hubee/pull/65)
- Suppression du devcontainer, jugé inutile. [#82](https://github.com/datagouv/hubee/pull/82)
- Mise à jour des gems et suppression des contraintes de version. [#66](https://github.com/datagouv/hubee/pull/66)
