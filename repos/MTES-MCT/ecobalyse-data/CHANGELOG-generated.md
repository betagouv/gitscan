## Changelog : ecobalyse-data (30 derniers jours, au 5 mai 2026)

### Résumé
Les 30 derniers jours ont été marqués par une importante mise à jour des données, notamment l'ajout de nouveaux ingrédients (UE, compléments laitiers, transformations de métaux), l'amélioration de la gestion des origines géographiques et des processus de fabrication, ainsi que des corrections et alignements de données existantes. Des efforts ont également été faits pour améliorer la structure des données et la clarté des tests.

### Évolutions fonctionnelles
- Ajout de nouveaux ingrédients issus de l'Union Européenne [#262](https://github.com/MTES-MCT/ecobalyse-data/issues/262).
- Ajout de compléments laitiers aux données [#266](https://github.com/MTES-MCT/ecobalyse-data/issues/266).
- Ajout de transformations de métaux et d'autres matériaux [#257](https://github.com/MTES-MCT/ecobalyse-data/issues/257).
- Ajout de données pour les transformations d'ingrédients [#265](https://github.com/MTES-MCT/ecobalyse-data/issues/265).
- Ajout de métadonnées alimentaires aux processus génériques [#263](https://github.com/MTES-MCT/ecobalyse-data/issues/263).
- Ajout de transformations de cuisson [#260](https://github.com/MTES-MCT/ecobalyse-data/issues/260).
- Correction de l'irrigation pour le coton biologique [#255](https://github.com/MTES-MCT/ecobalyse-data/issues/255).
- Correction d'erreurs dans les ingrédients [#256](https://github.com/MTES-MCT/ecobalyse-data/issues/256).
- Alignement des noms affichés (displayName) pour une meilleure cohérence [#258](https://github.com/MTES-MCT/ecobalyse-data/issues/258).

### Évolutions techniques
- Refactorisation de la structure des fichiers `activities.json` en fichiers LCI atomiques [#279](https://github.com/MTES-MCT/ecobalyse-data/issues/279).
- Amélioration de l'explicitation des chemins d'accès aux données dans les tests [#278](https://github.com/MTES-MCT/ecobalyse-data/issues/278).
- Synchronisation des processus [#276](https://github.com/MTES-MCT/ecobalyse-data/issues/276).
- Nettoyage et alignement des alias de fin de vie (EoL) [#275](https://github.com/MTES-MCT/ecobalyse-data/issues/275), [#273](https://github.com/MTES-MCT/ecobalyse-data/issues/273), [#270](https://github.com/MTES-MCT/ecobalyse-data/issues/270).
- Modification du type de matériau [#253](https://github.com/MTES-MCT/ecobalyse-data/issues/253).

### Autres changements
- Renommage de la viande de porc [#285](https://github.com/MTES-MCT/ecobalyse-data/issues/285).
- Définition de la France comme origine par défaut pour certains ingrédients biologiques [#281](https://github.com/MTES-MCT/ecobalyse-data/issues/281).
- Ajout de packages CTCP à food2 [#284](https://github.com/MTES-MCT/ecobalyse-data/issues/284).
- Ajout d'une origine "outre-mer" [#282](https://github.com/MTES-MCT/ecobalyse-data/issues/282).
- Suppression de la densité de bétail [#277](https://github.com/MTES-MCT/ecobalyse-data/issues/277).
- Remplissage des alias vides [#261](https://github.com/MTES-MCT/ecobalyse-data/issues/261).
- Suppression des animaux vivants de l'affichage [#259](https://github.com/MTES-MCT/ecobalyse-data/issues/259).
- Nettoyage de code : suppression de transformations de métaux obsolètes [#288](https://github.com/MTES-MCT/ecobalyse-data/issues/288).
- Création de cellules de batterie [#272](https://github.com/MTES-MCT/ecobalyse-data/issues/272).
