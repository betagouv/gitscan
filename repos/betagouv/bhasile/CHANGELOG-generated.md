## Changelog : bhasile (30 derniers jours, au 6 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des transformations de structures d'hébergement, avec notamment la prise en charge des avenants, des actes administratifs et des places d'hébergement. L'interface utilisateur a été améliorée, notamment avec l'ajout de statistiques et la correction de bugs visuels. Des optimisations techniques ont également été réalisées pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de la gestion des RMU (Référentiel des Mouvements Urbains) [#1441](https://github.com/betagouv/bhasile/issues/1441).
- Amélioration de l'affichage des actes sur la page structure [#1447](https://github.com/betagouv/bhasile/issues/1447).
- Affichage du nombre de places fermées sur la page de vérification [#1429](https://github.com/betagouv/bhasile/issues/1429).
- Ajout de boutons de suppression pour les codes DNA et FINESS [#1428](https://github.com/betagouv/bhasile/issues/1428).
- Affichage d'un badge pour les transformations à venir [#1425](https://github.com/betagouv/bhasile/issues/1425).
- Ajout de la possibilité de modifier le cas de figure [#1406](https://github.com/betagouv/bhasile/issues/1406).
- Ajout de la gestion des avenants dans les transformations [#1330](https://github.com/betagouv/bhasile/issues/1330).
- Ajout de la gestion de l'extension/contraction des actes administratifs [#1323](https://github.com/betagouv/bhasile/issues/1323) et de l'hébergement [#1321](https://github.com/betagouv/bhasile/issues/1321).
- Ajout de statistiques sur les structures et les places [#1337](https://github.com/betagouv/bhasile/issues/1337), [#1414](https://github.com/betagouv/bhasile/issues/1414), [#1418](https://github.com/betagouv/bhasile/issues/1418).
- Ajout d'indicateurs d'impact [#1331](https://github.com/betagouv/bhasile/issues/1331), [#1360](https://github.com/betagouv/bhasile/issues/1360).
- Amélioration de la pré-remplissage des informations lors de la création de structures [#1420](https://github.com/betagouv/bhasile/issues/1420).

### Évolutions techniques
- Mise à jour de Zod vers la version 4 [#1440](https://github.com/betagouv/bhasile/issues/1440).
- Suppression des requêtes SQL obsolètes pour les structures, CPOMs et opérateurs [#1400](https://github.com/betagouv/bhasile/issues/1400), [#1435](https://github.com/betagouv/bhasile/issues/1435), [#1434](https://github.com/betagouv/bhasile/issues/1434).
- Refactorisation de la gestion des erreurs API [#1443](https://github.com/betagouv/bhasile/issues/1443).
- Utilisation de `useSaveMutation` pour les sauvegardes [#1445](https://github.com/betagouv/bhasile/issues/1445).
- Introduction de la notion de `structureVersion` pour gérer l'historique des structures [#1354](https://github.com/betagouv/bhasile/issues/1354).
- Migration des transformations [#1324](https://github.com/betagouv/bhasile/issues/1324).
- Amélioration des tests (traduction en français, ajout de tests e2e) [#1431](https://github.com/betagouv/bhasile/issues/1431), [#1377](https://github.com/betagouv/bhasile/issues/1377).

### Autres changements
- Correction de bugs visuels (flickering de l'en-tête) [#1456](https://github.com/betagouv/bhasile/issues/1456).
- Suppression de la génération statique de nonce et state dans la configuration d'authentification [#1457](https://github.com/betagouv/bhasile/issues/1457).
- Améliorations de l'interface utilisateur (design, layout) [#1455](https://github.com/betagouv/bhasile/issues/1455), [#1426](https://github.com/betagouv/bhasile/issues/1426).
- Ajout de la possibilité de spécifier l'extension/contraction sur le label des places autorisées [#1436](https://github.com/betagouv/bhasile/issues/1436).
- Déduction du nombre de places LGBT/FVV [#1439](https://github.com/betagouv/bhasile/issues/1439).
- Ajout d'un lien vers la campagne sur la page de version de la structure [#1379](https://github.com/betagouv/bhasile/issues/1379).
- Correction de l'utilisation de l'année pour les indicateurs financiers [#1433](https://github.com/betagouv/bhasile/issues/1433).
- Suppression des activités SQL [#1437](https://github.com/betagouv/bhasile/issues/1437).
- Ajout de la possibilité de spécifier la date de fermeture d'une structure [#1432](https://github.com/betagouv/bhasile/issues/1432).
- Suppression de la question sur l'adresse administrative [#1427](https://github.com/betagouv/bhasile/issues/1427).
