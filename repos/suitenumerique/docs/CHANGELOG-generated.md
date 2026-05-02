## Changelog : docs (30 derniers jours, au 2026-04-30)

### Résumé
Les dernières mises à jour se concentrent sur l'intégration de nouvelles fonctionnalités d'intelligence artificielle via Mistral SDK, l'amélioration de la gestion du contenu (streaming, endpoints dédiés) et des corrections de bugs pour une meilleure expérience utilisateur et une sécurité renforcée. Des améliorations d'accessibilité ont également été apportées.

### Évolutions fonctionnelles
- Intégration de nouvelles fonctionnalités d'IA via le SDK Mistral, permettant d'utiliser des modèles de langage avancés. [#33a9e99](https://github.com/suitenumerique/docs/commit/33a9e99)
- Ajout d'un lien vers la documentation dans le menu d'aide. [#ee90443](https://github.com/suitenumerique/docs/commit/ee90443)
- Intégration de Crisp (chat d'assistance) accessible depuis le menu d'aide. [#572074d](https://github.com/suitenumerique/docs/commit/572074d)
- Possibilité de configurer l'URI de la requête d'authentification forward. [#394fbc5](https://github.com/suitenumerique/docs/commit/394fbc5)
- Amélioration de l'ordre d'affichage des documents épinglés (tri par date de dernière mise à jour). [#e652cdd](https://github.com/suitenumerique/docs/commit/e652cdd)
- Ajout d'un support hors-ligne pour le contenu via Service Workers. [#ff2c61a](https://github.com/suitenumerique/docs/commit/ff2c61a)
- Mise en cache du contenu et des métadonnées pour les requêtes API via Service Workers. [#4d250a7](https://github.com/suitenumerique/docs/commit/4d250a7)

### Évolutions techniques
- Mise à jour de l'image Nginx vers la dernière version. [#4fe508b](https://github.com/suitenumerique/docs/commit/4fe508b)
- Refonte de l'architecture de gestion du contenu : création d'endpoints dédiés pour la mise à jour et le streaming du contenu. [#6b3d197](https://github.com/suitenumerique/docs/commit/6b3d197, #d7a186a](https://github.com/suitenumerique/docs/commit/d7a186a, #207f214](https://github.com/suitenumerique/docs/commit/207f214)
- Suppression de l'endpoint `descendants` obsolète. [#5e22bc4](https://github.com/suitenumerique/docs/commit/5e22bc4)
- Mise à jour de Docspec vers la version 3.0.0 et adaptation de l'API du convertisseur. [#2d2e326](https://github.com/suitenumerique/docs/commit/2d2e326)
- Utilisation d'Uvicorn pour exécuter l'application Django en environnement de développement. [#ef93763](https://github.com/suitenumerique/docs/commit/ef93763)
- Amélioration de la gestion des erreurs 5xx avec une structure plus accessible. [#9a5d81f](https://github.com/suitenumerique/docs/commit/9a5d81f)
- Refactorisation des tests E2E pour une meilleure organisation et compatibilité. [#d933435](https://github.com/suitenumerique/docs/commit/d933435)
- Ajout de vérifications de sécurité et mises à jour de dépendances (axios, lodash, next, uuid, lxml). [#0060c59](https://github.com/suitenumerique/docs/commit/0060c59, #48fb17b](https://github.com/suitenumerique/docs/commit/48fb17b, #be38e68](https://github.com/suitenumerique/docs/commit/be38e68, #c464715](https://github.com/suitenumerique/docs/commit/c464715)

### Autres changements
- Correction d'une vulnérabilité de sécurité JavaScript. [#fa9d56d](https://github.com/suitenumerique/docs/commit/fa9d56d)
- Corrections de bugs liés à la gestion des interlinks (modal clipping, positionnement). [#c20e71e](https://github.com/suitenumerique/docs/commit/c20e71e, #b3dd8f2](https://github.com/suitenumerique/docs/commit/b3dd8f2)
- Améliorations de l'accessibilité (gestion des lecteurs d'écran, labels, titres). [#a2860e8](https://github.com/suitenumerique/docs/commit/a2860e8, #e59d8a4](https://github.com/suitenumerique/docs/commit/e59d8a4)
- Corrections de bugs divers (tests, gestion des médias, validation des emojis, etc.). [#487d0b1](https://github.com/suitenumerique/docs/commit/487d0b1, #cfd1fd0](https://github.com/suitenumerique/docs/commit/cfd1fd0, #37091ca](https://github.com/suitenumerique/docs/commit/37091ca, #7df5aba](https://github.com/suitenumerique/docs/commit/7df5aba)
- Mise à jour de la documentation (PR template, contributing.md, ajout de la politique IA). [#d0bf24f](https://github.com/suitenumerique/docs/commit/d0bf24f, #2da87ba](https://github.com/suitenumerique/docs/commit/2da87ba, #30ed563](https://github.com/suitenumerique/docs/commit/30ed563)
- Ajout d'un fichier `UPGRADE.md` pour documenter les changements majeurs et les incompatibilités. [#1c2bafb](https://github.com/suitenumerique/docs/commit/1c2bafb)
