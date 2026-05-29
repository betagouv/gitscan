## Changelog : ecobalyse (30 derniers jours, au 28 mai 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'amélioration de la précision des données, notamment en matière de distances de transport, de gestion des origines géographiques et de données spécifiques à certains secteurs comme l'alimentation et les batteries. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de l'infrastructure et de la gestion des données.

### Évolutions fonctionnelles
- **Alimentation :** Publication de la section réglementaire pour les produits alimentaires. [#2312](https://github.com/MTES-MCT/ecobalyse/issues/2312)
- **Recyclage :** Ajout d'informations sur le recyclage des batteries et des cellules de batterie dans le catalogue LCI. [#2244](https://github.com/MTES-MCT/ecobalyse/issues/2244)
- **Utilisateur :** Ajout du champ `recyclable` pour les éléments. [#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229)
- **Explorer :** Amélioration de l'affichage des impacts dans l'explorateur d'objets et de VELI.
- **Données :** Ajout d'ingrédients HUE et UE dans les données. [#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177), [#2075](https://github.com/MTES-MCT/ecobalyse/issues/2075)
- **Données :** Ajout d'exemples de "Minibus quadricycle à assistance électrique". [#2182](https://github.com/MTES-MCT/ecobalyse/issues/2182)

### Évolutions techniques
- **Distances :** Mise à jour et application des distances intra-pays. [#2301](https://github.com/MTES-MCT/ecobalyse/issues/2301)
- **Transport :** Gestion des distances vers le hub et des transports globaux avec refroidissement. [#2259](https://github.com/MTES-MCT/ecobalyse/issues/2259), [#2239](https://github.com/MTES-MCT/ecobalyse/issues/2239)
- **Calcul :** Refactorisation du rapport variation de déchets. [#2306](https://github.com/MTES-MCT/ecobalyse/issues/2306)
- **CI/CD :** Amélioration de la résilience du runner de tests E2E. [#2342](https://github.com/MTES-MCT/ecobalyse/issues/2342)
- **Infrastructure :** Exclusion du dossier `data` de l'image Scalingo. [#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300)
- **Synchronisation des données :** Ajout de `processes_generic` à la synchronisation des données ecobalyse_data. [#2258](https://github.com/MTES-MCT/ecobalyse/issues/2258)
- **Architecture :** Réassignation des transformations compatibles lors de la mise à jour des matériaux. [#2230](https://github.com/MTES-MCT/ecobalyse/issues/2230)

### Autres changements
- **Documentation :** Ajout d'un ADR pour la gestion de la localisation des composants. [#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900)
- **Données :** Restauration des origines d'outre-mer dans les données. [#2334](https://github.com/MTES-MCT/ecobalyse/issues/2334)
- **Corrections :** Correction de bugs liés à la régression du feed, aux transports, aux compléments textiles, et aux problèmes de performance de l'explorateur. [#2318](https://github.com/MTES-MCT/ecobalyse/issues/2318), [#2313](https://github.com/MTES-MCT/ecobalyse/issues/2313), [#2292](https://github.com/MTES-MCT/ecobalyse/issues/2292), [#2291](https://github.com/MTES-MCT/ecobalyse/issues/2291), [#2154](https://github.com/MTES-MCT/ecobalyse/issues/2154)
- **Sécurité :** Correction d'un problème de service des impacts avec un token invalide. [#2353](https://github.com/MTES-MCT/ecobalyse/issues/2353)
- **Divers :** Diverses corrections de données, mises à jour de dépendances et améliorations de la configuration.
