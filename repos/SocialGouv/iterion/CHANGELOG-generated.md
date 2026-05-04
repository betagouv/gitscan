## Changelog : iterion (30 derniers jours, au 02 mai 2026)

### Résumé
Ce mois-ci, iterion a connu une évolution majeure avec une refonte de l'éditeur, de l'exécution des workflows et de l'intégration avec les modèles d'IA. L'accent a été mis sur l'amélioration de l'expérience utilisateur, la robustesse du système et l'ajout de nouvelles fonctionnalités comme la gestion des workflows en mode "pause/reprise" et l'intégration de nouveaux outils. De nombreux tests ont été ajoutés pour garantir la qualité et la stabilité du projet.

### Évolutions fonctionnelles
- Ajout d'un SDK TypeScript pour interagir avec l'API iterion via la ligne de commande.
- Amélioration de l'éditeur avec une palette de nœuds, des panneaux latéraux repliables, un inspecteur amélioré et des raccourcis clavier.
- Implémentation de la pause et de la reprise des workflows, permettant de sauvegarder l'état et de continuer plus tard.
- Possibilité de récupérer les journaux d'exécution même après la fin d'un workflow.
- Ajout d'un système de gestion des coûts pour chaque nœud et une vue récapitulative des coûts.
- Intégration de nouveaux outils et modèles d'IA, notamment Claude et GPT-5.5.
- Amélioration de la gestion des erreurs et de la robustesse du système.
- Ajout d'un système de gestion des fichiers et de la configuration.
- Ajout d'un système de gestion des sessions pour les workflows interactifs.
- Ajout d'un système de routage pour les modèles d'IA.

### Évolutions techniques
- Refonte de l'architecture de l'exécution des workflows pour une meilleure gestion des erreurs et des interruptions.
- Migration vers le framework Cobra pour la ligne de commande.
- Amélioration de la gestion des dépendances et des versions.
- Ajout de tests unitaires, d'intégration et de fuzzing pour garantir la qualité du code.
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Utilisation de Worktrees pour l'isolation des exécutions.
- Implémentation d'un système de journalisation plus complet et informatif.
- Utilisation de la bibliothèque `claw-code-go` pour l'intégration avec les modèles d'IA.
- Amélioration de la sécurité avec la gestion des chemins et la validation des entrées.
- Ajout d'un exportateur OTLP/gRPC pour les métriques de performance.

### Autres changements
- Mise à jour de la documentation avec de nouveaux exemples et des guides d'utilisation.
- Ajout d'une licence MIT.
- Correction de nombreuses erreurs et améliorations de la stabilité.
- Nettoyage du code et suppression du code obsolète.
- Amélioration de la configuration et de l'installation.
- Ajout d'un système de gestion des tâches pour automatiser les processus de développement.
- Ajout de tests de couverture pour garantir la qualité du code.
- Mise en place d'un système de CI/CD pour automatiser les déploiements.
