## Changelog : transport-site (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface back-office pour le suivi des jobs, la modernisation de la pile JavaScript, et l'intégration et l'amélioration du support du format NeTEx pour l'échange de données de transport. Des corrections de tests fragiles et des améliorations d'accessibilité ont également été apportées.

### Évolutions fonctionnelles
- **Back-office :** Ajout d'une nouvelle page de suivi des jobs avec un side-panel pour les détails et une vue scrollable des informations. [#5486](https://github.com/etalab/transport-site/issues/5486) et [#5495](https://github.com/etalab/transport-site/issues/5495)
- **NeTEx :** Prise en compte du format NeTEx pour le suivi des données. [#5480](https://github.com/etalab/transport-site/issues/5480)
- **NeTEx :** Conversion des données NeTEx en GeoJSON et affichage sur une carte. [#5463](https://github.com/etalab/transport-site/issues/5463)
- **API :** Ajout de métadonnées pour le format NeTEx. [#5477](https://github.com/etalab/transport-site/issues/5477)
- **Accessibilité :** Amélioration de la navigation au clavier du menu principal. [#5466](https://github.com/etalab/transport-site/issues/5466)
- **Validation IRVE :** Utilisation du validateur intégré de transport.data.gouv pour la validation IRVE. [#5469](https://github.com/etalab/transport-site/issues/5469)

### Évolutions techniques
- **JavaScript :** Mise à jour majeure de la pile JavaScript, incluant le tooling et le build (ESLint 10, Prettier). [#5493](https://github.com/etalab/transport-site/issues/5493)
- **JavaScript :** Mise à jour des librairies JavaScript (DeckGL, Vega, etc.). [#5499](https://github.com/etalab/transport-site/issues/5499)
- **SCSS :** Migration de `@import` vers `@use` pour les styles SCSS. [#5502](https://github.com/etalab/transport-site/issues/5502)
- **FontAwesome :** Mise à jour de FontAwesome de la version 6 à la version 7. [#5500](https://github.com/etalab/transport-site/issues/5500)
- **Concentrateur IRVE :** Amélioration du concentrateur IRVE dynamique. [#5479](https://github.com/etalab/transport-site/issues/5479)
- **Cachex :** Correction d'un test fragile lié à Cachex. [#5485](https://github.com/etalab/transport-site/issues/5485)
- **Métriques :** Correction d'un test fragile lié aux métriques. [#5484](https://github.com/etalab/transport-site/issues/5484)
- **Configuration :** Suppression des références à `Mix.env()` en cours d'exécution. [#5481](https://github.com/etalab/transport-site/issues/5481)

### Autres changements
- Suppression du code mort lié à la conversion GTFS vers NeTEx. [#5487](https://github.com/etalab/transport-site/issues/5487)
- Correction d'un warning dans la CI. [#5504](https://github.com/etalab/transport-site/issues/5504)
- Correction d'un test fragile. [#5494](https://github.com/etalab/transport-site/issues/5494) et [#5472](https://github.com/etalab/transport-site/issues/5472)
- Ajout de support pour l'override des "response_headers" pour le type S3. [#5482](https://github.com/etalab/transport-site/issues/5482)
- Amélioration de la validation NeTEx (plus compacte si tout est valide). [#5476](https://github.com/etalab/transport-site/issues/5476)
- Ajout de couverture de tests pour la conversion NeTEx en GeoJSON. [#5474](https://github.com/etalab/transport-site/issues/5474)
- Correction de la police du menu principal. [#5468](https://github.com/etalab/transport-site/issues/5468)
- Identification des grandes fonctionnalités NeTEx. [#5467](https://github.com/etalab/transport-site/issues/5467)
- Résumé de validation IRVE. [#5429](https://github.com/etalab/transport-site/issues/5429)
- Gestion des valeurs nil pour `critical_errors?` dans le validateur GTFSRT. [#5465](https://github.com/etalab/transport-site/issues/5465)
