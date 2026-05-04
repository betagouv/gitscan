## Changelog : claw-code-go (30 derniers jours, au 2 mai 2026)

### Résumé
Ce changelog couvre une période d'intense développement sur claw-code-go, principalement axée sur l'implémentation de fonctionnalités en cours de portage depuis l'implémentation Rust originale. Les efforts se sont concentrés sur l'ajout de nouveaux outils, l'amélioration de l'intégration avec des services externes (modèles de langage, fournisseurs de cloud), et l'amélioration de la sécurité et de la flexibilité du projet. De nombreuses améliorations concernent l'API, les plugins et les outils disponibles.

### Évolutions fonctionnelles
- Ajout d'un outil `computer_use` permettant d'interagir avec le bureau de l'utilisateur (capture d'écran, clics, saisie de texte) via `xdotool` et ImageMagick sous Linux.
- Implémentation d'un système de marketplace pour les plugins, permettant de télécharger et d'installer des plugins à partir d'une URL spécifiée, avec vérification de signature.
- Ajout des outils `ask_user` et `remote_trigger` qui étaient précédemment des stubs. `ask_user` permet de poser des questions à l'utilisateur avec des options structurées, et `remote_trigger` permet de déclencher des actions à distance.
- Implémentation de fournisseurs de modèles de langage réels : AWS Bedrock, Azure Foundry et Vertex AI.
- Ajout de la prise en charge des modèles xAI et DashScope.
- Ajout d'une commande `/timeline` pour afficher l'historique des sessions.
- Ajout d'une commande `/lineage` pour afficher l'historique des sessions.
- Amélioration de la gestion des erreurs et des timeouts pour les requêtes HTTP.
- Ajout de la possibilité de configurer l'URL des moteurs de recherche Brave et DuckDuckGo via des variables d'environnement.
- Ajout de la possibilité de spécifier des variables d'environnement lors de l'exécution de commandes Bash.
- Ajout de la possibilité de récupérer le prix des modèles via l'API.
- Ajout de la prise en charge de l'authentification OAuth pour le MCP (Model Contract Provider).

### Évolutions techniques
- Refactorisation du code pour améliorer la structure et la maintenabilité.
- Ajout de tests unitaires et d'intégration pour couvrir les nouvelles fonctionnalités.
- Mise à jour des dépendances.
- Amélioration de la gestion des erreurs et de la journalisation.
- Implémentation d'un système de cache pour les modèles de langage.
- Ajout de la prise en charge de la télémétrie avec OpenTelemetry (OTLP/gRPC).
- Utilisation de `go.opentelemetry.io/otel` pour la télémétrie.
- Amélioration de la sécurité avec la vérification des signatures des plugins et la correction de vulnérabilités identifiées lors de revues de code.
- Utilisation de `aws-sdk-go-v2` pour l'intégration avec AWS Bedrock.
- Amélioration de la gestion des contextes et des annulations.
- Refonte de l'API pour exposer de nouvelles fonctionnalités et améliorer l'expérience des développeurs.
- Ajout de la prise en charge de la compression des messages pour améliorer les performances.
- Implémentation d'un système de persistance des sessions.
- Ajout de la prise en charge de la gestion des plugins avec des hooks de cycle de vie.

### Autres changements
- Ajout d'une licence MIT.
- Mise à jour de la documentation.
- Nettoyage du code.
- Correction de bugs mineurs.
- Amélioration de la performance.
- Ajout de tests pour les nouveaux fournisseurs de modèles de langage.
- Documentation des workflows de test avec les fournisseurs de cloud.
- Ajout de commentaires et de documentation pour améliorer la compréhension du code.
- Correction de plusieurs problèmes de sécurité identifiés lors de revues de code.
- Mise à jour de la structure du projet pour faciliter l'importation en tant que module distant.
- Suppression de code mort et de dépendances inutiles.
- Amélioration de la gestion des erreurs et des logs.
