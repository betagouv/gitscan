## Changelog : iterion (30 derniers jours, au 2026-04-16)

### Résumé
Les dernières semaines ont été marquées par une refonte majeure de l'éditeur visuel, avec l'ajout de nouvelles fonctionnalités de manipulation de nœuds, de gestion des flux de travail et d'intégration d'agents d'IA.  Des améliorations significatives ont également été apportées à l'exécution des workflows, notamment la gestion des erreurs, la reprise après interruption et l'intégration de nouveaux outils. Enfin, l'infrastructure de test a été renforcée avec l'ajout de tests de fuzzing, d'injection de chaos et de benchmarks de performance.

### Évolutions fonctionnelles
- **Éditeur visuel :**
    - Ajout d'une bibliothèque de nœuds préconfigurés avec glisser-déposer.
    - Amélioration du routage des connexions entre les nœuds.
    - Ajout de la possibilité de grouper visuellement les nœuds.
    - Ajout d'un panneau latéral pour l'édition des nœuds.
    - Possibilité de trier les nœuds chronologiquement.
- **Workflow :**
    - Ajout d'un mode "round robin" pour exécuter des tâches en parallèle.
    - Ajout d'un mécanisme de reprise après échec pour les workflows interrompus.
    - Implémentation d'un système de suivi du coût des workflows.
    - Ajout d'un système de revue et de correction des workflows.
- **Intégration d'agents :**
    - Intégration de Claude Code et Codex pour l'exécution de tâches.
    - Streaming des activités des agents (entrées, sorties, appels d'outils).
    - Ajout de la possibilité de déléguer des tâches à des agents.
- **Documentation :**
    - Ajout d'exemples d'utilisation de l'éditeur et des workflows.
    - Mise à jour de la documentation sur l'intégration d'agents.

### Évolutions techniques
- **Refactoring :**
    - Standardisation de la journalisation avec `iterlog`.
    - Refonte de l'architecture de l'exécution des workflows.
    - Remplacement de la structure `Node` monolithique par une interface polymorphe.
    - Migration vers le framework Cobra pour la CLI.
- **Tests :**
    - Ajout de tests de fuzzing, d'injection de chaos et de benchmarks de performance.
    - Amélioration de la couverture des tests d'intégration.
    - Ajout de tests e2e live.
- **Infrastructure :**
    - Mise à jour des dépendances.
    - Amélioration du processus de CI/CD.
    - Utilisation de `taskfile` pour la gestion des tâches.
- **Autres :**
    - Utilisation de `corepack` et `token-bureau` pour la gestion des versions de Node.js.
    - Ajout de la prise en charge de WebSocket pour la surveillance des fichiers.

### Autres changements
- Ajout de la documentation pour la fonction `run-and-refine`.
- Correction de bugs mineurs et améliorations de la stabilité.
- Nettoyage du code et suppression du code mort.
- Amélioration des messages de log.
- Ajout de commentaires et de documentation au code.
