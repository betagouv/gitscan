## Changelog : claw-code-go (30 derniers jours, au 5 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'écosystème de claw-code-go, notamment l'ajout de fonctionnalités clés pour l'utilisation d'outils (vision, exécution de commandes), la gestion des plugins (marketplace distant, signature), et l'intégration de nouveaux fournisseurs de modèles de langage. De nombreuses corrections et optimisations ont également été apportées pour améliorer la stabilité et la performance.

### Évolutions fonctionnelles
- **Outils :** Ajout de l'outil `computer_use` permettant d'interagir avec le système d'exploitation (capture d'écran, clics de souris, saisie de texte) via `xdotool` et ImageMagick.
- **Plugins :** Implémentation d'un marketplace distant pour les plugins, avec vérification de signature (cosign) et installation sécurisée. Nouvelle commande CLI `claw-code-go plugin install` pour installer les plugins depuis le marketplace.
- **Interaction utilisateur :** Ajout d'implémentations fonctionnelles pour les outils `ask_user` (avec options structurées) et `remote_trigger`.
- **Fournisseurs de modèles :** Intégration des fournisseurs AWS Bedrock, Azure Foundry, xAI et DashScope.
- **Interface utilisateur :** Ajout d'une commande `timeline` pour visualiser l'historique des sessions et d'une commande `lineage` pour suivre l'évolution des tâches.
- **API :** Exposition de façades publiques pour les hooks, LSP, MCP et autres composants, facilitant l'intégration avec d'autres systèmes.
- **Télémetrie :** Ajout d'un exportateur de logs au format OTLP/gRPC pour une meilleure surveillance et analyse.

### Évolutions techniques
- **Refactoring :** Simplification du code et suppression de code mort dans plusieurs modules.
- **Sécurité :** Correction de vulnérabilités potentielles identifiées lors de revues de code et de tests de sécurité.
- **Performance :** Optimisations de la gestion de la mémoire et des requêtes HTTP.
- **Architecture :** Amélioration de la modularité et de l'extensibilité du code.
- **Tests :** Ajout de tests unitaires et d'intégration pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- **Configuration :** Amélioration de la gestion de la configuration et des variables d'environnement.
- **Dépendances :** Mise à jour des dépendances et ajout de nouvelles dépendances pour supporter les nouvelles fonctionnalités.
- **Gestion des erreurs :** Introduction d'une gestion des erreurs plus structurée et informative.
- **Authentification :** Implémentation d'un broker OAuth pour une authentification sécurisée avec des fournisseurs externes.
- **Compatibilité :** Amélioration de la compatibilité avec l'implémentation Rust originale.

### Autres changements
- Ajout d'une licence MIT au projet.
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés.
- Amélioration de la structure du changelog.
- Ajout de tests de performance.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Documentation des workflows de test cloud-provider.
- Ajout de tests de fumée pour les fournisseurs Bedrock, Vertex et Foundry.
- Ajout de la possibilité de spécifier un chemin d'accès personnalisé pour le marketplace des plugins.
- Ajout de la possibilité de désactiver la vérification de signature des plugins.
- Amélioration de la gestion des timeouts HTTP.
- Ajout de la possibilité de spécifier un format de sortie pour les commandes CLI.
- Ajout de la possibilité de spécifier un répertoire de destination pour l'installation des plugins.
- Ajout de la possibilité de spécifier un timeout pour l'installation des plugins.
