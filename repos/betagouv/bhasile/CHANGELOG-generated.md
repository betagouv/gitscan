## Changelog : bhasile (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant les transformations de structures d'hébergement, avec une refonte du formulaire, l'ajout de validations et de tests associés. Des améliorations significatives ont également été apportées aux statistiques et aux indicateurs de performance, notamment pour le suivi des RMU et de l'impact. Des corrections de bugs et des optimisations diverses ont également été implémentées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de l'indicateur RMU et de ses statistiques. [#1468](https://github.com/betagouv/bhasile/issues/1468)
- Affichage du nombre de structures sur la page CPOM. [#1470](https://github.com/betagouv/bhasile/issues/1470)
- Ajout d'indicateurs d'impact et amélioration de leur présentation. [#1331](https://github.com/betagouv/bhasile/issues/1331), [#1360](https://github.com/betagouv/bhasile/issues/1360)
- Ajout de statistiques sur les types de places. [#1361](https://github.com/betagouv/bhasile/issues/1361)
- Ajout de statistiques sur les finances. [#1448](https://github.com/betagouv/bhasile/issues/1448)
- Possibilité de modifier le cas de figure d'une structure. [#1345](https://github.com/betagouv/bhasile/issues/1345)
- Ajout de la possibilité de gérer les avenants dans les transformations. [#1330](https://github.com/betagouv/bhasile/issues/1330)
- Ajout de la gestion des fermetures de structures. [#1408](https://github.com/betagouv/bhasile/issues/1408)
- Affichage du nombre de places fermées sur la page de vérification. [#1429](https://github.com/betagouv/bhasile/issues/1429)
- Ajout de badges indiquant les transformations en cours. [#1425](https://github.com/betagouv/bhasile/issues/1425)
- Ajout d'un historique des structures. [#1376](https://github.com/betagouv/bhasile/issues/1376)
- Ajout de la possibilité de supprimer des codes DNA ou FINESS. [#1428](https://github.com/betagouv/bhasile/issues/1428)
- Ajout de la possibilité de transférer des codes DNA lors des transformations. [#1424](https://github.com/betagouv/bhasile/issues/1424)

### Évolutions techniques
- Refonte du formulaire de transformation avec validation et gestion des erreurs. [#1342](https://github.com/betagouv/bhasile/issues/1342), [#1348](https://github.com/betagouv/bhasile/issues/1348), [#1350](https://github.com/betagouv/bhasile/issues/1350)
- Mise en place de tests E2E pour les transformations. [#1377](https://github.com/betagouv/bhasile/issues/1377), [#1390](https://github.com/betagouv/bhasile/issues/1390)
- Utilisation de structure versions pour une meilleure gestion des données. [#1354](https://github.com/betagouv/bhasile/issues/1354)
- Suppression de requêtes SQL obsolètes (opérateur, cpom, activités). [#1437](https://github.com/betagouv/bhasile/issues/1437), [#1435](https://github.com/betagouv/bhasile/issues/1435), [#1434](https://github.com/betagouv/bhasile/issues/1434)
- Amélioration de la gestion des erreurs API. [#1443](https://github.com/betagouv/bhasile/issues/1443)
- Mise à jour de Zod vers la version 4. [#1440](https://github.com/betagouv/bhasile/issues/1440)
- Amélioration de la sécurité avec la suppression de la génération statique de nonce. [#1457](https://github.com/betagouv/bhasile/issues/1457)

### Autres changements
- Correction de bugs divers liés aux tests E2E. [#1460](https://github.com/betagouv/bhasile/issues/1460), [#1477](https://github.com/betagouv/bhasile/issues/1477), [#1464](https://github.com/betagouv/bhasile/issues/1464)
- Correction de bugs liés aux dates RMU. [#1478](https://github.com/betagouv/bhasile/issues/1478)
- Amélioration de l'interface utilisateur (style, positionnement, affichage). [#1466](https://github.com/betagouv/bhasile/issues/1466), [#1471](https://github.com/betagouv/bhasile/issues/1471), [#1465](https://github.com/betagouv/bhasile/issues/1465)
- Ajout de la Seine-Saint-Denis aux alias de département. [#1467](https://github.com/betagouv/bhasile/issues/1467)
- Traduction des noms des tests en français. [#1431](https://github.com/betagouv/bhasile/issues/1431)
- Correction de problèmes d'affichage et de flickering. [#1456](https://github.com/betagouv/bhasile/issues/1456), [#1462](https://github.com/betagouv/bhasile/issues/1462)
- Diverses corrections et améliorations de l'interface utilisateur et du code.
