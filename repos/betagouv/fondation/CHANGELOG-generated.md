## Changelog : fondation (30 derniers jours, au 2026-07-16)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur une refonte architecturale majeure vers une approche "feature-first" pour le frontend, améliorant la maintenabilité et l'évolutivité. De nouvelles fonctionnalités ont été ajoutées pour la gestion des fichiers et des observations, et des corrections ont été apportées pour améliorer la stabilité et l'expérience utilisateur. Des mises à jour de dépendances et des optimisations de performance ont également été réalisées.

### Évolutions fonctionnelles
- Ajout d'un bouton "+" pour ajouter des observations dans la liste des observations. [#497](https://github.com/betagouv/fondation/issues/497)
- Possibilité de joindre des fichiers à une nomination. [#407](https://github.com/betagouv/fondation/issues/407)
- Ajout de la date d'audition du magistrat. [#431](https://github.com/betagouv/fondation/issues/431)
- Amélioration de la gestion des fichiers dans les rapports officiels (suppression des fichiers sans issue, modification de l'introduction des fichiers suspendus). [#462](https://github.com/betagouv/fondation/issues/462), [#463](https://github.com/betagouv/fondation/issues/463)
- Refonte de la présentation des observations avec un panneau latéral dédié. [#474](https://github.com/betagouv/fondation/issues/474)
- Les labels d'issue des fichiers de nomination sont maintenant servis par l'API. [#473](https://github.com/betagouv/fondation/issues/473)
- Suppression du modal de rappel de suivi d'observation lors de la définition d'un résultat. [#493](https://github.com/betagouv/fondation/issues/493)

### Évolutions techniques
- Migration vers Vitest pour les tests unitaires. [#437](https://github.com/betagouv/fondation/issues/437)
- Mise à jour de TypeScript vers la version 6. [#480](https://github.com/betagouv/fondation/issues/480)
- Mise à jour de Prisma vers la version 7. [#481](https://github.com/betagouv/fondation/issues/481)
- Refactorisation du code vers une architecture "feature-first" pour le frontend, améliorant la modularité et la maintenabilité. [#432](https://github.com/betagouv/fondation/issues/432), [#433](https://github.com/betagouv/fondation/issues/433), [#427](https://github.com/betagouv/fondation/issues/427), [#430](https://github.com/betagouv/fondation/issues/430), [#428](https://github.com/betagouv/fondation/issues/428), [#431](https://github.com/betagouv/fondation/issues/431), [#429](https://github.com/betagouv/fondation/issues/429)
- Internalisation des enums et modèles partagés dans l'API pour réduire les dépendances externes. [#490](https://github.com/betagouv/fondation/issues/490), [#491](https://github.com/betagouv/fondation/issues/491), [#483](https://github.com/betagouv/fondation/issues/483), [#485](https://github.com/betagouv/fondation/issues/485), [#486](https://github.com/betagouv/fondation/issues/486)
- Suppression des modèles partagés obsolètes. [#496](https://github.com/betagouv/fondation/issues/496), [#495](https://github.com/betagouv/fondation/issues/495), [#499](https://github.com/betagouv/fondation/issues/499)
- Pré-bundling des dépendances Tipptap pour éviter les problèmes d'optimisation. [#487](https://github.com/betagouv/fondation/issues/487)
- Déplacement des tests E2E de l'API vers un package dédié. [#441](https://github.com/betagouv/fondation/issues/441)
- Utilisation des tokens de couleurs DSFR au lieu des couleurs Tailwind natives. [#418](https://github.com/betagouv/fondation/issues/418)
- Suppression d'un appel obsolète à sheetjs.sh dans le build Scalingo. [#501](https://github.com/betagouv/fondation/issues/501)
- Amélioration de la gestion des caches Vite. [#489](https://github.com/betagouv/fondation/issues/489)

### Autres changements
- Ajout d'une ADR (Architecture Decision Record) pour la nouvelle architecture frontend. [#434](https://github.com/betagouv/fondation/issues/434)
- Refonte des stories MagistratObservations. [#488](https://github.com/betagouv/fondation/issues/488)
- Mise à jour des dépendances (piscina, oxfmt, oxlint, @faker-js/faker, @hey-api/openapi-ts, etc.).
- Correction de problèmes de sélection de fichiers. [#466](https://github.com/betagouv/fondation/issues/466)
- Correction de problèmes de génération de rapports. [#481](https://github.com/betagouv/fondation/issues/481)
- Amélioration de la gestion des erreurs lors de la vérification de l'OpenAPI. [#472](https://github.com/betagouv/fondation/issues/472)
- Ajout d'un composant NewTable virtualisé. [#442](https://github.com/betagouv/fondation/issues/442)
- Suppression de règles de rapport inutilisées. [#494](https://github.com/betagouv/fondation/issues/494)
- Amélioration de la gestion des requêtes Storybook. [#479](https://github.com/betagouv/fondation/issues/479)
- Déploiement de Storybook sur Scalingo. [#477](https://github.com/betagouv/fondation/issues/477)
- Ajout de xlsx en tant que dépendance locale. [#476](https://github.com/betagouv/fondation/issues/476)
- Correction de l'affichage du titre du président. [#465](https://github.com/betagouv/fondation/issues/465)
- Suppression de l'étape sheetjs obsolète du workflow Storybook. [#478](https://github.com/betagouv/fondation/issues/478)
- Correction d'un problème d'affichage des "de" avant les voyelles dans les documents générés. [#444](https://github.com/betagouv/fondation/issues/444)
