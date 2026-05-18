## Changelog : conversations (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des documents, notamment en introduisant un contexte hybride pour la recherche et en permettant l'intégration de fichiers de projet pour la recherche RAG. Des améliorations ont également été apportées à l'interface utilisateur, avec l'ajout d'un tutoriel d'onboarding et de nouvelles options de configuration. Enfin, des corrections de bugs et des optimisations techniques ont été réalisées pour améliorer la stabilité et les performances.

### Évolutions fonctionnelles
- Ajout d'un nouveau tutoriel d'onboarding pour guider les nouveaux utilisateurs. [#8b2321d](https://github.com/suitenumerique/conversations/commit/8b2321d)
- Nouvelle modale de configuration des paramètres utilisateur. [#5ca4ef9](https://github.com/suitenumerique/conversations/commit/5ca4ef9)
- Possibilité de gérer les fichiers de projet pour la recherche RAG (Retrieval-Augmented Generation). [#0eae7a2](https://github.com/suitenumerique/conversations/commit/0eae7a2)
- Amélioration du contexte des documents avec une approche hybride. [#2bde1bb](https://github.com/suitenumerique/conversations/commit/2bde1bb) et [#66c5f7d](https://github.com/suitenumerique/conversations/commit/66c5f7d)
- Le paramètre "allow_smart_web_search" est maintenant par défaut à "False". [#37a61dc](https://github.com/suitenumerique/conversations/commit/37a61dc)
- Le paramètre "allow_conversation_analytics" est maintenant en lecture seule dans l'interface d'administration. [#014cf00](https://github.com/suitenumerique/conversations/commit/014cf00)
- Correction de l'affichage de l'image du premier pas du tutoriel d'onboarding. [#84eebd0](https://github.com/suitenumerique/conversations/commit/84eebd0)
- La modale de projet respecte maintenant l'indicateur de fonctionnalité "document-upload". [#e4f1d94](https://github.com/suitenumerique/conversations/commit/e4f1d94)

### Évolutions techniques
- Ajout de configurations supplémentaires au chart Helm pour corriger la configuration de Tilt. [#e9a9cab](https://github.com/suitenumerique/conversations/commit/e9a9cab)
- Ajout d'une instruction pour éviter les hallucinations d'URL à l'agent de conversation. [#3dd7e2f](https://github.com/suitenumerique/conversations/commit/3dd7e2f)
- Mise à jour de `lxml` et `pypdf`. [#da740f6](https://github.com/suitenumerique/conversations/commit/da740f6)
- Correction des tests en ajoutant de nouvelles instructions à tous les tests. [#af618c7](https://github.com/suitenumerique/conversations/commit/af618c7)
- Ajout d'un outil d'auto-documentation. [#d26a824](https://github.com/suitenumerique/conversations/commit/d26a824)
- Suppression de la partie "thinking" pour les modèles qui ne supportent pas le raisonnement. [#6bb3135](https://github.com/suitenumerique/conversations/commit/6bb3135)

### Autres changements
- Ajout de tests pour le composant `SourceItem`. [#890dc10](https://github.com/suitenumerique/conversations/commit/890dc10)
- Correction d'un crash de streaming avec les APIs compatibles OpenAI. [#9096d9e](https://github.com/suitenumerique/conversations/commit/9096d9e)
