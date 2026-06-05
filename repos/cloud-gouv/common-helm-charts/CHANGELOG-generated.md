## Changelog : common-helm-charts (30 derniers jours, au 4 juin 2026)

### Résumé
Ce changelog présente les récentes améliorations apportées aux charts Helm de common-helm-charts. Les évolutions se concentrent sur l'ajout de nouveaux charts (pgbench, dashboard HAProxy), l'amélioration des charts existants (Argo Secrets, pgbench) et la correction de bugs pour une meilleure stabilité et sécurité.

### Évolutions fonctionnelles
- Ajout d'un chart pour déployer un benchmark `pgbench` pour PostgreSQL, permettant de tester les performances de la base de données. [#18](https://github.com/cloud-gouv/common-helm-charts/pull/18)
- Ajout d'un dashboard HAProxy pour Grafana, offrant une visualisation des statistiques du load balancer. [#20](https://github.com/cloud-gouv/common-helm-charts/pull/20)
- Amélioration du chart `pgbench` avec externalisation des scripts de benchmark et correction du `securityContext` pour permettre l'écriture des résultats sur le système de fichiers. [#21](https://github.com/cloud-gouv/common-helm-charts/pull/21)
- Correction d'un problème de provisioning des secrets dans Argo. [#10](https://github.com/cloud-gouv/common-helm-charts/pull/10)

### Évolutions techniques
- Correction d'une condition dans le template pour gérer correctement les objets `$data` vides. [#24](https://github.com/cloud-gouv/common-helm-charts/pull/24)
- Correction du chart pgbench pour ne demander aucune limite de CPU.
- Correction du chart pgbench pour spécifier le namespace de déploiement.
- Ajout de PodSecurityContext et securityContext pour le chart pgbench.

### Autres changements
- Ajout d'une variable `extraenv` pour permettre la configuration d'environnements supplémentaires.
- Documentation améliorée pour le chart `pgbench`.
- Ajout d'un chart de base.
- Correction de la gestion du namespace dans le chart Argo Secrets.
- Ajout d'une condition RBAC et d'un job pour le chart Argo Secrets.
