## Changelog : dora (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilisation et la synchronisation des données, notamment via la mise en place d'un nouveau cadre de migration pour faciliter les échanges avec Data Inclusion. Les utilisateurs bénéficient également d'une meilleure recherche géographique, de nouvelles informations sur les services (horaires d'accueil) et d'un système de notifications Slack pour le suivi de la modération.

### Évolutions fonctionnelles
- **Recherche améliorée** : Ajout d'une fonctionnalité de recherche pour les communes et les EPCI [#1340](https://github.com/gip-inclusion/dora/issues/1340).
- **Informations services** : Ajout du champ "horaires d'accueil" pour les services.
- **Notifications** : Mise en place de notifications Slack lors du passage d'une orientation en modération [#1296](https://github.com/gip-inclusion/dora/issues/1296).
- **Administration** : 
    - Les Groupes de Travail (GT) peuvent désormais accéder directement à la page d'administration d'une structure [#1286](https://github.com/gip-inclusion/dora/issues/1286).
    - Correction des liens vers l'administration Django [#1295](https://github.com/gip-inclusion/dora/issues/1295).
- **Gestion des services** : Suppression de la limite du nombre de catégories par service [#1289](https://github.com/gip-inclusion/dora/issues/1289).
- **Exports** : Ajout de la colonne "Identifiant FT" dans l'export des orientations reçues [#1290](https://github.com/gip-inclusion/dora/issues/1290).
- **Corrections** : Amélioration de l'utilisation des labels de financement pour les services [#1309](https://github.com/gip-inclusion/dora/issues/1309).

### Évolutions techniques
- **Synchronisation de données (Framework di_v1)** : Implémentation d'un nouveau cadre de migration et de commandes de "backfill" pour automatiser et fiabiliser la synchronisation des données vers Data Inclusion (descriptions, zones d'éligibilité, conditions d'accès, etc.) [#913886b, #1345, #1318, #5c65b5b, #1306, #7ca16ca].
- **Qualité des données** : 
    - Fusion algorithmique des descriptions de services pour plus de cohérence [#1293](https://github.com/gip-inclusion/dora/issues/1293).
    - Automatisation de la mise à jour mensuelle de la base Sirene [#1310](https://github.com/gip-inclusion/dora/issues/1310).
    - Ajout d'une commande pour l'anonymisation des données [#1321](https://github.com/gip-inclusion/dora/issues/1321).
- **Refactoring du modèle Services** : Simplification de la structure des services par le renommage de champs et la suppression de modèles de catégories obsolètes (ServiceKind) [#1282](https://github.com/gip-inclusion/dora/issues/1282, #1266, #1257).
- **Performance** : Optimisation de la vitesse de chargement des pages d'édition via la parallélisation des appels API [#1281](https://github.com/gip-inclusion/dora/issues/1281).
- **Stabilité** : Rollback de la version Django pour garantir la stabilité de l'environnement [#1313](https://github.com/gip-inclusion/dora/issues/1313).

### Autres changements
- **Nettoyage du code** : Suppression de plusieurs commandes de gestion (management commands) et scripts obsolètes.
- **Nettoyage de la base de données** : Retrait de colonnes et de champs non utilisés (ex: `orientation_reasons` [#1317](https://github.com/gip-inclusion/dora/issues/1317) et `use_inclusion_numerique_scheme` [#1279](https://github.com/gip-inclusion/dora/issues/1279)).
- **Documentation** : Amélioration de la documentation technique sur les données d'orientation.
