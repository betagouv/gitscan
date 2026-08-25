## Changelog : pilotage-airflow (30 derniers jours, au 24/08/2026)

### Résumé
Ce mois a été marqué par une mise à jour majeure de l'infrastructure vers Airflow 3 et par un enrichissement significatif des modèles de données. Les processus de traitement des enquêtes (ESAT, FAGERH, IMER) ont été affinés pour garantir une meilleure précision des indicateurs et une orchestration plus robuste.

### Évolutions fonctionnelles
- **Enquêtes ESAT** : Amélioration de la clarté des données via le renommage de colonnes, ajustement des seuils de complétude et fiabilisation du mapping des réponses.
- **Enquêtes FAGERH** : Ajout de nouveaux modèles pour le calcul du taux d'emploi, mise à jour du mapping des prestations et intégration du suivi des bénéficiaires directs.
- **Enquête IMER** : Mise en place de l'orchestration et ajustement de la planification des tâches.
- **Reporting** : Ajout de colonnes de comptage des préconisations dans les tables de données finales (marts).

### Évolutions techniques
- **Infrastructure** : Migration complète vers Airflow 3, incluant la mise à jour des DAGs et l'implémentation d'un nouveau gestionnaire d'authentification (`simpleAuthManager`).
- **CI/CD** : Optimisation des pipelines de tests pour éviter les exécutions inutiles et amélioration de la gestion du cache pour l'outil `setup-uv`.

### Autres changements
- **Documentation** : Amélioration de la qualité rédactionnelle et mise à jour des définitions des modèles de données DBT.
