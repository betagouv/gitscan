## Changelog : buildkit-operator (30 derniers jours, au 7 novembre 2026)

### Résumé
Ce mois-ci, l'accent a été mis sur la sécurisation du moteur de build et l'optimisation des processus de déploiement automatique. Les améliorations apportées aux outils d'automatisation permettent une détection plus rapide des vulnérabilités et une gestion plus fiable des mises à jour de l'infrastructure.

### Évolutions fonctionnelles
- Le Helm chart accepte désormais des références d'images via des digests immuables, renforçant la sécurité des déploiements [#29](https://github.com/SocialGouv/buildkit-operator/pull/29).

### Évolutions techniques
- **Sécurité** : Mise à jour de BuildKit vers la version v0.34.2 pour corriger une vulnérabilité critique (GHSA-w26x-xg27-7qjc) [#62](https://github.com/SocialGouv/buildkit-operator/pull/62).
- **CI/CD & Déploiement** :
    - Optimisation du workflow GitOps avec l'utilisation de clés de déploiement en écriture [#33](https://github.com/SocialGouv/buildkit-operator/pull/33) et la mise à jour automatique du dépôt après un build d'image réussi [#30](https://github.com/SocialGouv/buildkit-operator/pull/30).
    - Sécurisation de la commande SSH en limitant sa portée à l'étape de clonage [#34](https://github.com/SocialGouv/buildkit-operator/pull/34).
- **Automatisation (Renovate)** :
    - Amélioration de la réactivité face aux vulnérabilités grâce à une exécution horaire des scans [#28](https://github.com/SocialGouv/buildkit-operator/pull/28) et une gestion optimisée des exécutions quotidiennes [#27](https://github.com/SocialGouv/buildkit-operator/pull/27).
    - Optimisation de la gestion de la concurrence pour éviter les conflits de planification des tâches automatiques [#36](https://github.com/SocialGouv/buildkit-operator/pull/36), [#54](https://github.com/SocialGouv/buildkit-operator/pull/54).
