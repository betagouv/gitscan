## Changelog : envergo (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur, notamment sur les pages d'instruction et de création de dossiers, ainsi que par des corrections de bugs et des optimisations de performance. Des efforts ont également été déployés pour améliorer la gestion des données, en particulier concernant les haies, les plantations et les données Natura 2000.

### Évolutions fonctionnelles
- Amélioration de l'expérience utilisateur sur la page d'instruction avec l'ajout de notes privées et une refonte de l'interface. [#1113](https://github.com/MTES-MCT/envergo/issues/1113)
- Refonte de la page d'accueil avec un nouveau sélecteur de département et l'affichage d'informations contextuelles. [#1187](https://github.com/MTES-MCT/envergo/issues/1187)
- Ajout d'une fonctionnalité d'archivage des données DN (Démarche Numérique). [#1177](https://github.com/MTES-MCT/envergo/issues/1177)
- Amélioration de la gestion des coefficients et des données de configuration. [#1169](https://github.com/MTES-MCT/envergo/issues/1169)
- Ajout d'une procédure d'urgence pour la gestion des dossiers. [#1174](https://github.com/MTES-MCT/envergo/issues/1174)
- Correction d'un bug empêchant l'affichage correct des liens dans les notes d'instruction. [#1182](https://github.com/MTES-MCT/envergo/issues/1182)
- Amélioration de l'affichage des cartes de densité. [#1147](https://github.com/MTES-MCT/envergo/issues/1147)
- Ajout de la possibilité de créer des critères Natura 2000. [#1192](https://github.com/MTES-MCT/envergo/issues/1192)
- Correction d'un problème lié à l'importation multiple de données. [#1143](https://github.com/MTES-MCT/envergo/issues/1143)

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Mise à jour des dépendances (Playwright, Node.js).
- Amélioration de la gestion des tests, notamment pour les tests E2E.
- Correction de problèmes de performance liés à l'upload de fichiers. [#283587](https://github.com/MTES-MCT/envergo/issues/283587)
- Optimisation de la gestion des requêtes HTTP avec l'ajout de timeouts.
- Amélioration de la gestion des erreurs et ajout de logs plus informatifs.
- Renommage de variables et de classes pour une meilleure cohérence.
- Suppression de code obsolète.
- Migration de la base de données pour supporter les nouvelles fonctionnalités.

### Autres changements
- Mise à jour de la documentation.
- Correction de typos et amélioration de la qualité du code.
- Ajout de commentaires pour faciliter la compréhension du code.
- Amélioration des messages d'erreur et des notifications.
- Mise à jour des traductions.
- Correction de problèmes de linting.
- Suppression de données sensibles dans les tests.
- Amélioration de la sécurité.
