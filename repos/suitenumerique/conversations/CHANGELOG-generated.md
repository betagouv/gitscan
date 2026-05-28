## Changelog : conversations (30 derniers jours, au 26 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout d'un tutoriel d'intégration, la possibilité de taper pendant la génération de réponses par l'IA, et une meilleure gestion des projets et des documents. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'un tutoriel d'intégration (onboarding) pour guider les nouveaux utilisateurs. [#8b2321d](https://github.com/suitenumerique/conversations/commit/8b2321d)
- Possibilité de taper une nouvelle question pendant que l'IA génère une réponse. [#763ed4b](https://github.com/suitenumerique/conversations/commit/763ed4b)
- Gestion des fichiers de projet pour la recherche RAG (Retrieval-Augmented Generation). [#0eae7a2](https://github.com/suitenumerique/conversations/commit/0eae7a2)
- Nouvelle interface de configuration (settings) pour personnaliser l'application. [#5ca4ef9](https://github.com/suitenumerique/conversations/commit/5ca4ef9)
- Amélioration du contexte des documents avec une approche hybride. [#66c5f7d](https://github.com/suitenumerique/conversations/commit/66c5f7d)
- Ajout d'une bannière de statut configurable avec une visibilité limitée dans le temps. [#5e0e408](https://github.com/suitenumerique/conversations/commit/5e0e408)

### Évolutions techniques
- Amélioration de l'instruction pour éviter les hallucinations d'URL. [#dca0eef](https://github.com/suitenumerique/conversations/commit/dca0eef)
- Limitation de l'outil d'auto-documentation aux questions concernant les métadonnées. [#a1ae4d5](https://github.com/suitenumerique/conversations/commit/a1ae4d5)
- Mise à jour des dépendances `lxml` et `pypdf`. [#da740f6](https://github.com/suitenumerique/conversations/commit/da740f6)
- Configuration supplémentaire du chart Helm pour corriger la configuration de Tilt. [#e9a9cab](https://github.com/suitenumerique/conversations/commit/e9a9cab)
- Correction d'un crash de streaming avec les APIs compatibles OpenAI. [#9096d9e](https://github.com/suitenumerique/conversations/commit/9096d9e)
- Désactivation des scripts d'installation Yarn dans le build Docker. [#119b814](https://github.com/suitenumerique/conversations/commit/119b814)

### Autres changements
- Mise à jour des chaînes de caractères traduites. [#f03e101](https://github.com/suitenumerique/conversations/commit/f03e101)
- Publication de la version 0.0.16. [#293efff](https://github.com/suitenumerique/conversations/commit/293efff)
- Modification du paramètre par défaut de `allow_smart_web_search` à `False`. [#37a61dc](https://github.com/suitenumerique/conversations/commit/37a61dc)
- Rendre le paramètre `allow_conversation_analytics` en lecture seule dans l'interface d'administration. [#014cf00](https://github.com/suitenumerique/conversations/commit/014cf00)
