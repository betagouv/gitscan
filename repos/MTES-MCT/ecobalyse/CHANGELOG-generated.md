## Changelog : ecobalyse (30 derniers jours, au 29 juin 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données, notamment pour les secteurs de l'alimentation, des véhicules et de l'emballage. Des améliorations ont été apportées à la gestion des processus génériques, avec une meilleure prise en compte des transports et des masses. L'interface utilisateur a également été optimisée, notamment pour l'affichage des détails et l'exploration des données.

### Évolutions fonctionnelles
- Ajout de la possibilité de filtrer les processus invisibles dans le calculateur générique. [#2537](https://github.com/MTES-MCT/ecobalyse/issues/2537)
- Amélioration de l'affichage des détails de l'explorateur avec un état conservé. [#2554](https://github.com/MTES-MCT/ecobalyse/issues/2554)
- Ajout de plusieurs éléments alimentaires aux exemples de données. [#2563](https://github.com/MTES-MCT/ecobalyse/issues/2563)
- Ajout d'un exemple de "Pizza bolognese Bio (350g)". [#2553](https://github.com/MTES-MCT/ecobalyse/issues/2553)
- Ajout de matériaux d'emballage pour les objets et les véhicules. [#2555](https://github.com/MTES-MCT/ecobalyse/issues/2555)
- Mise à jour des exemples de véhicules. [#2457](https://github.com/MTES-MCT/ecobalyse/issues/2457)
- Prise en charge des processus dépendants de la masse du produit dans le générique. [#2560](https://github.com/MTES-MCT/ecobalyse/issues/2560)
- L'étape d'assemblage est maintenant obligatoire dans le générique. [#2551](https://github.com/MTES-MCT/ecobalyse/issues/2551)
- Ajout de la prise en charge du transport aérien dans le générique. [#2377](https://github.com/MTES-MCT/ecobalyse/issues/2377)
- Ajout de batteries (NMC622, AA, AAA) et de processus d'assemblage. [#2362](https://github.com/MTES-MCT/ecobalyse/issues/2362), [#2375](https://github.com/MTES-MCT/ecobalyse/issues/2375)
- Ajout de verre feuilleté. [#2403](https://github.com/MTES-MCT/ecobalyse/issues/2403)
- Ajout de transport routier depuis le Maroc. [#2144](https://github.com/MTES-MCT/ecobalyse/issues/2144)
- Ajout de bois et de papier pour l'emballage et ouverture vers l'emballage d'objets. [#2404](https://github.com/MTES-MCT/ecobalyse/issues/2404)
- Ajout de CFF dans les processus d'emballage alimentaire. [#2320](https://github.com/MTES-MCT/ecobalyse/issues/2320)
- Ajout de processus pour les pneus. [#2415](https://github.com/MTES-MCT/ecobalyse/issues/2415)

### Évolutions techniques
- Refactorisation du chargement des données via HTTP. [#2416](https://github.com/MTES-MCT/ecobalyse/issues/2416)
- Synchronisation de la base de données et des modèles via une migration. [#2536](https://github.com/MTES-MCT/ecobalyse/issues/2536)
- Mise à jour des dépendances npm et node. [#2486](https://github.com/MTES-MCT/ecobalyse/issues/2486), [#2531](https://github.com/MTES-MCT/ecobalyse/issues/2531)
- Mise à jour des dépendances Python. [#2399](https://github.com/MTES-MCT/ecobalyse/issues/2399)
- Refactorisation des fichiers de processus dans le pipeline de données. [#2437](https://github.com/MTES-MCT/ecobalyse/issues/2437)
- Amélioration de la fiabilité des tests E2E. [#2422](https://github.com/MTES-MCT/ecobalyse/issues/2422)
- Suppression de processus obsolètes. [#2311](https://github.com/MTES-MCT/ecobalyse/issues/2311), [#2472](https://github.com/MTES-MCT/ecobalyse/issues/2472)
- Correction de la syntaxe du modèle d'issue. [#2544](https://github.com/MTES-MCT/ecobalyse/issues/2544)
- Utilisation de JSON pour stocker les composants. [#2393](https://github.com/MTES-MCT/ecobalyse/issues/2393)

### Autres changements
- Correction du tri des exemples génériques. [#2565](https://github.com/MTES-MCT/ecobalyse/issues/2565)
- Localisation de l'étape d'assemblage des exemples food2 en France. [#2567](https://github.com/MTES-MCT/ecobalyse/issues/2567)
- Mise à jour de la documentation et des exemples pour veli. [#2457](https://github.com/MTES-MCT/ecobalyse/issues/2457)
- Suppression de sunflower-oil-eu. [#2474](https://github.com/MTES-MCT/ecobalyse/issues/2474)
- Modification du libellé pour food1. [#2523](https://github.com/MTES-MCT/ecobalyse/issues/2523)
- Déplacement de brocoli vers brocoli-eu. [#2476](https://github.com/MTES-MCT/ecobalyse/issues/2476)
- Mise à jour des paramètres de dependabot. [#2532](https://github.com/MTES-MCT/ecobalyse/issues/2532)
- Ajout d'un affichage "Alimentaire BÉTA". [#2538](https://github.com/MTES-MCT/ecobalyse/issues/2538)
- Correction d'un bug lié à l'impact non-tissé polyester. [#2421](https://github.com/MTES-MCT/ecobalyse/issues/2421)
- Modification du type de matériau des fibres PET recyclées. [#2365](https://github.com/MTES-MCT/ecobalyse/issues/2365)
- Correction du facteur de complément forestier. [#2391](https://github.com/MTES-MCT/ecobalyse/issues/2391)
- Amélioration de la précision des calculs. [#2303](https://github.com/MTES-MCT/ecobalyse/issues/2303)
