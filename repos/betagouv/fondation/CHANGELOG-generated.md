## Changelog : fondation (30 derniers jours, au 13 juillet 2026)

### Résumé
Cette période a été marquée par une refonte architecturale majeure de l'interface utilisateur vers une approche "feature-first", améliorant la maintenabilité et l'évolutivité du projet. De nouvelles fonctionnalités ont été ajoutées concernant la gestion des fichiers de nomination et des observations, tandis que des corrections et des améliorations ont été apportées à l'expérience utilisateur et à la sécurité.

### Évolutions fonctionnelles
- Possibilité d'attacher des fichiers aux dossiers de nomination. [#407](https://github.com/betagouv/fondation/issues/407)
- Ajout de la date d'audition du magistrat. [#463](https://github.com/betagouv/fondation/issues/463)
- Amélioration de l'affichage des observations, désormais dans un panneau latéral. [#474](https://github.com/betagouv/fondation/issues/474)
- Les labels d'issue des fichiers de nomination sont maintenant servis par l'API. [#473](https://github.com/betagouv/fondation/issues/473)
- Réintégration des observateurs "legacy". [#464](https://github.com/betagouv/fondation/issues/464)
- Amélioration de la gestion des fichiers dans les rapports officiels (suppression des fichiers sans issue, modification de l'introduction des fichiers suspendus). [#462](https://github.com/betagouv/fondation/issues/462), [#463](https://github.com/betagouv/fondation/issues/463)
- Correction pour permettre l'importation correcte des fichiers LOLFI. [#417](https://github.com/betagouv/fondation/issues/417)
- Correction pour autoriser les positions actuelles de nomination inconnues. [#416](https://github.com/betagouv/fondation/issues/416)

### Évolutions techniques
- Refonte de l'architecture frontale vers une approche "feature-first" pour une meilleure organisation et maintenabilité du code. [#432](https://github.com/betagouv/fondation/issues/432), [#433](https://github.com/betagouv/fondation/issues/433), [#428](https://github.com/betagouv/fondation/issues/428), [#431](https://github.com/betagouv/fondation/issues/431), [#430](https://github.com/betagouv/fondation/issues/430), [#429](https://github.com/betagouv/fondation/issues/429), [#427](https://github.com/betagouv/fondation/issues/427)
- Migration des tests vers Vitest. [#437](https://github.com/betagouv/fondation/issues/437)
- Déplacement des tests E2E de l'API vers un package dédié. [#441](https://github.com/betagouv/fondation/issues/441)
- Mise à jour des dépendances : `@faker-js/faker`, `@hey-api/openapi-ts`, `oxlint-tsgolint`, `piscina`, `vite`, `react`.
- Mise à jour des versions de NestJS, S3 et Puppeteer.
- Utilisation des tokens de couleurs DSFR au lieu des couleurs Tailwind natives. [#418](https://github.com/betagouv/fondation/issues/418)
- Suppression des dépendances inutilisées.
- Amélioration de la gestion des migrations de base de données. [#443](https://github.com/betagouv/fondation/issues/443)
- Ajout de barrels d'index dans le répertoire `shared`. [#440](https://github.com/betagouv/fondation/issues/440)
- Ajout d'une documentation ADR pour l'architecture frontale "feature-first". [#434](https://github.com/betagouv/fondation/issues/434)
- Amélioration de la gestion des colonnes de transparence en les déplaçant vers une table spécifique. [#445](https://github.com/betagouv/fondation/issues/445)

### Autres changements
- Configuration pour échouer les builds si les clients OpenAPI générés divergent du contrat. [#472](https://github.com/betagouv/fondation/issues/472)
- Correction d'un problème d'affichage des "de" avant une voyelle dans les documents générés. [#444](https://github.com/betagouv/fondation/issues/444)
- Correction d'un bug empêchant la sélection de fichiers désactivés. [#466](https://github.com/betagouv/fondation/issues/466)
- Correction du titre du président dans l'introduction. [#465](https://github.com/betagouv/fondation/issues/465)
- Correction d'un problème de mémoire avec Renovate. [#420](https://github.com/betagouv/fondation/issues/420)
- Organisation du projet Renovate en plusieurs projets. [#457](https://github.com/betagouv/fondation/issues/457)
- Ajout d'un composant `NewTable` virtualisé pour les tableaux. [#442](https://github.com/betagouv/fondation/issues/442)
- Correction d'un problème lié à l'indexation de `archivedAt` dans le schéma de session. [#415](https://github.com/betagouv/fondation/issues/415)
