## Changelog : common-helm-charts (30 derniers jours, au 06 juillet 2026)

### Résumé
Cette version apporte des améliorations à plusieurs charts, notamment l'ajout d'annotations aux applications, la possibilité d'ajouter des annotations à External Secrets, l'intégration d'un fingerprint d'alerte pour Matrix, un tableau de bord de base pour Coturn et l'ajout d'Auditbeat. Une fonctionnalité de test de stress a également été ajoutée à pgbench.

### Évolutions fonctionnelles
- **Applications:** Ajout d'annotations aux charts d'applications pour une meilleure identification et gestion. [#32](https://github.com/cloud-gouv/common-helm-charts/pull/32)
- **External Secrets:** Permet désormais l'ajout d'annotations aux ressources External Secrets. [#29](https://github.com/cloud-gouv/common-helm-charts/pull/29)
- **Matrix:** Ajout de l'ID et du fingerprint d'alerte dans les templates pour une meilleure traçabilité des alertes. [#28](https://github.com/cloud-gouv/common-helm-charts/pull/28)
- **Coturn:** Intégration d'un tableau de bord basique pour visualiser les métriques de Coturn.
- **pgbench:** Ajout d'une fonctionnalité de test de stress pour évaluer les performances de pgbench. [#22](https://github.com/cloud-gouv/common-helm-charts/pull/22)

### Évolutions techniques
- **Coturn:** Correction de la source de données pour le tableau de bord.
- **Auditbeat:** Intégration du chart Auditbeat pour l'audit des événements Kubernetes. [#26](https://github.com/cloud-gouv/common-helm-charts/pull/26)
- **VM:** Ajout d'un tableau de bord pour afficher toutes les métriques d'une machine virtuelle.
