## Changelog : dora (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois-ci, Dora a concentré ses efforts sur la fiabilisation et la synchronisation des données, notamment via l'intégration d'un nouveau cadre de migration pour l'écosystème Data Inclusion. Les utilisateurs bénéficient de nouvelles capacités de recherche géographique et d'une interface enrichie pour la gestion des territoires, tandis que l'infrastructure de stockage a été modernisée.

### Évolutions fonctionnelles
- **Gestion des territoires** : Création d'une nouvelle page d'accueil "Gérer mon territoire" dédiée aux Groupes Territoriaux (GT) [#1339].
- **Recherche géographique** : Ajout d'une fonctionnalité permettant de rechercher des communes et des EPCI [#1340].
- **Enrichissement des services** : 
    - Ajout du champ "horaires d'accueil" pour les services.
    - Amélioration de la gestion des descriptions et des liens de mobilisation.
    - Correction de la synchronisation des modèles de services [#1370].
- **Exports et données** : Ajout de l'identifiant FT dans les exports des orientations reçues [#1290].
- **Améliorations de l'expérience utilisateur** :
    - Optimisation du chargement des structures pour le personnel afin d'éviter les surcharges [#1353].
    - Correction pour empêcher la création de doublons de formulaires pour un même service [#1354].

### Évolutions techniques
- **Infrastructure de stockage** : Migration du stockage S3 local de MinIO vers SeaweedFS [#1376].
- **Pipeline de données** : 
    - Mise en place d'un nouveau framework de migration (di_v1) pour sécuriser la synchronisation des données vers Data Inclusion.
    - Implémentation de mécanismes de "double écriture" pour garantir la cohérence des données (conditions d'accès, zones d'éligibilité, descriptions) lors des transitions.
    - Automatisation de la mise à jour mensuelle de la base Sirene [#1310].
- **Sécurité et maintenance** : 
    - Introduction d'une commande de gestion pour l'anonymisation des données [#1321].
    - Ajustements de l'infrastructure CI et rollback de la version Django pour assurer la stabilité [#1313, #1355].

### Autres changements
- **Nettoyage** : Suppression de plusieurs commandes de gestion (management commands) et scripts obsolètes.
- **Base de données** : Retrait de la colonne `orientation_reasons` [#1317].
- **Documentation** : Amélioration de la documentation concernant les données d'orientation.
