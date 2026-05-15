## Changelog : claw-code-go (30 derniers jours, au 13 mai 2026)

### Résumé
Les 30 derniers jours ont été marqués par une avancée significative du projet, notamment avec l'ajout de nouvelles fonctionnalités clés comme la prise en charge de l'exécution de commandes sur le système via l'outil `computer_use`, l'intégration d'un marché de plugins distant pour étendre les capacités de claw-code-go, et l'implémentation complète des outils `ask_user` et `remote_trigger`. De nombreuses améliorations ont également été apportées à l'API, à la sécurité et à l'infrastructure du projet.

### Évolutions fonctionnelles
- Ajout de l'outil `computer_use` permettant d'interagir avec le système d'exploitation (capture d'écran, clics de souris, saisie de texte) via `xdotool` et `ImageMagick`.
- Implémentation d'un marché de plugins distant permettant d'installer et de gérer des plugins pour étendre les fonctionnalités de claw-code-go. Une commande CLI `claw-code-go plugin install` est disponible.
- Implémentation complète des outils `ask_user` (avec options structurées) et `remote_trigger`.
- Ajout de la prise en charge des fournisseurs AWS Bedrock, Azure Foundry et Vertex AI.
- Ajout de la possibilité de spécifier un effort de raisonnement par modèle via l'API.
- Ajout de la possibilité de passer des variables d'environnement à l'exécution de commandes Bash.
- Ajout d'une commande CLI `claw-code-go timeline` pour afficher l'historique des sessions.
- Ajout d'une commande CLI `claw-code-go store` pour gérer les plugins.

### Évolutions techniques
- Refactorisation importante du code, notamment pour l'API et la gestion des erreurs.
- Ajout de l'exportation OTLP/gRPC pour la télémétrie.
- Amélioration de la gestion des timeouts et des erreurs HTTP.
- Mise en place d'un système de vérification de signature pour les plugins.
- Utilisation de cosign pour la signature des plugins.
- Ajout d'un registre de modèles en direct avec actualisation asynchrone.
- Amélioration de la sécurité, notamment concernant la classification des LLM et l'authentification SSE.
- Refonte de la structure du README pour mettre en avant les fonctionnalités clés.
- Ajout d'une licence MIT.
- Renommage du chemin du module en `github.com/SocialGouv/claw-code-go`.
- Suppression de la dépendance `goai`.
- Amélioration de la gestion du contexte et de l'annulation des tâches.

### Autres changements
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et les changements d'API.
- Ajout de tests unitaires et d'intégration pour les nouvelles fonctionnalités.
- Corrections de bugs mineurs et améliorations de la qualité du code.
- Ajout de tests de fumée pour les fournisseurs cloud.
- Ajout de la possibilité de configurer l'URL des moteurs de recherche Brave et DuckDuckGo.
- Ajout de la possibilité de définir un effort de raisonnement par modèle.
- Ajout de la possibilité de surcharger les variables d'environnement pour les fournisseurs externes.
- Amélioration de la gestion des erreurs et des logs.
