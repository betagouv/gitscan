## Changelog : Docurba (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, Docurba a bénéficié d'améliorations significatives en termes de performance et de stabilité, notamment grâce à l'optimisation des requêtes en base de données et à une meilleure gestion des tests. De nouvelles fonctionnalités ont été ajoutées pour faciliter la gestion des procédures et des enquêtes, ainsi que des améliorations de l'interface utilisateur, notamment un bandeau d'information pour les utilisateurs non authentifiés.

### Évolutions fonctionnelles
- Ajout d'un bandeau d'information sur la page de connexion pour clarifier la procédure de création de compte [#1867](https://github.com/MTES-MCT/Docurba/issues/1867).
- Ajout d'un bandeau de connexion pour les utilisateurs non authentifiés [#1865](https://github.com/MTES-MCT/Docurba/issues/1865).
- Mise en place d'une page dédiée à l'enquête ZAN 2026.
- Possibilité de filtrer les procédures dans l'administration par type de collectivité porteuse.
- Activation de la modification de la collectivité porteuse d'une procédure dans l'administration.
- Affichage de la colonne "procédure archivée" dans l'administration.
- Prototype d'une fonctionnalité d'enquête (survey).
- Suppression des procédures d'enquête si les procédures associées sont archivées.

### Évolutions techniques
- Optimisation des requêtes SQL pour corriger des problèmes de performance (N+1 queries) [#1865](https://github.com/MTES-MCT/Docurba/issues/1865).
- Amélioration de la configuration des tests : utilisation d'une base de données de test plus proche de la production, ajout de couverture de code (coverage) et utilisation du SHA de commit pour identifier les builds.
- Refonte de l'indexation Django pour gérer les colonnes générées.
- Utilisation des couleurs du thème Vuetify au lieu de CSS spécifiques dans le composant LoginBanner.
- Mise à jour de l'infrastructure de déploiement pour nettoyer la mémoire des serveurs plus fréquemment (déploiement horaire).
- Correction d'un test instable.
- Ajout d'un fichier README pour faciliter l'intégration de nouveaux développeurs.
- Mise à jour de plusieurs dépendances : `pytest`, `ruff`, `django-debug-toolbar`, `django`, `pygments`, `pytest-cov`, `django-datadog-logger`.

### Autres changements
- Mise à jour de la documentation et des kits de communication Nuxt.
- Correction de liens et de fautes de frappe dans la documentation et l'interface utilisateur.
- Correction d'un problème empêchant la restauration des migrations Django.
- Ajout d'un type de commune (CommuneType) avec des choix textuels.
- Réveil des applications et nettoyage de la mémoire.
