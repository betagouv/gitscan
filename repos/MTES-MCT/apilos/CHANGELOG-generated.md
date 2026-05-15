## Changelog : apilos (30 derniers jours, au 13 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des financements et des programmes, notamment dans le calcul des financements mixtes et la modification de l'administration des programmes. Des optimisations de performance ont également été réalisées pour accélérer la récupération des données de logements. Enfin, des corrections ont été apportées à la génération de documents CAF et au mapping des propriétés de financement.

### Évolutions fonctionnelles
- Ajout d'une commande permettant de modifier l'administration d'une liste de programmes. [#2160](https://github.com/MTES-MCT/apilos/issues/2160)
- Correction du nom du gestionnaire dans le template FicheCAF et suppression du champ `loyer_m2` inutile. [#2163](https://github.com/MTES-MCT/apilos/issues/2163)
- Amélioration de la logique de calcul des financements mixtes et ajustement des tests associés. [#2159](https://github.com/MTES-MCT/apilos/issues/2159)
- Gestion des champs à choix dans le mapping des propriétés de financement. [#2157](https://github.com/MTES-MCT/apilos/issues/2157)

### Évolutions techniques
- Optimisation de la récupération des logements grâce au préchargement et à la mise en cache. [#2155](https://github.com/MTES-MCT/apilos/issues/2155)
- Optimisation générale de la performance. [#2156](https://github.com/MTES-MCT/apilos/issues/2156)

### Autres changements
- Mise à jour de plusieurs dépendances :
    - `@gouvfr/dsfr` (1.14.2 -> 1.14.4) [#2138](https://github.com/MTES-MCT/apilos/issues/2138)
    - `actions/upload-artifact` (5 -> 7) [#2137](https://github.com/MTES-MCT/apilos/issues/2137)
    - `@hotwired/turbo` (8.0.21 -> 8.0.23) [#2124](https://github.com/MTES-MCT/apilos/issues/2124)
    - `orgoro/coverage` (3.2 -> 3.3) [#2162](https://github.com/MTES-MCT/apilos/issues/2162)
    - `redis` (6.4.0 -> 7.4.0) [#2111](https://github.com/MTES-MCT/apilos/issues/2111)
    - `beautifulsoup4` (4.13.5 -> 4.14.3) [#2110](https://github.com/MTES-MCT/apilos/issues/2110)
    - `virtualenv` [#2105](https://github.com/MTES-MCT/apilos/issues/2105)
    - `@hotwired/turbo` [#2131](https://github.com/MTES-MCT/apilos/issues/2131)
- Recette de nouvelles fonctionnalités. [#2161](https://github.com/MTES-MCT/apilos/issues/2161)
