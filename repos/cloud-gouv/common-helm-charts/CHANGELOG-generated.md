## Changelog : common-helm-charts (30 derniers jours, au 2026-05-13)

### Résumé
Ce mois-ci, le projet s'est enrichi d'un nouveau chart permettant de réaliser des benchmarks de performance sur PostgreSQL grâce à pgbench.  Une amélioration a également été apportée pour permettre l'utilisation de secrets externes, offrant ainsi plus de flexibilité dans la configuration des applications.

### Évolutions fonctionnelles
- Ajout du chart `pgbench-job` pour exécuter des tests de performance sur PostgreSQL. Ce chart permet de mesurer la capacité de votre instance PostgreSQL à gérer une charge de travail spécifique. [#18](https://github.com/cloud-gouv/common-helm-charts/pull/18)
- Possibilité d'utiliser des secrets externes avec les charts, augmentant la flexibilité et la sécurité de la gestion des informations sensibles. [#15](https://github.com/cloud-gouv/common-helm-charts/issues/15)

### Évolutions techniques
- Amélioration de la configuration de sécurité (securityContext) du chart `pgbench-job` pour permettre à l'utilisateur postgres d'écrire les résultats des benchmarks sur le système de fichiers.
- Spécification du namespace pour le déploiement du chart `pgbench-job`.
- Correction de la configuration du `securityContext` pour le déploiement `pgbench-job`.

### Autres changements
- Ajout de documentation pour le chart `pgbench-job`.
- Corrections mineures et ajustements pour le chart `pgbench-job` afin d'optimiser son fonctionnement.
