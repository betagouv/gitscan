## Changelog : common-helm-charts (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les charts Helm de common-helm-charts ont bénéficié d'améliorations significatives en termes de monitoring et de tests de performance. Des tableaux de bord Grafana ont été ajoutés pour Coturn et pour le monitoring de machines virtuelles, et des tests de stress ont été intégrés pour PostgreSQL. Des corrections ont également été apportées pour améliorer la stabilité et la configuration des charts existants.

### Évolutions fonctionnelles
- Ajout d'un tableau de bord Grafana basique pour le serveur Coturn, permettant de visualiser les métriques de performance. [#26](https://github.com/cloud-gouv/common-helm-charts/pull/26)
- Ajout d'un tableau de bord Grafana pour afficher les métriques d'une machine virtuelle. [#26](https://github.com/cloud-gouv/common-helm-charts/pull/26)
- Intégration de tests de stress FIO aux benchmarks PostgreSQL pour évaluer les performances en conditions de charge. [#22](https://github.com/cloud-gouv/common-helm-charts/pull/22)
- Ajout de l'ID et de l'empreinte (fingerprint) des alertes Matrix dans les templates pour une identification plus facile. [#28](https://github.com/cloud-gouv/common-helm-charts/pull/28)

### Évolutions techniques
- Refactorisation des tableaux de bord Grafana pour éviter la multiplication des ConfigMaps et simplifier la gestion. [#25](https://github.com/cloud-gouv/common-helm-charts/pull/25)
- Correction d'une condition dans les tableaux de bord Grafana pour gérer correctement les cas où l'objet `$data` est vide. [#24](https://github.com/cloud-gouv/common-helm-charts/pull/24)
- Amélioration de la configuration des tests PostgreSQL en permettant la variation des tailles de blocs et des modes de lecture/écriture.
- Correction de la gestion des namespaces dans le provisioning des secrets, limitant à un seul namespace. [#17](https://github.com/cloud-gouv/common-helm-charts/pull/17)
- Ajout de variables d'environnement supplémentaires pour une configuration plus flexible.

### Autres changements
- Ajout d'un nouveau chart. [#35ba62e](https://github.com/cloud-gouv/common-helm-charts/commit/35ba62e118018068955941143239571593885374)
- Ajout d'une condition RBAC et d'un job pour le provisioning des secrets. [#17](https://github.com/cloud-gouv/common-helm-charts/pull/17)
