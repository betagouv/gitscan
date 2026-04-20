## Changelog : jeveuxaider-back (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration des performances et de la robustesse de la plateforme, notamment au niveau de la base de données et des notifications. Des ajustements ont été apportés pour faciliter l'intégration de France Travail et améliorer le suivi des missions pour les mineurs. L'équipe a également travaillé sur l'amélioration du suivi des activités et la correction de bugs.

### Évolutions fonctionnelles
- Amélioration du traitement des invitations et gestion des erreurs lors de l'acceptation [#170](https://github.com/betagouv/jeveuxaider-back/issues/170).
- Intégration d'évolutions spécifiques pour France Travail [#166](https://github.com/betagouv/jeveuxaider-back/issues/166).
- Ajout de notifications par email pour les mises à jour des modèles de missions [#149](https://github.com/betagouv/jeveuxaider-back/issues/149).
- Ajustements pour la gestion des missions pour les mineurs, incluant la fermeture automatique des missions [#146](https://github.com/betagouv/jeveuxaider-back/issues/146) et [#157](https://github.com/betagouv/jeveuxaider-back/issues/157).
- Amélioration des statistiques PPG pour les référents [#137](https://github.com/betagouv/jeveuxaider-back/issues/137).
- Correction de l'affichage des noms d'activités liés aux missions [#168](https://github.com/betagouv/jeveuxaider-back/issues/168).

### Évolutions techniques
- Mise en place d'une base de données réplica pour améliorer la performance et la disponibilité [#164](https://github.com/betagouv/jeveuxaider-back/issues/164).
- Ajout d'index sur les colonnes `created_at` et `conversation_id` de la table `messages` pour optimiser les requêtes [#165](https://github.com/betagouv/jeveuxaider-back/issues/165).
- Refactoring du contrôleur `GoalsJVAController` pour supprimer les paramètres et méthodes inutilisés [#163](https://github.com/betagouv/jeveuxaider-back/issues/163).
- Amélioration de la configuration des notifications email avec l'ajout d'une adresse de réponse (`reply-to`) [#162](https://github.com/betagouv/jeveuxaider-back/issues/162), [#161](https://github.com/betagouv/jeveuxaider-back/issues/161) et [#160](https://github.com/betagouv/jeveuxaider-back/issues/160).
- Optimisation du processus de backfill pour l'historique des activités (activity log) avec l'ajout de colonnes `old_state` et `new_state`, l'utilisation de CTE et de pagination par plages [#150](https://github.com/betagouv/jeveuxaider-back/issues/150), [#151](https://github.com/betagouv/jeveuxaider-back/issues/151), [#152](https://github.com/betagouv/jeveuxaider-back/issues/152), [#153](https://github.com/betagouv/jeveuxaider-back/issues/153), [#154](https://github.com/betagouv/jeveuxaider-back/issues/154) et [#155](https://github.com/betagouv/jeveuxaider-back/issues/155).
- Désactivation du "device code grant" dans la configuration de Passport pour renforcer la sécurité [#156](https://github.com/betagouv/jeveuxaider-back/issues/156).
- Suppression de la dépendance MistralAI et des routes associées [#159](https://github.com/betagouv/jeveuxaider-back/issues/159).

### Autres changements
- Suppression du code lié aux missions terminées de la tâche `ApiEngagementExportMissionsJob`.
- Mise à jour de la documentation et de la configuration.
