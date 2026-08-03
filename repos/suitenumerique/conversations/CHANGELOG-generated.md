## Changelog : conversations (30 derniers jours, au 29 juillet 2026)

### Résumé
Les dernières mises à jour de Conversations se concentrent sur l'amélioration de l'expérience utilisateur avec l'ajout de résumés de conversations et une barre de progression, ainsi que sur l'optimisation des performances en traitant les fichiers et les conversations de manière asynchrone. Des corrections de bugs et des améliorations de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un résumé des messages dans une conversation [#585cf9e](https://github.com/suitenumerique/conversations/commit/585cf9e).
- Ajout d'une barre de progression lors des opérations asynchrones [#3568717](https://github.com/suitenumerique/conversations/commit/3568717).
- Implémentation d'une fonctionnalité "Modifier dans Docs" pour exporter un message vers la documentation [#1a19225](https://github.com/suitenumerique/conversations/commit/1a19225).
- Ajout d'un indicateur de l'impact carbone (CO2) sur les messages de l'assistant [#554ff4a](https://github.com/suitenumerique/conversations/commit/554ff4a).
- Amélioration du widget d'impact CO2 [#c823027](https://github.com/suitenumerique/conversations/commit/c823027).

### Évolutions techniques
- Passage au traitement asynchrone de la summarisation des conversations côté backend [#585cf9e](https://github.com/suitenumerique/conversations/commit/585cf9e).
- Refactorisation pour traiter les fichiers de conversation de manière asynchrone, améliorant ainsi les performances [#d9cf44f](https://github.com/suitenumerique/conversations/commit/d9cf44f).
- Suppression de l'ancien backend Find RAG et de ses paramètres associés [#55266db](https://github.com/suitenumerique/conversations/commit/55266db).
- Amélioration de la sécurité en protégeant l'analyse des fichiers contre les "decompression bombs" et les fichiers PDF trop volumineux [#d48bbb0](https://github.com/suitenumerique/conversations/commit/d48bbb0).
- Extraction d'un composant réutilisable pour la bannière de saisie de chat côté frontend [#e1ea8fb](https://github.com/suitenumerique/conversations/commit/e1ea8fb).
- Mise à jour et épinglage de dépendances pour corriger des vulnérabilités (CVE) [#aab6e91](https://github.com/suitenumerique/conversations/commit/aab6e91), [#2337408](https://github.com/suitenumerique/conversations/commit/2337408).
- Amélioration de la configuration de l'environnement de test et des dépendances [#7a9b58b](https://github.com/suitenumerique/conversations/commit/7a9b58b), [#1466e32](https://github.com/suitenumerique/conversations/commit/1466e32).

### Autres changements
- Mise à jour des chaînes de traduction (i18n) [#d9fd8f1](https://github.com/suitenumerique/conversations/commit/d9fd8f1).
- Correction de l'extension des fichiers lors de l'exportation de la documentation [#a2af746](https://github.com/suitenumerique/conversations/commit/a2af746), [#7e89b33](https://github.com/suitenumerique/conversations/commit/7e89b33).
- Mise à jour de la version à 0.0.21 et 0.0.20 [#672af33](https://github.com/suitenumerique/conversations/commit/672af33), [#c6ae4a5](https://github.com/suitenumerique/conversations/commit/c6ae4a5).
- Changement de l'illustration 404 [#2579a14](https://github.com/suitenumerique/conversations/commit/2579a14).
