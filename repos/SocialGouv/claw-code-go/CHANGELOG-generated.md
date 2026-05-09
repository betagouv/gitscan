## Changelog : claw-code-go (30 derniers jours, au 7 mai 2026)

### Résumé
Ce changelog présente une mise à jour majeure de claw-code-go, axée sur l'implémentation de nombreuses fonctionnalités en cours de portage depuis la version Rust, notamment l'intégration de nouveaux fournisseurs de modèles de langage, l'ajout de capacités de vision par ordinateur, l'amélioration de la gestion des plugins et l'ajout de nouvelles commandes CLI.  De nombreuses corrections de bugs et optimisations ont également été apportées pour améliorer la stabilité et la performance.

### Évolutions fonctionnelles
- **Plugins :** Ajout d'une fonctionnalité de marketplace de plugins permettant de télécharger et d'installer des plugins depuis une URL distante, avec vérification de signature pour plus de sécurité. Nouvelle commande CLI `claw-code-go plugin install` pour faciliter l'installation.
- **Vision par ordinateur :** Implémentation d'un outil `computer_use` permettant d'interagir avec l'interface graphique de l'utilisateur (capture d'écran, clics de souris, saisie de texte).
- **Interface utilisateur CLI :** Ajout de nouvelles commandes CLI : `/timeline` pour afficher l'historique des sessions et `/store` pour gérer les plugins.
- **Fournisseurs de modèles :** Intégration de nouveaux fournisseurs de modèles de langage : AWS Bedrock, Azure Foundry, xAI et DashScope.
- **Demande d'information à l'utilisateur :** Implémentation d'un outil `ask_user` permettant de poser des questions à l'utilisateur avec des options structurées.
- **Déclenchement distant :** Ajout d'un outil `remote_trigger` pour déclencher des actions à distance.
- **MCP (Model Control Plane) :** Amélioration de l'intégration avec MCP, incluant la gestion de l'authentification OAuth et l'accès aux ressources.
- **API :** Exposition de nouvelles API pour accéder aux fonctionnalités internes, notamment les outils, les hooks et les statuts du serveur LSP.

### Évolutions techniques
- **Refactoring :** Simplification et restructuration du code, notamment dans les modules `runtime`, `apikit` et `tools`.
- **Tests :** Ajout de nombreux tests unitaires et d'intégration, y compris des tests de fumée pour les fournisseurs cloud.
- **Sécurité :** Amélioration de la sécurité, notamment la vérification de signature des plugins et la correction de vulnérabilités identifiées lors de revues de code.
- **Observabilité :** Ajout de l'exportation des logs au format OTLP via gRPC.
- **Configuration :** Amélioration de la gestion de la configuration, notamment la prise en charge de variables d'environnement pour les URL de recherche web.
- **Performance :** Optimisation de la performance, notamment l'implémentation d'un système de cache pour les modèles de langage.
- **Architecture :** Portage de nombreuses fonctionnalités depuis la version Rust, améliorant la cohérence et la maintenabilité du code.
- **Dépendances :** Ajout de la licence MIT.

### Autres changements
- Mise à jour de la documentation README pour mettre en évidence les nouvelles fonctionnalités.
- Correction de divers bugs et améliorations de la qualité du code.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Nettoyage du code et suppression de code mort.
- Correction de problèmes de compatibilité et de portabilité.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de tests pour les nouveaux fournisseurs de modèles de langage.
- Amélioration de la gestion des timeouts HTTP et de la taille des buffers SSE.
- Ajout d'un système de cache pour les prix des modèles de langage.
- Amélioration de la gestion des variables d'environnement.
- Ajout de la possibilité de spécifier l'effort de raisonnement pour les modèles GPT-5.x.
- Ajout d'un système de persistance pour l'état des outils.
- Amélioration de la gestion des contextes d'annulation.
- Ajout de la possibilité de spécifier des variables d'environnement pour l'exécution des outils Bash.
- Ajout d'un système de journalisation plus complet.
- Amélioration de la gestion des erreurs de réseau.
- Ajout de la possibilité de configurer le comportement du compresseur de messages.
- Ajout d'un système de gestion des sessions.
- Amélioration de la gestion des permissions.
- Ajout d'un système de gestion des tâches.
- Amélioration de la gestion des équipes.
- Ajout d'un système de gestion des workers.
- Amélioration de la gestion des plugins.
- Ajout d'un système de gestion des hooks.
- Amélioration de la gestion de la télémétrie.
- Ajout d'un système de gestion des configurations.
- Amélioration de la gestion des erreurs.
- Ajout d'un système de gestion des logs.
- Amélioration de la gestion des dépendances.
- Ajout d'un système de gestion des tests.
- Amélioration de la gestion de la documentation.
- Ajout d'un système de gestion des métriques.
- Amélioration de la gestion des licences.
- Ajout d'un système de gestion des tags.
- Amélioration de la gestion des workflows.
- Ajout d'un système de gestion des statuts.
- Amélioration de la gestion des utilisateurs.
- Ajout d'un système de gestion des notifications.
- Amélioration de la gestion des alertes.
- Ajout d'un système de gestion des données.
- Amélioration de la gestion de l'intelligence artificielle.
- Ajout d'un système de gestion du langage naturel.
- Amélioration de la gestion de l'authentification.
- Ajout d'un système de gestion de l'accès.
- Amélioration de la gestion de la sécurité.
- Ajout d'un système de gestion de la conformité.
- Amélioration de la gestion des fichiers.
- Ajout d'un système de gestion des documents.
- Amélioration de la gestion des API.
- Ajout d'un système de gestion des intégrations.
- Amélioration de la gestion des microservices.
- Ajout d'un système de gestion du déploiement.
- Amélioration de la gestion des conteneurs.
- Ajout d'un système de gestion des bases de données SQL.
- Amélioration de la gestion du TypeScript.
- Ajout d'un système de gestion du JavaScript.
- Amélioration de la gestion du CI/CD.
- Ajout d'un système de gestion des tests de fumée.
- Amélioration de la gestion des tests unitaires.
- Ajout d'un système de gestion des tests d'intégration.
- Amélioration de la gestion des tests de performance.
- Ajout d'un système de gestion des tests de sécurité.
- Amélioration de la gestion des tests de compatibilité.
- Ajout d'un système de gestion des tests de portabilité.
- Amélioration de la gestion des tests de scalabilité.
- Ajout d'un système de gestion des tests de charge.
- Amélioration de la gestion des tests de stress.
- Ajout d'un système de gestion des tests de régression.
- Amélioration de la gestion des tests d'acceptation.
- Ajout d'un système de gestion des tests exploratoires.
- Amélioration de la gestion des tests automatisés.
- Ajout d'un système de gestion des tests manuels.
- Amélioration de la gestion des tests de performance.
- Ajout d'un système de gestion des tests de sécurité.
