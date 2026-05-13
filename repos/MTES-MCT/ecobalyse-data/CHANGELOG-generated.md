## Changelog : ecobalyse-data (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'enrichissement des données avec de nouveaux ingrédients (batteries, ingrédients UE, compléments laitiers, etc.) et l'amélioration de la précision des données existantes (origine des ingrédients, transformations de métaux). Des optimisations de performance ont également été apportées pour accélérer l'export des données, notamment grâce à l'utilisation de `bw2calc.MultiLCA()`. Enfin, une restructuration des fichiers de données a été effectuée pour une meilleure organisation et maintenabilité.

### Évolutions fonctionnelles
- Ajout de données pour les cellules de batterie dans le catalogue LCI. [#289](https://github.com/MTES-MCT/ecobalyse-data/issues/289)
- Ajout de nouveaux ingrédients issus de l'Union Européenne. [#262](https://github.com/MTES-MCT/ecobalyse-data/issues/262)
- Ajout de compléments laitiers aux données. [#266](https://github.com/MTES-MCT/ecobalyse-data/issues/266)
- Ajout de transformations de métaux et d'autres données associées. [#257](https://github.com/MTES-MCT/ecobalyse-data/issues/257)
- Correction de l'irrigation du coton biologique. [#255](https://github.com/MTES-MCT/ecobalyse-data/issues/255)
- Ajout de transformations de cuisson. [#260](https://github.com/MTES-MCT/ecobalyse-data/issues/260)
- Ajout de packages CTCP à food2. [#284](https://github.com/MTES-MCT/ecobalyse-data/issues/284)
- Ajout d'une origine "Outre-Mer" pour certains ingrédients. [#282](https://github.com/MTES-MCT/ecobalyse-data/issues/282)

### Évolutions techniques
- Optimisation de la performance de l'export des données en utilisant `bw2calc.MultiLCA()`. [#290](https://github.com/MTES-MCT/ecobalyse-data/issues/290)
- Correction de la multiplication incorrecte de l'occupation des terres pour l'herbe pâturée. [#291](https://github.com/MTES-MCT/ecobalyse-data/issues/291)
- Suppression des activités obsolètes du fichier `activities.json` et restructuration en fichiers LCI atomiques. [#292](https://github.com/MTES-MCT/ecobalyse-data/issues/292) et [#279](https://github.com/MTES-MCT/ecobalyse-data/issues/279)
- Refactoring pour aligner les alias EoL et les catégories EoL. [#275](https://github.com/MTES-MCT/ecobalyse-data/issues/275) et [#273](https://github.com/MTES-MCT/ecobalyse-data/issues/273)
- Amélioration de la définition de l'origine par défaut pour certains ingrédients biologiques (France). [#281](https://github.com/MTES-MCT/ecobalyse-data/issues/281)
- Amélioration de la définition de l'origine par défaut pour certains ingrédients de France d'Outre-Mer. [#297](https://github.com/MTES-MCT/ecobalyse-data/issues/297)
- Suppression de la densité du bétail. [#277](https://github.com/MTES-MCT/ecobalyse-data/issues/277)
- Remplacement des animaux vivants par des données plus appropriées. [#259](https://github.com/MTES-MCT/ecobalyse-data/issues/259)
- Synchronisation des processus. [#276](https://github.com/MTES-MCT/ecobalyse-data/issues/276)
- Remplacement des chemins des données dans les tests par des chemins plus explicites. [#278](https://github.com/MTES-MCT/ecobalyse-data/issues/278)

### Autres changements
- Ajout de données CMAP transformées. [#265](https://github.com/MTES-MCT/ecobalyse-data/issues/265)
- Renommage de la viande de porc. [#285](https://github.com/MTES-MCT/ecobalyse-data/issues/285)
- Remplissage des alias vides. [#261](https://github.com/MTES-MCT/ecobalyse-data/issues/261) et [#270](https://github.com/MTES-MCT/ecobalyse-data/issues/270)
- Alignement des `displayName` v2. [#258](https://github.com/MTES-MCT/ecobalyse-data/issues/258)
- Synchronisation des données avec le dépôt principal et optimisation de la taille des chunks. [#299](https://github.com/MTES-MCT/ecobalyse-data/issues/299)
- Nettoyage de code : suppression de code obsolète dans la transformation des métaux. [#288](https://github.com/MTES-MCT/ecobalyse-data/issues/288)
