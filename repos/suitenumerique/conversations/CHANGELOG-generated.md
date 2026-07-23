## Changelog : conversations (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des fichiers, notamment un traitement asynchrone pour une meilleure performance. L'interface utilisateur a été peaufinée avec des corrections de bugs et des améliorations visuelles, ainsi qu'un indicateur d'impact carbone pour les messages de l'assistant. Des changements techniques ont été effectués pour optimiser le code et préparer le terrain pour de futures évolutions.

### Évolutions fonctionnelles
- Ajout d'un indicateur d'impact carbone sur les messages de l'assistant [#554ff4a](https://github.com/suitenumerique/conversations/commit/554ff4a).
- Implémentation d'une fonctionnalité "Modifier dans Docs" pour exporter facilement les messages vers la documentation [#1a19225](https://github.com/suitenumerique/conversations/commit/1a19225).
- Amélioration de la gestion des erreurs et des messages d'information, notamment avec l'utilisation de couleurs sémantiques pour les bannières [#b33481a](https://github.com/suitenumerique/conversations/commit/b33481a).
- Correction d'un bug qui empêchait le rafraîchissement du titre de la conversation dans le panneau latéral replié [#91b5554](https://github.com/suitenumerique/conversations/commit/91b5554).
- Mise à jour de l'illustration de la page 404 [#2579a14](https://github.com/suitenumerique/conversations/commit/2579a14).
- Correction d'un problème empêchant l'application de fonctionner correctement pour les utilisateurs sans nom complet ou adresse email [#08127a3](https://github.com/suitenumerique/conversations/commit/08127a3).

### Évolutions techniques
- Suppression de l'ancien backend Find RAG et de ses paramètres associés [#55266db](https://github.com/suitenumerique/conversations/commit/55266db).
- Protection contre les "decompression bombs" et les fichiers PDF trop volumineux lors de l'analyse [#d48bbb0](https://github.com/suitenumerique/conversations/commit/d48bbb0).
- Traitement asynchrone des fichiers de conversation et des fichiers de projet pour améliorer les performances [#d9cf44f](https://github.com/suitenumerique/conversations/commit/d9cf44f) et [#059ac93](https://github.com/suitenumerique/conversations/commit/059ac93).
- Mise en place de Celery pour l'exécution de tâches en arrière-plan [#9abe4b9](https://github.com/suitenumerique/conversations/commit/9abe4b9).
- Ajout d'un mécanisme de repli (fallback) pour les modèles [#b57d758](https://github.com/suitenumerique/conversations/commit/b57d758).
- Refactorisation du module de vues de chat et utilisation de constantes partagées [#0c06446](https://github.com/suitenumerique/conversations/commit/0c06446).
- Amélioration de la configuration de l'environnement de test et des dépendances [#7a9b58b](https://github.com/suitenumerique/conversations/commit/7a9b58b) et [#1466e32](https://github.com/suitenumerique/conversations/commit/1466e32).
- Extraction d'un composant réutilisable pour la bannière de saisie de chat [#e1ea8fb](https://github.com/suitenumerique/conversations/commit/e1ea8fb).

### Autres changements
- Mise à jour des traductions [#bd8c532](https://github.com/suitenumerique/conversations/commit/bd8c532).
- Mise à jour des logos et des favicons [#ea17208](https://github.com/suitenumerique/conversations/commit/ea17208).
- Correction de liens et de cibles [#9dd4cb7](https://github.com/suitenumerique/conversations/commit/9dd4cb7).
- Mise à jour des dépendances frontales et de messagerie [#68dd00b](https://github.com/suitenumerique/conversations/commit/68dd00b).
- Mise à jour de la version à 0.0.19 [#77c41c4](https://github.com/suitenumerique/conversations/commit/77c41c4).
