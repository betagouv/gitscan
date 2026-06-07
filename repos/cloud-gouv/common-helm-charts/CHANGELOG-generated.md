## Changelog : common-helm-charts (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les charts Helm ont été améliorés pour offrir une meilleure gestion des secrets, des tableaux de bord Grafana plus robustes et une configuration plus flexible pour certains déploiements. Des améliorations ont également été apportées au chart pgbench pour faciliter l'exécution de benchmarks.

### Évolutions fonctionnelles
- **Grafana :** Refactorisation des tableaux de bord Grafana pour éviter la multiplication des ConfigMaps et améliorer la gestion des données [#25](https://github.com/cloud-gouv/common-helm-charts/issues/25).
- **pgbench :** Amélioration du chart pgbench avec externalisation des scripts de benchmark pour une plus grande flexibilité et maintenabilité [#21](https://github.com/cloud-gouv/common-helm-charts/issues/21).
- **Haproxy :** Ajout d'un nouveau tableau de bord Grafana dédié à Haproxy pour une meilleure supervision et analyse des performances [#20](https://github.com/cloud-gouv/common-helm-charts/issues/20).
- **Secrets :** Correction de la gestion des secrets dans Argo, permettant un provisioning plus fiable et sécurisé [#17](https://github.com/cloud-gouv/common-helm-charts/issues/17) et [#10](https://github.com/cloud-gouv/common-helm-charts/issues/10).

### Évolutions techniques
- Ajout de la possibilité de définir des variables d'environnement supplémentaires pour certains charts.
- Amélioration de la condition RBAC et ajout d'un job pour une meilleure gestion des autorisations et des tâches planifiées.

### Autres changements
- Correction d'une condition pour gérer correctement les objets `$data` vides.
- Limitation à un seul namespace pour certaines configurations.
- Ajout d'un nouveau chart (détails non spécifiés dans les commits).
- Travaux de développement divers [#19](https://github.com/cloud-gouv/common-helm-charts/issues/19).
