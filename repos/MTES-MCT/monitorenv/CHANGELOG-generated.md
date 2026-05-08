## Changelog : monitorenv (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les évolutions de monitorenv se sont concentrées sur l'amélioration de la gestion des aires réglementaires, des zones de vigilance et des données des navires. Des corrections et des optimisations ont également été apportées à l'interface utilisateur et aux processus de données, notamment pour la gestion des AMP et des données de contrôle conchylicole.

### Évolutions fonctionnelles
- **Aires réglementaires :** Suppression de fonctionnalités et de colonnes obsolètes liées aux aires réglementaires, simplification du formulaire et correction de bugs liés à la mise à jour des données.
- **Zones de vigilance :** Refonte de la table des zones de vigilance avec des filtres améliorés, des colonnes épinglées et une présentation plus claire.
- **Navires :** Ajout du tonnage brut des navires UMS et amélioration de la récupération des données des navires.
- **AMP :** Mise en évidence des nouvelles AMP et correction du flux de données associé.
- **Cartographie :** Correction d'un bug lié à la requête de recherche dans la carte.
- **Tags :** Ajout d'un message d'avertissement pour les tags en cours de complétion.
- **Contrôle conchylicole :** Ajout de colonnes liées à la plongée lors des opérations de contrôle conchylicole.

### Évolutions techniques
- **Cypress :** Mise à jour de Cypress en version 15.14.2 et remplacement de `Cypress.env` par `Cypress.expose`.
- **Dépendances :** Mises à jour de plusieurs dépendances, notamment `@sentry/browser`, `docker/login-action`, `python-dotenv`, `pytest`, `cryptography`, `ol-mapbox-style` et `black`.
- **CI/CD :** Configuration de dependabot pour exclure `package.lock` et désactiver le rebase automatique.
- **Architecture :** Refactorisation de la table des missions pour la rendre extensible.
- **Tests :** Ajout de tests unitaires et d'intégration pour valider les nouvelles fonctionnalités et les corrections de bugs.
- **Base de données :** Ajout d'un index sur les données d'identification et refactorisation de la récupération des données des navires.

### Autres changements
- Amélioration de la visibilité de l'environnement (intégration/pré-production) dans l'interface utilisateur.
- Suppression du feature flag "Regulatory areas".
- Correction de la favicon en production.
- Ajout d'un bouton de réinitialisation sur les modales de mission, de reporting et de tableau de bord.
- Ajout d'un message d'avertissement pour les tags en cours de complétion.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de validation sur les cas d'utilisation de patch.
- Suppression de l'affichage du tag de période par défaut.
- Ajout d'un titre aux options du sélecteur Natinf.
- Correction de l'icône de tri des chevrons.
- Mise à jour du libellé "Drone" dans l'unité de contrôle.
