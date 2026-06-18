## Changelog : ecobalyse (30 derniers jours, au 2026-06-17)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement de la base de données avec de nouveaux composants et processus, notamment dans les domaines des batteries, des emballages et des transports. Des améliorations ont également été apportées à la fiabilité des tests et à la gestion des données, ainsi qu'à l'interface utilisateur pour une meilleure expérience.

### Évolutions fonctionnelles
- Ajout de données pour les câbles ([#2459](https://github.com/MTES-MCT/ecobalyse/issues/2459)).
- Mise à jour des données relatives aux batteries ([#2453](https://github.com/MTES-MCT/ecobalyse/issues/2453)).
- Ajout de données pour les batteries NMC622, AA et AAA ([#2406](https://github.com/MTES-MCT/ecobalyse/issues/2406)).
- Ajout de données pour le verre feuilleté ([#2403](https://github.com/MTES-MCT/ecobalyse/issues/2403)).
- Ajout de données pour le transport routier depuis le Maroc ([#2144](https://github.com/MTES-MCT/ecobalyse/issues/2144)).
- Ajout de données pour les emballages en bois et papier, et ouverture vers les emballages objets ([#2404](https://github.com/MTES-MCT/ecobalyse/issues/2404)).
- Ajout de données pour le polyester non tissé ([#2421](https://github.com/MTES-MCT/ecobalyse/issues/2421)).
- Ajout de données pour le processus de fabrication de pneus ([#2415](https://github.com/MTES-MCT/ecobalyse/issues/2415)).
- Ajout de la possibilité de gérer les compléments alimentaires dans l'interface utilisateur ([#2027](https://github.com/MTES-MCT/ecobalyse/issues/2027)).
- Ajout d'un champ "recyclable" ([#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229)).
- Ajout de données pour les céréales et les légumineuses cuites ([#2402](https://github.com/MTES-MCT/ecobalyse/issues/2402)).
- Ajout de données pour le gaz dans la cuisine ([#2211](https://github.com/MTES-MCT/ecobalyse/issues/2211)).
- Publication de la section réglementaire pour l'alimentation ([#2312](https://github.com/MTES-MCT/ecobalyse/issues/2312)).
- Amélioration de l'affichage des alias dans l'explorateur ([#2444](https://github.com/MTES-MCT/ecobalyse/issues/2444)).
- Ajout de l'emballage CFF dans les processus d'emballage alimentaire ([#2320](https://github.com/MTES-MCT/ecobalyse/issues/2320)).

### Évolutions techniques
- Amélioration de la fiabilité des tests E2E en supprimant les tentatives ([#2422](https://github.com/MTES-MCT/ecobalyse/issues/2422)).
- Refactorisation pour autoriser les clés d'impact manquantes ou mises à zéro par défaut ([#2417](https://github.com/MTES-MCT/ecobalyse/issues/2417)).
- Utilisation de JSON pour stocker les composants ([#2393](https://github.com/MTES-MCT/ecobalyse/issues/2393)).
- Mise à jour des dépendances npm et python ([#2389](https://github.com/MTES-MCT/ecobalyse/issues/2389), [#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341)).
- Amélioration de la résilience de l'exécuteur de tests E2E ([#2342](https://github.com/MTES-MCT/ecobalyse/issues/2342)).
- Ajout de packaging dédié pour l'interface utilisateur et les paramètres de requête ([#2438](https://github.com/MTES-MCT/ecobalyse/issues/2438)).
- Mise à jour des dépendances pytest-databases ([#2321](https://github.com/MTES-MCT/ecobalyse/issues/2321)).

### Autres changements
- Ajout d'un ADR pour la gestion de la localisation des composants ([#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900)).
- Suppression de processus obsolètes ([#2311](https://github.com/MTES-MCT/ecobalyse/issues/2311)).
- Correction de l'affichage du nom du processus d'assemblage de batterie ([#2375](https://github.com/MTES-MCT/ecobalyse/issues/2375)).
- Correction du type de matériau du recyclage PET fibre ([#2365](https://github.com/MTES-MCT/ecobalyse/issues/2365)).
- Correction du facteur de complément forestier ([#2391](https://github.com/MTES-MCT/ecobalyse/issues/2391)).
- Correction d'un bug de régression dans l'alimentation ([#2318](https://github.com/MTES-MCT/ecobalyse/issues/2318)).
- Correction de l'application des ratios de transport aux distances par défaut ([#2307](https://github.com/MTES-MCT/ecobalyse/issues/2307)).
- Suppression du transport aérien entre les étapes de transformation ([#2398](https://github.com/MTES-MCT/ecobalyse/issues/2398)).
- Correction du bug d'impacts détaillés sur l'objet/veli ([#1709](https://github.com/MTES-MCT/ecobalyse/issues/1709)).
- Correction de la gestion des jetons invalides ([#2353](https://github.com/MTES-MCT/ecobalyse/issues/2353)).
