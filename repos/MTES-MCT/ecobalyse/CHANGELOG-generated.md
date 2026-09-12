## Changelog : ecobalyse (30 derniers jours, au 10 septembre 2026)

### Résumé
Ce mois a été marqué par une restructuration importante de la gestion des données, notamment via l'introduction d'une nouvelle taxonomie permettant une classification plus automatique des matériaux. Les capacités de simulation ont été enrichies par de nouveaux exemples et une meilleure gestion des catégories de produits, tandis que l'interface utilisateur a été affinée pour offrir une expérience plus fluide et précise.

### Évolutions fonctionnelles
- **Gestion des produits et matériaux** : Automatisation de la déduction des types de matériaux via la taxonomie ([#2779](https://github.com/MTES-MCT/ecobalyse/issues/2779)), gestion des opérations d'assemblage et des consommations par défaut selon la catégorie de produit ([#2753](https://github.com/MTES-MCT/ecobalyse/issues/2753), [#2744](https://github.com/MTES-MCT/ecobalyse/issues/2744)) et correction des anomalies de hiérarchie ([#2652](https://github.com/MTES-MCT/ecobalyse/issues/2652)).
- **Enrichissement des données** : Création de nouvelles catégories de véhicules et mise à jour des exemples associés ([#2724](https://github.com/MTES-MCT/ecobalyse/issues/2724), [#2725](https://github.com/MTES-MCT/ecobalyse/issues/2725)) et introduction d'un nouveau système de taxonomie pour remplacer l'ancien fichier d'ingrédients ([#2746](https://github.com/MTES-MCT/ecobalyse/issues/2746)).
- **Optimisation de l'interface (UI)** : Affichage de la masse unitaire des articles de production ([#2766](https://github.com/MTES-MCT/ecobalyse/issues/2766)), rendu des éléments partagés dans les lignes de composants ([#2772](https://github.com/MTES-MCT/ecobalyse/issues/2772)) et masquage des sélecteurs lors de requêtes vides ([#2750](https://github.com/MTES-MCT/ecobalyse/issues/2750)).
- **Simulation** : Chargement automatique d'exemples par défaut pour le simulateur générique ([#2782](https://github.com/MTES-MCT/ecobalyse/issues/2782)).

### Évolutions techniques
- **Performance et base de données** : Optimisation des insertions via l'utilisation de batchs ([#2790](https://github.com/MTES-MCT/ecobalyse/issues/2790)) et correction de la sérialisation JSONB ([#2713](https://github.com/MTES-MCT/ecobalyse/issues/2713)).
- **Architecture et code** : Renforcement de la généricité du code ([#2721](https://github.com/MTES-MCT/ecobalyse/issues/2721)), partage des stratégies SimaPro ([#2745](https://github.com/MTES-MCT/ecobalyse/issues/2745)) et adoption du typechecker `ty` ([#2728](https://github.com/MTES-MCT/ecobalyse/issues/2728), [#2731](https://github.com/MTES-MCT/ecobalyse/issues/2731)).
- **Infrastructure et sécurité** : Mise à jour de la compatibilité avec Scalingo ([#2801](https://github.com/MTES-MCT/ecobalyse/issues/2801), [#2776](https://github.com/MTES-MCT/ecobalyse/issues/2776)), montée de version de Maildev pour la sécurité ([#2771](https://github.com/MTES-MCT/ecobalyse/issues/2771)) et correction des tests E2E ([#2741](https://github.com/MTES-MCT/ecobalyse/issues/2741)).

### Autres changements
- **Nettoyage des données** : Suppression de données obsolètes ou inutiles, comme certains ratios de cuisson ou des activités de lait de vache vides ([#2759](https://github.com/MTES-MCT/ecobalyse/issues/2759), [#2743](https://github.com/MTES-MCT/ecobalyse/issues/2743)).
- **Qualité logicielle** : Correction d'erreurs via Ruff ([#2706](https://github.com/MTES-MCT/ecobalyse/issues/2706)) et ajustement du formatage JSON ([#2754](https://github.com/MTES-MCT/ecobalyse/issues/2754)).
