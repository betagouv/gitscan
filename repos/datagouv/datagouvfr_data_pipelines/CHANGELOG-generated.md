## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les pipelines de données ont bénéficié d'optimisations significatives en termes de gestion de la mémoire, notamment pour les traitements de données géographiques (parcelles OM, DVF). Plusieurs corrections ont été apportées pour améliorer la robustesse des pipelines, notamment concernant la gestion des fichiers, des connexions FTP/SFTP et des dates. De nouvelles données PNT ont été intégrées et un pipeline pour la géolocalisation des données DVF a été migré vers Airflow.

### Évolutions fonctionnelles
- Ajout de nouveaux packs de données PNT. [#669](https://github.com/datagouv/datagouvfr_data_pipelines/issues/669)
- Migration du pipeline de géolocalisation des données DVF vers Airflow. [#653](https://github.com/datagouv/datagouvfr_data_pipelines/issues/653)
- Publication des données de qualité de l'eau remaniées dans un nouveau jeu de données. [#665](https://github.com/datagouv/datagouvfr_data_pipelines/issues/665)
- Amélioration de la gestion des messages longs pour l'envoi via Tchap. [#663](https://github.com/datagouv/datagouvfr_data_pipelines/issues/663)
- Ajout de la pagination et d'un filtre d'état à l'API Airflow. [#662](https://github.com/datagouv/datagouvfr_data_pipelines/issues/662)

### Évolutions techniques
- Optimisations de la consommation de mémoire pour les pipelines traitant les données OM (parcelles) et DVF, notamment en optimisant le tri et la concaténation des données.
- Utilisation de la nouvelle syntaxe Airflow et suppression des avertissements de dépréciation grâce à l'Airflow SDK. [#661](https://github.com/datagouv/datagouvfr_data_pipelines/issues/661)
- Amélioration de la gestion des connexions FTP, notamment en récupérant la connexion au moment de l'exécution.
- Suppression régulière des digests anciens pour optimiser le stockage. [#672](https://github.com/datagouv/datagouvfr_data_pipelines/issues/672)
- Ajout d'un mécanisme d'arrêt anticipé pour accélérer les mises à jour de datagouv.
- Correction de la gestion des time slots pour OM.
- Ajout d'un label de dépréciation pour les DAGs. [#666](https://github.com/datagouv/datagouvfr_data_pipelines/issues/666)

### Autres changements
- Suppression de notifications spam inutiles. [#667](https://github.com/datagouv/datagouvfr_data_pipelines/issues/667)
- Amélioration de la mise en page des notifications HVD. [#664](https://github.com/datagouv/datagouvfr_data_pipelines/issues/664)
- Corrections mineures de logging et de documentation.
- Suppression de fichiers et variables inutilisés.
- Correction de références datagouv.
- Augmentation du timeout pour le DAG météo FTP.
