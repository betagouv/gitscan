## Changelog : claw-code-go (30 derniers jours, au 16 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience d'utilisation de claw-code-go, notamment de nouvelles fonctionnalités pour la gestion des tâches, l'orchestration de workflows, l'intégration de modèles plus puissants et une meilleure gestion de la mémoire et des prompts. Des optimisations et corrections ont également été apportées pour améliorer la fiabilité et la performance.

### Évolutions fonctionnelles
- Ajout d'un outil "oracle" permettant de solliciter un modèle plus puissant pour des requêtes spécifiques. [#7612b9b](https://github.com/SocialGouv/claw-code-go/commit/7612b9b)
- Implémentation de sous-agents définis dynamiquement à l'exécution avec des types configurables, permettant un parallélisme réel et une meilleure gestion des tâches. [#9af2f42](https://github.com/SocialGouv/claw-code-go/commit/9af2f42)
- Introduction d'un moteur d'orchestration de workflows basé sur JavaScript (goja) avec des fonctions `agent()`, `parallel()` et `pipeline()`. [#fe05d8c](https://github.com/SocialGouv/claw-code-go/commit/fe05d8c)
- Ajout de la gestion de graphes de tâches avec des dépendances, des alias et un vocabulaire unifié. [#5f67a18](https://github.com/SocialGouv/claw-code-go/commit/5f67a18)
- Possibilité de charger des commandes de projet à partir de fichiers Markdown dans le répertoire `.claude/commands/`. [#1d45deb](https://github.com/SocialGouv/claw-code-go/commit/1d45deb)
- Amélioration de la gestion des prompts avec des sections configurables et des options pour définir des prompts système via la ligne de commande ou des fichiers. [#3b4fdda](https://github.com/SocialGouv/claw-code-go/commit/3b4fdda) et [#93f1b5f](https://github.com/SocialGouv/claw-code-go/commit/93f1b5f)
- Ajout d'une mémoire persistante basée sur des fichiers Markdown importables avec des limites de profondeur, de cycle et de taille. [#aa1e101](https://github.com/SocialGouv/claw-code-go/commit/aa1e101) et [#9947944](https://github.com/SocialGouv/claw-code-go/commit/9947944)
- Ajout d'une recherche sémantique locale de code. [#a55f3c6](https://github.com/SocialGouv/claw-code-go/commit/a55f3c6)
- Possibilité de spécifier des en-têtes personnalisés pour les requêtes à l'API Anthropic. [#05398ca](https://github.com/SocialGouv/claw-code-go/commit/05398ca)

### Évolutions techniques
- Refactorisation de l'identité client de l'API pour une meilleure configuration et compatibilité. [#dad0827](https://github.com/SocialGouv/claw-code-go/commit/dad0827)
- Simplification et déduplication du code lié à la gestion des prompts. [#776a069](https://github.com/SocialGouv/claw-code-go/commit/776a069)
- Correction d'une erreur dans la gestion des schémas d'outils OpenAI qui incluait des valeurs nulles incorrectes. [#c9eed79](https://github.com/SocialGouv/claw-code-go/commit/c9eed79)
- Mise à jour de l'environnement de développement avec Go 1.26 et l'utilisation de `direnv`. [#15fbb2c](https://github.com/SocialGouv/claw-code-go/commit/15fbb2c)
- Amélioration de la gestion des erreurs et des timeouts. [#21c4b7d](https://github.com/SocialGouv/claw-code-go/commit/21c4b7d)
- Correction de la gestion du paramètre `--cwd` pour le prompt système. [#20b0741](https://github.com/SocialGouv/claw-code-go/commit/20b0741)

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les changements de configuration. [#6845f7f](https://github.com/SocialGouv/claw-code-go/commit/6845f7f) et [#492a5f5](https://github.com/SocialGouv/claw-code-go/commit/492a5f5) et [#e988c1c](https://github.com/SocialGouv/claw-code-go/commit/e988c1c)
- Ajout d'un backend SearXNG auto-hébergé pour l'outil de recherche web. [#0faf395](https://github.com/SocialGouv/claw-code-go/commit/0faf395)
- Suppression du binaire compilé du suivi Git et ajout d'un fichier `.gitignore` pour le répertoire `vendor/`. [#dccf92b](https://github.com/SocialGouv/claw-code-go/commit/dccf92b)
- Correction de la limite de sortie maximale pour le modèle `claude-sonnet-4-6`. [#83e24cc](https://github.com/SocialGouv/claw-code-go/commit/83e24cc)
- Ajout de la surface des tokens de réflexion facturés avec précision dans les détails d'utilisation. [#70d79d4](https://github.com/SocialGouv/claw-code-go/commit/70d79d4)
- Demande de résumés de raisonnement pour les requêtes Anthropic. [#a27d632](https://github.com/SocialGouv/claw-code-go/commit/a27d632)
- Surface des résumés de raisonnement en tant que blocs de contenu de réflexion. [#270cf74](https://github.com/SocialGouv/claw-code-go/commit/270cf74)
- Ajout de permissions intégrées en lecture seule pour bash. [#2289fe7](https://github.com/SocialGouv/claw-code-go/commit/2289fe7)
- Injection de `<system-reminder>` pour la synchronisation. [#e38d04b](https://github.com/SocialGouv/claw-code-go/commit/e38d04b)
- Ajout d'un résumé de transfert à neuf sections pour la compaction. [#b4bfb3f](https://github.com/SocialGouv/claw-code-go/commit/b4bfb3f)
- Enseignement de la politique d'utilisation dans les descriptions des outils principaux. [#04558c6](https://github.com/SocialGouv/claw-code-go/commit/04558c6)
- Tests unitaires et d'intégration mis à jour. [#aa87bf1](https://github.com/SocialGouv/claw-code-go/commit/aa87bf1) et [#02ffe13](https://github.com/SocialGouv/claw-code-go/commit/02ffe13)
