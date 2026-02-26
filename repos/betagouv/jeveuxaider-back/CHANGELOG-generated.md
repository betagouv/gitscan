## Changelog : jeveuxaider-back (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées au backend de la plateforme "Je veux aider" au cours des 30 derniers jours. Les modifications incluent des améliorations de la gestion des missions et des statistiques, des corrections de bugs et des optimisations de performance. De nouvelles fonctionnalités ont également été ajoutées, comme la possibilité de modérer les témoignages et de redémarrer le scheduler de l'application frontale.

### Évolutions fonctionnelles
- Ajout de la possibilité de modérer les témoignages (#130).
- Ajout d'une commande pour supprimer un témoignage par son ID (#132).
- Amélioration des filtres pour prendre en charge les valeurs de tableau pour les départements et les régions.
- Ajout du champ `is_open_to_minors` et de la logique correspondante dans les templates de missions (#123).
- Possibilité de redémarrer le scheduler de l'application frontale (#128).
- Ajout de statistiques sur les volontaires dans le deuxième modèle d'email de rappel.
- Correction du message de l'écouteur d'emails pour fonctionner avec `canBeNotified` (#127).
- Amélioration des notifications Slack avec des composants Block Kit (#126).

### Évolutions techniques
- Mise à jour de Laravel Passport vers la version 13 et des dépendances associées (#133).
- Mise à jour des versions de Laravel (#129).
- Refactorisation des méthodes `registerMediaConversions` pour autoriser un paramètre Media nullable.
- Refactorisation des classes `UserHasExportedDatas` et `UserHasImportedDatas` pour mettre à jour le canal Slack vers `#produit-logs`.
- Refactorisation des notifications Slack avec l'introduction d'un Trait `HasSlackNotification` (#125).
- Optimisation de la méthode `overviewPlaces` dans `NumbersController` et nettoyage du code inutilisé.
- Correction de la gestion des valeurs nulles dans les statistiques et ajustement du paramètre de taille pour les statistiques de trafic.
- Mise à jour des routes de statistiques pour refléter les nouvelles méthodes d'évolution et marquage des anciennes routes pour suppression.
- Correction de l'email du destinataire de la notification dans `ReseauController`.
- Suppression des relations inutiles dans `MissionController` (#122).
- Correction des filtres de chaînes par des filtres exacts dans `ActivityLogController` (#124).
- Refactorisation de `StatisticsPublicController` pour améliorer la clarté et l'efficacité.

### Autres changements
- Mise à jour de PHPUnit et de ses dépendances (#120).
- Correction du filtre d'état pour correspondre exactement aux requêtes de participation.
- Correction de la durée du filtre de mission envoyée et correction du nom de la variable.
- Suppression de méthodes inutilisées et mise à jour de la logique de notification dans `EngagementController` et `MarketplaceMissionController`.
- Commentaires dans plusieurs classes de notifications pour désactiver l'affectation du canal Slack.
- Correction d'un bug dans `MissionRecommendation` concernant la durée du filtre des missions envoyées.
- Bump de la dépendance `psy/psysh` de 0.12.18 à 0.12.19 (#121).
