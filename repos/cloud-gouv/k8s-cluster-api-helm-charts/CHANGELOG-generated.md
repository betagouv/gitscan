## Changelog : k8s-cluster-api-helm-charts (30 derniers jours, au 16 avril 2026)

### Résumé
Cette version apporte des améliorations à la gestion des CIDR, des volumes snapshot, des secrets externes et des règles de sécurité pour les nœuds worker. Des corrections ont également été apportées pour permettre des configurations plus flexibles et résoudre des problèmes de comportement inattendu.

### Évolutions fonctionnelles
- **Sécurité des nœuds worker:** Possibilité d'injecter des règles de sécurité supplémentaires (Security Groups) assignées aux nœuds worker via la PR [#76](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/76).
- **Gestion des secrets externes:** Correction des noms de clés dans la gestion des secrets externes [#77](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/77) et [#77](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/77).
- **Volumes Snapshot:** Désactivation par défaut des snapshots de volumes, avec la possibilité de les activer via une configuration dédiée [#78](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/78).
- **Gestion des NodePools:** Correction d'un problème empêchant la configuration correcte des NodePools sans contenu spécifique [#73](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/73).

### Évolutions techniques
- **Gestion des CIDR:** Corrections et améliorations de la gestion des CIDR, incluant des tests et des ajustements pour assurer un comportement correct [#74](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/74), [#75](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/75) et [#79](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/79).
- **Suppression de hooks bloquants:** Suppression de hooks qui empêchaient les modifications des secrets [#72](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/72).

### Autres changements
- Amélioration des tests pour la gestion des CIDR.
- Correction de tests unitaires.
