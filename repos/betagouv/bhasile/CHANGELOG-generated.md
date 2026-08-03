## Changelog : bhasile (30 derniers jours, au 31 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur l'amélioration des statistiques et du tableau de bord, avec l'ajout de nouvelles données (RMU, activités, contrôle qualité) et une meilleure visualisation des informations. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant les transformations de structures et la gestion des erreurs.

### Évolutions fonctionnelles
- Ajout d'un bloc de statistiques pour le RMU (Répertoire des Mouvements d'Usagers) sur le tableau de bord. [#1468](https://github.com/betagouv/bhasile/issues/1468)
- Ajout d'un bloc de statistiques pour le contrôle qualité sur le tableau de bord. [#1448](https://github.com/betagouv/bhasile/issues/1448)
- Ajout d'un bloc de statistiques pour les activités sur le tableau de bord. [#1484](https://github.com/betagouv/bhasile/issues/1484)
- Amélioration de la navigation sur la carte des statistiques, permettant de passer entre région et département. [#1526](https://github.com/betagouv/bhasile/issues/1526)
- Ajout d'une carte statique sur la page des statistiques. [#1516](https://github.com/betagouv/bhasile/issues/1516)
- Ajout d'un bloc de rappels sur le tableau de bord. [#1486](https://github.com/betagouv/bhasile/issues/1486)
- Ajout d'un bloc affichant les transformations en cours sur le tableau de bord. [#1479](https://github.com/betagouv/bhasile/issues/1479)
- Affichage du nombre de structures sur la page CPOM. [#1470](https://github.com/betagouv/bhasile/issues/1470)
- Amélioration de l'affichage des actes sur la page structure. [#1447](https://github.com/betagouv/bhasile/issues/1447)
- Ajout d'une alerte en cas d'incohérence de lieu. [#1473](https://github.com/betagouv/bhasile/issues/1473)
- Ajout d'une indication du type de transformation (extension/contraction) sur l'étiquette des places autorisées. [#1439](https://github.com/betagouv/bhasile/issues/1439)
- Ajout de notifications sur le tableau de bord. [#1487](https://github.com/betagouv/bhasile/issues/1487)

### Évolutions techniques
- Migration de la typologie d'adresse vers l'adresse. [#1541](https://github.com/betagouv/bhasile/issues/1541)
- Refonte de la gestion des erreurs API avec une réponse standardisée. [#1443](https://github.com/betagouv/bhasile/issues/1443)
- Mise à jour de Zod vers la version 4. [#1440](https://github.com/betagouv/bhasile/issues/1440)
- Modularisation de la récupération des données des Démarches Numériques. [#1499](https://github.com/betagouv/bhasile/issues/1499)
- Suppression des références à l'ancienne campagne. [#1511](https://github.com/betagouv/bhasile/issues/1511)
- Suppression des SQL liés aux activités, CPOM et opérateur. [#1535, #1437, #1434](https://github.com/betagouv/bhasile/issues/1535)
- Utilisation de `useSaveMutation` pour les sauvegardes. [#1445](https://github.com/betagouv/bhasile/issues/1445)
- Amélioration de la gestion des tests E2E et correction de plusieurs erreurs. [#1542, #1529, #1525, #1512, #1477, #1464, #1431, #1377](https://github.com/betagouv/bhasile/issues/1542)
- Correction d'une erreur de connexion à la base de données. [#1548](https://github.com/betagouv/bhasile/issues/1548)
- Correction d'un problème d'hydratation pour l'opérateur. [#1546](https://github.com/betagouv/bhasile/issues/1546)
- Ajout de gardes pour la production. [#1530](https://github.com/betagouv/bhasile/issues/1530)
- Backfill des typologies de structure. [#1528](https://github.com/betagouv/bhasile/issues/1528)

### Autres changements
- Documentation de la structure de la typologie. [#1531](https://github.com/betagouv/bhasile/issues/1531)
- Correction de plusieurs problèmes d'affichage et de style. [#1496, #1466, #1465, #1456, #1455, #1453, #1436]
- Suppression du banner Place d'asile. [#1493](https://github.com/betagouv/bhasile/issues/1493)
- Traduction des noms des tests en français. [#1431](https://github.com/betagouv/bhasile/issues/1431)
- Correction de problèmes liés aux dates RMU. [#1532, #1462, #1433]
- Ajout de Seine-Saint-Denis aux alias. [#1467](https://github.com/betagouv/bhasile/issues/1467)
- Amélioration de la sécurité concernant les uploads de fichiers. [#1460](https://github.com/betagouv/bhasile/issues/1460)
- Mise en place d'un cron pour certaines tâches. [#1515](https://github.com/betagouv/bhasile/issues/1515)
- Correction d'un bug lié à la structure des versions initiales. [#1549](https://github.com/betagouv/bhasile/issues/1549)
