## Changelog : graal (30 derniers jours)

### Résumé
Les dernières mises à jour de Graal se concentrent sur l'ajout de fonctionnalités pour la gestion des modèles de langage (LLM) comme Claude, améliorant ainsi les capacités d'analyse et de traitement des amendements législatifs. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées pour une meilleure expérience utilisateur et une plus grande stabilité.

### Évolutions fonctionnelles
- Ajout de boutons de connexion en mode développement pour faciliter les tests et la revue des environnements.
- Amélioration de la mise en page de la page d'accueil avec l'utilisation de composants DSFR Tile.
- Possibilité de supprimer des fichiers de bases de données d'amendements avec une reconstruction.
- Intégration de workflows pour le modèle de langage Claude.
- Ajout de la configuration des modèles de langage (LLM) via l'interface utilisateur et l'API.
- Limitation du nombre de requêtes par minute pour la configuration des LLM afin de prévenir les abus.

### Évolutions techniques
- Ajout de variables d'environnement Docker pour la configuration.
- Génération automatique des types d'API.
- Amélioration de la configuration des tests pour éviter les interférences entre les bases de données de développement et de test.
- Mise en place d'un mécanisme de nouvelle tentative pour la génération des types d'API.
- Correction de la configuration de `VITE_ENABLE_DEV_LOGIN`.
- Correction de la mise à jour du store de jobs lorsque les tâches sont terminées.
- Amélioration des permissions pour le webfetch de Claude dans les workflows CI.
- Correction d'un bug dans le workflow CI de Claude.
- Utilisation des IDs des fichiers de configuration au lieu de leurs noms pour éviter les collisions.
- Ajout de support pour les pull requests étiquetées dans les workflows CI.
- Suppression de l'utilisation de la version `latest` dans les workflows CI.

### Autres changements
- Ajout d'un fichier `CLAUDE.md` pour la documentation de Claude.
- Petites corrections diverses.
