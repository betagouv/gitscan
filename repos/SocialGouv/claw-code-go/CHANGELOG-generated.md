## Changelog : claw-code-go (30 derniers jours, au 15 avril 2026)

### Résumé
Ce changelog reflète une période d'activité intense sur le projet claw-code-go, principalement axée sur le portage de fonctionnalités de l'implémentation Rust originale vers Go, en utilisant Iterion. Les efforts se concentrent sur l'ajout de support pour de nouveaux fournisseurs d'IA (xAI, DashScope), l'amélioration de l'infrastructure des outils, l'implémentation de fonctionnalités clés comme la persistance du plan d'exécution, et la construction d'une interface utilisateur en ligne de commande (TUI) complète.  De nombreuses améliorations de performance et de parité avec la version Rust ont également été apportées.

### Évolutions fonctionnelles
- Ajout du support pour les fournisseurs d'IA xAI et DashScope, incluant la détection automatique et l'intégration dans le registre de modèles.
- Implémentation d'une interface utilisateur en ligne de commande (TUI) avec des fonctionnalités telles que la coloration syntaxique, le support de différents formats de sortie, et la gestion du cycle de vie des tâches.
- Ajout de la gestion de l'historique, des coûts et des sessions dans l'interface utilisateur.
- Implémentation de la persistance du plan d'exécution, permettant de reprendre des tâches interrompues.
- Ajout de la gestion des permissions et d'un système de configuration.
- Amélioration de la gestion des outils, avec l'ajout de 33 outils supplémentaires et la correction de plusieurs problèmes de parité avec la version Rust.
- Ajout de la compression du résumé pour améliorer les performances.
- Ajout d'un validateur de cycle de vie MCP (Model Context Protocol).
- Ajout d'un système de plugins et de hooks pour étendre les fonctionnalités du projet.
- Ajout d'un logo ASCII art au démarrage de l'interface TUI.
- Amélioration de la documentation avec des captures d'écran et une description complète des fonctionnalités.

### Évolutions techniques
- Refactorisation de l'infrastructure des outils pour une meilleure performance et une plus grande parité avec la version Rust.
- Utilisation de structures de données typées pour améliorer la clarté et la maintenabilité du code.
- Implémentation de tests unitaires et d'intégration pour garantir la qualité du code.
- Amélioration de la gestion des erreurs et de la journalisation.
- Mise en place d'un système de cache pour les requêtes Anthropic afin d'optimiser les performances.
- Implémentation d'un système de gestion des sessions pour stocker et restaurer l'état des tâches.
- Utilisation de `filepath.Abs` pour garantir des chemins absolus corrects.
- Amélioration de la gestion des variables d'environnement.
- Portage de nombreuses fonctionnalités de la version Rust vers Go, notamment la gestion des permissions, la compression du résumé, et la gestion des outils.

### Autres changements
- Mise à jour de la documentation README pour refléter les dernières fonctionnalités et améliorations.
- Ajout d'un logo ASCII art au projet.
- Correction de plusieurs problèmes mineurs de code et d'interface utilisateur.
- Nettoyage du code et suppression du code mort.
- Amélioration de la cohérence du code avec les conventions de style Go.
