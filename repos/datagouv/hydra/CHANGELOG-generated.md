## Changelog : hydra (30 derniers jours, au 04 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Hydra se concentrent sur l'amélioration des performances, l'ajout de nouvelles fonctionnalités d'export de données (Parquet et GeoJSON) et l'intégration du stockage S3. Des corrections et des refactorings ont également été effectués pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de l'export GeoJSON à partir de la base de données uniquement dans le pipeline CSV. [#423](https://github.com/datagouv/hydra/pull/423)
- Possibilité d'exporter des fichiers Parquet directement à partir de la base de données. [#424](https://github.com/datagouv/hydra/pull/424)
- Ajout d'un champ `header` aux analyses Parquet. [#431](https://github.com/datagouv/hydra/pull/431)
- Intégration du stockage d'objets S3 via boto3, permettant de stocker les données sur Amazon S3. [#415](https://github.com/datagouv/hydra/pull/415)
- L'endpoint de santé inclut maintenant la version de Python utilisée. [#433](https://github.com/datagouv/hydra/pull/433)

### Évolutions techniques
- Passage à Python 3.14 pour améliorer les performances. [#378](https://github.com/datagouv/hydra/pull/378)
- Refactorisation du code de conversion, séparant les méthodes dans des fichiers dédiés dans le répertoire `/conversion`. [#422](https://github.com/datagouv/hydra/pull/422)
- Les exports Parquet et GeoJSON sont maintenant gérés par des queues RQ dédiées, améliorant la gestion des tâches asynchrones. [#425](https://github.com/datagouv/hydra/pull/425)
- Correction de problèmes d'upload sur S3. [#428](https://github.com/datagouv/hydra/pull/428)
- Amélioration de la configuration des buckets S3 avec un bucket par environnement et des préfixes basés sur l'extension des fichiers. [#429](https://github.com/datagouv/hydra/pull/429)
- Refactorisation des tests pour aligner la structure avec le package de conversion. [#427](https://github.com/datagouv/hydra/pull/427)

### Autres changements
- Correction d'une erreur mineure dans la docstring de la fonction `enqueue`. [#782ecaa](https://github.com/datagouv/hydra/commit/782ecaa)
- Application de l'option `--quiet` à tous les loggers en ligne de commande. [#432](https://github.com/datagouv/hydra/pull/432)
- Suppression d'un `__all__` redondant dans l'analyse CSV. [#426](https://github.com/datagouv/hydra/pull/426)
- Suppression d'une protection obsolète dans l'helper de conversion CSV vers GeoJSON. [#7591db4](https://github.com/datagouv/hydra/commit/7591db4)
- Correction de la publication dans CI lors des releases. [#398](https://github.com/datagouv/hydra/pull/398)
- Mise à jour de la dépendance `urllib3` pour corriger une vulnérabilité de sécurité. [#420](https://github.com/datagouv/hydra/pull/420)
