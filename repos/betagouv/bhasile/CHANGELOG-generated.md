## Changelog : bhasile (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur l'amélioration significative du parcours de transformation des structures d'hébergement, avec l'ajout de formulaires dédiés, la gestion des validations et l'intégration de nouveaux champs. Des améliorations ont également été apportées aux statistiques, à l'interface utilisateur et à la gestion des documents.

### Évolutions fonctionnelles
- Ajout de la gestion des transformations de structures : création, modification et validation des demandes de transformation. ([#1350](https://github.com/betagouv/bhasile/issues/1350), [#1352](https://github.com/betagouv/bhasile/issues/1352), [#1355](https://github.com/betagouv/bhasile/issues/1355), [#1361](https://github.com/betagouv/bhasile/issues/1361), [#1367](https://github.com/betagouv/bhasile/issues/1367), [#1368](https://github.com/betagouv/bhasile/issues/1368), [#1369](https://github.com/betagouv/bhasile/issues/1369), [#1371](https://github.com/betagouv/bhasile/issues/1371), [#1372](https://github.com/betagouv/bhasile/issues/1372), [#1373](https://github.com/betagouv/bhasile/issues/1373))
- Ajout de formulaires spécifiques pour les actes administratifs, les places et les hébergements dans le cadre des transformations. ([#1342](https://github.com/betagouv/bhasile/issues/1342), [#1343](https://github.com/betagouv/bhasile/issues/1343), [#1345](https://github.com/betagouv/bhasile/issues/1345))
- Amélioration de l'affichage des champs DNA et FINESS lors de la création de structures. ([#1371](https://github.com/betagouv/bhasile/issues/1371))
- Ajout de statistiques sur les types de places et les structures. ([#1337](https://github.com/betagouv/bhasile/issues/1337), [#1360](https://github.com/betagouv/bhasile/issues/1360))
- Ajout de la possibilité d'ajouter des avenants aux transformations. ([#1330](https://github.com/betagouv/bhasile/issues/1330))
- Ajout de logos pour les opérateurs. ([#1286](https://github.com/betagouv/bhasile/issues/1286))
- Ajout d'un nouveau bloc d'activité. ([#1262](https://github.com/betagouv/bhasile/issues/1262))
- Amélioration de l'affichage des dates d'expiration des documents. ([#1295](https://github.com/betagouv/bhasile/issues/1295))

### Évolutions techniques
- Refonte de la gestion des transformations avec l'introduction de `StructureVersion`. ([#1258](https://github.com/betagouv/bhasile/issues/1258))
- Optimisation des performances en déplaçant certaines logiques côté serveur. ([#1272](https://github.com/betagouv/bhasile/issues/1272))
- Amélioration de la configuration du déploiement sur Scalingo. ([#1303](https://github.com/betagouv/bhasile/issues/1303))
- Refactoring du repository de transformation. ([#1280](https://github.com/betagouv/bhasile/issues/1280))
- Ajout de tests E2E pour les nouvelles fonctionnalités. ([#1325](https://github.com/betagouv/bhasile/issues/1325), [#1357](https://github.com/betagouv/bhasile/issues/1357))
- Mise à jour de plusieurs dépendances.

### Autres changements
- Ajout de documentation pour Dependabot. ([#1322](https://github.com/betagouv/bhasile/issues/1322))
- Amélioration de l'accessibilité (a11y). ([#1308](https://github.com/betagouv/bhasile/issues/1308))
- Nettoyage du code et suppression de fichiers de migration obsolètes.
- Amélioration de l'affichage des filiales. ([#1317](https://github.com/betagouv/bhasile/issues/1317))
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
