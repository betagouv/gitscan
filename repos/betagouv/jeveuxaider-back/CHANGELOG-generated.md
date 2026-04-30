## Changelog : jeveuxaider-back (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances et de la gestion des missions, notamment celles destinées aux mineurs. Des corrections ont également été apportées pour assurer la cohérence des données et améliorer l'expérience utilisateur, en particulier concernant les notifications et l'acceptation des invitations.

### Évolutions fonctionnelles
- Ajout d'une pagination simple pour les journaux d'activité, facilitant leur consultation. [#176](https://github.com/betagouv/jeveuxaider-back/pull/176)
- Amélioration de la gestion des missions et des structures provenant d'Airtable, en gérant correctement leur suppression lorsqu'elles sont en statut "Brouillon".
- Ajout d'une commande pour fermer les missions destinées aux mineurs à partir de modèles fermés. [#174](https://github.com/betagouv/jeveuxaider-back/pull/174)
- Correction d'un problème empêchant l'ouverture de missions dupliquées pour les mineurs, en se basant sur les paramètres du modèle. [#173](https://github.com/betagouv/jeveuxaider-back/pull/173)
- Amélioration du message de bienvenue dans la notification "Association à une structure validée". [#201](https://github.com/betagouv/jeveuxaider-back/pull/201)
- Correction d'un bug lié au numéro de téléphone et au code postal manquants lors de la création d'un utilisateur. [#171](https://github.com/betagouv/jeveuxaider-back/pull/171)
- Amélioration de la gestion des erreurs lors de l'acceptation d'une invitation. [#170](https://github.com/betagouv/jeveuxaider-back/pull/170)
- Ajout de la configuration "reply-to" pour les notifications par email, permettant de personnaliser l'adresse de réponse. [#162](https://github.com/betagouv/jeveuxaider-back/pull/162)

### Évolutions techniques
- Ajout d'index partiels sur les tables `activity_log` et `participations` pour optimiser les performances. [#175](https://github.com/betagouv/jeveuxaider-back/pull/175)
- Utilisation de la réplication de base de données pour améliorer les performances et la disponibilité. [#164](https://github.com/betagouv/jeveuxaider-back/pull/164)
- Ajout d'un index sur les colonnes `created_at` et `conversation_id` de la table `messages` pour optimiser les requêtes. [#165](https://github.com/betagouv/jeveuxaider-back/pull/165)
- Suppression de paramètres et de méthodes inutilisés du contrôleur `GoalsJVAController` pour simplifier le code. [#163](https://github.com/betagouv/jeveuxaider-back/pull/163)
- Refactorisation du code pour supprimer les missions passées de la tâche `ApiEngagementExportMissionsJob`. [#168](https://github.com/betagouv/jeveuxaider-back/pull/168)
- Suppression de l'utilisation de `UseReplicaDBConnection` dans le contrôleur `StatisticsPublicController`. [#168](https://github.com/betagouv/jeveuxaider-back/pull/168)

### Autres changements
- Ajout d'une classe de test `TestNotification` pour tester la fonctionnalité "reply-to". [#160](https://github.com/betagouv/jeveuxaider-back/pull/160)
- Correction des noms d'activités manquants dans le mappage des activités de mission. [#168](https://github.com/betagouv/jeveuxaider-back/pull/168)
- Intégration des évolutions France Travail. [#166](https://github.com/betagouv/jeveuxaider-back/pull/166)
- Mise à jour de la librairie `laravel/passport` vers la version 13.7.1. [#167](https://github.com/betagouv/jeveuxaider-back/pull/167)
- Mise à jour de la librairie `phpoffice/phpspreadsheet` vers la version 1.30.4. [#177](https://github.com/betagouv/jeveuxaider-back/pull/177)
- Mise à jour de la librairie `phpseclib/phpseclib` vers la version 3.0.51. [#169](https://github.com/betagouv/jeveuxaider-back/pull/169)
