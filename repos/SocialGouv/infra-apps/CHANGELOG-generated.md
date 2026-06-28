## Changelog : infra-apps (30 derniers jours, au 27 juin 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'infrastructure Iterion, notamment avec le déploiement d'une nouvelle instance de production sur OVH, l'ajout de fonctionnalités de sécurité (authentification OIDC), et l'optimisation de la gestion des secrets et des environnements de développement. Des améliorations ont également été apportées à Buildkit Operator pour une meilleure gestion des environnements et des certificats.

### Évolutions fonctionnelles
- **Iterion :**
    - Activation de l'authentification unique (SSO) via GitHub sur les environnements preprod et production, permettant une gestion simplifiée des accès et l'ouverture de l'inscription en mode auto-provisionnement. [#43](https://github.com/SocialGouv/infra-apps/issues/43)
    - Mise en place d'un accès en niveaux pour les utilisateurs GitHub sur Iterion (niveau soumetteur). [#45](https://github.com/SocialGouv/infra-apps/issues/45)
    - Déploiement d'une nouvelle instance de production sur OVH avec une architecture haute disponibilité.
    - Ajout d'un marketplace public sur Iterion. [#41](https://github.com/SocialGouv/infra-apps/issues/41)
- **Buildkit Operator :**
    - Ajout du support du fournisseur OIDC Forgejo (git.devthefuture.org) pour une authentification sécurisée. [#48](https://github.com/SocialGouv/infra-apps/issues/48)
    - Renforcement de la sécurité de l'environnement OVH de production avec l'ajout d'un Ingress TLS, une épinglage strict et une limitation des gateways. [#47](https://github.com/SocialGouv/infra-apps/issues/47)
- **Charon :** Autorisation du `redirect_uri` preprod egapro Atlas v2 (proconnecttest). [#7c6d852](https://github.com/SocialGouv/infra-apps/commit/7c6d852)

### Évolutions techniques
- **Iterion :**
    - Migration des datastores de Bitnami vers Groundhog2k Mongo RS3 et MinIO distribué pour une meilleure performance et fiabilité.
    - Utilisation de SealedSecrets pour la gestion des secrets sensibles, améliorant la sécurité et la conformité.
    - Déploiement de NATS en tant que conteneur non-root pour renforcer la sécurité.
    - Mise en place d'un environnement sandbox Kubernetes pour les runners Iterion, avec gestion des secrets RBAC.
    - Plusieurs déploiements et épinglage de versions pour stabiliser l'environnement de production.
- **Buildkit Operator :**
    - Mise à jour vers la version v0.9.0 pour des corrections et améliorations générales.
    - Configuration du wildcard de gateway pour le domaine bkod.fabrique.
    - Capture de la configuration live du gateway (443, extraDomains, external-dns).

### Autres changements
- Nettoyage et refactoring du code pour améliorer la maintenabilité.
- Mise à jour de la documentation.
- Corrections de bugs mineurs et améliorations de la stabilité.
