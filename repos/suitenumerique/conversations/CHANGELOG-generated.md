## Changelog : conversations (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'expérience utilisateur, notamment l'ajout d'un indicateur d'impact environnemental pour les messages de l'assistant, la possibilité d'éditer les documents directement depuis l'interface, et des corrections de bugs pour une meilleure stabilité. Des optimisations techniques ont été réalisées pour améliorer la performance du traitement des fichiers et l'asynchronisation des tâches.

### Évolutions fonctionnelles
- Ajout d'un indicateur d'impact environnemental (CO2) sur les messages de l'assistant. [#554ff4a](https://github.com/suitenumerique/conversations/commit/554ff4a)
- Implémentation de la fonctionnalité "Edit in Docs" permettant de modifier un document directement depuis l'interface. [#1a19225](https://github.com/suitenumerique/conversations/commit/1a19225)
- Amélioration de l'interface utilisateur pour autoriser les utilisateurs sans nom complet. [#08127a3](https://github.com/suitenumerique/conversations/commit/08127a3)
- Mise à jour de l'illustration de la page 404. [#2579a14](https://github.com/suitenumerique/conversations/commit/2579a14)
- Utilisation de "L'Assistant" comme nom de produit par défaut. [#9199cfc](https://github.com/suitenumerique/conversations/commit/9199cfc)

### Évolutions techniques
- Traitement asynchrone des fichiers de conversation et de projet pour améliorer la performance. [#d9cf44f](https://github.com/suitenumerique/conversations/commit/d9cf44f), [#059ac93](https://github.com/suitenumerique/conversations/commit/059ac93)
- Mise en place de Celery pour la gestion des tâches asynchrones. [#9abe4b9](https://github.com/suitenumerique/conversations/commit/9abe4b9)
- Refactoring du module de vues de chat et utilisation de constantes partagées. [#0c06446](https://github.com/suitenumerique/conversations/commit/0c06446)
- Mise à jour de la version de Python et des dépendances. [#df4c0ae](https://github.com/suitenumerique/conversations/commit/df4c0ae)
- Simplification de la configuration de l'environnement de test. [#7a9b58b](https://github.com/suitenumerique/conversations/commit/7a9b58b), [#1466e32](https://github.com/suitenumerique/conversations/commit/1466e32)
- Ajout d'un mécanisme de repli pour les modèles. [#b57d758](https://github.com/suitenumerique/conversations/commit/b57d758)

### Autres changements
- Correction du rafraîchissement du titre de la conversation dans le panneau latéral replié. [#91b5554](https://github.com/suitenumerique/conversations/commit/91b5554)
- Mise à jour des chaînes de traduction. [#bd8c532](https://github.com/suitenumerique/conversations/commit/bd8c532)
- Mise à jour des logos et des icônes. [#ea17208](https://github.com/suitenumerique/conversations/commit/ea17208)
- Correction de la cible du lien de contact et du lien vers la documentation. [#9dd4cb7](https://github.com/suitenumerique/conversations/commit/9dd4cb7)
- Mise à jour des dépendances frontales et de messagerie. [#68dd00b](https://github.com/suitenumerique/conversations/commit/68dd00b)
- Gestion des erreurs 404 lors de la suppression d'un document. [#4263e9a](https://github.com/suitenumerique/conversations/commit/4263e9a)
