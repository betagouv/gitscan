## Changelog : transport-site (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface back-office pour le suivi des jobs, la modernisation de la stack JavaScript, l'ajout de support pour de nouveaux formats de données (NeTEx) et la correction de tests instables. Des améliorations d'accessibilité et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles
- Ajout du support pour les données GBFS de Yégo dans les métadonnées [#5512](https://github.com/etalab/transport-site/issues/5512).
- Nouvelle page de suivi des jobs dans le back-office, avec un panneau latéral pour les détails et un affichage verticalement scrollable [#5498](https://github.com/etalab/transport-site/issues/5498), [#5495](https://github.com/etalab/transport-site/issues/5495), [#5492](https://github.com/etalab/transport-site/issues/5492), [#5488](https://github.com/etalab/transport-site/issues/5488), [#5486](https://github.com/etalab/transport-site/issues/5486).
- Prise en compte des données NeTEx pour le suivi et affichage sur carte [#5480](https://github.com/etalab/transport-site/issues/5480), [#5477](https://github.com/etalab/transport-site/issues/5477), [#5475](https://github.com/etalab/transport-site/issues/5475), [#5476](https://github.com/etalab/transport-site/issues/5476), [#5474](https://github.com/etalab/transport-site/issues/5474), [#5463](https://github.com/etalab/transport-site/issues/5463).
- Amélioration de l'accessibilité avec la navigation au clavier du menu principal [#5468](https://github.com/etalab/transport-site/issues/5468) et [#5466](https://github.com/etalab/transport-site/issues/5466).
- Correction de l'affichage des icônes après une mise à jour [#5506](https://github.com/etalab/transport-site/issues/5506).

### Évolutions techniques
- Mise à jour majeure de la stack JavaScript : tooling, build, ESLint (v8 -> v10) et passage à Prettier pour le formatage du code [#5497](https://github.com/etalab/transport-site/issues/5497), [#5499](https://github.com/etalab/transport-site/issues/5499).
- Migration SCSS de `@import` vers `@use` [#5502](https://github.com/etalab/transport-site/issues/5502).
- Mise à jour de FontAwesome de la version 6 à la version 7 [#5500](https://github.com/etalab/transport-site/issues/5500).
- Refactorisation : suppression du code mort lié à l'ancien agrégateur dynamique IRVE du proxy unlock [#5510](https://github.com/etalab/transport-site/issues/5510) et à la conversion GTFS vers NeTEx [#5487](https://github.com/etalab/transport-site/issues/5487).
- Suppression des références à `Mix.env()` en cours d'exécution [#5481](https://github.com/etalab/transport-site/issues/5481).
- Passage du validateur IRVE à la demande au validateur intégré de transport.data.gouv [#5469](https://github.com/etalab/transport-site/issues/5469).
- Mise à jour du protobuf GTFS-rt [#5483](https://github.com/etalab/transport-site/issues/5483).

### Autres changements
- Correction de tests instables (Cachex et métriques) [#5485](https://github.com/etalab/transport-site/issues/5485), [#5484](https://github.com/etalab/transport-site/issues/5484), [#5494](https://github.com/etalab/transport-site/issues/5494), [#5472](https://github.com/etalab/transport-site/issues/5472).
- Ajout de support pour l'override des "response_headers" pour le type S3 [#5482](https://github.com/etalab/transport-site/issues/5482).
- Correction d'un warning dans la CI [#5504](https://github.com/etalab/transport-site/issues/5504).
- Correction du scheduler qui référençait une méthode renommée [#5489](https://github.com/etalab/transport-site/issues/5489).
