## Changelog : sites-conformes (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Sites Conformes se concentrent sur l'amélioration de la robustesse du projet, avec l'ajout de Sentry pour la surveillance des erreurs, des corrections de bugs sur le frontend, et des améliorations de la configuration et du packaging. Une nouvelle fonctionnalité permet également le stockage des médias directement en base de données PostgreSQL, offrant une alternative à l'utilisation de S3.

### Évolutions fonctionnelles
- Ajout de la possibilité de stocker les médias en PostgreSQL, offrant une alternative à S3. [#482](https://github.com/numerique-gouv/sites-conformes/issues/482)
- Corrections de bugs sur l'interface utilisateur (frontend). [#486](https://github.com/numerique-gouv/sites-conformes/issues/486)
- Intégration de Sentry pour la surveillance et la gestion des erreurs. [#445](https://github.com/numerique-gouv/sites-conformes/issues/445)

### Évolutions techniques
- Amélioration de la configuration Docker. [#519](https://github.com/numerique-gouv/sites-conformes/issues/519)
- Refonte du packaging du projet, incluant la récupération de la documentation. [#506](https://github.com/numerique-gouv/sites-conformes/issues/506) et [#514](https://github.com/numerique-gouv/sites-conformes/issues/514)
- Mise à jour des dépendances Python. [#501](https://github.com/numerique-gouv/sites-conformes/issues/501)
- Migration des sources namespacées vers `sites_conformes/`.
- Application automatique de corrections via pre-commit.
- Correction des erreurs de validation du fichier `publiccode.yml`. [#496](https://github.com/numerique-gouv/sites-conformes/issues/496)

### Autres changements
- Mise à jour de la documentation. [#511](https://github.com/numerique-gouv/sites-conformes/issues/511)
- Ajout de `demo` à `slugignore`.
- Revert d'une migration et ajout d'une nouvelle migration.
