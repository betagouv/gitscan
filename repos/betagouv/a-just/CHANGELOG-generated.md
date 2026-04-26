## Changelog : a-just (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la stabilité et de la fiabilité des tests E2E, ainsi que sur la mise à jour des dépendances du projet pour bénéficier des dernières corrections de sécurité et améliorations de performance. Des corrections ont également été apportées à l'interface utilisateur pour améliorer l'expérience utilisateur, notamment au niveau de la visualisation des données.

### Évolutions fonctionnelles
- Correction d'un bug dans les tests API concernant la modification des données utilisateur. [#522](https://github.com/betagouv/a-just/pull/522)
- Correction de la propagation de la valeur du stock calculé lors de la suppression de la saisie sur un stock "à vérifier" hérité du mois précédent. [#522](https://github.com/betagouv/a-just/pull/522)
- Amélioration de la visualisation des dernières données dans le cockpit.
- Suppression du nombre aléatoire pour la sécurité des mots de passe.

### Évolutions techniques
- Mise à jour de la configuration des tests E2E : navigateur, version de Cypress, méthode d'accès aux variables d'environnement.
- Refactorisation du Dockerfile pour les tests E2E afin d'améliorer la cohérence et la maintenabilité.
- Suppression de modules inutiles (babel-cli, esdoc, compodoc) et nettoyage du code.
- Mise à jour de nombreuses dépendances : Axios, Lodash, TypeScript, Angular, Node modules, modules de base de données, et actions GitHub.
- Suppression de `precommit` et mise à jour des versions des actions GitHub.
- Modification de la configuration de build pour le front-end.

### Autres changements
- Suppression de la documentation temporaire.
- Ajout d'options et de packages optionnels.
- Nettoyage des fichiers `package-lock.json`.
- Correction de logs inutiles.
- Ajout d'un module personnalisé `koa-smart`.
- Obtention de la date de ventilation par référentiel pour les enfants.
