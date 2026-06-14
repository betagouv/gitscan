## Changelog : hydra (30 derniers jours, au 12 juin 2026)

### Résumé
Les dernières mises à jour d'Hydra se concentrent sur l'amélioration de la robustesse, des performances et de la flexibilité du système. Des améliorations ont été apportées à l'exportation de données (Parquet et GeoJSON), au support du stockage S3, et à la gestion des logs. Une migration vers Python 3.14 a également été effectuée pour bénéficier des dernières optimisations du langage.

### Évolutions fonctionnelles
- Ajout de l'exportation de fichiers Parquet et GeoJSON via des files d'attente RQ dédiées, améliorant ainsi la gestion des tâches de conversion et l'évolutivité. [#425](https://github.com/datagouv/hydra/pull/425)
- Possibilité d'exporter des fichiers Parquet directement depuis la base de données, sans relire les fichiers CSV sources. [#424](https://github.com/datagouv/hydra/pull/424)
- Intégration du stockage d'objets S3 via `boto3`, permettant de stocker les données sur Amazon S3. [#415](https://github.com/datagouv/hydra/pull/415)
- Ajout du champ `header` à l'analyse des fichiers Parquet. [#431](https://github.com/datagouv/hydra/pull/431)
- L'endpoint de santé inclut maintenant la version de Python utilisée. [#433](https://github.com/datagouv/hydra/pull/433)

### Évolutions techniques
- Migration vers Python 3.14 pour des performances améliorées. [#378](https://github.com/datagouv/hydra/pull/378)
- Refactorisation de la CLI pour une meilleure organisation et maintenabilité. [#437](https://github.com/datagouv/hydra/pull/437)
- Amélioration de la gestion des uploads vers S3, corrigeant des problèmes potentiels. [#428](https://github.com/datagouv/hydra/pull/428)
- Refactorisation des tests pour améliorer la couverture et l'organisation. [#434](https://github.com/datagouv/hydra/pull/435)
- Séparation des méthodes de conversion dans des fichiers dédiés dans le répertoire `/conversion`. [#422](https://github.com/datagouv/hydra/pull/422)
- Contrainte de la version de `urllib3` pour corriger une vulnérabilité de sécurité (GHSA-mf9v-mfxr-j63j). [#420](https://github.com/datagouv/hydra/pull/420)

### Autres changements
- Suppression des couches OGC dans le payload. [#440](https://github.com/datagouv/hydra/pull/440)
- Mise à jour de la documentation README pour refléter les changements récents de l'API, de la CLI et du comportement du worker. [#439](https://github.com/datagouv/hydra/pull/439)
- Suppression d'une garde obsolète dans le helper CSV_TO_GEOJSON.
- Correction d'une erreur mineure dans la docstring de la fonction `enqueue`.
- Amélioration de la verbosité de la CLI avec l'option `--quiet` qui applique le silence à tous les loggers. [#432](https://github.com/datagouv/hydra/pull/432)
