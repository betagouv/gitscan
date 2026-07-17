## Changelog : conversations (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la performance et à la robustesse de la plateforme, notamment grâce à l'introduction de tâches asynchrones pour le traitement des fichiers et des conversations. L'interface utilisateur a également été peaufinée avec des corrections visuelles et l'ajout de fonctionnalités comme l'édition de documents directement depuis l'interface.

### Évolutions fonctionnelles
- Ajout de la fonctionnalité "Modifier dans les Docs" permettant d'exporter un message vers la documentation. [#1a19225](https://github.com/suitenumerique/conversations/commit/1a19225)
- Amélioration de l'interface utilisateur pour autoriser les utilisateurs sans nom complet. [#08127a3](https://github.com/suitenumerique/conversations/commit/08127a3)
- Mise à jour de l'illustration de la page 404 pour une meilleure expérience utilisateur. [#2579a14](https://github.com/suitenumerique/conversations/commit/2579a14)
- Correction du rafraîchissement du titre de la conversation dans le panneau latéral replié. [#91b5554](https://github.com/suitenumerique/conversations/commit/91b5554)
- Utilisation de "L'Assistant" comme nom de produit par défaut. [#9199cfc](https://github.com/suitenumerique/conversations/commit/9199cfc)

### Évolutions techniques
- Introduction de Celery pour l'exécution de tâches asynchrones, améliorant la réactivité de l'application. [#9abe4b9](https://github.com/suitenumerique/conversations/commit/9abe4b9)
- Traitement asynchrone des fichiers de conversation et de projet pour une meilleure performance. [#d9cf44f](https://github.com/suitenumerique/conversations/commit/d9cf44f), [#059ac93](https://github.com/suitenumerique/conversations/commit/059ac93)
- Refactorisation du module de vues de chat et utilisation de constantes partagées pour une meilleure maintenabilité. [#0c06446](https://github.com/suitenumerique/conversations/commit/0c06446)
- Mise à jour de la version de Python et des dépendances pour bénéficier des dernières corrections et améliorations. [#df4c0ae](https://github.com/suitenumerique/conversations/commit/df4c0ae)
- Ajout d'un mécanisme de repli sur un modèle par défaut en cas d'indisponibilité du modèle principal. [#b57d758](https://github.com/suitenumerique/conversations/commit/b57d758)
- Amélioration de la gestion des erreurs lors de la suppression de documents (traitement des 404 comme succès de désindexation). [#4263e9a](https://github.com/suitenumerique/conversations/commit/4263e9a)

### Autres changements
- Mise à jour des chaînes de traduction. [#bd8c532](https://github.com/suitenumerique/conversations/commit/bd8c532)
- Mise à jour des logos et des icônes. [#ea17208](https://github.com/suitenumerique/conversations/commit/ea17208)
- Correction de liens et de cibles de liens. [#9dd4cb7](https://github.com/suitenumerique/conversations/commit/9dd4cb7)
- Nettoyage et simplification de la configuration des tests. [#7a9b58b](https://github.com/suitenumerique/conversations/commit/7a9b58b), [#1466e32](https://github.com/suitenumerique/conversations/commit/1466e32)
