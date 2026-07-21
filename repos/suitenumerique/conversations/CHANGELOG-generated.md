## Changelog : conversations (30 derniers jours, au 19 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des fichiers et des documents, avec un traitement asynchrone pour une meilleure performance. L'interface utilisateur a été peaufinée avec des corrections de bugs et des améliorations visuelles, notamment un indicateur de consommation d'énergie pour les réponses de l'assistant. Des ajustements techniques ont été effectués pour la sécurité, la gestion des dépendances et la préparation de tâches en arrière-plan.

### Évolutions fonctionnelles
- Ajout d'un indicateur de consommation de CO2 sur les messages de l'assistant [#554ff4a](https://github.com/suitenumerique/conversations/commit/554ff4a).
- Possibilité d'éditer un message directement dans la documentation associée grâce à la fonctionnalité "Edit in Docs" [#1a19225](https://github.com/suitenumerique/conversations/commit/1a19225).
- Amélioration de l'interface utilisateur pour permettre l'utilisation sans nom complet [#08127a3](https://github.com/suitenumerique/conversations/commit/08127a3).
- Nouvelle illustration pour la page 404 [#2579a14](https://github.com/suitenumerique/conversations/commit/2579a14).
- Mise à jour du nom par défaut du produit en "L'Assistant" [#9199cfc](https://github.com/suitenumerique/conversations/commit/9199cfc).
- Affichage d'un message d'erreur spécifique en cas d'échec de l'analyse d'un document [#2ffffae](https://github.com/suitenumerique/conversations/commit/2ffffae).

### Évolutions techniques
- Suppression de l'ancien backend Find RAG et de ses paramètres associés [#55266db](https://github.com/suitenumerique/conversations/commit/55266db).
- Protection contre les attaques par décompression et les fichiers PDF trop volumineux [#d48bbb0](https://github.com/suitenumerique/conversations/commit/d48bbb0).
- Traitement asynchrone des fichiers de conversation et des fichiers du projet pour améliorer les performances [#d9cf44f](https://github.com/suitenumerique/conversations/commit/d9cf44f) et [#059ac93](https://github.com/suitenumerique/conversations/commit/059ac93).
- Mise en place de Celery pour l'exécution de tâches en arrière-plan [#9abe4b9](https://github.com/suitenumerique/conversations/commit/9abe4b9).
- Ajout d'un mécanisme de repli (fallback) pour les modèles d'IA [#b57d758](https://github.com/suitenumerique/conversations/commit/b57d758).
- Mise à jour de la version de Python et des dépendances [#df4c0ae](https://github.com/suitenumerique/conversations/commit/df4c0ae).
- Refactorisation du module de vues de chat et utilisation de constantes partagées [#0c06446](https://github.com/suitenumerique/conversations/commit/0c06446).
- Nettoyage et simplification de la configuration des tests [#7a9b58b](https://github.com/suitenumerique/conversations/commit/7a9b58b) et [#1466e32](https://github.com/suitenumerique/conversations/commit/1466e32).

### Autres changements
- Mise à jour des chaînes de traduction [#bd8c532](https://github.com/suitenumerique/conversations/commit/bd8c532).
- Mise à jour des logos et des icônes [#ea17208](https://github.com/suitenumerique/conversations/commit/ea17208).
- Correction de liens et de cibles [#9dd4cb7](https://github.com/suitenumerique/conversations/commit/9dd4cb7).
- Mise à jour des dépendances frontales et de messagerie [#68dd00b](https://github.com/suitenumerique/conversations/commit/68dd00b).
- Correction d'un bug empêchant le rafraîchissement du titre de la conversation dans le panneau latéral replié [#91b5554](https://github.com/suitenumerique/conversations/commit/91b5554).
