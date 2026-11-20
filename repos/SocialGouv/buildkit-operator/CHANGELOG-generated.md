## Changelog : buildkit-operator (30 derniers jours, au 16 novembre 2026)

### Résumé
Les évolutions récentes se concentrent sur le renforcement de la sécurité et l'optimisation des processus de déploiement automatique. Le projet améliore la fiabilité de sa chaîne CI/CD et permet une gestion plus stricte et stable des images utilisées dans l'infrastructure.

### Évolutions fonctionnelles
- **Helm** : les références d'images acceptent désormais l'utilisation de digests immuables, permettant de garantir la stabilité et l'intégrité des déploiements ([#29](https://github.com/SocialGouv/buildkit-operator/pull/29)).

### Évolutions techniques
- **Sécurité** : mise à jour de BuildKit pour corriger une vulnérabilité de sécurité ([#62](https://github.com/SocialGouv/buildkit-operator/pull/62)).
- **Déploiement & CI/CD** :
    - **Automatisation GitOps** : mise à jour automatique du dépôt GitOps après la réussite du build des images ([#30](https://github.com/SocialGouv/buildkit-operator/pull/30)).
    - **Amélioration du workflow de déploiement** : utilisation d'une clé de déploiement en écriture pour le dépôt GitOps ([#33](https://github.com/SocialGouv/buildkit-operator/pull/33)) et limitation de la portée de la commande SSH lors du clonage ([#34](https://github.com/SocialGouv/buildkit-operator/pull/34)).
    - **Optimisation de la gestion des dépendances** : ajustement de la fréquence et de la gestion de la concurrence de l'outil Renovate pour accélérer la détection des vulnérabilités et fiabiliser les cycles de mise à jour ([#27](https://github.com/SocialGouv/buildkit-operator/pull/27), [#28](https://github.com/SocialGouv/buildkit-operator/pull/28), [#36](https://github.com/SocialGouv/buildkit-operator/pull/36), [#54](https://github.com/SocialGouv/buildkit-operator/pull/54)).
