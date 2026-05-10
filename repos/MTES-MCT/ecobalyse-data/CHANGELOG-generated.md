## Changelog : ecobalyse-data (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration des données disponibles, notamment en ajoutant de nouveaux ingrédients et en affinant les métadonnées existantes. Des optimisations de performance ont également été apportées pour accélérer le processus d'exportation des données. Plusieurs corrections et nettoyages ont été effectués pour améliorer la qualité et la cohérence des données.

### Évolutions fonctionnelles
- Ajout de nouveaux ingrédients d'origine UE [#262](https://github.com/MTES-MCT/ecobalyse-data/issues/262).
- Ajout de métadonnées alimentaires dans les processus génériques [#263](https://github.com/MTES-MCT/ecobalyse-data/issues/263).
- Ajout de transformations de cuisson [#260](https://github.com/MTES-MCT/ecobalyse-data/issues/260).
- Ajout de packages CTCPA à food2 [#284](https://github.com/MTES-MCT/ecobalyse-data/issues/284).
- Ajout d'une origine "outre-mer" [#282](https://github.com/MTES-MCT/ecobalyse-data/issues/282).
- Amélioration de l'affichage des noms (displayName) pour une meilleure lisibilité [#258](https://github.com/MTES-MCT/ecobalyse-data/issues/258).
- Correction de l'irrigation du coton biologique [#255](https://github.com/MTES-MCT/ecobalyse-data/issues/255).
- Correction d'erreurs dans les ingrédients [#256](https://github.com/MTES-MCT/ecobalyse-data/issues/256).
- Ajout de transformations d'ingrédients CMAP [#265](https://github.com/MTES-MCT/ecobalyse-data/issues/265).

### Évolutions techniques
- Accélération de l'exportation des données grâce à l'utilisation de `bw2calc.MultiLCA()` [#290](https://github.com/MTES-MCT/ecobalyse-data/issues/290).
- Suppression de la multiplication par l'occupation des sols pour l'herbe pâturée [#291](https://github.com/MTES-MCT/ecobalyse-data/issues/291).
- Refactorisation et nettoyage du code pour améliorer la maintenabilité :
    - Suppression d'activités obsolètes dans `activities.json` [#292](https://github.com/MTES-MCT/ecobalyse-data/issues/292).
    - Suppression de la densité de bétail [#277](https://github.com/MTES-MCT/ecobalyse-data/issues/277).
    - Décomposition de `activities.json` en fichiers LCI atomiques [#279](https://github.com/MTES-MCT/ecobalyse-data/issues/279).
    - Nettoyage des catégories de fin de vie (EoL) [#273](https://github.com/MTES-MCT/ecobalyse-data/issues/273) et alignement des alias [#275](https://github.com/MTES-MCT/ecobalyse-data/issues/275), [#270](https://github.com/MTES-MCT/ecobalyse-data/issues/270).
    - Suppression des animaux vivants de l'affichage [#259](https://github.com/MTES-MCT/ecobalyse-data/issues/259).
- Clarification des chemins d'accès aux données utilisées dans les tests [#278](https://github.com/MTES-MCT/ecobalyse-data/issues/278).
- Synchronisation des processus [#276](https://github.com/MTES-MCT/ecobalyse-data/issues/276).
- Ajout de cellules de batterie [#272](https://github.com/MTES-MCT/ecobalyse-data/issues/272).

### Autres changements
- Renommage de la viande de porc [#285](https://github.com/MTES-MCT/ecobalyse-data/issues/285).
- Définition de "plane" par défaut pour certains ingrédients [#283](https://github.com/MTES-MCT/ecobalyse-data/issues/283).
- Définition de la France comme origine par défaut pour certains ingrédients biologiques [#281](https://github.com/MTES-MCT/ecobalyse-data/issues/281).
- Ajout de compléments de lait [#266](https://github.com/MTES-MCT/ecobalyse-data/issues/266).
- Remplissage des alias vides [#261](https://github.com/MTES-MCT/ecobalyse-data/issues/261).
- Ajout de transformations de métaux et autres [#257](https://github.com/MTES-MCT/ecobalyse-data/issues/257).
- Nettoyage de la transformation des métaux [#288](https://github.com/MTES-MCT/ecobalyse-data/issues/288).
