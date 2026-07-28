## Changelog : conversations (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations à la gestion des documents, notamment un traitement asynchrone des fichiers pour une meilleure performance. L'interface utilisateur a été peaufinée avec l'ajout d'un indicateur d'impact carbone et une correction de l'affichage du titre des conversations. Des corrections de sécurité ont également été implémentées pour protéger contre des attaques potentielles.

### Évolutions fonctionnelles
- Ajout d'un indicateur d'impact carbone sur les messages de l'assistant [#554ff4a](https://github.com/suitenumerique/conversations/commit/554ff4a).
- Implémentation d'une fonctionnalité "Modifier dans les Docs" pour exporter un message vers la documentation [#1a19225](https://github.com/suitenumerique/conversations/commit/1a19225).
- Correction de l'affichage du titre de la conversation dans le panneau latéral réduit [#91b5554](https://github.com/suitenumerique/conversations/commit/91b5554).
- Amélioration du widget d'impact CO2 [#c823027](https://github.com/suitenumerique/conversations/commit/c823027).
- Mise à jour de l'illustration de la page 404 [#2579a14](https://github.com/suitenumerique/conversations/commit/2579a14).
- Possibilité de gérer les utilisateurs sans nom complet [#08127a3](https://github.com/suitenumerique/conversations/commit/08127a3).

### Évolutions techniques
- Suppression du backend Find RAG et de ses paramètres associés [#55266db](https://github.com/suitenumerique/conversations/commit/55266db).
- Mise en place de tâches asynchrones avec Celery pour le traitement des fichiers et l'indexation [#9abe4b9](https://github.com/suitenumerique/conversations/commit/9abe4b9), [#059ac93](https://github.com/suitenumerique/conversations/commit/059ac93), [#d9cf44f](https://github.com/suitenumerique/conversations/commit/d9cf44f).
- Protection contre les attaques par décompression et les fichiers PDF volumineux [#d48bbb0](https://github.com/suitenumerique/conversations/commit/d48bbb0).
- Refactorisation du module de vues de chat et utilisation de constantes partagées [#0c06446](https://github.com/suitenumerique/conversations/commit/0c06446).
- Mise à jour et épinglage des dépendances pour corriger des vulnérabilités CVE [#aab6e91](https://github.com/suitenumerique/conversations/commit/aab6e91), [#2337408](https://github.com/suitenumerique/conversations/commit/2337408).
- Extraction d'un composant réutilisable pour la bannière de saisie de chat [#e1ea8fb](https://github.com/suitenumerique/conversations/commit/e1ea8fb).
- Implémentation d'un mécanisme de repli pour les modèles [#b57d758](https://github.com/suitenumerique/conversations/commit/b57d758).
- Nettoyage et simplification de la configuration des tests [#7a9b58b](https://github.com/suitenumerique/conversations/commit/7a9b58b), [#1466e32](https://github.com/suitenumerique/conversations/commit/1466e32).

### Autres changements
- Mise à jour des traductions [#d9fd8f1](https://github.com/suitenumerique/conversations/commit/d9fd8f1).
- Publication de la version 0.0.20 [#c6ae4a5](https://github.com/suitenumerique/conversations/commit/c6ae4a5).
- Correction du titre des fichiers exportés en Markdown [#a2af746](https://github.com/suitenumerique/conversations/commit/a2af746), [#7e89b33](https://github.com/suitenumerique/conversations/commit/7e89b33).
