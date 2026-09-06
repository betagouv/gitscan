## Changelog : pilotage-airflow (30 derniers jours, au 04/09/2026)

### Résumé
Ce mois-ci a été marqué par une extension significative des capacités d'analyse grâce à l'intégration de nouveaux modèles de données dédiés aux "actes métier" (emplois, inclusion). Parallèlement, le projet a franchi une étape majeure de modernisation avec la migration complète de l'infrastructure d'orchestration vers Airflow 3.

### Évolutions fonctionnelles
- **Nouveaux indicateurs "Actes Métier"** : Intégration de nouveaux modèles de données (DBT) couvrant les domaines de l'emploi, de "lemarché", "monrecap" et "gps" pour enrichir les calculs d'inclusion.
- **Nouveau flux de données** : Mise en place d'un DAG dédié pour la construction et l'inclusion des données "actes-métier".
- **Amélioration de la qualité des données** :
    - Correction de jointures erronées sur le modèle des contrats.
    - Nettoyage des doublons dans les données sources ESAT.
    - Renommage de colonnes ESAT pour une meilleure clarté métier et ajustement des seuils de complétude.
    - Correction de la logique de mapping des réponses pour les enquêtes ESAT.

### Évolutions techniques
- **Migration vers Airflow 3** : Mise à jour majeure de l'infrastructure d'orchestration, incluant l'adaptation des DAGs et la mise en œuvre du nouveau gestionnaire d'authentification (`simpleAuthManager`).
- **Optimisation des pipelines** : 
    - Ajout de nouveaux calendriers d'exécution (scheduling) pour `dbt_daily` et `imer`.
    - Optimisation de la suite de tests pour éviter l'exécution de tests inutiles.
- **Maintenance et stabilité** :
    - Application de correctifs de sécurité.
    - Ajustements de compatibilité (notamment pour Pandas 3 et les types de colonnes).
    - Amélioration de la gestion des erreurs (exceptions sur les noms manquants).

### Autres changements
- **Documentation** : Amélioration de la rédaction des contenus documentaires.
- **Qualité du code** : Ajustements de la configuration de linting (`sqlfluff`).
