## Changelog : bhasile (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois-ci, bhasile a bénéficié d'améliorations significatives en termes de gestion des structures, des transformations et de l'expérience utilisateur globale. L'ajout d'un tableau de bord avec des indicateurs clés, ainsi que des améliorations de la cartographie et des statistiques, permettent un suivi plus précis et efficace du parc de logements pour demandeurs d'asile. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord avec des blocs d'informations : rappels, transformations en cours, statistiques sur les RMU et l'activité. ([#1487](https://github.com/betagouv/bhasile/issues/1487), [#1484](https://github.com/betagouv/bhasile/issues/1484), [#1491](https://github.com/betagouv/bhasile/issues/1491))
- Amélioration de la cartographie avec l'ajout d'une carte statique sur la page des statistiques et la possibilité de naviguer entre région et département. ([#1526](https://github.com/betagouv/bhasile/issues/1526), [#1516](https://github.com/betagouv/bhasile/issues/1516))
- Possibilité de filtrer les statistiques par date. ([#1414](https://github.com/betagouv/bhasile/issues/1414))
- Ajout d'un indicateur visuel pour les structures avec des transformations à venir. ([#1425](https://github.com/betagouv/bhasile/issues/1425))
- Affichage du nombre de places fermées sur la page de vérification. ([#1429](https://github.com/betagouv/bhasile/issues/1429))
- Ajout de boutons de suppression pour les codes DNA et FINESS. ([#1428](https://github.com/betagouv/bhasile/issues/1428))
- Amélioration de la gestion des transformations : prévention de la sélection de la même structure plusieurs fois, interdiction de transformations de types différents, transfert des codes DNA. ([#1454](https://github.com/betagouv/bhasile/issues/1454), [#1424](https://github.com/betagouv/bhasile/issues/1424), [#1453](https://github.com/betagouv/bhasile/issues/1453))
- Ajout d'un formulaire d'actualisation des informations des structures. ([#1451](https://github.com/betagouv/bhasile/issues/1451), [#1449](https://github.com/betagouv/bhasile/issues/1449), [#1450](https://github.com/betagouv/bhasile/issues/1450))
- Ajout de la gestion de la date de fermeture des structures. ([#1432](https://github.com/betagouv/bhasile/issues/1432))

### Évolutions techniques
- Refactorisation de la gestion des statistiques pour utiliser l'API. ([#1430](https://github.com/betagouv/bhasile/issues/1430))
- Modularisation de la récupération des données des Démarches Numériques. ([#1499](https://github.com/betagouv/bhasile/issues/1499))
- Mise en place de tests E2E pour les transformations. ([#1377](https://github.com/betagouv/bhasile/issues/1377))
- Amélioration de la gestion des erreurs API. ([#1443](https://github.com/betagouv/bhasile/issues/1443))
- Mise à jour de la librairie Zod vers la version 4. ([#1440](https://github.com/betagouv/bhasile/issues/1440))
- Utilisation de `useSaveMutation` pour les opérations de sauvegarde. ([#1445](https://github.com/betagouv/bhasile/issues/1445))
- Suppression du code SQL obsolète lié aux activités et aux CPOM. ([#1437](https://github.com/betagouv/bhasile/issues/1437), [#1435](https://github.com/betagouv/bhasile/issues/1435), [#1434](https://github.com/betagouv/bhasile/issues/1434))
- Amélioration de la sécurité : protection des téléchargements de fichiers contre la suppression ou la visualisation non autorisée. ([#1460](https://github.com/betagouv/bhasile/issues/1460))

### Autres changements
- Ajout de documentation sur la typologie des structures. ([#1531](https://github.com/betagouv/bhasile/issues/1531))
- Traduction des noms des tests en français. ([#1431](https://github.com/betagouv/bhasile/issues/1431))
- Corrections de bugs et améliorations de l'interface utilisateur.
- Diverses corrections de tests E2E. ([#1542](https://github.com/betagouv/bhasile/issues/1542), [#1529](https://github.com/betagouv/bhasile/issues/1529), [#1525](https://github.com/betagouv/bhasile/issues/1525), [#1512](https://github.com/betagouv/bhasile/issues/1512), [#1477](https://github.com/betagouv/bhasile/issues/1477), [#1464](https://github.com/betagouv/bhasile/issues/1464), [#1472](https://github.com/betagouv/bhasile/issues/1472))
