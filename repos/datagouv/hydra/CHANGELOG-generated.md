## Changelog : hydra (30 derniers jours, au 22 juin 2026)

### Résumé
Les dernières mises à jour de Hydra se concentrent sur l'amélioration de la robustesse du système, notamment au niveau de la gestion des fichiers et des exports de données. Des corrections ont été apportées pour éviter des erreurs lors de la suppression de fichiers et de l'envoi de tâches en file d'attente. L'intégration de S3 pour le stockage d'objets a été améliorée, et des optimisations de performance ont été réalisées, notamment avec l'utilisation de Python 3.14.

### Évolutions fonctionnelles
- Ajout de l'export Parquet et GeoJSON via des files d'attente RQ dédiées, améliorant la gestion des conversions de données ([#425](https://github.com/datagouv/hydra/pull/425)).
- Intégration du stockage d'objets S3 via `boto3`, permettant de stocker les données sur Amazon S3 ([#415](https://github.com/datagouv/hydra/pull/415)).
- Ajout d'un champ `header` lors de l'analyse des fichiers Parquet, fournissant des informations supplémentaires sur les données ([#431](https://github.com/datagouv/hydra/pull/431)).
- L'endpoint de santé inclut maintenant la version de Python utilisée, facilitant le diagnostic des problèmes ([#433](https://github.com/datagouv/hydra/pull/433)).

### Évolutions techniques
- Mise à jour vers Python 3.14 pour des performances améliorées ([#378](https://github.com/datagouv/hydra/pull/378)).
- Refactorisation de l'interface en ligne de commande (CLI) pour une meilleure organisation et maintenabilité ([#437](https://github.com/datagouv/hydra/pull/437)).
- Amélioration de la gestion des uploads vers S3, corrigeant des problèmes de stockage ([#428](https://github.com/datagouv/hydra/pull/428)).
- Configuration d'un bucket S3 par environnement et utilisation de préfixes basés sur l'extension des fichiers pour une meilleure organisation du stockage ([#429](https://github.com/datagouv/hydra/pull/429)).
- Correction d'une erreur empêchant la suppression de fichiers dans certaines tables.
- Correction d'une erreur lors de l'envoi de tâches en file d'attente, assurant la transmission correcte des données.
- Utilisation correcte des arguments de mot-clé dans l'export Geojson et PMTiles.
- Amélioration de la couverture des tests unitaires.

### Autres changements
- Mise à jour de la documentation README pour refléter les changements récents de l'API, de la CLI et du comportement du worker ([#439](https://github.com/datagouv/hydra/pull/439)).
- Correction d'une vulnérabilité de sécurité en contraignant la version de `urllib3` ([#420](https://github.com/datagouv/hydra/pull/420)).
- Suppression des cibles `storage_path` obsolètes.
- Suppression des couches OGC du payload.
- Suppression d'une protection obsolète dans la conversion CSV vers GeoJSON.
- Correction d'une erreur de documentation dans la docstring de `enqueue`.
- Silence des logs de `botocore` lors de l'utilisation de l'option `--quiet` dans la CLI.
