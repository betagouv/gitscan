## Changelog : ecobalyse (30 derniers jours, au 6 juin 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement de la base de données avec de nouveaux matériaux et processus (batteries, bois, verre, transports), l'amélioration de la précision des calculs (facteurs de complément, distances de transport) et la correction de bugs liés à l'affichage et au fonctionnement de certaines fonctionnalités. Des améliorations techniques ont également été apportées pour la gestion des dépendances et l'infrastructure.

### Évolutions fonctionnelles
- Ajout de données pour les cellules NMC622 et les piles AA/AAA. [#2406](https://github.com/MTES-MCT/ecobalyse/issues/2406)
- Ajout de données pour l'emballage en bois et en papier, et ouverture de l'emballage à l'objet. [#2404](https://github.com/MTES-MCT/ecobalyse/issues/2404)
- Ajout de données pour le verre feuilleté. [#2403](https://github.com/MTES-MCT/ecobalyse/issues/2403)
- Ajout de données pour le transport routier depuis le Maroc. [#2144](https://github.com/MTES-MCT/ecobalyse/issues/2144)
- Ajout d'un champ "recyclable" pour les matériaux. [#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229)
- Publication de la section réglementaire "alimentation". [#2312](https://github.com/MTES-MCT/ecobalyse/issues/2312)
- Ajout d'ingrédients HUE dans les données. [#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177)
- Ajout de processus d'assemblage de batteries. [#2362](https://github.com/MTES-MCT/ecobalyse/issues/2362)
- Correction de l'affichage du nom des processus d'assemblage de batteries. [#2375](https://github.com/MTES-MCT/ecobalyse/issues/2375)
- Amélioration de la gestion des transports aériens et des distances de transport. [#2377](https://github.com/MTES-MCT/ecobalyse/issues/2398)
- Correction d'un bug empêchant l'affichage des impacts avec un token invalide. [#2353](https://github.com/MTES-MCT/ecobalyse/issues/2353)

### Évolutions techniques
- Mise à jour des dépendances npm et yarn. [#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341), [#2389](https://github.com/MTES-MCT/ecobalyse/issues/2389), [#2276](https://github.com/MTES-MCT/ecobalyse/issues/2276)
- Mise à jour des dépendances Python (brightway, pytest-databases). [#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341), [#2321](https://github.com/MTES-MCT/ecobalyse/issues/2321)
- Refactorisation du code pour améliorer la précision des calculs (coefficients de compléments alimentaires, ratios de variation de déchets). [#2314](https://github.com/MTES-MCT/ecobalyse/issues/2314), [#2306](https://github.com/MTES-MCT/ecobalyse/issues/2306)
- Amélioration de la résilience du runner de tests E2E. [#2342](https://github.com/MTES-MCT/ecobalyse/issues/2342)
- Correction de la synchronisation avec le dépôt de données. [#2265](https://github.com/MTES-MCT/ecobalyse/issues/2265)
- Suppression de processus obsolètes. [#2311](https://github.com/MTES-MCT/ecobalyse/issues/2311)
- Ajout de gaz au calcul de la cuisine. [#2211](https://github.com/MTES-MCT/ecobalyse/issues/2211)
- Ajout d'impacts à la cuisine. [#2284](https://github.com/MTES-MCT/ecobalyse/issues/2284)
- Monorepo pour les données. [#2272](https://github.com/MTES-MCT/ecobalyse/issues/2272)

### Autres changements
- Ajout d'une ADR pour la gestion de la localisation des composants. [#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900)
- Exclusion du dossier "data" de l'image Scalingo. [#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300)
- Correction du processus dans le traitement des déchets en décharge. [#2405](https://github.com/MTES-MCT/ecobalyse/issues/2405)
- Correction du type de matériau du recyclage des fibres PET. [#2365](https://github.com/MTES-MCT/ecobalyse/issues/2365)
- Correction d'un facteur de complément forestier erroné. [#2391](https://github.com/MTES-MCT/ecobalyse/issues/2391)
- Ajout de la vérification de la hiérarchie des ingrédients. [#2027](https://github.com/MTES-MCT/ecobalyse/issues/2027)
- Correction de l'affichage des processus d'assemblage de batteries. [#2292](https://github.com/MTES-MCT/ecobalyse/issues/2292)
- Correction des processus de cellules de batterie. [#2291](https://github.com/MTES-MCT/ecobalyse/issues/2291)
- Mise à jour de la base de données des navigateurs. [#2407](https://github.com/MTES-MCT/ecobalyse/issues/2407)
