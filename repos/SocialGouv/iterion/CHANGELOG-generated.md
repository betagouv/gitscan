## Changelog : iterion (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, iterion a connu une évolution significative, notamment autour de l'amélioration de l'expérience utilisateur avec une refonte de l'éditeur visuel, l'ajout de nouvelles fonctionnalités pour l'orchestration d'agents d'IA (notamment avec l'intégration de Claude Code), et des optimisations de performance et de fiabilité. De nombreux efforts ont été consacrés à l'amélioration de la robustesse et de la traçabilité des workflows, ainsi qu'à l'ajout de tests complets.

### Évolutions fonctionnelles
- Ajout d'un éditeur visuel amélioré avec :
    - Palette de nœuds préconfigurés avec glisser-déposer.
    - Gestion des connexions et du routage des nœuds.
    - Tri chronologique des nœuds.
    - Vue détaillée des sous-nœuds.
    - Amélioration de l'expérience utilisateur générale.
- Intégration native de Claude Code avec la possibilité de mettre en pause et reprendre l'exécution.
- Possibilité d'exposer des outils via `RegisterClawComputerUse`.
- Ajout d'un outil MCP natif pour Claude Code.
- Implémentation d'un système de routage pour les LLM.
- Amélioration de la gestion des sessions avec la possibilité de reprise après une interruption.
- Ajout d'un système de round robin pour l'exécution des tâches.
- Ajout d'un système de "human in the loop" pour l'amélioration des workflows.
- Ajout d'un système de revue et de correction des workflows.
- Amélioration de la gestion des erreurs et des logs.
- Ajout d'un système de suivi de l'effort de raisonnement des agents.
- Ajout d'un système de cache pour les prompts Anthropic afin de réduire les coûts.

### Évolutions techniques
- Refactorisation du code pour une meilleure organisation et maintenabilité.
- Migration vers le framework Cobra pour la CLI.
- Remplacement de `goai` par `claw-code-go/pkg/api` pour une meilleure intégration avec Claude Code.
- Amélioration de la gestion des dépendances.
- Ajout de tests unitaires, de tests de bout en bout et de tests de fuzzing.
- Amélioration de la couverture des tests.
- Implémentation d'un système de suivi du coût des workflows.
- Ajout d'un exporteur Prometheus pour la surveillance des métriques.
- Amélioration de la gestion des erreurs et des logs.
- Consolidation du code Go sous le package `pkg/`.
- Utilisation de `sync.Once` pour optimiser la résolution des modèles.
- Amélioration de la gestion des fichiers statiques.
- Mise à jour des dépendances.

### Autres changements
- Documentation mise à jour avec de nouveaux exemples et des guides d'utilisation.
- Nettoyage du code et suppression du code mort.
- Ajout de commentaires et de documentation au code.
- Correction de bugs mineurs.
- Ajout d'un fichier `.gitignore` pour ignorer les fichiers inutiles.
- Amélioration de la configuration du CI/CD.
- Ajout d'un plan de reprise pour les fonctionnalités différées.
- Ajout d'un plan de route pour les prochaines sessions de développement.
- Suppression de fonctionnalités obsolètes.
- Mise à jour de la documentation pour refléter les changements apportés au code.
- Ajout de tests de performance et de chaos injection.
- Ajout d'un système de suivi de la parité des fonctionnalités.
- Ajout de tests de couverture pour les fonctionnalités.
- Ajout d'un système de gestion des versions des artefacts.
- Amélioration de la gestion des erreurs et des logs.
- Ajout d'un système de gestion des configurations.
- Ajout d'un système de gestion des secrets.
- Ajout d'un système de gestion des utilisateurs et des permissions.
- Ajout d'un système de gestion des notifications et des alertes.
- Ajout d'un système de gestion de la sécurité et de la conformité.
- Ajout d'un système de gestion des données et des schémas.
- Ajout d'un système de gestion de la collaboration et du workflow.
- Ajout d'un système de gestion de l'intelligence artificielle et du NLP.
