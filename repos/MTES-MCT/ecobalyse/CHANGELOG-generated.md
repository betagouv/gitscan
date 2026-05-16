## Changelog : ecobalyse (30 derniers jours, au 13 mai 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données, notamment avec l'ajout d'ingrédients HUE, de données pour les batteries et des compléments pour l'alimentation animale. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour l'exploration des données et l'édition d'éléments, ainsi que des corrections de bugs pour améliorer la précision des calculs et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'ingrédients HUE (Huile Essentielle) dans les données ([#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177)).
- Prise en charge de la distance au hub pour les calculs génériques ([#2259](https://github.com/MTES-MCT/ecobalyse/issues/2259)).
- Ajout de données pour les cellules de batterie dans le catalogue LCI ([#2244](https://github.com/MTES-MCT/ecobalyse/issues/2244)).
- Ajout d'un pays d'origine "France d'Outre-Mer" par défaut ([#2243](https://github.com/MTES-MCT/ecobalyse/issues/2243)).
- Prise en charge du refroidissement global pour le transport générique ([#2239](https://github.com/MTES-MCT/ecobalyse/issues/2239)).
- Ajout d'un exemple de "Minibus quadricycle à assistance électrique" dans les données VELI ([#2182](https://github.com/MTES-MCT/ecobalyse/issues/2182)).
- Ajout de la possibilité d'afficher la dernière connexion de l'utilisateur ([#2181](https://github.com/MTES-MCT/ecobalyse/issues/2181)).
- Ajout de données CMAP transformées ([#2096](https://github.com/MTES-MCT/ecobalyse/issues/2096)).
- Amélioration de la localisation des transformations d'éléments ([#2100](https://github.com/MTES-MCT/ecobalyse/issues/2100)).
- Ajout d'un pays "Europe et Maghreb" ([#2085](https://github.com/MTES-MCT/ecobalyse/issues/2085)).
- Ajout de transformations de cuisson ([#2069](https://github.com/MTES-MCT/ecobalyse/issues/2069)).
- Ajout de la recherche facettée légère dans l'explorateur ([#2125](https://github.com/MTES-MCT/ecobalyse/issues/2125)).
- Possibilité d'éditer les éléments dans leur propre fenêtre modale ([#2111](https://github.com/MTES-MCT/ecobalyse/issues/2111)).

### Évolutions techniques
- Correction du calcul des compléments textiles ([#2231](https://github.com/MTES-MCT/ecobalyse/issues/2231)).
- Correction de la multiplication de l'occupation des sols pour l'herbe pâturée et ajustement des coefficients SE ([#2200](https://github.com/MTES-MCT/ecobalyse/issues/2200)).
- Correction de la nouvelle convention de signe pour les compléments ([#2201](https://github.com/MTES-MCT/ecobalyse/issues/2201)).
- Suppression de la multiplication de l'occupation des terres pour l'herbe pâturée et ajustement des coefficients SE ([#2200](https://github.com/MTES-MCT/ecobalyse/issues/2200)).
- Réaffectation des transformations compatibles lors de la mise à jour d'un matériau ([#2230](https://github.com/MTES-MCT/ecobalyse/issues/2230)).
- Nettoyage du code obsolète lié aux transformations de métaux ([#2195](https://github.com/MTES-MCT/ecobalyse/issues/2195)).
- Mise à jour des dépendances Python ([#2112](https://github.com/MTES-MCT/ecobalyse/issues/2112)).
- Mise à jour des dépendances Node.js ([#2153](https://github.com/MTES-MCT/ecobalyse/issues/2153)).
- Amélioration des messages d'erreur du backend de contribution ([#2092](https://github.com/MTES-MCT/ecobalyse/issues/2092)).
- Suppression de l'authentification par cookie ([#2110](https://github.com/MTES-MCT/ecobalyse/issues/2110)).

### Autres changements
- Renommage de la viande de porc ([#2169](https://github.com/MTES-MCT/ecobalyse/issues/2169)).
- Ajout de packages CTCPA à food2 ([#2166](https://github.com/MTES-MCT/ecobalyse/issues/2166)).
- Ajout d'origines d'outre-mer ([#2163](https://github.com/MTES-MCT/ecobalyse/issues/2163)).
- Suppression de données de picking pour l'explorateur textile ([#2129](https://github.com/MTES-MCT/ecobalyse/issues/2129)).
- Correction des problèmes de performance de l'explorateur ([#2154](https://github.com/MTES-MCT/ecobalyse/issues/2154)).
- Ajout de compléments laitiers ([#2108](https://github.com/MTES-MCT/ecobalyse/issues/2108)).
- Suppression de la densité de bétail ([#2124](https://github.com/MTES-MCT/ecobalyse/issues/2124)).
- Correction des composants d'objet ([#2142](https://github.com/MTES-MCT/ecobalyse/issues/2142)).
- Suppression de certains pays dans food1 ([#2101](https://github.com/MTES-MCT/ecobalyse/issues/2101)).
- Mise à jour des exemples VELI ([#1716](https://github.com/MTES-MCT/ecobalyse/issues/1716)).
- Correction des ingrédients ([#2022](https://github.com/MTES-MCT/ecobalyse/issues/2022)).
- Correction du coton biologique avec irrigation ([#2021](https://github.com/MTES-MCT/ecobalyse/issues/2021)).
- Ajout de 500km de transport routier par défaut pour la France ([#2099](https://github.com/MTES-MCT/ecobalyse/issues/2099)).
- Ajout d'un pays inconnu dans food1 ([#2102](https://github.com/MTES-MCT/ecobalyse/issues/2102)).
- Ajout de catégories EoL ([#2120](https://github.com/MTES-MCT/ecobalyse/issues/2120)).
- Correction des activités EoL ([#2105](https://github.com/MTES-MCT/ecobalyse/issues/2105)).
- Suppression de matériaux obsolètes ([#2151](https://github.com/MTES-MCT/ecobalyse/issues/2151)).
- Mise à jour de heat-europe ([#2117](https://github.com/MTES-MCT/ecobalyse/issues/2117)).
- Ajout de titres pour améliorer la lisibilité du modèle de problème ([#2122](https://github.com/MTES-MCT/ecobalyse/issues/2122)).
- Alignement des alias EoL ([#2123](https://github.com/MTES-MCT/ecobalyse/issues/2123)).
- Ajout de compléments forestiers ([#1750](https://github.com/MTES-MCT/ecobalyse/issues/1750)).
- Mise à jour de pre-commit ([#2173](https://github.com/MTES-MCT/ecobalyse/issues/2173)).
