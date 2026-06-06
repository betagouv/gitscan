## Changelog : sites-conformes (30 derniers jours, au 7 juin 2026)

### Résumé
Ce changelog présente les améliorations apportées à Sites Conformes au cours des 30 derniers jours. Les principales évolutions concernent l'ajout de Sentry pour la surveillance des erreurs, des améliorations de la documentation, la possibilité de stocker les médias directement en base de données (PostgreSQL) et des corrections de bugs sur l'interface utilisateur. Des travaux de packagification et de préparation de la release v3.2.0 ont également été réalisés.

### Évolutions fonctionnelles
- **Stockage des médias :** Possibilité de stocker les médias directement en PostgreSQL, offrant une alternative au stockage sur S3. [#482](https://github.com/numerique-gouv/sites-conformes/issues/482)
- **Corrections de bugs front-end :** Résolution de plusieurs bugs affectant l'interface utilisateur. [#486](https://github.com/numerique-gouv/sites-conformes/issues/486)

### Évolutions techniques
- **Intégration de Sentry :** Ajout de Sentry pour la surveillance et le suivi des erreurs applicatives. [#445](https://github.com/numerique-gouv/sites-conformes/issues/445)
- **Packagification :** Travaux de packagification du projet, incluant la récupération de la documentation et la préparation de la release v3.2.0. [#506](https://github.com/numerique-gouv/sites-conformes/issues/506), [#514](https://github.com/numerique-gouv/sites-conformes/issues/514)
- **Mise à jour des dépendances Python :** Mise à jour des dépendances Python pour bénéficier des dernières corrections et améliorations. [#501](https://github.com/numerique-gouv/sites-conformes/issues/501)
- **Refactoring :** Déplacement des sources namespacées dans le répertoire `sites_conformes/` en préparation de la release v3.2.0.
- **Préparation release v3.2.0 :** Application automatique des corrections proposées par `pre-commit` pour la version 3.2.0.

### Autres changements
- **Documentation :** Mise à jour de la documentation du projet. [#511](https://github.com/numerique-gouv/sites-conformes/issues/511)
- **Nom du dépôt :** Mise à jour du nom du dépôt. [#493](https://github.com/numerique-gouv/sites-conformes/issues/493)
- **Configuration :** Ajout de `demo` à `slugignore`.
