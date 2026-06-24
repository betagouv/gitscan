## Changelog : ecobalyse (30 derniers jours, au 23 juin 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement de la base de données avec de nouveaux composants et processus, notamment dans les domaines des batteries, de l'emballage et des transports. Des améliorations ont également été apportées à l'interface utilisateur, à la gestion des données et à la fiabilité des tests. Enfin, des corrections de bugs et des optimisations ont été réalisées pour améliorer l'expérience globale.

### Évolutions fonctionnelles
- Ajout de nouveaux processus et composants liés aux batteries (NMC622, AA, AAA) et aux véhicules. [#2459](https://github.com/MTES-MCT/ecobalyse/issues/2459) [#2453](https://github.com/MTES-MCT/ecobalyse/issues/2453) [#2366](https://github.com/MTES-MCT/ecobalyse/issues/2366)
- Ajout de nouveaux emballages : bois, papier, verre stratifié, PET. [#2404](https://github.com/MTES-MCT/ecobalyse/issues/2404) [#2403](https://github.com/MTES-MCT/ecobalyse/issues/2403) [#2320](https://github.com/MTES-MCT/ecobalyse/issues/2320)
- Ajout de transport routier depuis le Maroc. [#2144](https://github.com/MTES-MCT/ecobalyse/issues/2144)
- Amélioration de l'interface utilisateur pour l'affichage des alias dans l'explorateur. [#2444](https://github.com/MTES-MCT/ecobalyse/issues/2444)
- Ajout d'une interface utilisateur dédiée et de paramètres de requête pour l'emballage générique. [#2438](https://github.com/MTES-MCT/ecobalyse/issues/2438)
- Publication de la section réglementaire Food1. [#2312](https://github.com/MTES-MCT/ecobalyse/issues/2312)
- Ajout de gaz aux modes de cuisson. [#2211](https://github.com/MTES-MCT/ecobalyse/issues/2211)

### Évolutions techniques
- Refactorisation pour permettre l'absence d'impacts clés, avec une valeur par défaut de zéro. [#2417](https://github.com/MTES-MCT/ecobalyse/issues/2417)
- Amélioration de la fiabilité des tests E2E en évitant les tentatives répétées. [#2422](https://github.com/MTES-MCT/ecobalyse/issues/2422)
- Mise à jour des dépendances Python, NodeJS et npm. [#2531](https://github.com/MTES-MCT/ecobalyse/issues/2531) [#2499](https://github.com/MTES-MCT/ecobalyse/issues/2499) [#2486](https://github.com/MTES-MCT/ecobalyse/issues/2486) [#2399](https://github.com/MTES-MCT/ecobalyse/issues/2399) [#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341)
- Fusion des fichiers de processus dans le pipeline de données. [#2437](https://github.com/MTES-MCT/ecobalyse/issues/2437)
- Utilisation de JSON pour stocker les composants. [#2393](https://github.com/MTES-MCT/ecobalyse/issues/2393)
- Mise à jour de Brightway et des dépendances Python. [#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341)

### Autres changements
- Suppression de processus obsolètes dans les données VELI. [#2472](https://github.com/MTES-MCT/ecobalyse/issues/2472)
- Modification du nom de "broccoli" en "broccoli-eu". [#2476](https://github.com/MTES-MCT/ecobalyse/issues/2476)
- Correction de la terminologie pour "food1" afin d'utiliser un langage plus approprié. [#2523](https://github.com/MTES-MCT/ecobalyse/issues/2523)
- Ajout d'un ADR pour la gestion de l'emplacement des composants. [#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900)
- Correction d'un bug concernant le polyester non tissé dans le secteur des objets. [#2421](https://github.com/MTES-MCT/ecobalyse/issues/2421)
- Correction d'un facteur de complément forestier à 1000. [#2391](https://github.com/MTES-MCT/ecobalyse/issues/2391)
- Correction du type de matériau des fibres PET recyclées. [#2365](https://github.com/MTES-MCT/ecobalyse/issues/2365)
- Suppression de processus obsolètes. [#2311](https://github.com/MTES-MCT/ecobalyse/issues/2311)
- Correction de l'affichage du nom du processus d'assemblage de batterie. [#2375](https://github.com/MTES-MCT/ecobalyse/issues/2375)
- Mise à jour de la base de données des navigateurs. [#2407](https://github.com/MTES-MCT/ecobalyse/issues/2407)
- Correction de la gestion de la distance entre les hubs lors de la connaissance d'un seul pays. [#2347](https://github.com/MTES-MCT/ecobalyse/issues/2347)
- Amélioration de la résilience de l'exécuteur de tests E2E. [#2342](https://github.com/MTES-MCT/ecobalyse/issues/2342)
