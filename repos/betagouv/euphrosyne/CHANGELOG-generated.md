## Changelog : euphrosyne (30 derniers jours, au 2026-04-16)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation d'une nouvelle gestion du cycle de vie des données des projets, incluant des fonctionnalités de refroidissement des données et de gestion de leur disponibilité. Des améliorations ont également été apportées à l'interface utilisateur pour refléter l'état du cycle de vie, et des corrections de bugs ont été effectuées pour améliorer la stabilité et la fiabilité de la plateforme. Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Évolutions fonctionnelles
- Ajout d'une fonctionnalité permettant de supprimer les données sources d'un projet lorsque les données sont en état "HOT". [#1697](https://github.com/betagouv/euphrosyne/pull/1697)
- Implémentation d'un mécanisme de refroidissement des données de projet avec des règles d'éligibilité et une planification automatique. [#1700](https://github.com/betagouv/euphrosyne/pull/1700), [#1713](https://github.com/betagouv/euphrosyne/pull/1713)
- Ajout d'une commande `cool_project` pour gérer manuellement le refroidissement des données.
- Amélioration de l'interface utilisateur pour afficher l'état du cycle de vie du projet et bloquer les mutations lorsque le projet est dans un état immuable.
- Ajout d'un panneau d'administration pour gérer le cycle de vie des projets.
- Possibilité d'exempter un plan de prévention dans l'interface d'administration. [#1807](https://github.com/betagouv/euphrosyne/pull/1807)
- Correction d'un problème empêchant la définition correcte du rôle d'administrateur de laboratoire pour la gestion des données. [#1848](https://github.com/betagouv/euphrosyne/pull/1848)
- Correction d'un problème d'affichage de la sélection de la définition d'image de projet pour les utilisateurs non administrateurs. [#1849](https://github.com/betagouv/euphrosyne/pull/1849)

### Évolutions techniques
- Refactorisation de la gestion du cycle de vie des données, passant d'un niveau "run" à un niveau "projet".
- Ajout d'APIs pour déclencher et suivre les opérations du cycle de vie.
- Mise en place d'un mécanisme pour éviter les déclenchements concurrents du cycle de vie.
- Amélioration de la gestion des erreurs lors du démarrage des processus de gestion des données.
- Simplification du panneau de contrôle du cycle de vie.
- Migration du bouton "virtual office" vers TypeScript.
- Mise à jour de nombreuses dépendances : Django (6.0.4), Pillow (12.2.0), axios (1.15.0), jsdom (29.0.0), typescript-eslint (8.57.0/8.57.1/8.57.2), webpack-cli (7.0.2), mini-css-extract-plugin (2.10.1/2.10.2), dotenv (17.4.0), serialize-javascript (7.0.5), flatted (3.4.2), black (26.3.1), pytest-django (4.12.0), whitenoise (6.12.0), markdown (3.10.2), ipython (9.11.0/9.12.0), pytest (9.0.2/9.0.3), reportlab (4.4.7/4.4.10), types-requests, wheel.

### Autres changements
- Ajout de documentation pour les nouvelles fonctionnalités de gestion des données.
- Nettoyage de la documentation relative aux projets.
- Correction d'un test flaky lié au nom des projets créés par la factory. [#1806](https://github.com/betagouv/euphrosyne/pull/1806)
- Mise à jour du fichier `env.example` pour inclure la variable `DATA_COOLING_ENABLE`.
- Correction de messages pour les projets archivés.
- Ajout d'un fichier `epic.md` décrivant le plan global pour la gestion du cycle de vie des données.
- Suppression du support Palissy.
- Utilisation de la nouvelle API POP et du service IIIF.
- Correction de l'utilisation de `project_slug` dans les appels à `euphro-tools`.
- Correction de l'utilisation de `IsLabAdminUser` dans les vues de l'API de gestion des données.
- Ajout d'un admin Django pour la gestion du cycle de vie.
- Amélioration de la computation de l'éligibilité au refroidissement.
- Ajout de tests pour la récupération du cycle de vie.
