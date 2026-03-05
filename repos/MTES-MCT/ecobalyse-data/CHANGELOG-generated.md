## Changelog : ecobalyse-data (30 derniers jours)

### Résumé
Les dernières mises à jour d'ecobalyse-data se concentrent sur l'amélioration de la qualité des données, notamment en corrigeant des erreurs de nommage et d'encodage dans les bases de données importées (Ginko, Woolmark, Pastoeco). De nouvelles fonctionnalités ont également été ajoutées pour supporter de nouveaux types de données et formats de processus, et des optimisations ont été apportées pour améliorer la performance lors de l'exportation de données.

### Évolutions fonctionnelles
- Correction du nom incorrect dans la base de données source Pastoeco. [#224](https://github.com/MTES-MCT/ecobalyse-data/issues/224)
- Correction du séparateur dans l'en-tête Simapro de la base de données Woolmark. [#225](https://github.com/MTES-MCT/ecobalyse-data/issues/225)
- Utilisation de la base de données Ginko organique reconstruite avec les noms corrects. [#218](https://github.com/MTES-MCT/ecobalyse-data/issues/218)
- Ajout de nouveaux ingrédients avec des métadonnées prédites. [#196](https://github.com/MTES-MCT/ecobalyse-data/issues/196)
- Ajout de compléments forestiers. [#208](https://github.com/MTES-MCT/ecobalyse-data/issues/208)
- Correction de l'exportation après la correction de l'encodage. [#226](https://github.com/MTES-MCT/ecobalyse-data/issues/226)
- Correction du problème de pâturage permanent. [#213](https://github.com/MTES-MCT/ecobalyse-data/issues/213)
- Nouveau format pour les processus génériques. [#220](https://github.com/MTES-MCT/ecobalyse-data/issues/220)

### Évolutions techniques
- Correction de l'encodage de l'importation Simapro. [#222](https://github.com/MTES-MCT/ecobalyse-data/issues/222)
- Optimisation de la performance lors de l'exportation de toutes les données, pour éviter de ralentir le système. [#212](https://github.com/MTES-MCT/ecobalyse-data/issues/212)

### Autres changements
- Tri des fichiers `processes.json` et `activities.json` pour une meilleure organisation. [#223](https://github.com/MTES-MCT/ecobalyse-data/issues/223) et [#216](https://github.com/MTES-MCT/ecobalyse-data/issues/216)
