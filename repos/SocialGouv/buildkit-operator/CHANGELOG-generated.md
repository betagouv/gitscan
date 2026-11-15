## Changelog : buildkit-operator (30 derniers jours, au 14/11/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité et l'optimisation des processus de déploiement. Une mise à jour critique de BuildKit a été appliquée pour corriger une vulnérabilité, tandis que les pipelines de déploiement (CI/CD) et la gestion des dépendances ont été affinés pour gagner en fiabilité et en rapidité de réaction face aux alertes de sécurité.

### Évolutions fonctionnelles
- **Helm Chart** : Les références d'images acceptent désormais l'utilisation de digests immuables, permettant des déploiements plus stables et sécurisés ([#29](https://github.com/SocialGouv/buildkit-operator/pull/29)).

### Évolutions techniques
- **Sécurité** : Mise à jour de BuildKit vers la version 0.34.2 pour corriger une vulnérabilité (GHSA-w26x-xg27-7qjc) ([#62](https://github.com/SocialGouv/buildkit-operator/pull/62)).
- **Déploiement & CI/CD** :
    - Optimisation du flux GitOps : intégration de clés de déploiement en écriture pour le clonage du dépôt ([#33](https://github.com/SocialGouv/buildkit-operator/pull/33)) et mise à jour automatique du dépôt GitOps après la validation des images ([#30](https://github.com/SocialGouv/buildkit-operator/pull/30)).
    - Amélioration de la gestion des dépendances (Renovate) : ajustement de la fréquence d'exécution pour détecter les vulnérabilités plus rapidement et optimisation de la gestion de la concurrence pour éviter les conflits de tâches planifiées ([#27](https://github.com/SocialGouv/buildkit-operator/pull/27), [#28](https://github.com/SocialGouv/buildkit-operator/pull/28), [#36](https://github.com/SocialGouv/buildkit-operator/pull/36), [#54](https://github.com/SocialGouv/buildkit-operator/pull/54)).
    - Sécurisation de la commande SSH lors de l'étape de clonage dans les pipelines de déploiement ([#34](https://github.com/SocialGouv/buildkit-operator/pull/34)).
