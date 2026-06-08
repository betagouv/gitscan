## Changelog : jeveuxaider-back (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances et de la synchronisation des données, notamment concernant les missions et les organisations. Des corrections ont été apportées pour mieux gérer les missions supprimées et filtrer les résultats de recherche. Des améliorations ont également été apportées à la gestion des notifications et à l'expérience des structures.

### Évolutions fonctionnelles
- **Synchronisation Airtable :** Amélioration de la synchronisation des missions depuis Airtable, incluant désormais la prise en compte des missions supprimées et la possibilité de filtrer les organisations par ID. [#192](https://github.com/betagouv/jeveuxaider-back/issues/192) [#185](https://github.com/betagouv/jeveuxaider-back/issues/185)
- **Notifications :** Ajout d'un bandeau avec l'adresse email du destinataire dans les notifications. [#189](https://github.com/betagouv/jeveuxaider-back/issues/189)
- **Désinscription Structures :** Implémentation de la fonctionnalité permettant aux structures de se désinscrire de manière autonome. [#172](https://github.com/betagouv/jeveuxaider-back/issues/172)
- **Filtres Marketplace :** Correction d'un filtre temporaire pour les adultes dans le Marketplace. [#199](https://github.com/betagouv/jeveuxaider-back/issues/199)
- **Recherche :** Utilisation de l'opérateur `ilike` pour une recherche moins stricte. [#106](https://github.com/betagouv/jeveuxaider-back/issues/106)

### Évolutions techniques
- **Performances :** Ajout d'index et de paramètres d'autovacuum pour la table de l'historique d'activité afin d'améliorer les performances. [#188](https://github.com/betagouv/jeveuxaider-back/issues/188)
- **Optimisation des requêtes :** Optimisation et refactoring des requêtes liées aux statistiques de modération pour une meilleure efficacité et lisibilité. [#184](https://github.com/betagouv/jeveuxaider-back/issues/184)
- **Index Partiels :** Ajout d'un index partiel pour améliorer les performances des requêtes sur les statistiques. [#186](https://github.com/betagouv/jeveuxaider-back/issues/186)
- **Refactoring :** Suppression de la fonctionnalité de partage de missions et des notifications associées. [#200](https://github.com/betagouv/jeveuxaider-back/issues/200)
- **Refactoring :** Suppression du code lié à `actingAs` et refactorisation de la gestion de l'état de participation. [#191](https://github.com/betagouv/jeveuxaider-back/issues/191)
- **Rolables :** Refonte de la gestion des `rolables.fonction`. [#194](https://github.com/betagouv/jeveuxaider-back/issues/194)
- **Airtable Sync :** Amélioration de la logique de synchronisation des missions depuis Airtable pour exclure les missions non pertinentes. [#190](https://github.com/betagouv/jeveuxaider-back/issues/190)

### Autres changements
- Suppression d'un filtre de département inutilisé dans les invitations. [#185](https://github.com/betagouv/jeveuxaider-back/issues/185)
