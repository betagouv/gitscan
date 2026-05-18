## Changelog : monitorenv (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des aires réglementaires, l'optimisation de l'interface utilisateur pour les missions et les rapports, ainsi que sur la correction de bugs et l'amélioration de la stabilité de l'application. Des améliorations techniques ont également été apportées, notamment la mise à jour des dépendances et la configuration du CI/CD.

### Évolutions fonctionnelles

- Ajout de la possibilité d'ajouter une période (cercle temporel) au nom des Aires de Vigilance [#29b6535](https://github.com/MTES-MCT/monitorenv/commit/29b6535).
- Amélioration de l'interface utilisateur pour l'affichage des informations détaillées des Aires de Vigilance [#24031c7](https://github.com/MTES-MCT/monitorenv/commit/24031c7).
- Refonte de la table des missions pour la rendre extensible, facilitant ainsi la consultation des informations [#c424cf9](https://github.com/MTES-MCT/monitorenv/commit/c424cf9).
- Ajout de tags aux missions avec des actions environnementales et une période associée [#d225a21](https://github.com/MTES-MCT/monitorenv/commit/d225a21).
- Ajout d'un bouton de réinitialisation sur les modales de mission, de rapports et du tableau de bord [#153e04a](https://github.com/MTES-MCT/monitorenv/commit/153e04a).
- Ajout de nouvelles colonnes liées à la plongée lors d'opérations de contrôles conchylicoles [#0312b6d](https://github.com/MTES-MCT/monitorenv/commit/0312b6d).
- Correction de l'affichage des tags par défaut [#b8899f6](https://github.com/MTES-MCT/monitorenv/commit/b8899f6).
- Correction de fautes de frappe dans le fichier README [#5bd4eb4](https://github.com/MTES-MCT/monitorenv/commit/5bd4eb4).

### Évolutions techniques

- Mise à jour de Cypress de la version 14.5.3 à la version 15.14.2 [#6cd4987](https://github.com/MTES-MCT/monitorenv/commit/6cd4987).
- Mise à jour de @sentry/browser de la version 8.54.0 à la version 10.51.0 [#7e9ff49](https://github.com/MTES-MCT/monitorenv/commit/7e9ff49).
- Refactorisation du code lié aux aires réglementaires, simplification du flux de mise à jour et suppression de code obsolète [#a392cbf](https://github.com/MTES-MCT/monitorenv/commit/a392cbf), [#f92eefc](https://github.com/MTES-MCT/monitorenv/commit/f92eefc), [#ec556dc](https://github.com/MTES-MCT/monitorenv/commit/ec556dc), [#ea6fbe8](https://github.com/MTES-MCT/monitorenv/commit/ea6fbe8), [#e3c11ab](https://github.com/MTES-MCT/monitorenv/commit/e3c11ab), [#c83d4ca](https://github.com/MTES-MCT/monitorenv/commit/c83d4ca), [#bae93e6](https://github.com/MTES-MCT/monitorenv/commit/bae93e6), [#94cc272](https://github.com/MTES-MCT/monitorenv/commit/94cc272), [#63b061a](https://github.com/MTES-MCT/monitorenv/commit/63b061a), [#0b78f1d](https://github.com/MTES-MCT/monitorenv/commit/0b78f1d).
- Remplacement de Cypress.env par Cypress.expose [#b0de394](https://github.com/MTES-MCT/monitorenv/commit/b0de394).
- Mise à jour de la configuration de dependabot.yaml [#fee35f4](https://github.com/MTES-MCT/monitorenv/commit/fee35f4).
- Désactivation du rebase automatique sur dependabot [#5ec9a44](https://github.com/MTES-MCT/monitorenv/commit/5ec9a44).
- Ajout de validation sur les cas d'utilisation de patch [#6728627](https://github.com/MTES-MCT/monitorenv/commit/6728627).
- Correction de la requête de recherche dans la carte [#ad1ef22](https://github.com/MTES-MCT/monitorenv/commit/ad1ef22).
- Correction d'erreurs de type [#36dfa21](https://github.com/MTES-MCT/monitorenv/commit/36dfa21).

### Autres changements

- Ajout de nouveaux tags [#7651fcc](https://github.com/MTES-MCT/monitorenv/commit/7651fcc).
- Correction des tests [#8938264](https://github.com/MTES-MCT/monitorenv/commit/8938264).
- Mise à jour du label "Drone" pour l'unité de contrôle [#459f193](https://github.com/MTES-MCT/monitorenv/commit/459f193).
- Ajout d'un message d'avertissement pour la complétion des tags [#d68436c](https://github.com/MTES-MCT/monitorenv/commit/d68436c), [#9c5fa7b](https://github.com/MTES-MCT/monitorenv/commit/9c5fa7b), [#9ba60b3](https://github.com/MTES-MCT/monitorenv/commit/9ba60b3).
- Correction de l'icône de favicon en production [#b91332f](https://github.com/MTES-MCT/monitorenv/commit/b91332f).
- Correction du flux de mise à jour des aires réglementaires du CACEM [#6dfdde2](https://github.com/MTES-MCT/monitorenv/commit/6dfdde2).
