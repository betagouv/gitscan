## Changelog : graal (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe de développement s'est concentrée sur l'ajout de la gestion de configurations pour les modèles de langage (LLM) et l'amélioration de la gestion des fichiers Excel pour la configuration du système. Des améliorations de l'interface utilisateur et des corrections de bugs ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une interface utilisateur pour la configuration des fichiers Excel (#224).
- Possibilité de supprimer les configurations Excel via le backend.
- Ajout de workflows utilisant le modèle de langage Claude.
- Amélioration de la mise en page de la page d'accueil avec des composants DSFR.
- Correction d'un bug empêchant la suppression de manifestes de la base de données si le fichier S3 correspondant n'existait pas.
- Correction d'un bug lié à l'URL de l'API dans les boutons d'authentification.
- Ajout de la gestion des requêtes OAuth dans la base de données PostgreSQL.
- Ajout d'un titre à l'onglet du navigateur pour une meilleure identification de l'application.

### Évolutions techniques
- Ajout d'un backend pour la configuration des modèles de langage (LLM).
- Ajout des configurations LLM à la base de données.
- Refactorisation du backend pour la gestion des fichiers de configuration Excel, en utilisant les IDs pour éviter les collisions.
- Ajout d'un mécanisme de retry pour la génération des types d'API.
- Amélioration des tests pour éviter les interférences entre les bases de données de test et de développement.
- Utilisation de variables d'environnement pour les uploads S3.
- Correction d'un crash du pipeline de traitement lié à S3 et aux opérations asynchrones.
- Amélioration des appels à la fonction `require_db_role` en fournissant l'utilisateur.
- Mise à jour de la configuration du CI/CD pour supporter les pull requests labellisées et éviter l'utilisation de la version "latest".

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités.
- Publication des versions 1.46.0, 1.45.0, 1.44.2, 1.44.1, 1.44.0, 1.43.1, 1.43.0, 1.42.0, 1.41.0 et 1.40.0.
