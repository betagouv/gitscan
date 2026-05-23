## Changelog : conversations (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec l'ajout d'un tutoriel d'onboarding, la possibilité de taper pendant la génération de réponse du modèle, et une gestion améliorée des projets et des documents. Des corrections de bugs et des optimisations ont également été apportées pour une meilleure stabilité et performance.

### Évolutions fonctionnelles
- Ajout d'un tutoriel d'onboarding pour guider les nouveaux utilisateurs. [#8b2321d](https://github.com/suitenumerique/conversations/commit/8b2321d)
- Possibilité de taper dans la zone de texte pendant que le modèle génère une réponse. [#763ed4b](https://github.com/suitenumerique/conversations/commit/763ed4b)
- Gestion des fichiers de projet pour la recherche RAG (Retrieval-Augmented Generation). [#0eae7a2](https://github.com/suitenumerique/conversations/commit/0eae7a2)
- Amélioration du contexte hybride pour les documents, combinant différentes sources. [#66c5f7d](https://github.com/suitenumerique/conversations/commit/66c5f7d) et [#2bde1bb](https://github.com/suitenumerique/conversations/commit/2bde1bb)
- Nouvelle interface de configuration des paramètres. [#5ca4ef9](https://github.com/suitenumerique/conversations/commit/5ca4ef9)
- Ajout d'une bannière de statut configurable avec une visibilité limitée dans le temps. [#5e0e408](https://github.com/suitenumerique/conversations/commit/5e0e408)
- Possibilité de basculer vers une nouvelle conversation lors de la création d'un projet. [#d243b55](https://github.com/suitenumerique/conversations/commit/d243b55)

### Évolutions techniques
- Amélioration de l'instruction pour éviter les hallucinations d'URL. [#dca0eef](https://github.com/suitenumerique/conversations/commit/dca0eef)
- Mise à jour de `lxml` et `pypdf`. [#da740f6](https://github.com/suitenumerique/conversations/commit/da740f6)
- Correction d'un crash en streaming avec les APIs compatibles OpenAI. [#9096d9e](https://github.com/suitenumerique/conversations/commit/9096d9e)
- Ajout de configurations Helm supplémentaires pour corriger la configuration de Tilt. [#e9a9cab](https://github.com/suitenumerique/conversations/commit/e9a9cab)
- Restriction de l'accès en administration au paramètre `allow_conversation_analytics`. [#014cf00](https://github.com/suitenumerique/conversations/commit/014cf00)
- Modification de la valeur par défaut de `allow_smart_web_search` à `False`. [#37a61dc](https://github.com/suitenumerique/conversations/commit/37a61dc)
- Ajout d'instructions supplémentaires aux tests pour une meilleure couverture. [#af618c7](https://github.com/suitenumerique/conversations/commit/af618c7)
- Ajout d'un outil d'auto-documentation. [#d26a824](https://github.com/suitenumerique/conversations/commit/d26a824)
- Limitation de l'outil d'auto-documentation aux questions liées aux métadonnées. [#a1ae4d5](https://github.com/suitenumerique/conversations/commit/a1ae4d5)

### Autres changements
- Mise à jour des chaînes de traduction. [#f03e101](https://github.com/suitenumerique/conversations/commit/f03e101)
- Publication de la version 0.0.16. [#293efff](https://github.com/suitenumerique/conversations/commit/293efff)
- Correction de la formulation de la première étape du tutoriel. [#84eebd0](https://github.com/suitenumerique/conversations/commit/84eebd0)
