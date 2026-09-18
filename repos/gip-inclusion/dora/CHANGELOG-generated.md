## Changelog : dora (30 derniers jours, au 17 septembre 2026)

### Résumé
Ce mois-ci, Dora a principalement progressé sur la fiabilisation et la synchronisation de ses données, notamment grâce à la mise en place d'un nouveau cadre de migration pour faciliter l'échange avec Data Inclusion. Les utilisateurs bénéficient d'une information plus riche sur les services (horaires, descriptions améliorées) et de nouvelles capacités de recherche. Des optimisations de performance et de nouveaux outils de notification (Slack) viennent renforcer l'efficacité de la plateforme.

### Évolutions fonctionnelles
- **Amélioration des services** : Ajout des horaires d'accueil et optimisation des descriptions via une fusion algorithmique pour plus de clarté [#1293](https://github.com/gip-inclusion/dora/issues/1293) ([#1306](https://github.com/gip-inclusion/dora/issues/1306)).
- **Recherche et navigation** : Ajout d'une route de recherche pour les communes et les EPCI [#1340](https://github.com/gip-inclusion/dora/issues/1340) et suppression de la limite du nombre de catégories par service [#1289](https://github.com/gip-inclusion/dora/issues/1289).
- **Notifications et alertes** : Mise en place de notifications Slack lors du passage d'une orientation en modération [#1296](https://github.com/gip-inclusion/dora/issues/1296).
- **Gestion administrative** : Accès facilité aux pages d'administration des structures pour les Groupes Territoriaux (GT) [#1286](https://github.com/gip-inclusion/dora/issues/1286) et correction des URL de l'administration Django [#1295](https://github.com/gip-inclusion/dora/issues/1295).
- **Exports de données** : Enrichissement de l'export des orientations avec l'identifiant FT [#1290](https://github.com/gip-inclusion/dora/issues/1290).
- **Corrections d'interface** : Résolution de problèmes de doublons de formulaires pour les services [#1354](https://github.com/gip-inclusion/dora/issues/1354).

### Évolutions techniques
- **Synchronisation de données (Data Inclusion)** : Déploiement d'un nouveau framework de migration (`di_v1`) permettant la synchronisation et le remplissage automatique (backfill) des champs vers Data Inclusion (zones d'éligibilité, réseaux porteurs, mobilisation, etc.) [#913886b](https://github.com/gip-inclusion/dora/issues/913886b) ([#1345](https://github.com/gip-inclusion/dora/issues/1345)).
- **Optimisation des performances** : Parallélisation des appels pour l'édition des services et des modèles [#1281](https://github.com/gip-inclusion/dora/issues/1281) et optimisation du chargement des structures pour le personnel afin d'éviter les surcharges [#1353](https://github.com/gip-inclusion/dora/issues/1353).
- **Automatisation** : Création d'une tâche mensuelle pour la mise à jour automatique de la base Sirene [#1310](https://github.com/gip-inclusion/dora/issues/1310).
- **Outils de maintenance** : Ajout d'une commande d'anonymisation des données [#1321](https://github.com/gip-inclusion/dora/issues/1321).
- **Refactorisation et infrastructure** : 
    - Renommage et restructuration des champs de description des services [#1282](https://github.com/gip-inclusion/dora/issues/1282).
    - Mise à jour de l'image Minio dans la CI [#1355](https://github.com/gip-inclusion/dora/issues/1355).
    - Rollback de la version Django pour assurer la stabilité [#1313](https://github.com/gip-inclusion/dora/issues/1313).

### Autres changements
- **Nettoyage** : Suppression de plusieurs commandes de gestion (management commands) et scripts obsolètes pour alléger le projet.
- **Documentation** : Amélioration de la documentation concernant les données d'orientation [#85d0072](https://github.com/gip-inclusion/dora/issues/85d0072).
