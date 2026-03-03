## Changelog : graal (30 derniers jours)

### Résumé
Les dernières mises à jour de Graal se concentrent sur l'amélioration de la gestion des configurations, notamment l'ajout de la prise en charge des fichiers Excel stockés dans S3 et l'intégration de nouveaux modèles de langage (LLM) comme Claude. L'interface utilisateur a également été améliorée avec l'ajout de composants DSFR et des boutons de connexion dédiés pour les environnements de revue. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de boutons de connexion dédiés pour les environnements de revue, facilitant l'accès pour les développeurs et testeurs.
- Implémentation d'une interface utilisateur pour la configuration et la gestion des fichiers Excel.
- Possibilité de supprimer les configurations Excel via le backend.
- Intégration de workflows pour le modèle de langage Claude.
- Amélioration de la mise en page de la page d'accueil avec des composants DSFR Tile.
- Ajout de la prise en charge de la configuration de modèles de langage (LLM) avec une interface dédiée.

### Évolutions techniques
- Refactorisation du backend pour la gestion des fichiers de configuration Excel, utilisant les IDs pour éviter les collisions.
- Ajout d'un mécanisme de nouvelle tentative pour la génération des types d'API.
- Amélioration de la configuration du pipeline CI/CD pour supporter les pull requests labellisées et éviter l'utilisation de la dernière version des dépendances.
- Ajout de tests pour s'assurer que la base de données de test n'interfère pas avec la base de données de développement.
- Mise en place d'une gestion des configurations pour les modèles de langage (LLM) dans la base de données.
- Augmentation du taux de limitation par défaut pour Albert.

### Autres changements
- Ajout d'un fichier `CLAUDE.md` pour documenter la configuration de Claude.
- Correction d'un bug où le texte des boutons de connexion en développement n'apparaissait pas.
- Correction d'un bug lié à l'utilisation de `VITE_API_URL` dans les boutons d'authentification.
- Petites corrections diverses.
