## Changelog : bhasile (30 derniers jours, au 2026-07-17)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration des tableaux de bord et des statistiques, notamment avec l'ajout de nouveaux indicateurs clés (RMU, activités, contrôle qualité) et la refonte de l'affichage des données. Des améliorations significatives ont également été apportées à la gestion des transformations de structures, incluant des corrections de bugs, de nouvelles fonctionnalités et une meilleure intégration avec les versions des structures.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord pour suivre les transformations en cours [#1479](https://github.com/betagouv/bhasile/issues/1479).
- Ajout d'un bloc de statistiques pour le nombre de RMU [#1491](https://github.com/betagouv/bhasile/issues/1491).
- Ajout d'un bloc de statistiques pour les activités [#1484](https://github.com/betagouv/bhasile/issues/1484).
- Ajout d'un bloc de statistiques pour le contrôle qualité [#1448](https://github.com/betagouv/bhasile/issues/1448).
- Amélioration de l'affichage des structures fermées et actives [#1401](https://github.com/betagouv/bhasile/issues/1401).
- Possibilité de modifier le cas de figure d'une structure [#1406](https://github.com/betagouv/bhasile/issues/1406).
- Ajout d'un historique des structures [#1382](https://github.com/betagouv/bhasile/issues/1382) et [#1376](https://github.com/betagouv/bhasile/issues/1376).
- Affichage du nombre de places sur la page CPOM [#1470](https://github.com/betagouv/bhasile/issues/1470).
- Ajout d'un indicateur visuel pour les transformations en cours [#1425](https://github.com/betagouv/bhasile/issues/1425).
- Possibilité de supprimer une transformation [#1365](https://github.com/betagouv/bhasile/issues/1365).
- Amélioration de la gestion des codes DNA et FINESS (ajout, suppression, transfert) [#1424](https://github.com/betagouv/bhasile/issues/1424), [#1375](https://github.com/betagouv/bhasile/issues/1375) et [#1466](https://github.com/betagouv/bhasile/issues/1466).
- Ajout d'un formulaire d'actualisation des informations [#1451](https://github.com/betagouv/bhasile/issues/1451) avec des parties client et serveur [#1449](https://github.com/betagouv/bhasile/issues/1449] et un bandeau d'information [#1450](https://github.com/betagouv/bhasile/issues/1450).

### Évolutions techniques
- Modularisation de la récupération des démarches numériques [#1499](https://github.com/betagouv/bhasile/issues/1499).
- Refonte de l'architecture pour utiliser les versions des structures [#1354](https://github.com/betagouv/bhasile/issues/1354) et [#1391](https://github.com/betagouv/bhasile/issues/1391).
- Amélioration des tests E2E et correction de nombreux problèmes [#1374](https://github.com/betagouv/bhasile/issues/1374), [#1394](https://github.com/betagouv/bhasile/issues/1394), [#1390](https://github.com/betagouv/bhasile/issues/1390), [#1329](https://github.com/betagouv/bhasile/issues/1329) et [#1353](https://github.com/betagouv/bhasile/issues/1353).
- Mise à jour de Zod vers la version 4 [#1440](https://github.com/betagouv/bhasile/issues/1440).
- Amélioration de la sécurité en protégeant les téléchargements de fichiers [#1460](https://github.com/betagouv/bhasile/issues/1460).
- Suppression de code SQL obsolète [#1437](https://github.com/betagouv/bhasile/issues/1437), [#1435](https://github.com/betagouv/bhasile/issues/1435) et [#1434](https://github.com/betagouv/bhasile/issues/1434).
- Utilisation de `useSaveMutation` pour les sauvegardes [#1445](https://github.com/betagouv/bhasile/issues/1445).
- Standardisation des réponses d'erreur de l'API [#1443](https://github.com/betagouv/bhasile/issues/1443).

### Autres changements
- Correction de divers bugs et améliorations de l'interface utilisateur [#1496](https://github.com/betagouv/bhasile/issues/1496), [#1480](https://github.com/betagouv/bhasile/issues/1480), [#1475](https://github.com/betagouv/bhasile/issues/1475), [#1473](https://github.com/betagouv/bhasile/issues/1473), [#1471](https://github.com/betagouv/bhasile/issues/1471), [#1469](https://github.com/betagouv/bhasile/issues/1469), [#1465](https://github.com/betagouv/bhasile/issues/1465), [#1456](https://github.com/betagouv/bhasile/issues/1456) et [#1455](https://github.com/betagouv/bhasile/issues/1455).
- Ajout de tests unitaires et d'intégration [#1472](https://github.com/betagouv/bhasile/issues/1472).
- Mise à jour de la documentation et traduction des noms de tests en français [#1431](https://github.com/betagouv/bhasile/issues/1431).
- Suppression de la bannière "Place d'asile" [#1493](https://github.com/betagouv/bhasile/issues/1493).
- Ajout de Seine-Saint-Denis aux alias de département [#1467](https://github.com/betagouv/bhasile/issues/1467).
- Correction de problèmes de layout et de style [#1496](https://github.com/betagouv/bhasile/issues/1496), [#1466](https://github.com/betagouv/bhasile/issues/1466) et [#1455](https://github.com/betagouv/bhasile/issues/1455).
