## Changelog : monitorenv (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des aires réglementaires et des zones de vigilance, avec des optimisations de l'interface utilisateur et des corrections de bugs. Des améliorations techniques ont également été apportées, notamment concernant la gestion des dépendances et la configuration de l'environnement de production.

### Évolutions fonctionnelles
- **Aires réglementaires :** Refonte complète de la gestion des aires réglementaires, incluant la suppression d'anciens champs et tables, et l'amélioration du flux de mise à jour des données provenant du CACEM. [#1234](https://github.com/MTES-MCT/monitorenv/issues/1234)
- **Zones de vigilance :** Ajout d'une nouvelle table pour les zones de vigilance, avec des filtres améliorés, des colonnes épinglées et une présentation en lignes extensibles.
- **Missions :** Possibilité d'ajouter des tags aux missions avec des informations sur l'action environnementale et la période concernée.
- **Recherche :** Correction du comportement de la recherche dans la carte.
- **Filtres :** Ajout d'un filtre pour les zones récentes.
- **Contrôle conchylicole :** Ajout de colonnes liées à la plongée lors d'opérations de contrôle conchylicole.

### Évolutions techniques
- **Dépendances :** Mise à jour de plusieurs dépendances, notamment Cypress, Sentry, et les librairies Python utilisées dans le pipeline CI/CD.
- **Cypress :** Remplacement de `Cypress.env` par `Cypress.expose` pour une meilleure gestion de l'environnement de test.
- **Dependabot :** Configuration améliorée de Dependabot pour exclure `package.lock` et désactiver le rebasage automatique.
- **Indexation :** Ajout d'un index sur les données d'identification pour optimiser les performances.
- **Authentification :** Amélioration de la logique de vérification de l'organisation unitaire (OU) pour les notifications par email.
- **Refactoring :** Refactorisation de la table des missions pour la rendre extensible.

### Autres changements
- **Documentation :** Amélioration de la documentation interne.
- **Tests :** Correction de tests unitaires et E2E.
- **UI :** Amélioration de la visibilité de l'environnement (intégration, pré-production).
- **Favicon :** Correction de l'URL de la favicon.
- **Bannière :** Réajout de la bannière sur toutes les pages.
- **Labels :** Mise à jour du label "Drone" pour les unités de contrôle.
