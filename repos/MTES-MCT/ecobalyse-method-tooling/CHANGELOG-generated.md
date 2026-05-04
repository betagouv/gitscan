## Changelog : ecobalyse-method-tooling (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des ingrédients transformés, notamment en s'inspirant des données Agribalyse. Des améliorations ont été apportées à la prédiction de métadonnées, à la gestion des alias et à l'intégration avec VoLCA. Des corrections et des ajustements ont également été effectués sur les données et les processus existants.

### Évolutions fonctionnelles
- Ajout de la prise en charge des ingrédients HUE [#1a1d227](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/1a1d227).
- Amélioration de la gestion des noms d'affichage des activités pour garantir leur unicité [#0fff8fa](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0fff8fa).
- Ajout d'une colonne `is_byproduct` et actualisation des sorties avec les co-produits d'allocation [#9e842e7](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9e842e7).
- Ajout d'une colonne `dummy_op` et actualisation des sorties à partir de la descente en couches [#63e132d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/63e132d).
- Ajout de la possibilité de prédire les métadonnées des ingrédients transformés via `predict.py` [#9bbaec7](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/9bbaec7).
- Ajout de noms d'affichage en français avec un modèle de traduction [#38c444c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/38c444c).
- Ajout de la prise en charge de la variante UE (Unités Européennes) avec des données sources CSV et des protections contre les conflits [#979bb69](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/979bb69), [#69a7652](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/69a7652), [#6fd681a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/6fd681a).

### Évolutions techniques
- Adaptation à la dernière version de pyvolca [#0158bb1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0158bb1).
- Refactorisation pour adopter `VoLCA include_edges` et le filtrage de classification [#6843eb3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/6843eb3).
- Extraction des paramètres de transformation pour toutes les activités de preset transformé [#98c63a2](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/98c63a2).
- Utilisation de preset transformé côté serveur pour la recherche des consommateurs [#c2a30bc](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c2a30bc).
- Remplacement complet du mix de consommation au lieu d'un seul ingrédient à l'intérieur [#d74e379](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d74e379).
- Correction de la gestion des collisions de noms d'affichage lors de la fusion [#d4815d3](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d4815d3).

### Autres changements
- Documentation ajoutée pour les scripts `transformed-ingredients` [#5102526](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5102526).
- Mise à jour du fichier README [#347e70b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/347e70b).
- Corrections et ajustements de données pour divers ingrédients (mangue, betterave, radis, viandes BIO) [#51b346a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/51b346a), [#b77cb2a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b77cb2a), [#cde390c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/cde390c), [#7883829](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/7883829).
- Suppression des ingrédients.json pour l'entraînement du prédicteur et la recherche finale des données [#54da4ac](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/54da4ac).
- Suppression des marqueurs d'année (ex: ` 2025`) des alias d'activité [#25f0172](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/25f0172).
- Suppression des marqueurs `{{archive-alias}}` avant la prédiction [#2dc1373](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/2dc1373).
- Raccourcissement des alias d'ingrédients en supprimant les listes alternatives dans l'élément source [#a083be1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/a083be1).
- Modification du format des fichiers de documentation de txt vers md [#e0409e1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/e0409e1).
- Correction de l'export et régénération de tous les fichiers [#1b00f66](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/1b00f66).
- Correction d'un nom de processus incorrect [#5cd5eee](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5cd5eee).
- Mise à jour des fichiers sources [#540867f](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/540867f), [#2158bb1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/2158bb1).
- Ajout d'un snapshot des ingrédients transformés générés comme base de référence [#5cefe47](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5cefe47).
- Ajout d'une description dans la docstring expliquant la stratégie utilisée [#b4b261c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b4b261c).
- Ajout d'un fichier `.gitignore` [#b26f2df](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b26f2df).
