## Changelog : nitrates (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration significative de la validation des données, notamment via l'intégration de références Miro et l'ajout de fonctionnalités de filtrage et de tri.  Des améliorations ont également été apportées au simulateur, avec une meilleure gestion des règles, des dates et de l'affichage des résultats. Enfin, des optimisations de performance et des corrections de bugs ont été réalisées.

### Évolutions fonctionnelles
- **Validation des données :**
    - Intégration de références Miro pour les validations, incluant l'affichage des widget IDs et la possibilité de naviguer vers les boards Miro correspondants [#140](https://github.com/betagouv/nitrates/issues/140).
    - Ajout de filtres et de tris sur les données de validation (scope, nature, ordre Miro).
    - Amélioration de l'interface utilisateur pour la validation, avec un auto-scroll vers la première feuille non validée et la préservation des filtres lors de la navigation.
    - Possibilité de visualiser les captures d'écran des validations couvertes.
- **Simulateur :**
    - Correction de l'affichage des règles partagées (plafond et ASC).
    - Amélioration de la gestion des dates et des bornes dans le calendrier, avec une absorption des bornes adjacentes à une date saisie.
    - Ajout de la possibilité de saisir des dates directement via l'URL.
    - Affichage des ZAR (Zones d'Action Renforcée) sur la carte du simulateur.
- **Résultats :**
    - Amélioration de l'affichage des résultats, avec une période d'autorisation plus claire et un format de date unifié.
    - Ajout d'un panneau de débogage pour afficher les règles appliquées et les informations de la parcelle.
- **Administration :**
    - Amélioration de l'interface d'administration pour l'édition des règles et des arbres de décision.
    - Ajout d'icônes et d'une meilleure organisation des éléments dans l'interface d'administration.

### Évolutions techniques
- **Performance :**
    - Optimisation de la fonction `get_criteria` pour réduire les requêtes inutiles.
    - Mise en cache des référentiels pour améliorer les performances.
    - Scission des effluents peu chargés pour une meilleure organisation des données.
- **Tests :**
    - Augmentation de la couverture de tests du cœur moteur à 98-100%.
    - Ajout de tests Playwright pour valider le fonctionnement de l'interface utilisateur.
    - Exclusion des tests et des migrations du rapport de couverture pour ne mesurer que le code fonctionnel.
- **Infrastructure :**
    - Mise à jour des arbres de décision actifs Grand Est (PAN, PAR, ZAR).
    - Refonte du système d'ouverture géographique pour permettre l'activation/désactivation par région.
- **Code :**
    - Refactoring du code pour améliorer la lisibilité et la maintenabilité.
    - Utilisation de Python sandboxé pour l'évaluation des expressions dans les catalogues paramétrés.
    - Migration des arbres de décision pour aligner les numéros de version.

### Autres changements
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de l'expérience utilisateur.
- Ajout de nouvelles règles et de digestats dans les référentiels.
- Amélioration de la grammaire et de la logique du calculateur.
- Corrections de style et d'alignement dans l'interface utilisateur.
