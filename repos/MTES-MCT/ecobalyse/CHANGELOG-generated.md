## Changelog : ecobalyse (30 derniers jours, au 18 août 2026)

### Résumé
Ce mois-ci, le projet s'est concentré sur l'enrichissement de sa base de données avec de nouveaux exemples de produits (véhicules, alimentation, produits génériques) et l'amélioration de l'expérience utilisateur via des ajustements d'interface et de sécurité. Des optimisations techniques ont également été réalisées pour améliorer la rapidité du système et la robustesse du code.

### Évolutions fonctionnelles
- **Enrichissement des données de modélisation** :
    - Ajout de nouvelles catégories, matériaux et exemples pour les véhicules ([#2725](https://github.com/MTES-MCT/ecobalyse/issues/2725), [#2724](https://github.com/MTES-MCT/ecobalyse/issues/2724), [#2689](https://github.com/MTES-MCT/ecobalyse/issues/2689), [#2687](https://github.com/MTES-MCT/ecobalyse/issues/2687)).
    - Ajout d'exemples alimentaires (haricots verts, mangues) et ajustement des ingrédients pour le poisson ([#2712](https://github.com/MTES-MCT/ecobalyse/issues/2712), [#2711](https://github.com/MTES-MCT/ecobalyse/issues/2711), [#2676](https://github.com/MTES-MCT/ecobalyse/issues/2676)).
    - Implémentation de catégories de produits génériques ([#2714](https://github.com/MTES-MCT/ecobalyse/issues/2714)) et d'opérations d'assemblage ([#2683](https://github.com/MTES-MCT/ecobalyse/issues/2683)).
    - Correction des processus de fabrication pour l'aluminium et l'acier ([#2679](https://github.com/MTES-MCT/ecobalyse/issues/2679)).
- **Interface utilisateur et expérience (UI/UX)** :
    - Amélioration de l'affichage des graphiques Highcharts en mode sombre ([#2690](https://github.com/MTES-MCT/ecobalyse/issues/2690)).
    - Ajout d'un bouton pour l'ajout d'un article de production unique ([#2664](https://github.com/MTES-MCT/ecobalyse/issues/2664)).
- **Sécurité** :
    - Restriction de l'accès aux impacts détaillés ([#2669](https://github.com/MTES-MCT/ecobalyse/issues/2669)).

### Évolutions techniques
- **Performances et architecture** :
    - Accélération de la récupération de l'historique des scores ([#2642](https://github.com/MTES-MCT/ecobalyse/issues/2642)).
    - Migration de l'historique des scores vers la base de données `ecobalyse-data` ([#2580](https://github.com/MTES-MCT/ecobalyse/issues/2580)).
    - Correction de la sérialisation JSON pour les types JSONB ([#2713](https://github.com/MTES-MCT/ecobalyse/issues/2713)) et de la synchronisation de l'export de données ([#2707](https://github.com/MTES-MCT/ecobalyse/issues/2707)).
- **Qualité du code et outils** :
    - Refactoring de la gestion des données : remplacement de `msgspec` par `pydantic` ([#2686](https://github.com/MTES-MCT/ecobalyse/issues/2686)) et suppression de la duplication des schémas de processus ([#2680](https://github.com/MTES-MCT/ecobalyse/issues/2680)).
    - Amélioration de la vérification statique et du linting (adoption de `ty` [#2728](https://github.com/MTES-MCT/ecobalyse/issues/2728), corrections `ruff` [#2706](https://github.com/MTES-MCT/ecobalyse/issues/2706)).
    - Correction des avertissements dans les tests de données ([#2671](https://github.com/MTES-MCT/ecobalyse/issues/2671)).
