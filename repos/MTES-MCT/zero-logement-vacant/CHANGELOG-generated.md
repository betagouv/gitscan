## Changelog : zero-logement-vacant (30 derniers jours, au 2026-05-19)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration des performances, la simplification de l'architecture et la préparation de nouvelles fonctionnalités pour l'import des données LOVAC 2026. Des corrections ont également été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment au niveau de la gestion des campagnes et de la cartographie.

### Évolutions fonctionnelles
- **Cartographie :** Amélioration de l'expérience utilisateur de la légende de la carte, avec un affichage plus clair et un style visuel amélioré [#1698](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1698).
- **Campagnes :** Possibilité de naviguer vers la liste des logements filtrée par campagne [#1762](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1762).
- **Export de données :** Différenciation de l'export des groupes et des campagnes, avec ajout de la colonne "ville propriétaire" pour l'export des groupes [#1761](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1761).
- **Statut des logements :** Correction de la gestion du statut des logements "jamais contacté" pour assurer une cohérence des données.

### Évolutions techniques
- **Architecture :** Suppression du préfixe `/api` des appels API, simplifiant ainsi l'architecture et les appels réseau [#1806](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1806).
- **Performances :** Optimisation significative du temps de calcul du nombre de logements, réduisant les temps de réponse pour les filtres [#1793](https://github.com/MTES-MCT/zero-logement-vacant/pulls/1793).
- **dbt :** Ajout de l'identifiant UUID des propriétaires (owner_uid) aux tables `owners` et `owner_housing` pour une meilleure gestion des données.
- **Tests :** Amélioration de la couverture et de la fiabilité des tests, notamment pour les tests d'intégration et les tests E2E.
- **Dépendances :** Mise à jour des dépendances npm et yarn.
- **CI/CD :** Correction de problèmes liés à la compilation des tests Dagster et à la configuration des variables d'environnement.
- **Suppression de code obsolète :** Suppression de code et de fonctionnalités obsolètes, notamment liées à l'ancien système de campagne.
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité, la maintenabilité et la performance.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements apportés à l'architecture et aux fonctionnalités.
- **Configuration :** Mise à jour de la configuration du projet pour améliorer la sécurité et la performance.
- **Analytics :** Ajout d'analytics pour suivre l'utilisation des nouvelles fonctionnalités et identifier les points d'amélioration.
- **Claude :** Intégration de Claude pour l'automatisation de certaines tâches et l'amélioration de la qualité du code.
- **Skills :** Ajout de nouvelles skills pour les agents Claude.
