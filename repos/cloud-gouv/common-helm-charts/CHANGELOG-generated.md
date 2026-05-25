## Changelog : common-helm-charts (30 derniers jours, au 2026-05-19)

### Résumé
Ce changelog présente l'ajout d'un nouveau chart Helm pour effectuer des benchmarks sur PostgreSQL avec pgbench. Ce chart permet de mesurer les performances de votre instance PostgreSQL et d'identifier d'éventuels goulots d'étranglement. Des améliorations ont également été apportées à la configuration et à la sécurité de ce chart.

### Évolutions fonctionnelles
- Ajout du chart `pgbench-job` pour exécuter des tests de performance avec pgbench sur une instance PostgreSQL. [#18](https://github.com/cloud-gouv/common-helm-charts/pull/18)
- Le chart `pgbench-job` permet de spécifier le namespace de déploiement. [#20](https://github.com/cloud-gouv/common-helm-charts/pull/20)
- Documentation ajoutée pour le chart `pgbench-job`. [#18](https://github.com/cloud-gouv/common-helm-charts/pull/18)

### Évolutions techniques
- Externalisation des scripts shell utilisés par `pgbench-job` pour une meilleure maintenabilité. [#21](https://github.com/cloud-gouv/common-helm-charts/pull/21)
- Configuration du `securityContext` pour le déploiement `pgbench-job` afin de permettre à l'utilisateur postgres d'écrire les résultats sur le système de fichiers. [#18](https://github.com/cloud-gouv/common-helm-charts/pull/18)
- Suppression de la limite de CPU par défaut pour `pgbench-job` afin d'optimiser les performances des benchmarks. [#18](https://github.com/cloud-gouv/common-helm-charts/pull/18)

### Autres changements
- Corrections mineures et améliorations de la configuration du chart `pgbench-job`. [#18](https://github.com/cloud-gouv/common-helm-charts/pull/18)
- Travaux de développement. [#19](https://github.com/cloud-gouv/common-helm-charts/pull/19)
