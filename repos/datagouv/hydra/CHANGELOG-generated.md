## Changelog : hydra (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des exportations de données, notamment en permettant la génération de formats comme Parquet et GeoJSON directement à partir de la base de données, réduisant ainsi la nécessité de relire les fichiers CSV sources. L'intégration de S3 pour le stockage d'objets a également été améliorée.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter au format Parquet et GeoJSON à partir de la base de données, via des files d'attente RQ dédiées. [#425](https://github.com/datagouv/hydra/pull/425)
- Génération de GeoJSON directement à partir de PostgreSQL au lieu de relire les CSV, améliorant ainsi les performances. [#404](https://github.com/datagouv/hydra/pull/404)
- Possibilité d'exporter au format Parquet uniquement à partir de la base de données. [#424](https://github.com/datagouv/hydra/pull/424)
- Intégration du stockage d'objets S3 via `boto3`, avec gestion des buckets par environnement et préfixes basés sur l'extension des fichiers. [#415](https://github.com/datagouv/hydra/pull/415), [#428](https://github.com/datagouv/hydra/pull/428), [#429](https://github.com/datagouv/hydra/pull/429)

### Évolutions techniques
- Refactorisation du code de conversion des données, avec séparation des méthodes dans des fichiers dédiés dans le dossier `/conversion`. [#422](https://github.com/datagouv/hydra/pull/422)
- Amélioration de la gestion des erreurs et suppression de code obsolète dans le pipeline CSV. [#423](https://github.com/datagouv/hydra/pull/423), [#426](https://github.com/datagouv/hydra/pull/426), [#427](https://github.com/datagouv/hydra/pull/427)

### Autres changements
- Correction d'une erreur mineure dans la documentation concernant l'enfilement des tâches.
- Suppression d'une protection inutile dans le helper de conversion CSV vers GeoJSON.
