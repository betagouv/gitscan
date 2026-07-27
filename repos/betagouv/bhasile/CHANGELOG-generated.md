## Changelog : bhasile (30 derniers jours, au 24 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par d'importantes améliorations de l'interface utilisateur, notamment l'ajout d'un tableau de bord pour le suivi des transformations et des statistiques, ainsi que des améliorations sur la gestion des structures et des lieux d'hébergement. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord pour visualiser l'état des transformations en cours [#1479](https://github.com/betagouv/bhasile/issues/1479) et [#1474](https://github.com/betagouv/bhasile/issues/1474).
- Amélioration de l'affichage et de la gestion des structures fermées [#1408](https://github.com/betagouv/bhasile/issues/1408).
- Ajout de statistiques sur l'activité et la qualité des contrôles [#1484](https://github.com/betagouv/bhasile/issues/1484), [#1491](https://github.com/betagouv/bhasile/issues/1491) et [#1430](https://github.com/betagouv/bhasile/issues/1430).
- Possibilité de filtrer les statistiques par RMU [#1481](https://github.com/betagouv/bhasile/issues/1481) et [#1468](https://github.com/betagouv/bhasile/issues/1468).
- Ajout d'indicateurs sur le nombre de places disponibles et fermées [#1429](https://github.com/betagouv/bhasile/issues/1429).
- Amélioration de la gestion des codes DNA et Finess, avec possibilité de suppression et de transfert [#1428](https://github.com/betagouv/bhasile/issues/1428) et [#1424](https://github.com/betagouv/bhasile/issues/1424).
- Ajout d'un formulaire d'actualisation des informations des structures [#1451](https://github.com/betagouv/bhasile/issues/1451), [#1464](https://github.com/betagouv/bhasile/issues/1464) et [#1472](https://github.com/betagouv/bhasile/issues/1472).
- Ajout d'un avertissement en cas d'incohérence de lieu [#1473](https://github.com/betagouv/bhasile/issues/1473).
- Amélioration de la gestion des transformations, avec des marqueurs sur le tableau des lieux [#1407](https://github.com/betagouv/bhasile/issues/1407).

### Évolutions techniques
- Modularisation de la récupération des données des démarches numériques [#1499](https://github.com/betagouv/bhasile/issues/1499).
- Mise en place d'un système de cron pour l'exécution de tâches planifiées [#1515](https://github.com/betagouv/bhasile/issues/1515).
- Refonte de la gestion des erreurs API avec une réponse standardisée [#1443](https://github.com/betagouv/bhasile/issues/1443).
- Utilisation de `useSaveMutation` pour la sauvegarde des données [#1445](https://github.com/betagouv/bhasile/issues/1445).
- Mise à jour de la version de Zod à la version 4 [#1440](https://github.com/betagouv/bhasile/issues/1440).
- Amélioration de la sécurité avec la suppression de la génération statique de nonce et d'état dans la configuration d'authentification [#1457](https://github.com/betagouv/bhasile/issues/1457).
- Protection des téléchargements de fichiers contre la suppression ou la visualisation non autorisée [#1460](https://github.com/betagouv/bhasile/issues/1460).
- Suppression du code SQL obsolète pour les opérateurs et les CPOM [#1435](https://github.com/betagouv/bhasile/issues/1435) et [#1434](https://github.com/betagouv/bhasile/issues/1434).

### Autres changements
- Suppression de la bannière "Place d'asile" [#1493](https://github.com/betagouv/bhasile/issues/1493).
- Correction de divers bugs et améliorations de la qualité du code.
- Traduction des noms des tests en français [#1431](https://github.com/betagouv/bhasile/issues/1431).
- Ajout de tests E2E pour les transformations [#1377](https://github.com/betagouv/bhasile/issues/1377).
- Ajout de Seine-Saint-Denis aux alias [#1467](https://github.com/betagouv/bhasile/issues/1467).
- Amélioration du style et de la disposition de certains éléments de l'interface utilisateur.
