## Changelog : ecobalyse-data (30 derniers jours, au 2026-05-14)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'enrichissement des données d'ACV, notamment avec l'ajout de nouveaux ingrédients (batteries, ingrédients UE, compléments laitiers, etc.) et l'amélioration de la gestion des origines géographiques. Des optimisations de performance ont également été apportées pour accélérer l'export des données, ainsi que des refactorings pour préparer une future fusion de dépôts.

### Évolutions fonctionnelles
- Ajout de nouveaux ingrédients dans le catalogue LCI, notamment des cellules de batterie [#289](https://github.com/MTES-MCT/ecobalyse-data/issues/289).
- Ajout de nouveaux ingrédients UE [#262](https://github.com/MTES-MCT/ecobalyse-data/issues/262).
- Ajout de compléments laitiers aux processus génériques [#266](https://github.com/MTES-MCT/ecobalyse-data/issues/266).
- Ajout de métadonnées alimentaires aux processus génériques [#263](https://github.com/MTES-MCT/ecobalyse-data/issues/263).
- Ajout de transformations de cuisson [#260](https://github.com/MTES-MCT/ecobalyse-data/issues/260).
- Prise en charge d'une origine "Outre-Mer" par défaut pour certains ingrédients [#297](https://github.com/MTES-MCT/ecobalyse-data/issues/297).
- Amélioration de la gestion des ingrédients HUE et refactoring des suffixes [#287](https://github.com/MTES-MCT/ecobalyse-data/issues/287).
- Ajout de la vérification de la hiérarchie des ingrédients [#294](https://github.com/MTES-MCT/ecobalyse-data/issues/294).

### Évolutions techniques
- Refactoring du dépôt pour préparer une future fusion, en déplaçant tous les fichiers dans un sous-dossier `data` [#293](https://github.com/MTES-MCT/ecobalyse-data/issues/293).
- Optimisation de l'export des données en utilisant `bw2calc.MultiLCA()` pour accélérer le processus [#290](https://github.com/MTES-MCT/ecobalyse-data/issues/290).
- Optimisation de la taille des *chunks* pour la resynchronisation des données [#299](https://github.com/MTES-MCT/ecobalyse-data/issues/299).
- Suppression de la multiplication de l'occupation des terres pour l'herbe pâturée [#291](https://github.com/MTES-MCT/ecobalyse-data/issues/291).
- Suppression du fichier `activities.json` et remplacement par des fichiers LCI atomiques [#279](https://github.com/MTES-MCT/ecobalyse-data/issues/279).
- Suppression de la densité de bétail [#277](https://github.com/MTES-MCT/ecobalyse-data/issues/277).

### Autres changements
- Correction d'un bug concernant l'irrigation du coton biologique [#255](https://github.com/MTES-MCT/ecobalyse-data/issues/255).
- Correction d'erreurs dans les ingrédients [#256](https://github.com/MTES-MCT/ecobalyse-data/issues/256).
- Ajout de packages CTCPA à food2 [#284](https://github.com/MTES-MCT/ecobalyse-data/issues/284).
- Mise à jour des chemins d'accès aux données dans les tests pour plus de clarté [#278](https://github.com/MTES-MCT/ecobalyse-data/issues/278).
- Alignement des alias EoL [#275](https://github.com/MTES-MCT/ecobalyse-data/issues/275).
- Création de cellules de batterie [#272](https://github.com/MTES-MCT/ecobalyse-data/issues/272).
- Correction des alias manquants [#270](https://github.com/MTES-MCT/ecobalyse-data/issues/270).
- Correction des activités EoL [#267](https://github.com/MTES-MCT/ecobalyse-data/issues/267).
- Remplacement de la valeur par défaut de l'origine par "France" pour certains ingrédients Bio [#281](https://github.com/MTES-MCT/ecobalyse-data/issues/281).
- Nettoyage de code : suppression d'anciens métaux de transformation [#288](https://github.com/MTES-MCT/ecobalyse-data/issues/288).
- Remplacement des alias vides [#261](https://github.com/MTES-MCT/ecobalyse-data/issues/261).
- Resynchronisation des processus [#276](https://github.com/MTES-MCT/ecobalyse-data/issues/276).
- Correction des catégories EoL [#273](https://github.com/MTES-MCT/ecobalyse-data/issues/273).
