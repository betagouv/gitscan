## Changelog : infra-apps (30 derniers jours, au 26 juin 2026)

### Résumé
Ce changelog fait état d'une période d'évolution significative pour l'application Iterion, avec l'ajout de fonctionnalités clés comme l'authentification via GitHub SSO, l'amélioration de la gestion des environnements (preprod, production) et l'optimisation de l'infrastructure sous-jacente (passage à des solutions plus robustes comme MongoDB et MinIO). Des efforts ont également été déployés pour améliorer la sécurité et la gestion des secrets.

### Évolutions fonctionnelles
- Ajout de l'authentification GitHub SSO avec différents niveaux d'accès pour Iterion [#45](https://github.com/SocialGouv/infra-apps/issues/45).
- Activation de l'auto-inscription via GitHub SSO pour Iterion [#43](https://github.com/SocialGouv/infra-apps/issues/43).
- Autorisation du redirect URI pour Charon (egapro Atlas v2) sur l'environnement de préproduction [#7c6d852](https://github.com/SocialGouv/infra-apps/commit/7c6d852).
- Déploiement d'Iterion Cloud sur l'environnement `ovh-dev` [#ab52eae](https://github.com/SocialGouv/infra-apps/commit/ab52eae).

### Évolutions techniques
- Mise en place d'une architecture haute disponibilité (HA) pour Iterion avec Valkey (Sentinel) [#46](https://github.com/SocialGouv/infra-apps/issues/46).
- Refonte de l'infrastructure de production d'Iterion :
    - Remplacement des datastores Bitnami par MongoDB RS3 (groundhog2k) et MinIO distribué [#4bcda29](https://github.com/SocialGouv/infra-apps/commit/4bcda29).
    - Utilisation de certificats TLS via cert-manager letsencrypt-prod pour une meilleure sécurité [#0055213](https://github.com/SocialGouv/infra-apps/commit/0055213).
- Amélioration de la gestion des secrets avec SealedSecret et suppression de nats-box [#cf6734e](https://github.com/SocialGouv/infra-apps/commit/cf6734e).
- Configuration du runner Kubernetes en mode sandbox sur l'environnement de préproduction [#b90db51](https://github.com/SocialGouv/infra-apps/commit/b90db51).
- Correction d'un blocage potentiel lié aux jobs MinIO sur l'environnement de production [#dd6efc2](https://github.com/SocialGouv/infra-apps/commit/dd6efc2).
- Exécution de NATS en tant qu'utilisateur non-root pour renforcer la sécurité [#3677827](https://github.com/SocialGouv/infra-apps/commit/3677827).
- Mise en place de plusieurs versions "pin" d'Iterion sur l'environnement de production pour stabiliser les déploiements [#938f36c](https://github.com/SocialGouv/infra-apps/commit/938f36c), [#e3fc7f3](https://github.com/SocialGouv/infra-apps/commit/e3fc7f3), [#02e524a](https://github.com/SocialGouv/infra-apps/commit/02e524a).
- Déplacement de l'environnement `ovh-dev` vers l'environnement de préproduction [#29c7911](https://github.com/SocialGouv/infra-apps/commit/29c7911).
- Mise à jour du chart Iterion de 0.16.1 vers 0.17.1 et 0.17.2 [#d9f379a](https://github.com/SocialGouv/infra-apps/commit/d9f379a).

### Autres changements
- Correction d'un bug concernant le seed du marketplace Iterion [#a62658b](https://github.com/SocialGouv/infra-apps/commit/a62658b).
- Suppression de clés globales Iterion LLM et passage à une gestion par organisation (BYOK) [#2fee85d](https://github.com/SocialGouv/infra-apps/commit/2fee85d).
- Mise à jour de la clé API Anthropic pour Iterion LLM [#175df91](https://github.com/SocialGouv/infra-apps/commit/175df91).
- Corrections temporaires et reverts liés aux tests E2E et à la configuration des images [#3d1e268](https://github.com/SocialGouv/infra-apps/commit/3d1e268), [#6b91523](https://github.com/SocialGouv/infra-apps/commit/6b91523), [#fb5570d](https://github.com/SocialGouv/infra-apps/commit/fb5570d).
- Travaux en cours (WIP) [#942df86](https://github.com/SocialGouv/infra-apps/commit/942df86).
- Exposition du Load Balancer sur le port 443 pour les runners PIC [#33434e2](https://github.com/SocialGouv/infra-apps/commit/33434e2).
