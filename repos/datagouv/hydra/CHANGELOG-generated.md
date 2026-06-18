## Changelog : hydra (30 derniers jours, au 2026-06-17)

### Résumé
Les dernières mises à jour d'Hydra améliorent la gestion des fichiers, l'exportation des données (notamment vers Parquet et GeoJSON), et l'intégration avec le stockage S3. Des corrections de bugs et des améliorations de la robustesse ont également été apportées, ainsi que des optimisations de performance et de la documentation.

### Évolutions fonctionnelles
- Ajout de l'exportation Parquet et GeoJSON vers des queues RQ dédiées, améliorant ainsi la performance et la scalabilité de ces opérations. ([#425](https://github.com/datagouv/hydra/pull/425))
- Implémentation du stockage S3 via boto3, permettant d'utiliser des buckets S3 pour le stockage des données. ([#415](https://github.com/datagouv/hydra/pull/415))
- Possibilité d'exporter au format Parquet directement depuis la base de données. ([#424](https://github.com/datagouv/hydra/pull/424))
- Amélioration de la gestion des fichiers et correction de bugs liés à la suppression de fichiers.
- Ajout du champ `header` lors de l'analyse Parquet. ([#431](https://github.com/datagouv/hydra/pull/431))

### Évolutions techniques
- Mise à jour de la version de Python utilisée pour améliorer les performances (Python 3.14). ([#378](https://github.com/datagouv/hydra/pull/378))
- Refactorisation de l'interface de ligne de commande (CLI) pour une meilleure organisation et maintenabilité. ([#437](https://github.com/datagouv/hydra/pull/437))
- Amélioration de la gestion des logs avec l'option `--quiet` pour réduire la verbosité. ([#436](https://github.com/datagouv/hydra/pull/436), [#432](https://github.com/datagouv/hydra/pull/432))
- Ajout de tests unitaires pour améliorer la couverture et la qualité du code. ([#434](https://github.com/datagouv/hydra/pull/434), [#449](https://github.com/datagouv/hydra/pull/449))
- Correction d'une vulnérabilité de sécurité en contraignant la version de la librairie urllib3. ([#420](https://github.com/datagouv/hydra/pull/420))
- Utilisation d'un bucket S3 par environnement et de préfixes basés sur l'extension des fichiers pour une meilleure organisation du stockage. ([#429](https://github.com/datagouv/hydra/pull/429))

### Autres changements
- Mise à jour de la documentation README pour refléter les changements récents de l'API, de la CLI et du comportement du worker. ([#439](https://github.com/datagouv/hydra/pull/439))
- Correction d'une erreur mineure dans la docstring de la fonction `enqueue`.
- Suppression de cibles `remainders` inutiles. ([#450](https://github.com/datagouv/hydra/pull/450))
- Correction d'un problème lié à l'analyse des sous-classes OGC. ([#444](https://github.com/datagouv/hydra/pull/444))
- Correction d'un problème lié au passage de dictionnaires à la file d'attente (queue). ([#446](https://github.com/datagouv/hydra/pull/446))
