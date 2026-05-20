## Changelog : monitorenv (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des aires réglementaires, des missions et des tags, ainsi que sur des corrections de bugs et des optimisations techniques. Des améliorations ont été apportées à l'interface utilisateur pour faciliter l'utilisation et la clarté des informations. Plusieurs dépendances ont également été mises à jour pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité d'ajouter des tags aux missions avec des actions environnementales et une période associée. [#29 avril](https://github.com/MTES-MCT/monitorenv/commit/d225a21)
- Refonte de la table des missions pour la rendre extensible et plus claire. [#29 avril](https://github.com/MTES-MCT/monitorenv/commit/c424cf9)
- Ajout d'un bouton de réinitialisation sur les modales de mission, de rapports et du tableau de bord. [#30 avril](https://github.com/MTES-MCT/monitorenv/commit/153e04a)
- Ajout de nouvelles colonnes liées à la plongée lors d'opérations de contrôles conchylicoles. [#30 avril](https://github.com/MTES-MCT/monitorenv/commit/29b6535)
- Ajout de nouveaux tags. [#12 mai](https://github.com/MTES-MCT/monitorenv/commit/7651fcc)
- Correction de l'affichage du champ "période" dans les tags, pour ne pas afficher le tag par défaut. [#28 avril](https://github.com/MTES-MCT/monitorenv/commit/b8899f6)
- Correction du filtre des tags dans la recherche de couches. [#19 mai](https://github.com/MTES-MCT/monitorenv/commit/f60a326)
- Correction du champ de recherche sur la carte. [#04 mai](https://github.com/MTES-MCT/monitorenv/commit/ad1ef22)

### Évolutions techniques
- Refactorisation du code lié aux aires réglementaires, simplification du flux de mise à jour et suppression de code obsolète. Plusieurs commits entre le 7 et le 18 mai.
- Mise à jour de plusieurs dépendances : Cypress (14.5.3 -> 15.14.2), @sentry/browser (8.54.0 -> 10.51.0), ol-mapbox-style (12.3.3 -> 13.4.1), pytest, cryptography, et diverses autres dépendances de développement.
- Amélioration du flux de mise à jour des aires réglementaires de l'environnement CACEM. Plusieurs commits entre le 7 et le 18 mai.
- Remplacement de `Cypress.env` par `Cypress.expose` pour une meilleure gestion des variables d'environnement dans les tests Cypress. [#04 mai](https://github.com/MTES-MCT/monitorenv/commit/b0de394)
- Ajout de validations sur les cas d'utilisation de patch. [#04 mai](https://github.com/MTES-MCT/monitorenv/commit/6728627)
- Correction de type errors. [#28 avril](https://github.com/MTES-MCT/monitorenv/commit/36dfa21)
- Suppression du mot "New" pour les aires réglementaires. [#07 mai](https://github.com/MTES-MCT/monitorenv/commit/0b78f1d)
- Correction de la favicon en production. [#27 avril](https://github.com/MTES-MCT/monitorenv/commit/b91332f)

### Autres changements
- Correction de fautes de frappe dans le README. [#11 mai](https://github.com/MTES-MCT/monitorenv/commit/5bd4eb4)
- Mise à jour du fichier `dependabot.yaml`. [#04 mai](https://github.com/MTES-MCT/monitorenv/commit/fee35f4)
- Exclusion du fichier `package.lock` des mises à jour de dépendances de Dependabot. [#28 avril](https://github.com/MTES-MCT/monitorenv/commit/22391f0)
- Désactivation du rebase automatique pour Dependabot. [#30 avril](https://github.com/MTES-MCT/monitorenv/commit/5ec9a44)
- Mise à jour du label "Drone" pour "Unité de contrôle". [#28 avril](https://github.com/MTES-MCT/monitorenv/commit/459f193)
- Correction de tests unitaires et E2E. Plusieurs commits entre le 12 et le 19 mai.
