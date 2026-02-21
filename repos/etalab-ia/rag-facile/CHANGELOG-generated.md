## Changelog : rag-facile (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par une amélioration significative de l'expérience utilisateur et de la fonctionnalité de rag-facile. De nouvelles fonctionnalités ont été ajoutées, notamment un système de compétences, une gestion de la mémoire de session basée sur Git, et une intégration avec un harnais smolagents pour le chat. L'interface CLI a été rationalisée et des outils de débogage ont été ajoutés.  Des améliorations ont également été apportées à la configuration et à la gestion des projets.

### Évolutions fonctionnelles
- Ajout d'un système de compétences avec 5 compétences intégrées et une intégration avec npx skills.
- Implémentation d'une gestion de la mémoire de session basée sur Git avec une summarisation post-session.
- Intégration d'un harnais smolagents pour le chat.
- Rationalisation de l'interface CLI avec des panneaux d'aide regroupés, une configuration simplifiée et une exécution plus intelligente de `just run`.
- Ajout d'un assistant d'initialisation de l'espace de travail pour guider les nouveaux utilisateurs.
- Ajout d'outils de débogage, notamment un drapeau `--debug` pour afficher les appels d'outils de l'agent.
- Ajout d'un outil `get_docs` avec une documentation intégrée.
- Ajout d'un outil `update_config` pour modifier la configuration.
- Ajout de la possibilité d'éditer la configuration via l'interface de chat.
- Ajout de la gestion des collections et de la possibilité de les activer/désactiver.
- Ajout de la prise en charge de l'expansion de requêtes avec des stratégies multi-requêtes et HyDE.
- Ajout de la prise en charge de l'API Albert pour la recherche et la récupération de documents.
- Ajout de la possibilité d'utiliser des collections publiques Albert.
- Ajout d'une fonction de recherche de datasets avec des filtres par tâche et langue.
- Ajout d'un système de configuration avec des commandes CLI dédiées.
- Ajout d'un mode standalone pour une installation plus simple.

### Évolutions techniques
- Refactorisation de l'architecture pour séparer les préoccupations et améliorer la maintenabilité.
- Utilisation de Moon pour la génération de templates de projets.
- Intégration de `just` pour la gestion des tâches de développement.
- Amélioration de la gestion des dépendances avec `uv`.
- Ajout de tests unitaires pour les nouvelles fonctionnalités.
- Mise à jour des dépendances vers les dernières versions.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Utilisation de type hints pour améliorer la lisibilité et la maintenabilité du code.
- Amélioration de la gestion des variables d'environnement.
- Ajout de workflows CI/CD pour automatiser les tests et le déploiement.

### Autres changements
- Ajout d'un fichier CHANGELOG pour documenter les modifications apportées au projet.
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les modifications apportées au code.
- Correction de bugs et amélioration de la stabilité du code.
- Amélioration de la lisibilité et de la cohérence du code.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Ajout d'un fichier .gitignore pour exclure les fichiers inutiles du contrôle de version.
- Ajout d'un fichier .env.example pour fournir un exemple de configuration des variables d'environnement.
- Ajout d'un fichier CONTRIBUTING.md pour documenter les directives de contribution au projet.
