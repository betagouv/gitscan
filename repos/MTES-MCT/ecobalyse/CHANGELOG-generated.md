## Changelog : ecobalyse (30 derniers jours, au 7 août 2026)

### Résumé
Cette période a été marquée par un enrichissement significatif de la base de données (alimentation, véhicules, matériaux) et une amélioration des capacités de modélisation grâce à l'introduction de catégories de produits génériques et d'opérations d'assemblage. L'expérience utilisateur a également été affinée avec de nouveaux éléments d'interface et une meilleure sécurisation des accès API.

### Évolutions fonctionnelles

**Modélisation et Données**
- Implémentation de catégories de produits génériques ([#2714](https://github.com/MTES-MCT/ecobalyse/issues/2714)) et d'opérations d'assemblage ([#2683](https://github.com/MTES-MCT/ecobalyse/issues/2683)).
- Enrichissement des exemples de données : produits alimentaires (mangues, haricots verts) ([#2712](https://github.com/MTES-MCT/ecobalyse/issues/2712), [#2711](https://github.com/MTES-MCT/ecobalyse/issues/2711)), matériaux pour véhicules électriques ([#2687](https://github.com/MTES-MCT/ecobalyse/issues/2687)) et mise à jour des exemples de véhicules ([#2629](https://github.com/MTES-MCT/ecobalyse/issues/2629)).
- Nouvelles capacités d'import/export : export au format Ecospold1 ([#2316](https://github.com/MTES-MCT/ecobalyse/issues/2316)), import BAFU depuis un export Simapro ([#2626](https://github.com/MTES-MCT/ecobalyse/issues/2626)) et inférence automatique du ratio cru/cuit ([#2663](https://github.com/MTES-MCT/ecobalyse/issues/2663)).
- Précisions sur les données : corrections des processus aluminium et acier ([#2679](https://github.com/MTES-MCT/ecobalyse/issues/2679)), gestion des ingrédients de poisson ([#2676](https://github.com/MTES-MCT/ecobalyse/issues/2676)) et ajout de tags pour le transport réfrigéré ([#2657](https://github.com/MTES-MCT/ecobalyse/issues/2657)).

**Interface et Expérience Utilisateur (UX)**
- Améliorations de l'interface : bouton d'ajout d'article de production unique ([#2664](https://github.com/MTES-MCT/ecobalyse/issues/2664)), mise en place d'étiquettes contextuelles ([#2632](https://github.com/MTES-MCT/ecobalyse/issues/2632)) et localisation des nouvelles transformations ([#2636](https://github.com/MTES-MCT/ecobalyse/issues/2636)).
- Corrections visuelles : gestion du mode sombre dans les graphiques Highcharts ([#2690](https://github.com/MTES-MCT/ecobalyse/issues/2690)) et affichage des noms de régions complets dans l'explorateur ([#2658](https://github.com/MTES-MCT/ecobalyse/issues/2658)).

**Sécurité et Accès**
- Mise à disposition de commandes API authentifiées ([#2653](https://github.com/MTES-MCT/ecobalyse/issues/2653)) et restriction de l'accès aux impacts détaillés ([#2669](https://github.com/MTES-MCT/ecobalyse/issues/2669)).

### Évolutions techniques

**Architecture et Performance**
- Fusion des dépôts de données et du front-end ([#2614](https://github.com/MTES-MCT/ecobalyse/issues/2614)).
- Optimisation de la vitesse de l'historique des scores ([#2642](https://github.com/MTES-MCT/ecobalyse/issues/2642)) et utilisation de la base de données dédiée `ecobalyse-data` ([#2580](https://github.com/MTES-MCT/ecobalyse/issues/2580)).
- Remplacement de la bibliothèque `msgspec` par `pydantic` ([#2686](https://github.com/MTES-MCT/ecobalyse/issues/2686)).

**Maintenance et CI/CD**
- Migration de la suite de tests E2E vers un job planifié ([#2633](https://github.com/MTES-MCT/ecobalyse/issues/2633)).
- Mise à jour d'Elm ([#2638](https://github.com/MTES-MCT/ecobalyse/issues/2638)) et correction des avertissements lors des tests de données ([#2671](https://github.com/MTES-MCT/ecobalyse/issues/2671)).
- Nettoyage du schéma des processus pour éviter les duplications ([#2680](https://github.com/MTES-MCT/ecobalyse/issues/2680)).

### Autres changements

**Configuration et Synchronisation**
- Correction de la synchronisation de l'export de données ([#2707](https://github.com/MTES-MCT/ecobalyse/issues/2707)).
- Amélioration de la gestion de la configuration (rechargement automatique après réception des processus détaillés [#2627](https://github.com/MTES-MCT/ecobalyse/issues/2627) et limitation des références aux processus génériques [#2660](https://github.com/MTES-MCT/ecobalyse/issues/2660)).
