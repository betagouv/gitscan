## Changelog : vao (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité (notamment via le RGAA), la correction de bugs et l'ajout de nouvelles fonctionnalités concernant la gestion des agréments et des documents, ainsi que des améliorations techniques pour la base de données et les tests.

### Évolutions fonctionnelles

*   **Agrément :**
    *   Amélioration du processus de renouvellement d'agrément avec prise en compte des retours RGAA [#1354](https://github.com/SocialGouv/vao/issues/1354).
    *   Correction de bugs et amélioration de l'affichage des dates et statuts des agréments [#1353](https://github.com/SocialGouv/vao/issues/1353), [#1352](https://github.com/SocialGouv/vao/issues/1352), [#1350](https://github.com/SocialGouv/vao/issues/1350).
    *   Ajout de la possibilité de modifier et transmettre un agrément via Fusager [#1348](https://github.com/SocialGouv/vao/issues/1348), [#1267](https://github.com/SocialGouv/vao/issues/1267).
    *   Correction de problèmes de rafraîchissement lors du renouvellement d'un agrément [#1335](https://github.com/SocialGouv/vao/issues/1335).
    *   Amélioration du contrôle des représentants légaux [#1339](https://github.com/SocialGouv/vao/issues/1339).
*   **Documents :**
    *   Correction de problèmes liés à l'upload de documents pour le renouvellement des agréments [#1384](https://github.com/SocialGouv/vao/issues/1384).
    *   Gestion des fichiers obligatoires et suppression des catégories inutiles [#1385](https://github.com/SocialGouv/vao/issues/1385).
*   **Notifications :**
    *   Implémentation de l'envoi de mails de confirmation pour les demandes d'agrément [#1320](https://github.com/SocialGouv/vao/issues/1320), [#1286](https://github.com/SocialGouv/vao/issues/1286).
*   **Accessibilité :**
    *   Améliorations de l'accessibilité (RGAA) sur plusieurs étapes des formulaires, notamment pour les champs et les labels [#1351](https://github.com/SocialGouv/vao/issues/1351), [#1347](https://github.com/SocialGouv/vao/issues/1347), [#1336](https://github.com/SocialGouv/vao/issues/1336), [#1325](https://github.com/SocialGouv/vao/issues/1325), [#1183](https://github.com/SocialGouv/vao/issues/1183).

### Évolutions techniques

*   **Base de données :**
    *   Ajout d'un Dockerfile pour l'initialisation de la base de données [#1283](https://github.com/SocialGouv/vao/issues/1283).
    *   Modification des actions de build de l'image database-init [#1305](https://github.com/SocialGouv/vao/issues/1305).
*   **Tests :**
    *   Ajout et amélioration des tests d'intégration et E2E [#1349](https://github.com/SocialGouv/vao/issues/1349), [#1344](https://github.com/SocialGouv/vao/issues/1344), [#1326](https://github.com/SocialGouv/vao/issues/1326), [#1315](https://github.com/SocialGouv/vao/issues/1315), [#1309](https://github.com/SocialGouv/vao/issues/1309).
    *   Correction de problèmes liés à l'exécution des tests en CI [#1328](https://github.com/SocialGouv/vao/issues/1328).
*   **CI/CD :**
    *   Amélioration des workflows CI/CD pour les tests et le déploiement.
*   **Divers :**
    *   Mise à jour de certaines dépendances et corrections de code (SonarQube).

### Autres changements

*   Nettoyage et refactoring du code.
*   Correction de coquilles et amélioration de la documentation.
*   Mise à jour de la configuration de l'application.
