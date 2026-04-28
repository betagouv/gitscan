## Changelog : docs (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de l'expérience utilisateur, notamment en matière de gestion de contenu, de performance et d'accessibilité. Des optimisations ont été apportées au backend pour la gestion des fichiers et des requêtes, tandis que le frontend a bénéficié de corrections de bugs et d'améliorations de l'interface utilisateur, notamment pour les liens internes et la navigation. L'accessibilité a également été renforcée avec des améliorations pour les lecteurs d'écran et la navigation au clavier.

### Évolutions fonctionnelles
- Ajout du support hors ligne pour le contenu via Service Workers [#4d250a7](https://github.com/suitenumerique/docs/commit/4d250a7).
- Intégration d'un lien vers la documentation dans le menu d'aide [#ee90443](https://github.com/suitenumerique/docs/commit/ee90443).
- Ajout d'un easter egg pour la création d'emojis dans les documents [#45fac1e](https://github.com/suitenumerique/docs/commit/45fac1e).
- Possibilité d'ouvrir les liens internes (interlinks) avec le bouton central de la souris ou les touches Ctrl/Cmd [#4dcf752](https://github.com/suitenumerique/docs/commit/4dcf752).
- Ajout d'un indicateur visuel pour les liens internes [#c20e71e](https://github.com/suitenumerique/docs/commit/c20e71e).
- Amélioration de l'expérience utilisateur pour la gestion des membres sur les petits écrans [#599b909](https://github.com/suitenumerique/docs/commit/599b909).

### Évolutions techniques
- Mise à jour de Docspec vers la version 3.0.0 et adaptation de l'API de conversion [#2d2e326](https://github.com/suitenumerique/docs/commit/2d2e326).
- Refonte de l'architecture pour la gestion du contenu, avec des endpoints dédiés pour la mise à jour et la récupération du contenu [#d7a186a](https://github.com/suitenumerique/docs/commit/d7a186a, #6f2cd8a](https://github.com/suitenumerique/docs/commit/6f2cd8a, #207f214](https://github.com/suitenumerique/docs/commit/207f214).
- Mise en place de headers ETag et Last-Modified pour optimiser la récupération du contenu [#6f2cd8a](https://github.com/suitenumerique/docs/commit/6f2cd8a).
- Utilisation d'Uvicorn pour exécuter l'application Django en environnement de développement [#ef93763](https://github.com/suitenumerique/docs/commit/ef93763).
- Factorisation des tests E2E dans un workflow séparé [#d933435](https://github.com/suitenumerique/docs/commit/d933435).
- Amélioration de la gestion des erreurs 5xx avec une page dédiée et une structure améliorée [#9a5d81f](https://github.com/suitenumerique/docs/commit/9a5d81f, #31fea43](https://github.com/suitenumerique/docs/commit/31fea43).
- Mise en place d'un système de feature flags pour l'import de documents [#f166e75](https://github.com/suitenumerique/docs/commit/f166e75).

### Autres changements
- Ajout d'une liste des changements incompatibles (breaking changes) dans le fichier UPGRADE.md [#1c2bafb](https://github.com/suitenumerique/docs/commit/1c2bafb).
- Mise à jour des dépendances lxml, axios et next avec des correctifs de sécurité [#e747e03](https://github.com/suitenumerique/docs/commit/e747e03, #0060c59](https://github.com/suitenumerique/docs/commit/0060c59, #48fb17b](https://github.com/suitenumerique/docs/commit/48fb17b).
- Corrections de typos dans le fichier contributing.md [#30ed563](https://github.com/suitenumerique/docs/commit/30ed563).
- Amélioration de l'accessibilité des étiquettes des résultats de recherche de documents [#e59d8a4](https://github.com/suitenumerique/docs/commit/e59d8a4).
- Ajout d'un checklist IA au template de PR et refonte de la documentation contributing.md [#d0bf24f](https://github.com/suitenumerique/docs/commit/d0bf24f, #2da87ba](https://github.com/suitenumerique/docs/commit/2da87ba).
- Mise à jour des chaînes de traduction [#e2d0e7c](https://github.com/suitenumerique/docs/commit/e2d0e7c).
- Suppression de l'endpoint descendants déprécié [#5e22bc4](https://github.com/suitenumerique/docs/commit/5e22bc4).
