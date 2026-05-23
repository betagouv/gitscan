## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 2026-05-21)

### Résumé
Ce changelog couvre les dernières améliorations apportées aux pipelines de données de data.gouv.fr. Les efforts se sont concentrés sur l'amélioration de la robustesse des pipelines, notamment en gérant mieux les données sources changeantes et les erreurs potentielles. Des optimisations ont également été apportées pour permettre l'exécution de notebooks directement dans Airflow, et l'intégration avec l'infrastructure OVH a été améliorée.

### Évolutions fonctionnelles
- Amélioration de la gestion des notifications pour une meilleure réactivité en cas de problème.
- Correction de la configuration de la salle Tchap par défaut [#657](https://github.com/datagouv/datagouvfr_data_pipelines/issues/657).
- Les cibles de monitoring PNT sont désormais publiques [#655](https://github.com/datagouv/datagouvfr_data_pipelines/issues/655).
- Correction de la gestion des valeurs de type NA dans les données RNIC pour éviter les erreurs d'importation.
- Adaptation aux modifications des sources de données, notamment pour le traitement des données RNIC [#660](https://github.com/datagouv/datagouvfr_data_pipelines/issues/660).

### Évolutions techniques
- Refactorisation pour permettre l'utilisation de variables d'environnement dans la configuration, facilitant l'exécution de notebooks dans Airflow.
- Amélioration de la transmission de fonctions comme paramètres de notebooks pour éviter les problèmes d'importation d'Airflow.
- Optimisations pour l'intégration avec l'infrastructure OVH, incluant la configuration de monitoring et la gestion des environnements.
- Correction de la logique de déclenchement des tâches pour une meilleure fiabilité.
- Correction de la gestion des doublons dans la colonne de clé primaire des données RNIC.
- Réorganisation des colonnes des données RNIC avant l'importation en base de données.
- Correction de bugs liés à la gestion des identifiants inutilisés.

### Autres changements
- Correction de typos et améliorations de la lisibilité du code.
- Mise à jour de la documentation pour clarifier le processus de déclassement.
- Ajout d'endpoints S3 pour une meilleure configuration.
- Correction de la configuration des DAGs pour la compatibilité avec Airflow 3 [#658](https://github.com/datagouv/datagouvfr_data_pipelines/issues/658).
- Correction de la watchlist [#660](https://github.com/datagouv/datagouvfr_data_pipelines/issues/660).
- Mise à jour du fichier `config.py` [#659](https://github.com/datagouv/datagouvfr_data_pipelines/issues/659).
