## Changelog : pilotage-airflow (30 derniers jours, au 04/08/2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur l'enrichissement des indicateurs issus des enquêtes (FAGERH, ESAT) et l'intégration de nouveaux flux de données (DORA, IMER). Ces évolutions permettent d'affiner la précision des analyses et d'automatiser davantage le suivi des activités de pilotage.

### Évolutions fonctionnelles
- **Enrichissement de l'enquête FAGERH** : intégration du taux d'emploi, mise à jour du mapping des prestations, analyse des bénéficiaires directs et ajout du comptage des préconisations dans les tables de synthèse (marts).
- **Intégration des données DORA** : mise en place de nouveaux modèles DBT et de DAGs Airflow pour le suivi des actes métier.
- **Amélioration de la qualité des données ESAT** : application de règles d'exclusion au niveau des champs pour garantir la fiabilité des résultats de l'enquête.
- **Suivi de l'IMER** : intégration du suivi de l'IMER à partir des données d'emplois.

### Évolutions techniques
- **Infrastructure et Orchestration** : mise à jour de la version d'Airflow et automatisation de l'orchestration pour le flux IMER.
- **Optimisation CI/CD** : amélioration des performances des pipelines de CI via la gestion du cache (`prune-cache`) pour l'action `setup-uv`.

### Autres changements
- **Documentation** : correction des définitions dans la documentation des modèles DBT pour l'enquête ESAT.
