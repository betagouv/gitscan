## Changelog : github-export (30 derniers jours, au 24 mai 2026)

### Résumé
Les récentes mises à jour de github-export se concentrent principalement sur l'amélioration de la gestion de l'état des migrations par lots et des découvertes, notamment via les workflows GitHub Actions. Une mise à jour du workflow `sync-orchestrator.yml` a également été effectuée.

### Évolutions techniques
- Amélioration de la mise à jour de l'état de la migration après le traitement par lots et la découverte grâce aux workflows GitHub Actions. Ces mises à jour concernent les workflows `migrate-batch.yml` et `sync-orchestrator.yml`.
- Mise à jour du workflow `sync-orchestrator.yml` pour optimiser la synchronisation. [#6c0dc88](https://github.com/betagouv/github-export/commit/6c0dc88)

### Autres changements
- Ajustements internes pour la gestion de l'état des migrations (commits automatisés par `github-actions[bot]`). Ces changements visent à améliorer la fiabilité et la robustesse du processus de migration.
