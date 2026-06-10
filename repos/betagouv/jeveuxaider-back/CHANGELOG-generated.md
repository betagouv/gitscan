## Changelog : jeveuxaider-back (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la robustesse de la plateforme, notamment au niveau de la synchronisation des données avec Airtable, de la gestion des missions et des statistiques. Des améliorations ont également été apportées à l'expérience des structures, avec notamment la possibilité de se désinscrire de manière autonome.

### Évolutions fonctionnelles
- Les structures peuvent maintenant se désinscrire de manière autonome [#172](https://github.com/betagouv/jeveuxaider-back/issues/172).
- Amélioration de la synchronisation des missions depuis Airtable :
    - Prise en compte des missions supprimées (soft-deleted) [#192](https://github.com/betagouv/jeveuxaider-back/issues/192).
    - Exclusion des missions non pertinentes en fonction de leur état et de leurs notes [#190](https://github.com/betagouv/jeveuxaider-back/issues/190).
    - Possibilité de synchroniser une seule fois les missions supprimées.
- Ajout d'une bannière d'email pour les destinataires des notifications [#189](https://github.com/betagouv/jeveuxaider-back/issues/189).
- Possibilité de filtrer les organisations par ID lors de la synchronisation Airtable [#200](https://github.com/betagouv/jeveuxaider-back/issues/200).
- Amélioration du filtre "adultes uniquement" dans le marketplace inversé [#199](https://github.com/betagouv/jeveuxaider-back/issues/199).
- Ajout d'une commande pour ajouter un utilisateur aux conversations [#193](https://github.com/betagouv/jeveuxaider-back/issues/193).
- Amélioration de la gestion de l'état de participation.

### Évolutions techniques
- Optimisation des requêtes de statistiques et de modération :
    - Ajout d'index partiels pour améliorer les performances [#186](https://github.com/betagouv/jeveuxaider-back/issues/186).
    - Refactoring et optimisation des requêtes [#184](https://github.com/betagouv/jeveuxaider-back/issues/184).
    - Ajout de jointures pour améliorer la logique de comptage [#187](https://github.com/betagouv/jeveuxaider-back/issues/187).
- Amélioration des performances de l'activité log avec l'ajout d'index et de paramètres d'autovacuum [#188](https://github.com/betagouv/jeveuxaider-back/issues/188).
- Refactoring de la logique de validation de l'état des structures pour exclure l'état "Désinscrite".
- Suppression de la fonctionnalité de partage de missions et des notifications associées [#200](https://github.com/betagouv/jeveuxaider-back/issues/200).
- Utilisation de l'opérateur `ilike` pour les recherches non sensibles à la casse [#106](https://github.com/betagouv/jeveuxaider-back/issues/106).
- Refactoring du code pour supprimer un filtre de département inutilisé dans les invitations.

### Autres changements
- Mise à jour de la documentation README pour refléter le rebranding du projet.
- Amélioration du formatage et de la lisibilité du template d'email de résumé des responsables.
- Revamp des "rolables.fonction".
- Mises à jour de dépendances Symfony (routing, http-kernel, mailer, mime).
