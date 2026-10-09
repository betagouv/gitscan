## Changelog : pilotage-airflow (30 derniers jours, au 08/10/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'enrichissement des capacités de reporting, notamment avec l'ajout de nouveaux modèles pour les orientations et les données GEIQ. Les données relatives aux utilisateurs et aux structures (IMER) ont été affinées pour offrir une vision plus précise. Parallèlement, l'infrastructure de données a été optimisée pour gagner en fiabilité et en sécurité.

### Évolutions fonctionnelles
- **Nouveaux modèles de données** : Ajout de modèles de reporting pour les orientations et intégration des modèles GEIQ.
- **Enrichissement des informations** : 
    - Ajout de précisions sur le profil utilisateur (type d'utilisateur, statut d'administrateur d'organisation).
    - Amélioration du modèle IMER incluant désormais les structures non-connectées et des vues d'informations détaillées.
    - Ajout de nouvelles colonnes et données pour le suivi Dora.
- **Amélioration du suivi métier** : 
    - Consolidation des sources d'actes métiers dans une table agrégée mensuelle.
    - Mise à jour des sources de données pour les emplois.
    - Nouveaux calculs pour les montants accordés et conventionnés.
- **Corrections** : Résolution d'un bug sur les données Dora.

### Évolutions techniques
- **Orchestration Airflow** : 
    - Modification de l'heure de lancement du DAG d'inclusion de données.
    - Suppression du DAG `dbt_imer` devenu obsolète.
- **Pipelines de données** : Mise à jour du récupérateur (fetcher) Dora et intégration de nouveaux imports pour accompagner les nouveaux modèles.
- **Sécurité et Qualité** : 
    - Mise à jour de sécurité (notamment `pyjwt`).
    - Optimisation des tests DBT pour éviter les exécutions indirectes inutiles.
    - Ajustement de la sévérité des tests de relation (passage en mode "warning") pour améliorer la fluidité des déploiements.
- **Maintenance du schéma** : Nettoyage de structures et de colonnes obsolètes (`structures.opening_hours_details`).

### Autres changements
- Correction de la nomenclature de certains modèles pour une meilleure clarté.
