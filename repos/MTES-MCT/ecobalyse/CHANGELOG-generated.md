## Changelog : ecobalyse (30 derniers jours, au 28 mai 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'amélioration de la précision des données, notamment en ce qui concerne les distances de transport, les impacts liés à la cuisine et au recyclage, ainsi que l'ajout de nouvelles données pour des catégories de produits spécifiques comme les batteries et les aliments. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout du champ "recyclable" pour les données des produits [#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229).
- Publication de la section réglementaire pour les données alimentaires (food1) [#2312](https://github.com/MTES-MCT/ecobalyse/issues/2312).
- Amélioration de la gestion des distances de transport, notamment pour les transports internationaux et intra-pays [#2301](https://github.com/MTES-MCT/ecobalyse/issues/2301), [#2347](https://github.com/MTES-MCT/ecobalyse/issues/2347).
- Ajout de données pour les cellules de batterie dans le catalogue LCI [#2244](https://github.com/MTES-MCT/ecobalyse/issues/2244).
- Correction d'une régression concernant l'affichage des données dans les flux [#2318](https://github.com/MTES-MCT/ecobalyse/issues/2318).
- Correction du calcul des compléments textiles [#2231](https://github.com/MTES-MCT/ecobalyse/issues/2231).
- Ajout d'ingrédients HUE (Huile Essentielle) aux données [#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177).
- Ajout d'exemples pour les minibus quadricycles à assistance électrique [#2182](https://github.com/MTES-MCT/ecobalyse/issues/2182).
- Correction de la gestion de l'origine par défaut (FranceOutreMer) [#2243](https://github.com/MTES-MCT/ecobalyse/issues/2243).

### Évolutions techniques
- Amélioration de la résilience du runner de tests E2E [#2342](https://github.com/MTES-MCT/ecobalyse/issues/2342).
- Refactorisation du calcul du ratio variation de déchets [#2306](https://github.com/MTES-MCT/ecobalyse/issues/2306).
- Mise à jour de la dépendance `pytest-databases` à la version >=0.18.0 [#2321](https://github.com/MTES-MCT/ecobalyse/issues/2321).
- Mise à jour des dépendances npm et yarn [#2330](https://github.com/MTES-MCT/ecobalyse/issues/2330).
- Exclusion du dossier de données de l'image Scalingo [#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300).
- Correction de la synchronisation avec le dépôt de données [#2265](https://github.com/MTES-MCT/ecobalyse/issues/2265).
- Ajout de l'impact de la cuisson aux données [#2284](https://github.com/MTES-MCT/ecobalyse/issues/2284).
- Monorepo des données [#2272](https://github.com/MTES-MCT/ecobalyse/issues/2272).
- Correction des avertissements Dependabot [#2270](https://github.com/MTES-MCT/ecobalyse/issues/2270).

### Autres changements
- Ajout d'une ADR pour la gestion de la localisation des composants [#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900).
- Restauration des origines d'outre-mer dans les données [#2334](https://github.com/MTES-MCT/ecobalyse/issues/2334).
- Correction de problèmes liés aux cellules de batterie [#2292](https://github.com/MTES-MCT/ecobalyse/issues/2292) et [#2291](https://github.com/MTES-MCT/ecobalyse/issues/2291).
- Correction d'un bug empêchant de servir les impacts avec un token invalide [#2353](https://github.com/MTES-MCT/ecobalyse/issues/2353).
- Correction du transport des éléments [#2174](https://github.com/MTES-MCT/ecobalyse/issues/2174).
- Ajout de la date de dernière connexion pour les utilisateurs [#2181](https://github.com/MTES-MCT/ecobalyse/issues/2181).
- Renommage du porc dans les données [#2169](https://github.com/MTES-MCT/ecobalyse/issues/2169).
