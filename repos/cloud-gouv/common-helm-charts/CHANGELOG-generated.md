## Changelog : common-helm-charts (30 derniers jours, au 9 avril 2026)

### Résumé
Ce changelog présente les améliorations apportées aux charts Helm communs au cours du dernier mois. Les principales évolutions concernent l'ajout de fonctionnalités pour la personnalisation des chemins d'applications, l'intégration du terminal web ArgoCD, et des corrections pour améliorer la synchronisation et la configuration des charts.

### Évolutions fonctionnelles
- Ajout de la possibilité de spécifier un chemin personnalisé pour les applications via le chart `Copier` [#4](https://github.com/cloud-gouv/common-helm-charts/issues/4).
- Le chart `client-namespace` supporte désormais l'activation du terminal web d'ArgoCD [#5](https://github.com/cloud-gouv/common-helm-charts/issues/5).

### Évolutions techniques
- Correction d'un problème de nom d'application cible dans le chart `Copier`.
- Correction de la racine de la comparaison dans `root-app`.
- Mise à jour des dashboards Argo.
- Correction d'un problème dans `helmfile` concernant les variables d'environnement [#3](https://github.com/cloud-gouv/common-helm-charts/issues/3).
- Synchronisation des changements depuis la branche principale.

### Autres changements
- Aucune information supplémentaire.
