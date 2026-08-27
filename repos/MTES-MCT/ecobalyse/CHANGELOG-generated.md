## Changelog : ecobalyse (30 derniers jours, au 26 août 2026)

### Résumé
Cette période a été marquée par un enrichissement important des bases de données, notamment pour les catégories de véhicules et de produits alimentaires. L'application gagne également en flexibilité grâce à l'introduction de nouvelles fonctionnalités génériques permettant de mieux gérer les assemblages et les catégories de produits.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Mise en place des opérations d'assemblage ([#2683](https://github.com/MTES-MCT/ecobalyse/issues/2683)).
    - Introduction de catégories de produits génériques ([#2714](https://github.com/MTES-MCT/ecobalyse/issues/2714)) et de leurs consommations par défaut ([#2744](https://github.com/MTES-MCT/ecobalyse/issues/2744)).
- **Enrichissement des données** :
    - Ajout de nouvelles catégories, matériaux et processus pour les véhicules ([#2689](https://github.com/MTES-MCT/ecobalyse/issues/2689), [#2724](https://github.com/MTES-MCT/ecobalyse/issues/2724), [#2725](https://github.com/MTES-MCT/ecobalyse/issues/2725), [#2687](https://github.com/MTES-MCT/ecobalyse/issues/2687)).
    - Ajout d'exemples alimentaires (mangues, haricots verts) ([#2711](https://github.com/MTES-MCT/ecobalyse/issues/2711), [#2712](https://github.com/MTES-MCT/ecobalyse/issues/2712)).
- **Interface utilisateur** :
    - Correction de l'affichage : masquage des onglets et du sélecteur de catégorie lors de requêtes vides ([#2750](https://github.com/MTES-MCT/ecobalyse/issues/2750)).

### Évolutions techniques
- **Refactorisation et architecture** :
    - Amélioration de la généricité du code et du partage des stratégies SimaPro ([#2745](https://github.com/MTES-MCT/ecobalyse/issues/2745), [#2721](https://github.com/MTES-MCT/ecobalyse/issues/2721)).
    - Optimisation du schéma des processus pour éviter les duplications ([#2680](https://github.com/MTES-MCT/ecobalyse/issues/2680)).
    - Migration de `msgspec` vers `pydantic` ([#2686](https://github.com/MTES-MCT/ecobalyse/issues/2686)).
- **Backend et données** :
    - Correction de la sérialisation JSON pour les types `jsonb` ([#2713](https://github.com/MTES-MCT/ecobalyse/issues/2713)).
    - Résolution de problèmes de synchronisation lors de l'export de données ([#2707](https://github.com/MTES-MCT/ecobalyse/issues/2707)).
- **Stabilité et maintenance** :
    - Correction des tests de bout en bout (E2E) ([#2741](https://github.com/MTES-MCT/ecobalyse/issues/2741)).
    - Retour à une version stable de Highcharts ([#2739](https://github.com/MTES-MCT/ecobalyse/issues/2739)).
    - Ajustement des délais d'affichage pour améliorer la fiabilité de l'interface ([#2748](https://github.com/MTES-MCT/ecobalyse/issues/2748)).

### Autres changements
- **Qualité du code** : Intégration du typechecker `ty` ([#2728](https://github.com/MTES-MCT/ecobalyse/issues/2728), [#2731](https://github.com/MTES-MCT/ecobalyse/issues/2731)) et correction d'erreurs de linting Ruff ([#2706](https://github.com/MTES-MCT/ecobalyse/issues/2706)).
- **Nettoyage** : Suppression d'activités de données obsolètes ou vides ([#2743](https://github.com/MTES-MCT/ecobalyse/issues/2743)).
