## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de la maintenabilité des pipelines de données, notamment en refactorisant le code et en gérant plus efficacement les erreurs. Des corrections ont également été apportées pour assurer l'exactitude des données traitées, en particulier pour les données météo et IRVE. Enfin, une maintenance a été effectuée sur certains DAGs, dont la désactivation d'un DAG obsolète.

### Évolutions fonctionnelles
- Correction du chemin vers le fichier geojson dans le pipeline IRVE. [#649](https://github.com/datagouv/datagouvfr_data_pipelines/pull/649)
- Exclusion du JDD consolidé du PAN dans le pipeline IRVE. [#645](https://github.com/datagouv/datagouvfr_data_pipelines/issues/645)
- Ajout de nouvelles colonnes dans les tables météo.
- Correction des types de données (dtypes) dans les fichiers Parquet. [#647](https://github.com/datagouv/datagouvfr_data_pipelines/issues/647)

### Évolutions techniques
- Refactorisation du pipeline météo PostgreSQL pour une vérification plus rapide de l'insertion des données. [#650](https://github.com/datagouv/datagouvfr_data_pipelines/issues/650)
- Déplacement de toute la logique liée aux schémas dans un dossier dédié "schema". [#649](https://github.com/datagouv/datagouvfr_data_pipelines/pull/649)
- Mise en place des connexions à la base de données de manière dynamique. [#647](https://github.com/datagouv/datagouvfr_data_pipelines/issues/647)
- Gestion des erreurs améliorée lors des requêtes PUT vers datagouv, avec réduction de l'indentation du code.
- Suppression d'un DAG obsolète pour le géocodage SIRENE.
- Prévention des exécutions concurrentes de certains DAGs.
- Amélioration de l'efficacité de la vérification de l'existence des fichiers PostgreSQL.

### Autres changements
- Linting du code pour améliorer la qualité et la cohérence.
- Ajout d'une notification sur le canal Simplifions.
- Suppression de l'utilisation de Markdown dans certains messages temporaires.
- Ping sur Tchap pour information.
- Désactivation des notifications pour les tops.
