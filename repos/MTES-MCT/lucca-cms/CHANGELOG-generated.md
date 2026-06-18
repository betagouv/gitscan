## Changelog : lucca-cms (30 derniers jours, au 2026-06-17)

### Résumé
Les dernières mises à jour de lucca-cms se concentrent sur l'amélioration de la qualité du code, la correction de problèmes de validation et l'ajout de fonctionnalités de surveillance des erreurs avec Sentry. Des efforts ont également été déployés pour améliorer la documentation et la packagification du projet.

### Évolutions fonctionnelles
- Ajout de l'intégration Sentry pour la surveillance des erreurs et l'alerte en cas de problèmes. [#445](https://github.com/MTES-MCT/lucca-cms/issues/445)
- Correction de la configuration Docker. [#519](https://github.com/MTES-MCT/lucca-cms/issues/519)
- Correction des erreurs de validation du fichier `publiccode.yml`. [#496](https://github.com/MTES-MCT/lucca-cms/issues/496)

### Évolutions techniques
- Packagification du projet, incluant la récupération de la documentation perdue lors d'un merge précédent. [#506](https://github.com/MTES-MCT/lucca-cms/issues/506) et [#514](https://github.com/MTES-MCT/lucca-cms/issues/514)
- Refactorisation des sources namespacées, les déplaçant vers `sites_conformes/`.
- Application automatique des corrections pré-commit.
- Mise à jour de la documentation. [#511](https://github.com/MTES-MCT/lucca-cms/issues/511)
- Ajout d'un fichier `cron.json`.

### Autres changements
- Ajout de `demo` au `slugignore`.
- Revert d'une migration et ajout d'une nouvelle migration.
- Corrections mineures et améliorations diverses du code.
