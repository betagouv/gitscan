## Changelog : transport-site (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du backoffice avec une nouvelle page de suivi des jobs et des améliorations de l'interface utilisateur.  Des progrès significatifs ont également été réalisés sur la prise en charge du format NeTEx, notamment sa conversion en GeoJSON pour l'affichage cartographique. Enfin, des corrections de tests et des mises à jour de tooling JavaScript ont été apportées pour améliorer la stabilité et la qualité du code.

### Évolutions fonctionnelles
- **Backoffice :** Ajout d'une nouvelle page de suivi des jobs avec un panneau latéral pour les détails de chaque job [#5486](https://github.com/etalab/transport-site/issues/5486).  Le panneau latéral est désormais verticalement scrollable [#5498](https://github.com/etalab/transport-site/issues/5498).
- **NeTEx :** Prise en charge du format NeTEx pour le suivi et l'affichage des métadonnées [#5477](https://github.com/etalab/transport-site/issues/5477).
- **NeTEx :** Conversion des données NeTEx en GeoJSON pour l'affichage sur une carte [#5463](https://github.com/etalab/transport-site/issues/5463).
- **IRVE :**  Passage du validateur IRVE à la demande au validateur intégré de transport.data.gouv [#5469](https://github.com/etalab/transport-site/issues/5469).
- **Accessibilité :** Amélioration de la navigation au clavier du menu principal [#5466](https://github.com/etalab/transport-site/issues/5466).
- **Interface utilisateur :** Correction de la police du menu principal [#5468](https://github.com/etalab/transport-site/issues/5468).

### Évolutions techniques
- **JavaScript :** Mise à jour majeure de la stack JavaScript (tooling et build) avec passage à ESLint 10 et Prettier pour le formatage du code [#5493](https://github.com/etalab/transport-site/issues/5493).
- **Concentrateur IRVE :** Mise en place d'un concentrateur IRVE dynamique v2 [#5479](https://github.com/etalab/transport-site/issues/5479).
- **Tests :** Correction de tests fragiles (Cachex, métriques) [#5485](https://github.com/etalab/transport-site/issues/5485), [#5484](https://github.com/etalab/transport-site/issues/5484), [#5472](https://github.com/etalab/transport-site/issues/5472).
- **Configuration :** Suppression des références à `Mix.env()` en cours d'exécution [#5481](https://github.com/etalab/transport-site/issues/5481).
- **GTFS-rt :** Mise à jour du protobuf GTFS-rt [#5483](https://github.com/etalab/transport-site/issues/5483).
- **Suppression de code mort :** Suppression du code de conversion GTFS vers NeTEx [#5487](https://github.com/etalab/transport-site/issues/5487).

### Autres changements
- **Documentation :** Ajout de support pour l'override des "response_headers" pour le type S3 [#5482](https://github.com/etalab/transport-site/issues/5482).
- **Validation NeTEx :** Amélioration de la validation NeTEx pour la rendre plus compacte en cas de succès [#5476](https://github.com/etalab/transport-site/issues/5476).
- **Couverture de tests :** Amélioration de la couverture de tests pour la conversion NeTEx en GeoJSON [#5474](https://github.com/etalab/transport-site/issues/5474).
- **Résumé de validation IRVE :** Ajout d'un résumé de validation IRVE [#5429](https://github.com/etalab/transport-site/issues/5429).
- **GTFSRT Validator:** Gestion des valeurs nil pour `critical_errors?` dans le validateur GTFSRT [#5465](https://github.com/etalab/transport-site/issues/5465).
