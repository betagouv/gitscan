## Changelog : infra-apps (30 derniers jours, au 22 juin 2026)

### Résumé
Ce changelog présente les évolutions récentes apportées à l'infrastructure d'applications. Les modifications majeures concernent le déploiement et la configuration de l'application Iterion, avec une migration vers une infrastructure plus robuste et sécurisée. Des améliorations ont également été apportées à l'intégration de Metabase et à la gestion des secrets.

### Évolutions fonctionnelles
- Autorisation du `redirect_uri` preprod pour Charon et egapro Atlas v2 (proconnecttest) [#7c6d852](https://github.com/SocialGouv/infra-apps/commit/7c6d852)
- Exposition du LoadBalancer Buildkit sur le port 443 pour les runners PIC via proxy, améliorant l'accessibilité et la sécurité. [#33434e2](https://github.com/SocialGouv/infra-apps/commit/33434e2)

### Évolutions techniques
- **Iterion :**
    - Déploiement d'Iterion Cloud sur l'environnement `ovh-dev`. [#ab52eae](https://github.com/SocialGouv/infra-apps/commit/ab52eae)
    - Migration de l'environnement `ovh-prod` vers une infrastructure haute disponibilité (HA) avec des datastores Groundhog2k Mongo RS3 et MinIO distribué. [#46721cf](https://github.com/SocialGouv/infra-apps/commit/46721cf) et [#4bcda29](https://github.com/SocialGouv/infra-apps/commit/4bcda29)
    - Correction d'un problème de blocage de déploiement avec le job MinIO bucket pour `ovh-prod`. [#dd6efc2](https://github.com/SocialGouv/infra-apps/commit/dd6efc2)
    - Configuration du TLS pour `ovh-prod` via cert-manager et Let's Encrypt. [#0055213](https://github.com/SocialGouv/infra-apps/commit/0055213)
    - Epinglement de la version d'Iterion `ovh-prod` à v0.15.0, v0.16.0 et v0.16.1 pour assurer la stabilité. [#29c7911](https://github.com/SocialGouv/infra-apps/commit/29c7911), [#02e524a](https://github.com/SocialGouv/infra-apps/commit/02e524a) et [#938f36c](https://github.com/SocialGouv/infra-apps/commit/938f36c)
    - Gestion des clés Iterion LLM via SealedSecret et suppression de nats-box inutilisé. [#cf6734e](https://github.com/SocialGouv/infra-apps/commit/cf6734e)
    - Mise à jour de la clé API Anthropic pour Iterion LLM. [#175df91](https://github.com/SocialGouv/infra-apps/commit/175df91)
    - Exécution de NATS en tant qu'utilisateur non-root pour la sécurité. [#3677827](https://github.com/SocialGouv/infra-apps/commit/3677827)
- **Metabase/Matomo:**
    - Augmentation de la taille du PVC de `metabase-matomo-sync` de 20Gi à 40Gi. [#25ff29b](https://github.com/SocialGouv/infra-apps/commit/25ff29b)
    - Mise à jour de l'image runtime de `metabase-matomo-sync` de node:14-alpine à node:24-alpine. [#8be2e70](https://github.com/SocialGouv/infra-apps/commit/8be2e70)

### Autres changements
- Suppression des clés globales Iterion LLM, passage à une gestion par organisation. [#2fee85d](https://github.com/SocialGouv/infra-apps/commit/2fee85d)
- Travaux en cours (WIP) [#942df86](https://github.com/SocialGouv/infra-apps/commit/942df86)
