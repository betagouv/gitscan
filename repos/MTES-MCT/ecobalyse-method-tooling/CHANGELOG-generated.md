## Changelog : ecobalyse-method-tooling (30 derniers jours, au 14 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration des outils de comparaison entre Brightway et VoLCA, notamment pour les bases de données BAFU et Agribalyse. De nouvelles fonctionnalités ont été ajoutées pour faciliter l'analyse et le diagnostic des données, ainsi que pour gérer les ingrédients et les exclusions à long terme.

### Évolutions fonctionnelles
- Ajout d'un outil pour comparer les données Brightway et VoLCA pour la base de données BAFU, incluant des diagnostics sur la caractérisation des flux [#1234](https://github.com/MTES-MCT/ecobalyse-method-tooling/issues/1234).
- Implémentation d'un outil pour évaluer la parité entre Brightway et VoLCA, avec des preuves documentées et la prise en compte de problèmes spécifiques à VoLCA (eaux souterraines).
- Possibilité d'exclure les éléments à long terme lors de la comparaison, en cohérence avec les options d'Ecobalyse.
- Amélioration de l'outil `agribalyse_recipe` avec l'ajout de l'option `--ingredients-only` et un lien vers la documentation pyvolca.
- Téléchargement direct de la base de données Agribalyse au lieu de générer un fichier TOML.
- Correction de l'unité de conversion km<->m dans la comparaison Brightway/VoLCA.

### Évolutions techniques
- Passage de l'outil `brightway_vs_volca` sous le répertoire `food/`.
- Refactoring du code pour déplacer `brightway_vs_volca` sous `bafu/` puis de nouveau sous `food/`.
- Nécessité de VoLCA 0.9.1 pour l'exclusion en masse des éléments à long terme.
- Épingle de la version de pyvolca à >=0.8.0 pour assurer la compatibilité.
- Utilisation de VoLCA via pyvolca pour l'upload de la base de données BAFU.

### Autres changements
- Documentation : Ajout de documentation sur les divergences entre antimony/stibnite et offshore seabed.
- Documentation : Ajout de `etat_egalise.html` comme preuve de parité.
- Extraction des recettes Agribalyse et ajout de fichiers README.
- Mise à jour des fichiers README.
