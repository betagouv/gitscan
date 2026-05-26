## Changelog : ecobalyse-method-tooling (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des données d'ingrédients et d'activités, notamment en vue de l'intégration de nouvelles variantes (HUE, NUE, BIO, OI, FR). Des corrections ont été apportées pour assurer la cohérence et la précision des données, ainsi que des optimisations pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- Amélioration du processus de fusion du catalogue LCI pour éviter les collisions de noms d'affichage entre les lots de données [#39304da](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/39304da).
- Ajout de la variante NUE et régénération des ingrédients transformés [#45c67d0](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/45c67d0).
- Re-export des prédictions pour toutes les variantes (FR, BIO, OI, NUE) [#f14ca5b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/f14ca5b).
- Correction du système de correspondance des groupes de cultures pour améliorer la précision des correspondances [#dc9a01e](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/dc9a01e).
- Correction de la logique de correspondance des voisins les plus proches pour pénaliser les références multi-mots bruyantes [#da4d97d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/da4d97d).
- Correction d'un problème avec la gestion des alias d'activités, notamment pour les activités héritées avec le suffixe `-2025` [#5626ea6](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5626ea6).
- Correction d'un problème avec la gestion des alias d'ingrédients, en supprimant les listes alternatives de la source [#a083be1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/a083be1).
- Correction pour la gestion des mangues [#51b346a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/51b346a).

### Évolutions techniques
- Refactorisation du script `export.py` pour unifier la logique des variantes, typifier le flux de données et différer les effets secondaires [#c0cf4de](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c0cf4de).
- Optimisation du code en supprimant les docstrings et commentaires redondants, et en intégrant les fonctions d'aide à usage unique [#cfcd323](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/cfcd323).
- Mise à jour de la bibliothèque `transformers` vers la version 5.x dans les métadonnées [#e46bea9](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/e46bea9).
- Adaptation au dernier version de `pyvolca` [#0158bb1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0158bb1).
- Suppression de `Soybean` de la variante BIO [#0ee7b9b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0ee7b9b).
- Modification du format des fichiers de documentation de `.txt` à `.md` [#e0409e1](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/e0409e1).

### Autres changements
- Mise à jour des chemins dans le fichier README pour refléter le nouveau dépôt `ecobalyse-data` [#3fa0659](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/3fa0659).
- Intégration des primitives de fusion du catalogue LCI et du générateur d'ingrédients transformés [#cba2cac](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/cba2cac).
- Modification de la façon dont les activités sont stockées, en les déplaçant vers `lci_catalog/` au lieu de `activities.json` [#0f45995](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0f45995).
- Suppression des marqueurs d'alias d'archive avant la prédiction [#2dc1373](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/2dc1373).
- Suppression du suffixe `-2025` des alias d'ingrédients [#c9f485d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c9f485d).
- Suppression des marqueurs d'année (par exemple, ` 2025`) des alias d'activité [#25f0172](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/25f0172).
- Mise à jour de la documentation et des commentaires pour une meilleure clarté.
- Correction de bugs mineurs et améliorations de la stabilité.
- Suppression des dépendances vulnérables [#d90e144](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d90e144).
