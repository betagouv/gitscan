## Changelog : conversations (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des documents et à l'expérience utilisateur, notamment la possibilité de résumer les conversations, un meilleur traitement des fichiers volumineux et des correctifs pour la stabilité et la sécurité. Des optimisations de performance ont également été apportées pour le traitement asynchrone des fichiers et des conversations.

### Évolutions fonctionnelles
- Ajout de la possibilité de résumer les messages d'une conversation. [#e79d366](https://github.com/suitenumerique/conversations/commit/e79d366)
- Implémentation d'une barre de progression lors de l'exécution de tâches asynchrones. [#3568717](https://github.com/suitenumerique/conversations/commit/3568717)
- Ajout d'une fonctionnalité "Modifier dans Docs" pour exporter un message vers la documentation. [#1a19225](https://github.com/suitenumerique/conversations/commit/1a19225)
- Amélioration du widget d'impact CO2 avec corrections et optimisations. [#c823027](https://github.com/suitenumerique/conversations/commit/c823027)
- Ajout d'un tooltip CO2 sur les messages de l'assistant. [#554ff4a](https://github.com/suitenumerique/conversations/commit/554ff4a)
- Modification de l'illustration de la page 404. [#2579a14](https://github.com/suitenumerique/conversations/commit/2579a14)

### Évolutions techniques
- Passage au traitement asynchrone des fichiers de conversation pour améliorer la performance. [#d9cf44f](https://github.com/suitenumerique/conversations/commit/d9cf44f)
- Passage au traitement asynchrone des fichiers de projet avec gestion de l'état d'indexation. [#059ac93](https://github.com/suitenumerique/conversations/commit/059ac93)
- Suppression du backend Find RAG et de ses paramètres associés. [#55266db](https://github.com/suitenumerique/conversations/commit/55266db)
- Amélioration de la sécurité en protégeant l'analyse des fichiers contre les "decompression bombs" et les fichiers PDF trop volumineux. [#d48bbb0](https://github.com/suitenumerique/conversations/commit/d48bbb0)
- Refonte des tests : simplification de la configuration de l'environnement et des dépendances. [#7a9b58b](https://github.com/suitenumerique/conversations/commit/7a9b58b) et [#1466e32](https://github.com/suitenumerique/conversations/commit/1466e32)
- Mise à jour et épinglage de dépendances pour corriger des vulnérabilités (CVE). [#aab6e91](https://github.com/suitenumerique/conversations/commit/aab6e91) et [#2337408](https://github.com/suitenumerique/conversations/commit/2337408)
- Résumé des conversations rendu asynchrone. [#585cf9e](https://github.com/suitenumerique/conversations/commit/585cf9e)
- Amélioration de la robustesse de la summarisation asynchrone des conversations. [#0671ac0](https://github.com/suitenumerique/conversations/commit/0671ac0)

### Autres changements
- Mise à jour des chaînes de caractères traduites (i18n). [#d9fd8f1](https://github.com/suitenumerique/conversations/commit/d9fd8f1)
- Correction de l'alignement des requêtes Albert RAG avec l'API actuelle. [#637a6ac](https://github.com/suitenumerique/conversations/commit/637a6ac)
- Ajout du support pour les noms complets nuls dans l'interface utilisateur. [#08127a3](https://github.com/suitenumerique/conversations/commit/08127a3)
- Extraction d'un composant réutilisable pour la bannière de saisie de chat. [#e1ea8fb](https://github.com/suitenumerique/conversations/commit/e1ea8fb)
- Correction du rafraîchissement du titre de la conversation dans le panneau latéral replié. [#91b5554](https://github.com/suitenumerique/conversations/commit/91b5554)
