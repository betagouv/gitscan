## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 18 juin 2026)

### Résumé
Ce changelog résume les améliorations et corrections apportées aux pipelines de données de data.gouv.fr au cours des 30 derniers jours. Les efforts se sont concentrés sur l'optimisation de la consommation de mémoire, l'ajout de nouveaux jeux de données (PNT, DVF, qualité de l'eau), la correction de bugs liés à la gestion des fichiers et des connexions, ainsi que l'amélioration du monitoring et des notifications.

### Évolutions fonctionnelles
- Ajout de nouveaux packs de données PNT. [#669](https://github.com/datagouv/datagouvfr_data_pipelines/issues/669)
- Migration du pipeline de géolocalisation des données DVF vers Airflow. [#653](https://github.com/datagouv/datagouvfr_data_pipelines/issues/653)
- Publication des données de qualité de l'eau dans un nouveau jeu de données. [#665](https://github.com/datagouv/datagouvfr_data_pipelines/issues/665)
- Amélioration de la gestion des messages longs pour les notifications Tchap. [#663](https://github.com/datagouv/datagouvfr_data_pipelines/issues/663)
- Ajout de la pagination et d'un filtre d'état à l'API Airflow. [#662](https://github.com/datagouv/datagouvfr_data_pipelines/issues/662)

### Évolutions techniques
- Optimisations significatives de la consommation de mémoire pour plusieurs pipelines, notamment pour les données OM (parcelles) et les fichiers compressés (gunzip en parallèle).
- Refactorisation du code pour une meilleure gestion des connexions SFTP.
- Utilisation de la nouvelle syntaxe Airflow et suppression des avertissements de dépréciation grâce à l'Airflow SDK. [#661](https://github.com/datagouv/datagouvfr_data_pipelines/issues/661)
- Amélioration de la gestion des erreurs et des timeouts, notamment pour le DAG météo FTP.
- Correction de bugs liés à la récupération des timeslots pour les données OM.
- Ajout d'un préfixe plus long pour les parcelles afin de réduire la taille des lots.
- Conversion de la date de mutation en chaîne de caractères après le tri pour optimiser les performances.
- Suppression de code inutilisé et nettoyage général du code.

### Autres changements
- Ajout d'un label de dépréciation pour certains DAGs. [#666](https://github.com/datagouv/datagouvfr_data_pipelines/issues/666)
- Correction de la disposition des notifications HVD. [#664](https://github.com/datagouv/datagouvfr_data_pipelines/issues/664)
- Mise à jour de la watchlist. [#660](https://github.com/datagouv/datagouvfr_data_pipelines/issues/660)
- Corrections de typos et améliorations de la documentation.
- Suppression de notifications spam. [#667](https://github.com/datagouv/datagouvfr_data_pipelines/issues/667)
