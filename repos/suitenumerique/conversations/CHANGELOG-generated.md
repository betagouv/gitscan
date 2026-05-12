## Changelog : conversations (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout d'un onboarding plus clair, de nouveaux paramètres et d'une meilleure gestion des documents. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme. L'ajout de la prise en charge de modèles open source et de l'authentification silencieuse OIDC élargissent les possibilités d'utilisation.

### Évolutions fonctionnelles
- Ajout d'un modal d'onboarding pour guider les nouveaux utilisateurs. [#8b2321d](https://github.com/suitenumerique/conversations/commit/8b2321d)
- Amélioration du contexte documentaire avec une approche hybride. [#2bde1bb](https://github.com/suitenumerique/conversations/commit/2bde1bb)
- Ajout de la prise en charge de l'authentification silencieuse OIDC pour une expérience utilisateur plus fluide. [#59d8f1e](https://github.com/suitenumerique/conversations/commit/59d8f1e)
- Ajout d'un outil de documentation automatique. [#d26a824](https://github.com/suitenumerique/conversations/commit/d26a824)
- Ajout d'un nouveau modal de paramètres. [#5ca4ef9](https://github.com/suitenumerique/conversations/commit/5ca4ef9)
- Prise en charge de l'analyse des conversations peut maintenant être configurée en lecture seule dans l'admin. [#014cf00](https://github.com/suitenumerique/conversations/commit/014cf00)
- Ajout de la prise en charge du format ODT pour l'importation de documents. [#5ca595b](https://github.com/suitenumerique/conversations/commit/5ca595b)

### Évolutions techniques
- Ajout de configurations Helm supplémentaires pour corriger la configuration de Tilt. [#e9a9cab](https://github.com/suitenumerique/conversations/commit/e9a9cab)
- Refactorisation des tests pour une meilleure maintenabilité. [#ebdb61b](https://github.com/suitenumerique/conversations/commit/ebdb61b) et [#af618c7](https://github.com/suitenumerique/conversations/commit/af618c7)
- Mise à jour des dépendances `lxml` et `pypdf`. [#da740f6](https://github.com/suitenumerique/conversations/commit/da740f6)
- Mise à jour de `pydantic-ai-slim` et d'autres paquets. [#a41c609](https://github.com/suitenumerique/conversations/commit/a41c609)
- Ajout de la prise en charge des modèles open source. [#0606c36](https://github.com/suitenumerique/conversations/commit/0606c36)
- Correction d'un crash de streaming avec les APIs compatibles OpenAI. [#9096d9e](https://github.com/suitenumerique/conversations/commit/9096d9e)
- Ajout d'instructions pour éviter les hallucinations d'URL dans l'agent de conversation. [#3dd7e2f](https://github.com/suitenumerique/conversations/commit/3dd7e2f)
- Obtention des données carbone depuis l'API Albert. [#26a5fa1](https://github.com/suitenumerique/conversations/commit/26a5fa1)

### Autres changements
- Correction de la formulation de la première étape du modal d'onboarding. [#84eebd0](https://github.com/suitenumerique/conversations/commit/84eebd0)
- Correction de la taille maximale du bouton "Nouvelle conversation dans le projet". [#b8b5630](https://github.com/suitenumerique/conversations/commit/b8b5630)
- Suppression de la partie "thinking" pour les modèles qui ne supportent pas le raisonnement. [#6bb3135](https://github.com/suitenumerique/conversations/commit/6bb3135)
- Modification de la valeur par défaut de `allow_smart_web_search` à `False`. [#37a61dc](https://github.com/suitenumerique/conversations/commit/37a61dc)
- Ajout d'un mode debug pour le développement local. [#2c023a7](https://github.com/suitenumerique/conversations/commit/2c023a7)
- Ajout de tests pour le composant `SourceItem`. [#890dc10](https://github.com/suitenumerique/conversations/commit/890dc10)
