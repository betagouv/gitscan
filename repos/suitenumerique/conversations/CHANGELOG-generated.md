## Changelog : conversations (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'expérience utilisateur, notamment la possibilité d'éditer directement les documents depuis l'interface, une nouvelle illustration pour les pages d'erreur 404 et une gestion améliorée de l'indexation des fichiers. Des optimisations techniques ont également été réalisées pour améliorer la performance et la robustesse de l'application.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité "Modifier dans les Docs" permettant d'éditer un document directement depuis l'interface. [#1a19225](https://github.com/suitenumerique/conversations/commit/1a19225)
- Nouvelle illustration pour les pages d'erreur 404. [#2579a14](https://github.com/suitenumerique/conversations/commit/2579a14)
- L'interface utilisateur accepte désormais les utilisateurs sans nom complet renseigné. [#08127a3](https://github.com/suitenumerique/conversations/commit/08127a3)
- Utilisation de "L'Assistant" comme nom de produit par défaut. [#9199cfc](https://github.com/suitenumerique/conversations/commit/9199cfc)
- Affichage d'un message d'erreur spécifique en cas d'échec de l'analyse d'un document. [#2ffffae](https://github.com/suitenumerique/conversations/commit/2ffffae)

### Évolutions techniques
- Mise en place de Celery pour l'exécution de tâches asynchrones, améliorant la réactivité de l'application. [#9abe4b9](https://github.com/suitenumerique/conversations/commit/9abe4b9)
- Amélioration de la gestion de l'indexation des fichiers, avec un traitement asynchrone et une gestion des erreurs 404 lors de la suppression. [#059ac93](https://github.com/suitenumerique/conversations/commit/059ac93), [#4263e9a](https://github.com/suitenumerique/conversations/commit/4263e9a)
- Refactorisation du module de vues de chat et utilisation de constantes partagées pour une meilleure maintenabilité. [#0c06446](https://github.com/suitenumerique/conversations/commit/0c06446)
- Mise à jour de la version de Python et des dépendances. [#df4c0ae](https://github.com/suitenumerique/conversations/commit/df4c0ae)
- Nettoyage et simplification de la configuration des tests. [#7a9b58b](https://github.com/suitenumerique/conversations/commit/7a9b58b), [#1466e32](https://github.com/suitenumerique/conversations/commit/1466e32)
- Ajout d'un mécanisme de repli (fallback) pour les modèles. [#b57d758](https://github.com/suitenumerique/conversations/commit/b57d758)

### Autres changements
- Mise à jour des chaînes de caractères traduites. [#bd8c532](https://github.com/suitenumerique/conversations/commit/bd8c532)
- Mise à jour des logos et des icônes. [#ea17208](https://github.com/suitenumerique/conversations/commit/ea17208)
- Correction de liens et de cibles. [#9dd4cb7](https://github.com/suitenumerique/conversations/commit/9dd4cb7)
- Mise à jour des dépendances frontales et de messagerie. [#68dd00b](https://github.com/suitenumerique/conversations/commit/68dd00b)
- Modification de la couleur d'avertissement pour les bannières. [#b33481a](https://github.com/suitenumerique/conversations/commit/b33481a)
- Amélioration du style des icônes de statut. [#2e5c5f5](https://github.com/suitenumerique/conversations/commit/2e5c5f5)
