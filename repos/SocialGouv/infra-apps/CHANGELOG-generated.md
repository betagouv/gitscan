## Changelog : infra-apps (30 derniers jours, au 2026-07-19)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la plateforme Iterion, avec des optimisations de performance, l'ajout de nouvelles fonctionnalités comme l'authentification via GitHub SSO et l'intégration de KEDA pour l'autoscaling. Des améliorations ont également été apportées à l'infrastructure Buildkit, notamment en matière de sécurité et de gestion des accès.

### Évolutions fonctionnelles
- **Iterion :** Ajout de l'authentification via GitHub SSO sur preprod et en production, permettant aux utilisateurs de s'inscrire et de se connecter plus facilement. [#40, #41, #42, #43, #45]
- **Iterion :** Activation du marketplace public en production. [#41]
- **Iterion :** Amélioration de la gestion des secrets avec l'utilisation de Valkey HA pour une meilleure disponibilité et sécurité. [#46]
- **Buildkit :** Ajout d'un fournisseur OIDC Forgejo pour l'authentification. [#48]
- **Buildkit :** Renforcement de la sécurité en production avec l'ajout d'un Ingress TLS et la limitation des accès. [#47]
- **Charon-egapro :** Ajout d'une whitelist pour les hôtes review-alpha et -staging.

### Évolutions techniques
- **Iterion :** Mise à jour du chart Iterion vers les versions 0.37.2, 0.35.0, 0.34.0, 0.33.0, 0.32.0, 0.23.2, 0.23.0, 0.22.0, 0.21.0, 0.17.2, 0.17.1, 0.16.1 et 0.15.0, apportant des corrections de bugs, des améliorations de performance et de nouvelles fonctionnalités.
- **Iterion :** Implémentation de KEDA pour l'autoscaling du runner, améliorant la réactivité et l'efficacité de la plateforme.
- **Iterion :** Optimisation de l'utilisation des ressources (mémoire, CPU) pour les runners et firecrawl.
- **Iterion :** Désactivation du cache de build NFS sur le runner de production pour résoudre des problèmes de blocage.
- **Iterion :** Utilisation de OAuth pour l'accès à Claude Code et ChatGPT, remplaçant les clés API obsolètes.
- **Buildkit :** Mise à jour de l'opérateur Buildkit vers les versions v0.12.0, v0.10.0 et v0.9.0.
- **Buildkit :** Configuration de l'accès S3 pour le cache cold-cache en production.
- **Kata :** Déploiement sur `buildkit-system` et activation de virtiofsd xattr pour améliorer la compatibilité avec Buildkit.

### Autres changements
- Correction de bugs mineurs et améliorations de la configuration pour plusieurs composants.
- Mise à jour de la documentation et du code pour améliorer la lisibilité et la maintenabilité.
- Suppression de clés API obsolètes.
- Ajustements de la configuration pour améliorer la stabilité et la performance.
- Suppression de configurations inutilisées.
