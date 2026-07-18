## Changelog : bhasile (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations sur le tableau de bord, notamment l'ajout de statistiques et de visualisations pour suivre l'activité et l'impact des structures d'hébergement. Des efforts ont également été déployés pour améliorer la gestion des transformations de structures et la qualité des données, avec l'introduction de versions pour les structures et des corrections de bugs.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord avec des blocs d'informations sur les transformations en cours [#1479](https://github.com/betagouv/bhasile/issues/1479) et les statistiques RMU [#1491](https://github.com/betagouv/bhasile/issues/1491).
- Mise en place d'un formulaire de mise à jour des informations des structures [#1451](https://github.com/betagouv/bhasile/issues/1451) avec une partie côté serveur [#1449](https://github.com/betagouv/bhasile/issues/1449) et côté client [#1450](https://github.com/betagouv/bhasile/issues/1450).
- Amélioration de la gestion des transformations : affichage d'un avertissement en cas d'incohérence de lieu [#1473](https://github.com/betagouv/bhasile/issues/1473), possibilité de modifier le cas de figure [#1406](https://github.com/betagouv/bhasile/issues/1406), et suppression des actes de la transformation pour les déplacer vers la structure [#1402](https://github.com/betagouv/bhasile/issues/1402).
- Ajout d'indicateurs de statistiques pour le contrôle qualité [#1448](https://github.com/betagouv/bhasile/issues/1448) et l'activité [#1484](https://github.com/betagouv/bhasile/issues/1484).
- Possibilité de filtrer les statistiques par département [#1480](https://github.com/betagouv/bhasile/issues/1480).
- Affichage du nombre de structures fermées sur la page de vérification [#1429](https://github.com/betagouv/bhasile/issues/1429).
- Ajout d'un sélecteur pour filtrer les structures par statut (fermées/actives) [#1401](https://github.com/betagouv/bhasile/issues/1401).
- Ajout d'un lien vers la campagne dans la version de la structure [#1379](https://github.com/betagouv/bhasile/issues/1379).

### Évolutions techniques
- Introduction d'un système de versions pour les structures afin de suivre l'historique des modifications [#1354](https://github.com/betagouv/bhasile/issues/1354) et [#1376](https://github.com/betagouv/bhasile/issues/1376).
- Refonte de la gestion des statistiques pour intégrer les RMU [#1468](https://github.com/betagouv/bhasile/issues/1468) et [#1442](https://github.com/betagouv/bhasile/issues/1442).
- Modularisation de la récupération des données des démarches numériques [#1499](https://github.com/betagouv/bhasile/issues/1499).
- Amélioration de la sécurité avec la protection des téléchargements de fichiers contre la suppression ou la visualisation non autorisée [#1460](https://github.com/betagouv/bhasile/issues/1460).
- Mise à jour de Zod en version 4 [#1440](https://github.com/betagouv/bhasile/issues/1440).
- Suppression de requêtes SQL inutiles pour optimiser les performances [#1400](https://github.com/betagouv/bhasile/issues/1400) et [#1435](https://github.com/betagouv/bhasile/issues/1435).
- Utilisation de `useSaveMutation` pour la sauvegarde des données [#1445](https://github.com/betagouv/bhasile/issues/1445).

### Autres changements
- Correction de plusieurs bugs et améliorations de la qualité du code.
- Traduction des noms des tests en français [#1431](https://github.com/betagouv/bhasile/issues/1431).
- Suppression de la bannière "Place d'asile" [#1493](https://github.com/betagouv/bhasile/issues/1493).
- Ajout de Seine-Saint-Denis aux alias [#1467](https://github.com/betagouv/bhasile/issues/1467).
- Amélioration de la gestion des erreurs et des messages d'erreur [#1465](https://github.com/betagouv/bhasile/issues/1465) et [#1444](https://github.com/betagouv/bhasile/issues/1444).
- Diverses corrections de tests et améliorations de la suite de tests.
