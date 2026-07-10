## Changelog : infra-apps (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de l'infrastructure Iterion, notamment le déploiement d'une nouvelle instance de production sur OVH, l'ajout de fonctionnalités d'autoscaling et l'amélioration de la sécurité et de la gestion des secrets. Des améliorations ont également été apportées à Buildkit Operator, notamment l'ajout de la prise en charge de l'authentification OIDC et l'amélioration de la configuration.

### Évolutions fonctionnelles
- **Iterion:** Ajout de la prise en charge de GitHub SSO sur preprod, permettant aux utilisateurs de s'authentifier via leur compte GitHub. [#40](https://github.com/SocialGouv/infra-apps/issues/40)
- **Iterion:** Activation du mode d'inscription public sur la production, permettant aux utilisateurs de s'auto-provisionner via GitHub SSO. [#43](https://github.com/SocialGouv/infra-apps/issues/43)
- **Iterion:** Ajout d'un marketplace public sur la production. [#41](https://github.com/SocialGouv/infra-apps/issues/41)
- **Iterion:** Implémentation de l'accès à plusieurs niveaux sur le marketplace GitHub SSO (submitter tier). [#45](https://github.com/SocialGouv/infra-apps/issues/45)
- **Buildkit Operator:** Ajout de la prise en charge de l'authentification OIDC pour une sécurité renforcée. [#48](https://github.com/SocialGouv/infra-apps/issues/48)
- **Charon:** Autorisation du redirect_uri pour preprod egapro Atlas v2.

### Évolutions techniques
- **Iterion:** Déploiement d'une nouvelle instance de production sur OVH avec une architecture haute disponibilité.
- **Iterion:** Mise en place d'un autoscaling basé sur KEDA pour le runner, améliorant la réactivité et l'efficacité.
- **Iterion:** Amélioration de la gestion des secrets avec l'utilisation de SealedSecrets et la suppression de clés globales inutilisées.
- **Iterion:** Utilisation de host_state pour les sandboxes Kubernetes, améliorant la stabilité et la sécurité.
- **Buildkit Operator:** Mise à jour vers la version v0.12.0, apportant des corrections et des améliorations de performance.
- **Buildkit Operator:** Ajout d'un provider OIDC Forgejo pour l'authentification.
- **Buildkit Operator:** Configuration du gateway wildcard pour bkod.fabrique.
- **Buildkit Operator:** Capture de la configuration live du gateway.
- **Buildkit Operator:** Renforcement de la sécurité de l'instance OVH avec TLS Ingress et une limitation du nombre de domaines.
- **Iterion:** Migration des datastores de Bitnami vers Groundhog2k Mongo RS3 et MinIO distribué.
- **Kata:** Déploiement dans l'espace de noms buildkit-system au lieu de kube-system.
- **Kata:** Activation de virtiofsd xattr pour résoudre les problèmes de hachage de contenu dans les VMs fork.

### Autres changements
- Mise à jour de la documentation et de la configuration pour refléter les changements apportés.
- Nettoyage du code et suppression des éléments inutilisés.
- Correction de bugs mineurs et améliorations de la stabilité.
- Plusieurs mises à jour de versions (charts Iterion, Buildkit Operator) pour corriger des bugs et améliorer la sécurité.
