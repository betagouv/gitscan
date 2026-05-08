## Changelog : ecobalyse-data (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'enrichissement et l'amélioration des données d'ACV, notamment pour les ingrédients alimentaires et les métaux. Des optimisations ont également été apportées pour accélérer le processus d'exportation des données. Plusieurs corrections et ajustements ont été effectués pour garantir la cohérence et la précision des données.

### Évolutions fonctionnelles
- Accélération de l'exportation des données grâce à l'utilisation de `bw2calc.MultiLCA()` [#290](https://github.com/MTES-MCT/ecobalyse-data/issues/290).
- Ajout de nouveaux ingrédients issus de l'Union Européenne [#262](https://github.com/MTES-MCT/ecobalyse-data/issues/262).
- Ajout de métadonnées alimentaires aux processus génériques [#263](https://github.com/MTES-MCT/ecobalyse-data/issues/263).
- Ajout de données pour les transformations de métaux [#257](https://github.com/MTES-MCT/ecobalyse-data/issues/257).
- Ajout de compléments pour le lait [#266](https://github.com/MTES-MCT/ecobalyse-data/issues/266).
- Ajout de transformations pour la cuisson [#260](https://github.com/MTES-MCT/ecobalyse-data/issues/260).
- Ajout de données pour les cellules de batterie [#272](https://github.com/MTES-MCT/ecobalyse-data/issues/272).
- Ajout de données pour les emballages CTPA dans la catégorie "food2" [#284](https://github.com/MTES-MCT/ecobalyse-data/issues/284).
- Ajout d'informations sur l'origine "oversea" [#282](https://github.com/MTES-MCT/ecobalyse-data/issues/282).
- Ajout de données pour les ingrédients transformés CMAP [#265](https://github.com/MTES-MCT/ecobalyse-data/issues/265).

### Évolutions techniques
- Suppression de la multiplication par la surface occupée par le pâturage [#291](https://github.com/MTES-MCT/ecobalyse-data/issues/291).
- Suppression de la densité du bétail [#277](https://github.com/MTES-MCT/ecobalyse-data/issues/277).
- Refactorisation de `activities.json` en fichiers LCI atomiques [#279](https://github.com/MTES-MCT/ecobalyse-data/issues/279).
- Remplacement des chemins des données dans les tests pour plus de clarté [#278](https://github.com/MTES-MCT/ecobalyse-data/issues/278).
- Synchronisation des processus [#276](https://github.com/MTES-MCT/ecobalyse-data/issues/276).

### Autres changements
- Renommage de la viande de porc [#285](https://github.com/MTES-MCT/ecobalyse-data/issues/285).
- Définition de "plane" par défaut pour certains ingrédients [#283](https://github.com/MTES-MCT/ecobalyse-data/issues/283).
- Définition de la France comme origine par défaut pour certains ingrédients biologiques [#281](https://github.com/MTES-MCT/ecobalyse-data/issues/281).
- Correction de l'irrigation du coton biologique [#255](https://github.com/MTES-MCT/ecobalyse-data/issues/255).
- Correction d'ingrédients [#256](https://github.com/MTES-MCT/ecobalyse-data/issues/256).
- Alignement des alias EoL [#275](https://github.com/MTES-MCT/ecobalyse-data/issues/275) et [#273](https://github.com/MTES-MCT/ecobalyse-data/issues/273).
- Correction des activités EoL [#267](https://github.com/MTES-MCT/ecobalyse-data/issues/267).
- Remplissage des alias vides [#261](https://github.com/MTES-MCT/ecobalyse-data/issues/261).
- Alignement des `displayName` v2 [#258](https://github.com/MTES-MCT/ecobalyse-data/issues/258).
- Masquage des animaux vivants [#259](https://github.com/MTES-MCT/ecobalyse-data/issues/259).
- Correction des derniers alias manquants [#270](https://github.com/MTES-MCT/ecobalyse-data/issues/270).
- Suppression du fichier `activities.json` [#292](https://github.com/MTES-MCT/ecobalyse-data/issues/292).
- Nettoyage de code : suppression de code obsolète concernant la transformation des métaux [#288](https://github.com/MTES-MCT/ecobalyse-data/issues/288).
