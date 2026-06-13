## Changelog : infra-apps (30 derniers jours, au 12 juin 2026)

### Résumé
Ce changelog fait état d'une série d'améliorations et de corrections concernant principalement l'application Iterion, avec un focus sur le déploiement sur l'environnement OVH et l'optimisation de son infrastructure. Des ajustements ont également été apportés à Metabase et au buildkit.

### Évolutions fonctionnelles
- **Iterion:** Déploiement d'Iterion Cloud sur l'environnement de développement OVH ([#ab52eae](https://github.com/SocialGouv/infra-apps/commit/ab52eae)).
- **Iterion:** Mise en place d'un environnement haute disponibilité (HA) pour Iterion sur OVH production ([#46721cf](https://github.com/SocialGouv/infra-apps/commit/46721cf)).
- **Iterion:** Utilisation de MongoDB ReplicaSet 3 et MinIO distribué pour le stockage de données sur OVH production ([#4bcda29](https://github.com/SocialGouv/infra-apps/commit/4bcda29)).
- **Metabase/Matomo Sync:** Augmentation de la taille du volume persistant (PVC) de 20Gi à 40Gi pour le job de synchronisation Metabase/Matomo ([#25ff29b](https://github.com/SocialGouv/infra-apps/commit/25ff29b)).

### Évolutions techniques
- **Iterion:** Correction d'un blocage de déploiement (cold-deploy deadlock) lié à un job MinIO sans hook sur OVH production ([#dd6efc2](https://github.com/SocialGouv/infra-apps/commit/dd6efc2)).
- **Iterion:** Configuration du TLS pour OVH production via cert-manager et Let's Encrypt, en utilisant des certificats par sous-domaine au lieu d'un wildcard ([#0055213](https://github.com/SocialGouv/infra-apps/commit/0055213)).
- **Iterion:** Exécution de NATS en tant qu'utilisateur non-root pour répondre aux exigences du cluster Kubernetes ([#3677827](https://github.com/SocialGouv/infra-apps/commit/3677827)).
- **Iterion:** Gestion des clés API Iterion LLM via SealedSecret et suppression de nats-box inutilisé ([#cf6734e](https://github.com/SocialGouv/infra-apps/commit/cf6734e)).
- **Iterion:** Mise à jour de la clé API Anthropic pour Iterion LLM ([#175df91](https://github.com/SocialGouv/infra-apps/commit/175df91)).
- **Iterion:** Suppression des clés globales Iterion LLM, passage à une gestion par organisation ([#2fee85d](https://github.com/SocialGouv/infra-apps/commit/2fee85d)).
- **Buildkit:** Exposition du LoadBalancer sur le port 443 en plus du port 1234 pour les runners PIC via proxy 443 ([#33434e2](https://github.com/SocialGouv/infra-apps/commit/33434e2)).
- **Metabase/Matomo Sync:** Mise à jour de l'image runtime de node:14-alpine vers node:24-alpine ([#8be2e70](https://github.com/SocialGouv/infra-apps/commit/8be2e70)).

### Autres changements
- Nettoyage et préparation de code (WIP) ([#942df86](https://github.com/SocialGouv/infra-apps/commit/942df86)).
