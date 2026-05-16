## Changelog : monitorenv (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des aires réglementaires, la correction de bugs et l'optimisation de l'interface utilisateur. Des améliorations techniques ont également été apportées pour la maintenance et la stabilité de l'application, notamment concernant les dépendances et les tests.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de l'ergonomie des zones de vigilance, avec l'ajout d'un cercle de période dans la ligne du nom et une correction de l'interface utilisateur en mode étendu. [#24031c7](https://github.com/MTES-MCT/monitorenv/pull/24031c7)
- Ajout de la possibilité d'ajouter des tags aux missions avec des actions environnementales et une période associée. [#d225a21](https://github.com/MTES-MCT/monitorenv/pull/d225a21)
- Refonte de la table des missions pour la rendre extensible, améliorant ainsi la présentation et l'interaction avec les données. [#c424cf9](https://github.com/MTES-MCT/monitorenv/pull/c424cf9)
- Ajout de champs liés à la plongée lors d'opérations de contrôles conchylicoles. [#29b6535](https://github.com/MTES-MCT/monitorenv/pull/29b6535)
- Correction d'une faute de frappe dans le fichier README.
- Ajout d'un bouton de réinitialisation sur les modales de mission, de rapports et de tableau de bord. [#153e04a](https://github.com/MTES-MCT/monitorenv/pull/153e04a)
- Correction de la requête de recherche dans l'input de la carte. [#ad1ef22](https://github.com/MTES-MCT/monitorenv/pull/ad1ef22)
- Suppression de l'affichage du tag de période par défaut. [#b8899f6](https://github.com/MTES-MCT/monitorenv/pull/b8899f6)
- Mise à jour du label "Drone" pour l'unité de contrôle. [#459f193](https://github.com/MTES-MCT/monitorenv/pull/459f193)

### Évolutions techniques
- Refactorisation du code lié aux aires réglementaires, simplification du flux de mise à jour et suppression de code obsolète.
- Amélioration du flux de mise à jour des aires réglementaires de l'environnement CACEM.
- Suppression du flux de mise à jour des thèmes et des tags depuis le CACEM.
- Correction de tests unitaires et E2E. [#8938264](https://github.com/MTES-MCT/monitorenv/pull/8938264)
- Remplacement de `Cypress.env` par `Cypress.expose` pour une meilleure gestion de l'environnement de test. [#b0de394](https://github.com/MTES-MCT/monitorenv/pull/b0de394)
- Mise à jour de plusieurs dépendances, notamment Cypress, Sentry, et les dépendances de développement.
- Ajout de validation sur les cas d'utilisation de patch. [#6728627](https://github.com/MTES-MCT/monitorenv/pull/6728627)
- Configuration de Dependabot pour exclure `package.lock` et désactiver le rebase automatique.
- Correction de type errors. [#36dfa21](https://github.com/MTES-MCT/monitorenv/pull/36dfa21)

### Autres changements
- Ajout de nouveaux tags au projet. [#7651fcc](https://github.com/MTES-MCT/monitorenv/pull/7651fcc)
- Correction de la favicon en production. [#b91332f](https://github.com/MTES-MCT/monitorenv/pull/b91332f)
- Ajout d'un message d'avertissement pour les complétions de tags. [#d68436c](https://github.com/MTES-MCT/monitorenv/pull/d68436c)
- Amélioration de la documentation et de la configuration de Dependabot.
- Modifications suite aux revues de code. [#dc18b7b](https://github.com/MTES-MCT/monitorenv/pull/dc18b7b) et [#ffdce4e](https://github.com/MTES-MCT/monitorenv/pull/ffdce4e)
