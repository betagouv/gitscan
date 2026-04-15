## Changelog : ecobalyse-method-tooling (30 derniers jours, au 15 avril 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de la gestion des données transformées, notamment l'extraction des paramètres de transformation d'Agribalyse et l'ajout de variantes pour l'Union Européenne. Des améliorations ont également été apportées à la gestion des noms d'affichage et à la résolution des activités, ainsi qu'à la génération des données finales.

### Évolutions fonctionnelles
- Ajout de la prise en charge d'une variante de données pour l'Union Européenne (UE) avec des mécanismes de sauvegarde pour éviter les collisions et les orphelins [#979bb69](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/979bb69).
- Possibilité d'exposer la colonne `is_byproduct` et de rafraîchir les sorties avec les co-produits d'allocation [#9e842e7](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9e842e7).
- Ajout d'une colonne `dummy_op` et rafraîchissement des sorties à partir d'une descente en couches [#63e132d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/63e132d).
- Prédiction des métadonnées d'ingrédients transformés via le script `predict.py` [#9bbaec7](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9bbaec7).
- Extraction des paramètres de transformation pour toutes les activités de preset transformées [#98c63a2](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/98c63a2).
- Ajout de noms d'affichage en français avec un modèle de traduction [#38c444c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/38c444c).
- Amélioration de la génération d'ingrédients transformés (résolution, filtrage, alias) [#9d14d98](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9d14d98).

### Évolutions techniques
- Utilisation de la transformation côté serveur pour la recherche des consommateurs [#c2a30bc](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c2a30bc).
- Remplacement complet des mixes de consommation au lieu d'un seul ingrédient à l'intérieur [#d74e379](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d74e379).
- Correction de la recherche des services écosystémiques et application des multiplicateurs dans les données finales [#7c52cb3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7c52cb3) et [#bdc88f5](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/bdc88f5).
- Correction de la gestion des localisations des activités : utilisation de la localisation de la base de données, CSV uniquement pour la désambiguïsation [#7c8f4d4](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7c8f4d4).
- Correction du renommage d'activité en cas de collision de `displayName` lors de la fusion [#d4815d3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d4815d3).

### Autres changements
- Ajout d'une docstring expliquant la stratégie utilisée [#b4b261c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b4b261c).
- Snapshot des ingrédients transformés générés comme base de référence [#5cefe47](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5cefe47).
- Ajout d'un fichier `.gitignore` [#b26f2df](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b26f2df).
- Suppression temporaire des animaux vivants [#fe1d5df](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/fe1d5df).
- Nouvelle version de BIO [#7417ff5](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7417ff5).
- Réexportation avec les impacts [#a070a08](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/a070a08).
- Inclusion de la localisation dans `activities.json` uniquement lorsque nécessaire pour la désambiguïsation [#d0c7b2f](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d0c7b2f).
