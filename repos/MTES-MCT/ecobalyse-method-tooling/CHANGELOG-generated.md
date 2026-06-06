## Changelog : ecobalyse-method-tooling (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du processus de transformation des ingrédients, notamment en corrigeant des problèmes de résolution de données, en optimisant la correspondance des ingrédients et en affinant la gestion des variantes.  Plusieurs corrections ont été apportées pour assurer la cohérence et la qualité des données transformées, ainsi que pour faciliter l'intégration avec le dépôt de données Ecobalyse.

### Évolutions fonctionnelles
- Amélioration de la correspondance des ingrédients grâce à une pénalisation des références multi-mots bruyantes dans le matcher de voisins les plus proches. [#da4d97d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/da4d97d)
- Correction de la gestion des collisions de noms d'affichage lors de la fusion du catalogue LCI. [#39304da](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/39304da)
- Suppression de la Soja de la variante BIO. [#0ee7b9b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/0ee7b9b)
- Génération de nouvelles versions avec 5 variantes. [#47f31af](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/47f31af)
- Mise à jour des chemins README pour refléter le dépôt de données Ecobalyse fusionné. [#3fa0659](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/3fa0659)

### Évolutions techniques
- Refactorisation du script `export.py` pour unifier la logique des variantes, typifier le flux de données et différer les effets secondaires. [#c0cf4de](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c0cf4de)
- Optimisation du matcher de groupes de cultures pour une meilleure correspondance et une plus grande transparence de la confiance. [#dc9a01e](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/dc9a01e)
- Simplification du code en supprimant les docstrings et commentaires redondants, et en intégrant les fonctions utilitaires à usage unique. [#cfcd323](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/cfcd323)
- Correction de la résolution VoLCA et déduplication des produits. [#c174dfa](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/c174dfa)
- Amélioration de la dérivation des entrées à partir du chemin du dépôt Ecobalyse. [#89d9915](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/89d9915)
- Mise à jour de `transformers` vers la version 5.x. [#e46bea9](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/e46bea9)
- Correction de la gestion des identités d'activité lors de la fusion du catalogue LCI, en préservant les identifiants UUID. [#081c66c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/081c66c)
- Suppression du suffixe `-2025` des alias au niveau de l'activité (espace de noms des ingrédients uniquement). [#b7dbe8a](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b7dbe8a)
- Correction de l'émission de clés de base de données redondantes au niveau supérieur. [#27ebf53](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/27ebf53)

### Autres changements
- Synchronisation de la documentation avec les entrées du catalogue LCI et ses 5 variantes. [#172190d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/172190d)
- Correction d'un problème d'ancrage des alias. [#ce4808c](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/ce4808c)
- Régénération des sorties après avoir ignoré les bases de données non chargées. [#b3145b5](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/b3145b5)
- Nouvelle génération. [#4850ca2](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/4850ca2)
- Correction pour préserver l'UUID de l'activité lors du renommage legacy `-2025`. [#5626ea6](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/5626ea6)
- Mise à jour des packages. [#3e7e52d](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/3e7e52d)
- Correction de vulnérabilités dans les fichiers `uv.lock`. [#d90e144](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/d90e144)
- Régénération des ingrédients transformés. [#300787b](https://github.com/MTES-MCT/ecobalyse-method-tooling/commit/300787b)
