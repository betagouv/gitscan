## Changelog : euphrosyne (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'implémentation d'une gestion du cycle de vie des données de projet, incluant des fonctionnalités de refroidissement (cooling) des données et une gestion des états de projet plus fine. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour la gestion des participations et des opérations de lifecycle, ainsi que des corrections de bugs et des mises à jour de dépendances.

### Évolutions fonctionnelles
- Ajout de la possibilité pour les responsables de modifier leurs propres participations [#1866](https://github.com/betagouv/euphrosyne/pulls/1866).
- Amélioration de l'interface utilisateur pour la liste des opérations de cycle de vie [#1851](https://github.com/betagouv/euphrosyne/pulls/1851).
- Ajout d'une période de grâce avant le refroidissement d'un projet.
- Amélioration de l'alignement des colonnes de participation dans l'interface utilisateur [#1897](https://github.com/betagouv/euphrosyne/pulls/1897).
- Possibilité pour les administrateurs de modifier le workflow des employés.
- Ajout d'un panneau d'administration pour la gestion du cycle de vie des projets dans l'interface utilisateur.
- Implémentation de transitions d'état du cycle de vie des projets et de règles de protection [#1857](https://github.com/betagouv/euphrosyne/pulls/1857).
- Ajout d'un planificateur automatique de refroidissement quotidien pour les projets éligibles.
- Implémentation d'une commande pour calculer la taille et le nombre de fichiers d'une exécution.
- Ajout d'un endpoint pour obtenir l'ID d'opération.
- Implémentation d'un endpoint de rappel pour la gestion des données.
- Amélioration de la documentation et des notes relatives au cycle de vie des données.

### Évolutions techniques
- Refactorisation de la gestion du cycle de vie des données au niveau du projet, avec de nouveaux modèles et une logique d'éligibilité.
- Mise en place d'un système de gestion des états de projet (HOT, COOL, COOLING) avec des restrictions d'accès et de modification.
- Ajout d'un workflow de déploiement vers Scalingo lors de la publication d'une nouvelle version.
- Utilisation du slug du projet pour le renommage du répertoire du projet.
- Correction de l'analyse de l'ID d'exécution dans le middleware [#1895](https://github.com/betagouv/euphrosyne/pulls/1895).
- Suppression de `downlevelIteration` du fichier `tsconfig.json`.
- Mise à jour de plusieurs dépendances : Django, djangorestframework, django-debug-toolbar, typescript, jsdom, prettier, vitest, webpack, axios, sentry, psycopg2, ipython, pytest, reportlab, fast-uri, fast-xml-builder, django-stubs, social-auth-app-django, wheel, sentry-sdk, types-requests, cropperjs, @typescript-eslint/eslint-plugin.
- Ajout de type ignore pour améliorer la compatibilité.
- Correction de l'emplacement du décorateur `api_view`.
- Ajout de tests pour la récupération du cycle de vie.
- Amélioration de la gestion des erreurs lors de l'initialisation de l'application.

### Autres changements
- Ajout de traductions manquantes.
- Correction de l'utilisation du slug du projet pour les URL de présignature des documents.
- Ajout de la variable d'environnement `DATA_COOLING_ENABLE` au fichier `env.example`.
- Mise à jour de la documentation du projet.
- Correction de l'utilisation d'IsLabAdminUser dans les vues API de gestion des données.
- Ajout d'une documentation pour la gestion des données.
- Ajout d'un fichier `epic.md` décrivant la gestion du cycle de vie des données.
