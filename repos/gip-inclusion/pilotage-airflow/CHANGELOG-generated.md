## Changelog : pilotage-airflow (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'intégration de nouvelles sources de données (DORA, RDV-I, FAGERH, ESAT) et l'amélioration de la qualité des données existantes. Des refactorings importants ont été réalisés sur les modèles DBT pour optimiser l'analyse et faciliter l'intégration future de nouvelles données.

### Évolutions fonctionnelles
- Intégration des données DORA pour les actes métier via un nouveau DAG et des modèles DBT.
- Ajout de la prise en compte des exclusions au niveau des champs pour les enquêtes ESAT.
- Intégration des données RDV-I pour les actes métier, incluant la création de modèles DBT et l'ajout d'une étape de construction dans le DAG existant.
- Intégration des réponses FAGERH, avec un traitement spécifique pour les codes départementaux afin de faciliter leur jointure avec les données de communes.
- Prise en compte de toutes les réponses dans le profil FAGERH.
- Suivi de l'IMER (Indicateur de Mesure de l'Emploi et de la Réinsertion) depuis les données d'emplois.

### Évolutions techniques
- Refactoring des modèles de données d'inclusion autour de tables de dimensions pour les structures et les services, améliorant ainsi l'organisation et la maintenabilité.
- Refactorisation des modèles DI (Dispositifs d'Insertion) et suppression des structures en double.
- Création d'une macro pour indexer les colonnes dans les modèles DBT.
- Documentation des tables RDVI dans le fichier `_sources.yml` de DBT.
- Refactorisation des modèles de réponses ESAT pour utiliser des réponses d'enquête mappées pour l'analyse et modification du DAG pour lancer avec un tag.
- Ajout de documentation pour les tables DORA dans le fichier `_sources.yml` de DBT.
- Suppression des doublons dans les offres/demandes.

### Autres changements
- Correction d'une référence obsolète dans le test d'inclusion des données.
- Ajout du numéro de département.
- Dump de la table "marche".
