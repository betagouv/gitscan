## Changelog : claw-code-go (30 derniers jours, au 14 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience d'utilisation de claw-code-go, notamment de nouvelles fonctionnalités pour la recherche, l'orchestration de tâches et la gestion de la mémoire. Des optimisations ont été apportées à l'API et à la gestion des prompts pour une meilleure performance et flexibilité. L'accent a été mis sur l'ajout de capacités d'automatisation et d'extension pour les agents.

### Évolutions fonctionnelles
- Ajout d'un moteur de recherche sémantique local pour la recherche de code, améliorant la pertinence des résultats. [#a55f3c6](https://github.com/SocialGouv/claw-code-go/commit/a55f3c6)
- Implémentation d'un système de tâches avec des dépendances, des alias et un vocabulaire unifié pour une meilleure organisation du travail. [#5f67a18](https://github.com/SocialGouv/claw-code-go/commit/5f67a18)
- Possibilité de définir des sous-agents dynamiquement à l'exécution avec des types personnalisés, permettant une plus grande flexibilité dans la création d'agents. [#9af2f42](https://github.com/SocialGouv/claw-code-go/commit/9af2f42)
- Ajout d'un outil "oracle" pour effectuer des requêtes à un modèle plus puissant, offrant une capacité d'analyse et de raisonnement accrue. [#7612b9b](https://github.com/SocialGouv/claw-code-go/commit/7612b9b)
- Introduction d'un moteur d'orchestration JavaScript pour la création de workflows complexes. [#fe05d8c](https://github.com/SocialGouv/claw-code-go/commit/fe05d8c)
- Possibilité de charger des commandes de projet à partir de fichiers Markdown dans le répertoire `.claude/commands/`. [#1d45deb](https://github.com/SocialGouv/claw-code-go/commit/1d45deb)
- Ajout de sections de prompt configurables pour une meilleure personnalisation du comportement de l'agent. [#93f1b5f](https://github.com/SocialGouv/claw-code-go/commit/93f1b5f)
- Implémentation d'une mémoire persistante basée sur des fichiers Markdown, permettant de conserver le contexte entre les sessions. [#aa1e101](https://github.com/SocialGouv/claw-code-go/commit/aa1e101)
- Amélioration de la gestion des prompts système avec des options pour les définir via la ligne de commande ou des fichiers de configuration. [#f211b8b](https://github.com/SocialGouv/claw-code-go/commit/f211b8b)

### Évolutions techniques
- Refactorisation de l'API pour consolider l'identité du client et simplifier le code. [#dad0827](https://github.com/SocialGouv/claw-code-go/commit/dad0827)
- Amélioration de la gestion des erreurs et des délais d'attente pour les requêtes streaming. [#1b49d47](https://github.com/SocialGouv/claw-code-go/commit/1b49d47)
- Mise à jour de l'environnement de développement avec Go 1.26 et l'outil direnv. [#15fbb2c](https://github.com/SocialGouv/claw-code-go/commit/15fbb2c)
- Correction de problèmes liés à l'omission de champs `required` dans les schémas d'outils OpenAI. [#c9eed79](https://github.com/SocialGouv/claw-code-go/commit/c9eed79)
- Correction d'un bug empêchant le changement de répertoire avec l'option `--cwd`. [#20b0741](https://github.com/SocialGouv/claw-code-go/commit/20b0741)
- Correction d'un problème de stockage de la liste de tâches dans l'arborescence de travail. [#21c4b7d](https://github.com/SocialGouv/claw-code-go/commit/21c4b7d)

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les changements de configuration. [#6845f7f](https://github.com/SocialGouv/claw-code-go/commit/6845f7f), [#70d79d4](https://github.com/SocialGouv/claw-code-go/commit/70d79d4), [#e988c1c](https://github.com/SocialGouv/claw-code-go/commit/e988c1c)
- Suppression des fichiers binaires compilés du suivi Git et du répertoire vendor. [#dccf92b](https://github.com/SocialGouv/claw-code-go/commit/dccf92b)
- Ajout d'un backend SearXNG auto-hébergé pour l'outil de recherche web. [#0faf395](https://github.com/SocialGouv/claw-code-go/commit/0faf395)
- Ajout de la surface des tokens de réflexion facturés dans les détails d'utilisation. [#70d79d4](https://github.com/SocialGouv/claw-code-go/commit/70d79d4)
- Ajout de la surface des résumés de raisonnement en tant que blocs de contenu de réflexion. [#270cf74](https://github.com/SocialGouv/claw-code-go/commit/270cf74)
