## Changelog : infra-apps (30 derniers jours, au 29 juin 2026)

### Résumé
Ce changelog résume les évolutions récentes du projet infra-apps, axées principalement sur l'amélioration et le déploiement de l'application Iterion, ainsi que sur la mise en place de l'opérateur Buildkit. Les changements incluent l'ajout de fonctionnalités de sécurité, l'optimisation de l'infrastructure, et la préparation pour des tests et des déploiements en production.

### Évolutions fonctionnelles
- Ajout de l'authentification OIDC sur l'opérateur Buildkit pour l'environnement de production OVH [#48](https://github.com/SocialGouv/infra-apps/issues/48).
- Renforcement de la sécurité de l'opérateur Buildkit en production (TLS Ingress, hard-pin, limitation du gateway) [#47](https://github.com/SocialGouv/infra-apps/issues/47).
- Activation du mode d'inscription ouvert (self-provision) via GitHub SSO pour Iterion en production [#43](https://github.com/SocialGouv/infra-apps/issues/43).
- Activation de la connexion GitHub SSO sur l'environnement de pré-production d'Iterion [#40](https://github.com/SocialGouv/infra-apps/issues/40).
- Ajout d'un accès en tier "submitter" via GitHub SSO pour Iterion [#45](https://github.com/SocialGouv/infra-apps/issues/45).
- Déploiement d'une version de Iterion (v0.21.0) en production avec GitHub SSO et un marketplace public [#41](https://github.com/SocialGouv/infra-apps/issues/41).
- Mise en place d'un marketplace de bots pour Iterion [#42](https://github.com/SocialGouv/infra-apps/issues/42).
- Autorisation du redirect URI pour l'environnement de pré-production d'Egapro Atlas v2 (proconnecttest) pour Charon [#7c6d852](https://github.com/SocialGouv/infra-apps/commit/7c6d852).

### Évolutions techniques
- Mise à jour de l'opérateur Buildkit en production vers la version v0.10.0.
- Ajout d'un fournisseur OIDC Forgejo pour l'opérateur Buildkit (git.devthefuture.org).
- Configuration du wildcard DNS pour l'opérateur Buildkit.
- Amélioration de la capture de la configuration du gateway pour l'opérateur Buildkit.
- Migration des datastores d'Iterion en production vers Groundhog2k Mongo RS3 et MinIO distribué.
- Mise en place d'un environnement haute disponibilité (HA) pour Iterion en production.
- Utilisation de Kubernetes sandbox avec host state et Secrets RBAC pour les runners d'Iterion.
- Déploiement d'Iterion sur un environnement dédié en pré-production.
- Mise en place de Valkey HA (Sentinel) pour Iterion.
- Configuration de NATS en tant que processus non-root pour Iterion.

### Autres changements
- Préparation de l'environnement de production d'Iterion pour des tests E2E.
- Mise à jour et gestion des clés API Anthropic pour Iterion via SealedSecret.
- Suppression de nats-box inutilisé pour Iterion.
- Suppression des clés globales Iterion-LLM au profit d'une gestion BYOK par organisation.
- Suspension temporaire de l'application Iterion en pré-production pendant un spike de performance.
- Diverses corrections et ajustements de versions pour Iterion (v0.15.0, v0.16.0, v0.16.1, v0.17.1, v0.17.2, v0.22.0, v0.23.0, v0.23.2).
