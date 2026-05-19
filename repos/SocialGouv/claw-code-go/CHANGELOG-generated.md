## Changelog : claw-code-go (30 derniers jours, au 18 mai 2026)

### Résumé
Les 30 derniers jours ont été marqués par une refonte importante de l'écosystème des outils et plugins de claw-code-go. De nouvelles fonctionnalités ont été ajoutées pour l'automatisation, la sécurité et l'intégration avec des services externes comme AWS Bedrock, Azure Foundry et Vertex AI. L'ajout d'un marché de plugins distant et d'outils d'interaction utilisateur (ask_user, remote_trigger) renforce la flexibilité et l'extensibilité de la plateforme. Des améliorations significatives ont également été apportées à la gestion des erreurs, à la performance et à la documentation.

### Évolutions fonctionnelles
- Ajout d'un nouveau tool `computer_use` permettant l'automatisation d'actions sur l'interface graphique (clics, saisie de texte, captures d'écran) sous Linux.
- Implémentation d'un marché de plugins distant permettant d'installer des plugins depuis une URL spécifiée, avec vérification de signature.
- Ajout des outils `ask_user` et `remote_trigger` pour interagir avec l'utilisateur et déclencher des actions externes.
- Intégration de nouveaux fournisseurs de modèles de langage : AWS Bedrock, Azure Foundry et Google Vertex AI.
- Possibilité d'utiliser des modèles OpenAI avec différents niveaux d'effort de raisonnement (`reasoning_effort`).
- Ajout d'un outil `timeline` en ligne de commande pour visualiser l'historique des sessions.
- Ajout d'un outil `store` en ligne de commande pour gérer les plugins.

### Évolutions techniques
- Refactorisation importante du code pour améliorer la structure et la maintenabilité.
- Ajout de tests unitaires et d'intégration pour couvrir les nouvelles fonctionnalités.
- Mise en place d'un système de cache pour le registre des modèles de langage.
- Amélioration de la gestion des erreurs et des timeouts.
- Implémentation de l'exportation des logs au format OTLP/gRPC pour une meilleure observabilité.
- Utilisation de cosign pour la vérification de la signature des plugins.
- Amélioration de la sécurité avec la fermeture de plusieurs vulnérabilités identifiées lors de revues de code.
- Refonte du système d'authentification OAuth pour MCP avec support de PKCE.
- Ajout de la gestion des variables d'environnement pour les fournisseurs de modèles de langage.
- Suppression de la dépendance à la librairie `goai`.
- Modification du chemin du module pour faciliter l'importation distante.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés.
- Restructuration du fichier README pour mettre en avant les principales fonctionnalités.
- Ajout d'une matrice de parité pour suivre l'état d'avancement des fonctionnalités.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout d'une option pour désactiver la vérification de signature des plugins.
- Ajout d'une option pour autoriser l'utilisation du marché de plugins en HTTPS non sécurisé.
- Amélioration des messages d'erreur pour faciliter le débogage.
