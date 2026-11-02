## Changelog : buildkit-operator (30 derniers jours, au 28 octobre 2026)

### Résumé
Les évolutions récentes se concentrent sur la sécurisation et l'automatisation du cycle de déploiement (GitOps) ainsi que sur l'amélioration de la gestion des images via Helm pour garantir des déploiements plus stables et reproductibles.

### Évolutions fonctionnelles
- **Helm Chart** : possibilité d'utiliser des digests immuables pour les références d'images, permettant de garantir l'intégrité et la reproductibilité des versions déployées ([#29](https://github.com/SocialGouv/buildkit-operator/pull/29)).

### Évolutions techniques
- **Déploiement & CI/CD** :
    - Optimisation du workflow GitOps : intégration d'une clé de déploiement en écriture ([#33](https://github.com/SocialGouv/buildkit-operator/pull/33)), limitation de la portée de la commande `GIT_SSH_COMMAND` à l'étape de clonage ([#34](https://github.com/SocialGouv/buildkit-operator/pull/34)) et automatisation de la mise à jour du dépôt GitOps après la validation des builds d'images ([#30](https://github.com/SocialGouv/buildkit-operator/pull/30)).
    - Maintenance de la CI : ajustement de la fréquence des tâches de mise à jour des dépendances (Renovate) pour une détection plus rapide des vulnérabilités ([#28](https://github.com/SocialGouv/buildkit-operator/pull/28)) et une meilleure stabilité des exécutions ([#27](https://github.com/SocialGouv/buildkit-operator/pull/27)).
