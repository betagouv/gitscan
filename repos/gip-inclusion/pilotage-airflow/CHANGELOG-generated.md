## Changelog : pilotage-airflow (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois a été marqué par un enrichissement significatif des données destinées aux tableaux de bord, notamment pour le suivi des "actes métiers". Les processus de traitement des enquêtes (FAGERH et ESAT) ont été affinés pour garantir une meilleure précision des indicateurs, tandis que l'architecture des modèles de données a été restructurée pour gagner en robustesse et en clarté.

### Évolutions fonctionnelles
- **Enrichissement du tableau de bord "Actes Métiers"** : Intégration de nouvelles sources de données (DORA, Matomo et RDV-I) pour fournir une vision plus complète.
- **Optimisation de l'enquête FAGERH** : 
    - Amélioration du calcul du taux d'emploi.
    - Mise à jour du mapping des prestations et de l'analyse des bénéficiaires directs.
    - Inclusion de l'intégralité des réponses dans les profils.
    - Optimisation des jointures géographiques (départements) pour faciliter le rapprochement avec les communes.
- **Amélioration de l'enquête ESAT** : Mise en place d'exclusions au niveau des champs pour affiner la qualité des données.
- **Nouveaux indicateurs et nettoyages** :
    - Ajout du comptage des préconisations dans les tables de synthèse (marts).
    - Suppression des doublons dans les flux offre/demande.
    - Ajout du suivi de l'IMER à partir des données d'emplois.

### Évolutions techniques
- **Refonte de l'architecture de données** : Restructuration des modèles d'inclusion de données autour de tables de dimensions (structures et services) pour une meilleure organisation.
- **Orchestration et infrastructure** :
    - Mise à jour de la version d'Airflow.
    - Automatisation de l'orchestration des flux IMER.
- **Optimisation du code** : Création d'une macro pour l'indexation des colonnes afin de standardiser les processus.

### Autres changements
- **Documentation** : Correction des définitions dans la documentation des modèles DBT pour l'enquête ESAT.
- **Tests** : Correction de références obsolètes dans les tests d'inclusion de données.
