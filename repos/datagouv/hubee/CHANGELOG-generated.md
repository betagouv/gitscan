## Changelog : hubee (30 derniers jours, au 13 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la sécurité, la modernisation de l'infrastructure et la préparation du portail V2. Des refactorings architecturaux ont été entrepris pour une meilleure modularité du code, et l'intégration de Sentry permettra un suivi plus précis des erreurs en production.

### Évolutions fonctionnelles
- **Sécurité:** Gestion améliorée de la configuration `force_ssl` et ajout d'une politique de sécurité de contenu (CSP) minimale pour renforcer la sécurité de l'application. [#87](https://github.com/datagouv/hubee/issues/87)
- **Portail V2:** Début de la mise en place du socle DSFR (Design System for French administration) pour le nouveau portail. [#73](https://github.com/datagouv/hubee/issues/73)

### Évolutions techniques
- **Infrastructure:** Mise à jour de Ruby en version 4.0.5 et de PostgreSQL en version 18.
- **CI/CD:** Restriction de la CI GitHub à l'analyse statique et à la sécurité, et ajout d'une exécution nocturne pour les tests. [#85](https://github.com/datagouv/hubee/issues/85)
- **Refactoring:** Refactorisation de l'architecture pour une meilleure modularité avec l'introduction de namespaces (`::API`, `::Portail`, `::Hubee`). [#69](https://github.com/datagouv/hubee/issues/69)
- **Monitoring:** Intégration de Sentry pour le suivi des erreurs et l'amélioration de la qualité de l'application. [#81](https://github.com/datagouv/hubee/issues/81)
- **Renovate:** Adoption de Renovate comme outil unique de mise à jour des dépendances. [#88](https://github.com/datagouv/hubee/issues/88) et [#72](https://github.com/datagouv/hubee/issues/72)

### Autres changements
- Ajout d'une gem client API Hubee V1. [#84](https://github.com/datagouv/hubee/issues/84)
- Documentation : Interdiction des références confidentielles dans le dépôt public. [#68](https://github.com/datagouv/hubee/issues/68)
- Suppression du devcontainer, jugé non utilisé. [#82](https://github.com/datagouv/hubee/issues/82)
- Mise à jour des gems et suppression des contraintes de version. [#66](https://github.com/datagouv/hubee/issues/66)
- Correction d'une vulnérabilité CVE dans la gem `crass`. [#80](https://github.com/datagouv/hubee/issues/80)
- Adoption du plugin `hubee-claude-plugin` comme source de vérité pour les aspects liés à l'IA. [#67](https://github.com/datagouv/hubee/issues/67)
- Gel de l'API V2, de PostgreSQL 18 et de Ruby 4.0.5 pour stabiliser l'environnement de développement. [#65](https://github.com/datagouv/hubee/issues/65)
