## Changelog : document-ia-data (30 derniers jours, au 13 août 2026)

### Résumé
Lancement du projet et mise en place de l'infrastructure de transformation de données. Les premières structures de données sont désormais opérationnelles, permettant de commencer l'analyse des informations relatives aux organisations.

### Évolutions fonctionnelles
- Ajout du premier modèle de données structuré pour les organisations (`core_organization`).

### Évolutions techniques
- Initialisation du dépôt et de l'architecture dbt Core.
- Configuration du schéma PostgreSQL.
- Implémentation des couches de transformation de données (staging, core et analytics).
- Intégration de `sqlfluff` pour le contrôle de la qualité et du formatage du code SQL.

### Autres changements
- Mise à jour de la documentation (README).
