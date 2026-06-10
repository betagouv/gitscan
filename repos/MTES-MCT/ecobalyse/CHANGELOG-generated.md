## Changelog : ecobalyse (30 derniers jours, au 09 juin 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement de la base de données avec de nouveaux matériaux et processus, notamment dans les domaines des batteries, de l'emballage et de l'alimentation. Des améliorations ont également été apportées à la gestion des transports, à la fiabilité des tests et à la précision des calculs. Enfin, des corrections de bugs et des optimisations techniques ont été réalisées pour améliorer l'expérience utilisateur et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de composants de batterie pour les véhicules ([#2366](https://github.com/MTES-MCT/ecobalyse/issues/2366)).
- Ajout de polyester non tissé comme matériau ([#2421](https://github.com/MTES-MCT/ecobalyse/issues/2421)).
- Ajout de bois et de papier pour l'emballage, avec possibilité d'ouverture vers un emballage objet ([#2404](https://github.com/MTES-MCT/ecobalyse/issues/2404)).
- Ajout de verre feuilleté comme matériau ([#2403](https://github.com/MTES-MCT/ecobalyse/issues/2403)).
- Ajout de transport routier depuis le Maroc ([#2144](https://github.com/MTES-MCT/ecobalyse/issues/2144)).
- Ajout d'ingrédients HUE (alimentation) ([#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177)).
- Ajout du champ "recyclable" pour les matériaux ([#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229)).
- Ajout de cellules de batterie dans le catalogue LCI ([#2244](https://github.com/MTES-MCT/ecobalyse/issues/2244)).
- Ajout de processus pour l'assemblage de batteries ([#2362](https://github.com/MTES-MCT/ecobalyse/issues/2362)).
- Amélioration de la gestion des compléments forestiers ([#2391](https://github.com/MTES-MCT/ecobalyse/issues/2391)).
- Amélioration de la vérification de la hiérarchie des ingrédients ([#2027](https://github.com/MTES-MCT/ecobalyse/issues/2027)).
- Implémentation du CFF (Coefficient de Facteur de Correction) dans les processus d'emballage alimentaire ([#2320](https://github.com/MTES-MCT/ecobalyse/issues/2320)).

### Évolutions techniques
- Refactorisation pour autoriser les clés d'impact manquantes ou initialisées à zéro ([#2417](https://github.com/MTES-MCT/ecobalyse/issues/2417)).
- Utilisation de JSON pour stocker les composants ([#2393](https://github.com/MTES-MCT/ecobalyse/issues/2393)).
- Amélioration de la fiabilité des tests E2E en supprimant les tentatives ([#2422](https://github.com/MTES-MCT/ecobalyse/issues/2422)).
- Mise à jour des dépendances npm et yarn ([#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341), [#2389](https://github.com/MTES-MCT/ecobalyse/issues/2389), [#2330](https://github.com/MTES-MCT/ecobalyse/issues/2330)).
- Mise à jour des dépendances Python et Brightway ([#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341)).
- Suppression de processus obsolètes ([#2311](https://github.com/MTES-MCT/ecobalyse/issues/2311)).
- Correction du type de matériau du recyclage PET fibre ([#2365](https://github.com/MTES-MCT/ecobalyse/issues/2365)).
- Correction de l'affichage du nom du processus d'assemblage de batterie ([#2375](https://github.com/MTES-MCT/ecobalyse/issues/2375)).
- Amélioration de la gestion des distances de transport et des hubs ([#2347](https://github.com/MTES-MCT/ecobalyse/issues/2347), [#2259](https://github.com/MTES-MCT/ecobalyse/issues/2259)).
- Correction de l'application des ratios de transport aux distances par défaut ([#2307](https://github.com/MTES-MCT/ecobalyse/issues/2307)).
- Correction de la précision des calculs pour éviter les différences de calcul ([#2303](https://github.com/MTES-MCT/ecobalyse/issues/2303)).
- Ajout d'ADR pour la gestion de la localisation des composants ([#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900)).

### Autres changements
- Ajout de céréales et de légumineuses à la cuisine ([#2402](https://github.com/MTES-MCT/ecobalyse/issues/2402)).
- Mise à jour de la base de données des navigateurs ([#2407](https://github.com/MTES-MCT/ecobalyse/issues/2407)).
- Ajout de NMC622 et de piles AA/AAA ([#2406](https://github.com/MTES-MCT/ecobalyse/issues/2406)).
- Correction d'un bug concernant le facteur de complément forestier ([#2391](https://github.com/MTES-MCT/ecobalyse/issues/2391)).
- Correction d'un bug lié à l'utilisation de l'air dans les étapes de transformation ([#2398](https://github.com/MTES-MCT/ecobalyse/issues/2398)).
- Restauration des origines d'outre-mer dans les données ([#2334](https://github.com/MTES-MCT/ecobalyse/issues/2334)).
- Exclusion du dossier "data" de l'image Scalingo ([#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300)).
- Correction du CI ([#2297](https://github.com/MTES-MCT/ecobalyse/issues/2297)).
- Ajout d'impacts à la cuisine ([#2284](https://github.com/MTES-MCT/ecobalyse/issues/2284)).
- Monorepo des données ([#2272](https://github.com/MTES-MCT/ecobalyse/issues/2272)).
- Correction des avertissements Dependabot ([#2270](https://github.com/MTES-MCT/ecobalyse/issues/2270)).
- Synchronisation avec le dépôt de données ([#2265](https://github.com/MTES-MCT/ecobalyse/issues/2265)).
