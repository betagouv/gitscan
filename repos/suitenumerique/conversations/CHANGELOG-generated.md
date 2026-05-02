## Changelog : conversations (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des documents (ajout du support ODT), l'authentification (connexion OIDC silencieuse), et l'ajout d'un outil d'auto-documentation. Des corrections de bugs ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment concernant le rendu du streaming et l'ouverture des liens sources.

### Évolutions fonctionnelles
- Ajout du support pour l'analyse des fichiers ODT (OpenDocument Text) et amélioration du routage des documents. [#5ca595b](https://github.com/suitenumerique/conversations/commit/5ca595b)
- Implémentation d'une connexion OIDC (OpenID Connect) silencieuse pour une expérience utilisateur plus fluide. [#59d8f1e](https://github.com/suitenumerique/conversations/commit/59d8f1e)
- Ajout d'un outil d'auto-documentation pour faciliter la compréhension et l'utilisation du projet. [#d26a824](https://github.com/suitenumerique/conversations/commit/d26a824)
- Amélioration de l'interface utilisateur pour les projets, notamment la taille maximale du bouton "nouvelle conversation". [#b8b5630](https://github.com/suitenumerique/conversations/commit/b8b5630)
- Nouvelle interface utilisateur pour l'en-tête de l'application. [#77b9b44](https://github.com/suitenumerique/conversations/commit/77b9b44)
- Les liens sources s'ouvrent désormais dans un nouvel onglet. [#5183bc4](https://github.com/suitenumerique/conversations/commit/5183bc4)
- Ajout du support pour les modèles open source. [#0606c36](https://github.com/suitenumerique/conversations/commit/0606c36)

### Évolutions techniques
- Correction d'un crash lié au streaming avec les APIs compatibles OpenAI. [#9096d9e](https://github.com/suitenumerique/conversations/commit/9096d9e)
- Refactorisation des tests pour améliorer leur maintenance et leur lisibilité. [#ebdb61b](https://github.com/suitenumerique/conversations/commit/ebdb61b)
- Mise à jour des dépendances `pydantic-ai-slim` et autres packages pour bénéficier des dernières corrections et améliorations. [#a41c609](https://github.com/suitenumerique/conversations/commit/a41c609)
- Mise à jour des dépendances backend et frontend pour corriger des vulnérabilités (CVE). [#2496098](https://github.com/suitenumerique/conversations/commit/2496098)
- Ajout d'un mode débogage pour faciliter le développement local. [#2c023a7](https://github.com/suitenumerique/conversations/commit/2c023a7)
- Mise à jour des dépendances `lxml` et `pypdf`. [#da740f6](https://github.com/suitenumerique/conversations/commit/da740f6)
- Ajout de tests pour le composant `SourceItem` en frontend. [#890dc10](https://github.com/suitenumerique/conversations/commit/890dc10)
- Ajout de linting supplémentaire en frontend. [#96a5920](https://github.com/suitenumerique/conversations/commit/96a5920)

### Autres changements
- Correction de tests et ajout d'instructions pour tous les tests. [#af618c7](https://github.com/suitenumerique/conversations/commit/af618c7)
- Mise à jour des descriptions des outils. [#a9f667b](https://github.com/suitenumerique/conversations/commit/a9f667b)
- Récupération des données carbone depuis l'API Albert. [#26a5fa1](https://github.com/suitenumerique/conversations/commit/26a5fa1)
- Correction d'un problème de langue forcée en anglais avant les tests du panneau latéral. [#74e3da7](https://github.com/suitenumerique/conversations/commit/74e3da7)
- Amélioration de l'interface utilisateur pour la partie projet. [#63c8e77](https://github.com/suitenumerique/conversations/commit/63c8e77)
- Correction du style du codeblock en mode clair. [#f28c468](https://github.com/suitenumerique/conversations/commit/f28c468)
