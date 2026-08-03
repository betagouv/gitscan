## Changelog : transport-site (30 derniers jours, au 27 juillet 2026)

### Résumé
Les récentes évolutions du site transport se concentrent sur l'amélioration de la sécurité, la mise à jour des règles de validation des données MobilityData, et des optimisations du processus de consolidation des données IRVE. Des mises à jour de librairies et la suppression d'un outil de replay de tests (exvcr) ont également été réalisées.

### Évolutions fonctionnelles
- Mise à jour des règles de validation pour la version 8.0.1 du format MobilityData [#5574](https://github.com/etalab/transport-site/issues/5574).
- Refactoring du processus de consolidation des données IRVE pour une meilleure efficacité et une pré-validation des données [#5559](https://github.com/etalab/transport-site/issues/5559).

### Évolutions techniques
- Mise en place d'un scanner de vulnérabilités et upgrades de librairies pour renforcer la sécurité du site [#5566](https://github.com/etalab/transport-site/issues/5566).
- Mise à jour de la définition des messages Protobuf pour le format GTFS-RT [#5569](https://github.com/etalab/transport-site/issues/5569).
- Suppression de l'outil de replay de tests `exvcr` [#5564](https://github.com/etalab/transport-site/issues/5564).
