## Changelog : infra-apps (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce changelog résume les améliorations apportées à l'infrastructure au cours du dernier mois. Les principaux changements concernent l'amélioration de la plateforme Iterion (gestion des runners, sandboxing, authentification) et du Buildkit Operator (gestion des builds, cache, sécurité). Des corrections et optimisations ont également été apportées à d'autres composants comme Metabase, Huginn et Kata.

### Évolutions fonctionnelles
- **Iterion :**
    - Activation de l'authentification via GitHub SSO sur preprod et ouverture des inscriptions en production. [#40](https://github.com/SocialGouv/infra-apps/issues/40) [#41](https://github.com/SocialGouv/infra-apps/issues/41) [#42](https://github.com/SocialGouv/infra-apps/issues/42) [#43](https://github.com/SocialGouv/infra-apps/issues/43) [#45](https://github.com/SocialGouv/infra-apps/issues/45)
    - Ajout d'un marketplace public pour Iterion en production. [#41](https://github.com/SocialGouv/infra-apps/issues/41)
    - Amélioration de la gestion des bots et du marketplace. [#42](https://github.com/SocialGouv/infra-apps/issues/42)
    - Intégration de Valkey HA pour une gestion d'état distribuée. [#46](https://github.com/SocialGouv/infra-apps/issues/46)
- **Buildkit Operator :**
    - Ajout d'un provider OIDC Forgejo pour l'authentification. [#47](https://github.com/SocialGouv/infra-apps/issues/47) [#48](https://github.com/SocialGouv/infra-apps/issues/48)
    - Mise en place d'une infrastructure GitOps pour ovh-prod.
- **Token Bureau :**
    - Configuration du serveur pour pointer vers la configuration des permissions montées.

### Évolutions techniques
- **Iterion :**
    - Amélioration de la gestion du sandbox pour les runners, incluant l'activation du sandbox K8s sur preprod et la configuration de l'utilisation automatique du sandbox.
    - Mise à jour de la version du chart Iterion (0.16.1 -> 0.17.1 -> 0.17.2 -> 0.21.0 -> 0.22.0 -> 0.23.0 -> 0.23.2).
    - Intégration de l'authentification OAuth pour Claude Code.
    - Ajout de KEDA pour l'autoscaling du runner en fonction de la profondeur de la queue.
    - Utilisation de l'API OAuth pour ChatGPT.
- **Buildkit Operator :**
    - Mises à jour de version (v0.9.0, v0.10.0, v0.12.0, v0.13.0, v0.14.2, v0.15.0).
    - Amélioration de la gestion du cache S3 (cadence, lifecycle, project defaults).
    - Amélioration de la configuration du gateway (wildcard, TLS, hard-pin).
    - Configuration du cache S3 pour ovh-prod.
- **Autres :**
    - Correction d'un problème de mount NFS sur Iterion (ovh-prod).
    - Augmentation des ressources allouées à Metabase après une panne.
    - Correction d'un problème de virtiofsd xattr sur Kata.
    - Correction d'un problème de KEDA NATS endpoint.
    - Autorisation de resync sur les namespaces adoptés par Rancher.

### Autres changements
- Mise à jour de la documentation et de la configuration.
- Nettoyage du code et suppression de configurations obsolètes.
- Ajustements de la configuration pour les environnements de test (E2E).
- Suppression d'une clé API Anthropic obsolète.
- Correction de l'ordre de tri des événements RSS dans Huginn.
- Suppression de la configuration de concurrence du runner Iterion (ovh-prod).
- Correction de l'OOMKilled sur le web-scrape de Firecrawl.
- Déplacement de SearXNG SealedSecret dans les templates.
- Ajout d'un backend de recherche web souverain SearXNG.
- Configuration de TZ=Europe/Paris via config.extraEnv pour Iterion.
- Augmentation de la limite de mémoire du runner Iterion.
- Mise à jour du chart Iterion (0.33.0, 0.34.0, 0.35.0, 0.37.2).
- Whitelisting des hôtes review-alpha/-staging pour Charon-Egapro.
