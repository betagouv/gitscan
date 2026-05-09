## Changelog : common-helm-charts (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, le projet a vu l'ajout d'un nouveau chart pour exécuter des benchmarks sur PostgreSQL (pgbench-job), ainsi que des améliorations concernant l'utilisation de secrets externes et la publication des charts en OCI. Des corrections ont également été apportées pour améliorer la sécurité et la stabilité des charts existants.

### Évolutions fonctionnelles
- Ajout d'un chart `pgbench-job` permettant d'exécuter des tests de performance sur une instance PostgreSQL. [#5b21c30](https://github.com/cloud-gouv/common-helm-charts/commit/5b21c30)
- Possibilité d'utiliser des secrets externes avec les charts, offrant une plus grande flexibilité dans la gestion des informations sensibles. [#15](https://github.com/cloud-gouv/common-helm-charts/pull/15)
- Correction d'un problème de déverrouillage du chart `restic`, améliorant sa fiabilité. [#13](https://github.com/cloud-gouv/common-helm-charts/pull/13)

### Évolutions techniques
- Mise en place d'un workflow de publication des charts au format OCI lors des releases. [#12](https://github.com/cloud-gouv/common-helm-charts/pull/12)
- Amélioration de la configuration de sécurité (securityContext) du chart `pgbench-job` pour permettre l'écriture des résultats sur le système de fichiers. [#10b8705](https://github.com/cloud-gouv/common-helm-charts/commit/10b8705) et [#73b0175](https://github.com/cloud-gouv/common-helm-charts/commit/73b0175)
- Suppression d'une limite CPU inutile dans un chart. [#11](https://github.com/cloud-gouv/common-helm-charts/pull/11)
- Correction du nom de l'application dans le chart `Copier`. [#3273416](https://github.com/cloud-gouv/common-helm-charts/commit/3273416)

### Autres changements
- Documentation du chart `pgbench-job`. [#450236b](https://github.com/cloud-gouv/common-helm-charts/commit/450236b)
- Nettoyage du code et des workflows CI. [#621ba03](https://github.com/cloud-gouv/common-helm-charts/commit/621ba03)
- Mise à jour de l'index de documentation et des packages. [#d567677](https://github.com/cloud-gouv/common-helm-charts/commit/d567677)
