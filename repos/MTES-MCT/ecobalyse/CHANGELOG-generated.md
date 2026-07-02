## Changelog : ecobalyse (30 derniers jours, au 01 juillet 2026)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'enrichissement des données avec de nouveaux éléments (aliments, véhicules, matériaux d'emballage) et l'amélioration de la précision des calculs, notamment en intégrant des données plus récentes (EF 3.1 adapté 1.03). Des corrections et des refactorings ont également été apportés pour améliorer la stabilité et la cohérence de l'application.

### Évolutions fonctionnelles
- Ajout de multiples exemples d'aliments dans l'interface pour faciliter l'utilisation. [#2563](https://github.com/MTES-MCT/ecobalyse/issues/2563)
- Ajout d'un exemple de "Pizza bolognese Bio (350g)". [#2553](https://github.com/MTES-MCT/ecobalyse/issues/2553)
- Amélioration de la gestion des processus génériques avec la prise en compte de la masse du produit. [#2560](https://github.com/MTES-MCT/ecobalyse/issues/2560)
- Ajout de la possibilité de définir l'origine par défaut des processus génériques. [#2414](https://github.com/MTES-MCT/ecobalyse/issues/2414)
- Ajout de composants pour les véhicules (batteries, câbles, pneus). [#2459](https://github.com/MTES-MCT/ecobalyse/issues/2459), [#2366](https://github.com/MTES-MCT/ecobalyse/issues/2366)
- Ajout de matériaux d'emballage pour objets et véhicules. [#2555](https://github.com/MTES-MCT/ecobalyse/issues/2555)
- Ajout de données pour les transports routiers depuis le Maroc. [#2144](https://github.com/MTES-MCT/ecobalyse/issues/2144)
- Mise à jour des données EF3.1 avec la version adaptée 1.03. [#2395](https://github.com/MTES-MCT/ecobalyse/issues/2395)

### Évolutions techniques
- Refactorisation du chargement des données en utilisant HTTP. [#2416](https://github.com/MTES-MCT/ecobalyse/issues/2416)
- Synchronisation de la base de données avec les modèles via une migration. [#2536](https://github.com/MTES-MCT/ecobalyse/issues/2536)
- Mise à jour des dépendances npm et yarn. [#2499](https://github.com/MTES-MCT/ecobalyse/issues/2499), [#2486](https://github.com/MTES-MCT/ecobalyse/issues/2486), [#2341](https://github.com/MTES-MCT/ecobalyse/issues/2341)
- Mise à jour des dépendances Python. [#2399](https://github.com/MTES-MCT/ecobalyse/issues/2399)
- Amélioration de la fiabilité des tests E2E. [#2422](https://github.com/MTES-MCT/ecobalyse/issues/2422)
- Modification de la logique pour gérer les transports aériens dans les calculs. [#2377](https://github.com/MTES-MCT/ecobalyse/issues/2377)

### Autres changements
- Corrections et ajustements de données pour divers produits (orange, tomate, café, betterave sucrière, graines de tournesol, etc.). [#2514](https://github.com/MTES-MCT/ecobalyse/issues/2514), [#2505](https://github.com/MTES-MCT/ecobalyse/issues/2505), [#2503](https://github.com/MTES-MCT/ecobalyse/issues/2503), [#2484](https://github.com/MTES-MCT/ecobalyse/issues/2484), [#2476](https://github.com/MTES-MCT/ecobalyse/issues/2476), [#2474](https://github.com/MTES-MCT/ecobalyse/issues/2474)
- Modification de l'unité d'électricité de "elecMJ" à "elecKwh". [#2561](https://github.com/MTES-MCT/ecobalyse/issues/2561)
- Ajout d'une région "Maghreb". [#2568](https://github.com/MTES-MCT/ecobalyse/issues/2568)
- Amélioration de l'affichage de l'application (ajout de "Alimentaire BÉTA"). [#2538](https://github.com/MTES-MCT/ecobalyse/issues/2538)
- Correction de la syntaxe des modèles d'issues. [#2544](https://github.com/MTES-MCT/ecobalyse/issues/2544)
- Suppression de processus obsolètes dans les données VELI. [#2472](https://github.com/MTES-MCT/ecobalyse/issues/2472)
- Amélioration de la terminologie pour les données alimentaires. [#2523](https://github.com/MTES-MCT/ecobalyse/issues/2523)
