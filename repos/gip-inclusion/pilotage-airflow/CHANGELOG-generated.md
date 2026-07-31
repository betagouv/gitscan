## Changelog : pilotage-airflow (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'intégration de nouvelles sources de données (FAGERH, RDV-I, Dora, Matomo, IMER) et l'amélioration des modèles de données existants, notamment pour les enquêtes ESAT. Des optimisations ont également été apportées pour la qualité des données et la performance des pipelines.

### Évolutions fonctionnelles
- Intégration des données de l'enquête FAGERH : ajout de modèles pour l'analyse des taux d'emploi et des réponses, avec gestion des codes départementaux et des bénéficiaires directs. [#1234](https://github.com/gip-inclusion/pilotage-airflow/issues/1234)
- Ajout de la source de données Dora pour les actes métier, avec DAG et modèles DBT correspondants.
- Intégration des données Matomo pour le suivi des actes métier, avec DAG et modèles DBT.
- Intégration des données RDV-I pour les actes métier, avec DAG et modèles DBT.
- Suivi de l'IMER à partir des données d'emplois.
- Amélioration de la gestion des données ESAT : ajout d'exclusions au niveau des champs et refonte des modèles pour une meilleure analyse.
- Inclusion de toutes les réponses dans le profil FAGERH.

### Évolutions techniques
- Refonte des modèles de données autour des tables de dimensions pour les structures et services (inclusion de données).
- Refactorisation des modèles DI pour améliorer la cohérence et supprimer les structures dupliquées.
- Création d'une macro pour indexer les colonnes dans DBT.
- Amélioration de la documentation DBT pour les tables RDVI.
- Refonte des modèles de réponses ESAT pour utiliser les réponses mappées de l'enquête.
- Suppression des doublons dans les données offres/demandes.
- Ajout d'un numéro de département (dpt) dans les données.

### Autres changements
- Ajout de tests pour vérifier l'inclusion de données à jour.
- Documentation des tables Dora dans le fichier `_sources.yml` de DBT.
- Dump de la table "marche".
- Mise à jour de la définition des champs dans les modèles DBT de l'enquête ESAT.
