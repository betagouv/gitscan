## Changelog : kube-dev (30 derniers jours)

### Résumé
Ce changelog présente les récentes mises à jour apportées à l'infrastructure Kubernetes gérée par ArgoCD. Les changements concernent principalement l'amélioration de la gestion des données Matomo, avec l'ajout d'un nouveau job pour l'export vers PostgreSQL et des ajustements de ressources pour optimiser son fonctionnement. Des corrections ont également été apportées à la configuration de PostgreSQL.

### Évolutions fonctionnelles
- Ajout d'un job pour exporter les données Matomo vers PostgreSQL via JDMA (#4120d23).
- Amélioration de la configuration du job `matomo-to-pg` avec l'ajout de la variable d'environnement `NODE_OPTIONS` (#8f9be4b).
- Ajustement des limites de ressources allouées au job `matomo-to-pg` pour une meilleure performance (#d494f98).

### Évolutions techniques
- Mise à jour de l'image du job cron Matomo vers la version `sync` (#239231a).
- Corrections diverses concernant la configuration de PostgreSQL (#545be71, #0289773, #bc1f00c, #ffe6b27, #efceecb, #1f7e52d, #479d5e7, #83c8ec8).
- Correction d'un problème avec JDMA (#980763f).
