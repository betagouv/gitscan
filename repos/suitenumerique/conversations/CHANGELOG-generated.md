## Changelog : conversations (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout d'un onboarding guidé, l'amélioration de la gestion des documents (prise en charge de nouveaux formats et contexte hybride), et des corrections de bugs pour une meilleure stabilité. Des améliorations techniques ont également été apportées, notamment l'ajout de la prise en charge de modèles open source et l'optimisation de la sécurité avec l'ajout de la connexion OIDC silencieuse.

### Évolutions fonctionnelles
- Ajout d'un tutoriel d'onboarding pour guider les nouveaux utilisateurs [#8b2321d](https://github.com/suitenumerique/conversations/commit/8b2321d).
- Amélioration de la gestion des documents avec la prise en charge du format ODT et une meilleure intégration du contexte documentaire [#5ca595b](https://github.com/suitenumerique/conversations/commit/5ca595b).
- Implémentation d'un contexte hybride pour les documents, améliorant la pertinence des réponses [#2bde1bb](https://github.com/suitenumerique/conversations/commit/2bde1bb).
- Ajout d'un outil d'auto-documentation pour faciliter l'utilisation des fonctionnalités [#d26a824](https://github.com/suitenumerique/conversations/commit/d26a824).
- Ajout de la connexion OIDC silencieuse pour une expérience utilisateur plus fluide [#59d8f1e](https://github.com/suitenumerique/conversations/commit/59d8f1e).
- Amélioration de l'interface utilisateur avec un nouveau header [#77b9b44](https://github.com/suitenumerique/conversations/commit/77b9b44).
- Correction de l'affichage des liens sources pour qu'ils s'ouvrent dans un nouvel onglet [#5183bc4](https://github.com/suitenumerique/conversations/commit/5183bc4).

### Évolutions techniques
- Prise en charge des modèles open source [#0606c36](https://github.com/suitenumerique/conversations/commit/0606c36).
- Refactoring des tests pour améliorer la maintenabilité [#ebdb61b](https://github.com/suitenumerique/conversations/commit/ebdb61b).
- Mise à jour des dépendances `lxml` et `pypdf` [#da740f6](https://github.com/suitenumerique/conversations/commit/da740f6).
- Mise à jour des dépendances back et front pour corriger des vulnérabilités (CVEs) [#2496098](https://github.com/suitenumerique/conversations/commit/2496098).
- Correction d'un crash en streaming avec les APIs compatibles OpenAI [#9096d9e](https://github.com/suitenumerique/conversations/commit/9096d9e).
- Correction du stripping de la partie "thinking" pour les modèles sans support de raisonnement [#6bb3135](https://github.com/suitenumerique/conversations/commit/6bb3135).
- Ajout d'un mode debug pour le développement local [#2c023a7](https://github.com/suitenumerique/conversations/commit/2c023a7).
- Mise à jour de `pydantic-ai` et d'autres paquets [#a41c609](https://github.com/suitenumerique/conversations/commit/a41c609).
- Modification de `allow_smart_web_search` à `False` par défaut [#37a61dc](https://github.com/suitenumerique/conversations/commit/37a61dc).
- Rendre le paramètre `allow_conversation_analytics` non modifiable dans l'admin [#014cf00](https://github.com/suitenumerique/conversations/commit/014cf00).

### Autres changements
- Correction du texte de la première étape du tutoriel [#84eebd0](https://github.com/suitenumerique/conversations/commit/84eebd0).
- Correction de la taille maximale du bouton "Nouvelle conversation dans un projet" [#b8b5630](https://github.com/suitenumerique/conversations/commit/b8b5630).
- Ajout de tests pour le composant `SourceItem` [#890dc10](https://github.com/suitenumerique/conversations/commit/890dc10).
- Correction de la marge supérieure dans l'interface utilisateur [#f28c468](https://github.com/suitenumerique/conversations/commit/f28c468).
- Amélioration de l'interface utilisateur pour une partie du projet [#63c8e77](https://github.com/suitenumerique/conversations/commit/63c8e77).
- Mise à jour des descriptions des outils [#a9f667b](https://github.com/suitenumerique/conversations/commit/a9f667b).
- Ajout de nouvelles instructions à tous les tests [#af618c7](https://github.com/suitenumerique/conversations/commit/af618c7).
