## Changelog : ecobalyse-method-tooling (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion et de la transformation des ingrédients dans le cadre de l'écobilan. Des améliorations significatives ont été apportées à l'outil `transformed-ingredients`, notamment en termes de résolution des données VoLCA, de déduplication des produits et de gestion des alias. L'intégration de nouveaux variants (NUE, HUE) et la correction de problèmes liés à la fusion du catalogue LCI ont également été des points clés.

### Évolutions fonctionnelles
- Amélioration de la résolution des données VoLCA dans `transformed-ingredients` [#1234](https://github.com/MTES-MCT/ecobalyse-method-tooling/issues/1234).
- Ajout de la prise en charge de nouveaux variants : NUE et HUE.
- Génération des prédictions pour tous les variants (FR, BIO, OI, NUE).
- Correction de la gestion des doublons de noms d'ingrédients lors de la fusion du catalogue LCI.
- Amélioration du matcher de groupes de cultures pour une meilleure correspondance et une plus grande précision.
- Suppression de l'ingrédient "Soybean" du variant BIO.
- Mise à jour des chemins dans le README pour refléter le nouveau dépôt `ecobalyse-data`.

### Évolutions techniques
- Refactorisation du script `export.py` pour unifier la logique des variants, typer le flux de données et différer les effets secondaires.
- Optimisation du code en supprimant les docstrings et commentaires redondants, et en intégrant les fonctions utilitaires à usage unique.
- Amélioration du matcher de voisins les plus proches pour pénaliser les références multi-mots bruyantes.
- Mise à jour de la dépendance `transformers` vers la version 5.x.
- Correction de la gestion des UUID d'activité lors de la migration des données.
- Suppression du suffixe `-2025` des alias d'activité au niveau de l'ingrédient.
- Intégration des primitives de fusion du catalogue LCI et de la génération d'ingrédients transformés.
- Mise à jour de `pyvolca`.

### Autres changements
- Synchronisation de la documentation de `transformed-ingredients` avec les entrées et les 5 variants du catalogue LCI.
- Correction d'un problème de collision de noms d'affichage lors de la fusion du catalogue LCI.
- Correction de bugs mineurs et améliorations de la robustesse du code.
- Mise à jour des dépendances vulnérables dans les fichiers `uv.lock`.
- Suppression des bases de données non chargées lors de la génération des ingrédients transformés.
