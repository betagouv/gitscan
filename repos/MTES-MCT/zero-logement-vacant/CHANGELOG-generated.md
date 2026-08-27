## Changelog : zero-logement-vacant (30 derniers jours, au 24 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape majeure avec la refonte complète de son système de gestion de base de données pour gagner en fiabilité. Les utilisateurs bénéficient de nouvelles fonctionnalités de gestion des propriétaires (option "ne pas contacter"), d'une cartographie améliorée et d'une mise en conformité accrue avec les normes d'accessibilité (RGAA). La stabilité globale de l'interface et des analyses a également été renforcée.

### Évolutions fonctionnelles
- **Gestion des propriétaires** : Introduction d'un statut "ne pas contacter" au niveau du propriétaire, permettant d'exclure automatiquement ces derniers des exports de données. [#1836](https://github.com/MTES-MCT/zero-logement-vacant/issues/1836)
- **Pilotage des campagnes** : Automatisation du changement de statut des logements en fonction des dates d'envoi prévues et gestion des reports de dates. [#1915](https://github.com/MTES-MCT/zero-logement-vacant/issues/1915)
- **Cartographie** : Amélioration de la visualisation avec une nouvelle projection et un affichage optimisé des points de logements. [#1937](https://github.com/MTES-MCT/zero-logement-vacant/issues/1937)
- **Accessibilité (RGAA)** : Améliorations de l'accessibilité pour les formulaires, la validation des erreurs et les éléments de navigation. [#1927](https://github.com/MTES-MCT/zero-logement-vacant/issues/1927), [#1928](https://github.com/MTES-MCT/zero-logement-vacant/issues/1928), [#1926](https://github.com/MTES-MCT/zero-logement-vacant/issues/1926)
- **Interface utilisateur** : 
    - Correction de la pagination dans les tableaux d'analyse. [#1936](https://github.com/MTES-MCT/zero-logement-vacant/issues/1936)
    - Stabilisation du chargement du tableau de bord d'analyse. [#1945](https://github.com/MTES-MCT/zero-logement-vacant/issues/1945)
    - Ajustement des libellés de filtres pour plus de clarté. [#1964](https://github.com/MTES-MCT/zero-logement-vacant/issues/1964)
    - Correction des filtres d'intercommunalité. [#1943](https://github.com/MTES-MCT/zero-logement-vacant/issues/1943)
- **Campagnes** : Possibilité de laisser les descriptions de campagne vides lors d'une mise à jour. [#1959](https://github.com/MTES-MCT/zero-logement-vacant/issues/1959)

### Évolutions techniques
- **Base de données** : Migration massive de l'outil de requête de Knex vers Kysely pour l'ensemble des dépôts, améliorant la sécurité du typage et la maintenabilité du code. [#1787](https://github.com/MTES-MCT/zero-logement-vacant/issues/1787)
- **CI/CD & Tests** : 
    - Parallélisation des tests de bout en bout (E2E) avec Playwright et Cypress pour accélérer les validations. [#1955](https://github.com/MTES-MCT/zero-logement-vacant/issues/1955)
    - Sécurisation des pipelines de revue (prévention de la fuite de secrets). [#1958](https://github.com/MTES-MCT/zero-logement-vacant/issues/1958)
    - Stabilisation des tests automatisés pour réduire les échecs aléatoires (flaky tests). [#1961](https://github.com/MTES-MCT/zero-logement-vacant/issues/1961)
- **Données & Analytics** : 
    - Optimisation et fiabilisation du pipeline de calcul de localisation des propriétaires via Dagster. [#1883](https://github.com/MTES-MCT/zero-logement-vacant/issues/1883), [#1944](https://github.com/MTES-MCT/zero-logement-vacant/issues/1944)
    - Corrections sur les indicateurs d'enrichissement et l'attribution des événements analytiques. [#1952](https://github.com/MTES-MCT/zero-logement-vacant/issues/1952), [#1951](https://github.com/MTES-MCT/zero-logement-vacant/issues/1951), [#1948](https://github.com/MTES-MCT/zero-logement-vacant/issues/1948)
- **Frontend** : Amélioration de la résilience face aux erreurs de chargement de fichiers (Vite chunks). [#1942](https://github.com/MTES-MCT/zero-logement-vacant/issues/1942)

### Autres changements
- Mise à jour de la documentation technique (plans de migration, spécifications de design et glossaire).
- Nettoyage général et formatage du code.
