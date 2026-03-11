## Changelog : k8s-cluster-api-helm-charts (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations à la gestion des clusters Kubernetes déployés via Cluster API sur Openstack et Outscale. Les changements incluent une correction pour la configuration de CoreDNS, une modernisation des addons CAPI et la prise en charge du multi-tenant sur Outscale.

### Évolutions fonctionnelles
- **Outscale:** Ajout de la possibilité de référencer un secret pour les déploiements multi-tenant. [#67](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/67)
- **CoreDNS:** Correction d'un problème d'anti-affinité pour CoreDNS, améliorant potentiellement sa stabilité et sa disponibilité. [#66](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/66)
- **Addons CAPI:** Correction d'une erreur de syntaxe YAML dans les addons CAPI, assurant un fonctionnement correct. [#68](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/issues/68)
- **Openstack:** Application de la correction d'anti-affinité CoreDNS également pour Openstack.

### Évolutions techniques
- **Addons CAPI:** Modernisation des addons CAPI pour améliorer la maintenabilité et la lisibilité du code. [#65](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/65)
