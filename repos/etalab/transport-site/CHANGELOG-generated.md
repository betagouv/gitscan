## Changelog : transport-site (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du back-office pour le suivi des jobs, l'intégration et la visualisation des données NeTEx, ainsi que la modernisation de la stack JavaScript. Des corrections de tests fragiles et des améliorations de l'accessibilité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une nouvelle page de suivi des jobs dans le back-office avec un panneau latéral pour les détails de chaque job [#5486](https://github.com/etalab/transport-site/issues/5486).
- Amélioration de la page de suivi des jobs avec un panneau latéral scrollable et une deuxième passe d'amélioration [#5495](https://github.com/etalab/transport-site/issues/5495), [#5488](https://github.com/etalab/transport-site/issues/5488).
- Prise en compte des données NeTEx pour le suivi des jobs [#5480](https://github.com/etalab/transport-site/issues/5480).
- Visualisation des données NeTEx converties en GeoJSON sur une carte [#5463](https://github.com/etalab/transport-site/issues/5463).
- Identification des grandes fonctionnalités dans les données NeTEx [#5467](https://github.com/etalab/transport-site/issues/5467).
- Amélioration de la police du menu principal pour une meilleure lisibilité [#5468](https://github.com/etalab/transport-site/issues/5468).
- Amélioration de la navigation au clavier du menu pour l'accessibilité [#5466](https://github.com/etalab/transport-site/issues/5466).

### Évolutions techniques
- Mise à jour majeure de la stack JavaScript (tooling et build) avec passage à ESLint 10 et Prettier pour le formatage du code [#5493](https://github.com/etalab/transport-site/issues/5493).
- Mise à jour de la version d'immutable en 4.3.8 [#5396](https://github.com/etalab/transport-site/issues/5396).
- Refactorisation : Suppression du code mort lié à la conversion GTFS vers NeTEx [#5487](https://github.com/etalab/transport-site/issues/5487).
- Suppression des références à `Mix.env()` en cours d'exécution pour une meilleure configuration [#5481](https://github.com/etalab/transport-site/issues/5481).
- Mise à jour du protobuf pour le GTFS-rt [#5483](https://github.com/etalab/transport-site/issues/5483).
- Passage du validateur IRVE à la demande au validateur intégré de transport.data.gouv [#5469](https://github.com/etalab/transport-site/issues/5469).
- Ajout de support pour l'override des "response_headers" pour le type S3 [#5482](https://github.com/etalab/transport-site/issues/5482).

### Autres changements
- Corrections de tests fragiles concernant Cachex, les métriques et d'autres tests [#5485](https://github.com/etalab/transport-site/issues/5485), [#5484](https://github.com/etalab/transport-site/issues/5484), [#5472](https://github.com/etalab/transport-site/issues/5472).
- Correction d'un test flaky lié à la méthode `refresh_places` [#5489](https://github.com/etalab/transport-site/issues/5489).
- Ajout de tests pour la conversion NeTEx vers GeoJSON [#5474](https://github.com/etalab/transport-site/issues/5474).
- Amélioration de la validation NeTEx pour une sortie plus compacte en cas de succès [#5476](https://github.com/etalab/transport-site/issues/5476).
- Ajout de métadonnées pour NeTEx [#5475](https://github.com/etalab/transport-site/issues/5475), [#5477](https://github.com/etalab/transport-site/issues/5477).
- Résumé de la validation IRVE [#5429](https://github.com/etalab/transport-site/issues/5429).
- Correction de la gestion des erreurs critiques dans le validateur GTFSRT [#5465](https://github.com/etalab/transport-site/issues/5465).
- Implémentation de la conversion NeTEx vers GeoJSON [#5312](https://github.com/etalab/transport-site/issues/5312).
