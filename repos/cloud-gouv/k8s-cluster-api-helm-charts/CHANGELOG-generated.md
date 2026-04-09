## Changelog : k8s-cluster-api-helm-charts (30 derniers jours, au 8 avril 2026)

### Résumé
Ce mois-ci, les charts Helm pour Cluster API ont bénéficié d'améliorations axées sur la flexibilité et la correction de bugs. Les utilisateurs peuvent désormais injecter des règles de sécurité supplémentaires pour les nœuds worker, et des corrections ont été apportées pour permettre la modification des secrets et la gestion des configurations de nœuds. Des améliorations ont également été apportées à la gestion des CIDR et de l'anti-affinité de CoreDNS.

### Évolutions fonctionnelles
- **Sécurité des nœuds worker :** Possibilité d'injecter des règles de sécurité supplémentaires (Security Groups) pour les nœuds worker via le chart `capi-cluster`. [#76](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/76)
- **Gestion des secrets :** Suppression des hooks qui empêchaient la modification des secrets, permettant ainsi une meilleure gestion des informations sensibles. [#72](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/72) et [#70](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/70)
- **Provisionnement de secrets :** Amélioration du provisionnement des secrets via l'utilisation de `ResourceSet`. [#71](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/71)

### Évolutions techniques
- **Gestion des CIDR :** Correction d'un problème lié à la gestion des CIDR. [#75](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/75) et [#74](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/74)
- **Gestion des NodePools :** Correction d'un bug empêchant la configuration correcte des NodePools sans contenu spécifique. [#73](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/73)
- **Anti-affinité CoreDNS :** Correction de la configuration de l'anti-affinité pour CoreDNS. [#66](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/66)

### Autres changements
- Ajout de tests pour la gestion des CIDR. [#74](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/74)
- Ajout d'un test pour l'ajout d'un role-id.
- Correction d'un problème de configuration par défaut.
