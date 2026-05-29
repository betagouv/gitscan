## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse des pipelines existants, notamment en gérant mieux les erreurs et les limites de taille des messages. Plusieurs pipelines ont été migrés ou adaptés pour fonctionner avec Airflow 3, et des améliorations ont été apportées à la configuration et à l'exécution des notebooks. Enfin, des travaux ont été réalisés pour faciliter le déploiement et la surveillance des pipelines sur l'infrastructure OVH.

### Évolutions fonctionnelles
- Migration du pipeline de géolocalisation des données DVF vers Airflow. [#653](https://github.com/datagouv/datagouvfr_data_pipelines/issues/653)
- Amélioration de la présentation des notifications HVD. [#664](https://github.com/datagouv/datagouvfr_data_pipelines/issues/664)
- Ajout de la pagination et d'un filtre d'état à l'API Airflow. [#662](https://github.com/datagouv/datagouvfr_data_pipelines/issues/662)
- Gestion des messages trop longs pour Tchap, évitant ainsi des erreurs d'envoi. [#663](https://github.com/datagouv/datagouvfr_data_pipelines/issues/663)

### Évolutions techniques
- Utilisation de l'Airflow SDK pour supprimer les avertissements de dépréciation et améliorer la qualité du code. [#661](https://github.com/datagouv/datagouvfr_data_pipelines/issues/661)
- Refactoring pour permettre l'utilisation de variables d'environnement dans la configuration, facilitant l'exécution des notebooks.
- Modification de la manière dont les fonctions sont passées en paramètres aux notebooks pour éviter d'importer Airflow dans ces derniers.
- Correction de plusieurs problèmes liés à l'importation de modules et à la configuration des tâches Airflow.
- Adaptation des DAGs de maintenance et de métadonnées pour la compatibilité avec Airflow 3. [#658](https://github.com/datagouv/datagouvfr_data_pipelines/issues/658)
- Déploiement des pipelines PNT (Points de Numérotation de Territoire) sur l'infrastructure OVH. [#655](https://github.com/datagouv/datagouvfr_data_pipelines/issues/655)
- Correction de la configuration de la salle Tchap par défaut. [#657](https://github.com/datagouv/datagouvfr_data_pipelines/issues/657)

### Autres changements
- Correction de typos et nettoyage du code.
- Mise à jour de la documentation concernant la mise hors service des anciens systèmes.
- Ajout des endpoints S3 dans la configuration.
- Suppression d'une liste d'IDs inutilisée.
- Mise à jour du fichier `config.py`.
