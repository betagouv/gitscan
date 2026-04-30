## Changelog : claw-code-go (30 derniers jours, au 29 avril 2026)

### Résumé
Ce changelog couvre une période d'intense développement pour claw-code-go, avec un focus sur l'implémentation de nouvelles fonctionnalités et l'amélioration de l'infrastructure existante. Les principaux changements incluent l'ajout de capacités de vision par ordinateur, la mise en place d'un marché de plugins distant, l'amélioration des outils d'interaction avec l'utilisateur et des corrections de sécurité. Le projet progresse rapidement vers la parité avec l'implémentation Rust originale.

### Évolutions fonctionnelles
- **Vision par ordinateur :** Ajout de l'outil `computer_use` permettant de contrôler l'ordinateur (capture d'écran, clics, saisie de texte) via `xdotool` et ImageMagick sous Linux.
- **Marché de plugins :** Implémentation d'un marché de plugins distant permettant de lister, télécharger et installer des plugins, avec vérification de signature (cosign). Nouvelle commande CLI `claw-code-go plugin install`.
- **Interaction utilisateur :** Implémentation des outils `ask_user` (avec options structurées) et `remote_trigger` (déclenchement distant).
- **Interface utilisateur (TUI) :** Amélioration de l'interface utilisateur en ligne de commande avec l'ajout d'une timeline des sessions, de la coloration syntaxique et de la possibilité de choisir le format de sortie.
- **Fournisseurs de modèles :** Ajout de support pour les fournisseurs AWS Bedrock, Azure Foundry et Vertex AI.
- **OAuth et authentification :** Implémentation d'un broker OAuth avec PKCE pour une authentification sécurisée.
- **Gestion des sessions :** Ajout de la persistance des sessions et de la gestion de l'historique.
- **Permissions et sécurité :** Implémentation d'un moteur de gestion des permissions et d'un classificateur LLM.

### Évolutions techniques
- **Refactoring et simplification :** Simplification du code, suppression de code mort et amélioration de la structure du projet.
- **Tests :** Ajout de tests unitaires et d'intégration pour couvrir les nouvelles fonctionnalités et améliorer la qualité du code. Ajout de tests de performance.
- **Télémetrie :** Intégration de l'exportation des logs via OpenTelemetry avec les protocoles gRPC et HTTP.
- **Architecture :** Amélioration de l'architecture avec l'ajout de hooks et d'événements de cycle de vie pour les plugins.
- **Sécurité :** Correction de failles de sécurité identifiées lors de revues de code et de tests.
- **Dépendances :** Ajout de nouvelles dépendances (OpenTelemetry, grpc) et mise à jour des dépendances existantes.
- **Configuration :** Amélioration de la gestion de la configuration et des variables d'environnement.
- **API :** Exposition de façades publiques pour les hooks, LSP, MCP, tâches, équipes, workers et outils.

### Autres changements
- **Documentation :** Mise à jour de la documentation, notamment le README, avec des informations sur les nouvelles fonctionnalités et l'utilisation du projet.
- **Logo :** Ajout d'un logo ASCII art au démarrage de l'interface TUI.
- **Workflow :** Documentation du workflow de test en environnement cloud.
- **Nettoyage du code :** Formatage du code avec `gofmt`.
- **Correction de bugs :** Correction de divers bugs et améliorations de la stabilité.
