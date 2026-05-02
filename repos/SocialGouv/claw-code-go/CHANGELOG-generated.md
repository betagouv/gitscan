## Changelog : claw-code-go (30 derniers jours, au 30 avril 2026)

### Résumé
Ce changelog couvre une période d'intense développement sur claw-code-go, avec une concentration majeure sur l'implémentation de fonctionnalités en cours de portage depuis l'implémentation Rust originale. Les efforts se sont concentrés sur l'ajout de nouveaux outils, l'amélioration de l'intégration avec divers fournisseurs de modèles de langage, l'amélioration de la sécurité et la correction de nombreux bugs pour atteindre la parité avec la version Rust. De nouvelles fonctionnalités de gestion des plugins et d'interface utilisateur ont également été introduites.

### Évolutions fonctionnelles
- Ajout d'un outil `computer_use` permettant d'interagir avec le système d'exploitation (capture d'écran, clics de souris, saisie de texte) via `xdotool` et `ImageMagick`.
- Implémentation d'un marché de plugins distant avec vérification de signature pour une installation sécurisée. Nouvelle commande CLI `claw-code-go plugin install`.
- Ajout d'implémentations fonctionnelles des outils `ask_user` (avec options structurées) et `remote_trigger`.
- Intégration de fournisseurs de modèles de langage réels : AWS Bedrock, Azure Foundry et Vertex AI.
- Ajout de la prise en charge de DashScope et xAI.
- Amélioration de l'interface utilisateur avec une commande `/timeline` pour visualiser l'historique des sessions et une commande `/lineage` pour suivre l'origine des données.
- Ajout d'une commande `/store` pour gérer les plugins.
- Prise en charge de l'authentification OAuth pour les fournisseurs de modèles de langage.
- Ajout de la possibilité de spécifier des variables d'environnement pour l'exécution de commandes bash.
- Ajout d'une fonctionnalité de recherche web avec la possibilité de personnaliser les URL de Brave et DuckDuckGo.

### Évolutions techniques
- Refactorisation importante du code pour améliorer la structure et la maintenabilité.
- Ajout de tests unitaires et d'intégration pour assurer la qualité du code.
- Mise en place d'un système de journalisation avec OpenTelemetry (OTLP) via gRPC et HTTP.
- Amélioration de la gestion des erreurs et des timeouts HTTP.
- Utilisation de SHA-256 pour la vérification de l'intégrité des plugins téléchargés.
- Implémentation d'un système de cache pour les prix des modèles de langage.
- Ajout de la prise en charge de la compression des messages pour optimiser les performances.
- Amélioration de la sécurité avec la fermeture de plusieurs vulnérabilités identifiées lors de revues de code.
- Mise à jour de la gestion des contextes pour assurer la propagation correcte de la cancellation.
- Refonte de la gestion des configurations et des paramètres.
- Ajout de tests de performance pour identifier les goulots d'étranglement.
- Renommage du chemin du module en `github.com/SocialGouv/claw-code-go` pour faciliter l'importation.

### Autres changements
- Mise à jour de la documentation avec des exemples d'utilisation et des informations sur les nouvelles fonctionnalités.
- Ajout d'un logo ASCII art à l'interface utilisateur en mode texte.
- Amélioration de la lisibilité du code avec des commentaires et une mise en forme cohérente.
- Correction de plusieurs bugs mineurs et améliorations de la stabilité.
- Suppression de code mort et simplification de certaines parties du code.
- Ajout d'un système de gestion des versions pour les plugins.
- Ajout d'une fonctionnalité de recherche de plugins.
- Amélioration de la gestion des dépendances.
