## Changelog : iterion (30 derniers jours, au 2026-04-17)

### Résumé
Ce mois-ci, iterion a connu une évolution significative, axée sur l'amélioration de l'expérience de développement et de l'automatisation des workflows. Les efforts se sont concentrés sur l'intégration de nouveaux agents (Claude Code, Codex), l'amélioration de la robustesse et de la traçabilité des exécutions, et le développement d'un éditeur visuel plus puissant et intuitif. De nombreuses améliorations techniques ont été apportées pour supporter ces nouvelles fonctionnalités et améliorer la qualité globale du code.

### Évolutions fonctionnelles

- **Intégration de nouveaux agents :** Ajout de la délégation vers Claude Code et Codex, permettant d'étendre les capacités d'automatisation d'iterion.
- **Amélioration du workflow de revue et correction :** Implémentation d'un workflow de revue et correction avec double verdict, permettant une validation plus rigoureuse des résultats.
- **Résolution de problèmes de contexte :** Correction d'un problème lié à la fenêtre de contexte de Codex, améliorant sa performance.
- **Reprise d'exécution :** Possibilité de reprendre une exécution interrompue ou annulée, améliorant la résilience du système.
- **Amélioration de l'éditeur visuel :**
    - Ajout d'une bibliothèque de nœuds préconfigurés avec glisser-déposer.
    - Amélioration du routage des connexions entre les nœuds.
    - Ajout d'un panneau de sélection de nœuds.
    - Ajout de la possibilité de créer des groupes de nœuds.
- **Journalisation améliorée :** Affichage des réponses des LLM, des appels aux outils et de l'activité de délégation au niveau d'information.
- **Nouvelle fonctionnalité "run-and-refine" :** Ajout d'une fonctionnalité pour tester itérativement les workflows.

### Évolutions techniques

- **Refactoring de la journalisation :** Standardisation de la journalisation avec `iterlog` dans tous les packages.
- **Refactorisation de l'architecture :**
    - Remplacement de la structure monolithique `Node` par une interface polymorphe.
    - Séparation des backends d'exécution.
    - Extraction de constantes partagées et amélioration de la cohérence du code.
- **Amélioration de la gestion des erreurs :** Ajout de mécanismes de reprise et de gestion des erreurs pour les exécutions déléguées.
- **Tests améliorés :** Ajout de tests de fuzzing, d'injection de chaos et de benchmarks de performance.
- **Migration vers Pnpm :** Migration du gestionnaire de paquets vers Pnpm.
- **Amélioration du CI/CD :** Optimisation du pipeline CI/CD pour les releases.
- **Utilisation de Cobra pour la CLI :** Migration de la CLI vers le framework Cobra pour une meilleure organisation et maintenabilité.
- **Implémentation d'un système de cache pour la découverte des outils.**

### Autres changements

- **Documentation mise à jour :** Ajout d'exemples et de documentation pour les nouvelles fonctionnalités.
- **Nettoyage du code :** Suppression du code mort et des fonctions obsolètes.
- **Correction de bugs mineurs :** Correction de divers bugs et améliorations de la stabilité.
- **Amélioration des logs et des messages d'erreur.**
- **Ajout de tests unitaires et d'intégration.**
- **Mise à jour des dépendances.**
