## Changelog : hydra (30 derniers jours, au 10 juin 2026)

### Résumé
Les dernières mises à jour d'Hydra se concentrent sur l'amélioration des performances, l'ajout de nouvelles fonctionnalités d'exportation de données (Parquet et GeoJSON), et l'intégration du stockage S3.  Des corrections de bugs et des refactorings ont également été effectués pour améliorer la stabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de l'exportation GeoJSON à partir de la base de données dans le pipeline CSV. [#423](https://github.com/datagouv/hydra/pull/423)
- Possibilité d'exporter au format Parquet directement à partir de la base de données. [#424](https://github.com/datagouv/hydra/pull/424)
- Ajout d'un champ `header` aux analyses Parquet. [#431](https://github.com/datagouv/hydra/pull/431)
- Intégration du stockage d'objets S3 via boto3, permettant de stocker les données sur Amazon S3. [#415](https://github.com/datagouv/hydra/pull/415)
- L'endpoint de santé inclut désormais la version de Python utilisée. [#433](https://github.com/datagouv/hydra/pull/433)

### Évolutions techniques
- Mise à jour vers Python 3.14 pour améliorer les performances. [#378](https://github.com/datagouv/hydra/pull/378)
- Refactorisation du code de conversion, séparant les méthodes dans des fichiers dédiés dans le répertoire `/conversion`. [#422](https://github.com/datagouv/hydra/pull/422)
- Les exports Parquet et GeoJSON sont désormais gérés par des queues RQ dédiées, améliorant la scalabilité et la réactivité. [#425](https://github.com/datagouv/hydra/pull/425)
- Correction d'un problème d'upload sur S3. [#428](https://github.com/datagouv/hydra/pull/428)
- Amélioration de la gestion des buckets S3 avec un bucket par environnement et des préfixes basés sur l'extension des fichiers. [#429](https://github.com/datagouv/hydra/pull/429)
- Refactorisation des tests pour une meilleure organisation. [#435](https://github.com/datagouv/hydra/pull/435)

### Autres changements
- Correction d'une erreur mineure dans la docstring de la fonction `enqueue`. [#782ecaa](https://github.com/datagouv/hydra/commit/782ecaa)
- Application de l'option `--quiet` à tous les loggers en ligne de commande. [#432](https://github.com/datagouv/hydra/pull/432)
- Contrainte de la version de `urllib3` pour corriger une vulnérabilité de sécurité (GHSA-mf9v-mfxr-j63j). [#420](https://github.com/datagouv/hydra/pull/420)
- Mise à jour de la documentation README pour refléter les changements récents de l'API, de la CLI et du comportement du worker. [#439](https://github.com/datagouv/hydra/pull/439)
