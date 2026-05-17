## Changelog : jeveuxaider-back (30 derniers jours, au 2026-05-15)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances du backend, notamment au niveau des requêtes statistiques et des journaux d'activité. Des améliorations ont également été apportées à la gestion des missions, en particulier celles concernant les mineurs, ainsi qu'à la gestion des structures et de leurs abonnements. Enfin, des corrections et des améliorations ont été apportées à l'expérience utilisateur, notamment concernant les notifications et l'acceptation des invitations.

### Évolutions fonctionnelles
- Les structures peuvent maintenant se désabonner de manière autonome. [#172](https://github.com/betagouv/jeveuxaider-back/issues/172)
- Ajout d'un filtre pour exclure les notes créées par l'utilisateur lui-même. [#180](https://github.com/betagouv/jeveuxaider-back/issues/180)
- Ajout de champs supplémentaires dans les exports de données. [#179](https://github.com/betagouv/jeveuxaider-back/issues/179)
- Amélioration de la gestion des missions et des structures provenant d'Airtable, notamment en gérant correctement la suppression des éléments en état "Brouillon".
- Ajout d'une commande pour fermer les missions destinées aux mineurs à partir de modèles fermés. [#174](https://github.com/betagouv/jeveuxaider-back/issues/174)
- Correction d'un problème empêchant l'ouverture de missions dupliquées pour les mineurs en fonction des paramètres du modèle. [#173](https://github.com/betagouv/jeveuxaider-back/issues/173)
- Amélioration du message de bienvenue dans la notification "StructureAssociationValidated". [#201](https://github.com/betagouv/jeveuxaider-back/issues/171)
- Gestion des erreurs lors de l'acceptation d'une invitation. [#170](https://github.com/betagouv/jeveuxaider-back/issues/170)
- Pagination implémentée pour les journaux d'activité, améliorant la navigation et les performances. [#176](https://github.com/betagouv/jeveuxaider-back/issues/176)

### Évolutions techniques
- Optimisation des requêtes statistiques en modifiant les jointures et les conditions pour les éléments "rolables". [#182](https://github.com/betagouv/jeveuxaider-back/issues/182)
- Optimisation des requêtes de comptage des modérations statistiques avec de nouveaux index. [#181](https://github.com/betagouv/jeveuxaider-back/issues/181)
- Ajout d'index partiels sur les tables `activity_log` et `participations` pour améliorer les performances des requêtes. [#175](https://github.com/betagouv/jeveuxaider-back/issues/175)
- Ajout d'index et de paramètres d'autovacuum pour le journal d'activité afin d'améliorer les performances. [#188](https://github.com/betagouv/jeveuxaider-back/issues/188)
- Amélioration de la requête de comptage des modérations en ajoutant la logique de jointure de l'objet. [#187](https://github.com/betagouv/jeveuxaider-back/issues/187)
- Ajout d'un index partiel pour améliorer les performances des requêtes sur les statistiques. [#186](https://github.com/betagouv/jeveuxaider-back/issues/186)
- Optimisation et refactorisation des requêtes de modération des statistiques pour une meilleure efficacité et lisibilité. [#184](https://github.com/betagouv/jeveuxaider-back/issues/184)
- Utilisation de l'opérateur `ilike` au lieu de la recherche exacte pour une meilleure flexibilité. [#106](https://github.com/betagouv/jeveuxaider-back/issues/106)
- Suppression d'un filtre de département inutilisé de la requête d'invitation.

### Autres changements
- Suppression de l'utilisation de `UseReplicaDBConnection` dans `StatisticsPublicController` (commentée).
- Correction d'un bug lié à la gestion des missions et des structures en brouillon provenant d'Airtable.
