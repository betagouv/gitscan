## Changelog : conversations (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur avec une nouvelle interface pour l'en-tête et des corrections d'interface, ainsi que sur l'ajout de nouvelles fonctionnalités comme l'authentification silencieuse via OIDC et la prise en charge de nouveaux formats de documents (ODT). Des améliorations techniques ont également été apportées, notamment le support de modèles open source et l'optimisation des performances.

### Évolutions fonctionnelles
- Ajout de l'authentification silencieuse via OIDC [#59d8f1e](https://github.com/suitenumerique/conversations/commit/59d8f1e)
- Prise en charge de l'analyse des documents ODT et amélioration du routage des documents [#5ca595b](https://github.com/suitenumerique/conversations/commit/5ca595b)
- Nouvelle interface utilisateur pour l'en-tête [#77b9b44](https://github.com/suitenumerique/conversations/commit/77b9b44)
- Possibilité de copier du texte formaté (rich text) dans Word ou d'autres éditeurs [#e0e1943](https://github.com/suitenumerique/conversations/commit/e0e1943)
- Amélioration de la gestion des projets avec la possibilité d'utiliser des instructions LLM personnalisées.
- Ajout d'une interface utilisateur pour la gestion des projets.
- Possibilité de taper pendant que le LLM génère une réponse [#42228d7](https://github.com/suitenumerique/conversations/commit/42228d7)
- Intégration de snippets de contexte et de LLM de Brave pour la recherche web [#cb2bfd5](https://github.com/suitenumerique/conversations/commit/cb2bfd5)
- Support pour les modèles open source [#0606c36](https://github.com/suitenumerique/conversations/commit/0606c36)

### Évolutions techniques
- Refactor des tests backend [#ebdb61b](https://github.com/suitenumerique/conversations/commit/ebdb61b)
- Mise à jour de Next.js de la version 15 à la version 16 et des dépendances Python [#9e37f71](https://github.com/suitenumerique/conversations/commit/9e37f71)
- Mise à jour de Pydantic AI et d'autres paquets [#a41c609](https://github.com/suitenumerique/conversations/commit/a41c609)
- Ajout d'un mode débogage pour le développement local [#2c023a7](https://github.com/suitenumerique/conversations/commit/2c023a7)
- Suppression des outils de recherche hérités de la configuration du modèle [#4f4c1b9](https://github.com/suitenumerique/conversations/commit/4f4c1b9)
- Obtention des données carbone à partir de l'API Albert [#26a5fa1](https://github.com/suitenumerique/conversations/commit/26a5fa1)
- Ajout de linting supplémentaire en frontend [#96a5920](https://github.com/suitenumerique/conversations/commit/96a5920)

### Autres changements
- Correction de la taille maximale du bouton "nouvelle conversation dans le projet" [#b8b5630](https://github.com/suitenumerique/conversations/commit/b8b5630)
- Mise à jour des descriptions des outils [#a9f667b](https://github.com/suitenumerique/conversations/commit/a9f667b)
- Correction de l'ouverture des liens sources dans un nouvel onglet [#5183bc4](https://github.com/suitenumerique/conversations/commit/5183bc4)
- Correction d'un bug lié à la langue anglaise forcée dans les tests E2E [#74e3da7](https://github.com/suitenumerique/conversations/commit/74e3da7)
- Correction d'un bug d'i18n pour le 1er avril [#47850f6](https://github.com/suitenumerique/conversations/commit/47850f6)
- Mise à jour des chaînes de caractères traduites [#f71ced5](https://github.com/suitenumerique/conversations/commit/f71ced5)
- Correction de problèmes d'UI pour les projets et les boutons [#dd61735](https://github.com/suitenumerique/conversations/commit/dd61735), [#c0fc6be](https://github.com/suitenumerique/conversations/commit/c0fc6be), [#72c80fd](https://github.com/suitenumerique/conversations/commit/72c80fd)
- Ajout d'une blague pour le 1er avril [#1133f57](https://github.com/suitenumerique/conversations/commit/1133f57)
- Correction de l'affichage des couleurs dans le mode sombre.
- Correction de bugs mineurs d'UI.
