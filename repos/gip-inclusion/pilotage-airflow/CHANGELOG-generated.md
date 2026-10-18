## Changelog : pilotage-airflow (30 derniers jours, au 15 octobre 2026)

### Résumé
Ce mois a été marqué par un enrichissement significatif des données de pilotage, notamment sur les thématiques d'orientation et des professionnels. Les travaux ont également porté sur l'optimisation de l'orchestration des flux pour éviter les conflits de synchronisation et sur le renforcement de la sécurité et de la qualité des données traitées.

### Évolutions fonctionnelles
- **Enrichissement des données et nouveaux modèles** :
    - Création de nouveaux modèles de reporting pour les orientations et d'un modèle consolidé pour les professionnels ("all pros").
    - Ajout de nouvelles informations dans les modèles : colonnes de refus, type d'utilisateur (`user_kind`) dans les orientations, nouvelles colonnes DORA et intégration des informations de structure dans le modèle IMER.
- **Amélioration de la qualité des données** :
    - Affinement des réponses ESAT grâce à l'application d'exclusions basées sur l'analyse des commentaires libres.
    - Corrections de bugs sur les données DORA.

### Évolutions techniques
- **Optimisation de l'orchestration** :
    - Ajustement des horaires de lancement des tâches DBT pour éviter les chevauchements entre les flux (notamment entre DORA et la synchronisation "Le Marché").
- **Maintenance des pipelines de données** :
    - Mise à jour du récupérateur (*fetcher*) DORA pour intégrer les nouveaux modèles métier (IMER et orientations).
    - Changement de la source de données pour les emplois.
    - Ajustements des schémas de base de données et suppression de champs obsolètes.
- **Sécurité et maintenance** :
    - Application de mises à jour de sécurité et de dépendances critiques (notamment `pyjwt` et `urllib3`).

### Autres changements
- **Refactorisation** : Renommage d'un modèle pour améliorer la clarté et la cohérence du projet.
