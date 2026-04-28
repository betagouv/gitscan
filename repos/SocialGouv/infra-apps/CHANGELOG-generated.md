## Changelog : infra-apps (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'observabilité et de l'accès aux données avec le déploiement d'Elasticsearch, ainsi que sur l'intégration de nouveaux outils comme Kuik et Huginn. Plusieurs corrections et ajustements ont été apportés pour stabiliser ces déploiements et améliorer leur configuration.

### Évolutions fonctionnelles
- **Elasticsearch:** Elasticsearch est maintenant exposé via Ingress, permettant un accès plus facile et une meilleure intégration avec d'autres services [#issue](https://github.com/SocialGouv/infra-apps/issues/). Il a été déployé sur l'environnement `ovh-dev` avec Kibana et une authentification par `fileRealm`.
- **Kuik:** Kuik a été déployé sur les environnements `ovh-prod` et `tools`, avec une désactivation initiale des webhooks via un sélecteur d'opt-in. Il est également en cours de test sur `ovh-dev` avant déploiement en production.
- **Huginn:** Huginn a été déployé en production et sur l'environnement `tools`. Des configurations de scénarios et des intégrations avec Mattermost et SMTP ont été ajoutées.
- **Openebs-nfs:** Openebs-nfs a été déployé sur l'environnement `tools`.

### Évolutions techniques
- **Kuik:**
    - Suppression du registre en cluster et routage de `docker.io` via le proxy cache Harbor pour optimiser les performances et la sécurité.
    - Ajout du champ `path` requis pour les images Docker provenant de `docker.io`.
- **Huginn:**
    - Ajout d'un chart Helm et d'un `applicationset` pour le déploiement sur l'environnement `ovh-dev`.
- **Infrastructure:**
    - Correction d'un problème d'accessibilité à Elasticsearch depuis `ingress-nginx` (correction du code 504).
- **Documentation:**
    - Ajout d'un document `CLAUDE.md` décrivant les modèles IaC (Infrastructure as Code) utilisés dans `infra-apps`.
    - Documentation des limitations de la branche "Always" sur les Kubernetes managés pour Kuik.
    - Documentation de l'intégration de Huginn.

### Autres changements
- Correction d'un problème lié à l'ignorance d'un secret autogénéré pour Kuik.
- Diverses corrections et ajustements de configuration pour Huginn durant sa phase de développement et de déploiement.
