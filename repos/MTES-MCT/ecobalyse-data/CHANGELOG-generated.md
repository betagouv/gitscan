## Changelog : ecobalyse-data (30 derniers jours)

### Résumé
Les dernières mises à jour d'ecobalyse-data se concentrent sur l'amélioration de la qualité et de la cohérence des données, notamment en corrigeant des erreurs dans les noms des sources de données et l'encodage des fichiers importés. Des optimisations ont également été apportées pour améliorer les performances lors de l'exportation de données. Enfin, de nouvelles données ont été ajoutées concernant les ingrédients avec métadonnées prédictives et les compléments forestiers.

### Évolutions fonctionnelles
- Correction du nom incorrect de la source de données Pastoeco (#224).
- Correction du séparateur dans l'en-tête Simapro de la base de données Woolmark (#225).
- Utilisation de la base de données Ginko organique reconstruite avec les noms corrects (#218).
- Correction de l'encodage lors de l'importation de fichiers Simapro (#222).
- Ajout de nouveaux ingrédients avec des métadonnées prédictives (#196).
- Ajout de données concernant les compléments forestiers (#208).
- Correction de la gestion des pâturages permanents (#213).

### Évolutions techniques
- Optimisation de l'exportation de toutes les données pour éviter de ralentir le système (#212).
- Ajout d'une vérification pour éviter les activités dupliquées (#205).
- Refactoring pour améliorer la lisibilité et la maintenabilité du code.

### Autres changements
- Tri des fichiers `processes.json` et `activities.json` pour une meilleure organisation (#223, #216).
- Modification de l'affichage du nom des proxies dans le packaging (#202).
- Correction mineure de l'export après la correction de l'encodage (#226).
