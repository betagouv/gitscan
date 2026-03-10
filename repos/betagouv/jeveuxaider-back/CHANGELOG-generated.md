## Changelog : jeveuxaider-back (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au backend de la plateforme "Je veux aider" au cours des 30 derniers jours. Les modifications incluent des améliorations de la recherche, des corrections de bugs, des mises à jour de sécurité et de nouvelles fonctionnalités pour la gestion des témoignages et des statistiques. L'objectif principal est d'améliorer la performance, la fiabilité et la fonctionnalité de la plateforme pour les agents de l'administration.

### Évolutions fonctionnelles
- Ajout des départements d'outre-mer (DOM-TOM) à la recherche de missions et de structures [#138](https://github.com/betagouv/jeveuxaider-back/issues/138).
- Possibilité de supprimer un témoignage par son ID via une nouvelle commande dédiée [#132](https://github.com/betagouv/jeveuxaider-back/issues/132).
- Nouvelle fonctionnalité permettant de revoir les témoignages [#130](https://github.com/betagouv/jeveuxaider-back/issues/130).
- Ajout d'un champ `is_open_to_minors` et de la logique correspondante dans les templates de missions [#123](https://github.com/betagouv/jeveuxaider-back/issues/123).
- Amélioration des notifications : mise à jour du sujet et du contenu de la notification `TerritoireWaitingValidation`.
- Mise à jour des statistiques des bénévoles dans le deuxième modèle d'email de rappel.
- Amélioration du statut de participation via l'API Engagement [#134](https://github.com/betagouv/jeveuxaider-back/issues/134).

### Évolutions techniques
- Refactorisation de la logique de filtrage des départements dans `NumbersController` pour améliorer la clarté et la performance [#82fe4fe](https://github.com/betagouv/jeveuxaider-back/commit/82fe4fe).
- Refactorisation de la logique de recherche pour les missions et les structures afin d'utiliser le scope `canBeSearchable` [#135](https://github.com/betagouv/jeveuxaider-back/issues/135).
- Mise à jour de Laravel Passport vers la version 13 et des dépendances associées [#133](https://github.com/betagouv/jeveuxaider-back/issues/133).
- Mise à jour des versions de Laravel [#129](https://github.com/betagouv/jeveuxaider-back/issues/129).
- Refactorisation des notifications Slack : introduction du trait `HasSlackNotification` [#125](https://github.com/betagouv/jeveuxaider-back/issues/125).
- Optimisation de la méthode `overviewPlaces` et nettoyage du code inutilisé dans `NumbersController` [#1d1f9b0](https://github.com/betagouv/jeveuxaider-back/commit/1d1f9b0).
- Correction de la gestion des valeurs nulles dans les statistiques et ajustement du paramètre de taille pour les statistiques de trafic [#1d800ab](https://github.com/betagouv/jeveuxaider-back/commit/1d800ab).
- Mise à jour des routes de statistiques pour refléter les nouvelles méthodes d'évolution et marquage des anciennes routes pour suppression [#81ae41a](https://github.com/betagouv/jeveuxaider-back/commit/81ae41a).
- Correction de l'écouteur de messages mail avec `canBeNotified` [#127](https://github.com/betagouv/jeveuxaider-back/issues/127).
- Mise à jour des notifications Slack avec des composants Block Kit [#126](https://github.com/betagouv/jeveuxaider-back/issues/126).
- Refactorisation de `registerMediaConversions` pour autoriser un paramètre `Media` nullable [#bfd6333](https://github.com/betagouv/jeveuxaider-back/commit/bfd6333).

### Autres changements
- Correction de l'adresse email du destinataire des notifications dans `ReseauController` (passage de Nivine à Augusta) [#13cb691](https://github.com/betagouv/jeveuxaider-back/commit/13cb691).
- Mise à jour du canal Slack pour les événements `UserHasExportedDatas` et `UserHasImportedDatas` vers `#produit-logs` [#9670102](https://github.com/betagouv/jeveuxaider-back/commit/9670102).
- Suppression de l'assignation du canal Slack dans plusieurs classes de notifications et commentaires dans d'autres [#4b96c15](https://github.com/betagouv/jeveuxaider-back/commit/4b96c15), [#f477479](https://github.com/betagouv/jeveuxaider-back/commit/f477479), [#e38d76b](https://github.com/betagouv/jeveuxaider-back/commit/e38d76b).
- Suppression de méthodes inutilisées et mise à jour de la logique de notification dans `EngagementController` et `MarketplaceMissionController` [#e38d76b](https://github.com/betagouv/jeveuxaider-back/commit/e38d76b).
- Ajout d'un template QA mineur [#49a57c7](https://github.com/betagouv/jeveuxaider-back/commit/49a57c7).
- Redémarrage de l'application front via une fonctionnalité dédiée [#128](https://github.com/betagouv/jeveuxaider-back/issues/128).
