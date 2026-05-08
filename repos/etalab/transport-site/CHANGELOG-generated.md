## Changelog : transport-site (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du back-office pour le suivi des jobs, l'intégration et la visualisation des données NeTEx, ainsi que des mises à jour techniques importantes de la stack JavaScript et la correction de tests fragiles. Des améliorations d'accessibilité ont également été apportées.

### Évolutions fonctionnelles

- **Back-office :** Ajout d'une nouvelle page de suivi des jobs avec un side-panel pour les détails et une vue scrollable des informations. [#5486](https://github.com/etalab/transport-site/issues/5486), [#5495](https://github.com/etalab/transport-site/issues/5495), [#5498](https://github.com/etalab/transport-site/issues/5498)
- **NeTEx :** Intégration de la prise en compte des données NeTEx pour le suivi et l'affichage sur une carte via une conversion en GeoJSON. [#5463](https://github.com/etalab/transport-site/issues/5463), [#5474](https://github.com/etalab/transport-site/issues/5474), [#5475](https://github.com/etalab/transport-site/issues/5475), [#5476](https://github.com/etalab/transport-site/issues/5476), [#5477](https://github.com/etalab/transport-site/issues/5477), [#5467](https://github.com/etalab/transport-site/issues/5467)
- **IRVE :** Passage du validateur IRVE à la demande au validateur intégré de transport.data.gouv. [#5469](https://github.com/etalab/transport-site/issues/5469)
- **Accessibilité :** Amélioration de la navigation au clavier du menu principal. [#5466](https://github.com/etalab/transport-site/issues/5466)
- **Interface utilisateur :** Correction de la police du menu principal. [#5468](https://github.com/etalab/transport-site/issues/5468)

### Évolutions techniques

- **Stack JavaScript :** Mise à jour majeure de la stack JavaScript, incluant le tooling, le build et les dépendances (ESLint 10, Prettier). [#5493](https://github.com/etalab/transport-site/issues/5493), [#5497](https://github.com/etalab/transport-site/issues/5497), [#5499](https://github.com/etalab/transport-site/issues/5499)
- **FontAwesome :** Mise à jour de FontAwesome de la version 6 à la version 7. [#5500](https://github.com/etalab/transport-site/issues/5500)
- **SCSS :** Migration de `@import` vers `@use` pour les styles SCSS. [#5502](https://github.com/etalab/transport-site/issues/5502)
- **Cachex & Métriques :** Correction de tests fragiles liés à Cachex et aux métriques. [#5484](https://github.com/etalab/transport-site/issues/5484), [#5485](https://github.com/etalab/transport-site/issues/5485)
- **Scheduler :** Correction d'une référence incorrecte dans le scheduler. [#5489](https://github.com/etalab/transport-site/issues/5489)
- **Suppression de code mort :** Suppression du code lié à la conversion GTFS vers NeTEx. [#5487](https://github.com/etalab/transport-site/issues/5487)
- **Configuration :** Suppression des références à `Mix.env()` en cours d'exécution. [#5481](https://github.com/etalab/transport-site/issues/5481)

### Autres changements

- **GTFS-rt :** Mise à jour du protobuf GTFS-rt. [#5483](https://github.com/etalab/transport-site/issues/5483)
- **Validateur GTFSRT :** Gestion des valeurs `nil` pour `critical_errors?`. [#5465](https://github.com/etalab/transport-site/issues/5465)
- **Correctif CI :** Correction d'un warning dans la configuration CI. [#5504](https://github.com/etalab/transport-site/issues/5504)
- **Concentrateur IRVE :** Amélioration du concentrateur IRVE dynamique. [#5479](https://github.com/etalab/transport-site/issues/5479)
- **Résumé de validation IRVE :** Ajout d'un résumé de validation IRVE. [#5429](https://github.com/etalab/transport-site/issues/5429)
