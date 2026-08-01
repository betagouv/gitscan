## Changelog : ecobalyse-method-tooling (30 derniers jours, au 31 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent principalement sur l'outil `agribalyse_recipe`, avec des améliorations significatives dans la gestion des ingrédients, de l'emballage et de l'extraction de données. Des corrections et des fonctionnalités ont également été ajoutées aux outils de comparaison et de diagnostic BAFU. L'intégration de Jupyter Notebook a été restaurée et améliorée.

### Évolutions fonctionnelles
- L'outil `agribalyse_recipe` permet désormais d'extraire l'emballage de chaque recette, affiché avec ses ingrédients. [#242b45a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/242b45a)
- Possibilité d'extraire tous les processus de la base de données avec l'option `--all`. [#5c377f4](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5c377f4)
- Ajout de l'option `--scope ciqual` pour gérer l'emballage des 2 500 produits Ciqual. [#7f8ff3f](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7f8ff3f)
- Les produits Ciqual incluent maintenant leurs propres ingrédients. [#0b2feb9](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0b2feb9)
- Ajout d'une option `--ingredients-only` pour l'extraction des ingrédients. [#7dfd3e0](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7dfd3e0)
- Restauration de l'intégration Jupyter Notebook et nettoyage de la configuration VoLCA. [#190be03](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/190be03)
- Ajout d'un outil de diagnostic pour la caractérisation des flux BAFU. [#9eb6835](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9eb6835)
- Ajout d'un outil de comparaison (parity-cloud) pour BAFU, permettant d'exclure les impacts à long terme avec l'option `--exclude-long-term`. [#242b45a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/242b45a)

### Évolutions techniques
- Mise à jour de la version minimale de `pyvolca` à 0.8.0 pour `transformed-ingredients`. [#c8e4af0](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c8e4af0)
- Utilisation de `pyvolca` pour piloter VoLCA et téléchargement de la base de données au lieu de générer un fichier TOML. [#1b39a4a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/1b39a4a)
- Correction de l'importation d'IPython dans `explore.py` pour la compatibilité avec IPython 9. [#89010cd](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/89010cd)
- Correction d'une inversion d'unités (km <-> m) dans l'outil de comparaison BAFU. [#990d761](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/990d761)
- Refactoring de la structure des outils BAFU, les déplaçant sous le répertoire `food/`. [#8b4eff0](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/8b4eff0, #1a6ffe8](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/1a6ffe8) )
- Mise à jour de la version de l'engine pin à 0.9.3 pour la compatibilité avec pyvolca 0.8.2. [#0a82e21](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0a82e21)

### Autres changements
- Documentation : alignement du titre de l'article et déplacement de la méthodologie vers le blog pour `agribalyse_recipe`.
- Documentation : ajout de liens vers la documentation de `pyvolca`.
- Documentation : ajout de preuves de parité et signalement d'un problème VoLCA lié aux eaux souterraines.
- Ajout de READMEs pour les nouvelles fonctionnalités. [#e85b591](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/e85b591)
- Suppression d'une reconstruction d'impact obsolète pour l'écotoxicité en eau douce. [#391c70d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/391c70d)
- Correction de bugs mineurs dans `agribalyse_recipe` concernant l'identification des ingrédients et la gestion des co-produits. [#bf90f85](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/bf90f85, #7ab5463](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7ab5463) )
- Correction de problèmes liés au calcul de l'emballage. [#d962c5d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d962c5d, #95852d0](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/95852d0) )
- Correction du chemin d'accès aux données dans les notebooks Jupyter. [#7d23aed](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7d23aed)
- Ajout d'une valeur par défaut pour le pourcentage de la partie non comestible des noix de cajou. [#6f6fcb6](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/6f6fcb6)
- Ajout de fichiers `.gitignore` pour exclure les états de runtime de Jupyter Notebook. [#880140b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/880140b)
