## Changelog : transport-site (30 derniers jours)

### Résumé
Le projet transport-site a connu une période d'amélioration continue au cours des 30 derniers jours, avec un accent particulier sur l'amélioration de la validation et de la gestion des données NeTEx, ainsi que sur l'optimisation de la recherche et de l'affichage des jeux de données. Des améliorations ont également été apportées à la consolidation des données IRVE et à l'interface utilisateur, notamment pour l'affichage des métadonnées et la navigation.

### Évolutions fonctionnelles
- Possibilité de passer le dashboard Metabase en plein écran. [#5399](https://github.com/etalab/transport-site/issues/5399)
- Correction d'un overflow des titres de ressources pour une meilleure lisibilité. [#5397](https://github.com/etalab/transport-site/issues/5397)
- Ajout d'une barre de recherche sur les datasets et les ressources. [#5380](https://github.com/etalab/transport-site/issues/5380)
- Ajout de la Suisse dans la liste des divisions administratives. [#5367](https://github.com/etalab/transport-site/issues/5367)
- Amélioration de la recherche : correction du tri sur les jeux de données les plus récents. [#5373](https://github.com/etalab/transport-site/issues/5373)
- Ajout d'un menu de navigation sur la page de détails des ressources. [#5311](https://github.com/etalab/transport-site/issues/5311)
- Possibilité de télécharger les rapports NeTEx au format Parquet. [#5375](https://github.com/etalab/transport-site/issues/5375)
- Ajout d'un indicateur "Périmé" sur les cartouches GTFS Flex. [#5332](https://github.com/etalab/transport-site/issues/5332)
- Affichage des dates de validité dans les cartouches NeTEx. [#5331](https://github.com/etalab/transport-site/issues/5331)

### Évolutions techniques
- Mise à jour de PostgreSQL de la version 14 à la version 18 et de TimescaleDB à la version 2.23 pour l'environnement CI. [#5027](https://github.com/etalab/transport-site/issues/5027)
- Amélioration de la performance de la recherche en utilisant des index en mémoire et en optimisant la gestion des facets. [#5340](https://github.com/etalab/transport-site/issues/5340), [#5333](https://github.com/etalab/transport-site/issues/5333)
- Refactoring et corrections diverses dans le code NeTEx pour améliorer la robustesse et la maintenabilité. [#5338](https://github.com/etalab/transport-site/issues/5338), [#5368](https://github.com/etalab/transport-site/issues/5368), [#5344](https://github.com/etalab/transport-site/issues/5344)
- Amélioration de la gestion des URL de ressources pour éviter les problèmes d'encodage. [#5363](https://github.com/etalab/transport-site/issues/5363)
- Optimisation de la consolidation IRVE pour la suppression des doublons et la remontée d'informations supplémentaires. [#5360](https://github.com/etalab/transport-site/issues/5360), [#5343](https://github.com/etalab/transport-site/issues/5343), [#5359](https://github.com/etalab/transport-site/issues/5359)

### Autres changements
- Mise à jour du logo et de la référence textuelle vers "Ministère des Transports". [#5386](https://github.com/etalab/transport-site/issues/5386)
- Ajout de la configuration pour le dashboard Metabase pour public-transit. [#5394](https://github.com/etalab/transport-site/issues/5394)
- Stabilisation des tests de navigation. [#5392](https://github.com/etalab/transport-site/issues/5392)
- Ajustement du menu principal pour les langues. [#5389](https://github.com/etalab/transport-site/issues/5389)
- Suppression de code mort dans le DatasetController. [#5329](https://github.com/etalab/transport-site/issues/5329)
- Correction d'un revert de la recherche par sous-type de données. [#5324](https://github.com/etalab/transport-site/issues/5324)
- Nettoyage routinier du code. [#5322](https://github.com/etalab/transport-site/issues/5322)
