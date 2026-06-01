## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'optimisation de la consommation de mémoire des pipelines, la migration de nouveaux traitements vers Airflow (DVF geoloc, qualité de l'eau), et l'amélioration de la robustesse et de la surveillance des pipelines existants. Plusieurs corrections ont été apportées pour améliorer la stabilité et la gestion des erreurs, notamment concernant les notifications Tchap et l'API Airflow.

### Évolutions fonctionnelles
- Migration du traitement des géolocalisations DVF vers Airflow, permettant une meilleure gestion et automatisation. [#653](https://github.com/datagouv/datagouvfr_data_pipelines/issues/653)
- Publication des données de qualité de l'eau dans un nouveau dataset, suite à un remaniement du pipeline associé. [#665](https://github.com/datagouv/datagouvfr_data_pipelines/issues/665)
- Amélioration de la gestion des messages trop longs pour Tchap, évitant ainsi des erreurs de notification. [#663](https://github.com/datagouv/datagouvfr_data_pipelines/issues/663)
- Ajout de la pagination et de filtres d'état à l'API Airflow pour une meilleure gestion des tâches. [#662](https://github.com/datagouv/datagouvfr_data_pipelines/issues/662)
- Correction de l'affichage du layout des notifications HVD. [#664](https://github.com/datagouv/datagouvfr_data_pipelines/issues/664)

### Évolutions techniques
- Optimisations significatives de la consommation de mémoire des pipelines, notamment en gérant plus efficacement les objets en mémoire et en optimisant le traitement des données (groupement/dégroupement OM parcelles, concaténation).
- Refactorisation du code pour utiliser la nouvelle syntaxe Airflow et éviter les avertissements de dépréciation. [#661](https://github.com/datagouv/datagouvfr_data_pipelines/issues/661)
- Utilisation de variables d'environnement pour la configuration des notebooks, permettant une exécution plus flexible et sécurisée.
- Amélioration de la gestion des endpoints S3 pour pandas et logging.
- Passage des PNT (Points de Nuisance Thématiques) sur l'infrastructure OVH. [#655](https://github.com/datagouv/datagouvfr_data_pipelines/issues/655)
- Suppression de l'utilisation de `literal_eval` pour des raisons de sécurité. [#660](https://github.com/datagouv/datagouvfr_data_pipelines/issues/660)

### Autres changements
- Correction de références datagouv.
- Mise à jour de la watchlist.
- Correction de typos.
- Ajout d'informations sur la mise hors service (decommission) dans la documentation.
- Configuration des cibles de monitoring PNT pour OVH.
- Correction de la configuration par défaut de la salle Tchap. [#657](https://github.com/datagouv/datagouvfr_data_pipelines/issues/657)
- Correction de bugs mineurs et améliorations de la gestion des logs.
- Mise à jour du fichier `config.py`.
