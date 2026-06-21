## Changelog : ecobalyse (30 derniers jours, au 18 juin 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement de la base de données avec de nouveaux éléments (composants, matériaux, transports) et l'amélioration de la précision des données existantes. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la fiabilité et la performance de l'application. Enfin, des améliorations ont été apportées à l'interface utilisateur pour faciliter l'exploration des données.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les processus par câble dans l'interface VELI. [#2459](https://github.com/MTES-MCT/ecobalyse/issues/2459)
- Ajout de la gestion des batteries dans VELI, incluant différents types de piles (AA, AAA, NMC622). [#2453](https://github.com/MTES-MCT/ecobalyse/issues/2453), [#2406](https://github.com/MTES-MCT/ecobalyse/issues/2406), [#2362](https://github.com/MTES-MCT/ecobalyse/issues/2362)
- Ajout de nouveaux matériaux et processus dans la base de données : verre feuilleté, emballages bois et papier, non-tissé polyester, pneus, céréales et légumineuses cuisinés. [#2415](https://github.com/MTES-MCT/ecobalyse/issues/2415), [#2404](https://github.com/MTES-MCT/ecobalyse/issues/2404), [#2421](https://github.com/MTES-MCT/ecobalyse/issues/2421), [#2402](https://github.com/MTES-MCT/ecobalyse/issues/2402), [#2397](https://github.com/MTES-MCT/ecobalyse/issues/2397)
- Ajout de la gestion du transport routier depuis le Maroc. [#2144](https://github.com/MTES-MCT/ecobalyse/issues/2144)
- Amélioration de l'affichage des alias dans l'explorateur de données. [#2444](https://github.com/MTES-MCT/ecobalyse/issues/2444)
- Ajout d'une fonctionnalité pour gérer l'emballage dédié avec des paramètres d'interface utilisateur et de requête. [#2438](https://github.com/MTES-MCT/ecobalyse/issues/2438)
- Publication de la section réglementaire pour l'alimentation. [#2312](https://github.com/MTES-MCT/ecobalyse/issues/2312)

### Évolutions techniques
- Refactorisation pour autoriser les clés d'impact manquantes, avec une valeur par défaut de zéro. [#2417](https://github.com/MTES-MCT/ecobalyse/issues/2417)
- Amélioration de la fiabilité des tests E2E en réduisant le besoin de tentatives. [#2422](https://github.com/MTES-MCT/ecobalyse/issues/2422)
- Mise à jour des dépendances Python, Node.js et npm. [#2499](https://github.com/MTES-MCT/ecobalyse/issues/2499), [#2500](https://github.com/MTES-MCT/ecobalyse/issues/2500), [#2486](https://github.com/MTES-MCT/ecobalyse/issues/2486), [#2399](https://github.com/MTES-MCT/ecobalyse/issues/2399), [#2389](https://github.com/MTES-MCT/ecobalyse/issues/2389), [#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341)
- Utilisation de JSON pour stocker les composants. [#2393](https://github.com/MTES-MCT/ecobalyse/issues/2393)
- Correction d'un bug empêchant l'affichage correct des impacts dans le comparateur VELI. [#2374](https://github.com/MTES-MCT/ecobalyse/issues/2374)
- Amélioration de la gestion des distances intra-pays. [#2301](https://github.com/MTES-MCT/ecobalyse/issues/2301)

### Autres changements
- Ajout d'un ADR (Architecture Decision Record) pour la gestion de la localisation des composants. [#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900)
- Suppression de processus obsolètes. [#2311](https://github.com/MTES-MCT/ecobalyse/issues/2311)
- Correction d'un bug lié au facteur de complément forestier. [#2391](https://github.com/MTES-MCT/ecobalyse/issues/2391)
- Correction d'un bug lié à la régression de l'alimentation. [#2318](https://github.com/MTES-MCT/ecobalyse/issues/2318)
- Mise à jour de la base de données browserslist. [#2407](https://github.com/MTES-MCT/ecobalyse/issues/2407)
- Suppression de la gestion du transport aérien entre les étapes de transformation. [#2398](https://github.com/MTES-MCT/ecobalyse/issues/2398)
