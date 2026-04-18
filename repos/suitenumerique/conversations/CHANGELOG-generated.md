## Changelog : conversations (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec une nouvelle interface pour l'en-tête et des corrections d'interface, ainsi que sur l'ajout de nouvelles fonctionnalités comme l'authentification silencieuse via OIDC, la prise en charge de l'analyse de fichiers ODT et l'intégration de modèles open source. Des améliorations techniques ont également été apportées, notamment des mises à jour de dépendances pour corriger des vulnérabilités et optimiser les performances.

### Évolutions fonctionnelles
- Ajout de l'authentification silencieuse via OIDC [#59d8f1e](https://github.com/suitenumerique/conversations/commit/59d8f1e).
- Prise en charge de l'analyse de fichiers ODT et amélioration du routage des documents [#5ca595b](https://github.com/suitenumerique/conversations/commit/5ca595b).
- Ajout de la possibilité de copier du texte formaté dans Word/Docs [#e0e1943](https://github.com/suitenumerique/conversations/commit/e0e1943).
- Nouvelle interface utilisateur pour l'en-tête [#77b9b44](https://github.com/suitenumerique/conversations/commit/77b9b44).
- Possibilité de taper pendant que le LLM génère une réponse [#42228d7](https://github.com/suitenumerique/conversations/commit/42228d7).
- Ajout de la prise en charge de modèles open source [#0606c36](https://github.com/suitenumerique/conversations/commit/0606c36).
- Intégration de snippets de recherche Brave [#cb2bfd5](https://github.com/suitenumerique/conversations/commit/cb2bfd5).

### Évolutions techniques
- Refactorisation des tests backend [#ebdb61b](https://github.com/suitenumerique/conversations/commit/ebdb61b).
- Mise à jour de pydantic-ai-slim et d'autres dépendances [#a41c609](https://github.com/suitenumerique/conversations/commit/a41c609).
- Mise à jour des dépendances backend et frontend pour corriger des CVEs [#2496098](https://github.com/suitenumerique/conversations/commit/2496098).
- Mise à jour de Next.js de la version 15 à la version 16 [#9e37f71](https://github.com/suitenumerique/conversations/commit/9e37f71).
- Suppression des outils de recherche legacy de la configuration du modèle [#4f4c1b9](https://github.com/suitenumerique/conversations/commit/4f4c1b9).
- Ajout d'un mode debug pour le développement local [#2c023a7](https://github.com/suitenumerique/conversations/commit/2c023a7).

### Autres changements
- Mise à jour des descriptions des outils [#a9f667b](https://github.com/suitenumerique/conversations/commit/a9f667b).
- Correction de la taille maximale du bouton "nouvelle conversation dans un projet" [#b8b5630](https://github.com/suitenumerique/conversations/commit/b8b5630).
- Correction de l'ouverture des liens sources dans un nouvel onglet [#5183bc4](https://github.com/suitenumerique/conversations/commit/5183bc4).
- Ajout d'un prank pour le 1er avril [#1133f57](https://github.com/suitenumerique/conversations/commit/1133f57).
- Mise à jour des chaînes de caractères traduites [#f71ced5](https://github.com/suitenumerique/conversations/commit/f71ced5).
- Correction d'un bug lié à l'internationalisation du prank du 1er avril [#47850f6](https://github.com/suitenumerique/conversations/commit/47850f6).
- Ajout de linting supplémentaire [#96a5920](https://github.com/suitenumerique/conversations/commit/96a5920).
- Correction de petits problèmes d'interface utilisateur (marges, CSS, sélecteur de modèle) [#787444c](https://github.com/suitenumerique/conversations/commit/787444c), [#72c80fd](https://github.com/suitenumerique/conversations/commit/72c80fd), [#c0fc6be](https://github.com/suitenumerique/conversations/commit/c0fc6be).
- Force la langue anglaise avant les tests du panneau de gauche [#74e3da7](https://github.com/suitenumerique/conversations/commit/74e3da7).
- Correction de la couleur du bouton de feedback [#f28c468](https://github.com/suitenumerique/conversations/commit/f28c468).
