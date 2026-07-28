## Changelog : ecobalyse-method-tooling (30 derniers jours, au 28 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration des outils de comparaison et de diagnostic pour les données Agribalyse et BAFU, ainsi que sur l'extraction et la gestion des recettes Agribalyse. Des corrections ont été apportées pour assurer la compatibilité avec les dernières versions des dépendances et pour améliorer la précision des calculs.

### Évolutions fonctionnelles
- Ajout d'un outil pour comparer les données Brightway et VoLCA, incluant des fonctionnalités pour exclure les données à long terme (similaire à l'option "noLT" d'Ecobalyse) via l'option `--exclude-long-term` [#242b45a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/242b45a).
- Ajout d'un outil de diagnostic pour la caractérisation des flux BAFU [#9eb6835](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9eb6835).
- Extraction des recettes Agribalyse et ajout de fichiers README correspondants [#e85b591](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/e85b591).
- Extraction de l'emballage de chaque recette Agribalyse en plus des ingrédients [#a5d64d5](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/a5d64d5).
- Possibilité de spécifier uniquement les ingrédients avec l'option `--ingredients-only` pour les recettes Agribalyse [#7dfd3e0](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7dfd3e0).
- Restauration de l'environnement Jupyter et nettoyage de la configuration VoLCA [#190be03](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/190be03).

### Évolutions techniques
- Mise à jour de l'importation d'IPython dans `explore.py` pour la compatibilité avec IPython 9 [#89010cd](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/89010cd).
- Correction de l'unité de conversion de km en m dans `brightway_vs_volca` [#990d761](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/990d761).
- Refactoring du code `brightway_vs_volca` pour le déplacer sous le répertoire `food/` [#1a6ffe8](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/1a6ffe8) et [#242b45a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/242b45a).
- Utilisation de pyvolca >=0.8.0 pour `transformed-ingredients` [#c8e4af0](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c8e4af0).
- Correction de la résolution des chemins de données dans les notebooks Jupyter [#7d23aed](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7d23aed).
- Correction de plusieurs erreurs dans la gestion des co-produits et des identifiants dans la recette Agribalyse [#bf90f85](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/bf90f85) et [#7ab5463](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7ab5463).
- Correction de problèmes liés au calcul du bilan de l'emballage dans la recette Agribalyse [#95852d0](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/95852d0).

### Autres changements
- Ajout de documentation sur les résultats de parité et les problèmes de VoLCA liés aux eaux souterraines [#ad308c1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/ad308c1) et [#c235f84](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c235f84).
- Ajout de la documentation `etat_egalise.html` comme preuve de parité [#c235f84](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c235f84).
- Mise à jour du titre du rapport dans `brightway_vs_volca` pour utiliser la variable `EB_DATABASE` [#7f1fd8e](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7f1fd8e).
- Ajout de la contrainte VoLCA 0.9.1 pour la fonctionnalité `bulk exclude-long-term` [#936fc44](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/936fc44).
- Ajout d'un fichier `.gitignore` pour ignorer l'état d'exécution de Jupyter [#880140b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/880140b).
- Correction de la valeur de la partie non comestible des noix de cajou [#6f6fcb6](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/6f6fcb6).
- Maintenance des fichiers README [#431771f](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/431771f).
