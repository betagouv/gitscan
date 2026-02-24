## Changelog : github-export (30 derniers jours)

### Résumé
Les dernières mises à jour de github-export se concentrent sur l'amélioration de la fiabilité et de l'efficacité du processus de migration. Des ajustements ont été apportés à l'ordonnanceur de synchronisation et des correctifs ont été implémentés pour ignorer les issues et les pull requests lors de la migration. De nombreuses mises à jour concernent également la gestion de l'état de la migration dans les workflows GitHub Actions.

### Évolutions fonctionnelles
- Correction d'un bug qui empêchait de sauter correctement les issues et les pull requests lors de la migration (#dcac9aa).
- L'ordonnanceur de synchronisation a été modifié pour s'exécuter quotidiennement à 2h00 UTC (#93035c2).

### Évolutions techniques
- Mise à jour du workflow `sync-orchestrator.yml` (#8c89dce).
- Amélioration de la mise à jour de l'état de la migration après le traitement par lots et la découverte dans les workflows GitHub Actions (plusieurs commits).

### Autres changements
- Aucune information supplémentaire.
