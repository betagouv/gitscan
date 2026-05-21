## Changelog : jeveuxaider-back (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances, notamment au niveau des requêtes statistiques et des logs d'activité, ainsi que sur la synchronisation des données avec Airtable. Des fonctionnalités ont également été ajoutées pour faciliter la gestion des missions, notamment pour celles concernant les mineurs, et pour améliorer l'expérience utilisateur en permettant la désinscription autonome des structures aux notifications.

### Évolutions fonctionnelles
- Possibilité pour les structures de se désinscrire de manière autonome aux notifications. [#172](https://github.com/betagouv/jeveuxaider-back/issues/172)
- Ajout d'un bandeau d'e-mail pour le destinataire dans les notifications. [#189](https://github.com/betagouv/jeveuxaider-back/issues/189)
- Ajout d'un filtre pour exclure les entrées propres à l'utilisateur dans les notes. [#180](https://github.com/betagouv/jeveuxaider-back/issues/180)
- Ajout de champs supplémentaires dans les exports de données. [#179](https://github.com/betagouv/jeveuxaider-back/issues/179)
- Amélioration de la gestion des missions et structures supprimées dans Airtable, notamment pour celles en statut "Brouillon".
- Ajout d'une commande pour fermer les missions destinées aux mineurs à partir de modèles fermés. [#174](https://github.com/betagouv/jeveuxaider-back/issues/174)
- Prévention de l'ouverture en double de missions pour mineurs basées sur les paramètres du modèle. [#173](https://github.com/betagouv/jeveuxaider-back/issues/173)
- Mise à jour du message de bienvenue dans la notification "StructureAssociationValidated".

### Évolutions techniques
- Optimisation des requêtes statistiques en mettant à jour les jointures et les conditions pour les rôles. [#182](https://github.com/betagouv/jeveuxaider-back/issues/182)
- Ajout d'index partiels aux tables `activity_log` et `participations` pour améliorer les performances. [#175](https://github.com/betagouv/jeveuxaider-back/issues/175)
- Ajout d'index et de paramètres d'autovacuum pour le log d'activité afin d'améliorer les performances. [#188](https://github.com/betagouv/jeveuxaider-back/issues/188)
- Optimisation et refactorisation des requêtes de modération des statistiques pour une meilleure efficacité et lisibilité. [#184](https://github.com/betagouv/jeveuxaider-back/issues/184)
- Ajout d'un index partiel pour améliorer les performances des requêtes sur les statistiques. [#186](https://github.com/betagouv/jeveuxaider-back/issues/186)
- Utilisation de l'opérateur `ilike` au lieu de la recherche exacte. [#106](https://github.com/betagouv/jeveuxaider-back/issues/106)
- Amélioration de la logique de synchronisation des missions depuis Airtable pour exclure les missions non pertinentes. [#190](https://github.com/betagouv/jeveuxaider-back/issues/190)
- Mise à jour de la synchronisation des missions depuis Airtable pour inclure les missions supprimées en douceur. [#192](https://github.com/betagouv/jeveuxaider-back/issues/192)
- Suppression du filtre de département inutilisé de la requête d'invitation.

### Autres changements
- Commentaires sur l'utilisation de `UseReplicaDBConnection` dans `StatisticsPublicController`.
- Mise à jour de la documentation.
