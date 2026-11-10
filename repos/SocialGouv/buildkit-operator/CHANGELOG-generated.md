## Changelog : buildkit-operator (30 derniers jours, au 09 novembre 2026)

### Résumé
Les évolutions de ce mois se sont concentrées sur la sécurisation du moteur de build et l'optimisation de l'automatisation. Les processus de déploiement et de maintenance des dépendances ont été fiabilisés pour permettre une réaction plus rapide aux vulnérabilités de sécurité.

### Évolutions fonctionnelles
- **Helm Chart** : Les références d'images acceptent désormais des empreintes numériques immuables (digests), permettant de garantir la stabilité et l'intégrité des déploiements ([#29](https://github.com/SocialGouv/buildkit-operator/pull/29)).

### Évolutions techniques
- **Sécurité** : Mise à jour de `moby/buildkit` vers la version 0.34.2 pour corriger une vulnérabilité de sécurité (GHSA-w26x-xg27-7qjc) ([#62](https://github.com/SocialGouv/buildkit-operator/pull/62)).
- **Déploiement (GitOps)** : Optimisation du pipeline de déploiement incluant l'utilisation d'une clé de déploiement en écriture pour le clonage et la mise à jour automatique du dépôt GitOps après la validation des images ([#30](https://github.com/SocialGouv/buildkit-operator/pull/30), [#33](https://github.com/SocialGouv/buildkit-operator/pull/33), [#34](https://github.com/SocialGouv/buildkit-operator/pull/34)).
- **CI/CD** : Amélioration de la gestion de l'automatisation des dépendances (Renovate) avec un nouveau calendrier d'exécution (horaire et quotidien) pour accélérer la détection des alertes de sécurité et améliorer la fiabilité des processus ([#27](https://github.com/SocialGouv/buildkit-operator/pull/27), [#28](https://github.com/SocialGouv/buildkit-operator/pull/28), [#36](https://github.com/SocialGouv/buildkit-operator/pull/36), [#54](https://github.com/SocialGouv/buildkit-operator/pull/54)).
