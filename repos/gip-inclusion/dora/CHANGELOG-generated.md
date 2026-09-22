## Changelog : dora (30 derniers jours, au 21 septembre 2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur l'enrichissement des informations relatives aux services (horaires, descriptions plus précises) et sur l'amélioration de la fiabilité des données synchronisées avec les partenaires. L'expérience utilisateur a été fluidifiée par l'ajout de nouvelles capacités de recherche géographique et de notifications automatiques pour le suivi des orientations.

### Évolutions fonctionnelles
- **Amélioration des informations services** : ajout des horaires d'accueil, gestion optimisée des descriptions via une fusion algorithmique [#1293](https://github.com/gip-inclusion/dora/issues/1293) et une double écriture pour plus de cohérence [#1306](https://github.com/gip-inclusion/dora/issues/1306), et intégration des champs de mobilisation.
- **Recherche et données** : mise à disposition d'une nouvelle route pour la recherche par communes et EPCI [#1340](https://github.com/gip-inclusion/dora/issues/1340) et ajout de champs supplémentaires pour la synchronisation avec Data Inclusion [#1345](https://github.com/gip-inclusion/dora/issues/1345).
- **Gestion des orientations** : mise en place de notifications Slack lors du passage d'une orientation en modération [#1296](https://github.com/gip-inclusion/dora/issues/1296) et ajout de l'identifiant FT dans les exports des orientations reçues [#1290](https://github.com/gip-inclusion/dora/issues/1290).
- **Corrections d'expérience utilisateur** : résolution des doublons de formulaires pour les services [#1354](https://github.com/gip-inclusion/dora/issues/1354) et optimisation du chargement des structures pour le personnel afin d'éviter les surcharges [#1353](https://github.com/gip-inclusion/dora/issues/1353).

### Évolutions techniques
- **Framework de données** : implémentation d'un nouveau cadre de migration (`di_v1`) pour sécuriser la synchronisation des données et gestion de la double écriture pour les zones d'éligibilité et les conditions d'accès [#1318](https://github.com/gip-inclusion/dora/issues/1318).
- **Automatisation et outils** : ajout d'une tâche mensuelle pour la mise à jour automatique de la base Sirene [#1310](https://github.com/gip-inclusion/dora/issues/1310) et création d'une commande d'anonymisation des données [#1321](https://github.com/gip-inclusion/dora/issues/1321).
- **Infrastructure et maintenance** : mise à jour de l'image Minio dans la CI [#1355](https://github.com/gip-inclusion/dora/issues/1355), rollback vers Django 6.0.8 [#1313](https://github.com/gip-inclusion/dora/issues/1313) et nettoyage de plusieurs scripts et commandes de gestion obsolètes.

### Autres changements
- **Documentation** : amélioration de la documentation relative aux données d'orientation.
- **Nettoyage** : suppression de la colonne `orientation_reasons` [#1317](https://github.com/gip-inclusion/dora/issues/1317).
