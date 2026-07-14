## Changelog : claw-code-go (30 derniers jours, au 13 juillet 2026)

### Résumé
Les dernières mises à jour de claw-code-go se concentrent sur l'amélioration des capacités d'orchestration, de recherche et de gestion de la mémoire, ainsi que sur l'ajout de nouveaux outils et fonctionnalités pour les agents conversationnels. Ces améliorations visent à rendre le projet plus puissant, flexible et facile à utiliser pour les développeurs.

### Évolutions fonctionnelles
- Ajout d'un backend SearXNG auto-hébergé pour l'outil `web_search` [#1234](https://github.com/SocialGouv/claw-code-go/issues/1234).
- Possibilité de spécifier des prompts système via la ligne de commande avec les options `--system-prompt` et `--append-system-prompt`, et de les définir dynamiquement.
- Implémentation d'une gestion des tâches avec des dépendances, des alias et un vocabulaire unifié.
- Ajout d'un outil `oracle` permettant de solliciter un modèle plus puissant pour des conseils.
- Introduction de types de sous-agents définis dynamiquement à l'exécution, avec des notifications de complétion.
- Ajout de commandes de projet chargées à partir de fichiers `.claude/commands/*.md`.
- Amélioration de la gestion de la mémoire avec l'injection de fichiers `MEMORY.md` et l'importation de fichiers avec des limites de profondeur, de cycle et de taille.
- Affichage des tokens facturés pour l'utilisation des modèles via l'API.
- Extraction des résumés de raisonnement pour les modèles OpenAI et Anthropic.
- Mise en place d'une politique d'utilisation intégrée dans les descriptions des outils.

### Évolutions techniques
- Refactorisation de l'identité client API pour une meilleure configuration et compatibilité.
- Consolidation de l'identité client dans `api.Identity` et suppression du code obsolète.
- Amélioration de la gestion des erreurs et des délais d'attente pour les flux de streaming.
- Implémentation d'un moteur d'orchestration JavaScript basé sur `goja` avec des fonctions `agent()`, `parallel()` et `pipeline()`.
- Mise en place d'un système de gestion des permissions avec une autorisation automatique en lecture seule pour `bash` et une gestion des permissions complètes.
- Simplification et déduplication du code lié aux prompts.
- Passage à Go 1.26 dans l'environnement de développement avec `devbox` et `direnv`.
- Correction d'une erreur dans la gestion du répertoire de travail avec `--cwd`.
- Amélioration de la gestion des erreurs lors de l'analyse des en-têtes `Retry-After`.
- Suppression du binaire compilé du suivi Git et du dossier `vendor/`.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les changements de configuration.
- Ajout d'une matrice de parité pour les sections de prompt et la gestion de la mémoire.
- Nettoyage du code avec un passage `gofmt` sur l'ensemble du projet.
- Correction de bugs mineurs et améliorations de la stabilité.
