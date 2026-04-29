## Changelog : transport-site (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de la prise en charge du format de données NeTEx, avec des fonctionnalités d'affichage cartographique et de validation. Des corrections de tests fragiles et des améliorations d'accessibilité ont également été apportées. Enfin, la validation des données IRVE a été simplifiée.

### Évolutions fonctionnelles
- Ajout d'une page de suivi des jobs dans le backoffice pour une meilleure supervision des traitements. [#5486](https://github.com/etalab/transport-site/issues/5486)
- Prise en charge du format NeTEx : affichage des données NeTEx sur une carte via une conversion en GeoJSON. [#5463](https://github.com/etalab/transport-site/issues/5463) et [#5312](https://github.com/etalab/transport-site/issues/5312)
- Amélioration de la validation des données NeTEx, avec un affichage plus compact des résultats en cas de succès. [#5476](https://github.com/etalab/transport-site/issues/5476)
- Simplification de la validation des données IRVE en utilisant le validateur intégré de transport.data.gouv. [#5469](https://github.com/etalab/transport-site/issues/5469)
- Amélioration de l'accessibilité : navigation au clavier du menu principal. [#5466](https://github.com/etalab/transport-site/issues/5466)
- Correction de la police du menu principal pour une meilleure lisibilité. [#5468](https://github.com/etalab/transport-site/issues/5468)

### Évolutions techniques
- Mise à jour du protobuf GTFS-rt. [#5483](https://github.com/etalab/transport-site/issues/5483)
- Ajout du support de l'override "response_headers" pour le type S3. [#5482](https://github.com/etalab/transport-site/issues/5482)
- Correction de tests unitaires fragiles (Cachex et métriques). [#5485](https://github.com/etalab/transport-site/issues/5485), [#5484](https://github.com/etalab/transport-site/issues/5484) et [#5472](https://github.com/etalab/transport-site/issues/5472)
- Gestion des erreurs critiques nil dans le validateur GTFSRT. [#5465](https://github.com/etalab/transport-site/issues/5465)

### Autres changements
- Ajout de métadonnées pour le format NeTEx, incluant la liste des fonctionnalités prises en charge. [#5475](https://github.com/etalab/transport-site/issues/5475) et [#5477](https://github.com/etalab/transport-site/issues/5477)
- Résumé de la validation IRVE pour une meilleure compréhension du processus. [#5429](https://github.com/etalab/transport-site/issues/5429)
