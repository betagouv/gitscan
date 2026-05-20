## Changelog : ecobalyse (30 derniers jours, au 2026-05-20)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données (ingrédients HUE, batteries, CMAP, aliments), l'amélioration de la gestion des transports (distance, refroidissement global), et la correction de bugs liés aux calculs, aux performances de l'interface utilisateur et à la synchronisation des données. Des améliorations ont également été apportées à l'expérience utilisateur, notamment dans l'explorateur d'objets et la gestion des éléments.

### Évolutions fonctionnelles
- Ajout de données pour les ingrédients HUE ([#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177)).
- Prise en charge de la distance au hub pour les calculs génériques ([#2259](https://github.com/MTES-MCT/ecobalyse/issues/2259)).
- Gestion du refroidissement global pour les transports génériques ([#2239](https://github.com/MTES-MCT/ecobalyse/issues/2239)).
- Ajout de données pour les cellules de batterie dans le catalogue LCI ([#2244](https://github.com/MTES-MCT/ecobalyse/issues/2244)).
- Ajout d'ingrédients CMAP transformés ([#2096](https://github.com/MTES-MCT/ecobalyse/issues/2096)).
- Ajout d'ingrédients UE ([#2075](https://github.com/MTES-MCT/ecobalyse/issues/2075)).
- Ajout d'un exemple de "Minibus quadricycle à assistance électrique" ([#2182](https://github.com/MTES-MCT/ecobalyse/issues/2182)).
- Ajout de métadonnées pour les aliments ([#2089](https://github.com/MTES-MCT/ecobalyse/issues/2089)).
- Amélioration de la recherche avec une recherche par facettes légère dans l'explorateur ([#2125](https://github.com/MTES-MCT/ecobalyse/issues/2125)).
- Possibilité d'éditer les éléments dans une fenêtre modale dédiée ([#2111](https://github.com/MTES-MCT/ecobalyse/issues/2111)).
- Ajout de compléments pour le lait ([#2108](https://github.com/MTES-MCT/ecobalyse/issues/2108)).
- Ajout d'un pays inconnu pour les aliments ([#2102](https://github.com/MTES-MCT/ecobalyse/issues/2102)).

### Évolutions techniques
- Synchronisation des données avec le dépôt de données améliorée ([#2265](https://github.com/MTES-MCT/ecobalyse/issues/2265)).
- Correction de problèmes de synchronisation avec le dépôt de données ([#2284](https://github.com/MTES-MCT/ecobalyse/issues/2284)).
- Refactorisation pour utiliser "stage" au lieu de "step" dans le code ([#1738](https://github.com/MTES-MCT/ecobalyse/issues/1738)).
- Mise à jour des dépendances NodeJS ([#2276](https://github.com/MTES-MCT/ecobalyse/issues/2276), [#2153](https://github.com/MTES-MCT/ecobalyse/issues/2153)).
- Mise à jour des dépendances Python ([#2112](https://github.com/MTES-MCT/ecobalyse/issues/2112)).
- Amélioration des performances de l'explorateur ([#2154](https://github.com/MTES-MCT/ecobalyse/issues/2154)).
- Correction de problèmes de performance dans l'explorateur ([#2154](https://github.com/MTES-MCT/ecobalyse/issues/2154)).
- Suppression de code obsolète (métaux, etc.) ([#2195](https://github.com/MTES-MCT/ecobalyse/issues/2195), [#2124](https://github.com/MTES-MCT/ecobalyse/issues/2124)).

### Autres changements
- Exclusion du dossier de données de l'image Scalingo ([#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300)).
- Correction de warnings Dependabot ([#2270](https://github.com/MTES-MCT/ecobalyse/issues/2270)).
- Correction du CI ([#2297](https://github.com/MTES-MCT/ecobalyse/issues/2297)).
- Ajout de la date de dernière connexion pour les utilisateurs ([#2181](https://github.com/MTES-MCT/ecobalyse/issues/2181)).
- Renommage de la viande de porc ([#2169](https://github.com/MTES-MCT/ecobalyse/issues/2169)).
- Ajout d'une origine "Outre-Mer" ([#2163](https://github.com/MTES-MCT/ecobalyse/issues/2163)).
- Correction du calcul des compléments textiles ([#2231](https://github.com/MTES-MCT/ecobalyse/issues/2231)).
- Correction de la multiplication de l'occupation des terres pour l'herbe pâturée ([#2200](https://github.com/MTES-MCT/ecobalyse/issues/2200)).
- Correction de la nouvelle convention de signe pour les compléments ([#2201](https://github.com/MTES-MCT/ecobalyse/issues/2201)).
- Correction de l'utilisation de l'énergie locale au stade d'utilisation/consommation ([#2180](https://github.com/MTES-MCT/ecobalyse/issues/2180)).
- Correction de la logique de réaffectation des transformations compatibles ([#2230](https://github.com/MTES-MCT/ecobalyse/issues/2230)).
- Définition de la France comme origine par défaut pour certains ingrédients bio ([#2150](https://github.com/MTES-MCT/ecobalyse/issues/2150)).
- Ajout de packages CTCPA pour les aliments ([#2166](https://github.com/MTES-MCT/ecobalyse/issues/2166)).
- Suppression de certains pays dans food1 ([#2101](https://github.com/MTES-MCT/ecobalyse/issues/2101)).
- Amélioration de l'UX de la fenêtre modale d'édition d'éléments ([#2128](https://github.com/MTES-MCT/ecobalyse/issues/2128)).
- Correction de problèmes liés à la hauteur des cellules de commentaires dans l'admin des processus ([#2112](https://github.com/MTES-MCT/ecobalyse/issues/2112)).
- Ajout de titres pour améliorer la lisibilité du modèle de rapport de bug ([#2122](https://github.com/MTES-MCT/ecobalyse/issues/2122)).
- Correction des catégories EoL ([#2120](https://github.com/MTES-MCT/ecobalyse/issues/2120)).
- Correction de l'alignement des impacts dans le simulateur d'objets ([#2120](https://github.com/MTES-MCT/ecobalyse/issues/2120)).
- Correction de l'ordre des transformations ([#1700](https://github.com/MTES-MCT/ecobalyse/issues/1700)).
- Correction de l'URL partageable ([#1741](https://github.com/MTES-MCT/ecobalyse/issues/1741)).
