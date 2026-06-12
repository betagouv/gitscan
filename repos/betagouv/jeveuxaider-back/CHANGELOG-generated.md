## Changelog : jeveuxaider-back (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la synchronisation des données avec Airtable, l'optimisation des performances des requêtes et l'ajout de fonctionnalités pour les structures, notamment la gestion des inscriptions et la possibilité de se désinscrire de manière autonome. Des améliorations ont également été apportées à la gestion des missions et des notifications.

### Évolutions fonctionnelles
- Les structures peuvent maintenant se désinscrire de manière autonome [#172](https://github.com/betagouv/jeveuxaider-back/issues/172).
- Amélioration de la synchronisation des missions depuis Airtable :
    - Prise en compte des missions supprimées lors de la synchronisation [#192](https://github.com/betagouv/jeveuxaider-back/issues/192).
    - Exclusion des missions non pertinentes lors de la synchronisation [#190](https://github.com/betagouv/jeveuxaider-back/issues/190).
    - Possibilité de synchroniser une seule mission supprimée [#192](https://github.com/betagouv/jeveuxaider-back/issues/192).
- Amélioration du filtrage des organisations dans la synchronisation Airtable pour supporter les IDs [#200](https://github.com/betagouv/jeveuxaider-back/issues/200).
- Ajout d'une bannière d'email pour le destinataire dans les notifications [#189](https://github.com/betagouv/jeveuxaider-back/issues/189).
- Mise à jour des workflows d'inscription des organisations [#193](https://github.com/betagouv/jeveuxaider-back/issues/193).
- Suppression de la fonctionnalité de partage de missions [#200](https://github.com/betagouv/jeveuxaider-back/issues/200).
- Ajout de la possibilité de filtrer les missions pour adultes uniquement dans le marketplace inversé [#199](https://github.com/betagouv/jeveuxaider-back/issues/199).

### Évolutions techniques
- Optimisation des performances des requêtes :
    - Ajout d'index et de paramètres d'autovacuum pour le journal d'activité [#188](https://github.com/betagouv/jeveuxaider-back/issues/188).
    - Ajout d'un index partiel pour améliorer les performances des requêtes statistiques [#186](https://github.com/betagouv/jeveuxaider-back/issues/186).
    - Amélioration de la requête de comptage des modérations [#187](https://github.com/betagouv/jeveuxaider-back/issues/187).
- Refactoring :
    - Renommage des méthodes `getLabel` en `getContextableLabel` pour plus de cohérence [#193](https://github.com/betagouv/jeveuxaider-back/issues/193).
    - Suppression de la logique d'actingAs et refactorisation de la gestion de l'état de participation [#191](https://github.com/betagouv/jeveuxaider-back/issues/191).
    - Utilisation de l'opérateur `ilike` pour les recherches non sensibles à la casse [#106](https://github.com/betagouv/jeveuxaider-back/issues/106).
- Amélioration de la logique de validation de l'état des structures pour exclure 'Désinscrite' [#193](https://github.com/betagouv/jeveuxaider-back/issues/193).
- Mise à jour de la commande `MissionsCloseOutdatedCommand` pour supporter une plage de mois dynamique et ajouter des notifications Slack [#200](https://github.com/betagouv/jeveuxaider-back/issues/200).
- Ajout d'une commande `AddUserToConversations` pour gérer la participation des utilisateurs aux conversations [#193](https://github.com/betagouv/jeveuxaider-back/issues/193).

### Autres changements
- Mise à jour de la documentation README.md pour refléter le rebranding du projet [#200](https://github.com/betagouv/jeveuxaider-back/issues/200).
- Amélioration du formatage et de la lisibilité du modèle d'email de résumé des responsables [#200](https://github.com/betagouv/jeveuxaider-back/issues/200).
- Refonte des `rolables.fonction` [#194](https://github.com/betagouv/jeveuxaider-back/issues/194).
- Suppression d'un filtre temporaire pour les adultes dans la requête de MarketplaceMissionController [#200](https://github.com/betagouv/jeveuxaider-back/issues/200).
