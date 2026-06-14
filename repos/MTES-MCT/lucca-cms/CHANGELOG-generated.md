## Changelog : lucca-cms (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la qualité du code, la correction de problèmes de validation et l'intégration d'outils de surveillance (Sentry) pour une meilleure gestion des erreurs. Des travaux de documentation et de packagification ont également été réalisés.

### Évolutions fonctionnelles
- Ajout de l'outil Sentry pour la surveillance des erreurs et des performances [#445](https://github.com/MTES-MCT/lucca-cms/issues/445).
- Correction de la configuration Docker [#519](https://github.com/MTES-MCT/lucca-cms/issues/519).
- Correction des erreurs de validation du fichier `publiccode.yml` [#496](https://github.com/MTES-MCT/lucca-cms/issues/496).

### Évolutions techniques
- Packagification du projet : récupération de la documentation perdue lors du merge et finalisation du processus [#506](https://github.com/MTES-MCT/lucca-cms/issues/506), [#514](https://github.com/MTES-MCT/lucca-cms/issues/514).
- Refactorisation du code pour la gestion des sources namespacées, en les déplaçant dans le répertoire `sites_conformes/` pour la version 3.2.0.
- Application des corrections automatiques du pre-commit pour la version 3.2.0.
- Mise à jour de la documentation [#511](https://github.com/MTES-MCT/lucca-cms/issues/511).

### Autres changements
- Création du fichier `cron.json`.
- Ajout de `demo` au `slugignore`.
- Revert d'un commit "add migration" suivi d'un nouveau commit "add migration".
