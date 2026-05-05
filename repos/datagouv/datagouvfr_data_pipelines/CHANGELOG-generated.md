## Changelog : datagouvfr_data_pipelines (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse et la fiabilité des pipelines de données, notamment concernant l'importation des données RNIC et la gestion des données de pétitions. Des corrections ont été apportées pour gérer les valeurs inattendues, les doublons et les changements dans les sources de données. Des optimisations ont également été réalisées pour améliorer l'efficacité de certains DAGs et réduire les notifications inutiles.

### Évolutions fonctionnelles
- Correction de la récupération de l'ID maximum pour les pétitions, améliorant ainsi le fonctionnement du pipeline associé. [#654](https://github.com/datagouv/datagouvfr_data_pipelines/issues/654)
- Amélioration de la gestion des valeurs de type NA dans les données RNIC, assurant une importation plus fiable.
- Correction de la gestion des doublons dans la colonne de clé primaire des données RNIC.
- Adaptation aux changements de format des données sources, garantissant la continuité des pipelines.

### Évolutions techniques
- Refactoring du DAG météo postgres pour inclure une vérification précoce de l'insertion, améliorant ainsi l'efficacité. [#650](https://github.com/datagouv/datagouvfr_data_pipelines/issues/650)
- Optimisation de la vérification de l'existence des fichiers PostgreSQL, rendant le processus plus rapide.
- Suppression d'un DAG obsolète (SIRENE geocodage).
- Amélioration de la gestion des notifications pour éviter les alertes inutiles et concentrer l'attention sur les problèmes importants.
- Correction de plusieurs typos et erreurs mineures dans le code.
- Ajout d'une nouvelle colonne dans un pipeline (détails non spécifiés).
- Prévention des exécutions concurrentes de certains DAGs pour éviter les conflits.

### Autres changements
- Nettoyage du code et application de règles de linting pour améliorer la qualité et la maintenabilité.
- Restauration de la conversion de messages en HTML.
- Suppression d'une vérification de cohérence non essentielle.
