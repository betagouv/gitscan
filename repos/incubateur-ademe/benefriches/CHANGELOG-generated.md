## Changelog : benefriches (30 derniers jours, au 13 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la refactorisation technique du code pour une meilleure maintenabilité et performance, notamment avec le passage à un nouveau système de tests et l'optimisation de la gestion des variables d'environnement. Des améliorations fonctionnelles ont été apportées à l'interface utilisateur pour les projets urbains, avec l'ajout de nouvelles sections et informations dans le résumé du projet. L'outil a également été enrichi avec de nouvelles données sur la ruralité des villes pour affiner les calculs d'impact.

### Évolutions fonctionnelles
- Ajout d'une section "Avancement" au résumé des projets urbains.
- Ajout de la possibilité de renseigner si un projet implique une réhabilitation.
- Affichage des empreintes des bâtiments dans le résumé des projets urbains.
- Ajout de la section "Acteurs" avec la possibilité de renseigner les entreprises en charge des bâtiments.
- Amélioration de l'affichage des informations sur les dépenses.
- Affichage de la surface contaminée et de la surface du site dans les exports CSV des projets de reconversion.
- Amélioration des messages d'erreur liés à l'authentification.

### Évolutions techniques
- Migration des tests unitaires et d'intégration vers le framework `node:test` et `node:assert`.
- Refactorisation importante du code, notamment dans les modules `api` et `shared`, avec application de règles de qualité de code plus strictes (oxlint).
- Passage à un système de build natif ESM avec SWC pour l'API.
- Amélioration du système de gestion des variables d'environnement pour les builds.
- Extraction et généralisation du moteur de formulaire "wizard-form".
- Optimisation de la gestion des données de ruralité des villes avec l'ajout de la base de données "France Ruralités".
- Amélioration du caching des builds E2E.

### Autres changements
- Documentation mise à jour pour refléter les changements techniques et l'utilisation de nouveaux outils.
- Clarification des règles de test et ajout de documentation pour l'utilisation de l'outil CLAUDE.
- Mise à jour des dépendances.
- Ajout d'un Makefile pour simplifier les tâches de build et de déploiement.
- Amélioration des logs pour les erreurs d'authentification.
