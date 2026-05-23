## Changelog : jeveuxaider-back (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances, notamment au niveau des requêtes statistiques et des logs d'activité, ainsi que sur la synchronisation des données avec Airtable et la gestion des missions, en particulier celles concernant les mineurs. Des améliorations ont également été apportées à la gestion des notifications et à l'autonomie des structures.

### Évolutions fonctionnelles
- Possibilité pour les structures de se désinscrire de manière autonome des notifications. [#172](https://github.com/betagouv/jeveuxaider-back/issues/172)
- Ajout d'un filtre pour exclure les entrées propres à l'utilisateur dans les notes. [#180](https://github.com/betagouv/jeveuxaider-back/issues/180)
- Ajout de champs supplémentaires dans les exports de données. [#179](https://github.com/betagouv/jeveuxaider-back/issues/179)
- Implémentation d'une pagination simple pour les logs d'activité. [#176](https://github.com/betagouv/jeveuxaider-back/issues/176)
- Ajout d'une bannière d'email de destinataire dans les emails de notification. [#189](https://github.com/betagouv/jeveuxaider-back/issues/189)
- Amélioration de la gestion de la synchronisation Airtable : prise en charge du filtrage des organisations par ID et synchronisation des missions supprimées. [#192](https://github.com/betagouv/jeveuxaider-back/issues/192), [#185](https://github.com/betagouv/jeveuxaider-back/issues/185)
- Ajout d'une commande pour fermer les missions pour mineurs à partir de modèles fermés. [#174](https://github.com/betagouv/jeveuxaider-back/issues/174)
- Prévention de l'ouverture de missions en double pour mineurs basée sur les paramètres du modèle. [#173](https://github.com/betagouv/jeveuxaider-back/issues/173)

### Évolutions techniques
- Optimisation des requêtes statistiques en modifiant les jointures et les conditions pour les rôles. [#182](https://github.com/betagouv/jeveuxaider-back/issues/182)
- Ajout d'index partiels aux tables `activity_log` et `participations` pour optimiser les performances. [#175](https://github.com/betagouv/jeveuxaider-back/issues/175), [#188](https://github.com/betagouv/jeveuxaider-back/issues/188)
- Ajout d'index partiel pour améliorer les performances des requêtes statistiques. [#186](https://github.com/betagouv/jeveuxaider-back/issues/186)
- Optimisation et refactorisation des requêtes de modération des statistiques pour plus d'efficacité et de lisibilité. [#184](https://github.com/betagouv/jeveuxaider-back/issues/184)
- Utilisation de l'opérateur `ilike` au lieu de la recherche exacte pour améliorer la flexibilité. [#106](https://github.com/betagouv/jeveuxaider-back/issues/106)
- Refactorisation de la gestion de l'état de participation et suppression de `actingAs`. [#191](https://github.com/betagouv/jeveuxaider-back/issues/191)
- Suppression du filtre de département inutilisé dans la requête d'invitation.
- Amélioration de la logique de synchronisation des missions pour exclure les missions non pertinentes en fonction de leur état et de leurs notes. [#190](https://github.com/betagouv/jeveuxaider-back/issues/190)
- Gestion de la suppression des missions et structures par Airtable dans l'état "Brouillon".

### Autres changements
- Commentaire de l'utilisation de `UseReplicaDBConnection` dans `StatisticsPublicController`.
- Mise à jour de la dépendance `phpseclib/phpseclib` de 3.0.51 à 3.0.52.
- Mise à jour de la dépendance `phpoffice/phpspreadsheet` de 1.30.2 à 1.30.4.
