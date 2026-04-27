## Changelog : jeveuxaider-back (30 derniers jours, au 25 avril 2026)

### Résumé
Ce changelog présente les améliorations apportées au backend de la plateforme "Je veux aider" au cours des 30 derniers jours. Les évolutions concernent principalement la gestion des missions, des notifications et l'infrastructure, avec un focus sur l'amélioration de la performance et la correction de bugs. Des ajustements ont également été faits pour supporter les évolutions France Travail et les statistiques pour les référents PPG.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la récupération du numéro de téléphone et du code postal de l'utilisateur [#171](https://github.com/betagouv/jeveuxaider-back/issues/171).
- Amélioration de la gestion des erreurs lors de l'acceptation d'une invitation [#170](https://github.com/betagouv/jeveuxaider-back/issues/170).
- Mise à jour du message de bienvenue dans la notification "StructureAssociationValidated".
- Ajout de la configuration "reply-to" pour les notifications par email, permettant de personnaliser l'adresse de réponse.
- Amélioration de l'implémentation de "reply-to" dans la classe `TestNotification` pour utiliser la classe `Address`.
- Ajout d'une classe `TestNotification` pour tester la fonctionnalité "reply-to".
- Prise en compte des ajustements pour les missions concernant les mineurs [#146](https://github.com/betagouv/jeveuxaider-back/issues/146).
- Implémentation des statistiques PPG pour les référents [#137](https://github.com/betagouv/jeveuxaider-back/issues/137).
- Ajout d'un script pour fermer automatiquement les missions concernant les mineurs [#157](https://github.com/betagouv/jeveuxaider-back/issues/157).

### Évolutions techniques
- Utilisation de la base de données réplica pour améliorer les performances, notamment dans le contrôleur `StatisticsPublicController` [#164](https://github.com/betagouv/jeveuxaider-back/issues/164).
- Ajout d'un index sur les colonnes `created_at` et `conversation_id` de la table `messages` pour optimiser les requêtes [#165](https://github.com/betagouv/jeveuxaider-back/issues/165).
- Suppression de paramètres et de méthodes inutilisés du contrôleur `GoalsJVAController` [#163](https://github.com/betagouv/jeveuxaider-back/issues/163).
- Suppression de la dépendance MistralAI et des routes associées du contrôleur `AIController` [#159](https://github.com/betagouv/jeveuxaider-back/issues/159).
- Mise à jour de la librairie Laravel Passport vers la version 13.7.1 [#167](https://github.com/betagouv/jeveuxaider-back/issues/167).
- Mise à jour de la librairie phpseclib/phpseclib vers la version 3.0.51 [#169](https://github.com/betagouv/jeveuxaider-back/issues/169).
- Mise à jour de la librairie aws/aws-sdk-php vers la version 3.374.2 [#158](https://github.com/betagouv/jeveuxaider-back/issues/158).

### Autres changements
- Suppression des missions passées de la tâche `ApiEngagementExportMissionsJob`.
- Commentaires sur l'utilisation de `UseReplicaDBConnection` dans `StatisticsPublicController`.
- Corrections mineures et refactoring du code.
