## Changelog : jeveuxaider-back (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances et de la gestion des missions, notamment celles liées aux mineurs et aux évolutions France Travail. Des corrections ont également été apportées pour améliorer la robustesse de l'application et l'expérience utilisateur, en particulier concernant la gestion des invitations et des notifications.

### Évolutions fonctionnelles
- Ajout de champs supplémentaires dans les exports de données. [#179](https://github.com/betagouv/jeveuxaider-back/pull/179)
- Implémentation d'une pagination simple pour les journaux d'activité, améliorant la navigation et la performance. [#176](https://github.com/betagouv/jeveuxaider-back/pull/176)
- Ajout d'une commande pour fermer les missions pour mineurs à partir de modèles fermés. [#174](https://github.com/betagouv/jeveuxaider-back/pull/174)
- Correction d'un problème empêchant l'ouverture de missions dupliquées pour mineurs basées sur les paramètres du modèle. [#173](https://github.com/betagouv/jeveuxaider-back/pull/173)
- Amélioration du message de bienvenue dans la notification "StructureAssociationValidated". [#171](https://github.com/betagouv/jeveuxaider-back/pull/171)
- Gestion des erreurs lors de l'acceptation d'une invitation. [#170](https://github.com/betagouv/jeveuxaider-back/pull/170)
- Correction de la gestion de la suppression de missions et structures depuis Airtable, notamment celles en état "Brouillon".
- Évolutions liées à France Travail. [#166](https://github.com/betagouv/jeveuxaider-back/pull/166)

### Évolutions techniques
- Ajout d'index partiels aux tables `activity_log` et `participations` pour optimiser les performances des requêtes. [#175](https://github.com/betagouv/jeveuxaider-back/pull/175)
- Utilisation de la base de données réplica pour certaines requêtes, améliorant la performance et la scalabilité. [#164](https://github.com/betagouv/jeveuxaider-back/pull/164)
- Suppression des missions passées du job d'export des engagements. [#169](https://github.com/betagouv/jeveuxaider-back/pull/169)
- Ajout d'un index sur les colonnes `created_at` et `conversation_id` de la table `messages` pour optimiser les requêtes. [#165](https://github.com/betagouv/jeveuxaider-back/pull/165)
- Suppression de paramètres et méthodes inutilisés dans le contrôleur `GoalsJVAController`. [#163](https://github.com/betagouv/jeveuxaider-back/pull/163)
- Suppression de l'utilisation de `UseReplicaDBConnection` dans `StatisticsPublicController`.

### Autres changements
- Correction de la correspondance des noms d'activité dans les missions. [#168](https://github.com/betagouv/jeveuxaider-back/pull/168)
- Mise à jour de la librairie `laravel/passport` vers la version 13.7.1. [#167](https://github.com/betagouv/jeveuxaider-back/pull/167)
- Mise à jour de la librairie `phpoffice/phpspreadsheet` vers la version 1.30.4. [#177](https://github.com/betagouv/jeveuxaider-back/pull/177)
- Mise à jour de la librairie `phpseclib/phpseclib` vers la version 3.0.51. [#169](https://github.com/betagouv/jeveuxaider-back/pull/169)
