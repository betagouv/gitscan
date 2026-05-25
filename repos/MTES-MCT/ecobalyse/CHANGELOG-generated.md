## Changelog : ecobalyse (30 derniers jours, au 22 mai 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'amélioration de la gestion des données, notamment l'ajout de nouvelles données pour les batteries, les ingrédients alimentaires et les textiles. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la précision des calculs et la performance de l'application. Enfin, des améliorations ont été apportées à l'infrastructure et au processus de CI/CD.

### Évolutions fonctionnelles
- Ajout du champ "recyclable" pour les matériaux [#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229).
- Intégration de données pour les cellules de batteries dans le catalogue LCI [#2244](https://github.com/MTES-MCT/ecobalyse/issues/2244).
- Ajout d'ingrédients HUE (Human Use Ecology) [#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177).
- Ajout d'ingrédients UE (Union Européenne) [#2075](https://github.com/MTES-MCT/ecobalyse/issues/2075).
- Prise en compte de la distance jusqu'au hub pour les calculs génériques [#2259](https://github.com/MTES-MCT/ecobalyse/issues/2259).
- Prise en compte du refroidissement global pour les transports [#2239](https://github.com/MTES-MCT/ecobalyse/issues/2239).
- Ajout de la possibilité de voir la dernière connexion de l'utilisateur [#2181](https://github.com/MTES-MCT/ecobalyse/issues/2181).
- Ajout de données CMAP transformées pour les ingrédients [#2096](https://github.com/MTES-MCT/ecobalyse/issues/2096).
- Amélioration du calcul des compléments textiles [#2231](https://github.com/MTES-MCT/ecobalyse/issues/2231).
- Correction d'une régression concernant le flux d'actualités [#2318](https://github.com/MTES-MCT/ecobalyse/issues/2318).

### Évolutions techniques
- Exclusion du dossier "data" de l'image Scalingo pour réduire sa taille [#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300).
- Correction de la configuration CI [#2297](https://github.com/MTES-MCT/ecobalyse/issues/2297).
- Synchronisation des données avec le dépôt ecobalyse-data pour les processus génériques [#2258](https://github.com/MTES-MCT/ecobalyse/issues/2258).
- Refactorisation pour utiliser "stage" au lieu de "step" dans le code [#1738](https://github.com/MTES-MCT/ecobalyse/issues/1738).
- Mise à jour des dépendances npm [#2276](https://github.com/MTES-MCT/ecobalyse/issues/2276).
- Correction des avertissements Dependabot [#2270](https://github.com/MTES-MCT/ecobalyse/issues/2270).
- Synchronisation avec le dépôt de données [#2265](https://github.com/MTES-MCT/ecobalyse/issues/2265).

### Autres changements
- Correction de problèmes liés aux processus de batterie [#2291](https://github.com/MTES-MCT/ecobalyse/issues/2291) et [#2292](https://github.com/MTES-MCT/ecobalyse/issues/2292).
- Ajout d'impacts pour la cuisson [#2284](https://github.com/MTES-MCT/ecobalyse/issues/2284).
- Monorepo pour les données [#2272](https://github.com/MTES-MCT/ecobalyse/issues/2272).
- Renommage de la viande de porc [#2169](https://github.com/MTES-MCT/ecobalyse/issues/2169).
- Suppression de matériaux obsolètes [#2151](https://github.com/MTES-MCT/ecobalyse/issues/2151).
- Correction de problèmes de performance de l'explorateur [#2154](https://github.com/MTES-MCT/ecobalyse/issues/2154).
- Correction de la multiplication de l'occupation des terres pour l'herbe broussée et ajustement des coefficients SE [#2200](https://github.com/MTES-MCT/ecobalyse/issues/2200).
- Correction de la nouvelle convention de signe pour les compléments [#2201](https://github.com/MTES-MCT/ecobalyse/issues/2201).
- Suppression d'une transformation métal obsolète [#2195](https://github.com/MTES-MCT/ecobalyse/issues/2195).
