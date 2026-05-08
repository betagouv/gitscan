## Changelog : jeveuxaider-back (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances, notamment au niveau des requêtes statistiques et des logs d'activité. Des corrections ont également été apportées pour améliorer la gestion des missions, en particulier celles liées aux mineurs et à la synchronisation avec Airtable. Enfin, des améliorations ont été apportées à l'export de données et à la gestion des invitations.

### Évolutions fonctionnelles
- Ajout d'un filtre pour exclure les propres entrées de l'utilisateur dans les notes. [#180](https://github.com/betagouv/jeveuxaider-back/issues/180)
- Ajout de champs supplémentaires dans les exports de données. [#179](https://github.com/betagouv/jeveuxaider-back/issues/179)
- Implémentation d'une pagination simple pour les logs d'activité. [#176](https://github.com/betagouv/jeveuxaider-back/issues/176)
- Correction de la gestion de la suppression de missions et de structures en état "Brouillon" depuis Airtable.
- Ajout d'une commande pour fermer les missions pour mineurs à partir de modèles fermés. [#174](https://github.com/betagouv/jeveuxaider-back/issues/174)
- Correction d'un problème empêchant l'ouverture de missions dupliquées pour mineurs en fonction des paramètres du modèle. [#173](https://github.com/betagouv/jeveuxaider-back/issues/173)
- Mise à jour du message de bienvenue dans la notification "StructureAssociationValidated". [#171](https://github.com/betagouv/jeveuxaider-back/issues/171)
- Amélioration de la gestion des erreurs lors de l'acceptation d'une invitation. [#170](https://github.com/betagouv/jeveuxaider-back/issues/170)
- Correction d'un bug lié à l'absence du numéro de téléphone et du code postal de l'utilisateur. [#171](https://github.com/betagouv/jeveuxaider-back/issues/171)

### Évolutions techniques
- Optimisation des requêtes statistiques en mettant à jour les jointures et les conditions pour les éléments modifiables. [#182](https://github.com/betagouv/jeveuxaider-back/issues/182)
- Optimisation des requêtes de modération des statistiques avec de nouveaux index. [#181](https://github.com/betagouv/jeveuxaider-back/issues/181)
- Ajout d'index partiels aux tables `activity_log` et `participations` pour optimiser les performances. [#175](https://github.com/betagouv/jeveuxaider-back/issues/175)
- Refactorisation : suppression des missions passées de `ApiEngagementExportMissionsJob`.
- Refactorisation : suppression de l'utilisation de `UseReplicaDBConnection` dans `StatisticsPublicController`.
- Mise en place d'une base de données réplica pour améliorer les performances. [#164](https://github.com/betagouv/jeveuxaider-back/issues/164)
- Correction des noms d'activité manquants dans le mapping d'activité des missions. [#168](https://github.com/betagouv/jeveuxaider-back/issues/168)
- Évolutions liées à France Travail. [#166](https://github.com/betagouv/jeveuxaider-back/issues/166)
- Mise à jour de Laravel Passport vers la version 13.7.1. [#167](https://github.com/betagouv/jeveuxaider-back/issues/167)

### Autres changements
- Correction de la configuration pour éviter l'ouverture de missions en double pour les mineurs.
- Documentation et nettoyage du code.
