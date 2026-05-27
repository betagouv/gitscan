## Changelog : ecobalyse (30 derniers jours, au 26 mai 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'amélioration des données, notamment l'ajout d'ingrédients, de processus et de détails sur les batteries. Des corrections de bugs et des optimisations ont été apportées pour améliorer la performance et la fiabilité de l'application, en particulier au niveau de l'explorateur et des calculs d'impacts. Des améliorations techniques ont également été réalisées pour faciliter le déploiement et la maintenance.

### Évolutions fonctionnelles
- Ajout de la publication de la section réglementaire pour l'alimentation. [#2312](https://github.com/MTES-MCT/ecobalyse/issues/2312)
- Ajout du champ "recyclable" pour les données. [#2229](https://github.com/MTES-MCT/ecobalyse/issues/2229)
- Amélioration de la gestion des distances de transport, incluant la prise en compte des distances intra-pays et des hubs. [#2301](https://github.com/MTES-MCT/ecobalyse/issues/2301)
- Ajout d'ingrédients HUE (Huile Essentielle). [#2177](https://github.com/MTES-MCT/ecobalyse/issues/2177)
- Ajout d'ingrédients UE. [#2075](https://github.com/MTES-MCT/ecobalyse/issues/2075)
- Ajout d'exemples de "Minibus quadricycle à assistance électrique" pour les données VELI. [#2182](https://github.com/MTES-MCT/ecobalyse/issues/2182)
- Ajout de données pour les cellules de batterie dans le catalogue LCI. [#2244](https://github.com/MTES-MCT/ecobalyse/issues/2244)
- Ajout de métadonnées génériques pour l'alimentation. [#2089](https://github.com/MTES-MCT/ecobalyse/issues/2089)

### Évolutions techniques
- Refactorisation du calcul du ratio variation de déchets. [#2306](https://github.com/MTES-MCT/ecobalyse/issues/2306)
- Amélioration de la résilience de l'exécuteur de tests E2E. [#2342](https://github.com/MTES-MCT/ecobalyse/issues/2342)
- Mise à jour de la dépendance `pytest-databases[postgres]` vers la version >=0.18.0. [#2321](https://github.com/MTES-MCT/ecobalyse/issues/2321)
- Mise à jour des dépendances npm/yarn. [#2330](https://github.com/MTES-MCT/ecobalyse/issues/2330)
- Exclure le dossier `data` de l'image Scalingo pour optimiser la taille. [#2300](https://github.com/MTES-MCT/ecobalyse/issues/2300)
- Correction de la synchronisation avec le dépôt de données. [#2265](https://github.com/MTES-MCT/ecobalyse/issues/2265)
- Mise à jour des dépendances npm dans le projet courant. [#2276](https://github.com/MTES-MCT/ecobalyse/issues/2276)
- Correction des avertissements Dependabot. [#2270](https://github.com/MTES-MCT/ecobalyse/issues/2270)
- Ajout de processus génériques pour la cuisine aux données. [#2284](https://github.com/MTES-MCT/ecobalyse/issues/2284)
- Monorepo pour les données. [#2272](https://github.com/MTES-MCT/ecobalyse/issues/2272)

### Autres changements
- Ajout d'une ADR pour la gestion de l'emplacement des composants. [#1900](https://github.com/MTES-MCT/ecobalyse/issues/1900)
- Restauration des origines d'outre-mer dans les données. [#2334](https://github.com/MTES-MCT/ecobalyse/issues/2334)
- Correction d'un bug de régression dans le flux d'alimentation. [#2318](https://github.com/MTES-MCT/ecobalyse/issues/2318)
- Correction d'un problème de recyclage des piles. [#2292](https://github.com/MTES-MCT/ecobalyse/issues/2292)
- Correction des processus liés aux piles. [#2291](https://github.com/MTES-MCT/ecobalyse/issues/2291)
- Correction de l'application des ratios de transport aux distances par défaut. [#2307](https://github.com/MTES-MCT/ecobalyse/issues/2307)
- Suppression de la cuisson. [#2313](https://github.com/MTES-MCT/ecobalyse/issues/2313)
- Correction de l'application de la nouvelle convention de signe pour les compléments. [#2201](https://github.com/MTES-MCT/ecobalyse/issues/2201)
- Correction des problèmes de performance de l'explorateur. [#2154](https://github.com/MTES-MCT/ecobalyse/issues/2154)
- Suppression de la densité de bétail. [#2124](https://github.com/MTES-MCT/ecobalyse/issues/2124)
- Correction de la multiplication de l'occupation des terres pour l'herbe pâturée et ajustement des coefficients SE. [#2200](https://github.com/MTES-MCT/ecobalyse/issues/2200)
- Ajout de l'utilisateur `last_login_at`. [#2181](https://github.com/MTES-MCT/ecobalyse/issues/2181)
- Correction des compléments textiles. [#2231](https://github.com/MTES-MCT/ecobalyse/issues/2231)
