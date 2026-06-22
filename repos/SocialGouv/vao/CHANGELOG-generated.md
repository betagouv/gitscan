## Changelog : vao (30 derniers jours, au 2026-06-19)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'accessibilité (RGAA) et la correction de bugs, notamment concernant le renouvellement des agréments, la gestion des documents et l'authentification. Des améliorations de sécurité ont également été apportées avec l'implémentation et la gestion du code à usage unique (OTP). Enfin, des optimisations de l'infrastructure et des dépendances ont été réalisées.

### Évolutions fonctionnelles
- Amélioration de l'accessibilité (RGAA) sur plusieurs étapes du renouvellement d'agrément, incluant les pages "Mon agrément", les étapes 3 et 4, et l'onglet "Dossier". [#1391](https://github.com/SocialGouv/vao/issues/1391), [#1354](https://github.com/SocialGouv/vao/issues/1354), [#1347](https://github.com/SocialGouv/vao/issues/1347)
- Ajout de textes d'information concernant les CGU et l'EIG. [#1417](https://github.com/SocialGouv/vao/issues/1417), [#1411](https://github.com/SocialGouv/vao/issues/1411)
- Correction de l'affichage et de la validation des informations de la personne physique. [#1388](https://github.com/SocialGouv/vao/issues/1388)
- Amélioration de la gestion des fichiers joints et normalisation des noms de fichiers uploadés. [#1389](https://github.com/SocialGouv/vao/issues/1389), [#1406](https://github.com/SocialGouv/vao/issues/1406)
- Implémentation de la fonctionnalité d'envoi de mail pour la prise en charge. [#1400](https://github.com/SocialGouv/vao/issues/1400)
- Ajout de la possibilité de renvoyer le code OTP et de valider la connexion. [#1396](https://github.com/SocialGouv/vao/issues/1396)
- Ajout de la fonctionnalité "Remember me" pour le code OTP. [#1408](https://github.com/SocialGouv/vao/issues/1408)
- Correction de l'affichage du statut de l'agrément après renouvellement. [#1398](https://github.com/SocialGouv/vao/issues/1398)
- Correction d'un bug empêchant l'activation du bouton "Fusager" lorsque le SIRET est correct. [#1352](https://github.com/SocialGouv/vao/issues/1352)
- Correction d'un problème de messages contradictoires lors du dépôt d'un fichier de complétude. [#1407](https://github.com/SocialGouv/vao/issues/1407)
- Correction d'un bug lié au titre des CGU et à l'OTP. [#1427](https://github.com/SocialGouv/vao/issues/1427)
- Ajout du nom de naissance sur la liste et le formulaire. [#1426](https://github.com/SocialGouv/vao/issues/1426)
- Correction d'un conflit entre le BO usager, les CGU et l'OTP. [#1420](https://github.com/SocialGouv/vao/issues/1420)
- Correction d'erreurs d'emails envoyés aux organismes. [#1419](https://github.com/SocialGouv/vao/issues/1419)

### Évolutions techniques
- Mise en place d'un mécanisme de "fail closed" pour l'antivirus. [#1413](https://github.com/SocialGouv/vao/issues/1413)
- Ajout d'une route pour la validation EIG. [#1418](https://github.com/SocialGouv/vao/issues/1418)
- Optimisation des ressources PostgreSQL en production (CPU et mémoire). [#1362](https://github.com/SocialGouv/vao/issues/1362), [#1363](https://github.com/SocialGouv/vao/issues/1363)
- Mise à jour de plusieurs dépendances : NestJS, Nodemailer, Knex, Axios, ts-jest, multer, Nuxt. [#1394](https://github.com/SocialGouv/vao/issues/1394), [#1393](https://github.com/SocialGouv/vao/issues/1393), [#1392](https://github.com/SocialGouv/vao/issues/1392), [#1376](https://github.com/SocialGouv/vao/issues/1376), [#1375](https://github.com/SocialGouv/vao/issues/1375), [#1374](https://github.com/SocialGouv/vao/issues/1374), [#1373](https://github.com/SocialGouv/vao/issues/1373)
- Amélioration de la configuration Jest et des timeouts pour les tests. [#1366](https://github.com/SocialGouv/vao/issues/1366)
- Refactoring du code TypeScript et mise à jour de la configuration de build.
- Utilisation de pnpm catalog.

### Autres changements
- Documentation et corrections de code diverses pour améliorer la qualité globale du projet.
- Ajout d'un feature flag pour la fonctionnalité OTP. [#1409](https://github.com/SocialGouv/vao/issues/1409)
- Suppression d'alertes remplacées par des toast. [#1421](https://github.com/SocialGouv/vao/issues/1421)
- Merge de la branche preprod vers main. [#1414](https://github.com/SocialGouv/vao/issues/1414)
