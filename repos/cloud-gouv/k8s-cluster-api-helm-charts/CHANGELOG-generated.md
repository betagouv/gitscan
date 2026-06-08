## Changelog : k8s-cluster-api-helm-charts (30 derniers jours, au 2026-06-05)

### Résumé
Ce changelog présente les récentes mises à jour des charts Helm pour Cluster API. Les modifications se concentrent sur la compatibilité avec les nouvelles versions de l'opérateur Cluster API et sur la correction de problèmes liés aux versions d'API, en particulier pour les déploiements sur OpenStack.

### Évolutions fonctionnelles
- Mise à jour des versions d'API pour assurer la compatibilité avec la dernière version de l'opérateur Cluster API.
- Correction de problèmes liés aux versions d'API pour les ressources OpenStack. [#80](https://github.com/cloud-gouv/k8s-cluster-api-helm-charts/pull/80)

### Évolutions techniques
- Modification de la structure de données pour permettre des overrides plus faciles des configurations.
- Rétrogradation vers l'utilisation de `map` pour faciliter les personnalisations.
- Corrections pour la gestion des adresses IP lors des mises à niveau.

### Autres changements
- Amélioration des tests pour valider les corrections apportées.
- Corrections spécifiques à l'environnement OpenStack pour assurer le bon fonctionnement des ressources.
