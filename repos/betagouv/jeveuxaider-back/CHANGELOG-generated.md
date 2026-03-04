## Changelog : jeveuxaider-back (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au backend de la plateforme "Je veux aider" au cours des 30 derniers jours. Les évolutions concernent principalement l'amélioration de la recherche de missions et de structures, la gestion des notifications, l'ajout de fonctionnalités pour la gestion des témoignages, et des optimisations techniques pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- Amélioration de la recherche de missions et de structures pour une meilleure pertinence. [#135](https://github.com/betagouv/jeveuxaider-back/issues/135)
- Ajout de la possibilité de mettre à jour le statut de participation aux missions via l'API. [#134](https://github.com/betagouv/jeveuxaider-back/issues/134)
- Mise à jour du sujet et du contenu des notifications pour les territoires en attente de validation.
- Possibilité de filtrer les missions par département et région en utilisant des tableaux de valeurs.
- Ajout d'une fonctionnalité pour examiner les témoignages. [#130](https://github.com/betagouv/jeveuxaider-back/issues/130)
- Ajout d'un champ `is_open_to_minors` aux missions et logique associée. [#123](https://github.com/betagouv/jeveuxaider-back/issues/123)
- Amélioration des notifications Slack avec des composants Block Kit pour une présentation plus structurée. [#126](https://github.com/betagouv/jeveuxaider-back/issues/126)
- Correction de l'écoute des messages de notification pour assurer leur bon fonctionnement. [#127](https://github.com/betagouv/jeveuxaider-back/issues/127)
- Ajout d'une commande pour supprimer un témoignage par son ID. [#132](https://github.com/betagouv/jeveuxaider-back/issues/132)
- Amélioration des statistiques des bénévoles dans les modèles d'emails de rappel. [#90675fd](https://github.com/betagouv/jeveuxaider-back/commit/90675fd)

### Évolutions techniques
- Mise à jour de Laravel Passport vers la version 13 et des dépendances associées. [#133](https://github.com/betagouv/jeveuxaider-back/issues/133)
- Refactorisation de la logique de recherche pour utiliser le scope `canBeSearchable`. [#135](https://github.com/betagouv/jeveuxaider-back/issues/135)
- Refactorisation des notifications Slack avec l'introduction d'un trait `HasSlackNotification`. [#125](https://github.com/betagouv/jeveuxaider-back/issues/125)
- Optimisation de la méthode `overviewPlaces` dans le contrôleur `NumbersController` et nettoyage du code inutilisé. [#1d1f9b0](https://github.com/betagouv/jeveuxaider-back/commit/1d1f9b0)
- Amélioration de la gestion des valeurs nulles dans les statistiques et ajustement du paramètre de taille pour les statistiques de trafic. [#1d800ab](https://github.com/betagouv/jeveuxaider-back/commit/1d800ab)
- Mise à jour des routes des statistiques pour refléter les nouvelles méthodes d'évolution et marquage des anciennes routes pour suppression. [#81ae41a](https://github.com/betagouv/jeveuxaider-back/commit/81ae41a)
- Correction de filtres de chaînes de caractères par des filtres exacts dans `ActivityLogController`. [#124](https://github.com/betagouv/jeveuxaider-back/issues/124)
- Refactorisation de la méthode `overviewPlaces` dans `StatisticsPublicController` pour plus de clarté et d'efficacité. [#d14ffd3](https://github.com/betagouv/jeveuxaider-back/commit/d14ffd3)
- Amélioration de la gestion des dates et refactorisation des requêtes de missions dans `StatisticsPublicController`. [#a2f5b53](https://github.com/betagouv/jeveuxaider-back/commit/a2f5b53)
- Suppression de relations inutiles dans `MissionController`. [#122](https://github.com/betagouv/jeveuxaider-back/issues/122)
- Mise à jour des versions de Laravel. [#129](https://github.com/betagouv/jeveuxaider-back/issues/129)
- Correction du filtre d'état pour les requêtes de participation dans `UserController`. [#d6a241a](https://github.com/betagouv/jeveuxaider-back/commit/d6a241a)
- Refactorisation pour réduire la durée du filtre de mission envoyée et correction du nom de variable. [#a050316](https://github.com/betagouv/jeveuxaider-back/commit/a050316)

### Autres changements
- Mise à jour de la dépendance `psy/psysh` de la version 0.12.18 à la version 0.12.19. [#121](https://github.com/betagouv/jeveuxaider-back/issues/121)
- Modification de l'adresse email du destinataire des notifications du réseau de Nivine à Augusta. [#13cb691](https://github.com/betagouv/jeveuxaider-back/commit/13cb691)
- Ajout d'une fonctionnalité pour redémarrer le scheduler de l'application frontale. [#128](https://github.com/betagouv/jeveuxaider-back/issues/128)
- Modification du canal Slack pour les événements `UserHasExportedDatas` et `UserHasImportedDatas`. [#9670102](https://github.com/betagouv/jeveuxaider-back/commit/9670102)
- Commentaires sur les affectations de canaux Slack dans plusieurs classes de notifications. [#4b96c15](https://github.com/betagouv/jeveuxaider-back/commit/4b96c15) et [#f477479](https://github.com/betagouv/jeveuxaider-back/commit/f477479)
- Commentaires sur les méthodes inutilisées et mise à jour de la logique de notification dans `EngagementController` et `MarketplaceMissionController`. [#e38d76b](https://github.com/betagouv/jeveuxaider-back/commit/e38d76b)
