## Changelog : claw-code-go (30 derniers jours, au 15 mai 2026)

### Résumé
Les 30 derniers jours ont été marqués par une avancée significative dans les fonctionnalités de claw-code-go, notamment avec l'ajout de la prise en charge de plugins via un marché distant, l'implémentation d'outils d'interaction avec l'utilisateur et de déclenchement distant, ainsi que l'intégration de nouveaux fournisseurs de modèles de langage (Bedrock, Vertex, Foundry). Des améliorations ont également été apportées à la sécurité, à la gestion des erreurs et à l'observabilité du projet.

### Évolutions fonctionnelles
- Ajout de la possibilité d'installer des plugins depuis un marché distant avec vérification de signature. [#8db196f](https://github.com/SocialGouv/claw-code-go/commit/8db196f)
- Implémentation des outils `ask_user` et `remote_trigger` pour interagir avec l'utilisateur et déclencher des actions à distance. [#d438b99](https://github.com/SocialGouv/claw-code-go/commit/d438b99)
- Intégration de nouveaux fournisseurs de modèles de langage : AWS Bedrock, Azure Foundry et Google Vertex AI. [#3ce3cea](https://github.com/SocialGouv/claw-code-go/commit/3ce3cea)
- Ajout d'un outil `computer_use` permettant d'automatiser des actions sur l'interface graphique (capture d'écran, clics, saisie de texte) sous Linux. [#5985640](https://github.com/SocialGouv/claw-code-go/commit/5985640)
- Possibilité d'utiliser des images comme source de données pour les modèles de langage via l'ajout du type `ImageSource`. [#52392bd](https://github.com/SocialGouv/claw-code-go/commit/52392bd)
- Ajout de commandes CLI pour gérer les sessions (`/timeline`) et afficher l'historique (`/lineage`). [#05756be](https://github.com/SocialGouv/claw-code-go/commit/05756be)

### Évolutions techniques
- Refactorisation du code pour améliorer la structure et la maintenabilité.
- Mise en place d'un système de gestion des erreurs plus robuste avec des erreurs typées pour faciliter la gestion des erreurs et les tentatives de relance. [#2574d7f](https://github.com/SocialGouv/claw-code-go/commit/2574d7f)
- Amélioration de la gestion des timeouts HTTP et de la taille des buffers SSE. [#cdc3f98](https://github.com/SocialGouv/claw-code-go/commit/cdc3f98)
- Ajout d'un système de journalisation basé sur OpenTelemetry avec exporteurs OTLP/HTTP et gRPC. [#f53ccbb](https://github.com/SocialGouv/claw-code-go/commit/f53ccbb)
- Implémentation d'un système de hooks pour étendre les fonctionnalités du projet. [#b5bbbd2](https://github.com/SocialGouv/claw-code-go/commit/b5bbbd2)
- Ajout de tests unitaires et d'intégration pour améliorer la qualité du code.
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés au projet.
- Renommage du module en `github.com/SocialGouv/claw-code-go` pour faciliter l'importation. [#ef4a4cd](https://github.com/SocialGouv/claw-code-go/commit/ef4a4cd)

### Autres changements
- Ajout d'une licence MIT. [#4bab540](https://github.com/SocialGouv/claw-code-go/commit/4bab540)
- Restructuration de la documentation README pour mettre en avant les principales fonctionnalités. [#146c3c0](https://github.com/SocialGouv/claw-code-go/commit/146c3c0)
- Amélioration de la gestion des variables d'environnement pour les fournisseurs de modèles de langage. [#1692325](https://github.com/SocialGouv/claw-code-go/commit/1692325)
- Correction de bugs et améliorations de la performance.
- Mise à jour des dépendances.
