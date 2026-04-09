## Changelog : iterion (30 derniers jours, au 2026-04-09)

### Résumé
Ce mois-ci, iterion a connu une évolution significative, notamment grâce à l'ajout d'un éditeur visuel pour la création de workflows, des améliorations de la robustesse et de la flexibilité de l'exécution des workflows, et des optimisations de l'intégration avec les modèles de langage (LLM). L'accent a été mis sur l'amélioration de l'expérience développeur et la préparation du terrain pour des fonctionnalités plus avancées.

### Évolutions fonctionnelles
- Ajout d'un éditeur visuel avec :
    - Glisser-déposer de nœuds depuis une bibliothèque.
    - Création automatique de documents pour démarrer rapidement.
    - Connexions visuelles entre les nœuds.
    - Palette de sous-nœuds avec glisser-déposer.
    - Routage intelligent des connexions pour une meilleure lisibilité.
    - Sélection et regroupement visuel des nœuds.
- Amélioration de la gestion des erreurs et reprise des exécutions interrompues.
- Possibilité de visualiser les réponses des LLM, les appels d'outils et l'activité de délégation au niveau d'information dans les logs.
- Ajout de la gestion de templates et de références de templates.
- Amélioration de la gestion des outils avec fingerprinting de schéma MCP et politiques d'utilisation par nœud.
- Ajout d'un support pour les routeurs LLM.
- Possibilité de contrôler l'auto-complétion des réponses.

### Évolutions techniques
- Refactorisation de l'architecture du runtime pour une meilleure modularité et extensibilité.
- Migration de la CLI vers le framework Cobra pour une meilleure organisation et gestion des commandes.
- Amélioration de la persistance des données (index des artefacts, résilience des checkpoints).
- Utilisation de WebSocket pour la surveillance des fichiers dans l'éditeur, permettant une mise à jour en temps réel.
- Remplacement de certaines structures monolithiques par des interfaces polymorphes pour une meilleure flexibilité.
- Amélioration des tests avec l'ajout de tests de fuzzing, de chaos injection et de benchmarks de performance.
- Mise à jour des dépendances et de l'infrastructure CI/CD.
- Implémentation de la continuité de session pour les nœuds de délégation.

### Autres changements
- Amélioration de la documentation avec des exemples plus complets et une tonalité plus conviviale.
- Nettoyage du code et suppression du code mort ou obsolète.
- Ajout de commentaires et d'explications pour faciliter la compréhension du code.
- Mise en place d'un système de versioning plus clair.
- Configuration de l'environnement de développement avec des outils comme direnv et corepack.
- Ajout de tests e2e live pour valider le bon fonctionnement des nouvelles fonctionnalités.
