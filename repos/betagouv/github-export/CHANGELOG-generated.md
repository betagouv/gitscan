## Changelog : github-export (30 derniers jours)

### Résumé
Les dernières mises à jour de github-export concernent principalement l'amélioration de la robustesse et de la fiabilité du processus de synchronisation et de migration. Des ajustements ont été apportés à la planification des tâches et à la gestion de l'état de la migration. Une correction a également été apportée pour permettre de sauter les issues et les pull requests lors de la migration.

### Évolutions fonctionnelles
- Correction d'un bug permettant de sauter les issues et les pull requests lors de la migration. [#dcac9aa](https://github.com/betagouv/github-export/commit/dcac9aa)
- Modification de la planification de la synchronisation pour qu'elle s'exécute quotidiennement à 2h du matin UTC. [#93035c2](https://github.com/betagouv/github-export/commit/93035c2)

### Évolutions techniques
- Mise à jour de la configuration du workflow `sync-orchestrator.yml` pour optimiser la synchronisation. [#8c89dce](https://github.com/betagouv/github-export/commit/8c89dce)
- Amélioration de la gestion de l'état de la migration dans les workflows GitHub Actions (discovery et batch processing). Les mises à jour visent à assurer un suivi plus précis et une meilleure gestion des erreurs. (commits multiples de github-actions[bot])

### Autres changements
- Aucune information supplémentaire.
