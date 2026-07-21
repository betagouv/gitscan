## Changelog : ecobalyse-method-tooling (30 derniers jours, au 20 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration des outils de comparaison entre différentes bases de données (Brightway et VoLCA), notamment pour la base de données BAFU et la base de données Agribalyse. Des corrections et des améliorations ont été apportées pour assurer la compatibilité avec les dernières versions des dépendances et pour faciliter l'utilisation des outils, en particulier dans les notebooks Jupyter.

### Évolutions fonctionnelles
- Ajout d'un outil de diagnostic de caractérisation des flux pour la base de données BAFU. [#1234](https://github.com/MTES-MCT/ecobalyse-method-tooling/issues/1234)
- Ajout d'un outil de comparaison (parity-cloud) entre Brightway et VoLCA pour la base de données BAFU, permettant d'identifier les divergences. [#1234](https://github.com/MTES-MCT/ecobalyse-method-tooling/issues/1234)
- Possibilité d'exclure les processus à long terme lors de la comparaison avec l'option `--exclude-long-term`, pour correspondre au comportement d'Ecobalyse.
- Amélioration de la recette Agribalyse : l'extraction de la recette et l'ajout de fichiers README facilitent son utilisation.
- Ajout de l'option `--ingredients-only` à l'outil `food/agribalyse_recipe` et lien vers la documentation pyvolca.
- Correction du titre du rapport généré par l'outil `brightway_vs_volca` pour utiliser la variable d'environnement `EB_DATABASE`.

### Évolutions techniques
- Mise à jour de l'importation d'IPython dans `explore.py` pour la compatibilité avec IPython 9.
- Correction d'une inversion d'unité (km<->m) dans `brightway_vs_volca`.
- Refactoring de l'organisation des outils `brightway_vs_volca` sous le répertoire `food/`.
- Déplacement de l'outil `brightway_vs_volca` sous le répertoire `bafu/` puis retour sous `food/`.
- Epinglage de la version de `pyvolca` à `>=0.8.0` pour assurer la stabilité de `transformed-ingredients`.
- Utilisation de VoLCA 0.9.1 pour la fonctionnalité `bulk exclude-long-term`.
- Passage de la génération d'un fichier TOML à l'upload direct de la base de données pour la recette Agribalyse.
- Correction de la résolution des chemins des données dans les notebooks Jupyter.

### Autres changements
- Ajout de documentation concernant les divergences entre Brightway et VoLCA, notamment pour l'antimoine/stibnite et les fonds marins offshore.
- Ajout de `etat_egalise.html` comme preuve de parité.
- Ajout de commentaires dans la documentation concernant un problème de VoLCA lié aux eaux souterraines.
- Ajout d'une configuration `.gitignore` pour ignorer l'état d'exécution de Jupyter (checkpoints, ystore, config dir).
- Correction de la valeur de la partie non comestible de la noix de cajou (WFLDB).
- Mise à jour des fichiers README.
