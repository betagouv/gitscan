## Changelog : jeveuxaider-back (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la performance et de la fiabilité de la plateforme, notamment au niveau de la gestion des logs d'activité et des notifications. Des ajustements ont également été apportés pour mieux supporter les missions pour les mineurs et les besoins spécifiques de France Travail. Enfin, des améliorations ont été apportées à la configuration des notifications par email.

### Évolutions fonctionnelles
- **Missions pour mineurs :** Amélioration du script de gestion des missions pour les mineurs, incluant une fermeture automatique des missions. [#157](https://github.com/betagouv/jeveuxaider-back/issues/157) et [#146](https://github.com/betagouv/jeveuxaider-back/issues/146)
- **Statistiques PPG :** Ajout de statistiques pour les référents PPG (Plateforme de Partage de Gares). [#137](https://github.com/betagouv/jeveuxaider-back/issues/137)
- **Notifications par email :** Ajout de la configuration "reply-to" pour les notifications par email, permettant de définir une adresse de réponse spécifique. [#162](https://github.com/betagouv/jeveuxaider-back/issues/162), [#161](https://github.com/betagouv/jeveuxaider-back/issues/161) et [#160](https://github.com/betagouv/jeveuxaider-back/issues/160)
- **Modèles de missions :** Ajout de notifications par email lors de la mise à jour des modèles de missions. [#149](https://github.com/betagouv/jeveuxaider-back/issues/149)
- **France Travail :** Intégration d'évolutions spécifiques pour France Travail. [#166](https://github.com/betagouv/jeveuxaider-back/issues/166)

### Évolutions techniques
- **Base de données :** Ajout d'une réplique de base de données pour améliorer la disponibilité et la performance. [#164](https://github.com/betagouv/jeveuxaider-back/issues/164)
- **Performance - Logs d'activité :** Optimisation significative du processus de backfill des logs d'activité, incluant l'ajout de colonnes `old_state` et `new_state`, l'utilisation de CTE (Common Table Expression) et de pagination par plages, et l'ajout d'index temporaires. [#154](https://github.com/betagouv/jeveuxaider-back/issues/154), [#153](https://github.com/betagouv/jeveuxaider-back/issues/153), [#152](https://github.com/betagouv/jeveuxaider-back/issues/152), [#151](https://github.com/betagouv/jeveuxaider-back/issues/151), [#150](https://github.com/betagouv/jeveuxaider-back/issues/150)
- **Performance - Messages :** Ajout d'index sur les colonnes `created_at` et `conversation_id` de la table `messages` pour améliorer la performance des requêtes. [#165](https://github.com/betagouv/jeveuxaider-back/issues/165)
- **Refactoring :** Suppression de paramètres et de méthodes inutilisés dans le contrôleur `GoalsJVAController`. [#163](https://github.com/betagouv/jeveuxaider-back/issues/163)
- **Sécurité :** Désactivation du "device code grant" dans la configuration de Passport pour renforcer la sécurité. [#156](https://github.com/betagouv/jeveuxaider-back/issues/156)
- **Suppression de dépendance :** Suppression de la dépendance MistralAI et des routes associées. [#159](https://github.com/betagouv/jeveuxaider-back/issues/159)

### Autres changements
- Suppression des missions passées de la tâche `ApiEngagementExportMissionsJob`. [#169](https://github.com/betagouv/jeveuxaider-back/issues/169)
- Correction de l'absence de noms d'activité dans le mapping des activités de mission. [#168](https://github.com/betagouv/jeveuxaider-back/issues/168)
