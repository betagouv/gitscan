## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de l'efficacité des pipelines de données, notamment en optimisant l'utilisation de la mémoire et en migrant vers de nouvelles infrastructures (OVH Minio). Des corrections ont également été apportées pour améliorer la gestion des fichiers, des connexions et des erreurs, ainsi que pour supporter de nouveaux jeux de données.

### Évolutions fonctionnelles
- Ajout de la prise en charge de nouveaux packs PNT [#669](https://github.com/datagouv/datagouvfr_data_pipelines/issues/669).
- Publication du rework de la qualité de l'eau dans un nouveau jeu de données [#665](https://github.com/datagouv/datagouvfr_data_pipelines/issues/665).
- Migration de la géolocalisation DVF vers Airflow [#653](https://github.com/datagouv/datagouvfr_data_pipelines/issues/653).
- Prise en charge des messages longs pour Tchap [#663](https://github.com/datagouv/datagouvfr_data_pipelines/issues/663).
- Ajout d'un label de dépréciation pour les DAGs [#666](https://github.com/datagouv/datagouvfr_data_pipelines/issues/666).
- Correction des timeslots pour OM.
- Correction de références datagouv.

### Évolutions techniques
- Migration vers l'utilisation des buckets OVH au lieu de Minio [#675](https://github.com/datagouv/datagouvfr_data_pipelines/issues/675) et [#670](https://github.com/datagouv/datagouvfr_data_pipelines/issues/670).
- Utilisation de l'Airflow SDK pour les imports [#674](https://github.com/datagouv/datagouvfr_data_pipelines/issues/674) et pour supprimer les avertissements de dépréciation et le lint [#661](https://github.com/datagouv/datagouvfr_data_pipelines/issues/661).
- Optimisation de l'utilisation de la mémoire (RAM) pour les pipelines de traitement des parcelles (OM) et des fichiers compressés (csvgz).
- Suppression des digests anciens de manière périodique [#672](https://github.com/datagouv/datagouvfr_data_pipelines/issues/672).
- Amélioration de la gestion des connexions FTP et S3.
- Augmentation du timeout pour certains DAGs (météo).
- Correction de la gestion des types de contenu (content-type) lors du chargement sur S3.
- Amélioration de la gestion des erreurs et des timeouts lors de la récupération des headers.

### Autres changements
- Correction de la gestion des chemins et des préfixes sur S3.
- Suppression de notifications potentiellement spammantes et de tickets Zammad inutiles [#667](https://github.com/datagouv/datagouvfr_data_pipelines/issues/667).
- Amélioration de la documentation et du code (linting, suppression de variables inutilisées).
- Correction de bugs mineurs et améliorations de la robustesse générale du code.
- Ajout de tests et de vérifications pour améliorer la qualité du code.
- Correction de la mise en page de la notification HVD [#664](https://github.com/datagouv/datagouvfr_data_pipelines/issues/664).
- Ajout de la possibilité de spécifier le port dans les connexions Airflow [#676](https://github.com/datagouv/datagouvfr_data_pipelines/issues/676).
