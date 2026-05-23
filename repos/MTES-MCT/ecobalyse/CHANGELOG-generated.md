## Changelog : ecobalyse (30 derniers jours, au 22 mai 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'amélioration de la qualité des données, l'ajout de nouvelles fonctionnalités pour la gestion des ingrédients et des matériaux (notamment dans les domaines des batteries, des textiles et de l'alimentation), et des corrections de bugs pour améliorer la stabilité et la performance de l'application. Des optimisations ont également été apportées à l'interface utilisateur et à l'infrastructure.

### Évolutions fonctionnelles
- Ajout d'un champ "recyclable" pour les ingrédients et matériaux ([#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229)).
- Intégration de données sur les ingrédients HUE ([#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177)).
- Ajout de données pour les cellules de batterie dans le catalogue LCI ([#2244](https://github.com/MTES-MCT/ecobalyse/issues/2244)).
- Amélioration de la recherche avec une recherche facettée légère dans l'explorateur ([#2125](https://github.com/MTES-MCT/ecobalyse/issues/2125)).
- Ajout de la possibilité de voir la date de dernière connexion des utilisateurs ([#2181](https://github.com/MTES-MCT/ecobalyse/issues/2181)).
- Ajout d'ingrédients UE ([#2075](https://github.com/MTES-MCT/ecobalyse/issues/2075)).
- Ajout d'exemples de "Minibus quadricycle à assistance électrique" ([#2182](https://github.com/MTES-MCT/ecobalyse/issues/2182)).

### Évolutions techniques
- Correction d'un bug de régression du flux RSS ([#2318](https://github.com/MTES-MCT/ecobalyse/issues/2318)).
- Correction pour ne pas appliquer les ratios de transport aux distances par défaut ([#2307](https://github.com/MTES-MCT/ecobalyse/issues/2307)).
- Correction d'un problème lié à la synchronisation avec le dépôt de données ([#2265](https://github.com/MTES-MCT/ecobalyse/issues/2265)).
- Mise à jour des dépendances npm ([#2276](https://github.com/MTES-MCT/ecobalyse/issues/2276)).
- Exclusion du dossier de données de l'image Scalingo pour optimiser la taille ([#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300)).
- Correction de la CI ([#2297](https://github.com/MTES-MCT/ecobalyse/issues/2297)).
- Refactorisation pour utiliser "stage" au lieu de "step" dans le code ([#1738](https://github.com/MTES-MCT/ecobalyse/issues/1738)).
- Amélioration de la gestion des transports d'éléments ([#2174](https://github.com/MTES-MCT/ecobalyse/issues/2174)).
- Amélioration de la gestion des transports de refroidissement globaux ([#2239](https://github.com/MTES-MCT/ecobalyse/issues/2239)).
- Correction de la computation des compléments textiles ([#2231](https://github.com/MTES-MCT/ecobalyse/issues/2231)).
- Correction de la convention des signes pour les compléments ([#2201](https://github.com/MTES-MCT/ecobalyse/issues/2201)).

### Autres changements
- Corrections concernant les cellules de batterie et les processus associés ([#2291](https://github.com/MTES-MCT/ecobalyse/issues/2291), [#2292](https://github.com/MTES-MCT/ecobalyse/issues/2292)).
- Ajout d'impacts à la cuisson dans les données ([#2284](https://github.com/MTES-MCT/ecobalyse/issues/2284)).
- Monorepo pour les données ([#2272](https://github.com/MTES-MCT/ecobalyse/issues/2272)).
- Correction des avertissements Dependabot ([#2270](https://github.com/MTES-MCT/ecobalyse/issues/2270)).
- Renommage de la viande de porc ([#2169](https://github.com/MTES-MCT/ecobalyse/issues/2169)).
- Suppression de matériaux obsolètes ([#2151](https://github.com/MTES-MCT/ecobalyse/issues/2151)).
- Suppression de la densité de bétail ([#2124](https://github.com/MTES-MCT/ecobalyse/issues/2124)).
- Correction de problèmes de performance de l'explorateur ([#2154](https://github.com/MTES-MCT/ecobalyse/issues/2154)).
- Suppression de certains pays dans food1 ([#2101](https://github.com/MTES-MCT/ecobalyse/issues/2101)).
- Ajout de packages CTCPA à food2 ([#2166](https://github.com/MTES-MCT/ecobalyse/issues/2166)).
- Ajout d'une origine "Outre-Mer" ([#2163](https://github.com/MTES-MCT/ecobalyse/issues/2163)).
- Définition de la France comme origine par défaut pour certains ingrédients Bio ([#2150](https://github.com/MTES-MCT/ecobalyse/issues/2150)).
