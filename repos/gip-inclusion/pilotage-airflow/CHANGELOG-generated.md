## Changelog : pilotage-airflow (30 derniers jours, au 15/09/2026)

### Résumé
Ce mois a été marqué par une mise à jour majeure de l'infrastructure vers Airflow 3 et un enrichissement significatif des modèles de données. Le projet a considérablement étendu sa capacité d'analyse sur les thématiques des "actes métiers", du "GEIQ" et du projet "Fagerh", tout en optimisant la fiabilité des flux de données pour prévenir les interruptions de service.

### Évolutions fonctionnelles
- **Enrichissement des données :** Intégration de nouveaux modèles de données pour le GEIQ, les "actes métiers" (incluant Monrecap, GPS et LeMarché) et le projet Fagerh (ajout des informations sur les organismes, les partenaires et les participations MDPH).
- **Amélioration de l'analyse :** Consolidation des données "Dora" et "Les Emplois" pour les parcours d'orientation et l'IMER, ainsi que création de tables agrégées mensuelles pour les sources d'actes métiers.
- **Précision des indicateurs :** Mise à jour des calculs des montants accordés/conventions, renommage de colonnes pour plus de clarté (ESAT) et ajustement des seuils de complétude des données.
- **Gestion des accès :** Ajout de la logique de distinction du statut d'administrateur d'organisation pour les utilisateurs.

### Évolutions techniques
- **Migration majeure :** Passage à Airflow 3, incluant la mise à jour des DAGs et l'adoption du `SimpleAuthManager`.
- **Optimisation des performances :** Modification de la fréquence de récupération des données Matomo (intervalles quotidiens) pour éviter les dépassements de délai (timeouts).
- **Fiabilité et Qualité de la donnée :**
  - Correction de jointures erronées sur le modèle des contrats et suppression de doublons dans les données ESAT.
  - Optimisation des tests DBT (réduction des tests indirects et passage de certains tests de relation en mode "warning").
  - Application de correctifs de sécurité.
- **Orchestration :** Ajustement des calendriers d'exécution (schedules) pour plusieurs processus (IMER, DBT daily, Data Inclusion) et suppression des DAGs et tags obsolètes.

### Autres changements
- **Documentation :** Amélioration de la qualité rédactionnelle et de la documentation de population des DAGs.
- **Maintenance :** Ajustements de l'outil de linting SQLFluff et nettoyage général du code.
