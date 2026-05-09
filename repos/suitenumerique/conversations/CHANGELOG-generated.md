## Changelog : conversations (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout d'un tutoriel d'onboarding, l'amélioration de la recherche documentaire avec un contexte hybride, et l'ajout de support pour de nouveaux formats de documents (ODT). Des corrections de bugs et des optimisations de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un tutoriel d'onboarding pour guider les nouveaux utilisateurs. [#8b2321d](https://github.com/suitenumerique/conversations/commit/8b2321d)
- Amélioration du contexte documentaire en utilisant une approche hybride. [#2bde1bb](https://github.com/suitenumerique/conversations/commit/2bde1bb)
- Ajout du support pour l'analyse de documents au format ODT. [#5ca595b](https://github.com/suitenumerique/conversations/commit/5ca595b)
- Implémentation d'une connexion OIDC silencieuse pour une meilleure expérience utilisateur. [#59d8f1e](https://github.com/suitenumerique/conversations/commit/59d8f1e)
- Ajout d'un outil d'auto-documentation pour faciliter l'utilisation des fonctionnalités. [#d26a824](https://github.com/suitenumerique/conversations/commit/d26a824)
- Ajout de support pour les modèles open source. [#0606c36](https://github.com/suitenumerique/conversations/commit/0606c36)
- Amélioration de la gestion des liens dans les sources, qui s'ouvrent désormais dans un nouvel onglet. [#5183bc4](https://github.com/suitenumerique/conversations/commit/5183bc4)

### Évolutions techniques
- Refactorisation des tests pour une meilleure maintenabilité. [#ebdb61b](https://github.com/suitenumerique/conversations/commit/ebdb61b)
- Mise à jour des dépendances `lxml` et `pypdf`. [#da740f6](https://github.com/suitenumerique/conversations/commit/da740f6)
- Mise à jour des dépendances frontend et backend pour corriger des vulnérabilités (CVE). [#2496098](https://github.com/suitenumerique/conversations/commit/2496098)
- Amélioration de la gestion des erreurs lors du streaming avec les APIs compatibles OpenAI. [#9096d9e](https://github.com/suitenumerique/conversations/commit/9096d9e)
- Ajout d'un mode debug pour faciliter le développement local. [#2c023a7](https://github.com/suitenumerique/conversations/commit/2c023a7)
- Modification du paramètre par défaut de `allow_smart_web_search` à `False`. [#37a61dc](https://github.com/suitenumerique/conversations/commit/37a61dc)
- Le paramètre `allow_conversation_analytics` est maintenant en lecture seule dans l'interface d'administration. [#014cf00](https://github.com/suitenumerique/conversations/commit/014cf00)
- Suppression de la partie "thinking" pour les modèles qui ne supportent pas le raisonnement. [#6bb3135](https://github.com/suitenumerique/conversations/commit/6bb3135)
- Ajout d'instructions pour prévenir les hallucinations d'URL dans l'agent de conversation. [#3dd7e2f](https://github.com/suitenumerique/conversations/commit/3dd7e2f)

### Autres changements
- Correction du texte d'une étape du tutoriel d'onboarding. [#84eebd0](https://github.com/suitenumerique/conversations/commit/84eebd0)
- Correction de la taille maximale du bouton "Nouvelle conversation dans un projet". [#b8b5630](https://github.com/suitenumerique/conversations/commit/b8b5630)
- Mise à jour des descriptions des outils. [#a9f667b](https://github.com/suitenumerique/conversations/commit/a9f667b)
- Amélioration de l'interface utilisateur pour le projet. [#63c8e77](https://github.com/suitenumerique/conversations/commit/63c8e77)
- Correction du style du codeblock en mode clair. [#f28c468](https://github.com/suitenumerique/conversations/commit/f28c468)
- Ajout de tests pour le composant `SourceItem`. [#890dc10](https://github.com/suitenumerique/conversations/commit/890dc10)
