## Changelog : vao (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les évolutions de VAO se sont concentrées sur l'amélioration de l'expérience utilisateur lors des procédures de renouvellement d'agrément, avec des corrections et des ajouts liés à la saisie d'informations, la gestion des fichiers et l'envoi de notifications. Des améliorations techniques ont également été apportées, notamment concernant l'initialisation de la base de données et l'intégration de tests.

### Évolutions fonctionnelles
- Correction de l'affichage du statut "A_CORRIGER" pour les agréments. [#1297](https://github.com/SocialGouv/vao/issues/1297)
- Amélioration de la gestion des doublons de documents lors du renouvellement d'agrément. [#1295](https://github.com/SocialGouv/vao/issues/1295)
- Mise en place de l'envoi de mails de confirmation pour les demandes d'agrément. [#1286](https://github.com/SocialGouv/vao/issues/1286)
- Correction de bugs et améliorations de l'étape 3 du processus de renouvellement d'agrément (bilan, adresse, ajout de séjours). [#1284](https://github.com/SocialGouv/vao/issues/1284), [#1259](https://github.com/SocialGouv/vao/issues/1259), [#1258](https://github.com/SocialGouv/vao/issues/1258)
- Correction de problèmes liés à la validation et au brouillon lors de l'étape 2 du renouvellement d'agrément. [#1272](https://github.com/SocialGouv/vao/issues/1272), [#1256](https://github.com/SocialGouv/vao/issues/1256)
- Amélioration de l'étape 1 du renouvellement d'agrément (gestion des représentants légaux). [#1266](https://github.com/SocialGouv/vao/issues/1266)
- Ajout de fonctionnalités pour la gestion des messages et des agréments dans l'interface "fusager". [#1273](https://github.com/SocialGouv/vao/issues/1273), [#1269](https://github.com/SocialGouv/vao/issues/1269), [#1268](https://github.com/SocialGouv/vao/issues/1268), [#1266](https://github.com/SocialGouv/vao/issues/1266)
- Correction de l'affichage des dates et du statut dans l'interface OVA. [#1294](https://github.com/SocialGouv/vao/issues/1294)
- Correction de l'accès à la liste des usages. [#1293](https://github.com/SocialGouv/vao/issues/1293)
- Correction de l'inversion du nom et prénom dans l'affichage OVA. [#1333](https://github.com/SocialGouv/vao/issues/1333)
- Amélioration de la conformité RGAA (accessibilité) : labels et boutons. [#1281](https://github.com/SocialGouv/vao/issues/1281), [#1084](https://github.com/SocialGouv/vao/issues/1084)

### Évolutions techniques
- Ajout d'un Dockerfile pour l'initialisation de la base de données. [#1283](https://github.com/SocialGouv/vao/issues/1283)
- Correction de problèmes liés à la construction de l'image database-init. [#1305](https://github.com/SocialGouv/vao/issues/1305)
- Ajout de tests frontend pour certaines fonctionnalités (agrement, fichiers par catégorie). [#1307](https://github.com/SocialGouv/vao/issues/1307)
- Amélioration de la suppression des branches dans les actions CI/CD.
- Suppression de code inutile et nettoyage général du code.
- Suppression des caractères vides dans les requêtes. [#1285](https://github.com/SocialGouv/vao/issues/1285)

### Autres changements
- Mise à jour de la documentation.
- Corrections mineures et refactoring du code.
