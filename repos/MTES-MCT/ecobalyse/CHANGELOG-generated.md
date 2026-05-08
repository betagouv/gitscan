## Changelog : ecobalyse (30 derniers jours, au 7 mai 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'amélioration des données, notamment l'ajout d'ingrédients européens, de compléments alimentaires et de métadonnées pour l'alimentation. Des corrections et améliorations ont également été apportées à l'interface utilisateur, aux performances de l'explorateur et à la gestion des transformations et des transports. Enfin, des ajustements ont été effectués pour affiner la précision des calculs et des impacts environnementaux.

### Évolutions fonctionnelles
- Ajout de l'option de se connecter avec la date du dernier accès utilisateur ([#2181](https://github.com/MTES-MCT/ecobalyse/issues/2181)).
- Ajout d'exemples pour le "Minibus quadricycle à assistance électrique" dans les données VELI ([#2182](https://github.com/MTES-MCT/ecobalyse/issues/2182)).
- Ajout d'ingrédients européens ([#2075](https://github.com/MTES-MCT/ecobalyse/issues/2075)).
- Ajout de la possibilité d'éditer les éléments dans une fenêtre modale dédiée ([#2111](https://github.com/MTES-MCT/ecobalyse/issues/2111)).
- Ajout d'une recherche légère et structurée (faceted search) dans l'explorateur ([#2125](https://github.com/MTES-MCT/ecobalyse/issues/2125)).
- Ajout du pays "Europe et Maghreb" ([#2085](https://github.com/MTES-MCT/ecobalyse/issues/2085)).
- Ajout de compléments pour les forêts ([#1750](https://github.com/MTES-MCT/ecobalyse/issues/1750) - mentionné dans le changelog existant, mais toujours pertinent).
- Ajout de la possibilité de sélectionner des emballages CTCPA ([#1697](https://github.com/MTES-MCT/ecobalyse/issues/1697) - mentionné dans le changelog existant, mais toujours pertinent).

### Évolutions techniques
- Correction de la multiplication incorrecte de l'occupation des terres pour l'herbe pâturée et ajustement des coefficients SE ([#2200](https://github.com/MTES-MCT/ecobalyse/issues/2200)).
- Réassignation des transformations compatibles lors de la mise à jour d'un matériau ([#2230](https://github.com/MTES-MCT/ecobalyse/issues/2230)).
- Application de la nouvelle convention de signe pour les compléments ([#2201](https://github.com/MTES-MCT/ecobalyse/issues/2201)).
- Calcul des transports d'éléments ([#2174](https://github.com/MTES-MCT/ecobalyse/issues/2174)).
- Amélioration des performances de l'explorateur ([#2154](https://github.com/MTES-MCT/ecobalyse/issues/2154)).
- Mise à jour des dépendances Python ([#2112](https://github.com/MTES-MCT/ecobalyse/issues/2112)).
- Mise à jour des dépendances npm ([#2080](https://github.com/MTES-MCT/ecobalyse/issues/2080), [#2153](https://github.com/MTES-MCT/ecobalyse/issues/2153)).
- Suppression du code obsolète lié à la densité de bétail ([#2124](https://github.com/MTES-MCT/ecobalyse/issues/2124)).
- Suppression de l'authentification par cookie ([#2110](https://github.com/MTES-MCT/ecobalyse/issues/2110)).
- Suppression de données de picking obsolètes pour les produits textiles ([#2129](https://github.com/MTES-MCT/ecobalyse/issues/2129)).
- Suppression de matériaux obsolètes ([#2151](https://github.com/MTES-MCT/ecobalyse/issues/2151)).

### Autres changements
- Nettoyage du code : suppression de transformations métal obsolètes ([#2195](https://github.com/MTES-MCT/ecobalyse/issues/2195)).
- Correction de noms de produits (porc) et alignement des alias EoL ([#2169](https://github.com/MTES-MCT/ecobalyse/issues/2169), [#2123](https://github.com/MTES-MCT/ecobalyse/issues/2123)).
- Ajout de transformations de cuisson ([#2069](https://github.com/MTES-MCT/ecobalyse/issues/2069)).
- Amélioration des messages d'erreur du backend de contribution ([#2092](https://github.com/MTES-MCT/ecobalyse/issues/2092)).
- Ajout de métadonnées pour l'alimentation ([#2089](https://github.com/MTES-MCT/ecobalyse/issues/2089)).
- Ajout d'ingrédients CMAP transformés ([#2096](https://github.com/MTES-MCT/ecobalyse/issues/2096)).
- Correction de l'utilisation du mix énergétique local au stade d'utilisation/consommation ([#2180](https://github.com/MTES-MCT/ecobalyse/issues/2180)).
- Correction de l'impact détaillé sur l'objet/veli ([#2039](https://github.com/MTES-MCT/ecobalyse/issues/2039)).
- Correction de l'affichage des légendes des graphiques comparateurs lors de l'exportation ([#1704](https://github.com/MTES-MCT/ecobalyse/issues/1704)).
- Correction de l'ordre des transformations ([#1700](https://github.com/MTES-MCT/ecobalyse/issues/1700)).
- Correction de l'URL partageable ([#1741](https://github.com/MTES-MCT/ecobalyse/issues/1741)).
- Amélioration de l'UX de la fenêtre modale d'édition d'éléments ([#2128](https://github.com/MTES-MCT/ecobalyse/issues/2128)).
- Ajout de 500km de transport routier par défaut pour certains pays ([#2068](https://github.com/MTES-MCT/ecobalyse/issues/2068)).
- Correction du processus de transformation par défaut dans food1 ([#2065](https://github.com/MTES-MCT/ecobalyse/issues/2065)).
- Ajout de la France comme origine par défaut pour certains ingrédients Bio ([#2150](https://github.com/MTES-MCT/ecobalyse/issues/2150)).
- Ajout de pays d'origine outre-mer ([#2163](https://github.com/MTES-MCT/ecobalyse/issues/2163)).
- Ajout de packages CTCPA à food2 ([#2166](https://github.com/MTES-MCT/ecobalyse/issues/2166)).
- Correction de l'irrigation du coton biologique ([#2021](https://github.com/MTES-MCT/ecobalyse/issues/2021)).
