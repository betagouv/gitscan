## Changelog : vao (30 derniers jours, au 22 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'application, notamment sur la gestion des agréments (création, renouvellement, validation, et affichage des statuts). Des corrections d'accessibilité ont également été apportées, ainsi que des améliorations de la gestion des fichiers et des tests pour garantir une meilleure qualité et fiabilité de l'application. L'initialisation de la base de données a été revue avec l'ajout d'un Dockerfile dédié.

### Évolutions fonctionnelles
- Amélioration de la gestion des statuts des agréments, notamment l'ajout du statut "À CORRIGER" [#1202](https://github.com/SocialGouv/vao/issues/1202).
- Correction de l'affichage des dates et des statuts dans l'application [#1383](https://github.com/SocialGouv/vao/issues/1383).
- Correction du rafraîchissement des renouvellements d'agrément [#1335](https://github.com/SocialGouv/vao/issues/1335).
- Amélioration de la gestion des représentants légaux : accès, étapes de saisie, et correction d'erreurs d'intitulé [#1183](https://github.com/SocialGouv/vao/issues/1183), [#1336](https://github.com/SocialGouv/vao/issues/1336).
- Correction du bouton "Activer" du fusager lorsqu'il est en brouillon et que le SIRET est identique [#1352](https://github.com/SocialGouv/vao/issues/1352).
- Amélioration de la gestion des fichiers : suppression des catégories de fichiers inutiles, gestion des doublons, et ajout de contraintes sur les fichiers obligatoires [#1346](https://github.com/SocialGouv/vao/issues/1346), [#1384](https://github.com/SocialGouv/vao/issues/1384), [#1385](https://github.com/SocialGouv/vao/issues/1385).
- Ajout de l'envoi d'emails de confirmation pour les demandes d'agrément [#1149](https://github.com/SocialGouv/vao/issues/1149).
- Correction de l'affichage des tabs agréments (scroll) [#1395](https://github.com/SocialGouv/vao/issues/1395).
- Correction de la validation de la date du certificat [#1386](https://github.com/SocialGouv/vao/issues/1386).
- Amélioration de la gestion des hébergements (création) [#1344](https://github.com/SocialGouv/vao/issues/1344).
- Correction du chemin de téléchargement des documents en back-office [#1399](https://github.com/SocialGouv/vao/issues/1399).

### Évolutions techniques
- Ajout d'un Dockerfile pour l'initialisation de la base de données [#1283](https://github.com/SocialGouv/vao/issues/1283).
- Amélioration de la couverture des tests d'intégration et des tests frontend [#1309](https://github.com/SocialGouv/vao/issues/1309), [#1315](https://github.com/SocialGouv/vao/issues/1315).
- Refactoring du code pour supprimer les doublons et améliorer la lisibilité.
- Mise en place d'un cron pour la gestion des DREETS en SVA [#1297](https://github.com/SocialGouv/vao/issues/1297).
- Amélioration de la gestion des erreurs de validation des agréments [#1350](https://github.com/SocialGouv/vao/issues/1350).
- Correction de problèmes liés à l'exécution des tests E2E en CI.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités et les corrections de bugs.

### Autres changements
- Nettoyage du code et suppression de code obsolète.
- Mise à jour de la documentation.
- Correction de problèmes de style et de formatage.
- Amélioration de la gestion des migrations de la base de données.
- Correction de coquilles et d'erreurs mineures.
- Suppression de la branche dans les actions de build de l'image database-init.
- Correction de l'URL du fichier Dockerfile dans les actions de build.
- Suppression de la catégorie `MOTIVATION` des fichiers.
