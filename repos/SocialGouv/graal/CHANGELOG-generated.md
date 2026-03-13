## Changelog : graal (30 derniers jours)

### Résumé
Les dernières mises à jour de Graal se concentrent sur l'amélioration de la gestion des configurations, notamment l'ajout de la configuration des modèles de langage (LLM) avec des limites de débit et une interface dédiée. Des améliorations ont également été apportées à l'interface utilisateur, notamment sur la page d'accueil, et des corrections de bugs ont été implémentées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de boutons de connexion en mode développement pour faciliter les tests et la revue des environnements.
- Amélioration de la mise en page de la page d'accueil avec l'utilisation de composants DSFR Tile [#224](https://github.com/SocialGouv/graal/issues/224).
- Possibilité de supprimer des fichiers des bases de données d'amendements avec une reconstruction [#229](https://github.com/SocialGouv/graal/issues/229).
- Ajout d'une configuration pour limiter le nombre de requêtes par minute aux modèles de langage (LLM).
- Ajout d'une interface pour configurer les modèles de langage (LLM).

### Évolutions techniques
- Ajout d'une configuration pour utiliser les IDs des fichiers de configuration au lieu de leurs noms, évitant ainsi des collisions.
- Refonte du mécanisme de gestion des jobs pour une meilleure mise à jour de l'état.
- Ajout d'un mécanisme de retry pour la génération des types d'API.
- Amélioration de la configuration des variables d'environnement pour VITE_ENABLE_DEV_LOGIN.
- Ajout de workflows pour Claude.
- Amélioration des permissions webfetch pour Claude.
- Correction de la configuration du workflow PR pour Claude.
- Ajout de tests pour s'assurer que la base de données de test n'interfère pas avec la base de données de développement.

### Autres changements
- Ajout d'un fichier `CLAUDE.md` pour documenter la configuration de Claude.
- Correction d'un problème d'affichage du texte des boutons de connexion en mode développement.
- Amélioration de la gestion des logs pour les messages d'authentification.
- Correction de la configuration du workflow CI/CD pour éviter l'utilisation de la dernière version des dépendances.
- Ajout de support pour les pull requests labellisées dans le workflow CI/CD.
- Petites corrections diverses.
