## Changelog : ecobalyse-method-tooling (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des ingrédients transformés, notamment en intégrant des données issues de nouvelles sources (feuille Google, Agribalyse) et en affinant les processus de transformation et de classification. Des corrections et améliorations ont également été apportées à l'exportation des données et à la gestion des activités.

### Évolutions fonctionnelles
- Ajout de la prise en charge des variantes UE et génération des données correspondantes. [#979bb69](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/979bb69)
- Prédiction des métadonnées d'ingrédients transformés via le script `predict.py`. [#9bbaec7](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9bbaec7)
- Ajout de noms d'affichage en français pour les ingrédients, utilisant un modèle de traduction. [#38c444c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/38c444c)
- Amélioration de la gestion des coproduits et de l'allocation lors de la génération des données. [#9e842e7](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9e842e7)
- Ajout d'une colonne `dummy_op` pour faciliter l'analyse des données. [#63e132d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/63e132d)
- Correction de la gestion des viandes actives dans le format BIO. [#b77cb2a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b77cb2a)
- Correction de la gestion des radis crus/cuits. [#cde390c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/cde390c)

### Évolutions techniques
- Refactorisation pour adopter `VoLCA include_edges` et filtrage de la classification. [#6843eb3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/6843eb3)
- Utilisation de la source de données transformée côté serveur pour la recherche de consommateurs. [#c2a30bc](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c2a30bc)
- Amélioration de la gestion des collisions de noms d'activités lors de la fusion. [#d4815d3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d4815d3)
- Extraction des paramètres de transformation pour toutes les activités transformées. [#98c63a2](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/98c63a2)
- Remplacement global des mixes de consommation au lieu d'un seul ingrédient. [#d74e379](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d74e379)
- Correction de la recherche des services écosystémiques et application des multiplicateurs. [#7c52cb3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7c52cb3) et [#bdc88f5](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/bdc88f5)
- Récupération des CSV sources à partir d'une feuille Google pour l'exportation. [#8fb75de](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/8fb75de)

### Autres changements
- Ajout d'un fichier README pour les scripts `transformed-ingredients`. [#5102526](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5102526)
- Ajout d'une documentation expliquant la stratégie utilisée. [#b4b261c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b4b261c)
- Création d'un snapshot des ingrédients transformés générés comme base de référence. [#5cefe47](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5cefe47)
- Ajout d'un fichier `.gitignore`. [#b26f2df](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b26f2df)
