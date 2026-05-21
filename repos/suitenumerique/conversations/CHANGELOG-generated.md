## Changelog : conversations (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la recherche documentaire avec l'introduction d'un contexte hybride, l'ajout de la gestion des fichiers de projet pour la recherche RAG, et l'amélioration de la fiabilité de l'IA en réduisant les hallucinations d'URL. Une nouvelle interface d'onboarding a été ajoutée pour faciliter la prise en main, et des améliorations ont été apportées à la configuration et à la gestion des paramètres utilisateur.

### Évolutions fonctionnelles
- Ajout d'un tutoriel d'onboarding pour guider les nouveaux utilisateurs [#8b2321d](https://github.com/suitenumerique/conversations/commit/8b2321d).
- Amélioration du contexte documentaire avec une approche hybride pour une recherche plus pertinente [#2bde1bb](https://github.com/suitenumerique/conversations/commit/2bde1bb) et [#66c5f7d](https://github.com/suitenumerique/conversations/commit/66c5f7d).
- Possibilité de gérer les fichiers de projet pour la recherche RAG (Retrieval-Augmented Generation) [#0eae7a2](https://github.com/suitenumerique/conversations/commit/0eae7a2).
- Nouvelle interface de configuration des paramètres utilisateur [#5ca4ef9](https://github.com/suitenumerique/conversations/commit/5ca4ef9).
- Ajout d'une bannière de statut configurable avec une visibilité limitée dans le temps [#5e0e408](https://github.com/suitenumerique/conversations/commit/5e0e408).
- Amélioration de la gestion de la création de projets, qui ouvre désormais une nouvelle conversation [#d243b55](https://github.com/suitenumerique/conversations/commit/d243b55).

### Évolutions techniques
- Amélioration de l'instruction pour réduire les hallucinations d'URL [#dca0eef](https://github.com/suitenumerique/conversations/commit/dca0eef) et [#3dd7e2f](https://github.com/suitenumerique/conversations/commit/3dd7e2f).
- Mise à jour des librairies `lxml` et `pypdf` [#da740f6](https://github.com/suitenumerique/conversations/commit/da740f6).
- Correction d'un crash lié au streaming avec les APIs compatibles OpenAI [#9096d9e](https://github.com/suitenumerique/conversations/commit/9096d9e).
- Ajout de configurations supplémentaires au chart Helm pour faciliter la configuration avec Tilt [#e9a9cab](https://github.com/suitenumerique/conversations/commit/e9a9cab).
- Ajout d'un outil de documentation automatique [#d26a824](https://github.com/suitenumerique/conversations/commit/d26a824).
- Suppression de la partie "thinking" pour les modèles qui ne supportent pas le raisonnement [#6bb3135](https://github.com/suitenumerique/conversations/commit/6bb3135).

### Autres changements
- Correction de l'affichage d'une image dans la première étape du tutoriel [#84eebd0](https://github.com/suitenumerique/conversations/commit/84eebd0).
- Modification du paramètre par défaut de `allow_smart_web_search` à `False` [#37a61dc](https://github.com/suitenumerique/conversations/commit/37a61dc).
- Rendre le paramètre `allow_conversation_analytics` en lecture seule dans l'administration [#014cf00](https://github.com/suitenumerique/conversations/commit/014cf00).
- Correction de l'affichage du modal de projet en fonction du flag de fonctionnalité d'upload de documents [#e4f1d94](https://github.com/suitenumerique/conversations/commit/e4f1d94).
- Restriction de l'outil de documentation automatique aux questions de métadonnées [#a1ae4d5](https://github.com/suitenumerique/conversations/commit/a1ae4d5).
- Ajout de tests pour le composant `SourceItem` [#890dc10](https://github.com/suitenumerique/conversations/commit/890dc10).
- Correction de tests suite à l'ajout de nouvelles instructions [#af618c7](https://github.com/suitenumerique/conversations/commit/af618c7).
