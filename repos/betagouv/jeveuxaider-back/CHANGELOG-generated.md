## Changelog : jeveuxaider-back (30 derniers jours, au 2026-05-14)

### Résumé
Ce mois-ci, les améliorations se sont concentrées sur l'optimisation des performances, notamment au niveau des requêtes statistiques et des journaux d'activité. Des fonctionnalités ont également été ajoutées pour faciliter la gestion des structures et des missions, ainsi que pour améliorer l'expérience utilisateur, notamment en permettant aux structures de se désinscrire de manière autonome.

### Évolutions fonctionnelles
- Les structures peuvent maintenant se désinscrire de manière autonome [#172](https://github.com/betagouv/jeveuxaider-back/issues/172).
- Ajout d'un filtre pour exclure les propres entrées de l'utilisateur dans les notes [#180](https://github.com/betagouv/jeveuxaider-back/issues/180).
- Ajout de champs supplémentaires dans les exports de données [#179](https://github.com/betagouv/jeveuxaider-back/issues/179).
- Implémentation d'une pagination simple pour les journaux d'activité [#176](https://github.com/betagouv/jeveuxaider-back/issues/176).
- Correction de la gestion de la suppression de missions et de structures depuis Airtable, notamment pour les éléments en état "Brouillon".
- Ajout d'une commande pour fermer les missions pour mineurs à partir de modèles fermés [#174](https://github.com/betagouv/jeveuxaider-back/issues/174).
- Correction d'un problème empêchant l'ouverture de missions pour mineurs basées sur les paramètres du modèle [#173](https://github.com/betagouv/jeveuxaider-back/issues/173).
- Correction du message de bienvenue dans la notification "StructureAssociationValidated" [#21](https://github.com/betagouv/jeveuxaider-back/issues/21).
- Correction d'un bug lié au numéro de téléphone et au code postal manquants pour les utilisateurs [#171](https://github.com/betagouv/jeveuxaider-back/issues/171).
- Amélioration de la gestion des erreurs lors de l'acceptation d'une invitation [#170](https://github.com/betagouv/jeveuxaider-back/issues/170).

### Évolutions techniques
- Ajout d'index et de paramètres d'autovacuum pour le journal d'activité afin d'améliorer les performances [#188](https://github.com/betagouv/jeveuxaider-back/issues/188).
- Amélioration de la requête de comptage des modérations en ajoutant la logique de jointure de l'objet [#187](https://github.com/betagouv/jeveuxaider-back/issues/187).
- Ajout d'un index partiel pour améliorer les performances des requêtes statistiques [#186](https://github.com/betagouv/jeveuxaider-back/issues/186).
- Optimisation et refactorisation des requêtes de modération des statistiques pour plus d'efficacité et de lisibilité [#184](https://github.com/betagouv/jeveuxaider-back/issues/184).
- Optimisation des requêtes statistiques en mettant à jour les jointures et les conditions pour les éléments modifiables [#182](https://github.com/betagouv/jeveuxaider-back/issues/182).
- Optimisation des requêtes de modération des statistiques avec de nouveaux index [#181](https://github.com/betagouv/jeveuxaider-back/issues/181).
- Ajout d'index partiels aux tables `activity_log` et `participations` pour l'optimisation [#175](https://github.com/betagouv/jeveuxaider-back/issues/175).
- Implémentation d'une base de données réplica pour améliorer les performances [#164](https://github.com/betagouv/jeveuxaider-back/issues/164).
- Suppression des missions passées de `ApiEngagementExportMissionsJob` [#169](https://github.com/betagouv/jeveuxaider-back/issues/169).
- Suppression de l'utilisation de `UseReplicaDBConnection` dans `StatisticsPublicController` (refactorisation).

### Autres changements
- Correction d'un problème lié à la duplication de missions ouvertes aux mineurs en fonction des paramètres du modèle.
- Ajout de noms d'activité manquants dans le mappage des activités de mission [#168](https://github.com/betagouv/jeveuxaider-back/issues/168).
