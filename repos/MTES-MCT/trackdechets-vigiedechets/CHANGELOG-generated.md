## Changelog : trackdechets-vigiedechets (30 derniers jours)

### Résumé
Les dernières mises à jour de Vigiedéchets se concentrent sur l'amélioration de la présentation des données dans les feuilles de rapport, la correction de requêtes pour utiliser les données les plus récentes, et l'ajout de fonctionnalités pour l'export de données et la visualisation cartographique. Des améliorations ont également été apportées à la configuration des workers Celery.

### Évolutions fonctionnelles
- Amélioration de l'affichage des origines des déchets par type BSD dans les feuilles de rapport (#446).
- Ajout du support pour les adresses email autorisées lors de l'export de données (#443).
- Ajout de statistiques cumulées annuelles aux rubriques cartographiques (#433).
- Affichage des partenaires des éco-organismes dans les feuilles de rapport et les PDF (#430).
- Correction de la ponctuation dans le message concernant les partenaires des éco-organismes (#434).
- Modification de l'ordre des sections dans les feuilles de rapport, plaçant la section ICPE avant les données des bordereaux (#426).
- Correction de la fonction `build_stats` pour actualiser correctement la carte ICPE (#432).

### Évolutions techniques
- Correction des requêtes pour utiliser les tables `latest_registry_*` pour toutes les données du registre (NDW, terres excavées, SSD) (#445).
- Modification du champ `size` dans le modèle `DataExport` pour utiliser `PositiveBigIntegerField` (#436).
- Ajout de paramètres de configuration supplémentaires pour les workers Celery (#424).

### Autres changements
- Rien à signaler.
