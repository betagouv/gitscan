## Changelog : ecobalyse (30 derniers jours, au 28 avril 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données, notamment pour les ingrédients alimentaires, les matériaux et les processus de transformation. Des améliorations de l'interface utilisateur ont été apportées, en particulier pour la recherche et l'édition d'éléments, ainsi que pour l'exploration des données. Plusieurs corrections de bugs et optimisations techniques ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de métadonnées génériques pour les aliments ([#2089](https://github.com/MTES-MCT/ecobalyse/issues/2089)).
- Définition de la France comme origine par défaut pour certains ingrédients biologiques ([#2150](https://github.com/MTES-MCT/ecobalyse/issues/2150)).
- Suppression d'éléments obsolètes (matériaux, densité d'élevage) pour simplifier la base de données ([#2124](https://github.com/MTES-MCT/ecobalyse/issues/2124), [#2151](https://github.com/MTES-MCT/ecobalyse/issues/2151)).
- Amélioration de l'expérience utilisateur lors de l'édition d'éléments via une fenêtre modale dédiée ([#2111](https://github.com/MTES-MCT/ecobalyse/issues/2111), [#2128](https://github.com/MTES-MCT/ecobalyse/issues/2128)).
- Ajout d'une recherche avancée (faceted search) légère dans l'explorateur de données ([#2125](https://github.com/MTES-MCT/ecobalyse/issues/2125)).
- Ajout d'un pays "Europe et Maghreb" ([#2085](https://github.com/MTES-MCT/ecobalyse/issues/2085)).
- Ajout de la possibilité d'ajouter un pays inconnu pour les données alimentaires ([#2102](https://github.com/MTES-MCT/ecobalyse/issues/2102)).
- Ajout de compléments de processus dans l'explorateur ([#1966](https://github.com/MTES-MCT/ecobalyse/issues/1966)).
- Ajout de processus de recyclage ([#2005](https://github.com/MTES-MCT/ecobalyse/issues/2005)).
- Ajout de compléments pour les aliments animaux ([#1944](https://github.com/MTES-MCT/ecobalyse/issues/1944)).
- Correction du calcul par défaut des kilomètres de transport routier pour la France ([#2099](https://github.com/MTES-MCT/ecobalyse/issues/2099), [#2109](https://github.com/MTES-MCT/ecobalyse/issues/2109)).
- Localisation des transformations d'éléments ([#2100](https://github.com/MTES-MCT/ecobalyse/issues/2100)).
- Ajout de processus de transformation liés à la cuisine ([#2069](https://github.com/MTES-MCT/ecobalyse/issues/2069)).
- Ajout de catégories de fin de vie (EoL) corrigées et alignées ([#2120](https://github.com/MTES-MCT/ecobalyse/issues/2120), [#2105](https://github.com/MTES-MCT/ecobalyse/issues/2105)).
- Ajout de types de matériaux ([#1980](https://github.com/MTES-MCT/ecobalyse/issues/1980)).

### Évolutions techniques
- Mise à jour des dépendances Node.js ([#2153](https://github.com/MTES-MCT/ecobalyse/issues/2153), [#2112](https://github.com/MTES-MCT/ecobalyse/issues/2112)).
- Amélioration de la gestion des erreurs dans le backend de la contribution ([#2092](https://github.com/MTES-MCT/ecobalyse/issues/2092)).
- Refactorisation du code pour utiliser "stage" au lieu de "step" ([#1738](https://github.com/MTES-MCT/ecobalyse/issues/1738)).
- Mise à jour de la configuration de Dependabot pour une meilleure gestion des branches et des écosystèmes ([#1977](https://github.com/MTES-MCT/ecobalyse/issues/1977)).
- Suppression de l'authentification par cookie ([#2110](https://github.com/MTES-MCT/ecobalyse/issues/2110)).
- Amélioration de la lisibilité du modèle de rapport de bug ([#2122](https://github.com/MTES-MCT/ecobalyse/issues/2122)).
- Correction de problèmes liés aux composants d'objet ([#2142](https://github.com/MTES-MCT/ecobalyse/issues/2142)).
- Mise à jour des dépendances Python ([#2112](https://github.com/MTES-MCT/ecobalyse/issues/2112)).
- Mise à jour des dépendances Elm ([#2014](https://github.com/MTES-MCT/ecobalyse/issues/2014), [#2080](https://github.com/MTES-MCT/ecobalyse/issues/2080)).

### Autres changements
- Ajout de tests d'intégrité de la base de données JSON ([#1953](https://github.com/MTES-MCT/ecobalyse/issues/1953)).
- Amélioration des messages d'erreur du backend de contribution ([#2092](https://github.com/MTES-MCT/ecobalyse/issues/2092)).
- Correction de la synchronisation des données ecobalyse-data ([#1979](https://github.com/MTES-MCT/ecobalyse/issues/1979)).
- Suppression de l'affichage des animaux vivants ([#2053](https://github.com/MTES-MCT/ecobalyse/issues/2053)).
- Ajout de compléments pour le lait ([#2108](https://github.com/MTES-MCT/ecobalyse/issues/2108)).
- Correction de l'emplacement des activités créées ([#1919](https://github.com/MTES-MCT/ecobalyse/issues/1919)).
- Ajout de la possibilité de configurer la visibilité de la documentation de l'API food1 legacy ([#2088](https://github.com/MTES-MCT/ecobalyse/issues/2088)).
- Correction de l'ajout de 500km de transport routier pour certains pays ([#2004](https://github.com/MTES-MCT/ecobalyse/issues/2004)).
- Correction de la duplication de processus dans l'explorateur ([#1968](https://github.com/MTES-MCT/ecobalyse/issues/1968)).
- Ajout de la catégorie de matériaux aux ingrédients ([#1972](https://github.com/MTES-MCT/ecobalyse/issues/1972)).
- Ajout de processus d'utilisation des forêts ([#1750](https://github.com/MTES-MCT/ecobalyse/issues/1750)).
- Correction de l'application de massperunit à l'emballage ([#1763](https://github.com/MTES-MCT/ecobalyse/issues/1763)).
- Correction de l'erreur de perte de données de session lors de la navigation entre les versions ([#1756](https://github.com/MTES-MCT/ecobalyse/issues/1756)).
- Ajout du slash manquant à l'URL partageable ([#1741](https://github.com/MTES-MCT/ecobalyse/issues/1741)).
- Correction de l'alignement des impacts dans les détails du simulateur d'objet ([#1720](https://github.com/MTES-MCT/ecobalyse/issues/1720)).
- Correction de l'ordre des transformations préservé ([#1700](https://github.com/MTES-MCT/ecobalyse/issues/1700)).
- Correction du bug des impacts détaillés sur l'objet/veli ([#1709](https://github.com/MTES-MCT/ecobalyse/issues/1709)).
- Correction de la hauteur de la cellule de commentaire dans l'admin des processus ([#1712](https://github.com/MTES-MCT/ecobalyse/issues/1712)).
- Mise à jour de la documentation de l'API ([#1742](https://github.com/MTES-MCT/ecobalyse/issues/1742)).
- Modification du mix électrique par défaut vers l'Inde ([#1702](https://github.com/MTES-MCT/ecobalyse/issues/1702)).
- Mise à jour des exemples veli ([#1716](https://github.com/MTES-MCT/ecobalyse/issues/1716)).
- Ajout de processus de transformation des métaux ([#2041](https://github.com/MTES-MCT/ecobalyse/issues/2041)).
- Modification des types de matériaux ([#1965](https://github.com/MTES-MCT/ecobalyse/issues/1965)).
- Correction du processus de transformation du coton biologique avec irrigation ([#2021](https://github.com/MTES-MCT/ecobalyse/issues/2021)).
- Correction du commit en lot dans load_processes_fixtures ([#2098](https://github.com/MTES-MCT/ecobalyse/issues/2098)).
- Ajout de processus de transformation dans les activités de fin de vie ([#2004](https://github.com/MTES-MCT/ecobalyse/issues/2004)).
- Ajout de compléments de processus dans l'explorateur ([#1966](https://github.com/MTES-MCT/ecobalyse/issues/1966)).
- Correction de l'erreur de processus par défaut dans food1 ([#2065](https://github.com/MTES-MCT/ecobalyse/issues/2065)).
- Correction du bug d'impacts détaillés sur l'objet/veli ([#2039](https://github.com/MTES-MCT/ecobalyse/issues/2039)).
- Ajout de l'affichage des ecs pour les invités dans l'explorateur des processus ([#1748](https://github.com/MTES-MCT/ecobalyse/issues/1748)).
- Correction de l'affichage du nom de l'emballage ([#1711](https://github.com/MTES-MCT/ecobalyse/issues/1711)).
- Ajout de la possibilité de contribuer des exemples de PR à partir de l'interface utilisateur ([#2028](https://github.com/MTES-MCT/ecobalyse/issues/2028)).
- Modification des types de matériaux dans les données ([#2070](https://github.com/MTES-MCT/ecobalyse/issues/2070)).
- Correction de l'alignement des noms d'affichage v2 ([#2082](https://github.com/MTES-MCT/ecobalyse/issues/2082)).
- Ajout de processus de recyclage ([#2005](https://github.com/MTES-MCT/ecobalyse/issues/2005)).
- Suppression de certains pays dans food1 ([#2101](https://github.com/MTES-MCT/ecobalyse/issues/2101)).
- Suppression de la densité d'élevage ([#2124](https://github.com/MTES-MCT/ecobalyse/issues/2124)).
- Suppression des activités EoL ([#2123](https://github.com/MTES-MCT/ecobalyse/issues/2123)).
- Correction des catégories EoL ([#2120](https://github.com/MTES-MCT/ecobalyse/issues/2120)).
- Correction des activités EoL ([#2105](https://github.com/MTES-MCT/ecobalyse/issues/2105)).
- Ajout de compléments pour le lait ([#2108](https://github.com/MTES-MCT/ecobalyse/issues/2108)).
- Correction de l'alignement des alias EoL ([#2123](https://github.com/MTES-MCT/ecobalyse/issues/2123)).
- Mise à jour des dépendances heat-europe ([#2117](https://github.com/MTES-MCT/ecobalyse/issues/2117)).
- Correction de l'ajout de 500km de transport routier pour la France ([#1999](https://github.com/MTES-MCT/ecobalyse/issues/1999)).
- Ajout de 2000km de route pour certains pays ([#2068](https://github.com/MTES-MCT/ecobalyse/issues/2068)).
- Ajout de 2000km de route pour certains pays ([#2068](https://github.com/MTES-MCT/ecobalyse/issues/2068)).
- Suppression de cookie auth ([#2110](https://github.com/MTES-MCT/ecobalyse/issues/2110)).
- Ajout de la possibilité de calculer les impacts de distribution ([#1963](https://github.com/MTES-MCT/ecobalyse/issues/1963)).
- Ajout de la catégorie de matériaux aux ingrédients ([#1972](https://github.com/MTES-MCT/ecobalyse/issues/1972)).
- Ajout de processus d'utilisation des aliments ([#1971](https://github.com/MTES-MCT/ecobalyse/issues/1971)).
