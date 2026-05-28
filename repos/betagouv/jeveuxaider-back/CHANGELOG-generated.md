## Changelog : jeveuxaider-back (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances du backend, notamment au niveau des requêtes statistiques et des logs d'activité. Des corrections ont été apportées pour mieux gérer la synchronisation des données avec Airtable, en particulier pour les missions supprimées ou en brouillon. De nouvelles fonctionnalités ont été ajoutées pour faciliter la gestion des notifications et des abonnements des structures.

### Évolutions fonctionnelles
- Les structures peuvent maintenant se désinscrire de manière autonome des notifications. [#172](https://github.com/betagouv/jeveuxaider-back/issues/172)
- Un bandeau d'email de destinataire a été implémenté dans les emails de notification. [#189](https://github.com/betagouv/jeveuxaider-back/issues/189)
- Possibilité de filtrer les missions par ID lors de la synchronisation avec Airtable.
- Ajout de champs supplémentaires dans les exports de données. [#179](https://github.com/betagouv/jeveuxaider-back/issues/179)
- Pagination implémentée pour les logs d'activité, améliorant la navigation et la performance. [#176](https://github.com/betagouv/jeveuxaider-back/issues/176)

### Évolutions techniques
- Optimisation des requêtes statistiques en modifiant les jointures et les conditions pour les rôles. [#182](https://github.com/betagouv/jeveuxaider-back/issues/182)
- Ajout d'index partiels sur les tables `activity_log` et `participations` pour améliorer les performances des requêtes. [#175](https://github.com/betagouv/jeveuxaider-back/issues/175)
- Ajout d'index et configuration d'autovacuum pour le log d'activité afin d'améliorer les performances. [#188](https://github.com/betagouv/jeveuxaider-back/issues/188)
- Refactor de la gestion de l'état de participation, suppression de `actingAs`. [#191](https://github.com/betagouv/jeveuxaider-back/issues/191)
- Optimisation et refactoring des requêtes de modération des statistiques pour une meilleure efficacité et lisibilité. [#184](https://github.com/betagouv/jeveuxaider-back/issues/184)
- Amélioration de la logique de synchronisation des missions avec Airtable pour inclure les missions supprimées et exclure les missions non pertinentes. [#190](https://github.com/betagouv/jeveuxaider-back/issues/190), [#192](https://github.com/betagouv/jeveuxaider-back/issues/192)
- Utilisation de l'opérateur `ilike` au lieu de la recherche exacte pour une meilleure flexibilité. [#106](https://github.com/betagouv/jeveuxaider-back/issues/106)
- Suppression du filtre de département inutilisé dans la requête d'invitation.
- Correction de la gestion de la suppression de missions et de structures dans l'état "Brouillon" lors de la synchronisation Airtable.

### Autres changements
- Ajout d'un filtre pour exclure les entrées propres de l'utilisateur dans les notes. [#180](https://github.com/betagouv/jeveuxaider-back/issues/180)
- Amélioration du calcul des statistiques de modération. [#187](https://github.com/betagouv/jeveuxaider-back/issues/187)
- Ajout d'un index partiel pour améliorer les performances des requêtes de statistiques. [#186](https://github.com/betagouv/jeveuxaider-back/issues/186)
