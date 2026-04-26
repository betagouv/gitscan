## Changelog : transport-site (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'intégration et la validation des données NeTEx, un format d'échange de données de transport. Des progrès significatifs ont été réalisés pour convertir ces données en GeoJSON pour une visualisation cartographique, ainsi que pour améliorer l'accessibilité et la robustesse de l'application.

### Évolutions fonctionnelles
- Amélioration de la validation des données NeTEx, avec une présentation plus compacte des résultats de validation [#5476].
- Intégration du validateur IRVE directement dans transport.data.gouv, remplaçant l'appel à un validateur externe [#5469].
- Affichage des données NeTEx converties en GeoJSON sur une carte [#5463].
- Identification des grandes fonctionnalités dans les métadonnées NeTEx [#5467].
- Amélioration de la navigation au clavier du menu principal pour une meilleure accessibilité [#5466].
- Résumé des résultats de validation IRVE plus clair [#5429].

### Évolutions techniques
- Conversion des données NeTEx en GeoJSON : ajout de couverture de tests pour assurer la fiabilité [#5474].
- Correction de tests fragiles pour améliorer la stabilité de la suite de tests [#5472].
- Gestion des valeurs `nil` dans le validateur GTFSRT pour éviter les erreurs [#5465].
- Amélioration de la police du menu principal pour une meilleure lisibilité [#5468].
- Implémentation de la gestion des métadonnées NeTEx [#5475, #5477].

### Autres changements
- Validation NeTEx : amélioration de la performance de la validation [#5476].
- Travaux préparatoires pour la conversion NeTEx vers GeoJSON [#5312].
