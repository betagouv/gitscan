## Changelog : ecobalyse-data (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées au projet ecobalyse-data au cours des 30 derniers jours. Les modifications incluent des corrections de données dans les bases de données d'ACV, des améliorations de la gestion des processus et des activités, ainsi que des optimisations de performance pour l'exportation des données.

### Évolutions fonctionnelles
- Correction du nom incorrect dans la base de données source Pastoeco. [#224](https://github.com/MTES-MCT/ecobalyse-data/issues/224)
- Correction du séparateur dans l'en-tête Simapro de la base de données Woolmark. [#225](https://github.com/MTES-MCT/ecobalyse-data/issues/225)
- Utilisation de la base de données Ginko organique reconstruite avec les noms corrects. [#218](https://github.com/MTES-MCT/ecobalyse-data/issues/218)
- Ajout du transport routier vers les aéroports ou les ports. [#211](https://github.com/MTES-MCT/ecobalyse-data/issues/211)
- Correction de l'affichage des pâturages permanents. [#213](https://github.com/MTES-MCT/ecobalyse-data/issues/213)
- Ajout de nouveaux ingrédients avec des métadonnées prédites. [#196](https://github.com/MTES-MCT/ecobalyse-data/issues/196)
- Nouveau format pour les processus génériques. [#220](https://github.com/MTES-MCT/ecobalyse-data/issues/220)

### Évolutions techniques
- Refactorisation pour rendre les métadonnées des activités compatibles entre différents contextes. [#221](https://github.com/MTES-MCT/ecobalyse-data/issues/221)
- Unification de l'alias entre `activities_to_create` et `activities`. [#228](https://github.com/MTES-MCT/ecobalyse-data/issues/228)
- Correction de l'encodage de l'import Simapro. [#222](https://github.com/MTES-MCT/ecobalyse-data/issues/222)
- Optimisation de l'exportation pour éviter de ralentir le système. [#212](https://github.com/MTES-MCT/ecobalyse-data/issues/212)

### Autres changements
- Tri des fichiers `processes.json` et `activities.json`. [#223](https://github.com/MTES-MCT/ecobalyse-data/issues/223) et [#216](https://github.com/MTES-MCT/ecobalyse-data/issues/216)
- Nouvelle exportation après la correction de l'encodage. [#226](https://github.com/MTES-MCT/ecobalyse-data/issues/226)
