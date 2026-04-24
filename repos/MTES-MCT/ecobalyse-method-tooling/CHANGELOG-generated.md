## Changelog : ecobalyse-method-tooling (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des ingrédients transformés, notamment en automatisant la rétro-ingénierie des paramètres de transformation d'Agribalyse et en intégrant des données spécifiques à l'Union Européenne. Des corrections et améliorations ont également été apportées à la génération des données finales et à la gestion des activités Brightway.

### Évolutions fonctionnelles
- Ajout de la prise en charge des variantes d'ingrédients de l'Union Européenne (UE) avec la création de fichiers CSV sources et des mécanismes de sauvegarde pour éviter les conflits et les orphelins. [#979bb69](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/979bb69)
- Possibilité de prédire les métadonnées d'ingrédients transformés via le script `predict.py`. [#9bbaec7](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9bbaec7)
- Ajout d'une colonne `is_byproduct` et actualisation des sorties avec les co-produits d'allocation. [#9e842e7](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9e842e7)
- Ajout d'une colonne `dummy_op` et actualisation des sorties à partir de la descente en couches. [#63e132d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/63e132d)
- Ajout de noms d'affichage en français grâce à un modèle de traduction. [#38c444c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/38c444c)
- Amélioration de la génération d'ingrédients transformés avec résolution, filtrage et alias. [#9d14d98](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9d14d98)

### Évolutions techniques
- Refactorisation pour adopter `VoLCA include_edges` et le filtrage de classification. [#6843eb3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/6843eb3)
- Utilisation de `server-side transformed preset` pour la recherche de consommateurs. [#c2a30bc](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c2a30bc)
- Remplacement global des mix de consommation au lieu d'un seul ingrédient à l'intérieur. [#d74e379](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d74e379)
- Correction de la gestion des noms d'activités en cas de collision lors de la fusion. [#d4815d3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d4815d3)
- Correction de l'émission de l'entrée `base-variant` et adaptation aux renommages de la base de données VoLCA. [#5596325](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5596325)
- Correction de la propagation de l'emplacement cible dans les fichiers `replace.to` générés. [#d936a3f](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d936a3f)
- Correction du problème avec le chou rave cuit/cru. [#cde390c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/cde390c)

### Autres changements
- Ajout d'un README pour les scripts `transformed-ingredients`. [#5102526](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5102526)
- Ajout d'une documentation (docstring) expliquant la stratégie utilisée. [#b4b261c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b4b261c)
- Rétro-ingénierie des paramètres de transformation d'Agribalyse. [#5f4d61b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5f4d61b)
- Correction de l'extraction des services écosystémiques et application des multiplicateurs dans les données finales. [#7c52cb3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7c52cb3) et [#bdc88f5](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/bdc88f5)
- Correction de la recherche des services écosystémiques et application des multiplicateurs dans les données finales. [#c769b5f](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c769b5f)
- Suppression des identifiants suffixés en double. [#7883829](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7883829)
- Correction de l'export et régénération de tous les fichiers. [#1b00f66](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/1b00f66) et [#5cd5eee](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5cd5eee)
- Ajout d'un fichier `.gitignore`. [#b26f2df](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b26f2df)
- Snapshot des ingrédients transformés générés comme base de référence. [#5cefe47](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5cefe47)
