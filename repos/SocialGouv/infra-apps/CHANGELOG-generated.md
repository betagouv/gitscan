## Changelog : infra-apps (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce changelog résume les évolutions récentes du projet infra-apps, principalement axées sur l'amélioration et la stabilisation de l'application Iterion, ainsi que sur la mise en place d'une infrastructure plus robuste pour Buildkit. Des améliorations significatives ont été apportées à l'autoscaling, à la sécurité et à la gestion des environnements de production et de pré-production.

### Évolutions fonctionnelles
- **Iterion :**
    - Activation du single sign-on (SSO) via GitHub sur l'environnement de pré-production. [#40](https://github.com/SocialGouv/infra-apps/issues/40)
    - Ouverture de l'inscription sur l'environnement de production avec activation du SSO GitHub pour l'auto-provisionnement. [#43](https://github.com/SocialGouv/infra-apps/issues/43)
    - Ajout d'un accès en lecture seule au marketplace pour les utilisateurs non-soumetteurs. [#45](https://github.com/SocialGouv/infra-apps/issues/45)
    - Implémentation de Valkey HA (Sentinel) pour une gestion d'état distribuée. [#46](https://github.com/SocialGouv/infra-apps/issues/46)
    - Renforcement de la sécurité avec l'ajout d'un accès en niveaux (submitter tier) via GitHub SSO.
- **Buildkit :**
    - Ajout d'un fournisseur OIDC Forgejo pour l'authentification.
    - Activation de la vérification d'identité OIDC sur l'environnement ovh-prod. [#48](https://github.com/SocialGouv/infra-apps/issues/48)
    - Durcissement de l'environnement ovh-prod avec l'ajout d'un Ingress TLS, une épingle stricte et une limitation du nombre de domaines gérés par le gateway. [#47](https://github.com/SocialGouv/infra-apps/issues/47)
    - Mise en place d'une infrastructure GitOps pour ovh-prod.

### Évolutions techniques
- **Iterion :**
    - Amélioration de l'autoscaling avec KEDA, basé sur la profondeur de la queue.
    - Augmentation de la limite de mémoire du runner à 8Gi pour éviter les erreurs OOM.
    - Mise à jour du chart Iterion vers les versions 0.37.4, 0.37.2, 0.35.0, 0.34.0, 0.33.0 et 0.32.0.
    - Activation du cache de construction pour les runners.
    - Correction d'un problème avec l'endpoint NATS de KEDA.
    - Ajout d'un tmpfs writable pour les secrets en-pod.
    - Mise en place d'un override de sandbox pour les runners sans sandbox.
    - Utilisation d'images Devbox pour les runners.
    - Correction de problèmes liés à la gestion des secrets et à l'accès aux fichiers.
- **Buildkit :**
    - Mise à jour de l'opérateur Buildkit vers les versions v0.12.0, v0.10.0 et v0.9.0.
    - Configuration de l'opérateur Buildkit pour utiliser des certificats TLS gérés par cert-manager pour l'environnement ovh-prod.
    - Ajout de credentials S3 sealed pour les builds Buildkit sur ovh-prod.
    - Correction de la capture de la configuration live du gateway.
- **Général :**
    - Correction d'un problème de déploiement de Kata dans le namespace buildkit-system.
    - Activation de virtiofsd xattr pour résoudre les problèmes de hachage de contenu dans les VMs fork.
    - Suspension temporaire de l'application iterion-preprod pendant une période de pointe de production.

### Autres changements
- Correction de l'autorisation du redirect_uri pour l'environnement de pré-production Charon egapro Atlas v2.
- Suppression d'une épingle temporaire d'image E2E.
- Mise à jour de la documentation et de la configuration.
- Nettoyage du code et refactoring.
