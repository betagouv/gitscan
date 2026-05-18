## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse et de la flexibilité des pipelines de données, notamment en ce qui concerne le traitement des données RNIC et des pétitions. Des améliorations ont également été apportées à la configuration et à l'exécution des notebooks Airflow, ainsi qu'à la gestion des notifications.

### Évolutions fonctionnelles
- Correction d'un bug concernant la récupération de l'ID maximum pour les pétitions [#654](https://github.com/datagouv/datagouvfr_data_pipelines/issues/654).
- Amélioration de la gestion des valeurs manquantes (NA-like) dans les données RNIC.
- Correction de la gestion des doublons dans la colonne de clé primaire des données RNIC.
- Correction de l'ordre des colonnes dans les données RNIC avant l'importation en base de données.
- Correction d'un bug concernant la visibilité des cibles de monitoring PNT.
- Correction d'un bug concernant la salle Tchap par défaut [#657](https://github.com/datagouv/datagouvfr_data_pipelines/issues/657).

### Évolutions techniques
- Refactorisation pour permettre l'utilisation de variables d'environnement dans la configuration, facilitant l'exécution des notebooks.
- Modification pour passer des fonctions comme paramètres aux notebooks, évitant ainsi l'importation d'Airflow dans les notebooks.
- Amélioration de la gestion des erreurs et des règles de déclenchement des tâches.
- Déploiement des pipelines PNT sur OVH (#655 et #656).
- Amélioration de la gestion des endpoints S3.

### Autres changements
- Ajout d'informations sur la mise hors service (decommission) dans la documentation.
- Nettoyage du code et des notifications.
- Mise à jour de la configuration (`config.py`).
- Correction de typos et suppression de code inutilisé.
- Amélioration des notifications pour une meilleure clarté.
- Suppression d'une vérification de cohérence non nécessaire.
- Adaptation du code aux changements de sources de données.
