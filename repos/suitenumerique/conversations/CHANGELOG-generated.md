## Changelog : conversations (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance, la sécurité et l'expérience utilisateur. Des optimisations ont été apportées au traitement des fichiers et des conversations, notamment en utilisant des tâches asynchrones pour éviter les blocages. L'interface utilisateur a été améliorée avec l'ajout d'un indicateur d'impact carbone et la correction de bugs visuels. La sécurité a également été renforcée avec des protections contre les attaques par décompression et la gestion des tailles de fichiers.

### Évolutions fonctionnelles
- Ajout d'un indicateur d'impact carbone sur les messages de l'assistant [#554ff4a](https://github.com/suitenumerique/conversations/commit/554ff4a).
- Implémentation d'une fonctionnalité "Modifier dans Docs" pour exporter les messages vers la documentation [#1a19225](https://github.com/suitenumerique/conversations/commit/1a19225).
- Mise à jour de l'interface utilisateur pour autoriser les noms complets vides [#08127a3](https://github.com/suitenumerique/conversations/commit/08127a3).
- Amélioration du widget d'impact CO2 [#c823027](https://github.com/suitenumerique/conversations/commit/c823027).
- Modification de l'illustration de la page 404 [#2579a14](https://github.com/suitenumerique/conversations/commit/2579a14).

### Évolutions techniques
- Suppression du backend Find RAG et de ses paramètres associés [#55266db](https://github.com/suitenumerique/conversations/commit/55266db).
- Mise en place de tâches asynchrones avec Celery pour le traitement des fichiers et des conversations [#29abe4b9](https://github.com/suitenumerique/conversations/commit/9abe4b9), [#d9cf44f](https://github.com/suitenumerique/conversations/commit/d9cf44f), [#059ac93](https://github.com/suitenumerique/conversations/commit/059ac93).
- Protection contre les attaques par décompression et les fichiers PDF trop volumineux [#d48bbb0](https://github.com/suitenumerique/conversations/commit/d48bbb0).
- Refactorisation du module de vues de chat et utilisation de constantes partagées [#0c06446](https://github.com/suitenumerique/conversations/commit/0c06446).
- Mise à jour et épinglage des dépendances pour corriger des vulnérabilités CVE [#aab6e91](https://github.com/suitenumerique/conversations/commit/aab6e91), [#2337408](https://github.com/suitenumerique/conversations/commit/2337408).
- Ajout d'un mécanisme de repli de modèle [#b57d758](https://github.com/suitenumerique/conversations/commit/b57d758).
- Amélioration des tests : nettoyage des paramètres et des fixtures, simplification de la configuration de l'environnement de test [#7a9b58b](https://github.com/suitenumerique/conversations/commit/7a9b58b), [#1466e32](https://github.com/suitenumerique/conversations/commit/1466e32).
- Extraction d'un composant réutilisable pour la bannière de saisie de chat [#e1ea8fb](https://github.com/suitenumerique/conversations/commit/e1ea8fb).

### Autres changements
- Correction du titre de la conversation dans le panneau latéral replié [#91b5554](https://github.com/suitenumerique/conversations/commit/91b5554).
- Modification du titre des exports de documentation pour utiliser un format horodaté localisé [#2e79f94](https://github.com/suitenumerique/conversations/commit/2e79f94).
- Correction de l'extension des fichiers exportés en documentation (suppression de `.md`) [#a2af746](https://github.com/suitenumerique/conversations/commit/a2af746), [#7e89b33](https://github.com/suitenumerique/conversations/commit/7e89b33).
