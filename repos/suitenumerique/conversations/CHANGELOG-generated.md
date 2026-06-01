## Changelog : conversations (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à l'expérience utilisateur, notamment en permettant de continuer à taper pendant que l'IA génère une réponse, en introduisant un nouveau modal de paramètres et en améliorant la gestion des documents avec un contexte hybride. Des correctifs ont également été apportés pour améliorer la stabilité et la précision des réponses de l'IA. Enfin, des améliorations ont été apportées à l'infrastructure pour faciliter le développement local.

### Évolutions fonctionnelles
- Possibilité de continuer à taper une question pendant que l'IA génère une réponse. [#763ed4b](https://github.com/suitenumerique/conversations/commit/763ed4b)
- Nouveau modal de paramètres pour une configuration plus facile. [#5ca4ef9](https://github.com/suitenumerique/conversations/commit/5ca4ef9)
- Amélioration du contexte des documents avec une approche hybride, combinant différentes sources d'informations. [#2bde1bb](https://github.com/suitenumerique/conversations/commit/2bde1bb)
- Introduction d'un tutoriel guidé (onboarding modal) pour aider les nouveaux utilisateurs à démarrer. [#8b2321d](https://github.com/suitenumerique/conversations/commit/8b2321d)
- Gestion des fichiers de projet pour la recherche RAG (Retrieval-Augmented Generation). [#0eae7a2](https://github.com/suitenumerique/conversations/commit/0eae7a2)
- Ajout d'une bannière de statut configurable avec une visibilité limitée dans le temps. [#5e0e408](https://github.com/suitenumerique/conversations/commit/5e0e408)

### Évolutions techniques
- Amélioration de l'instruction pour réduire les "hallucinations" d'URL par l'IA. [#dca0eef](https://github.com/suitenumerique/conversations/commit/dca0eef)
- Optimisation de l'utilisation du contexte hybride pour les documents. [#66c5f7d](https://github.com/suitenumerique/conversations/commit/66c5f7d)
- Configuration supplémentaire pour les charts Helm afin de faciliter la configuration de l'environnement local avec Tilt. [#e9a9cab](https://github.com/suitenumerique/conversations/commit/e9a9cab)
- Restriction de l'accès à la documentation automatique à des questions spécifiques. [#a1ae4d5](https://github.com/suitenumerique/conversations/commit/a1ae4d5)
- Suppression des scripts d'installation Yarn dans le build Docker pour améliorer la sécurité. [#119b814](https://github.com/suitenumerique/conversations/commit/119b814)
- Suppression de la partie "réflexion" (thinking part) pour les modèles d'IA qui ne la supportent pas. [#6bb3135](https://github.com/suitenumerique/conversations/commit/6bb3135)

### Autres changements
- Mise à jour des chaînes de caractères traduites. [#f03e101](https://github.com/suitenumerique/conversations/commit/f03e101)
- Correction d'un problème d'affichage du modal de projet avec la fonctionnalité de téléchargement de documents. [#e4f1d94](https://github.com/suitenumerique/conversations/commit/e4f1d94)
- Modification de la valeur par défaut de `allow_smart_web_search` à `False`. [#37a61dc](https://github.com/suitenumerique/conversations/commit/37a61dc)
- Rendre le paramètre `allow_conversation_analytics` en lecture seule dans l'interface d'administration. [#014cf00](https://github.com/suitenumerique/conversations/commit/014cf00)
- Correction de la formulation de l'étape 1 de l'image du tutoriel. [#84eebd0](https://github.com/suitenumerique/conversations/commit/84eebd0)
