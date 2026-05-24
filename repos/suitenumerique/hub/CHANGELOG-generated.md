## Changelog : hub (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, le projet Hub a connu une refonte majeure de son frontend, passant d'une codebase legacy à une nouvelle architecture basée sur Next.js et TypeScript. Cette refonte inclut l'implémentation d'une interface de chat avec une barre latérale et un panneau d'outils, ainsi que l'ajout de la prévisualisation de fichiers. Des améliorations ont également été apportées à l'infrastructure et aux tests.

### Évolutions fonctionnelles
- Ajout d'une interface de chat avec une liste de conversations et une zone de conversation. [#236fb9c](https://github.com/suitenumerique/hub/commit/236fb9c)
- Implémentation d'un panneau d'outils avec une liste de documents. [#e8b1ad0](https://github.com/suitenumerique/hub/commit/e8b1ad0)
- Possibilité de prévisualiser des fichiers (PDF, images, vidéos, audio) dans le panneau d'outils. [#c3a9df4](https://github.com/suitenumerique/hub/commit/c3a9df4)
- Ajout d'un sélecteur de compte avec support pour Gaufre et UserProfile. [#9d1cd7e](https://github.com/suitenumerique/hub/commit/9d1cd7e)
- Ajout d'un composant Avatar. [#7a770db](https://github.com/suitenumerique/hub/commit/7a770db)

### Évolutions techniques
- Refonte complète du frontend avec Next.js et TypeScript. [#b138a46](https://github.com/suitenumerique/hub/commit/b138a46)
- Mise à jour de la configuration et des outils de build. [#a075378](https://github.com/suitenumerique/hub/commit/a075378)
- Consolidation du stack Docker et de la base de données pour les tests E2E. [#6aa53a3](https://github.com/suitenumerique/hub/commit/6aa53a3)
- Ajout de fixtures et de routes de test E2E pour le backend. [#4e888c5](https://github.com/suitenumerique/hub/commit/4e888c5)
- Mise à jour de la configuration Playwright et des dépendances. [#7e6e6ae](https://github.com/suitenumerique/hub/commit/7e6e6ae)
- Suppression de l'ancienne codebase frontend. [#88c31b5](https://github.com/suitenumerique/hub/commit/88c31b5)
- Suppression des anciens tests E2E. [#f679994](https://github.com/suitenumerique/hub/commit/f679994)
- Mise à jour des workflows CI/CD. [#fc4a041](https://github.com/suitenumerique/hub/commit/fc4a041)
- Mise à jour de la configuration i18n et des traductions. [#f679e1d](https://github.com/suitenumerique/hub/commit/f679e1d)

### Autres changements
- Ajout d'Architecture Decision Records (ADR). [#3c75b8c](https://github.com/suitenumerique/hub/commit/3c75b8c)
- Ajustement du fichier README.md pour Docker. [#57adfb6](https://github.com/suitenumerique/hub/commit/57adfb6)
- Ajout d'assets publics. [#da95319](https://github.com/suitenumerique/hub/commit/da95319)
- Ajout de hooks, d'utilitaires et de styles globaux. [#c5d2ab1](https://github.com/suitenumerique/hub/commit/c5d2ab1)
- Ajout des fonctionnalités de base (authentification, API, configuration, drivers, gestion des erreurs). [#b138a46](https://github.com/suitenumerique/hub/commit/b138a46)
- Correction du routage Nginx pour l'export statique. [#48f818b](https://github.com/suitenumerique/hub/commit/48f818b)
- Mise à jour des packages i18n et des dépendances root. [#43ea40f](https://github.com/suitenumerique/hub/commit/43ea40f)
- Suppression du package eslint-plugin-docs. [#307582d](https://github.com/suitenumerique/hub/commit/307582d)
