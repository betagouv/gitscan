## Changelog : conversations (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration de documents pour une recherche plus pertinente, l'amélioration de l'expérience utilisateur avec un nouveau processus d'onboarding et des paramètres plus accessibles, ainsi que des corrections de bugs et des optimisations techniques pour une meilleure stabilité et performance. L'ajout de la gestion des fichiers de projet pour la recherche RAG est également une évolution importante.

### Évolutions fonctionnelles
- Ajout d'un nouveau processus d'onboarding avec un modal pour guider les nouveaux utilisateurs. [#8b2321d](https://github.com/suitenumerique/conversations/commit/8b2321d)
- Amélioration du contexte des documents en le rendant hybride, combinant différentes sources pour une meilleure pertinence. [#2bde1bb](https://github.com/suitenumerique/conversations/commit/2bde1bb)
- Possibilité de gérer les fichiers de projet pour la recherche RAG (Retrieval-Augmented Generation). [#0eae7a2](https://github.com/suitenumerique/conversations/commit/0eae7a2)
- Ajout d'une nouvelle modale de paramètres pour une meilleure accessibilité. [#5ca4ef9](https://github.com/suitenumerique/conversations/commit/5ca4ef9)
- Ajout d'une authentification OIDC silencieuse pour une expérience utilisateur plus fluide. [#59d8f1e](https://github.com/suitenumerique/conversations/commit/59d8f1e)
- Mise à jour des descriptions des outils disponibles. [#a9f667b](https://github.com/suitenumerique/conversations/commit/a9f667b)

### Évolutions techniques
- Ajout d'instructions pour éviter les hallucinations d'URL dans l'agent de conversation. [#3dd7e2f](https://github.com/suitenumerique/conversations/commit/3dd7e2f)
- Mise à jour des configurations du chart Helm pour corriger la configuration de Tilt. [#e9a9cab](https://github.com/suitenumerique/conversations/commit/e9a9cab)
- Amélioration de la gestion du contexte hybride des documents. [#66c5f7d](https://github.com/suitenumerique/conversations/commit/66c5f7d)
- Modification du paramètre `allow_smart_web_search` pour qu'il soit par défaut à `False`. [#37a61dc](https://github.com/suitenumerique/conversations/commit/37a61dc)
- Le paramètre `allow_conversation_analytics` est maintenant en lecture seule dans l'interface d'administration. [#014cf00](https://github.com/suitenumerique/conversations/commit/014cf00)
- Ajout d'un outil de documentation automatique. [#d26a824](https://github.com/suitenumerique/conversations/commit/d26a824)
- Correction d'un crash de streaming avec les APIs compatibles OpenAI. [#9096d9e](https://github.com/suitenumerique/conversations/commit/9096d9e)
- Suppression de la partie "thinking" pour les modèles qui ne supportent pas le raisonnement. [#6bb3135](https://github.com/suitenumerique/conversations/commit/6bb3135)
- Mise à jour des dépendances `lxml` et `pypdf`. [#da740f6](https://github.com/suitenumerique/conversations/commit/da740f6)
- Obtention des données carbone depuis l'API Albert. [#26a5fa1](https://github.com/suitenumerique/conversations/commit/26a5fa1)

### Autres changements
- Correction du texte du premier pas dans le processus d'onboarding. [#84eebd0](https://github.com/suitenumerique/conversations/commit/84eebd0)
- Correction de la taille du bouton "Nouvelle conversation dans le projet". [#b8b5630](https://github.com/suitenumerique/conversations/commit/b8b5630)
- Ajout de tests pour le composant `SourceItem`. [#890dc10](https://github.com/suitenumerique/conversations/commit/890dc10)
- Ajout de nouvelles instructions à tous les tests. [#af618c7](https://github.com/suitenumerique/conversations/commit/af618c7)
