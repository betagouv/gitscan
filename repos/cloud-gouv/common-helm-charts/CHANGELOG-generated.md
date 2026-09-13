## Changelog : common-helm-charts (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, le catalogue de charts s'enrichit avec l'ajout de nouveaux composants (itsm-ng et Envoy) et l'amélioration de plusieurs outils existants. Les utilisateurs bénéficieront d'une plus grande flexibilité pour les sauvegardes MinIO, de nouvelles capacités de gestion d'utilisateurs et de tableaux de bord (dashboards) plus précis pour le monitoring.

### Évolutions fonctionnelles
- **Nouveaux composants** : Ajout des charts pour `itsm-ng` [#53](https://github.com/cloud-gouv/common-helm-charts/pull/53) et `envoy` [#48](https://github.com/cloud-gouv/common-helm-charts/pull/48).
- **Améliorations de configuration** :
    - `minio-backup` : les secrets sont désormais optionnels, offrant plus de flexibilité lors du déploiement [#52](https://github.com/cloud-gouv/common-helm-charts/pull/52).
    - `auditbeat` : mise à jour des règles de configuration.
    - Projets d'applications : possibilité d'inclure des utilisateurs additionnels [#45](https://github.com/cloud-gouv/common-helm-charts/pull/45).
- **Visualisation et Monitoring** : Amélioration et corrections des tableaux de bord `coturn` [#51](https://github.com/cloud-gouv/common-helm-charts/pull/51) et `interco` [#49](https://github.com/cloud-gouv/common-helm-charts/pull/49).

### Évolutions techniques
- **CI/CD** : Optimisation du pipeline d'intégration continue pour utiliser le champ "version" lors du processus de tagging [#47](https://github.com/cloud-gouv/common-helm-charts/pull/47).
