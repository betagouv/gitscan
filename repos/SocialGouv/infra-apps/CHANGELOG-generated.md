## Changelog : infra-apps (30 derniers jours, au 27 mai 2026)

### Résumé
Ce changelog présente les récentes mises à jour apportées à l'infrastructure d'applications de SocialGouv. Les changements incluent des améliorations de sécurité pour Metabase, des corrections de configuration pour Huginn et Matomo, ainsi qu'une augmentation de la capacité de stockage pour le processus de synchronisation Metabase-Matomo. Des ajustements ont également été effectués pour améliorer la compatibilité et la stabilité des runners Buildkit.

### Évolutions fonctionnelles
- **Metabase :** Autorisation des routes d'intégration publiques via oauth2-proxy, améliorant ainsi la flexibilité d'utilisation de Metabase.
- **Huginn :** Correction de problèmes liés aux nouvelles chaînes (channels) et mise à jour des secrets pour assurer son bon fonctionnement.
- **Charon :** Implémentation de la déconnexion initiée par le RP (Relying Party) via une mise à jour d'image. [#37](https://github.com/SocialGouv/infra-apps/pull/37)
- **Matomo :** Correction de liens RSS brisés dans Huginn pour assurer la bonne réception des données.
- **Metabase-Matomo Sync :** Augmentation de la taille du volume persistant (PVC) de 20Gi à 40Gi pour le processus de synchronisation, afin de gérer un volume de données plus important. [#25ff29b](https://github.com/SocialGouv/infra-apps/commit/25ff29b)

### Évolutions techniques
- **Metabase :** Adoption des CRD Traefik dans le processus GitOps pour une gestion plus automatisée et déclarative de l'infrastructure.
- **Metabase :** Protection de l'environnement de production avec oauth2-proxy (authentification via GitHub SocialGouv) pour renforcer la sécurité.
- **Buildkit Runners :** Exposition du Load Balancer sur le port 443 (en plus du port 1234) pour les runners PIC via un proxy 443, améliorant ainsi l'accessibilité et la sécurité.
- **Metabase-Matomo Sync :** Mise à jour de l'image runtime de node:14-alpine vers node:24-alpine pour bénéficier des dernières corrections de sécurité et améliorations de performance.

### Autres changements
- Préparation de la configuration pour l'exposition du Load Balancer Buildkit.
- Travaux en cours (wip) sur divers aspects de l'infrastructure.
