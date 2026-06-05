## Changelog : ecobalyse (30 derniers jours, au 2026-06-04)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données environnementales, notamment pour les transports, l'alimentation, les batteries et l'emballage. Des améliorations ont également été apportées à la gestion des distances de transport et à la correction de bugs pour une meilleure précision et fiabilité des calculs. Enfin, des optimisations techniques et des mises à jour de dépendances ont été réalisées pour améliorer la performance et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout des données de transport routier depuis le Maroc. [#2144](https://github.com/MTES-MCT/ecobalyse/issues/2144)
- Implémentation du CFF (Coefficient de Facteur de Forme) pour les processus d'emballage alimentaire. [#2320](https://github.com/MTES-MCT/ecobalyse/issues/2320)
- Ajout de la prise en compte des batteries et de leur assemblage dans le catalogue de données. [#2362](https://github.com/MTES-MCT/ecobalyse/issues/2362)
- Ajout d'un champ "recyclable" pour les données. [#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229)
- Publication de la section réglementaire pour l'alimentation. [#2312](https://github.com/MTES-MCT/ecobalyse/issues/2312)
- Ajout d'ingrédients HUE (Huile Essentielle) dans les données. [#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177)
- Amélioration de la gestion des transports, notamment la prise en compte des distances et des transports internationaux avec refroidissement. [#2239](https://github.com/MTES-MCT/ecobalyse/issues/2239) et [#2347](https://github.com/MTES-MCT/ecobalyse/issues/2347)

### Évolutions techniques
- Mise à jour des dépendances Python et Brightway. [#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341)
- Amélioration de la résilience du runner de tests E2E. [#2342](https://github.com/MTES-MCT/ecobalyse/issues/2342)
- Refactorisation du code pour déplacer les coefficients des compléments alimentaires. [#2314](https://github.com/MTES-MCT/ecobalyse/issues/2314)
- Refactorisation pour améliorer le ratio variation de déchets. [#2306](https://github.com/MTES-MCT/ecobalyse/issues/2306)
- Correction de la précision des calculs pour éviter les différences computationnelles. [#2303](https://github.com/MTES-MCT/ecobalyse/issues/2303)
- Mise à jour des dépendances npm. [#2389](https://github.com/MTES-MCT/ecobalyse/issues/2389) et [#2330](https://github.com/MTES-MCT/ecobalyse/issues/2330)
- Ajout d'une ADR (Architecture Decision Record) pour la gestion de la localisation des composants. [#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900)
- Suppression de processus obsolètes. [#2311](https://github.com/MTES-MCT/ecobalyse/issues/2311)
- Correction de l'affichage du nom des assemblages de batteries. [#2375](https://github.com/MTES-MCT/ecobalyse/issues/2375)
- Différenciation des utilisations de PET. [#2376](https://github.com/MTES-MCT/ecobalyse/issues/2376)

### Autres changements
- Ajout de gaz au calcul pour la cuisine. [#2211](https://github.com/MTES-MCT/ecobalyse/issues/2211)
- Restauration des origines d'outre-mer dans les données. [#2334](https://github.com/MTES-MCT/ecobalyse/issues/2334)
- Exclusion du dossier "data" de l'image Scalingo. [#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300)
- Correction de la configuration CI. [#2297](https://github.com/MTES-MCT/ecobalyse/issues/2297)
- Ajout d'impacts pour la cuisine. [#2284](https://github.com/MTES-MCT/ecobalyse/issues/2284)
- Monorepo des données. [#2272](https://github.com/MTES-MCT/ecobalyse/issues/2272)
- Correction des avertissements Dependabot. [#2270](https://github.com/MTES-MCT/ecobalyse/issues/2270)
- Synchronisation avec le dépôt de données. [#2265](https://github.com/MTES-MCT/ecobalyse/issues/2265)
- Correction d'un bug empêchant l'affichage des impacts avec un token invalide. [#2353](https://github.com/MTES-MCT/ecobalyse/issues/2353)
- Suppression du transport aérien entre les étapes de transformation. [#2398](https://github.com/MTES-MCT/ecobalyse/issues/2398)
