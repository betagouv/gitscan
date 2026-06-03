## Changelog : ecobalyse (30 derniers jours, au 2 juin 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données, notamment dans les domaines de l'emballage alimentaire, des composants électroniques et des batteries, ainsi que sur l'amélioration de la précision des calculs et de la gestion des transports. Des corrections de bugs et des améliorations de l'infrastructure ont également été apportées pour une meilleure stabilité et performance de l'application.

### Évolutions fonctionnelles
- Ajout de la prise en compte du CFF (Climate Focus Factor) dans les processus d'emballage alimentaire. [#2320](https://github.com/MTES-MCT/ecobalyse/issues/2320)
- Intégration de processus pour l'assemblage de batteries. [#2362](https://github.com/MTES-MCT/ecobalyse/issues/2362)
- Ajout du champ "recyclable" pour les données des produits. [#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229)
- Publication de la section réglementaire pour les données alimentaires. [#2312](https://github.com/MTES-MCT/ecobalyse/issues/2312)
- Ajout d'exemples pour les minibus électriques. [#2182](https://github.com/MTES-MCT/ecobalyse/issues/2182)
- Amélioration de la gestion des distances de transport, notamment pour les cas où un seul pays est connu. [#2347](https://github.com/MTES-MCT/ecobalyse/issues/2347)
- Prise en compte des transports internationaux avec refroidissement. [#2239](https://github.com/MTES-MCT/ecobalyse/issues/2239)
- Ajout d'ingrédients HUE (Human Use Ecology). [#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177)

### Évolutions techniques
- Mise à jour des dépendances Brightway et Python. [#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341)
- Refactorisation du code pour déplacer les coefficients des compléments alimentaires. [#2314](https://github.com/MTES-MCT/ecobalyse/issues/2314)
- Réduction de la précision des calculs pour éviter les différences computationnelles. [#2303](https://github.com/MTES-MCT/ecobalyse/issues/2303)
- Refactorisation du ratio de variation de déchets. [#2306](https://github.com/MTES-MCT/ecobalyse/issues/2306)
- Amélioration de la résilience du runner de tests E2E. [#2342](https://github.com/MTES-MCT/ecobalyse/issues/2342)
- Mise à jour des dépendances npm. [#2330](https://github.com/MTES-MCT/ecobalyse/issues/2330)
- Correction de la synchronisation avec le dépôt de données. [#2265](https://github.com/MTES-MCT/ecobalyse/issues/2265)
- Ajout d'impacts à la cuisson. [#2284](https://github.com/MTES-MCT/ecobalyse/issues/2284)
- Monorepo pour les données. [#2272](https://github.com/MTES-MCT/ecobalyse/issues/2272)
- Mise à jour des dépendances node. [#2276](https://github.com/MTES-MCT/ecobalyse/issues/2276)

### Autres changements
- Documentation : Ajout d'une ADR (Architecture Decision Record) pour la gestion de la localisation des composants. [#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900)
- Suppression de processus obsolètes. [#2311](https://github.com/MTES-MCT/ecobalyse/issues/2311)
- Correction du type de matériau des fibres PET recyclées. [#2365](https://github.com/MTES-MCT/ecobalyse/issues/2365)
- Correction de la cellule de batterie recyclée. [#2292](https://github.com/MTES-MCT/ecobalyse/issues/2292) et [#2291](https://github.com/MTES-MCT/ecobalyse/issues/2291)
- Exclusion du dossier de données de l'image Scalingo. [#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300)
- Correction de la configuration CI. [#2297](https://github.com/MTES-MCT/ecobalyse/issues/2297)
- Correction d'un bug empêchant l'affichage des impacts avec un token invalide. [#2353](https://github.com/MTES-MCT/ecobalyse/issues/2353)
- Correction d'une régression dans l'alimentation. [#2318](https://github.com/MTES-MCT/ecobalyse/issues/2318)
- Correction de l'application des ratios de transport aux distances par défaut. [#2307](https://github.com/MTES-MCT/ecobalyse/issues/2307)
- Restauration des origines d'outre-mer des données. [#2334](https://github.com/MTES-MCT/ecobalyse/issues/2334)
- Mise à jour et application des distances intra-pays. [#2301](https://github.com/MTES-MCT/ecobalyse/issues/2301)
- Correction de la multiplication de l'occupation des terres pour l'herbe pâturée et ajustement des coefficients SE. [#2200](https://github.com/MTES-MCT/ecobalyse/issues/2200)
- Correction de la nouvelle convention de signe pour les compléments. [#2201](https://github.com/MTES-MCT/ecobalyse/issues/2201)
- Mise à jour du mix énergétique par défaut vers celui de l'Inde. [#1702](https://github.com/MTES-MCT/ecobalyse/issues/1702)
- Renommage de la viande de porc. [#2169](https://github.com/MTES-MCT/ecobalyse/issues/2169)
